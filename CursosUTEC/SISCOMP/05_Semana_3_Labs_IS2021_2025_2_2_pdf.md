---
curso: SISCOMP
titulo: 05 - Semana 3/Labs_IS2021_2025___2-2
slides: 2
fuente: 05 - Semana 3/Labs_IS2021_2025___2-2.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
September 4, 2025
                                        S3: Assembly Exercises


Question 1. Write the following strings using ASCII encoding. Write the final answer in hexadecimal:
   • hello there
   • To the rescue!

Question 2. Store the strings of the exercise 1 in a byte-addressable memory starting at memory address
0x004F05BC. The first character of the string is stores at the lowest byte address. Indicate the memory
address of each byte.
Question 3. The nor instruction is not part of the RISC-V instruction set because the same functionality
can be implemented using existing instructions. Write a short assembly code snippet that has the following
functionality: s3 = s4 NOR s5. Use as few instructions as possible.
Question 4. Convert the following hig-level code snippets into RISC-V assembly language. Assume g
and h as variables that are located in a0 and a1, respectively.

  1 if ( g > h )
  2      g = g + 1;
  3 else
  4      h = h - 1;


  1   if ( g <= h )
  2        g = 0;
  3   else
  4        h = 0;


Question 5. Convert the following high-level code snippet into RISC-V assembly. Assume that the base
address of array1 and array2 are held in t1 and t2 and that the array2 is initialized before it is used. Use
as few instructions as possible.

  1   int   i;
  2   int   array1 [100];
  3   int   array2 [200];
  4   ...
  5   for   ( i = 0; i <100: i = i + 1)
  6         array1 [ i ] = array2 [ i ];


Question 6. Write RISC-V assembly code for placing the following immediates in s7. Use a minimum
number of instructions.
   • 29
   • -214
   • -2999
   • 0xABCDE000
   • 0xEEEEEFAB




                                                     1
                                                                                                              2

Question 7. Write a high-level language function for int find42(int array[], int size). Size specifies the
number of elements in array, and array[], specifies the base address of the array. The function should
return the index number of the first array entry that holds the value of 42. If no array entry is 42, it should
return the value -1.
Question 8. Convert the high-level function from exercise 7 into RISC-V assembly code.
  IS-UTEC
