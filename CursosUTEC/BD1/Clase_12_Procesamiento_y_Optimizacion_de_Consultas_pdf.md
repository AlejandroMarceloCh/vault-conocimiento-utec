---
curso: BD1
titulo: Clase 12 Procesamiento y Optimización de Consultas
slides: 111
fuente: Clase 12 Procesamiento y Optimización de Consultas.pdf
---

 PROCESAMIENTO Y
 OPTIMIZACIÓN DE
    CONSULTAS

CS2041- Base de Datos I
        Ciclo 2024 - 1




          Teófilo Chambilla - tchambilla@utec.edu.pe
             Brenner Ojeda - bojeda@utec.edu.pe
     CS2041 Base de Datos I
     Teófilo Chambilla Aquino




Índice
• Memoria
• Procesamiento de consulta
• Optimización sintáctica
• Optimización física (costos,
  indexs)
• Optimización semántica
CS2041 BASE DE DATOS I
CICLO 2024-1




                                                                           Planificación y
Introducción                                                               Optimización de Consultas




Modelo Relacional     Algebra Relacional &       SQL
                                                         Formas Normales    Transacciones        NoSQL
                       Cálculo Relacional

 Entidad - Relación                          Actualización, Dependencias
                                             Restricciones funcionales
CS2041- Base de datos I                                                  Computer Science




   RESULTADOS DE APRENDIZAJE


    ❏      Podrá explicar Optimización sintáctica, físico y semántico.
    ❏      Utilizar algoritmos de optimización de consultas SQL,
           como Hash-Join, Nested-Loop, Merge-Join
    ❏      Podrá explicar y utilizar correctamente los índices Hash y
           Árboles B+
CS2041- Base de datos I                       Computer Science




   Motivación




                                ER

                          Modelo Relacional




                               SQL
CS2041- Base de datos I                                                         Computer Science


  Las preguntas de hoy




                          ¿Cómo se deberían guardar las tablas en memoria?

                Y ¿cómo se pueden optimizar las consultas sobre estas tablas?

                                                                                          …
CS2041- Base de datos I




                    1     Memoria




                                    Capítulo 9.1 | Ramakrishnan / Gehrke
Acceso a memoria
Secuencial
        Memoria:   1   2   3   4   5   6   …




Aleatorio
        Memoria:   1   2   3   4   5   6   …
Costos de acceder a los datos (estimaciones)

                                    ¡El Disco Duro es muy lento!
                            En particular para acceso aleatorio (latencia)




                                                            (transmisión)
 30 GB/s     600 MB/s            100 MB/s



                Disco de
Memoria
                 Estado                 Disco Duro
Principal
                 Sólido
50–150 ns       10–100 μs                  5–15 ms
                                                               (latencia)
Costos de acceder a los datos (estimaciones)
                   ¿Por qué usamos el disco duro entonces?




            Más rápida ✔
Memoria                      ✔ Más barato     Disco Duro
Principal                    ✔ Persistente
                             ✔ Capacidad
Alta latencia de los discos duros

               ¿Por qué la latencia de discos duros es tan alta?




   Tiene un brazo mecánico que tiene que moverse para cambiar el bloque
Bloques en el disco duro




     Más eficiente al nivel de hardware.
          Evite espacio no usable.
CS2041- Base de datos I




                    2     Procesamiento de
                          consultas
SQL es un lenguaje declarativo

Uno dice lo que quiere, no cómo debería ser computado

   – Idealmente, el motor puede elegir el mejor plan de
       ejecución independientemente de su expresión
                         particular
     • Pero, esto es caro, entonces en la práctica, hay diferencias
 – Regresaremos al tema de rendimiento y optimización
                más adelante en el curso
 – Pero en general, se puede expresar una consulta en la
     forma “más natural” y dejar la ejecución al motor
SQL es un lenguaje declarativo


 ❏ Uno dice lo que quiere, no cómo debería ser
   computado
 ❏ Idealmente, el motor puede elegir el mejor
   plan de ejecución independientemente de la
   expresión particular de la consulta
 ❏ El usuario no tiene que preocuparse por la
   optimización de la consulta
