---
curso: METNUM
titulo: 10 - Semana 9/Sem9_Spline Cúbico y Ajuste de Curvas
slides: 55
fuente: 10 - Semana 9/Sem9_Spline Cúbico y Ajuste de Curvas.pdf
---

Métodos Numéricos
Spline Cúbico
y Ajuste de Curvas -S9
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


                                    Profesores: Utec-Ciencias
Temas

1 Spline Cúbico



2 Ajuste por mínimos cuadrados



3 Linealización



4 Actividad




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 21, 2026   1 / 54
        Objetivos
            Construir interpolaciones polinomiales por tramos mediante splines cúbicos de
            datos.
            Resolver problemas de ajuste de curvas mediante el método de mínimos
            cuadrados para determinar el modelo que mejor aproxima un conjunto de datos
            experimentales.
            Evaluar la calidad del modelo ajustado mediante el análisis del coeficiente de
            determinación (R²) y métricas de error para determinar su idoneidad.




Universidad de Ingeniería y Tecnología         Métodos Numéricos               May 21, 2026   2 / 54
1
    SPLINE
    CÚBICO
Spline en diseño
Situación
La figura muestra un pato malvasía en vuelo, cuyo
contorno puede ser muestreado mediante una se-
rie de puntos para ilustrar el proceso de interpo-
lación polinomial.
Este tipo de técnica tiene aplicaciones más allá del
ámbito académico: por ejemplo, en el diseño de
gráficos por computadora y animaciones digitales.            Figure: Pato Malvasía
Al capturar el perfil de un objeto —en este caso, el cuerpo del pato— a través de
puntos seleccionados estratégicamente, se puede reconstruir una curva suave que
represente su silueta con precisión.


Universidad de Ingeniería y Tecnología   Métodos Numéricos              May 21, 2026   4 / 54
                                                         Además, el uso inteligente de
                                                         la interpolación permite que el
                                                         diseño sea eficiente:
                                                             Se colocan más puntos
                                                             en zonas donde la curva
                                                             cambia bruscamente
                                                             (como en el contorno del
                                                             ala).
                                                             Se colocan menos puntos
                                                             donde la forma es más
                                                             suave.
Este tipo de aproximación es fundamental en Optimizando tanto la fidelidad
áreas como el modelado de personajes en ani- del modelo como los recursos
mación, donde se requiere construir formas com- computacionales.
plejas y realistas a partir de datos discretos.

Universidad de Ingeniería y Tecnología   Métodos Numéricos                May 21, 2026   5 / 54
Formalización de contenidos
La idea consiste en tomar una colección de puntos que delineen el contorno del
pato malvasía, y unirlos mediante curvas para aproximar su silueta. Este proceso
permite modelar la forma del pato de manera precisa a partir de datos discretos.

       Un spline es una función de interpolación segmentaria a través de polinomios
       de bajo grado, normalmente desde grado 1 hasta grado 3.
       Su aplicación principal es el modelamiento de superficies curvas a partir de
       muchos puntos a través de software de modelado.
       Con esta herramienta se desarrollan por ejemplo: Los perfiles de las alas de
       los aviones, el casco de los barcos, los alabes de una turbina, todos los
       elementos ergonómicos, etc.




Universidad de Ingeniería y Tecnología    Métodos Numéricos            May 21, 2026   6 / 54
Spline Cúbico
Un spline cúbico S es una función a trozos que interpola a f en los n + 1 puntos
(x0 , y0 ), (x1 , y1 ), (x2 , y2 ), . . . , (xn , yn ) (con a = x0 < x1 < . . . < xn = b). S está
definido en el intervalo [a; b] de la siguiente manera:
                                             
                                             
                                                   S0 (x) si x ∈ [x0 , x1 ]
                                              S1 (x) si x ∈ [x1 , x2 ]
                                             
                               S(x) =                     ..      ..
                                             
                                             
                                                          .       .
                                                 Sn−1 (x) si x ∈ [xn−1 , xn ]
                                             

Que cumple las siguientes condiciones:




Universidad de Ingeniería y Tecnología         Métodos Numéricos                 May 21, 2026   7 / 54
Continuación
       Sk (x) = ak (x − xk )3 + bk (x − xk )2 + ck (x − xk ) + dk donde x ∈ [xk ; xk +1 ] y
       k = 0, 1, 2, . . . , n − 1.
       n es el número de subintervalos.
       S(xk ) = yk , para toda k = 0, 1, 2, . . . , n
       S(x) es continua en [a; b].
       Es decir: Sk (xk +1 ) = Sk +1 (xk +1 ) para k = 0, 1, 2, . . . , n − 2.
       S ′ (x) es continua en [a; b].
       Es decir: Sk′ (xk +1 ) = Sk′ +1 (xk +1 ) para k = 0, 1, 2, . . . , n − 2.
       S ′′ (x)es continua en [a; b].
       Es decir: Sk′′ (xk +1 ) = Sk′′+1 (xk +1 ) para k = 0, 1, 2, . . . , n − 2.
