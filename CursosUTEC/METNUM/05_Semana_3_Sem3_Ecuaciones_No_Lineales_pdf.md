---
curso: METNUM
titulo: 05 - Semana 3/Sem3_Ecuaciones No Lineales
slides: 49
fuente: 05 - Semana 3/Sem3_Ecuaciones No Lineales.pdf
---

Métodos Numéricos
Ecuaciones No Lineales - S3
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
                                         1 Métodos Cerrados
                                         2 Métodos Abiertos




Universidad de Ingeniería y Tecnología   Métodos Numéricos    1 / 48
        Objetivos
            Localizar y delimitar raices mediante métodos gráficos y analíticos
            Resolver ecuaciones no lineales con Bisección Newton y Punto Fijo
            Determinar convergencia y eficiencia de métodos cerrados y abiertos




Universidad de Ingeniería y Tecnología              Métodos Numéricos             2 / 48
1   MÉTODOS
    CERRADOS
Problema
Dada f una función real con valores reales (es decir f : R → R) nos interesa
encontrar al menos una raíz de la ecuación:

                                         f (x) = 0

Es decir, interesa encontrar x̂ ∈ R tal que f (x̂) = 0.
En algunos casos, la ecuación se puede resolver de forma analítica y obtener la
raíz exacta, pero, para la gran mayoría de las ecuaciones encontrar raíces es
complicado y debe hacerse de manera numérica.




Universidad de Ingeniería y Tecnología          Métodos Numéricos              4 / 48
Métodos Gráficos
El método gráfico es útil porque proporciona un valor inicial a ser usado por otros
métodos.

  Ejemplo
 Utilice un argumento geométrico (método gráfico) para garantizar la existencia de
 una única raíz positiva r de la ecuación
                                           π 
                                ex−1 − cos    x =0
                                            4




Universidad de Ingeniería y Tecnología      Métodos Numéricos                   5 / 48
Teorema de Bolzano
Sea f una función continua en el intervalo [a, b]. Presenta un cambio de signo en
los extremos del intervalo,
                                  f (a) · f (b) < 0
entonces, podemos garantizar que existe al menos un valor x̂ ∈ [a, b] tal que
f (x̂) = 0.
       La condición de continuidad es esencial para garantizar la existencia de
       una raíz.
       Dentro de ese intervalo la función puede tener más de una raíz.




Universidad de Ingeniería y Tecnología       Métodos Numéricos                  6 / 48
Continuación...
Observación:
Si f (a)f (b) > 0, entonces se puede dar diversas situaciones en el intervalo [a, b].

                 𝑓(𝑥)                                             𝑓(𝑥)




                              a                 b       𝑥                    a       𝜉   b   𝑥

                                         𝑓(𝑥)




                                                    a       𝜉1    𝜉2 b           𝑥



Universidad de Ingeniería y Tecnología                           Métodos Numéricos               7 / 48
Método de la Bisección
El método de la bisección es un tipo de búsqueda incremental en el que el intervalo se
divide siempre a la mitad. Si la función cambia de signo sobre un intervalo, se evalúa la
función en el punto medio. La posición de la raíz se determina situándola en el punto medio
del subintervalo, dentro del cual ocurre un cambio de signo. El proceso se repite hasta
obtener una mejor aproximación.
   0 Comienza desde un intervalo [a0 , b0 ] = [a, b] que contiene la raíz de la ecuación
     f (x) = 0, por lo que f (a)f (b) < 0, f es continua en [a, b].
   1 Se calcula el valor de la función en el punto medio, c0 = a0 +b
                                                                  2
                                                                     0
                                                                       intervalo [a0 , b0 ].
   2 Si f (c0 ) tiene el mismo signo que f (a0 ) establecemos a1 = c0 . Pero Si f (c0 ) tiene el
     mismo signo que f (b0 ) establecemos b1 = c0 .
   3 Se realizan, una cantidad de veces, los pasos 1 y 2 con el intervalo [a0 , b0 ] = [a1 , b1 ].




Universidad de Ingeniería y Tecnología              Métodos Numéricos                          8 / 48
    Método de la Bisección
    Algorithm 1: Método de Bisección
  Input: a, b tales que f (a)f (b) < 0, tolerancia Tol, número máximo de iteraciones N
  Output: Aproximación c de la raíz de f (x) = 0
1 for i ← 0 to N do
              a+b
