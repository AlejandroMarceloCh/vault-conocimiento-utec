---
curso: IO1
titulo: Semana14-Capitulo5
slides: 126
fuente: Semana14-Capitulo5.pdf
---

    X2


        Y1
                                                                 Programación entera
3




2




1



        Y2
                                                  X1
    0         1              2             3


             ©Fabien Cornillier, Investigación de operaciones 1: Modelos determinísticos
Problemas enteros
    clásicos
                Problema de asignación
                (Assignment Problem)


Tenemos n personas para hacer n tareas. Cada persona tiene que
hacer exactamente una tarea. Hay personas más eficientes que
otras para hacer una tarea especı́fica, ası́ tenemos un costo cij si la
persona i es asignada a la tarea j. Hallar la asignación de costo
mı́nimo.
       Problema de asignación
       (Assignment Problem)
       n
       XXn
min              cij xij
       i=1 i=1
       Xn
s.t.         xij = 1        8i 2 {1, . . . , n}
       j=1
       Xn
             xij = 1        8j 2 {1, . . . , n}
       i=1
                                                     2
             xij 2 {0, 1} 8(i, j) 2 {1, . . . , n}
                  Problema de la mochila
                 (0–1 Knapsack Problem)


Tenemos un presupuesto b para invertir en varios proyectos y se
consideran n proyectos potenciales donde ai es el monto que
inversión para desarrollar el proyecto i, y ci el valor esperado de su
utilidad. Hallar un subconjunto de proyectos en los cuales
invertir sin exceder el presupuesto y maximizando el valor
esperado de la utilidad total.
       i=1
                                                     2
         xij 2 {0, 1}
        Problema       8(i,
                   de la    j) 2 {1, . . . , n}
                         mochila
       (0–1 Knapsack Problem)

         n
         X
max            c i xi
        i=1
        Xn
s.t.           ai xi  b
         i=1
                 xi 2 {0, 1}   8i 2 {1, . . . , n}
Bin-Packing 1D
2D
3D
Set covering
     problem
Set covering
     problem
Set covering
     problem
 Explosión
combinatoria
Explosión combinatoria
                             ¿Cuantas
                             soluciones
                             posibles?

  Problema de asignación
  Problema de la mochila
     Covering Problem
Traveling Salesman Problem
Explosión combinatoria
     Problema de asignación




             ?
     Asignaciones factibles
Explosión combinatoria
     Problema de asignación




             n!
     Asignaciones factibles
Explosión combinatoria
 Problema de la mochila y Covering Problem




                   ?
        Combinaciones factibles
Explosión combinatoria
 Problema de la mochila y Covering Problem




                 2 n
        Combinaciones factibles
Explosión combinatoria
             TSP




            ?
       Ciclos factibles
            ¿Cuantos caminos
                posibles?
1       2




    3

        ¿Cuantos caminos
            posibles?

1   2




3   4
    1       2   1       2




    3       4   3       4




        1           2




3       3           4
            ¿Cuantos caminos
                posibles?

1       2




    5
3       4
1       2   1        2   1       2
                                     1       2


    5           5            5
                                         5
3       4   3        4   3       4
                                     3       4

1       2
            1        2   1       2
                                     1       2


    5
                5            5
3       4                                5
            3        4   3       4
                                     3       4

1       2
            1        2   1       2
                                     1       2


    5
                5            5
3       4                                5
            3        4   3       4
                                     3       4




                12
                ¿Cuantos caminos
                    posibles?

1           2

    6


        5

3           4

    60
                                  ¿Cuantos caminos
                                      posibles?
            7                10

                     8
1                2

    6                    9

            12               11
        5

3                4




    19,958,400
                20 puntos




6,082,255,020,4416,000
               ¿Con 100 puntos?

46663107721972076340849619428133350245357984132190
81073429648194760879999661495780447073198807825914
31268489604136118791255926054584320000000000000000
000000 soluciones …
Explosión combinatoria
             TSP




   (n–1)! / 2
       Ciclos factibles
Exactamente…
                               ¿Con 1000 puntos?
2011936300385468867718512169615019928596874321053573162718999552149692561993145102960221042434847024002399
9430509859802931583343649740427945066191483497229549871225204353687995941181386359436625988975297549763806
0437487731248521800709139047323248145528196943718943243668559590522912891823924988506238316444917977867716
2565926619792315377787045571312087371746737767143232883058338986983344101456036895719268597941249040634339
1918727986587306804268976726211079329660096404543914865421569642220164061577930551848840067865210808437380
4837935674156012739294660383584566224213118065706254390104000130841575513670913988852392317934085082182512
0768456991406324051065463806224481799643525574824877099546711107834162860404106665930584057768079182734920
2335448780145047526880823792386421094483982312247258038267670409945069272124399247997665955086167777830106
9725199868140375068918807653563880963424517176312600007944267573665805851051984087960755453894009696589057
0972726286119327707305314460939801119194857380442531384314835733373487814556170412196040800768904449469822
5913162183580838108958445488995595187701563731114499400259772220714100609368087299632147829087331415147778
5149512162076590808605232916018393453058630079391760375758142112770132585241652113071987143466530845448984
2412950627291635841132290332633849793263411364035378906959290894448261040821741724129966330216838300884998
0641593039419307513973297756557827601804699409030606927930015071784726361210317231589873029734128655189504
2012216219232828622507201410942626235467595310464511568246636748782756979360279827114374887005706673481357
7114229311886937691152419328444882309636919074500703836552233201299497451111108829521699509430092832632425
3089985117809694850893002040594486495915551058561492295082096053444219356092782306248039936145425964840968
6194321307419828691145561562512093324676571985068714265963324937668609470347140717059260079007061672414007
5256998471450767415388222845495365762166391441349323013949321605695417531085475012986949317771385983714111
2437879338287617211010378681528474941254398446408137692443169845497991314047806072549743585062225823063018
9514654560444543471014255320091077199728578402970936374499047127371086791200531838702297870892580414615067
6790409200484981862621152804279518503121356217084545020768450529669919178889697054850138767360000000000000
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
000000000000000000000 soluciones …
   Aplicación con
   85,900 puntos




