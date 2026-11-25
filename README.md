# 👁️ OmniCount Pro — Spatial Crowd Intelligence & Multi-Class Object Telemetry

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![YOLO](https://img.shields.io/badge/YOLO-YOLOv8%20(Ultralytics)-red.svg)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)
![OpenCV](https://img.shields.io/badge/Vision-OpenCV%20%7C%20Spatial%20KDE-green.svg)
![UI](https://img.shields.io/badge/UI-Streamlit%20%2B%20Plotly-blueviolet.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

**OmniCount Pro** is an academic-grade Computer Vision and Spatial Intelligence platform that unifies real-time object detection, pairwise Euclidean social proximity modeling, 2D Gaussian crowd density heatmaps, and multimodal AI forensic surveillance auditing powered by **YOLOv8** and **Google Gemini**.

---

## 🏛️ Academic Relevance & University Admissions Overview
Standard object counting scripts only report isolated bounding box counts. Top computer vision programs (such as *Politecnico di Milano*, *Politecnico di Torino*, and *University of Bologna*) emphasize:
1. **Spatial Geometry & Graph Theory:** Modeling pairwise distance matrices between visual agents to quantify congestion dynamics and social proximity.
2. **Thermal Density Modeling:** Applying 2D Gaussian kernel accumulation to identify crowd bottlenecks in urban spaces.
3. **Multimodal LLM Reasoning:** Bridging raw geometric detections with large multimodal models to generate contextual urban safety audits in **English** and **Italian**.
4. **Semantic Knowledge Ontologies:** Categorizing detected items into structured macro-taxonomies (Humans, Vehicles, Technology, Infrastructure, Consumables) with linguistic definitions and functional purposes.

---

## 🌟 Key Engineering Features

- **Deep Object Localization (YOLOv8):** Single-stage convolutional inference on the 80-class COCO benchmark with Non-Maximum Suppression (NMS).
- **Pairwise Social Proximity Graph:**
  - Calculates continuous Euclidean distances between all human centroids.
  - Automatically renders dynamic red vector connection lines between individuals violating configurable distance thresholds.
- **Empirical Crowd Congestion Index (CCI):**
  - Formulates a normalized congestion ratio quantifying crowd compaction risk.
- **2D Gaussian Crowd Density Heatmaps:**
  - Blends smooth thermal accumulation maps (`cv2.COLORMAP_JET`) over visual frames to spotlight pedestrian congestion hotspots.
- **Perspective Scale Distribution:**
  - Evaluates bounding box area ratios to categorize objects into Small ($<2\%$), Medium ($2\%-15\%$), and Large ($>15\%$) visual footprints.
- **Gemini AI Surveillance Audit (Bilingual EN/IT):**
  - Synthesizes geometric telemetry into peer-review-grade surveillance briefs, scene classification, and safety interventions using the official `google-genai` SDK.
- **Dual Interface:** Interactive Streamlit Web Dashboard (`streamlit run app.py`) and high-throughput headless CLI (`python main.py`).

---

## 📁 Repository Architecture

```text
├── app.py                  # Interactive Streamlit Web Dashboard (Visuals, Heatmap, Telemetry)
├── main.py                 # Terminal Command Line Interface (CLI Engine)
├── detector.py             # Core YOLOv8 inference & multi-layer visual renderer
├── spatial_analyzer.py     # Euclidean geometry, CCI formula & Gaussian KDE engine
├── gemini_vision_audit.py  # Google Gemini AI Surveillance Auditor (google-genai)
├── coco_definitions.py     # 80-Class Semantic Knowledge Base & Macro Taxonomy
├── requirements.txt        # Production dependencies
├── .env.example            # Environment template for Gemini API key
├── .gitignore              # Clean repository tracking rules
└── README.md               # Scientific documentation
```

---

## 🧠 Mathematical Formulation

### 1. Pairwise Euclidean Distance
For any pair of detected individuals $i$ and $j$ with bounding box centroids $(x_i, y_i)$ and $(x_j, y_j)$:
$$d(i, j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}$$

### 2. Crowd Congestion Index (CCI)
Given $N$ detected individuals, the total possible unique pairings is $\binom{N}{2} = \frac{N(N-1)}{2}$.  
Let $C_{\text{thresh}}$ be the count of pairs where $d(i, j) < \tau_{\text{proximity}}$:
$$\text{CCI} = \left( \frac{C_{\text{thresh}}}{\max\left(1, \frac{N(N-1)}{2}\right)} \right) \times 100\%$$

### 3. Spatial Gaussian Accumulation
Density at coordinate $(x, y)$ is accumulated across all $N$ pedestrian centroids $(x_c, y_c)$ using radial kernel variance $\sigma$:
$$D(x, y) = \sum_{k=1}^{N} \exp\left( -\frac{(x - x_{c,k})^2 + (y - y_{c,k})^2}{2\sigma^2} \right)$$

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/anasaleemkhan/OmniCount.git
cd OmniCount
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Gemini API Key (Optional for AI Audit)
Get a free key at [Google AI Studio](https://aistudio.google.com/):
```bash
# Windows PowerShell
$env:GEMINI_API_KEY="your-api-key-here"

# Linux / macOS
export GEMINI_API_KEY="your-api-key-here"
```
*(Or create a `.env` file containing `GEMINI_API_KEY=your_key_here`).*

---

## 💻 How to Run

### Option A: Launch Standalone Interactive Webpage (Recommended)
Double-click `index.html` in any web browser, or launch the lightweight local server:
```bash
python web_server.py
```
*Access in browser at `http://localhost:8000` (or deploy directly via **GitHub Pages**).*

### Option B: Launch Interactive Streamlit Dashboard
```bash
streamlit run app.py
```
*Access in browser at `http://localhost:8501`.*

### Option C: Run in Terminal (CLI Mode)
```bash
# Basic detection on an image
python main.py --image your_photo.jpg

# Detection with custom confidence, proximity threshold, and AI forensic audit
python main.py --image your_photo.jpg --conf 0.40 --proximity 110 --ai --lang en
```

---

## 📊 Sample CLI Output

```text
==============================================================================
           👁️ OMNICOUNT PRO - SPATIAL VISION & TELEMETRY REPORT           
==============================================================================
Total Objects Detected    : 8
Total People Count        : 5
Crowd Congestion Index    : 40.0% (High Density)
Clustered People Pairs    : 4 of 10 pairs
------------------------------------------------------------------------------
No.  Object           Category       Count   Definition & Functional Purpose
------------------------------------------------------------------------------
1    Person           Humans         5       Def: A human individual of any age or gender.
                                             Purpose: Pedestrian mobility and social interaction.
------------------------------------------------------------------------------
2    Bicycle          Vehicles       2       Def: A human-powered two-wheeled vehicle.
                                             Purpose: Zero-emission personal urban commuting.
------------------------------------------------------------------------------
3    Backpack         Accessories    1       Def: A fabric load-bearing pack on shoulders.
                                             Purpose: Hands-free carriage of portable computing.
------------------------------------------------------------------------------

[✓] Annotated visual saved to : output_detected.jpg
[✓] Spatial heatmap saved to  : output_heatmap.jpg
[✓] Raw telemetry saved to   : telemetry_report.json
==============================================================================
```

---

## 📄 Resume Bullet Points (Copy & Paste)

```markdown
• OmniCount Pro — Spatial Computer Vision & Crowd Telemetry Engine | Python, YOLOv8, OpenCV, Gemini API, Plotly
- Engineered a deep computer vision platform executing multi-class object localization, pedestrian spatial density mapping, and pairwise Euclidean social proximity modeling on the 80-class COCO benchmark.
- Developed algorithmic modules calculating normalized Crowd Congestion Indices (CCI) and generating 2D Gaussian density heatmaps (KDE) to isolate spatial clustering bottlenecks in urban surveillance scenes.
- Integrated Google Gemini via the `google-genai` SDK to transform geometric coordinate telemetry into bilingual (English/Italian) forensic risk briefs and smart city safety recommendations.
- Built a responsive visual analytics dashboard in Streamlit and Plotly featuring real-time confidence sliders, object scale distributions, and semantic knowledge ontologies.
```

---

## 👤 Author
Developed by **Anas Aleem**  
Email: [anasaleemofficial@gmail.com](mailto:anasaleemofficial@gmail.com)  
GitHub: [@anasaleemkhan](https://github.com/anasaleemkhan)

---

## 📜 License
This project is open-source and licensed under the [MIT License](LICENSE).
