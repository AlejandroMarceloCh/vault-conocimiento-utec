---
curso: BD1
titulo: Clase 6 Structured Query Language
slides: 144
fuente: Clase 6 Structured Query Language.pdf
---

## Slide 1
Portada. "CLASE 6: STRUCTURED QUERY LANGUAGE (SQL)" · CS2041 - Base de Datos I · Ciclo 2024-1. Autores: Teófilo Chambilla - tchambilla@utec.edu.pe, Brenner Ojeda - bojeda@utec.edu.pe. Colaboración de Aidan Hogan (Universidad de Chile). Fondo decorativo (túnel digital con figura humana).

## Slide 2
Índice del capítulo (lista con viñetas): Introducción · Structured Query Language (SQL) · Proyectar todo: SELECT * · Seleccionar filas: WHERE (=|<>|<|<=|etc.) · Unión (distinta): UNION · Diferencia: EXCEPT · Intersección: INTERSECT · Cruz: CROSS JOIN · Joins internos · Joins Externos · Valores Nulos · Consultas anidadas · Agregación · Limitar resultados. Fondo decorativo: mano robótica sobre mapa mundial digital.

## Slide 3
Encabezado de sección "CS2041 / Base de Datos I / Ciclo 2024-1". Diagrama de barra de progreso del curso con 8 segmentos horizontales (barras azules rellenas = temas ya vistos, barras claras = pendientes), etiquetados debajo: "Introducción", "Modelo Relacional", "Entidad - Relación", "Algebra Relacional & Cálculo Relacional", "SQL" (resaltado con recuadro celeste, es el tema actual, con icono de un personaje ninja/mago apuntando), "SQL II". Icono de bandera a cuadros al final de la línea de tiempo (meta del curso).

## Slide 4
Título "El álgebra y el cálculo". Dos recuadros comparativos lado a lado:
- Izquierda "El Álgebra Relacional (Mínima / Clásica)": fórmulas π_{A1,...,An}(R), σ_condición(R), ρ_{Ai/Aj}(R); operaciones R1 ∪ R2, R1 × R2, R1 − R2; abajo en gris tenue (atenuado) R1 ∩ R2, R1 ⋈_condición R2 (indicando que son derivables, no primitivas).
- Derecha "El Cálculo Relacional (de tuplas)": Fórmulas atómicas (sea c una constante, OP ∈ {<,>,=,≤,≥,≠}): formas R, R.a OP R'.a', R.a OP c, c OP R.a. Debajo: "Una fórmula puede ser: una fórmula atómica o (recursivamente) p y q formulas: ¬p, p∧q, p∨q, p⇒q, ∃R(p), ∀R(p)".
Debajo de los recuadros, pregunta retórica en texto grande: "¿Cómo se pueden expresar estos lenguajes matemáticos en un lenguaje computacional?"

## Slide 5
Título "El lenguaje estructurado de consulta / Structured Query Language (SQL)" en azul. Ilustración decorativa de personaje ninja/mago sentado en un trono con un lápiz gigante brillante. Cita de referencia: "Capítulo 5 Database Management Systems, Ramakrishnan / Gehrke (Third Edition)".

## Slide 6
Título "Los inicios de SQL …". Dos fotografías (retratos) de los creadores: Donald Chamberlin (IBM) y Raymond F. Boyce (IBM). Texto: "Conceptualizado por Donald Chamberlin (IBM) y Raymond F. Boyce (IBM) en 1974".

## Slide 7
Título "1974 …". Tres fotografías históricas en blanco y negro/vintage: (1) izquierda, gran mainframe/rack de equipo de cómputo de la época con una mujer posando junto a él (foto publicitaria retro); (2) arriba derecha, hombre usando un terminal de computadora con pantalla de texto verde/monocromo; (3) abajo derecha, mujer tecleando en un terminal de computadora antiguo. Ilustra el contexto tecnológico de 1974.

## Slide 8
Título "La evolución de SQL", con logo/ícono de base de datos (cilindros apilados) y wordmark "SQL" en naranja. Línea de tiempo horizontal 1970-2015 con marcas de años (1970,1975,1980,1985,1990,1995,2000,2005,2010,2015). Hitos etiquetados en diagonal sobre la línea: "El álgebra relacional" (~1970), "SEQUEL (Chamberlin y Boyce)" en azul (~1974), "SQL (Oracle v2 y IBM System R)" (~1979), "SQL-86 (Primer estándar)", "SQL-89 (Revisión menor de SQL-86)", "SQL-92 (Revisión sustancial de SQL-89)", "SQL:1999 (Recursión, expresiones regulares, etc.)", "SQL:2003 (Apoyo básico para XML, etc.)", "SQL:2006 (Apoyo avanzado para XML, etc.)", "SQL:2008 (Revisión menor)", "SQL:2011 (Datos temporales, etc.)". Subtítulo: "(Sistemas de bases de datos comerciales)".

## Slide 9
Título "Sistemas de bases de datos (con SQL)". Captura/tabla tipo ranking (fuente: db-engines.com), "140 systems in ranking, September 2018". Tabla con columnas: Rank (Sep2018/Aug2018/Sep2017), DBMS, Database Model, Score (Sep2018/Aug2018/Sep2017). Reproducción parcial de filas visibles:
| Rank | DBMS | Model | Score Sep2018 |
|---|---|---|---|
| 1 | Oracle | Relational DBMS | 1309.12 |
| 2 | MySQL | Relational DBMS | 1180.48 |
| 3 | Microsoft SQL Server | Relational DBMS | 1051.28 |
| 4 | PostgreSQL | Relational DBMS | 406.43 |
| 5 | DB2 | Relational DBMS | 181.06 |
| 6 | Microsoft Access | Relational DBMS | 133.39 |
| 7 | SQLite | Relational DBMS | 115.46 |
| 8 | Teradata | Relational DBMS | 77.38 |
| 9 | MariaDB | Relational DBMS | 70.64 |
| 10 | Hive | Relational DBMS | 59.63 |
| 11 | SAP Adaptive Server | Relational DBMS | 58.04 |
| 12 | FileMaker | Relational DBMS | 55.30 |
| 13 | SAP HANA | Relational DBMS | 52.73 |
| 14 | Microsoft Azure SQL Database | Relational DBMS | 25.25 |
| 15 | Informix | Relational DBMS | 24.91 |
| 16 | Vertica | Relational DBMS | — |
| 17 | Firebird | Relational DBMS | — |
| 18 | Amazon Redshift | Relational DBMS | — |
| 19 | Netezza | Relational DBMS | — |
| 20 | Google BigQuery | Relational DBMS | — |
| 21 | Impala | Relational DBMS | — |
| 22 | Spark SQL | Relational DBMS | — |
| 23 | Greenplum | Relational DBMS | 10.85 |
| 24 | dBASE | Relational DBMS | 10.20 |

Recuadro amarillo destacado con texto: "¡Varios sistemas pueden tener varias interpretaciones del estándar de SQL! Pero normalmente el "core" de SQL es compatible en los sistemas más populares." Link al pie: http://db-engines.com/en/ranking/relational+dbms

## Slide 10
Título "Sistemas de bases de datos (con SQL)". Diagrama tipo flor/Venn con 5 "pétalos" elípticos de colores alrededor de un círculo central amarillo etiquetado "Core": pétalo superior "MySQL" (rosa claro), pétalo derecho superior gris (sin etiqueta visible), pétalo derecho grande rojo oscuro "Oracle", pétalo inferior derecho oliva/verde (sin etiqueta visible), pétalo inferior "IMB DB2" (rosado, sic - typo de "IBM DB2"), pétalo izquierdo celeste "PostgreSQL". Ilustra que cada sistema tiene funcionalidades propias que se superponen en un núcleo SQL común ("Core").

## Slide 11
Título "SQL en alto nivel". Lista con viñetas de dos colores:
- Azul: "Lenguaje de Manipulación de Datos (LMD) — o DML: Data Manipulation Language en inglés — Actualizar filas, consultar tablas, etc."
- Naranja: "Lenguaje de Definición de Datos (LDD) — o DDL: Data Definition Language en inglés — Crear y definir tablas"
- Gris: "Disparadores (triggers), transacciones, seguridad, SQL dinámico, etcétera"

## Slide 12
Título "Los planetas". Tres tablas de ejemplo (esquema de base de datos usado en todo el capítulo) sobre fondo gris con textura estelar decorativa:
Tabla **Planeta** (nombre subrayado = llave primaria) con columnas nombre, dist, radio, grav, días, años, temp, anillo:
| nombre | dist | radio | grav | días | años | temp | anillo |
|---|---|---|---|---|---|---|---|
| Mercurio | 0,39 | 0,38 | 2,8 | 58,646 | 0,241 | 440 | false |
| Venus | 0,72 | 0,95 | 8,9 | -243,019 | 0,615 | 730 | false |
| Tierra | 1,00 | 1,00 | 9,8 | 0,997 | 1,000 | 288 | false |
| Marte | 1,52 | 0,53 | 3,7 | 1,026 | 1,880 | 186 | false |
| Júpiter | 5,20 | 10,97 | 22,9 | 0,414 | 11,862 | 152 | true |
| Saturno | 9,54 | 9,14 | 9,1 | 0,444 | 29,447 | 134 | true |
| Urano | 19,19 | 3,98 | 7,8 | -0,719 | 84,017 | 76 | true |
| Neptuno | 30,07 | 3,86 | 11,0 | 0,671 | 164,791 | 53 | true |

