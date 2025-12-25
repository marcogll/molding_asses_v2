# Guía del Assessment: Nivel Medio (Técnico de Ajuste)

## Objetivo
Evaluar la capacidad del personal para intervenir en el proceso, realizar montajes y solucionar problemas de calidad (Troubleshooting) utilizando lógica técnica y conocimiento de las variables de la máquina.

## Áreas Evaluadas
- **Máquina**: Ratio de intensificación, L/D, funcionamiento de bombas y válvulas check.
- **Procesos**: Tiempo de residencia, descompresión (suck back), cojín y transferencia (VPT).
- **Molde**: Enfriamiento, ángulos de salida, altura de molde y venteos.
- **Operaciones**: SMED básico, orden de arranque de canales calientes y SPC.

## Metodología de Evaluación
- **Total de preguntas**: 60.
- **Sistema de puntaje**: 
    - Preguntas Teóricas: 2.0 puntos.
    - Preguntas Prácticas: 2.5 puntos.
- **Puntaje Máximo Posible**: ~135 puntos.

### Resultado Mínimo Esperado (Passing Score)
Debido a que este personal tiene la autoridad para modificar parámetros, el estándar de aprobación es más riguroso: **80%**.

| Porcentaje | Estatus | Acción |
|------------|---------|--------|
| < 80% | No Aprobado | Restricción de acceso a menús de proceso en máquina. |
| 80% - 90% | Aprobado | Técnico de ajuste autorizado. |
| > 90% | Experto | Mentor de piso y candidato a Nivel Avanzado. |

---

## Banco de Preguntas

### [mach_1] Máquina (Teórico) - 2 pts
**¿Qué mide exactamente un termopar (thermocouple) en el barril de calefacción?**

*   La temperatura real del plástico fundido
*   La temperatura del metal del barril
*   La presión del aceite hidráulico
*   La temperatura del tornillo

> **Respuesta Correcta:** La temperatura del metal del barril
>
> **Razonamiento:** Los termopares están instalados en el acero del barril; la temperatura del plástico suele ser un poco distinta debido a la fricción interna (calor por cizalla).

### [mach_2] Máquina (Práctico) - 2.5 pts
**Si el ratio de intensificación (RI) es 10:1 y el manómetro hidráulico marca 1,000 PSI, ¿cuánta presión hay en la punta del tornillo?**

*   1,000 PSI
*   10,000 PSI
*   100 PSI
*   2,000 PSI

> **Respuesta Correcta:** 10,000 PSI
>
> **Razonamiento:** La presión del plástico es la presión hidráulica multiplicada por el Ratio de Intensificación de la máquina.

### [mach_3] Máquina (Práctico) - 2.5 pts
**Durante la fase de sostenimiento (hold), el tornillo sigue avanzando lentamente (creeping). ¿Cuál es la causa más probable?**

*   La temperatura de la boquilla es alta
*   La válvula check (anillo de cierre) tiene fugas
*   El molde está muy frío
*   La presión de inyección es demasiado alta

> **Respuesta Correcta:** La válvula check (anillo de cierre) tiene fugas
>
> **Razonamiento:** Si el anillo de cierre no sella bien, el plástico regresa hacia los filetes del tornillo, impidiendo que se mantenga una presión constante en la cavidad.

### [mach_4] Máquina (Teórico) - 2 pts
**¿Qué significa la relación L/D en un tornillo de inyección?**

*   Longitud total entre Diámetro del tornillo
*   Largo de la boquilla entre Diámetro de la tolva
*   Límite de Desgaste del acero
*   La relación entre el largo del barril y la distancia entre platinas

> **Respuesta Correcta:** Longitud total entre Diámetro del tornillo
>
> **Razonamiento:** Es una medida de la capacidad de mezclado y fundido; una relación mayor suele indicar una mejor homogenización del plástico.

### [mach_5] Máquina (Práctico) - 2.5 pts
**¿Cuál es la consecuencia de tener una temperatura demasiado alta en la garganta de alimentación (hopper throat)?**

*   El plástico se funde más rápido
*   Los pellets se pegan y forman un puente, impidiendo que el material baje
*   La pieza sale con más brillo
*   Los pellets fluyen mejor sin formar puentes

> **Respuesta Correcta:** Los pellets se pegan y forman un puente, impidiendo que el material baje
>
> **Razonamiento:** Si la garganta se calienta, el plástico comienza a ablandarse antes de entrar al tornillo, bloqueando el paso del material (bridging).

