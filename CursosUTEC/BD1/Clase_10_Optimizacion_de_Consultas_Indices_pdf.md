---
curso: BD1
titulo: Clase 10 Optimización de Consultas (Indices)
slides: 21
fuente: Clase 10 Optimización de Consultas (Indices).pdf
---

  Procesamiento y
  Optimización de
     Consultas

CS2041- Base de Datos I
          Ciclo 2024-1




      Teófilo Chambilla - tchambilla@utec.edu.pe
         Brenner Ojeda - bojeda@utec.edu.pe
    CS2041 Base de Datos I
    Teófilo Chambilla Aquino




Índice
• Uso de indices en SQL
• Explain Analyze
Índices en Bases de Datos

• Son estructuras que toman el par (llave, atributo) de una tabla
   para agilizar la búsqueda
• Se busca el atributo en el índice y se retornan las filas de
   los elementos encontrados
• Se buscan las filas en la tabla directamente
• OJO, el mal uso de los índices puede provocar una PEOR
   performance de la consulta
                                        Entonces, hay que usar
                                       índices dependiendo de
                                        la consulta a optimizar
  Índices: Hash vs. Árbol B+
                                        Levemente más eficiente para
                                        búsquedas exactas asumiendo una
                                        función de hash ideal




                           Arból B+ es más popular



Mucho más eficiente para
búsquedas por rango
Ejemplo uso de índices en SQL
         CREATE TABLE Prueba(
              uid int primary key,
              c1 int,
              c2 text,
              c3 numeric,
              c4 timestamp,
              c5 interval,
              c6 int
         );
Generamos datos aleatorios

INSERT INTO Prueba select id,
random()*10000,
md5(random()::text),
10000*random(),
clock_timestamp(),
(random()*1000::int||' hour')::interval,
random()*99999
from generate_series(1,1000000) t(id);
       Conﬁguración ‘work_mem’ en PostgreSQL para acelerar
       consultas SQL lentas


       • El valor predeterminado para work_memes 4 MB
               SET work_mem = '256MB';
                    SELECT * FROM users ORDER BY LOWER(display_name);
               RESET work_mem;




                 Este ejemplo muestra cómo permitir que una consulta SQL específica use
                 hasta 256 MB de memoria física para realizar la clasificación y luego
                 restablece el work_mem valor de la sesión actual al valor predeterminado
                 actual.




Fuente: https://andreigridnev.com/blog/2016-04-16-increase-work_mem-parameter-in-postgresql-to-make-expensive-queries-faster/
    ¿Cómo saber que una consulta es lenta?


               EXPLAIN : muestra el plan de ejecución de una declaración




EXPLAIN [ ( option [, ...] ) ] statement                     EXPLAIN (FORMAT JSON) SELECT * FROM foo;
EXPLAIN [ ANALYZE ] [ VERBOSE ] statement                                QUERY PLAN
                                                             --------------------------------
where option can be one of:                                   [                              +
                                                                {                            +
   ANALYZE [ boolean ]                                            "Plan": {                  +
   VERBOSE [ boolean ]                                               "Node Type": "Seq Scan",+
                                                                     "Relation Name": "foo", +
   COSTS [ boolean ]
                                                                     "Alias": "foo",         +
   BUFFERS [ boolean ]
                                                                     "Startup Cost": 0.00,   +
   FORMAT { TEXT | XML | JSON | YAML }                               "Total Cost": 155.00,   +
                                                                     "Plan Rows": 10000,     +
                                                                     "Plan Width": 4         +
                                                                  }                          +
                                                                }                            +
                                                              ]
                                                             (1 row)
¿Cómo saber que una consulta es lenta?




      EXPLAIN notiﬁca que se utiliza un Seq Scan: una secuencia, bloque por bloque,
      que lee los datos de la tabla Prueba
¿Cómo saber que una consulta es lenta?




¿Qué es el costo ?
El primer valor 0.00 es el costo para obtener la primera ﬁla. El segundo valor
24286.00 son los costos para obtener todas las ﬁlas.
Las ﬁlas (rows) son el número aproximado de ﬁlas devueltas cuando se
realiza una operación de exploración secuencial. El planiﬁcador devuelve este
valor. En este caso, coincide con el número real de ﬁlas en la tabla.
El ancho(width) es un tamaño promedio de una ﬁla en bytes.
¿Cómo saber que una consulta es lenta?




  El comando muestra los siguientes parámetros:
   ●   Actual time, es el tiempo real en milisegundos dedicado a obtener la
       primera ﬁla y todas las ﬁlas, respectivamente
   ●   Planning time, es el tiempo dedicado a obtener el plan de ejecución.
   ●   rows, es el número real de ﬁlas recibidas con Seq Scan.
   ●   loops, es el número de veces que se tuvo que realizar la operación Seq
       Scan.
   ●   Execution time, es el tiempo total de ejecución de la consulta.
¿Cómo saber que una consulta es lenta?




   ●   Buffers: read es el número de bloques que PostgreSQL lee del disco.
   ●   Leemos la tabla por bloques. Si el caché está vacío. Tuvimos que acceder a 1914
       bloques para leer toda la tabla del disco.
   ●   Buffers: shared hit es el número de bloques recuperados del caché
       PostgreSQL.
¿Cómo saber que una consulta es lenta?




   ●   Solo se ﬁltran 10145 ﬁlas del 1 millón , son eliminadas del resultado. Nos
       quedamos 989855 ﬁlas.
  Crear índices en SQL
CREATE INDEX nombre ON tabla(attr) USING method
• nombre: el nombre del índice
• tabla(attr): la tabla y atributos sobre los que se
  construirá el índice
• method: puede ser b-tree (por defecto), hash, GIN, etc
Crear índices en SQL
• Para filtrar prueba por c1:
    CREATE INDEX idx_prueba1 ON prueba USING btree (c1)


    Query returned successfully in 1 secs 215 msec.
¿Cómo saber que una consulta es lenta?




   ●   El número estimado de ﬁlas ha cambiado. ¿Qué hay del índice?
   ●   Forzaremos a usar el índice deshabilitando Seq Scan:
       ¿Cómo saber que una consulta es lenta?




               ●     En índice Bitmap Scan e Index Cond,utiliza el índice
                     idx_prueba1 en lugar de Filter




Fuente: https://codingsight.com/query-optimization-in-postgresql-explain-basics-part-1/
https://medium.com/@Alibaba_Cloud/principles-and-optimization-of-5-postgresql-indexes-btree-hash-gin-gist-and-brin-4d133e7f1842
OJO con los índices
• Por mucho que el índice exista, no siempre será
  usado, pues si se requieren muchas tuplas, el
  sobrecosto será demasiado
Visualizar gráﬁcamente la ejecución de la consulta




  ●   En Windows Shif+F7
      Visualizar gráﬁcamente la ejecución de la consulta




FUENTE: https://www.postgresonline.com/journal/archives/27-Reading-PgAdmin-Graphical-Explain-Plans.html

¿Preguntas?

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
