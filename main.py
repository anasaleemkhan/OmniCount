"""
OmniCount Pro - Enterprise Computer Vision CLI Engine.
Detects objects and people, performs spatial crowd proximity analysis,
generates Gaussian density heatmaps, and provides semantic English definitions.
"""

import argparse
import json
import os
import sys
from detector import OmniDetector
from gemini_vision_audit import generate_vision_audit_report


def main():
    parser = argparse.ArgumentParser(
        description="OmniCount Pro - Spatial Computer Vision & Crowd Telemetry Engine"
    )
    parser.add_argument(
        "--image", "-i",
        type=str,
        default=None,
        help="Path to input image (JPG, PNG)"
    )
    parser.add_argument(
        "--model", "-m",
        type=str,
        default="yolov8n.pt",
        help="YOLO model weight (default: yolov8n.pt)"
    )
    parser.add_argument(
        "--conf", "-c",
        type=float,
        default=0.35,
        help="Detection confidence threshold (default: 0.35)"
    )
    parser.add_argument(
        "--proximity", "-p",
        type=float,
        default=90.0,
        help="Proximity distance threshold in pixels (default: 90.0)"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="output_detected.jpg",
        help="Output path for annotated image"
    )
    parser.add_argument(
        "--heatmap",
        type=str,
        default="output_heatmap.jpg",
        help="Output path for Gaussian density heatmap"
    )
    parser.add_argument(
        "--ai",
        action="store_true",
        help="Generate Google Gemini forensic intelligence audit"
    )
    parser.add_argument(
        "--lang",
        type=str,
        choices=["en", "it"],
        default="en",
        help="Language for AI audit report ('en' or 'it')"
    )

    args = parser.parse_args()

    image_path = args.image
    if not image_path:
        # Search for any jpg or png in current folder
        imgs = [f for f in os.listdir(".") if f.lower().endswith((".jpg", ".jpeg", ".png"))]
        if imgs:
            image_path = imgs[0]
            print(f"[i] Using discovered image: {image_path}")
        else:
            # Create synthetic canvas
            import numpy as np
            import cv2
            canvas = np.full((600, 800, 3), 235, dtype=np.uint8)
            cv2.putText(canvas, "OmniCount Pro Test Scene", (150, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (40, 40, 40), 2)
            image_path = "sample_test.jpg"
            cv2.imwrite(image_path, canvas)
            print(f"[i] Generated sample image: {image_path}")

    print(f"\n[+] Initializing OmniDetector ({args.model})...")
    detector = OmniDetector(model_weights=args.model)

    print(f"[+] Processing scene: {image_path} (Confidence: {args.conf}, Proximity: {args.proximity}px)...")
    res = detector.run_detection(
        image_input=image_path,
        confidence_threshold=args.conf,
        proximity_distance_px=args.proximity
    )

    telemetry = res["telemetry"]
    crowd = telemetry["crowd_metrics"]

    # Save output images
    import cv2
    cv2.imwrite(args.output, res["annotated_image"])
    cv2.imwrite(args.heatmap, res["heatmap_image"])

    # Display Terminal Telemetry
    print("\n" + "=" * 78)
    print("           👁️ OMNICOUNT PRO - SPATIAL VISION & TELEMETRY REPORT           ")
    print("=" * 78)
    print(f"Total Objects Detected    : {telemetry['total_objects']}")
    print(f"Total People Count        : {telemetry['people_count']}")
    print(f"Crowd Congestion Index    : {crowd['congestion_index']}% ({crowd['risk_level']})")
    print(f"Clustered People Pairs    : {crowd['close_pairs_count']} of {crowd['total_possible_pairs']} pairs")
    print("-" * 78)

    print(f"{'No.':<4} {'Object':<16} {'Category':<14} {'Count':<7} {'Definition & Functional Purpose'}")
    print("-" * 78)

    idx = 1
    for obj_name, count in telemetry["item_frequencies"].items():
        from coco_definitions import get_object_info
        info = get_object_info(obj_name)
        print(f"{idx:<4} {info['name']:<16} {info['category']:<14} {count:<7} Def: {info['definition']}")
        print(f"{'':<43} Purpose: {info['purpose']}")
        print("-" * 78)
        idx += 1

    print(f"\n[✓] Annotated visual saved to : {args.output}")
    print(f"[✓] Spatial heatmap saved to  : {args.heatmap}")

    # Export forensic JSON
    json_path = "telemetry_report.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(telemetry, f, indent=2)
    print(f"[✓] Raw telemetry saved to   : {json_path}")

    # AI Audit Generation if requested
    if args.ai:
        print(f"\n[+] Requesting Google Gemini Spatial Forensic Audit ({args.lang.upper()})...\n")
        audit = generate_vision_audit_report(telemetry, language=args.lang)
        print(audit)
        print("=" * 78)


if __name__ == "__main__":
    main()
