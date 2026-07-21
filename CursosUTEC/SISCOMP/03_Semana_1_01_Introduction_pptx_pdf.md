---
curso: SISCOMP
titulo: 03 - Semana 1/01.Introduction.pptx
slides: 22
fuente: 03 - Semana 1/01.Introduction.pptx.pdf
---

## Slide 1

Portada (decorativa: fondo azul de túnel tecnológico con silueta de robot humanoide).

Título: **COMPUTER SYSTEMS**
Subtítulo: MOTIVATION

## Slide 2

Título: **Goals**

Analyze the principal concepts of the course and the historical perspective.

(Imagen decorativa: científica de laboratorio con gafas de protección y tubos de ensayo, tratada en azul.)

## Slide 3

Título: **Summary**

Índice del capítulo en dos columnas, cada ítem con un icono lineal:

| # | Tema | # | Tema |
|---|------|---|------|
| 1. | Course motivation (icono portapapeles) | 4. | Trends (icono gráfico de barras) |
| 2. | Performance (icono bombilla) | 5. | Challenges (icono diana/personas) |
| 3. | History (icono bombilla) | 6. | Conclusions (icono diana/personas) |

(Fondo decorativo: mujer con visor de realidad virtual y globo terráqueo digital.)

## Slide 4

Slide separador de sección.

**1. Course Motivation**

(Imagen decorativa: mano robótica tocando un globo terráqueo digital.)

## Slide 5

Título: **Why we study Computer Systems?**

- Have an idea of how computers work.
- Be familiar with system programming.
- Better understand performance and system tools.

(Imagen: meme de un gato con lentes redondos frente a un laptop, con texto "HAPPY STUDYING!!". Banner superior decorativo con foto de equipo de trabajo mirando una laptop.)

## Slide 6

Slide separador de sección.

**2. Performance**

(Imagen decorativa: mano robótica tocando globo terráqueo digital.)

## Slide 7

Título: **Let's look at an example**

Tabla de especificaciones de una MacBook Pro:

| Feature | Specification |
|---------|---------------|
| Model | MacBook Pro 9,1 |
| Processor | Quad-Core Intel Core i7 |
| Processor Speed | 2,3 GHz |
| Number of processors | 1 |
| Number of cores | 4 |
| Floating-point Operations per Cycle | 4 |
| L2 Cache (per core) | 256 KB |
| L3 Cache | 6 MB |
| Hyper-Threading Technology | Enables |
| Memory | 8 GB |

Recuadro azul resaltado (cálculo del rendimiento pico):

**Best effort mode: 2.3 G × 1 × 4 × 4 = 36 800 MFLOPS**

$$\text{Rendimiento} = \text{freq} \times N_{proc} \times N_{cores} \times \text{FLOP/ciclo} = 2.3\,\text{GHz} \times 1 \times 4 \times 4 = 36\,800\ \text{MFLOPS}$$

## Slide 8

Título: **Best effort is also call _performance_**

Diagrama infográfico en zigzag: cinco círculos con iconos descienden en diagonal (lupa, diana, cohete, calendario, cadena/enlace), cada uno enlazado a un bloque de texto alternando izquierda/derecha. Los cinco factores que determinan el rendimiento:

- **What performance is:** (icono lupa) Efficiency with a computer system performs a task.
- **Programming:** (icono diana) Language, compiler and architecture. Determines the number of computer instructions for each source-level.
- **Algorithm:** (icono cohete) Is the first step. Determines both source-level statements and I/O operations need to be executed.
- **Processor and memory system:** (icono calendario) How fast instructions can be executed improves the performance.
- **I/O System:** (icono enlace) I/O operations are bottlenecks. How fast I/O operations can be executed improves the performance.

## Slide 9

Slide separador de sección.

**3. History**

(Imagen decorativa: mano robótica tocando globo terráqueo digital.)

## Slide 10

Título: **0th generation: Mechanics**

- Designed by Charles **Babbage** (1834).
- Mechanical **gears**: Discrete values.
- Programs: **Punched** cards.
- **Technological** restrictions.

(Imagen: fotografía de "The Analytical Engine" de Babbage, máquina de bronce con engranajes y varillas verticales en una vitrina de museo.)

Fuente: https://www.computerhistory.org/babbage/

## Slide 11

Título: **1st generation: Vacuum tubes**

- 1945: ENIAC, Colossus.
- Machine **language.**
- **Punched** cards, boards and wires.
- **Store** concept.

Diagrama de bloques de la arquitectura (modelo von Neumann): un bloque **Input** (arriba) apunta hacia abajo a un recuadro contenedor que incluye a la izquierda **Arithmetical / Logic Unit** y **Control Unit**, y a la derecha **Memory**; flechas bidireccionales conectan la ALU/Control Unit con Memory. Del contenedor sale una flecha hacia abajo al bloque **Output**.

```
        Input
          |
          v
  +----------------------------+
  | [Arithmetical/Logic Unit] ->  [Memory]
  | [Control Unit]            <-  [Memory]
  +----------------------------+
          |
          v
        Output
```

## Slide 12

Título: **2nd generation: Transistors**

- 1955: IBM 7094 (**mainframes**).
- **Assembly** language and **FORTRAN**.
- **I/O** separated from calculations.
- **Punched** cards and **magnetic** tape.
- **Loaders** (OS ancestors)

(Dos fotografías históricas en blanco y negro: izquierda, operadora sentada frente a una consola de sistema de procesamiento de datos con impresora — "Property of Museum of History & Industry, Seattle"; derecha, dos técnicos trabajando en un mainframe TRADIC con paneles de cableado.)

## Slide 13

Título: **3rd generation: Integrated Circuits**

