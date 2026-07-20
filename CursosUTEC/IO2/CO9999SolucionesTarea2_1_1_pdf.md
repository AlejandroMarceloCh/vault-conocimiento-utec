---
curso: IO2
titulo: CO9999SolucionesTarea2-1-1
slides: 8
fuente: CO9999SolucionesTarea2-1-1.pdf
---

                                    1.     Ejercicio
   Supongamos que tenemos dos monedas no equilibradas. Es decir, la
pro-babilidad de cara en la moneda 1 es 0.7 y la probabilidad de cara
en la moneda 2 es 0.6. Seleccionamos hoy una moneda. Si ésta sale cara,
entonces mañana seleccionaremos la moneda 1. Si la moneda que selec-
cionamos hoy sale sello, entonces mañana seleccionaremos la moneda 2.
Si el primer dı́a se selecciona la moneda a lanzar de manera aleatoria,
¿Cuál es la probabilidad de que el tercer dı́a se seleccione la moneda 1?

  Solución:

  Sea S ≡ {1, 2} el espacio de estados con P(X0 = 1) = P(X0 = 2) = 21
  Sea Xn ≡ Moneda seleccionada el dia n para n ≥ 0.
  Nótese que {Xn , n ≥ 0} es una cadena de Markov con matriz de transición:
                                              7            3
                                                                 
                                        P =      10        10
                                                  6         4
                                                 10        10

  Queremos calcular

    P(X3 = 1) = P(X3 = 1|X0 = 1) P(X0 = 1) + P(X3 = 1|X0 = 2) P(X0 = 2)

                                           667             333
                                                                     
                                P3 =            1000
                                                666
                                                           1000
                                                            334
                                                1000       1000
                                                667                      666
   Por lo tanto tenemos que P(X3 = 1|X0 = 1) = 1000 y P(X3 = 1|X0 = 2) = 1000 ,
                            1333
lo implica que P(X3 = 1) = 2000 ≈ 0,6665.


                                    2.     Ejercicio
  En las siguientes matrices de transición encuentre las clases de la ca-
dena de Markov asociada y determine si dichas clases son recurrentes o
transitivas. Justifique su respuesta en cada caso.

  Solución:

P1 . El diagrama de estados de esta cadena de Markov es:
                                                     1/2




                                    1                1/2             2




                                          1/2              1/2

                              1/2

                                                                         1/2
                                                       3



   Esta cadena es irreducible ya que todos los estados se comunican, por lo que la
única clase es {1, 2, 3} y en consecuencia, todos los estados son recurrentes.
                                                 1
                                                                                                                         2


P2 . El diagrama de estados de esta cadena de Markov es:
                                                         1



                                        1                                      4               1




                                                                           1                       2


                                      1/2

                                                             3                           1/2




   Esta cadena es irreducible ya que todos los estados se comunican, por lo que la
única clase es {1, 2, 3, 4, 5} y en consecuencia todos los estados son recurrentes.



P3 . El diagrama de estados de esta cadena de Markov es:

                                                                     1/4
                                                                                                   1/2
                                       1/2
                                                   1                                 2                   1




                                                   1/2
                                                                                     1/4

                                                 1/2

                                                                           3

                                                 1/2                               1/2




                                1/2          5                   4

                                                                           1/2


                                                   1/2



   En esta cadena encontramos tres clases: {1, 3}, {2} y {4, 5}.
   Si fi es la probabilidad de que arrancando desde i, la cadena eventualmente
retorne a i tenemos que:

            1
     f2 =                                                                                  la clase {2} es transitoria
            2
            ∞  k
            X  1                  1
     f1 =                   =          −1=2−1=1                                      la clase {1, 3} es recurrente
            k=1
                   2            1 − 12
             ∞        k
            X      1
     f4 =                   =1                                                       la clase {4, 5} es recurrente
                   2
            k=1




