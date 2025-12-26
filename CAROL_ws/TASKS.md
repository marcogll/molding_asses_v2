# TASKS.md: Próximos Pasos para el Desarrollo de CAROL-ws

Este archivo define las tareas de desarrollo pendientes para implementar la funcionalidad de `CAROL-ws`.

## Fase 1: Configuración Inicial y Validación del Empleado

-   [x] **Tarea 1.1: Configurar el servidor Express básico.**
    -   Crear el archivo `src/index.js`.
    -   Importar `express` y `dotenv`.
    -   Configurar el servidor para que escuche en el puerto definido en `.env`.
    -   Añadir un endpoint de prueba (ej. `/health`) que devuelva un estado `200 OK`.

-   [x] **Tarea 1.2: Añadir endpoint para obtener encuestas de Formbricks.**
    -   Añadir `axios` como dependencia.
    -   Crear `src/services/formbricksService.js` para obtener las encuestas.
    -   Crear `src/controllers/surveyController.js` y `src/routes/surveyRoutes.js`.
    -   Exponer un endpoint GET `/api/surveys` que devuelva la lista de encuestas.

-   [ ] **Tarea 1.3: Implementar el servicio de validación de empleados.**
    -   Crear el archivo `src/services/employeeService.js`.
    -   Crear una función `validateEmployee(employeeId)` que:
        -   Lea el archivo `data/employees.csv` usando `csv-parser`.
        -   Busque el `employee_id` proporcionado.
        -   Devuelva los datos del empleado si se encuentra y está activo, o `null` en caso contrario.
    -   **Nota:** Asegúrate de manejar la lectura asíncrona del archivo CSV.

-   [ ] **Tarea 1.3: Crear la ruta y el controlador de la evaluación.**
    -   Crear el archivo de rutas `src/routes/assessmentRoutes.js`.
    -   Definir una ruta GET `/assessment/:employeeId`.
    -   Crear el archivo del controlador `src/controllers/assessmentController.js`.
    -   Implementar una función en el controlador que:
        -   Obtenga el `employeeId` de los parámetros de la ruta.
        -   Llame a `employeeService.validateEmployee()`.
        -   Si el empleado no es válido, responda con un error 404 o una página de "Acceso denegado".
        -   Si es válido, continúe con la siguiente fase.

## Fase 2: Lógica de Asignación y Renderizado de la Encuesta

-   [ ] **Tarea 2.1: Desarrollar la lógica para determinar la encuesta.**
    -   En `assessmentController.js`, después de validar al empleado, implementar la lógica para decidir qué `survey_id` de Formbricks se debe mostrar.
    -   Por ahora, esta lógica puede ser simple (ej. un mapeo basado en el `role` del empleado).

-   [ ] **Tarea 2.2: Crear la vista para mostrar la encuesta.**
    -   Crear un archivo HTML simple en `src/views/assessment.html`.
    -   Este archivo debe incluir un contenedor (`<div>`) donde se montará la encuesta de Formbricks.
    -   Añadir un script que pueda recibir dinámicamente el `survey_id` y el `employee_id`.

-   [ ] **Tarea 2.3: Renderizar la encuesta de Formbricks.**
    -   Modificar el controlador `assessmentController.js` para que, en caso de una validación exitosa:
        -   Renderice la vista `assessment.html`.
        -   Pase el `survey_id` y el `employee_id` a la vista para que el script de Formbricks pueda inicializarse con los datos correctos.
    -   **Importante:** El `FORMBRICKS_URL` y el `FORMBRICKS_ENVIRONMENT_ID` del archivo `.env` serán necesarios para construir el script de embed.

## Fase 3: Finalización y Pruebas

-   [ ] **Tarea 3.1: Añadir manejo de errores.**
    -   Asegurarse de que todas las rutas y servicios manejen adecuadamente los errores (ej. archivo CSV no encontrado, errores de lectura).
    -   Implementar un middleware de manejo de errores en `src/index.js`.

-   [ ] **Tarea 3.2: Realizar pruebas manuales del flujo completo.**
    -   Crear un archivo `data/employees.csv` de prueba.
    -   Iniciar el servidor.
    -   Acceder a la URL `/assessment/:employeeId` con un ID válido y uno inválido para verificar el comportamiento.
    -   Confirmar que el embed de Formbricks se muestra correctamente para un empleado válido.

-   [ ] **Tarea 3.3: Limpieza del código y documentación.**
    -   Añadir comentarios al código donde sea necesario.
    -   Revisar que el código siga las convenciones definidas en `AGENTS.md`.
    -   Actualizar el `README.md` con instrucciones sobre cómo ejecutar el proyecto.
