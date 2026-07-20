---
curso: IO1
titulo: Semana11-Capitulo4B
slides: 43
fuente: Semana11-Capitulo4B.pdf
---

Investigación de
 operaciones 1

  Algoritmo Simplex
Método Simplex
Método simplex
  •   Inventado por George Dantzig en 1947

  •   Todavía el método más utilizado en programación
      lineal

  •   Permite saber si un programa lineal es factible o no

  •   Permite encontrar una solución óptima si existe

  •   Demuestra que un programa lineal no es acotado
      cuando no lo es

  •   SUPER RAPIDO!
      Método simplex: idea intuitiva

•   Se inicia el algoritmo en cualquier punto extremo.

•   A cada iteración, consideramos los puntos adyacentes del punto
    actual y seleccionamos uno que mejora la solución actual.

•   Iterar hasta que ningún punto adyacente mejore la solución actual.
                                         3
                                                                 x2 % 0   6
                3        2               stop!

                                                         4
                2
                             E       D
                                             C
                1              Espacio
    Max
                     F       de soluciones
                     A                               B
                0            1       2           3       4   5       6

FIGURA 2.1
                      start!
Espacio factible del modelo de Reddy Mikks
         stop!




start!
Primera etapa: forma estándar
                                                              desigualdades


          max    c 1 x1 + c 2 x 2 + · · · + c n xn
          s.t.     a11 x1 + a12 x2 + · · · + a1n xn  b1
                   a21 x1 + a22 x2 + · · · + a2n xn  b2
                                                   ..
                                                    .
                 am1 x1 + am2 x2 + · · · + amn xn  bm
                                       x1 , x2 , . . . , xn   0

                              no-negatividad
Segunda etapa: forma canónica

         a 1 x 1 + a 2 x2 + · · · + a n xn = b
         a 1 x1 + a 2 x2 + · · · + a n xn  b
         a 1 x 1 + a 2 x
  a x + a x + ··· + a x = b
                         2 + · · · + a n x n + s = b,       s
   1 1      2 2             n n
  a 1 x1 + a 2 x2 + · · · + a n xn  b   (m + n)!
  a1 x1 + a2 x2 + · · · + an xn + s = b,   s
                                          m! d! 0
                                      variable de holgura
                                      (m + n)!
                                        (slack variable)
                                       m! d!
    Modelo
 oneladas      completo
          de Tripel
 oneladas de Oscura
mizar z = 5x1 + 4x2

     maximizar z =   5x1   +     4x2
     s.t.            6x1   +     4x2      24
                      x1   +     2x2      6
                                                (1)
                      x1   +        x2    1
                                    x2    2
                               x1 , x2      0
