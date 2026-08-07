---
curso: FUNDOPS
titulo: 1 - Variabilidad en los Procesos
slides: 49
fuente: 1 - Variabilidad en los Procesos.pdf
---

## Slide 1

Portada del capítulo. Título: "La Variabilidad en los Procesos". Expositor: Mg. Óscar Gamonal Pajares. Slide decorativa/de portada, sin contenido técnico adicional.

## Slide 2

**Tiempo de Espera**

Pregunta guía: ¿Cuándo los usuarios de un servicio tienen que esperar para ser atendidos?

1. Cuando la demanda esperada es mayor a la capacidad de atención.
2. Cuando existe variabilidad en el tiempo entre llegadas, inclusive si existe capacidad de atención suficiente.

Solo texto, sin diagramas.

## Slide 3

**Ejemplo – Call Center**

En un Call Center se asigna una recepcionista de 7am a 8am. Promedio: 12 llamadas/hora, 4 minutos por llamada (una llamada cada 5 minutos).

Preguntas y respuestas (resaltadas en rojo):
- ¿El proceso tiene capacidad suficiente? Capacidad = (60 min/hora)/(4 min/llamada) = 15 llamadas/hora
- ¿Tiempo de espera promedio? Tiempo de Espera = 0 minutos
- ¿% de Utilización? %Utilización = Tasa de Llegadas/Capacidad = 12/15 = 80%

## Slide 4

**Ejemplo – Call Center**

Figura 9.1 "A Somewhat Odd Service Process" (tomada del libro de Cachon). Diagrama de Gantt horizontal: eje de tiempo de 7:00 a 8:00, con 12 filas (Caller 1 a Caller 12) mostrando barras negras que representan el tiempo de atención de cada llamada. Las barras están escalonadas en el tiempo, cada llamador atendido secuencialmente uno tras otro sin solaparse, ilustrando un proceso de servicio "algo extraño" donde las llamadas llegan a intervalos y se procesan en orden.

## Slide 5

**Ejemplo – Call Center**

Figura 9.2 "Data Gathered at a Call Center". Contiene:
- Tabla con columnas Caller (1-12), Arrival Time (0,7,9,12,18,22,25,30,36,45,51,55) y Processing Time (5,6,7,6,5,2,4,3,4,2,2,3).
- Línea de tiempo (7:00-8:00) con flechas marcando el momento de llegada de cada caller (Caller 1 a Caller 12).
- Histograma de barras: eje X "Processing Times" (2, 3, 4, 5, 6, 7 min), eje Y "Number of Cases" (0-3). Muestra 3 casos en 2 min, 2 en 3 min, 2 en 4 min, 2 en 5 min, 2 en 6 min, 1 en 7 min — ilustrando la variabilidad del tiempo de procesamiento.

## Slide 6

**Ejemplo – Call Center**

Figura 9.3 "Detailed Analysis of Call Center". Dos gráficos apilados:
- Superior: diagrama de Gantt (7:00-8:00) con 12 filas (Caller 1-12), cada barra dividida en dos segmentos: negro = "Processing Time" (con flecha señalando) y gris = "Wait Time" (con flecha señalando). Se ve claramente cómo aumenta el tiempo de espera para los callers intermedios (5-9) y disminuye hacia el final.
- Inferior: gráfico de barras "Inventory (Callers on Hold and In Service)" vs Time (7:00-8:00), eje Y de 0 a 5. Muestra un pico de inventario (4-5 llamadas simultáneas) alrededor de 7:25-7:35, luego decae.

## Slide 7

**Conceptos Generales**

Cuatro definiciones clave (texto, sin visual):
- Unidad de Flujo (Flow Unit): unidad que llega, se procesa y sale del sistema.
- Inventario (Inventory): número de unidades de flujo en el sistema, también WIP (Work-In-Process).
- Tiempo de Flujo (Flow Time): tiempo desde la llegada hasta la salida, incluye espera.
- Tasa de Flujo (Flow Rate): tasa a la cual salen las unidades ("throughput rate"); la tasa máxima es la "capacidad del proceso".

