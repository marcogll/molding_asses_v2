# Guía de Evaluación del Assessment (Code Carol)

## Descripción General
Este documento describe la metodología de evaluación para el sistema **Code Carol**. Las evaluaciones miden el conocimiento y las habilidades del personal en procesos de moldeo por inyección a través de preguntas de opción múltiple organizadas en diferentes niveles de dificultad.

## Estructura del Assessment

### Datos Maestros (JSON)
Estos archivos contienen la "fuente de verdad", incluyendo las preguntas, respuestas correctas, razonamientos técnicos y valores de puntuación. Se utilizan para el procesamiento automatizado y la sincronización con la API.
- `master_assesment/json/basic_assesment.json`: Datos maestros del Nivel Básico.
- `master_assesment/json/medium_assesment.json`: Datos maestros del Nivel Medio.
- `master_assesment/json/advanced_assesment.json`: Datos maestros del Nivel Avanzado.

### Guías de Estudio (Markdown)
Versiones limpias de las evaluaciones destinadas al estudio o revisión manual. Incluyen las preguntas y opciones, pero **excluyen** las respuestas correctas y el razonamiento para permitir su distribución.
- `docs/questions/LEVEL_1_BASIC_ASSESSMENT.md`: Guía del Nivel Básico.
- `docs/questions/LEVEL_2_MEDIUM_ASSESSMENT.md`: Guía del Nivel Medio.
- `docs/questions/LEVEL_3_ADVANCED_ASSESSMENT.md`: Guía del Nivel Avanzado.

### Categorías de Evaluación
- **Máquina**: Hardware, componentes y funciones de la inyectora.
- **Plásticos**: Propiedades químicas, reología y comportamiento de polímeros.
- **Seguridad**: Protocolos LOTO, resguardos y prevención de accidentes.
- **Molde**: Componentes del herramental, enfriamiento y mecánica del molde.
- **Calidad**: Identificación y solución de defectos estéticos y estructurales.
- **Operaciones**: Modos de operación, SMED y tiempos de ciclo.
- **Desperdicios (Waste)**: Gestión de scrap, purgas y eficiencia de material.
- **Procesos**: Variables de inyección, empaque, enfriamiento y moldeo científico.

## Método de Puntuación

### Valor por Pregunta (est_score)
Cada pregunta tiene un valor asignado basado en su nivel y tipo:

| Nivel | Teórica | Práctica |
|-------|---------|----------|
| Básico | 1.0 | 1.5 |
| Medio | 2.0 | 2.5 |
| Avanzado | 3.0 | 3.5 |

- **Teórica**: Evalúa el conocimiento conceptual y técnico.
- **Práctica**: Evalúa la aplicación de criterios para resolver problemas en piso o cálculos de ingeniería.

### Cálculo del Puntaje Total
El puntaje final es la suma de los valores (`est_score`) de todas las respuestas correctas.

**Fórmula:**
```
Puntaje Total = Σ(est_score de respuestas correctas)
```

### Puntajes Máximos Estimados
- **Básico**: 50 preguntas → ~62.5 puntos.
- **Medio**: 60 preguntas → ~135 puntos.
- **Avanzado**: 60 preguntas → ~195 puntos.

## Proceso de Evaluación

1. **Presentación**: Las preguntas se presentan en orden aleatorio (vía API) para asegurar la integridad de la prueba.
2. **Selección**: El usuario selecciona una opción de las disponibles.
3. **Retroalimentación**: El sistema muestra el razonamiento técnico después de cada respuesta (si se configura el modo aprendizaje).
4. **Reporte Final**: Se genera un porcentaje de aciertos y un desglose por categoría.

## Racional de Ponderación
- **Niveles**: El incremento de puntos en niveles avanzados refleja la mayor responsabilidad y experiencia requerida.
- **Ajuste por Tipo**: Las preguntas prácticas reciben +0.5 puntos adicionales por requerir análisis de situaciones reales, lo cual se considera de mayor complejidad que la teoría pura.

## Procesamiento de Datos para Analistas

### Formato de Datos
Cada archivo JSON sigue este esquema:

```json
{
  "id": "id_unico_pregunta",
  "categoria": "Categoría",
  "tipo": "Teórico|Práctico",
  "pregunta": "Texto de la pregunta",
  "respuestas": ["Opción A", "Opción B", "Opción C"],
  "respuesta_correcta": "Opción Correcta",
  "razonamiento": "Explicación técnica",
  "est_score": 1.0
}
```

### Métricas Clave para Análisis
- **Puntaje de competencia general**: Capacidad técnica global.
- **Fortalezas/Debilidades por Categoría**: Identifica si el gap está en seguridad, procesos, etc.
- **Desempeño Teórico vs. Práctico**: Determina si el evaluado tiene la base técnica o la habilidad de aplicación.
- **Progreso de Aprendizaje**: Evolución del score tras periodos de capacitación.