zar z = 5x1 + 4x2                                        desigualdades
    maximizar z =          5x1      +        4x2
    s.t.                   6x1      +        4x2          24
                            x1      +        2x2          6
                                                                    (1)
                            x1      +           x2        1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       <latexit sha1_base64="qyXUht5ZY8mIazZtIfwyx1N7g98=">AAAFlHiclVRtbxw1EPa1HJTjLaUSX/gySogA6djeXtqkH6jUF4GKlEAhlyZSLopmvbN3Vry2ZfvSPR35G/w3fgKf+QOMNy/thUYC39kaz8zzjGdm7cJpFeJg8Gfn1u33uu9/cOfD3kcff/LpZyt3P38V7MxL2pNWW39QYCCtDO1FFTUdOE9YF5r2i5Pnyb5/Sj4oa0Zx7uioxolRlZIYWWVXghgLI6xQvJaCeI0CxC7vQXwlvhGNOBa56PMuScNWCle6sKTbuJIeiG8ZDcwXeJ0xK7YWKzTvJLP/zTrg1XE8JWq2j/nXe2fMt7kie9aiYMxfLcN/486OV9YG2Va+sbk5gEE2eJQPh5tJ2Hq4kQ8hzwbtWBMX4+Xx3dt/jEsrZzWZKDWGcJgPXTxaoI9KajrrjWeBHMoTnNBiQram6OdncG2swy4RXJozV1YQLWhCbyBOCTTO7SyCdakZIYPRlDwB8tQ2hqw3voQuNMVI3qEj/68obaAsy8B6wAetTys+vBKTsbf+FhuaMki2vuPET2VUpxgJKgam6W3kbQmOU73KhdneFODQoa+U1kcLFsKJcmfXqDjpgibKMIfHiUc3DfBaxSmgAapdnEP6fsEjF8VzZVjNf2VKrv5ypRNWyWa5/liHMK+Ls15vHfb5HPCbLcjHYM3XgVMwMTiSWeAwkmkLAsaW6VBB1XzJqnnrBHJqlSQu+zqMLFDDxVOp/31uEBm4/9Sx8/nFCfd/TIhn1p4kHmqwTgmknrbxwHl7qkqOYg3soIRfduGgz8RceI6Dhku5+sJSpTnfETVxNdGgmYOtEkugN6dZSvUym36jYxM99puZUdKW6YssqcKZjsmlIowzT2Gxg84pM3kcqfmOZ2S3wP2zNZrkd3jdfrQYkWYew13bVpNphJ8ictbnuIAmtLBdiZoe72CU0237mrzkJ6j//7hqfn5u5LoZyjf58rrCzcKrYZYPsvzX4dqTZxd3+o74Uqzy65KLLfFEvBAvxZ6Qne2O7yw6v3e/6H7ffd794dz1VucCc08sje7P/wC+O6ig</latexit>




                                                x2        2
                                           x1 , x2          0

       introducción de                                                <latexit sha1_base64="pUSN/R++RE9Avr00GBm/kHf90gQ=">AAAFlHiclVTbbhs3EKWSqknVS5wWyEteBnaNtoCy0cqJnYcGyAUtUsBu01qODViGMeLOSoS5JEFSzgqKf6P/1k/oc3+gw7XlVG4MtFyRGs7MOcOZWe7IaRVir/dH68bNj9of37r9SefTzz7/4s7K3S/fBDv1kvak1dYfjDCQVob2ooqaDpwnrEaa9kcnL5N9/5R8UNYM4szRUYVjo0olMbLKrgQxFEZYoXgtBPEaBYhd3oP4WnwranEsctHlXZL64jvWAvsFXqfsjfwfGK95Jxn1F+uAV8c8SlRsH/LT+SBXt8EudGFJt3EpPVqKGZmxEiPm/rOJ9N/OkB2vrPWyrXxjc7MHvaz3JO/3N5Ow9Xgj70Oe9ZqxJi7G6+O7N38fFlZOKzJRagzhMO+7eDRHH5XUdNYZTgM5lCc4pvmYbEXRz87gyliHXSJYmDNXlBAtaEJvIE4INM7sNIJ1qRkhg8GEPAHy1DaGrDNcQOeaYiTv0JH/V5QmUJZlYD3go8anER9fisnYWf8HG5oiSLZ+4MTPZVSnGAlKBqbpbeRtAY5TvcyF2d4X4NChL5XWR3MWwolyZ1eoOOkRjZVhDo9jj24S4K2KE0ADVLk4g/T+gkcuiufKsJp/yhRc/eVKJ6yS9XL9sQphVo3OOp112OdzwG92RD4Ga74JnIKJwZHMAoeRTDsiYGyRDhVUxZesnDVOICdWSeKyr8PAAtVcPJX63+UGkYGHzx07n1+c8PDHhHhh7UnioRqrlEDqaRMPnLenquAo1sAOSvhlFw66TMyF5zhouJSrryyVmvMdUB1XEw2aGdgysQR6f5qlVBfZdGsd6+ixW0+NkrZIb2RBJU51TC4lYZx6CvMddE6Z8dNI9QOekd0C989WaJLf4VX70XxAmnkMd21bjScRforIWZ/jAprQwHYlanq6g1FOtu1b8pI/Qd3/x1Xx5+daruuhfJMX1xWuF970s7yX5b/21569uLjTt8V9scpfoVxsiWfilXgt9oRsbbd8a956177X/r79sv3DueuN1gXmK7E02j//DUOCqKA=</latexit>




     variables de holgura

                     maximizar z = 5x1 + 4x2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                (10)
                                                                igualdades
                    B. Meuhr      Hello World!

                            6x1 + 4x2 + s1 = 24                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             (11)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   s1 = 24    6x1      4x2 ,
                               x1 + 2x2 + s2 = 6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            (12)   s2 = 6    x1     2x2 ,
                                x1 + x2 + s 3 = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           (13)   s 3 = 1 + x1     x2 ,
                                         x2 + s 4 = 2              reescritura
                                                                         (14)   del                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                s4 = 2    x2 ,
                       x1 , x2 , s 1 , s 2 , s 3 , s 4    0       problema
                                                                         (15)cómo un
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   z = 5x1 + 4x2 .
                                                                     sistema de
                                                                     ecuaciones
                                             3I (X , X , X ) ESUNASOLUCI±N±PTIMA
                                                               3ECTION4ITLE
                                             (X , X , X , S , S , S , S ) ESTAMBIªNUNASOLUCI±N±PTIMA
                                             (, , , , , ) ESUNASOLUCI±NNO±PTIMA 
   s1 = 24        6x1        4x2 ,                       (5) 4HEQUICKBROWNFOXJUMPSOVERTH
   s2 = 6        x1       2x2 ,               es una(6)   solución factible
   s 3 = 1 + x1           x2 ,                           (7)
   s4 = 2        x2 ,                                     
                                                         (8)     3ECTION4ITLE
    z = 5x1 + 4x2 .                                      (9) Intentamos aumentar x1 sin
                                                               4HEninguna
                                                                que     QUICKBROWN        FOXJUMPSOVERTH
                                                                                  variable de
                                                               Xholgura
                                                                   =     , sea
                                                                             X  = negativa
                                                                                    .
                                                          3I (X , X , X , S , S , S , S ) ESUNASOLU
                                                           ¿de cuánto podemos
