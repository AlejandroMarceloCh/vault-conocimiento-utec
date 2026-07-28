---
curso: BD1
titulo: Clase 10 Optimización de Consultas (Indices)
slides: 21
fuente: Clase 10 Optimización de Consultas (Indices).pdf
---

## Slide 1

Portada decorativa (fondo azul con figura futurista, logo UTEC, franja "Reinventa el mundo", mascota TransformaTec). Título: "Procesamiento y Optimización de Consultas" — CS2041 Base de Datos I, Ciclo 2024-1. Autores: Teófilo Chambilla (tchambilla@utec.edu.pe), Brenner Ojeda (bojeda@utec.edu.pe).

## Slide 2

Slide de índice. Header decorativo con logo UTEC y foto de mano robótica (decorativa).

**Índice**
- Uso de índices en SQL
- Explain Analyze

## Slide 3

**Índices en Bases de Datos**

Texto con viñetas coloreadas:
- (morado) Son estructuras que toman el par (llave, atributo) de una tabla para agilizar la búsqueda
- (naranja) Se busca el atributo en el índice y se retornan las filas de los elementos encontrados
- (negro) Se buscan las filas en la tabla directamente
- (verde) OJO, el mal uso de los índices puede provocar una **PEOR performance de la consulta**

Callout/globo de texto (verde) apuntando a la última viñeta: "Entonces, hay que usar índices dependiendo de la consulta a optimizar"

## Slide 4

**Índices: Hash vs. Árbol B+**

Diagrama comparativo con dos estructuras:

1. **Índice Hash** (parte superior izquierda): lista de claves (Saturno, Mercurio, Venus, Marte, Tierra, ...) apuntando mediante flechas naranjas a una tabla hash con buckets numerados (000, 001, 002, 003, ..., 126, 127, ..., 254, 255). Algunos buckets están resaltados en verde (colisiones/ocupados) y apuntan a su vez a una tabla de datos con columnas de valores (Tierra 1.00/1.00, Mercurio 0.39/0.38, Marte 1.52/0.53, Saturno 9.54/9.14, etc.). A la derecha el texto: "Levemente más eficiente para **búsquedas exactas** asumiendo una función de hash ideal".

2. **Árbol B+** (parte inferior): diagrama de árbol de 3 niveles.
   - Raíz: nodo con clave separadora `186`.
   - Nivel intermedio: nodo izquierdo con claves `53 | 134`, nodo derecho con clave `440`.
   - Nivel hoja: 5 hojas enlazadas secuencialmente con flechas naranjas (indicando lista enlazada de hojas típica de B+):
     - `44 Pluto ...`
     - `53 Neptuno ... / 76 Urano ...`
     - `134 Saturno ... / 152 Júpiter ...`
     - `186 Marte ... / 288 Tierra ...`
     - `440 Mercurio ... / 730 Venus ...`
   - Texto: "Mucho más eficiente para **búsquedas por rango**".
   - Recuadro amarillo destacado: "Árból B+ es más popular" (con manchas de tinta roja/negra decorativas alrededor).

## Slide 5

**Ejemplo uso de índices en SQL**

Bloque de código SQL (con sintaxis coloreada: azul=keywords, rojo=nombre tabla, granate=tipos):

```sql
CREATE TABLE Prueba(
    uid int primary key,
    c1 int,
    c2 text,
    c3 numeric,
    c4 timestamp,
    c5 interval,
    c6 int
);
```

## Slide 6

**Generamos datos aleatorios**

Bloque de código SQL para poblar la tabla Prueba con 1 millón de filas aleatorias:

```sql
INSERT INTO Prueba select id,
random()*10000,
md5(random()::text),
10000*random(),
clock_timestamp(),
(random()*1000::int||' hour')::interval,
random()*99999
from generate_series(1,1000000) t(id);
```

## Slide 7

**Configuración 'work_mem' en PostgreSQL para acelerar consultas SQL lentas**

- El valor predeterminado para `work_mem` es 4 MB.

Bloque de código (fondo gris) que muestra cómo cambiarlo temporalmente para una sesión:

