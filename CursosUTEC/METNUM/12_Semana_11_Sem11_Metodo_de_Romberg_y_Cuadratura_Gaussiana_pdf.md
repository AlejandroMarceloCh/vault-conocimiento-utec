---
curso: METNUM
titulo: 12 - Semana 11/Sem11_Método de Romberg y Cuadratura Gaussiana
slides: 36
fuente: 12 - Semana 11/Sem11_Método de Romberg y Cuadratura Gaussiana.pdf
---

Métodos Numéricos
Romberg y C. Gaussiana - S11

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

                                         1 Integración de Romberg
                                         2 Cuadratura de Gauss
Índice




Universidad de Ingeniería y Tecnología   Métodos Numéricos          1 / 35
        Objetivos
            Estimar integrales definidas mediante el método de Romberg aplicando la
            extrapolación de Richardson sobre aproximaciones sucesivas del método del
            trapecio.

            Aplicar la cuadratura de Gauss para aproximar integrales definidas utilizando
            nodos y pesos óptimos.




Universidad de Ingeniería y Tecnología             Métodos Numéricos                        2 / 35
1   INTEGRACIÓN
    DE ROMBERG
Introducción
La integración de Romberg es una técnica diseñada para obtener integrales
numéricas de manera eficiente. Se basa en aplicaciones sucesivas de la regla del
trapecio, mediante refinamientos sucesivos del tamaño de paso, alcanzando así
mejores resultados con menos trabajo. Consideremos la siguiente integral y su
valor exacto:

           Z 0.8
     I=            (0.2 + 25x − 200x 2 + 675x 3 − 900x 4 + 400x 5 )dx = 1.6405333333
             0

En las reglas compuestas del trapecio o Simpson 1/3, a medida que se incrementa
la cantidad de intervalos de partición la aproximación debería ser mejor, ello es
correcto pero tiene sus límites precisamente por la acumulación de errores de
redondeo (tal como se muestra en la gráfica siguiente).


Universidad de Ingeniería y Tecnología           Métodos Numéricos                     4 / 35
Error relativo verdadero vs cantidad de intervalos




Universidad de Ingeniería y Tecnología   Métodos Numéricos   5 / 35
Formulación de contenidos
Consideremos la regla del trapecio múltiple aplicada al cálculo aproximado de
Z b
    f (x)dx con tamaño de paso h, se tiene entonces:
 a

                                           I = I(h) + E(h)                      (1)
Donde:
       I es el valor exacto de la integral.
       I(h) es el valor aproximado numéricamente.
       E(h) es el error de truncamiento. Recuerde que:

                                                    (b − a) 2 ′′
                                         E(h) = −          h f (μ)
                                                      12
              b−a
       h=         es el tamaño de paso utilizado.
               n
Universidad de Ingeniería y Tecnología                Métodos Numéricos         6 / 35
Formulación de contenidos
A continuación, consideremos dos aproximaciones distintas para I (diferenciándose
solo en sus tamaños de paso h1 y h2 ):
                                         I = I(h1 ) + E(h1 )
                                         I = I(h2 ) + E(h2 )
La intención es que h2 sea un refinamiento de h1 (por ejemplo: h2 = h21 ).

                        (b − a) 2 ′′
       Tenemos E(h) = −        h f (μ)
                          12
    Asumimos que la segunda derivada es aproximadamente constante en el
    intervalo.
Calculamos la relación de errores:
                           E(h1 )  h2                                      h2
                                  ≈ 12    entonces          E(h1 ) ≈ E(h2 ) 12
                           E(h2 )  h2                                      h2

Universidad de Ingeniería y Tecnología               Métodos Numéricos           7 / 35
Método de Romberg
       Reemplazando la aproximación obtenida para E(h1 ) en la ecuación del
       balance de error: I(h1 ) + E(h1 ) = I(h2 ) + E(h2 )
       Obtenemos una estimación directa para el error de la malla fina E(h2 ):

                                                         I(h2 ) − I(h1 )
                                              E(h2 ) ≈
                                                            h12
                                                                −1
                                                            h22

Finalmente, combinando los términos:
                                                                   I(h2 ) − I(h1 )
                                  I = I(h2 ) + E(h2 ) ≈ I(h2 ) +
                                                                       h12
                                                                       h22
                                                                           −1



Universidad de Ingeniería y Tecnología                     Métodos Numéricos         8 / 35
Método de Romberg
Si consideramos en particular el caso estándar donde el paso se reduce a la mitad
(h2 = h21 ) en la aproximación previa:
                                                        I(h2 ) − I(h1 )
                                         I ≈ I(h2 ) +
                                                              h12
                                                              h22
                                                                  −1


  Extrapolación de Richardson (Integración)
                                               4                     1
                                 I(h1 , h2 ) =       I(h2 )      −          I(h1 )
                                 | {z }        3     | {z }          3      | {z }
                               mejor aprox.        aprox. fina           aprox. gruesa