### [mach_6] Máquina (Teórico) - 2 pts
**En una máquina hidráulica, ¿qué componente es el encargado de suministrar el flujo de aceite?**

*   Las válvulas
*   La bomba
*   Los actuadores
*   Los sensores de temperatura

> **Respuesta Correcta:** La bomba
>
> **Razonamiento:** La bomba hidráulica convierte la energía mecánica del motor en flujo de aceite para mover todos los sistemas de la máquina.

### [mach_7] Máquina (Teórico) - 2 pts
**¿Cuál de estas platinas NO existe en una máquina de moldeo estándar?**

*   Platina fija
*   Platina móvil
*   Platina rotativa de expulsión
*   Una platina auxiliar

> **Respuesta Correcta:** Platina rotativa de expulsión
>
> **Razonamiento:** Las máquinas estándar tienen platina fija (lado inyección), móvil (lado cierre) y a veces una trasera de soporte (tailstock).

### [mach_8] Máquina (Práctico) - 2.5 pts
**Si cambias un termopar Tipo J por uno Tipo K en un controlador de canal caliente:**

*   No pasa nada, ambos miden igual
*   La lectura será errónea y causará problemas de proceso
*   El controlador se quemará instantáneamente
*   La lectura será más precisa automáticamente

> **Respuesta Correcta:** La lectura será errónea y causará problemas de proceso
>
> **Razonamiento:** Cada tipo de termopar genera un voltaje distinto por grado; el controlador leerá una temperatura que no es real.

### [molde_1] Molde (Teórico) - 2 pts
**¿Qué mitad del molde suele requerir más canales de enfriamiento?**

*   La mitad fija (cavidad)
*   La mitad móvil (corazón/core)
*   Ambas requieren exactamente lo mismo siempre
*   La mitad fija mantiene el calor más tiempo que la móvil

> **Respuesta Correcta:** La mitad móvil (corazón/core)
>
> **Razonamiento:** El plástico tiende a encogerse y abrazar el corazón (macho), por lo que el calor se queda atrapado ahí más tiempo.

### [molde_2] Molde (Teórico) - 2 pts
**¿Para qué sirve el ángulo de salida (draft angle) en las paredes del molde?**

*   Para que el plástico fluya mejor
*   Para facilitar la expulsión de la pieza sin que se raye o se pegue
*   Para que el molde se vea más profesional
*   Para amortiguar el impacto de los botadores al expulsar la pieza

> **Respuesta Correcta:** Para facilitar la expulsión de la pieza sin que se raye o se pegue
>
> **Razonamiento:** Sin ángulo de salida, la fricción entre el plástico y el acero impediría que los botadores saquen la pieza limpiamente.

### [molde_3] Molde (Práctico) - 2.5 pts
**Tienes un molde de 12 pulgadas de espesor y debe abrir 6 pulgadas para expulsar. ¿Cuál es la 'Luz de día' (daylight) mínima?**

*   12 pulgadas
*   18 pulgadas
*   24 pulgadas
*   30 pulgadas

> **Respuesta Correcta:** 18 pulgadas
>
> **Razonamiento:** La luz de día es la distancia total entre platinas; debe ser al menos el espesor del molde más la carrera de apertura.

### [molde_4] Molde (Teórico) - 2 pts
**¿Qué ventaja tiene un canal caliente (hot runner) frente a uno frío?**

*   Es más barato de fabricar
*   Reduce el tiempo de ciclo y elimina el desperdicio de colada
*   Usa menos electricidad
*   Es más fácil de fabricar

> **Respuesta Correcta:** Reduce el tiempo de ciclo y elimina el desperdicio de colada
>
> **Razonamiento:** Al no tener que enfriar y expulsar una colada gruesa, el ciclo es más rápido y se ahorra material.

### [molde_5] Molde (Práctico) - 2.5 pts
**Si un molde tiene 4 cavidades y una está bloqueada, ¿qué pasa con el tiempo de llenado?**

*   Se mantiene igual
*   Debe ajustarse, ya que el volumen de plástico ahora se reparte en menos cavidades
*   La máquina se detiene sola
*   El tiempo de ciclo se alarga sin cambio de perfil

> **Respuesta Correcta:** Debe ajustarse, ya que el volumen de plástico ahora se reparte en menos cavidades
>
> **Razonamiento:** Al haber menos espacio, la velocidad de llenado efectiva en las cavidades restantes cambia si no se ajusta el perfil.

