"""
Spatial Telemetry & Proximity Analysis Engine for Computer Vision.
Computes 2D Euclidean distance matrices, crowd congestion indices (CCI),
clustering graphs, object scale distributions, and Gaussian density heatmaps.
"""

import math
import numpy as np
import cv2
from typing import List, Dict, Tuple


def calculate_centroids(boxes: List[List[float]]) -> List[Tuple[float, float]]:
    """Calculates center points (xc, yc) for a list of bounding boxes [x1, y1, x2, y2]."""
    centroids = []
    for box in boxes:
        x1, y1, x2, y2 = box[:4]
        xc = (x1 + x2) / 2.0
        yc = (y1 + y2) / 2.0
        centroids.append((xc, yc))
    return centroids


def analyze_crowd_proximity(
    people_boxes: List[List[float]],
    distance_threshold_px: float = 90.0
) -> Dict:
    """
    Computes pairwise Euclidean distances between detected individuals.
    Identifies clustered pairs and calculates a normalized Crowd Congestion Index (CCI).
    """
    n = len(people_boxes)
    if n < 2:
        return {
            "total_people": n,
            "close_pairs_count": 0,
            "total_possible_pairs": 0,
            "congestion_index": 0.0,
            "clustered_indices": [],
            "close_pairs": [],
            "risk_level": "Minimal" if n == 1 else "Empty"
        }

    centroids = calculate_centroids(people_boxes)
    close_pairs = []
    clustered_indices = set()
    total_pairs = (n * (n - 1)) // 2

    for i in range(n):
        for j in range(i + 1, n):
            c1, c2 = centroids[i], centroids[j]
            dist = math.dist(c1, c2)
            if dist < distance_threshold_px:
                close_pairs.append({
                    "person_a": i,
                    "person_b": j,
                    "distance_px": round(dist, 1),
                    "coord_a": (int(c1[0]), int(c1[1])),
                    "coord_b": (int(c2[0]), int(c2[1]))
                })
                clustered_indices.add(i)
                clustered_indices.add(j)

    congestion_pct = round((len(close_pairs) / max(1, total_pairs)) * 100, 1)

    if congestion_pct > 50.0:
        risk_level = "Severe Congestion"
    elif congestion_pct > 25.0:
        risk_level = "High Density"
    elif congestion_pct > 10.0:
        risk_level = "Moderate Density"
    else:
        risk_level = "Low Density"

    return {
        "total_people": n,
        "close_pairs_count": len(close_pairs),
        "total_possible_pairs": total_pairs,
        "congestion_index": congestion_pct,
        "clustered_indices": list(clustered_indices),
        "close_pairs": close_pairs,
        "risk_level": risk_level
    }


def generate_gaussian_density_heatmap(
    image: np.ndarray,
    centroids: List[Tuple[float, float]],
    kernel_radius: int = 45
) -> np.ndarray:
    """
    Constructs a 2D spatial Gaussian density accumulator map
    and blends it with the original frame via a JET color gradient.
    """
    h, w = image.shape[:2]
    density_map = np.zeros((h, w), dtype=np.float32)

    for (xc, yc) in centroids:
        x, y = int(xc), int(yc)
        if 0 <= x < w and 0 <= y < h:
            # Draw smooth Gaussian kernel accumulation
            cv2.circle(density_map, (x, y), kernel_radius, 1.0, -1)

    # Apply Gaussian blur for smooth gradient transition
    density_map = cv2.GaussianBlur(density_map, (kernel_radius * 2 + 1, kernel_radius * 2 + 1), 0)

    # Normalize to 0-255
    if density_map.max() > 0:
        norm_map = (density_map / density_map.max() * 255).astype(np.uint8)
    else:
        norm_map = np.zeros((h, w), dtype=np.uint8)

    # Apply Jet color map
    color_heatmap = cv2.applyColorMap(norm_map, cv2.COLORMAP_JET)

    # Alpha blend overlay with source image
    alpha = 0.55
    blended = cv2.addWeighted(image, 1.0 - alpha, color_heatmap, alpha, 0)
    return blended


def categorize_object_scales(boxes: List[List[float]], image_shape: Tuple[int, int]) -> Dict[str, int]:
    """Classifies bounding boxes into Small, Medium, and Large based on relative visual footprint."""
    h, w = image_shape[:2]
    img_area = float(h * w)
    scales = {"Small (<2%)": 0, "Medium (2-15%)": 0, "Large (>15%)": 0}

    for box in boxes:
        x1, y1, x2, y2 = box[:4]
        box_area = max(0, x2 - x1) * max(0, y2 - y1)
        ratio = (box_area / img_area) * 100.0 if img_area > 0 else 0

        if ratio < 2.0:
            scales["Small (<2%)"] += 1
        elif ratio <= 15.0:
            scales["Medium (2-15%)"] += 1
        else:
            scales["Large (>15%)"] += 1

    return scales