2      c←
                2
3      if f (c) = 0 then
4            Terminar
5        if f (c)f (a) > 0 then
6              a←c
7        else
8              b←c

9   return c




    Universidad de Ingeniería y Tecnología              Métodos Numéricos                9 / 48
Continuación...




                Figure: Una representación gráfica del método de la bisección.

Universidad de Ingeniería y Tecnología              Métodos Numéricos            10 / 48
Continuación...




                Figure: Una representación gráfica del método de la bisección.

Universidad de Ingeniería y Tecnología              Métodos Numéricos            11 / 48
Continuación...




                Figure: Una representación gráfica del método de la bisección.

Universidad de Ingeniería y Tecnología              Métodos Numéricos            12 / 48
Continuación...




                Figure: Una representación gráfica del método de la bisección.

Universidad de Ingeniería y Tecnología              Métodos Numéricos            13 / 48
Continuación...
                                     𝜀𝑎 = 1
                        𝒂                            𝒄                        𝒃
                                                                                                2−0
         𝑖=0                                                                         𝜀𝑎 = 1 =
                                                                                                2𝟎+1
                        0                                                     2
                                             𝜀𝑎 = 0.5 1
                        𝒂                𝒄           𝒃                                          2−0
         𝑖=1                                                                       𝜀𝑎 = 0.5 =
                                                                                                2𝟏+1
                        0                0.5         1                        2
                                         𝜀𝑎 = 0.25
                                         𝒂      𝒄    𝒃                                          2−0
         𝑖=2                                                                      𝜀𝑎 = 0.25 =
                                                                                                2𝟐+1
                        0                0.5 0.75    1                        2


                Figure: Una representación gráfica del método de la bisección.

Universidad de Ingeniería y Tecnología                    Métodos Numéricos                            14 / 48
Convergencia de método de bisección
  Convergencia
 Sean a, b ∈ R tales que a < b y sea f : [a, b] → R una función que satisface:
    1   f es continua en el intervalo [a, b]
    2   f admite un cambio de signo en el intervalo [a, b]
 Entonces la sucesión de aproximaciones del método de bisección {xn } converge
 a alguna raíz x̂ ∈ [a, b] de f .

Resta ver cuál va a ser el criterio de parada del algoritmo.




Universidad de Ingeniería y Tecnología         Métodos Numéricos                 15 / 48
Error y algoritmos iterativos (en general)
En muchas aplicaciones reales, como cuando se emplean algoritmos iterativos, no se
conoce a priori la respuesta verdadera.

  Error y tolerancia
 Sea x0 , x1 , . . . , xn , . . . una sucesión (de aproximaciones) convergente a un valor
 desconocido. Entonces los errores absoluto y relativo al momento de estimar o
 calcular xn , están dados por:

                                                                                ξn
          ξn = |aprox. anterior − aprox. actual| = |xn − xn−1 |      ;   δn =
                                                                                |xn |

 Además, decimos que se tiene una tolerancia de Tol en el error absoluto (relativo)
 cuando:
                            ξn ≤ Tol     (δn ≤ Tol)


Universidad de Ingeniería y Tecnología           Métodos Numéricos                      16 / 48
Mínimo número de iteraciones del M. Bisección
  Condición de parada
 Si a = a0 y b = b0 son los extremos originales del intervalo donde ocurre un
 cambio de signo, una estimativa del error absoluto (ancho del intervalo) después
 de n pasos es el valor b−a
                        2n+1
                             .

 Fijado una tolerancia Tol en el error absoluto, para saber cuántos pasos hace el
 algoritmo debemos resolver:
                                    b−a
                                          ≤ Tol.
                                    2n+1

Claramente                                                    
                                                         b−a
                                               ln       2×Tol
                                         n=                     
                                           
                                                   ln 2         
                                                                 

Universidad de Ingeniería y Tecnología                   Métodos Numéricos    17 / 48
Ejemplo 1
  Ejemplo (EP 2023-2)
 Dada la siguiente ecuación no lineal:

                                         ex − x 3
                                           √      =0
                                             x


  (a) Elige un intervalo inicial [a0 , b0 ], donde se garantice la existencia de la menor
      raíz real positiva. Donde a0 y b0 son enteros, además b0 − a0 = 1.
  (b) Determine el mínimo número de iteraciones para aproximar la menor raíz
      real positiva con una tolerancia de 10−3 al aplicar el método de la bisección.
  (c) Realice dos iteraciones utilizando el método de la bisección con las
      condiciones encontradas en el ítem (a).


