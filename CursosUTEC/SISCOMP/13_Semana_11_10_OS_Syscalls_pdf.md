---
curso: SISCOMP
titulo: 13 - Semana 11/10. OS Syscalls
slides: 21
fuente: 13 - Semana 11/10. OS Syscalls.pdf
---

COMPUTING SYSTEMS

              Syscalls
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
                   Recall: OS Four Main Features
1. Memory Protection
   ● User programs can’t modify OS or other programs’ memory.
   ● Enforced by policy (abort, show error, etc.).
2. Timing Control
   ● A timer is set for each job.
   ● When it expires, the OS stops the program.
   ● Prevents CPU overuse or inﬁnite loops.
3. Privileged Instructions
   ● Only the OS can execute them (subset of ISA).
   ● If used by a user program → error → control returns to OS.
   ● I/O instructions are privileged.
4. Interrupts
   ● OS can give or regain control to/from user programs.
   ● Enables multitasking and hardware event handling.
                      User Programs restrictions


To guarantee OS main features:
   ● User programs must run in user mode only.
   ● Access to privileged operations (I/O, memory,
      CPU control) must go through syscalls.
   ● Direct hardware access or kernel modiﬁcation is
      not allowed.
→ This separation ensures protection, fairness, and
controlled execution.
2.
 Fundamentals
                            Abstraction Interfaces
● Application programming interface (API):
  ○ Gives a program access to the hardware
    resources and services.
  ○ Supplemented with high-level language (HLL)
    library call

● Application binary interface (ABI):
  ○ Deﬁnes the system call interface.

● Instruction set architecture (ISA):
  ○ Details the execution capabilities of the system.
  ○ Provides user ISA
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
3.
     System Calls
System calls
System calls
                                 System calls

1. Process Control: It handles the system calls for process creation, deletion, etc. Examples of
   process control system calls are: Load, Execute, Abort, and Wait for Signal events for process.
2. File Management: File manipulation events like Creating, Deleting, Reading Writing etc are
   being classiﬁed under ﬁle management system calls.
3. Device Management: Device Management system calls are being used to request the device,
   release the device, and logically attach and detach the device.
4. Information Maintenance: This type of system call is used to maintain the information about the
   system like time and date.
5. Communications: In order to have interprocess communications like send or receive the
   message, create or delete the communication connections, to transfer status information etc.
   communication system calls are used.
System calls
System calls in
 Windows and
     Linux
System calls in
 Windows and
     Linux
                    System calls used in OS
1. wait(): There are scenarios where the current process needs to wait for another process to
   complete the task. So to wait in this scenario, wait() system call is used.
2. fork(): This system call creates the copy of the process that has called it. The one which has
   called fork is called the parent process and the newly created copy is called the child
   process.
3. exec(): This system call is called when the running process wants to execute another
   executable ﬁle. The process id remains the same while the other resources used by the
   process are replaced by the newly created process.
4. kill(): Sometimes while working, we require to terminate a certain process. So kill system
   call is called which sends the termination signal to the process.
5. exit(): When we are actually required to terminate the program, an exit system call is used.
   The resources that are occupied by the process are released after invoking the exit system
   call.
                                     System calls

System calls (syscalls) provide the programmatic
interface between user space and the OS kernel.
● They are used to perform tasks that user programs
   cannot do directly — such as reading ﬁles, writing
   to the screen, or creating processes.
● Each system call has a unique ID number,
   managed by the System Call Interface.
● The user doesn’t need to know how it’s
   implemented — it’s accessed through APIs or
   runtime libraries.


                                                        Syscall execution diagram 2
                         Linux - Syscalls 😼
Here is a table of the Linux Syscalls, for different architectures
(including RISC-V):

https://syscalls.mebeim.net/




                reg a7 hast to equal 0x42
                when the interrupt             Linux source code ﬁle
                happens, in order to           location
                execute syscall writev

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