Nota: Las aproximaciones del trapecio compuesto son del orden O(h2 ), se
demuestra que estas combinaciones lineales eliminan el término de error principal,
alcanzando un orden O(h4 ).
Universidad de Ingeniería y Tecnología                        Métodos Numéricos          9 / 35
Ejemplo
En la tabla se muestran las aproximaciones calculadas según la regla del trapecio
para la función de prueba, cuyo valor exacto es 1.6405333333.

      N° de intervalos (n)               Tamaño de paso (h)       I(h)    Error relativo (%)
                      1                         0.8             0.1728          89.5
                      2                         0.4             1.0688          34.9
                      4                         0.2             1.4848           9.5

Determine mejores aproximaciones utilizando la regla de extrapolación de
Romberg.




Universidad de Ingeniería y Tecnología                Métodos Numéricos                        10 / 35
Solución
Combinando las aproximaciones de n = 1 y n = 2 intervalos obtenemos según
Romberg:

                                         4         1
                            I(h1 , h2 ) =  I(h2 ) − I(h1 )
                                         3         3
                                         4             1
                            I(h1 , h2 ) = (1.0688) − (0.1728) = 1.367467
                                         3             3
                                      1.640533 − 1.367467
El nuevo error relativo porcentual es:                    = 16.6%, claramente
                                             1.640533
superior a las aproximaciones iniciales aisladas.




Universidad de Ingeniería y Tecnología              Métodos Numéricos      11 / 35
Ejercicio
Similarmente a lo anterior, usando las estimaciones de 2 y 4 subintervalos (h = 0.4
y h = 0.2), obtenga una mejor aproximación y calcule su respectivo error relativo.

Desarrollo:
                                         4         1
                            I(h2 , h3 ) =  I(h3 ) − I(h2 )
                                         3         3
                                         4             1
                            I(h2 , h3 ) = (1.4848) − (1.0688) = 1.623467
                                         3             3
                                             1.640533 − 1.623467
El error relativo resultante cae drásticamente a:                = 1.04%
                                                   1.640533
¿Se podrá seguir generando nuevas aproximaciones combinadas con menor error?




Universidad de Ingeniería y Tecnología              Métodos Numéricos          12 / 35
Generalizando
En general se combinan dos aproximaciones conocidas para obtener una de orden
superior. La siguiente tabla muestra el esquema de las primeras iteraciones:

  Nivel (k)                        Fórmula de Combinación               Orden de Precisión
        1           Estimación estándar con la regla del trapecio             O(h2 )
                                  4          1
        2                           I(h2 ) − I(h1 )                           O(h4 )
                                  3          3
                                 16           1
        3                           I(h2 ) −    I(h1 )                        O(h6 )
                                 15          15
                                 64           1
        4                           I(h2 ) −    I(h1 )                        O(h8 )
                                 63          63




Universidad de Ingeniería y Tecnología              Métodos Numéricos                  13 / 35
Funcionamiento del algoritmo de Romberg




 Idea clave: Es un esquema piramidal donde los resultados de una columna
                    alimentan la precisión de la siguiente.
Universidad de Ingeniería y Tecnología   Métodos Numéricos           14 / 35
Algoritmo de Integración de Romberg
                                              4k −1                  1
                                  *Ij,k =             Ij+1,k −1 − k −1    Ij,k −1
                                            4k −1 − 1            4     −1


       Ij+1,k −1 e Ij,k −1 son las integrales más y menos exactas de la columna anterior.
       Ij,k representa la aproximación óptima mejorada.
       k es el nivel de integration, siendo k = 1 (primera columna) la estimación
       original del trapecio para particiones n = 1, 2, 4, 8, . . . , 2p .




Universidad de Ingeniería y Tecnología                       Métodos Numéricos      15 / 35
Observaciones
       Podemos usar como criterio de finalización tolerancias basadas en el error
                            I −I
       relativo aproximado: 1,k I1,k1,k −1 < tol
       Eficiencia extrema: El método de Simpson requiere 256 intervalos para
       estabilizar el valor de esta integral de prueba debido al redondeo. Romberg
       ofrece un resultado idéntico (con 7 cifras significativas) usando combinaciones
       inteligentes de solo 1, 2, 4 y 8 intervalos.




Universidad de Ingeniería y Tecnología        Métodos Numéricos                   16 / 35
2   CUADRATURA
    DE GAUSS
