---
curso: METNUM
titulo: 14 - Semana 13/Sem13_Sistema EDO
slides: 31
fuente: 14 - Semana 13/Sem13_Sistema EDO.pdf
---

Métodos
Numéricos
Sistemas EDO - S13
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
                                                      Índice
                                            1 Sistema de Ecuaciones
                                              Diferenciales Ordinarias
                                              de Primer Orden
                                            2 Ecuaciones         Difer-
                                              enciales    de    Orden
                                              Superior




Universidad de Ingeniería y Tecnología   Métodos Numéricos          June 1, 2026   1 / 30
        Objetivos:
            Transformar EDO de orden superior a sistema de primer orden.




Universidad de Ingeniería y Tecnología       Métodos Numéricos             June 1, 2026   2 / 30
1   SISTEMA DE
    ECUACIONES
    DIFERENCIALES
    ORDINARIAS
Sistema de Ecuaciones Diferenciales
Un sistema de n ecuaciones diferenciales de primer orden con n funciones
incógnitas y1 (t), · · · , yn (t) en la variable independiente t, tendrá la siguiente forma:

                                         y1′ = f1 (t, y1 , y2 , ..., yn )
                                         y2′ = f2 (t, y1 , y2 , ..., yn )
                                                       ..
                                                        .
                                         yn′ = fn (t, y1 , y2 , ..., yn )

donde: f1 , f2 , · · · , fn son funciones de las n + 1 variables t, y1 , y2 , · · · , yn .




Universidad de Ingeniería y Tecnología                 Métodos Numéricos              June 1, 2026   4 / 30
Sistema de Ecuaciones Diferenciales
MÉTODO DE EULER PARA SISTEMAS EDO (FORMA VECTORIAL)
El método de Euler en su forma vectorial se expresa como:

                                         yi+1 = yi + h F(ti , yi )

Para un sistema de 2 EDO, se tendría:
                                                        
                            x                 f (t, x, y )
                       y=       , F(t, y) =
                            y                g(t, x, y )
Note que para estos vectores la variable independiente es t y las variables
dependientes son x e y .
El método de Euler proporciona una aproximación sencilla al comportamiento de un
sistema dinámico, pero su precisión depende del tamaño del paso h.

Universidad de Ingeniería y Tecnología              Métodos Numéricos   June 1, 2026   5 / 30
Sistema de Ecuaciones Diferenciales
MÉTODO DE RK2 (HEUN) PARA SISTEMAS EDO (FORMA VECTORIAL)
El método de Heun, en su forma vectorial, se expresa como:
                                                  
                                         1      1
                         yi+1 = yi + h     k1 + k2
                                         2      2

donde:                                   k1 = F(ti , yi )
                                         k2 = F(ti + h, yi + hk1 )
Para sistema de 2 EDO:                                               
                          x                                f (t, x, y )
                      y=     ,                   F(t, y) =                .
                          y                                g(t, x, y )
       El método de RK2 mejora la precisión de Euler corrigiendo el siguiente paso
       con la pendiente media, sin aumentar significativamente la complejidad
       computacional.
Universidad de Ingeniería y Tecnología                Métodos Numéricos       June 1, 2026   6 / 30
Sistema de Ecuaciones Diferenciales
MÉTODO DE RK4 PARA SISTEMAS EDO (FORMA VECTORIAL)
El método de Runge-Kutta de cuarto orden en su forma vectorial se expresa como:
                                 h
                     yi+1 = yi + (k1 + 2k2 + 2k3 + k4 )
                                 6
                                                                                
donde:                                                                h      h
                       k1 = F(ti , yi )                    k3 = F ti + , yi + k2
                                                                      2      2
                                            
                                        h h
                       k2 = F ti + , yi + k1   k4 = F(ti + h, yi + hk3 )
                                        2 2