## Slide 8

**Inventario**

Figura 2.7 "Cumulative Inflow and Outflow". Gráfico escalonado (step function) con eje Y "Patients" (0-11) y eje X "Time" (7:00 a 18:00). Dos curvas escalonadas: línea negra gruesa "Cumulative Inflow" y línea gris "Cumulative Outflow", ambas suben en escalones conforme llegan/salen pacientes. Entre ambas curvas se marcan con flechas los conceptos "Inventory" (distancia vertical entre curvas) y "Flow Time" (distancia horizontal). Debajo, un histograma de barras grises de fondo representa la fórmula: Inventory = Cumulative Inflow − Cumulative Outflow.

## Slide 9

**Tiempo de Flujo Promedio (Average Flow Time)**

Tabla 2.3 "Calculation of Average Flow Time" con columnas: Number (1-11), Patient Name (vacío), Arrival Time, Departure Time, Flow Time. 11 filas de datos (ej. 7:35→8:50 = 1:15; 14:30→18:10 = 3:40, etc.). Fila final: Average = 2:04:33.

## Slide 10

**La Ley de Little (Little's Law)**

Fórmulas centrales (en rojo):
- Inventario Promedio (WIP) = Tasa de Flujo x Tiempo de Flujo
- I = WIP = R×T
- WIP = Work in Process

Solo texto/fórmulas, sin diagrama.

## Slide 11

**¿Por qué hay variabilidad en un Proceso?**

Existen 4 fuentes de variabilidad (lista numerada):
1. Variabilidad de las unidades entrantes.
2. Variabilidad de procesamiento.
3. Disponibilidad de los recursos.
4. Rutas aleatorias para diferentes unidades.

Solo texto.

## Slide 12

**Ejemplo – Call Center**

Figura 9.4 "Variability and Where It Comes From". Diagrama de flujo de proceso: caja "Input" (Random Arrivals, Incoming Quality, Product Mix) → flecha → triángulo "Buffer" → flecha → caja "Processing" → flecha de salida que se bifurca en salida principal y una flecha hacia abajo "Routes" (Variable Routing, Dedicated Machines). A la derecha de "Processing" se listan "Processing Times" (Inherent Variation, Lack of Operating Procedures, Quality Scrap/Rework) y "Resources" (Breakdowns/Maintenance, Operator Absence, Setup Times) como fuentes de variabilidad que afectan el proceso.

## Slide 13

**¿Cómo se mide la variabilidad?**

Texto explicativo: la desviación estándar es una medida absoluta de variabilidad (no indica si es alta o baja). Para medir en términos relativos se usa el coeficiente de variación:

$$CV = \frac{\text{Desviación Estándar}}{\text{Media}} = \frac{\sigma}{\mu}$$

## Slide 14

**Proceso de Llegadas**

Definiciones: Tiempo de llegada (AT), Tiempo entre llegadas (IA). Fórmula: $IA_i = AT_{i+1} - AT_i$.

Figura 9.5 "The Concept of Interarrival Times": tabla con columnas Call, Arrival Time (AT_i), Interarrival Time (IA_i), 7 filas de datos (Call 1: 6:00:29, Call 2: 6:00:52, IA=00:23... hasta Call 7: 6:06:28). A la derecha, línea de tiempo (6:00-6:06) con flechas marcando la llegada de cada Call (1-7) y debajo llaves marcando los intervalos IA1 a IA6.

## Slide 15

**Proceso Estacionario de Llegadas**

Texto: define proceso estacionario de llegadas (el número esperado de llegadas depende del tamaño del intervalo, no del momento de inicio); proceso de llegadas Poisson = tiempo entre llegadas exponencial; estacionalidad implica que el proceso NO es estacionario.

Figura 9.6 "Seasonality over the Course of a Day": gráfico de línea, eje Y "Number of Customers per 15 Minutes" (0-160), eje X "Time" (0:15 a 23:00+). Muestra dos picos pronunciados de tráfico (uno cerca de las 7:15-9:00 llegando a ~100, otro más alto cerca de 16:00-17:45 llegando a ~155), con valles bajos en la madrugada — evidenciando estacionalidad intradía.

## Slide 16

**Datos de Llegadas**

Texto lateral: "Calcular los tiempos entre llegadas a partir de los tiempos de llegadas". Tabla 9.1 "Call Arrivals at An-ser on April 2, from 6:00 a.m. to 10:00 a.m.": tabla densa de timestamps de llamadas organizados en 10 columnas x ~65 filas (cientos de horas:minutos:segundos de llegada), representando el dataset crudo de llegadas usado en los ejemplos del capítulo.

## Slide 17

**Proceso de Llegadas**

Texto: análisis para determinar si un proceso es estacionario — la curva de tiempos de llegada acumulados no debe alejarse de la recta que une el primer y último punto del intervalo.

Figura 9.7 "Test for Stationary Arrivals": dos gráficos de dispersión/línea lado a lado. Izquierda: eje Y "Cumulative Customers" (0-700), eje X "Time" (6:00-10:00); muestra una línea recta negra ("Expected Arrivals if Stationary") y una curva gris ("Actual, Cumulative Arrivals") que se desvía de la recta (por debajo en el tramo medio), indicando cierta desviación de estacionariedad. Derecha: zoom del rango 7:15:00-7:30:00, con puntos negros dispersos que siguen de cerca una línea recta, mostrando comportamiento aproximadamente estacionario en ese sub-intervalo.

## Slide 18

**Distribución Exponencial de Tiempo entre Llegadas**

Texto + fórmula (en rojo):
$$\text{Probabilidad}[IA \le t] = 1 - e^{-t/a}$$
Donde a = tiempo promedio entre llegadas = desviación estándar del tiempo entre llegadas. Explica que si IA es exponencial, el proceso es Poisson, y la propiedad de "falta de memoria" (la siguiente llegada no depende de la más reciente).

## Slide 19

**Distribución Exponencial de Tiempo entre Llegadas**

Figura 9.8 "Distribution Function of the Exponential Distribution (left) and an Example of a Histogram (right)". Izquierda: curva de función de distribución acumulada exponencial (crece rápido y se aplana, de 0 a 1) con eje Y "Probability {Interarrival Time ≤ t}" y eje X "Time". Derecha: histograma de barras "Number of Calls with Given Duration t" (eje Y 0-100) vs "Duration t" (eje X 0-3.2), con forma decreciente característica de una distribución exponencial (barras altas cerca de 0, decayendo hacia la derecha).

## Slide 20

**Distribución Exponencial de Tiempo entre Llegadas**

Figura 9.9 "Empirical versus Exponential Distribution for Interarrival Times". Gráfico de dispersión: eje Y "Distribution Function" (0-1), eje X "Interarrival Time" (0:00:00 a 1:09). Puntos negros dispersos (datos empíricos individuales) que siguen de cerca la curva teórica suave etiquetada "Exponential Distribution", con la nube de puntos etiquetada "Empirical Distribution (Individual Points)" — muestra que el ajuste empírico-teórico es bueno.

## Slide 21

**Variabilidad del Tiempo de Procesamiento**

Figura 9.11 "Processing Times in Call Center". Histograma de barras: eje Y "Frequency" (0-800), eje X "Call Durations [Seconds]" (0-1000). Forma fuertemente asimétrica a la derecha (cola larga): pico alto (~690) cerca de 50-100 segundos, decayendo rápidamente y formando una cola larga de baja frecuencia hasta 1000 segundos.

## Slide 22

**Tiempos de Procesamiento con Estacionalidad**

Figura 9.12 "Average Call Durations: Weekday versus Weekend". Gráfico de líneas: eje Y "Call Duration [Minutes]" (0-2.5), eje X "Time of the Day" (0:00-23:00). Dos series: línea punteada "Weekend Averages" (oscila entre ~1.1 y ~2.2 min, generalmente más alta) y línea sólida "Weekday Averages" (oscila entre ~0.8 y ~1.8 min, generalmente más baja) — evidenciando estacionalidad por día de la semana en la duración de llamadas.

## Slide 23

**Variabilidad del Tiempo de Procesamiento**

Texto: unidades llegan con patrón de demanda aleatorio. Fórmulas (rojo): a = 1/λ = Tiempo esperado entre Llegadas; Tasa de Flujo de Llegadas (Flow Rate) = R = λ = 1/a.

Figura 9.13 "A Simple Process with One Queue and One Server": diagrama de flujo con flecha "Inflow" → triángulo (buffer/cola) → flecha → cuadrado (servidor) → flecha "Outflow". Debajo, línea de tiempo con marcas "Entry to System", "Begin Service", "Departure".

## Slide 24

**Tiempo de Espera Promedio con 1 Recurso**

Texto + fórmulas (rojo): p = Tiempo Promedio de Procesamiento; Capacidad del Servidor = 1/p; Utilización (u) = Flow Rate/Capacidad = (1/a)/(1/p) = p/a < 100%.

Repite Figura 9.13 (mismo diagrama de cola-servidor único descrito en Slide 23).

## Slide 25

**Tiempo de Espera Promedio con 1 Recurso**

Texto + fórmulas (rojo): Tq = Tiempo de Espera en la Cola; Tiempo de Flujo: T = Tq + p.

Figura 9.14 "A Simple Process with One Queue and One Server": diagrama similar al 9.13 pero con detalle adicional — triángulo con 3 puntos negros etiquetado "Inventory Waiting Iq", cuadrado con 1 punto negro etiquetado "Inventory in Service Ip". Debajo, línea de tiempo con marcadores "Entry to System", "Begin Service", "Departure" y llaves dobles indicando "Waiting Time Tq", "Processing Time p", y en la fila inferior el total "Flow Time T = Tq + p".

## Slide 26

**Tiempo de Espera Promedio con 1 Recurso**

Texto + fórmulas (rojo): Iq = Inventario en la Cola; Ip = Inventario en Proceso; I = Inventario Total (WIP); I = Iq + Ip.

Repite Figura 9.14 (mismo diagrama descrito en Slide 25).

## Slide 27

**Tiempo de Espera Promedio con 1 Recurso**

Texto: para un proceso estacionario, el tiempo de espera en cola depende de 3 factores (tiempo de procesamiento, % utilización, variabilidades de llegada y servicio); no requiere distribución estadística específica.

Fórmula central (rojo):
$$T_q = p \cdot \left[\frac{\text{Utilización}}{1-\text{Utilización}}\right] \cdot \left[\frac{CV_a^2 + CV_p^2}{2}\right]$$

## Slide 28

**Ejemplo – Call Center**

Enunciado: recepcionista 2am-3am, llamada promedio 90 seg, desviación estándar 120 seg, 3 llamadas en 15 minutos.
a) Tiempo entre llegadas, b) % Utilización.
Cálculos: a = 15/3 = 5 min = 300 seg; p = 90 seg; σp = 120 seg; Utilización = p/a = 90/300 = 0.3 = 30%.

