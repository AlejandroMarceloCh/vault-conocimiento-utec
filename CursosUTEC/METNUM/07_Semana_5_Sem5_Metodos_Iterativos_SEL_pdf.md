---
curso: METNUM
titulo: 07 - Semana 5/Sem5_Metodos Iterativos SEL
slides: 60
fuente: 07 - Semana 5/Sem5_Metodos Iterativos SEL.pdf
---

Métodos Numéricos
Métodos Iterativos SEL - S5
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
                                         1 Método de Jacobi
                                         2 Método de Gauss-Seidel
                                         3 Convergencia




Universidad de Ingeniería y Tecnología   Métodos Numéricos          1 / 59
        Objetivos
            Aplica los métodos iterativos para la resolución de ecuaciones lineales.
            Identifica la convergencia de cada método iterativo.
            Calcula el error cometido al aplicar cada método.




Universidad de Ingeniería y Tecnología              Métodos Numéricos                  2 / 59
Introducción
En este capítulo trataremos con un SEL de la forma
                                         Ax = b
con A de orden n × n y de solución única. A continuación algunas razones del por
que se prefiere la solución iterativa en lugar de los métodos directos:
    Los métodos directos amplifican los errores numéricos durante las
    operaciones. Los métodos iterativos, al trabajar con aproximaciones sucesivas,
    tienden a controlar mejor estos errores.
    Los sistemas de gran tamaño, que surgen en problemas de ingeniería,
    dinámica de fluidos o la simulación de estructuras, generan matrices
    esparcidas.
    Los métodos directos suelen ser muy costosos computacionalmente debido a
    la complejidad de las operaciones con matrices grandes y densas. En cambio
    los iterativos trabajan con matrices esparsas

Universidad de Ingeniería y Tecnología        Métodos Numéricos               3 / 59
Introducción
Métodos iterativos básicos para resolver sistemas de ecuaciones lineales:

  Métodos Iterativos para resolver Ax = b
 Un método iterativo básico para resolver sistemas de ecuaciones lineales
 comienza con una aproximación x (0) y genera una sucesión de vectores que
 bajo condiciones de convergencia son soluciones aproximadas del sistema:

                                         {x (k ) },    k = 0, 1, 2, . . .

 tal que si converge, lo hace a la solución x del sistema Ax = b, esto es:

                                                 lim x (k ) = x.
                                                k →∞




Universidad de Ingeniería y Tecnología                      Métodos Numéricos   4 / 59
Esquema Iterativo (Punto Fijo para SEL)
       Transforma el sistema lineal Ax = b en la forma:

                                                         x = Tx + c

       donde T es una matriz fija de n × n y c un vector de dimensión n.
       La sucesión de aproximaciones se genera definiendo el esquema iterativo:

                                         x (k +1) = Tx (k ) + c, para k = 0, 1, 2, . . .


       El esquema iterativo requiere una aproximación inicial: x (0) .
       ¿Por qué no aplicar Newton-Raphson en este caso?


Universidad de Ingeniería y Tecnología                          Métodos Numéricos          5 / 59
1   MÉTODO DE
    JACOBI
Iteración de Jacobi
Dado un sistema de n ecuaciones lineales con n incógnitas de la forma:
                   
                   
                     a11 x1 + a12 x2 + . . . + a1n xn = b1
                    a21 x1 + a22 x2 + . . . + a2n xn = b2
                   
                       ..                           ..    ..
                   
                   
                       .                            .     .
                      an1 x1 + an2 x2 + . . . + ann xn = bn
                   

Si logramos despejar:
                                    1
                                       (b1 − a12 x2 − a13 x3 − · · · − a1n xn )
                                         x1 =
                                   a11
                                    1
                          x2 =         (b2 − a21 x1 − a23 x3 − · · · − a2n xn )
                                   a22
                             ..                     ..                     ..
                              .                      .                      .
                                 1
                        xn =        (bn − an1 x1 − an2 x2 − · · · − ann−1 xn−1 )
                                ann
entonces podemos definir un proceso iterativo:
Universidad de Ingeniería y Tecnología                   Métodos Numéricos         7 / 59
Forma algebraica del método de Jacobi
 (k +1)      1             
                           (k )     (k )             (k )
x1        =      b1 − a12 x2 − a13 x3 − · · · − a1n xn
            a11
   (k +1)    1            (k )     (k )             (k )
                                                          
x2        =      b2 − a21 x1 − a23 x3 − · · · − a2n xn
            a22
..                   ..                  ..
 .                    .                   .
                                                                               (0)
                                                                                                
                                                                              x1
                                                                             (0) 
 (k +1)    1            (k )     (k )               (k )
                                                          
                                                                        (0)
                                                                             x2 
xn      =      bn − an1 x1 − an2 x2 − · · · − ann−1 xn−1 , con semilla x =  .. 
                                                                                   
          ann                                                                . 
                                                                                                      (0)
                                                                                                     xn