### [molde_6] Molde (Práctico) - 2.5 pts
**¿Qué es la 'altura de molde' (die height) en la configuración de la máquina?**

*   La altura desde el piso hasta el molde
*   El espesor total del molde cerrado entre las platinas
*   La altura máxima a la que puede subir la grúa
*   La distancia desde la base hasta la cabeza de la máquina

> **Respuesta Correcta:** El espesor total del molde cerrado entre las platinas
>
> **Razonamiento:** Es un ajuste crítico para que la rodillera o el sistema hidráulico de cierre aplique la fuerza correcta.

### [molde_7] Molde (Teórico) - 2 pts
**¿Cuál es la función principal de los respiraderos (vents) en el molde?**

*   Dejar que entre aire para enfriar
*   Permitir que el aire atrapado salga mientras el plástico llena la cavidad
*   Lubricar los pernos extractores
*   Cerrar los respiraderos para retener más presión dentro del molde

> **Respuesta Correcta:** Permitir que el aire atrapado salga mientras el plástico llena la cavidad
>
> **Razonamiento:** Si el aire no sale, se comprime, causando quemaduras (quemado por gas) o tiros cortos.

### [molde_8] Molde (Práctico) - 2.5 pts
**¿Qué sucede si las mangueras de agua están conectadas 'en serie' en lugar de 'en paralelo' en un molde de muchas cavidades?**

*   Enfría mejor
*   Las últimas cavidades estarán más calientes que las primeras, causando piezas desiguales
*   Se ahorra agua
*   Las primeras cavidades se mantienen frías mientras las últimas se calientan

> **Respuesta Correcta:** Las últimas cavidades estarán más calientes que las primeras, causando piezas desiguales
>
> **Razonamiento:** El agua va absorbiendo calor; si pasa por muchas cavidades, al final ya no tiene capacidad de enfriar.

### [proc_1] Procesos (Teórico) - 2 pts
**¿Qué determina el punto de transferencia VPT (Velocity-to-Pressure)?**

*   Cuándo termina el llenado por velocidad y empieza la compactación por presión
*   La velocidad a la que se abre el molde
*   La temperatura de la boquilla
*   La presión de empaque

> **Respuesta Correcta:** Cuándo termina el llenado por velocidad y empieza la compactación por presión
>
> **Razonamiento:** Es el cambio de 'primera etapa' a 'segunda etapa'; crítico para evitar rebabas o tiros cortos.

### [proc_10] Procesos (Práctico) - 2.5 pts
**Para convertir 350 Bar a PSI aproximadamente:**

*   3500 PSI
*   5075 PSI
*   2400 PSI
*   4,000 PSI

> **Respuesta Correcta:** 5075 PSI
>
> **Razonamiento:** 1 Bar equivale a aproximadamente 14.5 PSI (350 x 14.5 = 5075).

### [proc_2] Procesos (Práctico) - 2.5 pts
**¿Cómo debe ser el 'cojín' (cushion) ideal en un proceso científico robusto?**

*   Cero (que el tornillo llegue al fondo)
*   Pequeño pero constante (ej. 5mm a 10mm), nunca llegando a cero
*   Lo más grande posible
*   Que el tornillo toque el fondo para asegurar la presión

> **Respuesta Correcta:** Pequeño pero constante (ej. 5mm a 10mm), nunca llegando a cero
>
> **Razonamiento:** Si el cojín llega a cero, la máquina no puede aplicar presión de sostenimiento a la pieza.

### [proc_3] Procesos (Teórico) - 2 pts
**¿Qué mide el tiempo de sellado de la compuerta (gate freeze time)?**

*   Cuánto tarda el molde en abrir
*   El tiempo necesario para que el plástico en la entrada se solidifique y no regrese
*   El tiempo de inyección
*   El tiempo que el molde tarda en abrir después de expulsar la pieza

> **Respuesta Correcta:** El tiempo necesario para que el plástico en la entrada se solidifique y no regrese
>
> **Razonamiento:** Una vez sellada la compuerta, aumentar el tiempo de hold ya no afecta el peso de la pieza.

### [proc_4] Procesos (Práctico) - 2.5 pts
**Si aumentas la contrapresión (back pressure) durante la dosificación:**

*   El tornillo carga más rápido
*   Mejora la mezcla y fundido, pero aumenta el desgaste y el tiempo de carga
*   La pieza sale con rebaba
*   Disminuye el tiempo de ciclo

