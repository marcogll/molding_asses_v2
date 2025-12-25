#!/usr/bin/env python3
"""
Traducción automática de evaluaciones de moldeo por inyección.
Traduce todas las preguntas del banco a múltiples idiomas técnicos.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, List

# Mapeo de idiomas ISO
LANGUAGES = {
    "en": "English",
    "fr": "French", 
    "br": "Brazilian Portuguese",
    "cn": "Simplified Chinese",
    "ge": "German"
}

# Diccionario de terminología técnica especializada
TECHNICAL_GLOSSARY = {
    "es": {
        "Short Shot": "Pieza Incompleta",
        "Sink Mark": "Marca de Hundimiento",
        "Flash": "Rebaba",
        "Warpage": "Deformación",
        "Weld Line": "Línea de Soldadura",
        "Gate Blush": "Blanqueamiento del Gate",
        "Jetting": "Flujo Serpentino",
        "Burn Marks": "Marcas de Quemado",
        "Moldeo por Inyección": "Injection Molding",
        "Barril": "Barrel",
        "Husillo": "Screw",
        "Tornillo": "Screw",
        "Tolva": "Hopper",
        "Boquilla": "Nozzle",
        "Bebedero": "Sprue",
        "Platina": "Platen",
        "Botador": "Ejector Pin",
        "Cavidad": "Cavity",
        "Molde": "Mold/Mould",
        "Tonelaje": "Clamping Force",
        "Cojín": "Cushion",
        "Contrapresión": "Back Pressure",
    }
}


class AssessmentTranslator:
    """Traductor de evaluaciones con preservación de terminología técnica"""
    
    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.json_dir = base_path / "master_assesment" / "json"
        
    def load_assessment(self, filename: str) -> List[Dict[str, Any]]:
        """Carga un archivo de evaluación JSON"""
        filepath = self.json_dir / filename
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def save_assessment(self, filename: str, data: List[Dict[str, Any]]):
        """Guarda una evaluación con formato bonito"""
        filepath = self.json_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def translate_field(self, text: str, target_lang: str) -> str:
        """
        Traduce un campo de texto.
        Por ahora retorna placeholder para que se traduzca manualmente.
        En producción, esto llamaría a una API de traducción (Google, DeepL, etc.)
        """
        # Aquí se integraría la API de traducción
        # return translate_api(text, source='es', target=target_lang, glossary=TECHNICAL_GLOSSARY)
        
        # Por ahora retornamos vacío para que se complete manualmente
        return ""
    
    def translate_multilingual_field(self, field: Dict[str, str], target_langs: List[str]) -> Dict[str, str]:
        """Traduce un campo multilingüe manteniendo el español base"""
        if not isinstance(field, dict):
            return field
            
        result = field.copy()
        spanish_text = field.get("es", "")
        
        for lang in target_langs:
            if lang not in result or result[lang] == "":
                # Aquí se haría la traducción real
                result[lang] = self.translate_field(spanish_text, lang)
        
        return result
    
    def process_question(self, question: Dict[str, Any], target_langs: List[str]) -> Dict[str, Any]:
        """Procesa una pregunta individual traduciendo todos sus campos"""
        result = question.copy()
        
        # Campos a traducir
        multilingual_fields = ["category", "question", "reasoning", "subheader"]
        
        for field_name in multilingual_fields:
            if field_name in result:
                result[field_name] = self.translate_multilingual_field(
                    result[field_name], 
                    target_langs
                )
        
        # Traducir opciones
        if "options" in result:
            translated_options = []
            for option in result["options"]:
                translated_option = option.copy()
                if "label" in translated_option:
                    translated_option["label"] = self.translate_multilingual_field(
                        translated_option["label"],
                        target_langs
                    )
                translated_options.append(translated_option)
            result["options"] = translated_options
        
        return result
    
    def translate_assessment(self, filename: str, target_langs: List[str] = None):
        """Traduce un archivo de evaluación completo"""
        if target_langs is None:
            target_langs = list(LANGUAGES.keys())
        
        print(f"📝 Procesando {filename}...")
        
        # Cargar datos
        data = self.load_assessment(filename)
        
        # Si es el funnel (dict), procesar de forma diferente
        if isinstance(data, dict):
            result = data.copy()
            # Traducir campos del funnel
            for field in ["title", "description"]:
                if field in result:
                    result[field] = self.translate_multilingual_field(
                        result[field],
                        target_langs
                    )
            
            # Traducir fields
            if "fields" in result:
                translated_fields = []
                for field in result["fields"]:
                    field_copy = field.copy()
                    
                    # Traducir label y description
                    for key in ["label", "description"]:
                        if key in field_copy:
                            field_copy[key] = self.translate_multilingual_field(
                                field_copy[key],
                                target_langs
                            )
                    
                    # Traducir opciones si existen
                    if "options" in field_copy:
                        translated_options = []
                        for option in field_copy["options"]:
                            option_copy = option.copy()
                            if "label" in option_copy:
                                option_copy["label"] = self.translate_multilingual_field(
                                    option_copy["label"],
                                    target_langs
                                )
                            translated_options.append(option_copy)
                        field_copy["options"] = translated_options
                    
                    translated_fields.append(field_copy)
                result["fields"] = translated_fields
            
            data = result
        else:
            # Es una lista de preguntas (assessment)
            data = [self.process_question(q, target_langs) for q in data]
        
        # Guardar resultado
        self.save_assessment(filename, data)
        print(f"✅ {filename} procesado correctamente\n")
    
    def translate_all(self):
        """Traduce todos los archivos de evaluación"""
        assessment_files = [
            "basic_assesment.json",
            "medium_assesment.json", 
            "advanced_assesment.json",
            "funnel_registration.json"
        ]
        
        target_langs = list(LANGUAGES.keys())
        
        print(f"🌍 Iniciando traducción a {len(target_langs)} idiomas: {', '.join(LANGUAGES.values())}\n")
        
        for filename in assessment_files:
            self.translate_assessment(filename, target_langs)
        
        print("🎉 Proceso de traducción completado!")
        print("\n⚠️  NOTA: Los campos están marcados como '' (vacíos).")
        print("   Se requiere integración con API de traducción (Google Translate, DeepL)")
        print("   o completar manualmente con ayuda de expertos técnicos.\n")


def main():
    """Función principal"""
    # Obtener ruta base del proyecto
    base_path = Path(__file__).parent.parent
    
    translator = AssessmentTranslator(base_path)
    translator.translate_all()


if __name__ == "__main__":
    main()
