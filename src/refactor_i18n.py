import json
import os
import uuid

def transform_to_i18n(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    new_data = []
    
    for q in data:
        # Generate IDs for options to decouple logic from text
        options = []
        correct_option_id = None
        
        for index, text in enumerate(q.get("respuestas", [])):
            opt_id = f"opt_{index}" # Simple ID based on index for consistency
            
            # Check if this option matches the correct answer string
            if text == q.get("respuesta_correcta"):
                correct_option_id = opt_id
            
            options.append({
                "id": opt_id,
                "label": {
                    "es": text,
                    "en": "", # Placeholder
                    "fr": "",
                    "br": "",
                    "cn": "",
                    "ge": ""
                }
            })
            
        new_q = {
            "id": q["id"],
            "category": {
                "es": q["categoria"],
                "en": "" # Placeholder
            },
            "type": q["tipo"], # "Teórico" or "Práctico" (Internal types might remain static or need mapping)
            "question": {
                "es": q["pregunta"],
                "en": "",
                "fr": "",
                "br": "",
                "cn": "",
                "ge": ""
            },
            "options": options,
            "correct_option_id": correct_option_id,
            "reasoning": {
                "es": q.get("razonamiento", ""),
                "en": "",
                "fr": "",
                "br": "",
                "cn": "",
                "ge": ""
            },
            "est_score": q.get("est_score", 1.0)
        }
        new_data.append(new_q)
        
    return new_data

def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved: {path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, "master_assesment/json")
    
    files = [
        "basic_assesment.json",
        "medium_assesment.json",
        "advanced_assesment.json"
    ]
    
    for filename in files:
        full_path = os.path.join(target_dir, filename)
        if os.path.exists(full_path):
            i18n_data = transform_to_i18n(full_path)
            # Overwrite original or create new? Let's overwrite as this is a refactor.
            save_json(i18n_data, full_path)
        else:
            print(f"File not found: {full_path}")
