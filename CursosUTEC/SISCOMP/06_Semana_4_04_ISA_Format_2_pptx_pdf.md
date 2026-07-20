---
curso: SISCOMP
titulo: 06 - Semana 4/04. ISA Format 2.pptx
slides: 34
fuente: 06 - Semana 4/04. ISA Format 2.pptx.pdf
---

COMPUTING SYSTEMS

 ISA FORMAT - MEMORY INSTRUCTIONS (LD/ST)
Motivation
We need to move beyond registers and reach memory
to make programs meaningful.

Understanding processor instructions allows us to
control data ﬂow and program behavior.




Goals
Manipulate memory directly with bare-metal load and
store instructions.

Understand how RISC-V addresses memory through
base registers and offsets.
Summary

1.   Memory
                           4.   Arrays




2.   Endianness
                           5.   Conclusions




3.   RISC-V instructions
                           6.
1.
     Memory
The memory stores
    • Data
    • Programs
• The memory contains bits
    • Bits are grouped into bytes (8 bits) and words
      (e.g., 8, 16, 32 bits)
• How the bits are accessed determines the
  addressability
    • E.g., word-addressable
    • E.g., 8-bit addressable (or byte-addressable)


• The total number of addresses is the
  address space
    • In ARM, the address space is 232
         • 32-bit addresses
    • In x86-64, the address space is (up to) 248
         • 48-bit addresses
   • In RISC-V, the address space is commonly 232
         • 32-bit addresses
   Accessing Memory
• There are two ways of accessing memory
  6 • Reading or loading
    • Writing or storing
• Two registers are necessary to access
  memory
    • Memory Address Register (MAR)
    • Memory Data Register (MDR)
• To read
    • Step 1: Load the MAR with the address
    • Step 2: Data is placed in MDR
• To write
    • Step 1: Load the MAR with the address
      and the MDR with the data
    • Step 2: Activate Write Enable signal
     Word-Addressable Memory
• Each data word has a unique address
     • In RISC-V, a unique address for each 32-bit data word
 7


                      Word Address                    Data     RISC-V memory

                                . . .                  . . .     . . .

                             00000003         D1617A1C           Word 3

                             00000002         13C81755           Word 2

                             00000001         F2F1F0F7           Word 1

                             00000000         89ABCDEF           Word 0
   Byte-Addressable Memory
• Each byte has a unique address
 8
   • Actually, RISC-V is byte-addressable



                    Byte Address                     Data            ARM memory

                               . . .
                     of the Word
                                                        . . .             . . .

                             0000000C D 1         61        7A       1C   Word 3
                             00000008 1 3         C8            17   55   Word 2

                             00000004 F 2          F1           F0   F7   Word 1
                                            How are these four bytes
                             00000000       89 A    B    C
                                                  addressed?
                                                            D    E F      Word 0
2.
 Endianness
   Byte-Addressable Memory
• Each byte has a unique address
10
   • Actually, RISC-V is byte-addressable



                    Byte Address                     Data            ARM memory

                               . . .
                     of the Word
                                                        . . .             . . .

                             0000000C D 1         61        7A       1C   Word 3
                             00000008 1 3         C8            17   55   Word 2

                             00000004 F 2          F1           F0   F7   Word 1
                                            How are these four bytes
                             00000000       89 A    B    C
                                                  addressed?
                                                            D    E F      Word 0
    Big Endian vs Little Endian
• Jonathan Swift’s Gulliver’s Travels
    • Little Endians broke their eggs on the little end of the egg
 11
    • Big Endians broke their eggs on the big end of the egg




•   How to number bytes within a word?
    • Little-endian: byte numbers start at the little (least significant) end
    • Big-endian: byte numbers start at the big (most significant) end
     Big Endian vs Little Endian
                           Big Endian                                              Little Endian
12                                Byte                             Word                  Byte
                                 Address                          Address               Address

                                       . . .                              . . .
     It doesn’t really matter which addressing type used – except when two systems
                                        share data                                          . . .

                       C           D           E         F                   C     F    E           D    C

                       8           9           A         B                   8     B    A           9    8

                       4           5           6         7                   4     7    6           5    4

                       0           1           2         3                   0     3    2           1    0
                   MSB                                LSB                         MSB                   LSB
             (Most Significant Byte)           (Least Significant Byte)
3.
     RISC-V instructions
Operands: Memory

