---
curso: SISCOMP
titulo: 03 - Semana 1/01.Data types and representation.pptx
slides: 28
fuente: 03 - Semana 1/01.Data types and representation.pptx.pdf
---

COMPUTER SYSTEMS

   DATA TYPES AND REPRESENTATION
Goals

 Analyze the main topics associated with data types,
        data sorting, and numerical systems.
Summary

1.   Numerical Systems
                           4.   Boolean algebra




2.   Memory organization
                           5.   Sign/Zero/Shift
                                Operations




3.   Byte ordering
                           6.   Conclusions
1.
     Numerical Systems
                                     Bits

● Binary Digit

● Useful for instructions, represent and manipulate numbers, sets, strings, etc.

● Electronic implementation: Bistable elements.
                    Numerical Systems

● Decimal numbers



● Binary numbers



● Hexadecimal numbers
                          Number Conversion
● Decimal to binary conversion

Convert


● Binary to decimal conversion

Convert


● Hexadecimal to decimal conversion

Convert
        Range for binary and decimal values

● N-digit binary number




● N-digit decimal number
                    Bits, Bytes and nibbles

● Bits

                                    ● 1 byte = 8 bits

                                    ● From 0 to 11111111 (binary)
● Bytes & Nibbles
                                    ● From 0 to 255 (decimal)

                                    ● From 0 to FF (hexadecimal)
● Bytes                        v
                            Data Representation

Data Type (C programming)         Typical 32-bit   Typical 64-bit
          char                          1                1
          short                         2                2
           int                          4                4
          long                          4                8
          float                         4                4
         double                         8                8
         pointer                        4                8
2.
 Memory organization:
 Byte oriented
Machine words
                 ● Native unit of information.
                 ● Machines have 64-bit word size.



                      Byte - Oriented
                Data accessed by programs : Address
3.
     Byte Ordering
                 How bytes are ordered in memory
● Big Endian :

     Least signiﬁcant byte has highest address (Sun, Mac, Internet).

● Little Endian:

     Least signiﬁcant byte has lowest address (x86, ARM, iOS, RISC-V).

  Example:

  Variable m has 4-byte value of 0x19283746, and the address &m is 0x200

  Big Endian                                     Little Endian
         0x200   0x201   0x202   0x203                  0x200    0x201   0x202   0x203

         19      28      37      46                     46         37    28      19
              Negative Numbers Representation
   Two-complement encoding to represent signed numbers.

   Method

1. Convert the unsigned number to binary.
2. After the least signiﬁcative “1”, invert all numbers.

   Example

The binary representation of -19 is:

1. 19 = 100112
2. Unsigned number: 100112 and invert: 011012, so the two-complement of -19 is 011012
4.
 Boolean Algebra
                George Boole and his Algebra

Algebraic representation of logic: “1” is true, “0” is false.

Some important operators are:

1. A & B   : AND operator
2. A | B   : OR operator
3. ~A      : NOT operator
4. A^B     : XOR operator

Operators &, |, ~, ^ are bitwise.
Operators &&, || are not bitwise.
               George Boole and his Algebra


   A&B                A|B             ~A             A^B
AND operator       OR operator    NOT operator   XOR operator




 A   B   A&B        A   B   A&B      A    ~A      A   B   A&B

 0   0    0         0   0    0       0    0       0   0    0

 0   1    0         0   1    1       1    1       0   1    1

 1   0    0         1   0    1                    1   0    1

 1   1    1         1   1    1                    1   1    1
5.
 Sign/Zero/Shift
                            Sign Extension

Number value is the same, sign bit is copied to most signiﬁcant bits.

Example

● 2 in 4-bit representation: 0010
● 2 in 8-bit sign-extended: 00000010

Example with signed numbers

● -6 in 4-bit representation: 1010
● -6 in 8-bit sign-extended: 11111010

                           Zero Extension

Number value is the same, zeros are copied to most signiﬁcant bits.

Example

● 2 in 4-bit representation: 0010
● 2 in 8-bit zero-extended: 00000010

Example with signed numbers

● -6 in 4-bit representation: 1010
● -6 in 8-bit zero-extended: 00001010
                                      Shift operations



                 Left Shift: x << y                          Right Shift: x >> y


● Shift x left y positions                     ● Shift x right y positions

● Throw away                                   ● Throw away
extra bits on left                             extra bits on right

● Fill with 0’s on right                       ● Fill with 0’s on left

                                                     Arithmetic Shift: Repeat MSB on left
                     Operations with Overﬂow
Overﬂow is when the result is too big to ﬁt in the bit size.

  Addition with                          Negation: Complement and add 1
    Overﬂow
                   Operations with Overﬂow
Integer subtraction: Add negation of second operand


     Subtraction with Overﬂow                   Subtraction with Overﬂow

                                      ● Subtraction of two + or two - : No overﬂow

                                      ● Subtraction + from - : Overﬂow if sign is 0

                                      ● Subtraction - from + : Overﬂow if sign is 1
Signed/Unsigned representation
Conclusions
 Data representation is fundamental to understand how computers
 work.



 Numerical systems allow to express big numbers amounts and
 operations.



 Signed numbers allow negative values to be represented in a computer
 system


 Boolean algebra translates logical operations (usually verbal) into
 mathematical expressions that the computer can execute based on
 instructions.
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
