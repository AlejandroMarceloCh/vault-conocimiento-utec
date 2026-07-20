---
curso: METNUM
titulo: 06 - Semana 4/Sem4_Sistema de Ecuaciones No Lineales
slides: 36
fuente: 06 - Semana 4/Sem4_Sistema de Ecuaciones No Lineales.pdf
---

Métodos Numéricos
Sistemas de E.N.L - S4
Hermes Yesser Pantoja Carhuavilca
(hpantoja@utec.edu.pe)
Jimmy Mendoza Montalvo
(jmendozam@utec.edu.pe)
Rósulo Pérez Cupe
(rperezc@utec.edu.pe)
Julio Cesar Barraza Bernaola
(jbarraza@utec.edu.pe)
Marco Antonio Cuyubamba Espinoza
(mcuyubamba@utec.edu.pe)
Ronaldo Walter Laureano Huayanay
(rlaureano@utec.edu.pe)


                                    Profesores: Utec-Ciencias
                                                         Índice
                                         1 Método de Newton
                                         2 Método de Punto Fijo




Universidad de Ingeniería y Tecnología    Métodos Numéricos       1 / 35
        Objetivos
            Localizar soluciones de ecuaciones no lineales de dos variables
            Resolver sistemas no lineales mediante los métodos de Newton Raphson y
            Punto Fijo




Universidad de Ingeniería y Tecnología            Métodos Numéricos                  2 / 35
Problema
Dadas las funciones f y g de dos variables reales con valores reales (es decir
f , g : R2 → R) nos interesa encontrar al menos una raíz del sistema de ecuaciones
no lineales:                     
                                    f (x, y ) = 0
                                    g(x, y ) = 0
Es decir, interesa encontrar al menos un par (x̂, ŷ ) ∈ R2 tal que f (x̂, ŷ ) = 0 y
g(x̂, ŷ ) = 0.
En casi la totalidad de casos encontrar la solución analítica es complicado, por lo
tanto se recurre a los métodos numéricos.




Universidad de Ingeniería y Tecnología       Métodos Numéricos                    3 / 35
Ejemplos de Sistemas No Lineales
       Hallar (x, y ) tales que:

                                          f (x, y ) = x 2 + xy − 10 = 0
                               

                                         g(x, y ) = 3xy 2 + y − 57 = 0


       Hallar (x, y ) tales que:

                          f (x, y ) = ln(x 2 + y 2 ) − sen(xy ) − ln(2π) = 0
                      

                         g(x, y ) = ex−y + cos(xy ) = 0




Universidad de Ingeniería y Tecnología                 Métodos Numéricos       4 / 35
Idea gráfica
Hallar la solución del sistema
                                         
                                             f (x, y ) = 0
                                             g(x, y ) = 0

Consiste en buscar la intersección de las curvas de nivel cero para ambas
funciones.
Por ejemplo, el sistema

                             f (x, y ) = x 2 + 1 − y = 0
                         

                           g(x, y ) = 2 cos(x) − y = 0

es la intersección de una parábola y la gráfica de la función coseno.




Universidad de Ingeniería y Tecnología               Métodos Numéricos      5 / 35
Idea gráfica
Podemos usar el siguiente script:
x = -10:0.1:10;
y = -10:0.1:10;
[X , Y ] = meshgrid (x , y ) ;
f1 = X .^2 + 1 - Y ;
f2 = 2* cos ( X ) - Y ;
figure (1) ;
h1 = surfc (X ,Y , f1 ) ;
set ( h1 , ' EdgeColor ' , ' none ') ; hold on
h2 = surfc (X ,Y , f2 ) ;
set ( h2 , ' EdgeColor ' , ' none ')
lightangle ( -45 ,30) ; lighting gouraud ; shading interp
contour (X , Y , f1 ,[0 ,0] , 'r ') ;
contour (X , Y , f2 ,[0 ,0] , 'b ') ;
grid on ; hold off ;
Universidad de Ingeniería y Tecnología   Métodos Numéricos   6 / 35
Idea gráfica
Obtenemos