14
     • Too much data to fit in only 32 registers
     • Store more data in memory
     • Memory is large, but slow
     • Commonly used variables still kept in registers
Recall: Byte-Addressable Memory

   • Each data byte has unique address
15
   • 32-bit word = 4 bytes, so word address increments by 4
Reading Memory
                                                      Important: Memory
                                                      Instructions
 • Memory reads are called load
16
   lw rd, imm12(rs1)            # load word to rd

   Address calculation:
     – add base address (rs1) to the offset (imm12)
     – address = (rs1 + imm12)
   Result:
    – rd holds the data at memory address [rs1 + imm12]
   Any register may be used as base address


                        rd ← Memory[rs1 + imm12]
Reading Memory
Load Variations (16 or 8 bytes)
17


Sign-Extended (if MSB=1, extend with 1s):
- lh rd, imm(rs1)             Half-Word (16-bit)
- lb rd, imm(rs1)             Byte (8-bit)

Unsigned (Zero-extended):
- lhu rd, imm(rs1)                Half-Word Unsigned (16-bit)
- lbu rd, imm(rs1)                Byte Unsigned (8-bit)
Reading Memory
• Load Instructions use I-Type Format (op=0x03)
• lw, lh, lb, …, depend on funct3
• Offset can only be Immediate

                         I-Type
Reading Memory
 • Example: Read a word of data at memory address 8 into x3
19
   • Address = (x0 + 8) = (0 + 8) = 8
   • x3 = 0x01EE2842 after load


   RISC V - Assembly Code
   lw x3, 8(x0)
                             x3 ←
Writing Memory
                                                      Important: Memory
                                                      Instructions
 • Memory writes are called stores
20
   sw rd, imm12(rs1)               # store word to rd

   Address calculation:
     – add base address (rs1) to the offset (imm12)
     – address = (rs1 + imm12)
   Result:
     – rd holds the data at memory address [rs1 + imm12]
    Any register may be used as base address


                        rd -> Memory[rs1 + imm12]

 Writing Memory
• Write Instructions use S-Type Format (op=0x23)
• sw, sh, sb, …, depend on funct3
• Offset can only be Immediate
Recap: Accessing Memory

22

• Address of a memory word must be multiplied by 4
• Examples:
  • Address of memory word 2 = 2 × 4 = 8
  • Address of memory word 10 = 10 × 4 = 40
Recap: Big-Endian and Little-Endian Memory
• How to number bytes within a word?
23   – Little-endian: byte numbers start at the little (least significant) end
     – Big-endian: byte numbers start at the big (most significant) end
Big-Endian and Little-Endian Example
Suppose x2 and x5 hold the values 8 and 0x23456789
 24
• After following code runs on big-endian system, what value is in
    R7?
• In a little-endian system?
           sw x5, 0(x2)
           lb x7, 1(x2)


                                                 Big-endian:
                                                 0x00000045
                                                 Little-endian:
                                                 0x00000067
Byte Addressing - Example
Byte Addressing - Example


                    How will Mem[s4] look
                    after executing
                    sb s3, 1(s4)?
Byte Addressing - Example


                    How will Mem[s4] look
                    after executing
                    sb s3, 1(s4)?
4.
 Arrays
Arrays in Memory




                   Array:
                   Contiguous Memory

                   arr[i] = &arr + (i*4) // 4 Byte
                                 Arrays in Memory



                                                    Multidimensional:
                                                    Stored the same as
                                                    1D Array!!!




Are there any relation between
1D and 2D array addressings?
        A[i] =? B[x][y]
Iterating Over Array (For Loop)
                                  Conclusions
 Memory lets us build more complex programs, without being limited only by
 registers.
   ○ It allows storing much more data, giving programs state and persistence
     beyond registers.
   ○ It is not only for data , memory can also be used for controlling or accessing
     more things (network, external inputs, video buffers, etc).


“Computers are really, basically, computing elements and a lot of memory. They are
                     pretty easy to understand…” - Paul Allen
Reference Books
 Patterson, D. A., & Hennessy, J. L. (2020). Computer Organization and
 Design RISC-V Edition: The Hardware Software Interface. Morgan
 Kaufmann


 “The elements of computing systems: building a modern computer
 from ﬁrst principles” Nisan, N., & Schocken, S. (2021). MIT press


 ”Digital Design and Computer Architecture, RISC-V Edition”. Morgan
 Kaufmann. Harris, S., & Harris, D. (2021).
Questions?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
