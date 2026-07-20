---
curso: OPTI
titulo: 02_Metodos unidimensionales
slides: 9
fuente: 02_Metodos unidimensionales.pdf
---

2. Métodos unidimensionales

       Optimización




                               1/9
Algoritmos iterativos




  Consisten en elegir un candidato inicial x (0) y generar una
  secuencia
                             x (1) , . . . , x (k)
  de modo que la sucesión converja a la solución del problema.




                                                                   2/9
Método de bisección


  Sea f : [a0 , b0 ] → R una función unimodal con solo un mı́nimo en
  el intervalo [a0 , b0 ]. Además f ′ existe y es continua.

  Algoritmo:
    1. Inicializamos a0 , b0 y k = 0.
                            ak + bk
    2. Definimos xk =
                               2
             Si f ′ (xk ) < 0, entonces ak+1 = xk .
             Si f ′ (xk ) > 0, entonces bk+1 = xk .
             Si f ′ (xk ) = 0, entonces el algoritmo termina.
    3. k = k + 1 y si bk − ak < ϵ terminamos el algoritmo, de lo
       contrario, repetimos desde el paso 2.



                                                                        3/9
Ejercicio



     Ejercicio 1

     Use el método de bisección para encontrar el valor de x que
     minimiza a la función

                       f (x) = 8e 1−x + 7 log(x)

     en el intervalo [1, 2]. Encuentre un intervalo para x de longi-
     tud menor o igual a 0.1.




                                                                       4/9
Método de Newton



  Sea f : [a0 , b0 ] → R unimodal de modo que existen f ′ y f ′′ ; y que
  f ′′ (x) > 0 para todo x ∈ [a0 , b0 ].

  Algoritmo:
   1. Inicializamos x0 y k = 1.
                              f ′ (xk )
   2. Definimos xk+1 = xk − ′′          .
                              f (xk )
   3. k = k + 1 y si |xk+1 − xk | < ϵ terminamos el algoritmo, de lo
      contrario, repetimos desde el paso 2.




                                                                           5/9
Condición de parada

  El algoritmo se detiene cuando la diferencia entre dos de los
  valores es menor a cierto valor establecido ϵ (llamado precisión o
  tolerancia).

                            |xk+1 − xk | < ϵ.
     Ejercicio 2

     Use el método de Newton para encontrar el valor de x que
     minimiza a la función
                                  2
                        f (x) = e x + (2x − 1)3 .

     Utilice valores apropiados para x0 y una tolerancia de ϵ =
     10−5 .



                                                                        6/9
Método de la secante



  Sea f : [a0 , b0 ] → R unimodal de modo que existe f ′ . En el
  método de Newton consideramos
                                             f ′ (xk )
                          xk+1 = xk −                   .
                                             f ′′ (xk )

  Podemos aproximar la segunda derivada por

                                     f ′ (xk ) − f ′ (xk−1 )
                      f ′′ (xk ) =
                                           xk − xk−1




                                                                   7/9
Método de la secante




  Algoritmo:
   1. Inicializamos x0 , x−1 y k = 1.
                                    xk − xk−1
   2. Definimos xk+1 = xk − ′                         f ′ (xk ).
                                f (xk ) − f ′ (xk−1 )
   3. k = k + 1 y si |xk+1 − xk | < ϵ terminamos el algoritmo, de lo
      contrario, repetimos desde el paso 2.




                                                                       8/9
Condición de parada



     Ejercicio 3

     Use el método de la secante para encontrar el valor de x que
     minimiza a la función
                                1
                         f (x) = x 2 − senx.
                                2
     Utilice valores apropiados para x0 y x−1 ; y una precisión de
     ϵ = 10−5 .




                                                                      9/9

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
