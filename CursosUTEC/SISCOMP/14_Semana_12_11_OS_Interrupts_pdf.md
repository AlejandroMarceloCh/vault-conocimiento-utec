---
curso: SISCOMP
titulo: 14 - Semana 12/11. OS Interrupts
slides: 15
fuente: 14 - Semana 12/11. OS Interrupts.pdf
---

## Slide 1

Portada (decorativa: fondo azul de túnel tecnológico con figura de robot humanoide).

**COMPUTING SYSTEMS**
Interrupts
Professor: Luz A. Adanaqué

Based on lecture notes by Prof. Jorge Gonzalez

## Slide 2

Slide dividida en dos columnas de texto (imagen decorativa de científica en laboratorio a la izquierda).

**Motivation**
User programs need to perform tasks securely.
But how can they communicate safely with the kernel?

**Goals**
Understand how system calls connect user programs and the kernel.

Recognize the importance of security and protection in this interaction.

## Slide 3

Slide de índice/agenda (imagen decorativa de mujer con visor VR).

**Summary**

1. (icono de portapapeles) Introduction
2. (icono de bombilla) Background
3. (icono de bombilla) System Calls

## Slide 4

Slide separador de sección (imagen decorativa de mano robótica tocando un globo terráqueo digital).

**1. Introduction**

## Slide 5

**Recall: OS Basics**

- **Definition 1: Execution Modes**
  - **User Mode**: Restricted access to memory and instructions.
  - **Kernel Mode**: Full privileges, unrestricted execution.

Diagrama a la derecha (recuperado): pila de tres bloques 3D apilados verticalmente, cada uno con flechas curvas a la derecha que descienden de un nivel al siguiente:

- Bloque superior verde **User Space** — subtítulo: "Applications | Libraries | User Processes".
- Flecha amarilla descendente → etiqueta "Restricted Access via API".
- Bloque medio amarillo **Kernel Space** — subtítulo: "CPU, Memory, and Device Management".
- Flecha roja descendente → etiqueta con icono de advertencia (triángulo ⚠) "Privileged Access".
- Bloque inferior rojo **Hardware** — subtítulo: "CPU | Memory | Device".

La idea del diagrama: User Space accede al Kernel Space solo de forma restringida vía API; el Kernel Space accede al Hardware con acceso privilegiado.

## Slide 6

Slide separador de sección (imagen decorativa de mano robótica y globo digital, igual estética que slide 4).

**2. Interrupts**

## Slide 7

**Interrupts**

Interrupts are the events that can be caused by hardware or software that signals the processor to complete the ongoing instruction and immediately handle the Interrupt Service Routine (ISR) which contains the information for dealing with the interrupt.

(Slide solo de texto sobre fondo blanco.)

## Slide 8

**Interrupts**

Interrupts are the events that take place to inform the operating system to stop the current execution of the current process and handle the Interrupt Service Routine (ISR).

ISR is responsible for finding out which software or hardware caused the interruption and informing the CPU about it.

CPU will service the request and after the completion of the request, CPU resumes the execution of the process which CPU was previously executing. Interrupts can be caused by hardware as well as software.

(Slide solo de texto.)

## Slide 9

**Interrupts**

Definition: **Interrupts are signals that temporarily stop** the CPU's normal execution to handle an event.

- They allow the operating system to respond immediately to hardware or software requests.
- Usually triggered by hardware or system events.
- CPU saves what it was doing, handles the interrupt, then returns to normal work.
- **Example:** typing on a keyboard triggers interrupts so characters appear immediately.

**Diagrama a la derecha — "Syscall execution diagram 1"** (recuperado). Muestra la ejecución de un syscall cruzando de user mode a kernel mode (separados por una línea horizontal roja):

- Zona superior **User mode** — bloque morado etiquetado "User program":
  ```
  printf("Hello world!") calls
     write(1, buf, sz)
  --------------------------------
     movl $SYS_write, %eax
     int 64
     ret        // usys.S
  ```
  La instrucción `int 64` dispara una flecha que cruza la línea roja hacia el kernel.
