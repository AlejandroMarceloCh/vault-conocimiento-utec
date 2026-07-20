---
curso: BD1
titulo: Clase 9 Depedencia Funcional y Formas Normales
slides: 85
fuente: Clase 9 Depedencia Funcional y Formas Normales.pdf
---

   DEPENDENCIA
FUNCIONAL Y FORMAS
    NORMALES

CS2041- Base de Datos I
        Ciclo 2024 - 1




         Teófilo Chambilla - tchambilla@utec.edu.pe
            Brenner Ojeda - bojeda@utec.edu.pe
CS2041- Base de datos I                                               Computer Science




   RESULTADOS DE APRENDIZAJE


    ❏      Podrá explicar los conceptos de normalización de tablas.
    ❏      Podrá determinar si un modelo de base de datos es
           correcto usando dependencias funcionales.
    ❏      Podrá aplicar las formas normales 1FN, 2FN, 3FN, FNBC
CS2041
BASE DE DATOS I
CICLO 2024-1




Introducción                                                  Formas Normales


                                                                      Optimización y
Modelo Relacional     Algebra Relacional &        SQL
                                                                      Procesamiento
                       Cálculo Relacional

 Entidad - Relación                          Actualización,
                                             Restricciones
Las preguntas de hoy




      ¿Y cómo se puede saber si es un buen diseño relacional o no?



                                                                     …
                  Directrices informales
   Directrices de diseño informales para los esquemas de relación


Antes de tratar la teoría formal, veremos cuatro medidas
informales de calidad para el diseño de un esquema de relación:

• La semántica de los atributos.
• La reducción de información redundante en las tuplas.
• La reducción de los valores NULL en las tuplas.
• Prohibición de la posibilidad de generar tuplas falsas.
                     Directrices informales (Semántica)

    Ejemplo:

          EMPLEADO                                      FK
          NombreE    Dni    FechaNac   Dirección   NumeroDpto
                                                                         LOCALIZACIONES_DPTO
                     PK                                                      FK
                                                                         NumeroDpto UbicaciónDpto
         DEPARTAMENTO                  FK
                                                                                       PK
         NombreDpto NumeroDpto DniDirector
                     PK


                                                                        TRABAJA_EN
         PROYECTO                                            FK         FK        FK

         NombreProyecto NumProyecto UbicaciónProyecto NumDptoProyecto   Dni NumProyecto Horas
                           PK
                                                                             PK


La facilidad con la que se pueda explicar el significado de los atributos de una
relación es una medida informal de lo bien que está diseñada esa relación.
 Directrices informales (tuplas falsas)




¿Ambas son correctas?
Directrices informales (tuplas falsas)
                          Considere la relación
                          r(ABC) y sus proyecciones
                          r1(AB) y r2(BC).




                            tuplas falsas




                          Observación
                          No todas las descomposiciones de una
                          tabla se pueden combinar utilizando la
                          combinación natural para reproducir el
                          mesa original
Directrices informales (tuplas falsas)
                            Considere las siguientes
                            dos relaciones r1 (ABC) y
                            r2 (BCD).




                       Calcular la unión natural r = r1⊗r2
                           Evalúe las proyecciones
                         r1 '= 𝜫ABC (r) y r2' = 𝜫BCD (r)



                            Observación
                            Las tablas r2 y r2' son iguales, sin
                            embargo, la tupla <2,2,6> r1 pero no
                            están presentes en r1'
DEPENDENCIAS FUNCIONALES

                           Capítulo 19 | Ramakrishnan / Gehrke
Conceptos básicos

- Las DF son un tipo particular de restricción.

- Permiten expresar hechos acerca de la realidad que
  se está modelando con la BD.
Dependencias funcionales

Dada una relación R
  y dos conjuntos de atributos X∈R, Y∈R
    X determina funcionalmente a Y
      si y sólo si
        dos tuplas que tiene el mismo valor de X
              deben por fuerza tener el mismo valor de Y


- X y Y pueden ser atributos compuestos
Dependencias funcionales

                  X→Y
Lectura:
  X determina funcionalmente a Y

  O también:

  Y depende funcionalmente de X
 - Esto no supone que Y→X en R.
        Ejemplo