## Slide 29

**Ejemplo – Call Center**

Continuación: llegadas Poisson (CVa=1). Calcular Tq y T.
$$T_q = 90 \cdot \left[\frac{0.3}{1-0.3}\right] \cdot \left[\frac{1^2+(120/90)^2}{2}\right] = 53.57 \text{ segundos}$$
T = Tq + p = 53.57 + 90 = 143.57 segundos.

## Slide 30

**Ejemplo – Call Center**

Calcular inventario promedio en el sistema. Por Ley de Little: I = R·T = 1/a(Tq+p). R = 1/300 unidades/segundo. T = 143.57 seg. I = 143.57/300 = 0.479 unidades.

## Slide 31

**Ejemplo – Call Center**

Calcular inventario promedio en la cola. Iq = R·Tq = Tq/a. R = 1/300 unidades/segundo. Tq = 53.57 seg. Iq = 53.57/300 = 0.179 unidades.

## Slide 32

**Ejemplo – Call Center**

Calcular número promedio de llamadas en servicio. Ip = Prob[0 llamadas]×0 + Prob[1 llamada]×1 = (1-u)×0 + u×1 = u. Ip = 0.3 llamadas.

## Slide 33

**Tiempo de Espera Promedio con Múltiples Recursos**

Figura 9.15 "A Process with One Queue and Multiple, Parallel Servers (m = 5)". Diagrama de flujo: flecha "Inflow" → triángulo (cola única) → flecha → caja rectangular con 5 pequeños cuadrados grises apilados verticalmente (representando 5 servidores en paralelo) → flecha "Outflow". Línea de tiempo abajo con "Entry to System", "Begin Service", "Departure".

