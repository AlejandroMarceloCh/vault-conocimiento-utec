---
curso: METNUM
titulo: 11 - Semana 10/Sem10_Diferenciación e Integración Numérica
slides: 38
fuente: 11 - Semana 10/Sem10_Diferenciación e Integración Numérica.pdf
---

Métodos
Numéricos
Dif. e Int. Numérica - S10
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

1 Diferenciación Numérica



2 Integración Numérica



3 Actividad




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 26, 2026   1 / 37
Objetivos

   1   Aplicar diferenciación numérica para aproximar la derivada de funciones
       desconocidas y/o funciones díficil de derivar.
   2   Aplicar el método de Simpson 1/3 en la aproximación de integrales y calcular el
       error estimado (cota del error).




Universidad de Ingeniería y Tecnología     Métodos Numéricos            May 26, 2026   2 / 37
    DIFERENCIACIÓN

1   NUMÉRICA
        Objetivos:
            Estimar derivadas con diferencias finitas seleccionando orden adecuado
            Aproximar integrales con reglas de Newton Cotes
            Determinar precision mediante cota de error y justificar metodo




Universidad de Ingeniería y Tecnología         Métodos Numéricos              May 26, 2026   4 / 37
Introducción

       Muchas aplicaciones de ingeniería requieren estimaciones numéricas de
       derivadas de funciones. Esto es especialmente cierto, cuando las derivadas
       analíticas no son posibles de obtener.
       También cuando la función no se conoce explícitamente, sólo se tiene la
       información de algunos puntos por donde pasa.




Universidad de Ingeniería y Tecnología   Métodos Numéricos            May 26, 2026   5 / 37
Formalización de contenidos
Comencemos con obtener una aproximación para f ′ (x) en un punto x0 .
Recordemos que la derivada de f (x) en un punto x0 , se define por:

                                                       f (x0 + h) − f (x0 )
                                         f ′ (x0 ) = lim                    .
                                                   h→0          h

Esta definición sugiere un método para aproximar f ′ (x0 ).
       Si se escoge a h una constante positiva pequeña (h > 0, h ≈ 0), entonces
                                                            f (x0 + h) − f (x0 )
                                              f ′ (x0 ) ≈                        .
                                                                     h

       Esta aproximación es llamada fórmula de diferencia hacia adelante para
       f ′ (x0 ).


Universidad de Ingeniería y Tecnología                       Métodos Numéricos       May 26, 2026   6 / 37
       Si reemplazamos h por −h en la fórmula de diferencia hacia adelante, donde h
       aún es positivo, obtenemos la fórmula de diferencia hacia atrás:
                                                         f (x0 ) − f (x0 − h)
                                           f ′ (x0 ) ≈                        .
                                                                   h

       Esta aproximación es conocida como fórmula de diferencia hacia atrás para
       f ′ (x0 ).
       Si promediamos las dos aproximaciones anteriores, obtenemos:
                                                       f (x0 + h) − f (x0 − h)
                                         f ′ (x0 ) ≈                           .
                                                                 2h

       Esta aproximación es llamada fórmula de diferencia centrada para f ′ (x0 ).




Universidad de Ingeniería y Tecnología                    Métodos Numéricos        May 26, 2026   7 / 37
Otras fórmulas para la derivada
 Fórmula de los tres puntos
 Considere como puntos de interpolación (xi , fi ), (xi+1 , fi+1 ) y (xi+2 , fi+2 ), donde
 fi = f (xi ) y xj , para j = i, i + 1, i + 2, están igualmente espaciados, es decir,
 xi+2 − xi+1 = xi+1 − xi = h. Utilice interpolación polinomial con la fórmula de
 Newton para obtener:

                                             4f (xi+1 ) − 3f (xi ) − f (xi+2 )
                               f ′ (xi ) =                                     + O(h2 ).
                                                           2h

Recuerde que: Existe xi < ξ < xi+2 tal que

              f (3) (ξ )                                                            f (3) (ξ ) 2
 R(x) =                  (x − xi )(x − xi+1 )(x − xi+2 )            ⇒ R ′ (xi ) =             h = O(h2 )
                  3!                                                                    3