Universidad de Ingeniería y Tecnología   Métodos Numéricos   7 / 35
1   MÉTODO DE
    NEWTON
Introducción
Una de las ventajas del método de Newton-Raphson, además de su velocidad de
convergencia, es que se puede generalizar fácilmente para la solución de sistemas
de ecuaciones no lineales.




Universidad de Ingeniería y Tecnología     Métodos Numéricos                 9 / 35
Método de Newton
Dado el sistema de ecuaciones no lineales:
                              
                                 f (x, y ) = 0
                                g(x, y ) = 0

Considerando el desarrollo de Taylor de las funciones f y g alrededor del punto
(x0 , y0 ) tenemos:

                                         ∂f                       ∂f
        f (x, y ) = f (x0 , y0 ) +          (x0 , y0 )(x − x0 ) +    (x0 , y0 )(y − y0 ) + R1 (x, y , f )
                                         ∂x                       ∂y

                                         ∂g                       ∂g
      g(x, y ) = g(x0 , y0 ) +              (x0 , y0 )(x − x0 ) +    (x0 , y0 )(y − y0 ) + R2 (x, y , g)
                                         ∂x                       ∂y




Universidad de Ingeniería y Tecnología                         Métodos Numéricos                            10 / 35
Método de Newton (continuación)
Si se simplifican los términos de error R1 y R2 se tiene el sistema:
                                       ∂f                        ∂f
            f (x, y ) ≈ f (x0 , y0 ) +    (x0 , y0 )(x − x0 ) +     (x0 , y0 )(y − y0 )
                                       ∂x                        ∂y
                                       ∂g                        ∂g
           g(x, y ) ≈ g(x0 , y0 ) +        (x0 , y0 )(x − x0 ) +     (x0 , y0 )(y − y0 )
                                       ∂x                        ∂y
Esto se puede escribir vectorialmente de la siguiente manera:
                                             F(x) ≈ F(x0 ) + J(x0 )(x − x0 )
donde
                                                                                                                           
                                                                                            ∂f              ∂f
                                                                                      ∂x (x0 , y0 )   ∂y (x0 , y0 )
      f                            x                       x0
F=                      x=                      x0 =                     JF (x0 ) =                                        ,
                                                                                                                           
      g                            y                       y0                               ∂g              ∂g
                                                                                            ∂x (x0 , y0 )   ∂y (x0 , y0 )

JF (x0 ) es llamada matriz Jacobiana.

Universidad de Ingeniería y Tecnología                              Métodos Numéricos                                 11 / 35
Método de Newton (continuación)
La ecuación anterior vale en general (2 o más ecuaciones):
                                         F(x) ≈ F(x0 ) + JF (x0 )(x − x0 )
Así, una aproximación x1 de la raíz (F(x) = 0) será una solución del sistema lineal:
                                          F(x0 ) + J(x0 )(x1 − x0 ) = 0


       Aproximación usando la inversa de la matriz Jacobiana:
                                               x1 = x0 − J −1 (x0 )F(x0 )


       Aproximación sin usar la inversa de la matriz Jacobiana:
                                         x1 = x0 − ∆x,    J(x0 )∆x = −F(x0 )



Universidad de Ingeniería y Tecnología                      Métodos Numéricos   12 / 35
Método de Newton (continuación)
El proceso iterativo usualmente queda de la siguiente manera:

                        x(k +1) = x(k ) − J −1 (x(k ) )F(x(k ) )                        k = 0; 1; 2; 3; · · ·

siendo necesario conocer el punto inicial o punto semilla x(0) .
                                                                T
Para un sistema de 2 ecuaciones no lineales con x = x y             se tendría:

                              x (k +1)               x (k )                             f (x (k ) , y (k ) )
                                                                                                          
                                             =                    − J −1 (x(k ) )
                              y (k +1)               y (k )                             g(x (k ) , y (k ) )