```sql
SET work_mem = '256MB';
SELECT * FROM users ORDER BY LOWER(display_name);
RESET work_mem;
```

Texto explicativo: este ejemplo muestra cómo permitir que una consulta SQL específica use hasta 256 MB de memoria física para realizar la clasificación (sort) y luego restablece el valor de `work_mem` de la sesión actual al valor predeterminado.

Fuente (enlace): https://andreigridnev.com/blog/2016-04-16-increase-work_mem-parameter-in-postgresql-to-make-expensive-queries-faster/

## Slide 8

**¿Cómo saber que una consulta es lenta?**

Texto: EXPLAIN muestra el plan de ejecución de una declaración.

Dos bloques de código lado a lado (fondo gris):

Izquierda — sintaxis general del comando EXPLAIN:
```
EXPLAIN [ ( option [, ...] ) ] statement
EXPLAIN [ ANALYZE ] [ VERBOSE ] statement

where option can be one of:

   ANALYZE [ boolean ]
   VERBOSE [ boolean ]
   COSTS [ boolean ]
   BUFFERS [ boolean ]
   FORMAT { TEXT | XML | JSON | YAML }
```

Derecha — ejemplo de salida en formato JSON:
```sql
EXPLAIN (FORMAT JSON) SELECT * FROM foo;
```
```
                       QUERY PLAN
--------------------------------
 [                              +
   {                            +
     "Plan": {                  +
       "Node Type": "Seq Scan", +
       "Relation Name": "foo",  +
       "Alias": "foo",          +
       "Startup Cost": 0.00,    +
       "Total Cost": 155.00,    +
       "Plan Rows": 10000,      +
       "Plan Width": 4          +
     }                          +
   }                            +
 ]
(1 row)
```

## Slide 9

**¿Cómo saber que una consulta es lenta?**

Captura de pantalla de una interfaz tipo pgAdmin ("Data Output" / Explain / Messages / Notifications):

Consulta ejecutada: `EXPLAIN SELECT * FROM Prueba`

Tabla de resultado (columna QUERY PLAN):
| # | QUERY PLAN |
|---|---|
| 1 | Seq Scan on prueba (cost=0.00..24286.00 rows=1000000 width=80) |

Texto: EXPLAIN notifica que se utiliza un **Seq Scan**: una secuencia, bloque por bloque, que lee los datos de la tabla Prueba.

## Slide 10

**¿Cómo saber que una consulta es lenta?**

Repite la misma captura de pantalla de la tabla del plan de consulta (Seq Scan on prueba, cost=0.00..24286.00 rows=1000000 width=80).

Explicación del significado del costo:
- ¿Qué es el costo? El primer valor **0.00** es el costo para obtener la primera fila. El segundo valor **24286.00** son los costos para obtener todas las filas.
- **Las filas (rows)** son el número aproximado de filas devueltas cuando se realiza una operación de exploración secuencial. El planificador devuelve este valor; en este caso coincide con el número real de filas en la tabla.
- **El ancho (width)** es un tamaño promedio de una fila en bytes.

## Slide 11

**¿Cómo saber que una consulta es lenta?**

Captura de pantalla pgAdmin con la consulta:
```sql
EXPLAIN (ANALYZE) SELECT * FROM Prueba
```

Tabla de resultado (QUERY PLAN):
| # | QUERY PLAN |
|---|---|
| 1 | Seq Scan on prueba (cost=0.00..24286.00 rows=1000000 width=80) (actual time=0.023..113.762 rows=1000000 loops=1) |
| 2 | Planning time: 0.092 ms |
| 3 | Execution time: 145.143 ms |

Lista de parámetros que muestra el comando:
- **Actual time**: tiempo real en milisegundos dedicado a obtener la primera fila y todas las filas, respectivamente.
- **Planning time**: tiempo dedicado a obtener el plan de ejecución.
- **rows**: número real de filas recibidas con Seq Scan.
- **loops**: número de veces que se tuvo que realizar la operación Seq Scan.
- **Execution time**: tiempo total de ejecución de la consulta.

## Slide 12

**¿Cómo saber que una consulta es lenta?**

