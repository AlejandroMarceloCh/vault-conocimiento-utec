---
curso: METNUM
titulo: 08 - Semana 6/Sem6_Casos SEL
slides: 33
fuente: 08 - Semana 6/Sem6_Casos SEL.pdf
---

Métodos Numéricos
Casos de SEL - S6
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
Ronaldo Walter Laureano Huayanay
(rlaureano@utec.edu.pe)


                                    Profesores: Utec-Ciencias
                                                  Índice
                                         1 Análisis   de Circuitos
                                           Eléctricos
                                         2 Sistema Masa-Resorte
                                         3 Discretización de una
                                           Ecuación Diferencial




Universidad de Ingeniería y Tecnología    Métodos Numéricos          1 / 32
        Resultados de Aprendizaje Específicos (RAE)
            Formular sistemas lineales desde discretización de modelos físicos.




Universidad de Ingeniería y Tecnología             Métodos Numéricos              2 / 32
1   CIRCUITOS
    ELÉCTRICOS
  CASO 1: Corrientes y voltajes en circuitos eléctricos
 Un problema común en ingeniería eléctrica es la determinación de corrientes y
 voltajes en algunos puntos de los circuitos con resistores. Tales problemas se
 resuelven utilizando las reglas para corrientes y voltajes de Kirchhoff.

                                              En cada unión, la suma de
                                              corrientes entrantes es igual a las
                                              salientes.
                                              La suma de cambios de voltaje en
                                              un recorrido cerrado debe ser cero.




Universidad de Ingeniería y Tecnología    Métodos Numéricos                    4 / 32
Ejemplo
Ahora determinaremos las ecuaciones para el siguiente circuito (ver Figura).
Aplicamos la regla 1 en la unión A: i1 + i3 = i2 .
En las dos aplicaciones de la regla de los lazos, nota que los signos en cada
ecuación se determinan según si la corriente se mueve de + a − o de − a +.




Universidad de Ingeniería y Tecnología     Métodos Numéricos                    5 / 32
Continuación...
Aplicar la regla 2 al lazo 1:

                                 −V1 + R1 i1 + R2 i2 + V2 + R4 i1 = 0

y

                                              (R1 + R4 )i1 + R2 i2 = V1 − V2

Aplicar la regla 2 al lazo 2:

                                          R 2 i2 + V 2 − V 3 + R 3 i3 = 0

y

                                                      R2 i2 + R3 i3 = V3 − V2


Universidad de Ingeniería y Tecnología                     Métodos Numéricos    6 / 32
Continuación...
Ahora tenemos tres ecuaciones y tres incógnitas:

                                 i1 − i2 + i3 = 0,
                                 (R1 + R4 )i1 + R2 i2 = V1 − V2 ,
                                 R2 i2 + R3 i3 = V3 − V2 .




Universidad de Ingeniería y Tecnología                       Métodos Numéricos   7 / 32
Ejercicio en Aula
Considere el circuito mostrado en la figura. Las corrientes asociadas con este
circuito son desconocidas, tanto en magnitud como en dirección. Esto no presenta
gran dificultad, ya que tan sólo se supone una dirección para cada corriente. Si la
solución resultante a partir de las leyes de Kirchhoff es negativa, entonces la
dirección supuesta fue incorrecta




Universidad de Ingeniería y Tecnología      Métodos Numéricos                  8 / 32
Continuación...
Suponiendo una dirección para las corrientes




Al aplicar el principio de conservación de carga en cada NODO (4 en cantidad) y
las diferencias de potencial para cada circuito o ciclo (2 en cantidad), planteamos
un sistema de 6 ecuaciones lineales cuyas 6 incógnitas son las intensidades de
corriente i indizadas por el nodo inicial y el nodo final.
Universidad de Ingeniería y Tecnología      Métodos Numéricos                   9 / 32
Continuación...
Ecuaciones de conservación de carga:
       nodo 2:
       nodo 3:
       nodo 4:
       nodo 5:
Ecuaciones de diferencia de potencial en cada circuito
       circuito 1:
       circuito 2:
Formule el sistema planteado en forma matricial y analice si es posible aplicar
algún método iterativo.




Universidad de Ingeniería y Tecnología     Métodos Numéricos                      10 / 32
          Ejercicio 2 (EP 2024 - 2)
          Procedimental: Dado el siguiente circuito:
                                           R3                   R6               R9                R12


                                                  V2                                    V4
                             R1                                      R7                                          R13

                                            i1                  i2                i3                i4

                                                  R4                                   R10
                              V1                                     V3                                     V5

                                           R2                   R5               R8                R11

                                       R1=2 Ω          R4=1 Ω        R7=1 Ω        R10=2 Ω        R13=1 Ω
                                       R2=2 Ω          R5=1 Ω        R8=1 Ω        R11=2 Ω
     R1
                                       R3=2 Ω          R6=1 Ω        R9=1 Ω        R12=2 Ω