P4 . El diagrama de estados de esta cadena de Markov es:
                                                                                   3



                                                      1/2
                                                                      1/2
                            1/4
                                          1                       2         1

                                                3/4




                                      1

                                                            5




                        1         3               4

                                                            2/3


                                          1/3


  En esta cadena encontramos cuatro clases: {1, 2}, {3}, {4} y {5}.
  La clase {3} es recurrente (de hecho el estado 3 es absorbente) ya que f3 = 1.
  La clase {4} es transitoria ya que f4 = 32 < 1.
  La clase {5} es transitoria ya que f5 = 0 < 1.
  La clase {1, 2} es recurrente ya que f1 = 1 (cuenta fastidiosa).

                                          3.    Ejercicio
   Una matrı́z de transición P se dice que es doblemente estocástica si
la suma de los elementos de sus columnas es igual a uno. Es decir,
                            X
(1)                            Pij = 1     ∀j.
                                      i

Si la cadena de Markov asociada a una matrı́z de transición doblemente
estocástica es irreducible, aperiódica y tiene un número finito de estados,
digamos M + 1 estados, 0, 1, · · · , M , mostrar que las probabilidades lı́mite
están dadas por
                               1
(2)                    πj =                j = 0, 1, · · · , M.
                             M +1

Prueba:

   Ya que la cadena de Markov es irreducible, finita y aperiódica, sabemos que las
                            n
