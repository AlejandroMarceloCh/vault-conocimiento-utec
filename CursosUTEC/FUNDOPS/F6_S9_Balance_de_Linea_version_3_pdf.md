---
curso: FUNDOPS
titulo: F6-S9 Balance de Línea (versión 3)
slides: 34
fuente: F6-S9 Balance de Línea (versión 3).pdf
---

FUNDAMENTOS DE OPERACIONES
Semana 9 - Balance de Línea
Índice:

1. Capacidad
2. Tiempo de Flujo (Flow Time)
3. Mano de Obra y Tiempo Ocioso
4. Balance de Línea
5. Incremento de Capacidad
Objetivos:

Al finalizar esta sesión, deberás ser capaz
de:

1. Calcular tiempos de operaciones, costos
  de mano de obra e indicadores de
  aprovechamiento de recursos.
2. Determinar una eficiente distribución de
  tareas y tiempos de actividades.
3. Generar estrategias para incrementar la
  capacidad de procesos en operaciones.
                                                        CASO NOVACRUZ
 Novacruz es una empresa que se dedica a fabricar scooters de alta gama. Si bien la demanda de su producto
 no era más de 100 scooters por semana a principios de marzo, creció dramáticamente, alcanzando pronto
 1,200 unidades por semana en el otoño.




                                                                                                        FIGURE 4.2 Lifecycle Demand
                                                                                                        Trajectory for Xootrs


Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4



                                                                                             FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
Capacidad
                                                        CASO NOVACRUZ

 La fabricación consta de 3 procesos de ensamble, en cada proceso trabaja un operario.
  ● En la primera actividad, se necesitan 13 min/scooter para ensamblar las primeras piezas, incluida la
       horquilla, el soporte de la dirección y el mango en T.
  ● En la segunda actividad, se necesitan 11 min/scooter para ensamblar la rueda, el freno y algunas otras
       partes relacionadas con el mecanismo de dirección.
  ● En la tercera actividad, se necesitan 8 min/scooter para limpiar el producto, aplicar las calcomanías y la
       cinta de agarre y realizar la prueba funcional final.




Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4



                                                                                             FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                               CASO NOVACRUZ

Cada proceso se ejecuta en un tiempo de procesamiento o tiempo de servicio.
La capacidad de un proceso que consta de un recurso o de un grupo de recursos que realizan la misma
actividad se calcula con la siguiente fórmula:




Ejemplo: Actividad 1



                                                 Tiempo de Procesamiento
                              Actividad                                    Capacidad (scooters/hora)
                                                    (minutos/scooter)
                                  1                        13                         4.6

                                  2                        11                        5.45

                                  3                        8                          7.5

                                                                           FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
Tiempo de flujo
(Flow Time)
                                                   CASO NOVACRUZ
Si no se cuenta con inventario inicial en ningún proceso ¿En cuánto tiempo se terminará de producir la primera unidad?

 En la suma de los tiempos de procesamiento de cada proceso

¿Cuánto tiempo pasa cada unidad a través de todo el proceso de producción?

 En la suma de los tiempos de procesamiento en cada proceso más los tiempos de espera en cada proceso.

¿Qué es la tasa de flujo o ritmo de producción o throughput?

 Es el número de unidades producidas de producto terminado por unidad de tiempo.

¿Qué proceso determina el ritmo de producción cuando hay demanda y materia prima en exceso?

 La capacidad del cuello de botella determina el ritmo de producción.

¿Qué es el tiempo de ciclo o cadencia de producción?
                                                                                                    Tiempo de
                                                                                                                       Capacidad
                                                                               Actividad          Procesamiento
 Es el tiempo que transcurre entre 2 unidades consecutivas de producto terminado, es igual al tiempo                (scooters/hora)
                                                                                                      de procesamiento
                                                                                                 (minutos/scooter)
 del cuello de botella cuando hay demanda y materia prima en exceso.                 1                    13                     4.6
                                                                                     2                    11                    5.45
                                                                                    FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                                                                     3                     8                     7.5
                                                        CASO NOVACRUZ
  ● El tiempo necesario para producir una unidad cuando no hay inventario:



                                                                Tiempo 1° scooter = 13 + 11 + 8 = 32 min
  ● Si el flujo es continuo (máquinas):



                                                              Tiempo de flujo (Flow Time) = 3 x 13 = 39 min

                                                                                    Tiempo de Procesamiento
                                                    Actividad                                                 Capacidad (scooters/hora)
                                                                                       (minutos/scooter)
                                                          1                                   13                         4.6
                                                          2                                   11                        5.45
                                                          3                                   8                          7.5

Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4



                                                                                                                  FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                                        CASO NOVACRUZ




   ● El tiempo total de producción de X unidades cuando no hay inventario es:
                                                             Tiempo Total de Producción de X unidades =
                                              Tiempo para Producir la 1ª Unidad + (X – 1)*Tiempo de Ciclo =
                                       Tiempo para Producir la 1ª Unidad + (X – 1)*Cadencia de Producción =
                                            Tiempo para Producir la 1ª Unidad + (X – 1)/Ritmo de Producción
                                 Tiempo Total de Producción de 100 unidades = 32 + (100-1)x 13 = 1,319 min
Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4



                                                                                                    FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