• Consideremos la    A    B    C    D
  relación r y
  veamos qué DF se   a1   b1   c1   d1
  satisfacen.
                     a1   b2   c1   d2

                     a2   b2   c2   d2

                     a2   b3   c2   d3

                     a3   b3   c2   d4
A ➜ C se satisface.

  – Las dos tuplas con valor a1 en A tienen el
    mismo valor en C, c1.
  – Las dos tuplas con valor a2 en A tienen el
    mismo valor en C, c2.
  – No existen otros pares de tuplas distintos
    que tengan el mismo valor en A.
C ➜ A no se satisface.

  – Sean t1=(a2, b3, c2, d3) y t2=(a3 ,b3, c2, d4)
  – tienen el mismo valor en C, c2 y
  – distintos valores en A, a2 y a3,
    respectivamente.
  ➜ hemos encontrado un par de tuplas t1 y t2
   tales que t1 [C] = t2 [C] pero t1 [A] ≠ t2 [A].
• r satisface muchas otras DF.
• Por ejemplo:
• AB ➜ D
•A ➜A y
• las demás DF triviales

(una DF de la forma α ➜ β es trivial si
  β⊆α )
Dependencias funcionales: Ejemplo
Considerar la siguiente relación y sus DFs

    EMP_PROY

   DNI   NumProyecto   Horas    NombreE    NombreProyecto    UbicacionProyecto

  DF1

  DF2

  DF3




                          {DNI, NumProyecto} → {Horas}


                                {DNI} → {NombreE}

               {NumProyecto} → {NombreProyecto, UbicacionProyecto}
Dependencias funcionales: Ejemplo
● Una empresa de alquiler de vehículos desea implementar una
  base de datos con la información de su negocio. Se tienen
  vehículos identificados por su número de matrícula, y de los
  que se conoce su marca, color, modelo y año.
● También se tienen clientes identificados por su número de
  cédula de identidad, y de los que se conoce su nombre,
  dirección y teléfono. Un contrato de alquiler de vehículo está
  identificado por un número de contrato y se realiza en una
  fecha dada entre un cliente y un vehículo, registrándose el
  periodo de alquiler en días y el precio del servicio.
● Se considera que en una misma fecha no se puede alquilar más
  de una vez el mismo vehículo al mismo cliente en la misma
  fecha.
Dependencias funcionales: Ejemplo
● Una empresa de alquiler de vehículos desea implementar una
  base de datos con la información de su negocio. Se tienen
  vehículos identificados por su número de matrícula, y de los
  que se conoce su marca, color, modelo y año.
● También se tienen clientes identificados por su número de
  cédula de identidad, y de los que se conoce su nombre,
  dirección y teléfono. Un contrato de alquiler de vehículo está
  identificado por un número de contrato y se realiza en una
  fecha dada entre un cliente y un vehículo, registrándose el
  periodo de alquiler en días y el precio del servicio.
● Se considera que en una misma fecha no se puede alquilar más
  de una vez el mismo vehículo al mismo cliente en la misma
  fecha.

Dependencias funcionales: Ejemplo
● Entonces podemos obtener las siguientes DFs:


    matrícula → {marca, color, modelo, año}

    cédula → {nombre, dirección, teléfono}

    nroContrato → {fecha, cédula, matrícula, período, precio}

    {fecha, cédula, matrícula} → nroContrato
Dependencias funcionales:

• Una DF es una propiedad del esquema, no de la instancia.
   – Una DF no puede ser inferida automáticamente a partir de
      una instancia.
   – Una instancia por sí sola es insuficiente para determinar si
      una DF se cumple en una relación (a menos que la muestra
      sea representativa), pero sí puede mostrar que una DF no
      se cumple.
 Dependencias funcionales
 Inferencia, deducción

       Sea F el conjunto de DFs especificadas en un
                  esquema de relación R.


● Habitualmente se especifican las DFs que son
  semánticamente obvias.
● Sin embargo, es habitual que muchas otras DFs se
  encuentren en otras instancias de la relación y entre los
  conjuntos de atributos que pueden derivarse y satisfacer
  las dependencias de F.
● Entonces, decimos que esas otras dependencias pueden
  inferirse o deducirse de las DF de F.
 Dependencias funcionales
 Inferencia, deducción
