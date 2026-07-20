---
curso: SISCOMP
titulo: 05 - Semana 3/Labs_IS2021_2025___2-1
slides: 2
fuente: 05 - Semana 3/Labs_IS2021_2025___2-1.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
September 9, 2025
                                               Laboratorio 1

Question 1. (8 ptos) Escribir un código en RISC V Assembly capaz de detectar overflow cuando se
suman dos números con signo, considere que los números se deben almacenar en a1, a2 y el resultado de
la operación se debe guardar en a0. Cuando hay overflow, guarde en el registro x2 el valor de 15 y cuando
no hay overflow guarde en el registro x2 el valor de 14.
     • Adjunte su código en .txt, completamente comentado.
     • Complete la siguiente tabla probando los casos indicados (el PC debe ser el valor que se lee al final
       del lazo).
     • En el caso 6, agregue una combinación de valores adicional a las pruebas solicitadas.
     • Complete la tabla con los valores tal y como los muestra la herramienta cpulator.

  Caso         a1               a2                  a0                 PC                  x2
  1            10               12
  2            10               -12
  3            10               10
  4            0                0
  5            -12              -12
  6

  Solución:

  1   addi a1 , a1 , -12
  2   addi a2 , a2 , -12
  3   add a0 , a1 , a2
  4   slti t1 , t2 ,0
  5   slt t2 , a0 , a1
  6   bne t1 , t2 , over
  7   addi x2 , x2 ,14
  8 over :
  9   addi x2 , x2 ,15

  Colocar la solución en: https://ripes.me

  Caso         a1               a2                  a0                 PC                  x2
  1            10               12                  0x16               0x1C                0x0E
  2            10               -12                 0xFFFFFFFE         0x20                0x0F
  3            10               10                  0x14               0x1C                0x0E
  4            0                0                   0                  0x1C                0x0E
  5            -12              -12                 0xFFFFFFE8         0x2C                0x0F
  6

Question 2. (7 ptos) Se tienen las siguientes instrucciones, señale cuáles de ellas utilizan un campo
Immediate en su formato de código máquina y de cuántos bits es, además señale el tipo de instrucción
(I,S,B,U o J), indique además cuáles de estas instrucciones utilizan formato extendido y de ellas, escrı́balo
en formato de 32 bits. Ingrese las instrucciones al compilador y verifique sus resultados. Adjunte su código
en .txt completamente comentado, cada lı́nea corre de manera independiente.
   Solución:
  IS-UTEC
                                                         1
                                                                          2

Instrucción       Imm (bits)        Type   Sign Extended?   32-bit
addi s3,s4,28
sll t1,t2,t3
srli s3,s1,14
sw s9,16(t4)
add s7,s8,s9
srai t0,t1, 0xC
ori s3,s1, 0xABC
lw s4,0x5C(t3)
Instrucción       Imm (bits)        Type   Sign Extended?   32-bit
addi s3,s4,28      Sı́, 12 bits      I      No               0x0000001C
sll t1,t2,t3       No                R      No               -
srli s3,s1,14      Sı́, 12 bits      I      No               0x0000000E
sw s9,16(t4)       Sı́, 7 + 5 bits   S      No               0x0000001C
add s7,s8,s9       No                R      No               -
srai t0,t1, 0xC    Sı́, 12 bits      I      No               0x0000000C
ori s3,s1, 0xABC   Sı́, 12 bits      I      No               0x00000ABC
lw s4,0x5C(t3)     Sı́, 12 bits      I      Si               0x0000005C