Tabla **Satélite** (nombre subrayado) columnas nombre, planeta, descubridor, año:
| nombre | planeta | descubridor | año |
|---|---|---|---|
| Luna | Tierra | ⊥ | ⊥ |
| Ganímedes | Júpiter | Galileo Galilei | 1610 |
| Calisto | Júpiter | Galileo Galilei | 1610 |
| Europa | Júpiter | Galileo Galilei | 1610 |
| Io | Júpiter | Galileo Galilei | 1610 |
| Titán | Saturno | Christiaan Huygens | 1655 |
| Tritón | Neptuno | William Lassell | 1846 |

Tabla **Aterrizaje** (nave subrayado) columnas nave, planeta, país, año:
| nave | planeta | país | año |
|---|---|---|---|
| Messenger | Mercurio | EEUU | 2015 |
| Venera 3 | Venus | URRS | 1966 |
| Pioneer | Venus | EEUU | 1978 |
| Mars 2 lander | Marte | URRS | 1971 |
| Viking 1 | Marte | EEUU | 1976 |
| Beagle 2 | Marte | ESA | 2003 |
| Galileo | Júpiter | EEUU | 2003 |

## Slide 13
Título "Forma básica de una consulta de SQL". Bloque de código central:
```sql
SELECT [atributos]
FROM   [tablas]
WHERE  [condición]
```
(palabras clave SELECT/FROM/WHERE en magenta). Ilustración decorativa del ninja/mago señalando con un lápiz. Nota al pie: "La sentencia SELECT permite recuperar información de la BD. No tiene nada que ver con la operación de selección del álgebra relacional."

## Slide 14
Título "Proyectar todo: SELECT *". Arriba, tabla Planeta completa (igual a slide 12) sobre fondo gris. Abajo, ejemplo de consulta y resultado:
```sql
SELECT *
FROM Planeta
```
Resultado (recuadro celeste), la misma tabla Planeta pero con las filas reordenadas (Saturno, Urano, Mercurio, Venus, Tierra, Marte, Júpiter, Neptuno) — ilustra que SQL no garantiza orden de filas sin ORDER BY. Nota al pie repetida sobre SELECT vs selección relacional.

## Slide 15
Título "¡Cuidado!". Texto grande: "SELECT indica proyectión (π)" y "WHERE indica selección (σ)" (aclara la confusión de nombres entre SQL y álgebra relacional). Diagrama con flecha curva doble que conecta un bloque de código SQL con su equivalente en álgebra relacional:
```sql
SELECT tipo
FROM   Cerveza
WHERE  grados > 4,8
```
↔ π_tipo(σ_grados>4,8(Cerveza))
Ilustración decorativa del ninja apuntando con lápiz.

## Slide 16
Título "Proyectar algo: SELECT [v1, …, vn]". Arriba, tabla Planeta completa (fondo gris). Abajo, ejemplo:
```sql
SELECT nombre, dist
FROM Planeta
```
Resultado (recuadro celeste) con columnas nombre y dist, filas en orden: Saturno 9,54; Urano 19,19; Mercurio 0,39; Venus 0,72; Tierra 1,00; Marte 1,52; Júpiter 5,20; Neptuno 30,07.

## Slide 17
Título "Seleccionar filas: WHERE (=|<>|<|<=|etc.)". Arriba, tabla Planeta completa. Abajo, ejemplo:
```sql
SELECT grav, temp
FROM Planeta
WHERE nombre = 'Venus'
```
Resultado (recuadro celeste): una sola fila, grav=8,9, temp=730.

## Slide 18
Título "Seleccionar filas: WHERE … AND … (OR|NOT)". Arriba, tabla Planeta completa. Abajo, ejemplo:
```sql
SELECT nombre, dist
FROM Planeta
WHERE radio > 1.0
AND anillo IS FALSE
```
Resultado (recuadro celeste): tabla con encabezados nombre/dist pero SIN filas — resultado vacío (ningún planeta con radio>1.0 y anillo false, ya que los de radio>1 son los gigantes gaseosos con anillo=true).

## Slide 19
Título "Duplicados: SELECT". Arriba, tabla Aterrizaje completa (fondo gris, igual a slide 12). Abajo, ejemplo:
```sql
SELECT planeta
FROM Aterrizaje
```
Resultado (recuadro celeste), columna planeta con duplicados: Marte, Marte, Marte, Venus, Venus, Mercurio, Júpiter. Recuadro de texto con borde punteado: "¿Algún problema aquí?" — plantea la pregunta de si SQL elimina duplicados por defecto (no lo hace).

## Slide 20
Slide decorativa/humorística: tira cómica de 3 viñetas de un astronauta bajo el agua (fondo azul marino), en la primera está solo, en la segunda aparecen dos peces nadando cerca, en la tercera hay varios peces rodeándolo y dice en un globo de diálogo "HOUSTON, TENEMOS UN PROBLEMA." Firma "P.PENNE" en la esquina. Chiste visual (peces = duplicados que se multiplican) enlazado al problema de duplicados de la slide anterior. Sin contenido técnico de SQL en esta slide.

## Slide 21
Título "Distinto: SELECT DISTINCT". Arriba, tabla Aterrizaje completa. Abajo, ejemplo:
```sql
SELECT DISTINCT planeta
FROM Aterrizaje
```
Resultado (recuadro celeste): planeta sin duplicados: Venus, Marte, Mercurio, Júpiter. Recuadro amarillo con borde punteado: "SQL "torce las reglas" del álgebra relacional a veces, por ejemplo, para permitir duplicados, orden, extensiones,". Recuadro morado debajo: "¿Qué piensan ustedes? ¿Duplicados en tablas/resultados son útiles?" (pregunta de discusión para la clase).

## Slide 22
Título "Ordenar resultados: ORDER BY [DESC|ASC]". Arriba, tabla Aterrizaje completa. Abajo, ejemplo:
```sql
SELECT *
FROM Aterrizaje
ORDER BY año DESC, nave
```
Resultado (recuadro celeste), tabla completa reordenada por año descendente y luego nave: Messenger(2015), Beagle 2(2003), Galileo(2003), Pioneer(1978), Viking 1(1976), Mars 2 lander(1971), Venera 3(1966).

## Slide 23
Título "Reunir tablas: JOIN". Arriba, tablas Planeta y Aterrizaje completas lado a lado. Abajo, ejemplo:
```sql
SELECT nombre, año, nave
FROM Planeta, Aterrizaje
WHERE nombre = planeta
AND dist > 1.00
AND año >= 2000
```
Resultado (recuadro celeste): columnas nombre/año/nave, 2 filas: Marte 2003 Beagle 2; Júpiter 2003 Galileo. Ilustra el join implícito (cruce + condición WHERE) entre dos tablas.

## Slide 24
Título "Alias: AS". Arriba, tablas Satélite y Aterrizaje completas. Abajo, ejemplo:
```sql
SELECT S.planeta AS splaneta
FROM Satélite S, Aterrizaje A
WHERE S.planeta = A.planeta
```
Resultado (recuadro celeste): columna splaneta con 4 filas repetidas "Júpiter". Muestra alias de tabla (S, A) y alias de columna (AS splaneta).

## Slide 25
Título "Alias: tablas". Arriba, tabla Satélite completa. Abajo, ejemplo de self-join usando alias de tabla:
```sql
SELECT s1.nombre AS nombre1,
       s2.nombre AS nombre2
FROM Satélite s1, Satélite s2
WHERE s1.año=s2.año
AND s1.nombre<s2.nombre
```
Resultado (recuadro celeste), columnas nombre1/nombre2: Calisto-Europa, Calisto-Ganímedes, Calisto-Io, Europa-Ganímedes, Europa-Io, Ganímedes-Io. (satélites descubiertos el mismo año, sin repetir pares).

## Slide 26
Título "Unión (distinta): UNIÓN". Arriba, tablas Planeta y Satélite completas. Abajo, ejemplo:
```sql
SELECT nombre
FROM Planeta
UNION
SELECT nombre
FROM Satélite
```
Resultado (recuadro celeste), columna nombre: Urano, Venus, Mercurio, Io, Júpiter, "…" (indica que continúa, unión sin duplicados de nombres de planetas y satélites).

## Slide 27
Título "Unión (con alias): UNION + AS". Arriba, tablas Planeta y Satélite completas. Abajo, ejemplo:
```sql
SELECT nombre AS planeta
FROM Planeta
UNION
SELECT planeta
FROM Satélite
```
Resultado (recuadro celeste), columna planeta con 8 valores: Urano, Venus, Mercurio, Tierra, Saturno, Neptuno, Júpiter, Marte (unión distinta de nombres de planetas propios y de los planetas donde hay satélites, usando AS para igualar nombres de columna).

## Slide 28
Título "Unión (bruta): UNION ALL". Arriba, tablas Planeta y Satélite completas. Abajo, ejemplo:
```sql
SELECT nombre AS planeta
FROM Planeta
UNION ALL
SELECT planeta
FROM Satélite
```
Resultado (recuadro celeste), columna planeta: Urano, Neptuno, Neptuno, Mercurio, Saturno, Saturno, "…" — con duplicados (UNION ALL no elimina repetidos, a diferencia de UNION).

## Slide 29
Título "Diferencia: EXCEPT". Arriba, tablas Planeta y Satélite completas. Abajo, ejemplo:
```sql
SELECT nombre AS planeta
FROM Planeta
WHERE dist > 1.00
EXCEPT
SELECT planeta
FROM Satélite
```
Resultado (recuadro celeste): columna planeta con 2 filas: Marte, Urano (planetas con dist>1.00 que NO tienen satélites en la tabla Satélite).

## Slide 30
Título "Intersección: INTERSECT". Arriba, tablas Planeta y Satélite completas. Abajo, ejemplo:
```sql
SELECT nombre AS planeta
FROM Planeta
WHERE dist > 1.00
INTERSECT
SELECT planeta
FROM Satélite
```
Resultado (recuadro celeste): columna planeta con 3 filas: Saturno, Júpiter, Neptuno (planetas con dist>1.00 que SÍ tienen satélites).