Para sistema de 2 EDO:                                                  
                                             x                f (t, x, y )
                                         y=     ,   F(t, y) =                .
                                             y                g(t, x, y )

       El método de RK4 logra un equilibrio entre precisión y eficiencia, mejorando
       las estimaciones sin un incremento excesivo en el costo computacional.
Universidad de Ingeniería y Tecnología                  Métodos Numéricos            June 1, 2026   7 / 30
Ejemplo de Sistema de EDO
Consideremos un modelo depredador-presa que describe la evolución de dos
poblaciones: 
                dx
              dt = 1.5x − 0.5xy
                                       
                                       ẋ = 1.5x − 0.5xy ,
             
             

              dy = −2y + 0.6xy          ẏ = −2y + 0.6xy
             
                                      
                 dt
con las condiciones iniciales: x(0) = 40,       y (0) = 9, donde:
       t representa el tiempo en (meses).
       x(t) representa la población de presas en el tiempo t (individuos).
       y (t) representa la población de depredadores en el tiempo t (individuos).
       Los coeficientes indican tasas de crecimiento y depredación (1/mes).
       El símbolo ẋ se usa para indicar la variación temporal de la variable x
       (individuos/mes).
Universidad de Ingeniería y Tecnología      Métodos Numéricos           June 1, 2026   8 / 30
Ejemplo de Sistema de EDO
Aplicamos el método de Euler con h = 0.1 para el sistema de ecuaciones
diferenciales. Para ello, definimos el sistema en forma vectorial:
                                                          
                               x                1.5x − 0.5xy
                         y=      , F(t, y) =
                               y                −2y + 0.6xy
Para i = 0:                              t0 = 0
                                         y1 = y0 + h F(t0 , y0 )
Calculamos F(t0 , y0 ):
                                                              
                        1.5(40) − 0.5(40)(9)     60 − 180      −120
        F(t0 , y0 ) =                         =             =        .
                         −2(9) + 0.6(40)(9)      −18 + 216     198
Finalmente, calculamos y1 :                                         
                                                  40         −120    28
                       y1 = y0 + h F(t0 , y0 ) =     + 0.1        =
                                                   9         198    28.8
Es decir: x(0.1) = 28, y (0.1) = 28.8
Universidad de Ingeniería y Tecnología             Métodos Numéricos         June 1, 2026   9 / 30
Ejemplo de Sistema de EDO (Continuación)
Para i = 1:                              t1 = t0 + h = (0) + (0.1) = 0.1
                                         y2 = y1 + h F(t1 , y1 )
Calculamos F(t1 , y1 ):
                                                                      
                    1.5(28) − 0.5(28)(28.8)        42 − 403.2      −361.2
    F(t1 , y1 ) =                             =                  =           .
                    −2(28.8) + 0.6(28)(28.8)     −57.6 + 483.84     426.24

Finalmente, calculamos y2 :
                                                                        
                               28           −361.2      28 − 36.12      −8.12
  y2 = y1 + h F(t1 , y1 ) =         + 0.1           =                 =          .
                              28.8          426.24     28.8 + 42.624     71.42

Es decir: x(0.2) = −8.12, y (0.2) = 71.42.



Universidad de Ingeniería y Tecnología                 Métodos Numéricos   June 1, 2026   10 / 30
Ejemplo de Sistema de EDO (Continuación)
Para i = 2:
                                         t2 = t1 + h = (0.1) + (0.1) = 0.2
                                         y3 = y2 + h F(t2 , y2 )
Calculamos F(t2 , y2 ):
                                                                          
                1.5(−8.12) − 0.5(−8.12)(71.42)     −12.18 + 289.86      277.68
F(t2 , y2 ) =                                   =                    =
                −2(71.42) + 0.6(−8.12)(71.42)      −142.84 − 346.42     −489.26

Finalmente, calculamos y3 :
                                                                        
                            −8.12           277.68    −8.12 + 27.768      19.65
y3 = y2 + h F(t2 , y2 ) =           + 0.1           =                  =         .
                            71.42           −489.26    71.42 − 48.926     22.49

