---
curso: SISCOMP
titulo: 09 - Semana 7/Labs_IS2021_2025___2-6
slides: 2
fuente: 09 - Semana 7/Labs_IS2021_2025___2-6.pdf
---

ladanaque@utec.edu.pe
IS2021: Computing Systems
October 2, 2025
                                           S7: Cache Memory

  Se tiene un sistema de memoria con 32 bits de bus de dirección y las siguientes caracterı́sticas:
    • tamaño de bloque: 64 bytes
    • L1 de 32KB 4-way set associative, con hit time de 1 ciclo.
    • L2 de 256KB 8-way set associative, con hit time de 6 ciclos.
    • L3 de 8MB 16-way set associative, con hit time de 20 ciclos.
    • Main memory: 200 ciclos.

Question 1. Considerando la siguiente dirección fı́sica: 0x12345678, para cada nivel de caché (L1,L2,L3)
calcule:
    • Número de sets.
    • Número de bits de offset.
    • Número de bits de ı́ndice.
    • Número de bits de tags.
    • El offset (hex), el ı́ndice (decimal) y el valor del tag (hex) para la dirección indicada.
Complete la siguiente tabla:
      Levels      Sets         Offbits       Indbits       Tagbits     OffVal       IndVal        TagVal
      L1
      L2
      L3

  Se miden los siguientes miss rate, de manera local:
    • L1 local miss rate: 4%
    • L2 local miss rate: 20%
    • L3 local miss rate: 50%
Question 2. Calcule:
   • El miss rate global.
   • El AMAT.
 Complete la siguiente tabla:
      Metric                             Cálculo                          Respuesta
      Global miss rate
      AMAT (ciclos)
Question 3. Se tienen los siguientes códigos:

  1          # Code 1
  2          li x1 , 5
  3      li x2 , 0
  4 LOOP :   beq x1 , x0 , DONE
  5      lw x2 , 4( x1 )
  6      lw x3 , 12( x1 )
  7      lw x4 , 8( x1 )
  8      addi x1 , x1 , -1
  9      j   LOOP
 10 DONE :

                                                       1
                                               2


1            # Code 2
2            li x1 , 5
3            li x2 , 0
4   LOOP :   beq x1 , x0 , DONE
5            lw    x3 , 4( x2 )
6            lw    x4 , 36( x2 )
7            addi x1 , x1 , -1
8            j         LOOP
9   DONE :

Complete la siguiente tabla:
    Block Size                     MR1   MR2
    64 B
    32 B
    16 B
    8B
    4B
IS-UTEC
