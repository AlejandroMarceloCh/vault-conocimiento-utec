---
curso: BD1
titulo: Clase 11 Normalizacion II
slides: 48
fuente: Clase 11 Normalizacion II.pdf
---

NORMALIZACIÓN (II)


CS2041- Base de Datos I
        Ciclo 2024 - 1




         Teófilo Chambilla - tchambilla@utec.edu.pe
            Brenner Ojeda - bojeda@utec.edu.pe
     CS2041 Base de Datos I
     Teófilo Chambilla Aquino




Índice

•   Formas normales
•   1NF
•   2NF
•   3NF
•   FNBC
•   Heurísticas
CS2041
BASES DE DATOS I
CICLO 2024-1




                                                                                Optimización y
Introducción                                                                    Procesamiento



Modelo Relacional     Algebra Relacional &        SQL
                                                              Formas Normales
                       Cálculo Relacional

 Entidad - Relación                          Actualización,
                                             Restricciones
FORMAS NORMALES

                  Capítulo 12 | Ramakrishnan / Gehrke
Hacia un buen diseño


   Nombre                         Tasa x                                   Rol
                   Departamento            DNI      Nombre    Apellido            M2       Avalúo
   Municipalidad                  m2                                       Lote


         A               I           2     111111   Claudio     Gonzalez     34    455       910

         A               I           2     111111   Claudio     Gonzalez     35    570      1140

         A               I           2     222222    Maria       Zapata      27    895      1790

         B              III         1.1    111111   Claudio     Gonzalez     10    150       165


         B              III         1.1    333333   Carlos     Fernandez     11    200       220


         B               X          1.1    444444    Elena       Abarca      13    150       165

         C               V          0.5    555555    Luisa       Muñoz       2     500       250

         D               V          3.5    111111   Claudio     Gonzalez     11    100       350

                        …           …        …        …            …         …         …     …

         G              III         4.5    111111   Claudio     Gonzalez     62    200       220
Dependencias funcionales

Esas “relaciones” de dependencia se llaman dependencias
funcionales:




                NombreMuni, Departamento➜ Tasa
                DNI➜Nombre, Apellido
                NombreMuni, Departamento, Rol ➜ DNI
                Tasa, m2 ➜ Avalúo



 ¿hay otras?

                Nombre                         Tasa x                             Rol
                                Departamento            DNI   Nombre   Apellido          M2   Avalúo
                Municipalidad                  m2                                 Lote
Dependencias funcionales

Pregunta capciosa Dadas las dependencias funcionales anteriores,
¿cuál son las llave de este esquema?




                  NombreMuni, Departamento➜ Tasa
                  DNI➜Nombre, Apellido
                  NombreMuni, Departamento, Rol ➜ DNI
                  Tasa, m2 ➜ Avalúo



¿cuál son las llave de este
                                     {NombreMuni, Departamento, Rol }
        esquema?
Idea de buen diseño
Cada “tema” en una tabla aparte:




      Nombre                         Tasa x                                   Rol
                      Departamento            DNI      Nombre    Apellido            M2       Avalúo
      Municipalidad                  m2                                       Lote


            A               I           2     111111   Claudio     Gonzalez     34    455       910

            A               I           2     111111   Claudio     Gonzalez     35    570      1140

            A               I           2     222222    Maria       Zapata      27    895      1790

            B              III         1.1    111111   Claudio     Gonzalez     10    150       165


            B              III         1.1    333333   Carlos     Fernandez     11    200       220


            B               X          1.1    444444    Elena       Abarca      13    150       165

            C               V          0.5    555555    Luisa       Muñoz       2     500       250

            D               V          3.5    111111   Claudio     Gonzalez     11    100       350

                           …           …        …        …            …         …         …     …

            G              III         4.5    111111   Claudio     Gonzalez     62    200       220
Idea de buen diseño                                                        Un modelo (casi) ideal

