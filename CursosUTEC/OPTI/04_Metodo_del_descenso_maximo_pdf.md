---
curso: OPTI
titulo: 04_Metodo del descenso maximo
slides: 20
fuente: 04_Metodo del descenso maximo.pdf
---

4. Método del descenso máximo

         Optimización




                                  1 / 20
Objetivos




      Describir los métodos de búsqueda lineal.
      Describir el método de descenso máximo.
      Mostrar un ejemplo donde se use dicho método.




                                                       2 / 20
Métodos de búsqueda lineal




                               3 / 20
Algoritmo




                           xk+1 = xk + αk pk
  donde:
      x0 : punto inicial
      pk : dirección de búsqueda en la iteración k.
      αk : longitud del paso en la iteración k.




                                                         4 / 20
Ejemplo



          Y     x0
              p0




                     X




                         5 / 20
Ejemplo



          Y           x0


                   α0 p0

              x1




                           X




                               6 / 20
Ejemplo



          Y                x0


                        α0 p0

                   x1
              p1




                                X




                                    7 / 20
Ejemplo



          Y                    x0


                            α0 p0

                       x1
              x2 α p
                 1 1




                                    X




                                        8 / 20
Una visualización muy útil




                               9 / 20
Criterio de parada




                     ||xk+1 − xk || < ϵ




                                          10 / 20
Método del Descenso Máximo

  Ejemplo f (x, y ) = x 2 + 10y 2

                                    Y


                                        x0 = (1, 1)


                                           x1 = (0.899, −0.008)
                                                                  X




                                                                      11 / 20
Método del Descenso Máximo
  Ejemplo f (x, y ) = x 2 + 10y 2
  Menor valor de f en un punto de la forma

                          (1, 1) − α(2, 20)




                                              12 / 20
Método del Descenso Máximo

  Ejemplo f (x, y ) = x 2 + 10y 2

                                    Y


                                             x0


                                        x2   x1
                                                  X




                                                      13 / 20
Algoritmo




   1. Inicializamos x0 .
   2. Definimos gk = ∇f (xk ). Hallamos αk de modo que
      f (xk − αk gk ) sea lo mı́nimo posible
   3. xk+1 = xk − αk gk
   4. Si ||xk+1 − xk || ≤ ϵ terminamos el algoritmo de lo contrario
      repetimos desde el paso 2.




                                                                      14 / 20
Algoritmos globalmente convergentes




  Decimos que un algoritmo es globalmente convergente si para
  cualquier punto inicial el algoritmo converge a un punto que
  cumple las condiciones necesarias para ser un mı́nimo.


  El algoritmo del Descenso Máximo es globalmente convergente.




                                                                  15 / 20
Ejemplo

  f (x, y ) = 10y 4 + (1 − x)2
  Punto inicial x0 = (3, 0.5).
  Iteracion 2:




                                 16 / 20
Ejemplo

  f (x, y ) = 10y 4 + (1 − x)2
  Punto inicial x0 = (3, 0.5).
  Iteracion 5:




                                 17 / 20
Ejemplo

  f (x, y ) = 10y 4 + (1 − x)2
  Punto inicial x0 = (3, 0.5).
  Iteracion 10:




                                 18 / 20
Ejemplo
  f (x, y ) = 10y 4 + (1 − x)2
  Punto inicial x0 = (3, 0.5).
  Valor de la función




                                 19 / 20
Conclusiones




     Los algoritmos de búsqueda lineal son una clase general de
     algoritmos que nos permiten minimizar funciones.
     El Método del Descenso Máximo se basa en movernos
     constantemente en la dirección opuesta al gradiente eligiendo
     el tamaño de paso en cada iteración.
     Es globalmente convergente.




                                                                      20 / 20

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