## Slide 31
Título "Patrones simples: LIKE". Arriba, tabla Planeta completa. Abajo, ejemplo:
```sql
SELECT nombre
FROM Planeta
WHERE nombre LIKE 'M%'
```
Resultado (recuadro celeste): Mercurio, Marte (nombres que empiezan con "M", % es comodín de cualquier secuencia).

## Slide 32
Título "Patrones simples: NOT LIKE". Arriba, tabla Planeta completa. Abajo, ejemplo:
```sql
SELECT nombre
FROM Planeta
WHERE nombre NOT LIKE '%no'
AND dist > 1.00
```
Resultado (recuadro celeste): Júpiter, Marte (planetas con dist>1.00 cuyo nombre no termina en "no", excluye Urano/Neptuno/Saturno... nota: Saturno termina en "no" también).

## Slide 33
Título "Abreviatura: IN". Arriba, tabla Aterrizaje completa. Abajo, ejemplo:
```sql
SELECT planeta
FROM Aterrizaje
WHERE país IN ('EEUU','ESA')
```
Resultado (recuadro celeste): Mercurio, Venus, Marte, Marte, Júpiter (aterrizajes de naves de EEUU o ESA).

## Slide 34
Título "Abreviatura: BETWEEN". Arriba, tabla Aterrizaje completa. Abajo, ejemplo:
```sql
SELECT planeta
FROM Aterrizaje
WHERE año BETWEEN 1971 AND 1978
```
Resultado (recuadro celeste): Marte, Marte, Venus (aterrizajes con año entre 1971 y 1978 inclusive).

## Slide 35
Slide de transición/resumen visual: gran iceberg fotográfico, la parte visible sobre el agua rotulada con viñetas de temas "ya vistos" (SELECT, FROM, WHERE · ORDER BY · JOIN (simple) · UNION, INTERSECT, EXCEPT · LIKE · IN, BETWEEN) y la palabra "SQL" grande escrita sobre el hielo bajo el agua; en la parte sumergida (bajo el agua), viñetas de temas "que faltan por ver" (Más tipos de JOIN · Nulos · Consultas anidadas · Agregación). Metáfora visual de que lo visto es solo "la punta del iceberg" de SQL.

## Slide 36
Slide de transición de sección, título "Producto cruz" en azul, ilustración decorativa del ninja/mago con lápiz sentado en trono (misma ilustración recurrente de las slides de transición).

## Slide 37
Título "Cruz: CROSS JOIN". Arriba, tablas Satélite y Aterrizaje completas (con columna renombrada "año-des" en Satélite). Abajo, dos formas equivalentes de escribir el producto cartesiano:
```sql
SELECT nombre, S.planeta, nave
FROM Satélite S CROSS JOIN Aterrizaje
```
y
```sql
SELECT nombre, S.planeta, nave
FROM Satélite S, Aterrizaje
```
Resultado (recuadro celeste), tabla nombre/S.planeta/nave con filas de ejemplo y puntos suspensivos indicando continuación: Luna-Tierra-Messenger, "…", Luna-Tierra-Galileo, Ganímedes-Júpiter-Messenger, "…", Ganímedes-Júpiter-Galileo, "…" (producto cartesiano completo, 7×7=49 filas).

## Slide 38
Slide de transición de sección, título "Joins internos" en azul, misma ilustración decorativa del ninja/mago con lápiz.

## Slide 39
Título "Cruzar tablas: JOIN". Contenido idéntico al de la slide 23 (mismas tablas Planeta/Aterrizaje, misma consulta con WHERE nombre=planeta AND dist>1.00 AND año>=2000, mismo resultado Marte 2003 Beagle 2 / Júpiter 2003 Galileo) — repetida aquí para introducir formalmente el concepto de JOIN dentro de la sección "Joins internos".

## Slide 40
Título "Cruzar tablas: EQUI JOIN". Arriba, tablas Planeta y Aterrizaje completas. Recuadro amarillo con borde punteado: "EQUI JOINS usan sólo '=' en el JOIN". Dos formas equivalentes de consulta:
```sql
SELECT nave, nombre, dist, año
FROM Planeta, Aterrizaje
WHERE nombre = planeta
```
y (sintaxis JOIN...ON explícita)
```sql
SELECT nave, nombre, dist, año
FROM Planeta JOIN Aterrizaje
ON nombre = planeta
```
Resultado (recuadro celeste), tabla nave/nombre/dist/año con 7 filas: Messenger-Mercurio-0,39-2015; Venera 3-Venus-0,72-1966; Pioneer-Venus-0,72-1978; Mars 2 lander-Marte-1,52-1971; Viking 1-Marte-1,52-1976; Beagle 2-Marte-1,52-2003; Galileo-Júpiter-5,20-2003.

## Slide 41
Título "Cruzar tablas: JOIN". Misma consulta y tablas que la slide 23/39. Recuadro gris con borde punteado formula la pregunta: "¿Esta consulta es un EQUI JOIN?". Debajo, recuadro verde con borde punteado responde: "¡Sí! Sólo la condición del join cuenta." (aclara que las condiciones adicionales de filtro AND dist>1.00 AND año>=2000 no afectan la clasificación como equi-join, solo importa que la condición de unión use "=").

## Slide 42
Título "Cruzar tablas: JOIN USING". Arriba, tablas Satélite y Aterrizaje completas. Ejemplo:
```sql
SELECT nombre, planeta
FROM Satélite
JOIN Aterrizaje USING (planeta)
```
Resultado (recuadro celeste): Ganímedes-Júpiter, Calisto-Júpiter, Europa-Júpiter, Io-Júpiter. Recuadro amarillo con borde punteado: "Se puede usar JOIN USING cuando todos los atributos del JOIN tengan el mismo nombre".

## Slide 43
Título "Cruzar tablas: NATURAL JOIN". Arriba, tablas Satélite y Aterrizaje completas. Recuadro amarillo con borde punteado: "Un EQUI-JOIN sobre los atributos que las tablas comparten (por pareja con AND)." Dos consultas equivalentes:
```sql
SELECT nombre, planeta
FROM Satélite
NATURAL JOIN Aterrizaje
```
y
```sql
SELECT nombre, planeta
FROM Satélite
JOIN Aterrizaje
    USING (planeta, año)
```
Resultado (recuadro celeste): tabla vacía (solo encabezados nombre/planeta) — al unir automáticamente por TODOS los atributos compartidos (planeta Y año), no hay coincidencias, ya que los años de descubrimiento de satélites no coinciden con los años de aterrizajes. Ilustra el peligro de NATURAL JOIN cuando hay más columnas compartidas de las esperadas.

## Slide 44
Título "Cruzar tablas: SELF JOIN". Arriba, tabla Aterrizaje completa. Recuadro amarillo con borde punteado: "Un JOIN sobre la tabla misma". Ejemplo con dos alias de la misma tabla:
```sql
SELECT A1.planeta, A2.planeta
FROM Aterrizaje A1
   JOIN Aterrizaje A2
     ON A1.año = A2.año
        AND A1.planeta <> A2.planeta
```
(con una flecha señalando la condición ON). Resultado (recuadro celeste), columnas A1.planeta/A2.planeta: Marte-Júpiter, Júpiter-Marte (aterrizajes del mismo año 2003 en planetas distintos).

## Slide 45
Título "Cruzar tablas: INNER JOIN". Arriba, tablas Planeta y Aterrizaje completas. Recuadro amarillo con borde punteado: "INNER JOIN por defecto …". Dos consultas equivalentes (nota: la primera tiene un typo "Planet" en vez de "Planeta"):
```sql
SELECT nave, nombre, dist, año
FROM Planet INNER JOIN Aterrizaje
ON nombre = planeta
```
y
```sql
SELECT nave, nombre, dist, año
FROM Planeta JOIN Aterrizaje
ON nombre = planeta
```
Resultado (recuadro celeste): mismas 7 filas que la slide 40 (Messenger-Mercurio-0,39-2015, etc.) — muestra que JOIN simple es equivalente a INNER JOIN (JOIN es INNER JOIN por defecto).

## Slide 46
Slide de transición de sección, título "Joins Externos" en azul, misma ilustración decorativa del ninja/mago con lápiz sentado en trono.

## Slide 47
Título "Joins Externos". Arriba, tablas Planeta y Aterrizaje completas. Recuadro gris con borde punteado plantea la pregunta motivadora: "¿Todos los planetas (y sus aterrizajes sí hay datos disponibles)?" — introduce la necesidad de joins externos (outer joins) para no perder filas sin coincidencia.

## Slide 48
Título "Joins Externos: LEFT [OUTER] JOIN". Arriba, tablas Planeta y Aterrizaje completas. Recuadro amarillo con borde punteado: "Se mantienen las tuplas de la izquierda si no hay datos desde la derecha". Dos consultas equivalentes:
```sql
SELECT nave, nombre, dist, año
FROM Planeta LEFT JOIN Aterrizaje
ON nombre = planeta
```
y
```sql
SELECT nave, nombre, dist, año
FROM Planeta LEFT OUTER JOIN Aterrizaje
ON nombre = planeta
```
Resultado (recuadro celeste): las 7 filas del inner join (Messenger-Mercurio..., Galileo-Júpiter) MÁS 4 filas adicionales con nave=⊥ (nulo) para los planetas sin aterrizaje: ⊥-Tierra-1,00-⊥, ⊥-Saturno-9,54-⊥, ⊥-Urano-19,19-⊥, ⊥-Neptuno-30,07-⊥.

