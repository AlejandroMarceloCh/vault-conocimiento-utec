---
curso: SISCOMP
titulo: 09 - Semana 7/Cache Memory
slides: 7
fuente: 09 - Semana 7/Cache Memory.pdf
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
    • Número de bits de tags.    -




    • El offset (hex), el ı́ndice (decimal) y el valor del tag (hex) para la dirección indicada.
Complete la siguiente tabla:
      Levels      Sets         Offbits         Indbits       Tagbits      OffVal    IndVal         TagVal
                                                                                                   OX9IAZ
                   a
      L1                                                       19          &X38            89
      L2                                                       17         0X38       ¢x59         &X 2168
      L3                                                       13         0x3844410x 246
  Se miden los siguientes miss rate, de manera local:
    • L1 local miss rate: 4% >- 0     .
                                       04
    • L2 local miss rate: 20% -> 0      2 .




    • L3 local miss rate: 50% > - 0 5     .




Question 2. Calcule:
   • El miss rate global.
   • El AMAT.
 Complete la siguiente tabla:
      Metric                              Cálculo                          Respuesta
      Global miss rate                        mr. x mr x       Mr3               40%            00 4.




      AMAT (ciclos)
                                                                                       I




                                                                                                 ciclos
                                                         ↓                             . 2
                                                                                       2

Question 3. Se tienen los siguientes códigos:        t , + mr. 1      -    >
  1          # Code 1
  2          li x1 , 5
  3      li x2 , 0
  4 LOOP :   beq x1 , x0 , DONE                3     accesos
  5
  6
         lw x2 , 4( x1 )
         lw x3 , 12( x1 )
                                                                    por
  7      lw x4 , 8( x1 )                             iteración
  8      addi x1 , x1 , -1
  9      j   LOOP
 10 DONE :

                                                         1
                                                                           2


1            # Code 2
2            li x1 , 5
3            li x2 , 0 >-                2 accesos
4
5
    LOOP :   beq x1 , x0 , DONE
             lw    x3 , 4( x2 )             por   iteración
6            lw    x4 , 36( x2 )
7            addi x1 , x1 , -1
8            j         LOOP
9   DONE :

Complete la siguiente tabla:
    Block Size                     MR1                        MR2
    64 B                                 /15                        1/18
    32 B                                 1/15                   21
                                                                     100
                                                                     .


    16 B                                 2/15
    8B
    4B
IS-UTEC
                                         475                        2
    S                         famaño de bloque                               64

    Para          L1 :


·        32kB                =       32x1024           =       32768 bytes

·
      Associativity :                         4       byth por set
·        No       .

                       bloque            :   64 x4             =   256



                                         3276-bytes
·        No   .       sets       :
                                         -




·     Index                   i      =
                                         log(120)                    i    =   7

·    offset : 6 bits                                  -    DAt


                              32-7-6                           32-13          19     bits
      Tag
                                                                          =
·                        :                                =




                              TAG                      INDEX                  Offer

                                             14
                                                  65
     31
          -

                             19 bits                   7 bits                     6 bits

    Para la dirección 0x12345678
                                                      &↳
                                                                         108111
          Dal
    ox
           T g                       1            A       2
                                                           d

                                                                    0x59
                                                                         S
                                                                                    ①X 38
                                                                                           ↓


                                                                    index              Offset


                      & x09 1A2                                    0x59             ① x38

    31                                                14 13         89        65               ①
    Para 12           famaño de bloque                           64
    -




·    Size        256kB            =        256 x 1024        =
                                                                 262144           bytes
·

     Associativity          8         bytspor set ->              64x8    =       512

·   Uro desets
        .
                       =     262144               =
                                                        512 sets
                             -




                                  512
                  i                                          9 bits
·
     Index             =
                            log2 (512)                 =




·    offset        6       bits       (DATO)
                   32-9-6                              17    bits
     tag     :
