#!/usr/bin/env python3
"""
Traducción técnica de evaluaciones usando IA (Google Gemini / OpenAI)
con preservación de terminología especializada en moldeo por inyección.
"""

import json
import os
import time
from pathlib import Path
from typing import Dict, Any, List
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Idiomas objetivo
TARGET_LANGUAGES = {
    "en": "English (Technical)",
    "fr": "French (Technical)",
    "br": "Brazilian Portuguese (Technical)",
    "cn": "Simplified Chinese (Technical)",
    "ge": "German (Technical)"
}

# Glosario técnico de referencia
TECHNICAL_CONTEXT = """
TECHNICAL GLOSSARY FOR INJECTION MOLDING TRANSLATION:

Key Terms:
- Short Shot = Pieza Incompleta (EN: Short Shot, FR: Manque de matière, BR: Peça Incompleta, CN: 短射, GE: Kurzer Schuss)
- Sink Mark = Marca de Hundimiento (EN: Sink Mark, FR: Retassure, BR: Marca de Afundamento, CN: 缩痕, GE: Einfallstelle)
- Flash = Rebaba (EN: Flash, FR: Bavure, BR: Rebarba, CN: 飞边, GE: Grat)
- Warpage = Deformación (EN: Warpage, FR: Déformation, BR: Empenamento, CN: 翘曲, GE: Verzug)
- Weld Line = Línea de Soldadura (EN: Weld Line, FR: Ligne de soudure, BR: Linha de Solda, CN: 熔接线, GE: Bindennaht)
- Gate = Compuerta (EN: Gate, FR: Seuil, BR: Entrada, CN: 浇口, GE: Anguss)
- Sprue = Bebedero (EN: Sprue, FR: Carotte, BR: Bico de Injeção, CN: 主流道, GE: Angusskanal)
- Barrel = Barril (EN: Barrel, FR: Fourreau, BR: Barril, CN: 料筒, GE: Zylinder)
- Screw = Husillo/Tornillo (EN: Screw, FR: Vis, BR: Rosca, CN: 螺杆, GE: Schnecke)
- Nozzle = Boquilla (EN: Nozzle, FR: Buse, BR: Bico, CN: 喷嘴, GE: Düse)
- Cavity = Cavidad (EN: Cavity, FR: Cavité, BR: Cavidade, CN: 型腔, GE: Kavität)
- Mold = Molde (EN: Mold, FR: Moule, BR: Molde, CN: 模具, GE: Form)
- Ejector Pin = Botador (EN: Ejector Pin, FR: Éjecteur, BR: Pino Ejetor, CN: 顶针, GE: Auswerferstift)
- Clamping Force = Tonelaje (EN: Clamping Force, FR: Force de fermeture, BR: Força de Fechamento, CN: 锁模力, GE: Schließkraft)
- Back Pressure = Contrapresión (EN: Back Pressure, FR: Contre-pression, BR: Contrapressão, CN: 背压, GE: Staudruck)
- Cushion = Cojín (EN: Cushion, FR: Coussin, BR: Colchão, CN: 缓冲垫, GE: Polster)

CRITICAL: Maintain technical precision. Do not simplify terms.
"""