- 1965: IBM 360 (**Instruction set architecture**).
- **First** Operating Systems (OS/360 MULTICS).
- **Multiprogramming.**
- Programming **languages** and **compilers** (BASIC, C).

Diagrama: bloque de memoria dividido verticalmente en cuatro particiones apiladas — de arriba a abajo **Job 3**, **Job 2**, **Job 1**, **Operating System** — con flechas que salen de la derecha etiquetadas **Memory Partitions**. A la izquierda, fotografía de un chip DIP (circuito integrado con patas). Ilustra la multiprogramación: el SO y varios trabajos residentes en particiones de memoria.

## Slide 14

Título: **4th generation: VLSI and PCs**

- 1980: Personal Computers (**Apple, IBM**).
- **Architectures:** x86-64, ARM, MIPS, PowerPC, SPARC, RISC-V.
- **Operating Systems:** UNIX, MINIX, Linux, MacOS, DOS, Windows.
- **ISA** (CISC, RISC): Cache, pipeline, SIMD, hyperthreading, multicore.

(Dos imágenes: arriba, primer plano de un chip VLSI montado en una placa de circuito impreso; abajo, foto en blanco y negro de una PC IBM de los 80 con monitor, unidad y teclado.)

## Slide 15

Slide separador de sección.

**4. Trends**

(Imagen decorativa: mano robótica tocando globo terráqueo digital.)

## Slide 16

Título: **Some trends**

Texto izquierdo:
Scaling on electronics continues to evolve:
- Increased **capacity** and **performance**.
- Reduced **cost**.

**Moore's law says:**
Number of transistors on a computer chip doubles every year (since 1965).

Consecuencias (con flechas de bloque):
- Limited by **power** consumption.
- Slow **down** since 2010.

Gráfico "Memory Capacity" (arriba derecha): línea ascendente de capacidad de memoria DRAM en escala logarítmica. Eje Y = Kbit capacity (10 a 10,000,000); eje X = Year of introduction (1976 a 2012). Puntos etiquetados progresivamente: 16K, 64K, 256K, 1M, 4M, 16M, 64M, 128M, 256M, 512M, 1G, 2G, 4G — mostrando el crecimiento exponencial de la capacidad.

## Slide 17

Título: **Some performance graphics**

Tres gráficos históricos de tendencias de procesadores (Hennessy & Patterson):

1. **Izquierda — Rendimiento vs. tiempo (1978-2018), escala log.** Curva de rendimiento relativo de procesadores. Anotada con tasas de mejora por época: 25%/year (inicio), 52%/year (~1986-2003), 23%/year, 12%/year, y 3.5%/year (final). Flecha roja "Move to multicore" señala ~2004-2005 (Intel Core Duo Extreme 2 cores). Listado de máquinas hito desde VAX 8700 y MIPS hasta Intel Core i7 4 cores 4.2 GHz. Muestra el estancamiento del single-thread.

2. **Arriba derecha — Clock Rate y Power vs. modelo de CPU (80286 1982 → Ivy Bridge 2012).** Doble eje: Clock Rate (MHz, línea celeste) y Power (watts, línea negra). El clock sube de 12.5 MHz hasta ~3600 MHz (Pentium 4 Prescott 2004) y luego se estanca (2667, 3300, 3400); la potencia sube hasta ~103 W y luego baja (95, 87, 77). Ilustra el "power wall".

3. **Abajo derecha — Processor vs. Memory gap (1980-2015), escala log.** Dos curvas: "Processor" crece rápidamente hasta ~2005 y se aplana en ~10,000; "Memory" crece muy lentamente hasta ~10. Ilustra la creciente brecha procesador-memoria (memory wall).

## Slide 18

Slide separador de sección.

**5. Challenges**

(Imagen decorativa: mano robótica tocando globo terráqueo digital.)

## Slide 19

Título: **What we can do now?**

1. **No more single core performance improvement**
   - More powerful microprocessor might not help.
2. **Memory-efficient programming**
   - Temporal and spatial locality.
3. **Parallelism**
   - Data-level, thread-level, request-level to improve performance.
4. **Application**

## Slide 20

Título: **Conclusions**

To create software that works **efficiently** with big data, it is necessary to understand how the hardware is **organized** and **managed** by an operating system.

- Computer architecture.
- Assembly language.
- Operating systems.

Diagrama derecho: pila de niveles de abstracción de un sistema de cómputo (de arriba abajo), cada nivel con un icono representativo:
- **Application Software** — `>"hello world!"`
- **Operating Systems** — laptop
- **Architecture** — registros/instrucciones
- **Micro-architecture** — bloques con flechas de datapath
- Logic — compuerta con "+"
- Digital Circuits — compuerta AND
- Analog Circuits — amplificador
- Devices — transistor
- Physics — átomo

Un recuadro azul resaltado agrupa los cuatro niveles superiores (Application Software, Operating Systems, Architecture, Micro-architecture), que son el foco del curso.

## Slide 21

Título: **Reference Books**

Bibliografía (cada entrada con flecha azul):

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface*. Morgan Kaufmann.
- "*The elements of computing systems: building a modern computer from first principles*" Nisan, N., & Schocken, S. (2021). MIT press.
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). *Operating system concepts* (9th edition, international student version). John Wiley & Sons Inc.
- "*Digital Design and Computer Architecture, RISC-V Edition*". Morgan Kaufmann. Harris, S., & Harris, D. (2021).

(Imagen decorativa: profesor escribiendo en una pizarra frente a estudiantes, tratada en azul.)

## Slide 22

Slide de cierre (decorativa: fondo azul de laboratorio con dos estudiantes trabajando en un equipo mecánico/telar).

Título: **Questions?**
Ponente: PhD. (C) Luz Adanaqué