Universidad de Ingeniería y Tecnología                                  Métodos Numéricos                          13 / 35
Método de Newton Vectorizado
Algoritmo 1: Método de Newton para SENL
Entrada: Funciones F(x), punto inicial x(0) , tolerancia en error relativo Tol
Salida: Aproximación x de la solución de F(x) = 0
k ←0
δr ← 1 (valor mayor a Tol)
Calcular la matriz Jacobiana J(x)
mientras δr > Tol hacer
    si det(J(x(k) )) = 0 entonces
         Terminar con error
    fin si
    x(k +1) ← x(k ) − J −1 (x(k ) )F(x(k) )
            ∥x(k+1) − x(k ) ∥∞
    δr ←
               ∥x(k+1) ∥∞
    k ←k +1
fin mientras
devolver x(k +1)


Universidad de Ingeniería y Tecnología                 Métodos Numéricos         14 / 35
Ejemplo
  Ejemplo
 Resuelva el sistema de ecuaciones:
                           f (x, y ) = x 2 + xy − 10 = 0
                      

                         g(x, y ) = 3xy 2 + y − 57 = 0

 Aplicando el método de Newton y considerando el punto semilla (x (0) , y (0) ) =
 (1.5; 3.5), (efectúe 3 iteraciones).

Para la inversa de una matriz de orden 2 × 2 puede usar:
                                        −1                                        
                             a11 a12                     1                a22 −a12
                                               =
                             a21 a22             a11 a22 − a21 a12       −a21  a11


Universidad de Ingeniería y Tecnología                     Métodos Numéricos             15 / 35
Solución:
La matriz Jacobiana es:
                                                                            
                                                 ∂f             ∂f
                                                 ∂x (x, y )     ∂y (x, y )
                                                                                                                     
                                                                                         2x + y              x
              J(x) = J(x, y ) =                                             =
                                                                                                                   
                                             ∂g                 ∂g
                                             ∂x (x, y )         ∂y (x, y )
                                                                                             3y 2        6xy + 1

Primera iteración:
                                                                                             −1
             (1)                 (0)
                                                  2x (0) + y (0)             x (0)
                                                                                                         f (x (0) , y (0) )
                                                                                                                         
            x                   x
                      =                  −
                                                                                             
            y (1)               y (0)                                                                    g(x (0) , y (0) )
                                                                                              
                                                              2
                                                    3(y (0) )         6x (0) y (0) + 1
                                                                 −1
                                               6.5      1.5                                                 
                            1.5                                              −2.5                    2.0360
                    =                   −                                                  =
                            3.5                                              1.625                   2.8439
                                             36.75 32.5
Universidad de Ingeniería y Tecnología                                Métodos Numéricos                                           16 / 35
Solución: (continúa)
Segunda iteración: (completar como ejercicio)
                                                                                         −1
                                                     2x (1) + y (1)         x (1)
            x (2)               x (1)                                                               f (x (1) , y (1) )
                                                                                                                    
                        =                    −
                                                                                         
            y (2)               y (1)                                                               g(x (1) , y (1) )
                                                                                          
                                                               2
                                                       3(y (1) )      6x (1) y (1) + 1
                                                                          −1             

                    =              −                                                     

                                            

                            =               




Universidad de Ingeniería y Tecnología                                Métodos Numéricos                                      17 / 35
Ejercicio 1 (EP 2023 - 2)
Verdadero o Falso:
En el sistema de ecuaciones no lineales:
                                          2
                              sec(x) − ey      = 0
                                   4x 2 + 5y   = 0

Podemos asegurar que el sistema tiene una solución única al resolverse mediante
                                               " #    π
el método de Newton con un punto semilla x(0) =       2 .
                                                      1




Universidad de Ingeniería y Tecnología     Métodos Numéricos               18 / 35
Ejercicio 2 (EP 2024 - 2)
Procedimental:
Dado el siguiente sistema de ecuaciones no lineales que describen el potencial φ y
la función de corriente ψ de un flujo uniforme inclinado:

                                         φ = V (x cos α + y sin α)
                             ψ = V (y cos α − x sin α)
Con los siguientes valores: φ = 1 m2 /s, ψ = −0.5 m2 /s, x = 3 m, y = 2 m,
                                                                  T
determine en caso de ser posible el valor aproximado de x = V α usando el
                                         T
