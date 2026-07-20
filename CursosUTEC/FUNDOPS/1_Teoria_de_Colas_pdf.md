---
curso: FUNDOPS
titulo: 1 - Teoría de Colas
slides: 27
fuente: 1 - Teoría de Colas.pdf
---

Teoría de Colas



        Expositor: Mg. Óscar Gamonal Pajares
Proceso de Llegadas
Para especificar el proceso de llegadas a un sistema es necesario determinar la
distribución de probabilidad del número de llegadas al proceso durante un periodo de
tiempo determinado.
El proceso de llegadas Poisson describe de una manera adecuada las llegadas a un
sistema, la función de probabilidad es la siguiente:


                                     𝑷 𝑿 = 𝝀𝒙 𝒆−𝝀 /𝒙!

Donde: λ: Tasa promedio de llegadas (número de llegadas/unidad de tiempo)
        x: Número de llegadas por periodo de tiempo
        e: Número de Euler = 2.71828

En Excel: POISSON.DIST(x, λ, 0)
Proceso de Llegadas Poisson a un Restaurant
Determinar la probabilidad correspondiente al número de clientes que llegan a un restaurant durante el
periodo de un minuto, si el proceso de llegadas es Poisson y en promedio llegan 45 clientes por hora.
Realizar los cálculos con la fórmula general y luego utilizando la fórmula de Excel.
Solución - Proceso de Llegadas Poisson a un Restaurant
Proceso de Servicio Exponencial - Tiempo de Servicio
Es el tiempo que transcurre desde el momento en que una unidad empieza a ser
atendida hasta que sale del sistema. Si el tiempo de servicio se expresa a través de una
función de distribución de probabilidad exponencial, se puede calcular la probabilidad de
que el tiempo de servicio sea menor o igual a un determinado tiempo t de acuerdo con la
siguiente fórmula:

                            𝑷 𝒕 𝒅𝒆 𝒔𝒆𝒓𝒗𝒊𝒄𝒊𝒐 ≤ 𝒕 = 𝟏 − 𝒆−µ𝒕

Donde: µ: Tasa de Servicio o Número promedio de unidades atendidas por unidad de
         tiempo (unidades/tiempo)
        e: Número de Euler = 2.71828

En Excel: DISTR.EXP.N(t, µ, 1)
Proceso de Servicio Exponencial – Tiempo de Servicio
Determinar la probabilidad correspondiente al tiempo de atención de una pizzería si se sabe que el proceso
de servicio es exponencial y el tiempo promedio de atención es igual a 30 clientes por hora. Realizar los
cálculos con la fórmula general y luego utilizando la fórmula de Excel.
Solución – Proceso de Servicio Exponencial
Disciplina de la Cola
Es la forma en que las unidades que esperan en la cola son organizadas para ser
atendidas, de tal forma que se asignan prioridades de atención en función a
determinadas características. La disciplina más comúnmente utilizada es la
denominada “Primero en Llegar, Primero en ser Servido”, aunque existen
disciplinas adicionales.
Líneas de Espera: Notación
La notación utilizada en las fórmulas que permiten determinar las características
de operación de un sistema con proceso de llegadas Poisson y tiempos de
servicio exponenciales, con una cola y un servidor son las siguientes:

P0: Probabilidad de que el sistema esté vacío.
λ: Tasa promedio de llegadas (unidades/tiempo).
µ: Tasa de servicio o Número promedio de unidades atendidas por unidad de
tiempo (unidades/tiempo).
Lq: Longitud promedio de la cola.
L: Número promedio de unidades en el sistema
Líneas de Espera: Notación

Wq: Tiempo promedio en la cola o tiempo de espera promedio.
Pw: Probabilidad de que una unidad que llega tenga que hacer cola.
Pn: Probabilidad de que haya n unidades en el sistema.
Línea de Espera con una Cola y un Servidor
Las fórmulas que permiten determinar las características de operación de un
sistema con proceso de llegadas Poisson y tiempos de servicio exponenciales,
con una cola y un servidor son las siguientes:
                                                         𝝀
