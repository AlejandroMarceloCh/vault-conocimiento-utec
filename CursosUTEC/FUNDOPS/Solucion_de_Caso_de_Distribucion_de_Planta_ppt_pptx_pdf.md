---
curso: FUNDOPS
titulo: Solución de Caso de Distribución de Planta (ppt)__pptx
slides: 15
fuente: Solución de Caso de Distribución de Planta (ppt)__pptx.pdf
---

Solución de Caso de
Distribución de Planta



   Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
   Enunciado
                                                                               Of 1            Of 2          Of 3         Of 4
Ejercicio de Distribución de Planta
                                                                               Prof:           Prof:         Prof:        Prof:
El presidente de Dorton University pidió al departamento                       A               B             C            D
de métodos que asigne a ocho profesores de biología, a
los cuales se les asignó un código con las siguientes
                                                                              Of 5            Of 6           Of 7         Of 8
letras (A, B, C, D, E, F, G y H) en ocho oficinas
                                                                              Prof:           Prof:          Prof:        Prof:
(numerados del 1 al 8 en el diagrama) del nuevo edificio                      E               F              D            E
de biología según se muestra.

Inicialmente los profesores están ubicados en las oficinas
de la siguiente forma, A en la oficina 1, B en 2, C en 3, y
así sucesivamente                                                                      Of              Of            Of           Of
                                                                                       1               2             3            4
La distancia entre oficinas contiguos es de 10m, y la
distancia entre no contiguos es de 15,18, 25 y 34 m como
se muestra en la siguiente figura
                                                                                      Of               Of            Of           Of
                                                                                      5                6             7            8
                                     Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
 Enunciado
                                                                  Restricciones:
Flujo de Información entre Profesores.
                                                                   El costo promedio por metro de traslado de
Entre las oficinas existe flujos de documentos
                                                                    documentos es de $1.00
físicos de información por semana, en la siguiente
tabla se muestra las veces que se realizaron los                   Las oficinas 1, 4, 5 y 8 son los únicos con ventanas.
flujos de información ida y vuelta en una semana                   D y E, los subdirectores del departamento de
                                                                    biología, deben tener oficinas con ventanas.
              Flujo de                    Flujo de                 H debe estar del otro lado del patio justo enfrente
   Ruta     información     Ruta        información                 de D.
   A-B           20          C-B             20                    A, G y H deben estar en la misma ala (ala sur o ala
   A-C           30          C-H             30                     norte)
   A-E           50          D-E             40                    F no debe estar junto a D o G ni directamente
   A-H           70          E-F             10                     enfrente de G.
   B-A           10          F-G             10
   B-F           30          G-H             40
   B-H           20          G-E             20



                               Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
      Condiciones:
                                                                      Tabla de relaciones                      Tabla de flujo de información
        Tabla de importancia
                                       Rango (metros
clave         Prioridad        Valor
                                        recorridos)
        ABSOLUTAMENTE
 A                              4        2400-1100
        NECESARIO
        ESPECIALMENTE
 E                              3        1099-500
        IMPORTANTE
  I     IMPORTANTE              2         499-200

 O      ORDINARIA (NORMAL)      1         199 - 1

 U      SIN IMPORTANCIA         0            0
 X      NO DESSEABLE            -1            -




                                       Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
Requerimientos:
1. HACER EL ANÁLISIS DE FLUJO DE MATERIALES CON LA MATRIZ “DESDE-HASTA”,
CALCULAR EL COSTO DE LA DISTRIBUCIÓN ACTUAL

2. REALIZAR LA RELACIÓN ENTRE ACTIVIDADES, LA MATRIZ DE CERCANÍAS Y EL
DIAGRAMA DE RELACIONES.
• UTILICE LA TABLA DE IMPORTANCIAS Y LA TABLA DE RELACIONES.
• EN LA TABLA DE RELACIONES UTILICE DE RAZONES LAS CONDICIONES DADAS


