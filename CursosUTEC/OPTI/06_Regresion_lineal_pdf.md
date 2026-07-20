---
curso: OPTI
titulo: 06_Regresion lineal
slides: 27
fuente: 06_Regresion lineal.pdf
---

6. Regresión Lineal


   Optimización




                       1 / 27
Objetivos




      Describir los modelos de regresión lineal.
      Definir el problema de optimización subyacente.
      Aplicar el método de gradiente descendiente para resolverlo.




                                                                      2 / 27
Regresión lineal




                    f (x) = b0 + b1 x
                                        3 / 27
Regresión lineal




                    f (x) = 1 + 2x
                     f (20) = 51
                                     4 / 27
Regresión lineal




               ¿Cuál es la “mejor” función lineal f ?

                                                          5 / 27
Data




       6 / 27
Residuos




  yi : valores observados
  ŷi = f (xi ):valores predichos.
  El residuo es:

                                ri = yi − ŷi




                                                7 / 27
Residuos




           8 / 27
Función objetivo

  Promedio de residuos al cuadrado (MSE)

                          n                n
                       1X 2   1X
                         ri =    (yi − ŷi )2
                       n      n
                         i=1              i=1

  Expresado en términos de los coeficientes tenemos
                                     n
                                  1X
                  R(b0 , b1 ) =     (yi − b0 − b1 xi )2
                                  n
                                    i=1


   Para encontrar la función f debemos encontrar los valores de b0 y
                 b1 que minimizan la función objetivo.



                                                                        9 / 27
Regresión múltiple




                       y = b0 + b1 x1 + b2 x2

                                                10 / 27
Aumentamos una columna




                y = b0 x0 + b1 x1 + b2 x2
                                            11 / 27
Matrices importantes


                          1 x11 x12 . . .   x1p
                                               
                         1 x21 x22 . . .   x2p 
                          ..
                                               
                                                
                         .                     
                          ..
                                               
                                                
                         .
                       X=                      
                                                
                         .
                          ..
                                                
                                                
                                               
                         .
                          ..
                                                
                                                
                          1 xn1 xn2 . . .   xnp   n×(p+1)




                                                    12 / 27
Matrices importantes


                          
                           y1
                          y2 
                          .. 
                          
                         .
                       y= 
                          
                          
                          
                          
                          
                           yn   n×1




                                      13 / 27
Matrices importantes




                            
                             b0
                            b1 
                            
                       β =  b2 
                            
                           .
                            .. 
                             bp   (p+1)×1




                                            14 / 27
Predicciones



                     1 x11 x12 . . .         x1p
                                                
                    1 x21 x22 . . .         x2p   
                                                  b
                     ..
                    
                                                  0
                    .                            b 
                                                   1
                     ..
                    
                                                  b2 
                                                  
                    .
               Xβ =                              . 
                    .                            . 
                     ..                          .
                                                  bp
                                                
                    .
                     ..                         
                     1 xn1 xn2 . . .         xnp

                  ŷi = b0 + b1 xi1 + · · · + bp xip



                                                           15 / 27
Residuos




                      y1 − ŷ1
                              
                    y2 − ŷ2 
                     .. 
                              
                     . 
           y − Xβ = 
                              
                               
                              
                              
                              
                              
                       yn − ŷn   n×1




                                        16 / 27
Función objetivo


  Promedio de los residuos cuadráticos (MSE).

                    n           n
                1X 2   1X               1
                  ri =    (yi − ŷi )2 = ||y − X β||2
                n      n                n
                  i=1          i=1

  Expresada en términos de los coeficientes tenemos

                                      1
                            R(β) =      ||y − X β||2
                                      n

   Esta es una función cuadrática de p + 1 variables: b0 , b1 , . . . bp+1 .




                                                                                 17 / 27
Gradiente




  Usando cálculo vectorial podemos demostrar

                              2
                     ∇R(β) = − X t (y − X β)
                              n




                                                18 / 27
Algoritmo de gradiente descendiente




      1. Inicializamos β0 (usualmente de manera aleatoria).
                           2
      2. βk+1 = βk + α[ X t (y − X βk )]
                           n
      3. Si ||xk+1 − xk || ≤ ϵ terminamos el algoritmo de lo con-
         trario repetimos desde el paso 2.




                                                                    19 / 27
Estandarización



  Es conveniente estandarizar para disminuir el número de
  condicionamiento del problema. La consiste en calcular las nuevas
  variables
                                    x − x̄
                            x std =
                                      sx
  donde x̄ es la media y sx la desviación estándar de x. Al calcular
  los coeficientes de esta regresión obtenemos

               y std = b1std x1std + b2std x2std + · · · + bpstd xpstd




                                                                         20 / 27

Coeficientes originales



  Podemos obtener los coeficientes correspondientes a las variables
  originales con las siguientes fórmulas
                                           sy
                              bi = bistd
                                           sx


                   b0 = mean(y − b1 x1 − . . . bp xp )




                                                                      21 / 27
Ejemplo




          22 / 27
Ejemplo




          23 / 27
Ejemplo




          24 / 27
Ejemplo




               β std = (−0.105, −0.431, 0.435, 0.679)


      y std = −0.105x1std − 0.431x2std + 0.435x3std + 0.679x4std




                                                                   25 / 27
Ejemplo




  y = 250739.489−5829.195x1 −48.299x2 +145.511x3 +41287.090x4




                                                                26 / 27
Conclusiones




     Una regresión lineal se puede convertir en un problema de
     optimización.
     Es conveniente estandarizar las variables antes de aplicar el
     método de gradiente descendiente.




                                                                     27 / 27

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