class AITranslator:
    """Traductor usando modelos de IA con contexto técnico"""
    
    def __init__(self, use_gemini: bool = True):
        """
        Inicializa el traductor
        
        Args:
            use_gemini: Si True usa Google Gemini, si False usa OpenAI
        """
        self.use_gemini = use_gemini
        self.client = None
        self._initialize_client()
        
    def _initialize_client(self):
        """Inicializa el cliente de API"""
        if self.use_gemini and GEMINI_API_KEY:
            try:
                import google.generativeai as genai
                genai.configure(api_key=GEMINI_API_KEY)
                self.client = genai.GenerativeModel('gemini-pro')
                print("✅ Usando Google Gemini para traducción")
            except ImportError:
                print("⚠️  google-generativeai no instalado. Instala con: pip install google-generativeai")
                self.use_gemini = False
                
        if not self.use_gemini and OPENAI_API_KEY:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=OPENAI_API_KEY)
                print("✅ Usando OpenAI para traducción")
            except ImportError:
                print("⚠️  openai no instalado. Instala con: pip install openai")
    
    def translate_text(self, text: str, target_lang: str, source_lang: str = "es") -> str:
        """
        Traduce un texto preservando terminología técnica
        
        Args:
            text: Texto a traducir
            target_lang: Código del idioma objetivo (en, fr, br, cn, ge)
            source_lang: Código del idioma fuente (default: es)
            
        Returns:
            Texto traducido
        """
        if not text or text.strip() == "":
            return ""
        
        target_lang_name = TARGET_LANGUAGES.get(target_lang, target_lang)
        
        prompt = f"""{TECHNICAL_CONTEXT}

TRANSLATION TASK:
- Source Language: Spanish (Technical - Injection Molding Industry)
- Target Language: {target_lang_name}
- Context: Technical assessment for injection molding operators and engineers

SOURCE TEXT:
{text}

INSTRUCTIONS:
1. Translate maintaining technical precision
2. Use the glossary above as reference
3. Preserve industry-standard terminology
4. Return ONLY the translated text, no explanations
5. If unsure, prefer the English technical term over literal translation

TRANSLATION:"""

        try:
            if self.use_gemini and self.client:
                response = self.client.generate_content(prompt)
                return response.text.strip()
            elif self.client:  # OpenAI
                response = self.client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a technical translator specialized in injection molding terminology."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.3
                )
                return response.choices[0].message.content.strip()
            else:
                print(f"⚠️  No API configurada. Retornando texto vacío.")
                return ""
                
        except Exception as e:
            print(f"❌ Error traduciendo: {e}")
            return ""
        
        # Rate limiting para evitar problemas con la API
        time.sleep(0.5)
    
    def translate_multilingual_field(self, field: Dict[str, str], target_langs: List[str]) -> Dict[str, str]:
        """Traduce un campo multilingüe"""
        if not isinstance(field, dict):
            return field
        
        result = field.copy()
        spanish_text = field.get("es", "")
        
        if not spanish_text:
            return result
        
        for lang in target_langs:
            # Solo traducir si está vacío o no existe
            if lang not in result or result[lang] == "":
                print(f"   🔄 Traduciendo a {lang}...", end=" ")
                translated = self.translate_text(spanish_text, lang)
                result[lang] = translated
                print(f"✅")
        
        return result
    
    def process_question(self, question: Dict[str, Any], target_langs: List[str]) -> Dict[str, Any]:
        """Procesa una pregunta traduciendo todos sus campos"""
        result = question.copy()
        
        print(f"\n📌 Pregunta ID: {result.get('id', 'unknown')}")
        
        # Campos multilingües
        multilingual_fields = ["category", "question", "reasoning", "subheader"]
        
        for field_name in multilingual_fields:
            if field_name in result and isinstance(result[field_name], dict):
                print(f"  Traduciendo campo: {field_name}")
                result[field_name] = self.translate_multilingual_field(
                    result[field_name],
                    target_langs
                )
        
        # Traducir opciones
        if "options" in result:
            print(f"  Traduciendo {len(result['options'])} opciones")
            translated_options = []
            for idx, option in enumerate(result["options"]):
                translated_option = option.copy()
                if "label" in translated_option:
                    translated_option["label"] = self.translate_multilingual_field(
                        translated_option["label"],
                        target_langs
                    )
                translated_options.append(translated_option)
            result["options"] = translated_options
        
        return result