método de Newton con x(0) = 1/3 π/3 y 2 iteraciones.
                              




Universidad de Ingeniería y Tecnología                 Métodos Numéricos      19 / 35

2   MÉTODO DE
    PUNTO FIJO
Punto Fijo para funciones de dos variables
Para una función vectorial de variable vectorial G : R2 → R2 el punto
p = (x ∗ , y ∗ ) se llama punto fijo de G si y solo si

                                              p = G(p)

Dadas las funciones u y v (reales de variable vectorial)

                 u:       R2     → R                       v:      R2     → R
                                                 y
                         (x, y ) → u(x, y )                       (x, y ) → v (x, y )

tales que G(x, y ) = (u(x, y ), v (x, y )), entonces para un punto fijo (x ∗ , y ∗ ) se
cumple                              ∗
                                      x = u(x ∗ , y ∗ )
                                      y ∗ = v (x ∗ , y ∗ )



Universidad de Ingeniería y Tecnología               Métodos Numéricos                    21 / 35
Método de Punto Fijo                                                     q
                                                              v (x, y ) = 57−y
                                         p
Ejemplo: Dadas las funciones u(x, y ) = 10 − xy           y                3x
entonces p = (2; 3) es un punto fijo para la función
                                                   r        !
                                  p                  57 − y
                     G(x, y ) =      10 − xy ,
                                                       3x

Luego, el método de punto fijo parte del sistema de ecuaciones no lineales
                                
                                   f (x, y ) = 0
                                   g(x, y ) = 0

y despeja dos funciones u : R2 → R, v : R2 → R tales que
                               
                                 x = u(x, y )
                                 y = v (x, y )

Este procedimiento es generalizable a 2 o más ecuaciones.
Universidad de Ingeniería y Tecnología    Métodos Numéricos                  22 / 35
Convergencia para el método del punto fijo
     Teorema
     Sea D = {(x1 , x2 , . . . , xn ) | ai ≤ xi ≤ bi , para toda i = 1, 2, . . . , n} para algún conjunto de constantes
     a1 , a2 , . . . , an y b1 , b2 , . . . , bn . Supongamos que G es una función continua de D ⊆ Rn en Rn con la
     propiedad de que G(x) ∈ D siempre que x ∈ D. Entonces G tiene un único punto fijo en D. Supongamos,
     además, que G tiene derivadas parciales continuas y que existe una constante K < 1 con

                                          ∂gj (x)       K
                                                    ≤     ,    siempre que x ∈ D,
                                            ∂xi         n

     para toda j = 1, 2, . . . , n y toda función componente gj . Entonces la sucesión {x(k ) }∞
                                                                                               k=0 , definida por una
     x(0) seleccionada en D arbitrariamente y generada por

                                         x(k) = G(x(k −1) ),     para cada k ≥ 1,

     converge en el único punto fijo p ∈ D.




Universidad de Ingeniería y Tecnología                            Métodos Numéricos                                  23 / 35
Ejemplo para trabajar en clase
El sistema no lineal
                                               x12 − 10x1 + x22 + 8 = 0,
                                            x1 x22 + x1 − 10x2 + 8 = 0,
puede transformarse en el problema de punto fijo

                                                              x12 + x22 + 8
                                         x1 = g1 (x1 , x2 ) =               ,
                                                                    10
                                                              x1 x22 + x1 + 8
                                         x2 = g2 (x1 , x2 ) =                 .
                                                                     10
Use el teorema anterior para demostrar que la función tiene un punto fijo y el
método converge en:

                             D = {(x1 , x2 ) | 0 ≤ x1 ≤ 1.5          ;    0 ≤ x2 ≤ 1.5}


Universidad de Ingeniería y Tecnología                          Métodos Numéricos         24 / 35
Ejemplo para trabajar en clase
Note que
                          x12 + x22 + 8                   x1 x22 + x1 + 8
                      g1 (x1 , x2 ) =   , g2 (x1 , x2 ) =                 .
                               10                                10
