---
curso: IO2
titulo: EC5 Solución
slides: 6
fuente: EC5 Solución.pdf
---

29/6/26, 2:22                                                    EC5



     EC5
     EC5 2026-1 A

     En una sucursal bancaria se dispone de 2 cajas para atender a los clientes. Si hay entre 0 y 1 cliente en
     el sistema, opera 1 caja; y si hay 2 clientes, funcionan las 2 cajas. Los clientes llegan según un proceso
     de Poisson con una tasa de λ clientes por minuto, y el tiempo de servicio en cada caja sigue una
     distribución exponencial con una tasa de μ clientes por minuto. Suponga que la capacidad máxima
     del sistema es de 2 clientes. Sea X(t) el número de clientes en la estación de cajas de la sucursal
     bancaria a tiempo “t”.


     Pregunta 1:
     Calcule la matriz de transición en un paso de la CMTD asociada a la CMTC. Defina el conjunto de
     estados.

     Primero definiremos el conjunto de estados:

                                                   S = {0, 1, 2}



     El enunciado indica que:

                           L : Tiempo entre llegadas de clientes a la sucursal bancaria

                           L ∼ exp(λ)




                           S i : Tiempo de servicio de la caja "i" para i = 1, 2

                           S i ∼ exp(μ)



     Analizando cada estado:

     Para X(t) = 0 (1 caja activa)

     En este estado solo puede ocurrir un nacimiento, es decir pasar al estado X(t) = 1 con probabilidad 1.

     El sistema cambiará de estado cuando llegue un cliente, por lo tanto, el tiempo que el sistema
     permanece con 0 clientes en la estación de pago será igual al tiempo entre llegadas.

                                                                                            ó
                 T 0 : Tiempo en el que el sistema permanece con 0 clientes en la estaci n de pago

                 T 0 ∼ exp(λ)

                 υ0 = λ



     Para X(t) = 1 (1 caja activa)

     En este estado pueden ocurrir dos escenarios:

           Puede ocurrir un nacimiento, es decir pasar al estado X(t) = 2

           Puede ocurrir una muerte, es decir pasar al estado X(t) = 0

     Si el tiempo entre llegadas es menor al tiempo de servicio de la caja 1, habrán dos clientes en el sistema,
     mientras si el tiempo de servicio de la caja 1 es menor al tiempo entre llegadas el sistema estará vacío.
     Las probabilidades de transición en un paso se calculan usando la probabilidad del primer fallo.
localhost:5256                                                                                                     1/6
29/6/26, 2:22                                                            EC5
                                                                               λ
                                                  P 12 = P (L < S 1 ) =
                                                                          λ + μ



                                                                               μ
                                                  P 10 = P (S 1 < L) =
                                                                          λ + μ



     El sistema cambiará de estado cuando llegue un cliente o termine de atenderse, por lo tanto, el tiempo
     que el sistema permanece con 1 cliente en la estación de pago será el mínimo entre el tiempo entre
     llegadas y el tiempo de servicio de la caja 1.

                                                                                         ó
                 T 1 : Tiempo en el que el sistema permanece con 1 cliente en la estaci n de pago

                 T 1 = min(S 1 , L)

                 T 1 = exp(λ + μ)

                 υ1 = λ + μ



     Para X(t) = 2 (2 cajas activas)

     En este estado solo puede ocurrir una muerte, es decir pasar al estado X(t) = 1 con probabilidad 1.

     El sistema cambiará de estado cuando cualquiera de las dos cajas activas termine su atención, por lo
     tanto, el tiempo que el sistema permanece con 2 clientes en la estación de pago será el mínimo entre
     los tiempos de servicio de la caja 1 y la caja 2.

                                                                                         ó
                 T 2 : Tiempo en el que el sistema permanece con 2 clientes en la estaci n de pago

                 T 2 = min(S 1 , S 2 )

                 T 2 = exp(2μ)

                 υ2 =   2μ



     La matriz de transición en un paso es:

                                                              0     1     0
                                                          ⎡                    ⎤
                                                               μ          λ
                                                    P =             0
                                                              λ+μ        λ+μ

                                                          ⎣                    ⎦
                                                              0     1     0




     Pregunta 2:
     Calcule la matriz generadora infinitesimal.

     Con el análisis de la pregunta 1, la matriz quedaría como:

                                                         −λ         λ           0
                                                     ⎡                               ⎤
                                              R =        μ     −(λ + μ)         λ

                                                     ⎣                               ⎦
                                                         0          2μ         −2μ




     Pregunta 3:
     Usando las ecuaciones BACKWARD de Kolmogorov, formule el sistema de ecuaciones diferenciales
     necesario para calcular la probabilidad de que en “t” unidades de tiempo haya 1 cliente en el sistema
     dado que ahora no hay clientes.

     La pregunta nos pide calcular P     01 (t)




     Usando Backward tenemos lo siguiente:
localhost:5256                                                                                                2/6
29/6/26, 2:22




     Pregunta 4:


     $$




     $$


     EC5 2026-2 B




     Pregunta 1:

     estados.
                 ⎢ ⎥ ⎢ ⎥⎢ ⎥
                 ⎡



                 ⎣
                     P 00 (t)

                     P
                         ′



                         ′
                         10

                         ′
                     P 20 (t)



     El sistema de ecuaciones será:




     Formule las ecuaciones de balance.




     En una cafetería llegan dos tipos de clientes: aquellos que compran café y aquellos que compran té. Los
     clientes que adquieren café llegan según un proceso de Poisson con una tasa de λ clientes por minuto,
     mientras que los clientes que compran té llegan de manera independiente según un proceso de Poisson
     con una tasa de θ clientes por minuto. El tiempo de servicio para cualquier cliente sigue una distribución
     exponencial con una tasa de μ clientes por minuto. Suponga que la capacidad máxima del sistema es de
     2 clientes. Sea X(t) el número de clientes presentes en la cafetería en el instante “t”.




     Calcule la matriz de transición en un paso de la CMTD asociada a la CMTC. Defina el conjunto de



     Primero definiremos el conjunto de estados:



     El enunciado indica que:




localhost:5256
                              (t)
                                        ′
                                    P 01 (t)

                                    P
                                        ′
                                        11

                                        ′
                                    P 21 (t)
                                             (t)
                                                       ′
                                                   P 02 (t)

                                                   P
                                                       ′
                                                       12

                                                       ′
                                                   P 22 (t)




                                                       ′
                                                            (t)
                                                                  ⎤



                                                                  ⎦
                                                                      =
                                                                          ⎡



                                                                          ⎣
                                                                              −λ

                                                                              μ

                                                                              0




                                                   P 01 (t) = −λP 01 (t) + λP 11 (t)



                                                       ′




                                                       ′
                                                   P 21 (t) = 2μP 11 (t) − 2μP 21 (t)




                                                                      λP 0 = μP 1




                                                                      2μP 2 = λP 1




                                                                      P0 + P1 + P2 = 1
                                                                                        λ

                                                                                    −(λ + μ)

                                                                                       2μ




                                                                      (λ + μ)P 1 = λP 0 + μP 2




                                                                                  S = {0, 1, 2}
                                                                                               EC5




                                                                                                  −2μ




                                                   P 11 (t) = μP 01 (t) − (λ + μ)P 11 (t) + λP 21 (t)
                                                                                                     0

                                                                                                     λ
                                                                                                         ⎤⎡



                                                                                                         ⎦⎣
                                                                                                              P 00 (t)

                                                                                                              P 10 (t)

                                                                                                              P 20 (t)
                                                                                                                         P 01 (t)

                                                                                                                         P 11 (t)

                                                                                                                         P 21 (t)
                                                                                                                                    P 02 (t)

                                                                                                                                    P 12 (t)

                                                                                                                                    P 22 (t)
                                                                                                                                               ⎤



                                                                                                                                               ⎦




                                                                                                                                                   3/6
29/6/26, 2:22                                                   EC5
                            A : Tiempo entre llegadas de clientes que compran caf           é
                            A ∼ exp(λ)




                            B : Tiempo entre llegadas de clientes que compran t         é
                            B ∼ exp(θ)




                            S : Tiempo de servicio

                            S ∼ exp(μ)



     Podemos decir, que el tiempo entre llegadas de un cliente será el mínimo entre el tiempo entre llegadas
     de clientes que compran café y té

                                                                                    í
                                L : Tiempo entre llegadas de clientes a la caf eter a

                                L = min(A, B)

                                L ∼ exp(λ + μ)



     Analizando cada estado:

     Para X(t) = 0

     En este estado solo puede ocurrir un nacimiento, es decir pasar al estado X(t) = 1 con probabilidad 1.

     El sistema cambiará de estado cuando llegue un cliente, por lo tanto, el tiempo que el sistema
     permanece con 0 clientes en la estación de pago será igual al tiempo entre llegadas.

                   T 0 : Tiempo en el que el sistema permanece con 0 clientes en la caf eter a  í
                   T 0 ∼ exp(λ + θ)

                   υ0 = λ + θ



     Para X(t) = 1

     En este estado pueden ocurrir dos escenarios:

           Puede ocurrir un nacimiento, es decir pasar al estado X(t) = 2

           Puede ocurrir una muerte, es decir pasar al estado X(t) = 0

     Si el tiempo entre llegadas es menor al tiempo de servicio, habrán dos clientes en el sistema, mientras si
     el tiempo de servicio es menor al tiempo entre llegadas el sistema estará vacío. Las probabilidades de
     transición en un paso se calculan usando la probabilidad del primer fallo.

                                                                  λ + θ
                                          P 12 = P (L < S) =
                                                               λ + θ + μ



                                                                      μ
                                          P 10 = P (S < L) =
                                                               λ + θ + μ



     El sistema cambiará de estado cuando llegue un cliente o termine de atenderse, por lo tanto, el tiempo
     que el sistema permanece con 1 cliente en la cafetería será el mínimo entre el tiempo entre llegadas y el
     tiempo de servicio.




