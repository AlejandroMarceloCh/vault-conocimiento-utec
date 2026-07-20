---
curso: METNUM
titulo: 11 - Semana 10/Sem10_Laboratorio de Diferenciación e Integración Numérica
slides: 14
fuente: 11 - Semana 10/Sem10_Laboratorio de Diferenciación e Integración Numérica.pdf
---

Métodos
Numéricos
Diferenciación Numérica
Semana 10
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


1 Diferenciación Numérica




2 Actividad




Universidad de Ingeniería y Tecnología   Métodos Numéricos   May 26, 2026   1 / 13
        Objetivos:
            Implementar en MATLAB esquemas de diferencias finitas (adelante, atrás y
            centrada) para estimar derivadas, variando el tamaño de paso para analizar su
            efecto en el error.




Universidad de Ingeniería y Tecnología        Métodos Numéricos              May 26, 2026   2 / 13
    DIFERENCIACION

3   NUMERICA
Diferenciación Numérica
Halle la derivada de f (x) = x 2 ln(x) y evaluar la derivada en x0 = 2

 1   clc
 2   syms x
 3   f=inline('x^2*log(x)')
 4   Der01=diff(f(x))
 5   Der01_value=vpa(subs(Der01,2),15)




Universidad de Ingeniería y Tecnología   Métodos Numéricos               May 26, 2026   4 / 13
Continuación...
Aproximación de la 1era Derivada con 2 puntos:
Derivada hacia adelante:
                                                       f (x0 + h) − f (x0 )
                                         f ′ (x0 ) ≈
                                                                h



 1   x0=2;
 2   h=0.01;
 3   Der1_Adelante=(f(x0+h)-f(x0))/h

Derivada hacia atrás:
                                                       f (x0 ) − f (x0 − h)
                                         f ′ (x0 ) ≈
                                                                 h


Universidad de Ingeniería y Tecnología                    Métodos Numéricos   May 26, 2026   5 / 13
Continuación...
Derivada central:
                                                       f (x0 + h) − f (x0 − h)
                                         f ′ (x0 ) ≈
                                                                 2h



 1   format long
 2   x0=2;
 3   h=0.01;
 4   Der1_Central=(f(x0+h)-f(x0-h))/(2*h)




Universidad de Ingeniería y Tecnología                      Métodos Numéricos    May 26, 2026   6 / 13
Continuación...
Aproximación de la 1era Derivada con 4 puntos
Dado los puntos:
(x0 − 2h; f (x0 − 2h)), (x0 − h; f (x0 − h)), (x0 + h; f (x0 + h)), (x0 + 2h; f (x0 + 2h))

                                 f (x0 − 2h) − 8f (x0 − h) + 8f (x0 + h) − f (x0 + 2h)
                    f ′ (x) =
                                                         12h



 1   format long
 2   x0=2;
 3   h=0.01;
 4   Der1_4p=(f(x0-2*h)-8*f(x0-h)+8*f(x0+h)-f(x0+2*h))/(12*h)
 5   error=abs(Der1_4p-Der01_value)


Universidad de Ingeniería y Tecnología                Métodos Numéricos              May 26, 2026   7 / 13
Aplicación Diferenciación Numérica

                                         ∂f                  ∂f
Dada la función f (x, y ) = ex sen(y ), calcule
                                            (2; 3) y también    (2; 3),
                                         ∂x                  ∂y
considerando un tamaño de paso h = 0.01. Compare sus resultados con el valor
exacto.




Universidad de Ingeniería y Tecnología     Métodos Numéricos    May 26, 2026   8 / 13
Ajuste - EL2 2025-0
En un proyecto de ingeniería civil, se está estudiando la relación entre la carga aplicada x
(en toneladas) y la deflexión y (en milímetros) en una viga de acero. Se realizaron
mediciones experimentales y se obtuvieron los siguientes datos:
                                    x (toneladas)   10     20     30      40     50
                                       y (mm)       2.5    4.8    6.9     8.7   10.5
Se desea modelar la relación entre la carga x y la deflexión y mediante un ajuste lineal de
la forma y = mx + b, donde m es la pendiente y b es el intercepto. Realice lo siguiente:
   1   Plantee el sistema sobredeterminado Mp = y donde p = [m; b]. Almacene la matriz
       aumentada del sistema [M y ] en la variable MY.
   2   Determine el sistema de ecuaciones normales Ap = B. Almacene la matriz
       aumentada del sistema [A B] en la variable AB.
   3   Obtenga los valores de la pendiente e intercepto del modelo lineal, almacene los
       resultados en las variables pendiente e intercepto, respectivamente.
   4   Halle el valor del coeficiente de determinación r 2 . Almacene su respuesta en la
       variable r2.
Universidad de Ingeniería y Tecnología                    Métodos Numéricos            May 26, 2026   9 / 13
Integración A - EL2 2025-0
                       p
Considere la siguiente función f (x) =          4 − x 2 , con −1 ≤ x ≤ 1:
                                                y
                                           2


                                          1.5


                                           1


                                          0.5

                                                                    x
                                     −1                         1

Universidad de Ingeniería y Tecnología      Métodos Numéricos               May 26, 2026   10 / 13
Integración B - EL2 2025-0
Esta función al rotar genera un sólido de revolución como el mostrado en la figura:




Universidad de Ingeniería y Tecnología   Métodos Numéricos          May 26, 2026   11 / 13
Integración C - EL2 2025-0
La teoría nos dice que el área de la superficie obtenida al rotar una curva alrededor
del eje X generada por y = f (x), cuando f es positiva y tiene derivada continua,
está dada por:
                                        s
                                                 df (x) 2
                            Z b                       
                      S=        2π f (x) 1 +              dx
                              a                    dx

Se le pide implementar un script que efectúe lo siguiente:
   1 Calcule el área exacta de revolución y almacénela en la variable exac usando
       la función integral de Matlab.
   2 Use la cuadratura de Gauss con 10 puntos para encontrar el área y
       almacénela en la variable aproxCG.
   3 Encuentre el área aproximada utilizando el método de Trapecio compuesto (20
       subintervalos), almacene el resultado obtenido en la variable aproxTC.
   4 Encuentre el área superficial usando el método de Simpson 1/3 compuesto
       con 20 subintervalos y almacénela en
Universidad de Ingeniería y Tecnología
                                               la variable aproxSC.
                                          Métodos Numéricos            May 26, 2026 12 / 13
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
