---
curso: SISCOMP
titulo: 13 - Semana 11/10. OS Syscalls
slides: 21
fuente: 13 - Semana 11/10. OS Syscalls.pdf
---

## Slide 1

Portada (decorativa: fondo de túnel tecnológico con silueta de robot humanoide).

**COMPUTING SYSTEMS**

Syscalls
Professor: Luz A. Adanaqué

Based on lecture notes by Prof. Jorge Gonzalez

## Slide 2

Slide dividida: a la izquierda foto decorativa de científica de laboratorio con tubos de ensayo (tono azul). Texto a la derecha.

**Motivation**

User programs need to perform tasks securely.
But how can they communicate safely with the kernel?

**Goals**

Understand how system calls connect user programs and the kernel.

Recognize the importance of security and protection in this interaction.

## Slide 3

Foto decorativa (mujer con visor VR, globo terráqueo digital de fondo). Índice del capítulo con iconos.

**Summary**

1. (icono portapapeles) Introduction
2. (icono bombilla) Background
3. (icono bombilla) System Calls

## Slide 4

Slide separadora de sección (decorativa: mano robótica tocando un globo digital).

**1. Introduction**

## Slide 5

**Recall: OS Basics**

- **Definition 1: Execution Modes**
  - **User Mode**: Restricted access to memory and instructions.
  - **Kernel Mode**: Full privileges, unrestricted execution.

**Visual (diagrama de capas 3D, fondo negro):** tres bloques apilados tipo "cajas isométricas":
- **User Space** (verde, arriba): "Applications | Libraries | User Processes".
- **Kernel Space** (amarillo, medio): "CPU, Memory, and Device Management".
- **Hardware** (rojo, abajo): "CPU | Memory | Device".

A la derecha, dos flechas curvas descendentes: de User Space a Kernel Space, etiquetada **"Restricted Access via API"**; de Kernel Space a Hardware, etiquetada con un icono de advertencia (triángulo) **"Privileged Access"**.

## Slide 6

**Recall: OS Four Main Features**

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

(Slide solo texto, sin figura.)

## Slide 7

**User Programs restrictions**

To guarantee OS main features:
- User programs must run in **user mode** only.
- **Access to privileged operations** (I/O, memory, CPU control) must go through syscalls.
- Direct hardware access or kernel modification is **not allowed**.

→ This separation ensures protection, fairness, and controlled execution.

**Visual (diagrama de bloques con flechas bidireccionales):**
- Bloque rojo superior: **Applications**.
- Flecha doble vertical hacia abajo a bloque azul: **Kernel**.
- Del Kernel bajan tres flechas dobles a tres bloques verdes: **CPU**, **Memory**, **Devices**.

Es decir: Applications ↔ Kernel ↔ {CPU, Memory, Devices}.

## Slide 8

Slide separadora de sección (decorativa: mano robótica y globo digital).

**2. Fundamentals**

## Slide 9

**Abstraction Interfaces**

- **Application programming interface (API):**
  - Gives a **program access to the hardware** resources and services.
  - Supplemented with **high-level language (HLL)** library call.
- **Application binary interface (ABI):**
  - Defines the **system call interface** (resaltado).
- **Instruction set architecture (ISA):**
  - Details the **execution capabilities** of the system.
  - Provides *user ISA*.

**Visual (diagrama de niveles de abstracción):** pila de capas apiladas (de arriba a abajo): **Application programs** → **Libraries/utilities** → **Operating system** → **Execution hardware**. Debajo del hardware se ramifican: **System interconnect (bus)**, **Memory translation**, **I/O devices and networking**, **Main memory**.

A la izquierda, líneas horizontales de colores marcan las fronteras de cada interfaz sobre la pila:
- **API** (verde): frontera entre application programs y libraries.
- **ABI** (azul): frontera que abarca libraries/OS hacia el hardware.
- **ISA** (rojo): frontera entre operating system y execution hardware.