> **Respuesta Correcta:** Mejora la mezcla y fundido, pero aumenta el desgaste y el tiempo de carga
>
> **Razonamiento:** La contrapresión obliga al tornillo a trabajar más para fundir el plástico, eliminando burbujas de aire y mejorando el color.

### [proc_5] Procesos (Práctico) - 2.5 pts
**¿Cuál es la forma más rápida de subir la temperatura del plástico fundido sin tocar las resistencias?**

*   Bajar la velocidad de inyección
*   Aumentar la velocidad de rotación del tornillo o la contrapresión
*   Cerrar las mangueras de agua
*   Incrementar la presión de cierre para calentar el plástico

> **Respuesta Correcta:** Aumentar la velocidad de rotación del tornillo o la contrapresión
>
> **Razonamiento:** Genera más fricción mecánica (cizallamiento), lo cual calienta el plástico desde adentro.

### [proc_6] Procesos (Teórico) - 2 pts
**¿Qué variable controla el llenado de la cavidad en la 'primera etapa'?**

*   Presión
*   Velocidad (Flujo)
*   Tiempo de enfriamiento
*   Temperatura de fundido

> **Respuesta Correcta:** Velocidad (Flujo)
>
> **Razonamiento:** En el moldeo científico, la primera etapa debe ser controlada por velocidad para asegurar un llenado uniforme.

### [proc_7] Procesos (Práctico) - 2.5 pts
**En un estudio de viscosidad, si duplicas la velocidad de inyección y la presión no sube casi nada, el material es:**

*   Muy viscoso
*   No-Newtoniano (adelgazamiento por cizalla)
*   Newtoniano (como el agua)
*   Está en zona de flujo laminar

> **Respuesta Correcta:** No-Newtoniano (adelgazamiento por cizalla)
>
> **Razonamiento:** Los plásticos fluyen más fácil entre más rápido se empujen; esto permite inyectar piezas complejas.

### [proc_8] Procesos (Práctico) - 2.5 pts
**¿Para qué sirve el temporizador de retardo del tornillo (screw delay)?**

*   Para que el operador descanse
*   Para permitir que el tornillo empiece a cargar solo después de que el plástico en la boquilla haya enfriado un poco
*   Para retrasar la inyección
*   Para evitar que el tornillo cargue mientras el molde aún está abierto

> **Respuesta Correcta:** Para permitir que el tornillo empiece a cargar solo después de que el plástico en la boquilla haya enfriado un poco
>
> **Razonamiento:** Ayuda a prevenir el goteo de la boquilla (drooling) al final del ciclo.

### [proc_9] Procesos (Teórico) - 2 pts
**¿En qué etapa del proceso el polímero encuentra la presión más alta?**

*   Inyección (1ra etapa)
*   Empaque/Packing (2da etapa)
*   Dosificación
*   Secado del material

> **Respuesta Correcta:** Empaque/Packing (2da etapa)
>
> **Razonamiento:** Durante el empaque se aplica la presión final para compactar el material dentro de un molde ya lleno.

### [cal_1] Calidad (Práctico) - 2.5 pts
**¿Cuál es la causa más común de las burbujas de aire (air bubbles) en piezas transparentes?**

*   Molde muy frío
*   Atrapamiento de aire durante la dosificación o inyección muy rápida
*   Baja temperatura de fundido
*   La presión de empaque es demasiado alta

> **Respuesta Correcta:** Atrapamiento de aire durante la dosificación o inyección muy rápida
>
> **Razonamiento:** A diferencia de los vacíos por contracción, las burbujas de aire suelen venir del proceso de plastificación o llenado turbulento.

### [cal_2] Calidad (Práctico) - 2.5 pts
**Aparecen 'manchas plateadas' (splay) repentinamente. Revisas el secador y está apagado. Esto confirma que el defecto es causado por:**

*   Degradación térmica
*   Humedad en el material
*   Presión de inyección alta
*   Contaminación con lubricante en el barril

> **Respuesta Correcta:** Humedad en el material
>
> **Razonamiento:** El splay es el síntoma clásico de humedad que se convierte en vapor dentro del barril.

### [cal_3] Calidad (Práctico) - 2.5 pts
**Si una pieza tiene 'rechupes' (sink marks), ¿cuál de estos cambios es el más efectivo?**

*   Aumentar el tiempo o la presión de sostenimiento (hold)
*   Inyectar más rápido
*   Bajar la contrapresión
*   Abrir la válvula de ventilación

> **Respuesta Correcta:** Aumentar el tiempo o la presión de sostenimiento (hold)
>
> **Razonamiento:** El rechupe ocurre porque no entró suficiente plástico para compensar la contracción mientras la pieza enfriaba.