En general:
                                                       
                                         n
       (k +1)       1                   X          (k ) 
     xi         =       bi −                   aij xj        , para i = 1, 2, . . . , n siempre que aii ̸= 0
                    aii
                                    j=1,j̸=i



Universidad de Ingeniería y Tecnología                               Métodos Numéricos                         8 / 59
Forma matricial del método de Jacobi
Sea el sistema Ax = b, donde
                                                                          
                                              a11     a12    ...       a1n
                                            a21      a22    ...       a2n 
                                          A= .                         ..  .
                                                                          
                                                       ..    ..
                                             ..        .       .        . 
                                               an1    an2    ...       ann
Consideremos la siguiente descomposición de A:
                                       
      a11             0      ...     0        
                                                0       0       ...      0
                                                                                   
                                                                                     0 −a12   ...    −a1n
                                                                                                          
                            ..      ..      −a21     0       ...      0         0   0    ...    −a2n 
      0            a22         .     . 
                                        
   D=                                  ,L =                           ..  , U =  ..
                                                                                                       
      .             ..                          .      ..      ..                       ..   ..      .. 
      ..                    ..
                                .              ..       .         .      .        .    .      .     . 
                      .              0 
              0      ...      0     ann        −an1   −an2      ...      0           0   0    ...     0

De tal forma que:
                                               A=D−L−U

Universidad de Ingeniería y Tecnología                       Métodos Numéricos                            9 / 59
Forma matricial del método de Jacobi (ejemplo)
Sea el sistema Ax = b, donde
                                                              
                        −6 2 1 1                            −90
                       −4 8 −3 2                         −150 
                  A=  1 2 5 0 
                                                       b=
                                                           300  .
                                                                 

                        −1 3 1 8                            210

entonces la matriz A se descompone de la siguiente manera:
                                                                 
       −6 0 0 0                 0   0     0 0              0 −2 −1 −1
      0 8 0 0               4    0     0 0           0 0    3 −2 
 D=  0 0 5 0  L =  −1 −2 0 0  U =  0 0
                                                                  
                                                                 0  0 
        0 0 0 8                 1 −3 −1 0                  0 0   0  0

De tal forma que:
                                         D − L − U = A.
Universidad de Ingeniería y Tecnología            Métodos Numéricos   10 / 59
Continuación...
Sustituyendo esta partición de A en el sistema Ax = b queda

                                                 (D − L − U)x = b


                                                 Dx = (L + U)x + b

                                             x = D −1 (L + U)x + D −1 b
Entonces queda definido el método iterativo:

                                         x (k +1) = D −1 (L + U)x (k ) + D −1 b

donde Tj = D −1 (L + U), es la Matriz de Iteración de Jacobi y cj = D −1 b es el
vector de Jacobi.


Universidad de Ingeniería y Tecnología                        Métodos Numéricos   11 / 59
Universidad de Ingeniería y Tecnología   Métodos Numéricos   12 / 59
Ejemplo 1
Dado el sistema de ecuaciones lineales:
                    
                    
                      −6x1 + 2x2 + x3 + x4                                 =     −90
                       −4x1 + 8x2 − 3x3 + 2x4                               =     −150
                    
                       x + 2x2 + 5x3                                        =     300
                     1
                    
                    
                       −x1 + 3x2 + x3 + 8x4                                 =     210

   1   Despeje la componente xi de la ecuación i, para i = 1, 2, 3, 4.
   2   Defina el método iterativo:
                                                     
                                         4
                     (k +1)   1         X       (k )
                   xi       =       bi −   aij xj  , para i = 1, 2, 3, 4
                              aii
                                                      j=1,j̸=i

                 (0)               (0)        (0)            (0)
   3   Sea x1 = 20; x2                   = 5 x3     = 30; x4       = 10 calcule dos iteraciones del
       método.

Universidad de Ingeniería y Tecnología                             Métodos Numéricos                  13 / 59
                                   
                                   
                                    −6x1 + 2x2 + x3 + x4      =     −90
                                     −4x1 + 8x2 − 3x3 + 2x4    =     −150
                                   
                                     x + 2x2 + 5x3             =     300
                                    1
                                   
                                   
                                     −x1 + 3x2 + x3 + 8x4      =     210
Al despejar xi de la i ésima ecuación se obtiene:
            FORMA ALGEBRAICA                                              FORMA MATRICIAL
                90        2     1    1
 x1 =              + 0x1 + x2 + x3 + x4
                 6        6     6    6
               −150 4             3    2
 x2 =               + x1 + 0x2 + x3 − x4
                 8     8          8    8
                300 1      2         0
 x3 =              − x1 − x2 + 0x3 + x4
                 5    5    5         5
                210 1      3     1
 x4 =              + x1 − x2 − x3 + 0x4
                 8    8    8     8