3. REALIZAR EL DIAGRAMA RELACIONAL DE RECORRIDOS – ACTIVIDADES.
• UTILICE LA TABLA DE FLUJO DE IMFORMACIÓN




                    Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
1. HACER EL ANÁLISIS DE FLUJO DE MATERIALES CON LA MATRIZ “DESDE-HASTA”,
CALCULAR EL COSTO DE LA DISTRIBUCIÓN ACTUAL

 a) Se realiza una matriz “desde – hasta” para evaluar las distancias entre oficinas

 Para esto se usa la información donde se indica la distancia entre oficinas, por ejemplo, para la
 distancia entre la oficina del profesor A hasta la oficina del profesor B es 10, ya que son contiguas
                          1               1
                          0               0

   Of 1        Of 2           Of 3            Of 4                                    A     B      C    D    E    F    G    H
   Prof.       Prof.          Prof.           Prof.                            A      -     10     20   30   15   18   25   34
   A           B              C               D
                                                                               B             -     10   20   18   15   18   25
                                                                               C                    -   10   25   18   15   18
                                                                               D                         -   34   25   18   15
                                                                               E                              -   10   20   30
                                                                               F                                   -   10   20
                                                                               G                                        -   10
  Of 5          Of 6          Of 7            Of 8                             H                                             -
  Prof.         Prof.         Prof.           Prof.
  E             F             G               H



                               Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
    1. HACER EL ANÁLISIS DE FLUJO DE MATERIALES CON LA MATRIZ “DESDE-HASTA”,
    CALCULAR EL COSTO DE LA DISTRIBUCIÓN ACTUAL

b) Se realiza una matriz “desde – hasta” para evaluar la
cantidad de recorridos entre oficinas
Utilizamos la información de los flujos de
información, es decir la cantidad de veces recorridas
por semana
                Flujo de                     Flujo de
     Ruta     información     Ruta         información
      A-B          20          C-B              20
      A-C          30          C-H              30
                                                                                                        Suma de flujos de información
      A-E          50          D-E              40
      A-H          70          E-F              10
      B-A          10          F-G              10
      B-F          30          G-H              40
      B-H          20          G-E              20



                                     Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
     1. HACER EL ANÁLISIS DE FLUJO DE MATERIALES CON LA MATRIZ “DESDE-HASTA”,
     CALCULAR EL COSTO DE LA DISTRIBUCIÓN ACTUAL

c) Se realiza una matriz “desde – hasta” para evaluar la                                   Multiplicamos distancias entre oficinas por la cantidad
cantidad de metros recorridos                                                              de veces de recorridos de flujos de información, para
                                                                                                    obtener los metros totales recorridos
  matriz “desde – hasta” con las distancias entre oficinas

           A     B     C     D     E     F      G     H                                        A       B       C      D      E       F       G        H     total
    A      -     10    20    30    15    18     25   34                                A       -      300     600     0     750      0       0       2380   4030
    B             -    10    20    18    15     18   25
                                                                                       B       0       -      200     0      0      450      0       500    1150
    C                   -    10    25    18     15   18
    D                         -    34    25     18   15                                C       0       0       -      0      0       0       0       540    540
     E                              -    10     20   30                                D       0       0       0      -    1360      0       0        0     1360
     F                                    -     10   20
    G                                            -   10                                E       0       0       0      0       -     100     400       0     500
    H                                                  -                               F       0       0       0      0      0        -     100       0     100
matriz “desde – hasta” con la cantidad de recorridos entre oficinas
                                                                                       G       0       0       0      0      0       0       -       400    400
                                                                                       H       0       0       0      0      0       0       0        -      0
                                                                                                                                                            8080

                                                                               El costo promedio por metro de traslado de documentos es de $1.00
                                                                               Por lo tanto, el costo total es: $8080


                                              Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
2. REALIZAR LA RELACIÓN ENTRE ACTIVIDADES, LA MATRIZ DE CERCANÍAS Y EL
DIAGRAMA DE RELACIONES.

