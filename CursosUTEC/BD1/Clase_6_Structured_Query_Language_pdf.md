---
curso: BD1
titulo: Clase 6 Structured Query Language
slides: 144
fuente: Clase 6 Structured Query Language.pdf
---

               CLASE 6:
          STRUCTURED QUERY
            LANGUAGE (SQL)

        CS2041- Base de Datos I
                                   Ciclo 2024-1




             Teófilo Chambilla - tchambilla@utec.edu.pe
                Brenner Ojeda - bojeda@utec.edu.pe

En colaboración Aidan Hogan de la Universidad de Chile (https://aidanhogan.com/)
          CS2041 Base de Datos I
          Teófilo Chambilla Aquino




     Índice
•   Introducción
•   Structured Query Language (SQL)
•   Proyectar todo: SELECT *
•   Seleccionar filas: WHERE (=|<>|<|<=|etc.)
•   Unión (distinta): UNION
•   Diferencia: EXCEPT
•   Intersección: INTERSECT
•   Cruz: CROSS JOIN
•   Joins internos
•   Joins Externos
•   Valores Nulos
•   Consultas anidadas
•   Agregación
•   Limitar resultados
CS2041
BASE DE DATOS I
CICLO 2024-1


                                                                  SQL

                                           Algebra Relacional &
Introducción Modelo Relacional
                                            Cálculo Relacional          SQL II

                      Entidad - Relación
El álgebra y el cálculo




  … ¿Cómo se pueden expresar estos lenguajes
  matemáticos en un lenguaje computacional?
El lenguaje estructurado de consulta
Structured Query Language
(SQL)




                                       Capítulo 5 Database Management Systems,
                                            Ramakrishnan / Gehrke (Third Edition)
    Los inicios de SQL …




Conceptualizado por
   Donald Chamberlin (IBM)   y   Raymond F. Boyce (IBM)
    en 1974
1974 …
La evolución de SQL
Sistemas de bases de datos (con SQL)




                   ¡Varios sistemas pueden tener varias
                  interpretaciones del estándar de SQL!
                  Pero normalmente el “core” de SQL es
                compatible en los sistemas más populares.

                     http://db-engines.com/en/ranking/relational+dbms
Sistemas de bases de datos (con SQL)
        SQL en alto nivel

• Lenguaje de Manipulación de Datos (LMD)
  – o DML: Data Manipulation Language en inglés
  – Actualizar filas, consultar tablas, etc.

• Lenguaje de Definición de Datos (LDD)
  – o DDL: Data Definition Language en inglés
  – Crear y definir tablas

• Disparadores (triggers), transacciones, seguridad,
  SQL dinámico, etcétera
Los planetas
     Forma básica de una consulta de SQL




La sentencia SELECT permite recuperar información de la BD. No tiene nada
que ver con la operación de selecci ́on del ́algebra relacional.
                  Proyectar todo: SELECT *




La sentencia SELECT permite recuperar información de la BD. No tiene nada
que ver con la operación de selección del álgebra relacional.
                   ¡Cuidado!




La sentencia SELECT permite recuperar información de la BD. No tiene nada
que ver con la operación de selección del álgebra relacional.
Proyectar algo: SELECT [v1, …, vn]
Seleccionar filas: WHERE (=|<>|<|<=|etc.)
Seleccionar filas: WHERE … AND … (OR|NOT)
Duplicados: SELECT




                     ¿Algún problema aquí?

        Distinto: SELECT DISTINCT




   SQL “torce las reglas” del álgebra
 relacional a veces, por ejemplo, para
permitir duplicados, orden, extensiones,
                etcétera.
       ¿Qué piensan    ustedes?
¿Duplicados en tablas/resultados son útiles?
Ordenar resultados: ORDER BY [DESC|ASC]
Reunir tablas: JOIN
Alias: AS
Alias: tablas
Unión (distinta): UNIÓN
Unión (con alias): UNION + AS
Unión (bruta): UNION ALL
Diferencia: EXCEPT
Intersección: INTERSECT
Patrones simples: LIKE
Patrones simples: NOT LIKE
Abreviatura: IN
Abreviatura: BETWEEN
      • SELECT, FROM, WHERE
      • ORDER BY
      • JOIN (simple)
      • UNION, INTERSECT, EXCEPT
      • LIKE
      • IN, BETWEEN




SQL   • Más tipos de JOIN
      • Nulos
      • Consultas anidadas
      • Agregación
Producto cruz
Cruz: CROSS JOIN
Joins internos
Cruzar tablas: JOIN
     Cruzar tablas: EQUI JOIN




EQUI JOINS usan sólo ‘=‘ en el JOIN

    Cruzar tablas: JOIN




  ¿Esta consulta es un EQUI JOIN?




¡Sí! Sólo la condición del join cuenta.
        Cruzar tablas: JOIN USING




    Se puede usar JOIN USING cuando todos
los atributos del JOIN tengan el mismo nombre
           Cruzar tablas: NATURAL JOIN




Un EQUI-JOIN sobre los atributos que las tablas comparten (por pareja con AND).
Cruzar tablas: SELF JOIN




       Un JOIN sobre la tabla misma
 Cruzar tablas: INNER JOIN




INNER JOIN por defecto …
Joins Externos
 Joins Externos




¿Todos los planetas (y sus aterrizajes sí hay datos disponibles)?
     Joins Externos: LEFT [OUTER] JOIN




Se mantienen las tuplas de la izquierda si no hay datos desde la derecha
     Joins Externos: RIGHT [OUTER] JOIN




Se mantienen las tuplas de la derecha si no hay datos desde la izquierda
Joins Externos: FULL OUTER JOIN




  Se mantienen las tuplas de la derecha y la izquierda
Join Interno versus Joins Externos
Valores Nulos


   https://es.wikipedia.org/wiki/Null_(SQL)
                           Capítulo 5.6 | Ramakrishnan / Gehrke
Nulos




        DESCONOCIDO o INAPLICABLE
             (No significa FALSO)
Nulos: IS NULL
Nulos: IS NOT NULL
Comparación con nulos
 Comparación con nulos




¡El nulo en la consulta y el nulo en los datos son distintos!
       Comparación con nulos




                                               ???




Cuando no importa el valor del desconocido, el resultado se mantiene.
Cuando importa el valor del desconocido, el resultado es desconocido.
        Comparación con nulos




Cuando no importa el valor del desconocido, el resultado se mantiene.
Cuando importa el valor del desconocido, el resultado es desconocido.
Nulos: COALESCE




 Elegir el primer valor que no sea NULL

Ejercicio interactivo




       ¿Qué resultados devolverá la consulta?
Ejercicio interactivo




      ¿Cuáles resultados devolverá la consulta?
Consultas anidadas




                     Capítulo 5.4 | Ramakrishnan / Gehrke
Consultas Anidadas: WHERE/IN




       Subconsulta
Consultas Anidadas: WHERE/IN




            ¿Necesitamos una consulta anidada aquí?
Consultas Anidadas: WHERE/NOT IN
Consultas Anidadas: WHERE/NOT IN
Consultas Anidadas: WHERE/EXISTS




         Correlación:
 La subconsulta depende de la
       consulta exterior
Consultas Anidadas: WHERE/NOT EXISTS
Consultas Anidadas: WHERE/(NOT) UNIQUE




UNIQUE (no suportado por Postgres ☹):
           0 o 1 resultados
Consultas Anidadas: WHERE/ANY (o SOME)




   ANY y SOME son sinónimos
Consultas Anidadas: WHERE/ALL
Ejercicio interactivo




          ¿Los naves que han aterrizado
         en un planeta con (un) anillo(s)?
Ejercicio interactivo




          ¿Los naves que han aterrizado
         en un planeta con (un) anillo(s)?
Ejercicio interactivo




    ¿Los aterrizajes de la URRS que se hicieron antes
          que el primer aterrizaje de los EEUU?
Ejercicio interactivo




    ¿Los aterrizajes de la URRS que se hicieron antes
          que el primer aterrizaje de los EEUU?
Ejercicio interactivo




          ¿Los primeros aterrizajes
                de cada país?
Ejercicio interactivo




          ¿Los primeros aterrizajes
                de cada país?
Más consultas anidadas
        Consultas Anidadas: Valor




La subconsulta tiene que devolver
 un valor y una columna –si no…

Consultas Anidadas: Valor
Consultas Anidadas: Valor
Consultas Anidadas: Fila
Consultas Anidadas: Fila
Consultas Anidadas: Fila
Consultas Anidadas: Fila
Consultas Anidadas: FROM




      El alias Multi es
         obligatorio
Agregación



             Capítulo 5.5| Ramakrishnan / Gehrke
Operadores de agregación
Agregación: COUNT
Agregación: COUNT (DISTINCT afuera)
Agregación: COUNT DISTINCT
Agregación: COUNT(*)
Agregación: AVG




                      promedio
                                 Postgres


                      promedio
Depende del sistema
Agregación: AVG DISTINCT




                      promedio
                                 Postgres


                      promedio
Depende del sistema


                      promedio
Agregación: AVG (con casting)




                    promedio
Agregación: MIN
Agregación: MIN
Agregación: MIN
Agregación por planeta: explícitamente

Agregación por planeta: GROUP BY
     SELECT
      column_1,
      column_2,
      aggregate_function(column_3)
     FROM
      table_name
     GROUP BY
      column_1,
      column_2;
Agregación: GROUP BY
                      Agregación: GROUP BY




https://www.w3resource.com/sql/aggregate-functions/count-having.php
Agregación por planeta: GROUP BY
Agregación por planeta: GROUP BY/HAVING
Agregación por planeta: GROUP BY/HAVING
       SELECT
         column_1,
         aggregate_function(column_3)
       FROM
         table_name
       GROUP BY
         column_1,
       HAVING
        condition;
                   Agregación: GROUP BY/HAVING




https://www.w3resource.com/sql/aggregate-functions/count-having.php
                     Agregación: GROUP BY/HAVING




https://www.w3resource.com/sql/aggregate-functions/Max-having.php
Ejercicio interactivo




  Mostrar el agente que tiene mayor cantidad de órdenes




                    AGENT_CODE COUNT(AGENT_CODE)

                     A002          7
   Solución
SELECT agent_code,
COUNT(agent_code)
FROM orders
GROUP BY agent_code
HAVING COUNT (agent_code)=
(
    SELECT MAX(mycount)
    FROM (
        SELECT agent_code,
    COUNT(agent_code) mycount
    FROM orders
    GROUP BY agent_code)
);
Agregación por planeta: GROUP BY/HAVING
Agregación por planeta: HAVING/EVERY
Agregación por planeta: HAVING/ANY




           Postgres
Ejercicio interactivo




¿Los descubridores que han descubierto más que dos satélites
                    del mismo planeta?
Ejercicio interactivo




 ¿Los descubridores que han descubierto más de dos satélites
                     del mismo planeta?
Ejercicio interactivo




   ¿Las distancias de los planetas que han sido visitados
                   por tres o más países?
Ejercicio interactivo




   ¿Las distancias de los planetas que han sido visitados
                   por tres o más países?
Más detalles:
https://en.wikipedia.org/wiki/Select_(SQL)#Limiting_result_rows



Limitar resultados
Sistemas de bases de datos (con SQL)




              ¡Varios sistemas pueden tener varias
             interpretaciones del estándar de SQL!
             Pero normalmente el “core” de SQL es
           compatible en los sistemas más populares.

          http://db-engines.com/en/ranking/relational+dbms
Ordenar resultados: ORDER BY [DESC|ASC]

    Devolver n resultados: FETCH FIRST




Una versión estándar (desde SQL:2008) que se usa en Postgres y DB2.
    Devolver n resultados: LIMIT




Una versión no estándar que se usa en Postgres, SQLite y MySQL.
  Devolver n resultados: TOP




Una versión no estándar que se usa en SQL Server y MS Access.
           Devolver n resultados: ROW_NUMBER()




Una versión estándar (desde SQL:2003) que se usa en Postgres, DB2, MS Access, Oracle
        Devolver empates: RANK()




Una versión estándar (desde SQL:2003) que devuelva empates en el orden.
    Saltar n resultados: LIMIT + OFFSET




Una versión no estándar que se usa en Postgres, SQLite y MySQL.
Ejercicio interactivo




  ¿Los nombres de los tres planetas con los años más largos
          que estén más lejos del Sol que la Tierra?
Ejercicio interactivo




  ¿Los nombres de los tres planetas con los años más largos
          que estén más lejos del Sol que la Tierra?
Ejercicio interactivo




   ¿El nombre del planeta con el tercer año más largo
         que esté más lejos del Sol que la Tierra?
Ejercicio interactivo




    ¿El nombre del planeta con el tercer año más largo
          que esté más lejos del Sol que la Tierra?
    Más funciones



¡Dependen mucho del sistema particular!
Aritmético
Aritmético
Strings
Condicionales
Consultas directas vs.
  consultas anidadas
SQL tiene mucha redundancia
Consultas directas vs. consultas anidadas
 Nombres y géneros de los co-actores de Liv Tyler.




               ¿Son equivalentes pero cuál es más eficiente?
Consultas directas vs. consultas anidadas
Nombres y géneros de los co-actores de Liv Tyler.




             ¿Sonpoca
           ¡Hay   equivalentes pero cuál es más eficiente?
                       diferencia!
       Consultas directas vs. consultas anidadas
Nombres y géneros de co-actores de personas con una apellida “L%”.




       ¡Hay una diferencia (pero es poco predecible)!

   SQL es un lenguaje declarativo
Uno dice lo que quiere, no cómo se debería
computar

– Idealmente, el motor puede elegir el mejor plan
  de ejecución independientemente de su expresión
  particular
   • Pero, esto es caro, entonces en la práctica, hay
     diferencias
– Regresaremos al tema de rendimiento y
  optimización más adelante en el curso
– Pero en general, se puede expresar una consulta
  en la forma “más natural” y dejar la ejecución al
  motor
   SQL es un lenguaje declarativo
Uno dice lo que quiere, no cómo se debería
computar

– Idealmente, el motor puede elegir el mejor plan
  de ejecución independientemente de su expresión
  particular
   • Pero, esto es caro, entonces en la práctica, hay
     diferencias
– Regresaremos al tema de rendimiento y
  optimización más adelante en el curso
– Pero en general, se puede expresar una consulta
  en la forma “más natural” y dejar la ejecución al
  motor
      • SELECT, FROM, WHERE
      • ORDER BY
      • JOIN (simple)
      • UNION, INTERSECT, EXCEPT
      • LIKE
      • IN, BETWEEN




SQL   • Más tipos de JOIN
      • Nulos
      • Consultas anidadas
      • Agregación
Preguntas?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
