---
curso: BD2
titulo: 03 Tecnicas de Indexación-2
slides: 76
fuente: 03 Tecnicas de Indexación-2.pdf
---

# 03 Tecnicas de Indexación-2

## Índice

| Sección | Tema |
|---|---|
| 1 | [Métodos de Organización de Archivos — Sequential File](#métodos-de-organización-de-archivos--sequential-file) |
| 2 | [Binary Search Tree](#binary-search-tree) |
| 3 | [Agrupando Registros en Páginas](#agrupando-registros-en-páginas) |
| 4 | [Índice Dense vs Índice Sparse](#índice-dense-vs-índice-sparse) |
| 5 | [Sparse Index](#sparse-index) |
| 6 | [B+ Tree File](#b-tree-file) |
| 7 | [B+ Tree Index](#b-tree-index) |
| 8 | [Costo de operaciones (acceso a memoria secundaria)](#costo-de-operaciones-acceso-a-memoria-secundaria) |
| 9 | [Bitmap Index Scan en PostgreSQL](#bitmap-index-scan-en-postgresql) |
| 10 | [Hash File](#hash-file) |
| 11 | [Hash-based Index](#hash-based-index) |
| 12 | [Hash Indexes](#hash-indexes) |
| 13 | [Static Hashing](#static-hashing) |
| 14 | [Extendible Hashing](#extendible-hashing) |
| 15 | [Otras técnicas de hashing dinámico](#otras-técnicas-de-hashing-dinámico) |
| 16 | [Glosario](#glosario) |

## Métodos de Organización de Archivos — Sequential File

File Structures: An object-oriented approach with C++, Michael J. Folk. Addison Wesley, 3rd Edition, 1998.

### Sequential [Ordered] File

- Los registros se guardan de manera secuencial, usualmente basándose en la clave primaria de la tabla.
- Esto facilita un acceso ordenado y eficiente a los registros.
- Para lograr esto, es fundamental que el archivo conserve los registros organizados físicamente de acuerdo con el valor del campo de búsqueda (clave).
- Se puede acceder a un registro con $O(\log n)$ usando la estrategia de búsqueda binaria.

**datos.dat**

| Cod | Nombre | Ciclo |
|---|---|---|
| P-102 | Keiko | 5 |
| P-250 | Rafael | 7 |
| P-231 | Carlos | 3 |
| P-452 | Jorge | 5 |
| P-587 | Marisol | 1 |
| P-612 | Ricardo | 3 |
| P-682 | Fernando | 9 |

**Figura:** A la izquierda, el título «Sequential [Ordered] File» en negrita con subrayado, seguido de cuatro viñetas con el texto descrito. A la derecha, la tabla `datos.dat` con tres columnas (Cod, Nombre, Ciclo) y siete filas de datos. Una flecha azul vertical apunta hacia abajo a lo largo de la columna Cod, indicando el orden de almacenamiento secuencial.

(slides 2–3)

### Operaciones: Búsqueda binaria

**Búsqueda binaria en el archivo:**

- El algoritmo de búsqueda binaria se utiliza para encontrar un registro en el archivo con un valor de búsqueda $k$.
- Se necesitan $O(\log N)$ accesos a la memoria secundaria.
- Durante la búsqueda, es importante ignorar los registros que están marcados como eliminados.

```text
Require: k
l = 0
u = size() - 1
while u >= l do
    m = ⌊(l + u) / 2⌋
    re = readRecord(m)
    if re.key < k then
        u = m - 1
    else if re.key > k then
        l = m + 1
    else
        return m
    end if
end while
```

**Figura:** El título «Sequential File: Operaciones» en negrita con subrayado. Subtítulo «Búsqueda binaria en el archivo:» seguido de tres viñetas a la izquierda. A la derecha, un bloque de pseudocódigo enmarcado que describe el algoritmo de búsqueda binaria con las variables $k$, $l$, $u$, $m$ y la función `readRecord(m)`.

(slides 4)

### Operaciones: Mantenimiento del orden

- ¿Cómo se puede mantener el archivo siempre ordenado?
- ¿Cuál es el costo de insertar?
- ¿Cuál es el costo de eliminar?

**datos.dat**

| Cod | Nombre | Ciclo |
|---|---|---|
| P-102 | Keiko | 5 |
| P-250 | Rafael | 7 |
| P-231 | Carlos | 3 |
| P-452 | Jorge | 5 |
| P-587 | Marisol | 1 |
| P-612 | Ricardo | 3 |
| P-682 | Fernando | 9 |

**Figura:** El título «Sequential File: Operaciones» en negrita con subrayado. A la izquierda, tres preguntas en texto rojo. A la derecha, la tabla `datos.dat` con columnas Cod, Nombre y Ciclo, y siete filas de datos. Una flecha azul vertical apunta hacia abajo a lo largo de la columna Cod.

(slides 5)

### Estrategia del espacio extra

**Estrategia del espacio extra (1):**

- Las inserciones más recientes se guardan en un espacio extra.
- Debe haber un límite máximo de K registros en ese espacio adicional.
- La búsqueda debe realizarse en ambos espacios.
- De forma periódica, el archivo de datos debe ser reconstruido utilizando los registros del espacio extra.

**datos.dat**

| Cod | Nombre | Ciclo |
|---|---|---|
| P-102 | Keiko | 5 |
| P-250 | Rafael | 7 |
| P-231 | Carlos | 3 |
| P-452 | Jorge | 5 |
| P-587 | Marisol | 1 |
| P-612 | Ricardo | 3 |
| P-682 | Fernando | 9 |

**aux.dat**

| Cod | Nombre | Ciclo |
|---|---|---|
| P-312 | Gabriel | 3 |
| P-123 | Diana | 6 |
| … | | |

**Figura:** El título «Sequential File: Operaciones» en negrita con subrayado. Subtítulo «Estrategia del espacio extra (1):» seguido de cuatro viñetas a la izquierda. A la derecha, dos tablas apiladas: `datos.dat` (siete registros con flecha azul vertical en la columna Cod) y `aux.dat` (dos registros más puntos suspensivos indicando más registros hasta el límite K).

(slides 6)

### Estrategia del espacio adicional

**Estrategia del espacio adicional (2):**

- En el espacio adicional, también es posible organizar los registros según la clave.
- En este caso,
  - ¿Cuál sería la complejidad de acceso a memoria secundaria en operaciones de búsqueda e inserción?
  - ¿Cuál sería la complejidad al realizar la reconstrucción del archivo de datos?

**datos.dat**

| Cod | Nombre | Ciclo |
|---|---|---|
| P-087 | Saulo | 5 |
| P-150 | Carlos | 7 |
| P-262 | Mabel | 3 |
| P-331 | Josimar | 5 |
| P-487 | Jorge | 1 |
| P-512 | Cinthya | 3 |
| P-682 | Andrea | 9 |

**aux.dat**

| Cod | Nombre | Ciclo |
|---|---|---|
| P-223 | Gabriel | 6 |
| P-312 | Diana | 3 |
| P-655 | María | 7 |
| … | | |

**Figura:** El título «Sequential File: Operaciones» en negrita con subrayado. Subtítulo «Estrategia del espacio adicional (2):» seguido de viñetas a la izquierda, incluyendo dos sub-viñetas con preguntas sobre complejidad. A la derecha, dos tablas: `datos.dat` (siete registros ordenados por Cod con flecha azul vertical) y `aux.dat` (tres registros también ordenados por Cod con flecha azul vertical, más puntos suspensivos).

(slides 7)

### Estrategia de registros enlazados

**Estrategia de registros enlazados:**

- Determinar el lugar donde se incorporará el nuevo registro.
  - Si el espacio está disponible, proceder a la inserción.
  - Si no, guardar el registro en el espacio auxiliar.
    - En este caso, será necesario actualizar los punteros.
- Es fundamental reorganizar el archivo de datos de forma regular, integrando los registros del espacio auxiliar de manera ordenada.

**datos.dat**

| Id | Nombre | Ciclo |
|---|---|---|
| P-102 | Andrea | 5 |
| P-250 | Carlos | 7 |
| P-362 | Cinthya | 3 |
| P-231 | Josimar | 5 |
| P-087 | Jorge | 1 |
| P-312 | Mabel | 3 |
| P-982 | Saulo | 9 |

**aux.dat**

| Id | Nombre | Ciclo |
|---|---|---|
| P-312 | Gabriel | 3 |
| P-123 | Diana | 6 |

**Figura:** El título «Sequential File: Operaciones» en negrita con subrayado. Subtítulo «Estrategia de registros enlazados:» seguido de viñetas anidadas a la izquierda. A la derecha, las tablas `datos.dat` (7 registros) y `aux.dat` (2 registros). Flechas curvas azules conectan los registros en orden alfabético por Nombre a través de ambos archivos: Andrea (datos R1) → Carlos (datos R2) → Cinthya (datos R3) → Diana (aux R2) → Gabriel (aux R1) → Jorge (datos R5) → Josimar (datos R4) → Mabel (datos R6) → Saulo (datos R7). Una flecha azul vertical en la columna Nombre de `datos.dat` indica el orden físico original.

(slides 8)

### Inserción con punteros

**datos.dat**

| # | Id | Nombre | Ciclo | 1(d) |
|---|---|---|---|---|
| 1 | P-102 | Andrea | 5 | 2(d) |
| 2 | P-250 | Carlos | 7 | 3(d) |
| 3 | P-362 | Cinthya | 3 | 4(d) |
| 4 | P-231 | Josimar | 5 | 5(d) |
| 5 | P-087 | Jorge | 2 | 6(d) |
| 6 | P-312 | Mabel | 3 | 7(d) |
| 7 | P-982 | Saulo | 9 | -1(d) |

**Insertar**

| Id | Nombre | Ciclo |
|---|---|---|
| P-088 | Gabriel | 4 |
| P-312 | Gonzalo | 3 |
| P-087 | Maria | 2 |
| P-014 | Abel | 5 |

**aux.dat**

| # |
|---|
| 1 |
| 2 |
| 3 |
| 4 |

**Figura:** A la izquierda, la tabla `datos.dat` con siete registros y una columna de punteros (valores como `2(d)`, `3(d)`, …, `-1(d)`). Flechas azules enlazan cada puntero con la fila correspondiente en `datos.dat`. A la derecha, la sección «Insertar» con cuatro registros nuevos a insertar. Debajo, la tabla `aux.dat` vacía con cuatro filas numeradas (1 a 4) sin datos.

(slides 9)

### Eliminación de un registro

**Eliminación de un registro:**

- Se emplean los punteros para omitir los registros que han sido eliminados.
- Durante la reconstrucción del archivo, estos serán eliminados por completo.

| Id | Nombre | Ciclo | |
|---|---|---|---|
| P-102 | Andrea | 5 | → |
| P-250 | Carlos | 7 | → |
| P-362 | Cinthya | 3 | → (salta Josimar) |
| P-231 | ~~Josimar~~ | 5 | -1 |
| P-087 | Jorge | 1 | → (salta Mabel) |
| P-312 | ~~Mabel~~ | 3 | -1 |
| P-982 | Saulo | 9 | → |

Eliminar Josimar y Mabel

**Figura:** El título «Sequential File: Operaciones» en negrita con subrayado. Subtítulo «Eliminación de un registro:» seguido de dos viñetas a la izquierda. A la derecha, una tabla con columnas Id, Nombre, Ciclo y una columna de punteros. Los registros Josimar y Mabel aparecen tachados con puntero `-1`. Las flechas de los registros activos (Andrea, Carlos, Cinthya, Jorge, Saulo) omiten los registros eliminados: Cinthya salta a Jorge, Jorge salta a Saulo. En rojo debajo de la tabla: «Eliminar Josimar y Mabel».

(slides 10)

### Eliminación: Josimar, Jorge — Antes y después

→ Antes de eliminar

**datos.dat**

| # | Id | Nombre | Ciclo | 4(a) |
|---|---|---|---|---|
| 1 | P-102 | Andrea | 5 | 2(d) |
| 2 | P-250 | Carlos | 7 | 3(d) |
| 3 | P-362 | Cinthya | 3 | 1(a) |
| 4 | P-231 | Josimar | 5 | 5(d) |
| 5 | P-087 | Jorge | 2 | 6(d) |
| 6 | P-312 | Mabel | 3 | 3(a) |
| 7 | P-982 | Saulo | 9 | -1(d) |

**aux.dat**

| # | Id | Nombre | Ciclo | |
|---|---|---|---|---|
| 1 | P-088 | Gabriel | 4 | 2(a) |
| 2 | P-312 | Gonzalo | 3 | 4(d) |
| 3 | P-087 | Maria | 2 | 7(d) |
| 4 | P-014 | Abel | 5 | 1(d) |

→ Después de eliminar

**datos.dat**

| # | Id | Nombre | Ciclo | 4(a) |
|---|---|---|---|---|
| 1 | P-102 | Andrea | 5 | 2(d) |
| 2 | P-250 | Carlos | 7 | 3(d) |
| 3 | P-362 | Cinthya | 3 | 1(a) |
| 4 | ~~P-231~~ | ~~Josimar~~ | ~~5~~ | 0 |
| 5 | ~~P-087~~ | ~~Jorge~~ | ~~2~~ | 0 |
| 6 | P-312 | Mabel | 3 | 3(a) |
| 7 | P-982 | Saulo | 9 | -1(d) |

**aux.dat**

| # | Id | Nombre | Ciclo | |
|---|---|---|---|---|
| 1 | P-088 | Gabriel | 4 | 2(a) |
| 2 | P-312 | Gonzalo | 3 | 6(d) |
| 3 | P-087 | Maria | 2 | 7(d) |
| 4 | P-014 | Abel | 5 | 1(d) |

Eliminar: Josimar, Jorge

**Figura:** A la derecha, el texto «Eliminar: Josimar, Jorge» y «→ Antes de eliminar». Dos tablas: `datos.dat` (7 registros con punteros donde `(d)` indica referencia a `datos.dat` y `(a)` a `aux.dat`) y `aux.dat` (4 registros con punteros cruzados entre ambos archivos). En la versión posterior, las filas 4 y 5 de `datos.dat` (Josimar y Jorge) aparecen tachadas con puntero `0`. El puntero de Gonzalo en `aux.dat` cambió de `4(d)` a `6(d)`. La cadena lógica de punteros por nombre queda: Abel (aux R4) → Andrea (datos R1) → Carlos (datos R2) → Cinthya (datos R3) → Gabriel (aux R1) → Gonzalo (aux R2) → Mabel (datos R6) → Maria (aux R3) → Saulo (datos R7, puntero `-1(d)`).

(slides 11–12)

### Reconstrucción

**datos.dat**

| # | Id | Nombre | Ciclo | 1(d) |
|---|---|---|---|---|
| 1 | P-102 | Andrea | 5 | 2(d) |
| 2 | P-250 | Carlos | 7 | 3(d) |
| 3 | P-362 | Cinthya | 3 | 2(a) |
| 4 | ~~P-231~~ | ~~Josimar~~ | ~~5~~ | 0 |
| 5 | ~~P-087~~ | ~~Jorge~~ | ~~2~~ | 0 |
| 6 | P-312 | Mabel | 3 | 3(a) |
| 7 | P-982 | Saulo | 9 | 0(d) |

**aux.dat**

| # | Id | Nombre | Ciclo | |
|---|---|---|---|---|
| 1 | P-088 | Gonzalo | 4 | 6(d) |
| 2 | P-312 | Gabriel | 3 | 1(a) |
| 3 | P-087 | Maria | 2 | 7(d) |

**Reconstrucción**

| Id | Nombre | Ciclo |
|---|---|---|
| P-102 | Andrea | 5 |
| P-250 | Carlos | 7 |
| P-362 | Cinthya | 3 |
| P-312 | Gabriel | 3 |
| P-088 | Gonzalo | 4 |
| P-312 | Mabel | 3 |
| P-087 | Maria | 2 |
| P-982 | Saulo | 9 |

Insertar ordenadamente siguiendo los punteros

**Figura:** A la izquierda, las tablas `datos.dat` (con registros Josimar y Jorge tachados) y `aux.dat` (3 registros con punteros). Una flecha azul apunta hacia la tabla «Reconstrucción» a la derecha, que muestra los 8 registros activos en orden lógico. Debajo: «Insertar ordenadamente siguiendo los punteros». La cadena de punteros seguida es: Andrea (1) → Carlos (2) → Cinthya (3) → Gabriel (aux 2) → Gonzalo (aux 1) → Mabel (6) → Maria (aux 3) → Saulo (7, fin con `0(d)`).

**datos.dat** (7)

| # | Id | Nombre | Ciclo |
|---|---|---|---|
| 1 | P-102 | Andrea | 5 |
| 2 | P-250 | Carlos | 7 |
| 3 | P-362 | Cinthya | 3 |
| 4 | P-231 | Josimar | 5 |
| 5 | P-087 | Jorge | 2 |
| 6 | P-312 | Mabel | 3 |
| 7 | P-982 | Saulo | 9 |
| 8 | P-088 | Gonzalo | 4 |
| 9 | P-312 | Gabriel | 3 |
| 10 | P-087 | Maria | 2 |

**Reconstrucción**

| Id | Nombre | Ciclo |
|---|---|---|
| P-102 | Andrea | 5 |
| P-250 | Carlos | 7 |
| P-362 | Cinthya | 3 |
| P-312 | Gabriel | 3 |
| P-088 | Gonzalo | 4 |
| P-231 | Josimar | 5 |
| P-087 | Jorge | 2 |
| P-312 | Mabel | 3 |
| P-087 | Maria | 2 |
| P-982 | Saulo | 9 |

En la práctica, el espacio auxiliar se maneja en el mismo archivo de datos

**Figura:** La tabla `datos.dat` tiene un encabezado con el número «7» sobre la columna de índices. Las filas 1–7 están agrupadas con la etiqueta «ordenado» a la izquierda; las filas 8–10 con la etiqueta «no ordenado». Una flecha azul apunta de `datos.dat` hacia la tabla «Reconstrucción», que contiene 10 registros resultantes de fusionar el área no ordenada en el archivo principal. Texto inferior en azul: «En la práctica, el espacio auxiliar se maneja en el mismo archivo de datos».

**datos.dat** (7)

| # | Id | Nombre | Ciclo | Next |
|---|---|---|---|---|
| 1 | P-102 | Andrea | 5 | 2 |
| 2 | P-250 | Carlos | 7 | 3 |
| 3 | P-362 | Cinthya | 3 | 9 |
| 4 | P-231 | Josimar | 5 | 0 |
| 5 | P-087 | Jorge | 2 | 0 |
| 6 | P-312 | Mabel | 3 | 10 |
| 7 | P-982 | Saulo | 9 | -1 |
| 8 | P-088 | Gonzalo | 4 | 6 |
| 9 | P-312 | Gabriel | 3 | 8 |
| 10 | P-087 | Maria | 2 | 7 |

**Reconstrucción**

| Id | Nombre | Ciclo | |
|---|---|---|---|
| P-102 | Andrea | 5 | 2 |
| P-250 | Carlos | 7 | 3 |
| P-362 | Cinthya | 3 | 4 |
| P-312 | Gabriel | 3 | 5 |
| P-088 | Gonzalo | 4 | 6 |
| P-312 | Mabel | 3 | 7 |
| P-087 | Maria | 2 | 8 |
| P-982 | Saulo | 9 | -1 |

En la práctica, el espacio auxiliar se maneja en el mismo archivo de datos

**Figura:** Similar a la slide anterior, pero la tabla `datos.dat` incluye la columna «Next» con punteros enteros. Encabezado «7» sobre los índices. Filas 1–7 etiquetadas «ordenado»; filas 8–10 «no ordenado». Las filas 4 y 5 (Josimar y Jorge) están tachadas en rojo con `Next: 0`. La cadena lógica: 1→2→3→9→8→6→10→7→-1. Flecha azul hacia la tabla «Reconstrucción» con 8 registros activos y columna de secuencia (2, 3, 4, 5, 6, 7, 8, -1). Texto inferior en azul: «En la práctica, el espacio auxiliar se maneja en el mismo archivo de datos».

(slides 13–15)

### Resumen

Dos formas de manejar el espacio auxiliar

**Diagrama izquierdo — sin punteros:**

**datos.dat**

| Id | Nombre | Ciclo |
|---|---|---|
| P-102 | Andrea | 5 |
| P-250 | Carlos | 7 |
| P-362 | Cinthya | 3 |
| P-231 | Josimar | 5 |
| P-087 | Jorge | 1 |
| P-312 | Mabel | 3 |
| P-982 | Saulo | 9 |

**aux.dat**

| Id | Nombre | Ciclo |
|---|---|---|
| P-312 | Gabriel | 3 |
| P-123 | Diana | 6 |

- Search:
- Insert:
- Rebuild:
- Remove:

**Diagrama derecho — con punteros:**

Mismas tablas `datos.dat` y `aux.dat` con flechas curvas que enlazan los registros en orden: Andrea → Carlos → Cinthya → Gabriel (aux) → Josimar → Diana (aux) → Jorge → Mabel → Saulo → fin (símbolo nulo).

- Search:
- Insert:
- Rebuild:
- Remove:

**Figura:** Título «Sequential File: Resumen» en negrita con subrayado. Texto central «Dos formas de manejar el espacio auxiliar». Dos diagramas lado a lado: a la izquierda, las tablas `datos.dat` y `aux.dat` separadas sin flechas de enlace; a la derecha, las mismas tablas con flechas curvas que definen la secuencia lógica entre registros de ambos archivos. Debajo de cada diagrama, una lista de operaciones (Search, Insert, Rebuild, Remove) con campos vacíos.

(slides 16)

### Ventajas y desventajas

**Ventajas**

- Búsquedas eficientes

**Desventajas**

- Son difíciles de mantener.
  - Inserciones y eliminaciones requieren de una localización previa del registro.
- Costo extra para reorganizar el archivo.

| Id | Nombre | Ciclo | |
|---|---|---|---|
| P-102 | Andrea | 5 | → |
| P-250 | Carlos | 7 | → |
| P-362 | Cinthya | 3 | → |
| P-231 | Josimar | 5 | → |
| P-087 | Jorge | 1 | → |
| P-312 | Mabel | 3 | → |
| P-982 | Saulo | 9 | ↓ |

**Figura:** Título «Sequential File» en negrita con subrayado. A la izquierda, secciones «Ventajas» (con sub-viñeta «Búsquedas eficientes») y «Desventajas» (con sub-viñetas anidadas sobre mantenimiento e inserciones/eliminaciones, y costo de reorganización). A la derecha, tabla con columnas Id, Nombre, Ciclo y una columna sin encabezado con flechas curvas azules que enlazan cada fila con la siguiente en secuencia física; la última flecha apunta hacia abajo fuera de la tabla.

(slides 17)

## Binary Search Tree

### Concepto y preguntas

- ¿Qué tal si organizamos los registros utilizando la estrategia de Árbol Binario de Búsqueda?
  - Lo denominaremos BST File
- ¿De qué manera se modifica el archivo?
- ¿Cuál es la complejidad para insertar, eliminar y buscar?
- ¿Cómo aseguramos que el árbol se mantenga balanceado en todo momento (AVL File)?

**Figura:** Título «Binary Search Tree» en negrita con subrayado. Cuatro viñetas con preguntas en español sobre la organización de registros mediante BST File y AVL File.

(slides 18)

### Estructura en archivo

| | Cod | Nombre | Ciclo | Left | Right |
|---|---|---|---|---|---|
| 1 | P-271 | Josimar | 5 | 2 | 3 |
| 2 | P-255 | Manuel | 8 | 4 | -1 |
| 3 | P-362 | Cinthya | 3 | -1 | 5 |
| 4 | P-224 | Andrea | 2 | -1 | -1 |
| 5 | P-887 | Benjamin | 9 | -1 | -1 |

**Figura:** Título «Binary Search Tree» en negrita con subrayado. Tabla con 5 registros indexados (1 a 5) y columnas Cod, Nombre, Ciclo, Left, Right. El árbol binario de búsqueda representado tiene como raíz el índice 1 (P-271, Josimar): hijo izquierdo índice 2 (P-255, Manuel), hijo derecho índice 3 (P-362, Cinthya). Del nodo 2: hijo izquierdo índice 4 (P-224, Andrea), hijo derecho -1. Del nodo 3: hijo izquierdo -1, hijo derecho índice 5 (P-887, Benjamin). Los nodos 4 y 5 son hojas (Left y Right = -1).

(slides 19)

## Agrupando Registros en Páginas

### Organización en páginas

- En la práctica, el archivo secuencial se organiza en paginas manteniendo el orden lexicográfico en función de la llave.

| Cod | Nombre | Ciclo |
| :--- | :--- | :--- |
| P-102 | Keiko | 5 |
| P-250 | Rafael | 7 |
| P-231 | Carlos | 3 |
| P-452 | Jorge | 5 |
| P-587 | Marisol | 1 |
| P-612 | Ricardo | 3 |
| P-682 | Fernando | 9 |

**Page 1**

| RID | Cod | Nombre | Ciclo |
| :--- | :--- | :--- | :--- |
| 1 | P-102 | Keiko | 5 |
| 2 | P-250 | Rafael | 7 |
| 3 | P-231 | Carlos | 3 |

**Page 2**

| RID | Cod | Nombre | Ciclo |
| :--- | :--- | :--- | :--- |
| 4 | P-452 | Jorge | 5 |
| 5 | P-587 | Marisol | 1 |
| 6 | P-612 | Ricardo | 3 |

…

**Figura:** Título «Agrupando Registros en Páginas» en la parte superior. Una viñeta explica la organización en páginas manteniendo orden lexicográfico por llave. A la izquierda, una tabla con columnas Cod (subrayada, indicando llave), Nombre y Ciclo con siete registros. Una flecha azul apunta desde esa tabla hacia la derecha, donde se muestran dos tablas etiquetadas «Page 1» y «Page 2», cada una con columnas RID, Cod (subrayada), Nombre y Ciclo con tres registros por página. Después de Page 2 aparece un elipsis (…) indicando páginas adicionales (el registro P-682 Fernando quedaría en una página subsiguiente). En la esquina superior derecha, icono de silueta de cabeza humana con campana de notificación.

(slides 21)

### Bloques

- Los bloques son las unidades básicas de almacenamiento en un dispositivo físico, como un disco duro o una unidad SSD.
  - El sistema de archivos organiza los datos de un archivo en bloques para su almacenamiento y recuperación.
  - El tamaño de los bloques lo define el sistema de archivos y el dispositivo de almacenamiento, son unidades del tamaño que pueden variar.

**Figura:** Slide titulada «Agrupando Registros en Páginas». Tres viñetas explican el concepto de bloques como unidades básicas de almacenamiento. En la parte inferior, tres diagramas: (1) Una secuencia horizontal de cinco cajas conectadas por flechas bajo la etiqueta «File A», etiquetadas «File block 0» hasta «File block 4»; sobre «File block 4» hay un «0» con flecha saliente que representa un puntero nulo o fin de archivo. (2) Una lupa o efecto de expansión desde «File block 4» hacia un rectángulo vertical más grande dividido en cuatro secciones horizontales etiquetadas «Record 1», «Record 2», «Record 3» y «Record 4», mostrando cómo múltiples registros se agrupan dentro de un bloque. (3) En la esquina inferior derecha, un diagrama de hardware con una caja «Disk» (disco) y un chip «Cache» (RAM) conectados por una flecha de doble sentido que indica transferencia de bloques de datos entre almacenamiento secundario y memoria principal.

(slides 22)

### Paginación y memoria virtual

- La paginación se utiliza para la gestión de la memoria virtual, que puede incluir partes de archivos que se cargan en la RAM.
  - La paginación divide archivos grandes en páginas más pequeñas de tamaño fijo, no necesariamente del tamaño de un bloque.
  - La uniformidad del tamaño de las páginas simplifica la gestión de la memoria, ya que el sistema operativo puede realizar un seguimiento y asignar la memoria de manera más eficiente.

**Figura:** Slide titulada «Agrupando Registros en Páginas». Tres viñetas sobre paginación y memoria virtual. En la parte inferior, los mismos tres diagramas de la slide anterior: secuencia de bloques «File A» (File block 0 a File block 4) conectados por flechas; detalle de «File block 4» expandido mostrando Record 1, Record 2, Record 3 y Record 4 dentro del bloque; y diagrama Disk–Cache con flecha bidireccional.

(slides 23)

### Caso 1: Registro menor que el bloque

Se presentan dos casos:

1. La longitud del registro es menor que el tamaño del bloque
   - Este es el caso más común
   - El máximo número de registros que son almacenados dentro de un bloque es llamado "blocking factor": $b = \lfloor B/r \rfloor$, en donde:
     - $B$ es el tamaño del bloque en bytes
     - $r$ la longitud del registro en bytes

**Figura:** Slide titulada «Agrupando Registros en Páginas». Texto introductorio «Se presentan dos casos:». El caso 1 describe registros más cortos que el bloque, con dos sub-viñetas. La fórmula del blocking factor aparece con la notación de piso (floor): $b = \lfloor B/r \rfloor$, seguida de las definiciones de $B$ (tamaño del bloque en bytes) y $r$ (longitud del registro en bytes). La palabra «menor» aparece en negrita.

(slides 24)

### Caso 2: Registro mayor que el bloque

2. La longitud del registro es mayor que el tamaño del bloque
   - Se utiliza la organización extendida (spanned organization).
   - Un registro extendido puede abarcar diferentes bloques.
   - **File Blocks:** secuencia de bloques que contienen todos los registros del archivo.

**Figura:** Slide titulada «Agrupando Registros en Páginas». Caso 2: registro más largo que el bloque. Tres viñetas sobre organización extendida (spanned organization). Diagrama de cinco bloques rectangulares conectados secuencialmente por flechas: Bloque 1 contiene completamente el registro 1; Bloque 2 está dividido con el resto del registro 1 y el inicio del registro 2; Bloque 3 contiene el resto del registro 2; Bloque 4 contiene el inicio del registro 3; Bloque 5 contiene el resto del registro 3 y espacio vacío. La palabra «mayor» aparece en cursiva.

2. La longitud del registro es mayor que el tamaño del bloque
   - También se utiliza organización extendida para evitar espacios libres en los buffers.

Leer más …
*File Structures: an object oriented approach with C++.* Michael Folk. **Chapter 4.**

**Figura:** Slide titulada «Agrupando Registros en Páginas». Continuación del caso 2 con viñeta sobre evitar espacios libres en buffers mediante organización extendida. Diagrama de dos bloques: **Block $i$** contiene Record 1, Record 2, Record 3 y el inicio de Record 4, con una caja pequeña «P» (puntero) al final; una flecha conecta el segmento de Record 4 en Block $i$ con **Block $i+1$**, que comienza con «Record 4 (rest)», seguido de Record 5, Record 6, Record 7 y otra caja «P». Michael Folk.

(slides 25–26)

## Índice Dense vs Índice Sparse

File Structures: An object-oriented approach with C++, Michael J. Folk. Addison Wesley, 3rd Edition, 1998.

### Dense Index-file

**Dense Index-file:**

- Contiene una entrada para cada registro en el archivo de datos.
- Permite búsquedas muy rápidas de registros individuales, ya que cada registro tiene su propia entrada en el índice.

¿Ventajas y Desventajas?

**Index.dat**

| Nombre | Ubicación |
| :--- | :--- |
| Carlos | R3 |
| Fernando | R7 |
| Jorge | R4 |
| Keiko | R1 |
| Marisol | R5 |
| Rafael | R2 |
| Ricardo | R6 |

**Data.dat**

| | Código | Nombre | Ciclo |
| :--- | :--- | :--- | :--- |
| R1 | P-087 | Keiko | 5 |
| R2 | P-102 | Rafael | 7 |
| R3 | P-231 | Carlos | 3 |
| R4 | P-250 | Jorge | 5 |
| R5 | P-312 | Marisol | 1 |
| R6 | P-362 | Ricardo | 3 |
| R7 | P-982 | Fernando | 9 |

**Figura:** Slide titulada «Índice Dense vs Índice Sparse». Lado izquierdo: definición de Dense Index-file con dos viñetas y pregunta en rojo «¿Ventajas y Desventajas?». Lado derecho: dos tablas conectadas por flechas. «Index.dat» con columnas Nombre y Ubicación, entradas ordenadas alfabéticamente por nombre apuntando a IDs de registro (R1–R7). «Data.dat» con registros R1–R7, columnas Código, Nombre y Ciclo; los datos no están ordenados por nombre. Flechas conectan cada entrada del índice con su registro correspondiente en el archivo de datos (relación 1 a 1).

(slides 28)

### Sparse Index-file

**Sparse Index-file:**

- Contiene entradas solo para algunos registros en el archivo de datos, generalmente el primer registro en cada página de datos.
- Para encontrar un registro específico, primero se busca en el índice el bloque que podría contener el registro y luego se busca secuencialmente dentro del bloque asociado.
- *Sólo posible si datos están ordenados.*

¿Ventajas y Desventajas?

**Sparse Index**

| first_name | location |
| :--- | :--- |
| Cameron | → Block 1 |
| Flynn | → Block 2 |
| Loyd | → Block 3 |
| Shepherd | → Block 4 |

**Data File**

| first_name | last_name | email | phone |
| :--- | :--- | :--- | :--- |
| Cameron | Vance | c.vance@company.biz | |
| Cedric | Myles | c.myles@company.biz | |
| Darell | Winifred | d.winnifred@company.biz | |
| Davis | Thornton | d.thornton@company.biz | |
| Flynn | Gilbert | f.gilbert@company.biz | |
| Hamilton | Judith | h.judith@company.biz | |
| Isabel | Brenna | i.brenna@company.biz | |
| Kiley | Hardy | k.hardy@company.biz | |
| Loyd | Lucius | l.lucius@company.biz | |
| Minerva | Reid | m.reid@company.biz | |
| Oscar | Nathan | o.nathan@company.biz | |
| Rachelle | Debra | r.debra@company.biz | |
| Shepherd | Dylan | s.dylan@company.biz | |
| Susan | Tobias | s.tobias@company.biz | |
| Valerie | Raleigh | v.raleigh@company.biz | |
| Velvet | Clyde | v.clyde@company.biz | |

**Figura:** Slide titulada «Índice Dense vs Índice Sparse». Lado izquierdo: definición de Sparse Index-file con tres viñetas (la tercera en azul cursiva: «Sólo posible si datos están ordenados») y pregunta en rojo «¿Ventajas y Desventajas?». Lado derecho: diagrama estilo dibujo a mano. Tabla Sparse Index con columnas first_name y location; cuatro entradas (Cameron, Flynn, Loyd, Shepherd) con flechas apuntando a bloques del Data File. El Data File se organiza en cuatro bloques de cuatro filas cada uno, con columnas first_name, last_name, email y phone, ordenados alfabéticamente por first_name. Cada entrada del índice apunta al primer registro de su bloque correspondiente.

(slides 29)

## Sparse Index

### Construcción

- Construcción:

**Figura:** Slide titulada «Sparse Index» con subtítulo «Construcción:». Diagrama de dos niveles. **Index File** (arriba): rectángulo horizontal dividido en segmentos alternando punteros ($P$) y claves ($K$): $P_0$, $K_1$, $P_1$, $K_2$, $P_2$, …, $K_m$, $P_m$. **Data File** (abajo): rectángulo largo con páginas etiquetadas Page 0, Page 1, Page 2, …, Page m. Flechas desde $P_0$, $P_1$, $P_2$ y $P_m$ apuntan al inicio de Page 0, Page 1, Page 2 y Page m respectivamente. En el pie izquierdo, URL: https://dsf.berkeley.edu/dbcourse/lecs/lecture5.pdf.

(slides 30)

### Inserción — Condición 1: Hay espacio en el índice

- Construcción

¿Cómo insertar un nuevo registro?

**Condición 1: Hay espacio en el índice**

- Dividir la página en dos
- Insertar nueva key en el Page Index

**Figura:** Slide titulada «Sparse Index» con subtítulo «Construcción». Pregunta central «¿Cómo insertar un nuevo registro?». **Index File**: secuencia $[P_0]$ $[K_1]$ $[P_1]$ $[K_2]$ $[P_2]$ … $[K_c]$ $[P_c]$ seguida de celdas vacías. **Data File**: contenedor con Page 0, Page 1, Page 2, Page 3 hasta Page c. Fuera del contenedor principal, una caja «Page c + 1» con flecha naranja desde el área del índice indicando división o nueva entrada. Flechas negras desde $P_0$, $P_1$, $P_2$ y $P_c$ apuntan a Page 0, Page 1, Page 2 y Page c. Texto a la derecha describe Condición 1 (hay espacio en el índice): dividir la página en dos e insertar nueva key en el Page Index.

(slides 31)

### Inserción — Condición 2: No hay espacio en el índice

- Construcción

¿Cómo insertar un nuevo registro?

**Condición 2: No hay espacio en el índice**

- Crear nueva pagina con un solo registro
- Encadenar nueva pagina a la pagina actual

**Figura:** Slide titulada «Sparse Index» con subtítulo «Construcción». Pregunta «¿Cómo insertar un nuevo registro?». **Index File**: secuencia $P_0$, $K_1$, $P_1$, $K_2$, $P_2$, …, $K_m$, $P_m$. **Data File**: Page 0, Page 1, Page 2, Page 3, Page m. Flechas negras desde punteros del índice a las páginas correspondientes. A la derecha de Page m, bloque adicional «Page m + 1» con dos flechas curvas naranjas bidireccionales entre Page m y Page m + 1, indicando encadenamiento. Texto en naranja al pie describe Condición 2: no hay espacio en el índice — crear nueva página con un solo registro y encadenarla a la página actual.

(slides 32)

### Multilevel Index-File

**Multilevel Index-File:**

- Cuando los archivos de datos son muy grandes, un índice de un solo nivel puede ser ineficiente para las búsquedas.
- La indexación multinivel soluciona esto al establecer una jerarquía de índices, donde el índice superior dirige a bloques de entradas en niveles inferiores, hasta llegar a los registros de datos.

**Figura:** Slide titulada «Sparse Index» con subtítulo «Multilevel Index-File:». Dos viñetas explican la indexación multinivel. Diagrama jerárquico de tres niveles. **Nivel superior (index page / raíz):** un bloque con valores 8180 y 8910; tres flechas descendentes (desde slot izquierdo sin etiqueta, desde 8180 y desde 8910) apuntan a tres bloques del nivel medio. **Nivel medio (index pages):** tres bloques — izquierdo con 4222, 4528, 6330, 8050; central con 8280, 8570, 8604, 8808; derecho con 9016, 9532 y dos slots vacíos. Cada valor tiene flecha hacia abajo. **Nivel inferior (data pages):** fila continua de 25 cajas con valores: 4104*, 4123*, 4222*, 4450*, 4528*, 5012*, 6330*, 6423*, 8050*, 8105*, 8180*, 8245*, 8280*, 8406*, 8570*, 8600*, 8604*, 8700*, 8808*, 8887*, 8910*, 8953*, 9016*, 9200*, 9532* (asterisco indica clave del primer registro de cada página). Etiquetas laterales «index pages» y «data pages».

(slides 33)

### B+Tree: combinación de índices dense y sparse

El B+Tree combina ambos mundos: nodos hoja actúan como índice denso sobre las páginas de datos.

**Figura:** Slide titulada «Sparse Index». Diagrama jerárquico de un B+Tree. **Nodo superior (interno):** rectángulo horizontal con celdas $P_0$, $K_1$, $P_1$, $K_2$, $P_2$, …, $K_m$, $P_m$; dos flechas descendentes desde $P_0$ (al nodo hijo izquierdo) y $P_1$ (al nodo hijo derecho). **Nodos inferiores (hijos):** dos rectángulos idénticos con la misma estructura $P_0$, $K_1$, $P_1$, $K_2$, $P_2$, …, $K_m$, $P_m$. Barra azul clara en el pie con el texto «El B+Tree combina ambos mundos: nodos hoja actúan como índice denso sobre las páginas de datos.» Logo de UTEC en la esquina inferior derecha.

(slides 34)

## B+ Tree File

- Es una estructura de datos de árbol auto-balanceada que mantiene los datos ordenados y permite búsquedas, accesos secuenciales, inserciones y eliminaciones en tiempo logarítmico.
- Están optimizados para operaciones de E/S de disco, ya que minimizan el número de accesos al disco necesarios para encontrar un registro.
- Esto se logra al agrupar múltiples claves en cada nodo, lo que reduce la altura del árbol.

**Figura:** Slide dividida diagonalmente. Lado izquierdo: fotografía con filtro azul de científico de laboratorio trabajando con tubos de ensayo y pipeta.

(slides 35)

## B+ Tree Index

### Propiedades

**Propiedades del B+ Tree:**

- Todos los nodos hoja deben estar al mismo nivel de altura.
- Los nodos hoja apuntan a los registros reales en el archivo de datos.
  - Todos los nodos hoja están conectados de manera similar a una lista enlazada.
- Los nodos internos forman el directorio del índice.
  - Los nodos internos no contienen información del archivo de datos.
- Los nodos deben estar siempre llenos al menos en su mitad.

**Figura:** Slide titulada «B+ Tree Index». Lado izquierdo: diagrama con «Index Entries (Direct search)» representado por un triángulo grande con flecha apuntando a la raíz; flechas desde la base del triángulo hacia «Data Entries (Records)» — fila de cajas rectangulares en la parte inferior (nodos hoja); flechas de doble sentido conectan horizontalmente los nodos hoja (lista enlazada). Lado derecho: lista de «Propiedades del B+ Tree» con viñetas y sub-viñetas.

(slides 36)

### Clustered and Unclustered

**CLUSTERED** | **UNCLUSTERED**

(Index File)

Data entries → Data Records

(Data file)

**Figura:** Slide titulada «B+ Tree Index: Clustered and Unclustered». Comparación lado a lado separada por una línea horizontal que marca el límite entre «(Index File)» arriba y «(Data file)» abajo. **Lado izquierdo (CLUSTERED):** árbol B+ representado por triángulo en la parte superior; en el nivel inferior del índice, tres cajas rectangulares azules «Data entries» (nodos hoja) conectadas horizontalmente con flechas de doble sentido; flechas verdes desde los nodos hoja apuntan secuencial y ordenadamente a cuadrados verdes «Data Records» en el archivo de datos; la etiqueta «CLUSTERED» en rojo mayúsculas al pie. **Lado derecho (UNCLUSTERED):** estructura similar con triángulo y tres «Data entries» enlazados; flechas verdes cruzadas y entrelazadas desde los nodos hoja hacia ubicaciones no contiguas en los «Data Records»; la etiqueta «UNCLUSTERED» en rojo mayúsculas al pie.

Index File

Index entries

direct search for

data entries

**CLUSTERED** | **UNCLUSTERED**

Leaf nodes

Data file

Leaf nodes

**Figura:** Slide titulada «B+ Tree Index: Clustered and Unclustered». Comparación de índices agrupados y no agrupados. Línea horizontal separa «Index File» (arriba) de «Data file» (abajo). Texto central en naranja: «Index File: Index entries direct search for data entries». **CLUSTERED (izquierda):** árbol jerárquico (triángulo) con nodos intermedios; los **Leaf nodes** (etiqueta naranja) están **debajo** de la línea, dentro del área «Data file»; flechas rectas y paralelas desde el índice hacia bloques contiguos en el archivo de datos; el orden físico coincide con el orden lógico. **UNCLUSTERED (derecha):** árbol similar arriba; los **Leaf nodes** (etiqueta naranja) están **arriba** de la línea, dentro del «Index File», enlazados horizontalmente; punteros azules cruzados apuntan a bloques de datos (rectángulos con borde azul) debajo de la línea; el orden físico no coincide con el lógico.

(slides 37–38)

### Clustered index

**CLUSTERED**

Para crear un índice agrupado, primero se debe organizar el archivo de datos, dejando espacio extra en cada página para futuras inserciones.

**Figura:** Slide titulada «B+ Tree Index: clustered index». Lado izquierdo: diagrama jerárquico con etiqueta «CLUSTERED» en rojo mayúsculas. Triángulo blanco en la parte superior (raíz y niveles no-hoja) con flecha apuntando al vértice. Tres flechas negras desde la base del triángulo hacia una fila de tres cajas rectangulares (nodos intermedios/hoja). Flechas naranjas desde esas cajas hacia una fila inferior de cajas más pequeñas (páginas de datos). Flecha horizontal de doble sentido en naranja conecta los grupos de páginas de datos (lista enlazada entre páginas hoja). Lado derecho: párrafo explicativo sobre organizar el archivo de datos dejando espacio extra para futuras inserciones.

(slides 39)

**Raíz:** A-202 | A-349

**Nivel intermedio:**

| A-100 | A-120 | | A-256 | | A-387 |

**Data File**

| Código | Nombre | Ciclo |
| :--- | :--- | :--- |
| A-024 | Abel | 2 |
| A-100 | Ana | 2 |
| A-110 | Benito | 5 |
| A-120 | Berta | 1 |
| A-202 | Carlos | 3 |
| A-256 | Olenky | 4 |
| A-307 | Pablo | 9 |
| A-349 | Paolo | 4 |
| A-387 | Pedro | 9 |
| A-449 | Sofia | 4 |

Los nodos internos forman una jerarquía de índices dispersos.

**Figura:** Slide titulada «B+ Tree Index: clustered index». Diagrama completo de árbol B+ agrupado con tres niveles. **Raíz:** claves A-202 y A-349 con tres punteros grises a nodos intermedios. **Nivel intermedio:** nodo izquierdo con A-100 y A-120 (tres punteros); nodo central con A-256 (dos punteros); nodo derecho con A-387 (dos punteros). **Nivel hoja** (rectángulo azul punteado): siete nodos pequeños conectados por flechas azules de izquierda a derecha (lista enlazada); cada nodo tiene punteros grises hacia registros en el Data File. **Data File** (etiqueta lateral con flecha curva): registros ordenados por clave, cada uno con tres columnas (ID, Nombre, Valor): A-024|Abel|2, A-100|Ana|2, A-110|Benito|5, A-120|Berta|1, A-202|Carlos|3, A-256|Olenky|4, A-307|Pablo|9, A-349|Paolo|4, A-387|Pedro|9, A-449|Sofia|4. Texto al pie: «Los nodos internos forman una jerarquía de índices dispersos.» Logo de UTEC en la esquina inferior derecha.

(slides 40)

**Características:**

- Solo puede existir UN índice agrupado por tabla (el archivo tiene un único orden físico).
- Ventaja en Búsqueda por Rango [a, b]:
  - Se leen páginas contiguas → mínimo I/O.
- En InnoDB (MySQL):
  - La PK es siempre el clustered index; las hojas contienen el registro completo (índice en árbol = tabla).
- En PostgreSQL:
  - Se ejecuta `CLUSTER table USING index`, reorganiza el data file (heap), pero el orden no se mantiene automáticamente.

**Figura:** Diagrama con dos cajas conectadas por flechas horizontales.

**Caja izquierda — «Índice B+Tree (clustered)»:** Contiene un nodo hoja con tres entradas:
- `[5 → Pág1]` — flecha hacia la Pág 1 del archivo de datos.
- `[25 → Pág2]` — flecha hacia la Pág 2 del archivo de datos.
- `[48 → Pág3]` — flecha hacia la Pág 3 del archivo de datos.

**Caja derecha — «Archivo de datos (ordenado por k)»:** Tres páginas con registros ordenados por clave:
- **Pág 1:** k=5, k=10, k=15, k=20
- **Pág 2:** k=25, k=30, k=37, k=42
- **Pág 3:** k=48, k=52, k=60, k=75

**Leyenda inferior:** «Orden del índice = orden físico de las páginas de datos».

(slides 41)

### Unclustered index

**Figura:** Diagrama de un índice B+ Tree no agrupado sobre un Data File.

**Nivel raíz (nodo interno):** Contiene las claves `A-102` y `A-249`, con tres punteros hacia el nivel inferior.

**Nivel hoja (tres nodos enlazados horizontalmente con flechas azules):**

1. **Nodo izquierdo:** claves `A-024`, `A-101`, `A-102`. Cada clave tiene un puntero hacia un registro en el Data File.
2. **Nodo central:** claves `A-202`, `A-249`. Cada clave tiene un puntero hacia un registro en el Data File.
3. **Nodo derecho:** claves `A-357`, `A-856`. Cada clave tiene un puntero hacia un registro en el Data File.

**Data File (área sombreada en azul, etiquetada «Data File» en la esquina inferior derecha):** Siete registros en orden físico (de izquierda a derecha), no ordenados por clave:

| ID | Nombre | Valor |
|---|---|---|
| A-101 | Ana | 2 |
| A-024 | Jorge | 5 |
| A-102 | Maria | 1 |
| A-202 | Paul | 3 |
| A-856 | Marlon | 4 |
| A-357 | Lesly | 9 |
| A-249 | Pablo | 4 |

Los punteros desde los nodos hoja cruzan hacia registros dispersos en el Data File (por ejemplo, `A-024` apunta al segundo registro, `A-101` al primero).

**Anotaciones en la parte inferior izquierda:**
- Los nodos internos forman una jerarquía de índices dispersos.
- Los nodos hojas son índices densos.

(slides 42)

**Características:**

- Costo de range scan:
  - Potencialmente O(1) I/O por registro si las páginas están dispersas → heap fetch.
- Index-only scan:
  - Si todos los campos de la consulta están en el índice, no se accede al heap.
- Covering index:
  - índice no agrupado que incluye todas las columnas necesarias → evita heap fetch.
- PostgreSQL usa bitmap index scan para agrupar RIDs antes de leer el heap.

**Figura:** Diagrama con dos cajas conectadas por flechas.

**Caja izquierda — «Índice B+Tree (non-clustered)»:** Nodo hoja con cuatro entradas:
- `edad=22 →` apunta a Pág 7: RID=(7, 3)
- `edad=25 →` apunta a Pág 2: RID=(2, 1)
- `edad=30 →` apunta a Pág 4: RID=(4, 2)
- `edad=35 →` apunta a Pág 1: RID=(1, 4)

**Caja derecha — «Heap (datos desordenados)»:** Cuatro páginas con RIDs:
- Pág 7: RID=(7, 3)
- Pág 2: RID=(2, 1)
- Pág 4: RID=(4, 2)
- Pág 1: RID=(1, 4)

**Leyenda inferior:** «RID = (número de página, slot) → saltos aleatorios a páginas».

(slides 43)

### Clustered vs. Unclustered

- Decimos que el índice está agrupado si está construido sobre el mismo atributo utilizado para ordenar los registros en el archivo de datos.
  - De lo contrario, decimos que es un índice no agrupado.
- Un archivo de datos puede agruparse como máximo en una clave de búsqueda.
  - Claramente, podemos construir como máximo un índice agrupado para cada tabla, sin embargo podemos construir un número arbitrario de índices no agrupados.

**Figura:** Título «B+ Tree Index: Clustered vs. Unclustered» en la parte superior. Dos viñetas principales con sub-viñetas indentadas.

(slides 44)

**Índice Agrupado:**

- Un solo índice clustered por tabla.
- Datos ordenados físicamente por la clave.
- Búsqueda puntual: $O(\log_d N)$.
- Rango: $O(\log_d N + \text{páginas del rango})$.
- Ideal para: PK, búsquedas de rango.
- Inserción: puede causar page split en heap.

**Índice No Agrupado:**

- Múltiples índices por tabla.
- Estructura separada; apunta al heap.
- Búsqueda puntual: $O(\log_d N) + \text{heap fetch}$.
- Rango: puede ser costoso (random I/O).
- Ideal para: predicados de alta selectividad.
- Covering index elimina heap fetch.

**Figura:** Slide con fondo blanco dividido en dos columnas de viñetas. Columna izquierda titulada «Índice Agrupado» y columna derecha «Índice No Agrupado».

(slides 45)

### Inserción

- Inserción (pasos generales):
  - Se recorre el árbol desde la raíz en busca del nodo hoja que va a contener al registro a insertar usando la clave de búsqueda.
  - Si la clave ya esta presente en el nodo hoja, agregar el registro al archivo de datos (agregar un puntero al bucket si es necesario).
  - Si la clave no esta presente, agregar el registro al archivo principal (crear un bucket si es necesario).
  - Si hay espacio en el nodo hoja, agregar el par (clave-dirección) en dicho nodo.
  - En otro caso dividir el nodo y actualizamos el nodo padre (actualización en cascada).

**Figura:** Título «B+ Tree Index» en la parte superior. Una viñeta principal «Inserción (pasos generales):» con cinco sub-viñetas indentadas.

(slides 46)

### Eliminación

- Eliminación (pasos generales):
  - Se recorre el árbol en búsqueda del nodo hoja que contiene el registro a eliminar.
  - Remover el par (clave-puntero) del nodo hoja.
  - Si el nodo se queda con pocas entradas debido a la eliminación realizada, realizar:
    - Si las entradas en el nodo y un hermano encajan en un solo nodo, fusione los hermanos.
    - Si no encajan, redistribuir los registros entre el nodo y un hermano de manera que ambos tengan más del número mínimo de entradas.
    - Actualice la clave de búsqueda el correspondiente en el nodo padre.
  - Las eliminaciones pueden ocasionar una actualización en cascada hacia arriba hasta que se encuentre un nodo con mas de la mitad de entradas.

**Figura:** Título «B+ Tree Index» en la parte superior. Una viñeta principal «Eliminación (pasos generales):» con sub-viñetas indentadas, incluyendo tres sub-viñetas anidadas bajo la condición de pocas entradas.

(slides 47)

### Complejidad

- Complejidad:
  - Cada nodo interno tiene entre $\lceil R/2 \rceil$ y $R$ entradas. Siendo $R$ es el factor de bloque.
  - Cada nodo hoja tiene entre $\lceil R/2 \rceil$ y $R - 1$ entradas. Ya que el ultimo espacio se reserva para el puntero al siguiente nodo.
  - Si consideramos $M$ como el total de claves de búsqueda para construir el índice (unclustered), la altura del árbol no es mas que $\lceil \log_{\lceil R/2 \rceil} M \rceil$. Este sería el costo de búsqueda.
  - Para inserciones y eliminaciones: costo de búsqueda + costo del split * nodos desbordados.

**Figura:** Título «B+ Tree Index» en la parte superior. Una viñeta principal «Complejidad:» con cuatro sub-viñetas que incluyen fórmulas matemáticas con notación de techo ($\lceil \cdot \rceil$) y logaritmo.

(slides 48)

### Ventajas y deficiencias

- Ventajas:
  - Se reorganiza automáticamente con pequeños cambios locales cuando ocurren inserciones y eliminaciones.
  - No se requiere la reorganización de todo el archivo para mantener el rendimiento.
  - Soporta múltiples operadores de búsqueda de base de datos (order by, between, etc.)
- Deficiencias:
  - El rendimiento se degrada a medida que el archivo crece: demasiados bloques de desbordamiento.
- **Las ventajas del B+ Tree superan sus desventajas.**

**Figura:** Título «B+ Tree Index» en la parte superior. Dos secciones «Ventajas:» y «Deficiencias:» con sub-viñetas. La frase final «Las ventajas del B+ Tree superan sus desventajas.» aparece en negrita y color azul.

(slides 49)

## Costo de operaciones (acceso a memoria secundaria)

| | Scan | Equality | Range | Insert | Delete |
|---|---|---|---|---|---|
| **Heap** | $MD$ | $MD$ | $MD$ | $1D$ | $MD$ |
| **Sorted** | $MD$ | $D\log_2(M)$ | $D\log_2 M + \#\text{matches}$ | 1) $D\log_2 M + cD$<br>2) $MD$ | 1) $D\log_2 M + cD$<br>2) $MD$ |
| **Static Hash** | $MD$ | $1D + \text{colisión}$ | $MD$ | $D + \text{colisión}$ | $D + \text{colisión}$ |
| **B+ Tree** | $MD$ | $D\log_{R/2}(M)$ | $D\log_{R/2}(M) + \#\text{matches}$ | $D\log_{R/2}(M) + \text{reasignación}$ | $D\log_{R/2}(M) + \text{reasignación}$ |

$M$: Número de páginas/buckets &nbsp;&nbsp;&nbsp; $R$: Número de registros por página &nbsp;&nbsp;&nbsp; $D$: (Promedio) Costo de lectura/escritura en disco

**Figura:** Título «Costo de operaciones (acceso a memoria secundaria)» en la parte superior. Tabla comparativa de cinco operaciones (Scan, Equality, Range, Insert, Delete) para cuatro técnicas (Heap, Sorted, Static Hash, B+ Tree). Leyenda de variables en la parte inferior.

(slides 50)

## Bitmap Index Scan en PostgreSQL

### ¿Cómo funciona?

**Problema:** un índice non-clustered sobre edad=25 retorna muchos RIDs dispersos → cada RID puede implicar un acceso a una página diferente del heap.

**Solución PostgreSQL:** construir un bitmap de páginas en memoria antes de leer el heap.

**Figura:** Diagrama de tres pasos secuenciales conectados por flechas.

**① B+Tree Index Scan (non-clustered, sobre edad):**

Hoja B+Tree (edad=25):
- edad=25 → (pág 7, slot 2)
- edad=25 → (pág 2, slot 0)
- edad=25 → (pág 5, slot 3)
- edad=25 → (pág 1, slot 1)
- edad=25 → (pág 6, slot 0)

Flecha etiquetada «RIDs» hacia el paso 2.

**② Bitmap en Memoria (1 bit por página del heap):**

Bitmap (1 bit/página):
- 0 — Pág 0
- 1 — Pág 1 ← contiene edad=25
- 1 — Pág 2 ← contiene edad=25
- 0 — Pág 3
- 0 — Pág 4
- 1 — Pág 5 ← contiene edad=25
- 1 — Pág 6 ← contiene edad=25
- 1 — Pág 7 ← contiene edad=25

Flecha etiquetada «páginas» hacia el paso 3.

**③ Heap Fetch (ordenado) (páginas en orden físico):**

Heap leído en orden físico:
- Pág 1 → leer 1 vez (buscar slots con edad=25)
- Pág 2 → leer 1 vez (buscar slots con edad=25)
- Pág 5 → leer 1 vez (buscar slots con edad=25)
- Pág 6 → leer 1 vez (buscar slots con edad=25)
- Pág 7 → leer 1 vez (buscar slots con edad=25)

**Beneficio:** los 5 RIDs dispersos se convierten en 5 accesos secuenciales a páginas ordenadas → se evita el problema de thrashing de caché en heap random-access.

(slides 51)

### Combinación de índices con AND / OR

**Query:** `SELECT * FROM empleados WHERE edad = 25 AND depto = 'TI'`

PostgreSQL construye un bitmap por cada índice y luego hace AND bit a bit antes de acceder al heap:

| Página | Bitmap A<br>idx_edad (edad=25) | Bitmap B<br>idx_depto (depto='TI') | AND<br>Intersección de páginas | OR<br>Unión de páginas |
|---|---|---|---|---|
| Pág 0 | 0 | 0 | 0 | 0 |
| Pág 1 | 1 | 1 | 1 | 1 |
| Pág 2 | 0 | 1 | 0 | 1 |
| Pág 3 | 0 | 0 | 0 | 0 |
| Pág 4 | 1 | 0 | 0 | 1 |
| Pág 5 | 1 | 1 | 1 | 1 |
| Pág 6 | 0 | 1 | 0 | 1 |
| Pág 7 | 1 | 0 | 0 | 1 |

AND → leer solo págs: 1, 5 &nbsp;&nbsp; OR → leer págs: 1, 2, 4, 5, 6, 7 → siempre en orden físico, 1 sola una pasada por el heap.

**Figura:** Cuatro columnas verticales de bitmaps (Bitmap A en tono marrón, Bitmap B en tono verde, AND en tono azul oscuro, OR en tono púrpura), cada una con 8 filas (Pág 0 a Pág 7) con valores 0 o 1. Texto resumen en la parte inferior.

(slides 52)

## Hash File

- Utiliza una función hash para asignar direcciones a los registros.
- Permite acceso rápido y directo a los registros.
- Es especialmente eficiente en búsquedas de igualdad basadas en una clave.
- Puede sufrir colisiones (múltiples registros asignados a la misma dirección).
- Se emplean técnicas de resolución de colisiones como encadenamiento o direccionamiento abierto.

*Fundamentals of Database Systems, Elmasri & Navathe (Sixth Edition), Chapter 18.*

**Figura:** Slide con diseño de portada institucional. En el lado izquierdo, fotografía con filtro azul de un científico en laboratorio con bata, guantes y gafas de seguridad trabajando con pipeta y tubos de ensayo. Título central «Hash File» en texto grande y negrita. Cinco viñetas con iconos de flecha azul. Cita bibliográfica en cursiva en la parte inferior. Líneas decorativas punteadas en azul y amarillo en los bordes.

(slides 53)

## Hash-based Index

### Componentes

- Componentes
  - Hash Function
  - Hash Index
  - Bucket/Página

**Figura:** Diagrama de flujo de un índice basado en hash.

**Entrada:** Una clave etiquetada «key» entra a un círculo etiquetado «h» (función hash).

**Hash Index (tabla vertical):** Índices de $0$ a $N-1$, con flechas desde la función hash hacia los buckets correspondientes.

**Almacenamiento (cilindro con borde punteado):**
- **Main Buckets:** Buckets principales numerados $0, 1, 2, \ldots, N-1$.
- **Overflow Buckets:** Buckets de desbordamiento enlazados desde los main buckets cuando se llenan. El bucket $0$ apunta a un overflow bucket; el bucket $2$ apunta a un overflow bucket que a su vez apunta a otro (indicado con «…»); el bucket $N-1$ apunta a un overflow bucket.

**Hash Function:**

$$index(key) = h(key) \bmod M$$

- key: clave de búsqueda.
- M: número de bloques disponibles.

Generalmente se usa un método de hash eficiente.

(slides 54)

- Componentes
  - Hash Function: h(key) es una función de mapeo que asocia todo el conjunto de claves de búsqueda a la dirección real del bucket en memoria secundaria. La función hash debe seleccionar de manera que los registros sean esparcidos de manera uniforme. Puede darse que los registros con diferentes valores de clave de búsqueda se asignen al mismo grupo; por lo tanto, se debe buscar secuencialmente todo el bucket para localizar un registro.
  - Hash Index: es el espacio de valores de la función hash y sus direcciones a los buckets de datos.
  - Bucket: los datos son organizados en buckets. Un bucket generalmente corresponde a una página/bloque en donde se almacena uno o mas registros.

**Figura:** Título «Hash-based Index» en la parte superior. Una viñeta principal «Componentes» con tres sub-viñetas detalladas (Hash Function, Hash Index, Bucket).

(slides 55)

## Hash Indexes

**Figura:** Diagrama jerárquico (árbol) de clasificación de técnicas de hashing.

**Nivel raíz:** Caja central «HASHING».

**Segundo nivel (dos ramas desde HASHING):**
- Izquierda: «STATIC HASHING»
- Derecha: «DYNAMIC HASHING»

**Tercer nivel (tres ramas desde DYNAMIC HASHING):**
- «EXTENDIBLE HASHING»
- «TRIE HASHING» (con nota al pie «* Dynamic Hashing»)
- «LINEAR HASHING»

(slides 56)

## Static Hashing

### Definición

- Definición
  - La función de hash asigna cada clave a un bucket en un rango fijo de direcciones.
  - Cuando los buckets se llenan, se crean áreas de overflow (encadenamiento).

**Figura:** Diagrama de estructura de archivo `Datos.dat` vacío.

Tabla con índices verticales $0$ a $5$ (6 buckets principales). Cada fila está dividida por una línea punteada vertical roja en dos zonas:
- **Main Buckets** (izquierda de la línea roja): buckets principales, actualmente vacíos.
- **Overflow Buckets** (derecha de la línea roja, etiqueta en rojo): áreas de desbordamiento, actualmente vacías.

**Factor de bloque: 4 registros por bloque** (caja azul en la parte inferior derecha).

(slides 57)

### Ejemplo de inserción

- Ejemplo
  - Insertar los siguientes datos:

**Keys:**

2, 3, 5

7, 11, 17

18, 19, 23

28, 29, 31

36, 37, 40

41, 46, 53

60, 61

$$index(key) = key \bmod 6$$

**Figura:** Diagrama de estructura de archivo `Datos.dat` vacío (misma estructura que slide 57).

Tabla con índices $0$ a $5$, dividida en Main Buckets (izquierda) y Overflow Buckets (derecha, separados por línea punteada roja). Todos los buckets están vacíos.

**Factor de bloque: 4 registros por bloque** (caja azul en la parte inferior derecha).

(slides 58)

**Figura:** Diagrama de estructura de archivo `Datos.dat` con buckets poblados tras la inserción.

| Índice | Main Buckets | Overflow Buckets |
|---|---|---|
| 0 | 18, 36, 60 | |
| 1 | 7, 19, 31, 37 | 61 |
| 2 | 2 | |
| 3 | 3 | |
| 4 | 28, 40, 46 | |
| 5 | 5, 11, 17, 23 | 29, 53 |

Los valores en Overflow Buckets (61, 29, 53) aparecen en texto rojo, indicando que excedieron la capacidad del main bucket (factor de bloque: 4 registros por bloque).

**Factor de bloque: 4 registros por bloque** (caja azul en la parte inferior derecha).

(slides 59)

### Manejo del overflow

- Manejo del overflow: desbordamiento encadenado.

**Figura:** Dos tablas lado a lado: Main Buckets y Overflow Buckets, con punteros de encadenamiento.

**Main Buckets:**

| Índice | registros | puntero |
|---|---|---|
| 0 | 18, 36, 60 | |
| 1 | 7, 19, 31, 37 | 7 |
| 2 | 2 | |
| 3 | 3 | |
| 4 | 28, 40, 46 | |
| 5 | 5, 11, 17, 23 | 6 |

**Overflow Buckets:**

| Índice | registros | puntero |
|---|---|---|
| 6 | 29, 40, 53, 59 | 8 |
| 7 | 61 | |
| 8 | 65, 77 | |
| … | | |

**Cadenas de punteros:**
- Main Bucket 1 (puntero 7) → flecha azul → Overflow Bucket 7 (registros: 61).
- Main Bucket 5 (puntero 6) → flecha púrpura → Overflow Bucket 6 (registros: 29, 40, 53, 59; puntero 8) → flecha púrpura curva → Overflow Bucket 8 (registros: 65, 77).

(slides 60)

### Operaciones

- **Inserción:** se usa la función hash para asignar el registro al bucket correspondiente.
  - Si no hay espacio en el bucket colocar en el desbordamiento de dicho bucket.

- **Eliminación:** localizar la pagina del registro usando la función hash.
  - Eliminar el registro del main bucket o del overflow. En este último caso, traer un elemento del overflow bucket hacia el main bucket.

- **Búsqueda:** acceso directo usando la función hash y luego recorrido lineal en los buckets desbordados.

**Figura:** En el borde izquierdo hay un elemento decorativo triangular de color azul. El título «Static Hashing» aparece en la parte superior. Tres viñetas principales con encabezados en negrita y subrayados (**Inserción**, **Eliminación**, **Búsqueda**), cada una con una sub-viñeta indentada.

(slides 61)

### Deficiencias

- **Deficiencias:**
  - En el hash estático, la función hash mapea valores de la clave de búsqueda a un conjunto fijo de direcciones de buckets. Pero las bases de datos crecen o disminuyen con el tiempo.
  - Posible solución: reorganización periódica del archivo con una nueva función hash.
  - **Mejor solución:** permitir la modificación del número de buckets dinámicamente.

**Figura:** El título «Static Hashing» en la parte superior. Una viñeta principal «Deficiencias:» en negrita, seguida de tres sub-viñetas indentadas. La tercera sub-viñeta contiene «Mejor solución:» en negrita.

(slides 62)

## Extendible Hashing

### Introducción

- Introducido por Ronald Fagin et. al.(1979), *"Extendible hashing—a fast access method for dynamic files"*

- Es un tipo de hash dinámico para gestionar base de datos que crecen y reducen su tamaño en el tiempo (transaccionales).

- **La función hash genera una secuencia de bits.**

- En cualquier momento, solo se usa un sufijo/prefijo del binario para indexar los registros en una tabla de direcciones de buckets.

- **Crece duplicando directorio solo cuando es necesario.**

**Figura:** El título «Extendible Hashing» en la parte superior. Cinco viñetas; la primera incluye una cita en cursiva. Las frases «La función hash genera una secuencia de bits.» y «Crece duplicando directorio solo cuando es necesario.» aparecen en negrita.

(slides 63)

### Profundidad local y global

**Profundidad local:** Número de bits en el sufijo común de la secuencia de bits correspondiente a los registros en el bucket.

**Profundidad global** $D = 3$

**Figura:** Diagrama de Extendible Hashing con un directorio (Hash Index) a la izquierda y buckets a la derecha, conectados por flechas.

**Hash Index (directorio):** Columna vertical de 8 celdas etiquetadas con secuencias binarias de 3 bits, de arriba a abajo: `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111`. Etiqueta «Hash Index» en la parte inferior de la columna.

**Buckets (6 en total), cada uno con profundidad local $d$:**

1. **Bucket con $d=2$:** Apuntado por las entradas del directorio `000` y `100` (flechas azules). Los registros comparten el sufijo `00`.
2. **Bucket con $d=3$:** Apuntado por la entrada `001` (flecha roja).
3. **Bucket con $d=3$:** Apuntado por la entrada `010` (flecha azul).
4. **Bucket con $d=2$:** Apuntado por las entradas `011` y `101` (flechas rojas). Cuadro de texto asociado: «Todos los registros que terminan en **01**».
5. **Bucket con $d=3$:** Apuntado por la entrada `110` (flecha azul).
6. **Bucket con $d=3$:** Apuntado por la entrada `111` (flecha roja). Cuadro de texto asociado: «Todos los registros que terminan en **111**».

A la izquierda del directorio se indica «Profundidad global $D = 3$». A la derecha, la definición de «Profundidad local» como el número de bits en el sufijo común de la secuencia de bits correspondiente a los registros en el bucket.

(slides 64)

### Ejemplo — Estado inicial

**Ejemplo**

Key = 2, 3, 5, 7, 11, 17, 1, 8, 19, 23, 28, 29, 31, 32, 36

Factor de bloque: 3

$D = 2$

```
Bin(Key % 2^D)
```

**Figura:** Diagrama de Extendible Hashing en estado inicial.

**Parámetros:** Factor de bloque: 3 (capacidad máxima de 3 claves por bucket). Profundidad global $D = 2$ (en rojo). Función hash: `Bin(Key % 2^D)`.

**Lista de claves a insertar:** 2, 3, 5, 7, 11, 17, 1, 8, 19, 23, 28, 29, 31, 32, 36.

**Hash Index (directorio):** Columna vertical de 4 entradas ($2^D = 4$), etiquetadas de arriba a abajo: `00`, `01`, `10`, `11`. Etiqueta «Hash Index» en la parte inferior.

**Buckets (2 iniciales, ambos vacíos):**

1. **Bucket 0** (etiquetado con `0` a la izquierda), profundidad local $d=1$. Flechas azules desde las entradas del directorio `00` y `10` apuntan a este bucket. Tres slots vacíos.
2. **Bucket 1** (etiquetado con `1` a la izquierda), profundidad local $d=1$. Flechas rojas desde las entradas del directorio `01` y `11` apuntan a este bucket. Tres slots vacíos.

(slides 65)

**Figura:** Diagrama de Extendible Hashing tras insertar las primeras claves, con desbordamiento.

**Parámetros:** Factor de bloque: 3. Profundidad global $D = 2$ (en rojo).

**Hash Index (directorio):** 4 entradas: `00`, `01`, `10`, `11`.

**Buckets:**

1. **Bucket 0** ($d=1$): Contiene la clave `2`. Flechas azules desde `00` y `10`.
2. **Bucket 1** ($d=1$): Contiene las claves `3`, `5`, `7` y **`11`** (el valor **11** aparece en rojo, indicando desbordamiento al superar el factor de bloque de 3). Flechas rojas desde `01` y `11`.

(slides 66)

**Figura:** Diagrama de Extendible Hashing tras división de bucket, con nuevo desbordamiento.

**Parámetros:** Factor de bloque: 3. Profundidad global $D = 2$.

**Hash Index (directorio):** 4 entradas: `00`, `01`, `10`, `11`.

**Buckets (3):**

1. **Bucket 0:** Contiene `2`, `8`. Sufijo `0` a la derecha (profundidad local efectiva 1). Flechas azules desde `00` y `10`.
2. **Bucket 1:** Contiene `5`, `1`. Sufijo `01` a la derecha (profundidad local 2). Flecha roja desde `01`.
3. **Bucket 2** (fondo gris): Contiene `3`, `7`, `11`, **`19`** (el valor **19** en rojo, indicando desbordamiento). Sufijo `11` a la derecha (profundidad local 2). Flecha roja desde `11`.

(slides 67)

**Figura:** Diagrama de Extendible Hashing con profundidad global aumentada a 3, con desbordamiento en bucket 0.

**Parámetros:** Factor de bloque: 3. Profundidad global $D = 3$ (en rojo).

**Hash Index (directorio):** 8 entradas ($2^3$): `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111`.

**Buckets (4):**

1. **Bucket 0:** Contiene `2`, `8`, `28`, **`32`** (el valor **32** en rojo, indicando desbordamiento). Sufijo `0` a la derecha. Flechas azules/rojas desde `000`, `010`, `100`, `110`.
2. **Bucket 1:** Contiene `5`, `1`, `29`. Sufijo `01` a la derecha. Flechas desde `001` y `101`.
3. **Bucket 2:** Contiene `3`, `11`, `19`. Sufijo `011` a la derecha. Flecha desde `011`.
4. **Bucket 3** (fondo gris): Contiene `7`, `23`, `31`. Sufijo `111` a la derecha. Flecha desde `111`.

(slides 68)

**Figura:** Diagrama de Extendible Hashing tras división del bucket 0, con desbordamiento por inserción de 36.

**Parámetros:** Factor de bloque: 3. Profundidad global $D = 3$ (en rojo).

**Hash Index (directorio):** 8 entradas: `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111`.

**Buckets (5):**

1. **Bucket 0:** Contiene `8`, `28`, `32`, **`36`** (el valor **36** en rojo, indicando desbordamiento). Sufijo `00` a la derecha. Flecha desde `000`.
2. **Bucket 1:** Contiene `5`, `1`, `29`. Sufijo `01` a la derecha. Flechas desde `001` y `101`.
3. **Bucket 2:** Contiene `3`, `11`, `19`. Sufijo `011` a la derecha. Flecha desde `011`.
4. **Bucket 3:** Contiene `7`, `23`, `31`. Sufijo `111` a la derecha. Flecha desde `111`.
5. **Bucket 4** (fondo gris): Contiene `2`. Sufijo `10` a la derecha. Flechas desde `010` y `110`.

(slides 69)

**Figura:** Diagrama de Extendible Hashing tras inserción de la clave 27, con desbordamiento en bucket 2.

**Parámetros:** Factor de bloque: 3. Profundidad global $D = 3$.

**Lista de claves:** 2, 3, 5, 7, 11, 17, 1, 8, 19, 23, 28, 29, 31, 32, 36, **27** (el valor **27** en rojo, indicando la inserción más reciente).

**Hash Index (directorio):** 8 entradas: `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111`.

**Buckets (6):**

1. **Bucket 0:** Contiene `8`, `32`. Sufijo `000` a la derecha. Flecha desde `000`.
2. **Bucket 1:** Contiene `5`, `1`, `29`. Sufijo `01` a la derecha. Flechas desde `001` y `101`.
3. **Bucket 2:** Contiene `3`, `11`, `19`, **`27`** (el valor **27** en rojo, indicando desbordamiento). Sufijo `011` a la derecha. Flecha desde `011`.
4. **Bucket 3:** Contiene `7`, `23`, `31`. Sufijo `111` a la derecha. Flecha desde `111`.
5. **Bucket 4:** Contiene `2`. Sufijo `10` a la derecha. Flechas desde `010` y `110`.
6. **Bucket 5** (fondo gris): Contiene `28`, `36`. Sufijo `100` a la derecha. Flecha desde `100`.

(slides 70)

**Figura:** Diagrama de Extendible Hashing tras división del bucket 2, con nuevo bucket 6 para la clave 27.

**Parámetros:** Factor de bloque: 3. Profundidad global $D = 3$.

**Lista de claves:** 2, 3, 5, 7, 11, 17, 1, 8, 19, 23, 28, 29, 31, 32, 36, **27** (en rojo).

**Hash Index (directorio):** 8 entradas: `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111`.

**Buckets (7):**

1. **Bucket 0:** Contiene `8`, `32`. Sufijo `000` a la derecha. Flecha desde `000`.
2. **Bucket 1:** Contiene `5`, `1`, `29`. Sufijo `01` a la derecha. Flechas desde `001` y `101`.
3. **Bucket 2** (fondo gris): Contiene `3`, `11`, `19`. Sufijo `011` a la derecha. Flecha desde `011`. Un recuadro con el número **6** al final del bucket, con una flecha roja que apunta al bucket 6.
4. **Bucket 3:** Contiene `7`, `23`, `31`. Sufijo `111` a la derecha. Flecha desde `111`.
5. **Bucket 4:** Contiene `2`. Sufijo `10` a la derecha. Flechas desde `010` y `110`.
6. **Bucket 5:** Contiene `28`, `36`. Sufijo `100` a la derecha. Flecha desde `100`.
7. **Bucket 6** (fondo gris): Contiene **`27`** (en rojo). Creado por la división del bucket 2.

(slides 71)

### Búsqueda

- **Búsqueda:**
  - Sea $D$ la profundidad global del índice.
  - Aplicar la función hash sobre la clave de búsqueda y obtener la secuencia $D$-bit.
  - Haga coincidir la secuencia de $D$-bit con una entrada del directorio y dirigirse al bucket correspondiente para encontrar el registro.
    - El índice también provee información de la profundidad local de los buckets.

**Figura:** El título «Extendible Hashing» en la parte superior. Viñeta principal «Búsqueda:» en negrita y subrayada, con tres sub-viñetas indentadas; la tercera tiene una sub-sub-viñeta sobre la profundidad local de los buckets.

(slides 72)

### Inserción

- **Inserción:**
  - Para insertar un registro se debe usar la secuencia $D$-bit para localizar el bucket respectiva.
  - Si no encontró bucket, proceder a buscar uno con la profundidad local mínima. Si no lo encontró, proceder a crear el bucket.
  - Si encontró un bucket y no esta lleno, proceder a insertar.
  - Si el bucket esta lleno, dividir el bucket y reinsertar todos los registros.
    - Se crean nuevos buckets con una nueva profundidad local ($d = d + 1$).
    - El directorio es modificado.
  - Si ya no se puede incrementar la profundidad, se produce desbordamiento de buckets.
  - Si el desbordamiento es demasiado (parametrizar), entonces aumentar la profundidad global ($D = D + 1$)

**Figura:** El título «Extendible Hashing» en la parte superior. Viñeta principal «Inserción:» en negrita y subrayada, con seis sub-viñetas indentadas; la cuarta sub-viñeta tiene dos sub-sub-viñetas sobre la profundidad local y la modificación del directorio.

(slides 73)

### Eliminación

- **Eliminación:**
  - Localizar el buffer respectivo y remover el registro.
  - Si el bucket queda vacío, puede ser liberado.
    - Implica actualizar el índice.
  - Si dos buckets tienen poco elementos y tienen el mismo prefijo en la profundidad local anterior ($d-1$), proceder a mezclar.
    - Implica actualizar el índice.

**Figura:** El título «Extendible Hashing» en la parte superior. Viñeta principal «Eliminación:» en negrita y subrayada, con tres sub-viñetas indentadas; la segunda y la tercera tienen cada una una sub-sub-viñeta sobre la actualización del índice.

(slides 74)

### Ventajas y deficiencias

- **Ventajas:**
  - La eficiencia no se degrada con el crecimiento del archivo de datos.
  - Minimiza el espacio de overflow.
- **Deficiencias:**
  - El índice podría llegar a ser muy grande (mucho espacio en memoria).
  - Cambiar el tamaño del índice (tabla de direcciones) es una operación cara.
  - **No soporta búsqueda por rango.**

**Figura:** El título «Extendible Hashing» en la parte superior. Dos viñetas principales «Ventajas:» y «Deficiencias:» en negrita, cada una con sub-viñetas indentadas. La última sub-viñeta de Deficiencias («No soporta búsqueda por rango.») aparece en negrita.

(slides 75)

## Otras técnicas de hashing dinámico

- **Trie Hashing:**
  - Usa un **Trie Digital** en lugar de un directorio plano.
  - Expande solo las ramas necesarias cuando hay colisiones.

- **Linear Hashing (LH):**
  - Usa un **split secuencial** de buckets.
  - Mantiene un nivel $n$ y un puntero de división $p$.

✓ *Fundamentals of Database Systems, Elmasri & Navathe (Sixth Edition), Chapter 18.*

✓ *Linear hashing: a new tool for file and table addressing. Litwin, W. (1980)*

**Figura:** El título «Otras técnicas de hashing dinámico» en la parte superior. Dos viñetas principales (Trie Hashing y Linear Hashing (LH)), cada una con dos sub-viñetas indentadas. Términos «Trie Digital» y «split secuencial» en negrita. En la parte inferior, dos referencias bibliográficas precedidas por iconos de checkmark (✓), en cursiva.

(slides 76)

## Glosario

- **Blocking factor:** El máximo número de registros que son almacenados dentro de un bloque; $b = \lfloor B/r \rfloor$, donde $B$ es el tamaño del bloque en bytes y $r$ la longitud del registro en bytes.
- **Dense Index-file:** Contiene una entrada para cada registro en el archivo de datos; permite búsquedas muy rápidas de registros individuales, ya que cada registro tiene su propia entrada en el índice.
- **Sparse Index-file:** Contiene entradas solo para algunos registros en el archivo de datos, generalmente el primer registro en cada página de datos; para encontrar un registro específico, primero se busca en el índice el bloque que podría contener el registro y luego se busca secuencialmente dentro del bloque asociado. Sólo posible si datos están ordenados.
- **Multilevel Index-File:** Jerarquía de índices donde el índice superior dirige a bloques de entradas en niveles inferiores, hasta llegar a los registros de datos.
- **BST File:** Organización de registros utilizando la estrategia de Árbol Binario de Búsqueda.
- **AVL File:** Árbol binario de búsqueda que se mantiene balanceado en todo momento.
- **B+ Tree File:** Estructura de datos de árbol auto-balanceada que mantiene los datos ordenados y permite búsquedas, accesos secuenciales, inserciones y eliminaciones en tiempo logarítmico; optimizada para operaciones de E/S de disco al agrupar múltiples claves en cada nodo.
- **Índice agrupado (clustered):** Índice construido sobre el mismo atributo utilizado para ordenar los registros en el archivo de datos; solo puede existir un índice agrupado por tabla.
- **Índice no agrupado (unclustered):** Índice construido sobre un atributo distinto al utilizado para ordenar los registros en el archivo de datos; se pueden construir un número arbitrario por tabla.
- **Covering index:** Índice no agrupado que incluye todas las columnas necesarias para una consulta, evitando heap fetch.
- **Index-only scan:** Si todos los campos de la consulta están en el índice, no se accede al heap.
- **RID:** Identificador de registro como (número de página, slot).
- **Hash Function:** Función de mapeo $h(key)$ que asocia todo el conjunto de claves de búsqueda a la dirección real del bucket en memoria secundaria; $index(key) = h(key) \bmod M$, donde $M$ es el número de bloques disponibles.
- **Hash Index:** Espacio de valores de la función hash y sus direcciones a los buckets de datos.
- **Bucket:** Unidad de organización de datos; generalmente corresponde a una página/bloque en donde se almacena uno o más registros.
- **Static Hashing:** La función de hash asigna cada clave a un bucket en un rango fijo de direcciones; cuando los buckets se llenan, se crean áreas de overflow (encadenamiento).
- **Overflow Buckets:** Áreas de desbordamiento enlazadas desde los main buckets cuando estos se llenan.
- **Extendible Hashing:** Tipo de hash dinámico para gestionar bases de datos que crecen y reducen su tamaño en el tiempo; la función hash genera una secuencia de bits y solo se usa un sufijo/prefijo del binario para indexar los registros en una tabla de direcciones de buckets.
- **Profundidad local:** Número de bits en el sufijo común de la secuencia de bits correspondiente a los registros en el bucket.
- **Profundidad global ($D$):** Número de bits del sufijo/prefijo binario usado en un momento dado para indexar los registros en la tabla de direcciones de buckets.
- **Trie Hashing:** Usa un Trie Digital en lugar de un directorio plano; expande solo las ramas necesarias cuando hay colisiones.
- **Linear Hashing (LH):** Usa un split secuencial de buckets; mantiene un nivel $n$ y un puntero de división $p$.
- **Spanned organization (organización extendida):** Organización utilizada cuando la longitud del registro es mayor que el tamaño del bloque; un registro extendido puede abarcar diferentes bloques.