## Slide 49
Título "Joins Externos: RIGHT [OUTER] JOIN". Arriba, mismas tablas. Recuadro amarillo: "Se mantienen las tuplas de la derecha si no hay datos desde la izquierda". Dos consultas equivalentes:
```sql
SELECT nave, nombre, dist, año
FROM Aterrizaje RIGHT JOIN Planeta
ON nombre = planeta
```
y
```sql
SELECT nave, nombre, dist, año
FROM Aterrizaje RIGHT OUTER JOIN Planeta
ON nombre = planeta
```
Resultado (recuadro celeste): idéntico al de la slide 48 (mismas 11 filas, incluyendo las 4 con nave=⊥ para Tierra, Saturno, Urano, Neptuno) — ilustra que invertir el orden de las tablas con RIGHT JOIN produce el mismo resultado que LEFT JOIN con el orden original.

## Slide 50
Título "Joins Externos: FULL OUTER JOIN". Arriba, tablas Satélite y Aterrizaje completas. Recuadro amarillo: "Se mantienen las tuplas de la derecha y la izquierda". Ejemplo:
```sql
SELECT planeta, nave, nombre AS satélite
FROM Satélite FULL OUTER JOIN Aterrizaje
USING (planeta)
```
Resultado (recuadro celeste), columnas planeta/nave/satélite, 13 filas: Tierra-⊥-Luna; Júpiter-Galileo-Ganímedes; Júpiter-Galileo-Calisto; Júpiter-Galileo-Europa; Júpiter-Galileo-Io; Saturno-⊥-Titán; Neptuno-⊥-Tritón; Mercurio-Messenger-⊥; Venus-Venera 3-⊥; Venus-Pioneer-⊥; Marte-Mars 2 lander-⊥; Marte-Viking 1-⊥; Marte-Beagle 2 lander-⊥ (nota: aquí aparece como "Beagle 2 lander", posible fusión visual/typo respecto a "Beagle 2"). Combina filas con y sin coincidencia de ambos lados.

## Slide 51
Título "Join Interno versus Joins Externos". Cuatro diagramas de Venn con dos círculos I (izquierda) y D (derecha):
- [INNER] JOIN: solo intersección resaltada (naranja).
- LEFT [OUTER] JOIN: círculo I completo (dorado) + intersección, D restante en azul/lila.
- RIGHT [OUTER] JOIN: círculo D completo (dorado) + intersección, I restante en rosa.
- FULL OUTER JOIN: ambos círculos completos en dorado.

## Slide 52
Slide de transición de sección, título "Valores Nulos" en azul, ilustración decorativa del ninja/mago con lápiz sentado en trono. Enlace https://es.wikipedia.org/wiki/Null_(SQL). Cita: Capítulo 5.6 | Ramakrishnan / Gehrke.

## Slide 53
Título "Nulos". Muestra los distintos símbolos usados para representar nulo: ⊥, ∅, ⌐ (guión bajo estilizado), ∅ (circulo tachado), NULL (en rojo, resaltado). Recuadro amarillo: "DESCONOCIDO o INAPLICABLE (No significa FALSO)".

## Slide 54
Título "Nulos: IS NULL". Tabla Satélite completa (con Luna teniendo descubridor=⊥, año=⊥). Código:
```sql
SELECT nombre
FROM Satélite
WHERE descubridor IS NULL
```
Resultado (recuadro celeste): una fila, nombre=Luna.

## Slide 55
Título "Nulos: IS NOT NULL". Misma tabla Satélite. Código:
```sql
SELECT nombre
FROM Satélite
WHERE descubridor IS NOT NULL
```
Resultado (recuadro celeste): 6 filas — Ganímedes, Calisto, Europa, Io, Titán, Tritón (todas excepto Luna).

## Slide 56
Título "Comparación con nulos". Misma tabla Satélite. Código:
```sql
SELECT nombre
FROM Satélite
WHERE año > 1800
```
Resultado (recuadro celeste): una fila, nombre=Tritón (único satélite con año>1800; Luna con año=⊥ queda excluido porque la comparación con nulo da desconocido).

## Slide 57
Título "Comparación con nulos". Misma tabla Satélite. Recuadro amarillo: "¡El nulo en la consulta y el nulo en los datos son distintos!". Código:
```sql
SELECT nombre
FROM Satélite
WHERE año = NULL
```
Resultado (recuadro celeste): tabla vacía (sin filas) — comparar con `= NULL` nunca es verdadero, ni siquiera para filas con año nulo; hay que usar IS NULL.

## Slide 58
Título "Comparación con nulos". Tabla de verdad de lógica de tres valores (VERDADERO/FALSO/DESCONOCIDO) con columnas p, q, p OR q, p AND q, p = q. Filas con p y q ambos conocidos ya resueltas (ej. VERDADERO OR FALSO = VERDADERO, FALSO AND FALSO = FALSO, FALSO = FALSO → VERDADERO). Las filas donde p o q son DESCONOCIDO tienen las columnas p OR q, p AND q, p = q en blanco con "???" en un recuadro punteado gris — pregunta al alumno cómo se completarían. Texto: "Cuando no importa el valor del desconocido, el resultado se mantiene. Cuando importa el valor del desconocido, el resultado es desconocido."

## Slide 59
Repite el título "Comparación con nulos" y la misma tabla de verdad de la slide 58, ahora completa: filas con DESCONOCIDO resueltas explícitamente, por ejemplo VERDADERO OR DESCONOCIDO = VERDADERO (el resultado no depende del desconocido), FALSO OR DESCONOCIDO = DESCONOCIDO, VERDADERO AND DESCONOCIDO = DESCONOCIDO, FALSO AND DESCONOCIDO = FALSO, y p=q con cualquier DESCONOCIDO = DESCONOCIDO. Mismo texto explicativo al pie.

## Slide 60
Título "Nulos: COALESCE". Tabla Satélite completa. Recuadro amarillo: "Elegir el primer valor que no sea NULL". Código:
```sql
SELECT nombre, COALESCE(año,0) AS _año
FROM Satélite
ORDER BY _año
```
Resultado (recuadro celeste), columnas nombre/_año: Luna-0, Ganímedes-1610, Calisto-1610, Europa-1610, Io-1610, Titán-1655, Tritón-1846 — COALESCE sustituye el nulo de Luna por 0.

## Slide 61
Título "Ejercicio interactivo". Tablas Planeta y Satélite completas. Recuadro: "¿Qué resultados devolverá la consulta?". Código (recuadro verde):
```sql
SELECT nombre
FROM Planeta
WHERE EXISTS
  ( SELECT descubridor
    FROM Satélite
    WHERE Planeta.nombre = planeta
  )
```
Resultado aún no mostrado (recuadro celeste vacío).

## Slide 62
Repite el ejercicio de la slide 61 con el mismo código y tablas, ahora mostrando el resultado (recuadro celeste): columna nombre con Tierra, Júpiter, Saturno, Neptuno — planetas que tienen al menos un satélite registrado.

## Slide 63
Slide de transición de sección, título "Consultas anidadas" en azul, ilustración decorativa del ninja/mago con lápiz sentado en trono. Cita: Capítulo 5.4 | Ramakrishnan / Gehrke.

## Slide 64
Título "Consultas Anidadas: WHERE/IN". Tablas Planeta y Aterrizaje completas. Código:
```sql
SELECT nave, planeta
FROM Aterrizaje
WHERE planeta IN
  ( SELECT nombre
    FROM Planeta
    WHERE grav > 9.8 )   -- Subconsulta (recuadro amarillo punteado)
  AND año > 2000
```
Resultado (recuadro celeste): una fila, nave=Galileo, planeta=Júpiter. Imagen decorativa de una persona (meme, "Xzibit"-estilo).

## Slide 65
Título "Consultas Anidadas: WHERE/IN". Mismas tablas. Pregunta en recuadro: "¿Necesitamos una consulta anidada aquí?". Muestra reescritura equivalente sin subconsulta, usando join directo:
```sql
SELECT nave, P.planeta
FROM Aterrizaje A, Planeta P
WHERE A.planeta=P.nombre
  AND P.grav > 9.8
  AND año > 2000
```
Nota: la columna se llama "P.planeta" pero corresponde a P.nombre — posible inconsistencia menor. Imagen decorativa (Danny DeVito, meme).

## Slide 66
Título "Consultas Anidadas: WHERE/NOT IN". Tablas Planeta y Aterrizaje completas. Código:
```sql
SELECT nave, planeta
FROM Aterrizaje
WHERE planeta NOT IN
  ( SELECT nombre
    FROM Planeta
    WHERE grav > 9.8 )
  AND año > 2000
```
Resultado (recuadro celeste): dos filas, Beagle 2-Marte, Messenger-Mercurio.

## Slide 67
Título "Consultas Anidadas: WHERE/NOT IN". Mismas tablas. Código extendido con subconsulta anidada dos niveles:
```sql
SELECT nave, planeta
FROM Aterrizaje
WHERE planeta NOT IN
  ( SELECT nombre
    FROM Planeta
    WHERE grav > 9.8 OR planeta IN
      ( SELECT planeta
        FROM Aterrizaje
        WHERE país = 'ESA'
      )
  )
  AND año > 2000
```
Resultado (recuadro celeste): una fila, Messenger-Mercurio (Beagle 2/Marte queda excluido porque Marte tuvo un aterrizaje de país='ESA'). Imagen decorativa (meme duplicado de la persona de la slide 64).