Captura de pantalla pgAdmin con la consulta:
```sql
EXPLAIN (ANALYZE,BUFFERS) SELECT * FROM Prueba
```

Tabla de resultado (QUERY PLAN):
| # | QUERY PLAN |
|---|---|
| 1 | Seq Scan on prueba (cost=0.00..24286.00 rows=1000000 width=80) (actual time=0.021..112.087 rows=1000000 loops=1) |
| 2 | Buffers: shared hit=12372 read=1914 |
| 3 | Planning time: 0.093 ms |
| 4 | Execution time: 149.970 ms |

- **Buffers: read** es el número de bloques que PostgreSQL lee del disco.
- Leemos la tabla por bloques. Si el caché está vacío, tuvimos que acceder a 1914 bloques para leer toda la tabla del disco.
- **Buffers: shared hit** es el número de bloques recuperados del caché de PostgreSQL.

## Slide 13

**¿Cómo saber que una consulta es lenta?**

Captura de pantalla pgAdmin con la consulta:
```sql
EXPLAIN (ANALYZE,BUFFERS) SELECT * FROM Prueba where c1 > 100
```

Tabla de resultado (QUERY PLAN):
| # | QUERY PLAN |
|---|---|
| 1 | Seq Scan on prueba (cost=0.00..26786.00 rows=990303 width=80) (actual time=0.021..163.281 rows=989855 loops=1) |
| 2 | Filter: (c1 > 100) |
| 3 | Rows Removed by Filter: 10145 |
| 4 | Buffers: shared hit=12404 read=1882 |
| 5 | Planning time: 0.189 ms |
| 6 | Execution time: 202.004 ms |

Texto: Solo se filtran 10145 filas del 1 millón, son eliminadas del resultado. Nos quedamos 989855 filas.

## Slide 14

**Crear índices en SQL**

Sintaxis general (con colores: azul=keywords, rojo=nombre, naranja=tabla/attr):

```sql
CREATE INDEX nombre ON tabla(attr) USING method
```

- **nombre**: el nombre del índice
- **tabla(attr)**: la tabla y atributos sobre los que se construirá el índice
- **method**: puede ser b-tree (por defecto), hash, GIN, etc

## Slide 15

**Crear índices en SQL**

- Para filtrar prueba por c1:

Bloque de código (fondo gris):
```sql
CREATE INDEX idx_prueba1 ON prueba USING btree (c1)

Query returned successfully in 1 secs 215 msec.
```

## Slide 16

**¿Cómo saber que una consulta es lenta?**

Captura de pantalla pgAdmin, mismo query anterior repetido (con índice ya creado pero sin forzar su uso todavía):
```sql
EXPLAIN (ANALYZE,BUFFERS) SELECT * FROM Prueba where c1 > 100
```

Tabla de resultado (QUERY PLAN):
| # | QUERY PLAN |
|---|---|
| 1 | Seq Scan on prueba (cost=0.00..26786.00 rows=990300 width=80) (actual time=0.016..170.848 rows=989855 loops=1) |
| 2 | Filter: (c1 > 100) |
| 3 | Rows Removed by Filter: 10145 |
| 4 | Buffers: shared hit=12660 read=1626 |
| 5 | Planning time: 0.150 ms |
| 6 | Execution time: 210.817 ms |

Texto: El número estimado de filas ha cambiado. **¿Qué hay del índice?** Forzaremos a usar el índice **deshabilitando Seq Scan**.

## Slide 17

**¿Cómo saber que una consulta es lenta?**

Captura de pantalla pgAdmin con la consulta:
```sql
SET enable_seqscan TO off;
EXPLAIN (analyze,buffers) SELECT * FROM Prueba where c1 > 100
```

Tabla de resultado (QUERY PLAN):
| # | QUERY PLAN |
|---|---|
| 1 | Bitmap Heap Scan on prueba (cost=18551.25..45216.00 rows=990300 width=80) (actual time=84.284..249.998 rows=989855 loops=1) |
| 2 | Recheck Cond: (c1 > 100) |
| 3 | Heap Blocks: exact=14286 |
| 4 | Buffers: shared hit=13835 read=3159 |
| 5 | -> Bitmap Index Scan on idx_prueba1 (cost=0.00..18303.67 rows=990300 width=0) (actual time=81.843..81.843 rows=989855 loops=...) |
| 6 | Index Cond: (c1 > 100) |
| 7 | Buffers: shared hit=2452 read=256 |
| 8 | Planning time: 0.183 ms |
| 9 | Execution time: 290.197 ms |

