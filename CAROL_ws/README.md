# CAROL-ws

## Assessment Gateway Web Server

---

### Propósito

CAROL-ws es el web server gateway del proyecto Molding Assessment. Su función es orquestar el acceso, asignación y recolección de assessments de conocimiento técnico en moldeo por inyección utilizando Formbricks como motor de encuestas.

CAROL-ws no evalúa, no califica y no entrena. Solo mide y enruta.

El flujo está diseñado para:

- Medir conocimiento base (baseline)
- Definir planes de capacitación fuera del sistema
- Volver a medir después (ej. 12 meses)
- Comparar resultados contra KPIs reales de planta

---

### Rol dentro del repositorio

```
molding_assesment_v2/
├── docs/                # Metodología y razonamiento
├── formbricks/          # Surveys listos para importar
├── master_assesment/    # Estructura lógica de preguntas
├── CAROL_ws/            # Gateway web (este módulo)
└── src/                 # Scripts auxiliares
```

CAROL-ws es el único componente expuesto a usuarios finales.

---

### Qué hace CAROL-ws

- Identifica empleados por `employee_id`
- Valida empleados contra una lista cargada (CSV)
- Determina qué assessments debe presentar cada empleado
- Presenta encuestas vía:
  - Website & App Survey (Formbricks embed)
  - Redirect
- Recibe resultados vía Webhooks de Formbricks
- Persiste resultados para análisis longitudinal

---

### Qué NO hace

- No renderiza preguntas
- No calcula scores complejos
- No asigna capacitación
- No es LMS
- No genera dashboards

---

### Arquitectura

```
Empleado
   ↓
CAROL-ws
   ↓
Formbricks Web Survey
   ↓
Formbricks Webhook
   ↓
CAROL-ws Backend
   ↓
Base de datos / KPIs
```

---

### Integración con Formbricks

CAROL-ws se integra con:

- Formbricks Management API (referencia de surveys)
- Website & App Surveys (presentación)
- Webhooks (recolección de respuestas)

Las encuestas se crean y mantienen fuera de este servidor.

---

### Variables de entorno

Archivo .env (ubicado en la raíz del proyecto, `CAROL_ws/.env`):

```
FORMBRICKS_URL=https://feedback.soul23.cloud
FORMBRICKS_API_KEY=your_api_key_here
FORMBRICKS_ENVIRONMENT_ID=your_environment_id

APP_ENV=production
PORT=8000
HOST=0.0.0.0
```

---

### Modelo de datos mínimo

**Employees**

- `employee_id`
- `plant`
- `area`
- `role`
- `active`

**Assignments**

- `employee_id`
- `survey_id`
- `status`
- `assigned_at`
- `completed_at`

**Results**

- `employee_id`
- `survey_id`
- `score`
- `raw_payload`
- `timestamp`

---

### Flujo operativo

1. Se importa un CSV de empleados
2. El empleado accede con su `employee_id`
3. CAROL-ws asigna assessments según reglas
4. El usuario responde surveys en Formbricks
5. Formbricks envía resultados vía webhook
6. CAROL-ws almacena datos para comparación futura

---

### Enfoque

Medir primero. Capacitar después. Volver a medir con datos.

CAROL-ws existe para hacer visible el conocimiento operativo real.
