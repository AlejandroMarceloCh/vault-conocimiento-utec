---
curso: METNUM
titulo: 09 - Semana 7/Sem7_Interpolación Polinomial
slides: 40
fuente: 09 - Semana 7/Sem7_Interpolación Polinomial.pdf
---

Métodos Numéricos
Interpolación Polinomial S7
Hermes Yesser Pantoja Carhuavilca
(hpantoja@utec.edu.pe)
Jimmy Mendoza Montalvo
(jmendoza@utec.edu.pe)
Rósulo Pérez Cupe
(rperezc@utec.edu.pe)
Julio Cesar Barraza Bernaola
(jbarraza@utec.edu.pe)
Marco Antonio Cuyubamba Espinoza
(mcuyubamba@utec.edu.pe)
Ronaldo Walter Laureano Huayanay
(rlaureano@utec.edu.pe)


                                    Profesores: Utec-Ciencias
Temas

1 Interpolación Polinomial



2 Error de Interpolación



3 Actividad




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 4, 2026   1 / 39
1
    INTERPOLACIÓN
    POLINOMIAL
        Objetivos
            Construir polinomios interpolantes a partir de datos
            Estimar la cota de error del polinomio interpolante




Universidad de Ingeniería y Tecnología          Métodos Numéricos   May 4, 2026   3 / 39
Los tipos de datos en la ciencia

       Datos discretos (Tablas de datos)
              Experimentos
              Observaciones
              Cálculos
       Datos continuos
              Funciones dadas de manera explícita
              Soluciones analíticas




Universidad de Ingeniería y Tecnología       Métodos Numéricos   May 4, 2026   4 / 39
De lo continuo a lo discreto




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 4, 2026   5 / 39
De lo discreto a lo continuo ?




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 4, 2026   6 / 39
¿Qué queremos de los conjuntos de datos?
         12
                                                    Dado el conjunto de datos discretos
         10                                                           {(xi ; f (xi ))}
         8
 Eje Y
                                                    asociados a una proceso subyacente
                                                    f (x).
         6
                                                           ¿Podemos hallar dicha función f (x)?

         4                                                 ¿Podemos generar valores de f (x)
                                                           para algunas x de interés?
         2
               2       4       6     8 10 12 14
                                   Eje X
Universidad de Ingeniería y Tecnología            Métodos Numéricos                      May 4, 2026   7 / 39
Interpolación Polinomial
       Dado un conjunto de datos

                                         (x0 , y0 ), (x1 , y1 ), . . . , (xn , yn )
       buscamos una función P : I → R que satisfaga

                                         P(xi ) = yi ,           i = 0, . . . , n
       El interpolador P puede ser
              Polinomio Pn (x) (polinomio interpolante o polinomio de interpolación)
              Spline S(x) (polinomio de grado <= 3 definido a tramos)
       El intervalo I es el menor intervalo que contiene a los valores x0 , x1 , . . . , xn .




Universidad de Ingeniería y Tecnología                   Métodos Numéricos            May 4, 2026   8 / 39
Interpolación Polinomial
  Teorema
 Si x0 , x1 , . . . , xn son números reales distintos, entonces para n + 1 valores arbitrarios
 y0 , y1 , . . . , yn existe un único polinomio Pn de grado a lo sumo n tal que Pn (xi ) = yi , i =
 0, 1, . . . , n .

Pn (x) = an x n + an−1 x n−1 + . . . + a1 x + a0 ; Polinomio Interpolante.
Evaluando en x0 :
Pn (x0 ) = an x0n + an−1 x0n−1 + . . . + a1 x0 + a0 = y0
Evaluando     en los puntos restantes,    tenemos:
   x0 x0n−1 . . . x0 1
 n                                              
                                     an           y0
 x n x n−1 . . . x1 1   an−1   y1 
 1       1
                            ..   ..  =  .. 
                                                 
 ..       ..     ..
 .         .      . ··· .  .   . 
    xnn xnn−1 . . .           xn         1   a0      yn

