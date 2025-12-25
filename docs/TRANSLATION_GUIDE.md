# Guía de Traducción Técnica - Code Carol

## 📋 Resumen

Esta guía documenta el proceso de traducción de las evaluaciones técnicas a 5 idiomas adicionales, manteniendo la precisión terminológica en moldeo por inyección.

## 🌍 Idiomas Objetivo

| Código | Idioma | Prioridad | Status |
|--------|--------|-----------|--------|
| `en` | English (Technical) | Alta | 🟡 En Progreso |
| `fr` | French (Technical) | Media | ⚪ Pendiente |
| `br` | Brazilian Portuguese | Media | ⚪ Pendiente |
| `cn` | Simplified Chinese | Baja | ⚪ Pendiente |
| `ge` | German (Technical) | Baja | ⚪ Pendiente |

## 🔧 Herramientas Disponibles

### 1. Traducción Automática con IA

**Script:** `src/translate_with_ai.py`

Este script utiliza modelos de IA (Google Gemini o OpenAI) con un glosario técnico especializado.

#### Configuración

1. Copiar `.env.example` a `.env`
2. Agregar tu API key:
   ```bash
   # Para Google Gemini (recomendado)
   GEMINI_API_KEY=tu_api_key_aqui
   
   # ó para OpenAI
   OPENAI_API_KEY=tu_api_key_aqui
   ```

3. Instalar dependencias:
   ```bash
   pip install google-generativeai  # Para Gemini
   # o
   pip install openai  # Para OpenAI
   ```

#### Uso Básico

```bash
# Traducir todos los archivos con Gemini (default)
python src/translate_with_ai.py

# Usar OpenAI en su lugar
python src/translate_with_ai.py --openai

# Traducir un archivo específico
python src/translate_with_ai.py --file basic_assesment.json

# Traducir solo a inglés
python src/translate_with_ai.py --lang en

# Reanudar desde la pregunta 50
python src/translate_with_ai.py --file medium_assesment.json --start 50

# Procesar solo 10 preguntas (para pruebas)
python src/translate_with_ai.py --file basic_assesment.json --max 10
```

### 2. Preparación de Estructura (Sin Traducción)

**Script:** `src/translate_assessments.py`

Solo crea la estructura vacía sin traducir. Útil para:
- Preparar archivos para traducción manual
- Verificar la estructura antes de usar la IA

```bash
python src/translate_assessments.py
```

## 📖 Glosario Técnico

El script incluye un glosario especializado con términos clave de moldeo por inyección:

| Español | English | French | Portuguese | Chinese | German |
|---------|---------|--------|------------|---------|--------|
| Short Shot | Short Shot | Manque de matière | Peça Incompleta | 短射 | Kurzer Schuss |
| Sink Mark | Sink Mark | Retassure | Marca de Afundamento | 缩痕 | Einfallstelle |
| Flash / Rebaba | Flash | Bavure | Rebarba | 飞边 | Grat |
| Warpage / Deformación | Warpage | Déformation | Empenamento | 翘曲 | Verzug |
| Weld Line | Weld Line | Ligne de soudure | Linha de Solda | 熔接线 | Bindennaht |
| Gate / Compuerta | Gate | Seuil | Entrada | 浇口 | Anguss |
| Sprue / Bebedero | Sprue | Carotte | Bico de Injeção | 主流道 | Angusskanal |
| Barrel / Barril | Barrel | Fourreau | Barril | 料筒 | Zylinder |
| Screw / Husillo | Screw | Vis | Rosca | 螺杆 | Schnecke |
| Nozzle / Boquilla | Nozzle | Buse | Bico | 喷嘴 | Düse |
| Cavity / Cavidad | Cavity | Cavité | Cavidade | 型腔 | Kavität |
| Mold / Molde | Mold | Moule | Molde | 模具 | Form |
| Ejector Pin / Botador | Ejector Pin | Éjecteur | Pino Ejetor | 顶针 | Auswerferstift |
| Clamping Force / Tonelaje | Clamping Force | Force de fermeture | Força de Fechamento | 锁模力 | Schließkraft |
| Back Pressure / Contrapresión | Back Pressure | Contre-pression | Contrapressão | 背压 | Staudruck |
| Cushion / Cojín | Cushion | Coussin | Colchão | 缓冲垫 | Polster |

## 🔄 Workflow Recomendado

### Fase 1: Traducción al Inglés (Prioridad Alta)

1. **Traducción Automatizada:**
   ```bash
   python src/translate_with_ai.py --lang en
   ```

2. **Revisión Técnica:**
   - Revisar términos técnicos especializados
   - Verificar consistencia terminológica
   - Validar con expertos en moldeo de habla inglesa

