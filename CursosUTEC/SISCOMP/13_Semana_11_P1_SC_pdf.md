---
curso: SISCOMP
titulo: 13 - Semana 11/P1_SC
slides: 14
fuente: 13 - Semana 11/P1_SC.pdf
---

## Slide 1

Portada (decorativa: fondo de túnel tecnológico azul con silueta de robot humanoide, plantilla TransformaTec/UTEC).

Título: **COMPUTING SYSTEMS**

Subtítulo:
- Final Project
- Professor: Luz A. Adanaqué

## Slide 2

Slide de sección "Goal" (foto decorativa de científica en laboratorio a la izquierda).

**Goal**

Implement a kernel to manage three processes related to remote sensing on a satellite.

## Slide 3

Slide de agenda "Summary" (foto decorativa de mujer con visor VR y globo terráqueo digital).

**Summary**

| # | Ítem |
|---|------|
| 1. | Context (icono de portapapeles) |
| 2. | OS Management (icono de bombilla) |
| 3. | Final presentation (icono de bombilla) |

## Slide 4

**Project Tasks** (slide solo texto sobre fondo blanco)

1. **Processes**
   Implement processes related to remote sensing of parameters, detection of out-of-range values, and communication of received data.

2. **Scheduler**
   Implement a scheduler capable of managing process priorities, first in an imposed manner and then automatically through syscalls.

3. **OS Application**
   Integrate processes and the scheduler into an application hosted on an operating system, capable of operating manually or automatically, taking into account best practices for control and access to information.

## Slide 5

Slide divisor de sección (foto decorativa de mano robótica tocando un globo digital a la derecha).

**1.** Context (icono de portapapeles)

## Slide 6

**Satellite System**

Contenido visual (diagrama): en el centro-derecha hay un diagrama orbital. Muestra el **Sol** (icono, arriba) emitiendo rayos hacia una órbita elíptica dibujada alrededor de la **Tierra** (icono de globo, a la derecha del centro). Sobre la elipse, a la izquierda, está el **satélite** (icono con paneles solares y antena) acompañado de un icono de **termómetro** que representa el sensor de temperatura. La mitad superior de la órbita está etiquetada como **"Bright Area"** (lado iluminado por el Sol) y la mitad inferior como **"Dark Area"** (lado en sombra).

Texto (columna izquierda):

1. **Temperature sensor:**
   - Sensing time: every 5 minutes
   - Transmission data time: 1 minute

2. **LEO Orbit: 100 minutes:**
   - Bright Area: 42 minutes
   - Dark Area: 58 minutes

## Slide 7

**Processes** (slide de texto)

**Process 1:**
Temperature signal acquisition process: enter data corresponding to the temperature, which ranges from 45°C to 105°C during a LEO orbit, which lasts around 100 minutes (for testing purposes, this time can be shortened). Be sure to insert some data into this process that generates anomalies in the temperature value to trigger the deployment of cooling techniques and their subsequent restoration.

**Process 2:**
Process that deploys the cooling technique used whenever the reading from process 1 exceeds the 90°C, and it turn off when the temperature is 60°C. This process must display warnings via alerts when it is activated and deactivated.

**Process 3:**
Process that displays the reading received from the sensor (with UART protocol), originating from process 1. This reception must be based on a serial communication protocol.

Recuadro resaltado (banda azul clara al pie):
> Cada proceso debe ser desarrollado mediante la perspectiva de procesador y diseño de hardware en RISC - V, estableciendo trade-offs

## Slide 8

Slide divisor de sección (foto decorativa de mano robótica tocando globo digital a la derecha).

**2.** OS Management (icono de portapapeles)

Texto: El scheduler en el sistema operativo debe gestionar los siguientes escenarios de manera rápida y con alta performance.

## Slide 9

**1st Scenario: Baseline**

Texto: In this scenario, all processes run sequentially, without any priority associated with their operation. The OS must be able to detect which process is being performed through a request.

Contenido visual (diagrama de Gantt / cronograma de procesos): eje vertical etiquetado **PROCESSES**, eje horizontal **t (min)**. Se repite un patrón en cascada de tres bloques por ciclo, siempre en el mismo orden vertical descendente:
- **P1** (bloque amarillo, arriba) con etiqueta de estado al lado.
- **P2** (bloque verde, medio).
- **P3** (bloque rosado, abajo).

