---
curso: FUNDOPS
titulo: F6-S9 Balance de Línea (versión 3)
slides: 34
fuente: F6-S9 Balance de Línea (versión 3).pdf
---

## Slide 1

Portada decorativa (foto edificio UTEC, logo UTEC). Título "FUNDAMENTOS DE OPERACIONES" / subtítulo "Semana 9 - Balance de Línea".

## Slide 2

Slide "Índice:" con foto decorativa de fondo (estructura de concreto). Lista numerada:
1. Capacidad
2. Tiempo de Flujo (Flow Time)
3. Mano de Obra y Tiempo Ocioso
4. Balance de Línea
5. Incremento de Capacidad

## Slide 3

Slide "Objetivos:" con foto decorativa de fondo. Texto: "Al finalizar esta sesión, deberás ser capaz de:"
1. Calcular tiempos de operaciones, costos de mano de obra e indicadores de aprovechamiento de recursos.
2. Determinar una eficiente distribución de tareas y tiempos de actividades.
3. Generar estrategias para incrementar la capacidad de procesos en operaciones.

## Slide 4

Título "CASO NOVACRUZ" (resaltado cian/negro, se repite como encabezado en varias slides siguientes).

Texto: Novacruz es una empresa que fabrica scooters de alta gama. La demanda no era más de 100 scooters/semana a inicios de marzo, creció dramáticamente hasta 1,200 unidades/semana en el otoño.

Imágenes:
- Foto en blanco y negro de un scooter "Xootr" (patineta plegable con manubrio en T).
- Gráfico de líneas "FIGURE 4.2 Lifecycle Demand Trajectory for Xootrs": eje Y "Weekly Demand" de 0 a 1,400, eje X meses de March a January. La curva parte plana (~100-150) en March-May, sube progresivamente entre June-September (~300 a 900), llega a un pico cercano a 1,300 en October, y luego cae abruptamente a ~150-200 entre November-January.

Cita: "Obtained from 'Matching Supply with Demand', Author: Gerard Cachon, 3rd Edition, Chapter 4".

## Slide 5

Slide separadora de sección: "1. Capacidad" sobre foto decorativa de concreto (misma serie visual de separadores del curso).

## Slide 6

CASO NOVACRUZ. Texto: La fabricación consta de 3 procesos de ensamble, en cada proceso trabaja un operario (resaltado en amarillo).
- Actividad 1: 13 min/scooter — ensamblar horquilla, soporte de dirección y mango en T.
- Actividad 2: 11 min/scooter — ensamblar rueda, freno y partes del mecanismo de dirección.
- Actividad 3: 8 min/scooter — limpiar, aplicar calcomanías/cinta de agarre, prueba funcional final.

Diagrama de flujo de proceso: triángulo "Components" → flecha → caja "Activity 1" → triángulo pequeño (buffer) → caja "Activity 2" → triángulo pequeño (buffer) → caja "Activity 3" → flecha → triángulo "Finished Xootrs".

## Slide 7

CASO NOVACRUZ. Texto: cada proceso se ejecuta en un tiempo de procesamiento/servicio.

Fórmulas (resaltadas en rojo):
```
Capacidad del Proceso = Capacidad de 1 Recurso * Número de Recursos
Capacidad del Recurso = 1/Tiempo de Procesamiento
Capacidad del Proceso = Número de Recursos/Tiempo de Procesamiento
```
Recuadro con fórmula en inglés: Capacity = Number of resources / Processing time.

Ejemplo Actividad 1: Capacity = 1/(13 minutes/scooter) = 0.0769 scooter/minute → ×60 min/hora = 4.6 scooters/hora.

Tabla:
| Actividad | Tiempo de Procesamiento (min/scooter) | Capacidad (scooters/hora) |
|---|---|---|
| 1 | 13 | 4.6 |
| 2 | 11 | 5.45 |
| 3 | 8 | 7.5 |

## Slide 8

Slide separadora de sección: "2. Tiempo de flujo (Flow Time)" sobre foto decorativa.

## Slide 9