Universidad de Ingeniería y Tecnología          Métodos Numéricos                    18 / 48
Ejemplo 1
(a) Se va analizando en intervalos de longitud 1, como en la gráfica:




    La función es continua en [1, 2] y f (1)f (2) < 0.
(b) De la desigualdad se sigue:
                                         b−a           1
                                              ≤ tol → n+1 ≤ 10−3 → n = 9
                                         2n+1        2
Universidad de Ingeniería y Tecnología                  Métodos Numéricos   19 / 48

Ejemplo 1
 (c) Realizamos las iteraciones:
                                  Iter   a   c   b   f (a)   f (c)    f (b)   Error
                                   0     1       2
                                   1
                                   2




Universidad de Ingeniería y Tecnología                 Métodos Numéricos              20 / 48
Ejemplo 1
 (c) Realizamos las iteraciones:
                     Iter        a        c      b    f (a)        f (c)       f (b)    Error
                      0          1        1.5    2   1.7183      0.9036       -0.4320
                      1        1.5       1.75    2   0.9036      0.2988       -0.4320   0.25
                      2       1.75       1.875   2   0.2988     -0.0518       -0.4320   0.125




Universidad de Ingeniería y Tecnología                    Métodos Numéricos                     21 / 48
Ejercicio 2
  Ejemplo (Examen de Rezagados 2024 - 1)
 El flujo de corriente eléctrica en un circuito RLC, para determinados valores de la
 resistencia R , la inductancia L y la capacitancia C , viene dado por la expresión:

                                     i(t) = 10e−t/2 cos(3t) (miliamperios)

 Estime el primer instante cuando la corriente alcanza el valor de 2 miliamperios.
 Use el método de la bisección, considere el intervalo inicial [0; 0.5] seg y realice 2
 iteraciones




Universidad de Ingeniería y Tecnología                    Métodos Numéricos        22 / 48
2   MÉTODOS
    ABIERTOS
Introducción
Los métodos abiertos se basan en fórmulas que requieren únicamente de un
solo valor de inicio x0 o que empiecen con un par de ellos, pero que no
necesariamente encierran la raíz. A partir del punto inicial o puntos iniciales,
generan sucesiones aproximadas de la solución mediante una formula de iteración.
Su convergencia depende del punto inicial y la naturaleza de la función f . Sin
embargo, cuando convergan lo hacen mucho más rapido que los métodos cerrados.




Universidad de Ingeniería y Tecnología   Métodos Numéricos                 24 / 48
Método de Newton
De las fórmulas para localizar raíces, la fórmula de Newton-Raphson es una de las
más utilizadas. Si el valor inicial para la raíz es xi , entonces se puede trazar una
tangente desde el punto (xi ; f (xi )). El punto donde esta tangente cruza al eje x
representa una aproximación mejorada de la raíz.




Universidad de Ingeniería y Tecnología      Métodos Numéricos                    25 / 48
Interpretación Geométrica
      𝑓(𝑥)                                                      La ecuación de la recta tangente es:
                   Pendiente =𝑓′(𝑥𝑖 )                            f (xi ) − y = f ′ (xi )(xi − x)
     𝑓(𝑥𝑖 )
                                                                Cuando y = 0, x = xi+1 , reemplazando:
                                                                f (xi ) − 0 = f ′ (xi )(xi − xi+1 )
                                                     𝑓 𝑥𝑖 − 0
                                                                Despejando:

                                                                                              f (xi )
        0
                                    𝑥𝑖+1        𝑥𝑖
                                                                               xi+1 = xi −
                                                                                             f ′ (xi )
                                         𝑥𝑖 − 𝑥𝑖+1
                                                                Observación: El método no funciona si
                                                                f ′ (xi ) = 0.




Universidad de Ingeniería y Tecnología                           Métodos Numéricos                       26 / 48
     Método de Newton
     Algorithm 2: Método de Newton
  Input: Función f (x), punto inicial x0 , tolerancia en error relativo δr
  Output: Aproximación a x ∗ , raíz de f , es decir f (x ∗ ) = 0
1 k ← 0
2 δr ← 1 (valor mayor a Tol)
                          ′