localhost:5256                                                                                                    4/6
29/6/26, 2:22




     Para X(t) = 2




     Pregunta 2:
                            T 1 = min(L, S)

                            T 1 = exp(λ + θ + μ)

                            υ1 = λ + θ + μ




                            T 2 = exp(μ)

                            υ2 = μ



     La matriz de transición en un paso es:




     Calcule la matriz generadora infinitesimal.

     Con el análisis de la pregunta 1, la matriz quedaría como:




     Pregunta 3:


     dado que ahora hay 2 clientes.

     La pregunta nos pide calcular P

     Usando Forward tenemos lo siguiente:

         ⎡



         ⎣
             P
                 ′
             P 00 (t)

                 ′
                 10

                 ′
             P 20 (t)




localhost:5256
                      (t)
                                ′
                            P 01 (t)

                            P
                                ′
                                11

                                ′
                            P 21 (t)



     El sistema de ecuaciones será:
                                     (t)   P
                                               ′
                                           P 02 (t)

                                               ′
                                               12

                                               ′
                                           P 22 (t)
                                                    (t)
                                                          R =




                                                          ⎤



                                                          ⎦
                                                              =
                                                                  ⎡



                                                                  ⎣




                                                              21 (t)




                                                                  ⎡


                                                                  ⎣
                                                                        P =




                                                                       −(λ + θ)

                                                                            μ

                                                                            0




                                                                      P 00 (t)

                                                                      P 10 (t)

                                                                      P 20 (t)




                                                                                 ⎢⎥
                            T 1 : Tiempo en el que el sistema permanece con 1 cliente en la caf eter a




     En este estado solo puede ocurrir una muerte, es decir pasar al estado X(t) = 1 con probabilidad 1.

     El sistema cambiará de estado cuando un cliente de cualquier tipo termine su atención, por lo tanto, el
     tiempo que el sistema permanece con 2 clientes será igual al tiempo de servicio

                            T 2 : Tiempo en el que el sistema permanece con 2 clientes en la caf eter a




                                                                                 ⎡



                                                                                 ⎣
                                                                                       0

                                                                                       μ

                                                                                     λ+θ+μ


                                                                                       0




                                                                                           −(λ + θ + μ)




     Usando las ecuaciones FORWARD de Kolmogorov, formule el sistema de ecuaciones diferenciales




                                                                                     P 01 (t)




                                                                                     P 21 (t)
                                                                                                1




                                                                                                1




                                                                                                λ + θ




                                                                                                    μ




     necesario para calcular la probabilidad de que en “t” unidades de tiempo haya 1 cliente en el sistema




                                                                                     P 11 (t)
                                                                                                0




                                                                                                P 02 (t)

                                                                                                P 12 (t)

                                                                                                P 22 (t)
                                                                                                        EC5




                                                                                                          0

                                                                                                         λ+θ

                                                                                                        λ+θ+μ


                                                                                                          0




                                                                                                           ⎤⎡


                                                                                                           ⎦⎣
                                                                                                                ⎤



                                                                                                                ⎦




                                                                                                                     0

                                                                                                                    λ + θ

                                                                                                                    −μ




                                                                                                                −(λ + θ)

                                                                                                                     μ

                                                                                                                      0
                                                                                                                            ⎤



                                                                                                                            ⎦




                                                                                                                                   λ + θ
                                                                                                                                           í




                                                                                                                                −(λ + θ + μ)

                                                                                                                                     μ
                                                                                                                                           í




                                                                                                                                                0

                                                                                                                                               λ + θ

                                                                                                                                               −μ
                                                                                                                                                       ⎤


                                                                                                                                                       ⎦




                                                                                                                                                           5/6
29/6/26, 2:22                                                   EC5
                             ′
                           P 20 (t) = −(λ + θ)P 20 (t) + μP 21 (t)



                             ′
                           P 21 (t) = (λ + θ)P 20 (t) − (λ + θ + μ)P 21 (t) + μP 22 (t)



                             ′
                           P 22 (t) = (λ + θ)P 21 (t) − μP 22 (t)




     Pregunta 4:
     Formule las ecuaciones de balance.

                                      (λ + θ)P 0 = μP 1




                                      (λ + θ + μ)P 1 = (λ + θ)P 0 + μP 2




                                      μP 2 = (λ + θ)P 1




                                      P0 + P1 + P2 = 1




localhost:5256                                                                            6/6