CASO NOVACRUZ. Formato de preguntas y respuestas (fondo gris oscuro para la pregunta, gris claro para la respuesta):
- ¿En cuánto tiempo se terminará de producir la primera unidad si no hay inventario inicial? → En la suma de los tiempos de procesamiento de cada proceso.
- ¿Cuánto tiempo pasa cada unidad a través de todo el proceso? → Suma de tiempos de procesamiento en cada proceso más los tiempos de espera.
- ¿Qué es la tasa de flujo/ritmo de producción/throughput? → Número de unidades producidas de producto terminado por unidad de tiempo.
- ¿Qué proceso determina el ritmo de producción cuando hay demanda y materia prima en exceso? → La capacidad del cuello de botella.
- ¿Qué es el tiempo de ciclo o cadencia de producción? → Tiempo entre 2 unidades consecutivas de producto terminado, igual al tiempo de procesamiento del cuello de botella.

Tabla repetida (Actividad/Tiempo de Procesamiento/Capacidad) superpuesta parcialmente sobre la última pregunta, mismos valores 13/4.6, 11/5.45, 8/7.5.

## Slide 10

CASO NOVACRUZ.
- El tiempo necesario para producir una unidad cuando no hay inventario:
Fórmula (roja): Tiempo para Producir la 1ª Unidad = Σ(i=1 a n) t_i
Cálculo: Tiempo 1° scooter = 13 + 11 + 8 = 32 min
- Si el flujo es continuo (máquinas):
Fórmula (roja): Tiempo en el Sistema = Tiempo de Flujo (Flow Time) = Tiempo de Ciclo x Nro. Estaciones
Cálculo: Tiempo de flujo (Flow Time) = 3 x 13 = 39 min

Tabla repetida (Actividad/Tiempo de Procesamiento/Capacidad): 1-13-4.6, 2-11-5.45, 3-8-7.5.

## Slide 11

CASO NOVACRUZ. Recuadro de texto: "A partir de la segunda unidad, el tiempo entre unidades producidas consecutivamente es igual al tiempo de procesamiento del cuello de botella, por lo que el ritmo de producción es igual al ritmo del cuello de botella" (captura de texto, fuente serif, estilo distinto al resto — parece screenshot de un libro/documento).

Fórmula (roja): Tasa de Flujo (Flow Rate) o Ritmo de Producción = Ritmo del Cuello de Botella

Fórmula del tiempo total de producción de X unidades cuando no hay inventario (en rojo):
```
Tiempo Total de Producción de X unidades =
Tiempo para Producir la 1ª Unidad + (X – 1)*Tiempo de Ciclo =
Tiempo para Producir la 1ª Unidad + (X – 1)*Cadencia de Producción =
Tiempo para Producir la 1ª Unidad + (X – 1)/Ritmo de Producción
```
Ejemplo (en celeste): Tiempo Total de Producción de 100 unidades = 32 + (100-1) x 13 = 1,319 min

## Slide 12

Slide separadora de sección: "3. Mano de Obra y Tiempo Ocioso" sobre foto decorativa.

## Slide 13

CASO NOVACRUZ. Captura de texto (estilo screenshot, fuente serif azul): "El costo de mano de obra directa se calcula dividiendo el salario total entre el número de unidades producidas".

Fórmula (roja): Costo M.O. Directa Unitario = Salario Total/Número de Unidades Producidas

Texto: el tiempo ocioso es el tiempo inactivo de un operario, debido a que su tiempo de procesamiento es menor que el tiempo de procesamiento del cuello de botella (tiempo de ciclo).

Fórmula (roja):
```
Tiempo Ocioso de 1 Operario por Unidad =
    Tiempo de Ciclo – Tiempo de Procesamiento del Operario
```

## Slide 14

CASO NOVACRUZ. Captura de texto (screenshot estilo libro, azul):
"El tiempo ocioso total cuando hay un operario se calcula de la siguiente forma:"

Fórmula (roja): Tiempo Ocioso Total de un Operario = Número de Unidades Producidas * (Tiempo de Ciclo – Tiempo de Procesamiento del Proceso)

Texto: "El tiempo inactivo de todos los operarios en un mismo recurso i es:"
Fórmula (roja): Tiempo Ocioso Total_i = (Tiempo de Ciclo_i – Tiempo de Procesamiento_i) * Nro. Operarios_i

Texto: "La tasa de flujo (Flow Rate) es el menor valor entre la disponibilidad de la materia prima que ingresa al sistema, la demanda y la capacidad del proceso:"
Fórmula (roja): Tasa de Flujo = min{Disponibilidad de MP, Demanda, Capacidad}

## Slide 15

CASO NOVACRUZ. Captura de texto (screenshot, azul): "El tiempo de ciclo es el tiempo entre 2 unidades consecutivas producidas:"