3 Obtener expresión f (x)
4 while δr > Tol do
5     if f ′ (xk ) = 0 then
6             Terminar con error
                       f (xk )
 7        xk +1 ← xk −
                      f ′ (xk )
              |x    −x |
 8        δr ← k+1 k
                 |xk+1 |
 9        k ←k +1
10   return xk+1



     Universidad de Ingeniería y Tecnología                Métodos Numéricos   27 / 48
Ejemplo
  Ejemplo
 Aproximar una raíz de la función f (x) = ex−1 − cos π4 x utilizando el método de
                                                         

 Newton con x0 = 0.1. Realice 04 iteraciones. Calcule el error (relativo).

Solución: Tenemos x0 = 0.1, f ′ (x) = ex−1 + π4 sin π4 x
                                                                                

                                     i    xi   f (xi )   f ′ (xi )   Error relativo
                                     0   0.1
                                     1
                                     2
                                     3
                                     4



Universidad de Ingeniería y Tecnología                          Métodos Numéricos     28 / 48
Ejemplo
  Ejemplo
 Aproximar una raíz de la función f (x) = ex−1 − cos π4 x , utilizando el método
                                                         

 del Newton con x0 = 1.5. Realice 04 iteraciones. Calcule el error (relativo).

Solución: Tenemos x0 = 0.1, f ′ (x) = ex−1 + π4 sin π4 x .
                                                        

                             i         xi      f (xi )    f ′ (xi )   Error relativo
                             0      0.1000   -0.5903     0.4682              -
                             1      1.3609    0.9535     2.1232          0.9265
                             2      0.9118    0.1612     1.4312          0.4925
                             3      0.7991    0.0086     1.2793          0.1410
                             4      0.7924   0.00003     1.2704          0.0085



Universidad de Ingeniería y Tecnología                     Métodos Numéricos           29 / 48
Continuación




La gráfica nos muestrauna aproximación al valor de la raíz de la ecuación
f (x) = ex−1 − cos π4 x pero el método de Newton nos da un valor específico.


Universidad de Ingeniería y Tecnología    Métodos Numéricos                    30 / 48
Convergencia de método de Newton
  Convergencia
 Sean a, b ∈ R tales que a < b y sea f : [a, b] → R una función que satisface:
    1 Existe una raíz x ⋆ de f en el intervalo [a, b]

    2 f ′ (x) ̸= 0 en todo un intervalo I = [x ⋆ − δ, x ⋆ + δ] para algún δ > 0

    3 f ′′ (x) es continua en I

    4 x0 es suficientemente cercano a x ⋆ , x0 ∈ I

 Entonces, la sucesión de aproximaciones de Newton {xk } converge a x ⋆ .
 Además, si se cumple                             |f ′′ (x)|
                           M · δ < 1 con M = max             ,
                                              x∈I 2|f ′ (x)|

 se tiene que                                                         2
                                         |xk +1 − x ⋆ | ≤ M|xk − x ⋆ | ;
 es decir, el método de Newton converge cuadráticamente.
Universidad de Ingeniería y Tecnología                     Métodos Numéricos      31 / 48
Punto Fijo
  Definición
 Sea g : [a, b] → R una función continua en [a, b], se dice que p ∈ [a, b] es punto
 fijo de g si y solo si se cumple: g(p) = p

Ejemplo: Halle los puntos fijos de las siguientes funciones, en caso existan
   1   g(x) = 20 − x 2
   2   g(x) = x 3 − ex
   3   g(x) = −1 − x 2
Notas:
       Hallar punto fijo de g equivale a resolver g(x) = x
       Considerando f (x) = g(x) − x o f (x) = x − g(x), hallar puntos fijos de g es
       equivalente a hallar raices de f

Universidad de Ingeniería y Tecnología        Métodos Numéricos                   32 / 48
Método del Punto Fijo
Un punto fijo de una función g es una solución x ∗ de la siguiente ecuación

                                         g(x ∗ ) = x ∗

Geométricamente, es la intersección de la función y = g(x) con la función y = x.
Para resolver una ecuación f (x) = 0 , se reescribe en la forma:

                                          x = g(x)

La elección de g(x) no es única. Algunas formas acercan x a la solución, otras lo
alejan.




Universidad de Ingeniería y Tecnología            Métodos Numéricos           33 / 48
    Método del Punto Fijo
    Algorithm 3: Método del Punto Fijo
  Input: Función g(x), punto inicial x0 , tolerancia en error relativo δr
  Output: Aproximación x de la raíz de f (x) = 0