Very-large-scale integration (integración a muy
gran escala): creación de circuitos integrados
con miles de transistores
soluciones …
    Explosión combinatoria

   n     log n     n0.5   n2         2n             n!
   10     3.32    3.16    102    1.02 x 103     3.6 x 106
  100     6.64    10.00   104    1.27 x 1030   9.33 x 10157
  1000    9.97    31.62   106   1.07 x 10301   4.02 x 102567


Un TSP con 101 nodos tiene al rededor de 9.33 x 10157 ciclos
¿Un tema de potencia de computadoras?


   Tomamos un problema de mochila (2n) con 438 objetos y una
  computadora capaz de resolverlo en una hora por fuerza bruta.



 Una computadora 1.000.000 veces más rápida podrá resolver un
               problema con n = ? en una hora
¿Un tema de potencia de computadoras?


   Tomamos un problema de mochila (2n) con 438 objetos y una
  computadora capaz de resolverlo en una hora por fuerza bruta.



 Una computadora 1.000.000 veces más rápida podrá resolver un
              problema con n = 458 en una hora
¿Un tema de potencia de computadoras?
                       Si una computadora puede
                         evaluar mil millones de
                        soluciones por segundo:

 n      n       n2       n3       n5         2n             n!
 10   0.01µs   0.1µs     1µs     0.1ms      1µs          0.0036ms
 20   0.02µs   0.4µs     8µs     3.2ms      1ms           77 años
 50   0.05µs   2.5µs    125µs   312.5ms    13 días    9.64 x 1047 años
 60   0.06µs   3.6µs    216µs   777.6ms   36.5 años   2.64 x 1065 años
¿Un tema de potencia de computadoras?
      Problema con n        Si podemos evaluar un
     variables binarias     millón de millones de
                            soluciones por segundo y
   Si podemos evaluar mil   eliminar inmediatamente
   millones de soluciones   99.9999999% de las
   por segundo              soluciones no óptimas
      n         Tiempo          n         Tiempo
      30      1 segundo        70       1 segundo
      40      18 minutos       80       20 minutos
      50        13 días        90         14 días
      60        36 años        100        40 años
      70      37436 años       110      41161 años
¿Un tema de potencia de computadoras?
                                    Si podemos evaluar un
                                    millón de millones de
        ¿Cómo resolver              soluciones por segundo y
      problemas enteros             eliminar inmediatamente
           grandes?                 99.9999999% de las
                                    soluciones no óptimas
  Tenemos que eliminar mucho            n         Tiempo
             más que                   70       1 segundo
  99.99999999999999999999%             80       20 minutos
 de las soluciones sin evaluarlas      90         14 días
                                       100        40 años
                                       110      41161 años
                                 ip…
                                        mip…
                                          bip…




¿Cómo resolver los programas lineales enteros, mixtos y binarios?
        8                   9
        <X                  =
   Ejemplo
 mı́n
 S✓N :
           de;programa entero
               cj : S 2 F
         j2S