Nota:
Si S ′′ (x0 ) = S ′′ (xn ) = 0 se denomina el Spline Cúbico Natural.


Universidad de Ingeniería y Tecnología             Métodos Numéricos                May 21, 2026   8 / 54
Ejemplo 1
  Ejemplo
 Dada la función

                            −x 3
                           
                                                                       ; 0≤x ≤1
               f (x) =
                            1           3          2
                                2 (x − 1) + a(x − 1) + b(x − 1) + c    ; 1≤x ≤3

 Determine los valores de a, b y c de tal manera que la función f sea un spline
 cúbico natural.




Universidad de Ingeniería y Tecnología             Métodos Numéricos         May 21, 2026   9 / 54
Solución
Pedimos que S sea spline cúbico natural en [0, 3],
                
                S0 (x) = −x 3 ,                               0 ≤ x ≤ 1,
         S(x) =            1
                S1 (x) = (x − 1)3 + a(x − 1)2 + b(x − 1) + c, 1 ≤ x ≤ 3.
                           2
Condiciones:

       Continuidad de S en x = 1:                            Continuidad de S ′′ en x = 1:
               S0 (1) = S1 (1)                                   S0′′ (1) = S1′′ (1)
                   −1 = c            =⇒   c = −1                       −6 = 2a     =⇒ a = −3
                                 ′
       Continuidad de S en x = 1:
               S0′ (1) = S1′ (1)
                   −3 = b            =⇒   b = −3

Universidad de Ingeniería y Tecnología             Métodos Numéricos                   May 21, 2026   10 / 54
Solución
Por lo tanto, el spline cúbico natural S en [0, 3] es
                
                S0 (x) = −x 3 ,                               0 ≤ x ≤ 1,
       S(x) =              1
                S1 (x) = (x − 1)3 − 3(x − 1)2 − 3(x − 1) − 1, 1 ≤ x ≤ 3.
                           2
Y sobre las otras condiciones:
Condición de grado cúbico: se cumple.
Condición de interpolación: se asume pues no hay datos propiamente dichos.
Condición natural en x = 0: S ′′ (0) = 0.

                      Se verifica automáticamente pues      S0′′ (0) = −6 · 0 = 0

Condición natural en x = 3: S ′′ (3) = 0.

         S1′′ (x) = 3(x − 1) + 2a ∧ a = −3 ⇒ S1′′ (3) = 3(2) + 2(−3) = 0

Universidad de Ingeniería y Tecnología        Métodos Numéricos                 May 21, 2026   11 / 54
Ventaja sobre la interpolación polinomial
Por ejemplo, si de un laboratorio obtenemos 10 puntos de un experimento que
sabemos que debería tener una tendencia sinusoidal, sin embargo esta presenta
distorsión considerable, y luego quisieramos usar estos puntos para interpolar en
0.2.




Universidad de Ingeniería y Tecnología   Métodos Numéricos         May 21, 2026   12 / 54
Ventaja sobre la interpolación polinomial
Sin embargo, si comparamos la interpolación polinomial vs la interpolacion por
spline, tenemos lo siguiente:




Universidad de Ingeniería y Tecnología   Métodos Numéricos         May 21, 2026   13 / 54
 ¿Como se calcula un spline cúbico natural?
  Construcción del Spline
        Si tenemos n+1 puntos:
        (x0 , y0 ), (x1 , y1 ), (x2 , y2 ), (x3 , y3 ), (x4 , y4 ), . . . (xn , yn ),
        El Spline cúbico natural es un conjunto de polinomios
        Si (x) = ai (x − xi )3 + bi (x − xi )2 + ci (x − xi ) + di para i = 0, 1, ..n − 1
        donde:
              M −Mi
        ai = i+16hi
        bi = M2i
                            M +2M
        ci = y[xi , xi+1 ] − i+16 i hi
        di = yi
        hi = xi+1 − xi
        Mi = Si′′ (xi ) para i = 0, 1, ..n
        Mi para i = 1, ..n − 1 resuelven el siguiente sistema lineal.
