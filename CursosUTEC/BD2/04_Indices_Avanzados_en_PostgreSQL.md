---
curso: BD2
titulo: 04 Indices Avanzados en PostgreSQL
slides: 11
fuente: 04 Indices Avanzados en PostgreSQL.pdf
---

# 04 Indices Avanzados en PostgreSQL

## Índice

- [Introducción](#introducción)
- [Limitaciones del B-Tree](#limitaciones-del-b-tree)
- [Necesidad de explorar índices avanzados](#necesidad-de-explorar-índices-avanzados)
- [BRIN (Block Range Index)](#brin-block-range-index)
  - [Concepto y estructura](#concepto-y-estructura)
  - [Ejemplo práctico y consideraciones de ordenamiento](#ejemplo-práctico-y-consideraciones-de-ordenamiento)
- [GiST (Generalized Search Tree)](#gist-generalized-search-tree)
  - [Concepto y características](#concepto-y-características)
  - [R-Tree](#r-tree)
- [SP-GiST (Space-Partitioned GiST)](#sp-gist-space-partitioned-gist)
  - [Concepto y aplicaciones](#concepto-y-aplicaciones)
  - [KD-Tree](#kd-tree)
- [Comparación General de Índices](#comparación-general-de-índices)
- [Glosario](#glosario)

## Introducción

### Agenda

1. BRIN
2. GiST
3. SP-GiST

PostgreSQL: Documentation: Indexes

Hellerstein et al. – Generalized Search Trees for Database Systems (GiST Paper)

**Figura:** Slide de portada con fondo fotográfico de un túnel o corredor circular futurista en tonos azules profundos, con patrones tecnológicos y líneas tipo circuito. En el centro, una persona vista de espaldas camina hacia el interior del túnel; una de sus piernas aparece como prótesis o extremidad robótica. En la parte superior central, el código y nombre del curso «CS2042 - BASES DE DATOS II». En el centro, el título principal «Índices Avanzados en PostgreSQL» en letras grandes blancas; debajo, «SEMANA 05» en cursiva. Una línea horizontal punteada amarilla separa el título de los datos del instructor: «Heider Sanchez» y «hsanchez@utec.edu.pe».

**Figura:** Slide dividida en dos zonas. en el centro un número grande «1.» con subrayado azul, un icono de portapapeles azul y el título «Índices Avanzandos En PostgreSQL». en esa franja, lista numerada vertical con «1. BRIN», «2. GiST» y «3. SP-GiST» en texto blanco. En la parte inferior izquierda, dos referencias en texto pequeño: enlace «PostgreSQL: Documentation: Indexes» y cita «Hellerstein et al. – Generalized Search Trees for Database Systems (GiST Paper)».

(slides 1–2)

## Limitaciones del B-Tree

- Óptimo para igualdad (=) y orden (<, >, BETWEEN).
- No es eficiente en búsquedas por similitud o intersección.
- No funciona bien con arrays, JSONB o datos espaciales.
- Índices B-Tree pueden ser grandes y costosos en inserciones masivas.

**Figura:** Diagrama de un árbol B-Tree jerárquico a la izquierda de los bullets. Nodo raíz con el valor `13`, con dos punteros hacia nodos intermedios. Nodo intermedio izquierdo con valores `9` y `11`; nodo intermedio derecho con valor `16`. Del nodo `9, 11` descienden tres nodos hoja: uno con `1` y `4`, otro con `9` y `10`, y otro con `11` y `12`. Del nodo `16` descienden dos nodos hoja: uno con `13` y `15`, y otro con `16`, `20` y `25`. Flechas conectan cada nodo padre con sus hijos.

(slide 3)

## Necesidad de explorar índices avanzados

- Los datos no siempre se consultan de la misma forma.
- Necesidad de búsquedas más complejas (espacio, texto, jerarquías).
- Mejorar rendimiento con grandes volúmenes de datos.
- Reducir el tamaño de los índices (e.g. BRIN).
- Soporte para estructuras especializadas como arrays, documentos o geometrías.

**Figura:** Título «Necesidad de explorar índices avanzados» en la parte superior. A la derecha, icono de un cilindro azul de tres niveles que representa una base de datos, con nodos conectados encima (círculos, cuadrados y rombos en verde, amarillo y azul) que ilustran relaciones o estructuras de datos complejas. Triángulo decorativo azul en la esquina superior izquierda.

(slide 4)

## BRIN (Block Range Index)

### Concepto y estructura

Almacena resúmenes de bloques de datos (mínimo/máximo).

Ideal para tablas grandes con ordenamiento natural (e.g. fechas).

Índices muy compactos y rápidos de construir.

Consultas aproximadas que reducen el número de bloques leídos.

Cuanto más ordenados estén los datos físicamente, más eficiente será el BRIN.

**Figura:** Diagrama técnico de la estructura interna de un índice BRIN. A la izquierda, un bloque etiquetado «meta». Encima de los bloques de datos, una sección etiquetada «revmap» con dos filas de ranuras verticales pequeñas. Líneas (punteros) conectan las ranuras del `revmap` con bloques de datos en la parte inferior, cada uno con un rango de valores: `1..10`, `11..20`, `21..30`, `71..80`, `41..50`, `61..70`, `31..42` (este bloque resaltado en amarillo), `81..90` y `91..100`. El diagrama muestra que el índice registra el mínimo y máximo de cada bloque para que el motor pueda omitir rangos completos de bloques que no contengan los datos buscados. En la parte inferior, la leyenda «Cuanto más ordenados estén los datos físicamente, más eficiente será el BRIN.» en texto pequeño.

(slide 5)

### Ejemplo práctico y consideraciones de ordenamiento

```sql
CREATE INDEX idx_brin_sequential ON Table USING BRIN (year);
```

¿Qué pasa si los registros no están ordenados en la fecha?

**Figura:** Diagrama dividido en dos secciones verticales. Sección superior etiquetada «BRIN Index» a la izquierda: dos columnas de rangos. Columna 1 con rango de páginas `1 - 2` y rango de valores `1947-1963`. Columna 2 con rango de páginas `3 - 4` y rango de valores `1964-1973`. Sección inferior etiquetada «Table» a la izquierda: secuencia horizontal de bloques divididos en Page 1, Page 2, Page 3 y Page 4, con cuadrados azules que representan registros individuales. Años anotados sobre las páginas: Page 1 inicia con `1947`, contiene `1951`; Page 2 contiene otro `1951` y termina en `1963`; Page 3 inicia con `1964`; Page 4 contiene `1972` y `1973`. Flechas punteadas conectan los bloques del índice BRIN con los rangos de páginas que cubren. Debajo del diagrama, el comando SQL `CREATE INDEX idx_brin_sequential ON Table USING BRIN (year);`. En la parte inferior, pregunta en texto rojo: «¿Que pasa si los registros no estan ordenados en la fecha?».

(slide 6)

## GiST (Generalized Search Tree)

### Concepto y características

Soporta múltiples tipos de consultas: igualdad, rango, proximidad.

Índices para datos espaciales (PostGIS), texto completo, etc.

Estructura de árbol balanceado como B-Tree.

Flexible y extensible mediante operadores personalizados.

Soporta estructuras como R-Tree y Inverted Index.

**Figura:** Diagrama de árbol de búsqueda a la izquierda y lista de características a la derecha. Nodo raíz con dos cajas de rango: `(1,1)-(6,3)` y `(5,5)-(8,8)`. Rama izquierda del raíz conduce a un nodo con tres puntos `(1,1)`, `(3,2)` y `(6,3)`, cada uno con flecha hacia abajo indicando punteros a filas de datos. Rama derecha conduce a un nodo con tres puntos `(5,5)`, `(7,8)` y `(8,6)`, cada uno con flecha hacia abajo.

(slide 7)

### R-Tree

**Figura:** La slide se divide en dos partes: diagrama lógico del árbol arriba y representación espacial abajo.

**Diagrama lógico del árbol (parte superior):** Tres niveles jerárquicos etiquetados «Root page», «Branch pages» y «Leaf pages». Nodo raíz con entradas **R1** y **R2**. **R1** apunta a un nodo de rama con entradas **R3**, **R4** y **R5**. **R2** apunta a un nodo de rama con entradas **R6** y **R7**. **R3** apunta a una hoja con **R8**, **R9** y **R10**. **R4** apunta a una hoja con **R11** y **R12**. **R5** apunta a una hoja con **R13** y **R14**. **R6** apunta a una hoja con **R15** y **R16**. **R7** apunta a una hoja con **R17**, **R18** y **R19**.

**Representación espacial (parte inferior):** Plano 2D con regiones rectangulares anidadas. **R1** (rectángulo discontinuo) cubre la porción superior izquierda y central del espacio. **R2** (rectángulo discontinuo) cubre la porción inferior derecha; R1 y R2 pueden solaparse. Dentro de **R1**, subregiones **R3**, **R4** y **R5**. Dentro de **R2**, subregiones **R6** y **R7**. Dentro de **R3**, tres regiones más pequeñas con objetos de datos: **R8** encierra el objeto **D1** (polígono irregular); **R9** encierra el objeto **D2** (círculo); **R10** encierra el objeto **D3** (triángulo). **R11** (rectángulo vertical alto) y **R12** (rectángulo horizontal) anidados dentro de **R4**. Regiones **R17**, **R18** y **R19** anidadas dentro de **R7**, con solapamiento significativo entre ellas.

(slide 8)

## SP-GiST (Space-Partitioned GiST)

### Concepto y aplicaciones

Índices basados en partición del espacio de datos.

Eficiente para estructuras como árboles trie, quadtrees, k-d trees.

Útil en búsquedas espaciales y de prefijos.

Permite crear índices especializados para ciertos tipos de datos.

No es adecuado para todos los tipos de consultas.

```sql
insert into sites values
('postgrespro.ru'),
('postgrespro.com'),
('postgresql.org'),
('planet.postgresql.org');
```

Indexes in PostgreSQL — 6 (SP-GiST) : Postgres Professional

**Figura:** Diagrama de árbol jerárquico tipo trie que indexa las cuatro URLs del ejemplo SQL. Nodo raíz con etiqueta «meta» que apunta a un nodo con la letra **'p'**. Desde **'p'**, dos ramas: rama **'l'** (para `pl...`) conduce a una hoja con el resto de la cadena `anet.postgresql.org` (completando `planet.postgresql.org`); rama **'o'** (para `po...`) conduce a un nodo con el prefijo común **`stgres`**. Desde **`stgres`**, dos ramas: rama **'q'** (para `postgresq...`) conduce a hoja `l.org` (completando `postgresql.org`); rama **'p'** (para `postgresp...`) conduce a un nodo con el segmento **`ro.`**. Desde **`ro.`**, dos ramas: rama **'c'** (para `postgrespro.c...`) conduce a hoja `om` (completando `postgrespro.com`); rama **'r'** (para `postgrespro.r...`) conduce a hoja `u` (completando `postgrespro.ru`). En la parte inferior, referencia «Indexes in PostgreSQL — 6 (SP-GiST) : Postgres Professional».

(slide 9)

### KD-Tree

**Figura:** La slide contiene tres diagramas bajo el subtítulo «KD-Tree».

**Diagrama izquierdo — Particionamiento espacial 2D:** Cuadrado que representa un espacio 2D dividido en regiones rectangulares por líneas verticales y horizontales correspondientes a los puntos A a F. Primera línea vertical pasa por el punto **A**. Línea horizontal a la izquierda de A pasa por el punto **B**. A la derecha de A, el espacio se subdivide: línea horizontal pasa por **C**; debajo de C, línea vertical pasa por **D**; en la partición inferior, línea horizontal pasa por **E**; el punto **F** reside en la sección inferior derecha resultante.

**Diagrama central — Estructura KD-Tree:** Árbol binario con particiones recursivas en ejes alternados. Nodo raíz **A (40, 45)**; línea discontinua etiquetada «**x**» indica que la primera división es en el eje x. Primer nivel: rama izquierda conduce a nodo **B (15, 70)**; rama derecha conduce a nodo **C (70, 10)** con línea discontinua etiquetada «**y**» (división en eje y). Segundo nivel: rama derecha de C conduce a nodo **D (69, 50)** con línea discontinua etiquetada «**x**». Tercer nivel: rama izquierda de D conduce a nodo **E (66, 85)**; rama derecha conduce a nodo **F (85, 90)** con línea discontinua etiquetada «**y**».

**Diagrama derecho — Particionamiento en mapa mundial:** Mapa del mundo donde las masas continentales (Américas, Europa, África, Asia, Australia) están delineadas por alta densidad de puntos azules. Superpuesta, una malla compleja de rectángulos de distintos tamaños que ilustra cómo un índice SP-GiST divide recursivamente el espacio de coordenadas globales en regiones más pequeñas, con particiones más finas en zonas de mayor densidad (costas, continentes poblados) que en áreas dispersas como océanos.

(slide 10)

## Comparación General de Índices

B-Tree:

- Ideal para búsquedas por igualdad (=) y orden (<, >, BETWEEN).
- Es el índice predeterminado.

BRIN (Block Range INdexes).

- Eficiente para grandes volúmenes de datos que tienen un orden natural (por ejemplo, fechas o series de tiempo).
- Bajo costo de almacenamiento y mantenimiento.

GiST (Generalized Search Tree):

- Soporta consultas generales sobre datos espaciales, textuales y tipos personalizados.
- Ideal para búsquedas por proximidad, intersección, similitud, etc.

SP-GiST (Space-Partitioned GiST):

- Optimizado para estructuras jerárquicas (como árboles) y espaciales con partición natural (trie, quadtrees, etc.).
  Útil cuando los datos están naturalmente dispersos.

**Figura:** Título «Comparación General de Índices» en la parte superior. Cuatro secciones con encabezados «B-Tree:», «BRIN (Block Range INdexes).», «GiST (Generalized Search Tree):» y «SP-GiST (Space-Partitioned GiST):», cada una con sus viñetas correspondientes.

(slide 11)

## Glosario

- **BRIN (Block Range Index):** Índice que almacena resúmenes de bloques de datos (mínimo/máximo). Ideal para tablas grandes con ordenamiento natural; índices muy compactos y rápidos de construir.
- **GiST (Generalized Search Tree):** Índice generalizado que soporta múltiples tipos de consultas (igualdad, rango, proximidad), con estructura de árbol balanceado como B-Tree, flexible y extensible mediante operadores personalizados.
- **SP-GiST (Space-Partitioned GiST):** Índice basado en partición del espacio de datos, eficiente para estructuras como árboles trie, quadtrees y k-d trees; útil en búsquedas espaciales y de prefijos.
