---
curso: OPTI
titulo: 07_Metodo de Newton
slides: 8
fuente: 07_Metodo de Newton.pdf
---

7. El método de Newton

     Optimización




                          1/8
El método de Newton


                            y = Q(x)




      Y




                                       y = f (x)
             x0        x∗                  X
                  x1




                                                   2/8
Aproximación cuadrática

     Aproximación cuadrática

     Sea f : D ⊂ Rn → R una función de clase C 2 . La aproxima-
     ción cuadrática de f en a = (a1 , . . . , an ) ∈ D es

                                       1
      Q(x) = f (a) + ∇f (a) · (x − a) + (x − a)T Hf (a)(x − a)
                                       2

     Ejercicio 1

     Halle la aproximación cuadrática de

                     f (x, y ) = e x + cos(x 2 + y 2 )

     en el punto (0, 0).


                                                                   3/8
Mı́nimo de la aproximación cuadrática



  Si hallamos el gradiente de la aproximación cuadrática y la
  igualamos a 0 obtenemos

                      ∇f (a) + Hf (a)(x − a) = 0

  Si el Hessiano es una matriz positivo definida, entonces el mı́nimo
  de la aproximación cuadrática se halla en

                        x = a − Hf (a)−1 ∇f (a)




                                                                        4/8
Método de Newton




  El método de Newton consiste en considerar un punto inicial x0 e
  iterar
                   xk+1 = xk − Hf (xk )−1 ∇f (xk )
  con una condición de parada.

      Si f es una función de clase C 3 , el método de Newton es
    localmente convergente si Hf es una matriz definida positiva.




                                                                      5/8
Ejemplo donde no converge




    Ejercicio 2
                   4
    Sea f (x) = x 3 . Demuestre que el método de Newton no
    converge para ningún valor inicial x0 ̸= 0 (sin importar qué
    tan cerca esté de 0).




                                                                     6/8
Inclusión de la longitud de paso




  Podemos modificar el método incluyendo una longitud de paso

                   xk+1 = xk − αHf (xk )−1 ∇f (xk )

  donde α es la longitud de paso.




                                                                 7/8
Modificación de Levenberg-Marquardt


  Si Hf no es positivo definida podemos considerar en su lugar una
  matriz
                                Hf + µI
  de modo que la nueva matriz sea positivo definida. Con esta
  modificación tenemos

               xk+1 = xk − α[Hf (xk ) + µk I ]−1 ∇f (xk )

      Si µk → 0 el método se aproxima al método de Newton.
      Si µk → +∞ el método se aproxima al método del gradiente
      descendiente.




                                                                     8/8

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