a) Probabilidad de que el Sistema esté vacío:   𝑷𝟎 = 𝟏 −
                                                         µ


                                                   𝝀𝟐
b) Número Promedio de Unidades en la Cola: 𝐋𝐪 =
                                                µ(µ − 𝝀)


                                                              𝝀
c) Número Promedio de Unidades en el Sistema:        𝐋 = 𝐋𝐪 +
                                                              µ
Línea de Espera con una Cola y un Servidor
                                      𝑳𝒒
d) Tiempo Promedio en la Cola:   Wq =
                                       λ


                                                𝟏
e) Tiempo Promedio en el Sistema:      𝑾 = 𝑾𝒒 +
                                                µ


                                                          𝝀
f) Probabilidad que una unidad tenga que hacer cola: Pw =
                                                          µ


                                                         λ
g) Probabilidad que haya n unidades en el Sistema: Pn = ( )𝑛𝑃0
                                                         µ
Auto Rápido Quentaqui Frai Chiquen
El servicio de Auto Rápido de Quentaqui Frai Chiquen tiene una tasa de atención exponencial con promedio
de 60 clientes/hora, sabiendo que existe una única ventanilla de atención y que los clientes llegan en su auto
de acuerdo a una distribución de Poisson a razón de 30 clientes/hora, determinar:

a) La probabilidad de que el servicio de Auto Rápido se encuentre vacío.
b) El número promedio de autos esperando a ser atendidos.
c) El número promedio total de autos en el servicio.
d) El tiempo promedio de espera.
e) El tiempo promedio que transcurre desde que llega un auto hasta que se va.
f) La probabilidad de que cuando llegue un auto el servicio esté ocupado.
g) La probabilidad de que existan 5 autos en total.
Auto Rápido Quentaqui Frai Chiquen – 1 Ventanilla
Solución - Auto Rápido Quentaqui Frai Chiquen – 1 Ventanilla
Línea de Espera con una Cola y n Servidores
A continuación, se expresan las fórmulas que permiten determinar las
características de operación de un sistema con una cola y n servidores
considerando las siguientes características:

a) Las llegadas al sistema siguen un proceso Poisson.
b) Los tiempos de servicio son exponenciales.
c) El tiempo de servicio promedio en cada servidor es el mismo.
d) Cuando se desocupa un servidor la primera unidad en la cola empieza a ser
atendida.
Línea de Espera con una Cola y k Servidores
Las fórmulas que permiten determinar las características de operación de un sistema con una cola
y k servidores son las siguientes:

a) Probabilidad de que el Sistema esté vacío:

                                                  𝟏
                        𝑷𝟎 =
                                    λ 𝒏
                                    µ    𝝀 𝒌
                               σ𝒌−𝟏
                                𝒏=𝟎 𝒏! + µ /𝒌! (𝒌µ/(𝒌µ − λ))


b) Número Promedio de Unidades en la Cola:

                                                𝝀 𝒌
                                                ( ) λµ
                                                µ
                                    𝐋𝐪 =                 P0
                                            𝒌−𝟏 ! 𝒌µ − 𝝀 𝟐
Línea de Espera con una Cola y k Servidores
Las fórmulas que permiten determinar las características de operación de un
sistema con una cola y n servidores son las siguientes:

                                                       𝝀
c) Número Promedio de Unidades en el Sistema: 𝐋 = 𝐋𝐪 +
                                                       µ


                                      𝑳𝒒
d) Tiempo Promedio en la Cola:   Wq =
                                       λ


                                                 𝟏
e) Tiempo Promedio en el Sistema:     𝑾 = 𝑾𝒒 +
                                                 µ
Línea de Espera con una Cola y k Servidores
f) Probabilidad que una unidad tenga que hacer cola:

                          𝟏           𝝀   𝒌
                     Pw =                     𝒌µ/(𝒌µ − λ) 𝑷𝟎
                          𝒌!          µ