Universidad de Ingeniería y Tecnología            Métodos Numéricos                 May 4, 2026   9 / 39
 Ejemplo
 Determine el polinomio                  de    grado    2   que    interpola   los   siguientes    puntos:
 (−2; −27), (0; −1), (1; 0)

Solución:
Polinomio Interpolante (n = 2): P2 (x) = a2 x 2 + a1 x + a0
Sistema determinado (forma algebraica):
                                               2
P2 (x0 ) = a2 x02 + a1 x0 + a0 = y0 ⇒ a2 (−2) + a1 (−2) + a0 = −27 ⇒ 4a2 − 2a1 + a0 = −27
                                             2
P2 (x1 ) = a2 x12 + a1 x1 + a0 = y1 ⇒ a2 (0) + a1 (0) + a0 = −1 ⇒ a0 = −1
                                             2
P2 (x2 ) = a2 x22 + a1 x2 + a0 = y0 ⇒ a2 (1) + a1 (1) + a0 = 0 ⇒ a2 + a1 + a0 = 0
Sistema
 2       determinado
                        (forma
                               matricial):
                                                                     
   x0 x0 1            a2         y0          4 −2 1         a2       −27
 x 2 x1 1   a1  =  y1  ⇒  0 0 1   a1  =  −1 
    1
   x22 x2 1           a0         y2          1 1 1          a0         0
Resolviendo a2 = −4, a1 = 5, a0 = −1. Por lo tanto,

                                              P2 (x) = −4x 2 + 5x − 1.

Universidad de Ingeniería y Tecnología                  Métodos Numéricos                 May 4, 2026   10 / 39
Interpolación de Lagrange
Polinomios básicos de Lagrange

               Y (x − xi )                 (x − x0 )(x − x1 ) . . . (x − xk −1 )(x − xk +1 ) . . . (x − xn )
 Lk (x) =                           =
                      (xk − xi )         (xk − x0 )(xk − x1 ) . . . (xk − xk −1 )(xk − xk +1 ) . . . (xk − xn )
               i̸=k