Universidad de Ingeniería y Tecnología                     Métodos Numéricos            May 21, 2026   14 / 54
¿Como se calcula un spline cúbico natural?
  Construcción del Spline
        Mi se obtiene del siguiente sistema de ecuaciones:
                                                                                 
         2(h0 + h1 )              h1            0       ...             0
                                                                                          
                                                                                      M1
                                                                         ..
                                                                                    M2 
                                                                                 
        
             h1           2(h1 + h2 ) h2               ...               .        . 
              0                   . . .       . . .     . . .           0          .     =
                                                                                   . 
        
        
               ..                 . .
                                                                                          
                                                                                   Mn−2
                                                                                 
               .                     .      hn−3 2(hn−3 + hn−2 )      hn−2               
              0                   ...           0      hn−2       2(hn−2 + hn−1 )    Mn−1
                                                   
                  y [x1 , x2 ] − y [x0 , x1 ]
         
                 y [x2 , x3 ] − y [x1 , x2 ]       
                                                    
        6
                              ..                   
                               .                   
                                                    
         y[xn−2 , xn−1 ] − y [xn−3 , xn−2 ]
            y[xn−1 , xn ] − y [xn−2 , xn−1 ]

Universidad de Ingeniería y Tecnología      Métodos Numéricos              May 21, 2026   15 / 54
Ejemplo 2
 Ejemplo
 Calcule el spline cúbico natural que se interpole a los siguientes puntos, luego
 estime la velocidad en los instantes 3s y 10s, usando la funcion de interpolación.


                                         tiempo (s)   Velocidad (m/s)
                                             1               5
                                             5              10
                                             10             15
                                             12             25




Universidad de Ingeniería y Tecnología                Métodos Numéricos   May 21, 2026   16 / 54
Solución
Identificamos n = 3, luego planteamos el sistema de ecuaciones para los Mi :
                                                                                                       
             2(h0 + h1 )                 h1         M1                       y [x1 , x2 ] − y [x0 , x1 ]
                 ..                      ..       ..                                   ..
                                                 .  = 6 
                                                                                                      
                   .                       .                                              .            
                   hn−2           2(hn−2 + hn−1 )    Mn−1              y [xn−1 , xn ] − y [xn−2 , xn−1 ]

                                   i        x       y            hi          y [xi , xi+1 ]
                                  0        1        5            4              1.25
                                  1        5        10           5               1
                                  2        10       15           2               5
                                  3        12       25

                                       M0 = 0,               M3 = 0
                                                                      
                             18 5   M1   −1.5                      M1   −0.621
                                       =                     =⇒       =
                              5 14 M2     24                       M2    1.936

Universidad de Ingeniería y Tecnología                   Métodos Numéricos                           May 21, 2026   17 / 54
Continuación...
Usando las fórmulas de los coeficientes se sigue:
                Mi+1 − Mi                       Mi                              Mi+1 + 2Mi
         ai =             ,              bi =      ,    ci = y [xi , xi+1 ] −              hi ,        di = yi .
                   6 hi                         2                                    6

               Si [xi , xi+1 ]             ai              bi                   ci                d
               S0 [1, 5]                 −0.026            0               1.6641                 5
               S1 [5, 10]                0.0852        −0.31057           0.42181                 10
               S2 [10, 12]               −0.161        0.96806            3.70925                 15
Spline cúbico natural:
          S0 (x) = −0.026 (x − 1)3 + 0 (x − 1)2 + 1.6641 (x − 1) + 5,
          S1 (x) =        0.0852 (x − 5)3 − 0.31057 (x − 5)2 + 0.42181 (x − 5) + 10,
          S2 (x) = −0.161 (x − 10)3 + 0.96806 (x − 10)2 + 3.70925 (x − 10) + 15.
Interpolación en x = 3:
S0 (3) = −0.026 (3 − 1)3 + 0 (3 − 1)2 + 1.6641 (3 − 1) + 5 = 8.12.
Universidad de Ingeniería y Tecnología                     Métodos Numéricos                       May 21, 2026    18 / 54
ACTIVIDAD
 P1
 Determine el spline cúbico natural que interpola los siguientes datos:

                                         x   0 1 2 3
                                         y   1 1 0 10




Universidad de Ingeniería y Tecnología        Métodos Numéricos      May 21, 2026   19 / 54

2
    AJUSTE POR
    MÍNIMOS CUADRADOS
Formalización de Contenidos

El ajuste de curva permite expresar un conjunto de puntos de datos discretos (nube
de puntos) como una función continua. Generalmente los datos son
experimentales, que pueden tener una cantidad significativa de error y no es
necesario encontrar una función que pase por todos los puntos discretos.




