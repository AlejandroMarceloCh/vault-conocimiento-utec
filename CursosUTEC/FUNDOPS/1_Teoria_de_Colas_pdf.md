---
curso: FUNDOPS
titulo: 1 - Teoría de Colas
slides: 27
fuente: 1 - Teoría de Colas.pdf
---

## Slide 1

Portada del curso. Título "Teoría de Colas" centrado, en letras grandes azul oscuro. Al pie derecho: "Expositor: Mg. Óscar Gamonal Pajares". Slide decorativa/de portada, sin contenido técnico.

## Slide 2

**Proceso de Llegadas**

Para especificar el proceso de llegadas a un sistema es necesario determinar la distribución de probabilidad del número de llegadas al proceso durante un periodo de tiempo determinado. El proceso de llegadas Poisson describe de una manera adecuada las llegadas a un sistema, la función de probabilidad es la siguiente:

$$P(X) = \frac{\lambda^x e^{-\lambda}}{x!}$$

Donde:
- λ: Tasa promedio de llegadas (número de llegadas/unidad de tiempo)
- x: Número de llegadas por periodo de tiempo
- e: Número de Euler = 2.71828

En Excel: `POISSON.DIST(x, λ, 0)`

## Slide 3

**Proceso de Llegadas Poisson a un Restaurant**

Enunciado: Determinar la probabilidad correspondiente al número de clientes que llegan a un restaurant durante el periodo de un minuto, si el proceso de llegadas es Poisson y en promedio llegan 45 clientes por hora. Realizar los cálculos con la fórmula general y luego utilizando la fórmula de Excel.

Captura de una hoja de cálculo (Excel) con el planteamiento (celdas aún vacías, valores por calcular):

Bloque izquierdo (etiqueta verde "Proceso de Llegadas Poisson a un Restaurant"):
| Variable | Valor |
|---|---|
| λ = | 45 clientes/hora |
| λ = | ___ clientes/minuto |

Tabla de valores de x (0 a 5) en amarillo, repetida dos veces (una para fórmula general, otra para fórmula Excel), cada fila dice "x = [0..5] clientes en un minuto".

Bloque derecho: fórmula $P(X)=\lambda^x e^{-\lambda}/x!$ con la definición de λ y x, y dos secciones tituladas "Utilizando la fórmula general" y "Utilizando la fórmula de Excel: POISSON.DIT(x;λ;0)", cada una con filas P[x=0] a P[x=5] (celdas de resultado vacías) junto a la descripción textual de cada probabilidad.

## Slide 4

**Solución - Proceso de Llegadas Poisson a un Restaurant**

Misma hoja de cálculo que la slide 3, ahora con resultados calculados:

| Variable | Valor |
|---|---|
| λ = | 45 clientes/hora |
| λ = | 0.75 clientes/minuto |

Resultados (idénticos en ambos métodos, fórmula general y Excel):
| x | P[x] |
|---|---|
| 0 | 0.47237 |
| 1 | 0.35427 |
| 2 | 0.13285 |
| 3 | 0.03321 |
| 4 | 0.00623 |
| 5 | 0.00093 |

## Slide 5

**Proceso de Servicio Exponencial - Tiempo de Servicio**

Es el tiempo que transcurre desde el momento en que una unidad empieza a ser atendida hasta que sale del sistema. Si el tiempo de servicio se expresa a través de una función de distribución de probabilidad exponencial, se puede calcular la probabilidad de que el tiempo de servicio sea menor o igual a un determinado tiempo t de acuerdo con la siguiente fórmula:

$$P(t\ de\ servicio \le t) = 1 - e^{-\mu t}$$

Donde:
- µ: Tasa de Servicio o Número promedio de unidades atendidas por unidad de tiempo (unidades/tiempo)
- e: Número de Euler = 2.71828

En Excel: `DISTR.EXP.N(t, µ, 1)`

## Slide 6

**Proceso de Servicio Exponencial – Tiempo de Servicio**

Enunciado: Determinar la probabilidad correspondiente al tiempo de atención de una pizzería si se sabe que el proceso de servicio es exponencial y el tiempo promedio de atención es igual a 30 clientes por hora. Realizar los cálculos con la fórmula general y luego utilizando la fórmula de Excel.

Captura de hoja de cálculo (planteamiento, sin resolver aún; nótese que reutiliza visualmente la plantilla de "Proceso de Llegadas Poisson a un Restaurant" con λ=45 clientes/hora como resto de la plantilla anterior, valores de x en 0-5 y celdas P[x=0..5] vacías con la fórmula $P(X)=\lambda^x e^{-\lambda}/x!$; parece un artefacto de copiar la plantilla previa antes de adaptarla al caso de servicio exponencial).