i1                                    V1=20 VDC           V3=15 VDC            V5=20 VDC
                   R3
          V2                          V2=10 VDC           V4=10 VDC

i                  R6de Ingeniería y Tecnología
          Universidad                                                         Métodos Numéricos                        11 / 32
               R1 = 2 Ω              R4 = 1 Ω   R7 = 1 Ω      R10 = 2 Ω   R13 = 1 Ω

               R2 = 2 Ω              R5 = 1 Ω   R8 = 1 Ω      R11 = 2 Ω

               R3 = 2 Ω              R6 = 1 Ω   R9 = 1 Ω      R12 = 2 Ω




Universidad de Ingeniería y Tecnología                Métodos Numéricos               12 / 32
Continuación...
                                              X                      X
   1   [4 ptos] Aplicando la ley de Kirchoff (    caídas de voltaje=    fuentes de
       voltaje) para cada lazo, se obtiene un sistema de ecuaciones lineales (SEL).
       Exprese el SEL en la forma matricial Ax = b para estimar el vector de
                                    T                                       T
       corrientes x = i1 i2 i3 i4 , de manera que en b = b1 b2 b3 b4 se
       obtenga b1 , b3 > 0 y b2 , b4 < 0. Nota: considere que para el primer lazo se
       obtiene:
                           (R1 + R2 + R3 + R4 )i1 − R4 i2 = V1 + V2
   2   [2 ptos] Analice la convergencia del método iterativo de Jacobi mediante el
       criterio del radio espectral e indique si converge o diverge.
   3   [4 ptos] Realice 02 iteraciones utilizando el método de Jacobi algebraico o
                                                                       T
       matricial. Considere como vector semilla x(0) = 3 −3 3 −3 .
                                                        




Universidad de Ingeniería y Tecnología        Métodos Numéricos                  13 / 32
2   SISTEMA
    MASA-RESORTE
  CASO 2: Sistemas Masa-Resorte
 Dado el siguiente sistema masa-resorte con 3 bloques de masas diferentes,
 sostenido mediante 4 resortes:

                                         Al tratarse de un sistema masa-resorte,
                                         tenemos las siguientes ecuaciones,
                                         luego de hacer el D.C.L:
                                              k ∆l1 = k ∆l2 + k ∆l2 + m1 g
                                              k ∆l2 + k ∆l2 = k ∆l3 + m2 g
                                              k ∆l3 = m3 g




Universidad de Ingeniería y Tecnología    Métodos Numéricos                  15 / 32
Continuación...
Condición de balance de fuerzas:
   masa 1:
                kx1 = 2k(x2 − x1 ) + m1 g
       masa 2:
          2k(x2 − x1 ) = m2 g + k (x3 − x2 )
       masa 3:
                      k(x3 − x2 ) = m3 g
En forma matricial:
                          
     3k −2k 0         x1  m1 g
  −2k 3k −k  x2  = m2 g 
      0   −k     k    x3  m3 g

Universidad de Ingeniería y Tecnología         Métodos Numéricos   16 / 32
Ejercicio
                                         Los sistemas idealizados masa-resorte
                                         desempeñan un papel importante en la
                                         mecánica y en otros problemas de
                                         ingeniería. La figura muestra un arreglo de
                                         cuatro resortes en serie comprimidos por
                                         una fuerza de 2000 N. En el equilibrio, es
                                         posible desarrollar ecuaciones de balance
                                         de fuerzas si se definen las relaciones entre
                                         los resortes y así determinar los
                                         desplazamientos x1 , x2 , x3 y x4 . Para cada
                                         masa aplicamos la ley de Hooke,
                                         considerando el balance de fuerzas y los
                                         valores k1 = 150 N/m, k2 = 50 N/m, k3 = 75
                                         N/m y k4 = 225 N/m.

Universidad de Ingeniería y Tecnología    Métodos Numéricos                      17 / 32
Continuación...
Aplicamos la condición de balance de fuerzas para cada masa:
       masa 1:
       masa 2:
       masa 3:
       masa 4:
   1   Formule el sistema de ecuaciones lineales en forma matricial y resuélvalo por
       un método directo
   2   Es posible aplicar algún método iterativo?