·                                             =




                      TAG                     INDEX                 Offer

                                           65
      31                              15                                           ①
                                                                  -
        -

                 17 bits                      9       bits               6 bits

    Para    la dirección              QX12345678

                                                                  -
                  0001001080110100910101100111 1000
                                                                 index        Offset
                                  Tag
                            0x2468                               0x159        ①X38

                                                                    ↓
                                                                  345
 Pan
     miss rate global


 ①
                               &
                U

                12                         Mr xmrc X Mr
 ⑥      &
                                            ↓              ↓         ↓
       &
                13
20                                         0 04        0 2     .     0 S .
                                            .




zo    I    main menory



                                           0 04x0 2x0 5                                  0 4
     Global miss          rate     =        .              .
                                                                     .
                                                                                 =        .




        40 % de las referencias del                    CPU se            encuentram
 Ed                            -




                                                       decir                     se      encuentrar
           memoria                                                  , no
 en la
                               principal ,        es


                          de    los    viveles de              la   momnia                cacree
                                                                                          .
 en
        ninguno

     AMAT   =       t , + Mr (tz + Mr (tz + Mr (tmm)))


       & tz + Mr      ·
                           tum         =    20 + 0 5x200   .                 =   120

       · +2 + mr (             120)    =
                                            ⑤+ 0 2x120 .                 =       30


       9 ti + mr (30)                  =
                                            0+ 0 04 +30
                                                   .
                                                                     =       2   .
                                                                                     2



  AMAT      =
                     2 2
                      .         ciclos
Ejencicio B
     -




    códiço con             2        access
                                                     por iteración               Co2
    # it raciones : 10                               X2   =   0



     Block size                 :           64
                                                 ↓                  Block size : 32
                                                                         ①
                                                                                                  /16
     ⑪                      X3 , 4(X2)
                   In
                                                                                       "Es
                                                                   4=



F
                               XY , 36(X2)




               &
                    IW                                                 3)


                                                                                       D
     -



     -
                                                                       32
                                                                     -



     53                                                            36-



               ew          X3 ,         4) X2)                         63             3736
it I       :


                                                                  it 1   :              #
⑫ access               :   miss
                                                                             lu X3, 41X2)
                                                 :




                           compulsory




↑
                                                                   *
         ⑪ lw               X4              36(x2) v
                                        ,
                                                                    miss ner            bloque
                   hit
    it z       L
                   hit
                           ②        .


                                                                   *         tw       X4       36 (x2)
                                                                                           ,
    it 3       -
                           ②

                       i⑧
                                                                    miss zdo                   blogue
    ity
    its [
                                                                  it 2 :
               -


                                                                  it 3 :         2
H R  .
           ,
                   =
                           %                                       it 4 :        Z


    MR             =
                           Yo                                     it S :          2



                                                                  HR =           8/10

                                                                  Mr         =
                                                                                 2110
 3 access por iteración
Códia     Con
                                                                     col
# iteraciones            :
                                                X            5
                                                                 &
                                                         =
                                                     ,
  Block size         :     64B
                                          IwX2 , 4(X1) >
                                                       -                     9
 ①
                                          In     X3 , 12 (X1) >              17


       Yers
-

&
                   it                     In     Xy , 8 (X1) >
                                                             -               13
F3                                       addi        XI , X1 , -1
#

                  , 17 , 13 , 8 , 16 , 12 , 7 , 15, 11 , 6 , 14 , 10, , 13 , 9
 63                                                                  5
                  9

un    solo    bloque de 64 agrupa todos las disciones
      MR      =
                   15               HD    =
                                              14/15

 itI
 -




      -
      >   IwX2 4(x1)                           miss           (entral bloque)
                           ,

          en             X3 , 12 (x1)          hit



     Block Size                -
                               >   32B          -
                                                >            MR =     15

     Block size                -    16B         -            MR =    2/15
          ①                         16                   32            48




       =
       er
                                   -




                                   17

          i
           15                      31                    47             63
