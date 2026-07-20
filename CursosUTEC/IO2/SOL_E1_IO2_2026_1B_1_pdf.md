---
curso: IO2
titulo: SOL-E1-IO2-2026-1B (1)
slides: 4
fuente: SOL-E1-IO2-2026-1B (1).pdf
---

5/25/26, 3:35 PM                                                      SOL-E1-IO2-2026-1B



     SOL-E1-IO2-2026-1B




     Instrucciones generales:
       1. Esta evaluación es de carácter estrictamente individual. Usted está tomando esta prueba bajo conocimiento del
          reglamento de honestidad y buena conducta académica de la UTEC. Cualquier violación del mismo será reportado
          a las instancias pertinentes, anexando las pruebas recabadas, para su evaluación.
       2. Puede utilizar un formulario con el contenido teórico del curso. El mismo no puede contener ningún ejercicio
          resuelto. No se permitirá el uso de calculadoras para resolver el examen, deje las expresiones finales evaluadas en
          todos los parámetros necesarios para calcular la expresion. No es necesario que evalúen dichas expresiones.
          Cualquier resultado numérico correcto sin la justificación teórica adecuada no recibirá ningún crédito. Recuerde
          definir todas las variables aleatorias que vaya a necesitar para formular lo requerido en cada una de las preguntas.
       3. Usted tendrá en total 100 minutos para resolver el examen.


     Enunciados
     La Cadena de Suministro del Aguaje en RequenaLa empresa “Amazon Fruit S.A.” gestiona la logística de recolección de
     aguaje desde las comunidades recolectoras hasta su planta de procesamiento en Iquitos. El flujo de sacos de aguaje y
     la llegada de transportistas fluviales (peque-peques) presentan comportamientos estocásticos que deben ser
     modelados para optimizar la operación.

       1. (4 puntos) Se modela la llegada de pedidos de pulpa de aguaje desde el extranjero como un proceso de Poisson
          con λ = 0.5 pedidos/semana. Si se sabe que durante las primeras dos semanas se han recibido exactamente 3
          pedidos de pulpa de aguaje desde el extranjero, ¿cuál es el valor esperado del tiempo hasta recibir el noveno
          pedido de pulpa de aguaje desde el extranjero? Defina con precisión las variables aleatorias que se necesiten y
          justifique cada paso

     Solución:

     Sea S   9
                 =   el tiempo de llegada del noveno pedido de pulpa de aguaje

     Sea N (t) = el número de pedidos de pulpa de aguaje desde el extranjero en (0, t] ∼ P oisson (      t

                                                                                                         2
                                                                                                             )



     Se requiere usar los tiempos condicionales de llegada:

                                                                      9 − 3
                                            E(S 9 |N (2) = 3) = 2 +           = 14 semanas
                                                                        1

                                                                        2




       2. El número de botes que llegan al puerto de Iquitos puede modelarse como un proceso de Poisson homogéneo
          con tasa λ = 5 botes/día. De estos, el 20% transporta aguaje del “Humedal Protegido” y el 80% de las “Zonas
          Abiertas”.

     2.1) (4 puntos) Si en un día llegaron 10 botes en total, ¿cuál es la distribución de la cantidad de botes que vienen del
     “Humedal Protegido”? Defina con precisión las variables aleatorias que se necesiten y justifique cada paso

     Soluición:

localhost:3786                                                                                                                   1/4
5/25/26, 3:35 PM                                                                                                    SOL-E1-IO2-2026-1B

     Sea N (t) = el número de botes que llegan al puerto de Iquitos en (0, t] ∼ P oisson(5t)

     Por el teorema de bifurcación y considerando que los botes son clasificados como tipo I independientemente de
     todo lo demás como un bote que proviene del humedal protegido con probabilidad constante del 20%,
     podemos que decir que si N        H P (t)   es el número de botes que llegan al puerto de Iquitos provenientes del humedal
     protegido, entonces N        H P (1)|N (1)   = 10 ∼ Bin (10,
                                                                                                100
                                                                                                   20
                                                                                                        )   .

     2.2) (4 puntos) ¿Cuál es la probabilidad de que en un día lleguen exactamente 2 botes de zonas protegidas y 3 de
     zonas abiertas? Defina con precisión las variables aleatorias que se necesiten y justifique cada paso

     Solución:

     Sea N (t) = el número de botes que llegan al puerto de Iquitos en (0, t] ∼ P oisson(5t)

     Por el teorema de bifurcación y considerando que los botes son clasificados como tipo I independientemente de todo
     lo demás como un bote que proviene del humedal protegido con probabilidad constante del 20%, podemos que decir
     que si N    H P (t)   es el número de botes que llegan al puerto de Iquitos provenientes del humedal protegido y N                        ZA (t)   es
     el número de botes que llegan al puerto de Iquitos provenientes de zonas abiertas, entonces la probabilidad requerida
     viene dada por:

     P (N H P (1) = 2, N ZA (1) = 3) =P (N H P (1) = 2)P (N ZA (1) = 3)

                                                                                                            ó
                                             el teorema de bif urcaci n nos garantiza la independencia del procesos bif urcados

                                                       −1        −4          3
                                                   e        e            4
                                              =
                                                    2!              3!



       3. (4 puntos) La llegada de recolectores a la oficina de pagos varía según la intensidad de la cosecha. La oficina de
          pagos sólo abre durante 4 horas al día y la tasa de llegada de los recolectores a la oficina de pagos depende del
          tiempo y viene dada por λ(t) = 4t − t para 0 ≤ t ≤ 4 donde t representa las horas desde el inicio de la jornada.
                                                                2



          Calcule la probabilidad de que no llegue ningún recolector en la primera hora de trabajo, pero lleguen 4
          recolectores antes de la tercera hora de trabajo. Defina con precisión las variables aleatorias que se necesiten y
          justifique cada paso

     Solución:

     Sea N (t) el número de recolectores que llegan a la oficina de pagos en (0, t]. La probabilidad requerida se formula
     como sigue:

                     P (N (1) = 0, N (3) = 4) =P (N (1) = 0, N (3) − N (1) = 4)

                                                                             é
                                                            despu s de disnjuntizar los incrementos son independientes

                                                       =P (N (1) = 0)P (N (3) − N (1) = 4)

                                                                −m(1)                              0        m(3)−m(1)                      4
                                                            e                [m(1)]                     e                  (m(3) − m(1))
                                                       =
                                                                             0!                                                4!
                                                                    5                0        22                4
                                                                −            5                          5
                                                            e       3   [        ]           e 3 (          )
                                                                             3                          3
                                                       =
                                                                        0!                         4!



     En donde,

                                                                                         1
                                                                                                            2
                                                                                                                          5
                                                       m(1) ≡ ∫                              (4t − t )dt =
                                                                                     0
                                                                                                                          3

                                                                                                                3
                                                                                                                                    22
                                                                                                                           2
                                                       m(3) − m(1) ≡ ∫                                              (4t − t )dt =
                                                                                                            1
                                                                                                                                    3




localhost:3786                                                                                                                                               2/4
5/25/26, 3:35 PM                                                         SOL-E1-IO2-2026-1B

       4. (4 puntos) En la línea de envasado de pulpa de aguaje, las fallas mecánicas ocurren según un proceso de Poisson
          con λ = 0.1 fallas/hora. Cada falla genera un costo de reparación C que sigue una distribución Uniforme entre
          $100     y $500. Calcule el valor esperado y la varianza del costo acumulado por fallas tras 40 horas de operación.
          Defina con precisión las variables aleatorias que se necesiten y justifique cada paso

     Solución:

     Sea N (t) = # de fallas mecánicas en la línea de envasado de pulpa de aguaje (0, t] ∼ P oisson (                             t

                                                                                                                                  10
                                                                                                                                       )



     Sea C = costo en dólares de la falla mecánica i
            i




     Sea C(t) = Costo total acumulado por fallas mecánicas en la línea de envasado de pulpa de aguaje en (0, t]

     Note que

                                                                       N (t)


                                                             C(t) = ∑ C i

                                                                         i=1




     Se requiere calcular E(C(40)) y V ar(C(40)), para lo cual debemos usar la propiedad torre de la esperanza y la
     varianza condicional.

     Es decir,

                                         N (40)


                       E(C(40)) =E [ ∑ c i ]

                                          i=1


                                      por la propiedad torre de la esperanza condicional

                                               N (40)


                                    =E [E [ ∑ C i N (40)]]

                                                i=1


                                      en donde

             N (40)                      N (40)


        E [ ∑ C i N (40)] =E [ ∑ C i N (40) = n]

                 i=1                      i=1
                                                              n=N (40)


                                          n


                                    =E [∑ C i ] = nE(C)|              = N (40)E(C)
                                                           n=N (40)

                                         i=1


                                     Finalmente,

                                               N (40)


                       E(C(40)) =E [E [ ∑ C i N (40)]]

                                                i=1


                                                                                                                                      1
                                    =E[N (40)E(C)] = E(X)E(N (40)) =                  $300          ∗      40       ∗                            = $1200
                                                                                                                                  10
                                                                               E(U nif (100,500))       t=40horas
                                                                                                                             1
                                                                                                                        λ=        f allas/hora
                                                                                                                             10




     Por otro lado, usando la propiedad torre de la varianza condicional tenemos que:

          V ar(C(40)) =V ar[E(C(40)|N (40))] + E[V ar(C(40)|N (40))]

                                                                               é
                            usando que las C i s son independientes e id nticamente distribuidas

                                                                               2
                          =V ar[N (40)E(C)] + E[N (40)V ar(C)] = E                 (C)V ar(N (40)) + V ar(C)E(N (40))
                                                                                                                        2
                                                                                                   (500 − 100)
                               2                                                       2                                                              2
                          =E       (C)V ar(N (40)) + V ar(C)E(N (40)) = (300)              ∗ 4 +                            ∗ 4 = 413.333, 3$
                                                                                                           12




localhost:3786                                                                                                                                             3/4
5/25/26, 3:35 PM                SOL-E1-IO2-2026-1B

       300^2*4+((400^2)/12)*4


     [1] 413333.3




localhost:3786                                       4/4