Texto: En índice **Bitmap Scan** e **Index Cond**, utiliza el índice **idx_prueba1** en lugar de **Filter**.

Fuentes (enlaces): https://codingsight.com/query-optimization-in-postgresql-explain-basics-part-1/ y https://medium.com/@Alibaba_Cloud/principles-and-optimization-of-5-postgresql-indexes-btree-hash-gin-gist-and-brin-4d133e7f1842

## Slide 18

**OJO con los índices**

- Por mucho que el índice exista, no siempre será usado, pues si se requieren muchas tuplas, el sobrecosto será demasiado.

Dos capturas de terminal (fondo negro, texto verde/blanco tipo consola psql):

Ejemplo 1 — búsqueda exacta usa el índice:
```
cc3201=# EXPLAIN SELECT * FROM actor WHERE nombre = 'Jackson, Samuel L.';
                            QUERY PLAN
------------------------------------------------------------------
 Index Scan using actor_pkey on actor  (cost=0.00..8.28 rows=1 width=18)
   Index Cond: ((nombre)::text = 'Jackson, Samuel L.'::text)
(2 rows)
```

Ejemplo 2 — búsqueda con función `left()` NO usa índice, hace Seq Scan:
```
cc3201=# EXPLAIN SELECT * FROM actor WHERE left(nombre, 1) = 'F';
                        QUERY PLAN
-----------------------------------------------------------
 Seq Scan on actor  (cost=0.00..311.14 rows=73 width=18)
   Filter: ("left"((nombre)::text, 1) = 'F'::text)
(2 rows)
```

## Slide 19

**Visualizar gráficamente la ejecución de la consulta**

Captura de pantalla de un editor de queries (pestañas "Query Editor" / "Query History") con una consulta SQL compleja (subconsulta correlacionada con HAVING):

```sql
SELECT p_nombre,p_anho, COUNT(DISTINCT personaje)
FROM personaje P, actor A
WHERE P.a_nombre = A.nombre
AND A.genero = 'F'
GROUP BY p_nombre, p_anho
HAVING COUNT(DISTINCT personaje)=( SELECT  MAX(cantidad)
                        FROM (
                        SELECT p_nombre,p_anho, COUNT(DISTINCT personaje) AS cantidad
                        FROM personaje P, actor A
                        WHERE P.a_nombre = A.nombre
                        AND A.genero = 'F'
                        GROUP BY p_nombre, p_anho) Temp);
```

Texto: En Windows Shift+F7 (atajo para generar el plan gráfico).

## Slide 20

**Visualizar gráficamente la ejecución de la consulta**

Repite la misma consulta SQL de la slide 19 (arriba) y debajo muestra el **plan de ejecución gráfico** (diagrama de flujo con iconos de tablas y operadores conectados por flechas), generado con Shift+F7. Estructura del diagrama (dos ramas simétricas que confluyen):

Rama superior:
`personaje` (tabla) → `Hash` ← `actor` (tabla) → `Hash Inner Join` → `Sort` → `Aggregate` → `Aggregate` → `Aggregate` (nodo final, converge con la rama inferior)

Rama inferior (subconsulta del HAVING):
`personaje` (tabla) → `Hash` ← `actor` (tabla) → `Hash Inner Join` → `Sort` → (converge hacia el `Aggregate` final de la rama superior)

Cada nodo tiene un ícono (tabla=grilla de colores, hash=ícono de hash, sort=lista ordenada, aggregate=tabla agregada) con flechas negras indicando el flujo de datos entre operadores, terminando en el `Aggregate` final a la derecha.

Fuente (enlace): https://www.postgresonline.com/journal/archives/27-Reading-PgAdmin-Graphical-Explain-Plans.html

## Slide 21

Slide final, solo texto: "¿Preguntas?". Sin elementos visuales adicionales.