Cada “tema” en una tabla aparte:




                                           DNI      Nombre    Apellido



   Nombre                         Tasa x   111111   Claudio     Gonzalez       Rol
                   Departamento                                                       M2       Avalúo
   Municipalidad                  m2                                           Lote
                                           222222    Maria       Zapata

         A               I           2                                           34    455       910
                                           333333   Carlos     Fernandez
         B              III         1.1                                          35    570      1140
                                           444444    Elena       Abarca
         B               V          1.1                                          27    895      1790
                                           555555    Luisa       Muñoz
                                                                                 10    150       165
         B               X          1.1
                                             …        …            …

         C               V          0.5                                          11    200       220


         D               V          3.5                                          13    150       165

                        …           …                                            2     500       250

                                                                                 …         …     …
   Idea de buen diseño                                                           Un modelo (casi) ideal

     Cada “tema” en una tabla aparte:

                                                                                    Rol
                                                 DNI      Nombre    Apellido               M2       Avalúo
                                                                                    Lote



        Nombre                         Tasa x    111111   Claudio     Gonzalez        34    455       910
                        Departamento
        Municipalidad                  m2
                                                 222222    Maria       Zapata         35    570      1140
              A               I           2
                                                 333333   Carlos     Fernandez        27    895      1790
              B              III         1.1
                                                                                      10    150       165
                                                 444444    Elena       Abarca
              B              III         1.1
                                                 555555    Luisa       Muñoz          11    200       220

              B               X          1.1
                                                   …        …            …            13    150       165
              C               V          0.5
                                                                                      2     500       250
              D               V          3.5
                                                                                      11    100       350
                             …           …
                                                                                      …         …     …
                                       NombreMuni, Departamento➜ Tasa
                                       DNI➜Nombre, Apellido
                                       NombreMuni, Departamento, Rol ➜ DNI
Pero perdimos las
relaciones entre                       Tasa, m2 ➜ Avalúo
ellos
Normalización de las relaciones


         ● Normalización.
         El proceso de descomponer las relaciones
         "malas" insatisfactorias dividiendo sus
         atributos en relaciones más pequeñas


         ● Forma normal.
         Condición mediante el uso de claves y DF de
         una relación para certificar si un esquema de
         relación se encuentra en una forma normal
         particular.
Normalización de las relaciones

  1FN                  MALAS
  2FN
                       Dependencias funcionales
  3FN
  Boyce-Codd
  4FN                  Dependencias Multivaluadas
  5FN                  Dependencias de JOIN

                       BUENAS
Normalización de las relaciones
         ● 2NF, 3NF, BCNF.
         basadas en claves y DF de un esquema de
         relación.

         ● 4NF
         basado en claves, dependencias de múltiples
         valores: MVDs; 5NF basado en claves, unir
         dependencias

         Es posible que se necesiten propiedades
         adicionales para garantizar un buen diseño
         relacional (unión sin pérdida, conservación
         de la dependencia; Capítulo 11)
Normalización de las relaciones


          Un dominio es atómico si se considera que los
          elementos del dominio son unidades indivisibles.

          Un esquema relacional R está en primera 1NF si
          los dominios de todos los atributos de R son
          atómicos
Normalización de las relaciones

          No permite
          ● atributos compuestos
          ● atributos multivaluados
          ● relaciones anidadas; atributos cuyos valores
             para una tupla individual no son atómicos

          Considerado como parte de la definición de una
          relación.

          La mayoría de los RDBMS permiten que solo se
          definan las relaciones que están en Primera Forma
          Normal
Normalización de las relaciones
Normalización de las relaciones


     Matricula(dni, nombres, ApePat, ApeMat, cursos)




                                    ¿Algún problema aquí? …
Normalización de las relaciones

                                    ¿La solución? …
                        Crear otra tabla con Alumnos y Matrícula




           Alumnos(dni, nombres, ApePat, ApeMat)
           Matricula(dni, curso)
Todo bien




            ¿Pero si un cliente puede tener varios números de teléfono?
                                                                    …
UNF: Forma No Normalizada (UnNormalised Form)




                             UNF:
 Varias multiplicidades de valores en una columna de la tabla

