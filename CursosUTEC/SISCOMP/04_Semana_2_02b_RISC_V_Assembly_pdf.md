---
curso: SISCOMP
titulo: 04 - Semana 2/02b.RISC V Assembly
slides: 29
fuente: 04 - Semana 2/02b.RISC V Assembly.pdf
---

COMPUTER SYSTEMS

     RISC V ASSEMBLY
Goals

Analyze the assembly language and the instruction set
                architecture of RISC V
Summary

1.   Conditional
     Statements    4.   Conclusions




2.   Loops




3.   Arrays
                                  Summary
Motivation: Programs at high-level languages can be executed in modern
processor systems.


   Problem: We need to understand the machine code and deﬁne its
         relationship with programming languages constructs.


Overview:
● Overview of conditional statements, loops, arrays and function calls.
● ARM Assembly programming for high-level constructs.
● Code and execute with an ARM emulator.


Conclusion: We can create complex programs using assembly language
            by deﬁning correct machine code instructions.
1.
     Conditional
     Statements
                  If Statement

High level Code           RISC V Assembly Code

if(a == m)
  f = g+h;
a = m - h;
                        If Statement

   High level Code                  RISC V Assembly Code

   if(a == m)                       #s0 = a, s1 = m
     f = g + h;                     #s2 = f, s3 = g, s4 = h
   a = m - h;
                                    BNE s0, s1, L1
                                    ADD s2, s3, s4
                                    L1:
                                    SUB s0, s1, s4


Assembly tests opposite case (i != j) of high-level code (i == j)
               If/Else Statement

High level Code          RISC V Assembly Code

if(a == m)
  f = g+h;
else
  a = m - h;
               If/Else Statement

High level Code          RISC V Assembly Code

if(a == m)               #s0 = a, s1 = m
  f = g + h;             #s2 = f, s3 = g, s4 = h
else
  a = m - h;               BNE s0, s1, L1
                           ADD s2, s3, s4
                           j L2
                         L1:
                           SUB s0, s1, s4
                         L2:
           Switch/Case Statement

High level Code              RISC V Assembly Code

switch(button){
  case 1: am = 20; break;
  case 2: am = 50; break;
  case 3: am = 100; break;
  default: am = 0;
}
                  Switch/Case Statement

High level Code                       RISC V Assembly Code

Equivalent with if/else

if        (button == 1)   am = 20;
else if   (button == 2)   am = 50;
else if   (button == 3)   am = 100;
else                      am = 0;
                      Switch/Case Statement
High level Code                     RISC V Assembly Code
switch(sim){                #s0 = sim, s1 = am     case3:
  case 1: am = 20; break;                             ADDI t0,zero, 3
  case 2: am = 40; break;   case1:                    BNE s0, t0, def
  case 3: am = 60; break;      ADDI t0,zero, 1        ADDI s1,zero,60
  default: am = 0;             BNE s0, t0, case2      j done
}                              ADDI s1,zero,20
                               j done              def:
                                                      ADD s1,zero,zero
                            case2:                 done:
                               ADDI t0,zero, 2
                               BNE s0, t0, case3
                               ADDI s1,zero,40
                               j done
2.
 Loops
                         While Loop
High level Code              RISC V Assembly Code
int pow = 1
int x = 0;

while(pow != 128){
  pow = pow*2;
  x = x + 1;
  }

What does the code do?
                                 While Loop
High level Code                           RISC V Assembly Code
int pow = 1                            #s0 = pow, s1 = x
int x = 0;
                                          ADDI s0,zero,1
while(pow != 128){                        ADDI s1,zero,zero
  pow = pow*2;                            ADDI t0,zero,128
  x = x + 1;                           while:
  }                                       BEQ s0,t0,done
                                          SLLI s0,s0,1
                                          ADDI s1,s1,1
What does the code do?
                                          J while
                                       done:


     Assembly tests for the opposite case (pow == 128) of the C code (pow != 128).
                               For Loop