Aumentar x1 de 1                                            X , X , X )x1?
                                                          (aumentar        ESTAMBIªNUNASOLUCI±N±
 aumenta z de 5                                           3I (X , X , X ) ESUNASOLUCI±N±PTIMA
                               Aumentar  x2 de  1
                                                          (X , X , X , S , S , S , S ) ESTAMBIªNUN
      B. Meuhr          Hello World!
                                 aumenta z de 4           (, , , , , ) ESUNASOLUCI±NNO±
                                                          X = MIN(/, /) = 
                                                                                                                 x1         % 0    5
                                                                                             3

    3ECTION4ITLE
 3ECTION4ITLE
                                                                        2
                                                              x 1 = 4 3 x2
                                                                        3
                                                                                 1
                                                                                 62
                                                                                   s1 ,                  (16)
                                                                                                                          x2 % 0   6

         s1 = 24 6x1 4x2 ,                                            (5)
                                                                        4        1
                                                              s2 = 2      x2 + s 1 ,                     (17)4
       4HE
         s2         QUICKBROWN
                = 6 x1                  2x2 ,
4HE QUICKBROWN FOXJUMPSOVERTHELAZYDOG        FOXJUMPSOVERTHELAZYDOG
                                                                      (6)
                                                                      2 3        6
                                                                        5        1 E          D
X = Xs,3X=   =
                 = 
                    1  ,+
                         X
                          . x 1 =     x .
                                           2 
                                             ,                s 3 = 5 (7)
                                                                        3
                                                                          x  2
                                                                                 6
                                                                                   s 1 ,
                                                                                                   C
                                                                                                         (18)
3I (X3I,sX4(,=XX2,, X
                        S ,x,S2X,, ,S
                                         S,S, S)ESUNASOLUCI±N±PTIMA
                                                   ,  , S ) s4 = 2 1(8)
                                                             ESUNASOLUCI±N±PTIMA
                                                                        x2 ,             Espacio         (19)
                                                                               F     de soluciones
(X , X( ,XzX,=)XESTAMBIªNUNASOLUCI±N±PTIMA
               , 1X ) 2          ESTAMBIªNUNASOLUCI±N±PTIMA
                    5x      +     4x     .                            (9)2         5
                                                               z = 20 + xA     2     s1 .                (20)
3I (X , X , X ) ESUNASOLUCI±N±PTIMA                                3         6                     B
       3I     (  X  ,  X    ,  X    )   ESUNASOLUCI±N±PTIMA
(X , X , X , S , S , S , S ) ESTAMBIªNUNASOLUCI±N±PTIMA          0               1       2      3       4        5       6        6
                         
     ( X  , X  , X  , S  , S   , S   , S
(, , , , , ) ESUNASOLUCI±NNO±PTIMA
                                            ) ESTAMBIªNUNASOLUCI±N±PTIMA
                                                                
                                              FIGURA 2.1
     (, , , , , ) ESUNASOLUCI±NNO±PTIMA                  la nueva
                                              Espacio factible del modelo
                                                                                 
                                                                                solución
                                                                          de Reddy  Mikks es
                                                                                                 2
                                                                                             x1 = 4x2
                                                                                                         1
                                                                                                           s1 ,
                                                                                                 3       6
     X = MIN(/, /) =                                              (4, 0, 0, 2, 5, 2)      4       1
                                                                                       s2 = 2      x2 + s 1 ,
                                              B. Meuhr   Hello World!                            3       6
   si aumentamos de 4, la primera                      Para tener en cuenta las otras cuatro 5 restricciones,
                                                                                                         1      prim
                                                                                       s3 = 5      x2      s1 ,
     variable
         B. Meuhrde holgura
                    Hello World! se anula        gualdad con una ecuación, y luego trace la línea3 recta 6 resultan
                                                 diferentes. Por ejemplo, después de s4 =
                                                                                      sustituir
                                                                                             2 6xx21, ! 4x2 # 24 co
                                                 "  24, se determinan  dos
                                 por substitución, el sistema se reescribe:puntos  distintos  haciendo
                                                                                                   2     x 5
                                                                                                           1 "    0 pa
                                                                                        z =2420 + x2         s1 .
                                                 y luego que x2 " 0 para obtener x1 = 6 = 4.3 De este      6 mod
                                            1         1
                                    x1 = 3     s1 + s2 ,                        (21)
                                            4         2                                                      4
                                         3 1          3             2
                                    x2 = + s 1           s2 ,                      E
                                                                                (22)     D
                                         2 8          4
         2     1                         5 3(16) 5                                               C
x1 = 4     x2    s1 ,               s3 =        s1 + s2 ,           1           (23) Espacio
         3     6                         2 8          4                     F    de soluciones
         4     1                    s4 =
                                         1 1
                                                s   +
                                                      3
                                                         s
s2 = 2     x2 + s 1 ,                    2 8(17) 4
                                                  1        2 ,              A (24)                       B
         3     6
                               Intentamos    aumentar
                                              3         1      x2   0             1       2          3       4
         5     1                     z = 21      s1
                                              4(18) 2
                                                          s2 .                  (25)
s3 = 5     x2    s1 ,                              FIGURA 2.1
         3     6                                                       la nueva solución es
                               podemos aumentar      x2
                                              Espacio factible del modelo(3,
                                                                          de1.5,
                                                                             Reddy  Mikks
s 4 = 2 x2 ,                                (19)                                 0, 0, 2.5, 0.5)
                               de 1.5 (¿porqué?)
          2      5                                                                      1       1
 z = 20 + x2       s1 .                          (20)                          x1 = 3     s1 + s2 ,
          3      6                                                  Para tener en cuenta4 las 2otras cuatro r
                                        B. Meuhr Hello World!
                                                                                    3 1 y luego
                                                              gualdad con unax2ecuación,         3 trace la lí
                                                                                  = + s1           s2 ,
                           por substitución, el sistema se diferentes.
                                                               reescribe:           2 después
                                                                          Por ejemplo,  8        4de sustituir
                                                                                    5 3          5
                                                              " 24, se determinan
                                                                               s3 = dos s
                                                                                        puntos     distintos ha
                                                                                            1 + s2 ,
                            Todos los coeficientes de la variables                  2   8        4
                                                                                                             24
                                                              y luego que x2 " 0 1 para 1
                                                                                        obtener  3 x1 = 6 =
                                de holgura en z son negativos                  s4 =        s1 + s2 ,
                                                              que pasa por los puntos
                                                                                    2 (0,6)
                                                                                        8      y 4(4,0) es la lí
                                       -> TERMINADO!                A continuación        3
                                                                                    consideramos  1
                                                                                z = 21      s1      s2 .el efecto
   B. Meuhr   Hello World!                                                                4       2
                                                              (x , x ) en dos semiplanos, uno a cada lado
                                                                    1   2
                      1                                 x2 # 2    4
     4
     Variable de salida <–>
                        3   Variable de entrada
                                        x1    % 0                 5
                                                                                Para pasar de una solución
                                                        x2 % 0    6
     3                                                                          básica a otra solución básica se
              2
                                                  Solución básica 3:            necesita un intercambio entre
                                              4   (3, 1.5, 0, 0, 2.5, 0.5)      variables básicas y variables no
     2
                  E       D                              óptima!                básicas
                                  C
     1              Espacio                       ¿cuál variable entra en la base?
          F       de soluciones                       ¿cuál sale de la base?
          A                               B
                                                    Solución básica 6
                                                                         2 x1
     0            1       2           3       4     5      6
                                                      (4, 0, 0, 2, 5, 2)

   Solución
ible          básica
     del modelo        1: Mikks
                de Reddy
    (0, 0, 24, 6, 1, 2)
                            x1 entra en la base
       Para tener en cuenta slas otras
                              1 sale decuatro restricciones, primero sustituya cada desi-
                                        la base
  gualdad con una ecuación, y luego trace la línea recta resultante localizando dos puntos
  diferentes. Por ejemplo, después de sustituir 6x1 ! 4x2 # 24 con la línea recta 6x1 ! 4x2
                                                                                    24
  " 24, se determinan dos puntos distintos haciendo x1 " 0 para obtener x2 =           = 6
                 x3                              FIGURA   3.4
                                              ¿Cuáles de los siguientes pares de
                                                 Espacio
                                              puntos      de soluciones
                                                      extremos            del problema 3,
                                                                  no pueden
                                                 conjunto 3.2b
                                              representar   iteraciones simplex
                                  G           sucesivas: (A, B), (B, D), (E, H) y (A, I)?
                  D

             J            H
     F
                              B
                                             x1
                 A
                      I
                              A: (0, 0, 0)
                              B: (1, 0, 0)
         C            E       C: (0, 1, 0)
                              D: (0, 0, 1)
x2
                 x3                                  FIGURA 3.4
                                                  Suponga    que  las iteraciones
                                                     Espacio de soluciones del problema 3,
                                                  simplex se  inician
                                                     conjunto 3.2b     en A y que el
                                  G               óptimo ocurre en H. Indique si
                  D                               alguna de las siguientes
                                                  trayectorias son no legítimas
                          H                       para el algoritmo simplex, y
             J
     F                                            explique la razón:
                              B
                                             x1             (i) A–B–G–H
                 A
                      I                                     (ii) A–E–I–H
                              A: (0, 0, 0)                  (iii) A–C–E–B–A–D–G–H
                              B: (1, 0, 0)
         C            E       C: (0, 1, 0)
                              D: (0, 0, 1)
x2
                 x3                                           FIGURA    3.4
                                                            Si s1, s2, s3 y s4 son las variables
                                                            deEspacio
                                                                holguradeasociadas
                                                                           soluciones del problema 3,
                                                                                      a las
                      s3                s4                    conjunto 3.2b representadas por
                                                            restricciones
                                            G               los planos CEIJF, BEIHG, DFJHG e
                  D                                         IJH, respectivamente, identificar
                                                            las variables básicas y las
             J                      H           s2          variables no básicas en cada
     F
                                                            punto extremo.
                                        B
                                                       x1
                 A
                                I
                                        A: (0, 0, 0)
                                        B: (1, 0, 0)
         C                 E            C: (0, 1, 0)
                                        D: (0, 0, 1)
x2                         s1
                 x3                            FIGURA 3.4
                                              Espacio de soluciones del problema 3,
                                              conjunto
                                             Para  cada3.2b
                                                         una de las funciones
                                  G          objetivo abajo, cuál es la variable
                  D                          de entrada en la base? Con cuál
                                             valor entra en la base?
             J            H
     F                                 5. Para cada una de las funciones objetivo dadas y
                              B           seleccione la variable no básica que conduce al s
                                          x1
                 A                        termine la mejora asociada de z.
                      I
                              A: (0, 0, 0)    1)
                                           *(a)  Maximizar z = x1 - 2x 2 + 3x3

                              B: (1, 0, 0) (b)2) Maximizar z = 5x1 + 2x2 + 4x3
         C            E       C: (0, 1, 0) (c)3) Maximizar z = - 2x1 + 7x2 + 2x3
                              D: (0, 0, 1) (d)4) Maximizar z = x + x + x
                                                                1    2     3