1NF: Primera Forma Normal (First Normal Form)




                          1NF:
            Un valor en cada celda de la tabla
¿Todo bien con sola la 1NF?



                      ¿Algún problema aquí? …
 ¿Todo bien con sola la 1NF? No



                                        ¿Algún problema aquí? …
Soluciones con nulos                           Redundancia
  no cuentan aquí.
                             ¿Pero por qué es un problema? ¿Sólo espacio? …
                                        Anomalía de actualización:
                       Por ejemplo, se puede actualizar la dirección de Rankine en un
                                    lugar sin actualizar todos los valores
                                        Anomalía de inserción:
                           No podemos insertar un nuevo cliente a la tabla hasta
                                   tengamos un número de teléfono
                                          Anomalía de borrado:
                       Si el número de teléfono ahora está invalido, tendremos que
                                 borrar la fila entera con la dirección, etc.
¿Todo bien con sola la 1NF? No




                                ¿La solución? …
                         Crear otra tabla con rut y fono


                ¿Pero cómo podemos definir el problema aquí? …
                                                                 …
Modelo Relacional: Restricciones (Llaves)


Un conjunto de atributos de una relación
  forma una llave candidata
    si es una súper llave
      y no hay un subconjunto propio de esos atributos
      que es una súper llave
Modelo Relacional: Restricciones (Llaves)



           ¿Hay otra llave candidata?

                 Probablemente …


                 … o puede ser …

          (si no tenemos un tipo como Gengis Kan)
Modelo Relacional: Restricciones (Llaves)


Un atributo es primo
   si está en alguna llave candidata
Como obtener clave candidatas
desde las Dependencias funcionales

Una llave (súper o candidata)
  de una relación
    determina funcionalmente
      a todos los atributos
          de la relación
Como obtener clave candidatas
Heurística de solución
Sea la relación R y su conjunto de DFs F y
Sea S el conjunto de llaves candidatas:
1. Para cada atributo atómico Ai de R
    - Si {Ai}+ = R
       - Entonces Ai es una llave candidata S=S U Ai
2. Para cada par de atributos Ai ∉ S y Aj ∉ S
    - Si {AiAj}+ = R
       - Entonces S=S U {AiAj}
3. Continuar para tres atributos ...
Como obtener clave candidatas
Heurística de solución: Ejemplo
Sea la relación R(A, B, C, D, E) y
            F={BD→E,CD→AB,E→C,B→D}
 • {E}+ = {E,C}
 • {B}+ = {B,D,E,C,A}
 • {CD}+ = {C,D,A,B,E}
 • {AC}+ ={A,C}
 • {AD}+ ={A,D}
Descomposición
Definición
Sea la relación R y su conjunto de DFs F
  Una descomposición R1 y R2 sin pérdida:
   • Conservan los atributos de R
        – R = R1 U R2
   • Conservan las dependencias funcionales
        – F+ = {F1 U F2}+
   • No genera tuplas falsas, para ello:
        – {R1 ∩ R2} → R1 ó
        – {R1 ∩ R2} → R2
        * La intersección genera una DF válida en F
Descomposición
Ejemplo 1
Sea R(A,B,C,D,E) y F={AB→C, C→D, C→E}
La descomposición R1(A,B,C,D) y R2(C,E)
genera F1={AB→C, C→D} y F2={C→E}

   • Si conservan los atributos de R
   • Si conserva las dependencias funcionales
   • No genera tuplas falsas, ya que:
        – {R1 ∩ R2} → R2
        –        C → E ⊂ F+
Descomposición
Ejemplo 2
Sea R(A,B,C,D,E,F) y F= {AB→D, AC→E, ABD→F}
La descomposición R1(A,B,D,F) y R2(A,C,E)
genera F1={AB→D, ABD→F} y F2={AC→E}

   • Si conservan los atributos de R
   • Si conserva las dependencias funcionales
   • SI genera tuplas falsas, ya que:
        – {R1 ∩ R2} → R1: A → BDF ⊄ F+
        – {R1 ∩ R2} → R2: A → CE ⊄ F+