Universidad de Ingeniería y Tecnología                Métodos Numéricos                     14 / 59
Continuación...
       Entonces de define el proceso iterativo:

                               (k +1)            90      (k ) 2 (k ) 1 (k ) 1 (k )
                             x1          =          + 0x1 + x2 + x3 + x4
                                                 6            6        6        6
                               (k +1)          −150 4 (k )        (k )   3 (k ) 2 (k )
                             x2          =           + x1 + 0x2 + x3 − x4
                                                 8      8                8        8
                               (k +1)           300 1 (k ) 2 (k )          (k ) 0 (k )
                             x3          =          − x1 − x2 + 0x3 + x4
                                                 5     5       5                5
                               (k +1)           210 1 (k ) 3 (k ) 1 (k )            (k )
                             x4          =          + x1 − x2 − x3 + 0x4
                                                 8     8       8        8
                                         (0)               (0)                     (0)               (0)
       Iniciando en el punto x1                = 20   ;   x2     =5      ;    x3         = 30   ;   x4     = 10



Universidad de Ingeniería y Tecnología                         Métodos Numéricos                                  15 / 59
Continuación...
k =0

                   (1)             90       (0) 2 (0)    1 (0)   1 (0)
                 x1        =          + 0(x1 ) + (x2 ) + (x3 ) + (x4 )     =
                                   6            6        6       6
                   (1)           −150 4 (0)         (0)    3 (0)   2 (0)
                 x2        =           + (x1 ) + 0(x2 ) + (x3 ) − (x4 )    =
                                   8      8                8       8
                   (1)            300 1 (0)      2 (0)       (0)  0 (0)
                 x3        =          − (x1 ) − (x2 ) + 0(x3 ) + (x4 )     =
                                   5     5       5                5
                   (1)            210 1 (0)      3 (0)    1 (0)      (0)
                 x4        =          + (x1 ) − (x2 ) − (x3 ) + 0(x4 )     =
                                   8     8       8        8




Universidad de Ingeniería y Tecnología              Métodos Numéricos          16 / 59
Continuación...
k =0

                  (1)             90          2      1      1
                x1        =          + 0(20) + (5) + (30) + (10)        = 23.333
                                   6          6      6      6
                  (1)            −150 4                3      2
                x2        =           + (20) + 0(5) + (30) − (10)       =   0.000
                                   8     8             8      8
                  (1)            300 1         2             0
                x3        =          − (20) − (5) + 0(30) + (10)        = 54.000
                                   5    5      5             5
                  (1)            210 1         3      1
                x4        =          + (20) − (5) − (30) + 0(10)        = 23.125
                                   8    8      8      8




Universidad de Ingeniería y Tecnología              Métodos Numéricos               17 / 59
Continuación...
k =1

                 (2)90                     2          1              1
              x1       + 0(
                        =                )+ (      )+ (           )+ (          )    =
                     6                     6          6              6
          (2)     −150 4                                3              2
         x2   =         + (               ) + 0(    )+ (           )− (             ) =
                     8     8                            8              8
          (2)      300 1                   2                          0
         x3   =        − (               )− (       ) + 0(        )+ (          )    =
                     5    5                5                          5
          (2)      210 1                   3          1
         x4   =        + (               )− (       )− (               ) + 0(   )    =
                     8    8                8          8
asi sucesivamente.
k =2
k =3


Universidad de Ingeniería y Tecnología             Métodos Numéricos                      18 / 59
 Observación:
 El proceso iterativo anterior, puede ser expresado en su forma matricial:

                                     x = Tj x + cj =⇒ x (k +1) = Tj x (k ) + cj

Es decir:
                                           2      1        1                  90
                                                                              
                    0
                                                                      
        (k +1)                                                      (k )
      x                                    6      6        6     x            6
     1                                                        1  
                                                                               
                                                                               
     (k +1)   4
                                               3         2   (k )   −150 
                                                                        
     x2                                   0              −  x                 
                 8                              8         8  2           8
                                                                             
               =                                                       +
                                                                                
                                                                              
     (k +1)   1
     x3                                    2              0   (k )   300 
                                                                        
                 −                      −      0                x
                                                                 3  
                                                                                 
                5                        5              5                  5 
                                                                          
        (k +1)   
                    1                       3     1
                                                                   (k )   
                                                                             210
                                                                                 
      x4                                  −     −          0      x4
                 | 8                        8 {z 8            }            |   8
                                                                              {z }
                                         Tj =D −1 (L+U)                           cj =D −1 b
Universidad de Ingeniería y Tecnología                        Métodos Numéricos                19 / 59

2   MÉTODO DE
    GAUSS-SEIDEL
Método de Gauss Seidel
El método de Jacobi halla las componentes de x (k +1) usando solo las componentes de x (k ) :
                                                                           
                                                        n
                                (k +1)                                 (k ) 
                                                        X
               Jacobi: xi                = bi −                  aij xj        /aii , para i = 1, 2, . . . , n
                                                       j=1,j̸=i
                                                                                            
                                                  i−1                      n
                                                                (k )                    (k ) 
                                                  X                        X
                                     = bi −             aij xj        −           aij xj        /aii , para i = 1, 2, . . . , n
                                                  j=1                      j=i+1
                                             (k +1)                                                                         (k +1)
Sin embargo, para obtener xi                          , se podrían haber usado las componentes x1                                    ,
 (k +1)        (k +1)
