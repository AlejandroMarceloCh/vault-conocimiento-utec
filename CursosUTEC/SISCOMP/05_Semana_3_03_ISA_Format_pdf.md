---
curso: SISCOMP
titulo: 05 - Semana 3/03. ISA Format
slides: 32
fuente: 05 - Semana 3/03. ISA Format.pdf
---

COMPUTER SYSTEMS

      ISA FORMAT
Motivation
We need to move to a higher abstraction level between
the software and detailed hardware.

We need to understand the processor instructions to
be able to give commands.




Goals
Understand the instruction cycle.

Identify the RISC V instruction types and instruction
formats.
Summary

1.   Instruction
     Execution           4.   Language Machine
                              Code




2.   Instruction Cycle
                         5.   Conclusions




3.   Instruction Types
                         6.
1.
     Instruction Execution
                        Instruction Execution
By using instructions we can speak the language of the computer

Thus, we now know how to tell the computer to:

  ○ Execute computations in the ALU by using, for instance, an addition
  ○ Access operands from memory by using the load word instruction


             How are the instructions executed on the computer?

 The process of executing an instruction is called is the instruction cycle or instruction
                                        phases.
2.
 Instruction Cycle
                                   Instruction Cycle
The instruction cycle is a sequence of steps or phases, that an instruction goes through to be executed

              1.   FETCH: Take the instruction
              2.   DECODE: What is the instruction about?
              3.   EVALUATE ADDRESS: Does it need something (data) from mem.?
   Next
Instruction
              4.   FETCH OPERANDS: Take all the operands
              5.   EXECUTE: Perform the instruction real job.
              6.   STORE RESULT: Save the result (if it is needed …)

E.g.: Intel x86 instruction ADD [eax], edx has six phases

Not all instructions have the six phases. E.g:

          LW does not require EXECUTE
          ADD does not require EVALUATE ADDRESS
1. Fetch
The FETCH phase obtains the instruction from memory
and loads it into the instruction register.


                Step 1: Load MAR
                and increment PC


                                                      +1
                  Step 2: Access
                     memory

                  Step 3: Load IR
                 with the content
                     of MBR
  2. Decode
The DECODE phase identiﬁes the instruction.

• A 4-to-16 decoder identiﬁes which of the 16
  opcodes is going to be processed.

  • A decoder, the input is the four bits IR[24:21]




      DECODE identiﬁes the instruction
            to be processed
      3. Evaluate Address
The EVALUATE ADDRESS phase computes the address
of the memory location that is needed to process the
instruction.
                                                                Reg
Examples:                                                       File



1.    This phase is necessary in LW.
       It computes the address of the data word that is to be
       read from memory by adding an offset to the content of
       a register
2.    But not necessary in ADD.



     LDR calculates the address by adding a register
                   and an immediate
4. Fetch Operands
The FETCH OPERANDS phase obtains the source
operands needed to process the instruction.

Example: In LW
• Step 1: Load MAR with the address calculated in
  EVALUATE ADDRESS
• Step 2: Read memory, placing source operand in MBR

Example: In ADD
• Obtain the source operands from the register ﬁle
• In most current microprocessors, this phase can be done
  at the same time the instruction is being decoded




   LDR loads MAR (step 1), and places the
          results in MBR (step 2)
 4. Fetch Operands
The FETCH OPERANDS phase obtains the source
operands needed to process the instruction.

Example: In LW                                              Reg
                                                            File
• Step 1: Load MAR with the address calculated in
  EVALUATE ADDRESS
• Step 2: Read memory, placing source operand in MBR

Example: In ADD
• Obtain the source operands from the register ﬁle
• In most current microprocessors, this phase can be done
  at the same time the instruction is being decoded




      ADD operands from Register File.
  5. Execute

The EXECUTE phase executes the instruction

Example: In ADD, it performs addition in the ALU




          ADD adds SR1 and SR2
6. Store Results
The STORE RESULT phase writes to the designated
destination.

                                                    Reg
Once STORE RESULT is completed, a new instruction   File
cycle starts (with the FETCH phase)




    Instruction writes to RegFile or Memory
3.
     Instructions Types
                       RISC V Types of instructions

Three main types of instructions:

1.    Data-processing Instructions

     A. Logical operations
     B. Shifts / rotate
     C. Arithmetic
         c1. with conditional Execution
2. Branches
3. Memory
RISC V Types of instructions
3.
     Instructions Format
  R - Type Functions
R-type (register-type) instructions use three registers as operands: two as sources and one as a
destination
                              R - Type Functions
Translate the following RISC-V assembly instruction into machine language


                                      add t3, s4, s5

                                  I - Type Functions
● I-type (immediate) instructions use two register operands and one immediate operand.

● I-type instructions include addi, andi, ori, and xori, loads (lw, lh, lb, lhu, and lbu), and register
  jumps (jalr)
                             I - Type Functions
Translate the following assembly instruction into machine language.

                                          lw t3, −36(s4)
                           I - Type Functions
● I-type (immediate) instructions use two register operands and one immediate operand.

● I-type instructions include addi, andi, ori, and xori, loads (lw, lh, lb, lhu, and lbu), and register
  jumps (jalr)
                             S/B Type Functions

Like I-type instructions, S/B-type (store/branch) instructions use two register operands and one
immediate operand. However, both of the register operands are source registers (rs1 and rs2) in S/B-type,
whereas I-type instructions use one source register (rs1) and one destination register (rd)
                             S/B Type Functions
Branches (beq, bne, blt, bge, bltu, and bgeu) use the B-type instruction format.For B-type instructions,
rs1 and rs2 are the two source registers, and the 13-bit immediate branch offset, imm12:0 , gives the
number of bytes between the branch instruction and the BTA.
                             S/B Type Functions

Like I-type instructions, S/B-type (store/branch) instructions use two register operands and one
immediate operand. However, both of the register operands are source registers (rs1 and rs2) in S/B-type,
whereas I-type instructions use one source register (rs1) and one destination register (rd)
                              U/J Type Functions
U/J-type (upper immediate/jump) instructions have one destination register operand rd and a 20-bit
immediate ﬁeld. In U-type instructions, the remaining bits specify the most signiﬁcant 20 bits of a 32-bit
immediate. In J-type instructions, the remaining 20 bits specify the most signiﬁcant 20 bits of a 21-bit
immediate jump offset.
4.
 Language Machine
 Code
             Interpreting Machine Language Code

To interpret machine language, one must decipher the ﬁelds of each 32-bit instruction word.
Different instructions use different formats, but all formats share a 7-bit opcode ﬁeld.
Thus, the best place to begin is to look at the opcode to determine if it is an R-, I-, S/B-, or U/J-type
instruction.
E.g. Translate the following machine language code into assembly language.


            0x41FE83B3
            0xFDA48293
                               Conclusions
Now we can speak the language of the computer

Thus, we now know how to tell the computer to:

  ○ Execute computations in the ALU by using, for instance, an addition
  ○ Access operands from memory by using the load word instruction




                    Now we know the Instruction Cycle
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