x2
re el espacio de soluciones bidimensional que se muestra en la figura 3.6.
              Si las iteraciones simplex se inician en el punto A, identifique la trayectoria que co
onga que la función      objetivo   es
              duce al punto E óptimo.
                   x2                   Maximizar z = 3x1 + 6x2
               4
as iteraciones simplex se inician en el punto A, identifique la trayectoria que c
e al punto E3 óptimo.
                                                        Si el simplex se inicia en el punto
               2                                        A, ¿cuál es la trayectoria que
                        F           E
                                        D               conduce al punto E óptimo?
               1
                    G                   C
                    A       B
                                                        x1
         !1    0        1       2           3   4   5
                                                             FIGURA 3.6
              !1                                             Espacio de soluciones para el
    F         E                                              problema 7, conjunto 3.3b
                    D
bilidad, y el cambio del valor de z, suponiendo que la iteración inicial ocurre
               Si las iteraciones simplex se inician en el punto A, identifique la trayectoria que co
nto A y que la     función    objetivo
               duce al punto E óptimo.
                                         la  da
                   x2                   Maximizar z = 4x1 + x2
               4
ta (b), suponiendo que la función objetivo fuera
               3
                                        Maximizar z = x1 + 4x2 la variable de entrada
                                                       Determine
                                                           y el cambio del valor de z,
               2
