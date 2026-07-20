---
curso: SISCOMP
titulo: 07 - Semana 5/05. Pseudo Instructions.pptx
slides: 19
fuente: 07 - Semana 5/05. Pseudo Instructions.pptx.pdf
---

COMPUTING SYSTEMS

    RISC-V Pseudoinstructions
Goals

Learn about RISC-V Pseudo-Instructions (not part of
the ISA Format) and how they are assembled into
actual Machine Code instructions.
Summary

1.   Recall: ISA




2.   Pseudoinstructions
1.
     Recall: RISC-V
     Instructions
Recall: RISC-V Instructions
               Recall: RISC-V Instructions
ONLY THESE SIX INSTRUCTION TYPES EXIST!
                  Recall: RISC-V Instructions
However: We could use some other useful instructions!

    Examples:

   1. mv - (move) to copy values from one register to another.
   2. li - (load immediate) load an immediate value to a register.
   3. not - logical not.
   4. call - jump to a function in <label> and save return.
   5. ret - (return) return to caller.
   6. j - unconditional jump.
   7. jr - jump to address in reg.
   8. nop - do nothing.
      and many more…

    None of these are part of the RISC-V INSTRUCTION FORMAT
    But a RISC-V CPU could easily do them, using existing instructions!
2.
 Pseudoinstructions
                   RISC-V Pseudoinstructions


● Not part of the instruction set (cannot be directly converted to machine code).

● They are useful to programmers and compilers.

● Their intended goal CAN be achieved with one or more “real” instructions.

● They are converted into CPU compatible instructions during assembly.


           Pseudoinstructions are useful when coding, but the CPU
                 ends up executing something different☺
                                                    LI (LOAD IMMEDIATE)


                 li rd, imm                        ● Allows loading an immediate value into a
                                                     destination register.
                                                   ● If the immediate is up to 12 bits, the instruction
                                                     addi rd, x0, imm is used.
       No       Is imm > 12 bits ?     Yes
                                                   ● If the immediate is larger than 12 bits, it is split
                             lui rd, imm[31:12]      into two parts:
addi rd,x0,imm[11:0]                                 ○ The upper part is loaded with lui rd, imm[31:12].
                            addi rd,x0,imm[11:0]
                                                     ○ Then it is adjusted with addi rd, rd, imm[11:0].
                  NOP (NO OPERATION)


    nop          ● Indicates a “no operation” instruction, whose
                   execution does not produce any changes in
                   the registers or memory.
                 ● It is mainly used to create delay loops or to
                   resolve data dependencies.
addi x0,x0, 0
x0 always be 0
                  NOT

                 ● Indicates a bitwise logical negation (inverts
 not rd,rs1        all bits of a register).
                 ● It is implemented using an immediate XOR,
                   since an XOR with a number composed of all
                   '1's (which is -1) inverts each bit of the
                   operand.
xori rd,rs1,-1

                                             Recall: XOR properties
3.
     Directives
The program in the Code begins by
making the main label global (.globl main)
so that the main function can be called
from outside this ﬁle, typically by the OS or
bootloader.

The value N is then set to 5 (.equ N, 5).

What else?
Memory       Final
allocation   values of
of global    global
variables    variables
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
