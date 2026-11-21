"""
OmniCount Pro - Enterprise Computer Vision & Spatial Intelligence Dashboard.
Powered by YOLOv8, Euclidean Distance Geometry, Gaussian Heatmaps, and Google Gemini AI.
"""

import os
import cv2
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

from detector import OmniDetector
from gemini_vision_audit import generate_vision_audit_report, get_api_key

# Page Configuration
st.set_page_config(
    page_title="OmniCount Pro | Spatial Vision & Crowd Intelligence",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 0.1rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.2rem;
    }
    .metric-card {
        background: #F8FAFC;
        border-radius: 10px;
        border-left: 5px solid #2563EB;
        padding: 1rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">👁️ OmniCount Pro — Spatial Crowd & Object Intelligence</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Advanced Computer Vision Telemetry: Real-time Crowd Density, Pairwise Proximity Graphs, and AI Forensic Auditing.</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Controls
# ---------------------------------------------------------
st.sidebar.title("⚙️ Detection Parameters")

conf_threshold = st.sidebar.slider(
    "Detection Confidence Threshold",
    min_value=0.10,
    max_value=0.90,
    value=0.35,
    step=0.05,
    help="Higher values suppress uncertain predictions."
)

proximity_threshold = st.sidebar.slider(
    "Social Proximity Threshold (px)",
    min_value=40,
    max_value=250,
    value=100,
    step=10,
    help="Distance threshold below which individuals are classified as clustered."
)

draw_lines = st.sidebar.checkbox("Draw Proximity Vector Lines", value=True)

st.sidebar.markdown("---")
st.sidebar.subheader("🤖 Google Gemini Intelligence")
saved_key = get_api_key()
api_key_input = st.sidebar.text_input(
    "Gemini API Key",
    value=saved_key or "",
    type="password",
    help="Loads automatically from .env or enter here."
)

gemini_model = st.sidebar.selectbox(
    "Gemini Model",
    ["gemini-2.5-flash", "gemini-4-hydrogen", "gemini-1.5-flash"],
    index=0
)

audit_lang = st.sidebar.selectbox(
    "Audit Language / Lingua del Rapporto",
    ["English", "Italiano"],
    index=0
)
lang_code = "it" if audit_lang == "Italiano" else "en"

# ---------------------------------------------------------
# Image Input Source
# ---------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("📷 Image Source")
source_option = st.sidebar.radio(
    "Select Input",
    ["📂 Upload Custom Image", "🖼️ Generate Synthetic Test Scene"]
)

input_image = None
if source_option == "📂 Upload Custom Image":
    uploaded_file = st.sidebar.file_uploader("Upload Image (JPG, PNG)", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        pil_img = Image.open(uploaded_file).convert("RGB")
        input_image = np.array(pil_img)[:, :, ::-1].copy() # Convert RGB to BGR for OpenCV
else:
    # Synthetic multi-person scene generator
    canvas = np.full((600, 800, 3), 235, dtype=np.uint8)
    # Draw demo objects (cars, people boxes)
    cv2.rectangle(canvas, (100, 200), (220, 480), (180, 100, 50), -1)
    cv2.putText(canvas, "Vehicle Placeholder", (105, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    # People silhouettes
    for x in [300, 360, 550, 680]:
        cv2.circle(canvas, (x, 260), 22, (50, 120, 200), -1)
        cv2.rectangle(canvas, (x - 20, 285), (x + 20, 420), (50, 120, 200), -1)
    cv2.putText(canvas, "Synthetic Surveillance Scene", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (40, 40, 40), 2)
    input_image = canvas

if input_image is None:
    st.info("Please upload an image to begin computer vision spatial analysis.")
    st.stop()

# ---------------------------------------------------------
# Run Computer Vision Engine
# ---------------------------------------------------------
@st.cache_resource
def load_detector():
    return OmniDetector(model_weights="yolov8n.pt")

detector = load_detector()
results = detector.run_detection(
    image_input=input_image,
    confidence_threshold=conf_threshold,
    proximity_distance_px=proximity_threshold,
    draw_proximity_lines=draw_lines
)

telemetry = results["telemetry"]
annotated_bgr = results["annotated_image"]
heatmap_bgr = results["heatmap_image"]
crowd = telemetry["crowd_metrics"]

# Convert BGR to RGB for Streamlit Display
annotated_rgb = cv2.cvtColor(annotated_bgr, cv2.COLOR_BGR2RGB)
heatmap_rgb = cv2.cvtColor(heatmap_bgr, cv2.COLOR_BGR2RGB)
original_rgb = cv2.cvtColor(results["original_image"], cv2.COLOR_BGR2RGB)

# ---------------------------------------------------------
# Top Metrics Bar
# ---------------------------------------------------------
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Total Objects Detected", f"{telemetry['total_objects']}")
m2.metric("Total People Count", f"{telemetry['people_count']}")
m3.metric("Crowd Congestion Index (CCI)", f"{crowd['congestion_index']}%")
m4.metric("Proximity Risk Level", f"{crowd['risk_level']}")
m5.metric("Clustered Pairs", f"{crowd['close_pairs_count']}")

st.markdown("---")

# ---------------------------------------------------------
# Multi-Tab Analysis
# ---------------------------------------------------------
tab_viz, tab_heat, tab_charts, tab_gemini, tab_ontology = st.tabs([
    "📸 Visual Detections & Proximity Graph",
    "🌡️ Spatial Crowd Density Heatmap",
    "📊 Telemetry Analytics & Distributions",
    "🤖 Gemini AI Surveillance Audit",
    "📖 Semantic Object Knowledge Base"
])

# TAB 1: Visual Detections
with tab_viz:
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.subheader("Original Input Scene")
        st.image(original_rgb, use_container_width=True)
    with col_v2:
        st.subheader("Annotated Geometry & Proximity Vectors")
        st.caption("🔴 Red Lines: Pairwise Euclidean distance violation (< threshold). 🟢 Green: Distanced.")
        st.image(annotated_rgb, use_container_width=True)

# TAB 2: Spatial Density Heatmap
with tab_heat:
    st.subheader("🌡️ 2D Gaussian Kernel Crowd Density Heatmap")
    st.markdown("""
    This thermal gradient visualizes spatial pedestrian concentrations. Hotter colors (red/yellow) indicate
    dense crowd clusters, calculated by accumulating 2D Gaussian distributions centered on detected human centroids.
    """)
    st.image(heatmap_rgb, use_container_width=True)

# TAB 3: Telemetry Charts
with tab_charts:
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.subheader("📊 Category Taxonomy Distribution")
        cat_data = telemetry["category_distribution"]
        if cat_data:
            df_cat = pd.DataFrame(list(cat_data.items()), columns=["Category", "Count"])
            fig_cat = px.bar(
                df_cat, x="Category", y="Count", color="Category",
                title="Detections by Macro Category"
            )
            st.plotly_chart(fig_cat, use_container_width=True)
        else:
            st.write("No objects detected to display.")

    with col_c2:
        st.subheader("📐 Perspective Scale Distribution")
        scale_data = telemetry["scale_distribution"]
        df_scale = pd.DataFrame(list(scale_data.items()), columns=["Scale Category", "Count"])
        fig_scale = px.pie(
            df_scale, names="Scale Category", values="Count",
            title="Bounding Box Footprint Ratio (% of Frame)",
            hole=0.4
        )
        st.plotly_chart(fig_scale, use_container_width=True)

# TAB 4: Gemini AI Audit
with tab_gemini:
    st.subheader("🤖 Autonomous Forensic & Safety Intelligence Audit")
    st.markdown("""
    Generates an expert computer vision audit by piping geometric centroids, crowd clustering metrics,
    and object taxonomies directly into Google's latest **Gemini** multimodal architecture.
    """)

    btn_text = "Genera Rapporto di Sorveglianza con Gemini AI 🚀" if lang_code == "it" else "Generate Forensic Surveillance Audit with Gemini AI 🚀"

    if st.button(btn_text, type="primary"):
        with st.spinner("Executing spatial intelligence reasoning with Google Gemini..."):
            report = generate_vision_audit_report(
                telemetry=telemetry,
                model_name=gemini_model,
                language=lang_code,
                api_key_override=api_key_input
            )
            st.session_state["vision_report"] = report

    if "vision_report" in st.session_state:
        st.markdown(st.session_state["vision_report"])
        st.markdown("---")
        st.download_button(
            label="📥 Download Forensic Report (.md)",
            data=st.session_state["vision_report"],
            file_name=f"Forensic_Vision_Audit_{lang_code}.md",
            mime="text/markdown"
        )

# TAB 5: Semantic Object Knowledge Base
with tab_ontology:
    st.subheader("📖 Detected Objects: Definitions & Functional Purposes")
    freqs = telemetry["item_frequencies"]
    if freqs:
        for item_name, count in freqs.items():
            from coco_definitions import get_object_info
            info = get_object_info(item_name)
            with st.expander(f"🔹 {info['name']} (Count: {count}) — Category: {info['category']}"):
                st.write(f"**Definition:** {info['definition']}")
                st.write(f"**Intended Purpose & Utility:** {info['purpose']}")
    else:
        st.write("No classified objects detected in the current frame.")