La función a determinar no necesariamente pasa por todos los puntos pero si
representa a dichos puntos
Universidad de Ingeniería y Tecnología   Métodos Numéricos         May 21, 2026   21 / 54
Ajuste lineal por Mínimos Cuadrados
   1   Ajustar a una recta un conjunto de datos (pares ordenados)
       (x1 ; y1 ), (x2 ; y2 ) (x3 ; y3 ), . . . , (xn ; yn )

                             y
                                                                  a1 : Pendiente (Desconocido)
                                                              a0 : y-intersección (Desconocido)
                             yi                               e = yi − a1 xi − a0
        ei                                          a1 x + a0 i
               a1 xi + a 0                                    Error cometido para el
                                                              i-ésimo punto

                                         xi                       x

   2   El modelo lineal se corresponde con la recta y = a1 x + a0
   3   Para obtener a0 y a1 minimizamos la suma de los cuadrados de los errores
       cometidos.
Universidad de Ingeniería y Tecnología        Métodos Numéricos                May 21, 2026   22 / 54
Continuación...
Considerando la expresión
                                                   n
                                                   X             n
                                                                 X
                            Sr = Sr (a0 , a1 ) =         ei2 =     (yi − a1 xi − a0 )2
                                                   i=1           i=1


Observamos que depende de los parámetros a1 y a0 , en este caso xi e yi son
constantes, a0 y a1 serán hallados como los valores que minimizan a la
función Sr .
Para esto hallamos las derivadas parciales e igualamos a cero:
                                   n
                  
                     ∂Sr         X
                  
                           = −2     (yi − a1 xi − a0 )xi = 0
                   ∂a1
                  
                  
                                                   i=1
                  

                                                  n
                              
                               ∂Sr                X
                                         =   −2          (yi − a1 xi − a0 )   = 0
                              
                              
                               ∂a
                              
                                  0
                                                   i=1
Universidad de Ingeniería y Tecnología                   Métodos Numéricos               May 21, 2026   23 / 54
Ecuaciones Normales
Acomodando algebraicamente las ecuaciones en las variables a0 y a1 se llega al
siguiente sistema lineal:
                           n                 n           n
                                 !                !
                         X                  X           X
                               2
                    
                    
                    
                             xi a1 +           xi a0 =     xi yi
                          i=1               i=1         i=1
                                 n                        n
                                       !
                              X                         X
                                    x    a  + na      =      yi
                    
                                     i    1      0
                    
                    
                    
                                               i=1                         i=1
La forma matricial de dicho sistema es:
                                                  n         
                     n          n
                                                  X
                       X        X                      xi yi 
                           xi2      xi   a  
                                            1
                                                 i=1       
                                                          
                     i=1       i=1            =
                                                            
                     n
                                             
                                                            
                       X                a0          n
                           xi     n
                                                 X         
                                                        yi
                                                            
                                         i=1
                                                                         i=1

Universidad de Ingeniería y Tecnología               Métodos Numéricos           May 21, 2026   24 / 54
Continuación...
Al resolver el sistema anterior obtenemos los coeficientes a0 y a1
                                             n               n          n                   n
                                             X               X          X            1X
                                         n         xi yi −         xi         yi        xi yi − x̄ ȳ
                                                                                     n
                                             i=1             i=1        i=1                i=1
                             a1 =                                            !2 =     n
                                             n                   n                   1X
                                                                                                 xi2 − (x̄)2
                                             X                   X
                                         n          xi2 −               xi           n
                                              i=1                i=1                       i=1

                             a0 = ȳ − a1 x̄

donde
                                                             n                        n
                                                    1X                            1X
                                               x̄ =    xi ,                  ȳ =    yi .
                                                    n                             n
                                                         i=1                        i=1




Universidad de Ingeniería y Tecnología                                 Métodos Numéricos                       May 21, 2026   25 / 54
Bondad del ajuste lineal
Consideremos la suma de errores cuadráticos Sr y la suma total de cuadrados St :
                             n
                             X             n
                                           X                                                     n
                                                                                                 X
                    Sr =           ei2 =         (yi − a1 xi − a0 )2 ,                St =              (yi − ȳ )2 .
                             i=1           i=1                                                    i=1
El coeficiente de determinación es definido como sigue
                                    St − Sr    Sr
                                                r2 =
                                            =1− .
                                       St      St
Para el caso del ajuste lineal se cumple que
                                               n
                                               X               n
                                                               X          n
                                                                          X
                                           n         xi yi −         xi         yi
          ρ(xi , yi ) = v                      i=1
                                                   !2 v
                                                               i=1        i=1
                                                                                                !2 , ⇒      ρ(xi , yi )2 = r 2
                        u
                          u Xn                  n
                                                X
                                                      u n
                                                      u X                            n
                                                                                     X
                          tn   xi2 −              x tn  i y2 −              i              yi
                                 i=1            i=1                  i=1             i=1