x2      hasta xi−1 (porque ellas ya han sido calculadas):
                                                                                              
                                                 i−1                        n
                           (k +1)                           (k +1)                          (k ) 
                                                 X                          X
Gauss-Seidel: xi                    = bi −            aij xj          −            aij xj           /aii , para i = 1, 2, . . . , n
                                                 j=1                        j=i+1

siempre que aii ̸= 0.
Universidad de Ingeniería y Tecnología                                 Métodos Numéricos                                      21 / 59
Forma algebraica del método de Gauss-Seidel
                                                            
  (k +1)                    (k )       (k )             (k )
x1        = a111 b1 − a12 x2 − a13 x3 − · · · − a1n xn
                                                              
   (k +1)                 (k +1)         (k )             (k )
x2        = a122 b2 −a21 x1      − a23 x3 − · · · − a2n xn
..
 .
                                                                                      (0)
                                                                                         
                                                                                     x1
                                                                                    (0) 
  (k +1)
                 
                           (k +1)        (k +1)                  (k +1)
                                                                                   x2 
xn         = a1nn bn −an1 x1      − an2 x2      − · · · − ann−1 xn−1      ,    (0)
                                                                              x =  .. 
                                                                                          
                                                                                    . 
                                                                                      (0)
                                                                                     xn
siempre que aii ̸= 0.




Universidad de Ingeniería y Tecnología                Métodos Numéricos                   22 / 59
Ejemplo 2
Dado el sistema de ecuaciones lineales:
                    
                    
                      −6x1 + 2x2 + x3 + x4                               =     −90
                       −4x1 + 8x2 − 3x3 + 2x4                             =     −150
                    
                       x + 2x2 + 5x3                                      =     300
                     1
                    
                    
                       −x1 + 3x2 + x3 + 8x4                               =     210

   1   Despeje la componente xi de la ecuación i, para i = 1, 2, 3, 4.
   2   Defina el método iterativo:
                                                                
                                 i−1                4
              (k +1)   1        X         (k +1)
                                                    X       (k )
            xi       =      bi −     aij xj       −   aij xj  , para i = 1, 2, . . . , 4
                       aii
                                            j=1                j=i+1

                 (0)               (0)        (0)          (0)
   3   Sea x1 = 20; x2                   = 5 x3     = 30; x4     = 10, calcule dos iteraciones del
       método.

Universidad de Ingeniería y Tecnología                           Métodos Numéricos                   23 / 59
                                   
                                   
                                    −6x1 + 2x2 + x3 + x4      =     −90
                                     −4x1 + 8x2 − 3x3 + 2x4    =     −150
                                   
                                     x + 2x2 + 5x3             =     300
                                    1
                                   
                                   
                                     −x1 + 3x2 + x3 + 8x4      =     210
Al despejar xi de la i ésima ecuación se obtiene:

                                           90        2     1    1
                                  x1 =        + 0x1 + x2 + x3 + x4
                                            6        6     6    6
                                          −150 4             3    2
                                  x2 =         + x1 + 0x2 + x3 − x4
                                            8     8          8    8
                                           300 1      2         0
                                  x3 =        − x1 − x2 + 0x3 + x4
                                            5    5    5         5
                                           210 1      3     1
                                  x4 =        + x1 − x2 − x3 + 0x4
                                            8    8    8     8

Universidad de Ingeniería y Tecnología                Métodos Numéricos     24 / 59
Continuación...
       Entonces de define el proceso iterativo:

                           (k +1)                90      (k )   2 (k ) 1 (k ) 1 (k )
                         x1              =          + 0x1 + x2 + x3 + x4
                                                 6              6          6         6
                           (k +1)             −150 4 (k +1)           (k )   3 (k ) 2 (k )
                         x2              =           + x1        + 0x2 + x3 − x4
                                                8      8                     8         8
                           (k +1)             300 1 (k +1) 2 (k +1)             (k )   0 (k )
                         x3              =        − x1         − x2         + 0x3 + x4
                                               5     5           5                     5
                           (k +1)            210 1 (k +1) 3 (k +1) 1 (k +1)                (k )
                         x4              =       + x1         − x2         − x3        + 0x4
                                              8     8           8            8
                                             (0)               (0)                     (0)               (0)
       Iniciando en el punto x1                    = 20   ;   x2     =5      ;    x3         = 30   ;   x4     = 10



Universidad de Ingeniería y Tecnología                             Métodos Numéricos                                  25 / 59
Continuación...
k =0

                   (1)             90       (0) 2 (0)    1 (0)   1 (0)
                 x1        =          + 0(x1 ) + (x2 ) + (x3 ) + (x4 )     =
                                   6            6        6       6
                   (1)           −150 4 (1)         (0)    3 (0)   2 (0)
                 x2        =           + (x1 ) + 0(x2 ) + (x3 ) − (x4 )    =
                                   8      8                8       8
                   (1)            300 1 (1)      2 (1)       (0)  0 (0)
                 x3        =          − (x1 ) − (x2 ) + 0(x3 ) + (x4 )     =
                                   5     5       5                5
                   (1)            210 1 (1)      3 (1)    1 (1)      (0)
                 x4        =          + (x1 ) − (x2 ) − (x3 ) + 0(x4 )     =
                                   8     8       8        8




