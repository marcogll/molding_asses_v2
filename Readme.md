# Molding Assessment Framework (Automotive & Related)

## 1. Introducción y Propósito

Este proyecto define un **Framework Multi-nivel de Evaluación** orientado a estandarizar y medir objetivamente el conocimiento técnico en procesos de **moldeo por inyección**. Su finalidad principal no es solo calificar, sino diagnosticar el "punto de partida real" del equipo para operar, solucionar problemas y optimizar procesos de manufactura.

### ¿Por qué es vital este Assessment?
Basado en la documentación de `RAZONAMIENTO_Y_PROPOSITO.md`, este framework aborda problemas críticos de la industria:

*   **Estandarización Operativa:** Elimina el "moldeo por sentimiento", asegurando que todos los turnos operen bajo principios científicos.
*   **Reducción de Costos:** Un personal competente detecta la causa raíz de defectos (scrap) y evita ajustes innecesarios.
*   **Seguridad:** Evalúa conocimientos críticos (LOTO, protección de moldes) para prevenir accidentes y daños a herramentales costosos.
*   **Upskilling Dirigido:** Permite diseñar planes de capacitación basados en datos reales (brechas detectadas) en lugar de suposiciones.

---

## 2. Estructura del Framework (Niveles)

El sistema se divide en tres niveles progresivos, diseñados para diferentes roles dentro de la planta.

### 🟢 Nivel 1: Básico (Operaciones de Piso)
*   **Objetivo:** Evaluar el conocimiento fundamental para operar una máquina de forma segura y productiva.
*   **Perfil:** Operadores de producción.
*   **Enfoque:**
    *   Partes de la máquina (Tolva, Barril, Boquilla).
    *   Seguridad (Reglas de oro, Paros de emergencia).
    *   Identificación visual de defectos (Tiro corto, Rebaba).
*   **Aprobación:** Mínimo **75%**.

### 🟡 Nivel 2: Medio (Técnico de Ajuste)
*   **Objetivo:** Evaluar la capacidad para realizar montajes, arranques de máquina y solucionar problemas (Troubleshooting) con lógica técnica.
*   **Perfil:** Técnicos de montaje, Técnicos de proceso junior.
*   **Enfoque:**
    *   Variables de proceso (Tiempo de residencia, VPT, Cojín).
    *   Funcionamiento de válvulas check y bombas.
    *   Moldes (Enfriamiento, Venteos).
*   **Aprobación:** Mínimo **80%** (Mayor rigor por tener autoridad sobre parámetros).

### 🔴 Nivel 3: Avanzado (Ingeniería de Procesos)
*   **Objetivo:** Validar el dominio del **Moldeo Científico**, reología y optimización avanzada.
*   **Perfil:** Ingenieros de Proceso, Líderes de Planta, Especialistas.
*   **Enfoque:**
    *   Reología (Viscosidad no-newtoniana, Shear rate).
    *   Curvas de viscosidad y balance de cavidades.
    *   Análisis estadístico (CPK) y Diseño de Herramental.
*   **Aprobación:** Mínimo **80%** (Excelencia técnica requerida).

---

## 3. Metodología Técnica

El núcleo del assessment reside en su estructura de datos y sistema de puntuación ponderado, diseñado para dar más valor a la resolución de problemas prácticos y al conocimiento avanzado.

### Archivos de Datos (JSON)
Las preguntas se almacenan en archivos JSON estructurados por nivel en la carpeta `master_assesment/json/`:
*   `basic_assesment.json` (~50 preguntas)
*   `medium_assesment.json` (~60 preguntas)
*   `advanced_assesment.json` (~60 preguntas)

### Categorías de Evaluación
El conocimiento se desglosa en áreas clave para permitir un análisis granular:
*   Máquina
*   Plásticos (Materiales)
*   Seguridad
*   Molde
*   Calidad
*   Operaciones
*   Desperdicios
*   Procesos

### Sistema de Puntuación (Scoring System)
Cada pregunta tiene un valor `est_score` (estimated score) que varía según la dificultad y el tipo de conocimiento. Se premia más la capacidad **Práctica** (saber hacer/resolver) que la **Teórica** (saber el concepto).

| Nivel | Puntos (Teórico) | Puntos (Práctico) |
| :--- | :---: | :---: |
| **Básico** | 1.0 | 1.5 |
| **Medio** | 2.0 | 2.5 |
| **Avanzado** | 3.0 | 3.5 |

**Fórmula de Cálculo:**
> `Score Total = Σ (est_score de respuestas correctas)`

Esto significa que un error en una pregunta práctica avanzada penaliza más el score final que un error en una teoría básica.

---

## 4. Datos y Analítica (Data Science)

Para científicos de datos o desarrolladores que integren este framework, el procesamiento de los JSON sigue este esquema.

### Estructura del Objeto de Pregunta
```json
{
  "id": "unique_id",
  "categoria": "Máquina",
  "tipo": "Práctico",
  "pregunta": "¿Qué sucede si...?",
  "respuestas": ["Opción A", "Opción B", "Opción C"],
  "respuesta_correcta": "Opción B",
  "razonamiento": "Explicación técnica del porqué...",
  "est_score": 2.5
}
```

### Métricas Clave a Extraer
Al procesar los resultados, se deben generar las siguientes métricas para aportar valor al negocio:
1.  **Score Global y Porcentaje:** (Puntos obtenidos / Puntos posibles).
2.  **Breakdown por Categoría:** Identificar si un técnico es fuerte en "Máquina" pero débil en "Plásticos".
3.  **Brecha Teórico-Práctica:** Comparar el desempeño en preguntas tipo `Teórico` vs `Práctico`.
4.  **Evolución:** Comparar resultados Pre-Training vs Post-Training (Re-assessment).

---

## 5. Uso de Resultados

El resultado del assessment no debe ser punitivo. Su uso correcto es:

1.  **Diagnóstico:** Crear una "Línea Base" del conocimiento actual de la planta.
2.  **Plan de Acción:**
    *   Si el fallo es en **Seguridad**: Paro y re-entrenamiento inmediato.
    *   Si el fallo es en **Proceso**: Asignación de mentoría técnica.
3.  **Validación:** Evaluar la efectividad del entrenamiento 12 meses después, correlacionando con KPIs operativos (Scrap, OEE).

---

## 6. Conclusión

Este framework transforma la capacitación técnica de un "gasto genérico" a una **inversión estratégica basada en datos**. Al medir con precisión el nivel de competencia (Básico a Ingeniería), las plantas de inyección pueden asegurar procesos más estables, seguros y rentables.