e la siguiente PL: F                E                      suponiendo que el punto inicial es
                                        D
                                                           el punto A
               1            Maximizar z = 16x  + 15x
                    G           C            1      2
                    A       B
                                                           x1
         !1    0        1       2           3    4    5
                                                                FIGURA 3.6
              !1                        40x1 + 31x2 … 124 Espacio de soluciones para el
                                                                problema 7, conjunto 3.3b
                                         -x1 +       x2 … 1

                                                                1   2
               Si las iteraciones simplex se inician en el punto A, identifique la trayectoria que co
onsidere la siguiente   PL:
               duce al punto E óptimo.
                   x2               Maximizar z = 16x1 + 15x2
               4
jeto a
               3                        40x1 + 31x2 … 124
                                                       Determine la variable de entrada
               2
                                        -x1 +      x2 …y 1el cambio del valor de z,
                        F       E                      suponiendo que el punto inicial es
                                    D      x1         …el3punto A
               1
                    G               C       x 1, x 2 Ú 0
                    A       B
                                                           x1
) Resuelva
        !1 el0 problema
                    1    mediante
                          2     3   el 4método
                                            5 simplex, donde la variable de entrada es
                                                     FIGURA 3.6
  la variable no básica con el coeficiente más negativo en la fila z.
           !1                                        Espacio de soluciones para el
) Resuelva el problema mediante el algoritmo simplex,   seleccionando     siempre
                                                     problema 7, conjunto 3.3b     la variab
  de entrada como la variable no básica con el coeficiente menos negativo en la fila z.
Ejemplo en dimensión 3 (sin gráfico)

              max    5x1 + 4x2 + 3x3
              s.t.    2x1 + 3x2 + x3  5
                      4x1 + x2 + 2x3  11
                     3x1 + 4x2 + 2x3  8
                           x1 , x2 , x3   0
max    5x1 + 4x2 + 3x3
                                               max 5x1 + 4x2 + 3x3
s.t.    2x1 + 3x2 + x3  5
                                               max
                                               s.t.   5x 1 +  4x 2 + 3x
                                                        2x1 + 3x2 + x3  3
        4x1 + x2 + 2x3  11                 Introducción de
       3x1 + 4x2 + 2x3  8                     s.t. de2x
                                            variables   4x 1 + 3x
                                                        holgurax2 2++2xx3
             x1 , x2 , x3     0                        3x4x1 1++4xx2 + 2x3
                                                       3x1 + 4x12,+  x22x
                                                                       , 3
                                                               x1 , x2 , x3
                            2x1 + 3x2 + x3 + w1 = 5,     w1    0
                            2x1 + 3x2 + x3 + w1 = 5,     w1    0
                            w1 = 5 2x1 + 3x2 + x3 ,      w1    0
