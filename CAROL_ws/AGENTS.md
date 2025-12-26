# AGENTS.md: Guía para el desarrollo de CAROL-ws

Este documento proporciona directrices y convenciones para los agentes de IA que trabajen en el proyecto `CAROL-ws`.

## 1. Stack Tecnológico

-   **Lenguaje:** JavaScript (ES6+)
-   **Entorno de ejecución:** Node.js
-   **Framework principal:** Express.js
-   **Gestor de paquetes:** npm
-   **Variables de entorno:** `dotenv`

## 2. Arquitectura del Proyecto

El proyecto sigue una arquitectura modular para separar responsabilidades.

-   `src/`: Contiene todo el código fuente de la aplicación.
-   `src/index.js`: Punto de entrada principal de la aplicación. Aquí se configura e inicia el servidor Express.
-   `src/routes/`: Define las rutas de la API. Cada archivo corresponde a un recurso principal (ej. `employees.js`). Su única responsabilidad es recibir la petición HTTP y llamar al controlador correspondiente.
-   `src/controllers/`: Contiene la lógica de negocio para cada ruta. Los controladores procesan la petición, llaman a los servicios necesarios y envían la respuesta al cliente. No deben contener lógica de acceso a datos directa.
-   `src/services/`: Alberga la lógica de negocio más compleja y reutilizable, como la validación de empleados contra el CSV o la interacción con APIs externas.
-   `src/views/`: Contiene las plantillas o archivos HTML para renderizar las vistas. Para este proyecto, su uso principal será mostrar el embed de la encuesta de Formbricks.
-   `data/`: Almacena archivos de datos estáticos, como el CSV de empleados.

## 3. Flujo de la Petición

1.  El cliente (navegador) hace una petición a una URL.
2.  El servidor Express en `src/index.js` recibe la petición.
3.  La petición es dirigida al **enrutador** correspondiente en `src/routes/`.
4.  El enrutador invoca a la función del **controlador** asociada en `src/controllers/`.
5.  El controlador utiliza los **servicios** de `src/services/` para realizar las operaciones necesarias (ej. buscar empleado en el CSV).
6.  El controlador renderiza una **vista** de `src/views/` o envía una respuesta JSON.

## 4. Tarea Principal: Validación y Despliegue de Encuesta

El flujo principal a implementar es:

1.  **Recepción del `employee_id`:** El servidor debe exponer una ruta, por ejemplo, `/assessment/:employee_id`.
2.  **Validación del empleado:**
    -   Utilizar el servicio de validación (`src/services/employeeService.js`).
    -   Este servicio leerá el archivo `data/employees.csv`.
    -   Verificará si el `employee_id` existe y está activo.
    -   Si no es válido, mostrar una página de error.
3.  **Determinación de la encuesta:**
    -   Basado en los datos del empleado en el CSV (rol, área, etc.), determinar qué `survey_id` de Formbricks le corresponde.
4.  **Renderizado del embed:**
    -   Renderizar una vista (`src/views/assessment.html` o similar).
    -   Incrustar el snippet de JavaScript de Formbricks en esa vista, pasando el `employee_id` y el `survey_id` como parámetros.

## 5. Gestión de Dependencias

-   Utiliza `npm` para instalar dependencias.
-   Añade las dependencias de producción con `npm install <package>`.
-   Añade las dependencias de desarrollo (ej. `nodemon`) con `npm install <package> --save-dev`.

## 6. Variables de Entorno

-   Todas las claves, URLs de API y configuraciones sensibles deben estar en el archivo `.env` en la raíz del proyecto (`CAROL_ws/.env`).
-   Nunca subas el archivo `.env` al repositorio. Ya está incluido en `.gitignore`.
-   Utiliza el paquete `dotenv` para cargar estas variables.

## 7. Pruebas

-   Aunque no se ha configurado un framework de pruebas, el código debe escribirse de forma que sea testable. Separa la lógica de negocio en los servicios para facilitar las pruebas unitarias en el futuro.

Al seguir estas directrices, aseguraremos un desarrollo coherente y mantenible del proyecto `CAROL-ws`.