## Slide 7

**Solución – Proceso de Servicio Exponencial**

Captura de hoja de cálculo con la solución de la pizzería:

| Variable | Valor |
|---|---|
| µ = | 30 clientes/hora |
| µ = | 0.5 clientes/minuto |

Fórmula: $P(t\ de\ servicio \le t) = 1 - e^{-\mu t}$

"Utilizando la fórmula general: P(t de servicio <= t) = 1 - e^(-µt)":
| t <= | Probabilidad |
|---|---|
| 0.5 min | 0.22120 |
| 1 min | 0.39347 |
| 1.5 min | 0.52763 |
| 2 min | 0.63212 |
| 2.5 min | 0.71350 |
| 3 min | 0.77687 |

"Utilizando la fórmula de Excel: DISTR.EXP.N(x;µ;1)": misma tabla, mismos resultados (0.22120, 0.39347, 0.52763, 0.63212, 0.71350, 0.77687).

## Slide 8

**Disciplina de la Cola**

Es la forma en que las unidades que esperan en la cola son organizadas para ser atendidas, de tal forma que se asignan prioridades de atención en función a determinadas características. La disciplina más comúnmente utilizada es la denominada "Primero en Llegar, Primero en ser Servido", aunque existen disciplinas adicionales.

## Slide 9

**Líneas de Espera: Notación**

La notación utilizada en las fórmulas que permiten determinar las características de operación de un sistema con proceso de llegadas Poisson y tiempos de servicio exponenciales, con una cola y un servidor, son las siguientes:

- P0: Probabilidad de que el sistema esté vacío.
- λ: Tasa promedio de llegadas (unidades/tiempo).
- µ: Tasa de servicio o Número promedio de unidades atendidas por unidad de tiempo (unidades/tiempo).
- Lq: Longitud promedio de la cola.
- L: Número promedio de unidades en el sistema.

## Slide 10

**Líneas de Espera: Notación** (continuación)

- Wq: Tiempo promedio en la cola o tiempo de espera promedio.
- Pw: Probabilidad de que una unidad que llega tenga que hacer cola.
- Pn: Probabilidad de que haya n unidades en el sistema.

## Slide 11

**Línea de Espera con una Cola y un Servidor**

Las fórmulas que permiten determinar las características de operación de un sistema con proceso de llegadas Poisson y tiempos de servicio exponenciales, con una cola y un servidor, son las siguientes:

a) Probabilidad de que el Sistema esté vacío:
$$P_0 = 1 - \frac{\lambda}{\mu}$$

b) Número Promedio de Unidades en la Cola:
$$L_q = \frac{\lambda^2}{\mu(\mu-\lambda)}$$

c) Número Promedio de Unidades en el Sistema:
$$L = L_q + \frac{\lambda}{\mu}$$

## Slide 12

**Línea de Espera con una Cola y un Servidor** (continuación)

d) Tiempo Promedio en la Cola:
$$W_q = \frac{L_q}{\lambda}$$

e) Tiempo Promedio en el Sistema:
$$W = W_q + \frac{1}{\mu}$$

f) Probabilidad que una unidad tenga que hacer cola:
$$P_w = \frac{\lambda}{\mu}$$

g) Probabilidad que haya n unidades en el Sistema:
$$P_n = \left(\frac{\lambda}{\mu}\right)^n P_0$$

## Slide 13

**Auto Rápido Quentaqui Frai Chiquen**

Enunciado: El servicio de Auto Rápido de Quentaqui Frai Chiquen tiene una tasa de atención exponencial con promedio de 60 clientes/hora, sabiendo que existe una única ventanilla de atención y que los clientes llegan en su auto de acuerdo a una distribución de Poisson a razón de 30 clientes/hora, determinar:

a) La probabilidad de que el servicio de Auto Rápido se encuentre vacío.
b) El número promedio de autos esperando a ser atendidos.
c) El número promedio total de autos en el servicio.
d) El tiempo promedio de espera.
e) El tiempo promedio que transcurre desde que llega un auto hasta que se va.
f) La probabilidad de que cuando llegue un auto el servicio esté ocupado.
g) La probabilidad de que existan 5 autos en total.

## Slide 14

**Auto Rápido Quentaqui Frai Chiquen – 1 Ventanilla**

Captura de hoja de cálculo (planteamiento, sin resolver). Bloque de datos (etiqueta verde "Quentaqui Frai Chiquen - 1 ventanilla de Atención"):

