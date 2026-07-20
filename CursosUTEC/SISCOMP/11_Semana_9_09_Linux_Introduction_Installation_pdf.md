---
curso: SISCOMP
titulo: 11 - Semana 9/09. Linux Introduction & Installation
slides: 18
fuente: 11 - Semana 9/09. Linux Introduction & Installation.pdf
---

COMPUTING SYSTEMS

   Linux Introduction & Installation




                                       Professor: Luz Adanaque
Motivation
To become familiar with the Linux environment as a
foundation for system-level work

To understand why Linux is widely used            in
programming, servers, and embedded systems.




Goals
Install and run Linux inside a virtual machine using
QEMU.

Practice      essential      shell      commands.
Summary

1.   From ISA to OS
                                4.   Basic shell commands




2.   About Linux




3.   Installing Linux in a VM
1.
     From ISA to OS
                Why Move Beyond the ISA?



● The ISA deﬁnes how the processor
  executes instructions. But running real
  programs requires more than instructions.

● We need a system that manages memory,
  ﬁles, and hardware — that’s the Operating
  System.
                           ISA Limitations



● Directly programming hardware is powerful
  but complex.
● Every task (I/O, storage, multitasking) must
  be manually controlled.
● Hard to scale beyond simple demos or
  embedded systems.
  ○ Need abstraction layers for efﬁciency
    and safety.

  That why, the OS abstracts the hardware!
                                                 OS Abstraction layers and their Interfaces.
                     The Operating System
● Deﬁnition
  ○ A program that controls the execution of
    application programs
  ○ An interface between applications and
    hardware
● With 3 important keys:
  ○ Convenience: Simple to use, from the
    programmer's perspective
  ○ Efﬁciency: Important metric related to the
    speciﬁc task
  ○ Ability to evolve: Permits the effective
    development, testing, and introduction of
    new system functions without interfering
    with service.                                OS Abstraction layers and their Interfaces.
2.
 About Linux
                             What is Linux?

● Linux is a free and open-source kernel
  based on Unix.
● Created by Linus Torvalds in 1991.
● Uses a monolithic architecture that
  manages hardware, memory, and
  processes.
What is a kernel?
● The kernel is the core part of an OS
  between the hardware and user
  programs, managing how applications
  use CPU, memory, storage, and devices.
                                           ↑ Tux. The mascot
     So, Linux is not the OS itself!       of Linux            ← Linus Torvalds
                         Linux Distros
            There are a LOT of distros!!!




Distro popularity rankings
                      Linux Current Usage


● Runs everywhere: from supercomputers
  to smartphones and IoT devices.
● Dominates servers: most web servers
  and cloud systems run on Linux (e.g.
  AWS, Google Cloud).
● Android is based on the Linux kernel.
● Used in development: preferred by
  programmers, DevOps, and
  cybersecurity professionals.
3.
     Installing Linux in a
     VM
                            Requirements

● Operating System: A Windows 10 or 11
  machine (this guide assumes Windows).
● Virtualization Support: Enabled in
  BIOS/UEFI
  ○ Look for Intel VT-x or AMD-V options.
  ○ Check your computer manufacturer’s      We will be using QEMU as our hypervisor.

     manual if unsure.
● Disk Space: At least 20 GB of free
  storage for the virtual machine.
● Memory: Minimum 4 GB RAM (8 GB
  recommended).
     QEMU INSTALLATION & ISO PREPARATION

● Download QEMU from
  https://qemu.weilnetz.de/w64/(Search for the
  “QEMU installer” under the base directory.)
● Run the installation wizard and make sure to
  enable the “Add QEMU to System PATH”
  option.
● Open a terminal window, and check the qemu
  installed version, using the following
  command:


● After this, download the Ubuntu distro .iso
                                                 https://qemu.weilnetz.de/w64/ directory.
  from https://ubuntu.com/download/desktop
      QEMU INSTALLATION & ISO PREPARATION

● Create a virtual QEMU DISK at your preferred local pwd.
  ○ Run the command qemu-img create wizard and make sure to enable the
    “Add QEMU to System PATH” option.



● With the Ubuntu .iso and QEMU disk created, use the following to start the vm:




                                         If the commands fails, make sure the qemu installation directory is added to the user PATH.
4.
 Basic shell commands
                         Basic Shell commands
After the initial Ubuntu setup, open a terminal using: CTRL + ALT + T
1. ls – Lists ﬁles and directories in the current
   folder.
2. pwd – Prints the current working directory
   (shows where you are).
3. cd – Changes the current directory.
4. cp – Copies ﬁles or directories.
5. mv – Moves or renames ﬁles and directories.
6. rm – Removes (deletes) ﬁles or directories.
7. source – Runs a script in the current shell
   environment.
8. export – Sets environment variables.
9. exit – Closes the current terminal session.
                                                                Ubuntu default terminal.

              Try this commands!
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