## Slide 34

**Tiempo de Espera Promedio con Múltiples Recursos**

Fórmulas (rojo):
- Capacidad = m/p
- Utilización = Tasa de Flujo/Capacidad = (1/a)/(m/p) = p/(a×m)
- Flow Time = T = Tq + p
- $$T_q = \frac{p}{m}\left[\frac{\text{Utilización}^{\sqrt{2(m+1)}-1}}{1-\text{Utilización}}\right]\left[\frac{CV_a^2+CV_p^2}{2}\right]$$
- I = Ip + Iq
- Inventario en Proceso = Número de Recursos × Utilización
- Ip = m·u = p/a
- Iq = R·Tq = (1/a)·Tq

## Slide 35

**Tiempo de Espera Promedio con Múltiples Recursos**

Figura 9.16 "Summary of Key Performance Measures". Diagrama de flujo detallado: flecha "Inflow" → rectángulo punteado "Inventory in the System I = Iq + Ip" que contiene: una fila de 8 círculos negros dentro de un marco gris etiquetada "Inventory Waiting Iq" (cola), y a la derecha una columna de 4 cuadrados grises con puntos negros etiquetada "Inventory in Service Ip" (servidores ocupados) → flecha "Outflow". Debajo, línea de tiempo con "Entry to System", "Begin Service", "Departure" y marcadores de "Waiting Time Tq", "Processing Time p", y total "Flow Time T = Tq + p".

