---
curso: SISCOMP
titulo: 14 - Semana 12/11. OS Interrupts
slides: 15
fuente: 14 - Semana 12/11. OS Interrupts.pdf
---

COMPUTING SYSTEMS

            Interrupts
    Professor: Luz A. Adanaqué




                        Based on lecture notes by Prof. Jorge Gonzalez
Motivation
User programs need to perform tasks securely.
But how can they communicate safely with the kernel?




Goals
Understand how system calls connect user programs
and the kernel.

Recognize the importance of security and protection in
this interaction.
Summary

1.   Introduction




2.   Background




3.   System Calls
1.
     Introduction
                         Recall: OS Basics



- Deﬁnition 1: Execution Modes
  ○ User Mode: Restricted access to
    memory and instructions.
  ○ Kernel Mode: Full privileges,
    unrestricted execution.
2.
 Interrupts
                                        Interrupts


Interrupts are the events that can be caused by hardware or software that signals the processor to
complete the ongoing instruction and immediately handle the Interrupt Service Routine (ISR)
which contains the information for dealing with the interrupt.
                                     Interrupts

Interrupts are the events that take place to inform the operating system to stop the current
execution of the current process and handle the Interrupt Service Routine (ISR).

ISR is responsible for ﬁnding out which software or hardware caused the interruption and
informing the CPU about it.

CPU will service the request and after the completion of the request, CPU resumes the
execution of the process which CPU was previously executing. Interrupts can be caused by
hardware as well as software.
                                       Interrupts
Deﬁnition: Interrupts are signals that temporarily
stop the CPU’s normal execution to handle an event.

● They allow the operating system to respond
  immediately to hardware or software requests.

● Usually triggered by hardware or system events.

● CPU saves what it was doing, handles the interrupt,
  then returns to normal work.

● Example: typing on a keyboard triggers interrupts
  so characters appear immediately.                     Syscall execution diagram 1
                                 Hardware Interrupts
When an external device wants the attention of the
operating system to service a certain request, it raises
an interrupt which is called a hardware interrupt. All
the external devices are connected to a single
Interrupt Request Line and the Interrupt Request Line
is used for the interrupts.

The hardware interrupts are further categorized into
two types:

● Maskable Interrupts: Hardware interrupts that can
  be ignored or disabled are called maskable
  interrupts.
● Non-Maskable interrupts: Hardware interrupts that
  can’t be ignored or disabled are called
  non-maskable interrupts.
                               Software Interrupts

Software interrupts generally take place when there
are exceptions in the process or by using special
instructions that cause the interrupts. While having
the system calls in our system, we generally have
the software interrupt.

Division by zero throws an exception which causes
the software interrupt, whereas while we use fork()
system call, fork() also invokes a software interrupt
3.
     CPU Response
                                    CPU Response



When the interrupt occurs, the CPU completes the execution of ongoing
instructions and handles the ISR. However once the interrupt is resolved,
the CPU continues to execute from where an execution was stopped prior
to the interrupt.
                                  Context Switching
Context Switching is the process where the state of the current process is saved and stored, while
another process is brought for execution. Once the execution of the new process is completed, the CPU
restores the state of the old process and continues the execution from where the execution of the
process was left.

So following steps are involved while handling the interrupts:

● The First step involved in handling the interrupt is to check the priority of the interrupt.
● If the priority is low compared to the current process under execution, then the interrupt is saved in
  the memory.
● If the priority is high compared to the current process under execution, CPU saves the context of the
  current process.
● CPU loads the new process which invoked the interrupt and executes that.
● On completion of the requested service, CPU loads the process that was under execution prior to the
  interrupt and resumes the execution from where the execution was interrupted.
Reference Books
 Patterson, D. A., & Hennessy, J. L. (2020). Computer Organization and
 Design RISC-V Edition: The Hardware Software Interface. Morgan
 Kaufmann


 “The elements of computing systems: building a modern computer
 from ﬁrst principles” Nisan, N., & Schocken, S. (2021). MIT press



 Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). Operating system concepts
 (9th edition, international student version). John Wiley & Sons Inc.



 ”Digital Design and Computer Architecture, RISC-V Edition”. Morgan
 Kaufmann. Harris, S., & Harris, D. (2021).

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