max     x1 + 0.64x2
s.t.    50x1 + 31x2  250
          3x1      2x2      4
                             2
                x 1 , x2 2 Z +


               1

           <X                  =
    mı́n          cj : S 2 F
   S✓N :                       ;
  Redondeo de solución continua
            j2S


                                                solución LP
  max      x1 + 0.64x2
  s.t.
  Solución50x    +  31x
           LP: (1.9637,
               1         2  250
                        4.9223)

            3x1 ¿(2,2x
Redondeo: ¿cuál?                 4
                     5)?2 ¿(2, 4)?
                               2
                   x1 ,0)x2 2 Z+
  Solución entera: (5,
                                     solución
    … y es aún peor para             entera
    los problemas binarios
                  1
Programación lineal y programación lineal entera


                       Conclusión

         La idea básica que consiste en aplicar el
         simplex y redondear la solución óptima
         generalmente no funciona.
Programación lineal y programación lineal entera


                       Sin embargo…

        El simplex (u otro método como puntos
        interiores) es indispensable para los
        programas lineales enteros, mixtos o binarios.
Relajación lineal
   (LP Relaxation)
   s.t.       Ax  b
               Relajación
                     n    lineal (o continua)
               x 2 Z+
                      (LP Relaxation)

          (P)
          T        T         La relajación lineal RP de P se obtiene
max       c x+h y
                             por la supresión de las restricciones
                                 de integralidad (relajación LP)
s.t.      Ax + Gy  b
                       n
                  x 2 Z+
                       p
                  y 2 R+
                                                              n
   s.t.       Ax  b                                     x 2 Z+
               Relajación lineal (o continua)                 p
               x 2 Z+n                                   y 2 R+
                      (LP Relaxation)

          (P)                              (RP)
                                             T           T
max       T
          c x+h y  T              max      c x+h y

s.t.      Ax + Gy  b             s.t.     Ax + Gy  b
                                                              n
                       n
                  x 2 Z+                                 x 2 R+
                                                              p
                       p
                  y 2 R+                                 y 2 R+
  problema entero original               relajación LP
        8                   9
        <X                  =
   Ejemplo
 mı́n
 S✓N :
           de;programa entero
               cj : S 2 F
         j2S
                                                Solución de
          (P)                                  la relajación
max     x1 + 0.64x2                              lineal (Rp)
s.t.    50x1 + 31x2  250
          3x1      2x2      4
                             2
                x 1 , x2 2 Z +   solución de
                                     (P)


               1
            Relajación lineal (o continua)
                   (LP Relaxation)




Si F (P) es el espacio de soluciones factibles de P, entonces:
F (P) ✓ F (RP ).
Limite superior de un problema P de maximización


     ⇤   ⇤
Si (x , y ) es una solución óptima de P y (x, y ) es una solución
óptima de RP , entonces:
                     T       T       T ⇤     T ⇤
                    c x +h y       c x +h y .

El valor óptimo de RP es un limite superior de P.
Limite superior de un problema P de maximización
  Un mismo problema se puede
formular de varias formas distintas


    Una formulación puede ser
         mejor que otra
3




2




1




    0   1   2   3   4
            Envolvente convexa de P

3                               F (RP3 ) ✓ F (RP1 ) y F (RP3 ) ✓ F (RP2 )


2
                                        F (RP3 ) ✓ F (RP1 ) y F (RP3 ) ✓ F (RP2 )
                          La formulación P3 es mejor que las formulaciones P1 y P2 .
1


                                  P3 es la envolvente convexa de P

    0   1     2   3   4
            Envolvente convexa de P

3
                           La envolvente convexa P3 es la
                               formulación ideal de P

2                         Un punto extremo (y entero) de P3
                              es solución óptima de P
1
                          Si resolvemos la relajación lineal
                           de P3 obtenemos una solución
                                 óptima entera de P
    0   1     2   3   4
            Envolvente convexa de P

3



                            ¿Podríamos determinar la envolvente
2
                           convexa de P y resolver su relajación
                          lineal para tener la solución optima del
1                                    problema entero?



    0   1     2   3   4
¿Porqué no determinar la envolvente convexa de P
         y resolver su relajación lineal?



           Identi car todas las restricciones
             que con guren la envolvente
             convexa de P es un problema
          generalmente mucho más difícil que
                 el mismo problema P



     fi
fi
Algoritmo de Branch & Bound
         Divide y vencerás
                     Idea general
                   ⇤
Queremos resolver z = max{cx|x 2 X }.
                   {X         } ⇤ X     X
         Queremos resolver z = max{cx|x 2 X }.
Particionamos
          ⇤
              X en
                  ⇤
                      1
                       ⇤
                        , X 2
Entonces z = max{z1 , z2 }.
       Particionamos
      Queremos             ⇤
                          z {X
                       X en
                 resolver    = 1 ,X X   }
                                 max{cx|x 2 X }.
                                    1 2
                   ⇤           ⇤    ⇤
                        en {X11, zX22}.
       Entonces z =Xmax{z
      Particionamos                   }
                                      X2
                 ⇤           ⇤
      Entonces z = max{z1 , z2 }. ⇤
                         Idea general
                   ⇤
Queremos resolver z = max{cx|x 2 X }.
Particionamos X en {X1 , X2 }           X
           ⇤             ⇤
Entonces z = max{z1 , z2 }. ⇤

    ⇤    ⇤
Si z1 > z2 es inútil explorar X2 .     X1
No hay solución óptima en X2 .                 ⇤    ⇤
                                             Si z1 > z2 es in
                                             No hay solución
                         Idea general
                   ⇤
Queremos resolver z = max{cx|x 2 X }.
Particionamos X en {X1 , X2 }                    X
           ⇤             ⇤
Entonces z = max{z1 , z2 }. ⇤

    ⇤    ⇤
Si z1 > z2 es inútil explorar X2 .              X1
No hay solución óptima en X2 .                                ⇤    ⇤
                                                            Si z1 > z2 es in
                                                      ⇤
¿Cómo saber que es inútil explorar X2 sin calcular z2 ?   No hay solución
                                               ⇤
Podemos determinar una lı́mite superior de z2 . ¿Cómo?

                         Idea general
                   ⇤
Queremos resolver z = max{cx|x 2 X }.
Particionamos X en {X1 , X2 }                    X
           ⇤             ⇤
Entonces z = max{z1 , z2 }. ⇤

    ⇤    ⇤
Si z1 > z2 es inútil explorar X2 .              X1
No hay solución óptima en X2 .                                ⇤    ⇤
                                                            Si z1 > z2 es in
                                                      ⇤
¿Cómo saber que es inútil explorar X2 sin calcular z2 ?   No hay solución
                                               ⇤
Podemos determinar una lı́mite superior de z2 . ¿Cómo?
                       X2


                   3
función objetivo


                   2




                   1



                            X
                                            X1
                       0        1   2   3
                     X2
ramificación sobre                solución continua
   la variable x2
                3




                2




                1



                          X
                                                X1
                     0        1   2        3
                         X2
    ramificación sobre
       la variable x2
                             Y1
                    3




                    2



  resolución del
problema relajado   1
    sobre Y2

                             Y2
                                              X1
                         0        1   2   3
                        X2

                                         solución continua
                            Y1
                    3




                    2



  resolución del
problema relajado   1
    sobre Y2

                            Y2
                                                     X1
                        0        1   2          3
    X2       ramificación sobre
                la variable x1

        Y1
3




2




1



        Y2
                                      X1
    0         1        2          3
    X2       ramificación sobre
                la variable x1

        Y1
3




2




1



        Y2
                                      X1
    0         1        2          3
                            X2               primera
 ahora tenemos que
                                             solución
  averiguar si una
                                             entera
mejor solución entera           Y1
                        3
   existe sobre Y1


                        2




                        1



                                Y2
                                                   X1
                            0        1   2     3
 ahora tenemos que          X2
                                             solución
  averiguar si una                           continua
mejor solución entera           Y1
                        3
   existe sobre Y1


                        2




                        1



                                Y2
                                                  X1
                            0        1   2    3
    X2               ramificación
                       sobre la
                      variable x1
        Y1
3




2




1



        Y2
                                X1
    0        1   2          3
                                 X2               ramificación
                                                    sobre la
                                                   variable x1
                                     Y1
                             3

                  solución
                  continua
                             2




                             1
 el límite superior
no permite podar
          Y1
                                     Y2
                                                             X1
                                 0        1   2          3
                                 X2


                                     Y1
                             3

                   segunda
               solución entera
                             2




solución sobre Y2 mejor      1
 que solución sobre Y1
   (solo un poquito…)
                                     Y2
                                                      X1
                                 0        1   2   3
                     s.t.   5x1 + 7x2 + 4x3 + 3x4  14
                                        xi 2 {0, 1}   8i = {1, . . . , 4}

  x1 + x2 + x3  2
  x1 + x2 + x4  2
                      Problema original X

                                 max       x1 + 2x2
                                 s.t.    4x1 + 6x2  9
                   (X)
                                            x1 + x2  4
                                                          2
                                            (x1 , x2 ) 2 Z+



dentificar un conjunto C ⇢ 1, . . . , n de elementos tal que:
                                        X
                                            w x > W,
                   xi 2 {0, 1}   8i = {1, . . . , 4}


                                 Inicialización
           max       x1 + 2x2
                                                             Z*=+∞
           s.t.     4x1 + 6x2  9
    (X)                                                Subproblemas activos:
                      x1 + x2  4
                                                               X
                                    2
                      (x1 , x2 ) 2 Z+



o C ⇢ 1, . . . , n de elementos tal que:
                   X
                       wi xi > W,
                  xi 2 {0, 1}   8i = {1, . . . , 4}


      Resolución de la relajación LP de X
          max        x1 + 2x2
                                                             Z*=+∞
           s.t.    4x1 + 6x2  9
    (X)                                                Subproblemas activos:
                      x1 + x2  4
                                                               X
                                    2
                      (x1 , x2 ) 2 Z+


                                   Solución LP: (1.5, 2.5)
o C ⇢ 1, . . . , n de elementos tal que:Z*(LP(X)): 3.5
                   X
                       wi xi > W,
                   xi 2 {0, 1}   8i = {1, . . . , 4}


                 Rami cación de X sobre x2
          max        x1 + 2x2                          Dos nuevos subproblemas:
           s.t.     4x1 + 6x2  9                                   ⇤
                                                             x2  bx2 c = 2   (Y1)
    (X)
                      x1 + x2  4                                   ⇤
                                                             x2 dx2 e = 3     (Y2)
                                    2
                      (x1 , x2 ) 2 Z+


                                   Solución LP: (1.5, 2.5)
o C ⇢ 1, . . . , n de elementos tal que:Z*(LP(X)): 3.5
                   X
                       wi xi > W,
            fi
                    i




      Resolución de la relajación LP de Y1
           max          x1 + 2x2
                                                                Z*=+∞
   (Y1)
           s.t.     4x1 + 6x2  9
                                                          Subproblemas activos:
                         x1 + x2  4
                                                                  X
                              x2  2                              Y1
                                       2
                         (x1 , x2 ) 2 R+                          Y2


                                   Solución LP: (0.75, 2.0)
                                       Z*(LP(Y1)): 3.25
o C ⇢ 1, . . . , n de elementos tal que:
                   X
       Resolución de la relajación LP de Y2
           max       x1 + 2x2
                                                            Z*=+∞
    (Y2)
           s.t.     4x1 + 6x2  9
                                                     Subproblemas activos:
                      x1 + x2  4
                                                             X
                            x2    3                          Y1
                                    2
                      (x1 , x2 ) 2 R+                        Y2


                                 Solución LP: No factible


o C ⇢ 1, . . . , n de elementos tal que:
                   X
                    i




                Rami cación de Y1 sobre x1
           max          x1 + 2x2                     Dos nuevos subproblemas:

   (Y1)
           s.t.     4x1 + 6x2  9                                    ⇤
                                                              x1  bx1 c = 0 (Y1,1)
                         x1 + x2  4                                 ⇤
                                                              x1 dx1 e = 1 (Y1,2)
                              x2  2
                                       2
                         (x1 , x2 ) 2 R+

                                   Solución LP: (0.75, 2.0)
                                       Z*(LP(Y1)): 3.25
o C ⇢ 1, . . . , n de elementos tal que:
           fi
                   X
                      xi 2 {0, 1}     8i = {1, . . . , 4}

2
2       Resolución de la relajación LP de Y1,1
             max          x1 + 2x2
             s.t.         4x1 + 6x2  9                                Z*=+∞
    (Y1,1)                  x1 + x2  4
                                                                 Subproblemas activos:
                                 x2  2
                                                                          X
                                 x1  0
                                          2                              Y1
                            (x1 , x2 ) 2 R+
                                                                         Y2
                                                                         Y1,1
                                              Solución LP: (0, 1.5)      Y1,2
unto C ⇢ 1, . . . , n de elementos tal que: Z*(LP(Y1,1)): 3.0
                      X
                          wi xi > W,
                    i2C

                      xi 2 {0, 1}     8i = {1, . . . , 4}

2
2       Resolución de la relajación LP de Y1,2
             max          x1 + 2x2
             s.t.         4x1 + 6x2  9                                 Z* = 3.0
    (Y1,2)                  x1 + x2  4
                                                                  Subproblemas activos:
                                 x2  2
                                                                           X
                                 x1    1
                                          2
                                                                           Y1
                            (x1 , x2 ) 2 R+
                                                                           Y2
                                                                          Y1,1
                                              Solución LP: (1.0, 2.0)     Y1,2
unto C ⇢ 1, . . . , n de elementos tal que: Z*(LP(Y1,2)): 3.0
                      X
                          wi xi > W,
                    i2C
                      xi 2 {0, 1}     8i = {1, . . . , 4}

2
2                              Eliminación de Y1,1
             max          x1 + 2x2
             s.t.         4x1 + 6x2  9                                 Z* = 3.0
    (Y1,1)                  x1 + x2  4
                                                                   Subproblemas activos:
                                 x2  2            Relajación               X
                                 x1  0          Z*(LP(Y1,1)) no
                                          2                                Y1
                            (x1 , x2 ) 2 R+       mejor que Z*             Y2
                                                                           Y1,1
                                              Solución LP: (0, 1.5)        Y1,2
unto C ⇢ 1, . . . , n de elementos tal que: Z*(LP(Y1,1)): 3.0
                      X
                          wi xi > W,
                    i2C
              Eliminación de Y1
                                         Z* = 3.0
                                    Subproblemas activos:
                                             X
Mejor solución entera de Y1 = 3.0
                                            Y1
                                            Y2
                                            Y1,1
                                            Y1,2
              Eliminación de X
                                        Z* = 3.0
                                   Subproblemas activos:
                                            X
Mejor solución entera de X = 3.0
                                           Y1
                                           Y2
                                           Y1,1
                                           Y1,2
                                                                     xi 2 {0, 1}       8i = {1, . . . , 4}

                           x1 + x2 + x3  2
                           x1 + x2 + x4  2


                                                           max           x1 + 2x2
                                                            s.t.         4x1 + 6x2  9           Solución LP: (1.5, 2.5)
                                                                           x1 + x2  4               Z*(LP(X)): 3.5

                                                                           (x1 , x2 ) 2 Z2+                   Descartado por



                                      ⇤
                                                                                                       X       infactibilidad
                                                                                                                           x2  bx2⇤ c = 2
                                                                                                                           x2 dx2⇤ e = 3
                            x2  bxun
                        Identificar   2 cconjunto
                                           =2     C ⇢ 1, . . . , n de elementos tal que:
                            x2 LP:    ⇤
                                   dx2(0.75,
                                        e = 2.0)
                                               3
                          Solución                                 X                                                         No factible
                              Z*(LP(Y1)): 3.25                         wi xi > W,
Descartado por
                                                                   i2C
límite superior
  (bounding)
                   X    para obtener las restricción:             X
                                                                          |C|    1.
                                                    x1  bx1⇤ ci2C
                                                                =0
           ⇤
 x1  bx1 c = 0                                     x1 dx1⇤ e = 1
 x1     dx ⇤e = 1
 Solución LP:
           1 (0, 1.5)                              Solución LP: (1.0, 2.0)
   Z*(LP(Y1,1)): 3.0                                  Z*(LP(Y1,2)): 3.0
         Enumeración implicita
               ⇤
Para resolver z = max{cx|x 2 X }
    Particionamos el espacio factible X en {Y1 , . . . , Yn }
    Para cada parte Yi de la partición de X , calculamos un lı́mite
              ⇤                           ⇤
    superior zLP (Yi ) del valor óptimo z (Yi ).
        ⇤
    Si zLP (Yi ) es menor que la mejor solución ya encontrada,
    podamos Yi .
    Sino, particionamos recursivamente Yi .
                    Algoritmo

A cada paso del algoritmo, tenemos que mantener:
    una lista de subproblemas activos (no resueltos o no
    eliminados)
              ⇤
    el valor Z de la mejor solución encontrada
                         ⇤
    el valor inicial de Z es        T
                               1 o c x para un valor x factible
    conocido
                                   Algoritmo
                           1   Si existe un subproblema activo en la lista, elegir un
                               subproblema Yi de la lista. Sino terminar.
                           2   Resolver la relajación lineal de Yi : obtenemos la solución
                               relajada LP(Yi ). Si la relajación lineal de Yi no es factible,
hubiera sido eliminado
                               eliminar Yi y volver al paso 1.
antes si fuera una
                               Si ZLP(Yi )      ⇤
                                              Z , eliminar Y
solución entera no mejor   3
                                                                i y volver al paso 1.
                           4                                                           ⇤
                               Si LP(Yi ) es una solución entera mejor mejor que Z (es decir
                                            ⇤               ⇤
                               ZLP(Yi ) > Z ), actualizar Z con el nuevo valor óptimo
                               ZLP(Yi ) (es decir Z ⇤   ZLP(Yi ) ) y volver al paso 1.
                           5   Si ZLP(Yi ) no es una solución entera, resolver Yi directamente,
                               o crear nuevos subproblemas (particionar Yi ) y agregarlos a la
                               lista de subproblemas activos y volver al paso 1.
Estrategias de recorrido
      Ejemplo simpli cado




fi
                                                                                                             A
                                                                                                                    60.75
                                                                                                                  Solución
    Breadth-First                                                                                                fraccional




                                                             B                                                                                      C
                                                                    60.0                                                                                     57.3
                                                                  Solución                                                                                 Solución
                                                                 fraccional                                                                               fraccional




                               D                                                          E         57
                                                                                                                                       F        55.7
                                                                                                                                                                       G     55.5
                                      55.5
                                    Solución                                                     Solución                                     Solución                     Solución
                                   fraccional                                                   fraccional                                   fraccional                     entera




           H                                         I                        J                         K                     L                      M
                   55.5                                     55.2                                               55.8                 55.2
                 Solución                                 Solución                No factible                Solución             Solución                No factible
                fraccional                               fraccional                                           entera               entera



N                     O                     P                    Q
       55.2                    54.9                54.9                 54.9
     Solución                Solución            Solución             Solución
      entera                  entera            fraccional             entera
                                                                                                                 A                 1
                                                                                                                         60.75
                                                                                                                       Solución
    Breadth-First                                                                                                     fraccional




                                                             B                    2                                                                          C                      3
                                                                    60.0                                                                                              57.3
                                                                  Solución                                                                                          Solución
                                                                 fraccional                                                                                        fraccional




                               D                4                                             E         57
                                                                                                                  5                             F        55.7
                                                                                                                                                                     6          G         55.5
                                                                                                                                                                                                   7
                                      55.5
                                    Solución                                                         Solución                                          Solución                         Solución
                                   fraccional                                                       fraccional                                        fraccional                         entera




           H                                         I                        J                      8      K                 9        L                      M
                   55.5                                     55.2                                                   55.8                      55.2
                 Solución                                 Solución                    No factible                Solución                  Solución                No factible
                fraccional                               fraccional                                               entera                    entera



N                     O                     P                    Q
       55.2                    54.9                54.9                 54.9
     Solución                Solución            Solución             Solución
      entera                  entera            fraccional             entera
                                                                                                            A
                                                                                                                   60.75
                                                                                                                 Solución
     Best-First                                                                                                 fraccional




                                                            B                                                                                      C
                                                                   60.0                                                                                     57.3
                                                                 Solución                                                                                 Solución
                                                                fraccional                                                                               fraccional




                              D                                                          E         57
                                                                                                                                      F        55.7
                                                                                                                                                                      G     55.5
                                     55.5
                                   Solución                                                     Solución                                     Solución                     Solución
                                  fraccional                                                   fraccional                                   fraccional                     entera




          H                                         I                        J                         K                     L                      M
                  55.5                                     55.2                                               55.8                 55.2
                Solución                                 Solución                No factible                Solución             Solución                No factible
               fraccional                               fraccional                                           entera               entera



N                    O                     P                    Q
      55.2                    54.9                54.9                 54.9
    Solución                Solución            Solución             Solución
     entera                  entera            fraccional             entera
                                                                                                                A                 1
                                                                                                                        60.75
                                                                                                                      Solución
     Best-First                                                                                                      fraccional




                                                            B                    2                                                                          C                      3
                                                                   60.0                                                                                              57.3
                                                                 Solución                                                                                          Solución
                                                                fraccional                                                                                        fraccional




                              D                4                                             E         57
                                                                                                                 5                             F        55.7
                                                                                                                                                                    6          G         55.5
                                                                                                                                                                                                  7
                                     55.5
                                   Solución                                                         Solución                                          Solución                         Solución
                                  fraccional                                                       fraccional                                        fraccional                         entera




          H                                         I                        J                      8      K                 9        L                      M
                  55.5                                     55.2                                                   55.8                      55.2
                Solución                                 Solución                    No factible                Solución                  Solución                No factible
               fraccional                               fraccional                                               entera                    entera



N                    O                     P                    Q
      55.2                    54.9                54.9                 54.9
    Solución                Solución            Solución             Solución
     entera                  entera            fraccional             entera
                                                                                                            A
                                                                                                                   60.75
                                                                                                                 Solución
    Depth-First                                                                                                 fraccional




                                                            B                                                                                      C
                                                                   60.0                                                                                     57.3
                                                                 Solución                                                                                 Solución
                                                                fraccional                                                                               fraccional




                              D                                                          E         57
                                                                                                                                      F        55.7
                                                                                                                                                                      G     55.5
                                     55.5
                                   Solución                                                     Solución                                     Solución                     Solución
                                  fraccional                                                   fraccional                                   fraccional                     entera




          H                                         I                        J                         K                     L                      M
                  55.5                                     55.2                                               55.8                 55.2
                Solución                                 Solución                No factible                Solución             Solución                No factible
               fraccional                               fraccional                                           entera               entera



N                    O                     P                    Q
      55.2                    54.9                54.9                 54.9
    Solución                Solución            Solución             Solución
     entera                  entera            fraccional             entera
                                                                                                                A                 1
                                                                                                                        60.75
                                                                                                                      Solución
    Depth-First                                                                                                      fraccional




                                                            B                    2                                                                          C                      11
                                                                   60.0                                                                                              57.3
                                                                 Solución                                                                                          Solución
                                                                fraccional                                                                                        fraccional




                              D                3                                             E         57
                                                                                                                 8                             F        55.7
                                                                                                                                                                    12         G      55.5
                                                                                                                                                                                               13
                                     55.5
                                   Solución                                                         Solución                                          Solución                      Solución
                                  fraccional                                                       fraccional                                        fraccional                      entera




          H                  4                      I                7       J                      9      K                 10       L                      M
                  55.5                                     55.2                                                   55.8                      55.2
                Solución                                 Solución                    No factible                Solución                  Solución                No factible
               fraccional                               fraccional                                               entera                    entera



N               5    O                 6   P                    Q
      55.2                    54.9                54.9                 54.9
    Solución                Solución            Solución             Solución
     entera                  entera            fraccional             entera
        Otra idea:
algoritmo de plano de corte
     Acercándonos a la envolvente convexa
              Restricción válida
                             T
Se dice de una restricción ⇡ x  ⇡0 que es válida para el
programa P cuando está satisfecha por cualquier solución del
espacio factible de P:

                                       h                         i
          T                                0            T 0
  C = {⇡ x  ⇡0 } válida para P , x 2 F (P) ) ⇡ x  ⇡0
                Plano de corte

     0