Recordando! Dependencias parciales
•   Dependencia parcial significa que un atributo no primo depende funcionalmente de parte
    de una clave candidata. (Un atributo no primo es un atributo que no forma parte de
    ninguna clave candidata).
      –
•   Por ejemplo, comencemos con R {ABCD} y las dependencias funcionales AB-> CD y A-> C.
      –
•   La única clave candidata para R es AB. C y D son atributos no primo. C depende
    funcionalmente de A. A es parte de una clave candidata. Eso es una dependencia parcial.
Normalización en 2FN
- Definición
  - Está en 1FN
  - Cada atributo no primo depende funcionalmente
    de manera total de toda clave de R
- Descomposición
  - Las DF parciales (no totales) se llevan a nuevas
    tablas.
  - En la tabla original queda la clave y los atributos
    que dependen totalmente de ella
Normalización en 2FN
Ejemplo
- Sea R(A,B,C,D,E) y F = {AB→ CE, B→D}
  - No está en 2FN
- Descomposición
  - DF Parcial AB→CE, entonces
    - R1(A,B,C,E)
    - R2(B,D)
       - (R1∩ R2 → R2) ⊂ F+
Normalización en 3FN
- Definición
   - Está en 2FN
   - Una tabla está en 3FN ssi para toda df no trivial X→Y en R:
      - X es superclave ó Y es atributo primo




- Descomposición
   - R(A,X,Y,B) donde X → Y incumple 3FN
   - Crear otra relación con X+, donde X es clave
   - Eliminar Y de R
Normalización en 3FN
Ejemplo
- Sea R(A,X,Y,B) y F = {A →XB, X→Y}.
   - No es 3FN, X no es superclave

- Tomando las F como base:
   - R1(A,X,B)
   - R2(X,Y)
      - (R1∩ R2 → R2) ⊂ F+

Normalización en 3FN
- Descomposición (usando F-)
  - Calcular F mínimo
  - Convertir cada dependencia en una relación
        (X → Y ⇒ Ri(XY))
  - Si no está la llave en una relación, agregarla
Normalización en 3FN
Ejemplo
- Sea R(A, B, C, D, E) y F = {A → B, A → C, C →
  D, B → E}.
   - F es mínimo
- {A}+ = {A,B,C,D,E} ⇒ A es clave única
- Tomando las cuatro DFs:
  - R1(A,B), preserva la clave
  - R2(A,C), preserva la clave
  - R3(C,D)
  - R4(B,E)
Normalización en FNBC
- Definición
     - Está en 3FN (... válido desde 1FN)
     - Para toda DF X→Y en R:
         - X es superclave


- Descomposición
     - R(A,X,Y,B) donde X → Y incumple FNBC
     - Crear dos relaciones
         - R1 = R - Y
         - R2(X,Y)


Esta estrategia de normalización no asegura preservar dependencias, pero sı
asegura la recuperación de la información por join.
Normalización en FNBC
Ejemplo
Sea R(A, B, C, D, E) y F = {A → BC, C → D, B → E}.

1- R no está en FNBC, C→D incumple FNBC
   Partimos: R1(A,B,C,E) y R2(C,D).
2- R1 no está en FNBC, B→E incumple FNBC
   Partimos: R3(A,B,C) y R4(B,E)

Resultado: R2(C,D), R3(A,B,C) y R4(B,E)
Ejercicio
R(A,B,C,D,E) y F{ A->B, A->D, C->E} Normalizar en 3FN y
FNBC
AC -> ABCDE , AC es una superllave.
No hay atributos primos y tampoco está en 3FN
A->B y A->D ⇒ A->BD
C->E viola FNBC Partimos R1(ABCD) y R2(CE)
A-BD viola FBNC Partimos R3(AC) y R4(ABD)
Resumen
1. Buen diseño evita anomalías
2. Las dependencias funcionales ayudan a un
buen diseño
3. Ideal es FNBC, pero no siempre se logra
4. Pero siempre se puede 3FN
Preguntas?
GRACIAS
TEÓFILO CHAMBILLA

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