1 k ← 0
2 δr ← 1 (valor mayor a Tol)
3 while δr > Tol do
4     xk +1 ← g(xk )
             |x    −x |
5     δr ← k+1 k
                |xk+1 |
6     k ←k +1
7   return xk+1




    Universidad de Ingeniería y Tecnología                Métodos Numéricos   34 / 48
Método del Punto Fijo

  Ejemplo
 Dada la ecuación x 3 + 4x 2 − 10 = 0. Expresar la ecuación en la forma x = g(x)

Solución:
 a) x = g(x) = x − x 3 − 4x 2 + 10
                   1/2
                 10
 b) x = g(x) = 4+x




Universidad de Ingeniería y Tecnología    Métodos Numéricos                  35 / 48
Continuación...
Ahora vamos a usar el proceso iterativo x(n+1) = g(x(n) );         n = 0, 1, 2, . . . para los
dos despejes, tomando como semilla x (0) = 1.8.
                                                                                 1/2
                                                                             10
               Iteración x = g(x) = x − x 3 − 4x 2 + 10 x = g(x) =          4+x
                     0                           1.8                               1.8
                     1                       −6.992
                     2                   149.281087
                     3                   −3415685.7
                     4
                     5
                     6
                     7



Universidad de Ingeniería y Tecnología         Métodos Numéricos                          36 / 48
Continuación...
Ahora vamos a usar el proceso iterativo x(n+1) = g(x(n) );         n = 0, 1, 2, . . . para los
dos despejes, tomando como semilla x (0) = 1.8.
                                                                                 1/2
                                                                             10
               Iteración x = g(x) = x − x 3 − 4x 2 + 10 x = g(x) =          4+x
                     0                           1.8                         1.8
                     1                       −6.992                 1.313064329
                     2                   149.281087                 1.371915816
                     3                   −3415685.7                 1.364380177
                     4                                               1.36533815
                     5                                              1.365216255
                     6                                              1.365231764
                     7                                              1.365229791



Universidad de Ingeniería y Tecnología         Métodos Numéricos                          37 / 48
Convergencia de método del punto fijo
  Convergencia
 Sean [a, b] un intervalo si g : [a, b] → R es una función continua en [a, b] y
 derivable en ⟨a, b⟩ tal que:
    1   Para cualquier punto x en [a, b], se tiene que g(x) ∈ [a, b] (condición de
        existencia).
    2   Se cumple |g ′ (x)| < 1 para cualquier x ∈ ⟨a, b⟩ (condición de contracción).
 Entonces existe un único punto p ∈ ⟨a, b⟩ tal que g(p) = p. Además, si x(0)
 es algún punto del intervalo [a, b], y la sucesión {x(k ) } se construye de manera
 recursiva
                                  x(k +1) = g(x(k ) )

 entonces la sucesión {x(k ) } converge al punto fijo p de la función g.


Universidad de Ingeniería y Tecnología        Métodos Numéricos                  38 / 48
Representación gráfica
En 1a) y 1b) el método del punto fijo converge, tienen un comportamiento monótono.

             𝑦                                                  𝑦
             𝑏                                                 𝑏

                                         𝒚𝟏 = 𝒙                                        𝒚𝟏 = 𝒙

                                                  𝒚𝟐 = 𝒈 𝒙


                                                                                             𝒚𝟐 = 𝒈 𝒙


             𝑎                                                 𝑎

                    𝑎           𝑥2 𝑥1       𝑥0       𝑏 𝑥             𝑎    𝑥1      𝑥2         𝑥0         𝑏 𝑥
                                Figura 1a                                        Figura 1b



Universidad de Ingeniería y Tecnología                       Métodos Numéricos                                39 / 48

            𝑎                                             𝑎
Representación
      𝑎   𝑥 𝑥 𝑥 gráfica
                   𝑏 𝑥           2   1      0          𝑎 𝑥1 𝑥2         𝑥0       𝑏 𝑥
En 1c) y 1d) el método de punto
                     Figura 1a  fijo diverge, tienen un comportamiento
                                                             Figura 1b    oscilatorio o en