Introducción
       Estos métodos eliminan la rigidez de los esquemas de Newton-Cotes: NO
       fijan los puntos uniformemente, sino que los eligen de manera óptima junto
       con sus respectivos pesos.
       Se utiliza el método de coeficientes indeterminados para forzar la integración
       exacta sobre las bases polinomiales y = 1, x, x 2 , x 3 , . . .
       Requiere realizar una transformación equivalente para mapear cualquier
                                                                *[−1, 1].
       intervalo genérico [a, b] al intervalo de diseño normado




Universidad de Ingeniería y Tecnología        Métodos Numéricos                  18 / 35
Elección de puntos donde evaluar




Universidad de Ingeniería y Tecnología   Métodos Numéricos   19 / 35

Fórmula de Gauss-Legendre de dos puntos
                   Z                     1
Si el objetivo directo es calcular I =        f (x)dx:
                                         −1

                                                 *I ≈ c0 f (x0 ) + c1 f (x1 )
       Planteamos el operador aproximado:
       Contamos con 4 grados de libertad (incógnitas libres): los pesos c0 , c1 y las
       raíces nodales x0 , x1 .
       Imponiendo integración exacta para polinomios hasta grado 3, se genera un
       sistema no lineal cerrado.




Universidad de Ingeniería y Tecnología           Métodos Numéricos                 20 / 35
Fórmula de Gauss-Legendre de dos puntos
                                                    Z 1
                         c0 (1) + c1 (1)       =          1dx      =2        =⇒      c0 + c 1 = 2
                                                    Z−1
                                                      1
                      c0 (x0 ) + c1 (x1 )      =          xdx      =0        =⇒      c0 x0 + c1 x1 = 0
                                                    Z−1
                                                      1
                      c0 (x02 ) + c1 (x12 )    =          x 2 dx   = 23      =⇒      c0 x02 + c1 x12 = 32
                                                    Z−1
                                                      1
                      c0 (x03 ) + c1 (x13 )    =          x 3 dx   =0        =⇒      c0 x03 + c1 x13 = 0
                                                     −1


  Solución Única del Sistema
                                                           −1                                   1
            c0 = 1,           c1 = 1          e       x0 = √ ≈ −0.5773,                   x1 = √ ≈ 0.5773
                                                            3                                    3

                                              Z 1                                      
                                                                       −1              1
                                         I=         f (x)dx ≈ f        √      +f √
Universidad de Ingeniería y Tecnología         −1                      Métodos Numéricos3
                                                                         3                                  21 / 35
Cambio de variable (Mapeo Lineal)
Para migrar de las fronteras físicas a las del dominio de cuadratura, aplicamos la
transformación lineal:
     (b + a) + (b − a)z
x=                          =⇒     dx = b−a2 dz
              2
Donde la correspondencia espacial es exacta: z ∈ [−1, 1] ↔ x ∈ [a, b]. En
consecuencia:
                 Z b           Z 1                      
                                      (b + a) + (b − a)z b − a
                     f (x)dx =     f                            dz
                  a             −1              2            2




Universidad de Ingeniería y Tecnología      Métodos Numéricos                  22 / 35
Ejemplo
Utilice la cuadratura de Gauss de dos puntos para aproximar la integral:
                          Z 0.8
                   I=             (0.2 + 25x − 200x 2 + 675x 3 − 900x 4 + 400x 5 )dx
                            0

Solución:
       Reemplazando a = 0 y b = 0.8, la función de transformación es:
       x = 0.4 + 0.4z.
       El diferencial se transforma en: dx = 0.4dz.




Universidad de Ingeniería y Tecnología                   Métodos Numéricos             23 / 35
Continuación ...
           Z 1
                  0.2 + 25(0.4 + 0.4z) − 200(0.4 + 0.4z)2 + 675(0.4 + 0.4z)3 − . . . (0.4dz)
                                                                                    
    I=
            −1
           Z 1
       =  g(z)dz
            −1
                         
             −1          1
       ≈1×g √      +1×g √     = 0.516741 + 1.305837 = 1.822578
               3          3

Esto representa un error relativo del 11.1%. Requiere solo dos evaluaciones
funcionales frente a las cuatro necesarias en un trapecio equivalente.




Universidad de Ingeniería y Tecnología               Métodos Numéricos                     24 / 35
Generalización
       Para elevar el orden de precisión matemática, incrementamos el número de
       puntos de evaluación simétricos zi y ajustamos los pesos asociados ci .
       Las coordenadas de los nodos corresponden exactamente a las raíces de los
       Polinomios de Legendre.
       A continuación se tabulan las constantes óptimas de diseño de
       Gauss-Legendre hasta 5 puntos.




Universidad de Ingeniería y Tecnología      Métodos Numéricos                25 / 35
Tabla de Coeficientes de Gauss-Legendre




Universidad de Ingeniería y Tecnología   Métodos Numéricos   26 / 35
Ejemplo
Use la fórmula de tres puntos de la tabla para calcular la misma integral:
                                              Z 0.8               Z 1
                                         I=           f (x)dx =         g(z)dz
                                               0                   −1