max    5x1 + 4x2 + 3x3
s.t.    2x1 + 3x2 + x3  5
        4x1 + x2 + 2x3  11
       3x1 + 4x2 + 2x3  8
             x1 , x2 , x3   0
                                max    ⇣ = 5x1 + 4x2 + 3x3
                                s.t.   w1 = 5          2x1       3x2      x3
                                       w2 = 11           4x1       x2     2x3
                                       w3 = 8          3x1       4x2      2x3
                                       x1 , x 2 , x 3 , w 1 , w 2 , w 3   0
max    ⇣ = 5x1 + 4x2 + 3x3
s.t.   w1 = 5          2x1       3x2      x3
       w2 = 11           4x1       x2     2x3
       w3 = 8          3x1       4x2      2x3
       x1 , x 2 , x 3 , w 1 , w 2 , w 3   0

                                                Solución factible inicial?

                                                     (0, 0, 0, 5, 11, 8)
max    ⇣ = 5x1 + 4x2 + 3x3
s.t.   w1 = 5          2x1       3x2      x3
       w2 = 11           4x1       x2     2x3
       w3 = 8          3x1       4x2      2x3
       x1 , x 2 , x 3 , w 1 , w 2 , w 3   0

                                              Que variable debería entrar
                                                      en la base?
max    ⇣ = 5x1 + 4x2 + 3x3
s.t.   w1 = 5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               2x1    3x2   x3
       w2 = 11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               4x1    x2   2x3
       w3 = 8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               3x1    4x2   2x3
       x1 , x 2 , x 3 , w 1 , w 2 , w 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  0

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Que variable debería salir de
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        la base?
       <latexit sha1_base64="4nq/aKtn/T8k0zvEKjCyAojR9cY=">AAAE+HiclVPBbhRHEB1gCWQJwZBjLiUbKxyWYWeNbS6WgEgIIqwQvMaWvJZV21Oz23JPd6u718xmNL+RMzfELcrHIHEin0L1rg3YxIe0pqXqqapX/V5VD62SPnS7Hy5cvNS6/N2Vq9+3r/1w/ccbCzdvvfJm4gRtC6OM2x2iJyU1bQcZFO1aR1gOFe0MD3+N/p0jcl4a3Q9TS/sljrQspMDAvw4WfhtoI3VOOsDt6iCDDSilHtSDwqGoV5u613Rgfsiypr7fdOaHB0290gyaja/ibh8sLHXT9Wxlba0L3bT7IOv11qKxvrqS9SBLu7O1lByvFwc3L/01yI2YlFxdKPR+L+vZsF+jC1IoatqDiSeL4hBHVI/IlBTctIEzaxm2iODEndq8gGBAEToNYUygcGomAYyNhH0K/TE5AuStTPBpe3CSWisKgZxFS+6bKrNCaZqCcYD3ZzEzc/WzGZ3t5a/QUOdesPc/bvxIBHmEgaDgxLidCXzMwTLVz1wY7YsAexZdIZXar9nwh9I2Z6CY9JBGUjOGw5FDO/bwWoYxoAYqbZhCnBFwyKI4VoZ/8zfv/WmlY64U1Wn9sfR+Wg6bdnsZdvge8NIMyQVv9C+eKejgLYnUcxnBsEMCzs3jpbwseZCL6SwIxNhIQSz7MvQNUMXiydj/DjeINNx7ZDl4Ppz+3pOY8diYw4hDFZaRQOzprB5YZ45kzlWMhk0U8PsW7HYYmIXnOqhZysWnhgrFfPtUhcUIg3oKpogonr7c5hTVEzadSoUqOOxUEy2FyeNE5lTgRIUYUhCGiSNfb6K1Uo82AlV3eQcO89w/U6KOcXtn/ft1nxTjaO7aczkaB3gWkFnP8zxqP0vbEqhoYxODGD83r8kJfuad/4dVGm3OxTo/lV/yyXOF841XvTTrptkfvaWHj4/f9NXk52QxuZNkyXryMHmavEi2E5H8nbxPPib/tv5svWm9bb2bh168cJzzU3Jqtf75BHrjnxU=</latexit>