- Zona inferior **kernel mode**:
  - Bloque verde **IDT** (Interrupt Descriptor Table) con la entrada "64 → syscall". La flecha de `int 64` llega a la entrada 64.
  - Desde IDT una flecha va al código:
    ```
    syscall() {
       syscalls[%eax]()
    } // syscall.c
    ```
  - A la derecha, bloque verde **syscalls table** con la entrada "sys_write". El código `syscalls[%eax]()` indexa esa tabla.
  - Desde la tabla, una flecha baja hacia:
    ```
    sys_write(...) {
       // do real work
    } // sysfile.c
    ```

Flujo: el programa de usuario invoca `write` → `int 64` → IDT entrada 64 → `syscall()` → busca en la syscalls table por `%eax` → `sys_write` → ejecuta el trabajo real en `sysfile.c`.

## Slide 10

**Hardware Interrupts**

When an external device wants the attention of the operating system to service a certain request, it raises an interrupt which is called a hardware interrupt. All the external devices are connected to a single Interrupt Request Line and the Interrupt Request Line is used for the interrupts.

The hardware interrupts are further categorized into two types:

- **Maskable Interrupts**: Hardware interrupts that can be ignored or disabled are called maskable interrupts.
- **Non-Maskable interrupts**: Hardware interrupts that can't be ignored or disabled are called non-maskable interrupts.

**Diagrama a la derecha (recuperado)** — árbol jerárquico de clasificación de interrupts:

```
              Interrupts
             /          \
   Hardware Interrupt   Software Interrupt
       /        \
 Maskable    Non-Maskable
 Interrupt     Interrupt
```

Nodo raíz "Interrupts" (recuadro rosa) se ramifica en "Hardware Interrupt" y "Software Interrupt" (recuadros verdes); "Hardware Interrupt" a su vez se ramifica en "Maskable Interrupt" y "Non-Maskable Interrupt" (recuadros lila).

## Slide 11

**Software Interrupts**

Software interrupts generally take place when there are exceptions in the process or by using special instructions that cause the interrupts. While having the system calls in our system, we generally have the software interrupt.

Division by zero throws an exception which causes the software interrupt, whereas while we use fork() system call, fork() also invokes a software interrupt.

**Diagrama a la derecha (recuperado)** — flujo de un software interrupt vía `fork()` usando la Trap Table:

- Bloque de código de usuario (recuadro rosa):
  ```
  ...
  fork();
  ...
  ------------------
  fork() {
     ...
     trap N_SYS_FORK()
     ...
  }
  ```
- La llamada `fork()` salta a la función `fork()` (flecha), que ejecuta `trap N_SYS_FORK()`.
- Esa trap apunta a la **Trap Table** (recuadro grande lila): entrada `sys_fork()` (recuadro verde).
- Desde la Trap Table una flecha va a la implementación real:
  ```
  sys_fork() {
     /* system function */
     ...
     return;
  }
  ```
- El `return` regresa el control (flecha de retorno) de vuelta al código de usuario en `fork()`.

Flujo: `fork()` → `trap N_SYS_FORK()` → Trap Table (`sys_fork`) → implementación `sys_fork()` → return al llamador.

## Slide 12

Slide separador de sección (imagen decorativa de mano robótica y globo digital).

**3. CPU Response**

## Slide 13

**CPU Response**

When the interrupt occurs, the CPU completes the execution of ongoing instructions and handles the ISR. However once the interrupt is resolved, the CPU continues to execute from where an execution was stopped prior to the interrupt.

Imagen a la derecha (decorativa): ilustración retro pixel-art de una computadora de escritorio antigua con nubes, texto "Nimbus Network" y "Cloud Computing Made Easy". Meme/ilustración decorativa sin contenido técnico.

## Slide 14

**Context Switching**

Context Switching is the process where the state of the current process is saved and stored, while another process is brought for execution. Once the execution of the new process is completed, the CPU restores the state of the old process and continues the execution from where the execution of the process was left.

So following steps are involved while handling the interrupts:

- The First step involved in handling the interrupt is to check the priority of the interrupt.
- If the priority is low compared to the current process under execution, then the interrupt is saved in the memory.
- If the priority is high compared to the current process under execution, CPU saves the context of the current process.
- CPU loads the new process which invoked the interrupt and executes that.
- On completion of the requested service, CPU loads the process that was under execution prior to the interrupt and resumes the execution from where the execution was interrupted.

(Slide solo de texto.)

## Slide 15

**Reference Books**

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann.
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press.
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). *Operating system concepts* (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).

(Imagen decorativa de profesor escribiendo en pizarra a la derecha.)