Es decir: x(0.3) = 19.65, y (0.3) = 22.49.
Se procede de manera similar hasta t = 2 meses.

Universidad de Ingeniería y Tecnología                   Métodos Numéricos   June 1, 2026   11 / 30
Ejemplo de Sistema de EDO (Continuación)
Los resultados usando el método de Euler con h = 0.1 hasta t = 2 meses:
          ti          xi                yi        F (1)       F (2)       xi+1      yi+1
          0          40              9.0000       -120     198.0000     28.0000   28.8000
         0.1      28.0000           28.8000   -361.2000    426.2400     -8.1200   71.4240
         0.2      -8.1200           71.4240    277.8014    -490.8257    19.6601   22.3414
         0.3      19.6601           22.3414   -190.1276    218.8586     0.6474    44.2273
         0.4       0.6474           44.2273    -13.3449     -71.2754    -0.6871   37.0997
         0.5      -0.6871           37.0997    11.7151      -89.4944    0.4844    28.1503
         0.6       0.4844           28.1503     -6.0914     -48.1190    -0.1247   23.3384
         0.7      -0.1247           23.3384     1.2685      -48.4236    0.0021    18.4960
         0.8       0.0021           18.4960     -0.0164     -36.9687    0.0005    14.7992
         0.9       0.0005           14.7992     -0.0028     -29.5941    0.0002    11.8398
         1.0       0.0002           11.8398     -0.0009     -23.6782    0.0001    9.4720


Universidad de Ingeniería y Tecnología              Métodos Numéricos             June 1, 2026   12 / 30
Ejemplo de Sistema de EDO (Continuación)
Los resultados usando el método de Euler con h = 0.1 hasta t = 2 meses:
                 ti         xi              yi      F (1)      F (2)       xi+1     yi+1
                1.1      0.0001          9.4720   -0.0004   -18.9433      0.0001   7.5776
                1.2      0.0001          7.5776   -0.0002   -15.1549      0.0001   6.0621
                1.3      0.0001          6.0621   -0.0001   -12.1241         0     4.8497
                1.4         0            4.8497       0      -9.6993         0     3.8798
                1.5         0            3.8798       0      -7.7595         0     3.1038
                1.6         0            3.1038       0      -6.2076         0     2.4831
                1.7         0            2.4831       0      -4.9661         0     1.9865
                1.8         0            1.9865       0      -3.9729         0     1.5892
                1.9         0            1.5892       0      -3.1783         0     1.2714
                2.0         0            1.2714       0          0           0     1.2714



Universidad de Ingeniería y Tecnología                Métodos Numéricos              June 1, 2026   13 / 30
Ejemplo de Sistema de EDO (Continuación)
                                                            Dinámica de Población de Presas y Depredadores
                                                       40
                                                                                                            Euler




                            Pob. de presas
                                                                                                            RK2 (Heun)
                                                       20                                                   RK4


                                                        0


                                                   -20
                                                            0           0.5           1               1.5                2
                                                                               Tiempo [meses]
                                                       80




                                Pob. de depredadores
                                                                                                            Euler
                                                       60                                                   RK2 (Heun)
                                                                                                            RK4
                                                       40

                                                       20

                                                        0
                                                            0           0.5           1               1.5                2
                                                                               Tiempo [meses]

Universidad de Ingeniería y Tecnología                                            Métodos Numéricos                          June 1, 2026   14 / 30
2   EDO DE
    ORDEN SUPERIOR
Ecuaciones Diferenciales de Orden Superior
Las ecuaciones diferenciales de orden superior son aquellas que contienen
derivadas de una función desconocida de orden mayor o igual a dos. Se expresan
en la forma general:                                        
                           F t, x, x ′ , x ′′ , . . . , x (n) = 0

donde n es el orden de la ecuación. Si la ecuación contiene únicamente la derivada
más alta sin productos entre términos dependientes, se dice que está en su forma
normal:
                          x (n) = f (t, x, x ′ , x ′′ , . . . , x (n−1) ).
