import json
import os

def generate_markdown(level_name, json_path, output_path, passing_score, max_score, lang='es'):
    with open(json_path, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    with open(output_path, 'w', encoding='utf-8') as f:
        # Header
        f.write(f"# Code Carol: {level_name}\n\n")
        
        # Methodology Section
        f.write("## ℹ️ Información General\n")
        f.write(f"- **Total de preguntas:** {len(questions)}\n")
        f.write(f"- **Puntaje Máximo Posible:** ~{max_score} puntos.\n")
        f.write(f"- **Passing Score:** {passing_score}\n\n")
        
        f.write("---\n\n")
        f.write("## 📝 Banco de Preguntas\n\n")

        for i, q in enumerate(questions, 1):
            # Extract localized data
            category = q['category'].get(lang, q['category'].get('es', 'General'))
            question_text = q['question'].get(lang, q['question'].get('es', ''))
            q_type = q['type']
            score = q.get('est_score', 1)
            
            # Card Header
            f.write(f"### {i}. {question_text}\n\n")
            
            # Metadata Table (Card-like styling)
            f.write("| 🏷️ Categoría | ⚙️ Tipo | 💎 Puntos | 🆔 ID |\n")
            f.write("| :--- | :---: | :---: | :---: |\n")
            f.write(f"| {category} | {q_type} | {score} pts | `{q['id']}` |\n\n")
            
            # Options as Checkboxes
            for opt in q['options']:
                opt_text = opt['label'].get(lang, opt['label'].get('es', ''))
                f.write(f"- [ ] {opt_text}\n")
            
            f.write("\n<br>\n\n---\n\n")

    print(f"✅ Generado ({lang}): {output_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Configuración de los 3 niveles
    levels = [
        {
            "name": "Nivel Básico (Operaciones de Piso)",
            "json": os.path.join(base_dir, "master_assesment/json/basic_assesment.json"),
            "out": os.path.join(base_dir, "docs/questions/LEVEL_1_BASIC_ASSESSMENT.md"),
            "pass": "75%",
            "max": 62.5
        },
        {
            "name": "Nivel Medio (Técnico de Ajuste)",
            "json": os.path.join(base_dir, "master_assesment/json/medium_assesment.json"),
            "out": os.path.join(base_dir, "docs/questions/LEVEL_2_MEDIUM_ASSESSMENT.md"),
            "pass": "80%",
            "max": 135
        },
        {
            "name": "Nivel Avanzado (Ingeniería de Procesos)",
            "json": os.path.join(base_dir, "master_assesment/json/advanced_assesment.json"),
            "out": os.path.join(base_dir, "docs/questions/LEVEL_3_ADVANCED_ASSESSMENT.md"),
            "pass": "80%",
            "max": 195
        }
    ]

    for lvl in levels:
        if os.path.exists(lvl["json"]):
            generate_markdown(lvl["name"], lvl["json"], lvl["out"], lvl["pass"], lvl["max"], lang='es')
        else:
            print(f"❌ No encontrado: {lvl['json']}")
