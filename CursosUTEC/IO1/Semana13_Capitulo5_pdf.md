---
curso: IO1
titulo: Semana13-Capitulo5
slides: 85
fuente: Semana13-Capitulo5.pdf
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



          Identificar todas las restricciones
            que configuren la envolvente
            convexa de P es un problema
         generalmente mucho más difícil que
                 el mismo problema P
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


             Ramificación de X sobre x2
          max        x1 + 2x2                         Dos nuevos subproblemas:
           s.t.    4x1 + 6x2  9                                    ⇤
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




            Ramificación de Y1 sobre x1
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

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