Sea P el problema P al cual se agrega una restricción C válida
para P. La restricción C es un plano de corte para P si
F (RP 0 ) ⇢ F (RP ).
                   Corte válido

                        T
Un plano de corte C = {⇡ x  ⇡0 } es un corte válido para x 2 Rp
    T
si ⇡ x > ⇡0 .
Algoritmo del plano de corte

       Ejemplo:
Problema de la mochila
    Problema de la mochila
       max    8x1 + 11x2 + 6x3 + 4x4
       s.t.   5x1 + 7x2 + 4x3 + 3x4  14
                                         max     8x1 + 11x2 + 6x3 + 4
                           xi 2 {0, 1}   8i = {1, . . . , 4}
                                         s.t.    5x1 + 7x2 + 4x3 + 3x
Averiguar que las restricciones siguientes son planos de corte:xi 2 {0, 1

                    x1 + x2 + x3  2
                    x1 + x2 + x4  2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Problema de la mochila


<latexit sha1_base64="v89D5JD+kxiQw5a6eEeLiONMLZw=">AAAD0HichVJLbxMxEJ5kgYbwSsqRi0WKxKGKkl6oUA8VyYFjeKSt1ESV1+tt3Pqx2F7UaLVCXPlR/A+u3DnxB5h1VqJpirA0M5+/+WY8GjnOpHB+MPjRaEZ37t7bat1vP3j46PGTTnf7yJncMj5lRhp7ElPHpdB86oWX/CSznKpY8uP4clTljz9z64TRH/0y43NFz7VIBaMeKdP5DjPQYECgT4Cj98h4RFfoY0ihgDHe0qAQwNB+I3oNJRD4gBmKMUemigw7xchZrM3RV9wOjND6QS3QZ8jaWp1jlPAJowhVBL1EU/UkJtRf4ETV6yR0WmlWb2nM5deUI1Q6zHvsUFXkeCPIFaFHGap10PKQ+ffcu/95Z2ejx9+tCbTi1l0o+BW2qPBWQv+s0xv0B+GQTTCsQQ/qMznrNg5miWG54tozSZ07He5nfl5Q6wWTvGzPcsczyi7pOT91C2P9rjbMKEXnhcm8SHi6rkGoqeJuXoSvVJIXyCQkNRZNexLY6xUFVc4tVYxKRf3C3cxV5K25ivHGSIcDjDkOb/mECsuTMf5dJTy3xYxxIctiJutoQ1yf16f780LoLPdcs9W4aS6JN6T63STBjszLJQLKrMCtELagljLs79q47+HN7W6Co73+EPG7vd7hm3rzLXgGz+ElDOEVHMJbmMAUWONns9XsNrej99FV9CX6upI2G3XNU1g70bc/fNf7Tw==</latexit>




<latexit sha1_base64="TYCUYmIc/tJESXhf5nzg12/vAtQ=">AAADTnicbVJNbxMxEJ3d8hHCR1M4crEISBxKlPRChThUpAeOQZC2UjcKXq+3sepdL7a3arTNlSv8NK4c+QGckLgheLsJEmmxNDPPb55nZ8eOC62c7/e/BuHGtes3brZutW/fuXtvs7N1/8CZ0go5FkYbexRzJ7XK5dgrr+VRYSXPYi0P49NhnT88k9Ypk7/z80JOMn6Sq1QJ7kGZzoIiysmQgk9IwnswHugcPqaUKhqRhaKAOegE7Ad0L2hBjN5CyREf0xDGqESm3guoY+QsqpTwNZfRd2QVIqdt7HXDWqgcVLap/bd6XTECX0I9RQ8KO9XwQ3z3HJwCjlBD0gegC/AX9IwGTRd1xWUvy05s80eMzugbTij8qaHetNPt9/rNYlfBYAW6tFqj6VbwMkqMKDOZe6G5c8eD3cJPKm69Elou2lHpZMHFKT+Rx25mrN/OjTBZxieVKbxKZLquAcx5Jt2kai5ywZ6ASVhqLCz3rGH/PVHxzLl5FkOZcT9zl3M1+d9czXhjtEMD+xLNWzniyspkHy8nU17aKhJS6UUV6VW0TVzv16e7k0rlRellLpbtpqVm3rD6bbEEFYXXcwAurMJUmJhxywXquzbmPbg83avgYKc3AH6z0917tZp8ix7SI3qKu31Oe/Qa73FMIngffAw+BZ/DL+HP8Ff4eykNg9WZB7S2Nlp/AJH450w=</latexit>




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              Se tiene que remover cualquier
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              elemento de C para
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              satisfacer la restricción de
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              capacidad
                                                           Ejercicio
actice: Cover Inequalities
 ise 3
      Consideramos el problema
 er the knapsack problem:      de mochila siguiente:


         X = {x 2 B : 11x1 + 6x2 + 6x3 + 5x4 + 5x5 + 4x6 + x7  19}
                      7


s many cover inequalities for this problem as you can. Are your cover ineq
al? 1. Identi car unas coberturas
    2. Identi
Exercise 3     car coberturas  mínimas
    3. Escribir los cortes válidos correspondientes
       (las restricciones de corte)


         fi
         fi
                                                                Ejercicio
actice: Cover Inequalities
 ise 3
      Consideramos el problema
 er the knapsack problem:      de mochila siguiente:


         X = {x 2 B : 11x1 + 6x2 + 6x3 + 5x4 + 5x5 + 4x6 + x7  19}
                      7

                          Solution 3
s many cover inequalities    for this problem   as  you can.
                        Some cover inequalities for X are:   Are your cover ineq
al? 1. Identi car unas coberturas
    2. Identi  car coberturas  mínimas                     x1 + x2 + x3  2
Exercise 3
    3. Escribir los cortes válidos correspondientes        x1 + x2 + x6  2
       (las restricciones de corte)
                                                           x1 + x5 + x6  2
                                                       x3 + x4 + x5 + x6  3
         fi
         fi
                      Estrategia

1   Resolver RP y obtener la solución continua x
2   Si x 2 Z , el tenemos la solución óptima del programa entero.
            n

    Se termina el algoritmo.
3   Determinar un corte válido C para x y P.
4   Agregar la restricción C al programa P y volver al paso 1.

          problema de separación:
           paso más importante
Algoritmo de plano de corte cuando un problema
   se formula con un número exponencial de
                 restricciones
Ejemplo: TSP
Formular una restricción de grado por cada nod
    Problema del viajante de comercio
                    !
   (Traveling Salesman Problem  – TSP)
                         xij = 2, ∀i ∈ V.
       Grafo       ij∈δ(i)

                                    Objetivo:
                                   x12 + x13 + x14 + x15 =
   1           3                   Hallar el ciclo
                                   x    +  x     +
                             hamiltoniano más corto…
                                     12      23     x 24 + x 25 =
                                   x 13 +  x 23  +  x
                              …el tour (o un tour) de 34 + x 35 =
                   5
                              menos     + xque
                                   x14costo  24  +  x34 + x45 =
                                                  pasa
                                  por cada nodo
   2           4                   x15 + x25
                               exactamente    una+vez
                                                    x35 + x45 =
1          3
                   Para   determinar
                       x12 = x            las
                               13 = x24 = x 35 = x45 = 1
               5
                   aristas  que
                       x14 = x     utilizar
                               15 = x        en= x34 = 0
                                      23 = x25

2          4
                   el tour, de nimos las

    x1,2 = 1       variables binarias xij
    x1,3 = 1
    x1,4 = 0       xij = 1 si se utiliza la arista (i,j)
    x1,5 = 0       xij = 0 sino
    x2,3 = …                           Casa Abierta Facultad de Ciencias, Junio 2011 – p.18




      fi
                          Costo de cada arista
            Modelo de optimización:

Minimizar el costo                   !
total de las aristas           min          cij xij
seleccionadas                        ij∈E
                              s.r.
                               !
                                      xij = 2, ∀i ∈ V,
    1        3          ¿Esa solución
                              ij∈δ(i)
                                          es
                        factible?
                   5         xij ∈ {0, 1}, ∀ij ∈ E.
    2        4          ¿Porqué?
            Funciona?
            En nuestro ejemplo sí, en general NO.
                          Costo de cada arista
            Modelo de optimización:

Minimizar el costo                  !
total de las aristas          min          cij xij
seleccionadas                       ij∈E
                              s.r.
                               !
 De tal manera que cada                 xij = 2,       ∀i ∈ V,
 nodo tenga 2 aristas         ij∈δ(i)

 adyacentes                   xij ∈ {0, 1},          ∀ij ∈ E.

            Funciona?
            En nuestro ejemplo sí, en general NO.
                   !
         Modelo de     xij = 2, ∀i ∈ V.
                   optimización:
                   ij∈δ(i)
Nodo 1
                                 !
                              x12 + xc13ij x
                             min           +ijx14 + x15 = 2
   1         3                   ij   E
                               x12 + x23 + x24 + x25 = 2
                                    ∈
                             s.r.x13 + x23 + x34 + x35 = 2
                   5          !
                               x14 +x x24=+2,x34 +∀ix45 =
                                                      ∈ V,2
                                       ij
   2         4                  x 15
                             ij∈δ(i)
                                     + x 25 + x 35 + x 45 = 2

                             xij ∈ {0, 1},     ∀ij ∈ E.
           Nodo 4                                 Casa Abierta Facultad de Ciencias, Junio 2

         Funciona?
         En nuestro ejemplo sí, en general NO.
         En un circuito cada nodo es de grado
             2 (cada nodo tiene 2 aristas
                       incidentes)


Si cada nodo es de grado 2, tenemos un circuito ???
bciclos
   Cada nodo tiene 2 aristas
    incidentes,
ueden  aparecerpero…
                soluciones que contengan subciclos


                        2            4

     No es una     1                     6
     solución
     factible           3            5

                         Subciclos
bciclos Eliminar las soluciones con subciclos:
            añadir   nuevas  restricciones
ueden aparecer soluciones que contengan subciclos


                        2        4

                  1                    6

                        3        5
Eliminar los subciclos es              Ejemplo, para el
                                      subconjunto {1,2,3}
impedir cualquier ciclo
      Subciclos
para cada subconjunto
                                     rechazamos cada
                                  solución que contiene 3 o
de puntosPueden                         más aristas
           del grafoaparecer soluciones que contengan sub

 x1,2 + x1,3 + x2,3 = 3
                                     2             4

añadir la restricción         1                               6

 x1,2 + x1,3 + x2,3 < 3              3             5
Eliminar los subciclos es             Ejemplo, para el
                                     subconjunto {4,5,6}
impedir cualquier ciclo
      Subciclos
para cada subconjunto
                                     rechazamos cada
                                  solución que contiene 3 o
de puntosPueden                   más aristas adyacentes
           del grafoaparecer soluciones que contengan sub

 x4,5 + x4,6 + x5,6 = 3
                                     2             4

añadir la restricción         1                               6

 x4,5 + x4,6 + x5,6 < 3              3             5
                           Segundo intento:
                                      Costo        de    cada    arista
                           Añadir una restricción por cada S ⊂ V para eliminar
                           subciclos:
                                                !
 Minimizar el costo total de               min       cij xij
 las aristas seleccionadas                      ij∈E
                                           s.r.
                                            !
De tal manera que cada nodo tenga                  xij = 2, ∀i ∈ V,
2 aristas adyacentes                       ij∈δ(i)
                                             !
                                                   xij ≤ |S| − 1, ∀S ⊂ V,
      Subciclos Restricciones de
                                                           ij∈E(S)

       Puedeneliminación          de
             aparecer soluciones que    subciclos
                                     contengan subciclos   xij ∈ {0, 1},   ∀ij ∈ E.
                               2       4

                          1                 6
                                                                                      Casa Abierta Facultad de Ciencias, Ju

                               3       5
    s.t.             ai xi  b
              i=1
 Problema del   viajante
             xi 2         de
                  {0, 1} 8i   comercio
                            2 {1, . . . , n}
(Traveling Salesman Problem – TSP)
           n
           XXn
 min                   cij xij
           i=1 j=1
           X
  s.t.              xij = 1        8i = {1, . . . , n}
           j:j6=i
           X
                    xij = 1        8j = {1, . . . , n}
           i:i6=j
                                                            2
                    xij 2 {0, 1} 8(i, j) 2 {1, . . . , n}

    Segundo intento:
                       ¿Cuantas
    Añadir una restricción           variables?
                             por cada S   ⊂ V para eliminar
    subciclos:
                         !
                    min       cij xij ¿Cuantas
                         ij∈E        restricciones
                    s.r.               de grado?
                     !
                            xij = 2, ∀i ∈ V,
                     ij∈δ(i)
  ¿Cuantas            !
restricciones                  xij ≤ |S| − 1,     ∀S ⊂ V,
                     ij∈E(S)
de eliminación
de subciclos?       xij ∈ {0, 1},      ∀ij ∈ E.


                                                        Casa Abierta Facultad de Ciencias, Junio 2011 – p.25
ntento:
          ¿Cuantas
a restricción          variables?
              por cada S    ⊂ V para eliminar
 :
           !                                                                                        n(n-1)/2 variables
       min     cij xij
            ij∈E
      s.r.
       !
                 xij = 2,     ∀i ∈ V,
       ij∈δ(i)
        !
                 xij ≤ |S| − 1,        ∀S ⊂ V,
       ij∈E(S)

      xij ∈ {0, 1},         ∀ij ∈ E.


                                             Casa Abierta Facultad de Ciencias, Junio 2011 – p.25
ntento:
a restricción por cada S ⊂ V para eliminar
 :
            !               ¿Cuantas                                                            n(n-1)/2 variables
       min       cij xij restricciones de
            ij∈E
                             grado?
       s.r.
        !                                                                                       n restricciones
               xij = 2, ∀i ∈ V,                                                                    de grado
      ij∈δ(i)
       !
                xij ≤ |S| − 1,     ∀S ⊂ V,
      ij∈E(S)

      xij ∈ {0, 1},     ∀ij ∈ E.


                                         Casa Abierta Facultad de Ciencias, Junio 2011 – p.25
ntento:
a restricción por cada S ⊂ V para eliminar
 :
           !                                                                                       n(n-1)/2 variables
       min     cij xij
           ij∈E
      s.r.
       !                                                                                           n restricciones
                xij = 2,     ∀i ∈ V,                                                                  de grado
      ij∈δ(i)
       !
                xij ≤ |S| − 1,        ∀S ⊂ V,
                                                                                                   2 restricciones
                                                                                                    n-1
      ij∈E(S)

      xij ∈ {0, 1},        ∀ij ∈ E.
                                          ¿Cuantas                                                 de eliminación de
                                        restricciones
                                        de eliminación                                                 subciclos
                                        de subciclos?
                                            Casa Abierta Facultad de Ciencias, Junio 2011 – p.25
ntento:
a restricción por cada S ⊂ V para eliminar                                                             Con n = 100:
 :
           !                                                                                        4950 variables
       min     cij xij
           ij∈E
      s.r.                                                                                         100 restricciones
       !
                xij = 2,     ∀i ∈ V,                                                                   de grado
      ij∈δ(i)

                                                                                                    ~6.338x10
       !
                xij ≤ |S| − 1,        ∀S ⊂ V,                                                                 29
      ij∈E(S)

      xij ∈ {0, 1},        ∀ij ∈ E.
                                                                                                   restricciones de
                                                                                                    eliminación de
                                            Casa Abierta Facultad de Ciencias, Junio 2011 – p.25       subciclos
ntento:
a restricción por cada S ⊂ V para eliminar                                                            Con n = 267:
 :
           !                                                                                         ~1.1857x10 80
       min     cij xij
           ij∈E
                                                                                                   restricciones de
      s.r.                                                                                          eliminación de
       !
                xij = 2,     ∀i ∈ V,                                                                   subciclos
      ij∈δ(i)
       !
                xij ≤ |S| − 1,        ∀S ⊂ V,
                                                                                         Número estimado de
      ij∈E(S)

      xij ∈ {0, 1},        ∀ij ∈ E.                                                      átomos en la parte
                                                                                          visible del universo:
                                            Casa Abierta Facultad de Ciencias, Junio 2011 – p.25
                                                                                                   10 80

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
