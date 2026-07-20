---
curso: BD2
titulo: 01 Arquitectura BDMS
slides: 28
fuente: 01 Arquitectura BDMS.pdf
---

# 01 Arquitectura BDMS

## Índice

- [Arquitectura Interna de un DBMS](#arquitectura-interna-de-un-dbms)
- [Motivación](#motivación)
- [Arquitectura General de un DBMS](#arquitectura-general-de-un-dbms)
- [Flujo Completo: SQL → Disco](#flujo-completo-sql--disco)
- [Parser](#parser)
  - [Fase 1: Análisis Léxico (Tokenización)](#fase-1-análisis-léxico-tokenización)
  - [Fase 2: Análisis Sintáctico (AST)](#fase-2-análisis-sintáctico-ast)
  - [Fase 3: Verificación Semántica](#fase-3-verificación-semántica)
- [Optimizer](#optimizer)
- [Executor](#executor)
- [Buffer Manager](#buffer-manager)
- [File Manager](#file-manager)
- [Transaction Manager](#transaction-manager)
- [Write-Ahead Log (WAL) y Recovery](#write-ahead-log-wal-y-recovery)
- [Disco](#disco)
- [Flujo Completo — Recapitulación](#flujo-completo--recapitulación)
- [Laboratorio](#laboratorio)

## Arquitectura Interna de un DBMS

Comprender cómo una consulta SQL se transforma en operaciones físicas sobre disco dentro de un DBMS.

**Referencias bibliográficas:**
- Silberschatz – Database System Concepts (7th Ed.), Chapter 1: Introduction
- Ramakrishnan – Database Management Systems (3rd Ed.), Chapter 1: Overview of Database Systems

(slides 2)

## Motivación

**Figura:** Diagrama en caja azul (parte superior derecha) con flujo vertical: caja «SQL» con flecha hacia abajo a caja «DBMS», que a su vez apunta a un icono de cilindro que representa la base de datos o almacenamiento físico.

Dada la consulta:
- SELECT * FROM users WHERE id = 100;

¿Cómo el DBMS transforma la consulta SQL en acciones ejecutables?
- El usuario dice qué quiere, pero no cómo obtenerlo.

El DBMS debe decidir:
- si usar un índice
- si hacer un escaneo completo
- cómo acceder al disco
- cómo usar la memoria

Silberschatz: esta separación entre declaración y ejecución física es uno de los principios clave de los sistemas de bases de datos.

**Figura:** Tres bloques de contenido. Caja azul superior derecha con el diagrama SQL → DBMS → cilindro y el texto de la consulta de ejemplo. Caja con borde naranja inferior izquierda con el encabezado «El DBMS debe decidir:» y cuatro bullets. Caja con borde verde inferior derecha con la cita de Silberschatz.

(slides 3)

## Arquitectura General de un DBMS

Ramakrishnan – Database Management Systems

**Figura:** Diagrama de arquitectura general de un DBMS. En el lado izquierdo, cuatro entradas externas conectadas mediante flechas bidireccionales al bloque vertical «DBMS Interfaces»: «DDL statements», «Interactive Query», «Applications» y «Database Tools». El bloque «DBMS Interfaces» conecta al interior del DBMS (caja grande). En la sección superior del interior: «Connection Manager», «Security Manager», «DDL compiler» y «Database utilities». En el centro, subcaja «Query Processor» que contiene: «DML compiler», «Query parser», «Query rewriter», «Query optimizer» y «Query executor» en la parte inferior de ese grupo. En la parte inferior, subcaja «Storage Manager» con: «Transaction Manager», «Buffer Manager», «Lock Manager» y «Recovery Manager». En la base, un cilindro etiquetado «Database» conectado al Storage Manager, particionado en tres secciones: «raw data», «indices» y «catalog». Número de slide «4» en la esquina inferior derecha del diagrama.

(slides 4)

## Flujo Completo: SQL → Disco

**Figura:** Diagrama de flujo horizontal de izquierda a derecha. A la izquierda, icono azul ondulado etiquetado «SQL Query». Flecha hacia la subcaja «Query Processor» que agrupa tres etapas en secuencia: «Parser» (caja teal), «Optimizer» (caja verde) y «Executor» (caja naranja). Flecha hacia la subcaja «Storage Manager» con «Buffer Mgr» (caja naranja oscuro) y «File Mgr» (caja roja). Flecha final hacia cilindro morado etiquetado «Disco». Debajo de cada componente, su nombre completo y descripción: «Parser — Analiza la sintaxis del SQL recibido»; «Optimizer — Genera el plan de ejecución óptimo»; «Executor — Ejecuta el plan nodo por nodo»; «Buffer Manager — Gestiona páginas en memoria RAM»; «File Manager — Lee/escribe páginas en disco físico».

Cada capa agrega semántica y abstracción hasta llegar al almacenamiento físico.

### El Parser recibe la consulta

```sql
SELECT e.name, d.dept_name, SUM(e.salary) as suma
FROM employees e JOIN departments d ON e.dept_id = d.id
WHERE e.hire_date > '2020-01-01'
group by e.name, d.dept_name
```

¿Qué hace el DBMS con esto?

Entiende                   Decide                   Lo busca
qué se pide              cómo buscarlo             y lo retorna

**Figura:** Una barra vertical gris conecta el bloque de código con la pregunta central «¿Qué hace el DBMS con esto?». Debajo, tres cajas horizontales de colores: caja morada izquierda «Entiende qué se pide», caja azul central «Decide cómo buscarlo», caja verde derecha «Lo busca y lo retorna».

(slides 5–6)

## Parser

### Fase 1: Análisis Léxico (Tokenización)

El parser lee el texto SQL carácter a carácter y lo divide en unidades mínimas con significado: los tokens.

#### Tipos de Token en SQL

| Tipo | Ejemplos |
|---|---|
| KEYWORD | SELECT, FROM, WHERE, JOIN, GROUP BY |
| IDENTIFIER | employees, e.name, dept_id, salary |
| LITERAL | '2020-01-01', 50000, TRUE, NULL |
| OPERATOR | > < = != AND OR NOT LIKE |
| DELIMITER | ( ) , ; . |
| WHITESPACE | espacios, tabs, newlines → ignorados |

#### Ejemplo: tokenizando nuestra query

SELECT       e.name          ,     d.dept_name          ,        SUM
(        e.salary        )       FROM      employees         e
JOIN       departments

Analogía compilador: igual al Lexer/Scanner — transforma código fuente en una lista de tokens antes de parsear.

**Figura:** Tabla de tipos de token con filas codificadas por color: KEYWORD (morado claro), IDENTIFIER (azul claro), LITERAL (verde claro), OPERATOR (naranja claro), DELIMITER (rojo claro), WHITESPACE (gris claro). A la derecha, descomposición visual de la consulta en tokens coloreados según su tipo: SELECT (morado), e.name (azul), , (rojo), d.dept_name (azul), , (rojo), SUM (morado), ( (rojo), e.salary (azul), ) (rojo), FROM (morado), employees (azul), e (azul), JOIN (morado), departments (azul). En la parte inferior, caja morada oscura con la analogía al compilador.

(slides 7)

### Fase 2: Análisis Sintáctico (AST)

El parser verifica que la secuencia de tokens sigue las reglas gramaticales del SQL y construye un Árbol de Sintaxis Abstracta.

#### Gramática SQL simplificada

```
SELECT_stmt :=
  SELECT target_list
  FROM     from_clause
  [JOIN    join_clause]
  [WHERE where_clause]
  [GROUP BY groupby_clause]
  [ORDER BY orderby_clause]
  [LIMIT    n]

-- [] = opcional
```

Error sintáctico: SELECT name FROM WHERE salary > 0
→ Error: se esperaba identificador después de FROM

#### AST generado para nuestra query

**Figura:** Árbol jerárquico de operadores de álgebra relacional, de arriba hacia abajo:
- Nodo raíz: $\pi$ con etiqueta «e.name, d.dept_name, SUM(salary) -> suma»
- Segundo nivel: $\gamma$ con etiqueta «name, dept_name, SUM(salary)»
- Tercer nivel: $\sigma$ con etiqueta «e.hire_date > "2020-01-01"»
- Cuarto nivel: $\bowtie$ con etiqueta «e.dept_id = d.id»
- Quinto nivel (dos ramas): rama izquierda con $\rho$ etiquetado «e» conectado a la hoja «employees»; rama derecha con $\rho$ etiquetado «d» conectado a la hoja «departments». Flechas conectan cada nodo padre con sus hijos.

#### Operadores del Álgebra Relacional

| Operador | Descripción | Ejemplo |
|---|---|---|
| $\sigma$ (sigma) | Selección: Filtra filas. | Ej: $\sigma_{\text{salary}>50000}(\text{Employees})$ |
| $\pi$ (pi) | Proyección: Selecciona columnas. | Ej: $\pi_{\text{name, dept}}(\text{Emp})$ |
| $\bowtie$ (join) | Join: Combina tablas por condición. | |
| $\rho$ (rho) | Renombrado: Renombra relaciones o atributos | |
| $\cup \cap -$ | Unión, Intersección, Diferencia de conjuntos | |
| $\gamma$ (gamma) | Agrupamiento: GROUP BY con funciones de agregación | |

**Figura:** Tabla de seis filas con operadores de álgebra relacional, cada fila con su símbolo, descripción en español y ejemplo cuando aplica.

Ejemplo:

```sql
select R.A, R.C
from R, S
where R.A = S.A and
      ((R.B = 1 and S.D = 2) or
       (R.C > 3 and S.D = 2))
```

**Figura:** Flecha horizontal desde la consulta SQL hacia un árbol de álgebra relacional. De arriba hacia abajo:
- Nodo raíz: $\Pi_{R.A, R.C}$ (proyección de las columnas del SELECT)
- Segundo nivel: $\sigma_{(R.B=1 \lor R.C>3) \land S.D=2}$ con una flecha roja apuntando a este nodo y la palabra «distributiva» en rojo al lado, indicando que la expresión original $((R.B = 1 \land S.D = 2) \lor (R.C > 3 \land S.D = 2))$ se simplificó usando la ley distributiva a $(R.B=1 \lor R.C>3) \land S.D=2$
- Tercer nivel: $\bowtie_A$ (join sobre el atributo A, representando la condición R.A = S.A y las tablas del FROM)
- Hojas: «R» (izquierda) y «S» (derecha)

(slides 8–10)

### Fase 3: Verificación Semántica

El AST es sintácticamente correcto — pero ¿existen realmente esas tablas y columnas? ¿Los tipos son compatibles?

#### Existencia de tablas ✓
- ¿Existe 'employees' en el schema actual?
- ¿Tiene el usuario permiso para leerla?

#### Existencia de columnas ✓
- ¿'e.name', 'e.salary', 'd.dept_name' existen en sus respectivas tablas?

#### Ambigüedad de nombres !
- Si dos tablas tienen columna 'id', ¿a cuál se refiere 'id' sin prefijo?

#### Compatibilidad de tipos ✓
- ¿Puede compararse hire_date (DATE) con '2020-01-01' (string literal)?

#### Funciones de agregación ✓
- ¿SUM() se usa con columna numérica?
- ¿GROUP BY incluye las columnas requeridas?

#### Alias y resolución ✓
- 'e' y 'd' se resuelven a las tablas correspondientes declaradas en FROM.

Fuente de verdad: el parser consulta el System Catalog (pg_class, pg_attribute, pg_type) para resolver cada nombre de tabla, columna y tipo.

**Figura:** Seis cajas oscuras dispuestas en cuadrícula 2×3, cada una con franja lateral de color e icono de estado: verde con checkmark (✓) para Existencia de tablas, Existencia de columnas, Compatibilidad de tipos, Funciones de agregación y Alias y resolución; roja con signo de exclamación (!) para Ambigüedad de nombres.

(slides 11)

## Optimizer

El optimizer recibe el query tree y genera el plan físico de menor costo estimado. Es el componente más complejo del DBMS.

### Del AST al Plan de Ejecución Óptimo

#### Pipeline interno del Optimizer

1. **Reescritura lógica**
   Aplica reglas de equivalencia del álgebra relacional: empujar predicados, eliminar subconsultas redundantes, aplanar vistas.

2. **Enumeración de planes**
   Genera combinaciones de join orders y algoritmos (Nested Loop, Hash Join, Merge Join). El espacio es factorial en el número de tablas.

3. **Estimación de costo**

4. **Selección del plan**
   Elige el plan de menor costo estimado. Produce el Plan de Ejecución Físico — un árbol de operadores concretos.

#### Plan físico resultante para nuestra query

```text
HashAggregate       (GROUP BY e.name, d.dept_name)
  -> Hash Join          (e.dept_id = d.id)
       Hash Cond: e.dept_id = d.id
       -> Seq Scan on departments d
       -> Index Scan on employees e
            Index: idx_hire_date
            Filter: hire_date > '2020-01-01'
```

cost=0.00..845.32          rows=1240   width=64

- Seq page cost = 1.0
- Random page cost = 4.0
- CPU tuple cost = 0.01
- Statistics: pg_statistic

```sql
SELECT e.name, d.dept_name, SUM(e.salary) as suma
FROM employees e JOIN departments d ON e.dept_id = d.id
WHERE e.hire_date > '2020-01-01'
group by e.name, d.dept_name
```

**Figura:** Dos columnas. Columna izquierda con los cuatro pasos numerados del pipeline interno del optimizer. Columna derecha con caja oscura que muestra el árbol del plan físico en formato texto indentado (HashAggregate → Hash Join → Seq Scan on departments d / Index Scan on employees e con índice idx_hire_date y filtro hire_date > '2020-01-01'). Debajo del árbol, métricas de costo (cost, rows, width) y parámetros de estimación (Seq page cost, Random page cost, CPU tuple cost, Statistics: pg_statistic). En la parte inferior, la consulta SQL de ejemplo en texto azul.

(slides 12)

### Optimización Sintáctica

- Optimización Sintáctica
  - Lleva las condiciones y proyecciones lo más abajo posible.

- Ejercicio
  - Optimizar la siguiente consulta:

```sql
SELECT NOMBRE
FROM EST, ACT, PROY
WHERE EST.COD = ACT.COD
  AND ACT.COD = PROY.COD
  AND EST.NOMBRE != "Jorge"
  AND EST.CARRERA = "CS"
  AND (ACT.HORAS = 4 OR ACT.HORAS = 6)
```

**Figura:** Diagrama de optimización sintáctica. Estado inicial (izquierda): operador de selección $\sigma_{\text{cond}}$ en la cima del árbol, operando sobre el resultado de un join $\bowtie$ entre las relaciones R (izquierda) y S (derecha). Flecha hacia el estado final (derecha): selecciones empujadas hacia abajo — $\sigma_{\text{cond1}}$ aplicada directamente sobre R, $\sigma_{\text{cond2}}$ aplicada directamente sobre S, luego el join $\bowtie$, y $\sigma_{\text{cond3}}$ encima del join para condiciones que solo pueden evaluarse después del join. A la derecha del diagrama, el bloque de ejercicio con la consulta SQL a optimizar.

(slides 13)

## Executor

El Executor recorre el plan físico como un árbol: llama a cada nodo para que produzca tuplas, que pasan al nodo padre.

### Evaluando el Plan Nodo por Nodo

#### Modelo Volcano / Iterator

Cada nodo implementa 3 funciones:

- `open()` → inicializa el nodo
- `next()` → retorna una tupla
- `close()` → libera recursos

El nodo raíz llama next() al hijo, que llama next() a su hijo, etc.

→ Pull-based / lazy evaluation

#### Tipos de Nodo

**Acceso**
- Seq Scan
- Index Scan
- Bitmap Scan

**Join**
- Nested Loop
- Hash Join
- Merge Join

**Agreg.**
- Hash Aggregate
- Group Aggregate
- Sort
- Limit

**Figura:** Dos columnas con fondo oscuro. Columna izquierda «Modelo Volcano / Iterator» con las tres funciones (open, next, close), el flujo de llamadas next() de padre a hijo, y el concepto «Pull-based / lazy evaluation» resaltado en amarillo. Columna derecha «Tipos de Nodo» con tres secciones de color: Acceso (azul) con Seq Scan, Index Scan y Bitmap Scan; Join (naranja) con Nested Loop, Hash Join y Merge Join; Agreg. (morado) con Hash Aggregate, Group Aggregate, Sort y Limit.

(slides 14)

### Seq Scan vs Index Scan

#### Sequential Scan

✓ Ventajas

- Eficiente para tablas pequeñas
- Sin overhead de estructura adicional
- Óptimo cuando selectividad > 10-20%
- No requiere acceso aleatorio a disco

✗ Limitaciones

- Muy lento en tablas grandes con filtros selectivos
- Lee todas las páginas independientemente del filtro

Usar cuando: Tablas pequeñas, queries sin filtros, filtros con alta selectividad (muchas filas retornadas)

#### Index Scan

✓ Ventajas

- Rápido para alta selectividad (pocas filas)
- Evita leer páginas irrelevantes
- Útil para ORDER BY si hay índice ordenado

✗ Limitaciones

- Acceso aleatorio a disco (costoso en HDD)
- Overhead del índice en INSERT/UPDATE/DELETE

Usar cuando: Filtros muy selectivos (< 5-10% de filas), columnas en WHERE con índice, ORDER BY con índice.

**Figura:** Comparación en dos columnas. Columna izquierda con encabezado azul «Sequential Scan» y secciones de ventajas (✓), limitaciones (✗) y «Usar cuando». Columna derecha con encabezado verde «Index Scan» y las mismas tres secciones.

(slides 15)

## Buffer Manager

El Buffer Manager mantiene un pool de páginas en RAM. Su objetivo: minimizar el I/O a disco satisfaciendo las peticiones del Executor.

### La Caché de Páginas del DBMS

#### Buffer Pool

Área de memoria dividida en frames de tamaño fijo (igual al page size del disco, típicamente 8 KB en PostgreSQL). El DBMS controla este espacio directamente, sin delegar al OS.

#### Page Table

Estructura hash que mapea: disk_page_id → frame_number. Incluye dos metadatos críticos por frame: pin_count (cuántos procesos usan la página) y dirty_bit (fue modificada).

#### Dirty Pages

Una página dirty fue modificada en RAM pero aún no escrita al disco. Antes de flushear, el Buffer Manager garantiza que el registro WAL correspondiente ya esté en disco (principio Write-Ahead Log).

**Figura:** Diagrama de tres capas. Capa inferior «On-Disk File» con cuatro bloques etiquetados page1, page2, page3 y page4 en disco. Capa superior derecha «Buffer Pool» con frames de memoria conteniendo page1, page3 y page2 cargados; un cuarto frame etiquetado frame4 vacío. Capa central «Page Table» como mecanismo de búsqueda: flechas rojas desde entradas de la Page Table hacia las ubicaciones correspondientes en el Buffer Pool. Icono de pin rojo junto a la entrada de page1 (representa pin_count). Icono de candado rojo junto a la entrada de page2. Línea punteada roja conecta la entrada de page2 en la Page Table de vuelta a page2 en el On-Disk File, representando sincronización o fetch de página.

(slides 16)

### Políticas de Reemplazo

Cuando el buffer está lleno y se necesita cargar una nueva página, el sistema debe decidir qué página reemplazar.

**LRU** — Least Recently Used
Expulsa la página menos usada recientemente. Simple y efectivo para workloads OLTP. Default en muchos DBMS.

**Clock** — Clock / Second Chance
Aproximación eficiente de LRU con un puntero circular y bit de referencia. Menor overhead que LRU puro.

**LRU-K** — LRU de K referencias
Considera las últimas K referencias, no solo la más reciente. Mejor para workloads mixtos (PostgreSQL usa una variante).

**MRU** — Most Recently Used
Reemplaza la más recientemente usada. Óptimo para sequential scans completos donde la página no se reutilizará.

Pin count > 0 → el frame NO puede ser reemplazado (está siendo usado por el Executor). Al terminar, el Executor hace unpin.

**Figura:** Cuatro filas con encabezados naranjas para cada política (LRU, Clock, LRU-K, MRU) y cajas de descripción en color crema a la derecha con su explicación. En la parte inferior, nota sobre pin count y unpin.

(slides 17)

## File Manager

El File Manager traduce abstracciones lógicas (page_id, tabla) a posiciones físicas en disco. Opera por debajo del Buffer Manager.

### Organización en Disco

**Heap File**
Colección no ordenada de páginas. Registros insertados al final. Acceso secuencial o por RID (Record ID).

**Page / Block**
Unidad mínima de I/O (típicamente 4KB–16KB). Contiene cabecera, slots de registros y espacio libre.

**Gestión de Espacio**
El file manager rastrea páginas libres, con espacio disponible, y asigna nuevas páginas según demanda.

**Figura:** Pila vertical central de cajas conectadas por línea gris central, de arriba hacia abajo: «Buffer Manager» (morado oscuro), «Heap Files / Segmentos» (morado medio), «Páginas (Pages / Blocks)» (morado claro), «Registros (Tuples)» (morado muy claro), «Almacenamiento Físico (Disco)» (naranja). A la derecha, tres cajas oscuras con las definiciones de Heap File, Page / Block y Gestión de Espacio, cada una alineada con su capa correspondiente en la pila.

(slides 18)

### Organización Física en Disco

#### Estructura de una Página

- Header (24 bytes)
- ItemId Array
- Espacio Libre
- Tupla N
- Tupla 2
- Tupla 1

tabla = 1 o más archivos
sectores, cilindros, bloques

#### Heap File y RID

- Colección NO ordenada de páginas
- INSERT: agrega al final (append)
- DELETE: marca tupla como inválida (no la borra físicamente)
- UPDATE: DELETE + INSERT (en InnoDB/PostgreSQL MVCC)
- Full Scan si no hay índice adecuado

RID = (page_id, slot_number)
Identificador físico único de cada tupla.

**Figura:** Columna izquierda con diagrama vertical de la estructura interna de una página: bloque superior «Header (24 bytes)», debajo «ItemId Array», bloque verde grande «Espacio Libre» en el centro, y en la parte inferior tres bloques «Tupla N», «Tupla 2» y «Tupla 1» apilados de arriba hacia abajo (las tuplas crecen desde abajo hacia el espacio libre). Anotaciones laterales: «tabla = 1 o más archivos» y «sectores, cilindros, bloques». Columna derecha con lista de características del Heap File y caja roja inferior con la fórmula RID = (page_id, slot_number) y su descripción.

(slides 19)

## Transaction Manager

El Transaction Manager no es secuencial - está activo en PARALELO con todos los demás componentes durante toda la transacción.

### Garantizando ACID

#### A Atomicity
Todo o nada. Si falla cualquier parte de la transacción, se deshacen TODOS los cambios. Nunca queda en estado parcial.

#### C Consistency
La BD pasa de un estado válido a otro estado válido. Las restricciones (PK, FK, CHECK) siempre se mantienen.

#### I Isolation
Transacciones concurrentes no se ven entre sí (según el nivel de aislamiento configurado: READ COMMITTED, SERIALIZABLE, etc.).

#### D Durability
Un COMMIT confirmado sobrevive a cualquier fallo del sistema. El WAL garantiza esto.

**Figura:** Cuatro bloques de colores con las letras A (azul), C (verde), I (naranja) y D (rojo) y sus definiciones de las propiedades ACID. A la derecha, diagrama de estados de transacción titulado «Transaction States in DBMS»: estado inicial «Active» con transición «Read / Write operations» hacia «Partially Committed» y transición «Failure» hacia «Failed». Desde «Partially Committed», transición «Permanent Store» hacia «Committed» y «Failure» hacia «Failed». Desde «Failed», transición «Roll Back» hacia «Aborted». «Committed» conduce a «Terminated». «Aborted» conduce a «Terminated». «Terminated» es el estado final para transacciones exitosas (Committed) y fallidas (Aborted).

(slides 20)

### Subcomponentes del Transaction Manager

**Lock Manager**

- Controla el acceso concurrente con locks compartidos (S) y exclusivos (X).
- Detecta deadlocks mediante un wait-for graph.
- Protocolo 2PL (Two-Phase Locking): crecimiento → punto de lock → decrecimiento.

**Log Manager (WAL)**

- Write-Ahead Log: cada cambio se escribe en el log ANTES de ir a disco.
- Garantiza Durability y permite Recovery.
- Force-the-Log rule: el log se sincroniza (fsync) en cada COMMIT.

**Recovery Manager**

Tras un crash, usa el WAL para:

- REDO → re-aplica transacciones confirmadas
- UNDO → revierte transacciones incompletas
- Checkpoints limitan cuánto log hay que releer.

**Figura:** La slide presenta un encabezado de sección con barra morada que dice «Subcomponentes del Transaction Manager». Debajo, tres columnas paralelas con los títulos «Lock Manager», «Log Manager (WAL)» y «Recovery Manager», cada una con sus bullets correspondientes.

(slides 21)

## Write-Ahead Log (WAL) y Recovery

**PRINCIPIO WAL:** Todo cambio debe ser registrado en el log ANTES de que la página modificada se escriba en disco.

**Figura:** Flujo horizontal de cinco pasos numerados, conectados por flechas de izquierda a derecha:

1. **BEGIN Transaction** (caja azul)
2. **Modificar página en RAM** (caja verde)
3. **Escribir WAL record** (caja naranja)
4. **COMMIT (fsync WAL)** (caja verde)
5. **bgwriter flushea a disco (async)** (caja morada)

**UNDO (Rollback)**

Revierte cambios de transacciones incompletas al momento del crash. Usa el log para deshacer operaciones.

**REDO (Roll-forward)**

Re-aplica cambios de transacciones confirmadas que no llegaron a disco. Garantiza durabilidad.

**Checkpoint**

Punto de sincronización: todos los cambios hasta aquí están en disco. Limita cuánto log debe reproducirse.

**Figura:** Debajo del flujo de cinco pasos, tres bloques verticales alineados horizontalmente: «UNDO (Rollback)» con encabezado rojo, «REDO (Roll-forward)» con encabezado verde, y «Checkpoint» con encabezado naranja. Cada bloque contiene su descripción correspondiente.

(slides 22)

## Disco

Todo el trabajo de los componentes anteriores tiene un único objetivo: reducir la cantidad de veces que se accede al disco.

### Latencia: por qué el I/O importa tanto

| Componente | Latencia |
|---|---|
| CPU Register | < 1 ns |
| L1 Cache | ~1 ns |
| L2/L3 Cache | ~10 ns |
| RAM (Buffer) | ~100 ns |
| SSD NVMe | ~100 µs |
| SSD SATA | ~500 µs |
| HDD (7200rpm) | ~10 ms |

1 acceso a HDD ≈ 10,000,000 instrucciones de CPU. El Buffer Manager existe para evitar esto.

**Figura:** Gráfico de barras horizontales que compara la latencia de cada componente de almacenamiento, ordenado de más rápido (arriba) a más lento (abajo). Las barras de CPU Register, L1 Cache y L2/L3 Cache son muy cortas y de color verde. La barra de RAM (Buffer) es amarilla y ligeramente más larga. Las barras de SSD NVMe (naranja) y SSD SATA (rojo-naranja) son notablemente más largas. La barra de HDD (7200rpm) es la más larga y de color rojo, representando ~10 ms. Cada barra tiene su etiqueta de componente a la izquierda y su valor de latencia a la derecha.

(slides 23)

## Flujo Completo — Recapitulación

Siguiendo nuestra query de ejemplo de principio a fin:

1. **PARSER** — Tokeniza el SQL → construye el AST → verifica 'employees', 'departments', 'e.name', 'hire_date' en pg_catalog.

2. **OPTIMIZER** — Genera planes candidatos → estima costos con pg_statistic → elige: Index Scan en employees + Hash Join + Hash Aggregate.

3. **EXECUTOR** — Recorre el plan de arriba abajo. Llama next() en cada nodo. Para leer datos, llama al Buffer Manager.

4. **BUFFER MGR** — ¿Está la página en RAM? → cache hit, retorna inmediatamente. No está? → pide al File Manager que la cargue desde disco.

5. **FILE MGR** — Traduce page_id → offset en archivo del SO. Lee 8 KB del disco. El Buffer Manager guarda la página en un frame libre.

6. **TX MANAGER** — Durante todo el proceso: gestiona locks de lectura (S-locks), registra operaciones en WAL, libera locks al COMMIT.

7. **DISCO** — Fuente última de los datos. Los 8KB de la página viajan: Disco → File Mgr → Buffer Pool → Executor → Aplicación.

**Figura:** Siete filas numeradas del 1 al 7. Cada fila tiene una etiqueta de color a la izquierda (PARSER en morado, OPTIMIZER en azul oscuro, EXECUTOR en verde, BUFFER MGR en naranja, FILE MGR en rojo-naranja, TX MANAGER en morado, DISCO en negro) y su descripción de texto a la derecha. Las flechas (→) indican el flujo secuencial de cada paso.

(slides 24)

## Laboratorio

### Actividades de la Semana

**01 Repaso PostgreSQL**

- Instalación y configuración de seguridad (pg_hba.conf, roles)
- Consultas SQL: SELECT, JOIN, subqueries, aggregations
- Procedimientos almacenados (PL/pgSQL básico)

**02 EXPLAIN ANALYZE**

- Ejecutar EXPLAIN ANALYZE sobre distintas queries
- Identificar Seq Scan vs Index Scan
- Analizar join methods: Nested Loop, Hash Join, Merge Join

**03 Exploración pg_catalog**

- Consultar pg_class para listar tablas e índices
- Inspeccionar pg_stats para ver histogramas de columnas
- Comparar n_distinct real vs estimado por el optimizer

**Figura:** Tres bloques de contenido dispuestos horizontalmente. El bloque «01 Repaso PostgreSQL» tiene encabezado azul a la izquierda. El bloque «02 EXPLAIN ANALYZE» tiene encabezado verde en el centro. El bloque «03 Exploración pg_catalog» tiene encabezado morado a la derecha. Cada bloque lista sus actividades con bullets.

(slides 26)

### EXPLAIN ANALYZE en PostgreSQL

EXPLAIN ANALYZE ejecuta la consulta y muestra el plan real con métricas de tiempo y filas.

```sql
EXPLAIN ANALYZE
  SELECT e.name, d.department_name
  FROM employees e
  JOIN departments d
    ON e.dept_id = d.id
  WHERE e.salary > 50000;
```

```text
-- Output del plan:
Hash Join (cost=12..45 rows=120)
  → Seq Scan on employees
  → Hash on departments
```

#### QUÉ OBSERVAR

| Métrica | Significado |
|---|---|
| cost= | Estimación del optimizer (startup..total) |
| rows= | Filas estimadas por el plan |
| actual time= | Tiempo real de ejecución (ms) |
| actual rows= | Filas realmente procesadas |
| loops= | Veces que se ejecutó el nodo |
| buffers: | Páginas leídas del buffer / disco |

**Figura:** La slide se divide en dos cajas oscuras. La caja izquierda contiene el ejemplo de consulta SQL con EXPLAIN ANALYZE y el output del plan de ejecución. La caja derecha, titulada «QUÉ OBSERVAR», lista las métricas del plan con sus descripciones.

(slides 27)

### Explorando pg_catalog

| Catálogo | Descripción | Columnas clave |
|---|---|---|
| pg_class | Tablas, índices, vistas, secuencias. | relname, relkind, reltuples, relpages |
| pg_attribute | Columnas de cada tabla/vista. | attname, atttypid, attnotnull, attnum |
| pg_statistic / pg_stats | Estadísticas para el optimizer. Histogramas, MCVs, n_distinct, correlation | |
| pg_index | Índices definidos en la BD. | indrelid, indkey, indisunique, indisprimary |
| pg_constraint | Restricciones PK, FK, UQ, Check. | conname, contype, conrelid, confrelid |
| information_schema | Vista estándar SQL (portable). | tables, columns, table_constraints, key_column_usage |

**Figura:** Seis cajas de colores organizadas en dos columnas de tres filas. Columna izquierda: «pg_class» (naranja-marrón), «pg_statistic / pg_stats» (durazno claro), «pg_constraint» (verde azulado). Columna derecha: «pg_attribute» (naranja-marrón), «pg_index» (azul), «information_schema» (morado). Cada caja muestra el nombre del catálogo a la izquierda en texto blanco y su descripción con columnas clave a la derecha en texto negro.

(slides 28)

## Glosario

- **Token:** Unidad mínima con significado en que el parser divide el texto SQL durante la tokenización.
- **AST (Abstract Syntax Tree / Árbol de Sintaxis Abstracta):** Estructura que el parser construye al verificar que la secuencia de tokens sigue las reglas gramaticales del SQL.
- **$\sigma$ (sigma):** Selección — filtra filas.
- **$\pi$ (pi):** Proyección — selecciona columnas.
- **$\bowtie$ (join):** Combina tablas por condición.
- **$\rho$ (rho):** Renombrado — renombra relaciones o atributos.
- **$\gamma$ (gamma):** Agrupamiento — GROUP BY con funciones de agregación.
- **System Catalog:** Fuente de verdad que el parser consulta (pg_class, pg_attribute, pg_type) para resolver cada nombre de tabla, columna y tipo.
- **Plan de Ejecución Físico:** Árbol de operadores concretos que produce el optimizer al elegir el plan de menor costo estimado.
- **Modelo Volcano / Iterator:** Cada nodo del plan implementa `open()`, `next()` y `close()`; evaluación pull-based / lazy.
- **Seq Scan (Sequential Scan):** Escaneo secuencial de todas las páginas de una tabla.
- **Index Scan:** Acceso a filas mediante índice; evita leer páginas irrelevantes.
- **Buffer Pool:** Área de memoria dividida en frames de tamaño fijo (igual al page size del disco).
- **Page Table:** Estructura hash que mapea disk_page_id → frame_number; incluye pin_count y dirty_bit por frame.
- **Dirty Page:** Página modificada en RAM que aún no fue escrita al disco.
- **Heap File:** Colección no ordenada de páginas; registros insertados al final.
- **Page / Block:** Unidad mínima de I/O (típicamente 4KB–16KB); contiene cabecera, slots de registros y espacio libre.
- **RID (Record ID):** Identificador físico único de cada tupla; RID = (page_id, slot_number).
- **ACID:** Atomicity (todo o nada), Consistency (estado válido a estado válido), Isolation (transacciones concurrentes no se ven entre sí), Durability (COMMIT confirmado sobrevive a fallos; el WAL lo garantiza).
- **WAL (Write-Ahead Log):** Cada cambio se escribe en el log ANTES de ir a disco; todo cambio debe registrarse en el log antes de que la página modificada se escriba en disco.
- **REDO (Roll-forward):** Re-aplica cambios de transacciones confirmadas que no llegaron a disco.
- **UNDO (Rollback):** Revierte cambios de transacciones incompletas al momento del crash.
- **Checkpoint:** Punto de sincronización donde todos los cambios hasta ahí están en disco; limita cuánto log debe reproducirse.
- **2PL (Two-Phase Locking):** Protocolo de locks con fase de crecimiento → punto de lock → decrecimiento.
- **Lock compartido (S) / exclusivo (X):** Tipos de locks para controlar acceso concurrente.
