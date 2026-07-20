---
curso: IO2
titulo: EC4 Solución
slides: 6
fuente: EC4 Solución.pdf
---

8/6/26, 0:12                                                 EC4 Solución



     EC4 Solución
        library(markovchain)


      Package:         markovchain
      Version:         0.9.3
      Date:            2023-05-18 10:50:02 UTC
      BugReport: https://github.com/spedygiorgio/markovchain/issues


        library(igraph)



      Attaching package: 'igraph'

      The following objects are masked from 'package:stats':

               decompose, spectrum

      The following object is masked from 'package:base':

               union


     EC4 2026-1 A

     Una empresa de comestibles está realizando un análisis del comportamiento de los consumidores
     respecto a cuatro nuevos productos lanzados al mercado: (1) SugarFest, (2) Alphagas, (3) Bioflex y (4)
     Chocobombs. Tras un estudio riguroso, se determinó que si un cliente elige SugarFest en una compra,
     en la siguiente volverá a elegir este producto con una probabilidad de 0.4 o cambiará a Bioflex con una
     probabilidad de 0.6. Si elige Alphagas, volverá a seleccionarlo con una probabilidad de 0.2, optará por
     Bioflex con una probabilidad de 0.6 o por Chocobombs con una probabilidad de 0.2. Si elige Bioflex,
     en la siguiente compra escogerá Alphagas con una probabilidad de 0.8, Chocobombs con una
     probabilidad de 0.1 y volverá a elegir Bioflex con la probabilidad restante. Finalmente, si elige
     Chocobombs, volverá a comprarlo con una probabilidad de 0.5 o cambiará a Alphagas con una
     probabilidad de 0.5.


     Pregunta 1:
     Haga el gráfico de transición entre los estados y escriba la matriz de transición en un paso. Escriba los
     estados en el orden señalado en el enunciado

        mc1 <- new("markovchain",transitionMatrix = matrix(c(0.4,0,0.6,0,
                                                             0,0.2,0.6,0.2,
                                                                  0,0.8,0.1,0.1,
                                                                  0,0.5,0,0.5),nrow=4,byrow=T))
        mc1


      Unnamed Markov chain
       A 4 - dimensional discrete Markov Chain defined by the following states:
       1, 2, 3, 4

localhost:6949                                                                                                   1/6
8/6/26, 0:12                                                  EC4 Solución

       The transition matrix     (by rows)    is defined as follows:
          1   2   3   4
      1 0.4 0.0 0.6 0.0
      2 0.0 0.2 0.6 0.2
      3 0.0 0.8 0.1 0.1
      4 0.0 0.5 0.0 0.5


        plot(mc1,layout=layout_with_gem)




     Pregunta 2:
     Clasifique todos los estados: Determine si la CMTD es reducible, si hay estados absorbentes, identifique
     todas las clases y si son transitorias, recurrentes, periódicas o aperiódicas. Escriba los estados en el
     orden señalado en el enunciado.

        summary(mc1)


      Unnamed Markov chain     Markov chain that is composed by:
      Closed classes:
      2 3 4
      Recurrent classes:
      {2,3,4}
      Transient classes:
      {1}
      The Markov chain is not irreducible
      The absorbing states are: NONE
localhost:6949                                                                                                  2/6
8/6/26, 0:12                                                               EC4 Solución

     Todas las clases son aperiódicas, al ver los bucles se puede deducir fácilmente

        hittingProbabilities(mc1)


               1 2 3 4
      1 0.4 1 1 1
      2 0.0 1 1 1
      3 0.0 1 1 1
      4 0.0 1 1 1

           f 1 = 0.4
                               ∞                             ∞                       ∞                             ∞

                                         k                             k                       k                             k
           f 2 = 0.2 + 0.6 ∗ ∑ 0.1           ∗ 0.8 + 0.6 ∗ ∑ 0.1           ∗ 0.1 ∗ ∑ 0.5           ∗ 0.5 + 0.2 ∗ ∑ 0.5           ∗ 0.5

                               k=0                           k=0                     k=0                           k=0

                                     1                             1                       1                             1
           f 2 = 0.2 + 0.6 ∗                 ∗ 0.8 + 0.6 ∗                 ∗ 0.1 ∗                 ∗ 0.5 + 0.2 ∗                 ∗ 0.5
                               1 − 0.1                       1 − 0.1                 1 − 0.5                        1 − 0.5

           f2 = 1



     La CMTC es reducible y no hay estados absorbentes.


     Pregunta 3:
     Calcule la probabilidad de que en la cuarta compra un cliente escoja Chocobombs, dado que en la
     segunda compra escogío Alphagas. Para simplificar el cálculo, puede usar solo las filas y columnas
     necesarias para obtener el resultado solicitado.

     Nos solicitan:

                                                       P (X 4 = 4|X 2 = 2)



     Debemos usar las ecuaciones de Chapman-Kolmogorov para calcular la matriz de transición en dos
     pasos.

     Tenga en cuenta que no es necesario calcular toda la matriz, podemos optar por solo multiplicar las filas
     y columnas que nos dan el resultado solicitado.

        mc1^2


      Unnamed Markov chain^2
       A 4 - dimensional discrete Markov Chain defined by the following states:
       1, 2, 3, 4
       The transition matrix (by rows) is defined as follows:
           1    2    3    4
      1 0.16 0.48 0.30 0.06
      2 0.00 0.62 0.18 0.20
      3 0.00 0.29 0.49 0.22
      4 0.00 0.35 0.30 0.35


        (mc1^2)[2,4]


      [1] 0.2