Clasificación:
       Lineales: La función F es lineal respecto a x y sus derivadas.
       No lineales: Contienen términos no lineales de x o sus derivadas.
       Homogéneas: No tienen términos independientes.
       No homogéneas: Contienen una función forzante g(t).
Universidad de Ingeniería y Tecnología    Métodos Numéricos             June 1, 2026   16 / 30
Reducción de EDO de orden superior a un sistema de primer orden
En forma general, un PVI de orden n se expresa como:
                                            y (n) = f (t, y , y ′ , y ′′ , . . . , y (n−1) ),
cuyas condiciones iniciales son:
                                                                                                            (n−1)
                 y (t0 ) = y0 ,      y ′ (t0 ) = y0′ ,    y ′′ (t0 ) = y0′′ ,    ...,      y (n−1) (t0 ) = y0       .
Introducimos nuevas variables dependientes:
                              y1 = y ,       y2 = y ′ ,      y3 = y ′′ ,        ...,    yn = y (n−1) .
Derivando, obtenemos el siguiente sistema con sus condiciones iniciales:
                    ′
                   
                    y1 = y2 ,                           y1 (t0 ) = y0 ,
                   
                   
                     y2′ = y3 ,                          y2 (t0 ) = y0′ ,
                   
                   
                   
                   
                   
                     ..
                   
                     .
                   
                                                                          (n−2)
                   
                        ′
                      yn−1 = yn ,                        yn−1 (t0 ) = y0        ,
                   
                   
                   
                   
                   
                                                                      (n−1)
                   
                    ′
                      yn = f (t, y1 , y2 , . . . , yn ), yn (t0 ) = y0       .
Universidad de Ingeniería y Tecnología                            Métodos Numéricos                             June 1, 2026   17 / 30
Ejemplo: EDO de 3◦Orden a S.EDO de 1◦Orden
Consideremos el PVI de tercer orden:
      x ′′′ + 3x ′′ − 2x ′ + 4x = cos(t),              C.I :x(0) = 2,         x ′ (0) = −1,   x ′′ (0) = 3.
Para reducirlo a un sistema de primer orden, definimos:
                                           x1 = x,     x2 = x ′ ,   x3 = x ′′ .
Derivando estas ecuaciones, obtenemos:
                       x1′ = x2 ,        x2′ = x3 ,   x3′ = −3x3 + 2x2 − 4x1 + cos(t).
Así, el sistema equivalente de primer orden es:
                 
                    ′
                 x1 = x2 ,
                                                                              x1 (0) = 2
                  x2′ = x3 ,                                                   x2 (0) = −1
                 
                  ′
                  x3 = −3x3 + 2x2 − 4x1 + cos(t),                              x3 (0) = 3

Universidad de Ingeniería y Tecnología                    Métodos Numéricos                   June 1, 2026    18 / 30
Ejemplo: EDO de 2◦ Orden a S.EDO de 1◦ Orden
Consideremos el PVI de segundo orden:

                         x ′′ + 5x ′ + 6x = e−t ,           C.I :      x(0) = 1,    x ′ (0) = 0.

Para reducirlo a un sistema de primer orden, definimos:

                                                      x1 = x,      x2 = x ′ .

Derivando estas ecuaciones, obtenemos:

                                         x1′ = x2 ,     x2′ = −5x2 − 6x1 + e−t .