## Slide 10

**Interrupts**

Definition: **Interrupts are signals that temporarily stop** the CPU's normal execution to handle an event.

- They allow the operating system to respond immediately to hardware or software requests.
- Usually triggered by hardware or system events.
- CPU saves what it was doing, handles the interrupt, then returns to normal work.
- **Example:** typing on a keyboard triggers interrupts so characters appear immediately.

**Visual — "Syscall execution diagram 1":** diagrama con una línea roja horizontal que separa **User mode** (arriba) de **kernel mode** (abajo).
- En User mode, un bloque **"User program"** (morado) con código:
  ```
  printf("Hello world!") calls
  write(1, buf, sz)

  movl $SYS_write, %eax
  int 64
  ret       // usys.S
  ```
- Una flecha baja desde `int 64` cruzando a kernel mode hacia un bloque **IDT** (verde) con entrada `64 → syscall`.
- De IDT sale una flecha a código:
  ```
  syscall() {
    syscalls[%eax]()
  } // syscall.c
  ```
- A la derecha, bloque **"syscalls table"** (verde) con entrada `sys_write`.
- Flecha desde la tabla hacia:
  ```
  sys_write(...) {
    // do real work
  } // sysfile.c
  ```

## Slide 11

Slide separadora de sección (decorativa: mano robótica y globo digital).

**3. System Calls**

## Slide 12

**System calls**

**Visual — "WORKING OF A SYSTEM CALL":** diagrama de dos franjas (morado claro):
- Franja superior **USER MODE** con tres cajas rosadas numeradas: **(1) User Process Executing** → **(2) Gets System Call** → **(3) Return From System Call**.
- Franja inferior **KERNEL MODE** con una caja **(4) Execute System Call**.
- Flechas: de (2) baja a (4) en kernel mode; de (4) sube a (3) de vuelta en user mode. (1)→(2) horizontal.

## Slide 13

**System calls**

**Visual (diagrama de burbujas radial):** un semicírculo central **"Types of System Calls"** del que salen conectores a cinco burbujas de colores:
- **Process Control** (morada)
- **File Management** (turquesa)
- **Device Management** (azul)
- **Information Management** (rosada)
- **Communication** (turquesa)

## Slide 14

**System calls** (los 5 tipos, texto detallado)

1. **Process Control:** It handles the system calls for process creation, deletion, etc. Examples of process control system calls are: Load, Execute, Abort, and Wait for Signal events for process.
2. **File Management:** File manipulation events like Creating, Deleting, Reading Writing etc are being classified under file management system calls.
3. **Device Management:** Device Management system calls are being used to request the device, release the device, and logically attach and detach the device.
4. **Information Maintenance:** This type of system call is used to maintain the information about the system like time and date.
5. **Communications:** In order to have interprocess communications like send or receive the message, create or delete the communication connections, to transfer status information etc. communication system calls are used.

(Slide solo texto.)

## Slide 15

**System calls**

**Visual (diagrama clásico Tanenbaum de una llamada `read`, 11 pasos):** un recuadro grande dividido en **User space** (arriba, celeste) y **Kernel space (Operating system)** (abajo, azul).

En user space, dos bloques apilados:
- Bloque superior rosa **"Library procedure read"** con tres filas (de arriba a abajo): `Return to caller`, `Trap to the kernel`, `Put code for read in register` (paso 5).
- Bloque inferior morado **"User program calling read"** con filas (de abajo hacia arriba): `1 Push nbytes`, `2 Push & buffer`, `3 push fd`, `Call read`, `Increment SP` (paso 11).

En kernel space: **Dispatch** (7) → tabla de handlers (8) → **Sys call handler**.

Numeración del flujo (1–11): pushes de argumentos (1,2,3) → Call read (4) → poner código en registro (5) → trap al kernel (6) → Dispatch (7) → tabla (8) → Sys call handler (9) → retorno (10) → Increment SP (11) → Return to caller. Etiquetas laterales: "User program calling read" y "Library procedure read".