son funciones continuas en D = [0, 1.5] × [0, 1.5].
Verificamos la condición de existencia:
                 G(x) = (g1 (x1 , x2 ), g2 (x1 , x2 )) ∈ D, para todo x = (x1 , x2 ) ∈ D
En efecto, para g1 se tiene
           0 ≤ x1 ≤ 1.5            ;     0 ≤ x2 ≤ 1.5 → 0 ≤ x12 ≤ 2.25        ;   0 ≤ x22 ≤ 2.25,
                                                     → 8 ≤ x12 + x22 + 8 ≤ 13,
                                                             x12 + x22 + 8
                                                     → 0.8 ≤                 ≤ 1.3,
                                                                    10
                                                     → 0 ≤ g1 (x1 , x2 ) ≤ 1.5.

Universidad de Ingeniería y Tecnología                    Métodos Numéricos                         25 / 35
Ejemplo para trabajar en clase
Note que
                          x12 + x22 + 8                   x1 x22 + x1 + 8
                      g1 (x1 , x2 ) =   , g2 (x1 , x2 ) =                 .
                               10                                10
son funciones continuas en D = [0, 1.5] × [0, 1.5].
Verificamos la condición de existencia:
                 G(x) = (g1 (x1 , x2 ), g2 (x1 , x2 )) ∈ D, para todo x = (x1 , x2 ) ∈ D
En efecto, para g2 se tiene
         0 ≤ x1 ≤ 1.5            ;       0 ≤ x2 ≤ 1.5 → 0 ≤ x1 ≤ 1.5       ;   0 ≤ x22 ≤ 2.25,
                                                     → 0 ≤ x1 ≤ 1.5        ;   1 ≤ x22 + 1 ≤ 3.25,
                                                     → 0 ≤ x1 (x22 + 1) ≤ 1.5 × 3.25,
                                                             x1 (x22 + 1) + 8
                                                     → 0.8 ≤                    ≤ 1.2875,
                                                                      10
                                                     → 0 ≤ g2 (x1 , x2 ) ≤ 1.5.
Universidad de Ingeniería y Tecnología                     Métodos Numéricos                         26 / 35
Ejemplo para trabajar en clase
Para
             x12 + x22 + 8                   x1 x22 + x1 + 8
g1 (x1 , x2 ) =            , g2 (x1 , x2 ) =                 , (x1 , x2 ) ∈ D = [0, 1.5]×[0, 1.5].
                  10                                10
Verificamos la condición de contracción: existe K < 1 tal que
                      ∂g1 (x)  K ∂g2 (x)  K
                              ≤ ,        ≤ ,             para todo x ∈ D, i = 1, 2.
                       ∂xi     2  ∂xi     2
En efecto, existe K = 0.9, tal que para g1 se tiene
                                         ∂g1 (x)  x1   ∂g1 (x)   x2
                                                 = ,           =
                                          ∂x1     5     ∂x2      5
                                         ∂g1 (x)   x1   1.5   0.9
                                                 =    ≤     ≤
                                          ∂x1      5     5     2
                                         ∂g1 (x)   x2   1.5   0.9
                                                 =    ≤     ≤
                                          ∂x2      5     5     2
Universidad de Ingeniería y Tecnología                 Métodos Numéricos                  27 / 35
Ejemplo para trabajar en clase
Para
             x12 + x22 + 8                   x1 x22 + x1 + 8
g1 (x1 , x2 ) =            , g2 (x1 , x2 ) =                 , (x1 , x2 ) ∈ D = [0, 1.5]×[0, 1.5].
                  10                                10
Verificamos la condición de contracción: existe K < 1 tal que
                      ∂g1 (x)  K ∂g2 (x)  K
                              ≤ ,        ≤ ,                   para todo x ∈ D, i = 1, 2.
                       ∂xi     2  ∂xi     2
En efecto, existe K = 0.9, tal que para g2 se tiene
                                         ∂g2 (x)  x2 + 1     ∂g2 (x)   x1 x2
                                                 = 2     ,           =
                                          ∂x1       10        ∂x2       5
                                     ∂g2 (x)   x2 + 1   2.25 + 1   0.9
                                             = 2      ≤          ≤
                                      ∂x1        10        10       2
                                              ∂g2 (x)   x1 x2   2.25   0.9
                                                      =       ≤      ≤
                                               ∂x2       5        5     2