## Slide 68
Título "Consultas Anidadas: WHERE/EXISTS". Tablas Planeta y Aterrizaje completas. Código:
```sql
SELECT nombre, dist
FROM Planeta
WHERE EXISTS
  ( SELECT *
    FROM Aterrizaje
    WHERE año >= 2000 AND nombre = planeta )
ORDER BY dist DESC
```
(el recuadro punteado amarillo resalta "nombre" en la condición interna, señalando la correlación con la tabla externa). Resultado (recuadro celeste): 3 filas ordenadas por dist descendente — Júpiter-5,20, Marte-1,52, Mercurio-0,39. Recuadro amarillo: "Correlación: La subconsulta depende de la consulta exterior".

## Slide 69
Título "Consultas Anidadas: WHERE/NOT EXISTS". Mismas tablas. Código:
```sql
SELECT nombre, dist
FROM Planeta
WHERE NOT EXISTS
  ( SELECT *
    FROM Aterrizaje
    WHERE año >= 2000 AND nombre = planeta )
ORDER BY dist DESC
```
Resultado (recuadro celeste): 5 filas ordenadas por dist descendente — Neptuno-30,07, Urano-19,19, Saturno-9,54, Tierra-1,00, Venus-0,72 (planetas sin aterrizaje reciente).

## Slide 70
Título "Consultas Anidadas: WHERE/(NOT) UNIQUE". Mismas tablas. Código:
```sql
SELECT nombre, dist
FROM Planeta
WHERE UNIQUE
  ( SELECT *
    FROM Aterrizaje
    WHERE nombre = planeta )
ORDER BY dist DESC
```
Resultado (recuadro celeste): 6 filas ordenadas por dist descendente — Neptuno-30,07, Urano-19,19, Saturno-9,54, Júpiter-5,20, Tierra-1,00, Mercurio-0,39 (planetas con 0 o 1 aterrizajes). Recuadro amarillo: "UNIQUE (no suportado por Postgres ☹): 0 o 1 resultados".

## Slide 71
Título "Consultas Anidadas: WHERE/ANY (o SOME)". Tablas Planeta y Aterrizaje completas. Código:
```sql
SELECT nombre
FROM Planeta P1
WHERE P1.grav > ANY
  ( SELECT P2.grav
    FROM Planeta P2
    WHERE P2.dist > 1.00 )
ORDER BY P1.dist DESC
```
Resultado (recuadro celeste): 6 filas — Neptuno, Urano, Saturno, Júpiter, Tierra, Venus. Recuadro amarillo: "ANY y SOME son sinónimos".

## Slide 72
Título "Consultas Anidadas: WHERE/ALL". Mismas tablas. Código:
```sql
SELECT nombre
FROM Planeta P1
WHERE P1.grav > ALL
  ( SELECT P2.grav
    FROM Planeta P2
    WHERE P2.dist < 1.00 )
ORDER BY P1.dist DESC
```
Resultado (recuadro celeste): 4 filas — Neptuno, Saturno, Júpiter, Tierra.

## Slide 73
Título "Ejercicio interactivo". Tablas Planeta y Aterrizaje completas. Pregunta: "¿Los naves que han aterrizado en un planeta con (un) anillo(s)?". Resultado ya mostrado (recuadro celeste): una fila, nave=Galileo. Código aún oculto (recuadro naranja vacío).

## Slide 74
Repite el ejercicio de la slide 73, ahora mostrando el código (recuadro verde):
```sql
SELECT nave
FROM Aterrizaje
WHERE planeta IN
  ( SELECT nombre
    FROM Planeta
    WHERE anillo IS TRUE
  )
```
Resultado (recuadro celeste): nave=Galileo.

## Slide 75
Título "Ejercicio interactivo". Tabla Aterrizaje completa. Pregunta: "¿Los aterrizajes de la URRS que se hicieron antes que el primer aterrizaje de los EEUU?". Resultado ya mostrado: 2 filas — Venera 3 (Venus, URRS, 1966), Mars 2 lander (Marte, URRS, 1971). Código aún oculto.

## Slide 76
Repite el ejercicio de la slide 75 mostrando el código (recuadro verde):
```sql
SELECT *
FROM Aterrizaje A1
WHERE A1.país = 'URRS'
AND A1.año < ALL
  ( SELECT A2.año
    FROM Aterrizaje A2
    WHERE A2.país = 'EEUU'
  )
```
Resultado (recuadro celeste): mismas 2 filas de la slide 75.

## Slide 77
Título "Ejercicio interactivo". Tabla Aterrizaje completa. Pregunta: "¿Los primeros aterrizajes de cada país?". Resultado ya mostrado: 3 filas — Beagle 2 (Marte, ESA, 2003), Venera 3 (Venus, URRS, 1966), Viking 1 (Marte, EEUU, 1976). Código aún oculto.

## Slide 78
Repite el ejercicio de la slide 77 mostrando el código (recuadro verde):
```sql
SELECT *
FROM Aterrizaje A1
WHERE A1.año <= ALL
  ( SELECT A2.año
    FROM Aterrizaje A2
    WHERE A2.país = A1.país
  )
```
Resultado (recuadro celeste): mismas 3 filas de la slide 77.

## Slide 79
Slide de transición decorativa, "Más consultas anidadas" en azul. Imagen decorativa: fotografía de unas manos pintando/dibujando en un cuaderno de bocetos con efecto de infinito recursivo (representa recursión/anidamiento). Mascota ninja con lápiz al costado.

## Slide 80
Título "Consultas Anidadas: Valor". Tabla Planeta completa. Código:
```sql
SELECT nombre
FROM Planeta P1
WHERE P1.grav >
  ( SELECT P2.grav
    FROM Planeta P2
    WHERE P2.nombre = 'Tierra' )
ORDER BY P1.dist DESC
```
Resultado (recuadro celeste): 2 filas — Neptuno, Júpiter. Recuadro amarillo: "La subconsulta tiene que devolver un valor y una columna –si no…" (frase incompleta, continúa en siguiente slide).

## Slide 81
Título "Consultas Anidadas: Valor" (título en rojo, indicando caso de error). Misma tabla Planeta. Código:
```sql
SELECT nombre
FROM Planeta P1
WHERE P1.grav >
  ( SELECT P2.grav
    FROM Planeta P2
    WHERE P2.temp > 300 )
ORDER BY P1.dist DESC
```
Resultado (recuadro celeste): `Error: La tabla devolió más de una fila` — la subconsulta escalar devuelve múltiples filas (Mercurio y Venus tienen temp>300), lo cual no es válido para una comparación de valor único.

## Slide 82
Título "Consultas Anidadas: Valor" (en rojo). Misma tabla Planeta. Código:
```sql
SELECT nombre
FROM Planeta P1
WHERE P1.grav >
  ( SELECT P2.grav, P2.nombre
    FROM Planeta P2
    WHERE P2.nombre = 'Tierra' )
ORDER BY P1.dist DESC
```
Resultado (recuadro celeste): `Error: La tabla devolió más de una columna` — la subconsulta devuelve 2 columnas cuando debe devolver solo 1.

## Slide 83
Título "Consultas Anidadas: Fila". Tabla Satélite completa. Código con comparación de tupla (row constructor):
```sql
SELECT S1.nombre, S1.planeta
FROM Satélite S1
WHERE (S1.año, S1.descubridor) =
  ( SELECT S2.año, S2.descubridor
    FROM Satélite S2
    WHERE S2.nombre = 'Ío' )
```
Resultado (recuadro celeste): 4 filas — Io-Júpiter, Calisto-Júpiter, Europa-Júpiter, Ganímedes-Júpiter (todos los satélites con mismo año/descubridor que Ío).

## Slide 84
Título "Consultas Anidadas: Fila" (en rojo). Misma tabla Satélite. Código:
```sql
SELECT S1.nombre, S1.planeta
FROM Satélite S1
WHERE (S1.año, S1.descubridor) =
  ( SELECT S2.año, S2.descubridor
    FROM Satélite S2
    WHERE S2.planeta = 'Júpiter' )
```
Resultado (recuadro celeste): `Error: La subconsulta devuelve demasiadas columnas` (mensaje sospechoso de ser copy-paste; en contexto real correspondería a "demasiadas filas", dado que hay 4 satélites de Júpiter con distinto año/descubridor... aunque en los datos todos comparten 1610/Galileo Galilei — de cualquier modo el mensaje mostrado en la slide es el indicado).

## Slide 85
Título "Consultas Anidadas: Fila" (en rojo). Misma tabla Satélite. Código idéntico al de la slide 84. Resultado (recuadro celeste): `Error: La tabla devolvió más de una fila`.

## Slide 86
Título "Consultas Anidadas: Fila". Misma tabla Satélite. Código con IN en vez de =:
```sql
SELECT S1.nombre, S1.planeta
FROM Satélite S1
WHERE (S1.año, S1.descubridor) IN
  ( SELECT S2.año, S2.descubridor
    FROM Satélite S2
    WHERE S2.planeta = 'Júpiter' )
```
Resultado (recuadro celeste): 4 filas — Io-Júpiter, Calisto-Júpiter, Europa-Júpiter, Ganímedes-Júpiter. Usar IN en vez de = evita el error porque acepta múltiples filas de comparación.

## Slide 87
Título "Consultas Anidadas: FROM". Tablas Planeta y Aterrizaje completas. Código con subconsulta en el FROM (tabla derivada):
```sql
SELECT nombre, grav
FROM
  ( SELECT A1.planeta
    FROM Aterrizaje A1, Aterrizaje A2
    WHERE A1.planeta=A2.planeta
    AND A1.país<>A2.país ) Multi,
  Planeta
WHERE nombre=Multi.planeta
  AND grav > 8.0
ORDER BY grav
```
Recuadro amarillo: "El alias Multi es obligatorio". Resultado (recuadro celeste): 2 filas idénticas — Venus-8.9, Venus-8.9 (aparece duplicado por el self-join sin DISTINCT, al combinar pares de países distintos que aterrizaron en Venus).