localhost:6949                                                                                                                           3/6
8/6/26, 0:12                                                 EC4 Solución

     EC4 2026-1 B

     Una universidad está analizando las preferencias de sus estudiantes entre cuatro plataformas de
     aprendizaje virtual: (1) EduMaster, (2) LearnPro, (3) SkillNet y (4) CampusPlus. Tras recopilar datos
     durante varios semestres, se determinó que si un estudiante utiliza EduMaster en un periodo
     académico, en el siguiente continuará usándola con una probabilidad de 0.2, cambiará a LearnPro con
     una probabilidad de 0.1 o migrará a SkillNet con una probabilidad de 0.7. Si utiliza LearnPro, siempre
     permanecerá en esta plataforma. Si utiliza SkillNet, permanecerá en SkillNet con una probabilidad de
     0.3 o cambiará a CampusPlus con una probabilidad de 0.7 Finalmente, si utiliza CampusPlus,
     continuará utilizándola con una probabilidad de 0.6, o cambiará a SkillNet con una probabilidad de 0.4.


     Pregunta 1:
     Haga el gráfico de transición entre los estados y escriba la matriz de transición en un paso. Escriba los
     estados en el orden señalado en el enunciado

        mc2 <- new("markovchain",transitionMatrix = matrix(c(0.2,0.1,0.7,0,
                                                             0,1,0,0,
                                                                  0,0,0.3,0.7,
                                                                  0,0,0.4,0.6),nrow=4,byrow=T))
        mc2


      Unnamed Markov chain
       A 4 - dimensional discrete Markov Chain defined by the following states:
       1, 2, 3, 4
       The transition matrix (by rows) is defined as follows:
          1   2   3   4
      1 0.2 0.1 0.7 0.0
      2 0.0 1.0 0.0 0.0
      3 0.0 0.0 0.3 0.7
      4 0.0 0.0 0.4 0.6


        plot(mc2,layout=layout_with_gem)




localhost:6949                                                                                                   4/6
8/6/26, 0:12                                                  EC4 Solución




     Pregunta 2:
     Clasifique todos los estados: Determine si la CMTD es reducible, si hay estados absorbentes, identifique
     todas las clases y si son transitorias, recurrentes, periódicas o aperiódicas. Escriba los estados en el
     orden señalado en el enunciado.

        summary(mc2)


      Unnamed Markov chain     Markov chain that is composed by:
      Closed classes:
      2
      3 4
      Recurrent classes:
      {2},{3,4}
      Transient classes:
      {1}
      The Markov chain is not irreducible
      The absorbing states are: 2


     Todas las clases son aperiódicas, al ver los bucles se puede deducir fácilmente




localhost:6949                                                                                                  5/6
8/6/26, 0:12                                                 EC4 Solución
                                         f 1 = 0.2

                                         f2 = 1
                                                             ∞

                                                                       k
                                         f 3 = 0.3 + 0.7 ∗ ∑ 0.6           ∗ 0.4

                                                             k=0

                                                                   1
                                         f 3 = 0.3 + 0.7 ∗                 ∗ 0.4
                                                             1 − 0, 6

                                         f3 = 1



     La CMTC es reducible y el estado 2 es absorbente.


     Pregunta 3:
     Calcule la probabilidad de que al quinto semestre un alumno escoja SkillNet, dado que en el tercer
     semestre escogió EduMaster. Para simplificar el cálculo, puede usar solo las filas y columnas necesarias
     para obtener el resultado solicitado.

     Nos solicitan:

                                               P (X 5 = 3|X 3 = 1)



     Debemos usar las ecuaciones de Chapman-Kolmogorov para calcular la matriz de transición en dos
     pasos.

     Tenga en cuenta que no es necesario calcular toda la matriz, podemos optar por solo multiplicar las filas
     y columnas que nos dan el resultado solicitado.

        mc2^2


      Unnamed Markov chain^2
       A 4 - dimensional discrete Markov Chain defined by the following states:
       1, 2, 3, 4
       The transition matrix (by rows) is defined as follows:
           1    2    3    4
      1 0.04 0.12 0.35 0.49
      2 0.00 1.00 0.00 0.00
      3 0.00 0.00 0.37 0.63
      4 0.00 0.00 0.36 0.64


        (mc2^2)[1,3]


      [1] 0.35




localhost:6949                                                                                                   6/6
