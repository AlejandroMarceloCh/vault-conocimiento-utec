---
curso: OPTI
titulo: 05_Metodo del gradiente descendiente
slides: 18
fuente: 05_Metodo del gradiente descendiente.pdf
---

5. Método del gradiente descendiente


            Optimización




                                        1 / 18
Introducción


                Y


                    xk


                    −∇f (xk )
                                X




                                    2 / 18
Objetivos




      Describir el método de gradiente descendiente.
      Conocer cómo elegir el tamaño de paso.
      Mostrar un ejemplo donde se use dicho método.




                                                        3 / 18
α es constante


                 Y


                     xk


                     −α∇f (xk )

                                  X




                                      4 / 18
Algoritmo




   1. Inicializamos x0 .
   2. Definimos gk = ∇f (xk ).
   3. xk+1 = xk − αgk .
   4. Si ||xk+1 − xk || ≤ ϵ terminamos el algoritmo de lo contrario
      repetimos desde el paso 2.




                                                                      5 / 18
Ejemplo


  Ejemplo f (x, y ) = x 2 + 10y 2


                           α = 0.01
                          x0 = (1, 1)
                   ∇f (x, y ) = (2x, 20y )
                    ∇f (1, 1) = (2, 20)
                          x1 = (1, 1) − 0.01(2, 20)
                               = (0.98, 0.8)




                                                      6 / 18
Ejemplo

  Ejemplo f (x, y ) = x 2 + 10y 2



                                    α = 0.01

                                    Y
                                          x0 = (1, 1)

                                         x1 = (0.98, 0.8)


                                                            X




                                                                7 / 18
α muy grande
                   x2
               Y




                        −α∇f (x1 )



                         x0


                          −α∇f (x0 )
                                       X




                    x1
                                           8 / 18
α muy pequeño


                 Y

                     x0


                     xk

                          X




                              9 / 18
Algoritmos globalmente convergentes




  Decimos que un algoritmo es globalmente convergente si para
  cualquier punto inicial el algoritmo converge a un punto que
  cumple las condiciones necesarias para ser un mı́nimo.




                                                                 10 / 18
Convergencia del método




  Teorema
  Sea f : Rn → R una función con matriz Hessiana Hf (x) cuyos
  valores propios siempre son menores que L. Entonces el método del
  gradiente descendiente es globalmente convergente si
                                    1
                               α≤
                                    L




                                                                       11 / 18
Caso de una función cuadrática




     Si f es una función cuadrática, el algoritmo es globalmente
                        convergente si y solo si
                                     2
                                α<
                                     L
      donde L es el máximo valor propio de la matriz Hessiana.




                                                                     12 / 18
Ejemplo


  Ejemplo f (x, y ) = x 2 + 10y 2


                        ∇f (x, y ) = (2x, 20y )
                                              
                                       fxx fxy
                        Hf (x, y ) =
                                       fyx fyy
                                            
                                       2 0
                        Hf (x, y ) =
                                       0 20
                                L = 20
                                      2
                                α <       = 0.1
                                     20




                                                   13 / 18
Ejemplo

  f (x, y ) = 10y 4 + (1 − x)2
  Punto inicial x0 = (3, 0.5).
  Iteracion 2:




                                 14 / 18
Ejemplo

  f (x, y ) = 10y 4 + (1 − x)2
  Punto inicial x0 = (3, 0.5).
  Iteracion 10:




                                 15 / 18
Ejemplo

  f (x, y ) = 10y 4 + (1 − x)2
  Punto inicial x0 = (3, 0.5).
  Iteracion 200:




                                 16 / 18
Ejemplo

  f (x, y ) = 10y 4 + (1 − x)2
  Punto inicial x0 = (3, 0.5).
  Valor de la función




                                 17 / 18
Conclusiones




     El método del gradiente descendiente simplifica al método del
     descenso máximo pues el valor de α es constante.
     Debemos tener cuidado al elegir el valor de α: no puede ser
     muy pequeño ni muy grande.
     Si lo elegimos correctamente, el método del gradiente
     descendiente es globalmente convergente.




                                                                       18 / 18

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