Universidad de Ingeniería y Tecnología              Métodos Numéricos          26 / 59
Continuación...
k =0


         (1)           90          2       1      1
       x1       =         + 0(20) + (5) + (30) + (10)                = 23.333
                       6           6       6      6
         (1)           −150 4                   3       2
       x2       =            + (23.333) + 0(5) + (30) − (10)         =   1.666
                         8     8                8       8
         (1)           300 1             2                0
       x3       =          − (23.333) − (1.666) + 0(30) + (10)       = 54.666
                        5    5           5                5
         (1)           210 1             3          1
       x4       =          + (23.333) − (1.666) − (54.666) + 0(10)   = 21.708
                        8    8           8          8




Universidad de Ingeniería y Tecnología         Métodos Numéricos                 27 / 59
Continuación...
k =1

                 (2)90                     2          1              1
              x1       + 0(
                        =                )+ (      )+ (           )+ (          )    =
                     6                     6          6              6
          (2)     −150 4                                3              2
         x2   =         + (               ) + 0(    )+ (           )− (             ) =
                     8     8                            8              8
          (2)      300 1                   2                          0
         x3   =        − (               )− (       ) + 0(        )+ (          )    =
                     5    5                5                          5
          (2)      210 1                   3          1
         x4   =        + (               )− (       )− (               ) + 0(   )    =
                     8    8                8          8
asi sucesivamente.
k =2
k =3


Universidad de Ingeniería y Tecnología             Métodos Numéricos                      28 / 59
Forma matricial del método de Gauss-Seidel
Sea el sistema Ax = b, donde
                                                                           
                                             a11       a12    ...       a1n
                                           a21        a22    ...       a2n 
                                         A= .                           ..  .
                                                                           
                                                        ..    ..
                                            ..          .       .        . 
                                                 an1   an2    ...       ann

Consideremos la siguiente partición de A:
                                      
    a11             0      ...      0        
                                               0         0       ...      0
                                                                                    
                                                                                       0    −a12   ...    −a1n
                                                                                                               
                          ..       ..      −a21       0       ...      0         0      0     ...    −a2n 
    0             a22        .      . 
 D=                                   ,L =  .                          ..  , U =  ..
                                                                                                            
    .              ..                                   ..      ..                          ..    ..      .. 
    ..                    ..
                              .
                                             ..         .         .      .        .       .       .     . 
                     .              0 
            0      ...      0      ann        −an1     −an2      ...      0            0     0     ...     0

De tal forma que:
                                              A = D − L − U.
Universidad de Ingeniería y Tecnología                        Métodos Numéricos                                29 / 59
Sustituyendo esta partición de A en Ax = b queda

                                               (D − L − U)x = b


                                              (D − L)x = Ux + b


                                         x = (D − L)−1 Ux + (D − L)−1 b
Se define el método iterativo como:

                                    x (k +1) = (D − L)−1 Ux (k ) + (D − L)−1 b

donde Tgs = (D − L)−1 U, es la Matriz de Iteración de Gauss-Seidel y
cgs = (D − L)−1 b es el vector de Gauss-Seidel.



Universidad de Ingeniería y Tecnología                     Métodos Numéricos     30 / 59
Ejemplo 3
En el caso del método de Gauss Seidel la matriz de iteración se calcula mediante
Tgs = (D − L)−1 U y el vector mediante cgs = (D − L)−1 b, es decir (para el mismo
sistema planteado en el método anterior)

                              1       1      1
                                               
                                                                    15
                                                                        
                         0
                                                         
            (k +1)                                     (k )
          x                   3       6      6      x
         1                                      1 
                                                                       
                                                              45 
                           1      11       1           
         (k +1)   0                             (k )       −
                                                                        
         x2                                −    x2              4
                                                                         
                              6      24       6 
                                                                      
                   =                                      + 
                                                                    
                                                                   123 
                                               
         (k +1)  
         x3         0 −      2     13     1    (k ) 
                                                  x3 
                                    −
                                                                        
                                                                2 
        
        
                    
                             15     60    30  
                                                          
                                                                       
                                                                   789
                                                                        
            (k +1)    
                                1    119 19
                                                      (k )
          x4             0 −       −                 x4
                      |       240 {z 960 240 }                 | 32 {z }
                                         Tgs =(D−L)−1 U                       cgs =(D−L)−1 b




Universidad de Ingeniería y Tecnología                    Métodos Numéricos                    31 / 59
Resumen - Formas Matriciales

La solución del sistema Ax = b se obtiene mediante la siguiente expresión
recursiva.

A=D−L−U
x (k +1) = Tx (k ) + c

                                  Método         T               c
                                  Jacobi           −1
                                                 D (L + U)       −1
                                                                D b
                                  Gauss-Seidel   (D − L)−1 U (D − L)−1 b