Procesamiento de consultas
Procesamiento y optimización de consultas

                  Consulta (SQL)
                                                        Compilador
           Análisis léxico y sintáctico Validación
                                                         Árbol o grafo
                                                         de consulta
                    Forma intermedia
                                                           Verifica Índices

                        Optimizador


                     Plan de ejecución


                   Generador de Código                  Modo compilado
                                                        o interpretado

                                       Código
                                                           Tipo de ejecución

                    Procesador de BD
                                                             Si hay error, el mensaje
                                            Resultado        correspondiente
¿Cómo evaluar una consulta SQL ?
❏   Análisis sintáctico:¿está bien escrita?
❏   Análisis semántico:¿qué sentido tiene?
❏   ¿qué     posibilidades     tenemos        para
    ejecutarla?
❏   ¿Cuál es la posibilidad más conveniente
    (más rápida, más “barata”, etc?
❏   Tomar la decisión.
CS2041- Base de datos I




                    3     Optimización
                          Sintáctica
Traducción de SQL al álgebra relacional
            Bloque de
            consulta 1

                         SELECT APELLIDO, NOMBRE                                 Bloque de
                                                                                 consulta 2
                         FROM EMPLEADO WHERE

                         SALARIO         > ( SELECT MAX(SALARIO) FROM
                                              EMPLEADO WHERE NUMD=5);

                                         Traducción al álgebra



      πAPELLIDO, NOMBRE(σSALARIO >C(EMPLEADO))

       Elegir plan de consulta

                                                 FMAX(SALARIO)(σNUMD=5(EMPLEADO))
            Se evalúa sólo una vez. El
            resultado se trata como                    Elegir plan de consulta
            una constante (>C)

  Plan de Ejecución
  Consulta en SQL                                       Plan de Ejecución
  SELECT C.Comprador
  FROM Producto P, Compra C, Persona Q                           π comprador
  WHERE P.categoria = ‘telefono’ AND
        C.comprador = Q.nombre AND                           σcategoria=’telefono’
        C.prod = P.nombre;

                                                           |x|comprador =nombre(Hash Join)
Plan: Árbol de operadores de álgebra
relacional con la elección de algoritmos         |x|prod =
por cada operador.                                                              Persona
                                                 pnombre         (B+ Tree)

                                               Compra               Producto




    Lo ideal es conseguir el mejor plan. En la práctica se evitan los peores.
Optimización sintáctica: Heurística
     ❏   Objetivo: reducir el tamaño de las tablas intermedias
     ❏   Optimizador:
         ○   Reglas heurísticas: modifican la representación interna de la
             consulta
         ○   Después se genera un plan de ejecución:
              ■   Para ejecutar grupos de operaciones
              ■   Según los caminos de acceso que tengan los ficheros

     ❏   Regla principal:

         ○   Primero ejecutar seleccionar (σ) y proyectar (π)

         ○   Al final ejecutar reunir (|×|, *) y otras operaciones binarias
Árbol de consulta
   SELECT P.NÚMEROP, P.NÚMD, E.APELLIDO,
          E.DIRECCIÓN, E.FECHA_NCTO
   FROM PROYECTO AS P, DEPARTAMENTO AS D,
          EMPLEADO AS E
   WHERE P.NÚMD=D.NÚMEROD
         AND D.NSS_JEFE=E.NSS
         AND P.LOCALIZACIÓN=‘Stafford’
                                                       π P.NÚMEROP, P.NÚMD, E.APELLIDO,
                                                       E.DIRECCIÓN, E.FECHA_NCTO




                                                       |×| D.NSS_JEFE=E.NSS




                                  Orden de ejecución
                                                                          E
                                                       |×| P.NÚMD=DNÚMEROD

                                                                          D
                                                       σP.LOCALIZACIÓNP=‘Stafford’
                                                            P
Árbol de consulta inicial o canónico
                                                   ●   Lo genera el analizador sintáctico de
SELECT P.NÚMEROP, P.NÚMD, E.APELLIDO,                  manera estándar
       E.DIRECCIÓN, E.FECHA_NCTO                   ●   Sin optimizar
FROM PROYECTO AS P, DEPARTAMENTO AS D,             ●   Primero los ×, luego condiciones de σ
       EMPLEADO AS E                                   y |×|. Por último π.
WHERE P.NÚMD=D.NÚMEROD                             ●   Muy ineficiente (debido a los ×)
      AND D.NSS_JEFE=E.NSS
      AND P.LOCALIZACIÓN=‘Stafford’
                                         π P.NÚMEROP, P.NÚMD, E.APELLIDO,
                                         E.DIRECCIÓN, E.FECHA_NCTO


                                         σD.NSS_JEFE=E.NSS Y
                                         P.NÚMD=DNÚMEROD Y
                                         P.LOCALIZACIÓNP=‘Stafford’


                                                       ×
                                                                      E
                                                       ×
                                               P                 D
Optimización con árboles: ejemplo
                                                         ●   Transformar el árbol en uno de
SELECT APELLIDO                                              ejecución eficiente
FROM EMPLEADO, TRABAJA_EN, PROYECTO                      ●   Basada en reglas de equivalencia (r.e.)
                                                             entre expresiones del álgebra
WHERE NOMBREP=‘Acuario’                                      relacional
  AND NÚMEROP=NÚMP AND NSSE=NSS                          ●   Reglas heurísticas: guían la aplicación
  AND FECHA_NCTO>‘31-DIC-1957’                               de las r.e



 Apellido de los empleados que
 trabajan en el proyecto Acuario                       π APELLIDO
 nacidos después de 1957
                                                σNOMBREP=‘Acuario’ Y NÚMEROP=NÚMP Y
                ×
           Los crean un fichero muy
                                                NSSE=NSS Y FECHA_NCTO>’31-DIC-1957’
           grande Sólo se necesita usar la
           tupla del proyecto Acuario. Sólo
           reunir los empleados nacidos                       ×
           después de 1957.
                                                                           Proyecto
                                                              ×
         Mejor primero los   σ                Empleado                  Trabaja_En
Optimización con árboles: ejemplo(2)
                                         1                                               2
   π APELLIDO                                         π APELLIDO

   σNOMBREP=‘Acuario’ Y NÚMEROP=NÚMP Y            σ NÚMEROP=NÚMP
   NSSE=NSS Y FECHA_NCTO>’31-DIC-1957’                     ×
                ×                                 σ NSSE=NSS       σNOMBREP=‘Acuario’
                             Proyecto
                ×                                      ×                      Proyecto
 Empleado                 Trabaja_En
                                             σFECHA_NCTO>’31-DIC-1957’ Trabaja_En

                                                Empleado




  Mejor primero los   σ
                                                                     ×
                                              Mejor que el primer sea con el
                                              proyecto Acuario que sólo obtiene una
                                              tupla (NOMBREP es clave)
 Optimización con árboles: ejemplo(3)
         π APELLIDO
                                             2         π APELLIDO                            3



     σ NÚMEROP=NÚMP                                       σ NSSE=NSS
              ×                                                  ×

     σ NSSE=NSS       σNOMBREP=‘Acuario’              σ NNÚMEROP=NÚMP
                                                      σFECHA_NCTO>’31-DIC-1957’
          ×                       Proyecto                                        Empleado
                                                          ×
σFECHA_NCTO>’31-DIC-1957’ Trabaja_En                                      Trabaja_En

                                                 σNOMBREP=‘Acuario’
   Empleado

                                                    Proyecto




           Mejor primero ×  con
           proyecto Acuario                       Mejor   |×| que × más σ
    Optimización con árboles: ejemplo(4)
      π APELLIDO                            3
                                                      π APELLIDO                            4


         σ NSSE=NSS                                      |×| NSSE=NSS
                ×
     σ NNÚMEROP=NÚMP                                 |×| NNÚMEROP=NÚMP
     σFECHA_NCTO>’31-DIC-1957’                       σFECHA_NCTO>’31-DIC-1957’
                                 Empleado
         ×                                                                       Empleado
                         Trabaja_En                                      Trabaja_En

σNOMBREP=‘Acuario’                              σNOMBREP=‘Acuario’

   Proyecto                                        Proyecto




   Mejor   |×| que × más σ                               Hay otras formas más . . .
Reglas de transformación
1.   Descomponer σ C si C tiene ANDs en varias σ en cascada
         σc1 AND c2... AND cn(R) ≡ σc1 (σc2 (...(σcn (R)...)

2.   Mover las σC lo más abajo posible (lo que admitan los atributos de C). Esto es
     posible ya que σ es conmutativa con otras operaciones.

3.   Recolocar las hojas para que los σ más restrictivos se ejecuten antes (que
     producen una relación con menos tuplas). Esto es válido para los operadores
     conmutativos y asociativos: x, |x|, ∪ y ∩.

4.   Combinar × y σ en |×|

5.   Por cada πlista descomponer lista y mover los πsublista obtenidos lo más abajo
     posible. Crear nuevas π si es necesario.

6.   Identificar grupos de operaciones que se puedan ejecutar con un solo algoritmo
     (es decir, con un solo recorrido a los ficheros implicados).
     Ejemplo
  A partir de la siguiente consulta SQL el optimizador llega, en un paso intermedio,
  al árbol de consulta que figura a continuación. Obtén un árbol optimizado posible

SELECT Artículo.NomArt
                                                                    π    Artículo.NomArt
FROM Ingrediente, Art_Ingr, Artículo
WHERE Ingrediente.NomIngr = Art_Ingr.NomIngr
                                                             σ   Art_Ingr.NomArt = Artículo.NomArt
AND Art_Ingr.NomArt = Artículo.NomArt
AND Ingrediente.Precio > 1000
AND NomArt=”Pizza Marinera”
                                                                        x

                                        σIngrediente.NomIngr = Art_Ingr.NomIngr σ     NomArt=”Pizza Marinera”




                                                                                                            Orden de ejecución
                                                        x
                                                                                           Articulo
                                  σPrecio > 1000
                                                               Art_Ingr
                                   Ingrediente
¿Es suficiente la
transformación?
¿Cuál es el costo del plan estimado?
Recordar
 Plan: Árbol de operadores de álgebra relación con la elección de
 algoritmos por cada operador.




                  Entonces lo que faltaria para convertir un árbol en
                  plan de ejecución:

                   ● Algoritmos básicos por cada operador.
                      ○ Hay uno o varios por cada operación del
                         álgebra.
                   ● Algunos algoritmos exigen una organización de
                     datos determinada.
                      ○ Por ejemplo que haya índice primario.
OPTIMIZACIÓN FÍSICA
CS2041- Base de datos I




                    4     Optimización Física
SISTEMA DE COSTOS
Componentes del coste

 ● Bloques transferidos: depende de las estructuras de
   acceso y de la colocación de los bloques (contiguos,
   mismo cilindro, dispersos)
 ● Ficheros intermedios generados
 ● Cómputos en memoria sobre los ficheros intermedios:
   búsqueda, ordenación, fusión, cálculos
 ● Comunicación: envío de la consulta y recepción del
   resultado
                                                Generalmente se usa
                                                este

             Coste principal:
             – BD grandes: bloques transferidos
             – BD pequeñas (entran en memoria): cómputos
             – BD distribuidas: comunicación
Memoria Principal vs. Memoria Secundaria


                      • Datos guardados en memoria secundaria
          Memoria     • La lectura se hace por bloques
         Secundaria   • Un bloque tiene un tamaño de B tuplas




                      • Los datos son llevados a memoria principal
         Memoria      • La memoria tiene una capacidad de M tuplas
         Principal
Sistema de Costos


                              • Datos guardados en memoria secundaria
            Memoria           • La lectura se hace por bloques
           Secundaria         • Un bloque tiene un tamaño de B tuplas


                                Sistema de Costos:
                      Cuenta los accesos a la memoria secundaria.
                    Cada vez que se lee o escribe, se suma 1 al costo.
     Asume que las operaciones en memoria principal toman un tiempo despreciable.

                              • Los datos son llevados a memoria principal
            Memoria           • La memoria tiene una capacidad de M tuplas
            Principal
Transferencia de bloques y tuplas a RAM
                                   • Un bloque tiene un tamaño de B tuplas
Sistema de Costos                  • La memoria tiene una capacidad de M tuplas




    ¿Cuánto cuesta leer n tuplas desde la memoria secundaria?



              ¿Cuántos bloques caben en memoria?



                       ¿Cuántos bloques usa una relación R?

BÚSQUEDA
Búsqueda
• Devolver todas las tuplas de una relación que
  satisfagan alguna condición
Búsqueda Secuencial
• Se leen todas las tuplas de la relación R
• Se seleccionan las que cumplan la condición




                ¿Cuántas tuplas se leen?


         ¿Cuánto cuesta en términos de bloques?

             ¿Cómo podemos optimizar la búsqueda?
                                                    …
ÍNDICES

          Capítulo 9.3 | Ramakrishnan / Gehrke
Búsqueda de registro sin indice
      Desordenado                 Ordenado

 9                         Nombre            FNac   Salario   depart

 5                         Aron, Bid

                           Aboot, Men
 13

 8
                           Acosta


 6
                           Alfred, Bid
 15
                           Alvez, Men
 3

 17
                           Arce

 21                        Avilez, Bid
 11
                           Avaro, Men
 16

 2
                           Azen
                    O(n)
                                                                       O(log (n))
Indice Primario
Índice Agrupado
Índice Secundario
(unique)
Índice Secundario
(campo no clave)
Índice
• Estructura los datos para facilitar búsquedas
Índice Hash
          Función
 Llaves              Cajones                   Datos
           Hash




                    La llave puede ser cualquier conjunto de
                              atributos de la tabla.
Ejemplo función hash
Índice Hash
                 Función
 Llaves                                Cajones                   Datos
                  Hash
                 ¿El costo de búsqueda con un índice hash?

   Caso ideal:                    para devolver una tupla
   Peor caso:



          Asumiremos una búsqueda que devuelva una sola tupla.
           Para devolver k tuplas, hay que “sumar”  al costo.

   Caso ideal:                    para devolver k tuplas
Índice Hash
                 Función
 Llaves                                 Cajones                     Datos
                  Hash
                 ¿El costo de búsqueda con un índice hash?

   Caso ideal:                     para devolver una tupla
   Peor caso:



                        Pero ¿qué tipo de búsqueda?

          ¡Hemos asumido que se sabe el valor exacto de la llave!
Índice Hash
                 Función
 Llaves                                Cajones                    Datos
                  Hash
                 ¿El costo de búsqueda con un índice hash?

   Caso ideal:                    para devolver una tupla
   Peor caso:


                  ¿Qué pasa con las búsquedas por rango?



                                      Buscar n valores (ideal):
                                      Leer todo:
 Índice Árbol B

                                         186
                                         •     •



                  53         134                          440
                  •      •     •                         •       •




44           76                    152                   288              730



                      Árbol B: Árbol ordenado, balanceado

     a–b Árbol B: Los nodos internos tienen entre a y b hijos (a ≥                 )

                                                   ¿Este caso?       2–3 Árbol B
Índice Árbol B+

                                 186
                                 •     •



                 53       134                    440
                •     •     •                   •      •




   Árbol B+: Árbol B donde se guardan las tuplas en las hojas del árbol.
              Las hojas guardan todas las llaves y sus valores.
     Se conectan las hojas para poder hacer búsquedas por rango más
                                 eficientes.
Índice Árbol B+

                                     186 con un árbol B+?
                    ¿El costo de búsqueda
                                    •    •
                                                                Depende …

                 53        134                      440
                •      •     •                      •       •




   Árbol B+: Árbol B donde se guardan las tuplas en las hojas del árbol.
              Las hojas guardan todas las llaves y sus valores.
     Se conectan las hojas para poder hacer búsquedas por rango más
                                 eficientes.
Índice Árbol B+

                                 186
                                 •     •



                53       134                      440
               •     •     •                     •      •




     ¿El costo en términos de bloques leídos de memoria secundaria?

   Si se guarda cada nodo como un bloque en memoria secundaria:
                              para devolver una tupla
Índice Árbol B+

                                  186
                                  •     •



                 53       134                      440
                •     •     •                     •      •




      ¿El costo en términos de bloques leídos de memoria secundaria?


   Si se cachean la raíz y los nodos internos en memoria principal:
                             para devolver una tupla

Índices: Hash vs. Árbol B+

                                        Levemente más eficiente para
                                        búsquedas exactas asumiendo una
                                        función de hash ideal




                           Arból B+ es más popular



Mucho más eficiente para
búsquedas por rango
Crear Índices: SQL
• Por defecto, se crea un índice para la llave
  primaria de la tabla

• Para crear/borrar índices sobre otros
  atributos:
  .
JOINS
Reunir tablas: (EQUI) JOIN




   ¿Cómo deberíamos ejecutar el join?
Loop anidado (sin índices)




     4   2   2   6   3   1   …




     5   3   2   4   7   4   …
Loop anidado (sin índices)




     4   2   2   6   3   1   …




     5   3   2   4   7   4   …
Loop anidado (sin índices)




     4   2   2   6   3   1   …




     5   3   2   4   7   4   …
Loop anidado (sin índices)




     4   2   2   6   3   1   …   4   4




     5   3   2   4   7   4   …
Loop anidado (sin índices)




     4   2   2   6   3   1   …   4   4




     5   3   2   4   7   4   …
Loop anidado (sin índices)




     4   2   2   6   3   1   …   4   4

                                 4   4


     5   3   2   4   7   4   …
Loop anidado (sin índices)




     4   2   2   6   3   1   …   4   4

                                 4   4


     5   3   2   4   7   4   …
Loop anidado (sin índices)




     4   2   2   6   3   1   …   4   4

                                 4   4


     5   3   2   4   7   4   …
Loop anidado (sin índices)




     4   2   2   6   3   1   …   4   4

                                 4   4


     5   3   2   4   7   4   …
Loop anidado (sin índices)




     4   2   2   6   3   1   …   4   4

                                 4   4

                                 2   2
     5   3   2   4   7   4   …
Loop anidado (sin índices)




     4   2   2   6   3   1   …   4   4

                                 4   4

                                 2   2
     5   3   2   4   7   4   …

                                 …
Loop anidado (sin índices)




        ¿Costo?

      ¿Memoria?

      ¿Elegir R y S?
Loop anidado (con índices)




    6   3   4   2   3   1   …




    1   2   4   4   6   7   …

                                ÍNDICE
Loop anidado (con índices)




    6   3   4   2   3   1   …            6   6




    1   2   4   4   6   7   …

                                ÍNDICE
Loop anidado (con índices)




    6   3   4   2   3   1   …            6   6




    1   2   4   4   6   7   …

                                ÍNDICE
Loop anidado (con índices)




    6   3   4   2   3   1   …            6   6




    1   2   4   4   6   7   …

                                ÍNDICE

Loop anidado (con índices)




    6   3   4   2   3   1   …            6   6




    1   2   4   4   6   7   …

                                ÍNDICE
Loop anidado (con índices)




     6   3   4   2   3   1   …            6   6




     1   2   4   4   6   7   …

                                 ÍNDICE
Loop anidado (con índices)




    6   3   4   2   3   1   …            6   6




    1   2   4   4   6   7   …

                                ÍNDICE
Loop anidado (con índices)




    6   3   4   2   3   1   …            6   6




    1   2   4   4   6   7   …

                                ÍNDICE
Loop anidado (con índices)




    6   3   4   2   3   1   …            6   6

                                         4   4


    1   2   4   4   6   7   …

                                ÍNDICE
Loop anidado (con índices)




    6   3   4   2   3   1   …            6   6

                                         4   4

                                         4   4
    1   2   4   4   6   7   …

                                ÍNDICE
Loop anidado (con índices)




    6   3   4   2   3   1   …            6   6

                                         4   4

                                         4   4
    1   2   4   4   6   7   …

                                ÍNDICE
Loop anidado (con índices)




    6   3   4   2   3   1   …            6   6

                                         4   4

                                         4   4
    1   2   4   4   6   7   …

                                ÍNDICE   …
Loop anidado (con índices)




         ¿Costo?




  El “mejor caso” aquí asume que, para cada tupla r, las tuplas s1,…,sk que
      sean compatibles con r estén en un número constante de bloques.
Loop anidado (con índices)




       ¿Costo?




     ¿Memoria?

     ¿Elegir R y S?
Hash-join




    6   3   4   2   3   1   …             6   6




    1   2   4   4   6   7   …   MEM. P.
Hash-join




    6   3   4   2   3   1   …             6   6




    1   2   4   4   6   7   …   MEM. P.
Hash-join




    6   3   4   2   3   1   …             6   6

                                          4   4


    1   2   4   4   6   7   …   MEM. P.
Hash-join




    6   3   4   2   3   1   …             6   6

                                          4   4

                                          4   4
    1   2   4   4   6   7   …   MEM. P.

                                          …
Hash-join




       ¿Costo?



     ¿Memoria?



     ¿Elegir R y S?
Sort-merge-join




    6   3   4   2   3   1   …   ORDERAR




    6   2   4   7   6   1   …   ORDENAR
Sort-merge-join




    1   2   3   3   4   6   …   1   1




    1   2   4   6   6   7   …
Sort-merge-join




    1   2   3   3   4   6   …   1   1




    1   2   4   6   6   7   …
Sort-merge-join




    1   2   3   3   4   6   …   1   1

                                2   2


    1   2   4   6   6   7   …
Sort-merge-join




    1   2   3   3   4   6   …   1   1

                                2   2


    1   2   4   6   6   7   …

Sort-merge-join




    1   2   3   3   4   6   …   1   1

                                2   2


    1   2   4   6   6   7   …
Sort-merge-join




    1   2   3   3   4   6   …   1   1

                                2   2


    1   2   4   6   6   7   …
Sort-merge-join




    1   2   3   3   4   6   …   1   1

                                2   2

                                4   4
    1   2   4   6   6   7   …

                                …
Sort-merge-join




         ¿Costo?


       ¿Memoria?


      ¿Elegir R y S?

  Puede ser que las relaciones ya estén ordenadas por los atributos del
               join, en cual caso ¡es una buena opción!
Joins: Comparación
                    ¿Cuál es mejor?
              1. Loop anidado (sin índice)
              2. Loop anidado (con índice)
                     3. Hash-join
                  4. Sort-merge-join

         • Loop anidado (sin índice):
            – Nunca es bueno
         • Loop anidado (con índice):
            – Cuando el índice está disponible y:
                • Pocas tuplas en S satisfacen el join
         • Hash-join
            – Cuando R cabe en memoria y:
                • Muchas tuplas en S satisfacen el join
         • Sort-merge-join
            – Cuando R y S ya están ordenados por los
              atributos del join y:
                • Muchas tuplas en ambos satisfacen el join
Lo que vimos hoy
   SQL es un lenguaje declarativo
 Uno dice lo que quiere, no cómo debería ser computado

Idealmente, el motor puede elegir el mejor plan de ejecución
independientemente de la expresión particular de la consulta


El usuario no tiene que preocuparse por la optimización de la
consulta




Video Sugerido: https://www.youtube.com/watch?v=1HH4ZYXhJYE
CS2041- Base de datos I




                    5     Optimización
                          semántica
 OBJETIVO: SIMPLIFICAR LA PREGUNTA INICIAL

                                    SELECT E.APELLIDO
                                    FROM EMPLEADO AS E INNER JOIN
Empleados que ganan más que su
                                          EMPLEADO AS S ON E.NSS_SUPERV = S.NSS
supervisor
                                    WHERE E.SALARIO > S.SALARIO



           Supongamos que existe la siguiente restricción de
           integridad semántica:
           “ningún empleado puede ganar más que su
           supervisor directo”


                                                       No hace falta procesar la
                                                       consulta anterior ya que no
                                                       devolverá ninguna tupla
CS2041 Base de datos I                                                Computer Science




         Resumen
        ➔ Es importante considerar que la memoria es Limitada y
          por ello debemos escribir consultas optimizadas.
        ➔ El uso reglas heurísticas para la optimización sintáctica
          es crucial.
        ➔ Hace uso de los índices sea HASH, BTree es importante
          para grandes volúmenes de datos.
        ➔ El uso de los algoritmos de optimización depende del
          tipo de índice y sobre el atributo que se le aplicó.
GRACIAS
TEÓFILO CHAMBILLA

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