## Slide 88
Slide de transición de sección, título "Agregación" en azul, ilustración decorativa del ninja/mago con lápiz sentado en trono. Cita: Capítulo 5.5 | Ramakrishnan / Gehrke.

## Slide 89
Título "Operadores de agregación". Lista de funciones: COUNT([DISTINCT] A), SUM([DISTINCT] A), AVG([DISTINCT] A), MAX(A), MIN(A).

## Slide 90
Título "Agregación: COUNT". Tabla Aterrizaje completa. Código:
```sql
SELECT COUNT(planeta) AS conteo
FROM Aterrizaje
```
Resultado (recuadro celeste): conteo=7.

## Slide 91
Título "Agregación: COUNT (DISTINCT afuera)". Misma tabla Aterrizaje. Código con DISTINCT mal ubicado (resaltado en punteado naranja, fuera de los paréntesis de COUNT):
```sql
SELECT DISTINCT COUNT(planeta) AS conteo
FROM Aterrizaje
```
Resultado (recuadro celeste): conteo=7 — el DISTINCT aplicado al resultado final no cambia nada porque solo hay una fila de salida (agregación total).

## Slide 92
Título "Agregación: COUNT DISTINCT". Misma tabla Aterrizaje. Código con DISTINCT dentro del COUNT:
```sql
SELECT COUNT(DISTINCT planeta) AS conteo
FROM Aterrizaje
```
Resultado (recuadro celeste): conteo=4 — cuenta planetas únicos (Mercurio, Venus, Marte, Júpiter).

## Slide 93
Título "Agregación: COUNT(*)". Misma tabla Aterrizaje. Código:
```sql
SELECT COUNT(*) AS conteo
FROM Aterrizaje
```
Resultado (recuadro celeste): conteo=7 — cuenta todas las filas sin importar nulos en columnas específicas.

## Slide 94
Título "Agregación: AVG". Misma tabla Aterrizaje. Código:
```sql
SELECT AVG(año) AS promedio
FROM Aterrizaje
```
Dos resultados comparados: recuadro celeste "Postgres" → promedio=1987,429 (decimales completos); recuadro celeste inferior sin etiqueta → promedio=1987 (truncado, comportamiento de otro sistema). Recuadro amarillo: "Depende del sistema".

## Slide 95
Título "Agregación: AVG DISTINCT". Misma tabla. Código:
```sql
SELECT AVG(DISTINCT año) AS promedio
FROM Aterrizaje
```
Tres resultados comparados: "Postgres" → promedio=1984,833; otro recuadro → promedio=1984; un tercer recuadro sin etiqueta → promedio=1985 — ilustra que distintos sistemas redondean/truncan diferente. Recuadro amarillo: "Depende del sistema".

## Slide 96
Título "Agregación: AVG (con casting)". Misma tabla. Código:
```sql
SELECT AVG(CAST(año AS FLOAT)) AS promedio
FROM Aterrizaje
```
Resultado (recuadro celeste): promedio=1987,429 — forzar tipo FLOAT asegura precisión decimal independientemente del sistema.

## Slide 97
Título "Agregación: MIN". Misma tabla. Código:
```sql
SELECT MIN(año) AS mínimo
FROM Aterrizaje
```
Resultado (recuadro celeste): columna "año"=1966 (nota: la columna resultado se etiqueta "año" en la captura pese al alias "mínimo" en el código — posible inconsistencia visual del render).

## Slide 98
Título "Agregación: MIN". Misma tabla. Código con columna adicional sin agregar ni agrupar:
```sql
SELECT MIN(año) AS mínimo, planeta
FROM Aterrizaje
```
Resultado (recuadro celeste): `Error: Si hay un operador de agregación solo se puede devolver el resultado de ese operador (o de un operador (GROUP BY))` — ilustra la regla de que columnas no agregadas requieren GROUP BY.

## Slide 99
Título "Agregación: MIN". Misma tabla. Código con subconsulta correlacionada para obtener la fila completa del mínimo:
```sql
SELECT A1.planeta, A1.año
FROM Aterrizaje A1
WHERE A1.año =
  ( SELECT MIN(A2.año)
    FROM Aterrizaje A2
  )
```
Resultado (recuadro celeste): planeta=Venus, año=1966.

## Slide 100
Título "Agregación por planeta: explícitamente". Misma tabla. Código que construye manualmente (con UNION, mostrado parcialmente/cortado en la slide) el conteo de aterrizajes por planeta usando subconsultas explícitas para cada valor:
```sql
SELECT A1.planeta, conteo
FROM Aterrizaje A1,
  ( SELECT COUNT(*) AS conteo
    FROM Aterrizaje A2
    WHERE A2.planeta = 'Mercurio'
  ) Mercurio
WHERE A1.planeta = 'Mercurio'
UNION
SELECT A1.planeta, conteo
FROM Aterrizaje A1,
  ( SELECT COUNT(*) AS conteo
    ...
```
(código continúa fuera de la slide, cortado). Resultado parcial (recuadro celeste): planeta/conteo — Mercurio-1, Venus-2, "..."/"..." indicando que continuaría para Marte y Júpiter. Ilustra lo tedioso de calcular agregaciones por grupo sin GROUP BY, motivando la siguiente sección.

## Slide 101
Título "Agregación por planeta: GROUP BY". Plantilla genérica de sintaxis en bloque de código:
```sql
SELECT
  column_1,
  column_2,
  aggregate_function(column_3)
FROM
  table_name
GROUP BY
  column_1,
  column_2;
```

## Slide 102
Título "Agregación: GROUP BY". Diagrama/captura ilustrativa (w3resource.com) explicando el concepto con una tabla de ejemplo `agents` no relacionada al esquema de planetas: columnas AGENT_NAME/WORKING_AREA con 12 filas (Alex-London, Subbarao-Bangalore, Benjamin-Hampshair, etc.). Código:
```sql
SELECT working_area, COUNT(*)
FROM agents
GROUP BY working_area;
```
Diagrama con líneas de colores conectando cada agente a su área de trabajo, mostrando cómo se agrupan. Tabla resultado: WORKING_AREA/COUNT(*) — San Jose-1, Torento-1, London-2, Hampshair-1, New York-1, Brisban-1, Bangalore-3, Chennai-1, Mumbai-1. Texto "the working_area have been grouped and appearing once".

## Slide 103
Título "Agregación: GROUP BY". Segundo diagrama ilustrativo (w3resource.com) con tabla `customer` (CUST_COUNTRY/OPENING_AMT), ~14 filas para Australia/Canada/India (y más). Código:
```sql
SELECT cust_country, SUM(opening_amt), COUNT(cust_country)
FROM customer
GROUP BY cust_country;
```
Diagrama muestra flechas "COUNT cust_country for each group" y "SUM opening_amt for each group" convergiendo en la tabla resultado: CUST_COUNTRY/SUM(OPENING_AMT)/COUNT(CUST_COUNTRY) — India-73000-10, USA-18000-4, Australia-19000-3, Canada-25000-3, UK-26000-5. Fuente: w3resource.com/sql/aggregate-functions/count-having.php.

## Slide 104
Título "Agregación por planeta: GROUP BY". Tabla Aterrizaje completa. Código:
```sql
SELECT planeta, COUNT(*) AS conteo
FROM Aterrizaje
GROUP BY planeta
```
Resultado (recuadro celeste): Mercurio-1, Venus-2, Marte-3, Júpiter-1.

## Slide 105
Título "Agregación por planeta: GROUP BY/HAVING". Misma tabla. Código:
```sql
SELECT planeta, COUNT(*) AS conteo
FROM Aterrizaje
GROUP BY planeta
HAVING MAX(año)<2000
```
Resultado (recuadro celeste): Venus-2 (único planeta cuyo aterrizaje más reciente es anterior a 2000).

## Slide 106
Título "Agregación por planeta: GROUP BY/HAVING". Plantilla genérica de sintaxis:
```sql
SELECT
  column_1,
  aggregate_function(column_3)
FROM
  table_name
GROUP BY
  column_1,
HAVING
  condition;
```

## Slide 107
Título "Agregación: GROUP BY/HAVING". Diagrama ilustrativo (w3resource.com) con tabla `agents` (AGENT_NAME/COMMISSION, 12 filas). Código:
```sql
SELECT commission, COUNT(*)
FROM agents
GROUP BY commission
HAVING COUNT(*)>3;
```
Diagrama muestra agrupación por comisión (.15, .11, .14, .13, .12) con conteos 4,2,2,2,2 respectivamente, filtrado por HAVING COUNT(*)>3 deja solo la fila .15-4. Fuente: w3resource.com/sql/aggregate-functions/count-having.php.

## Slide 108
Título "Agregación: GROUP BY/HAVING". Diagrama ilustrativo (w3resource.com) con tabla `customer` (CUST_CITY/CUST_COUNTRY/OUTSTANDING_AMT). Código en dos pasos:
```sql
SELECT cust_city, cust_country, MAX(outstanding_amt)
FROM customer
GROUP BY cust_country, cust_city
HAVING MAX(outstanding_amt)>10000;
```
y una variante sin HAVING:
```sql
SELECT cust_city, cust_country, MAX(outstanding_amt)
FROM customer
GROUP BY cust_country, cust_city;
```
Tablas intermedias muestran el agrupamiento por ciudad+país con su máximo, y la tabla final filtrada por HAVING con 5 filas (Bangalore-India-12000, Chennai-India-11000, London-UK-11000, Mumbai-India-12000, Toronto-Canada-11000). Fuente: w3resource.com/sql/aggregate-functions/Max-having.php.