Universidad de Ingeniería y Tecnología                Métodos Numéricos     32 / 59
    CONVERGENCIA

3
Definición
  Definición (Matriz diagonal estrictamente dominante)
 Una Matriz A es diagonal estrictamente dominante (DED) por filas si para cada
 fila i = 1, . . . , n:                   X
                                 |aii | >   |aij |.
                                         j̸=i


Ejemplo: La siguiente matriz es diagonal estrictamente dominante
                                          
                              −7 2       3     7>2+3
                       A= 5 9           1  9>5+1
                                1 4 −6         6>1+4




Universidad de Ingeniería y Tecnología          Métodos Numéricos          34 / 59
Diagonal dominancia (Matriz de coeficientes)
Considere los siguientes sistemas de ecuaciones
                                               
    
     −8x1 + 2x2 + x3 − 2x4 = 30                
                                                 −3x1 + 12x2 + x3 − 2x4          =     20
       x1 − 7x2 − x3 − 3x4       = 90              x1 − 3x2 − x3 − 7x4            =     60
                                               
(1)                                         (2)
    
     −2x1  + 3x 2 − 10x 3 + x 4 = 510          
                                                 −2x 1 + 3x2 + 8x3 + x4          =     10
        x1 − x2 − x3 + 5x4       = 600             6x1 − x2 − x3 + 2x4            =     60
                                               

                                                      
    
     −8x1 + 2x2 + x3 − 2x4              =   40        
                                                        −8x1 + 2x2 + x3 − 2x4    =   30
       x1 − 7x2 − x3 − 3x4               =   30           x1 − 7x2 − x3 − 3x4     =   90
                                                      
(3)                                                (4)
    
     −2x1 + 3x2 − 10x3 + x4             =   20        
                                                        −2x1 + 13x2 − 3x3 + x4   =   51
        x1 − x2 − x3 + 3x4               =   10            x1 − x2 − x3 + 8x4     =   65
                                                      

Determine si la matriz de coeficientes es diagonal estrictamente dominante. En
caso contrario, ¿es posible convertirla a diagonal estrictamente dominante?



Universidad de Ingeniería y Tecnología            Métodos Numéricos               35 / 59
Convergencia
  Teorema de la Diagonal dominancia
 Para el sistema Ax = b, si A es una matriz diagonal estrictamente dominante,
 entonces las iteraciones de Jacobi y Gauss-Seidel convergen para cualquier vector
 inicial.
     Importante: El criterio de la diagonal dominancia se aplica a la matriz A del
     sistema de ecuaciones lineales.
     Propiedad: Cuando ambos métodos Jacobi y Gauss-Seidel convergen,
     Gauss-Seidel converge más rápido.                   
                                              −7 2      3
Ejemplo: Sea el sistema Ax = 1 con A =  5 9            1 , entonces las
                                               1 4 −6
iteraciones de Jacobi y Gauss-Seidel convergen para cualquier valor inicial.


Universidad de Ingeniería y Tecnología      Métodos Numéricos                  36 / 59
Ejercicio: Determinar los valores de p para que la matriz A sea DED
                                                  
                                     p−1      p 0
                             Ap =       2 −p 2 
                                         0    1 2

Además, sea el sistema
                                         Ap x = b, p = −5,
¿la convergencia del método iterativo de Jacobi depende del lado derecho b?




Universidad de Ingeniería y Tecnología             Métodos Numéricos          37 / 59
Definición
  Definición (Radio Espectral)
 Sea T ∈ Cn×n una matriz cuadrada. El radio espectral de T se define como:

                               ρ(T ) = max{|λ| : λ es un valor propio de T },

       Los valores propios de T , obtenidos resolviendo la ecuación característica:
       det(T − λI) = 0, siendo I la matriz identidad de tamaño n × n.
Ejemplo: Determinar el radio espectral de la matriz:
                                             
                                        3 0
                                T =
                                        2 1




Universidad de Ingeniería y Tecnología                  Métodos Numéricos        38 / 59
Radio espectral (Matriz de iteración)
Dadas las matrices de iteración y sus respectivos valores propios:
                                                           
        2    2 −1       λ1 = 2                    −1 2      1    λ1 = 0.5392
 T = 0 −1
                 0    λ2 = 2            T =      0 2 −1      λ2 = −2.2143
        0 −1      2     λ3 = −1                     1 0 −1       λ3 = 1.6751

                                                           
                                 −1
                                                   1 −2  1   λ1 = 1.75
    −1 −1 −1   λ1 = 0            1                 1  2  0  λ2 = −1.64 + 2.41i
                                                            
T = 1  0  2  λ2 = 1.41i ; T = 
                                 2                 0 −2  1  λ3 = −1.64 − 2.41i
     0 −1  1   λ3 = −1.41i
                                   0                1 −1 −1   λ4 = −1.46
Determine el radio espectral.




Universidad de Ingeniería y Tecnología    Métodos Numéricos                 39 / 59