Solución:

 I ≈ 0.5555556 · g(−0.7745967) + 0.8888889 · g(0) + 0.5555556 · g(0.7745967)
   = 1.640533              (Aproximación Analítica Exacta)

Análisis: Al ser una cuadratura de 3 puntos, integra exactamente polinomios de
grado ≤ 5 (2n − 1). Como nuestra función objetivo era de grado 5, el error
numérico es cero.



Universidad de Ingeniería y Tecnología                        Métodos Numéricos   27 / 35
Análisis del error en Cuadratura Gaussian
El error analítico residual de las fórmulas de Gauss-Legendre está acotado por:

                                                  22n+3 [(n + 1)!]4
                                         Eg =                          3
                                                                           f (2n+2) (ξ )
                                                (2n + 3) [(2n + 2)!]

Donde:
       n + 1 es la cantidad total de puntos muestreados.
       f (2n+2) (ξ ) es la derivada de orden superior evaluada en algún punto crítico
       ξ ∈ [−1, 1].




Universidad de Ingeniería y Tecnología                         Métodos Numéricos           28 / 35
                                                R 2π
Cota de Error para                                0    sin(x) dx
       Integral de análisis: f (x) = sin(x) en el rango [0, 2π].
       Transformación al espacio maestro [−1, 1]:

                                         x = πt + π   ⇒     f (t) = π sin(πt + π)

       Derivando sucesivamente obtenemos la cuarta derivada de control:

                                                f (4) (t) = π5 sin(πt + π)

       Cota máxima absoluta:
                                                   max |f (4) (ξ )| = π5
                                                 −1≤ξ ≤1




Universidad de Ingeniería y Tecnología                       Métodos Numéricos      29 / 35
                                              R 2π
Cota de Error para                                 0   sin(x) dx
       Evaluando la ecuación del error para n = 1 (cuadratura de 2 puntos):

                                                        25 [2!]4 (4)
                                               Eg =             f (ξ )
                                                        5 [4!]3

       Acotando el operador mediante el máximo teórico:

                                                    32 · 16
                                         |Eg | ≤              max |f (4) (ξ )|
                                                   5 · 13824 −1≤ξ≤1

       Cota final calculada:
                                                        1 5
                                             |Eg | ≤       π ≈ 2.2668
                                                       135




Universidad de Ingeniería y Tecnología                      Métodos Numéricos    30 / 35
Aplicación - EF - 2024 - 1                                               R 2π
Aproxime la siguiente integral de una función segmentada: If =            0
                                                                                  f (x)dx donde:
        (
         sin(x), 0 ≤ x ≤ π/2
f (x) =
         cos(x), π/2 < x ≤ 2π

                                         f
                                     1

                                                                              x
                                             π
                                             2
                                                 π           3π          2π
                                                              2
                                  −1


Sugerencia: Aplique de forma independiente la cuadratura de Gauss en cada subdominio
suave: [0, π/2] y [π/2, 2π].



Universidad de Ingeniería y Tecnología               Métodos Numéricos                             31 / 35
Aplicación - EF 2023 - 2
Una empresa de cartelería necesita estimar el área de un cartel publicitario
irregular. Por restricciones de acceso, solo se registran las dos dimensiones
horizontales clave detalladas en el esquema gráfico. Estime el área total encerrada
aplicando las técnicas de cuadratura óptimas estudiadas.




Universidad de Ingeniería y Tecnología     Métodos Numéricos                   32 / 35
Aplicación - EF 2023 - 1
Un análisis requiere aproximar el área bajo la trayectoria y = sin(x 2 ) en el intervalo
cerrado [0, 1.5]. Ante la falta de una antiderivada elemental, se propone resolver
mediante una cuadratura de Gauss-Legendre de 3 puntos usando las constantes
de control:

                         Pesos (ci )     0.5555556    0.8888889           0.5555556
                         Nodos (zi )     -0.7745967        0              0.7745967

Sabiendo que el valor analítico exacto de referencia es 0.778238, determine el
número exacto de cifras significativas correctas obtenidas por este método.




Universidad de Ingeniería y Tecnología                Métodos Numéricos               33 / 35
Conclusiones
       Romberg: Permite transformar aproximaciones mediocres de la regla del
       trapecio O(h2 ) en aproximaciones de orden superior O(h2k ) mediante la
       eliminación sistemática de los términos del error de truncamiento.
       Cuadratura Gaussiana: Maximiza la eficiencia de integración al liberar la
       posición de los nodos. Brinda la máxima precisión polinomial posible (2n − 1)
       por cada evaluación funcional realizada.




Universidad de Ingeniería y Tecnología       Métodos Numéricos                   34 / 35
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
