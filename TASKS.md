# Roadmap de Tareas: Code Carol (Fase de Expansión)

Este archivo detalla las tareas secuenciales para evolucionar Code Carol hacia una plataforma multilingüe y gestionada por servidor web.

## Fase 1: Estructura de Datos y Perfilamiento

- [x] **1.1. Refactorización de JSONs Maestros (i18n)**
    - [x] Modificar la estructura JSON actual: De `{"pregunta": "Texto"}` a `{"question": {"es": "Texto", "en": "Text", ...}}`.
    - [x] Actualizar los scripts de generación de documentación (`generate_docs.py`) para leer el nuevo formato.
    
- [x] **1.2. Desarrollo del 'Funnel' de Registro**
    - [x] Crear `master_assesment/json/funnel_registration.json`.
    - [x] Definir campos: Nombre, No. Empleado, Departamento, Puesto, Autoevaluación (%), Años de Experiencia.
    - [x] Validar tipos de datos (Select, Slider, Input).

## Fase 2: Localización y Contenido Multilingüe

- [ ] **2.1. Traducción Técnica (EN - Inglés)**
    - [ ] Traducir Nivel 1, 2 y 3.
    - [ ] Validar terminología técnica (ej. "Short Shot", "Sink Mark").
    
- [ ] **2.2. Traducción Técnica (FR - Francés)**
    - [ ] Traducir banco de preguntas.
    
- [ ] **2.3. Traducción Técnica (BR - Portugués)**
    - [ ] Traducir banco de preguntas.
    
- [ ] **2.4. Traducción Técnica (CN - Chino Simplificado)**
    - [ ] Traducir banco de preguntas.
    
- [ ] **2.5. Traducción Técnica (GE - Alemán)**
    - [ ] Traducir banco de preguntas.

## Fase 3: Desarrollo del Web Server (Backend & Logic)

- [x] **3.1. Setup del Servidor**
    - [x] Inicializar proyecto (Node.js/Express).
    - [ ] Configurar base de datos (SQLite para dev, PostgreSQL para prod).
    
- [ ] **3.2. Implementación de Modelos de Base de Datos**
    - [ ] Tabla `Participants`: (ID, Nombre, Dept, Rol, Exp, Self_Eval).
    - [ ] Tabla `Assessments`: (ID, Idioma, JSON_Ref).
    - [ ] Tabla `Results`: (Participant_ID, Assessment_ID, Score, Breakdown).

- [ ] **3.3. Lógica de Enrutamiento (The Funnel Engine)**
    - [ ] Implementar algoritmo de decisión:
        - *Input:* Puesto + Años Exp + Self Eval.
        - *Output:* ID de la evaluación asignada (Básica, Media o Avanzada).

- [ ] **3.4. API Endpoints**
    - [ ] `POST /register`: Recibe datos del funnel.
    - [ ] `GET /assessment/{id}`: Entrega el JSON de la evaluación en el idioma solicitado.
    - [ ] `POST /submit`: Recibe respuestas y calcula score.

## Fase 4: Frontend e Interfaz de Usuario

- [ ] **4.1. Interfaz de Registro (Landing Page)**
    - [ ] Formulario dinámico basado en `funnel_registration.json`.
    - [ ] Selector de Idioma (Global).

- [ ] **4.2. Interfaz de Evaluación**
    - [ ] Renderizador de preguntas (aprovechando el formato JSON actualizado).
    - [ ] Feedback visual.

## Fase 5: Despliegue y Documentación

- [ ] **5.1. Dockerización**
    - [ ] Crear `Dockerfile` y `docker-compose.yml`.
    
- [ ] **5.2. Actualización de Documentación**
    - [ ] Actualizar `Readme.md` con instrucciones de despliegue del servidor.