Propiedades
     Lk es un polinomio de grado n.
                (
                  1 si k = j
     Lk (xj ) =
                  0 si k ̸= j
Polinomio interpolante (forma de Lagrange) o Polinomio interpolante de Lagrange:
                                                                                 n
                                                                                 X
                   Pn (x) = y0 L0 (x) + y1 L1 (x) + . . . + yn Ln (x) =                 yk Lk (x).
                                                                                 k =0


Universidad de Ingeniería y Tecnología                     Métodos Numéricos                     May 4, 2026   11 / 39
 Ejemplo
 Hallar los polinomios básicos de Lagrange y el polinomio interpolante de Lagrange que
 interpola los siguientes puntos: (−2; −27), (0; −1), (1; 0)

Solución:
Polinomio Interpolante: P2 (x) = y0 L0 (x) + y1 L1 (x) + y2 L2 (x)
Polinomios básicos de Lagrange:
           (x − x1 )(x − x2 )       (x − 0)(x − 1)                   1     1
L0 (x) =                       =                        ⇒ L0 (x) = x 2 − x
          (x0 − x1 )(x0 − x2 )   ((−2) − 0)((−2) − 1)                6     6
           (x − x0 )(x − x2 )    (x − (−2))(x − 1)                 1 2 1
L1 (x) =                       =                    ⇒ L1 (x) = − x − x + 1
          (x1 − x0 )(x1 − x2 )   (0 − (−2))(0 − 1)                 2     2
           (x − x0 )(x − x1 )    (x − (−2))(x − 0)               1 2 2
L2 (x) =                       =                    ⇒ L2 (x) = x + x
          (x2 − x0 )(x2 − x1 )   (1 − (−2))(1 − 0)               3     3
Reemplazando y simplificando:
     P2 (x) = −27L0 (x) − L1 (x)                    
                      1 2 1             1 2 1
     P2 (x) = −27       x − x − − x − x +1
                      6        6        2      2
     P2 (x) = −4x 2 + 5x − 1
Universidad de Ingeniería y Tecnología      Métodos Numéricos              May 4, 2026   12 / 39
Ejercicio
 Ejercicio
 Dado los siguientes puntos:

                                         x   0   0.8       2
                                         y   1   0.4      0.2

 hallar los polinomios básicos de Lagrange y el polinomio interpolante de Lagrange.




Universidad de Ingeniería y Tecnología           Métodos Numéricos   May 4, 2026   13 / 39
Diferencias Divididas
  Definición
 La diferencia dividida de primer orden de f con respecto a xi , xi+1 es denotada
 por f [xi , xi+1 ] y es definida:

                                                              f (xi+1 ) − f (xi )
                                           f [xi , xi+1 ] =
                                                                  xi+1 − xi

  Definición
 La diferencia dividida de segundo orden de f con respecto a xi , xi+1 , xi+2 es
 denotada por f [xi , xi+1 , xi+2 ] y es definida:

                                                            f [xi+1 , xi+2 ] − f [xi , xi+1 ]
                                  f [xi , xi+1 , xi+2 ] =
                                                                       xi+2 − xi

Universidad de Ingeniería y Tecnología                        Métodos Numéricos                 May 4, 2026   14 / 39
Diferencias Divididas
  Definición
 Si se tienen las (k − 1)-ésima diferencias divididas f [xi , . . . , xi+k −1 ] y
 f [xi+1 , . . . , xi+k ] entonces la diferencia dividida de orden k de f con respecto a
 xi , . . . , xi+k es denotada por f [xi , . . . , xi+k ] y es definida:

                                                     f [xi+1 , . . . , xi+k ] − f [xi , . . . , xi+k −1 ]
                          f [xi , . . . , xi+k ] =
                                                                         xi+k − xi




Universidad de Ingeniería y Tecnología                          Métodos Numéricos                           May 4, 2026   15 / 39
Tabla de Diferencias Divididas
Las diferencias divididas son calculadas en una tabla:



   xi                f (xi )                 [, ]                 [, , ]             [, , , ]
   x0                f [x0 ]             f [x0 , x1 ]          f [x0 , x1 , x2 ]   f [x0 , x1 , x2 , x3 ]
   x1                f [x1 ]             f [x1 , x2 ]          f [x1 , x2 , x3 ]
   x2                f [x2 ]             f [x2 , x3 ]
   x3                f [x3 ]



Universidad de Ingeniería y Tecnología                  Métodos Numéricos             May 4, 2026     16 / 39
 Ejemplo
 Calcule las diferencias divididas con la siguiente data:

                                         x      y         y[ , ]     y[ , , ]
                                         −2    −27
                                         0     −1
                                         1      0

Solución:
Diferencia divididas de primer orden:
                 y1 − y0       (−1) − (−27)
y [x0 , x1 ] =             =                      ⇒ y [x0 , x1 ] = 13
                 x1 − x0          0 − (−2)
                 y2 − y1       0 − (−1)
y [x1 , x2 ] =             =                ⇒ y[x1 , x2 ] = 1
                 x2 − x1         1−0
Diferencia divididas de segundo orden:
                    y [x1 , x2 ] − y [x0 , x1 ]    1 − 13
y [x0 , x1 , x2 ] =                             =             ⇒ y [x0 , x1 , x2 ] = −4
                             x2 − x0              1 − (−2)

Universidad de Ingeniería y Tecnología                  Métodos Numéricos                May 4, 2026   17 / 39
 Ejemplo
 Calcule las diferencias divididas con la siguiente data:

                                         x        y       y[ , ]   y[ , , ]
                                         −2      −27       13        -4
                                          0      −1         1
                                          1       0

Solución:
Diferencia divididas de primer orden:
                 y1 − y0       (−1) − (−27)
y [x0 , x1 ] =             =                      ⇒ y [x0 , x1 ] = 13
                 x1 − x0          0 − (−2)
                 y2 − y1       0 − (−1)
y [x1 , x2 ] =             =                ⇒ y [x1 , x2 ] = 1
                 x2 − x1         1−0
Diferencia divididas de segundo orden:
                    y [x1 , x2 ] − y [x0 , x1 ]    1 − 13
y [x0 , x1 , x2 ] =                             =             ⇒ y [x0 , x1 , x2 ] = −4
                             x2 − x0              1 − (−2)

Universidad de Ingeniería y Tecnología                  Métodos Numéricos                May 4, 2026   18 / 39
Ejercicio
 Ejercicio
 Calcule las diferencias divididas con la siguiente data:

                                     x   f (x)   f[, ]        f[, , ]        f[, , , ]
                                     0      1
                                     1      4
                                     2      7
                                     4    19




Universidad de Ingeniería y Tecnología                   Métodos Numéricos               May 4, 2026   19 / 39

Interpolación Polinomial fórmula de Newton
Si queremos escribir el polinomio interpolante de la forma:

Pn (x) = b0 + b1 (x − x0 ) + b2 (x − x0 )(x − x1 ) + . . . + bn (x − x0 )(x − x1 ) . . . (x − xn−1 )

Se observa que:

                            f (x1 ) − f (x0 )
b0 = f (x0 ), b1 =                            = f [x0 , x1 ], . . . , bk = f [x0 , x1 , . . . , xk ],    k = 0, 1, . . . , n
                                x1 − x 0

El polinomio interpolante (forma de Newton) o polinomio interpolante de Newton:
                                         n
                                         X
                Pn (x) = f [x0 ] +              f [x0 , . . . , xk ](x − x0 )(x − x1 ) . . . (x − xk −1 )
                                         k =1




Universidad de Ingeniería y Tecnología                        Métodos Numéricos                         May 4, 2026   20 / 39
 Ejemplo
 Determine el polinomio de grado 2 que interpola los siguientes puntos:
 (−2; −27), (0; −1), (1; 0)

Solución:
Calculamos la tabla de diferencias divididas:

                                         x     y     y[ , ]    y[ , , ]
                                         −2   −27     13         -4
                                          0   −1       1
                                          1    0

Luego, el polinomio interpolante:
    P2 (x) = y0 + y [x0 , x1 ](x − x0 ) + y [x0 , x1 , x2 ](x − x0 )(x − x1 )
    P2 (x) = −27 + 13(x − (−2)) − 4(x − (−2))(x − 0)
    P2 (x) = −4x 2 + 5x − 1
Universidad de Ingeniería y Tecnología              Métodos Numéricos           May 4, 2026   21 / 39
 Ejercicio
 Dado los siguientes puntos

                                         x   0   0.8       2
                                         y   1   0.4      0.2

 halle el polinomio interpolante mediante la fórmula de Newton.




Universidad de Ingeniería y Tecnología           Métodos Numéricos   May 4, 2026   22 / 39
    ERROR DE

2   INTERPOLACIÓN
Error de Interpolación

  Definición
 El error de reemplazar la función f (x) por el polinomio Pn (x) es

                                         En (x, f ) = f (x) − Pn (x)


       El error varía de un punto a otro punto. En los puntos de interpolación el error
       es cero pero es diferente de cero en los otros puntos.
       Estaremos más interesados en el máximo del error absoluto |En (x, f )| sobre el
       intervalo [a, b]. Este máximo es llamado Cota del error.




Universidad de Ingeniería y Tecnología               Métodos Numéricos   May 4, 2026   24 / 39
Error de Interpolación Polinomial
  Teorema
 Supongamos que x0 , x1 , . . . , xn son n + 1 puntos distintos en el intervalo [a, b] y
 f (x) tiene n + 1 derivadas continuas. Entonces, para cada x en [a, b], un número
 ξ (x) en ⟨a, b⟩ existe con
                                                   f (n+1) (ξ (x))
                            f (x) = Pn (x) +                       (x − x0 ) . . . (x − xn )
                                                      (n + 1)!

 donde Pn (x) es el polinomio interpolante de Newton de grado <= n. De esta
 manera, el error es dado por la fórmula

                                                f (n+1) (ξ (x))
                                 En (x, f ) =                   (x − x0 ) . . . (x − xn )
                                                   (n + 1)!


Universidad de Ingeniería y Tecnología                     Métodos Numéricos                   May 4, 2026   25 / 39
Error de Interpolación
Nota:
       Si el intervalo [a, b] no es dado, considere [a, b] el intervalo más pequeño que
       contiene a los puntos x1 , x2 , . . . , xn .
       Necesitamos la función f (x) para calcular la cota de error.




Universidad de Ingeniería y Tecnología     Métodos Numéricos             May 4, 2026   26 / 39
Continuación...

 Ejemplo
 Para la función f (x) = cos(x), sea x0 = 0, x1 = 0.6 x2 = 0.9
        Halle el polinomio interpolante para aproximar f (0.45).
        Encuentre el error absoluto en 0.45.
        Utilizando el teorema encuentre la cota de error.




Universidad de Ingeniería y Tecnología     Métodos Numéricos       May 4, 2026   27 / 39
Solución
       Aproximación P(0.45) = 0.898100747
       Error (exacto) en x = 0.45:
       cos(45) − P(0.45) = 0.9004471024 − 0.898100747 ≈ 0.0023
       Cota de error
                                 f ′′′ (ξ (x))
                                               x(x − 0.6)(x − 0.9)
                                         E2 (x, f ) =
                                        3!
       Queremos calcular max |E2 (x, f )|
                                         x∈[0;0,9]
       Acotaremos el error en dos pasos:
              Encontrar
                                                                  max |f ′′′ (x)|
                                                                 x∈[0;0,9]

              Encontrar
                                                        max |x(x − 0.6)(x − 0.9)|
                                                     x∈[0;0.9]



Universidad de Ingeniería y Tecnología                            Métodos Numéricos   May 4, 2026   28 / 39
Solución
Calculando
                                                max |f ′′′ (x)|
                                              x∈[0;0.9]


       Calculando las derivadas
         f (x) = cos(x)
         f ′ (x) = − sin(x)
         f ′′ (x) = − cos(x)
         f ′′′ (x) = sin(x)
       | sin(x)| es creciente en el intervalo [0; 0.9]. Luego

                                          max | sin(x)| ≤ | sin(0.9)|
                                         x∈[0;0.9]




Universidad de Ingeniería y Tecnología               Métodos Numéricos   May 4, 2026   29 / 39
Solución
                   m1                                           Calculando:
    0.057
                                                                                 max |x(x − 0.6)(x − 0.9)|
      0.05                                                                   x∈[0;0.9]

                                                                      Extremos locales
      0.04
                                                                      g(x) = x(x − 0.6)(x − 0.9)
                                                                      g ′ (x) = 3(x 2 − x + 0.18) = 0
      0.03
                                                                      m1 = 0.2354248689
     0.02                                       m2                    m2 = 0.7645751311
    0.017                                                             |g(m2 )| = 0.0170405184
      0.01                                                            |g(x)| ≤ |g(m1 )| = 0.05704
                                                         x
          0
              0      0.2      0.4        0.6   0.8 0.9


Universidad de Ingeniería y Tecnología                       Métodos Numéricos                  May 4, 2026   30 / 39
Solución
Colocamos junto las dos estimaciones

                                                 | sin(ξ (x))|
                               |E2 (x, f )| =                  |x(x − 0.6)(x − 0.9)|
                                                       6

                                                          | sin(0, 9)|
                                         |E2 (x, f )| ≤                × 0.05704
                                                               6

                                               |E2 (x, f )| ≤ 0.0074468




Universidad de Ingeniería y Tecnología                       Métodos Numéricos         May 4, 2026   31 / 39
Estimación del error cuando f (x) es desconocida:
Regla del Término Siguiente
       Frecuentemente f (x) no es conocida, y la enésima derivada de f (x) es
       también desconocida.
       Se puede probar que la n-ésima diferencia dividida es una estimación de la
       n-ésima derivada de f :

                                              f (n+1) (ξ (x))
                                                              = f [x0 , . . . , xn ]
                                                 (n + 1)!

       De esta manera, reemplazando en la fórmula de error se tiene:
                                En (x, f ) = f [x0 , . . . , xn , xn+1 ](x − x0 ) . . . (x − xn )




Universidad de Ingeniería y Tecnología                      Métodos Numéricos                       May 4, 2026   32 / 39
Ejemplo
 Ejemplo
 Para la función
                                                        x
                                         f (x) = x 2 e− 2


        Construir la tabla de las diferencias divididas para los puntos
        x0 = 1.1; x1 = 2; x2 = 3.5; x3 = 5; x4 = 7.1
        Encontrar el polinomio interpolante de Newton de grado 1 utilizando
        diferencias divididas para aproximar al valor de f (x) en x = 1.75.
        Use la regla del término siguiente para estimar el error de la interpolación
        para f (1.75).




Universidad de Ingeniería y Tecnología         Métodos Numéricos          May 4, 2026   33 / 39
Solución
       La tabla de diferencias divididas es:

                                          x     f (x)       f [, ]       f [, , ]
                                         1.1   0.6981     0.8593        −0.1755
                                          2    1.4715     0.4381
                                         3.5   2.1287

       P1 (x) = 0.6981 + 0.8593(x − 1.1)
       P2 (x) = 0.6981 + 0.8593(x − 1.1) −0.1755(x − 1.1)(x − 2)
       De la regla del término siguiente obtenemos:

                         E1 (1.75; f ) = −0.1755(1.75 − 1.1)(1.75 − 2) = 0.02852




Universidad de Ingeniería y Tecnología                  Métodos Numéricos           May 4, 2026   34 / 39
3   ACTIVIDAD
Actividad: Estimación mediante Interpolación de
Lagrange
En el control de calidad de una planta de producción, se desea estimar el
comportamiento de una variable de proceso en momentos específicos del día para
los cuales no se tienen mediciones directas. Se cuenta con los siguientes datos
recogidos durante un día particular:

                                         Hora (h)   Variable de proceso (y)
                                            6                 152
                                            9                 185
                                           11                 210
                                           16                 280
                                           18                 310




Universidad de Ingeniería y Tecnología                  Métodos Numéricos     May 4, 2026   36 / 39
Continuación...
Desarrolla las siguientes tareas:
   1   Construye el polinomio interpolante de Lagrange utilizando los datos de la
       tabla. Puedes utilizar los cinco puntos dados o seleccionar un subconjunto
       adecuado para mejorar la precisión local.
   2   Estima el valor de la variable de proceso a las 10 horas y a las 15 horas
       evaluando el polinomio obtenido.
   3   Utiliza un asistente de IA para solicitar una guía paso a paso sobre cómo
       construir el polinomio de Lagrange. Pregunta también por posibles dificultades
       o errores comunes en su aplicación. Reflexiona: ¿en qué aspectos te ayudó la
       IA y qué limitaciones encontraste al usarla?
   4   Compara brevemente la interpolación de Lagrange con otro método de
       estimación (por ejemplo, interpolación lineal o ajuste por mínimos cuadrados).
       ¿Cuál crees que sería más conveniente en un entorno de producción real?
       Justifica tu respuesta.
Universidad de Ingeniería y Tecnología    Métodos Numéricos             May 4, 2026   37 / 39
Conclusiones




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 4, 2026   38 / 39
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