Universidad de Ingeniería y Tecnología                      Métodos Numéricos                 May 26, 2026   8 / 37
 Ejemplo
 Sea f (x) = x1 . Aproxime f ′ (2) mediante las fórmulas de diferencia hacia adelante,
 hacia atrás y centrada con h = 0.01. ¿Cuál de las tres aproximaciones es mejor?

Solución:
                                                                 1
                                         f (2 + 0.01) − f (2)       −1
                            f ′ (2) ≈                         = 2.01 2 = −0.248756
                                                 0.01             0.01
                                                                1
                                         f (2) − f (2 − 0.01)     − 1
                            f ′ (2) ≈                         = 2 1.99 = −0.251256
                                                 0.01             0.01
                                                                1
                                 f (2 + 0.01) − f (2 − 0.01)       − 1
                     f ′ (2) ≈                               = 2.01 1.99 = −0.250006
                                           2(0.01)                0.02
En este caso es muy sencillo calcular el valor exacto ya que f ′ (x) = − x12 , por lo tanto,
f ′ (2) = −0.25. Claramente la fórmula centrada es mejor.


Universidad de Ingeniería y Tecnología                  Métodos Numéricos            May 26, 2026   9 / 37
 Ejercicio
                 √         
                     x 2 +x
             sen2 cosx−x
 Sea f (x) =      √        . Se desea calcular f ′ (0.25).
              sen √ x−1
                               x 2 +1


Solución:
Para calcular la f ′ (0.25) analíticamente se requiere primero derivar f (x) haciendo uso de la
regla del cociente y la regla de la cadena y luego evaluar la derivada en x = 0.25. En este
caso, la expresión de f ′ (x) es más compleja que la de f (x) y tediosa de obtener.
Una alternativa, es usar por ejemplo, la fórmula de diferencia centrada con h = 0.005 para
hallar el valor de f ′ (0.25):
                                   f (0.255) − f (0.245)
                                 f ′ (0.25) ≈            = −9.067464.
                                           0.01
La solución exacta es f ′ (0.25) = −9.066699, por lo tanto, la magnitud del error absoluto de
la solución aproximada es:
|Ea | = |Vexacto −Vaproximado | = |−9.066699+9.067464| = 0.000765.
Universidad de Ingeniería y Tecnología          Métodos Numéricos             May 26, 2026   10 / 37
Fórmulas de derivación numérica
                                    Primera derivada                                   Error
                                   f (xi+1 ) − f (xi−1 )
                             f ′ (xi ) =                                               O(h2 )
                                             2h
                    ′        −f (xi+2 ) + 4f (xi+1 ) − 3f (xi )
                   f (xi ) =                                                           O(h2 )
                                             2h
                                 Segunda derivada                                      Error
                                  f (xi+1 ) − 2f (xi ) + f (xi−1 )
                     f ′′ (xi ) =                                                      O(h2 )
                                                  h2
                    f (x i+2 ) − 4f (x i+1 ) + 6f (xi ) − 4f (xi−1 ) + f (xi−2 )
       f ′′ (xi ) =                                                                    O(h4 )
                                                  h2
                                    Tercera derivada                                   Error
                          f (xi+3 ) − 3f (xi+2 ) + 3f (xi+1 ) − f (xi )
             f ′′′ (xi ) =                                                             O(h)
                                               h3
               −3f (xi+3 )  + 14f  (x i+2 ) − 24f (xi+1 ) + 18f (xi ) − 5f (xi−1 )
 f ′′′ (xi ) =                                                                         O(h2 )
                                               2h3

Universidad de Ingeniería y Tecnología                             Métodos Numéricos            May 26, 2026   11 / 37
Conceptualización - EF 2025-0
Se tiene una función f cuya derivada en el punto x0 necesita ser aproximada,
considerando el tamaño de paso h > 0. Si tenemos en cuenta las aproximaciones:

                              f (x0 + h) − f (x0 )
                f ′ (x0 ) ≈                           aproximación hacia adelante
                                       h
                   f (x0 ) − f (x0 − h)
                   f ′ (x0 ) ≈           aproximación hacia atrás
                             h