| Variable | Valor |
|---|---|
| µ = | 60 autos/hora |
| λ = | 45 autos/hora |

Nota: en esta slide el enunciado dice λ=30 clientes/hora, pero la hoja de cálculo del ejemplo usa λ=45 autos/hora (posible inconsistencia de la plantilla original del PDF; se transcribe tal cual aparece en la imagen).

Tabla naranja de incógnitas (a-g) con celdas vacías: P0=, Lq= (autos), L= (autos), Wq= (minutos), W= (minutos), Pw=, n=5, P5=.

Al lado derecho se repiten las 7 fórmulas (a-g) del modelo de un servidor (idénticas a las de las slides 11-12).

## Slide 15

**Solución - Auto Rápido Quentaqui Frai Chiquen – 1 Ventanilla**

Misma hoja de cálculo que la slide 14, ahora resuelta:

| Variable | Valor |
|---|---|
| µ = | 60 autos/hora |
| λ = | 45 autos/hora |

| Resultado | Valor | Unidad |
|---|---|---|
| a) P0 = | 0.25 | |
| b) Lq = | 2.25 | autos |
| c) L = | 3.00 | autos |
| d) Wq = | 3.00 | minutos |
| e) W = | 4.00 | minutos |
| f) Pw = | 0.75 | |
| n = | 5 | |
| g) P5 = | 0.0593 | |

Al lado derecho, mismas 7 fórmulas del modelo de un servidor como referencia.

## Slide 16

**Línea de Espera con una Cola y n Servidores**

A continuación, se expresan las fórmulas que permiten determinar las características de operación de un sistema con una cola y n servidores considerando las siguientes características:

a) Las llegadas al sistema siguen un proceso Poisson.
b) Los tiempos de servicio son exponenciales.
c) El tiempo de servicio promedio en cada servidor es el mismo.
d) Cuando se desocupa un servidor la primera unidad en la cola empieza a ser atendida.

## Slide 17

**Línea de Espera con una Cola y k Servidores**

Las fórmulas que permiten determinar las características de operación de un sistema con una cola y k servidores son las siguientes:

a) Probabilidad de que el Sistema esté vacío:
$$P_0 = \dfrac{1}{\sum_{n=0}^{k-1}\dfrac{(\lambda/\mu)^n}{n!} + \dfrac{(\lambda/\mu)^k}{k!}\cdot\dfrac{k\mu}{k\mu-\lambda}}$$

b) Número Promedio de Unidades en la Cola:
$$L_q = \dfrac{(\lambda/\mu)^k \lambda\mu}{(k-1)!\,(k\mu-\lambda)^2} P_0$$

## Slide 18

**Línea de Espera con una Cola y k Servidores** (continuación)

c) Número Promedio de Unidades en el Sistema:
$$L = L_q + \frac{\lambda}{\mu}$$

d) Tiempo Promedio en la Cola:
$$W_q = \frac{L_q}{\lambda}$$

e) Tiempo Promedio en el Sistema:
$$W = W_q + \frac{1}{\mu}$$

## Slide 19

**Línea de Espera con una Cola y k Servidores** (continuación)

f) Probabilidad que una unidad tenga que hacer cola:
$$P_w = \frac{1}{k!}\left(\frac{\lambda}{\mu}\right)^k \cdot \frac{k\mu}{k\mu-\lambda}\cdot P_0$$

g) Probabilidad que haya n unidades en el Sistema:
$$P_n = \frac{(\lambda/\mu)^n}{n!} P_0 \quad \text{Si } n \le k$$
$$P_n = \frac{(\lambda/\mu)^n}{k!\,k^{(n-k)}} P_0 \quad \text{Si } n > k$$

## Slide 20

**Auto Rápido Quentaqui Frai Chiquen – 2 Ventanillas**

Enunciado: El gerente de Quentaqui Frai Chiquen ha decidido implementar una nueva ventanilla de atención con la misma tasa de servicio igual a 60 clientes por hora, manteniendo una sola cola, y sabiendo que los clientes llegan en su auto de acuerdo a una distribución de Poisson a razón de 30 clientes/hora, determinar:

a) La probabilidad de que el servicio de Auto Rápido se encuentre vacío.
b) El número promedio de autos esperando a ser atendidos.
c) El número promedio total de autos en el servicio.
d) El tiempo promedio de espera.
e) El tiempo promedio que transcurre desde que llega un auto hasta que se va.
f) La probabilidad de que cuando llegue un auto el servicio esté ocupado.
g) La probabilidad de que existan 5 autos en total.

## Slide 21

