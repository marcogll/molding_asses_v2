#!/usr/bin/env python3
"""
Script de prueba para verificar traducciones
Traduce solo las primeras 3 preguntas del basic_assesment para validación
"""

import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from translate_with_ai import AssessmentTranslationManager, TARGET_LANGUAGES


def test_translation():
    """Ejecuta prueba de traducción en muestra pequeña"""
    
    print("🧪 MODO DE PRUEBA - Traducción de Muestra")
    print("=" * 60)
    print("Se traducirán solo las primeras 3 preguntas para validación\n")
    
    base_path = Path(__file__).parent.parent
    
    # Usar Gemini por defecto
    manager = AssessmentTranslationManager(base_path, use_gemini=True)
    
    # Traducir solo 3 preguntas de basic_assesment
    print("📝 Archivo: basic_assesment.json")
    print("🎯 Preguntas: 3 primeras")
    print(f"🌍 Idiomas: {', '.join(TARGET_LANGUAGES.values())}\n")
    
    try:
        manager.translate_assessment_file(
            "basic_assesment.json",
            start_from=0,
            max_questions=3
        )
        
        print("\n" + "=" * 60)
        print("✅ PRUEBA COMPLETADA")
        print("=" * 60)
        print("\nRevisa el archivo:")
        print("  master_assesment/json/basic_assesment.json")
        print("\nPara traducir todo, ejecuta:")
        print("  python src/translate_with_ai.py")
        
    except Exception as e:
        print(f"\n❌ Error durante la prueba: {e}")
        print("\nVerifica:")
        print("  1. Que tu .env tiene GEMINI_API_KEY configurada")
        print("  2. Que instalaste: pip install google-generativeai python-dotenv")
        return False
    
    return True


if __name__ == "__main__":
    success = test_translation()
    sys.exit(0 if success else 1)