Fórmula (roja): Tiempo de Ciclo = 1/Tasa de Flujo o Ritmo de Producción

Texto: "El porcentaje de utilización de la mano de obra se calcula así:"
Fórmula (roja): % Utilización de M.O. = M.O./(M.O. + Tiempo Ocioso)

## Slide 16

CASO NOVACRUZ. Enunciado (captura tipo libro, azul): "Si se trabajan 35 horas semanales, la demanda semanal de scooters es igual a 125 unidades, en cada proceso trabaja un operario y el salario es igual a 12 $/hora, calcular el costo de mano de obra directa."

Tabla (arriba derecha): Actividad / Tiempo de Procesamiento (min/scooter) / Capacidad (scooters/hora): 1-13-4.6, 2-11-5.45, 3-8-7.5.

Columna izquierda "Sin considerar la Demanda":
- Tiempo de ciclo = 13 min/scooter (resaltado naranja)
- Semanalmente se podría producir = (35 hrs x 60 min)/13 min = 161 unid/semana (resaltado amarillo)

"Considerando una demanda: 125 unid/semana" (resaltado amarillo):
- Fórmula: Tiempo de Ciclo = 1/Tasa de Flujo o Ritmo de Producción
- Tiempo de Ciclo = 1/125 unid/sem = (35 hr x 60 min)/125 unid = 16.8 min (resaltado naranja)
- Fórmula: Costo M.O. Directa Unitario = Salario Total/Número de Unidades Producidas
- Costo de M.O. Directa = (3 x $12/hr x 35 hr/sem)/(125 unid/sem) = 10.08 $/unid

Columna derecha:
- Recuadro rojo: Tiempo Ocioso de 1 Operario por Unidad = Tiempo de Ciclo – Tiempo de Procesamiento del Operario
- T. Ocioso de 1 Operario por Unidad = (16.8-13)+(16.8-11)+(16.8-8) = 18.4 min/unid
- M.O. Efectiva por unidad = 13+11+8 = 32 min
- Recuadro rojo: % Utilización de M.O. = M.O./(M.O. + Tiempo Ocioso)
- Utilización de M.O. = 32/(32+18.4) = 63.5%

## Slide 17

CASO NOVACRUZ. "Número de Horas Laborables = 35 horas/semana". Tabla comparativa completa:

| | Operario 1 | Operario 2 | Operario 3 |
|---|---|---|---|
| Tiempo de Procesamiento | 13 min/unidad | 11 min/unidad | 8 min/unidad |
| Capacidad de Cada Proceso | 1/13 = 4.61 unid/hora | 1/11 = 5.45 unid/hora | 1/8 = 7.5 unid/hora |
| Capacidad del Proceso de Producción | 161 unidades/semana = 4.61 unidades/hora (celda combinada) |
| Demanda | 125 unidades/semana = 3.57 unidades/hora (celda combinada) |
| Ritmo de Producción o Tasa de Flujo (Flow Rate) | Min(Demanda, Capacidad del Proceso) = 3.57 unidades/hora (celda combinada) |
| Tiempo de Ciclo (Cadencia) | 1/(3.57 unidades/hora) = 16.8 minutos/unidad (celda combinada) |
| Tiempo de Inactividad | 16.8-13=3.8 min/unidad | 16.8-11=5.8 min/unidad | 16.8-8=8.8 min/unidad |
| %Utilización | 3.57/4.61=77.44% | 3.57/5.45=65.5% | 3.57/7.5=47.6% |

## Slide 18

Slide separadora de sección: "4. Balance de Línea" sobre foto decorativa.

## Slide 19

CASO NOVACRUZ. Tabla: Actividad/Tiempo de Procesamiento/Capacidad: 1-13-4.6, 2-11-5.45, 3-8-7.5.

Texto: "Existe un desbalance entre los 3 procesos, para reducir el desbalance se puede incrementar la capacidad de procesamiento de las siguientes formas" (resaltado amarillo en las dos opciones):
- Incrementar la capacidad del proceso reasignando operarios desde los recursos subutilizados hacia el cuello de botella.
- Incrementar la capacidad del proceso reasignando trabajo del cuello de botella a los recursos subutilizados.

Texto: "Si la demanda cambia a 200 unidades semanales, no va a ser posible satisfacer la demanda debido a que en una semana solamente se pueden producir 161 unidades."

## Slide 20