● Ejemplo:
  ○ Si cada departamento tiene un director, de manera que
     NroDpto determina de forma única DniDirector:
     NroDpto → DniDirector.
  ○ y un director tiene un único número de teléfono
     TelDirector:
     DniDirector→TeléfonoDirector
● Entonces:
  ○ Ambas dependencias juntas suponen que
     NroDpto→TeléfonoDirector.
  ○ Esto es una DF inferida y no tiene que declararse
     explícitamente.
Dependencias funcionales

Clausura (F+)

   Es el conjunto de todas las dependencias que incluye F,
   junto con las dependencias que pueden inferirse de F.

   El cierre de F ( F+ ) es el conjunto de DF que F implica
   lógicamente.

   Dado F, podemos calcular F+ directamente de la definición
   formal de DF

Tener en cuenta que las DF en F+ deben cumplirse para todas las
instancias de la relación donde se cumpla F.
Dependencias funcionales:
Reglas de Inferencias
    ● RI1: Reflexiva: Si Y ⊆ X, entonces X → Y . Un conjunto de
         atributos siempre se determina a sí mismo (DF trivial).
    ● RI2: Aumento: {X → Y } |= XZ → YZ
    ● RI3: Transitiva: {X → Y , Y → Z} |= X → Z
    ● RI4: Descomposición o proyección: {X → YZ} |= X → Y .
    ● RI5: Unión o aditiva: {X → Y , X → Z} |= X → YZ
    ● RI6: Pseudotransitiva: {X → Y , WY → Z} |= WX → Z




Reglas de Armstrong: RI1 a RI3, son minimales. Las demás se pueden derivarse a partir de estas tres.
                     Ejempl
                     o
             Sea R = (A, B, C, G, H, I) y
       F = {A➜ B, A ➜ C, CG ➜ H, CG➜ I, B ➜ H}.

Algunos miembros de F+, serán:
                        A➜ H

-    Como A ➜ B y B ➜ H, aplicamos la regla de
    transitividad.

Es más fácil usar los Axiomas de Armstrong para
  demostrar A ➜ H de lo que fue deducir directamente
  de las definiciones como hicimos anteriormente.
                    Ejempl
                    o
              Sea    R = (A, B, C, G, H, I)   y
        F = {A➜ B, A ➜ C, CG ➜H, CG ➜ I, B ➜ H}.



                 CG ➜ HI

-Como    CG ➜ H y CG ➜I,
           La regla de unión implica que CG ➜ HI.
                      Ejempl
                      o
                  Sea R = (A, B, C, G, H, I)   y
     F = {A➜ B, A ➜ C, CG ➜ H, CG ➜ I, B ➜ H}.


                             AG ➜ I


Necesitamos varios pasos para demostrar AG ➜ I.
• Primero, observar que se cumple A ➜ C.
• Usando la regla de aumento, vemos que AG ➜ CG.
• Además, como tenemos que CG ➜ I,
      así por la regla de transitividad se cumple AG ➜ I.
Dependencias funcionales:
Reglas de Inferencias




               Demostración
Dependencias funcionales:
Clausura de X bajo F+

 Algoritmo para determinar X+ bajo F

        X+ := X                  Asigna todos los atributos de X

        repetir
           antiguaX+ := X+;
           para cada df Y→Z en F hacer
                si Y ⊆ X+ entonces             Agrega atributos a X   +



                    X+ := X+ U Z;
        hasta que (antiguaX+ = X+);                    No hay más
                                                        cambios en X+
Dependencias funcionales:
Clausura de X bajo F+ (Ejemplo)

 Sea la relación:
      R(A,B,C,D,E y F)                             X=A,B
                                                   X[0]=A,B
 Y F el conjunto de DFs:                           X[1] = A,B,C
                                                   X[2] = A,B,C,D
      F = {AB→C;                                   X[3] = A,B,C,D,E
           BC→AD;
                                                   {A,B} = A,B,C,D,E
           D→E;
           CF→B;}
 ¿Cual es la cerradura de {A,B} es decir {A,B}+?