Siempre la aproximación hacia adelante es mayor que la aproximación hacia atrás.




Universidad de Ingeniería y Tecnología               Métodos Numéricos       May 26, 2026   12 / 37
    INTEGRACIÓN

2   NUMÉRICA
Logros

   1   Aplica el método de Simpson 1/3 en la aproximación de integrales.
   2   Calcula el error estimado (cota del error).




Universidad de Ingeniería y Tecnología     Métodos Numéricos        May 26, 2026   14 / 37
Motivación




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 26, 2026   15 / 37
Motivación
Existen integrales que pueden ser hallados analíticamente haciendo uso del
segundo teorema fundamental del cálculo, sin embargo no todas las funciones
poseen antiderivada. En general
                       Z b
                             f (x)dx = F (b) − F (a)         donde         F ′ (x) = f (x)
                        a

Calcule (si es posible)
    Z 2
        ln(x) dx
         1
       Z 2
                   2
             e−x dx
         0
y comente sobre la necesidad de utilizar un método numérico


Universidad de Ingeniería y Tecnología                 Métodos Numéricos                 May 26, 2026   16 / 37
Introducción

La función que va a diferenciarse o integrarse estará, usualmente, en una de las
siguientes tres formas:
       Una función continua simple como un polinomio, una función exponencial o
       una función trigonométrica.
       Una función continua complicada que es difícil o imposible de diferenciar o
       integrar.
       Una función tabulada donde los valores de x y f (x) son dados en un conjunto
       discreto de puntos, lo cual es el caso cuando se tienen datos experimentales o
       de campo.




Universidad de Ingeniería y Tecnología    Métodos Numéricos           May 26, 2026   17 / 37
Cálculo aproximado de la Integral




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 26, 2026   18 / 37
Fórmula de Integración de Newton Cotes
Las Fórmulas de Newton Cotes son los tipos de integración más comunes, se
basan en la estrategia de reemplazar una función complicada ó datos tabulados por
un polinomio de aproximación que es fácil de integrar.
                                              Z b               Z b
                                         I=         f (x)dx ≈         Pn (x)dx
                                               a                 a

donde:
                                 Pn (x) = a0 + a1 x + . . . + an−1 x n−1 + an x n




Universidad de Ingeniería y Tecnología                   Métodos Numéricos          May 26, 2026   19 / 37

Ejemplo 1:
Para calcular el área bajo la gráfica de la curva, es decir la integral definida
(suponiendo que es complicada o imposible), en (a) se utiliza un polinomio de
primer grado (una recta) como una aproximación. Mientras que en (b), se emplea
una parábola con el mismo propósito.




Universidad de Ingeniería y Tecnología   Métodos Numéricos        May 26, 2026   20 / 37
Formalización de contenidos
Otra forma de obtener una estimación más exacta de una integral consiste en usar
polinomios de grado superior para unir los puntos.

  Regla de Simpson 1/3
 Resulta cuando el polinomio de interpolación de segundo grado P2 (x) se integra:
                                              Z b               Z b
                                         I=         f (x)dx ≈         P2 (x)dx
                                               a                 a

 Se consideran los puntos de interpolación (a, f (a)), (c, f (c)) y (b, f (b)) donde
 c = a+b
      2 para construir el polinomio interpolante de segundo grado.




Universidad de Ingeniería y Tecnología                   Métodos Numéricos       May 26, 2026   21 / 37
Obtención y estimación del error de la regla de
Simpson 1/3
Desarrollando                                 Z b               Z b
                                         I=         f (x)dx ≈         P2 (x)dx
                                               a                 a
se tiene que

                                h                                      1
                         I=       [f (a) + 4f (c) + f (b)] +        − f (4) (ξ )h5
                               |3          {z            }          | 90 {z      }
                               Regla de Simpson 1/3             Error de truncamiento
         Donde:
         h = b−a
               2 es el tamaño de paso,
         c = a+b
              2 es el punto medio,
         a < ξ < b.