Mano de Obra y
Tiempo Ocioso
CASO NOVACRUZ




                FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
CASO NOVACRUZ




                FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
CASO NOVACRUZ




                FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                  CASO NOVACRUZ


                                                                     Tiempo de
                                                                                             Capacidad
 Sin considerar la Demanda                        Actividad        Procesamiento
                                                                                          (scooters/hora)
                                                                  (minutos/scooter)
 Tiempo de ciclo = 13 min/scooter                    1                    13                     4.6
Semanalmente se podría producir =                    2                    11                    5.45
(35 hrs x 60 min) / 13 min = 161 unid/semana         3                     8                     7.5



Considerando una demanda: 125 unid/semana
                                                   T. Ocioso de 1 Operario por Unidad
  Tiempo de Ciclo                                  = ( 16.8 -13) + (16.8-11)+(16.8-8) = 18.4 min/unid
    = 1 / 125 unid/sem
    = (35 hr x 60 min) / 125 unid = 16.8 min          M.O. Efectiva por unidad = 13+11+8 = 32 min


  Costo de M.O. Directa
   = (3 x $12/hr x 35 hr/sem ) / (125 unid/sem)
   = 10.08 $/unid                                        Utilización de M.O. = 32 / (32+18.4) = 63.5 %

                                                              FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                               CASO NOVACRUZ

● Número de Horas Laborables = 35 horas/semana
                                    Operario 1            Operario 2                   Operario 3
  Tiempo de Procesamiento       13 minutos/unidad     11 minutos/unidad             8 minutos/unidad
                               1/13 unidades/minuto
  Capacidad de Cada                                 1/11 unidades/minuto =       1/8 unidades/minuto =
                                         =
  Proceso                                             5.45 unidades/hora           7.5 unidades/hora
                                4.61 unidades/hora
  Capacidad del Proceso de
                                             161 unidades/semana = 4.61 unidades/hora
  Producción
  Demanda                                    125 unidades/semana = 3.57 unidades/hora
  Ritmo de Producción o
                                     Min (Demanda, Capacidad del Proceso) = 3.57 unidades/hora
  Tasa de Flujo (Flow Rate)
  Tiempo de Ciclo (Cadencia)                 1/(3.57 unidades/hora) = 16.8 minutos/unidad
                                  16.8 – 13 = 3.8           16.8 – 11 = 5.8          16.8 – 8 = 8.8
  Tiempo de Inactividad
                                  minutos/unidad           minutos/unidad           minutos/unidad
  %Utilización                  3.57/4.61 = 77.44%        3.57/5.45 = 65.5%        3.57/7.5 = 47.6%

                                                                        FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
Balance de Línea
                               CASO NOVACRUZ
                                          Tiempo de Procesamiento           Capacidad
                       Actividad
                                             (minutos/scooter)           (scooters/hora)
                           1                        13                         4.6
                           2                        11                        5.45
                           3                        8                          7.5

Existe un desbalance entre los 3 procesos, para reducir el desbalance se puede incrementar la capacidad de
procesamiento de las siguientes formas:

● Incrementar la capacidad del proceso reasignando operarios desde los recursos subutilizados hacia el cuello
   de botella.
● Incrementar la capacidad del proceso reasignando trabajo del cuello de botella a los recursos subutilizados.

Si la demanda cambia a 200 unidades semanales, no va a ser posible satisfacer la demanda debido a que en
una semana solamente se pueden producir 161 unidades.
                                                                           FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                                                          CASO NOVACRUZ




Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4

                                                                                             FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2

                                                          CASO NOVACRUZ

Debido a que el tiempo empleado por cada operario para realizar las actividades asignadas para una
unidad está desbalanceado, se deben reasignar actividades de un operario a otro considerando la
secuencia de producción.


El balance ideal se puede lograr si el tiempo total empleado se divide entre los 3 operarios por igual:
                                                         (792+648+450)/3 = 1,890/3 = 630 segundos


Lo que se debe hacer es asignar a cada operario una cantidad de tiempo que sea lo más cercana a 630
segundos y luego calcular el porcentaje de utilización.

  Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4



                                                                                               FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                                            CASO NOVACRUZ

La mejor asignación posible es la siguiente:


● Al operario 1 le restamos las 2 últimas tareas y las asignamos al operario 2:


Tiempo de Ciclo 1 = 792 – 51 – 118 = 623 segundos


● Al operario 2 le restamos las 3 últimas tareas y las asignamos al operario 3:


Tiempo de Ciclo 2 = 648 + 51 + 118 – 84 – 56 – 75 = 602 segundos
Tiempo de Ciclo 3 = 450 + 84 + 56 + 75 = 665 segundos

    Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4



                                                                                                 FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                                        CASO NOVACRUZ




Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4



                                                                                             FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                                                                                               792