Universidad de Ingeniería y Tecnología                       Métodos Numéricos              28 / 35
Criterio de parada y norma infinito
Sea {x(k) } la sucesión generada por el método del punto fijo. Se detiene la iteración en el
paso k + 1 si el error relativo satisface:
                                         ∥x(k +1) − x(k ) ∥∞
                                                             < Tol,
                                            ∥x(k +1) ∥∞
donde Tol > 0 es una tolerancia predefinida, y ∥ · ∥∞ denota la norma infinito.

Definición de la norma infinito:
       Para un vector x = (x1 , x2 , . . . , xn )⊤ ∈ Rn , la norma infinito se define como:
                                             ∥x∥∞ =     max |xi |.
                                                      i=1,2,...,n

       Para una matriz A = [aij ] ∈ Rm×n , la norma infinito se define como:
                                                             n
                                                             X
                                            ∥A∥∞ = max              |aij |,
                                                     1≤i≤m
                                                             j=1


Universidad de Ingeniería y Tecnología                  Métodos Numéricos                     29 / 35
Método del Punto Fijo para SENL
Algoritmo 2: Método del Punto Fijo para SENL
Entrada: Función G(x), punto inicial x(0) , tolerancia en error relativo Tol
Salida: Aproximación x de la solución de x = G(x)
k ←0
δr ← 1 (valor mayor a Tol)
mientras δr > Tol hacer
    x(k +1) ← G(x(k) )
            ∥x(k+1) − x(k) ∥∞
    δr ←
               ∥x(k+1) ∥∞
    k ←k +1
fin mientras
devolver x(k +1)




Universidad de Ingeniería y Tecnología                 Métodos Numéricos       30 / 35
Ejemplo 1
  Ejemplo
 Dado el sistema de ecuaciones:
                                           x12 − 10x1 + x22 + 8 = 0
                                         x1 x22 + x1 − 10x2 + 8 = 0

                                              (0)   (0)
 Considerando el punto semilla (x1 , x2 ) = (0.3; 1.25), efectúe 3 iteraciones para
 cada uno de los siguientes casos: "Utilice" la herramienta IA para validar las
 funciones dadas.
                            x 2 + x22 + 8
     
      x1 = u(x1 , x2 ) = 1
     
   1                                10
                                  2
      x = v (x , x ) = x1 x2 + x1 + 8
     
         2         1 2
                                     10
        x1 = u(x1 , x2 ) = x1 − 9x1 + x22 + 8
                             2
     
   2
        x2 = v (x1 , x2 ) = x1 x22 + x1 − 9x2 + 8
Universidad de Ingeniería y Tecnología                    Métodos Numéricos     31 / 35
Ejemplo 1 (continuación)
Solución: Caso 1.
                                                     (k )     (k )
                                         Iter(k )   x1      x2           Error
                                            0
                                            1
                                            2
                                            3




Universidad de Ingeniería y Tecnología                      Métodos Numéricos    32 / 35
Conclusiones
       El método de Newton es eficiente para sistemas no lineales pero requiere
       calcular la inversa de la matriz jacobiana en cada iteración, lo cual puede ser
       costoso.
       El método de Punto Fijo depende de construir funciones adecuadas para
       garantizar convergencia y verificar condiciones de contracción.
       Ambos métodos iterativos necesitan puntos iniciales (o puntos semilla)
       cercanos a la solución para asegurar convergencia, destacando la importancia
       de analizar la condición inicial.




Universidad de Ingeniería y Tecnología        Métodos Numéricos                   33 / 35
Bibliografía
      Steven C. Chapra and Raymond P. Canale.
      Métodos numéricos para ingenieros, 7a ed. McGraw-Hill, 2015.
      Richard L. Burden and J. Douglas Faires.
      Análisis numérico, 7a ed. Thompson, 2002.




Universidad de Ingeniería y Tecnología     Métodos Numéricos         34 / 35

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
