# Code Carol

> **Hub de evaluación integral para medir, estandarizar y potenciar el conocimiento técnico en moldeo por inyección.**
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
*   Instancia de Formbricks activa (VPS).
*   Variables de entorno configuradas (`.env`).

### Instalación
1. Clonar el repositorio.
2. Instalar dependencias:
   ```bash
   pip install requests python-dotenv
   ```
3. Configurar tu `.env` basándote en `.env.example`.

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
├── docs/                           # Metodología y guías por nivel
├── formbricks/                     # JSONs listos para la API de Formbricks
├── master_assesment/               # Fuente de verdad de las preguntas (Scoring y Razonamiento)
├── src/
│   └── sync_to_formbricks.py       # Script de carga a la API
├── .env.example                    # Plantilla de configuración
└── Readme.md                       # Este archivo
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

## 📚 Documentación Vinculada

Para profundizar en áreas específicas, consulta:

*   **[Metodología de Evaluación](docs/metodology.md):** Detalle del sistema de puntos (Score Teórico vs Práctico).
*   **[Nivel 1 - Básico](docs/questions/LEVEL_1_BASIC_ASSESSMENT.md):** Temario para operadores.
*   **[Nivel 2 - Medio](docs/questions/LEVEL_2_MEDIUM_ASSESSMENT.md):** Temario para técnicos.
*   **[Nivel 3 - Avanzado](docs/questions/LEVEL_3_ADVANCED_ASSESSMENT.md):** Temario para ingeniería.
*   **[Razonamiento y Propósito](docs/RAZONAMIENTO_Y_PROPOSITO.md):** El "Por qué" del proyecto.

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
*   **Versión actual:** v2.0 (Estructura JSON y Guías Markdown completas).