class AssessmentTranslationManager:
    """Gestiona la traducción de evaluaciones completas"""
    
    def __init__(self, base_path: Path, use_gemini: bool = True):
        self.base_path = base_path
        self.json_dir = base_path / "master_assesment" / "json"
        self.translator = AITranslator(use_gemini=use_gemini)
        
    def load_assessment(self, filename: str) -> List[Dict[str, Any]] | Dict[str, Any]:
        """Carga un archivo JSON de evaluación"""
        filepath = self.json_dir / filename
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def save_assessment(self, filename: str, data: List[Dict[str, Any]] | Dict[str, Any]):
        """Guarda evaluación con formato"""
        filepath = self.json_dir / filename
        # Backup del archivo original
        backup_path = filepath.with_suffix('.json.backup')
        if filepath.exists() and not backup_path.exists():
            import shutil
            shutil.copy(filepath, backup_path)
            print(f"💾 Backup guardado: {backup_path.name}")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def translate_assessment_file(self, filename: str, target_langs: List[str] = None, 
                                  start_from: int = 0, max_questions: int = None):
        """
        Traduce un archivo de evaluación
        
        Args:
            filename: Nombre del archivo JSON
            target_langs: Lista de códigos de idioma
            start_from: Índice desde donde empezar (para reanudar)
            max_questions: Máximo de preguntas a procesar (None = todas)
        """
        if target_langs is None:
            target_langs = list(TARGET_LANGUAGES.keys())
        
        print(f"\n{'='*60}")
        print(f"📝 PROCESANDO: {filename}")
        print(f"{'='*60}\n")
        
        data = self.load_assessment(filename)
        
        # Si es el funnel (dict), proceso diferente
        if isinstance(data, dict):
            result = data.copy()
            
            # Traducir título y descripción
            for field in ["title", "description"]:
                if field in result:
                    print(f"Traduciendo {field}...")
                    result[field] = self.translator.translate_multilingual_field(
                        result[field],
                        target_langs
                    )
            
            # Traducir campos del formulario
            if "fields" in result:
                for field_idx, field in enumerate(result["fields"]):
                    print(f"\n📋 Campo {field_idx + 1}/{len(result['fields'])}: {field.get('id', 'unknown')}")
                    
                    for key in ["label", "description"]:
                        if key in field:
                            field[key] = self.translator.translate_multilingual_field(
                                field[key],
                                target_langs
                            )
                    
                    # Traducir opciones
                    if "options" in field:
                        for option in field["options"]:
                            if "label" in option:
                                option["label"] = self.translator.translate_multilingual_field(
                                    option["label"],
                                    target_langs
                                )
            
            data = result
        else:
            # Es una lista de preguntas
            total = len(data)
            end_idx = min(start_from + max_questions, total) if max_questions else total
            
            print(f"📊 Total de preguntas: {total}")
            print(f"🎯 Procesando desde {start_from} hasta {end_idx}\n")
            
            for idx in range(start_from, end_idx):
                print(f"\n[{idx + 1}/{total}]", end=" ")
                data[idx] = self.translator.process_question(data[idx], target_langs)
                
                # Guardar progreso cada 10 preguntas
                if (idx + 1) % 10 == 0:
                    self.save_assessment(filename, data)
                    print(f"\n💾 Progreso guardado (hasta pregunta {idx + 1})")
        
        # Guardar resultado final
        self.save_assessment(filename, data)
        print(f"\n✅ {filename} completado!")
    
    def translate_all(self, selected_files: List[str] = None):
        """Traduce todos los archivos de evaluación"""
        files = selected_files or [
            "funnel_registration.json",
            "basic_assesment.json",
            "medium_assesment.json",
            "advanced_assesment.json"
        ]
        
        print(f"\n🌍 INICIANDO TRADUCCIÓN TÉCNICA")
        print(f"📚 Archivos: {len(files)}")
        print(f"🗣️  Idiomas: {', '.join(TARGET_LANGUAGES.values())}\n")
        
        for filename in files:
            self.translate_assessment_file(filename)
        
        print(f"\n{'='*60}")
        print("🎉 ¡TRADUCCIÓN COMPLETADA!")
        print(f"{'='*60}\n")


def main():
    """Función principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Traductor de evaluaciones técnicas")
    parser.add_argument("--file", type=str, help="Archivo específico a traducir")
    parser.add_argument("--start", type=int, default=0, help="Pregunta desde donde empezar")
    parser.add_argument("--max", type=int, help="Máximo de preguntas a procesar")
    parser.add_argument("--openai", action="store_true", help="Usar OpenAI en vez de Gemini")
    parser.add_argument("--lang", type=str, help="Idioma específico (en, fr, br, cn, ge)")
    
    args = parser.parse_args()
    
    # Verificar API keys
    if args.openai and not OPENAI_API_KEY:
        print("❌ Error: OPENAI_API_KEY no configurada en .env")
        return
    elif not args.openai and not GEMINI_API_KEY:
        print("❌ Error: GEMINI_API_KEY no configurada en .env")
        return
    
    base_path = Path(__file__).parent.parent
    manager = AssessmentTranslationManager(base_path, use_gemini=not args.openai)
    
    target_langs = [args.lang] if args.lang else list(TARGET_LANGUAGES.keys())
    
    if args.file:
        manager.translate_assessment_file(
            args.file,
            target_langs=target_langs,
            start_from=args.start,
            max_questions=args.max
        )
    else:
        manager.translate_all()


if __name__ == "__main__":
    main()
