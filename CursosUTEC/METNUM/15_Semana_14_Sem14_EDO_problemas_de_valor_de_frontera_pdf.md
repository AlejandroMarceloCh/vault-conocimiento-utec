---
curso: METNUM
titulo: 15 - Semana 14/Sem14_EDO problemas de valor de frontera
slides: 34
fuente: 15 - Semana 14/Sem14_EDO problemas de valor de frontera.pdf
---

Métodos
Numéricos
EDO-PVF - S14
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
                                            1 Ecuaciones       Difer-
                                              enciales    Ordinarias
                                              Lineales de Segundo
                                              Orden con valores en la
                                              Frontera
                                            2 Método del Disparo
                                            3 Método de Diferencias
                                              Finitas




Universidad de Ingeniería y Tecnología   Métodos Numéricos        June 1, 2026   1 / 33
        Objetivos
            Resolver problemas de valor de frontera (PVF) mediante el método de disparo
            Resolver problemas de valor de frontera mediante diferencias finitas,
            formulando el sistema algebraico para obtener solución numérica aproximada.




Universidad de Ingeniería y Tecnología        Métodos Numéricos             June 1, 2026   2 / 33
1   EDO lineales de
    Segundo Orden con
    Valores en la Frontera
Problema de Valor de Frontera (PVF)
Ya sabemos resolver un Problema de Valor Inicial (PVI) de 2do orden:

  PVI
                                         y ′′ = f (x, y , y ′ )    para       a≤x ≤b
                                               y (a) = y0 ,           y (a) = y0′ .
                                                                        ′


Ahora estamos interesados en resolver:

  PVF
                                         y ′′ = f (x, y , y ′ )    para       a≤x ≤b
                                                 y (a) = α,            y (b) = β

Este problema se conoce como Problema de Valor de Frontera (PVF)


Universidad de Ingeniería y Tecnología                            Métodos Numéricos    June 1, 2026   4 / 33
Existencia y unicidad de la solución del PVF
        La solución numérica del PVF planteado dependerá de la garantía de la
        existencia de una solución única.
        No siempre un PVF tiene solución única.

  Existencia y unicidad de la solución de un PVF
 La existencia de la solución única del PVF está garantizada siempre que:
         ∂f ∂f
   1 f,    ,     son continuas en D = {(x, y , y ′ ) | x ∈ [a, b], y ∈ R, y ′ ∈ R}.
        ∂y ∂y ′
         ∂f
    2       >0          en D.
         ∂y
                                         ∂f
    3   Existe una constante M tal que        ≤M        en D.
                                         ∂y ′

Universidad de Ingeniería y Tecnología     Métodos Numéricos               June 1, 2026   5 / 33
Ejemplo
Consideremos el PVF:
                                         2      2     sin(ln(x))
                                 y ′′ = − y ′ + 2 y +            , 1 ≤ x ≤ 2,
                                         x     x          x2
                                                y (1) = 1,        y (2) = 2

   1   Tenemos D = {(x, y , y ′ ) | x ∈ [1, 2], y ∈ R, y ′ ∈ R}
   2   La función f (x, y , y ′ ) = − x2 y ′ + x22 y + sen(ln(x))
                                                          x2
                                                                  es continua en D
       ∂f    2     ∂f      2
   3   ∂y = x 2 , ∂y ′ = − x también son continuas en D.
       ∂f    2    1
   4   ∂y = x 2 ≥ 2 > 0 en D.

   5   Existe M = 2 tal que              ∂f
                                         ∂y ′    = x2 ≤ M en D.
Como se verifican las condiciones del teorema hay solución única.
Universidad de Ingeniería y Tecnología                       Métodos Numéricos       June 1, 2026   6 / 33
PVF lineales
Dado un PVF
                                         y ′′ = f (x, y , y ′ )    para       a≤x ≤b
                                                 y (a) = α,            y (b) = β
Definición: Si la función f (x, y , y ′ ) se puede expresar como

                                         f (x, y , y ′ ) = p(x)y ′ + q(x)y + r (x),

se dice que la EDO de segundo orden y ′′ = f (x, y , y ′ ) es lineal.

En este caso, una solución única existe si:
   1   p(x), q(x) y r (x) son continuas en [a, b].

   2   q(x) > 0 en [a, b].



