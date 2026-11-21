"""
OmniCount Pro - Core Computer Vision & Object Localization Engine.
Executes YOLOv8 deep inference, spatial geometry parsing, and multi-layer visual rendering.
"""

import os
from collections import Counter
from typing import Dict, List, Optional, Tuple
import cv2
import numpy as np

try:
    from ultralytics import YOLO
    ULTRALYTICS_AVAILABLE = True
except ImportError:
    ULTRALYTICS_AVAILABLE = False

from coco_definitions import get_object_info
from spatial_analyzer import (
    analyze_crowd_proximity,
    categorize_object_scales,
    generate_gaussian_density_heatmap,
    calculate_centroids
)


class OmniDetector:
    def __init__(self, model_weights: str = "yolov8n.pt"):
        self.model_weights = model_weights
        self.model = None
        if ULTRALYTICS_AVAILABLE:
            try:
                self.model = YOLO(model_weights)
            except Exception as e:
                print(f"[!] Warning loading YOLO model: {e}")

    def run_detection(
        self,
        image_input,
        confidence_threshold: float = 0.35,
        proximity_distance_px: float = 90.0,
        draw_proximity_lines: bool = True
    ) -> Dict:
        """
        Runs full computer vision detection, crowd proximity analysis,
        and spatial heatmap generation on an image array or file path.
        """
        # Load image array
        if isinstance(image_input, str):
            image = cv2.imread(image_input)
            if image is None:
                raise FileNotFoundError(f"Could not load image from: {image_input}")
        elif isinstance(image_input, np.ndarray):
            image = image_input.copy()
        else:
            raise ValueError("image_input must be a file path string or numpy ndarray")

        h, w = image.shape[:2]
        detections = []
        people_boxes = []

        if self.model is not None:
            results = self.model.predict(source=image, conf=confidence_threshold, verbose=False)
            boxes_obj = results[0].boxes

            if boxes_obj is not None and len(boxes_obj) > 0:
                for b in boxes_obj:
                    coords = [float(x) for x in b.xyxy[0]]
                    cls_id = int(b.cls[0])
                    conf = float(b.conf[0])
                    cls_name = self.model.names[cls_id]
                    info = get_object_info(cls_name)

                    item = {
                        "class_name": cls_name,
                        "category": info["category"],
                        "confidence": round(conf, 3),
                        "box": [round(c, 1) for c in coords],
                        "definition": info["definition"],
                        "purpose": info["purpose"]
                    }
                    detections.append(item)

                    if cls_name == "person":
                        people_boxes.append(coords)
        else:
            # Fallback mock for demo if ultralytics is not yet compiled
            pass

        # 1. Proximity & Crowd Dynamics
        crowd_metrics = analyze_crowd_proximity(people_boxes, distance_threshold_px=proximity_distance_px)

        # 2. Scale Distribution
        all_boxes = [d["box"] for d in detections]
        scale_metrics = categorize_object_scales(all_boxes, (h, w))

        # 3. Object Counts & Category Breakdown
        detected_names = [d["class_name"] for d in detections]
        category_counts = Counter([d["category"] for d in detections])
        item_counts = Counter(detected_names)

        # 4. Render Visual Annotations
        annotated_img = image.copy()
        clustered_set = set(crowd_metrics.get("clustered_indices", []))

        # Draw bounding boxes
        for idx, d in enumerate(detections):
            x1, y1, x2, y2 = [int(v) for v in d["box"]]
            is_person = (d["class_name"] == "person")
            
            # Color code: Red for clustered people, Green for distanced people, Blue for other objects
            if is_person:
                # Find person index
                p_idx = [i for i, pb in enumerate(people_boxes) if pb == d["box"]]
                if p_idx and p_idx[0] in clustered_set:
                    color = (0, 0, 255) # Red (Clustered)
                    label = f"Person [Clustered] {d['confidence']:.2f}"
                else:
                    color = (0, 200, 0) # Green (Distanced)
                    label = f"Person {d['confidence']:.2f}"
            else:
                color = (255, 120, 0) # Blue-ish for objects
                label = f"{d['class_name']} {d['confidence']:.2f}"

            cv2.rectangle(annotated_img, (x1, y1), (x2, y2), color, 2)
            cv2.putText(
                annotated_img, label, (x1, max(20, y1 - 8)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2, cv2.LINE_AA
            )

        # Draw proximity connection lines between people in close proximity
        if draw_proximity_lines:
            for pair in crowd_metrics.get("close_pairs", []):
                pt1 = pair["coord_a"]
                pt2 = pair["coord_b"]
                cv2.line(annotated_img, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)
                # Draw distance text in center of line
                mid_x = (pt1[0] + pt2[0]) // 2
                mid_y = (pt1[1] + pt2[1]) // 2
                cv2.circle(annotated_img, (mid_x, mid_y), 3, (0, 0, 255), -1)

        # Telemetry HUD on Top of Frame
        hud_text = f"Objects: {len(detections)} | People: {len(people_boxes)} | Congestion Index: {crowd_metrics['congestion_index']}% ({crowd_metrics['risk_level']})"
        cv2.rectangle(annotated_img, (0, 0), (w, 42), (20, 20, 20), -1)
        cv2.putText(
            annotated_img, hud_text, (15, 28),
            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 255), 2, cv2.LINE_AA
        )

        # 5. Render Density Heatmap
        people_centroids = calculate_centroids(people_boxes)
        heatmap_img = generate_gaussian_density_heatmap(image, people_centroids)

        # Package telemetry
        telemetry = {
            "total_objects": len(detections),
            "people_count": len(people_boxes),
            "unique_classes_count": len(item_counts),
            "crowd_metrics": crowd_metrics,
            "scale_distribution": scale_metrics,
            "category_distribution": dict(category_counts),
            "item_frequencies": dict(item_counts),
            "detailed_detections": detections
        }

        return {
            "telemetry": telemetry,
            "annotated_image": annotated_img,
            "heatmap_image": heatmap_img,
            "original_image": image
        }