CASO NOVACRUZ. Tabla "Task Duration" (screenshot estilo libro) con detalle de tareas por trabajador:
- Worker 1: Prepare cable(30), Move cable(25), Assemble washer(100), Apply fork/threading cable end(66), Assemble socket head screws(114), Steer pin nut(49), Brake shoe/spring/pivot bolt(66), Insert front wheel(100), Insert axle bolt(30), Tighten axle bolt(43), Tighten brake pivot bolt(51), Assemble handle cap(118). Total: 792.
- Worker 2: Assemble brake lever and cable(110), Trim and cap cable(59), Place first rib(33), Insert axles and cleats(96), Insert rear wheel(135), Place second rib and deck(84), Apply grip tape(56), Insert deck fasteners(75). Total: 648.
- Worker 3: Inspect and wipe off(95), Apply decal and sticker(20), Insert in bag(43), Assemble carton(114), Insert Xootr and manual(94), Seal carton(84). Total: 450.

Gráfico de barras apiladas "Cycle Time before Line Balancing": eje Y "Processing Time [Seconds]" 0-900, 3 columnas (Step 1, Step 2, Step 3) formadas por segmentos numerados 1-26 apilados. Step 1 llega a ~792 (segmentos 1-12), Step 2 a ~648 (segmentos 13-20), Step 3 a ~450 (segmentos 21-26). Anotaciones con líneas indican qué número corresponde a cada segmento (1,2,3...12 en Step1; 13...20 en Step2; 21...26 en Step3).

## Slide 21

CASO NOVACRUZ. Texto: "Debido a que el tiempo empleado por cada operario para realizar las actividades asignadas para una unidad está desbalanceado, se deben reasignar actividades de un operario a otro considerando la secuencia de producción."

Texto (rojo, destacado): "El balance ideal se puede lograr si el tiempo total empleado se divide entre los 3 operarios por igual: (792+648+450)/3 = 1,890/3 = 630 segundos"

Texto: "Lo que se debe hacer es asignar a cada operario una cantidad de tiempo que sea lo más cercana a 630 segundos y luego calcular el porcentaje de utilización."

## Slide 22

CASO NOVACRUZ. Texto: "La mejor asignación posible es la siguiente:"
- Al operario 1 le restamos las 2 últimas tareas y las asignamos al operario 2: Tiempo de Ciclo 1 = 792 – 51 – 118 = 623 segundos
- Al operario 2 le restamos las 3 últimas tareas y las asignamos al operario 3: Tiempo de Ciclo 2 = 648 + 51 + 118 – 84 – 56 – 75 = 602 segundos; Tiempo de Ciclo 3 = 450 + 84 + 56 + 75 = 665 segundos

A la derecha se repite la misma tabla de tareas por trabajador (Task Duration) de la slide 20, como referencia.

## Slide 23

CASO NOVACRUZ. Dos gráficos de barras apiladas apilados verticalmente: "Cycle Time before Line Balancing" (arriba) y "Cycle Time after Line Balancing" (abajo), ambos con eje Y "Processing Time [Seconds]" 0-900 y columnas Step 1/Step 2/Step 3 formadas por segmentos numerados.

Antes: Step1 alcanza ~792 (tareas 1-12), Step2 ~648 (13-20), Step3 ~450 (21-26).
Después: Step1 alcanza ~623 (tareas 1,2,3,4,5,6,7,8 — sin 9 y 11 que se movieron), Step2 alcanza ~602 (11,12,13,14,15,16,17), Step3 alcanza ~665 (18,19,20,21,24,25,26).

A la derecha, leyenda numerada 1-26 con el nombre de cada tarea (Prepare Cable, Move Cable, Assemble Washer, Apply Fork Threading Cable End, Assemble Socket Head Screws, Steer Pin Nut, Brake Shoe Spring Pivot Bolt, Insert Front Wheel, Insert Axle Bolt, Tighten Axle Bolt, Tighten Brake Pivot Bolt, Assemble Handle and Cap, Assemble Brake Lever and Cable, Trim and Cap Cable, Place First Rib, Insert Axles and Cleats, Insert Rear Wheel, Place Second Rib and Deck, Apply Grip Tape, Insert Deck Fasteners, Inspect and Wipe Off, Apply Decal and Sticker, Insert in Bag, Assemble Carton, Insert Xootr and Manual, Seal Carton).

## Slide 24