### [cal_4] Calidad (Teórico) - 2 pts
**¿Qué defecto causa el fenómeno llamado 'Jetting'?**

*   El plástico entra como un chorro serpenteante sin tocar las paredes del molde
*   El plástico se quema en la boquilla
*   La pieza se pega en el corazón
*   El plástico se pega en las paredes con exceso de presión

> **Respuesta Correcta:** El plástico entra como un chorro serpenteante sin tocar las paredes del molde
>
> **Razonamiento:** Ocurre cuando la velocidad de inyección es muy alta al pasar por una compuerta pequeña hacia un área grande.

### [cal_5] Calidad (Práctico) - 2.5 pts
**Al dejar una pieza caliente sobre una mesa de metal fría, esta se dobla hacia arriba. Esto se debe a:**

*   Gravedad
*   Enfriamiento desigual (la cara contra la mesa enfrió más rápido que la cara al aire)
*   El material es de mala calidad
*   La humedad del aire es alta

> **Respuesta Correcta:** Enfriamiento desigual (la cara contra la mesa enfrió más rápido que la cara al aire)
>
> **Razonamiento:** La cara que enfría rápido 'tira' del resto de la pieza, causando una deformación por tensiones térmicas.

### [cal_6] Calidad (Teórico) - 2 pts
**¿Qué es una 'veta de color' en la pieza?**

*   Una línea causada por el molde rayado
*   Mala mezcla del pigmento o concentrado de color en el barril
*   Exceso de enfriamiento
*   El molde estaba perfectamente alineado

> **Respuesta Correcta:** Mala mezcla del pigmento o concentrado de color en el barril
>
> **Razonamiento:** Indica que el tornillo no está homogeneizando bien el pigmento con la resina base.

### [cal_7] Calidad (Práctico) - 2.5 pts
**¿Cómo se distingue un 'vacío' (void) de una 'burbuja de aire'?**

*   No se pueden distinguir
*   El vacío desaparece si calientas la pieza (es contracción); la burbuja se expande
*   La burbuja es siempre más grande
*   El vacío se mantiene sin responder al calor

> **Respuesta Correcta:** El vacío desaparece si calientas la pieza (es contracción); la burbuja se expande
>
> **Razonamiento:** El vacío es un hueco por falta de presión (física); la burbuja contiene gas atrapado.

### [cal_8] Calidad (Práctico) - 2.5 pts
**Detectas 'splay' y sospechas que es por degradación térmica. ¿Cómo lo compruebas?**

*   Haciendo un purga al aire y oliendo si el gas es picante o el color está amarillento
*   Subiendo más la temperatura
*   Pesando la pieza
*   Reducir la velocidad de inyección y revisar si desaparecen las manchas

> **Respuesta Correcta:** Haciendo un purga al aire y oliendo si el gas es picante o el color está amarillento
>
> **Razonamiento:** El plástico quemado cambia de color y desprende un olor fuerte a gas químico.

### [cal_9] Calidad (Práctico) - 2.5 pts
**¿Cómo se llama la temperatura en la que las piezas ya no sufren deformación al ser expulsadas?**

*   Temperatura de fundido
*   Temperatura de deflexión térmica (HDT)
*   Temperatura de expulsión segura
*   Temperatura de solidificación parcial

> **Respuesta Correcta:** Temperatura de deflexión térmica (HDT)
>
> **Razonamiento:** Es el punto donde el material tiene suficiente integridad estructural para resistir la fuerza de los botadores sin deformarse.

### [seg_1] Seguridad (Práctico) - 2.5 pts
**¿Por qué es peligroso dejar la boquilla contra el molde cuando la máquina no está operando?**

*   Se puede rayar el bebedero
*   El calor de la boquilla puede degradar el plástico atrapado o calentar el molde innecesariamente
*   La boquilla se puede enfriar demasiado
*   Enfriar la boquilla con spray mientras la máquina está apagada

> **Respuesta Correcta:** El calor de la boquilla puede degradar el plástico atrapado o calentar el molde innecesariamente
>
> **Razonamiento:** Mantener el contacto térmico degrada el plástico en la punta y puede generar gases peligrosos o taponamientos.

### [seg_2] Seguridad (Práctico) - 2.5 pts
**¿Qué indican las señales de LOTO (Bloqueo/Etiquetado) en una máquina?**