**Auto Rápido Quentaqui Frai Chiquen – 2 Ventanillas**

Captura de hoja de cálculo (planteamiento). Bloque de datos ("Quentaqui Frai Chiquen - 2 Ventanillas de Atención"):

| Variable | Valor |
|---|---|
| µ = | 60 autos/hora |
| λ = | 45 autos/hora |
| k = | 2 ventanillas |

Tabla naranja de incógnitas (a-g) vacía: P0=, Lq= (autos), L= (autos), Wq= (minutos), W= (minutos), Pw=, n=(vacío), P=.

Al costado derecho se repiten las 7 fórmulas (a-g) del modelo de k servidores (slides 17-19).

## Slide 22

**Solución - Auto Rápido Quentaqui Frai Chiquen – 2 Ventanillas**

Misma hoja resuelta:

| Variable | Valor |
|---|---|
| µ = | 60 autos/hora |
| λ = | 45 autos/hora |
| k = | 2 ventanillas |

| Resultado | Valor | Unidad |
|---|---|---|
| a) P0 = | 0.45 | |
| b) Lq = | 0.12 | autos |
| c) L = | 0.87 | autos |
| d) Wq = | 0.16 | minutos |
| e) W = | 1.16 | minutos |
| f) Pw = | 0.20 | |
| n = | 5 | |
| g) P5 = | 0.0067 | |

Al costado derecho, las mismas 7 fórmulas del modelo de k servidores como referencia.

## Slide 23

**La Ley de Little**

El número de unidades que se encuentran en el sistema es igual a la tasa de llegadas multiplicada por el tiempo que la unidad se encuentra dentro del sistema:

a) Número Promedio de Unidades en el Sistema: $L = \lambda W$

b) Número Promedio de Unidades en la Cola: $L_q = \lambda W_q$

c) Tiempo Promedio en la Cola: $W_q = \dfrac{L_q}{\lambda}$

d) Tiempo Promedio en el Sistema: $W = W_q + \dfrac{1}{\mu}$

## Slide 24

**Evaluación Económica de Líneas de Espera**

El costo total de un sistema está compuesto por el costo de espera y el costo de servicio, utilizando la siguiente notación:

- cw: Costo de espera de cada unidad por unidad de tiempo
- L: Número promedio de unidades en el sistema
- cs: Costo de servicio de cada servidor por unidad de tiempo
- k: Número de Servidores
- CT: Costo Total por periodo de tiempo

$$CT = c_w L + c_s k$$

## Slide 25

**Auto Rápido Quentaqui Frai Chiquen** (evaluación económica)

Enunciado: Compare los costos totales del servicio de Auto Rápido con 1 servidor y con 2 servidores, considerando que la empresa asigna un costo de 20 dólares por hora al tiempo de espera de un cliente y que el costo del servicio es igual a 10 dólares la hora.

Para 1 servidor:
$$CT = c_w L + c_s k \implies CT = 20 \times 3 + 10 \times 1 = 70\ \text{US\$/hora}$$

Para 2 servidores:
$$CT = c_w L + c_s k \implies CT = 20 \times 0.87 + 10 \times 2 = 37.4\ \text{US\$/hora}$$

Conclusión implícita: con 2 servidores el costo total es menor (37.4 vs 70 US$/hora), pese al mayor costo de servicio, porque cae fuertemente el costo de espera (L pasa de 3 a 0.87).

## Slide 26

**Notación de 3 símbolos de Kendall: A/B/k**

Los diferentes modelos de líneas de espera se pueden clasificar de acuerdo a la notación de Kendall A/B/k:

- A: Distribución de probabilidad de las llegadas al sistema.
- B: Distribución de probabilidad del tiempo de servicio.
- k: Número de servidores.

Los valores para A y B pueden ser los siguientes:

- M – Representa a una distribución Poisson de las llegadas o a una distribución exponencial del tiempo de servicio.
- D – Representa que las llegadas o el tiempo de servicio son constantes o determinísticos.
- G – Representa a cualquier distribución de probabilidad en la que se conoce la media y la desviación estándar.

## Slide 27

**Notación de 3 símbolos de Kendall: A/B/k** (ejercicio)

Especifique de acuerdo a la notación de Kendall los siguientes modelos de líneas de espera:

- Modelo de espera del caso Quentaqui Frai Chiquen con proceso de llegadas Poisson, tiempo de servicio exponencial y 2 servidores.
  → **M/M/2**
- Modelo de espera con un proceso de llegadas Poisson y tiempo de servicio en el que se conoce la media y la desviación estándar del tiempo de atención, con 4 servidores.
  → **M/G/4**