Universidad de Ingeniería y Tecnología        Métodos Numéricos                 18 / 32
Ejercicio 3 (EP 2024 - 2)
Procedimental: Dado el siguiente sistema masa-resorte

                                   x2                           F
             +x
                                                           m2
                                                                                        K11 = K12 = K13 = 5 N/m
                                               K21                    K22               K21 = K22 = 15 N/m
                                   x1
   Movimiento de                                                                        m1 = m2 = 0 kg
   masas y resortes                                        m1
                                                                                        F = 12 N/m
   únicamente en
     eje vertical                                                                       g = 9.81 m/s2
                                         K11         K12        K13




Universidad de Ingeniería y Tecnología                              Métodos Numéricos                        19 / 32

Continuación...
   1   [4 ptos] Al aplicar la segunda ley de Newton a cada masa se obtiene un
       sistema de ecuaciones lineales (SEL). Exprese el SEL en la forma matricial
                                                                   T
       Ax = b para estimar el vector de desplazamientos x = x1 x2 , de manera
       que los valores de los elementos de la diagonal de A sean positivos.
   2   [3 ptos] Analice la convergencia del método iterativo de Jacobi. Indique si
       converge o diverge (solo 2 opciones).
   3   [3 ptos] Realice 02 iteraciones utilizando el método de Jacobi. Considere
                                        T
       como vector semilla x(0) = 1 1 . Halle el error relativo cometido en cada
                                   

       iteración.




Universidad de Ingeniería y Tecnología        Métodos Numéricos                  20 / 32
3
    DISCRETIZACIÓN
    DE
    ECUACIÓN
    DIFERENCIAL
  CASO 3: Discretizando una Ecuación Diferencial
 Las ecuaciones algebraicas lineales surgen al resolver por discretización una
 ecuación diferencial. Por ejemplo: En la siguiente figura se muestra una barra, la
 cual se encuentra en contacto con una pared a 120°C.




 La ecuación diferencial que describe la variación de temperatura en la barra es:

                                         d 2T      hc P
                                            2
                                                 −      (T − T∞ )       =0
                                         dx x=xi    kA            T =Ti
Universidad de Ingeniería y Tecnología                     Métodos Numéricos    22 / 32
Considerando que es posible aproximar la solución reemplazando la segunda
derivada por una aproximación (diferencia finita central):

                                         d 2T      Ti−1 − 2Ti + Ti+1
                                            2
                                                 =
                                         dx x=xi         ∆x 2

La discretización de la ecuación diferencial se presenta de la siguienta forma:

   d 2T      hc P                                           Ti−1 − 2Ti + Ti+1   hc P
      2
           −      (T − T∞ )       =0                 →               2
                                                                              =      (Ti − T∞ )
   dx x=xi    kA            T =Ti                                 ∆x             kA

Es decir, para cada nodo interior i (donde tiene sentido la aproximación de la
derivada) se cumple:

                                                        hc P∆x 2
                                  Ti−1 − 2Ti + Ti+1 =            (Ti − T∞ )
                                                           kA

Esto conduce a un sistema de ecuaciones lineales.
Universidad de Ingeniería y Tecnología                   Métodos Numéricos                  23 / 32
Condiciones de frontera en el sist. discretizado
La ecuación discretizada previamente es válida únicamente para los nodos
interiores. Para cerrar el sistema de ecuaciones lineales, se deben incorporar dos
condiciones de frontera, las cuales pueden ser:
     Dirichlet: se prescribe el valor de la temperatura
                                         T1 = Ta ,      TN = Tb
       Neumann: se prescribe el flujo (derivada)
                                         dT              dT
                                                ,
                                         dx x=a          dx x=b
    que se aproximan mediante diferencias finitas.
    Mixtas (Robin): combinación de temperatura y flujo, típicamente asociadas a
    convección.
Estas condiciones permiten obtener un sistema lineal cerrado para las
temperaturas nodales.
Universidad de Ingeniería y Tecnología               Métodos Numéricos        24 / 32
Ejercicio en Aula
La ecuación diferencial siguiente

                                         d 2T
                                              + c(Ta − T ) = 0
                                         dx 2
proviene de un balance de calor para una barra larga y delgada (véase la figura):




Universidad de Ingeniería y Tecnología               Métodos Numéricos        25 / 32
Continuación...
       T (x) (en o C) es la temperatura en x
       x (en m) es la distancia a lo largo de la barra
       c (em m−2 ) es el coeficiente de transferencia de calor entre la barra y el aire
       del ambiente
       Ta (en o C) es la temperatura del aire circundante