*   Que la máquina está lista para producir
*   Que hay energías peligrosas (eléctrica, presión, mecánica) aisladas por mantenimiento
*   Que el molde es nuevo
*   Que la máquina está en mantenimiento programado

> **Respuesta Correcta:** Que hay energías peligrosas (eléctrica, presión, mecánica) aisladas por mantenimiento
>
> **Razonamiento:** Es el procedimiento de seguridad vital para asegurar que nadie encienda la máquina mientras alguien trabaja en ella.

### [seg_3] Seguridad (Práctico) - 2.5 pts
**Al purgar materiales como el POM (Acetal) después de un PVC, ¿qué precaución es crítica?**

*   Usar guantes de seda
*   No mezclarlos nunca, ya que pueden reaccionar químicamente y causar una explosión de gas en el barril
*   Bajar la presión de inyección al mínimo
*   Aplicar aire comprimido al barril para ventilar los gases

> **Respuesta Correcta:** No mezclarlos nunca, ya que pueden reaccionar químicamente y causar una explosión de gas en el barril
>
> **Razonamiento:** Ciertos plásticos son químicamente incompatibles y generan gases tóxicos o presión explosiva si se juntan en el barril caliente.

### [seg_4] Seguridad (Práctico) - 2.5 pts
**Si escuchas un ruido metálico fuerte en la unidad de cierre, debes:**

*   Subir el tonelaje
*   Presionar Paro de Emergencia e investigar antes de que el molde se dañe
*   Esperar a que termine el turno
*   Reducir el voltaje de la máquina

> **Respuesta Correcta:** Presionar Paro de Emergencia e investigar antes de que el molde se dañe
>
> **Razonamiento:** Cualquier ruido inusual indica una falla mecánica que puede causar un accidente o daño catastrófico al molde.

### [seg_5] Seguridad (Práctico) - 2.5 pts
**¿Cuál es la forma correcta de manejar un molde suspendido por una grúa?**

*   Empujarlo con las manos por debajo
*   Mantenerse fuera del área de caída y usar cuerdas guía si es necesario
*   Sujetarse del cáncamo de izaje
*   Mover el molde con las manos por debajo

> **Respuesta Correcta:** Mantenerse fuera del área de caída y usar cuerdas guía si es necesario
>
> **Razonamiento:** Nunca se debe estar debajo de una carga suspendida por riesgo de falla del equipo de izaje.

### [plast_1] Plásticos (Teórico) - 2 pts
**¿Qué sucede con las moléculas de un plástico cristalino (ej. Nylon) cuando se enfrían muy lento?**

*   Se vuelven desordenadas
*   Tienen tiempo de formar cristales más grandes, aumentando la rigidez
*   Se degradan por el calor
*   Las moléculas se vuelven más flexibles aunque se enfríen lento

> **Respuesta Correcta:** Tienen tiempo de formar cristales más grandes, aumentando la rigidez
>
> **Razonamiento:** El grado de cristalinidad depende directamente de la tasa de enfriamiento; enfriar lento permite mayor orden molecular.

### [plast_2] Plásticos (Teórico) - 2 pts
**¿Qué propiedad del plástico se ve afectada principalmente por la longitud de sus cadenas (peso molecular)?**

*   Solo el color
*   La resistencia mecánica y la viscosidad
*   La transparencia
*   La densidad

> **Respuesta Correcta:** La resistencia mecánica y la viscosidad
>
> **Razonamiento:** Cadenas más largas se enredan más, aumentando la resistencia del material y dificultando su flujo (mayor viscosidad).

### [plast_3] Plásticos (Teórico) - 2 pts
**¿Cuál es la definición correcta de 'Polimerización'?**

*   El acto de moler plástico usado
*   Unir moléculas cortas (monómeros) para formar cadenas largas (polímeros)
*   Enfriar el plástico en el molde
*   Mezclar resinas diferentes

> **Respuesta Correcta:** Unir moléculas cortas (monómeros) para formar cadenas largas (polímeros)
>
> **Razonamiento:** Es el proceso químico de creación del plástico a partir de sus componentes básicos.

### [plast_4] Plásticos (Práctico) - 2.5 pts
**Si comparamos un plástico Amorfo y uno Cristalino, ¿cuál suele encogerse (shrinkage) más al enfriarse?**

*   El Amorfo
*   El Cristalino
*   Ambos encogen igual
*   El plástico amorfo se vuelve más transparente

> **Respuesta Correcta:** El Cristalino
>
> **Razonamiento:** Las moléculas cristalinas se ordenan y empaquetan más juntas al enfriarse, ocupando menos espacio.