La secuencia siempre es P1 → P2 → P3 (secuencial, sin prioridades). Las etiquetas de estado junto a cada P1 marcan si el enfriamiento (P2) está ON/OFF en ese instante:
- En t≈5: P1 **OFF**
- En t≈10: P1 **ON**
- (puntos suspensivos "○ ○ ○" indican continuación)
- En t≈42: P1 **ON**
- Hacia el final: P1 **OFF**
- En t≈100: P1 **OFF**

Marcas de tiempo en el eje: 5, 10, 42, 100. Debajo, una flecha divide el eje en dos regiones: **ZONA LUMINOSA** (izquierda, hasta ~42) y **ZONA OSCURA** (derecha).

## Slide 10

**2nd Scenario**

Texto: In this scenario, an order of priorities is imposed, the scheduler must be able to switch between processes, and the OS must indicate if there is any loss of information due to the abrupt change between non-consecutive processes.

Contenido visual (diagrama de Gantt): mismo formato que el slide 9 pero con **orden de prioridades cambiado**. El orden vertical descendente de los bloques ahora es:
- **P1** (amarillo, arriba)
- **P3** (rosado, medio) — con etiqueta de estado al lado
- **P2** (verde, abajo)

Es decir la secuencia es P1 → P3 → P2, saltando de proceso no consecutivo (de P1 a P3). Etiquetas de estado junto a P3:
- En t≈5: **OFF**
- En t≈10: **ON**
- (puntos suspensivos)
- En t≈42: **OFF**
- En t≈95: **OFF**

Marcas de tiempo: 5, 10, 42, 95, 100. Regiones: **ZONA LUMINOSA** / **ZONA OSCURA**.

## Slide 11

**3rd Scenario**

Texto (idéntico al 2nd): In this scenario, an order of priorities is imposed, the scheduler must be able to switch between processes, and the OS must indicate if there is any loss of information due to the abrupt change between non-consecutive processes.

Contenido visual (diagrama de Gantt): mismo formato, con **otro orden de prioridades**. El orden vertical descendente de los bloques es:
- **P2** (verde, arriba)
- **P1** (amarillo, medio)
- **P3** (rosado, abajo)

Secuencia P2 → P1 → P3. Este ciclo se repite 4 veces a lo largo del eje (con puntos suspensivos "○ ○ ○" entre los grupos centrales). En este scenario no se muestran etiquetas ON/OFF.

Marcas de tiempo: 5, 10, 42, 95, 100. Regiones: **ZONA LUMINOSA** / **ZONA OSCURA**.

## Slide 12

**4th Scenario: Syscalls**

Texto: In this scenario, the application runs automatically, i.e., data is transmitted continuously, respecting its times and ranges, then a communication flag is activated and syscalls are generated to switch to the other processes. The OS must be able to store the value of the PC where the current process stopped and resume it when the system call is finished executing.

Contenido visual (diagrama de Gantt): eje vertical **PROCESSES**, horizontal **t (min)**. Aquí **P1 (amarillo) es el proceso base que corre de forma continua/prolongada** — sus bloques son mucho más anchos que en los scenarios previos (representa transmisión continua). Cada vez que salta a otro proceso aparece debajo un bloque estrecho **P2** (verde) y luego **P3** (rosado). El patrón:
- Al inicio (t≈5 y t≈6): P1 corto, luego P3.
- En t≈10: P1 corto seguido de P2 y P3.
- Después: bloques **P1 muy anchos** intercalados con pares P2 (verde) + P3 (rosado) al final de cada ejecución de P1.

Marcas de tiempo: 5, 6, 10, 100. Regiones: **ZONA LUMINOSA** / **ZONA OSCURA**.

## Slide 13

**Handling Data**

Texto: As one process is interrupted by other, is necessary to handle information about PC (and the stack) and the status execution of the current process in order to continue the execution of the interrupted process.

Contenido visual (mismo diagrama de Gantt del slide 12, con anotaciones añadidas): en la transición central donde un bloque **P1 ancho** es interrumpido, se resaltan **dos rectángulos con borde rojo** etiquetados **"PC" y "PC"** justo en el punto de corte/reanudación de P1. Ilustran que al interrumpir el proceso se guarda el valor del Program Counter (y el stack) para poder retomar la ejecución. El resto del diagrama es igual: bloques anchos de P1 (amarillo) intercalados con P2 (verde) y P3 (rosado).

Marcas de tiempo: 5, 6, 10, 100. Regiones: **ZONA LUMINOSA** / **ZONA OSCURA**.

## Slide 14

**Reference Books** (foto decorativa de profesor escribiendo en pizarra a la derecha). Lista con flechas azules:

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). *Operating system concepts* (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).
