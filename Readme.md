# Carol: Molding Assessment Framework

> **CAROL (Competence Assessment and Review Online Learning)** es un hub de evaluación integral para medir, estandarizar y potenciar el conocimiento técnico en moldeo por inyección.
> Soluciona la falta de métricas objetivas en la competencia del personal, transformando el "sentimiento" operativo en datos accionables para reducir scrap, mejorar el OEE y garantizar la seguridad.

## 📋 Tabla de Contenidos

1. [Objetivo del Proyecto](#-objetivo-del-proyecto)
2. [Guía de Uso](#-guía-de-uso)
3. [Estructura del Repositorio](#-estructura-del-repositorio)
4. [Ejemplos de Resultados](#-ejemplos-de-resultados)
5. [KPIs Relevantes](#-kpis-relevantes)
6. [Documentación Vinculada](#-documentación-vinculada)
7. [Contribución](#-contribución)
8. [Créditos y Autores](#-créditos-y-autores)
9. [Licencia y Ética](#-licencia-y-ética)
10. [Actualizaciones](#-actualizaciones)

---

## 🎯 Objetivo del Proyecto

Este repositorio actúa como un **núcleo central de evaluación (Assessment Hub)**. Su propósito va más allá de un simple examen; es una herramienta de diagnóstico y mejora continua diseñada para:

1.  **Medir el Nivel de Competencia Real:** Evaluar objetivamente al personal operativo, técnico y de ingeniería mediante un sistema de puntuación ponderado (Teórico vs. Práctico).
2.  **Identificar Brechas de Conocimiento:** Detectar áreas específicas de debilidad (ej. Reología, Seguridad, Defectos) para dirigir la capacitación.
3.  **Base de Datos para Entrenamiento:** Generar inputs para planes de "Upskilling" personalizados.
4.  **Evolución de KPIs:** Correlacionar el incremento del conocimiento técnico con la mejora de indicadores de planta (Scrap, OEE) en un horizonte de 12 meses.

**Alcance (Scope):**
*   **Incluye:** Evaluaciones técnicas (Nivel 1, 2 y 3), lógica de puntuación, bancos de preguntas (JSON) y guías de implementación.
*   **No Incluye:** Software de simulación de inyección ni control directo de máquinas.

---

## 🚀 Guía de Uso

### Prerrequisitos
*   Python 3.8+ instalado.
*   Instancia de Formbricks activa (VPS) - *opcional para sincronización*.
*   Variables de entorno configuradas (`.env`).
*   API Key de Google Gemini o OpenAI - *opcional, solo para traducción automática*.

### Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone <repo_url>
   cd molding_assesment_v2
   ```

2. **Instalar dependencias básicas:**
   ```bash
   pip install requests python-dotenv
   ```

3. **Para traducción automática (opcional):**
   ```bash
   # Opción 1: Google Gemini (recomendado)
   pip install google-generativeai
   
   # Opción 2: OpenAI
   pip install openai
   ```

4. **Configurar variables de entorno:**
   ```bash
   cp .env.example .env
   nano .env  # Editar con tus API keys
   ```

### Verificar Estado del Proyecto

```bash
# Ver progreso del roadmap y próximas tareas
python src/check_tasks.py
```

### Traducción Multilingüe (Nuevo ✨)

Code Carol ahora soporta **evaluaciones en 6 idiomas**: Español (ES), Inglés (EN), Francés (FR), Portugués Brasileño (BR), Chino Simplificado (CN) y Alemán (GE).

#### Traducir con IA (Google Gemini / OpenAI)

```bash
# Probar traducción con muestra de 3 preguntas
python src/test_translation.py

# Traducir todo al inglés
python src/translate_with_ai.py --lang en

# Traducir a todos los idiomas
python src/translate_with_ai.py

# Usar OpenAI en lugar de Gemini
python src/translate_with_ai.py --openai --lang en

# Reanudar traducción desde pregunta 50
python src/translate_with_ai.py --file basic_assesment.json --start 50
```

**Características:**
- 🧠 **Traducción con IA contextual** - Preserva terminología técnica
- 📖 **Glosario especializado** - 15+ términos de moldeo por inyección
- 💾 **Backups automáticos** - Guarda `.backup` antes de modificar
- 🔄 **Progreso incremental** - Guarda cada 10 preguntas
- 🌍 **5 idiomas adicionales** - EN, FR, BR, CN, GE

**Documentación completa:** [`docs/TRANSLATION_GUIDE.md`](docs/TRANSLATION_GUIDE.md)

### Sincronización con Formbricks
Para enviar las evaluaciones a tu instancia de Formbricks, ejecuta:
```bash
python src/sync_to_formbricks.py
```
Este script transformará los JSON maestros en encuestas listas para usar en tu VPS: `https://feedback.soul23.cloud`.

## 🛠️ Integración con Formbricks API

Este proyecto utiliza la [Management API de Formbricks](https://formbricks.com/docs/api-reference/management-api--survey/create-survey) para automatizar la creación de evaluaciones.

**Características de la integración:**
- **Localización Automática:** El script envuelve los textos en el formato `{"default": "..."}` requerido.
- **Estructura Dinámica:** Soporta preguntas de opción múltiple (`multipleChoiceSingle`) y texto abierto.
- **Pantallas Personalizadas:** Incluye automáticamente una *Welcome Card* y una *End Screen* profesional.

---

## 📂 Estructura del Repositorio

```text
/
├── docs/                              # Metodología y guías por nivel
│   ├── AGENTS.md                      # Definición de agentes IA
│   ├── RAZONAMIENTO_Y_PROPOSITO.md   # Justificación del proyecto
│   ├── metodology.md                  # Sistema de puntuación
│   ├── TRANSLATION_GUIDE.md          # ✨ Guía de traducción técnica
│   ├── PROJECT_STATUS.md             # ✨ Estado actual del proyecto
│   └── questions/                    # Markdown por nivel
├── formbricks/                        # JSONs listos para la API de Formbricks
├── master_assesment/                  # Fuente de verdad (JSON maestros)
│   └── json/
│       ├── basic_assesment.json      # ~180 preguntas Nivel 1
│       ├── medium_assesment.json     # ~175 preguntas Nivel 2
│       ├── advanced_assesment.json   # ~180 preguntas Nivel 3
│       └── funnel_registration.json  # Formulario de perfilamiento
├── src/                               # Scripts de automatización
│   ├── generate_docs.py              # Generador de documentación
│   ├── refactor_i18n.py              # Migración a multilingüe
│   ├── sync_to_formbricks.py         # Sincronización con Formbricks
│   ├── translate_assessments.py      # ✨ Preparador de estructura i18n
│   ├── translate_with_ai.py          # ✨ Traductor con IA (Gemini/OpenAI)
│   ├── test_translation.py           # ✨ Script de prueba de traducción
│   └── check_tasks.py                # ✨ Verificador de progreso del roadmap
├── .env.example                       # Plantilla de configuración
├── TASKS.md                           # Roadmap de desarrollo
└── Readme.md                          # Este archivo
```

---

## 📊 Ejemplos de Resultados

Un reporte de evaluación típico genera los siguientes outputs para análisis:

### Ejemplo de Output Individual
```json
{
  "candidato": "Tech_01",
  "nivel": "Nivel 2 - Medio",
  "score_total": 82.5,
  "resultado": "APROBADO",
  "breakdown": {
    "Seguridad": "100% (Excelente)",
    "Procesos": "65% (Requiere Atención)",
    "Defectos": "90% (Bueno)"
  },
  "recomendacion": "Reforzar capacitación en Variables de Proceso (VPT, Cojín)."
}
```

### Impacto Esperado (Antes vs. Después)
| Métrica | Antes del Training | 12 Meses Post-Training |
| :--- | :---: | :---: |
| **Nivel Promedio Equipo** | 45% (Básico) | 85% (Medio-Alto) |
| **Tiempo de Cambio (SMED)** | 45 min | 28 min |
| **Scrap Rate** | 3.5% | 1.8% |

---

## 📈 KPIs Relevantes

El éxito de este assessment se mide a través de indicadores de planta reales.

| KPI | Definición | Por qué importa |
| :--- | :--- | :--- |
| **OEE (Overall Equipment Effectiveness)** | Disponibilidad x Rendimiento x Calidad. | Indica la eficiencia real. Personal capacitado reduce paros menores. |
| **Scrap Rate** | (Piezas defectuosas / Total producidas) * 100. | Directamente relacionado con la habilidad de troubleshooting del técnico. |
| **Cycle Time Efficiency** | Tiempo ciclo real vs. Estándar. | El conocimiento avanzado permite optimizar el ciclo sin sacrificar calidad. |
| **MTTR (Mean Time To Repair)** | Tiempo promedio para solucionar una falla. | Técnicos competentes diagnostican la causa raíz más rápido. |
| **Skill Gap Index** | % de brecha entre el skill ideal y el real. | Métrica directa de RRHH para medir la efectividad del programa. |

---

## 🛠️ Herramientas de Desarrollo

Para facilitar el mantenimiento y la expansión del proyecto, se incluyen scripts de utilidad en la carpeta `src/`:

### Scripts Principales

*   **`src/check_tasks.py`**: ✨ **NUEVO** - Muestra progreso del roadmap con barras visuales y comandos sugeridos.
*   **`src/translate_with_ai.py`**: ✨ **NUEVO** - Traductor automático con IA (Gemini/OpenAI) con glosario técnico especializado.
*   **`src/test_translation.py`**: ✨ **NUEVO** - Prueba de traducción con muestra de 3 preguntas para validación.
*   **`src/generate_docs.py`**: Genera automáticamente los archivos Markdown de la carpeta `docs/questions/` a partir de los JSON maestros.
*   **`src/refactor_i18n.py`**: Herramienta utilizada para migrar la estructura de los JSONs al formato multilingüe.
*   **`src/sync_to_formbricks.py`**: Sincroniza las evaluaciones con la instancia de Formbricks.
*   **`src/translate_assessments.py`**: Preparador de estructura i18n sin traducción automática (para completar manualmente).

### Uso Rápido

```bash
# Ver estado del proyecto
python src/check_tasks.py

# Probar traducción
python src/test_translation.py

# Traducir evaluaciones
python src/translate_with_ai.py --lang en

# Generar documentación
python src/generate_docs.py
```

---

## 📚 Documentación Vinculada

Para profundizar en áreas específicas, consulta:

### Guías Principales

*   **[📊 Estado del Proyecto](docs/PROJECT_STATUS.md):** ✨ **NUEVO** - Análisis completo del progreso, métricas y próximos pasos.
*   **[🌍 Guía de Traducción](docs/TRANSLATION_GUIDE.md):** ✨ **NUEVO** - Manual completo de traducción multilingüe con glosario técnico.
*   **[📋 Roadmap de Tareas](TASKS.md):** Checklist de desarrollo por fases.

### Documentación Técnica

*   **[Metodología de Evaluación](docs/metodology.md):** Detalle del sistema de puntos (Score Teórico vs Práctico).
*   **[Agentes del Sistema](docs/AGENTS.md):** Definición de roles y agentes de IA para la expansión del proyecto.
*   **[Razonamiento y Propósito](docs/RAZONAMIENTO_Y_PROPOSITO.md):** El "Por qué" del proyecto.

### Contenido de Evaluaciones

*   **[Nivel 1 - Básico](docs/questions/LEVEL_1_BASIC_ASSESSMENT.md):** Temario para operadores (~180 preguntas).
*   **[Nivel 2 - Medio](docs/questions/LEVEL_2_MEDIUM_ASSESSMENT.md):** Temario para técnicos (~175 preguntas).
*   **[Nivel 3 - Avanzado](docs/questions/LEVEL_3_ADVANCED_ASSESSMENT.md):** Temario para ingeniería (~180 preguntas).

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas para mantener el banco de preguntas actualizado y relevante!

1.  **Fork** este repositorio.
2.  Crea una rama para tu feature (`git checkout -b feature/nueva-pregunta-nivel-2`).
3.  Agrega tus preguntas al JSON correspondiente siguiendo el esquema existente.
4.  Haz **Commit** de tus cambios.
5.  Abre un **Pull Request**.

Por favor, asegúrate de que las nuevas preguntas tengan una respuesta técnica verificable y un razonamiento claro.

---

## 👥 Créditos y Autores

Este proyecto ha sido posible gracias a la colaboración multidisciplinaria:

*   **Fortunato Salazar:** Idea original, diseño de cuestionarios y definición de métricas de evaluación.
*   **Marco Gallegos:** Optimización de cuestionarios, desarrollo del sistema de automatización (formas) y análisis de datos.

---

## ⚖️ Licencia y Ética

**Licencia:** Este proyecto se distribuye bajo la licencia MIT (o la que aplique al proyecto privado).
**Código de Conducta:** Se espera que todos los colaboradores mantengan un ambiente de respeto profesional. El objetivo es educar y mejorar, no juzgar.

---

## 🔄 Actualizaciones

*   **Última actualización:** 25 de Diciembre, 2025.
*   **Versión actual:** v2.1 (Sistema de Traducción Multilingüe con IA).
*   **Novedades:**
    - ✨ Sistema de traducción automática con IA (Gemini/OpenAI)
    - ✨ Soporte para 6 idiomas (ES, EN, FR, BR, CN, GE)
    - ✨ Glosario técnico especializado en moldeo por inyección
    - ✨ Scripts de verificación de progreso del roadmap
    - ✨ Guías completas de traducción y estado del proyecto
