"""
Gemini AI Spatial Intelligence & Surveillance Audit Module.
Transforms computer vision detection telemetry and proximity metrics into
academic-grade forensic reports and urban safety recommendations.
"""

import json
import os
from typing import Dict, Optional
from dotenv import load_dotenv

# Load local environment variables
current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(current_dir, ".env"))

try:
    from google import genai
    from google.genai import types
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


def get_api_key(api_key_override: Optional[str] = None) -> Optional[str]:
    """Retrieves API key from override, environment, or .env file."""
    if api_key_override and api_key_override.strip():
        return api_key_override.strip()

    # Direct search in local and parent .env
    for candidate in [
        os.path.join(current_dir, ".env"),
        os.path.join(current_dir, "EduPath-AI", ".env"),
        os.path.join(os.path.dirname(current_dir), ".env")
    ]:
        if os.path.exists(candidate):
            try:
                with open(candidate, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("GEMINI_API_KEY=") and not line.startswith("#"):
                            val = line.split("=", 1)[1].strip().strip('"').strip("'")
                            if val:
                                return val
            except Exception:
                pass

    return os.getenv("GEMINI_API_KEY", "").strip() or None


def generate_vision_audit_report(
    telemetry: Dict,
    model_name: str = "gemini-2.5-flash",
    language: str = "en",
    api_key_override: Optional[str] = None
) -> str:
    """Generates an academic forensic audit report from spatial detection telemetry."""
    key = get_api_key(api_key_override)
    telemetry_json = json.dumps(telemetry, indent=2)

    if not key or not GEMINI_AVAILABLE:
        # Fallback simulation
        people = telemetry.get("people_count", 0)
        total = telemetry.get("total_objects", 0)
        congestion = telemetry.get("crowd_metrics", {}).get("congestion_index", 0.0)
        risk = telemetry.get("crowd_metrics", {}).get("risk_level", "Normal")

        if language == "it":
            return f"""### 👁️ Rapporto Forense di Sorveglianza Visiva *(Modalità Demo)*
> **Nota:** Configura la chiave API Gemini per sbloccare l'analisi multimodale in tempo reale.

- **Oggetti Totali Rilevati:** {total}
- **Persone Presenti:** {people}
- **Indice di Congestione della Folla:** {congestion}% ({risk})

#### Valutazione Spaziale & Sicurezza Urbana:
L'analisi geometrica evidenzia un modello di aggregazione pedonale classificato come **{risk}**.
La distribuzione degli oggetti riflette un ambiente antropico attivo. Si raccomanda il monitoraggio delle vie di transito e dei corridoi pedonali."""

        return f"""### 👁️ Computer Vision & Spatial Intelligence Audit *(Demonstration Mode)*
> **Notice:** Provide a Gemini API key to activate live reasoning via `{model_name}`.

- **Total Detected Objects:** {total}
- **Total People Count:** {people}
- **Crowd Congestion Index (CCI):** {congestion}% ({risk})

#### Spatial Distribution & Safety Appraisal:
Pairwise Euclidean proximity telemetry classifies the pedestrian clustering status as **{risk}**.
The object category breakdown suggests an active communal or transit setting. Regular pedestrian flow balancing is recommended."""

    # Prompt Engineering for Academic Vision Examiner
    if language == "it":
        prompt = f"""
Sei un Senior Computer Vision Researcher e Analista di Smart Cities presso un centro di ricerca europeo (es. Politecnico di Milano).
Hai ricevuto la telemetria geometrica e semantica estratta da un modello YOLOv8:

```json
{telemetry_json}
```

Genera un rapporto accademico rigoroso e professionale strutturato in Markdown:
1. **Classificazione della Scena & Contesto Urbano**: Basandoti sugli oggetti rilevati e sul numero di persone, deduci il setting plausibile (es. piazza pubblica, aula, terminal di transito, ufficio).
2. **Analisi Spaziale della Folla & Metriche di Prossimità**: Interpreta l'Indice di Congestione della Folla (CCI) e le coppie ravvicinate. C'è rischio di assembramento o blocco dei flussi?
3. **Tassonomia degli Oggetti & Interazione Uomo-Oggetto**: Analizza la relazione tra le persone e gli oggetti circostanti (veicoli, tecnologia, accessori).
4. **Raccomandazioni per Smart Cities & Sicurezza Pubblica**: Suggerisci interventi di gestione dei flussi pedonali e allocazione delle risorse.
"""
    else:
        prompt = f"""
You are a Principal Computer Vision Researcher and Smart City Surveillance Auditor.
You have been provided with the spatial telemetry, pairwise Euclidean proximity, and multi-class detections extracted by a YOLOv8 deep learning pipeline:

```json
{telemetry_json}
```

Generate an academic-grade, structured Computer Vision & Spatial Intelligence Report in clean Markdown:
1. **Scene Classification & Contextual Inferences**: Deduce the plausible real-world environment (e.g., pedestrian plaza, transportation hub, educational auditorium, workplace) based on object co-occurrence and human density.
2. **Crowd Dynamics & Proximity Risk Analysis**: Evaluate the Crowd Congestion Index (CCI), clustered pairs, and spatial clustering footprint. What are the flow bottlenecks?
3. **Object Taxonomy & Human-Asset Interaction**: Interpret the interaction between individuals and surrounding assets (vehicles, electronics, gear, infrastructure).
4. **Actionable Smart City & Safety Interventions**: Propose algorithmic flow optimization, safety monitoring recommendations, and automated alerting thresholds.
"""

    client = genai.Client(api_key=key)
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        return response.text
    except Exception as e:
        # Fallback to secondary model if first choice encounters rate limits
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except Exception as e2:
            return f"⚠️ **Gemini API Execution Error:** {str(e2)}"