## Slide 16

**System calls in Windows and Linux** (tabla, parte 1)

| Types of System Calls | Windows | Linux |
|---|---|---|
| Process Control | CreateProcess() | fork() |
| | ExitProcess() | exit() |
| | WaitForSingleObject() | wait() |
| File Management | CreateFile() | open() |
| | ReadFile() | read() |
| | WriteFile() | write() |
| | CloseHandle() | close() |

## Slide 17

**System calls in Windows and Linux** (tabla, parte 2)

| Types of System Calls | Windows | Linux |
|---|---|---|
| Device Management | SetConsoleMode() | ioctl() |
| | ReadConsole() | read() |
| | WriteConsole() | write() |
| Information Maintenance | GetCurrentProcessID() | getpid() |
| | SetTimer() | alarm() |
| | Sleep() | sleep() |
| Communication | CreatePipe() | pipe() |
| | CreateFileMapping() | shmget() |
| | MapViewOfFile() | mmap() |

## Slide 18

**System calls used in OS**

1. **wait():** There are scenarios where the current process needs to wait for another process to complete the task. So to wait in this scenario, wait() system call is used.
2. **fork():** This system call creates the copy of the process that has called it. The one which has called fork is called the parent process and the newly created copy is called the child process.
3. **exec():** This system call is called when the running process wants to execute another executable file. The process id remains the same while the other resources used by the process are replaced by the newly created process.
4. **kill():** Sometimes while working, we require to terminate a certain process. So kill system call is called which sends the termination signal to the process.
5. **exit():** When we are actually required to terminate the program, an exit system call is used. The resources that are occupied by the process are released after invoking the exit system call.

(Slide solo texto.)

## Slide 19

**System calls**

System calls (syscalls) provide **the programmatic interface between user space and the OS kernel**.
- They are used to perform tasks that user programs **cannot do directly** — such as reading files, writing to the screen, or creating processes.
- Each system call has a unique **ID number**, managed by the **System Call Interface**.
- The user **doesn't need to know how it's implemented** — it's accessed through APIs or runtime libraries.

**Visual — "Syscall execution diagram 2":** en la parte superior un comando en recuadro: `cp my-test.txt new-text.txt`. Debajo, un bloque **"source file"** con flecha hacia **"destination file"**. Entre ellos, un recuadro celeste **"Example System Call Sequence"** que lista el pseudocódigo del `cp`:
```
Acquire input file name
  Write prompt to screen
  Accept input
Acquire output file name
  Write prompt to screen
  Accept input
Open the input file
  if file doesn't exist, abort
Create output file
  if file exists, abort
Loop
  Read from input file
  Write to output file
Until read fails
Close output file
Write completion message to screen
Terminate normally
```

## Slide 20

**Linux - Syscalls** (con emoji de gato)

Here is a table of the Linux Syscalls, for different architectures (including RISC-V):

https://syscalls.mebeim.net/

**Visual (captura de pantalla de la web syscalls.mebeim.net, tema oscuro):** tabla con columnas **Number (a7)**, **[-] Name**, **[-] Symbol**, **[-] Definition location**:

| Number (a7) | Name | Symbol | Definition location |
|---|---|---|---|
| 65 (0x41) | readv | __riscv_sys_readv | fs/read_write.c:1155 |
| 66 (0x42) | writev | __riscv_sys_writev | fs/read_write.c:1161 |

Dos flechas rosadas anotan la captura:
- Bajo la columna Number: **"reg a7 hast to equal 0x42 when the interrupt happens, in order to execute syscall writev"**.
- Bajo la columna Definition location: **"Linux source code file location"**.

## Slide 21

Slide de cierre (decorativa: foto de profesor escribiendo en pizarra, tono azul).

**Reference Books**

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann.
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press.
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). *Operating system concepts* (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).