### [plast_5] Plásticos (Teórico) - 2 pts
**¿Qué mide un viscosímetro o reómetro capilar?**

*   La dureza del plástico sólido
*   La resistencia del plástico fundido a fluir bajo presión
*   La cantidad de humedad en el pellet
*   La conductividad térmica del plástico

> **Respuesta Correcta:** La resistencia del plástico fundido a fluir bajo presión
>
> **Razonamiento:** Mide la viscosidad, que es el parámetro clave para entender cómo llenará el plástico el molde.

### [plast_6] Plásticos (Teórico) - 2 pts
**¿A qué temperatura se considera que un plástico amorfo pasa de un estado rígido a uno gomoso?**

*   Punto de fusión (Tm)
*   Temperatura de transición vítrea (Tg)
*   Punto de ebullición
*   Temperatura de flujo

> **Respuesta Correcta:** Temperatura de transición vítrea (Tg)
>
> **Razonamiento:** En los amorfos, la Tg marca el cambio de comportamiento estructural antes de fluir por completo.

### [plast_7] Plásticos (Práctico) - 2.5 pts
**¿Quién desarrolló comercialmente el Nylon por primera vez?**

*   BASF
*   DuPont
*   SABIC
*   Ineos

> **Respuesta Correcta:** DuPont
>
> **Razonamiento:** DuPont es históricamente el pionero en la creación y comercialización de la poliamida (Nylon).

### [op_1] Operaciones (Práctico) - 2.5 pts
**¿Cuál es el propósito del 'tiempo de reposo térmico' (heat soak) en un canal caliente?**

*   Ahorrar luz
*   Permitir que todo el acero del sistema alcance la temperatura uniforme para evitar fugas y roturas
*   Calentar el molde más rápido
*   Dejar las resistencias apagadas para ahorrar energía antes del ciclo

> **Respuesta Correcta:** Permitir que todo el acero del sistema alcance la temperatura uniforme para evitar fugas y roturas
>
> **Razonamiento:** Los componentes se expanden con el calor; si inyectas antes de que todo esté dilatado, el plástico puede fugar por las uniones.

### [op_2] Operaciones (Práctico) - 2.5 pts
**¿En qué modo se debe realizar un 'air shot' (disparo al aire) para verificar el material?**

*   Automático
*   Manual
*   Semiautomático
*   Semiautomático con la puerta abierta

> **Respuesta Correcta:** Manual
>
> **Razonamiento:** Permite al operador controlar el disparo de forma segura mientras observa la calidad del fundido fuera del molde.

### [op_3] Operaciones (Práctico) - 2.5 pts
**¿Qué orden de encendido es el más seguro para un molde de canal caliente?**

*   Todo al mismo tiempo
*   Manifold primero, luego las boquillas y al final el bebedero (si aplica)
*   Boquillas primero para que no se tapen
*   Encender primero el bebedero y luego el manifold con la máquina caliente

> **Respuesta Correcta:** Manifold primero, luego las boquillas y al final el bebedero (si aplica)
>
> **Razonamiento:** Asegura que el plástico tenga una ruta abierta desde el centro hacia afuera antes de aplicar presión.

### [op_4] Operaciones (Práctico) - 2.5 pts
**Si la máquina se detiene por una falla eléctrica por más de 30 minutos con material degradable (ej. PVC) en el barril, ¿qué debes hacer?**

*   Esperar a que regrese la luz e inyectar
*   Purgar el barril inmediatamente con un material de limpieza o estable en cuanto haya energía
*   No hacer nada
*   Esperar a que el material degrade por sí solo

> **Respuesta Correcta:** Purgar el barril inmediatamente con un material de limpieza o estable en cuanto haya energía
>
> **Razonamiento:** El calor estático degrada el material, lo que puede corroer el barril o causar gases tóxicos.

### [op_5] Operaciones (Teórico) - 2 pts
**¿Qué significa SPC en el entorno de moldeo?**

*   Sistema de Presión Constante
*   Control Estadístico de Procesos
*   Seguridad de Plásticos Críticos
*   Planificación de Seguridad de Cambios

> **Respuesta Correcta:** Control Estadístico de Procesos
>
> **Razonamiento:** Es la metodología para monitorear las variables del proceso y asegurar que las piezas se mantengan en tolerancia.

### [op_6] Operaciones (Práctico) - 2.5 pts
**Al purgar el barril, notas que el plástico sale con burbujas y hace ruido de 'explosiones' pequeñas. Esto indica:**

