---
curso: SISCOMP
titulo: 04 - Semana 2/02a.Assembly Language
slides: 24
fuente: 04 - Semana 2/02a.Assembly Language.pdf
---

COMPUTER SYSTEMS

     ASSEMBLY LANGUAGE
Goals

Analyze the assembly language and the instruction set
                architecture of RISC V
Summary

1.   Numerical Systems
                           4.   Boolean algebra




2.   Memory organization
                           5.   Sign/Zero/Shift
                                Operations




3.   Byte ordering
                           6.   Conclusions
1.
     Instructions
                        RISC V Architecture

● An instruction the most basic unit of computer processing:

  - Instructions are words in the language of a computer
  - Instruction Set Architecture (ISA) is the vocabulary

● RISC V is a Reduced Instruction Set Computer (RISC), with a small number of
  simple instructions
  Other architectures, such as Intel’s x86, are Complex Instruction Set Computers
  (CISC)
                             Sequential Execution
● Instructions and data are stored in memory: Typically the instruction length is the word length

● Instructions: Commands in a computer’s language

  • Assembly language: human-readable format of instructions
  • Machine language: computer-readable format (1’s and 0’s)


● The processor fetches instructions from memory sequentially (ﬁrst one instruction, then the next one)


● The address of the current instruction is stored in the program counter (PC)
 • If word-addressable memory, the processor increments the PC by 1.
 • If byte-addressable memory, the processor increments the PC by the word length (4 in ARM)

E.g: OS sets the PC to 0x00400000 (start of a program), increment from this address value.
                     Program Stored in Memory
● 4 instructions stored in consecutive words in memory
● No need to understand the program now. We will get back to it
Memory Map
                     ADD Instruction


      C Code                     RISC V Assembly Code
      a = b + c;                 add a, b, c



• ADD: mnemonic – indicates operation to perform
• b, c: source operands
• a: destination operand
                     SUB Instruction

      C Code                      RISC V Assembly Code
      a = b + c;                  SUB a, b, c



• SUB: mnemonic – indicates operation to perform
• b, c: source operands
• a: destination operand
                  Multiple Instructions

More complex code handled by multiple RISC V instructions



    C Code                     RISC V assembly code
    a = b + c - d;             ADD t, b, c       # t = b + c
                               SUB a, t, d       # a = t - d
           Instructions with Registers

ADD Instruction


        C Code        RISC V Assembly Code
                      # R0 = a, R1 = b, R2 = c

        a = b + c     ADD R0, R1, R2
   Operands: Constants and Immediates

● Many instructions can use constants or immediate operands

● For example: ADD and SUB

● Value is immediately available from instruction



         C Code                   RISC V Assembly Code
                                  #R0 = a, R1 = b
         a = a + 4;               addi R0, R0,4
         b = a – 12;              addi R1, R0,-12
            Generating Constants

      Constant must have < 8 bits of precision

C Code                       RISC V Assembly Code

a = 23;                      # R0 = a, R1 = b
b = -78;                     addi R0, zero, 23
                             addi R1, zero, -78
         Generating Larger Constants

     load upper immediate (lui) < 20-bit (MSB)

C Code                      RISC V Assembly Code

a = 0xABCDE123              lui s2, 0xABCDE
                            addi s2, s2, 0x123
                       Memory
RISC V uses 32-bit memory addresses and 32-bit data words in
                  byte-addressable memory
                     Endianness




RISC V uses 32-bit memory
addresses and 32-bit data
words in byte-addressable
         memory
             Reading Memory

                   load word (lw)

C Code                                 RISC V Assembly Code

a = mem[2]                             #s5 = a
                                       lw s5, 8(zero)


             The code loads memory word 2, located
                    ad address 8 into a (s5)
                       zero: base register
            Writing Memory

                 store word (sw)

C Code                              RISC V Assembly Code

mem[5]=42                           addi t3,zero,42 #t3 = 42
                                    sw t3, 20(zero)


             Code writes the value 42 from register t3
            into memory word 5, located at address 20
                               Ada Lovelace

● British mathematician , 1815-1852

● Wrote the ﬁrst computer program

● Her program calculated the Bernoulli numbers on
  Charles Babbage’s Analytical Engine

● She was a child of the poet Lord Byron


    At her time, no high-level languages:
        • e.g., C, Java, Python
        • Written at higher level of abstraction

 Types of Instructions and Programming
 Blocks
Three main types of instructions:

1. Data-processing Instructions
2. Branches
3. Memory                           We study how to
                                    implement
                                    high-level programs
High-level Constructs:              using low-level
    •   if/else statements          deﬁnitions
    •   for loops
    •   while loops
    •   arrays
    •   function calls
How are these instructions executed?

 ○   By using instructions we can speak the language of the computer


 ○   Thus, we now know how to tell the computer to


        ■   Execute computations in the ALU by using, for instance, an addition
        ■   Access operands from memory by using the load word instruction


 ○   But, how are these instructions executed on the computer?
        ■   The process of executing an instruction is called is the instruction cycle
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
