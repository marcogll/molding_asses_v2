# Agentes del Proyecto Code Carol

Este documento define los agentes especializados (IA o roles humanos) necesarios para ejecutar la siguiente fase de expansión del proyecto **Code Carol**.

## 1. Agente Arquitecto de Sistema (System Architect)
**Objetivo:** Diseñar la infraestructura escalable del Web Server y la base de datos.
- **Responsabilidades:**
    - Definir el esquema de base de datos (SQL/NoSQL) para usuarios, resultados y mapeo de encuestas.
    - Diseñar la arquitectura de la API (REST/GraphQL) para el enrutamiento de encuestas.
    - Seleccionar el stack tecnológico (ej. FastAPI/Django + PostgreSQL).
- **Herramientas:** Diagramas ER, Docker, Python.

## 2. Agente Lingüista Internacional (Polyglot Content Dev)
**Objetivo:** Transformar el contenido monolingüe a una estructura multilingüe robusta.
- **Responsabilidades:**
    - Refactorizar los JSONs maestros para soportar internacionalización (i18n).
    - Traducir y localizar técnicamente las preguntas a: Inglés (EN), Francés (FR), Portugués (BR), Chino (CN) y Alemán (GE).
    - Asegurar que los términos técnicos de moldeo sean precisos en cada idioma.
- **Herramientas:** Herramientas de traducción asistida, JSON, Glosarios técnicos de inyección.

## 3. Agente de Lógica de Negocio (Funnel Logic Expert)
**Objetivo:** Desarrollar el algoritmo de asignación de evaluaciones.
- **Responsabilidades:**
    - Crear la lógica que decide qué encuesta asignar basada en los datos del "Funnel" (Años de exp + Autoevaluación + Puesto).
    - Ejemplo: Si *Autoevaluación < 30%* y *Exp < 1 año* → Asignar Nivel Básico.
    - Implementar el cuestionario de perfilamiento (`funnel_registration.json`).

## 4. Agente Desarrollador Full-Stack (Web Server Dev)
**Objetivo:** Implementar el servidor y la interfaz de usuario.
- **Responsabilidades:**
    - Codificar el backend para manejar registros y sesiones.
    - Crear una interfaz web (Frontend) simple y responsiva para el registro de participantes.
    - Integrar la API de Formbricks o desarrollar un motor de encuestas nativo si es necesario para el soporte multilingüe dinámico.

## 5. Agente Analista de Datos (Data Scientist)
**Objetivo:** Estructurar la salida de datos para análisis predictivo.
- **Responsabilidades:**
    - Diseñar los dashboards de comparación (Percepción vs. Realidad).
    - Crear reportes automáticos de brechas de habilidades (Skill Gap Analysis).