For (initialization; condition; loop operation) statement

● Initialization: executes before the loop begins.

● Condition: is tested at the beginning of each iteration.

● Loop operation: executes at the end of each iteration.

● Statement: executes each time the condition is met.
                         Do/While Loop
High level Code                RISC V Assembly Code
int pow = 1
int x = 0;

do{
  pow = pow*2;
  x = x + 1;
  } while(pow != 128);
                         Do/While Loop
High level Code                RISC V Assembly Code
int pow = 1                    #s0 = pow, s1 = x
int x = 0;
                                 ADDI s0,zero,1
do{                              ADD s1,zero,zero
  pow = pow*2;                   ADDI t0,zero,128
  x = x + 1;
  } while(pow != 128);         while:
                                  SLLI s0,s0,1
                                  ADDI s1,s1,1
                                  BNE s0,t0,while
                               done:
                                 For Loop
High level Code                     RISC V Assembly Code
int sum = 0;
int i;

for(i = 0; i < 10; i = i + 1){
  sum = sum + i;
  }
                                 For Loop
High level Code                     RISC V Assembly Code
int sum = 0;                         #s0 = i, s1 = sum
int i;
                                        ADDI s1,zero,0
for(i = 0; i < 10; i = i + 1){          ADDI s0,zero,0
  sum = sum + i;                        ADDI t0,zero,10
  }                                  for:
                                        BGE s0,t0,done
                                        ADD s1,s1,s0
                                        ADDI s0,t0,1
                                        J for
                                     done:

                                 For Loop
High level Code                     RISC V Assembly Code
int sum = 0;                         #s0 = i, s1 = sum
int i;
                                        ADDI s1,zero,0
for(i = 0; i < 10; i = i + 1){          ADDI s0,zero,0
  sum = sum + i;                        ADDI t0,zero,10
  }                                  for:
                                        BGE s0,t0,done
                                        ADD s1,s1,s0
                                        ADDI s0,t0,1
                                        J for
                                     done:




                How to do a decremental loop?
3.
     Arrays
                                    Arrays


Access large amounts of similar data:

  ● Index: access to each element
  ● Size: number of elements

Example: 5-element array

Base address = 0x14000000
  (address of ﬁrst element, scores[0])

Array elements accessed relative to base address.
                   For Loop to access an array
High level Code                  RISC V Assembly Code
                                  #s0 = scores base address, s1 = i
int i;
int scores[200];                  ADDI s1,zero,0
                                  ADDI t2,zero,200
for(i = 0; i < 200; i = i + 1)
                                  for:
  scores[i] = scores[i] + 10      BGE s1,t2,done
                                  SLLI t0,s1,2
                                  ADD t0,t0,s0
                                  LW t1, 0(t0)
                                  ADDI t1,t1,10
                                  SW t1, 0(t0)
                                  ADDI s1,s1,1
                                  J fo
                                  done:
 ASCII Code and Cast of
       Characters

• American Standard Code for Information
 Interchange (ASCII)

• Each text character has unique byte value
    • For example, S = 0x53, a = 0x61, A = 0x41
    • Lower-case and upper-case differ by
      0x20 (32)
                         Load & Store in an array

● RISC-V also deﬁnes lh, lhu, and sh half-word loads and stores that operate on 16-bit data.
● Memory addresses for these instructions must be half-word aligned



                                             “Hello!”

                                        H = 0x48
                                        e = 65
                                        l = 6C
                                        l = 6C
                                        o = 6F
                                        ! = 21
                                        Null = 00
Conclusions
 We reviewed fundamentals concepts in programming languages
 constructs.



 We reviewed assembly implementation for conditional statements,
 loops, arrays.



 We coded and executed high-level constructs using ARM syntax and
 instructions.



 We conclude that complex programs have a direct implementation in
 machine code that allows to execute them in the processor.
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