espiral.
            𝑦                                              𝑦
            𝑏                                             𝑏
                                                                    𝒚𝟐 = 𝒈 𝒙
                        𝒚𝟐 = 𝒈 𝒙

                                                                                         𝒚𝟏 = 𝒙
                                         𝒚𝟏 = 𝒙




            𝑎                                             𝑎

                    𝑎          𝑥0 𝑥1        𝑥2    𝑏 𝑥           𝑎     𝑥1     𝑥0     𝑥2            𝑏 𝑥
                                Figura 1c                                   Figura 1d


Universidad de Ingeniería y Tecnología                  Métodos Numéricos                               40 / 48
Ejemplo
  Ejemplo
 La ecuación x 2 − x = 0, tiene en el intervalo [0.64; 1.44] una única raíz α.
                                                             √
     Verificar que α es un punto fijo de la función g(x) = x.
        Pruebe que la sucesión {x (n) } definida por

                                             x (0) = 0.64
                                         
                                                       √
                                             x (n+1) = x (n) ,       n≥0

        Converge a α




Universidad de Ingeniería y Tecnología                    Métodos Numéricos      41 / 48
Solución:
       Como α es raíz de la ecuación x 2 − x = 0 entonces α2 − α = 0
       De este modo:
                                                        √
                            α2 − α = 0 ⇔ α2 = α ⇔ α = α = g(α)
                                                        √
       Por lo tanto α es punto fijo de la función g(x) = x.
                                                     √
       Es necesario verificar que la función g(x) = x satisface en el intervalo
                                                                                    1
       [0.64; 1.44] las condiciones del teorema del punto fijo. Se tiene g ′ (x) = 2√ x
                                                                                        y
                          ′
       se observa que g es una función positiva y decreciente, por eso es fácil
       calcular el máximo de su valor absoluto:
                                                                              1
                         k=          max        |g ′ (x)| = g ′ (0.64) =           = 0.625 < 1
                                x∈[0.64;1.44]                              2 × 0.8



Universidad de Ingeniería y Tecnología                         Métodos Numéricos                 42 / 48
Luego hay que demostrar que g([0.64; 1.44]) ⊂ [0.64; 1.44]. Calculemos los valores
mínimo y máximo de g en el intervalo [0.64; 1.44]. Dado que g ′ > 0, la función g es
creciente:
                          min g(x) = g(0.64) = 0.8
                                         x∈[0.64;1.44]


                                            max          g(x) = g(1.44) = 1.2
                                         x∈[0.64;1.44]


                             g([0.64; 1.44]) = [g(0.64), g(1.44)] = [0.8; 1.2]
Así que:
                                              [0.8; 1.2] ⊂ [0.64; 1.44]
Por lo tanto, g tiene un único punto fijo en este intervalo.




Universidad de Ingeniería y Tecnología                          Métodos Numéricos   43 / 48
Comprobación gráfica




Comprobación de la convergencia del método del punto fijo en el intervalo
[0.64; 1.44] con x (0) = 0.64.


Universidad de Ingeniería y Tecnología    Métodos Numéricos                 44 / 48
Ejercicio 3
  Ejemplo (Examen parcial 2023 - 2)
 Determine la veracidad de la siguiente proposición:
                                                 ex − 1
 Sea: f (x) = ex − x (e − 1) − 1 y x = g(x) =           . Para cualquier punto x en
                                                  e−1
 [−1, 1] se cumple que g(x) ∈ [−1, 1]. Por ello, esta garantizada la convergencia
 del método de punto fijo en la determinación de la raíz real de la ecuación.




Universidad de Ingeniería y Tecnología      Métodos Numéricos                   45 / 48
Conclusiones
       Los métodos abiertos, aunque más rápidos, son menos estables que los
       métodos cerrados, los cuales ofrecen mayor seguridad en la convergencia.
       La convergencia de los métodos numéricos, en particular los métodos abiertos,
       depende en gran medida de la elección adecuada del valor inicial.
       La precisión en la resolución numérica es crucial, y un control adecuado de la
       tolerancia y el error garantiza resultados más fiables en aplicaciones prácticas.




Universidad de Ingeniería y Tecnología         Métodos Numéricos                   46 / 48
Bibliografía
      Steven C. Chapra and Raymond P. Canale
      Métodos numéricos para ingenieros, 7a ed.
      Richard L. Burden and J. Douglas Faires
      Análisis numérico, 7a ed.




Universidad de Ingeniería y Tecnología    Métodos Numéricos   47 / 48

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