probabilidades lı́mite {πj }j=0 son la solución única no negativa de:
                      (       PM
                        πj = i=0 πi Pij j = 0, 1, 2, . . . , M
(3)                     PM
                           j=0 πj = 1

  Veamos que πj = M1+1 ≥ 0 para j = 0, 1, 2, . . . , M satisface (??).
              PM        PM
  Claramente j=0 πj = j=0 M1+1 = M   M +1
                                       +1 = 1.
               PM             PM     1
                                                         PM
  Por otro lado j=0 πj Pij = j=0 M +1 Pij = M1+1 j=0 Pij = M1+1 = πj ya
   PM
que j=0 Pij = 1 al ser P doblemente estocástica.
                            M
   Como sabemos que {πj }j=0 es única entonces la probabilidad estacionaria de
estar en cada estado es M1+1 .
                                                                                    4


                                  4.   Ejercicio
  Sea Yn la suma de los resultados de lanzar un dado n veces de manera
independiente. Encuentre
(4)                       lı́m P [Yn sea múltiplo de 13].
                         n→∞


Solución:

  Nos interesa conocer lı́mn→∞ P(Yn es múltiplo de 13).
  Sea Xn = Yn mod 13. Se puede ver que Xn es una cadena de Markov.
  Ahora P(Yn es múltiplo de 13) = P(Xn = 0|X0 = 0) = (P n )00
  con donde P esta dada por:
                    0 61 61 16 16 16 16 0 0 0 0 0 0
                                                               
                  0 0 1 1 1 1 1 1 0 0 0 0 0
                            6 6   6  6   6    6
                  0 0 0 1 1 1 1 1 1 0 0 0 0
                                                               
                              6   6  6   6    6   6
                  0 0 0 0 1 1 1 1 1 1 0 0 0
                                                               
                                  6  6   6    6   6  6
                  0 0 0 0 0 1 1 1 1 1 1 0 0
                                                               
                                     6   6    6   6  6   6
                  0 0 0 0 0 0 1 1 1 1 1 1 0
                                                               
                                        6    6   6  6   6 6    
                                              1   1  1   1 1   1
             P =  01 0 0 0 0 0 0 6 61 61 16 61 61 
                   16 01 0 0 0 0 0 0 6 61 16 61 61 
                                                               
                   16 61 01 0 0 0 0 0 0 6 61 61 61 
                                                               
                   16 61 61 01 0 0 0 0 0 0 6 16 61 
                                                               
                   16 61 61 61 01 0 0 0 0 0 0 6 61 
                                                               
                  
                     6  6   6 6   6  0 0 0 0 0 0 0 6
                     1  1   1 1   1  1
                     6  6   6 6   6  6  0 0 0 0 0 0 0
  P es doblemente estocástica, irreducible, aperiódica y tiene 13 estados.
                                                                               1
  Gracias al ejercicio anterior tenemos que lı́mn→∞ P(Yn es múltiplo de 13) = 13

                                  5.   Ejercicio
   Considere 3 cajas, una roja, una blanca y una azul. La caja roja con-
tiene 1 bola roja y 4 azules; la caja blanca contiene 3 bolas blancas, 2
rojas y 2 azules; la caja azul contiene 4 bolas blancas, 3 rojas y 2 azules.
En el estado inicial, una bola es seleccionada de la caja roja y después
se regresa a la urna. En cada estado subsiguiente, se selecciona una bola
al azar de la caja del color de la última bola seleccionada e igualmente
se retorna a la caja de la cual fue seleccionada. A largo plazo, ¿cuál es
la proporción de bolas rojas seleccionadas? ¿cuál es la proporción de
blancas?, ¿cuál es la proporción de azules?
Solución:

  Sea S = {1, 2, 3} el espacio de estados, donde 1 representa bola roja, 2 representa
bola blanca y 3 representa bola azul. Sea Xn ≡ el color de la n-ésima bola seleccionada.
Es facil ver que {Xn , n ≥ 0} es una cadena de Markov con matriz de transición:
                                                4
                                       1        
                                       5    0   5
                                 P =  72   3
                                            7
                                                2
                                                7
                                        3   4   2
                                       9    9   9
                                                                                     5


  Queremos calcular π = [π1 , π2 , π3 ] la distribución de probabilidad lı́mite de la
cadena de Markov {Xn , n ≥ 0}.
  Sabemos que π satisface πP = π con π1 + π2 + π3 = 1.
                                        25
  Resolviendo encontramos que π1 = 89      , π2 = 28         36
                                                  89 y π3 = 89 .


                                     6.    Ejercicio
  Una pulga salta sobre los vértices de un triángulo de la siguiente
manera. Cuando está sobre el vértice i, se mueve en dirección horaria
con probabilidad pi y en dirección antihoraria con probabilidad qi = 1 − pi
para i = 1, 2, 3.

a. Encuentre la proporción del tiempo que la pulga pasa en cada vértice
del triángulo.
Solución:
El diagrama de estados de esta cadena de Markov es:
                                               q1




                                     1         p2        2




                                          p1        p3

                                q3

                                                             q2
                                                3



  Sea Xn el vértice donde se encuentra la pulga después de su n-ésimo salto. Se
puede ver que {Xn , n ≥ 0} es una cadena de Markov.
  La matriz de transición es
                                               
                                      0 q1 p1
                               P = p2 0 q2 
                                      q3 p3 0
y si 0 < pi < 1 ∀i ∈ {1, 2, 3}, la cadena de Markov es irreducible, positiva recu-
rrente y aperiódica.
   Para encontrar la proporción del tiempo que la pulga pasa en cada vértice,
debemos resolver el siguiente sistema de ecuaciones:
                               
                               
                                π2 p2 + π3 q3 = π1
                               
                               π q + π p = π
                                   1 1      3 3       2
                               
                               
                                π 1 p 1 + π 2 q2 = π 3
                                 π1 + π2 + π3 = 1
                               

  Resolviendo el sistema de ecuaciones encontramos:
                                         p3 (1 − p2 )
                   π1 =
                        p1 (1 − p3 ) + p2 (1 − p1 ) + p3 (1 − p2 ) − 3
                                       p1 (1 − p3 ) − 1
                   π2 =
                        p1 (1 − p3 ) + p2 (1 − p1 ) + p3 (1 − p2 ) − 3
                   π3 = 1 − π1 − π2
                                                                                      6


b. ¿Qué tan frecuentemente la pulga se mueve una vez en dirección
antihoraria seguida por 5 saltos en dirección horaria?
Solución:
Sea A el evento “La pulga salta en dirección anti-horaria y luego salta en dirección
horaria 5 veces”.
  Sea Vi ≡ “La pulga esta en el vértice i” = {Xn = i} para i ∈ {1, 2, 3}.
  Gracias a la formula de probabilidad total tenemos que

                      3
                      X
             P(A) =         P(A|Vi ) P(Vi )
                      i=1
                      3
                      X
                  =         P(A|Vi )πi
                      i=1
                  = q1 p2 p1 p3 p1 π1 + q2 p3 p2 p1 p3 p2 π2 + q3 p1 p3 p2 p1 p3 π3
                  = q1 p21 p22 p3 + q2 p1 p22 p23 π2 + q3 p21 p2 p23 π3



                                       7.     Ejercicio
a. Sea πi la proporción a largo plazo del tiempo que una cadena de Mar-
kov dada pasa en el i−ésimo estado.Explique porqué πi es la proporción
de transiciones que llegan del estado i y también es la proporción de
transiciones que salen del estado i.
Solución:
El número de trasiciones al estado i para tiempo n, el número de transiciones que
se originan desde el estado i para tiempo n, y el número de perı́odos que la cadena
pasa en el estado i, difieren a lo sumo por uno. Entonces las proporciones a largo
plazo deben coincidir.


b. ¿πi Pij representa la proporción de transiciones que satisfacen cuál
propiedad?
Solución:
πi Pij representa la proporción a largo plazo de transiciones que van desde el estado
i hasta el j.

     P
c. ¿ i πi Pij representa la proporción de transiciones que satisfacen cuál
propiedad?
Solución:
P
  i πi Pij es la proporción a largo plazo de transiciones que van al estado j.


                                                   P
d. Usando lo anterior, explique porqué πi = i πi Pij
Solución:
ComoPπj es también la proporción de transiciones que llegan al estado j, entonces
πj = i πi Pij .
                                                                                    7


                                    8.       Ejercicio
   Para la cadena de Markov con estados 1,2,3, y 4 y cuya matrı́z de
transición P viene dada por
                                             
                              0,4 0,2 0,1 0,3
                             0,1 0,5 0,2 0,2 
(5)                     P =                  
                             0,3 0,4 0,2 0,1 
                               0   0   0   1
Encuentre fi3 y si3 para i = 1, 2, 3.
Solución:
Ya que 4 es un estado absorbente y se puede visitar eventualmente, esta cadena de
Markov es reducible con dos clases {1, 2, 3} y {4}. La clase {1, 2, 3} es transitoria
(ya que 4 es un estado absorbente).
   Tenemos que:
                                              4   2      1
                                                 
                                             10   10     10
                                PT =  1     10
                                                  5
                                                  10
                                                         2 
                                                         10
                                              3   4      2
                                             10   10     10
                                     6              2        1
                                                               
                                     10           − 10     − 10
                                       1            5        2 
                           I − PT = − 10
                                   
                                                   10      − 10
                                       3             4          8
                                    − 10          − 10         10
                                                   64    40        18
                                                                      
                                              29          29        29
                          S ≡ (I − PT )−1 =  29
                                              28          90
                                                          29
                                                                    26 
                                                                    29
                                              38          60        56
                                              29          29        29
por lo que tenemos que:
                                       18
                                 S13 =    ≈ 0,6207
                                       29
                                       26
                                 S23 =    ≈ 0,8966
                                       29
                                       56
                                 S33 =    ≈ 1,9310
                                       29
y
                                  S13 − 0   18
                            f13 =         =    ≈ 0,3214
                                    S33     56
                                  S23 − 0   26
                            f23 =         =    ≈ 0,4643
                                    S33     56
                                  S33 − 1   27
                            f33 =         =    ≈ 0,4821
                                    S33     56

                                    9.       Ejercicio
    Para un proceso de ramificación, calcule π0 cuando

a. P0 = 1/4 y P2 = 3/4
Solución:
µ = 0 · 14 + 2 · 43 = 32 > 1
    entonces π0 = π00 + 34 π02 por lo que resolviendo en función de π0 obtenemos dos
raı́ces distintas, 1 y 13 , por lo que π0 = 13 .
                                                                                         8


b. P0 = 1/4 y P2 = 3/4
Solución:
µ = 0 · 14 + 1 · 21 + 2 · 14 = 12 + 21 = 1 por lo que π0 = 1.
c. P0 = 1/6, P1 = 1/2 y P3 = 1/3.
Solución:
µ = 0 · 16 + 1 · 21 + 3 · 13 = 12 + 1 = 23 > 1
   entonces π0 = 16 π00 + 12 π01 + 31 π03 , es decir, debemos encontrar las raı́ces de
                                      2π03 − 3π0 + 1.
Claramente 1 es una raı́z por lo que ahora podemos encontrar las raı́ces del polino-
mio cuadrático restante 2π02 + 2π0 − 1.          √           √
  El polinomio tiene dos raı́ces distintas, − 12 − 23 y − 12 + 23 . Seleccionaremos la
más pequeña positiva.         √
  Obtenemos que π0 = − 12 + 23 ≈ 0,3660
