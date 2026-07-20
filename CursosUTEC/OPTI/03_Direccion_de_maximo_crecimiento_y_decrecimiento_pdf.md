---
curso: OPTI
titulo: 03_Direccion de maximo crecimiento y decrecimiento
slides: 13
fuente: 03_Direccion de maximo crecimiento y decrecimiento.pdf
---

3. Dirección de máximo crecimiento y
             decrecimiento

            Optimización




                                         1 / 13
¿Cómo llegar a la cima de una montaña?




                                           2 / 13
Mapa topográfico




                    3 / 13
Conjuntos de nivel


     Conjuntos de nivel

     Sea f : D ⊂ Rn → R y sea c ∈ R. El conjunto de nivel de
     valor c es el conjunto de todos los puntos (x1 , . . . , xn ) ∈ D
     tales que f (x1 , . . . , xn ) = c.


                 Si n = 2 → curvas de nivel


                 Si n = 3 → superficies de nivel




                                                                         4 / 13
Ejercicio 1




     Ejercicio 1

     Grafique conjuntos de nivel de las siguientes funciones.
      a. f : R2 → R, f (x, y ) = x 2 − y 2 con las curvas de nivel
         correspondientes a los valores 0, ±1 y ±2.
                     x −y
      b. f (x, y ) = 2      con c = 0, ± 21 , ±1.
                    x + y2




                                                                     5 / 13
Derivada direccional


                                            Z




           X     a
                                                        b
                                      v                     Y

                            (a, b)
     Dv f (x) es la pendiente en la dirección del vector unitario v .


                                                                         6 / 13
Cálculo de la derivada direccional


     Teorema
     Si f : D ⊂ Rn → R es diferenciable en x, entonces las
     derivadas direccionales de f en x existen para todo vector
     unitario v ∈ Rn y se cumple

                         Dv f (x) = ∇f (x) · v .

     Ejercicio 2

     Sea f (x, y , z) = x 2 e −yz . Halle la razón de cambio ins-
     tantáneo en (1, 0, 0) en la dirección del vector (2, 2, 4).




                                                                     7 / 13
Dirección de máximo crecimiento




  Recordemos que si f : D ⊂ Rn → R es diferenciable en x ∈ D,
  entonces
                          Dv f (x) = ∇f · v

    ¿Qué dirección debe tener v para que este valor sea máximo?




                                                                     8 / 13
Dirección de máximo crecimiento




     Teorema
     Sea f : D ⊂ Rn → R diferenciable en x. Si ∇f (x) ̸= 0,
     entonces
         ∇f (x) es la dirección de máximo crecimiento en x
         −∇f (x) es la dirección de máximo decrecimiento en x.




                                                                   9 / 13
Vector gradiente y curvas de nivel




     Teorema
     Sea D ⊂ Rn abierto y f : D ⊂ Rn → R una función de clase
     C 1 . Entonces el vector
                               ∇f (x)
     es perpendicular al conjunto de nivel de f que pasa por x.




                                                                  10 / 13
Gráficamente

                                           ∇f (x0 , y0 )


                                  Y


                 f(x, y)=c


                                                           X




   El vector ∇f (x0 , y0 ) es perpendicular a la curva de nivel que pasa
                            por el punto (x0 , y0 ).

                                                                           11 / 13
Idea para minimizar una función

                     f (x, y ) = x 2 + y 2

                           Y

                                             x0




                                                  X




                                                      12 / 13
Ejercicio 3

Considere la función f (x, y ) = 100x 2 + y 2 . Notemos que

                        f (1, 1) = 101.

 a) Halle el punto (1, 1) − ∇f (1, 1) y calcule el valor de
    la función en dicho punto. ¿Disminuye el valor de la
    función?
 b) ¿Por qué esto no contradice el hecho de que la dirección
    opuesta al gradiente es la de máximo decrecimiento?




                                                                 13 / 13

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