r 2 es el cuadrado del coeficiente de correlación lineal entre xi e yi .
Universidad de Ingeniería y Tecnología                           Métodos Numéricos                                May 21, 2026   26 / 54
Ejemplo

Halle la recta de la forma
                                                    y = a1 x + a0
que mejor se ajusta a los siguientes datos (mostrados en la tabla), determinando
asímismo la calidad del ajuste

                                         xi   -10     -5       4     15        20
                                         yi   -30     25      80     50        -40




Universidad de Ingeniería y Tecnología                     Métodos Numéricos         May 21, 2026   27 / 54
Desarrollo
Según las necesidades del cálculo elaboramos la siguiente tabla

                        xi       yi       xi2     yi2     yi xi       xi3      xi4     yi xi2
                       -10      -30      100     900      300       -1000    10000    -3000
                        -5      25        25     625     -125        -125     625      625
                         4      80        16    6400      320         64      256     1280
                       15       50       225    2500      750       3375     50625    11250
                       20       -40      400    1600     -800       8000    160000   -16000
             X
                       24        85      766    12025     445       10314   221506   -5845

En la última fila de la tabla se tiene la suma de las respectivas columnas, las cuales
utilizamos para determinar x̄, ȳ , a1 , a0 , St , Sr y r 2 [ejercicio].



Universidad de Ingeniería y Tecnología                  Métodos Numéricos             May 21, 2026   28 / 54
Utilizando los datos de la tabla construida formulamos las ecuaciones normales:
                          6                 6            6
                                !              !
                         X               X             X
                              2
                    
                    
                    
                            xi a1 +          xi a0 =      xi yi
                         i=1 !            i=1          i=1
                        X6                            X 6
                             x    a    na                  yi
                    
                    
                    
                             i    1 +    0         =
                                         i=1                                  i=1

Es decir:                                      
                                                   766a1 + 24a0 = 445
                                                   24a1 + 5a0 = 85
Resolviendo obtenemos:

                                         a1 = 0.0569      ;       a0 = 16.7271

Luego la recta es
                                               y = 0.0569x + 16.7271
Universidad de Ingeniería y Tecnología                    Métodos Numéricos         May 21, 2026   29 / 54
Ejercicio:
  1 Dibuje en un mismo sistema de coordenadas los puntos y la recta hallada
                                                    S
  2 Halle el coeficiente de determinación r 2 = 1 − Sr y comente sobre su valor.
                                                      t



   xi       yi       ybi = 0.0569xi + 16.7271           ei = yi − ybi            ei2     yi − ȳ        (yi − ȳ )2
  -10      -30                16.1581                    -46.1581            2130.5702    -47             2209
   -5      25                 16.4426                      8.5574             73.2291       8               64
    4      80                 16.9547                     63.0453            3974.7099     63             3969
  15       50                 17.5806                     32.4194            1051.0175     33             1089
  20       -40                17.8651                    -57.8651            3348.3698    -57             3249
   Σ                                                                        10577.8965                   10580
                                         X
                                 Sr =        ei2 = 10577.8965,
                                         X
                                 St =        (yi − ȳ )2 = 10580,
                                              Sr     10577.8965
                                  r2 = 1 −       =1−            = 0.0002
                                              St       10580
Universidad de Ingeniería y Tecnología                  Métodos Numéricos                May 21, 2026     30 / 54
Planteando un sistema sobredeterminado
              xi -10 -5       4 15 20
Si los puntos                                 satisfacen la ecuación y = a1 x + a0 ,
              yi -30 25 80 50 -40
entonces las ecuaciones resultantes a1 xi + a0 = yi , 1 ≤ i ≤ 5, se pueden organizar
en forma matricial:                                    
                          −10 1                     −30
                         −5 1              25 
                                   a1                  
                                    a0 =  80 
                         4      1                      
                        
                         15 1                  50 
                           20 1                     −40
Se plantea en general un sistema de la forma

                                         Ma = y

donde la matriz de coeficientes M tiene tantas filas como puntos (5 en este caso) y
tantas columnas como parámetros desconocidos (2 en este caso).

Universidad de Ingeniería y Tecnología    Métodos Numéricos          May 21, 2026   31 / 54
Sistema sobredeterminado
Multiplicando a la igualdad por la transpuesta de matriz de coeficientes, es decir

                                                     M T Mx = M T y