Convergencia
  Teorema del radio espectral
 La sucesión x (k +1) = Tx (k ) +c, para k ≥ 0 converge a la solución única x = Tx +c
 si y sólo si ρ(T ) < 1.

       Importante: El criterio del radio espectral se aplica a la matriz de iteraciones T
       del método iterativo correspondiente.

Ejemplo: Analizar la convergencia del método iterativo, si su matriz de iteraciones
T está dada por:                               
                                      1/2    0
                              T =
                                        1 2/3



Universidad de Ingeniería y Tecnología         Métodos Numéricos                    40 / 59
Convergencia
  Teorema
 Una matriz A es definida positiva si x T Ax > 0 para todo x ̸= 0. Si A es simétrica y
 definida positiva, todos sus valores propios λi son positivos y el método iterativo
 de Jacobi converge.

Demostración: Queremos que los valores propios de Tj sean menores que 1.
       Sea λ valor propio de la matriz A definida positiva y v vector propio asociado:
       v T Av = v T (λv ) = λv T v > 0 → λ > 0.
       Para una matriz A definida positiva, Tj = I − D −1 A tiene valores propios
       λi = 1 − λλii (D)
                     (A)
                         .
       Dado que λi (A) > 0 y λi (D) > 0 (¿Por qué?), se cumple que |λi (Tj )| < 1.
Así ρ(Tj ) < 1, garantizando la convergencia del método de Jacobi.

Universidad de Ingeniería y Tecnología         Métodos Numéricos                     41 / 59
Ejemplo 4
                                         
                                      3x1 + x2  = 7
Dado el sistema de ecuaciones
                                      2x1 + 5x2 = 9
   1   Determine la matriz de iteración de Gauss-Seidel.
   2   Determine si la matriz de coeficientes es diagonal estrictamente dominante.
   3   Halle el radio espectral de la matriz de iteración de Gauss-Seidel.
   4   Determine si el método iterativo de Gauss Seidel es convergente.
   5   Realice dos iteraciones utilizando el método de Gauss-Seidel, considere
        (0)      (0)
       x1 = 1; x2 = 1.




Universidad de Ingeniería y Tecnología        Métodos Numéricos                  42 / 59
Solución
   1
                                                                                                                
                   3 0                             0 0                         0 −1                              3 0
       D=                       ;   L=                          ;    U=                      =⇒    D−L =
                   0 5                            −2 0                         0  0                              2 5
                                        5                                                                 −5   
                                         15       0                                                      0   15
            (D − L)−1 =                                           =⇒         Tgs = (D − L)−1 U =               
                                         −2        3                                                         2
                                         15       15                                                     0   15
   2                                                                                        
                                3 1                                                               |3| > |1|
                   A=                                  =⇒           Dado que se cumple:                     ,
                                2 5                                                               |5| > |2|
       la matriz A es diagonal estrictamente dominante.



Universidad de Ingeniería y Tecnología                                   Métodos Numéricos                        43 / 59
Continuación
   3   Hallando el radio espectral (ρ(Tgs )) de la matriz de iteración Tgs
                                                       −5                     
                                                    0   15                1 0
                                   |Tgs − λI| =               − λ              =0
                                                        2                 0 1
                                                    0   15
                                                                                       
                                          2                                       2              2
                 λ1 = 0,             λ2 =       =⇒            ρ(Tgs ) = Max |0|,            =
                                          15                                     15             15
                                              2
   4   Dado que el radio espectral ρ(Tgs ) = 15 < 1 entonces el Método de
       Gauss-Seidel es convergente.
       Nota: El método también es convergente por ser la matriz de coeficientes
       diagonal estrictamente dominante.



Universidad de Ingeniería y Tecnología                       Métodos Numéricos                       44 / 59
   5   Iteración 1:                                   
                                                 (1)                    −5   (0) 
                                             x1                     0    15     x1
                                                       =                             + cgs
                                                                                
                                                                             
                                                 (1)                      2      (0)
                                             x2                     0    15     x2
       donde, el vector columna cgs está dado por cgs = (D − L)−1 b. Siendo
                                  7 
                                  3
            7
       b=        , tenemos cgs =      
            9                       13
                                                           15
                                            
                                     (1)                       −5                  7            
                                   x1                      0    15            1         3          2
                                             =                                   +        =
                                                                                                  
                              
                                    (1)                         2             1         13         1
                                   x2                      0    15                      15

       Ahora puedes realizar una iteración más!!!


Universidad de Ingeniería y Tecnología                                   Métodos Numéricos                 45 / 59
Comparación

       Si ambos métodos convergen, generalmente, la iteración de Gauss-Seidel
       converge más rápidamente que la iteración de Jacobi.
       Existen algunos casos que la iteración de Jacobi converge pero Gauss-Seidel
       no.




Universidad de Ingeniería y Tecnología      Métodos Numéricos                 46 / 59
Ejercicio (Examen Parcial 2023-2)
Aplicación: Dado el siguiente sistema masa resorte con 3 bloques de masas
diferentes, sostenida mediante 4 resortes:




Considere m1 = 2 , m2 = 3 , m3 = 2.5 (en kg), k = 10 kg/s2 y g = 9.81 m/s2

Universidad de Ingeniería y Tecnología   Métodos Numéricos                   47 / 59
Ejercicio (Examen Parcial 2023-2)
  a) [4 ptos] La relación entre las masas y los desplazamiento (xi ) se modela
     mediante el siguiente sistema de ecuaciones

                                         kx1 − (x2 − x1 )(2k ) = m1 g                    (1)
                                          . . . . . . . . . . . . . . . . . . = m2 g     (2)
                                          . . . . . . . . . . . . . . . . . . = m3 g     (3)

       Complete las ecuaciones (2) y (3)




Universidad de Ingeniería y Tecnología                           Métodos Numéricos     48 / 59
Ejercicio (Examen Parcial 2023-2)
  b) [3 ptos] Si eliminamos el bloque 3 y el resorte que une el bloque 2 y el bloque
     3 obtenemos el siguiente sistema de ecuaciones:

                                          3kx1 − 2kx2 = m1 g
                                         −2kx1 + 2kx2 = m2 g

       Calcule los desplazamientos usando el método de Gauss-Seidel
                                                                  y Jacobi en la
                                                               1
       segunda iteración, partiendo del punto semilla x (0) =     .
                                                               1




Universidad de Ingeniería y Tecnología              Métodos Numéricos           49 / 59
Ejercicio (Examen Parcial 2023-2)
  c) [3 ptos] Del item anterior, indique cuál de los dos métodos converge más
     rápido. Utilice el radio espectral para responder a la pregunta.




Universidad de Ingeniería y Tecnología     Métodos Numéricos                    50 / 59
Aplicacion Ex. Parcial 2023-2
Una barra delgada y larga de 200 cm de longitud está sujeto en sus extremos a
50o C y 100o C, asimismo la temperatura ambiente proporciona a la barra 80o C tal
como se muestra en la figura




Universidad de Ingeniería y Tecnología    Métodos Numéricos                  51 / 59
Aplicacion Ex. Parcial 2023-2
Para conocer la distribución de la temperatura sobre la barra, su longitud L = 200
en este caso se particiona en n = 4 partes iguales, resultando un tamaño de paso
h = 50. La discretización de la ecuación diferencial que modela la distribución de la
temperatura a lo largo de la barra dá como resultado la ecuación en diferencias

                          −Ti−1 + (2 + ch2 )Ti − Ti+1 = ch2 Ta           i = 1; 2; 3

donde c = 0.001cm−2 es el coeficiente de transferencia de calor entre la barra y el
aire del ambiente, asimismo Ti = T (xi ) denota la temperatura en el punto de
coordenada xi , formulándose así un conjunto de ecuaciones lineales simultáneas.




Universidad de Ingeniería y Tecnología               Métodos Numéricos                 52 / 59
a) [2 ptos]
Luego de reordenar las ecuaciones planteadas (si fuera necesario) formule el
sistema
       en la forma Ax = b donde A es diagonal estrictamente dominante y
      T1
x = T2 .
      T3




Universidad de Ingeniería y Tecnología    Métodos Numéricos                    53 / 59
b) [2 ptos]
Analice la convergencia de los métodos iterativos de Jacobi y Gauss Seidel




Universidad de Ingeniería y Tecnología    Métodos Numéricos                  54 / 59
c) [3 ptos]
Luego de descomponer la matriz A en D , L y U, halle la matriz de iteración para
aplicar el proceso iterativo de Gauss-Seidel Tgs y el vector cgs . Sabiendo que:
                                                       2                −1
                                                        9      0     0
                                                                      
                                                        4       2
                                                                      
                                         (D − L) = 
                                                      81       9    0 
                                                                       
                                                                      
                                                        8       4    2
                                                       729     81    9




Universidad de Ingeniería y Tecnología                       Métodos Numéricos   55 / 59
d) [3 ptos]
Realice 02 iteraciones  utilizando
                                   el método de Gauss Seidel. Considere como
                        10
vector semilla x (0) = 20
                        30




Universidad de Ingeniería y Tecnología    Métodos Numéricos                     56 / 59
Conclusiones
       Los métodos iterativos generan soluciones aproximadas sucesivas para
       sistemas de ecuaciones lineales, iniciando desde una estimación inicial y
       refinándola iterativamente.
       La convergencia de los métodos iterativos depende de las propiedades de la
       matriz, como la diagonal dominancia o la positividad definida.
       Se utilizan para resolver sistemas grandes y dispersos, ya que controlan mejor
       los errores y requieren menos recursos que los métodos directos.




Universidad de Ingeniería y Tecnología        Métodos Numéricos                    57 / 59
Bibliografía
      Steven C. Chapra and Raymond P. Canale
      Métodos numéricos para ingenieros, 7a ed. McGraw-Hill, 2015.
      Richard L. Burden and J. Douglas Faires
      Análisis numérico, 7a ed. Thompson, 2002.




Universidad de Ingeniería y Tecnología     Métodos Numéricos         58 / 59
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