Utilizamos la información de la tabla de importancia, para saber que prioridad se asigna de acuerdo con los metros
recorridos

   Tabla de importancia                             Matriz de distancias recorridas                     Matriz de relación de actividades


                                                                                                             A   B   C   D   E   F G    H
                                                                                                         A   -   I   E   U   E   U U    A
                                                                                                         B       -   I   U   U   I U    E
                                                                                                         C           -   U   U   U U    E
                                                                                                         D               -   A   U U    U
                                                                                                         E                   -   O I    U
                                                                                                         F                       - O    U
                                                                                                         G                         -    I
                                                                                                         H                              -




                                Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
2. REALIZAR LA RELACIÓN ENTRE ACTIVIDADES, LA MATRIZ DE CERCANÍAS Y EL
DIAGRAMA DE RELACIONES.

Utilizamos la información de la matriz de relación entre actividades y la tabla de relaciones para armar el diagrama de
relaciones entre actividades. La asignación de valores de la tabla de relaciones es realizada de acuerdo con el
conocimiento del proceso o la situación analizada

 Matriz de relación de actividades              Tabla de relaciones                                          Diagrama de relación entre actividades

    A   B   C   D    E   F    G   H
A   -   I   E   U    E   U    U   A
B       -   I   U   U    I    U   E
C           -   U   U    U    U   E
D               -   A    U    U   U
E                    -   O    I   U
F                         -   O   U
G                             -      I
H                                    -




                                         Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
3. REALIZAR EL DIAGRAMA RELACIONAL DE RECORRIDOS – ACTIVIDADES.
UTILICE LA TABLA DE FLUJO DE INFORMACIÓN
                                                                                                    A      B    C    D       E    F      G   H    TOTAL
                                                                                              A      -     2    3    0       3    0      0   4     12
Para este análisis utilizamos la información de la matriz de
                                                                                              B            -    2    0       0    2      0   3     7
relación de actividades y la tabla de flujo de información, para                              C                 -    0       0    0      0   3     3
generar la matriz de asignación de valores por flujo de                                       D                      -       4    0      0   0     4
información                                                                                   E                              -    1      2   0     3
Matriz de relación de actividades          Tabla de flujo de información                      F                                   -      1   0     1
                                                                                              G                                          -   2     2
                                                                                              H                                               -    0
    A   B   C   D   E   F   G    H
                                                                                            TOTAL   0      2    5    0       7    3      3   12
A   -   I   E   U   E   U   U    A
B       -   I   U   U   I   U    E                                                             Se suman los valores de manera horizontal y vertical,
                                                                                               por ejemplo, en A= 12+0=12. Estos resultados son la
C           -   U   U   U   U    E                                                             importancia en unidades (profesores). Mayor valor ,
D               -   A   U   U    U                                                             mayor importancia.
E                   -   O   I    U
                                                                                                                PROFESORES       TOTAL
F                       -   O    U
                                                                                                                    A             12
G                            -   I
                                                                                                                    B             9
H                                   -                                                                               C             8
                                                                                                                    D             4
                                                                                                                    E             10
                                                                                                                    F             4
                                                                                                                    G             5
                                        Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta       H             12
3. REALIZAR EL DIAGRAMA RELACIONAL DE RECORRIDOS – ACTIVIDADES.
UTILICE LA TABLA DE FLUJO DE INFORMACIÓN
Para este análisis utilizamos la información de las tablas de
importancia analizadas anteriormente
        A   B      C       D   E        F     G      H    TOTAL
  A     -   2      3       0   3        0      0     4     12
  B         -      2       0   0        2      0     3     7
  C                -       0   0        0      0     3     3
  D                        -   4        0      0     0     4
  E                            -        1      2     0     3
  F                                     -      1     0     1
  G                                            -     2     2
  H                                                   -    0