max    ⇣ = 5x1 + 4x2 + 3x3
s.t.   w1 = 5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               2x1    3x2   x3
       w2 = 11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               4x1    x2   2x3
       w3 = 8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               3x1    4x2   2x3
       x1 , x 2 , x 3 , w 1 , w 2 , w 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  0

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               Que variable debería salir de
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          la base?
       <latexit sha1_base64="4nq/aKtn/T8k0zvEKjCyAojR9cY=">AAAE+HiclVPBbhRHEB1gCWQJwZBjLiUbKxyWYWeNbS6WgEgIIqwQvMaWvJZV21Oz23JPd6u718xmNL+RMzfELcrHIHEin0L1rg3YxIe0pqXqqapX/V5VD62SPnS7Hy5cvNS6/N2Vq9+3r/1w/ccbCzdvvfJm4gRtC6OM2x2iJyU1bQcZFO1aR1gOFe0MD3+N/p0jcl4a3Q9TS/sljrQspMDAvw4WfhtoI3VOOsDt6iCDDSilHtSDwqGoV5u613Rgfsiypr7fdOaHB0290gyaja/ibh8sLHXT9Wxlba0L3bT7IOv11qKxvrqS9SBLu7O1lByvFwc3L/01yI2YlFxdKPR+L+vZsF+jC1IoatqDiSeL4hBHVI/IlBTctIEzaxm2iODEndq8gGBAEToNYUygcGomAYyNhH0K/TE5AuStTPBpe3CSWisKgZxFS+6bKrNCaZqCcYD3ZzEzc/WzGZ3t5a/QUOdesPc/bvxIBHmEgaDgxLidCXzMwTLVz1wY7YsAexZdIZXar9nwh9I2Z6CY9JBGUjOGw5FDO/bwWoYxoAYqbZhCnBFwyKI4VoZ/8zfv/WmlY64U1Wn9sfR+Wg6bdnsZdvge8NIMyQVv9C+eKejgLYnUcxnBsEMCzs3jpbwseZCL6SwIxNhIQSz7MvQNUMXiydj/DjeINNx7ZDl4Ppz+3pOY8diYw4hDFZaRQOzprB5YZ45kzlWMhk0U8PsW7HYYmIXnOqhZysWnhgrFfPtUhcUIg3oKpogonr7c5hTVEzadSoUqOOxUEy2FyeNE5lTgRIUYUhCGiSNfb6K1Uo82AlV3eQcO89w/U6KOcXtn/ft1nxTjaO7aczkaB3gWkFnP8zxqP0vbEqhoYxODGD83r8kJfuad/4dVGm3OxTo/lV/yyXOF841XvTTrptkfvaWHj4/f9NXk52QxuZNkyXryMHmavEi2E5H8nbxPPib/tv5svWm9bb2bh168cJzzU3Jqtf75BHrjnxU=</latexit>




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Nueva solución
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     (5/2, 0, 0, 0, 1, 1/2)
                     Entra
                                           Pivot
                                                                Podemos reescribir x1 en
max    ⇣ = 5x1 + 4x2 + 3x3                                       función de las nuevas
                                                                  variables no básicas
s.t.   w1 = 5          2x1       3x2        x3                  5       1        3         1
                                                           x1 = 2         w
                                                                        2 1        x
                                                                                 2 2         x
                                                                                           2 3
Sale
       w2 = 11           4x1       x2       2x3
                                                           …y no sólo x1, sino también todas
       w3 = 8          3x1       4x2        2x3                  las variables básicas
                                                                                 max       ⇣ = 5x
                                5         1         3     1
                           x1 = 2           w
                                          2 1         x
                                                    2 2     x
                                                          2 3
       x1 , x 2 , x 3 , w 1 , w 2 , w 3         0                                s.t.      w1 =
                                            max       ⇣ = 12.5     2.5w1
                                                                                        w
                                                                              3.5x + 0.5x 2 =
                                                                                  2          3
                                                                                           w3 =
                                            s.t.      x1 = 2.5     0.5w1      1.5x2     0.5x3
                                                                                           x1 , x 2 ,
                                                      w2 = 1 + 2w1 + 5x2
                                                      w3 = 0.5 + 1.5w1 + 0.5x2          0.5x3
5   1        3      1
2     w
    2 1        x
             2 2      x
                    2 3



      max      ⇣ = 12.5          2.5w1           3.5x2 + 0.5x3
      s.t.     x1 = 2.5         0.5w1            1.5x2   0.5x3
               w2 = 1 + 2w1 + 5x2
               w3 = 0.5 + 1.5w1 + 0.5x2                  0.5x3
               x 1 , x2 , x3 , w 1 , w 2 , w 3     0
                                                                 Variable de entrada?
                                                                   Variable de salida?
                                                                        Pivot?
max    ⇣ = 12.5          2.5w1           3.5x2 + 0.5x3
s.t.   x1 = 2.5         0.5w1            1.5x2   0.5x3
       w2 = 1 + 2w1 + 5x2
       w3 = 0.5 + 1.5w1 + 0.5x2                  0.5x3
                  x3 = 1 + 3w1 + x2                      2w3
       x 1 , x2 , x3 , w 1 , w 2 , w 3     0


                                                  max      ⇣ = 13   w1    3x2   w3
                                                  s.t.     x1 = 2   2w1   2x2 + w3
                                                           w2 = 1 + 2w1 + 5x2
                                                           x3 = 1 + 3w1 + x2    2w3
                                                           x ,x ,x ,w ,w ,w      0
 De manera general, un