3. **Ajustes Manuales:**
   - Editar directamente los JSON en `master_assesment/json/`
   - Buscar y reemplazar términos inconsistentes

### Fase 2: Traducción a Otros Idiomas

Repetir el proceso para cada idioma:

```bash
# Francés
python src/translate_with_ai.py --lang fr

# Portugués
python src/translate_with_ai.py --lang br

# Chino
python src/translate_with_ai.py --lang cn

# Alemán
python src/translate_with_ai.py --lang ge
```

## ✅ Checklist de Calidad

Antes de dar por completada una traducción, verificar:

- [ ] Todos los campos tienen contenido (no vacíos)
- [ ] Términos técnicos son consistentes
- [ ] Se respetan las convenciones del idioma objetivo
- [ ] Las opciones de respuesta tienen sentido en contexto
- [ ] El razonamiento técnico es preciso
- [ ] Se mantiene el nivel de complejidad original

## 🔍 Validación Post-Traducción

1. **Ejecutar script de generación de docs:**
   ```bash
   python src/generate_docs.py
   ```
   Esto generará documentación Markdown en todos los idiomas para revisión.

2. **Verificar estructura JSON:**
   ```bash
   # Verificar que todos los JSON sean válidos
   python -m json.tool master_assesment/json/basic_assesment.json > /dev/null
   python -m json.tool master_assesment/json/medium_assesment.json > /dev/null
   python -m json.tool master_assesment/json/advanced_assesment.json > /dev/null
   python -m json.tool master_assesment/json/funnel_registration.json > /dev/null
   ```

3. **Contar campos vacíos:**
   ```bash
   # Ver cuántos campos aún están vacíos en cada idioma
   grep -r '"en": ""' master_assesment/json/ | wc -l
   grep -r '"fr": ""' master_assesment/json/ | wc -l
   grep -r '"br": ""' master_assesment/json/ | wc -l
   grep -r '"cn": ""' master_assesment/json/ | wc -l
   grep -r '"ge": ""' master_assesment/json/ | wc -l
   ```

## 💡 Consejos Técnicos

### Para Terminología Especializada

- **NO traducir** nombres de defectos estándar (Short Shot, Flash, etc.) - usar término inglés
- **SÍ traducir** las descripciones y explicaciones
- Consultar normas ISO 294 y SPI para terminología oficial

### Para Chino Simplificado

- Usar caracteres simplificados (简体中文)
- Verificar con GB/T 国家标准 (estándares nacionales chinos)
- Considerar contexto industrial de China Continental

### Para Idiomas Europeos

- Francés: Diferenciar entre moldeo canadiense vs europeo
- Alemán: Usar terminología DIN/ISO
- Portugués: Adaptarse a Brasil (no Portugal) para contexto industrial

## 📊 Métricas de Progreso

Total de elementos a traducir por archivo:

| Archivo | Preguntas | Campos Multilingües Aprox. |
|---------|-----------|----------------------------|
| `basic_assesment.json` | ~180 | ~900 |
| `medium_assesment.json` | ~175 | ~875 |
| `advanced_assesment.json` | ~180 | ~900 |
| `funnel_registration.json` | 6 campos | ~30 |

**Total estimado:** ~2,705 elementos de traducción × 5 idiomas = **~13,525 traducciones**

## 🚀 Próximos Pasos

Una vez completada la traducción:

1. Actualizar `src/generate_docs.py` para generar docs multilingües
2. Modificar `src/sync_to_formbricks.py` para soportar selección de idioma
3. Crear landing page multilingüe para el funnel de registro
4. Implementar backend para servir evaluaciones según idioma del usuario

## 📝 Notas

- **Backups:** El script crea automáticamente `.backup` de archivos originales
- **Progreso:** Se guarda cada 10 preguntas para evitar pérdida de datos
- **Rate Limits:** El script tiene delays entre llamadas a la API
- **Costos:** Estimar ~0.01-0.05 USD por pregunta con GPT-4, gratis con Gemini (con límites)

## 🆘 Troubleshooting

### Error: "No API configurada"
```bash
# Verificar que .env existe y tiene la key correcta
cat .env | grep API_KEY
```

### Error: "Module not found"
```bash
# Instalar dependencias faltantes
pip install google-generativeai python-dotenv
```

### Traducciones de baja calidad
- Cambiar a GPT-4: `--openai`
- Reducir temperatura en el código (ya está en 0.3)
- Expandir el glosario técnico en `translate_with_ai.py`

---

**Última actualización:** Diciembre 25, 2025
**Mantenido por:** Marco Gallegos & Fortunato Salazar