Universidad de Ingeniería y Tecnología                   Métodos Numéricos              May 26, 2026   22 / 37
Ejemplo 2:

Aplique la regla de Simpson 1/3 para aproximar
                                         Z 2
                                               ln(x)dx
                                          1

y encuentre el error estimado (cota del error) para la aproximación.




Universidad de Ingeniería y Tecnología         Métodos Numéricos       May 26, 2026   23 / 37
Solución:
Para Simpson 1/3 simple (n = 2): con h = 12 , puntos x = {1, 1.5, 2}:
                        Z 2                                                           
                                2−1                                  3
               S2 =   ln(x)dx ≈                         ln(1) + 4 ln( ) + ln(2)            ≈ 0.385835
                    1            6                                   2

Sea                                                                               
                                                                              −1
                                         f (x) = ln(x), f (4) (x) = 6
                                                                              x4
y el error de la regla de Simpson se puede acotar en el intervalo [1,2] como sigue

                                             h5 (4)       (0.5)5
                                |E2 | = −       f (x) ≤ 6        ≈ 0.002083
                                             90             90




Universidad de Ingeniería y Tecnología                    Métodos Numéricos                     May 26, 2026   24 / 37
Continuación ...

Finalmente,                              Z 2
                                               ln(x) = 0.385835 ± 0.002083
                                          1
Note que el valor exacto de la integral está dentro de este intervalo:
                            Z 2
                                                      2
                      I=          ln(x) dx = x ln x − x 1 = 2 ln 2 − 1 ≈ 0.386294
                              1

                                    Error real |S2 − I| = 4.597637 × 10−4 .




Universidad de Ingeniería y Tecnología                   Métodos Numéricos      May 26, 2026   25 / 37
La regla de Simpson 1/3 Compuesta
La regla de Simpson 1/3 se mejora al dividir el intervalo de integración en varios
segmentos de un mismo tamaño.




Universidad de Ingeniería y Tecnología   Métodos Numéricos           May 26, 2026   26 / 37
Continuación ...
Consideremos la partición regular x0 , x1 , x2 , · · · , xn del intervalo [a, b] donde a = x0 ,
b = xn , h = b−a
              n
En este caso se debe considerar n PAR (pues se integrará en cada tres puntos)
                    Z b                      Z xn
              I=          f (x)dx        =          f (x)dx
                      a                        x0

                                             Z x2                 Z x4                          Z xn
                                         =          f (x)dx +            f (x)dx + . . . +               f (x)dx
                                               x0                   x2                            xn−2

Al sustituir la regla de Simpson 1/3 en cada integral se obtiene
            h                                 h                                        h
       I≈     (f (x0 ) + 4f (x1 ) + f (x2 )) + (f (x2 ) + 4f (x3 ) + f (x4 )) + . . . + (f (xn−2 ) + 4f (xn−1 ) + f (xn ))
            3                                 3                                        3




Universidad de Ingeniería y Tecnología                        Métodos Numéricos                           May 26, 2026       27 / 37
Finalmente:
  Regla de Simpson 1/3 compuesta
                                                                              
                                          n−1             n−2
                           h             X               X
                        I≈    f (x0 ) + 4     f (xi ) + 2     f (xi ) + f (xn )
                           3
                                           i=1,3,5             i=2,4,6


el error estimado en la regla de Simpson 1/3 Compuesta se obtiene sumando los
errores individuales de los segmentos

                              (b − a)5 (4)       (b − a) 4 (4)
                  E =−              4
                                      f (ξ ) = −        h f (ξ ),        x0 < ξ < xn
                               180n                180




Universidad de Ingeniería y Tecnología               Métodos Numéricos             May 26, 2026   28 / 37
Ejercicio guiado:
Dada la integral:
                                              Z 2
                                         I=          ln(x)dx
                                               1


   1   Aplique la regla de Simpson 1/3 compuesta considerando n = 4 subintervalos
       para hallar un valor aproximado para I y encuentre el error estimado (cota del
       error) para la aproximación.
   2   Realice el cálculo anterior ahora para n = 6
   3   Compare los resultados para Simpson 1/3 simple, Simpson 1/3 compuesto con
       4 intervalos, Simpson 1/3 compuesto con 6 intervalos y el valor exacto.




