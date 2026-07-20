---
curso: METNUM
titulo: 03 - Semana 1/Sem1_Introducción y teoría de errores
slides: 28
fuente: 03 - Semana 1/Sem1_Introducción y teoría de errores.pdf
---

Métodos Numéricos
Introducción y teoría de errores
- S1
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
Unidad 1: Introducción
          Numéricos
                       a los Métodos
                                                 Índice
                                         1 Los métodos numéricos
                                           como herramientas de
                                           aproximación.
                                         2 Análisis de errores y
                                           Aproximación.




Universidad de Ingeniería y Tecnología   Métodos Numéricos         2 / 27
        Objetivos
    Al finalizar esta sesión, el estudiante será capaz de:
            Reconocer los métodos numéricos como herramientas para obtener soluciones
            aproximadas.
            Aplicar reglas de cifras significativas y redondeo en resultados numéricos,
            considerando la diferencia entre exactitud y precisión.
            Calcular el error absoluto y relativo para evaluar la precisión de soluciones
            numéricas.




Universidad de Ingeniería y Tecnología              Métodos Numéricos                       3 / 27
    MÉTODOS

1   NUMÉRICOS COMO
    HERRAMIENTAS DE
    APROXIMACIÓN
Unidad 1: Introducción a los métodos numéricos
  El Ciclo de Resolución Numérica
 La resolución de un problema en la industria no es lineal; es un proceso iterativo
 de abstracción, discretización, cómputo y validación estricta de tolerancias.



                  Problema Físico           Abstracción   Modelo Matemático Formulación Método Numérico
                                                                                                        t)
                   (Realidad / Industria)                      (Ecuaciones)                          ,∆        (Discretización)
                                                                                                   (N
                                                                                                es
                                                                                             ion
                                                           Rediseñar                     ra                             Programación
                                                            Modelo                          c
                                                                                      rite
                                                                                 us
                                                                                    ta
                                                                                 Aj
                                                          Validación y Error                 Ejecución       Implementación
                                                             (δr ≤ Tolerancia)                                (MATLAB / Código)
                                                                                       Dominio Computacional e Iterativo




Universidad de Ingeniería y Tecnología                                        Métodos Numéricos                                        5 / 27
 Unidad 2: Solución de Ecuaciones No Lineales
Definición Formal: Hallar x ∗ tal que
f (x ∗ ) = 0.
                                                                   f (x)
Aplicación Industrial:                                         2
      Puntos de equilibrio en circuitos.
     Cálculo de tasas de interés                                                      x
     (TIR).                                −2      −1                      1 Raíz 2       3
Métodos: Bisección,
Newton-Raphson.
                                                         −2




  Universidad de Ingeniería y Tecnología   Métodos Numéricos                              6 / 27
 Unidad 3: Sistemas de Ecuaciones Lineales
Definición Formal: Hallar x tal que
Ax = b.
                                                                     x2
Aplicación Industrial:
     Análisis de mallas (Leyes de
     Kirchhoff).                                                
                                                a11   a12     x1    b1
                                                                 =
      Esqueletos de renderizado 3D.             a21   a22     x2    b2




                                                                          x1




  Universidad de Ingeniería y Tecnología   Métodos Numéricos                   7 / 27
Unidad 4: Aproximación de funciones
                 Regresión (ML)                                      Interpolación
         5                                                5


         4                                                4

         3                                                3

         2                                                2

         1                                                1

         0                                                0
             0    1       2       3      4   5                0      1   2   3       4   5




Universidad de Ingeniería y Tecnología           Métodos Numéricos                           8 / 27
 Unidad 5: Integración Numérica
Definición
Rb          Formal: Evaluar
 a f (x)dx cuando la función es                y
compleja o se tienen datos
discretos.
                                           3
Aplicación Industrial:
      Cálculo de trabajo físico.
                                           2
      Centroides y momentos de
      inercia.
                                           1

                                                                                      x
                                                   a = x0          x1   x2   b = x3



  Universidad de Ingeniería y Tecnología       Métodos Numéricos                          9 / 27
  Unidad 6: Resolución Numérica de EDOs
Definición Formal: Dada
dy    ∆y
   ≈      = f (t, y ), resolver para y         y
dt    ∆t
como función de t.                                      Pend = f (t, yi )      (ti+1 , yi+1 )


 Método de Euler
                                                    (ti , yi )
           yi+1 = yi + f (ti , yi )∆t
                                                                      ∆t
Aplicación Industrial:                                                                     t
                                                                 ti         ti+1
      Dinámica de mecanismos.
      Cinética de reacciones químicas.
      Circuitos RLC transitorios.


  Universidad de Ingeniería y Tecnología   Métodos Numéricos                                    10 / 27
2   ANÁLISIS DE

    ERRORES Y
    APROXIMACIÓN
                                         Subtemas
                                         1. Fundamentos de Medición
                                                 Exactitud vs. Precisión.
                                                 Cifras significativas y reglas de
                                                 redondeo.

                                         2. Cuantificación de Errores
                                                 Errores de truncamiento y redondeo.
                                                 Error absoluto, relativo y porcentual.
                                                 Aproximación por Series de Taylor.



Universidad de Ingeniería y Tecnología     Métodos Numéricos                         12 / 27
Evaluación de Modelos: Exactitud vs. Precisión



                 Inexacto e               Exacto e   Inexacto y          Exacto y
                 Impreciso               Impreciso     Preciso           Preciso




Universidad de Ingeniería y Tecnología               Métodos Numéricos              13 / 27
 Cifras Significativas: Definición y Reglas
   Concepto Fundamental
  Es el número mínimo de dígitos necesarios para escribir un valor en notación
  científica sin pérdida de precisión.


Regla de los Ceros:
     Los ceros a la izquierda no son      Ejemplo Decimal
     significativos.                      0.000 006 302 tiene 4 cifras:
     Solo sirven para ubicar el punto
     decimal.                                                 6.302 × 10−6




 Universidad de Ingeniería y Tecnología   Métodos Numéricos                  14 / 27
 Cifras Significativas: Ambigüedad y Precisión
                                                       Implicación de precisión:
Ambigüedad en Enteros                                       142.7: Conocemos hasta el primer
                                                            decimal.
Un número como 92 500 es incierto.
¿Tiene 3, 4 o 5 cifras significativas?                      142.70: El equipo tiene sensibilidad
                                                            para el segundo decimal.
Solución: Notación Científica
     9.25 × 104                           (3 cifras)                      Escala de Absorbancia
                                                                                       Lectura
                                                                                         estimada
     9.250 × 104                          (4 cifras)
                                                                    2.0            0.3              0
     9.250 0 × 104                        (5 cifras)




 Universidad de Ingeniería y Tecnología                Métodos Numéricos                                15 / 27
 Ejemplo Práctico: Conteo de Cifras Significativas

                                           Valores               Cifras Significativas
                                            38.65
Actividad en Clase                          0.325
Determine el número de cifras             3.0 × 102
significativas para los sigu-             0.0000425
ientes valores medidos:
                                           2.0854
                                            35.80
                                           3 × 102
                                           3.1416
                                          3.00 × 102

 Universidad de Ingeniería y Tecnología      Métodos Numéricos                           16 / 27
Tipos de Errores

1. Error de Redondeo                       2. Error de Truncamiento
Límite del Hardware (IEEE 754).           Límite del Algoritmo. Resultado de usar
Números irracionales no caben en          una aproximación finita de una serie.
memoria.
                                                            N
                                                            X   (−1)n 2n+1
                                                   sin(x) ≈             x
                                                              (2n + 1)!
                                                              n=0




 Universidad de Ingeniería y Tecnología   Métodos Numéricos                  17 / 27
Cuantificación: Error Absoluto y Relativo

 Error Absoluto (ξ )                          Error Relativo (δr )
Llamamos error absoluto a la magni-          Es la relación respecto al valor ver-
tud de la diferencia exacta:                 dadero (A ̸= 0):

                      ξ = |A − a|                                      |A − a|
                                                                δr =
                                                                         |A|
Todo número Kξ ≥ ξ se denomina
cota del error absoluto.                     Todo número Kδ ≥ δr se denomina
                                             cota del error relativo.


 Error Relativo Porcentual (δp )
 Se obtiene al multiplicar el error relativo por 100: δp = δr × 100%

Universidad de Ingeniería y Tecnología      Métodos Numéricos                    18 / 27
Estimación del Número de Cifras Significativas
  Definición Formal
 Sean A y a dos números reales, con A ̸= 0. Se dice que a es una aproximación
 de A con n cifras significativas, si n es el mayor entero no negativo tal que:

                                                  δr ≤ 5 × 10−n
  ✓ Interpretación: Cuando a es una aproximación con n cifras significativas,
    entonces A y a coinciden en dichas cifras.

 Cálculo Directo de n
 A partir de la desigualdad anterior, se deduce la fórmula para determinar la
 cantidad de cifras significativas exactas:
                                                   
                                          ln(5/δr )
                                    n=
                                            ln 10
Universidad de Ingeniería y Tecnología                           Métodos
                                   Donde ⌊·⌋ representa la función       Numéricos entero).
                                                                   piso (máximo               19 / 27

Comparación de Escalas: Puente vs. Tornillo
  Ejercicio Práctico
 Supongamos que medimos un puente y un tornillo y resultan con 9999 cm y 9 cm
 respectivamente. Si los verdaderos valores son 10000 cm y 10 cm. Hallar el error
 absoluto y relativo para cada caso.




Universidad de Ingeniería y Tecnología     Métodos Numéricos                  20 / 27
Ejemplos
  Ejemplo
¿Cuál es el error absoluto y relativo de la aproximación a = 6.28 al valor de
A = 2π ≈ 6.283185?


  Ejemplo
 Calcule el error absoluto y el error relativo cometidos cuando el número A =
 ab × 104 se escribe erróneamente en código como a = ab × 105 .




Universidad de Ingeniería y Tecnología   Métodos Numéricos                21 / 27
Polinomio de Taylor y Residuo de Lagrange
  Teorema de Taylor
 Si f tiene n + 1 derivadas continuas en un intervalo que contiene a a, entonces:

                                         f ′′ (a)                    f (n) (a)
      f (x) = f (a) + f ′ (a)(x − a) +            (x − a)2 + · · · +           (x − a)n + Rn (x)
                                            2!                           n!



 Residuo de Lagrange (Rn )
 Representa el error de truncamiento cometido al aproximar la función usando
 solo n términos.
                                   f (n+1) (ζ )
                          Rn (x) =              (x − a)n+1
                                    (n + 1)!
 donde ζ es un valor desconocido que se encuentra entre a y x.
Universidad de Ingeniería y Tecnología               Métodos Numéricos                             22 / 27
Aproximación de Taylor: f (x) = sin(x)
Fijando el punto de expansión en a = 0, evaluamos las derivadas:

                                         Serie Alternada del Seno
    f (0) = sin(0) = 0
                                         Sustituyendo en el teorema, notamos que los
    f ′ (0) = cos(0) = 1                 términos de potencias pares se anulan:
    f ′′ (0) = − sin(0) = 0
    f ′′′ (0) = − cos(0) = −1                            x3 x5                     x 2n+1
                                          sin(x) ≈ x −      +    − · · · + (−1)n
                                                         3!   5!                 (2n + 1)!




Universidad de Ingeniería y Tecnología          Métodos Numéricos                     23 / 27
Ejemplo: Aproximación del Seno
  Ejemplo
 Estimar el valor de sin(15◦ ) usando una aproximación de 3 términos no nulos.
 Trabaje con 4 cifras decimales.

Paso 1: Conversión a radianes (¡Crucial en cálculo numérico!)
                                 π     π
                      x = 15◦ ·      =     ≈ 0.2618 rad
                                180    12
Paso 2: Evaluación del polinomio
                                  x3 x5
                    sin(x) ≈ x −     +
                                  3!    5!
                                                     (0.2618)3 (0.2618)5
                            sin(0.2618) ≈ 0.2618 −            +
                                                         6        120
                                         sin(15◦ ) ≈ 0.2588

Universidad de Ingeniería y Tecnología                Métodos Numéricos    24 / 27
Ejercicio: Tolerancia y Cifras Significativas
  Reto Computacional
 Para el ejemplo previo, considere el valor exacto sin(15◦ ) = 0.258819.
 ¿Cuál es la menor cantidad de términos requeridos en la aproximación para
 que el error relativo δr sea menor que una tolerancia preestablecida Kδ para 4
 cifras significativas?




Universidad de Ingeniería y Tecnología      Métodos Numéricos               25 / 27
Conclusiones




Universidad de Ingeniería y Tecnología   Métodos Numéricos   26 / 27
Bibliografia
      S. Chapra. Métodos numéricos para ingenieros, 7a ed. McGraw-Hill.
      R. Burden. Análisis numérico, 7a ed. Thompson.




Universidad de Ingeniería y Tecnología   Métodos Numéricos                27 / 27

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