CASO NOVACRUZ. Texto (rojo): "Ahora el cuello de botella es el proceso 3:"
- Tiempo de Ciclo = 665 segundos
- Tiempo Ocioso 1 = 665 – 623 = 42 segundos
- Tiempo Ocioso 2 = 665 – 602 = 63 segundos
- Tiempo Ocioso 3 = 0 segundos

Fórmula (roja): % Utilización de M.O. = M.O./(M.O. + Tiempo Ocioso)
Cálculo (rojo): (623 + 602 + 665)/(623 + 602 + 665 + 42 + 63 + 0) = 94.7%

Texto (rojo): "Con la nueva distribución de actividades en una semana se pueden producir:"
- N° Unidades a Producir = (35*3,600)/665 = 189.5 unidades/semana
- Costo de M.O. Directa = (3*35*12)/189 = 6.65 $/unidad
Recuadro: Costo M.O. Directa Unitario = Salario Total/Número de Unidades Producidas

A la derecha se repiten los dos gráficos de barras apiladas (before/after Line Balancing) con los totales 792/648/450 (antes) y 623/602/665 (después) marcados en rojo/azul, y la leyenda de tareas 1-26.

## Slide 25

Slide separadora de sección: "5. Incremento de Capacidad" sobre foto decorativa.

## Slide 26

CASO NOVACRUZ. Texto: "Si la demanda semanal se incrementa a 700 unidades se debe incrementar la capacidad de producción mediante las siguientes alternativas:"
- Utilizar la misma disposición con el mismo número de trabajadores, incrementando el número de líneas de producción.
- Asignar operarios adicionales a cada proceso, lo cual incrementa la capacidad de cada proceso y por lo tanto la capacidad total de producción.
- Dividir las tareas de cada proceso en varios procesos secuenciales, lo que incrementa la especialización de cada proceso.

## Slide 27

CASO NOVACRUZ. Mismo texto introductorio de la slide 26 (repetido, más corto). Diagrama grande con 3 bloques etiquetados a la izquierda:

- "Incremento del Número de Líneas" (amarillo): diagrama "Four Identical Lines Using the Initial Process Layout, One Worker per Step" — triángulo "Components" se ramifica en 4 líneas paralelas idénticas, cada una Step1→Step2→Step3 (con buffers triangulares entre pasos), y las 4 líneas convergen en triángulo "Finished Xootrs".
- "Incremento del Número de Operarios" (verde): diagrama "Components" → Step1 (con etiqueta "4 workers") → Step2 (4 workers) → Step3 (4 workers) → "Finished Xootrs", una sola línea pero con múltiples operarios por estación.
- "Incremento de Tareas Especializadas" (naranja): diagrama "Components" → cadena secuencial de 12 cajas numeradas 1→2→3→4→5→6→7→8→9→10→11→12 → "Finished Xootrs" ("One Line, One Worker per Step; Inventory between Steps Not Shown").

## Slide 28

CASO NOVACRUZ. "Incremento del Número de Líneas" (resaltado amarillo). Texto: "El número de líneas se obtiene dividiendo la demanda entre la capacidad de producción de la línea:"

Fórmula (roja): Número de Líneas = 700/189.5 = 3.69 => Número de Líneas = 4

Texto: "La desventaja de este enfoque es que se mantiene el mismo número de operarios en cada línea, no siendo necesariamente la mejor forma de asignar operarios a las actividades."

Texto (celeste): "Otra alternativa sería implementar 3 líneas de producción y la cantidad faltante producirla con sobretiempo."

## Slide 29

CASO NOVACRUZ. "Incremento del Número de Operarios" (resaltado verde). Texto: "El incrementar el número de líneas no necesariamente significa que la asignación sea óptima. Otra alternativa es determinar el número de operarios necesarios en cada proceso para lograr producir la cantidad requerida por la demanda."

Fórmulas (recuadro azul/rojo):
```
Capacidad Total del Proceso = N° Operarios*Capacidad del Proceso =>
Capacidad Total del Proceso = N° Operarios/Tiempo de Proceso =>
N° Operarios = Capacidad Total del Proceso*Tiempo de Proceso
```

Texto: "La capacidad requerida es 700 unidades/semana, considerando 35 hrs/semana, determinar la cantidad de operarios en cada proceso."