Cuando la segunda derivada se discretiza mediante:

                                         d 2T   Ti+1 − 2Ti + Ti−1
                                            2
                                              =
                                         dx            h2
donde la barra ha sido particionada en n pedazos dando lugar a los puntos: x0 , x1 ,
· · · , xn . Por otro lado Ti es la temperatura en el punto xi



Universidad de Ingeniería y Tecnología                 Métodos Numéricos            26 / 32
Continuación...
Al reemplazar en la E.D.O. obtenemos la ecuación en diferencias (discretización)

                    −Ti+1 + (2 + ch2 )Ti − Ti−1 = ch2 Ta        i = 1, 2, 3, · · · , n

Formulándose de esta manera (n − 1) ecuaciones lineales con (n − 1)incógnitas
T1 , T2 , · · · , Tn−1 .
Obs: T0 y Tn son conocidos
   1   Resuelva analíticamente la ecuación diferencial para una barra de 10 m             ,
       Ta = 20o C , T (0) = 40o C , T (10) = 200o C y c = 0.02m−2
   2   Considerando n = 5 en la discretización, plantee y resuelva un sistema de 4
       ecuaciones con 4 incógnitas que permita determinar las temperaturas en los
       pontos interiores de la barra T1 , T2 , T3 y T4 . Se sabe que T0 = 40 y T5 = 200



Universidad de Ingeniería y Tecnología             Métodos Numéricos                     27 / 32
                                             𝑑𝑥                                             120°C
                                                                                   Δ𝑥
Ejercicio 4 (EP 2024𝑇0 -=1)
                         𝑇1

Aplicación:
Se tiene una superficie expuesta (x = 0) de una pared plana con conductividad
térmica k constante el cual está sujeta a una radiación térmica que provoca una la
generación volumétrica de calor q.
                                         𝑇0 = 20°𝐶        𝑇1      𝑇2       𝑇3   𝑇4 = 50°𝐶


                                                     Δ𝑥
                                                      𝑑    𝑑𝑇
                                                         𝑘    +𝑞 =0
                                                      𝑑𝑥   𝑑𝑥

                                         𝑥           𝑑2 𝑇 𝑇𝑖−1 − 2𝑇𝑖 + 𝑇𝑖+1
                                                          =
                            𝐿                        𝑑𝑥 2       Δ𝑥 2


Universidad de Ingeniería y Tecnología                     Métodos Numéricos                28 / 32
Continuación...
Considerando que k = 0.5 W/m◦ C, q = 104 W/m3 , L = 10 cm, se pide realizar lo
siguiente:
   1   [3 ptos] Discretice la ecuación diferencial que gobierna la transferencia de
       calor en la pared plana y plantee el sistema de ecuaciones lineales. Para ello
       considere el orden de las ecuaciones como el orden de nodos: 1, 2 y 3.
       Escriba el sistema de ecuaciones en forma matricial en términos de q, L, k , T0
       y T4 .
   2   [4 ptos] Realice 2 iteraciones utilizando el método de Gauss-Seidel en forma
                                                                   T
       matricial. Considere como punto semilla T(0) = 40 40 40 . Halle el error
                                                        

       cometido en cada iteración. Nota: Use 4 cifras decimales.
   3   [3 ptos] Analice la convergencia del método iterativo de Gauss-Seidel
       mediante el criterio del radio espectral e indique claramente su conclusión
       (converge o diverge).


Universidad de Ingeniería y Tecnología        Métodos Numéricos                   29 / 32
Conclusiones
       En circuitos eléctricos, los métodos iterativos permiten resolver sistemas
       lineales provenientes de las leyes de Kirchhoff, eficientemente para circuitos
       complejos y matrices dispersas.
       En sistemas masa-resorte, los métodos iterativos facilitan calcular
       desplazamientos y fuerzas internas, abordando sistemas de ecuaciones
       derivados de balances de fuerzas.
       En discretización de ecuaciones diferenciales, los métodos iterativos resuelven
       sistemas lineales generados por aproximaciones de diferencias finitas,
       modelando fenómenos físicos como transferencia de calor.




Universidad de Ingeniería y Tecnología        Métodos Numéricos                   30 / 32
Bibliografía
      Steven C. Chapra and Raymond P. Canale
      Métodos numéricos para ingenieros, 7a ed.
      Richard L. Burden and J. Douglas Faires
      Análisis numérico, 7a ed.




Universidad de Ingeniería y Tecnología    Métodos Numéricos   31 / 32
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