...
Dependencias funcionales:
Clausura de X bajo F+ (Ejemplo)

 Sea la relación:
      EMP_PROY (NSS, NumProy, Horas, NomEmp, NomProy, LugarProy)
 Y F el conjunto de DFs:
      F = {NSS→NomEmp;
           NumProy→NomProy, LugarProy;
           NSS, NumProy→Horas}

 Aplicando el algoritmo se infiere las siguientes clausuras:
 ● {NSS}+ = {NSS, NomEmp}
 ● {NumProy}+ = {NumProy, NomProy, LugarProy}
 ● {NSS, NumProy}+ = {NSS, NumProy, NomEmp, NomProy, LugarProy,
     Horas}
Dependencias funcionales:
Equivalencia de conjuntos
Dos conjuntos de dfs E y F son equivalentes sii E+ = F+.

Entonces:
   ● Todas las DFs en E se pueden inferir de F y todas las de
   F se pueden inferir de E.
   ● E cubre a F y F cubre a E.

¿Cómo determinamos si F cubre a E?
Para cada X→Y ∈ E, calculamos X+ respecto a F y
verificamos que X+ incluya los atributos en Y.
Dependencias funcionales:
Equivalencia de conjuntos
Ejemplo:
● F = {AB→C, B→D, D→GC, CG→H}
● F1 = {D→H, B→C, AD→GH}

      ○ F1 cubre a F?
      ○ F cubre a F1?
      ○ F es equivalente a F1?
Dependencias funcionales:
Equivalencia de conjuntos
Ejemplo:
● F = {AB→C, B→D, D→GC, CG→H}
● F1 = {D→H, B→C, AD→GH}
● F2 = {B→D, D→G, D→C, CG→H}

      ○ ¿Qué pasa entre F2 y F?
      ○ ¿Qué pasa entre F1 y F2?
Dependencias funcionales:
Cobertura mínimo
Una cobertura mínima de un conjunto de DFs E es un
conjunto mínimo de DFs F que satisface lo siguiente:
 ● Toda dependencia en F tiene un solo atributo en su parte
   derecha.
 ● No podemos reemplazar ninguna dependencia X → A en F
   por una dependencia Y → A, donde Y es un subconjunto
   propio de X, y seguir siendo un conjunto de dependencias
   equivalente en F.
 ● No podemos quitar ninguna DF de F y seguir siendo un
   conjunto de dependencias equivalentes a F.




Un conjunto mínimo está en forma estándar o canónica y sin redundancia
Dependencias funcionales:
Cobertura mínimo
 Algoritmo para localizar cobertura mínima F para E
Dependencias funcionales:
Cobertura mínimo: Ejemplo

Modelo Relacional: Restricciones (Llaves)

• Una súper-llave identifica cada fila; p.ej.:




• Una llave candidata es una súper llave mínima; p.ej.:




• Se escogerá una de las llaves candidatas como llave primaria:
Modelo Relacional:
Restricciones (Dependencias funcionales)




         ¿Hay una dependencia funcional aquí?
Modelo Relacional:
Restricciones (Dependencias funcionales)




          ¿Es una dependencia funcional?
                      ¡No!
Modelo Relacional:
Restricciones (Dependencias funcionales)




      ¿Hay una dependencia funcional aquí
     usando la llave primaria (a la izquierda)?
Modelo Relacional:
Restricciones (Dependencias funcionales)

Una llave (súper o candidata)
  de una relación
    determina funcionalmente
      a todos los atributos
          de la relación
Modelo Relacional:
Restricciones (Dependencias funcionales)




      ¿Cómo podemos encontrar las llaves candidatas
          usando las dependencias funcionales?

                           Si la parte derecha contiene todos los atributos,
                                        la parte izquierda es …
                                          una súper llave.
        Además, si la parte izquierda es mínima en este respecto, es …
                           una llave candidata.
FORMAS NORMALES

                  Capítulo 19 | Ramakrishnan / Gehrke
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
CS2041 Base de datos I                                                   Computer Science




         Resumen
        ➔ Es importante conocer el contexto del negocio para determinar las
          Dependencias funcionales.
        ➔ Un buen diseño del modelo de base de datos evitará anomalías
        ➔ Otra manera de generar modelos de datos es usando
          dependencias funcionales
        ➔ Mediante las formas normales se puede terminar un buen diseño
          de la base de datos
GRACIAS
 Teóﬁlo Chambilla

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
