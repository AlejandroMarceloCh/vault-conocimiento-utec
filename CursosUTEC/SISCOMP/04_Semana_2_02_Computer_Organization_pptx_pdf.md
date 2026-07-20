---
curso: SISCOMP
titulo: 04 - Semana 2/02.Computer Organization.pptx
slides: 25
fuente: 04 - Semana 2/02.Computer Organization.pptx.pdf
---

COMPUTER SYSTEMS

    GENERAL INFORMATION
Goals

Understand the computer organization.

Identify the computer architectures and the Instruction
Set Architecture.
Summary

1.   Computer
     architecture   4.   Input / Output




2.   Memory
                    5.   First Concepts




3.   CPU
                    6.   Conclusions
              Computer Functions and Components
1. Data processing

   Multiple types of data and processing requirements.

2. Data storage

   ● Short-term
   ● Long-term

3. Data movement

   ● Input-output (I/O): when data are received from or delivered to a device
     (peripheral) that is directly connected to the computer
   ● Data communications: when data are moved over longer distances, to or
     from a remote device

4. Control

   A control unit manages the computer’s resources in response to commands
   (instructions).
                        RISC V Architecture


● First open - source instruction set architecture with broad commercial support.

● Deﬁned in 2010 by Krste Asanovic, Andrew Waterman, David Patterson.

● Comparable in capabilities to commercial architectures such as ARM and x86.

● Commercial chips: SiFive and Western Digital



          Once you’ve learned one architecture, it’s easier to learn
                            a different one ☺
1.
     Computer
     Architecture
                                                                  Von Neumann Architecture

                                                              ●     After Turing Machine (1936).

                                                              ●    Memory

                                                                    ○     Data memory
                                                                    ○     Instruction memory

                                                              ●    CPU
                                                                    ○ Arithmetic Logic Unit
                                                                    ○ Registers
                                                                    ○ Control




Proposed by [Burks, Goldstein and von Neumann, 1946] in “Preliminary discussion of the logical design of an electronic computing instrument”
                        Von Neumann Model
5 parts:
● Memory
● Processing Unit
● Input
● Output
● Control Unit

BottleNeck:
Total time for access data can be higher than
the execute program time.
                                                                                    Modiﬁed Harvard
              Harvard Architecture
                                                                                      Architecture




●   Complete separation of Instruction and Data memory regions.   ●   Some degree of separation between Instruction and Data
●   Rarely used in modern computers.                                  memory regions.
                                                                  ●   Modern Processors.
2.
 Memory
                                         Memory



                                                                                                      Instruction
    Physically           Logically           ROM vs RAM                 Data Memory
                                                                                                        Memory

Linear sequence of       To Store        Read Only Memory:          -   High - level program.     -   Before high - level.
                                                                                                  -   Low - level
    REGISTERS        -   Data.           Sequential occupation of   -   Variables, arrays, etc.       instructions.
                     -   Instructions.   locations..
                                                                    -   HW level:                 -   Binary values.
-   Addressable.           HOW?          Random Access Memory:          Binary values
-   Fixed-size                                                                                    -   Executable (binary)
                     Sequence of bits    Every register can be      -   Reading/Writing
                                         reached instantaneously.       memory registers.         -   Load to disk for
                                                                                                      running a program.
                          Memory
1. The memory stores

   Data/Programs

2. The memory contains bits

   Bits are grouped into bytes (8 bits) and words (e.g., 8, 16, 32 bits)

3. How the bits are accessed determines the
   addressability

  • E.g., word-addressable
  • E.g., 8-bit addressable (or byte-addressable)

• The total number of addresses is the address space

  • In x86, the address space is 2^32 y 2^64.
  • In ARM, the address space is 232.
        • 32-bit addresses
  • In x86-64, the address space is (up to) 248.
        • 48-bit addresses
                  Accessing Memory
1. There are two ways of accessing memory

  • Reading or loading
  • Writing or storing

2. Two registers are necessary to access memory

  • Memory Address Register (MAR)
  • Memory Data Register (MDR)

3. To read

  • Step 1: Load the MAR with the address
  • Step 2: Data is placed in MDR

4. To write

  • Step 1: Load the MAR with the address and the MDR
    with the data
  • Step 2: Activate Write Enable signal
3.
     Control Processing
     Unit
                                  Central Processing Unit
                                                Instructions

Execute the
                                                Tells the CPU which
instructions:                                   computation to perform



   Instructions
                                                               Instructions

   Tells the CPU which
                                                               Which execute next
   registers to access


                  Main Elements


                  ALU                                                  All Embedded
                  Set of registers
                  Control Unit
                           Processing Unit
• The processing unit can consist of many functional
  units.



• We start with a simple Arithmetic and Logic Unit
  (ALU), which executes computations
     • ARM: add, sub, mult, and, nor, …

• The ALU processes quantities that are referred to as
  words
     • Word length In ARM it is 32 bits

• Temporary storage: Registers:
  • E.g., to calculate (A+B)*C, the intermediate result of A+B
    is stored in a register
                                       REGISTERS
• Memory is big but slow

• Registers
   Registers are faster than memory
   Ensure fast access to operands
   Typically one register contains one word



• Register set or ﬁle
   RISC - V has 32 registers
   Each register is 32 bits (RV32I)
4.
 Input / Output
           Input and Output
 • Many devices can be used for input and output

 • They are called peripherals

 • Input
      • Keyboard
      • Mouse
      • Scanner
      • Disks
      • Etc.

• Output
     • Monitor
     • Printer
     • Disks
     • Etc.
              Control Unit


● The control unit is similar to the conductor of an
  orchestra

● It conducts the step-by-step process of
  executing (every instruction in) a program

● It keeps track of the instruction being executed
  with an instruction register (IR), which contains
  the instruction

● Another register contains the address of the
  next instruction to execute. It is called program
  counter (PC) or instruction pointer (IP)

         Programmer Visible (Architectural)
M[0]
         State
M[1]
M[2]
M[3]
                             Registers                              Instructions (and
M[4]
                             - given special names in the ISA    programs) specify how
                                (as opposed to addresses)       to transform the values
                             - general vs. special purpose       of programmer visible
M[N-1]                                                                    state

         Memory                          Program Counter
Array of storage locations             memory address
 indexed by an address            of the current instruction
                         Von Neumann
                            Model
Also called stored program computer (instructions
in memory). It has two key properties:

1. Stored program
     • Instructions stored in a linear memory array
     • Memory is uniﬁed between instructions and data.
     • The interpretation of a stored value depends on the
       control signals


2. Sequential instruction processing
     • One instruction processed (fetched, executed,
       completed) at a time
     • Program counter (instruction pointer) identiﬁes the
       current instruction
     • Program counter is advanced sequentially except for
       control transfer instructions
                       Arithmetic Logic Unit

Low - level arithmetic and logical
operations featured by the computer.

ALU functionality: Manufacturer design.

● HW Implementations: Efﬁcient but more
  expensive hardware.

● SW Implementations: Inexpensive and
  less efﬁcient.
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
Questions?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