Universidad de Ingeniería y Tecnología                            Métodos Numéricos    June 1, 2026   7 / 33
PVF lineales (continuación)
Verifiquemos que el PVF:

                                         2      2     sin(ln(x))
                                 y ′′ = − y ′ + 2 y +            , 1 ≤ x ≤ 2,
                                         x     x          x2
                                                y (1) = 1,        y (2) = 2

es lineal, en efecto f (x, y , y ′ ) = p(x)y ′ + q(x)y + r (x)
donde          p(x) = − x2 ,             q(x) = x22 ,   r (x) = sen(ln(x)
                                                                   x2
                                                                          .
Observe que:
   1   p(x), q(x) y r (x) son continuas en [1, 2].
   2   q(x) = x22 > 0.
Por lo tanto, el PVF lineal tiene solución única.


Universidad de Ingeniería y Tecnología                       Métodos Numéricos   June 1, 2026   8 / 33
Métodos numéricos para resolver PVF
       Hay diferentes métodos numéricos que permite obtener soluciones
       aproximadas a un PVF.

       Veremos dos técnicas bien conocidas para PVF lineales:
          1   El método del disparo.

          2   El método de las diferencias finitas.




Universidad de Ingeniería y Tecnología           Métodos Numéricos   June 1, 2026   9 / 33
2   PVF
    METODO DEL DISPARO
Método del disparo para PVF lineales
Dado el problema de valor frontera (PVF):

                                 y ′′ = p(x)y ′ + q(x)y + r (x)             a≤x ≤b
                                           y (a) = α,         y (b) = β

Planteamos dos problemas de valor inicial (PVI)
                      (
                       y ′′ = p(x)y ′ + q(x)y + r (x)                          a≤x ≤b
          (PVI 1)
                       y (a) = α, y ′ (a) = 0.
                                         (
                                          y ′′ = p(x)y ′ + q(x)y             a≤x ≤b
                         (PVI 2)
                                          y (a) = 0, y ′ (a) = 1,




Universidad de Ingeniería y Tecnología                  Métodos Numéricos               June 1, 2026   11 / 33
continuación...
Una vez resueltos los PVI formulados obtenemos las soluciones y1 (x) y y2 (x)
(respectivamente). Entonces la función

                                                            (β − y1 (b))
                                         y (x) = y1 (x) +                y2 (x)
                                                               y2 (b)

siempre que y2 (b) ̸= 0 constituye una solución para el problema de valor frontera
PVF inicialmente planteado.

  Ejercicio
 Verifique que la solución propuesta y (x) efectivamente satisface:

                                 y ′′ = p(x)y ′ + q(x)y + r (x)                 a≤x ≤b
                                              y (a) = α,          y (b) = β

Universidad de Ingeniería y Tecnología                      Métodos Numéricos            June 1, 2026   12 / 33
Solución del ejercicio
Sean y1 , y2 las soluciones de los problemas (PVI 1), (PVI 2). Sea y = y1 + λy2 con
λ = (β−y  1 (b))
      y2 (b) .
       Se cumplen las condiciones de frontera:

                               y(a) = y1 (a) + λy2 (a) = y1 (a) = α
                               y (b) = y1 (a) + λy2 (a) = y1 (b) + (β − y1 (b)) = β

       Cumple la ecuación diferencial

                                         y ′′ = y1′′ + λy2′′
                                             = (py1′ + qy1 + r ) + λ(py2′ + qy2 )
                                             = p(y1′ + λy2′ ) + q(y1 + λy2 ) + r
                                             = py ′ + qy + r

Por lo tanto, y = y1 + λy2 es solución del PVF.
Universidad de Ingeniería y Tecnología                         Métodos Numéricos      June 1, 2026   13 / 33
  Ejemplo 3
 Resuelva el PVF:
                                       2      2     sin(ln(x))
                               y ′′ = − y ′ + 2 y +            ,              1 ≤ x ≤ 2,
                                       x     x          x2
                                            y (1) = 1,        y (2) = 2
 mediante el método del disparo tomando h = 0.25

Los PVI que se tienen que resolver son:
   1   y1′′ = − x2 y1′ + x22 y1 + sin(ln(x))
                                      x2
                                             ,    1 ≤ x ≤ 2,          y1 (1) = 1,           y1′ (1) = 0

   2   y2′′ = − x2 y2′ + x22 y2 ,        1 ≤ x ≤ 2,   y2 (1) = 0,            y2′ (1) = 1.
Resolvemos los PVI con el método de RK4 para sistemas. Finalmente yaprox .


Universidad de Ingeniería y Tecnología                   Métodos Numéricos                         June 1, 2026   14 / 33
Resultados numéricos: PVI 1
                                          x       y1 (x)      y1′ (x)
                                         1.00   1.000000    0.000000
                                         1.25   1.048730    0.343633
                                         1.50   1.158625    0.517621
                                         1.75   1.301725    0.618762
                                         2.00   1.465033    0.683174

Resultados numéricos: PVI 2
                                          x       y2 (x)      y2′ (x)
                                         1.00   0.000000    1.000000
                                         1.25   0.202989    0.674975
                                         1.50   0.351483    0.531068
                                         1.75   0.474132    0.457834
                                         2.00   0.582985    0.416711

Universidad de Ingeniería y Tecnología              Métodos Numéricos   June 1, 2026   15 / 33
       La solución general del disparo es yaprox (x) = y1 (x) + λ y2 (x), donde

                                  2 − y1 (2)   2 − 1.4650326165
                          λ=                 =                  = 0.9176345573.
                                    y2 (2)       0.5829852191

       Finalmente se halla yaprox . Se proporciona la solución exacta para referencia.

              x             y1              y2        yaprox              yexacta      Er
             1.00        1.000000        0.000000   1.000000            1.000000    0.000000
             1.25        1.048730        0.202989   1.235000            1.235007    0.000005
             1.50        1.158625        0.351483   1.481157            1.481159    0.000001
             1.75        1.301725        0.474132   1.736806            1.736806    0.000000
             2.00        1.465033        0.582985   2.000000            2.000000    0.000000




Universidad de Ingeniería y Tecnología              Métodos Numéricos                  June 1, 2026   16 / 33
3   PVF
    METODO DE DIFERENCIAS
    FINITAS
Método de diferencias finitas para PVF lineales
       Consideremos el PVF
                                     y ′′ = p(x)y ′ + q(x)y + r (x)                a≤x ≤b
                                                    y (a) = α,          y (b) = β

       Este problema se puede resolver por el Método de las Diferencias Finitas.
       Se divide el intervalo [a, b] en n + 1 subintervalos igualmente espaciados, con
       un paso: h = b−a   n+1 .
       Se define x0 = a, xn+1 = b, y n puntos o nodos internos xi = x0 + ih para
       i = 1, 2, 3, · · · , n.
       A partir de la EDO, en cada uno de los nodos

                                         y ′′ (xi ) = p(xi )y ′ (xi) + q(xi )y (xi ) + r (xi ).



Universidad de Ingeniería y Tecnología                         Métodos Numéricos                  June 1, 2026   18 / 33
Método de diferencias finitas para PVF lineales
       El Método de las Diferencias Finitas se basa en sustituir las derivadas por
       fórmulas en diferencias.
       La fórmula en diferencias finitas centradas para la derivada primera:
                                                       y (xi+1 ) − y (xi−1 )
                                         y ′ (xi ) =                         + O(h2 )
                                                                2h

       La fórmula en diferencias finitas centradas para la derivada segunda:
                                                 y (xi+1 ) − 2y (xi ) + y (xi−1 )
                                  y ′′ (xi ) =                                    + O(h2 )
                                                               h2

       Así se eliminan las derivadas y el problema se transforma en un sistema de
       ecuaciones lineales (un sistema de n ecuaciones con n incógnitas).



Universidad de Ingeniería y Tecnología                       Métodos Numéricos               June 1, 2026   19 / 33

Método de diferencias finitas para PVF lineales
       Considerando las expresiones:

                                                          y (xi−1 ) ≈ yi−1

                                                             y (xi ) ≈ yi
                                                          y (xi+1 ) ≈ yi+1
                               p(xi ) = pi            ;      q(xi ) = qi           ;    r (xi ) = ri
       Reemplazamos en la ecuación diferencial

                                         y ′′ (xi ) = p(xi )y ′ (xi) + q(xi )y (xi ) + r (xi ).




Universidad de Ingeniería y Tecnología                         Métodos Numéricos                       June 1, 2026   20 / 33
Método de diferencias finitas para PVF lineales
       Obteniendo la ecuación discretizada:
              yi+1 − 2yi + yi−1   pi (yi+1 − yi−1 )
                       2
                                =                   + qi yi + ri ,   para i = 1, 2, . . . n.
                     h                   2h
       La cual puede ser reescrita como:
                                         
               h                         h
        −1 − pi yi−1 +(2+h2 qi )yi + −1 + pi yi+1 = −h2 ri ,                  para i = 1, 2, . . . n.
               2                         2

       Teniendo en cuenta que y0 e yn+1 son valores conocidos, se plantea un
       sistema de n ecuaciones lineales con n incógnitas de la forma:

                                                Ay = b̂.



Universidad de Ingeniería y Tecnología           Métodos Numéricos             June 1, 2026    21 / 33
  Método de diferencias finitas para PVF lineales
 Para el PVF
                                 y ′′ = p(x)y ′ + q(x)y + r (x)                a≤x ≤b
                                             y (a) = α,          y (b) = β

 El sistema lineal Ay = b
                        b a resolver es
                                                                            
                           b1       c1      0 ···      0       y1     d1 − a 1 α
                          a2
                                   b2     c2 · · ·    0     y2   d2 
                                                                             
                          0        a3     b3 · · ·    0     ..        .
                                                                           .
                                                            .  = 
                                                                                 
                          
                           ..                                             .     
                                    ..     .. ..                             
                          .           .     .    .   cn−1  yn−1     dn−1 
                             0      ···     0 an       bn      yn      dn − cn β


 donde

 ai = −1 − h2 pi , bi = (2+h2 qi ), ci = −1 + h2 pi , di = −h2 ri ,
                                                  
                                                                                        i = 1, 2, · · · , n.
Universidad de Ingeniería y Tecnología                     Métodos Numéricos             June 1, 2026   22 / 33
Método de diferencias finitas para PVF lineales
       Note que las condiciones de frontera, que aparecen en la primera y en la
       última ecuación, se pasaron al lado izquierdo.

       Sean p, q y r continuas en [a, b]. Si q ≥ 0 para todo x ∈ [a, b], entonces el
       sistema Ay = b̂ tiene solución única, siempre que:

                                                  2
                                             h<
                                                  M
       donde
                                         M = max |p(x)|
                                             x∈[a,b]




Universidad de Ingeniería y Tecnología      Métodos Numéricos           June 1, 2026   23 / 33
Método de diferencias finitas para PVF lineales
  Ejemplo 4
 Resuelva el PVF:
                                     2      2     sin(ln(x))
                             y ′′ = − y ′ + 2 y +            ,            1 ≤ x ≤ 2,
                                     x     x          x2
                                         y (1) = 1,        y (2) = 2
 mediante el método de diferencias finitas seleccionando h = 0.25




Universidad de Ingeniería y Tecnología                Métodos Numéricos                June 1, 2026   24 / 33
solución
       Número de subintervalos: Dado que h = b−a       b−a
                                             n+1 =⇒ n = h − 1 = 3

       Identificamos: p(x) = − x2 ; q(x) = x22 y r (x) = sin(ln
                                                            x2
                                                                x)

       Reemplazamos en:
                                        
             h                          h
        −1 − pi yi−1 +(2+h qi )yi + −1 + pi yi+1 = −h2 ri ,
                          2
                                                                     para i = 1, 2, . . . n.
             2                          2

       Y formulamos el sistema de ecuaciones lineales Ay = b̂ a resolver:

             2 + h2 q1 −1 + h2 p1                        −h r1 + 1 + h2 p1 α
                                               2                      
                                     0           y1
           −1 − h p2 2 + h2 q2 −1 + h p2  . y2  =           −h2 r2      
                  2                    2
                             h         2                    2           h
                                                                          
                0      −1 − 2 p3 2 + h q3        y3      −h r3 + 1 − 2 p3 β

Sustituyendo los valores correspondientes, el sistema Ay = b̂ es:

Universidad de Ingeniería y Tecnología        Métodos Numéricos      June 1, 2026   25 / 33
solución (continuación)
Planteamos el sistema de ecuaciones:
                                                     
          2.080000 −1.200000         0      y1   0.791148
        −0.833333 2.055556 −1.166667 y2  = −0.010957
               0       −0.857143 2.040816   y3   2.274880

Resolviendo el sistema Ay = b̂ se obtiene:

                                                     
                                              1.234737
                                         y = 1.480921
                                              1.736678




Universidad de Ingeniería y Tecnología        Métodos Numéricos   June 1, 2026   26 / 33
Método de diferencias finitas para PVF lineales
Así, calculando las soluciones exactas y comparando con las aproximaciones
obtenidas:

                                    x       yaprox     yexacta           Er
                                   1.00   1.000000   1.000000
                                   1.25   1.234737   1.235007
                                   1.50   1.480921   1.481159
                                   1.75   1.736678   1.736806
                                   2.00   2.000000   2.000000




Universidad de Ingeniería y Tecnología               Métodos Numéricos        June 1, 2026   27 / 33
Ejercicio: Datos y contexto
Supongamos que la ecuación diferencial que modela la temperatura T (x) a lo largo
de una barra es:
                                 d 2T      q
                                     2
                                       =−
                                  dx       k
donde:
       T (x) es la temperatura en el punto x de la barra.
       q es la generación de calor por unidad de volumen.
       k es la conductividad térmica.
Dado:
       q = 500
       k = 100
       T (0) = 300 K
       T (10) = 400 K
Universidad de Ingeniería y Tecnología     Métodos Numéricos       June 1, 2026   28 / 33
Preguntas
 1) Comprensión de los Elementos Fundamentales:
              Explique los principios de los métodos del Disparo y de Diferencias Finitas. ¿En
              qué situaciones es más conveniente usar uno sobre el otro para resolver
              problemas de valor en frontera?
 2) Implementación de Algoritmos:
              Desarrolle un algoritmo en pseudocódigo para implementar el método del
              Disparo para resolver la EDO dada. Realice la integración numérica desde x = 0
              hasta x = 10 con un tamaño de paso h = 1.
              Desarrolle un algoritmo en pseudocódigo para implementar el método de
              Diferencias Finitas para resolver la misma EDO. Utilice un tamaño de paso h = 1
              y realice la integración desde x = 0 hasta x = 10.




Universidad de Ingeniería y Tecnología         Métodos Numéricos              June 1, 2026   29 / 33
Continuación...
 3) Aplicación Práctica de Conceptos Teóricos:
              Utilice los métodos del Disparo y de Diferencias Finitas para resolver la EDO y
              obtenga las soluciones numéricas de la temperatura T (x) desde x = 0 hasta
              x = 10. Compare los resultados obtenidos con cada método y discuta las
              diferencias observadas.
 4) Desafío de Pensamiento Crítico:
              Analice las posibles fuentes de error al usar los métodos del Disparo y de
              Diferencias Finitas en este contexto. ¿Cómo afectan estos errores a la precisión
              de la solución obtenida para la temperatura a lo largo de la barra? ¿Qué medidas
              podrías tomar para reducir estos errores? ¿Cómo podrías mejorar la estimación
              de la temperatura si los datos del sistema contuvieran ruido debido a mediciones
              imprecisas?




Universidad de Ingeniería y Tecnología         Métodos Numéricos               June 1, 2026   30 / 33
Conclusiones
       La solución de una EDO-PVF depende de la continuidad de los coeficientes y
       las condiciones de la ecuación.
       El método del disparo convierte el EDO-PVF en dos EDO-PVI, resuelve cada
       uno y combina los resultados para obtener la solución aproximada.
       El método de diferencias finitas transforma la ecuación diferencial PVF en un
       sistema algebraico para su solución numérica.




Universidad de Ingeniería y Tecnología    Métodos Numéricos           June 1, 2026   31 / 33
Bibliografía
      Steven C. Chapra and Raymond P. Canale
      Métodos numéricos para ingenieros, 7a ed.
      Richard L. Burden and J. Douglas Faires
      Análisis numérico, 7a ed.




Universidad de Ingeniería y Tecnología   Métodos Numéricos   June 1, 2026   32 / 33
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