*   Demasiada presión de inyección
*   Humedad excesiva en el material
*   El tornillo está roto
*   El barril está demasiado frío para evaporar la humedad

> **Respuesta Correcta:** Humedad excesiva en el material
>
> **Razonamiento:** El agua atrapada se evapora instantáneamente al salir a la presión atmosférica, causando ese sonido y burbujas.

### [op_7] Operaciones (Práctico) - 2.5 pts
**Un molde de 4 cavidades con ciclo de 27 segundos debe producir 3,500 piezas. ¿Cuántas horas tardará?**

*   10.35 horas
*   6.56 horas
*   4.56 horas
*   5.25 horas

> **Respuesta Correcta:** 6.56 horas
>
> **Razonamiento:** 4 piezas cada 27 seg = 0.148 piezas/seg. 3500 / 0.148 = 23,648 segundos / 3600 = 6.56 horas.

### [desp_1] Desperdicios (Práctico) - 2.5 pts
**¿Qué efecto tiene usar demasiada descompresión (suck back)?**

*   La pieza sale más pesada
*   Puede succionar aire al barril, causando burbujas o manchas de quemado
*   Ahorra tiempo de ciclo
*   Reduce la presión de empaque

> **Respuesta Correcta:** Puede succionar aire al barril, causando burbujas o manchas de quemado
>
> **Razonamiento:** Retraer demasiado el tornillo mete aire a la zona de fundido, el cual se mezcla con el plástico y causa defectos.

### [desp_2] Desperdicios (Teórico) - 2 pts
**¿Qué es el 'tiempo de residencia'?**

*   El tiempo que el operador tarda en su descanso
*   El tiempo total que el plástico pasa dentro del barril caliente
*   El tiempo que la pieza dura en el molde
*   La contaminación solo afecta el color y se corrige con más presión

> **Respuesta Correcta:** El tiempo total que el plástico pasa dentro del barril caliente
>
> **Razonamiento:** Si el tiempo de residencia es muy largo, el calor degrada las cadenas químicas del plástico, arruinando sus propiedades.

### [desp_3] Desperdicios (Práctico) - 2.5 pts
**Si trabajas con un barril muy grande para una pieza muy pequeña, el principal riesgo es:**

*   Que la máquina no tenga fuerza
*   Degradación del plástico por exceso de tiempo de residencia
*   Que el molde no cierre
*   El costo del material baja por la purga

> **Respuesta Correcta:** Degradación del plástico por exceso de tiempo de residencia
>
> **Razonamiento:** El material tarda muchos ciclos en salir, exponiéndose al calor por demasiado tiempo.

### [desp_4] Desperdicios (Práctico) - 2.5 pts
**¿Cuál es la forma más eficiente de purgar para un cambio de color de negro a blanco?**

*   Inyectar 50 disparos de blanco
*   Limpiar físicamente el tornillo o usar un compuesto de purga especializado
*   Bajar la temperatura
*   Inyectar hasta que el color se iguale sin purgar

> **Respuesta Correcta:** Limpiar físicamente el tornillo o usar un compuesto de purga especializado
>
> **Razonamiento:** Usar solo resina virgen gasta mucho material y tiempo; los compuestos de purga 'arrastran' mejor los residuos.

### [desp_5] Desperdicios (Teórico) - 2 pts
**¿Qué sucede si el porcentaje de material recuperado (regrind) es demasiado alto?**

*   La pieza se vuelve irrompible
*   Se pierden propiedades mecánicas y el proceso se vuelve inestable
*   No pasa nada, es puro ahorro
*   La pieza se vuelve más resistente gracias al regrind

> **Respuesta Correcta:** Se pierden propiedades mecánicas y el proceso se vuelve inestable
>
> **Razonamiento:** El plástico se debilita cada vez que se funde; demasiado regrind afecta la calidad final.

### [desp_6] Desperdicios (Práctico) - 2.5 pts
**Si un operador tira las coladas al suelo y se llenan de polvo, ¿pueden recuperarse?**

*   Sí, el filtro las limpia
*   No, la contaminación externa arruinará las piezas nuevas y puede tapar compuertas
*   Sí, si se lavan con agua
*   Sí, si se lavan con solvente

> **Respuesta Correcta:** No, la contaminación externa arruinará las piezas nuevas y puede tapar compuertas
>
> **Razonamiento:** El regrind debe estar tan limpio como el material virgen para no comprometer el proceso.