## Slide 109
Título "Ejercicio interactivo". Captura de una tabla `orders` (no del esquema de planetas) con columnas ORD_NUM, ORD_AMOUNT, ADVANCE_AMOUNT, ORD_DATE, CUST_CODE, AGENT_CODE, ORD_DESCRIPTION — 9 filas visibles de ejemplo. Pregunta: "Mostrar el agente que tiene mayor cantidad de órdenes". Resultado ya mostrado (recuadro celeste): AGENT_CODE/COUNT(AGENT_CODE) → A002-7. Código aún oculto.

## Slide 110
Título "Solución". Código completo de la solución al ejercicio de la slide 109 (consulta anidada con HAVING + subconsulta de MAX sobre conteos agrupados):
```sql
SELECT agent_code,
COUNT(agent_code)
FROM orders
GROUP BY agent_code
HAVING COUNT(agent_code) =
(
  SELECT MAX(mycount)
  FROM (
    SELECT agent_code,
    COUNT(agent_code) mycount
    FROM orders
    GROUP BY agent_code)
);
```
Diagrama extenso (w3resource.com) a la derecha explica el proceso paso a paso: la tabla `orders` original se agrupa por agent_code obteniendo conteos por agente (A004-4, A002-7, A007-2, A009-1, A011-2, A012-2); luego se calcula el MAX(mycount)=7; finalmente se filtra con HAVING COUNT(agent_code)=7, dando el resultado final AGENT_CODE=A002, COUNT(AGENT_CODE)=7.

## Slide 111
Repite el contenido de la slide 105: título "Agregación por planeta: GROUP BY/HAVING", misma tabla Aterrizaje, mismo código (`HAVING MAX(año)<2000`) y mismo resultado (Venus-2).

## Slide 112
Título "Agregación por planeta: HAVING/EVERY". Tabla Aterrizaje completa. Código:
```sql
SELECT planeta, COUNT(*) AS conteo
FROM Aterrizaje
GROUP BY planeta
HAVING EVERY(año BETWEEN 2000 AND 2005)
```
Resultado (recuadro celeste): Júpiter-1 (único planeta donde todos sus aterrizajes caen en 2000-2005).

## Slide 113
Título "Agregación por planeta: HAVING/ANY". Misma tabla. Dos consultas equivalentes mostradas juntas:
```sql
SELECT planeta, COUNT(*) AS conteo
FROM Aterrizaje
GROUP BY planeta
HAVING ANY(año BETWEEN 2000 AND 2005)
```
```sql
SELECT planeta, COUNT(*) AS conteo
FROM Aterrizaje
GROUP BY planeta
HAVING bool_or(año BETWEEN 2000 AND 2005)
```
Recuadro amarillo etiqueta la segunda como "Postgres" (usa bool_or en vez de ANY). Resultado (recuadro celeste): Júpiter-1, Marte-3 (planetas con al menos un aterrizaje en ese rango).

## Slide 114
Título "Ejercicio interactivo". Tabla Satélite completa. Pregunta: "¿Los descubridores que han descubierto más que dos satélites del mismo planeta?" (redacción con "más que", corregida en la siguiente slide). Resultado ya mostrado (recuadro celeste): descubridor=Galileo Gailiei (nota: nombre con errata "Gailiei" en vez de "Galilei", tal como aparece en la slide). Código aún oculto.

## Slide 115
Repite el ejercicio de la slide 114, redacción corregida: "¿Los descubridores que han descubierto más de dos satélites del mismo planeta?". Código (recuadro verde):
```sql
SELECT DISTINCT descubridor
FROM Satélite
GROUP BY planeta, descubridor
HAVING COUNT(*)>2
```
Resultado (recuadro celeste): descubridor=Galileo Gailiei (misma errata tipográfica que en la slide 114).

## Slide 116
Título "Ejercicio interactivo". Tablas Planeta y Aterrizaje completas. Pregunta: "¿Las distancias de los planetas que han sido visitados por tres o más países?". Resultado ya mostrado (recuadro celeste): nombre=Martes (errata tipográfica por "Marte"), dist=1,52. Código aún oculto.

## Slide 117
Repite el ejercicio de la slide 116 mostrando el código (recuadro verde):
```sql
SELECT DISTINCT nombre, dist
FROM Planeta
WHERE nombre IN
  ( SELECT planeta
    FROM Aterrizaje
    GROUP BY planeta
    HAVING ( COUNT
      (DISTINCT país)>=3)
  )
```
Resultado (recuadro celeste): nombre=Martes (misma errata), dist=1,52.

## Slide 118
Slide de transición decorativa, título "Limitar resultados" en azul, mascota ninja/mago con lápiz sentada en trono. Enlace: "Más detalles: https://en.wikipedia.org/wiki/Select_(SQL)#Limiting_result_rows".

## Slide 119
Título "Sistemas de bases de datos (con SQL)". Repite/actualiza la tabla-ranking de sistemas de BD vista en la slide 9, ahora con fecha "123 systems in ranking, October 2016" y columnas Oct2016/Sep2016/Oct2015. Top 20: 1.Oracle(1417.10), 2.MySQL(1362.65), 3.Microsoft SQL Server(1214.18), 4.PostgreSQL(318.69), 5.DB2(180.56), 6.Microsoft Access(124.68), 7.SQLite(108.57), 8.Teradata(76.23), 9.SAP Adaptive Server(69.48), 10.FileMaker(54.95), 11.Hive(49.20), 12.SAP HANA(45.77), 13.MariaDB(40.28), 14.Informix, 15.Vertica, 16.Microsoft Azure, 17.Netezza, 18.Firebird, 19.Amazon Redshift, 20.dBASE(9.66). Recuadro amarillo: "¡Varios sistemas pueden tener varias interpretaciones del estándar de SQL! Pero normalmente el "core" de SQL es compatible en los sistemas más populares." Fuente: http://db-engines.com/en/ranking/relational+dbms.

## Slide 120
Título "Ordenar resultados: ORDER BY [DESC|ASC]". Tabla Aterrizaje completa. Código:
```sql
SELECT *
FROM Aterrizaje
ORDER BY año DESC, nave
```
Resultado (recuadro celeste): 7 filas ordenadas por año descendente, con desempate alfabético por nave — Messenger-Mercurio-EEUU-2015, Beagle 2-Marte-ESA-2003, Galileo-Júpiter-EEUU-2003, Pioneer-Venus-EEUU-1978, Viking 1-Marte-EEUU-1976, Mars 2 lander-Marte-URRS-1971, Venera 3-Venus-URRS-1966.

## Slide 121
Título "Devolver n resultados: FETCH FIRST". Tabla Aterrizaje completa. Recuadro amarillo: "Una versión estándar (desde SQL:2008) que se usa en Postgres y DB2." Código:
```sql
SELECT *
FROM Aterrizaje
ORDER BY año DESC, nave
FETCH FIRST 3 ROWS ONLY
```
Resultado (recuadro celeste): 3 filas — Messenger-Mercurio-EEUU-2015, Beagle 2-Marte-ESA-2003, Galileo-Júpiter-EEUU-2003.

## Slide 122
Título "Devolver n resultados: LIMIT". Misma tabla. Recuadro amarillo: "Una versión no estándar que se usa en Postgres, SQLite y MySQL." Código:
```sql
SELECT *
FROM Aterrizaje
ORDER BY año DESC, nave
LIMIT 3
```
Resultado (recuadro celeste): mismas 3 filas que la slide 121.

## Slide 123
Título "Devolver n resultados: TOP". Misma tabla. Recuadro amarillo: "Una versión no estándar que se usa en SQL Server y MS Access." Código:
```sql
SELECT TOP 3 *
FROM Aterrizaje
ORDER BY año DESC, nave
```
Resultado (recuadro celeste): mismas 3 filas.

## Slide 124
Título "Devolver n resultados: ROW_NUMBER()". Misma tabla. Recuadro amarillo: "Una versión estándar (desde SQL:2003) que se usa en Postgres, DB2, MS Access, Oracle." Código con función de ventana:
```sql
SELECT * FROM (
  SELECT ROW_NUMBER()
    OVER (ORDER BY año DESC, nave)
    AS row, *
  FROM Aterrizaje
) AS Ans
WHERE row <= 3
```
Resultado (recuadro celeste), columna adicional "row": 1-Messenger-Mercurio-EEUU-2015, 2-Beagle 2-Marte-ESA-2003, 3-Galileo-Júpiter-EEUU-2003.

## Slide 125
Título "Devolver empates: RANK()". Misma tabla. Recuadro amarillo: "Una versión estándar (desde SQL:2003) que devuelva empates en el orden." Código:
```sql
SELECT * FROM (
  SELECT RANK()
    OVER (ORDER BY año DESC)
    AS rnk, *
  FROM Aterrizaje
) AS Ans
WHERE rnk <= 2
```
Resultado (recuadro celeste), columna "rnk": 1-Messenger-Mercurio-EEUU-2015, 2-Beagle 2-Marte-ESA-2003, 2-Galileo-Júpiter-EEUU-2003 — las filas de Beagle 2 y Galileo (ambas año=2003) comparten rank=2, resaltadas con recuadro punteado naranja para señalar el empate.

## Slide 126
Título "Saltar n resultados: LIMIT + OFFSET". Misma tabla. Recuadro amarillo: "Una versión no estándar que se usa en Postgres, SQLite y MySQL." Código:
```sql
SELECT *
FROM Aterrizaje
ORDER BY año DESC, nave
OFFSET 1 LIMIT 3
```
Resultado (recuadro celeste): 3 filas, saltando la primera — Beagle 2-Marte-ESA-2003, Galileo-Júpiter-EEUU-2003, Pioneer-Venus-EEUU-1978.