## Slide 36

**Ejemplo de Tiempo de Espera Promedio con Múltiples Recursos**

Enunciado: banco, 79 clientes en 8:00-8:15am, 10 ventanillas, tiempo atención promedio 1.5 min, desviación estándar 2 min, tiempo entre llegadas exponencial. Datos: σp=2 min, p=1.5 min, m=10, a = 15×60/79 = 11.39 seg, u = p/(am) = 90/(11.39×10) = 0.79, CVp = σp/p = 2/1.5 = 1.33, CVa = 1.

## Slide 37

**Ejemplo de Tiempo de Espera Promedio con Múltiples Recursos**

Aplicación de la fórmula de Tq con múltiples recursos:
$$T_q = \frac{90}{10}\left[\frac{0.79^{\sqrt{2(11)}-1}}{1-0.79}\right]\left[\frac{1^2+1.33^2}{2}\right] = 24.94 \text{ segundos}$$

## Slide 38

**Caso de Tiempo de Espera Promedio con Múltiples Recursos**

Enunciado de caso (datos del Call Center en Excel, 6:00-10:00am, 10 recepcionistas, p=3 min, σp=5 min). Pide calcular: a) tiempo esperado entre llegadas, b) tasa de flujo, c) % utilización, d) tiempo de espera en cola, e) tiempo de flujo, f) inventario en servicio, g) inventario en cola, h) inventario total, i) número mínimo de recepcionistas para Tq < 1 minuto.

## Slide 39

**Tiempo de Espera Promedio con Múltiples Recursos**