Universidad de Ingeniería y Tecnología             Métodos Numéricos   May 26, 2026   29 / 37
Simpson 1/3 compuesta (n = 4)
h = 14 , x = {1, 1.25, 1.5, 1.75, 2}:

                                 hh                                                i
                       S4 =         f (1) + 4 f (1.25) + f (1.75) + 2f (1.5) + f (2) .
                                 3

                                               S4 = 0.386260

                       1        1
Cota: |E4 | ≤                =      ≈ 1.302083 × 10−4 .
                     30 · 44   7680

                                    Error real |S4 − I| = 3.479831 × 10−5 .




Universidad de Ingeniería y Tecnología                Métodos Numéricos                  May 26, 2026   30 / 37
Simpson 1/3 compuesta (n = 6)
h = 16 , x = 1, 76 , 43 , 32 , 53 , 11
     
                                    6 ,2 :

                                         hh                                         i
                               S6 =         f0 + 4(f1 + f3 + f5 ) + 2(f2 + f4 ) + f6 .
                                         3

                                                  S6 = 0.386287

                       1         1
Cota: |E6 | ≤                =       ≈ 2.572016 × 10−5 .
                     30 · 64   38880

                                    Error real |S6 − I| = 7.197841 × 10−6 .




Universidad de Ingeniería y Tecnología                    Métodos Numéricos              May 26, 2026   31 / 37
Comparación de resultados
           Método                         Aprox.       Error abs.       Cota
           Exacto 2 ln 2 − 1             0.386294         –               –
           Simpson simple n = 2          0.385835   4.5976 × 10−4   2.0833 × 10−3
           Simpson comp. n = 4           0.386260   3.4798 × 10−5   1.3021 × 10−4
           Simpson comp. n = 6           0.386287   7.1978 × 10−6   2.5720 × 10−5
                      1 4
Observación: la cota 30 h decrece ∝ n−4 , consistente con el orden O(h4 ) de Simpson.




Universidad de Ingeniería y Tecnología         Métodos Numéricos          May 26, 2026   32 / 37
Conceptualización - EF 2024-2
Sea la función:
                                         f (x) = 2ex−4
Definida en el intervalo [2, 6]. Al aproximar la integral definida en este intervalo
usando la regla de Simpson 1/3 con un tamaño de paso h = 1, el error E está
acotado por |E| ≤ M, donde M = 0.3284. Determine el valor de verdad del
enunciado y justify su respuesta de manera detallada.




Universidad de Ingeniería y Tecnología        Métodos Numéricos         May 26, 2026   33 / 37
Aplicación - EF 2023-2
La forma de los cables de suspensión principales de un puente colgante puede ser
modelada aproximadamente por la función
                                          !
                    ex/1.24 + e−x/1.24
      f (x) = 1.24                     −1     para    − 1.2 ≤ x ≤ 1.2 Km .
                             2

La longitud de los cables suspendidos principales está dado por la integral:
                                              Z 1.2 q
                                         L=          1 + (f ′ (x))2 dx
                                               −1.2

Aproxime la longitud del cable de suspensión principal utilizando el Método de
Simpson 1/3. Considere 4 subintervalos.




Universidad de Ingeniería y Tecnología                Métodos Numéricos   May 26, 2026   34 / 37
Aplicación - EF 2023-1
Determine el valor de verdad de la siguiente afirmación. Dada la información
registrada:
                          t 0 0.75 1.5 2.25          3
                                         y 0 0.51    a     1.75 0.42
Si el área aproximada bajo la curva en t ∈ [0, 3] y el eje X es 3.21 usando el
método de Simpson 1/3 compuesto, entonces el valor de a es 1.5.




Universidad de Ingeniería y Tecnología              Métodos Numéricos   May 26, 2026   35 / 37
Conclusiones:




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 26, 2026   36 / 37
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
