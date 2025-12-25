import json
import os
import requests
import random
import string
from dotenv import load_dotenv

load_dotenv()

FORMBRICKS_URL = os.getenv("FORMBRICKS_URL", "https://feedback.soul23.cloud")
API_KEY = os.getenv("FORMBRICKS_API_KEY", "fbk_re7r3JGIlwrFXUgxXv4-YHbNnvjc3gD9aVm13N2LvzE")
ENVIRONMENT_ID = os.getenv("FORMBRICKS_ENVIRONMENT_ID", "cmbjyaka9000fqr01fxyfn8f3")

def generate_pseudo_cuid():
    """Genera un ID pseudo-CUID para pasar la validación."""
    return 'c' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=24))

def transform_to_formbricks(question):
    """Transforma una pregunta del formato interno al formato de la API de Formbricks."""
    fb_q = {
        "id": question["id"],
        "type": question["type"],
        "headline": {"default": question["headline"]},
        "subheader": {"default": question.get("subheader", "")},
        "required": True,
    }
    
    if "choices" in question:
        fb_q["choices"] = [
            {"id": c["id"], "label": {"default": c["label"]}} 
            for c in question["choices"]
        ]
    
    if question["type"] == "multipleChoiceSingle":
        fb_q["shuffleOption"] = "none"
        
    return fb_q

def upload_survey(file_path):
    if not API_KEY or not ENVIRONMENT_ID:
        print("Error: FORMBRICKS_API_KEY o FORMBRICKS_ENVIRONMENT_ID no configurados.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = [transform_to_formbricks(q) for q in data["questions"]]

    payload = {
        "name": data["name"],
        "type": "link",
        "status": "inProgress",
        "environmentId": ENVIRONMENT_ID,
        "displayOption": "displayOnce",
        "questions": questions,
        "welcomeCard": {
            "enabled": True,
            "headline": {"default": f"Bienvenido al {data['name']}"},
            "html": {"default": "Por favor, responde con honestidad para evaluar tu nivel técnico."},
            "buttonLabel": {"default": "Comenzar"}
        },
        "endings": [
            {
                "id": generate_pseudo_cuid(),
                "type": "endScreen",
                "headline": {"default": "¡Evaluación Completada!"},
                "subheader": {"default": "Tus respuestas han sido registradas. El equipo técnico revisará los resultados."},
                "buttonLabel": {"default": "Cerrar"},
                "buttonLink": FORMBRICKS_URL
            }
        ]
    }

    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    endpoint = f"{FORMBRICKS_URL}/api/v1/management/surveys"
    response = requests.post(endpoint, json=payload, headers=headers)

    if response.status_code in [200, 201]:
        print(f"✅ Encuesta '{data['name']}' creada exitosamente.")
        print(f"🔗 URL: {response.json().get('data', {}).get('link', 'Ver en el panel')}")
    else:
        print(f"❌ Error al crear encuesta: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    # Sincronizar los 3 niveles
    surveys = [
        "../formbricks/formbricks_basic_ready.json",
        "../formbricks/formbricks_medium_ready.json",
        "../formbricks/formbricks_advanced_ready.json"
    ]
    
    for s in surveys:
        if os.path.exists(s):
            print(f"Subiendo {s}...")
            upload_survey(s)