Resolución del caso (a-d): σp=5 min, p=3 min, m=10.
a) Intervalo=4h, 687 llamadas, a=20.89 seg.
b) R = 1/a = 2.87 clientes/minuto.
c) u = p/(am) = (3×60)/(20.89×10) = 86.17%.
d) CVp=1.667, CVa=1.275 (de Excel). Tq calculado con la fórmula de múltiples recursos = 2.76 minutos.

## Slide 40

**Tiempo de Espera Promedio con Múltiples Recursos**

Resolución del caso (e-i):
e) T = Tq + p = 2.76 + 3 = 5.76 minutos
f) Ip = m×u = 10×0.8617 = 8.617 clientes
g) Iq = R×Tq = 2.87×2.76 = 7.92 clientes
h) I = Ip + Iq = 16.53 clientes
i) m = 12 recepcionistas → Tq = 0.502 minutos = 30.12 segundos.

## Slide 41

**Nivel de Servicio para los Tiempos de Espera**

Texto + fórmula (rojo): Nivel de Servicio = Probabilidad[t de espera ≤ tiempo límite]. Ejemplo: Nivel de Servicio = Prob[t de espera ≤ 3 minutos] = 95%.

## Slide 42

**Nivel de Servicio para los Tiempos de Espera**

Figura 9.17 "Empirical Distribution of Waiting Times at An-ser". Gráfico de dispersión: eje Y "Fraction of Customers Who Have to Wait x Seconds or Less" (0-1), eje X "Waiting Time [Seconds]" (0-200). Muchos puntos apilados verticalmente en x=0 (etiquetados "Fraction of Customers Who Get Served Without Waiting at All", llegando hasta ~0.7), y luego puntos dispersos ascendentes hacia la derecha (etiquetados "Waiting Times for Those Customers Who Do Not Get Served Immediately") que se acercan asintóticamente a 1.

## Slide 43

**Trade-Off entre el Tiempo de Espera y el Número de Servidores**

Texto: costos a considerar en el análisis (costo de espera, costo del servicio, costo de clientes que se retiran, costo de llamadas "ocupado"). Fórmula (rojo): Costo de M.O. Directa = Salario Total/Tasa de Flujo.

## Slide 44

**Trade-Off entre el Tiempo de Espera y el Número de Servidores**

Figura 9.18 "Economic Consequences of Waiting". Diagrama de flujo: "Incoming Calls" entra al sistema, se bifurca hacia "Blocked Calls (Busy Signal)" (llamadas rechazadas) o hacia el recuadro punteado "Call Center" que contiene triángulo "Calls on Hold" → caja "Sales Reps Processing Calls" → "Answered Calls" (salida). Desde "Calls on Hold" también sale una flecha hacia abajo a "Abandoned Calls (Tired of Waiting)". Debajo, tabla "Financial Consequences" con 4 columnas: Lost Throughput/Lost Goodwill; Holding Cost (Line Charges)/Lost Goodwill/Lost Throughput (Abandoned); Cost of Capacity; Revenue.

## Slide 45

**Trade-Off entre el Tiempo de Espera y el Número de Servidores**

Enunciado de ejemplo: costo recepcionista 10 US$/hora, servicio 1-800 a 0.05 $/minuto (aplicado a espera y atención), meta de contestar en 10 seg promedio, duración de llamada 3 min promedio. Pide elaborar tabla de tiempo de espera esperado vs número de recepcionistas (rango 8:00-8:15am de datos Excel).

## Slide 46

**Trade-Off entre el Tiempo de Espera y el Número de Servidores**

Datos del ejemplo: σp=5 min, p=3 min, Costo de Llamada 1-800=0.05 US$/min, Costo de Recepcionista=10 US$/hora, Tiempo de Espera deseado ≤10 seg, Hora 8:00-8:15am (900 seg), 42 clientes (de hoja de cálculo 5), a=19.49 seg/cliente, R=60/19.49=3.08 clientes/minuto, CVp=5/3=1.667, CVa=0.954 (obtenido de hoja de cálculo 5).

## Slide 47

