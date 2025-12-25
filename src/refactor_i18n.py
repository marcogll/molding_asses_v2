import json
import os
import uuid

def load_formbricks_subheaders(formbricks_ready_path):
    subheaders = {}
    try:
        with open(formbricks_ready_path, 'r', encoding='utf-8') as f:
            formbricks_data = json.load(f)
            for q in formbricks_data.get("questions", []):
                if "id" in q and "subheader" in q:
                    subheaders[q["id"]] = q["subheader"]
    except FileNotFoundError:
        print(f"Warning: Formbricks ready file not found at {formbricks_ready_path}. Subheaders will be empty.")
    except Exception as e:
        print(f"Error loading formbricks subheaders from {formbricks_ready_path}: {e}")
    return subheaders

def transform_to_i18n(file_path, subheaders_map):
    print(f"Processing {file_path} for subheaders...")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    new_data = []
    
    for q in data:
        # Assuming the structure is already i18n refactored, just add/update subheader
        if "subheader" not in q:
            q["subheader"] = {
                "es": subheaders_map.get(q["id"], ""),
                "en": "",
                "fr": "",
                "br": "",
                "cn": "",
                "ge": ""
            }
        else: # Update existing subheader if needed (e.g., if re-running or adding new language)
            q["subheader"]["es"] = subheaders_map.get(q["id"], q["subheader"].get("es", ""))
        
        new_data.append(q) # Append the modified question
        
    return new_data

def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved: {path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    master_json_dir = os.path.join(base_dir, "master_assesment/json")
    formbricks_ready_dir = os.path.join(base_dir, "formbricks")
    
    file_mappings = [
        ("basic_assesment.json", "formbricks_basic_ready.json"),
        ("medium_assesment.json", "formbricks_medium_ready.json"),
        ("advanced_assesment.json", "formbricks_advanced_ready.json")
    ]
    
    for master_filename, formbricks_filename in file_mappings:
        formbricks_full_path = os.path.join(formbricks_ready_dir, formbricks_filename)
        subheaders_map = load_formbricks_subheaders(formbricks_full_path)
        
        master_full_path = os.path.join(master_json_dir, master_filename)
        if os.path.exists(master_full_path):
            i18n_data = transform_to_i18n(master_full_path, subheaders_map)
            save_json(i18n_data, master_full_path)
        else:
            print(f"File not found: {master_full_path}")