Cálculos (celeste):
- Proceso 1 → N° Operarios = (700/(35*3,600)) * 623 = 3.461 ~ 4 operarios
- Proceso 2 → N° Operarios = (700/(35*3,600)) * 602 = 3.344 ~ 4 operarios
- Proceso 3 → N° Operarios = (700/(35*3,600)) * 665 = 3.694 ~ 4 operarios

## Slide 30

CASO NOVACRUZ. "Incremento de Tareas Especializadas" (resaltado naranja). Texto: "El incrementar la especialización de los operarios asignándoles pocas tareas, de tal forma que sea posible dividir los procesos en varios procesos en los que el tiempo de procesamiento disminuya, lo cual podría incrementar la capacidad de la línea. Para esto se requiere partir de la cantidad de operarios inicial, es decir 12 operarios, y asignarles secuencialmente las tareas de manera equilibrada."

Tabla "TABLE 4.3 Processing times and Task Allocation under Increased Specialization" (screenshot), con 12 trabajadores y sus tareas/duraciones:
- Worker 1: Prepare cable(30), Move cable(25), Assemble washer(100). Total: 155.
- Worker 2: Apply fork threading cable end(66), Assemble socket head screws(114). Total: 180.
- Worker 3: Steer pin nut(49), Brake shoe spring pivot bolt(66). Total: 115.
- Worker 4: Insert front wheel(100), Insert axle bolt(30), Tighten axle bolt(43). Total: 173.
- Worker 5: Tighten brake pivot bolt(51), Assemble handle cap(118). Total: 169.
- Worker 6: Assemble brake lever and cable(110), Trim and cap cable(59). Total: 169.
- Worker 7: Place first rib(33), Insert axles and cleats(96). Total: 129.
- Worker 8: Insert rear wheel(135). Total: 135.
- Worker 9: Place second rib and deck(84), Apply grip tape(56). Total: 140.
- Worker 10: Insert deck fasteners(75), Inspect and wipe off(95). Total: 170.
- Worker 11: Apply decal and sticker(20), Insert in bag(43), Assemble carton(114). Total: 177.
- Worker 12: Insert Xootr and manual(94), Seal carton(84). Total: 178.
- Total labor content: 1,890.

## Slide 31

CASO NOVACRUZ. "Incremento de Tareas Especializadas" (naranja). Texto: "Luego se calcula el porcentaje de utilización de la mano de obra:"

Cálculo (celeste): %Utilización = 1,890/(1,890+25+0+65+7+11+11+51+45+40+10+3+2) = 87.5%

Imagen: "FIGURE 4.7 Line Balance in a Highly Specialized Line (Different shades represent different tasks)". Gráfico de barras apiladas (2 tonos: gris claro y negro) para 12 trabajadores (eje X: Worker 1-12), eje Y "Processing Time [Seconds]" 0-200. Cada barra combina un segmento gris (una tarea) y uno negro (otra tarea/ocioso), con alturas totales variables entre ~115 y ~180 aprox, ilustrando el balance desigual entre las 12 estaciones especializadas.

## Slide 32

CASO NOVACRUZ. "Celdas de Trabajo" (resaltado celeste). Texto: "Otra alternativa es que un mismo operario realice los 3 procesos, a esto se denomina celda de trabajo, lo cual permite minimizar el tiempo ocioso:"

Diagrama: triángulo "Components" se ramifica en 3 celdas paralelas (recuadros redondeados "Same Person"), cada una con Step1→Step2→Step3 en línea, y las 3 celdas convergen en triángulo "Finished Xootrs". Una línea punteada vertical conecta la celda del medio con la de abajo (posible indicación de repetición del patrón).

## Slide 33

CASO NOVACRUZ. "Celdas de Trabajo". Texto: "Si la demanda fuera de 700 unidades por semana, y el tiempo total es 1,890 segundos, se debe calcular cuál es la capacidad de una celda y determinar luego cuántas celdas son necesarias:"

Cálculos (celeste):
- Capacidad de 1 celda = (1/1890)*3600*35 = 66.67 unidades/semana
- Cantidad de Celdas = 700/66.67 = 10.5 ~ 11 celdas

## Slide 34

Slide de cierre decorativa: foto de escalera de concreto con overlay celeste, logo UTEC grande "UNIVERSIDAD DE INGENIERÍA Y TECNOLOGÍA", texto de fondo con nombres de carreras (Mecatrónica, Bioingeniería, Ciencia de la Computación, Ambiental, Energía, Industrial, Eléctrica). Sin contenido académico nuevo.