P.L. en forma estándar
 se puede escribir así

       x3 = 1 + 3w1 + x2        2w3

                                 n
                                 X
                         max           c j xj
                                 j=1
                                 Xn
                         s.t.          aij xj  bi   i = 1, . . . , m
                                 j=1

                                 xj     0            j = 1, . . . , n
       n
       X
max          c j xj
                                                         Hasta ahora, el
       j=1
        n                                             diccionario inicial se ha
       X
s.t.         aij xj  bi   i = 1, . . . , m           obtenido asignando el
       j=1
                                                        valor 0 a todas las
                                                     variables x y el valor bi a
       xj     0            j = 1, . . . , n              cada variable wi


       Eso es válido solo si                       n
                                                   X
        los valores bi son              max   ⇣=         c j xj
       todos no-negativos                          j=1
                                                            n
                                                            X
                             s.t.
 Que hacemos si no es el caso?                wi = b i             aij xj   i = 1, . . . , m
                                                             j=1
       n
       X
max          c j xj
       j=1
       Xn
s.t.         aij xj  bi   i = 1, . . . , m
       j=1

       xj     0            j = 1, . . . , n   Trabajamos temporalmente con
                                              un problema auxiliar para el cual:

                                               1. Es fácil encontrar una solución
                                                  factible
                                               2. Una solución óptima
                                                  proporciona un diccionario
                                                  factible para el problema
                                                  original
       n
       X
max          c j xj
       j=1
                                               <- problema original
       Xn
s.t.         aij xj  bi   i = 1, . . . , m
       j=1

       xj     0            j = 1, . . . , n


            problema auxiliar ->       max          x0
                                               0                  1
                                                    n
                                                    X
                                        s.t.   @             aij xj A   x0  b i   i = 1, . . . , m
                                                    j=1

                                               xj        0                         j = 0, . . . , n
max          x0
         0                 1
             n
             X
s.t.     @            aij xj A   x0  b i   i = 1, . . . , m
             j=1

        xj        0                         j = 0, . . . , n


       El problema
       original tiene una                            En otras palabras:
       solución factible                             El problema original tiene una
       ssi el problema                               solución factible ssi la solución
       auxiliar tiene una                            óptima del problema auxiliar tiene
       solución factible                             un valor objetivo igual a 0.
       con x0 = 0
Ilustración

max      2x1       x2 <- problema original
 s.t.    x1 + x2           1
        x1      2x2        2
                 x2  1
             x1 , x 2   0                    problema auxiliar ?
Ilustración

max      2x1       x2 <- problema original
 s.t.    x1 + x2           1           max        x0
        x1      2x2        2
                                        s.t.       x1 + x 2      x0        1
                 x2  1
                                                  x1    2x2      x0        2
             x1 , x 2   0        problema auxiliar ->    x2      x0  1
                                                        x0 , x1 , x2    0
Ilustración                                    max    ⇠=     x0
                                               s.t.   w1 =     1 + x1   x 2 + x0
problema auxiliar ->
     max         x0                                   w2 =     2 + x1 + 2x2 + x0
                                                      w3 = 1      x2 + x0
      s.t.       x1 + x 2       x0        1
               x1      2x2      x0        2          Diccionario no factible, pero…

                        x2      x0  1
                                                      aplicamos un pivote donde
                       x0 , x1 , x2    0              x0 entra en la base y
                                                      donde la variable más
                                                      “infactible” sale

max    ⇠=     x0
s.t.   w1 =     1 + x1   x 2 + x0
       w2 =     2 + x1 + 2x2 + x0
                                           Resultado:
       w3 = 1      x2 + x0
                                    max      ⇠=     2 + x1 + 2x2       w2
       Diccionario no factible,
       pero…                        s.t.     w1 = 1       3x2 + w2
       Aplicamos un pivote donde             x0 = 2      x1    2x2 + w2
       x0 entra en la base y                 w3 = 3       x1    3x2 + w2
       donde la variable más
       “infactible” sale                                …un diccionario factible
    Después de 2 otros pivotes:
                                               Eliminamos los x0 y
x   ⇠=0     x0                                 reemplazamos la función
                                               objetivo auxiliar con la función
.   x2 = 0.33    0.33w1 + 0.33w2               objetivo original: obtenemos
    x1 = 1.33    x0 + 0.67w1 + 0.33w2          un diccionario inicial factible
                                               para el problema original:
    w3 = 0.67 + x0 + 0.33w1       0.33w2
                                       max     ⇣=     3    w1    w2
                                        s.t.   x2 = 0.33     0.33w1 + 0.33w2
    Función objetivo del                       x1 = 1.33 + 0.67w1 + 0.33w2
    problema original: ζ = − 2x1 − x2          w3 = 0.67 + 0.33w1        0.33w2
                                                                ¿Sólo factible?
                    ar …
              c tic
         p ra
 a r a
P


                               Simple Pivot Tool


                https://neos-guide.org/content/simple-pivot-tool

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
