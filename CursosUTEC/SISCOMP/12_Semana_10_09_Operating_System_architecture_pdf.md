---
curso: SISCOMP
titulo: 12 - Semana 10/09. Operating System architecture
slides: 15
fuente: 12 - Semana 10/09. Operating System architecture.pdf
---

## Slide 1

Portada (decorativa: silueta con brazo robótico en túnel de datos azul).

**COMPUTING SYSTEMS**

Operating System architecture
Professor: Luz A. Adanaqué

Based on lecture notes by Prof. Jorge Gonzalez

## Slide 2

Slide de texto (imagen decorativa: científica de laboratorio con guantes y gafas manipulando tubos de ensayo).

**Motivation**
To understand how operating system architecture defines its functionality and performance.

To recognize how design choices affect stability and modularity.

**Goals**
Identify and describe main OS architecture types.

## Slide 3

Índice / Summary (imagen decorativa: mujer con visor de realidad virtual sobre globo terráqueo digital). Cada punto tiene un ícono a su izquierda.

**Summary**

1. (ícono de portapapeles/checklist) **Definitions**
2. (ícono de bombilla) **Fundamentals**
3. (ícono de bombilla) **OS Structure**

## Slide 4

Slide divisoria de sección (imagen decorativa: mano robótica tocando un globo digital).

**1. Definitions** (con ícono de portapapeles)

## Slide 5

**Recall: The Operating System**

- Definition
  - **A program that controls** the **execution of application** programs
  - An **interface** between **applications and hardware**
- With 3 important keys:
  - **Convenience**: Simple to use, from the programmer's perspective
  - **Efficiency**: Important metric related to the specific task
  - **Ability to evolve**: Permits the effective development, testing, and introduction of new system functions without interfering with service.

**Visual (diagrama a la derecha — "OS Abstraction layers and their Interfaces"):** Diagrama de capas apiladas de la arquitectura de un sistema. De arriba hacia abajo, tres bloques verdes: **Application programs**, **Libraries/utilities**, **Operating system**. Debajo, bloques grises de hardware: **Execution hardware**, y en la fila inferior **System interconnect (bus)** junto con **Memory translation**, y más abajo **I/O devices and networking** junto con **Main memory**.

A la izquierda del diagrama hay etiquetas de las interfaces marcadas con líneas de colores que cortan horizontalmente entre las capas:
- **AP** (verde) — nivel de Application programs
- **AB** / **I** (azul) — interfaz entre libraries/utilities y aplicaciones (ABI/API)
- **IS** (rojo) — interfaz al sistema operativo
- **A** (rojo, línea que separa el OS del hardware de ejecución)

Muestra que cada capa se comunica con la de abajo a través de una interfaz bien definida (AP = interfaz de programa de aplicación, ISA/ABI, etc.).

## Slide 6

**OS Four Main Features** (lista numerada; en el original los cuatro aparecen numerados "1." por bug de plantilla, pero son 4 features distintos)

1. **Memory Protection**
   - User programs **can't modify** OS or other programs' memory.
   - Enforced by policy (abort, show error, etc.).
2. **Timing Control**
   - A **timer** is set for each job.
   - When it expires, the OS **stops** the program.
   - Prevents CPU overuse or infinite loops.
3. **Privileged Instructions**
   - Only the **OS** can execute them (subset of ISA).
   - If used by a user program → **error** → control returns to OS.
   - **I/O instructions** are privileged.
4. **Interrupts**
   - OS can **give or regain control** to/from user programs.
   - Enables **multitasking** and **hardware event handling**.

## Slide 7

Slide divisoria de sección (imagen decorativa: mano robótica tocando globo digital).

**2. Fundamentals** (con ícono de portapapeles)

## Slide 8

**Kernel**

- OS is also known as the **system kernel.**
- Isolated from the **user and applications.**
- **Interacts directly** with the hardware.
- **Acts as a resource manager and monitor.**

**Visual (diagrama a la derecha):** Diagrama de memoria/capas en forma de columna vertical dividida en dos zonas. La parte superior (bloques azules, etiquetada **Kernel** en rojo sobre fondo verde claro) contiene, de arriba a abajo: **Interrupt Processing**, **Device Drivers**, **Job Sequencing**, **Control Language Interpreter**. La parte inferior (fondo amarillo claro, etiquetada **User** en verde) contiene el bloque **User Program Area**. Ilustra la separación entre el espacio del kernel (funciones privilegiadas) y el área de programas de usuario.

## Slide 9

**OS Basics**

- **Definition 1: Execution Modes**
  - **User Mode**: Restricted access to memory and instructions.
  - **Kernel Mode**: Full privileges, unrestricted execution.
- **Definition 2: Multiprogram**
  - **Multiple (uni)programs** executed concurrently.
  - Each **(uni)program** may contain multiple threads.
  - Challenging for the **OS challenge**.

**Visual (diagrama a la derecha):** Diagrama isométrico 3D de tres bloques apilados sobre fondo negro:
- **User Space** (verde) — "Applications | Libraries | User Processes"
- **Kernel Space** (amarillo) — "CPU, Memory, and Device Management"
- **Hardware** (rojo) — "CPU | Memory | Device"