## Slide 127
Título "Ejercicio interactivo". Tabla Planeta completa. Pregunta: "¿Los nombres de los tres planetas con los años más largos que estén más lejos del Sol que la Tierra?". Resultado ya mostrado (recuadro celeste): Neptuno, Urano, Saturno. Código aún oculto.

## Slide 128
Repite el ejercicio de la slide 127 mostrando el código (recuadro verde):
```sql
SELECT nombre
FROM Planeta
WHERE radio > 1.0
ORDER BY años DESC
LIMIT 3
```
Resultado (recuadro celeste): mismas 3 filas — Neptuno, Urano, Saturno. (Nota: la condición usa `radio > 1.0` como proxy de "más lejos del Sol que la Tierra" en vez de `dist > 1.0`, posible inconsistencia con el enunciado, aunque en este dataset da el mismo resultado).

## Slide 129
Título "Ejercicio interactivo". Misma tabla Planeta. Pregunta: "¿El nombre del planeta con el tercer año más largo que esté más lejos del Sol que la Tierra?". Resultado ya mostrado (recuadro celeste): nombre=Saturno. Código aún oculto.

## Slide 130
Repite el ejercicio de la slide 129 mostrando el código (recuadro verde):
```sql
SELECT nombre
FROM Planeta
WHERE radio > 1.0
ORDER BY años DESC
LIMIT 1 OFFSET 2
```
Resultado (recuadro celeste): nombre=Saturno.

## Slide 131
Slide de transición decorativa, título "Más funciones" en azul, mascota ninja/mago con lápiz sentada en trono. Recuadro amarillo: "¡Dependen mucho del sistema particular!".

## Slide 132
Título "Aritmético". Lista de operadores y funciones aritméticas: `+, -, /, *, %`; `ABS(a)`; `CEIL(a)` o `CEILING(a)`; `FLOOR(a)`; `EXP(a,b)` o `POWER(a,b)`; `ROUND(a)` o `ROUND(a,b)`; `SQRT(a)`; "...".

## Slide 133
Título "Aritmético". Tabla Planeta completa. Código de ejemplo:
```sql
SELECT nombre,
  ABS(dist-1.0) AS distDeTierra
FROM Planeta
ORDER BY distDeTierra
```
Resultado (recuadro celeste): Tierra-0,00, Venus-0,28, Martes-0,52 (errata "Martes" por "Marte"), Mercurio-0,61, Júpiter-4,20, Saturno-8,54, Urano-18,19, Neptuno-29,07.

## Slide 134
Título "Strings". Lista de funciones de manejo de cadenas: `LOWER(a)` o `LOWERCASE(a)` o `LCASE(a)`; `UPPER(a)` o `UPPERCASE(a)` o `UCASE(a)`; `TRIM(a)`; `SUBSTRING(a,b)` o `SUBSTRING(a,b,c)`; `STARTSWITH(a,b)`; "...".

## Slide 135
Título "Condicionales". Sintaxis genérica de estructuras condicionales en SQL:
```
IF ... THEN ... [ELSE IF ...]* [ELSE]
CASE ... [WHEN ... THEN ...]* [ELSE ...]
...
```

## Slide 136
Slide de transición decorativa, título "Consultas directas vs. consultas anidadas" en azul, mascota ninja/mago con lápiz sentada en trono.

## Slide 137
Título "SQL tiene mucha redundancia". Collage de 8 fotografías reales de carteles/letreros con redundancia lingüística humorística (decorativas, ejemplo de la idea de "decir lo mismo de varias formas" aplicada al lenguaje natural, análoga a la redundancia de SQL): "¡Aviso! Se solicita trabajador(a) para trabajar"; "TENEMOS HIELO FRIO"; "LIBRERIA DE LIBROS"; "TENEMOS HIELO HASTA QUE SE ACABE"; portada de periódico "LA PRENSA — FALLECEN TRES AL SER ASESINADOS"; definición circular "Salmón ahumado: El salmón ahumado es un producto ahumado del salmón"; "PALETERIA DE PALETAS"; "FOTOCOPIAS IDENTICAS".

## Slide 138
Título "Consultas directas vs. consultas anidadas". Subtítulo: "Nombres y géneros de los co-actores de Liv Tyler." Cuatro variantes de consulta equivalentes sobre un esquema distinto (actor/personaje), mostradas en cuadrantes de colores:
(1) Selección/producto (azul):
```sql
SELECT DISTINCT A.nombre, A.genero
FROM actor A,
  personaje P1, personaje P2
WHERE P1.a_nombre='Tyler, Liv'
  AND P1.p_nombre = P2.p_nombre
  AND P1.p_anho = p2.p_anho
  AND A.nombre = P2.a_nombre
```
(2) Join explícito (naranja):
```sql
SELECT DISTINCT A.nombre, A.genero
FROM actor A NATURAL JOIN
  ( SELECT DISTINCT P2.a_nombre AS nombre
    FROM personaje P2 NATURAL JOIN
      ( SELECT DISTINCT P1.p_nombre, P1.p_anho
        FROM personaje P1
        WHERE P1.a_nombre='Tyler, Liv'
      ) PLT
  ) CLT
```
(3) Consulta anidada FROM (verde):
```sql
SELECT DISTINCT A.nombre, A.genero FROM
  ( SELECT DISTINCT P2.a_nombre FROM
    ( SELECT DISTINCT P1.p_nombre, P1.p_anho
      FROM personaje P1
      WHERE P1.a_nombre='Tyler, Liv'
    ) PLT, personaje P2
    WHERE PLT.p_nombre = P2.p_nombre
      AND PLT.p_anho = P2.p_anho
  ) CLT, actor A
WHERE CLT.a_nombre = A.nombre
```
(4) Consulta anidada WHERE/IN (gris):
```sql
SELECT DISTINCT A.nombre, A.genero
FROM actor A
WHERE A.nombre IN
  ( SELECT DISTINCT P2.a_nombre
    FROM personaje P2
    WHERE (P2.p_nombre,P2.p_anho) IN
      ( SELECT DISTINCT P1.p_nombre, P1.p_anho
        FROM personaje P1
        WHERE P1.a_nombre='Tyler, Liv'
      )
  )
```
Recuadro punteado (5): "[Hay más opciones]" con la pregunta "¿Son equivalentes pero cuál es más eficiente?".

## Slide 139
Repite el layout de la slide 138 (mismas 4 consultas, misma pregunta "Nombres y géneros de los co-actores de Liv Tyler.") ahora con tiempos de ejecución medidos anotados en cada cuadrante: (1) 10 ms, (2) 9 ms, (3) 11 ms, (4) 12 ms. Recuadro amarillo: "¡Hay poca diferencia!".

## Slide 140
Mismo layout de 4 consultas, ahora con la condición cambiada a un patrón LIKE ('%, L%' en vez de ='Tyler, Liv') y subtítulo "Nombres y géneros de co-actores de personas con una apellida "L%"." Tiempos anotados: (1) 160 ms, (2) 169 ms, (3) 167 ms, (4) 48 ms — la consulta anidada WHERE/IN es notablemente más rápida en este caso. Recuadro amarillo: "¡Hay una diferencia (pero es poco predecible)!".

## Slide 141
Título "SQL es un lenguaje declarativo". Subtítulo: "Uno dice lo que quiere, no cómo se debería computar". Diagrama: a la izquierda 4 recuadros con las 4 variantes de consulta de las slides 138-140 (Selección/producto, Join explícito, Consulta anidada FROM, Consulta anidada WHERE/IN), todas apuntando con flechas hacia un cubo dorado central etiquetado "Caja Negra" (representa el motor/optimizador de BD), que a su vez apunta a una salida: una terminal con fondo negro mostrando resultado tabular nombre/genero con ~28 filas de actores (Abbott Jane-F, Acevedo Gino-M, Allpress Bruce-M, Appleby Noel-M, Appleton Matt-M, Astin Ali-F, Astin Sean-M, Aston David-M, Bach John-M, Baker Sala-M, etc.). Ilustra que las 4 consultas equivalentes producen el mismo resultado independientemente del "cómo".

## Slide 142
Repite el título y diagrama de la slide 141 (mismo esquema Caja Negra), ahora con texto explicativo superpuesto en primer plano: "Idealmente, el motor puede elegir el mejor plan de ejecución independientemente de su expresión particular. Pero, esto es caro, entonces en la práctica, hay diferencias. Regresaremos al tema de rendimiento y optimización más adelante en el curso. Pero en general, se puede expresar una consulta en la forma "más natural" y dejar la ejecución al motor."

## Slide 143
Slide de cierre/resumen con metáfora de iceberg: imagen de un iceberg real, con la parte visible sobre el agua (arriba) listando lo cubierto en la primera mitad del capítulo: SELECT, FROM, WHERE; ORDER BY; JOIN (simple); UNION, INTERSECT, EXCEPT; LIKE; IN, BETWEEN. El texto "SQL" está escrito grande sobre la línea de flotación. Bajo el agua (parte sumergida, mucho más grande) lista lo cubierto en la segunda mitad: Más tipos de JOIN; Nulos; Consultas anidadas; Agregación — simbolizando que esa es la parte más extensa/compleja del lenguaje. Imagen decorativa inferior derecha: fotograma de la película Titanic (Jack y Rose) con subtítulo "Jack. Wake up." (meme/referencia cultural sobre "lo que queda bajo la superficie").

## Slide 144
Slide final "Preguntas?" sobre fondo azul oscuro. Imagen decorativa: escena animada de "El Principito" (con marca de agua "mcadamsdaily") — el personaje sentado en un planeta pequeño junto a su flor, mirando las estrellas.
