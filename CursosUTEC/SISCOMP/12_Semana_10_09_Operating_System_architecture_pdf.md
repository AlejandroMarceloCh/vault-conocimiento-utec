---
curso: SISCOMP
titulo: 12 - Semana 10/09. Operating System architecture
slides: 15
fuente: 12 - Semana 10/09. Operating System architecture.pdf
---

COMPUTING SYSTEMS

   Operating System architecture
    Professor: Luz A. Adanaqué




                         Based on lecture notes by Prof. Jorge Gonzalez
Motivation
To understand how operating system architecture
defines  its  functionality and   performance.

To recognize how design choices affect stability and
                   modularity.




Goals
Identify and describe main OS architecture types.
Summary

1.   Definitions




2.   Fundamentals




3.   OS Structure
1.
     Definitions
                 Recall: The Operating System
● Definition
  ○ A program that controls the execution of
    application programs
  ○ An interface between applications and
    hardware
● With 3 important keys:
  ○ Convenience: Simple to use, from the
    programmer's perspective
  ○ Efficiency: Important metric related to the
    specific task
  ○ Ability to evolve: Permits the effective
    development, testing, and introduction of new
    system functions without interfering with
    service.                                        OS Abstraction layers and their Interfaces.
                          OS Four Main Features
1. Memory Protection
    ● User programs can’t modify OS or other programs’ memory.
    ● Enforced by policy (abort, show error, etc.).
1. Timing Control
    ● A timer is set for each job.
    ● When it expires, the OS stops the program.
    ● Prevents CPU overuse or infinite loops.
1. Privileged Instructions
    ● Only the OS can execute them (subset of ISA).
    ● If used by a user program → error → control returns to OS.
    ● I/O instructions are privileged.
1. Interrupts
    ● OS can give or regain control to/from user programs.
    ● Enables multitasking and hardware event handling.
2.
 Fundamentals
                                   Kernel




● OS is also known as the system kernel.
● Isolated from the user and applications.
● Interacts directly with the hardware.
● Acts as a resource manager and
  monitor.
                               OS Basics
- Definition 1: Execution Modes
  ○ User Mode: Restricted access to
    memory and instructions.
  ○ Kernel Mode: Full privileges,
    unrestricted execution.
- Definition 2: Multiprogram
  ○ Multiple (uni)programs executed
    concurrently.
  ○ Each (uni)program may contain
    multiple threads.
  ○ Challenging for the OS challenge.
OS Basics
3.
 OS Structure
Monolithic Architecture
Reference Books
 Patterson, D. A., & Hennessy, J. L. (2020). Computer Organization and
 Design RISC-V Edition: The Hardware Software Interface. Morgan
 Kaufmann


 “The elements of computing systems: building a modern computer from
 first principles” Nisan, N., & Schocken, S. (2021). MIT press



 Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). Operating system concepts
 (9th edition, international student version). John Wiley & Sons Inc.



 ”Digital Design and Computer Architecture, RISC-V Edition”. Morgan
 Kaufmann. Harris, S., & Harris, D. (2021).

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