Una flecha amarilla curva de User Space hacia Kernel Space rotulada **"Restricted Access via API"**. Una flecha roja curva de Kernel Space hacia Hardware con un ícono de advertencia (triángulo) rotulada **"Privileged Access"**. Ilustra que las apps acceden al kernel solo vía API restringida y que el kernel es quien tiene acceso privilegiado al hardware.

## Slide 10

**OS Basics**

- **Definition 3: Process**
  - Defined in **1960 by Multics** designers.
  - **A program or job in execution** that can be associated to a set of system resources.
  - Contains **three key elements:**
    1. **Executable program**
    2. **Associated data:** variables, work space, buffers, etc.
    3. **Execution context:** Internal data of registers, priority, status and associations.
  - Allows the OS control over the process.

(Slide solo de texto; sin diagrama.)

## Slide 11

Slide divisoria de sección (imagen decorativa: mano robótica tocando globo digital).

**3. OS Structure** (con ícono de portapapeles)

## Slide 12

**Monolithic Architecture**

**All in Kernel implementation (e.g.: Linux, UNIX):**
- Scheduling, file system, networking, device drivers, memory management, and more.
- Usually, **implemented as a single process,** with all elements sharing the same address space.
- Description:
  - **Main program** that invokes the requested service procedure.
  - **A set of service procedures** that carry out the system calls.
  - **A set of utility procedures** that help the service procedures.

**Visual (diagrama a la derecha — arquitectura monolítica tipo UNIX):** Diagrama en dos niveles separados por una línea punteada.
- **User Level** (arriba): **User Programs** y **Libraries**; flechas de **Trap** (línea punteada) y llamadas apuntan hacia abajo al kernel.
- **Kernel Level** (fondo verde): en la parte superior el **System Call Interface** (barra horizontal). Debajo, a la izquierda el **File Subsystem** conectado con **Buffer Cache** y con los **Device Drivers** (divididos en **character** y **block**). A la derecha el **Process Control Subsystem**, que contiene **Inter-process communication**, **Scheduler** y **Memory management**. Flechas bidireccionales conectan File Subsystem ↔ Process Control Subsystem y ambos hacia abajo.
- En la base, **Hardware Control** dentro del kernel, y debajo (fuera, otra franja) el **Hardware Level**.

Ilustra que todos los subsistemas del OS conviven dentro del mismo nivel de kernel compartiendo espacio de direcciones.

## Slide 13

**2. Microkernel Architecture:**
- **Only a few essential functions** to the kernel: address spaces, interprocess communication (IPC), and basic scheduling.
- **Other OS services are provided by processes** (called servers) that run in user mode.
- **Servers are customized** to specific application or environment requirements.
- **Simplifies implementation,** and provides flexibility.

**Visual (diagrama a la derecha — microkernel MINIX 3):** Diagrama estratificado en cuatro capas. De arriba a abajo, tres bandas con procesos representados como círculos:
- **User progs**: Shell, Make, ... , Other
- **Servers**: FS, Proc., Reinc., ... , Other
- **Drivers**: Disk, TTY, Netw, Print, ... , Other

En la base, una banda oscura (marrón) que representa el **microkernel**, rotulada "Microkernel handles interrupts, processes, scheduling, IPC", conteniendo los procesos **Clock** y **Sys**. Flechas rotuladas **Process** apuntan desde la derecha hacia círculos "Other" de cada banda, indicando que todos son procesos independientes.

Recuadro inferior: **E.g.: MINIX 3 microkernel.**

## Slide 14

**2.1 Monolithic kernels vs microkernels**

To understand the difference between a mainstream OS, such as Linux, and a microkernel, such as seL4, let's look at Figure 2.1.

**Visual (Figure 2.1 — comparación monolítico vs microkernel):**

Lado izquierdo — **Monolithic kernel** (rotulado **20,000 kSLOC**): una sola pila grande en **Kernel Mode**, con capas amarillas apiladas: **VFS**, **IPC, File System**, **Scheduler, Virtual Memory**, **Device Drivers, Dispatcher**, sobre **Hardware** (azul). Una flecha bidireccional **Syscall** marca la frontera entre User Mode y Kernel Mode (casi todo está en kernel).

Lado derecho — **Microkernel** (rotulado **10 kSLOC**): el kernel es solo una franja verde delgada (**IPC, Threads, Virtual Memory**) sobre el **Hardware**. Todo lo demás corre en **User Mode** como cajas separadas por encima: **Application** (azul), **NW Protocol Stack** (amarillo), **Device Driver** (rosado), **File Server** (amarillo). Flechas **IPC** conectan la aplicación con los servidores a través del microkernel.

Pie: *Figure 2.1: Operating-system structure: Monolithic kernel (left) vs microkernel (right).*

Contraste clave: el monolítico ~20,000 kSLOC dentro del kernel vs el microkernel ~10 kSLOC en el kernel (mucho menos código privilegiado).

## Slide 15

**Reference Books** (imagen decorativa: profesor escribiendo en pizarra frente a estudiantes). Cada referencia con viñeta de flecha azul.

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). *Operating system concepts* (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).