TOTAL   0   2      5       0   7        3      3     12


                PROFESORES     TOTAL
                       A           12
                       B           9
                       C           8
                       D           4
                       E           10
                       F           4
                       G           5
                       H           12       Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
       3. REALIZAR EL DIAGRAMA RELACIONAL DE RECORRIDOS – ACTIVIDADES.
       UTILICE LA TABLA DE FLUJO DE INFORMACIÓN                                                                         Restricciones:
       Para este análisis utilizamos la información de las tablas de                                                       Las oficinas 1, 4, 5 y 8 son los únicos
       importancia analizadas anteriormente                                                                                 con ventanas.
                                                                                                                           D y E, los subdirectores del
                                                                                                                            departamento de biología, deben tener
                                                                                                                            oficinas con ventanas.
                                         TOTA
       A    B   C   D   E   F   G   H                                                                                   
                                           L                                                                                H debe estar del otro lado del patio
 A      -   2   3   0   3   0   0   4     12
                                                                                                                            justo enfrente de D.
 B          -   2   0   0   2   0   3     7                                                                                A, G y H deben estar en la misma ala
 C              -   0   0   0   0   3     3                                                                                 (ala sur o ala norte)
 D                  -   4   0   0   0     4                                                                                F no debe estar junto a D o G ni
 E                      -   1   2   0     3                                                                                 directamente enfrente de G.
 F                          -   1   0     1


                                                                                                                 1             2             3              4
 G                              -   2     2
 H                                  -     0
TOTA
       0    2   5   0   7   3   3   12

                                                                                                                        F             B              C             D
  L




                                                                                                                 5             6             7              8
                                                                                                                        E             G             A              H
                                                Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
3. REALIZAR EL DIAGRAMA RELACIONAL DE RECORRIDOS – ACTIVIDADES.
UTILICE LA TABLA DE FLUJO DE INFORMACIÓN

Con la nueva asignación de oficinas a cada profesor,
se realiza una nueva matriz desde - hasta de
distancias.                                                                             matriz desde - hasta de
                                                                                        distancias
                                                                                                A        B   C    D    E    F    G    H
                                                                                           A    0    18      15   18   20   25   10   10

                                                                                           B             0   10   20   18   10   15   25

                                                                                           C                 0    10   25   20   18   18

                                                                                           D                      0    34   30   25   15

                                                                                           E                           0    15   10   30

                                                                                           F                                0    18   34
                                                                                           G                                     0    20
                                                                                           H                                          0




                                 Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta
3. REALIZAR EL DIAGRAMA RELACIONAL DE RECORRIDOS – ACTIVIDADES.
UTILICE LA TABLA DE FLUJO DE INFORMACIÓN
Con la nueva matriz desde - hasta de distancias y la matriz de flujos de
información.
       matriz desde - hasta de distancias
         A    B    C    D    E    F      G     H
                                                                      Multiplicamos distancias entre oficinas por la cantidad de veces de recorridos
   A      0   18   15   18   20   25     10    10                         de flujos de información, para obtener los metros totales recorridos
   B          0    10   20   18   10     15    25                                A       B       C       D       E     F       G       H       total
   C               0    10   25   20     18    18                        A       -      540     450      0     1000    0       0       0       1990
   D                    0    34   30     25    15                        B       0       -      200      0       0    300      0      500      1000
                                                                         C       0       0       -       0       0     0       0      540       540
   E                         0    15     10    30
                                                                         D       0       0       0       -     1360    0       0       0       1360
   F                              0      18    34                        E       0       0       0       0       -    150     200      0        350
   G                                     0     20                        F       0       0       0       0       0     -      180      0        180
   H                                           0                         G       0       0       0       0       0     0       -      800       800
       matriz de flujos de información                                   H       0       0       0       0       0     0       0       -         0
                                                                                                                                               6220

                                                                      El costo promedio por metro de traslado de documentos es de $1.00
                                                                      Con la distribución inicial se obtuvo un costo de $8080, con esta
                                                                       nueva distribución se ha generado un ahorro de $1860


                                       Fundamentos de Operaciones / 2024-2 / Tarea de Distribución de planta

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