**Trade-Off entre el Tiempo de Espera y el Número de Servidores**

Captura de hoja de cálculo Excel "Trade-Off entre Tiempos de Espera y Número de Servidores": tabla con celdas amarillas/naranjas mostrando los parámetros: σp=5 min, p=3 min, Hora Inicial=08:00:00am, Hora Final=08:15:00am, Tamaño del intervalo=900 seg, Número de Clientes=42, a (sin datos de llamadas)=21.43 seg/cliente, a (con datos)=19.49 seg/cliente (resaltado como el valor usado para todos los cálculos, con flecha indicadora), R=3.08 clientes/minuto, CVp=1.667, CVa (rango 8:00-8:15am)=0.954 (con nota "Se obtiene del rango de tiempo entre llamadas de 8:00 am a 8:15 am"). Abajo: Costo de Llamada 1-800=0.05 US$/minuto, Costo de Recepcionista=10 US$/hora×recepcionista, Tiempo de Espera Deseado ≤10 segundos.

## Slide 48

**Trade-Off entre el Tiempo de Espera y el Número de Servidores**

Tabla completa (captura de Excel) "Importante: Se está considerando los datos de las llamadas de 8:00am a 8:15am":

| m | % Utilización (u=p/am) | Tq (segundos) | Costo M.O. por Llamada | Costo Línea por Llamada | Costo Total por Llamada |
|---|---|---|---|---|---|
| 1 | 923.65% | -372.21 | — | — | — |
| 2 | 461.83% | -421.36 | — | — | — |
| 3 | 307.88% | -415.97 | — | — | — |
| 4 | 230.91% | -387.13 | — | — | — |
| 5 | 184.73% | -355.46 | — | — | — |
| 6 | 153.94% | -334.67 | — | — | — |
| 7 | 131.95% | -340.94 | — | — | — |
| 8 | 115.46% | -427.78 | — | — | — |
| 9 | 102.63% | -1,535.44 | — | — | — |
| 10 | 92.37% | 324.31 | 0.5413 | 0.4203 | 0.9616 |
| 11 | 83.97% | 95.23 | 0.5955 | 0.2294 | 0.8248 |
| 12 | 76.97% | 41.08 | 0.6496 | 0.1842 | 0.8338 |
| 13 | 71.05% | 20.34 | 0.7037 | 0.1670 | 0.8707 |
| 14 | 65.98% | 10.83 | 0.7579 | 0.1590 | 0.9169 |
| 15 | 61.58% | 6.02 | 0.8120 | 0.1550 | 0.9670 |
| 16 | 57.73% | 3.45 | 0.8661 | 0.1529 | 1.0190 |
| 17 | 54.33% | 2.02 | 0.9203 | 0.1517 | 1.0719 |

Nota destacada: "Número de Recepcionistas necesarias para que el tiempo esperado en la cola (Tq) sea menor a 10 segundos" — la fila m=15 (Tq=6.02, resaltada en naranja) es la primera que cumple Tq<10 segundos. Las filas m=1 a 9 muestran utilización >100% (sistema saturado, Tq negativo sin sentido físico, celdas sombreadas indicando que no aplican costos).

## Slide 49

**Número de Servidores y Número de Clientes por Rango Horario**

Figura 9.19 "Staffing and Incoming Calls over the Course of a Day". Gráfico combinado: eje Y izquierdo "Number of Customers per 15 Minutes" (0-160), eje Y derecho "Number of CSRs" (Customer Service Reps, escala 1-17), eje X "Time" (0:15-23:00+). Línea negra de llamadas por 15 min con dos picos (uno ~100 hacia las 7:15-9:00, otro más alto ~155 hacia las 16:00-17:45). Superpuesto, un histograma de barras grises en escalones representa el número de CSRs asignados por franja horaria, que sube y baja siguiendo aproximadamente la curva de demanda (más servidores en las horas pico, menos en la madrugada) — ilustrando el dimensionamiento de personal según la demanda variable a lo largo del día.