obteniendo un sistema de ecuaciones:
                                                                               n     
                                     n             n
                                                                              X
                                     X
                                               2
                                                   X                     xi yi 
                                      x                xi   a  
                                  i=1 i                       1
                                                                   i=1       
                                                   i=1
                                                                             
                                  n                           =           
                                  X                                         
                                                           a0         n
                                       xi            n
                                                                   X         
                                                                          yi
                                                                              
                                         i=1
                                                                                i=1

Compare con el sistema de ecuaciones anterior, ¿es el mismo?



Universidad de Ingeniería y Tecnología                      Métodos Numéricos             May 21, 2026   32 / 54
Mejor una cuadrática
Dado que el valor de r 2 no es adecuado, al graficar nube de puntos y ver la forma
que tiene parece mas adecuado un ajuste cuadrático, es decir una funcion de la
forma
                                y = a2 x 2 + a1 x + a0
Para desarrollar:
       En base a lo realizado para el caso lineal formule el sistema sobredeterminado
       para hallar los parámetros desconocidos de la función aproximante o de ajuste
       cuadrática y luego formule las ecuaciones normales, resolviendo finalmente
       dicho sistema
       Verifique que en el caso de ajuste polinomial el sistema de ecuaciones y lado
       derecho tienen la misma forma general.




Universidad de Ingeniería y Tecnología    Métodos Numéricos           May 21, 2026   33 / 54
Sistema Sobredeterminado:                  Ecuaciones normales: M T Ma = M T y
Ma ≃ y                                                     2
                                                            x1 x22 x32 x42 x52
                                                                                 
                                                       T
Para el modelo cuadrático se plantea       Tenemos M =  x1 x2 x3 x4 x5 
                                                            1   1    1    1    1
              a2 xi2 + a1 xi + a0 = yi     Luego las ecuaciones normales son
Que en forma matricial es
                                                P 4 P 3 P 2    P 2 
                                                     x       x     x     a2
                                                  P i P i2 P i                    P xi yi
           2                                 xi3        xi    xi  a1  =  Pxi yi 
           x1      x1    1         y1             P 2 P
                                                                         a0
                                                     xi      xi   n                  yi
          x22
                              
           2      x2    1  a2
                                  y2 
                                   
                            a1 = y3 
          x3      x3    1            Que con los datos da
          
          x 2     x4    1 a0    y4 
            4                                                                     
           x52     x5    1         y5            221506 10314      766    a2      −5845
                                                10314      766     24  a1  =  445 
Y con los datos del problema da
                                                   766       24     5     a0       85
                                  
       100 −10 1                −30      Resolviendo a2 = −0.5277, a1 = 5.4391, a0 = 71.7431:
      25     −5 1    a2
                                 25 
                                                  f (x) = −0.5277x 2 + 5.4391x + 71.7431
                                   
      16      4     1 a1  =  80 
                                  
     225     15     1 a0       50 
       400    20     1            −40
  Universidad de Ingeniería y Tecnología   Métodos Numéricos                 May 21, 2026   34 / 54
Ejercicio:
                                                    S
  1 Halle el coeficiente de determinación r 2 = 1 − Sr y comente sobre su valor.
                                                      t
  2 Dibuje en un mismo sistema de coordenadas los puntos y la recta hallada
Tenemos
                      f (x) = −0.5277x 2 + 5.4391x + 71.7431
              xi       yi       ybi = f (xi )   ei = yi − ybi       ei2      yi − ȳ   (yi − ȳ )2
             -10      -30        -35.4179          5.4179        29.3536      -47        2209
              -5      25         31.3551          -6.3551        40.3873        8          64
              4       80         85.0563          -5.0563        25.5662       63        3969
             15       50         34.5971          15.4029       237.2493       33        1089
             20       -40        -30.5549         -9.4451        89.2099      -57        3249
              Σ                                                 421.7663                10580
                                          X
                                   Sr =         ei2 = 421.7663,      St = 10580,
                                                Sr     421.7663
                                    r2 = 1 −       =1−          = 0.9601
                                                St      10580
Universidad de Ingeniería y Tecnología                   Métodos Numéricos                May 21, 2026   35 / 54
Dibujamos finalmente los puntos y las funciones de ajuste lineal y cuadrática