g) Probabilidad que haya n unidades en el Sistema:

                           λ 𝑛
                    Pn = (     /𝑛!)𝑃0                Si: n <= k
                           µ

                           λ 𝑛        (𝑛 − 𝑘)
                    Pn = (     /(𝑘! 𝑘         ))𝑃0     Si: n > k
                           µ
Auto Rápido Quentaqui Frai Chiquen – 2 Ventanillas
El gerente de Quentaqui Frai Chiquen ha decidido implementar una nueva ventanilla de atención con la
misma tasa de servicio igual a 60 clientes por hora, manteniendo una sola cola, y sabiendo que los clientes
llegan en su auto de acuerdo a una distribución de Poisson a razón de 30 clientes/hora, determinar:

a) La probabilidad de que el servicio de Auto Rápido se encuentre vacío.
b) El número promedio de autos esperando a ser atendidos.
c) El número promedio total de autos en el servicio.
d) El tiempo promedio de espera.
e) El tiempo promedio que transcurre desde que llega un auto hasta que se va.
f) La probabilidad de que cuando llegue un auto el servicio esté ocupado.
g) La probabilidad de que existan 5 autos en total.

Auto Rápido Quentaqui Frai Chiquen – 2 Ventanillas
Solución - Auto Rápido Quentaqui Frai Chiquen – 2 Ventanillas
La Ley de Little
El número de unidades que se encuentran en el sistema es igual a la tasa de llegadas
multiplicada por el tiempo que la unidad se encuentra dentro del sistema:

a) Número Promedio de Unidades en el Sistema: 𝐋 = λW

b) Número Promedio de Unidades en la Cola:       𝐋𝐪 = λWq


                                       𝑳𝒒
c) Tiempo Promedio en la Cola:    Wq =
                                        λ

                                             𝟏
d) Tiempo Promedio en el Sistema: 𝑾 = 𝑾𝒒 +
                                             µ
Evaluación Económica de Líneas de Espera
El costo total de un sistema está compuesto por el costo de espera y el costo de
servicio, utilizando la siguiente notación:

cw: Costo de espera de cada unidad por unidad de tiempo
L: Número promedio de unidades en el sistema
cs: Costo de servicio de cada servidor por unidad de tiempo
k: Número de Servidores
CT: Costo Total por periodo de tiempo

                                 CT = cwL + csk
Auto Rápido Quentaqui Frai Chiquen
Compare los costos totales del servicio de Auto Rápido con 1 servidor y con 2 servidores, considerando que
la empresa asigna un costo de 20 dólares por hora al tiempo de espera de un cliente y que el costo del
servicio es igual a 10 dólares la hora.

Para 1 servidor:

CT = cwL + csk => CT = 20*3 + 10*1 = 70 US$/hora



Para 2 servidores:

CT = cwL + csk => CT = 20*0.87 + 10*2 = 37.4 US$/hora
Notación de 3 símbolos de Kendall: A/B/k
Los diferentes modelos de líneas de espera se pueden clasificar de acuerdo a la notación de Kendall A/B/k:

A: Distribución de probabilidad de las llegadas al sistema.
B: Distribución de probabilidad del tiempo de servicio.
k: Número de servidores.

Los valores para A y B pueden ser los siguientes:

M – Representa a una distribución Poisson de las llegadas o a una distribución exponencial del
    tiempo de servicio.
D – Representa que las llegadas o el tiempo de servicio son constantes o determinísticos.
G – Representa a cualquier distribución de probabilidad en la que se conoce la media y la desviación
estándar.
Notación de 3 símbolos de Kendall: A/B/k

Especifique de acuerdo a la notación de Kendall los siguientes modelos de líneas de espera:

▪   Modelo de espera del caso Quentaqui Frai Chiquen con proceso de llegadas Poisson, tiempo de servicio
    exponencial y 2 servidores.
         M/M/2

▪   Modelo de espera con un proceso de llegadas Poisson y tiempo de servicio en el que se conoce la media
    y la desviación estándar del tiempo de atención, con 4 servidores.
          M/G/4

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
