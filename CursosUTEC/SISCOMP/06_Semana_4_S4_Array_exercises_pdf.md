---
curso: SISCOMP
titulo: 06 - Semana 4/S4_ Array exercises
slides: 2
fuente: 06 - Semana 4/S4_ Array exercises.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
September 12, 2025
                                                   S4: Array Exercises

Question 1. Create a function in RISC-V that changes the uppercase letters in a string to lowercase.
The string ends with a null character (ASCII 0). Modify the original string directly in memory (in-place).
Characters that are not uppercase letters (A-Z) should not be changed.

  1   void s tr i n g_ t o _l o w er c a se ( char ’ str ) ;

  str(en a0): Pointer to the beginning of the string. The string ends with a byte with a value of 0x00.
  The function does not return a value; it modifies the string.
   • Iterate through the string byte by byte. Use lbu to read and sub to write.
   • A letter is uppercase if its ASCII is between ’A’ (0x41) and ’Z’ (0x5A).
   • To convert an uppercase letter to lowercase, add 0x20 (the difference between a and A).
   • Stop when you find the null character (0x00).
   • Example: “Hello WORLD 123!” becomes “hello world 123!”
   • ASCII: ’A’ = 0x41, ’Z’ = 0x5A, ’a’ = 0x61, ’0’ = 0x00

Test on CPUlator: ”CS3051z\0” and the output is: ”cs3051z\0

Question 2. Translate the following C code to search for the maximum value on an 10 numbers array.

  1 Global array
  2     int numbers [10];
  3     int ge t_ la rg es t_ nu mbe r ()
  4     {
  5         int largest = numbers [0];
  6         for ( int i = 1; i <10; i ++) {
  7               if ( number [ i ] > largest )
  8                     largest = numbers [ i ];
  9         }
 10     return largest ;
 11     }

Question 3. Consider the following RISC-V assembly language snippet. The numbers to the left of each
instruction indicate the instruction address.

  1 0 xA0028     Func1 : addi t4 , a1 , 0
  2 0 xA002C     ori a0 , a0 , 32
  3 0 xA0030     sub a1 , a1 , a0
  4 0 xA0034     jal Func2
  5 0 xA0058     Func2 : lw t2 , 4( a0 )
  6 0 xA005C     sw t2 , 16( a1 )
  7 0 xA0060     srli t3 , t2 , 8
  8 0 xA0064     beq t2 , t3 , Else
  9 0 xA0068     jr ra
 10 0 xA006C     Else : addi a0 , a0 , 4
 11 0 xA0070     j Func2

  List the instruction type and addressing mode used at each line of code.

                                                               1
                                                                                                    2

Question 4. Consider the following C code:

  1 // C code
  2 void setArray ( int num ) {
  3     int i ;
  4     int array [10];
  5     for ( i = 0; i < 10; i = i + 1)
  6           array [ i ] = compare ( num , i ) ;
  7     }
  8 int compare ( int a , int b ) {
  9     if ( sub (a , b ) >= 0)
 10           return 1;
 11     else
 12           return 0;
 13 }
 14 int sub ( int a , int b ) {
 15     return a - b ;
 16 }

  Implement the C code snippet in RISC-V assembly language. Use s4 to hold the variable i. Be sure to
handle the stack pointer appropriately. The array is stored on the stack of the setArray function.
  IS-UTEC