Universidad de Ingeniería y Tecnología   Métodos Numéricos          May 21, 2026   36 / 54
Observaciones
       El coeficiente r 2 determina la calidad del ajuste, algunos autores sugieren que
       debe ser mayor a 0.7. Un ajuste perfecto ocurre cuando se cumple r 2 = r = 1.
       El coeficiente de determinación r 2 se mantiene o aumenta conforme aumenta
       la complejidad del modelo (polinomio de mayor grado). Sin embargo, no
       siempre es preferible un mayor r 2 pues ello puede conducir a sobreajuste y
       otros problemas como el fenómeno de runge de la interpolación polinomial.
       Que el coeficiente de determinación r 2 coincida con el cuadrado del
       coeficiente de correlación solo es aplicable al ajuste lineal.
       El sistema sobredeterminado se puede resolver factorizando la matriz M en la
       forma QR. Esto puede mejorar la estabilidad y precisión de la solución.
       Muchas funciones de ajuste que no son lineales pueden ser transformadas a
       lineales (se dice que pueden ser "linealizadas")



Universidad de Ingeniería y Tecnología    Métodos Numéricos             May 21, 2026   37 / 54
Actividad - Examen final 2023 - 2
En un problema de ajuste lineal y = ax + b, si el coeficiente de correlación r es 0
entonces la suma de residuos cuadráticos Sr no coincide con la suma total de
cuadrados St .




Universidad de Ingeniería y Tecnología   Métodos Numéricos           May 21, 2026   38 / 54
3   LINEALIZACIÓN

Ajuste con funciones no lineales
Considere un modelo no lineal (por ejemplo, basado en la forma de la nube de
puntos):
                                   y = MeNx
Puede transformarse con el siguiente cambio de variable

                                         X = x, Y = ln(y )

en el modelo lineal
                                           Y = AX + B
donde A = N, B = ln(M).




Universidad de Ingeniería y Tecnología         Métodos Numéricos   May 21, 2026   40 / 54
Ajuste con funciones no lineales




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 21, 2026   41 / 54
Ajuste con funciones no lineales
Algunas funciones de ajuste no lineales y = g(x) puede ser transformadas en una
ecuación de la forma Y = aX + b, mediante cambios adecuados de variable, (es
decir pueden ser "linealizadas").
Por ejemplo:
   1   La función g(x) = MeNx al aplicar ln a ambos lados de la ecuación se
       convierte en la función lineal Y = AX + B, donde A = N; B = ln(M), X = x e
       Y = ln(g(x))
   2   Similarmente la funcion g(x) = Mx N se convierte en Y = AX +B, donde
       A = N, B = ln(M), X = ln(x) e Y = ln(g(x))
   3   La función g(x) = MxeNx se convierte
                                            en Y = AX +B, donde A = N,
                                   g(x)
       B = ln(M), X = x e Y = ln x




Universidad de Ingeniería y Tecnología   Métodos Numéricos          May 21, 2026   42 / 54
  Ejemplo
 Realice el ajuste mediante una función de la forma g(x) = MeNx para los puntos:

                                         xk   −4 2 10 14
                                         yk   20 6 2   1




Universidad de Ingeniería y Tecnología          Métodos Numéricos   May 21, 2026   43 / 54
  Ejemplo
 Realice el ajuste mediante una función de la forma g(x) = MeNx para los puntos:

                                              xk   −4 2 10 14
                                              yk   20 6 2   1

Tenemos                                                  
                                         ln g(x) = ln MeNx = Nx + ln M

Lo que sugiere definir la transformación

                                               X = x,     Y = ln y ,

y realizar el ajuste lineal de las variables Y = AX + B con A = N, b = ln M.



Universidad de Ingeniería y Tecnología                  Métodos Numéricos   May 21, 2026   44 / 54
Continuación
El ajuste lineal se realiza con los datos de X , Y :
                                         xk    yk Xk = xk Yk = ln(yk )
                                         −4    20     −4 ln(20) = 2.9957
                                          2    6        2 ln(6) = 1.7918
                                         10    2       10 ln(2) = 0.6931
                                         14    1       14 ln(1) = 0
Resolviendo las ecuaciones normales para Y = AX + B se tiene
                                              A = −0.1621,    B = 2.2617,
                                              Y = −0.1621 X + 2.2617.
Retornando al modelo exponencial
                             N = A = −0.1621,           M = eln M = eB = 9.5994,
                             y = g(x) = M eNx = 9.5994 e−0.1621x .
Universidad de Ingeniería y Tecnología                   Métodos Numéricos         May 21, 2026   45 / 54
  Ejemplo
 Realice el ajuste mediante una función de la forma g(x) = Mx N para los puntos:

                                         xk   1.12 1.3 1.5 3
                                         yk     6  0.5 2 11




Universidad de Ingeniería y Tecnología            Métodos Numéricos   May 21, 2026   46 / 54
Ajuste de la combinación lineal de funciones
Consideremos el conjunto de datos (x1 ; y1 ), (x2 ; y2 ) (x3 ; y3 ), . . . , (xm ; ym )
y la función de ajuste

                                   g(x) = c1 f1 (x) + c2 f2 (x) + · · · + cn fn (x)

