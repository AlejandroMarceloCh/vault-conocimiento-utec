---
curso: IO2
titulo: EC1 SOLUCIONES
slides: 7
fuente: EC1 SOLUCIONES.pdf
---

21/4/26, 23:03                                                  EC1 SOLUCIONES



     EC1 SOLUCIONES
     AUTHOR
     Fabian Vallebuona


     EC1 2026-1 A
     Como practicante del área de compras en una fábrica de dispositivos médicos de alta tecnología, usted
     ha propuesto implementar el modelo EOQ para optimizar el inventario de kits de sensores
     especializados, cuya demanda semanal se comporta de forma aleatoria con una probabilidad de 0.25 de
     ser de 200 unidades y de 0.75 de ser de 350 unidades. Para este análisis, se considera un costo de
     gestión por cada pedido de 120 dólares y un costo de mantenimiento de inventario de 6 dólares por
     unidad, bajo un entorno de control de calidad sumamente estricto donde la detección de un solo lote
     defectuoso implica la rescisión inmediata del contrato con el proveedor. Actualmente, dicho proveedor
     presenta una probabilidad de entregar un lote defectuoso de 0.1 y cuenta con un tiempo de entrega
     (lead time) que se distribuye uniformemente entre 2 y 5 días donde cada uno es independiente entre si.

     Nota: EOQ = √       2DS

                         H
                               donde D = Demanda, S=Costo de realizar un pedido, H=Costo de mantenimiento
     de inventario.


     Pregunta 1:
     Calcule el valor esperado del EOQ. (5 Puntos)

     Se tiene que la demanda está definida por:

                                                          200   , p = 0.25
                                               D = {
                                                          350   , p = 0.75



                                                                       2DS
                                               E[EOQ] = E[√                  ]
                                                                        H

                                                                       2DS
                                                            = E[√            ]
                                                                        H



     Recordemos que:

                                         E[g(X)] =         ∑         g(x)P (X = x)

                                                        X∈ I mg(X)




     Entonces:

                                               2 ∗ 200S                      2 ∗ 350S
                               E[EOQ] = (√                 )(0.25) + (√                  )(0.75)
                                                    H                            H


                                                    S = 120 H = 6



                                           2 ∗ 200 ∗ 120                     2 ∗ 350 ∗ 120
                          E[EOQ] = (√                      )(0.25) + (√                      )(0.75)
                                                6                                    6

                                    = 111.1019 unidades




       ((2*200*120/6)^(1/2))*(0.25) +((2*350*120/6)^(1/2))*(0.75)


localhost:6046                                                                                                1/7
21/4/26, 23:03                                                              EC1 SOLUCIONES

      [1] 111.1019


     Pregunta 2:
     Calcule el valor esperado del tiempo que la manufacturera continuará trabajando con el proveedor
     antes de que este falle. Considere cualquier otro tiempo no mencionado en el enunciado como
     despreciable. (6 Puntos)

     Se tienen las siguientes variables aleatorias.

                           L i : Lead Time del lote i

                           L ∼ unif (2, 5)




                                     ú
                           N : N mero de lotes entregados hasta recibir uno def ectuoso

                           N ∼ geo(0.1)



     Si la manufacturera dejará de trabajar con el proveedor cuando reciba un lote defectuoso, el tiempo de
     esta relación comercial está definido por:

                           S : Tiempo que la manuf acturera trabajar                     á con el proveedor
                                     N


                           S = ∑ Li

                                 i=1




     El problema nos pide

                                                                          N


                                                       E[S] = E[∑ L i ]

                                                                          i=1

                                                                                N


                                                                     = E[E[∑ L i |N ]]

                                                                              i=1




     Primero calculemos

                                N                                    n


                            E[∑ L i |N = n] = E[∑ L i |N = n] donde: N ⊥ L i

                               i=1                               i=1

                                                                     n


                                                      = E[∑ L i ] por linealidad de la esperanza

                                                                 i=1

                                                             n


                                                      = ∑ E[L i ]

                                                          i=1


                                                          7
                                                      =          n
                                                          2



     Ahora, E[∑                              , por lo que:
                  N                  7
                        L i |N ] =       N
                  i=1                2




localhost:6046                                                                                                2/7
21/4/26, 23:03                                                                     EC1 SOLUCIONES
                                                                             N


                                                       E[S] = E[∑ L i ]

                                                                             i=1

                                                                                   N


                                                                 = E[E[∑ L i |N ]]

                                                                                   i=1


                                                                             7
                                                                 = E[            N]
                                                                             2

                                                                       7       1
                                                                 =                             í
                                                                                       = 35 d as
                                                                       2 0.1



       (7/2)*(1/0.1)


      [1] 35


     Pregunta 3
     Calcule la varianza del tiempo que la manufacturera continuará trabajando con el proveedor antes de
     que este falle. Considere cualquier otro tiempo no mencionado en el enunciado como despreciable (6
     Puntos)

     El problema nos pide

                                                             N


                                   V ar[S] = V ar[∑ L i ]

                                                             i=1

                                                                   N                                N


                                                 = V ar[E[∑ L i |N ]] + E[V ar[∑ L i |N ]]

                                                                   i=1                             i=1




     Del ejercicio anterior tenermos que E[∑
                                                         N                             7
                                                                 L i |N ] =                N
                                                         i=1                           2




     Calculemos:

                                  N                                      n


                           V ar[∑ L i |N = n] = V ar[∑ L i |N = n]

                                 i=1                                     i=1

                                                                         n


                                                        = V ar[∑ L i |N = n] donde N ⊥ L i

                                                                         i=1

                                                                         n


                                                        = V ar[∑ L i ] donde L 1 ⊥ L 2 ⊥ ⋯ ⊥ L n

                                                                         i=1

                                                               n


                                                        = ∑ V ar[L i ]

                                                             i=1

                                                                             2
                                                             (5 − 2)
                                                        =                          n
                                                                    12
                                                             3
                                                        =          n
                                                             4



     Ahora, V ar[∑                              , por lo que:
                     N                  3
                     i=1
                           L i |N ] =       N
                                        4




localhost:6046                                                                                             3/7
21/4/26, 23:03                                                    EC1 SOLUCIONES
                                                    N


                                V ar[S] = V ar[∑ L i ]

                                                  i=1

                                                         N                         N


                                        = V ar[E[∑ L i |N ]] + E[V ar[∑ L i |N ]]

                                                        i=1                    i=1


                                                  7                   3
                                        = V ar[         N ] + E[          N]
                                                  2                   4

                                            49                    3
                                        =        V ar[N ] +           E[N ]
                                            4                     4
                                       49 1 − 0.1             3   1
                                                         +
                                                    2
                                        4    0, 1             4 0.1




                                        = 1110




       (49/4)*(0.9/0.1^2) + (3/4)*(1/0.1)


      [1] 1110


     Pregunta 4
     Si Var(X|Y) = c (una constante) para todo Y, y Var[E(X|Y)]=0, demuestre porqué la Var(X) = c. Argumente
     su respuesta. (3 puntos)

                                                  V ar(X|Y ) = c

                                                  V ar[E(X|Y )] = 0



     Entonces si usamos la propiedad torre de la varianza condicional.

                                    V ar(X) = V ar[E[X|Y ]] + E[V ar[X|Y ]]

                                    V ar(X) = 0 + E[c]

                                    V ar(X) = 0 + c = c




     EC1 2026-2 B
     En el marco de un proyecto de mejora continua, un equipo de estudiantes de ingeniería industrial ha
     decidido implementar una línea piloto de producción de botellas reutilizables para evaluar su
     rentabilidad antes de escalar el proceso. La profesora encargada ha solicitado estimar la ganancia diaria
     esperada para planificar la asignación de recursos. A partir de datos históricos, se ha determinado que la
     demanda diaria sigue la siguiente distribución: con probabilidad de 0.4 se venderán 15 botellas, con
     probabilidad de 0.35 se venderán 25 botellas y con probabilidad de 0.25 se venderán 40 botellas. El
     costo de producción por unidad es de 18 soles, mientras que el precio de venta es de 30 soles. Además,
     se incurre en un costo fijo diario de 120 unidades monetarias por operación. No obstante, la línea
     presenta fallos por lo que existe una probabilidad de que una botella salga defectuosa, la cual varía
     uniformemente entre 0 y 1.


     Pregunta 1:
     Calcule el valor esperado de la ganancia diaria del proyecto. Asuma que la producción se ajusta
     exactamente a la demanda y que las botellas defectuosas también son vendidas. (5 Puntos)

     La demanda diaria está definida por:

localhost:6046                                                                                                    4/7
21/4/26, 23:03




       (15*0.4)+(25*0.35)+(40*0.25)


      [1] 24.75




       12*((15*0.4)+(25*0.35)+(40*0.25))-120


      [1] 177


     Pregunta 2



     Se tienen las siguientes variables aleatorias:




     El problema nos pide:




     recordemos que:




     entonces




localhost:6046
                 P ∼ unif (0, 1)




                 N |P ∼ geo(P )
                                                    ⎩




                                          E[g(X)] = ∫
                                                      ⎪
                                                      ⎧15

                                                D = ⎨25

                                                      40




     Ahora calcularemos la esperanza de la ganancia diaria
                                                             EC1 SOLUCIONES
                                                             , p = 0.4

                                                             , p = 0.35

                                                             , p = 0.25



     donde E[D] = 15 ∗ 0.4 + 25 ∗ 0.35 + 40 ∗ 0.25 = 24.75 botellas




     Si se vende todo lo que se produce, la ganancia diaria está definida por:

                                               G = 30D − 18D − 120




                                       E[G] = E[30D − 18D − 120]

                                             = E[12D] − E[120]

                                             = 12E[D] − 120

                                             = 12 ∗ 24.75 − 120 = 177 soles




     Calcule el numero esperado de botellas que deberán ser producidas para obtener la primera botella
     defectuosa, considerando está en el conteo (6 Puntos)



                 P : probabilidad de que una botella sea def ectuosa




                 N : numero de botellas producidad hasta obtener la primera botella def ectuosa




                                                 E[N ] = E[E[N |P ]]


                                                       = E[




                                                          sopX
                                                                 1

                                                                 P
                                                                     ]




                                                                 g(X)f X (x)dx




                                                                                                         5/7
21/4/26, 23:03                                                                EC1 SOLUCIONES
                                                                          1
                                                                              1         1
                                                E[N ] = ∫                                     dP
                                                                      0
                                                                              P       1 − 0

                                                                                  1
                                                                  = ln(P )| 0




     La integral es impropia, pero si llegaste hasta acá, tienes el puntaje completo.


     Pregunta 3
     Si se produjeron 40 botellas en total, calcule la varianza de botellas defectuosas en esta muestra (6
     Puntos)

     La nueva variable aleatoria es:

                             ú
                       B : N mero de botellas def ectuosas en la muestra de 40 botellas

                       B|P ∼ bin(40, P )



     Calculemos

                                   V ar(B) = V ar[E[B|P ]] + E[V ar[B|P ]]

                                                = V ar[40P ] + E[40P (1 − P )]

                                                                                                        2
                                                = V ar[40P ] + E[40(P − P                                   )]
                                                              2                                                   2
                                                = 40 V ar[P ] + 40(E[P ] − E[P                                        ])



     Recordemos que:
                                                                                  2           2
                                               V ar[X] = E[X                          ] − E       [X]

                                                          2                                   2
                                               E[X            ] = V ar[X] + E                     [X]



     Entonces:
                                        2                                                                   2
                          E[B] = 40 V ar[P ] + 40(E[P ] − V ar[P ] − E                                          [P ])

                                                      2                                                 2
                                            (1 − 0)                    1 + 0                (1 − 0)                   1 + 0
                                        2                                                                                       2
                                 = 40                         + 40(                    −                        − (            ) )
                                              12                              2                   12                       2
                                                          2
                                 = 140 botellas




       ((40^2)*(1/12))+(40*((1/2)-(1/12)-(1/4)))


      [1] 140


     Pregunta 4
     Demuestre la propiedad torre de la esperanza condicional para el caso en dos variables aleatorias (X,Y)
     sean continuas (3 Puntos)




localhost:6046                                                                                                                       6/7
21/4/26, 23:03                                                 EC1 SOLUCIONES

                 E(E(Y |X)) = ∫           E(Y |X = x)f X (x)dx
                                  Sop X




                              recordando que E(Y |X = x) ≡ ∫                       yf Y |X (y|X = x)dy
                                                                           Sop Y




                           =∫             ∫           yf Y |X (y|X = x)f X (x)dydx
                                  Sop X       Sop Y



                           =∫             y∫           f Y ,X (y, x)dxdy
                                  Sop Y        Sop X


                              por la ley de probabilidad total


                           =∫             yf Y (y)dy = E(Y )
                                  Sop Y




localhost:6046                                                                                           7/7