Así, el sistema equivalente de primer orden con condiciones iniciales es:
                      (
                        x1′ = x2 ,                x1 (0) = 1
                          ′                 −t
                        x2 = −5x2 − 6x1 + e ,     x2 (0) = 0

Universidad de Ingeniería y Tecnología                          Métodos Numéricos                  June 1, 2026   19 / 30

Ejemplo: EDO de 2◦Orden a S.EDO de 1◦Orden
Solución con Método de RK2 Vectorizado
Aplicamos el método de Runge-Kutta de segundo orden con h = 0.1 para el
sistema:            (
                     x1′ = x2 ,                x1 (0) = 1
                       ′                −t
                     x2 = −5x2 − 6x1 + e ,     x2 (0) = 0
Definimos el sistema en forma vectorial:
                                                         
                         x1                      x2
                    y=      , F(t, y) =
                         x2                −5x2 − 6x1 + e−t

Considerando:
                                         k1 = F(t0 , y0 )
                                         k2 = F(t0 + h, y0 + hk1 )


Universidad de Ingeniería y Tecnología               Métodos Numéricos   June 1, 2026   20 / 30
Ejemplo: EDO de 2◦Orden a S.EDO de 1◦Orden
Solución con Método de RK2 Vectorizado
Para i = 0:
Calculamos los valores de k1 en t0 = 0 con x1 (0) = 1:
                                                          
                             x2 (0)                  0        0
             k1 =                          0  =             =
                    −5x2 (0) − 6x1 (0) + e       −6(1) + 1    −5

Calculamos los valores de k2 en t0 = 0 con x1 (0) = 1, x2 (0) = 0:
                                                                     
                                      x2 (0) + hk1 (2)
             k2 =
                     −5(x2 (0) + hk1 (2)) − 6(x1 (0) + hk1 (1)) + e−h
                                                                     
                                 0 + 0.1(−5)                      −0.5
                k2 =                                          =
                     −5(0 + 0.1(−5)) − 6(1 + 0.1(0)) + e−0.1     −2.5952


Universidad de Ingeniería y Tecnología     Métodos Numéricos              June 1, 2026   21 / 30
Ejemplo: EDO de 2◦Orden a S.EDO de 1◦Orden
Solución con Método de RK2 Vectorizado

Luego calculamos y1 :
                                                                          
                                                           1     1
                                         y1 = y0 + h         k1 + k2
                                                           2     2
                                                           
                                          1
                                      2 ((0) + (−0.5)) 
                                                                      
                          1                                       0.975
                    y1 =     + (0.1)  1                    =
                          0                                      −0.37976
                                         ((−5) + (−2.5952))
                                       2

Es decir: x1 (0.1) = 0.975, x2 (0.1) = −0.37976.



Universidad de Ingeniería y Tecnología                 Métodos Numéricos       June 1, 2026   22 / 30
Ejemplo: EDO de 2◦ Orden a S.EDO de 1◦ Orden
Solución con Método de RK2 Vectorizado
Para i = 1:
Calculamos los valores de k1 en t1 = 0.1 con x1 (0.1) = 0.975:
                                                                        
                    x2 (0.1)                            −0.37976
   k1 =                                  =
         −5x2 (0.1) − 6x1 (0.1) + e−0.1    −5(−0.37976) − 6(0.975) + e−0.1

Evaluando los términos:
                                                                        
                                               −0.37976            −0.37976
                 k1 =                                           =
                                         1.8988 − 5.85 + 0.9048    −3.0464




Universidad de Ingeniería y Tecnología                Métodos Numéricos        June 1, 2026   23 / 30
Ejemplo: EDO de 2◦ Orden a S.EDO de 1◦ Orden
Solución con Método de RK2 Vectorizado
Para i = 1:
Calculamos los valores de k2 en t1 = 0.1 con x1 (0.1) = 0.975, x2 (0.1) = −0.37976:
                                                                          
                                    x2 (0.1) + hk1 (2)
          k2 =
                −5(x2 (0.1) + hk1 (2)) − 6(x1 (0.1) + hk1 (1)) + e−(t1 +h)

Sustituyendo los valores:
                                                                       
                           −0.37976 + 0.1(−3.0464)
  k2 =
         −5(−0.37976 + 0.1(−3.0464)) − 6(0.975 + 0.1(−0.37976)) + e−0.2

Evaluando:                                          
                                              −0.6844
                                         k2 =
                                              −1.3814


Universidad de Ingeniería y Tecnología           Métodos Numéricos   June 1, 2026   24 / 30
Ejemplo: EDO de 2◦ Orden a S.EDO de 1◦ Orden
Solución con Método de RK2 Vectorizado
Luego calculamos y2 :                          
                                      1     1
                        y2 = y1 + h     k1 + k2
                                      2     2
Sustituyendo los valores:
                                                                      
                                            1
                                           ((−0.37976) + (−0.6844))
                                        
                          0.975
                    y2 =          + (0.1)  21
                         −0.37976
                                                                       
                                               ((−3.0464) + (−1.3814))
                                             2
Evaluando los términos:
                                                        
                      0.975              −0.53208    0.92179
              y2 =             + (0.1)            =
                     −0.37976            −2.2139     −0.60115

Es decir: x1 (0.2) = 0.92179, x2 (0.2) = −0.60115
Universidad de Ingeniería y Tecnología       Métodos Numéricos        June 1, 2026   25 / 30
Ejemplo: EDO de 2◦ Orden a S.EDO de 1◦ Orden
Los resultados usando el método de RK2 con h = 0.1 hasta t = 2 meses:
     i       t          x1                   x2       k1 (1)       k1 (2)     k2 (1)       k2 (2)
     0      0.0      1.00000             0.00000    0.00000      -5.00000   -0.50000      -2.5952
     1      0.1      0.97500             -0.37976   -0.37976      -3.0464    -0.6844      -1.3814
     2      0.2      0.92179             -0.60115   -0.60115      -1.7063   -0.77178     -0.57036
     3      0.3      0.85315             -0.71498   -0.71498     -0.80315    -0.7953    -0.043087
     4      0.4      0.77763             -0.75729   -0.75729     -0.20901   -0.77819     0.28608
     5      0.5      0.70086             -0.75344   -0.75344      0.16858   -0.73658     0.47863
     6      0.6      0.62636             -0.72108   -0.72108      0.39666   -0.68147     0.57845
     7      0.7      0.55623             -0.67235   -0.67235      0.52097   -0.62026     0.61664
     8      0.8      0.49160             -0.61547   -0.61547      0.5771    -0.55776     0.61507
     9      0.9      0.43294             -0.55586   -0.55586      0.58826   -0.49704     0.58896
    10      1.0      0.38029             -0.49700       —            —          —            —


Universidad de Ingeniería y Tecnología                  Métodos Numéricos              June 1, 2026   26 / 30
Ejemplo: EDO de 2◦ Orden a S.EDO de 1◦ Orden
                                         Solución de la EDO de Segundo Orden
                        1
                                                                         Solución exacta
                     0.8                                                 Solución Numérica con RK2
                x1
                     0.6

                     0.4
                            0              0.2        0.4              0.6            0.8                  1
                                                            Tiempo
                        0
                                                                                    variable auxiliar
                    -0.2
               x2   -0.4
                    -0.6

                            0              0.2        0.4              0.6            0.8                  1
                                                            Tiempo



Universidad de Ingeniería y Tecnología                      Métodos Numéricos                           June 1, 2026   27 / 30
Conclusiones
       La reducción de ecuaciones diferenciales de orden superior a sistemas de
       primer orden facilita su análisis y resolución numérica.
       El método de Runge-Kutta de segundo orden mejora la precisión respecto a
       Euler, equilibrando exactitud y eficiencia computacional.
       La elección del paso h es crucial en los métodos numéricos, pues influye en la
       estabilidad y precisión de la solución.




Universidad de Ingeniería y Tecnología    Métodos Numéricos            June 1, 2026   28 / 30
Bibliografía
      Steven C. Chapra and Raymond P. Canale
      Métodos numéricos para ingenieros, 7a ed.
      Richard L. Burden and J. Douglas Faires
      Análisis numérico, 7a ed.




Universidad de Ingeniería y Tecnología   Métodos Numéricos   June 1, 2026   29 / 30

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