cuyas funciones base son: f1 (x) , f2 (x) , · · · , fn (x)
los cuales han sido seleccionadas para realizar el ajuste adecuado (observando la
forma de la nube de puntos)
asimismo tenemos las constantes c1 , c2 , · · · , cn
       Hay m puntos (por lo general numeroso)
       Hay n funciones base (por lo general pequeño coincide con las cantidad de
       constantes)
       El objetivo principal es hallar las constantes


Universidad de Ingeniería y Tecnología                   Métodos Numéricos            May 21, 2026   47 / 54
Continuación...
Por ejemplo
   1   la función de ajuste para un polinomio cúbico es:

                                             g(x) = c1 x 3 + c2 x 2 + c3 x + c4

       la cual tiene las funciones base: x 3 , x 2 , x , 1
       Siendo el objetivo encontrar los coeficientes ci tal que g(xi ) ≈ yi .
   2   La funcion de ajuste coseno sinuidal
                                                                                            
                                                                  πt                      πt
                                         h(t) = a0 + a1 sen                + a2 cos
                                                                  6                       6

       tiene por funciones base a: 1 , sen π6t       , cos π6t
                                                              

       El objetivo es hallar los coeficientes a0 , a1 , a2


Universidad de Ingeniería y Tecnología                   Métodos Numéricos                         May 21, 2026   48 / 54
Método
Consideremos la función de ajuste con n funciones base y m datos

                               y = g(x) = c1 f1 (x) + c2 f2 (x) + · · · + cn fn (x)

Asumiendo que g(x) actúa como una función interpolante, se formula el sistema de
ecuaciones en las variables ci :
                 
                 
                    c1 f1 (x1 ) + c2 f2 (x1 ) + · · · + cn fn (x1 ) = y1 ,
                  c1 f1 (x2 ) + c2 f2 (x2 ) + · · · + cn fn (x2 ) = y2 ,
                 
                                                ..
                 
                 
                                                .
                    c1 f1 (xm ) + c2 f2 (xm ) + · · · + cn fn (xm ) = ym ,
                 




Universidad de Ingeniería y Tecnología                 Métodos Numéricos              May 21, 2026   49 / 54
Continuación...
El sistema planteado en términos matriciales
                                                              
                  f1 (x1 ) f2 (x1 ) · · · fn (x1 )     c1       y1
                f1 (x2 ) f2 (x2 ) · · · fn (x2 )   c2   y2 
                                                     ..  =  .. 
                                                              
                     ..       ..     ..      ..
                      .        .      .       .    .   . 
                             f1 (xm ) f2 (xm ) · · · fn (xm )        cn   ym

es decir:
                                                   Mc = y




Universidad de Ingeniería y Tecnología               Métodos Numéricos         May 21, 2026   50 / 54
Observaciones:
       La matriz de coeficientes M tiene m filas (igual a la cantidad de datos) y n
       columnas (igual a la cantidad de constantes)
       Este sistema es sobredeterminado dado que generalmente n es mucho menor
       que m
       Si se conoce la factorización QR de Gram-Schmidt o de Householder para la
       matriz M es recomendable utilizarlo.
       Esta vez resolvemos el sistema convirtiendolo a ecuaciones normales
       mediante la multiplicación por la matriz transpuesta

                                         (M T M)c = M T y




Universidad de Ingeniería y Tecnología       Métodos Numéricos          May 21, 2026   51 / 54
Actividad - EF 2024 - 2
Responda si la siguiente afirmación es verdadera o falsa: La obtención de los
parámetros A y B de la curva y = AeBx , mediante la linealización con el logaritmo
natural, es válida para cualquier conjunto de puntos (xi , yi ).
Nota: Asegurando que todos los puntos (xi , yi ) del conjunto original sean utilizados
en el proceso.




Universidad de Ingeniería y Tecnología   Métodos Numéricos             May 21, 2026   52 / 54
Ejercicio - EF 2024 - 2
En un sistema mecánico de amortiguamiento en el que se estudia la relación entre
la fuerza de amortiguamiento (y ) y la posición (x) de un componente móvil se
obtuvo los siguientes datos experimentales:

                                         x (cm) 1    2   3   4
                                         y (kN) 0.2 1.0 1.4 3.8

Realice un ajuste al modelo no lineal: y = Ax 2 + Bx cos(πx) y halle los
coeficientes A y B usando el método de mínimos cuadrados.
Observación: No efectúe cambio de unidades.




Universidad de Ingeniería y Tecnología            Métodos Numéricos   May 21, 2026   53 / 54

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