CASO NOVACRUZ                                                                                                                  648

                                                                                                                                           450
 Ahora el cuello de botella es el proceso 3:
 ● Tiempo de Ciclo = 665 segundos
 ● Tiempo Ocioso 1 = 665 – 623 = 42 segundos
 ● Tiempo Ocioso 2 = 665 – 602 = 63 segundos
 ● Tiempo Ocioso 3 = 0 segundos                                                                                                           665
                                                                                                                   623         602


 Por lo tanto:
 ● %Utilización =
 (623 + 602 + 665)/(623 + 602 + 665 + 42 + 63 + 0) = 94.7%


 Con la nueva distribución de actividades en una semana se pueden producir:
 ● N° Unidades a Producir = (35*3,600)/665 = 189.5 unidades/semana
 ● Costo de M.O. Directa = (3*35*12)/189 = 6.65 $/unidad
                      Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4

                                                                                                                         FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
Incremento de
Capacidad
                                                        CASO NOVACRUZ

 Si la demanda semanal se incrementa a 700 unidades se debe incrementar la capacidad de
 producción mediante las siguientes alternativas:


  ● Utilizar la misma disposición con el mismo número de trabajadores, incrementando el número de
       líneas de producción.
  ● Asignar operarios adicionales a cada proceso, lo cual incrementa la capacidad de cada proceso y
       por lo tanto la capacidad total de producción.
  ● Dividir las tareas de cada proceso en varios procesos secuenciales, lo que incrementa la
       especialización de cada proceso.


Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4



                                                                                             FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                                              CASO NOVACRUZ

       Si la demanda semanal se incrementa a 700 unidades se debe incrementar la capacidad de producción
       mediante las siguientes alternativas:

Incremento del Número de Líneas




Incremento del Número de Operarios




Incremento de Tareas Especializadas



      Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4


                                                                                                   FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                                        CASO NOVACRUZ

 Incremento del Número de Líneas
 El número de líneas se obtiene dividiendo la demanda entre la capacidad de producción de la línea:


                                       Número de Líneas = 700/189.5 = 3.69 => Número de Líneas = 4


 La desventaja de este enfoque es que se mantiene el mismo número de operarios en cada línea, no siendo
 necesariamente la mejor forma de asignar operarios a las actividades.


 Otra alternativa sería implementar 3 líneas de producción y la cantidad faltante producirla con
 sobretiempo.

Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4



                                                                                             FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                        CASO NOVACRUZ
Incremento del Número de Operarios
El incrementar el número de líneas no necesariamente significa que la asignación sea óptima. Otra alternativa es
determinar el número de operarios necesarios en cada proceso para lograr producir la cantidad requerida por la
demanda.




La capacidad requerida es 700 unidades/semana, considerando 35 hrs/semana, determinar la cantidad de
operarios en cada proceso.

                  Proceso 1 -> N° Operarios = (700 /(35*3,600)) * 623 = 3.461 ~ 4 operarios
                  Proceso 2 -> N° Operarios = (700 /(35*3,600)) * 602 = 3.344 ~ 4 operarios
                  Proceso 3 -> N° Operarios = (700 /(35*3,600)) * 665 = 3.694 ~ 4 operarios
                      Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4
                                                                                                                   FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
 CASO NOVACRUZ

Incremento de Tareas Especializadas
El incrementar la especialización de los operarios
asignándoles pocas tareas, de tal forma que sea posible
dividir los procesos en varios procesos en los que el
tiempo de procesamiento disminuya, lo cual podría
incrementar la capacidad de la línea.


Para esto se requiere partir de la cantidad de operarios
inicial,   es   decir    12          operarios,                 y        asignarles
secuencialmente las tareas de manera equilibrada.

                        Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4
                                                                                                                     FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                                        CASO NOVACRUZ

 Incremento de Tareas Especializadas
 Luego se calcula el porcentaje de utilización de la mano de obra:

                     %Utilización = 1,890/(1,890+25+0+65+7+11+11+51+45+40+10+3+2) = 87.5%




                      En la siguiente gráfica se muestra el balance
                      en una línea altamente especializada:




Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4


                                                                                             FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                                        CASO NOVACRUZ

 Celdas de Trabajo
 Otra alternativa es que un mismo operario realice los 3 procesos, a esto se denomina celda de trabajo, lo cual
 permite minimizar el tiempo ocioso:




Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4


                                                                                             FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2
                                                        CASO NOVACRUZ

 Celdas de Trabajo
 Si la demanda fuera de 700 unidades por semana, y el tiempo total es 1,890 segundos, se debe calcular cuál es
 la capacidad de una celda y determinar luego cuántas celdas son necesarias:


                                  Capacidad de 1 celda = (1/1890)*3600*35 = 66.67 unidades/semana


                                                    Cantidad de Celdas = 700/66.67 = 10.5 ~ 11 celdas




Obtained from “Matching Supply with Demand”, Author: Gerard Cachon, 3rd Edition, Chapter 4



                                                                                               FUNDAMENTOS DE OPERACIONES / Semana 9 / Ciclo 2024-2

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
