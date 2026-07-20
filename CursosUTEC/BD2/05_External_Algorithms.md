---
curso: BD2
titulo: 05 External Algorithms
slides: 21
fuente: 05 External Algorithms.pdf
---

# 05 External Algorithms

**Figura:** Slide de portada con fondo fotográfico de un túnel o corredor circular futurista en tonos azules profundos, con patrones tecnológicos y líneas de luz. En el centro, la silueta de una persona de pie mirando hacia el interior del túnel. En la parte superior central, el código y nombre del curso «CS2042 - BASES DE DATOS II». En el centro, el título principal «External Algorithms» en letras grandes blancas en negrita; debajo, «SEMANA 05» en cursiva blanca. Una línea horizontal punteada amarilla separa el título de los datos del instructor: «Heider Sanchez» y «hsanchez@utec.edu.pe». En la parte inferior, gráficos decorativos de líneas punteadas amarillas y blancas con aspecto de diagrama técnico.

## Índice

- [El Problema de la Escala](#el-problema-de-la-escala)
  - [Escenario ORDER BY](#escenario-order-by)
  - [Problema general y objetivo](#problema-general-y-objetivo)
  - [Escenario GROUP BY](#escenario-group-by)
- [Two-Phase Multiway Merge Sort](#two-phase-multiway-merge-sort)
  - [Fases del algoritmo](#fases-del-algoritmo)
  - [Ejemplo ilustrativo: generación de runs y merge](#ejemplo-ilustrativo-generación-de-runs-y-merge)
  - [Requisitos de RAM en la fase de merge](#requisitos-de-ram-en-la-fase-de-merge)
  - [Merge binario con dos buffers](#merge-binario-con-dos-buffers)
  - [Primera pasada de merge binario (L=1)](#primera-pasada-de-merge-binario-l1)
  - [Segunda pasada de merge binario (L=2)](#segunda-pasada-de-merge-binario-l2)
  - [Tercera pasada de merge binario (L=3)](#tercera-pasada-de-merge-binario-l3)
  - [Fusión de múltiples mezclas simultáneas](#fusión-de-múltiples-mezclas-simultáneas)
  - [Fusión multiway con buffers en memoria principal](#fusión-multiway-con-buffers-en-memoria-principal)
  - [Merge de 4 vías](#merge-de-4-vías)
- [External Hashing](#external-hashing)
  - [Fases del algoritmo](#fases-del-algoritmo-1)
  - [Particionamiento para GROUP BY](#particionamiento-para-group-by)
  - [Construcción para GROUP BY](#construcción-para-group-by)
  - [Ejemplo](#ejemplo)
  - [Extensiones](#extensiones)

## El Problema de la Escala

### Escenario ORDER BY

Dada la siguiente consulta SQL

```sql
SELECT * FROM R ORDER BY R.a
```

Como ejecutarla de manera eficiente bajo el siguiente escenario

● No hay ningún índice en el atributo R.a

● Tabla R es muy grande (aprox. 50 GB)

● La memoria RAM asignada es muy limitada (<= 1 GB)

**Figura:** Título «El Problema de la Escala» en la parte superior izquierda en texto grande negro. Debajo, el texto «Dada la siguiente consulta SQL» seguido de la consulta `SELECT * FROM R ORDER BY R.a` en fuente monoespaciada. A continuación, la pregunta «Como ejecutarla de manera eficiente bajo el siguiente escenario» y tres viñetas con círculos negros: sin índice en R.a, tabla de ~50 GB, y RAM limitada (<= 1 GB). Acento triangular azul en el borde izquierdo.

(slides 2)

### Problema general y objetivo

**El Problema General**

● Las operaciones de BD (order by, join, group-by, distinct) requieren materializaciones intermedias que pueden superar ampliamente la RAM disponible.

**Objetivo**

● Minimizar el número de I/O operations (lecturas/escrituras de páginas) durante el procesamiento de consultas.

**Figura:** Dos cajas rectangulares blancas con borde azul fino, cada una con barra de encabezado azul oscuro. La primera caja contiene el título «El Problema General» y el bullet sobre operaciones de BD (order by, join, group-by, distinct) y materializaciones intermedias que superan la RAM. La segunda caja contiene el título «Objetivo» y el bullet sobre minimizar I/O operations (lecturas/escrituras de páginas). Acento triangular azul en el borde izquierdo y región diagonal gris clara en el borde derecho.

(slides 3)

### Escenario GROUP BY

Dada la siguiente consulta SQL

```sql
SELECT R.a, count(*) FROM R GROUP BY R.a
```

Como ejecutarla de manera eficiente bajo el siguiente escenario

● No hay ningún índice en el atributo R.a

● Tabla R es muy grande (aprox. 50 GB)

● La memoria RAM asignada es muy limitada (<= 1 GB)

**Figura:** Título «El Problema de la Escala» en la parte superior izquierda. Texto «Dada la siguiente consulta SQL» seguido de `SELECT R.a, count(*) FROM R GROUP BY R.a` en fuente monoespaciada. Pregunta «Como ejecutarla de manera eficiente bajo el siguiente escenario» y tres viñetas: sin índice en R.a, tabla de ~50 GB, RAM limitada (<= 1 GB).

(slide 16)

## Two-Phase Multiway Merge Sort

**Figura:** las letras «UTEC» son visibles en el lado derecho de la fachada. Toda la imagen tiene una superposición semitransparente cian/azul claro. En el centro, el texto «External Sorting» en letras blancas grandes.

Sec. 4.2

### Fases del algoritmo

**Fase 1: Run Generation**

● Leer M páginas en memoria

● Ordenar internamente (quicksort, etc.)

● Escribir como run ordenado al disco

● Repetir hasta agotar la entrada

● Produce $\lceil B/M \rceil$ runs iniciales

**Fase 2: Multiway Merging**

● Leer el primer bloque de cada run

● Merge con heap de mínimos (k-way merge)

● Escribir páginas ordenadas al disco

● Usar $M-1$ buffers de entrada + 1 salida

● Produce la relación totalmente ordenada

**Figura:** Título «Two-Phase Multiway Merge Sort» en la parte superior. Referencia «Sec. 4.2» en la esquina superior derecha. Dos cajas con encabezado azul oscuro: la superior «Fase 1: Run Generation» con cinco bullets sobre lectura de M páginas, ordenamiento interno, escritura de runs, repetición y producción de $\lceil B/M \rceil$ runs; una flecha descendente conecta con la caja inferior «Fase 2: Multiway Merging» con cinco bullets sobre lectura del primer bloque de cada run, merge con min-heap (k-way merge), escritura al disco, uso de $M-1$ buffers de entrada + 1 de salida, y producción de la relación ordenada.

(slides 5)

### Ejemplo ilustrativo: generación de runs y merge

Sec. 4.2

**Fase 1: Run Generation** | **Fase 2: Multiway Merging**

**Figura:** Diagrama de flujo horizontal del algoritmo Two-Phase Multiway Merge Sort dividido en dos fases. **Fase 1 (izquierda):** Una columna vertical gris etiquetada como relación de entrada con 12 registros (letra, número): (G,24), (A,19), (D,31), (C,33), (B,14), (E,16), (R,16), (D,21), (M,3), (P,2), (D,7), (A,14). Flechas hacia cuatro bloques grises sin ordenar de 3 registros cada uno: Bloque 1: (G,24), (A,19), (D,31); Bloque 2: (C,33), (B,14), (E,16); Bloque 3: (R,16), (D,21), (M,3); Bloque 4: (P,2), (D,7), (A,14). Cada bloque pasa por «Internal Sort» y produce un run ordenado (columnas verdes): Run 1: (A,19), (D,31), (G,24); Run 2: (B,14), (C,33), (E,16); Run 3: (D,21), (M,3), (R,16); Run 4: (A,14), (D,7), (P,2). **Fase 2 (derecha):** Los runs se fusionan en «Merge Pass 1» (columnas amarillas «Merge»): la fusión de Run 1 y Run 2 produce (A,19), (B,14), (C,33), (D,31), (E,16), (G,24); la fusión de Run 3 y Run 4 produce (A,14), (D,7), (D,21), (M,3), (P,2), (R,16). «Merge Pass 2» fusiona ambos resultados en la columna de salida azul claro con el resultado final ordenado por letra: (A,14), (A,19), (B,14), (C,33), (D,7), (D,21), (D,31), (E,16), (G,24), (M,3), (P,2), (R,16). A la derecha, texto en rojo: «¿Y si hay mas datos?». Referencia «Sec. 4.2» en la esquina superior derecha.

(slide 6)

### Requisitos de RAM en la fase de merge

Sec. 4.2

**Fase 1: Run Generation** | **Fase 2: Multiway Merging**

¿Cuánto de Ram se Requiere?

**Figura:** Diagrama esquemático abstracto del Two-Phase Multiway Merge Sort de izquierda a derecha. A la izquierda, un rectángulo vertical alto segmentado representa el volumen de datos de entrada; una flecha indica que se divide en bloques. **Fase 1:** Bloques sin ordenar (iconos rectangulares rojos con esquinas redondeadas) se transforman en runs ordenados (iconos verdes). Debajo de los runs verdes aparece la anotación «N > P», donde N es el número de runs y P el número de páginas de memoria o factor de fan-in. **Fase 2:** Los runs se combinan en pasadas de merge (iconos amarillos). En el centro del diagrama, texto explicativo: «The merge phase continues until the overall number of runs are less than P i.e., N' < P.» y «Once N' < P, a final merge is performed to obtain the sorted output.» A la derecha, iconos azules representan la salida ordenada y fusionada («Output»). A la derecha de la slide, pregunta en rojo: «¿Cuánto de Ram se Requiere?». Referencia «Sec. 4.2» en la esquina superior derecha.

(slide 7)

### Merge binario con dos buffers

Sec. 4.2

● ¿Como ordenar bloques usando solo dos buffers?

    ○ Si se considera 10 bloques de 10 registros.

    ○ Se puede hacer mezclas binarias, con un árbol de mezcla de $\log_2 10 = 4$ niveles.

    ○ Durante cada capa, la lectura en memoria se ejecuta en bloques de 10M, se fusiona, se escribe de nuevo.

**Figura:** Slide con título «Two-Phase Multiway Merge Sort» y referencia «Sec. 4.2». Tres bullets sobre ordenar bloques con solo dos buffers: escenario de 10 bloques de 10 registros, mezclas binarias con árbol de $\log_2 10 = 4$ niveles, y lectura en memoria en bloques de 10M con fusión y escritura en cada capa. En la parte inferior, diagrama de flujo: a la izquierda, un rectángulo vertical etiquetado «DISK» con dos flechas de salida; al centro, caja «MAIN MEMORY» con tres componentes internos: «INPUT 1», «INPUT 2» (buffers de entrada que reciben datos del disco) y «OUTPUT TAPE» (buffer de salida donde se fusionan los datos); una flecha desde OUTPUT TAPE hacia un rectángulo vertical «DISK» a la derecha donde se escribe el resultado fusionado.

(slide 8)

### Primera pasada de merge binario (L=1)

**Figura:** Diagrama de una pasada de merge binario (2-way) entre disco y RAM con $L=1$. **Disco izquierdo (Hard Disk — entrada):** Ocho bloques grises de 4 enteros cada uno, organizados en 4 pares separados por líneas rosas horizontales. Par 1: [3, 5, 9, 10] y [1, 2, 5, 8]. Par 2: [4, 5, 8, 10] y [2, 3, 6, 7]. Par 3: [1, 3, 4, 10] y [2, 5, 7, 11]. Par 4: [1, 2, 3, 5] y [4, 5, 7, 10]. **Centro — RAM (L=1):** Caja azul con tres buffers naranjas vacíos etiquetados «Input 1», «Input 2» y «Output», configuración para merge de 2 vías (2 buffers de entrada + 1 de salida). **Disco derecho (Hard Disk — salida):** Ocho bloques naranjas resultantes tras la pasada de merge, también en 4 pares: [1, 2, 3, 5] y [5, 8, 9, 10] (fusión del Par 1); [2, 3, 4, 5] y [6, 7, 8, 10] (fusión del Par 2); [1, 2, 3, 4] y [5, 7, 10, 11] (fusión del Par 3); [1, 2, 3, 5] y [4, 5, 7, 10] (fusión del Par 4). Flechas implícitas de izquierda a centro a derecha indican el flujo de datos.

(slide 9)

### Segunda pasada de merge binario (L=2)

**Figura:** Diagrama de una segunda pasada de merge binario con RAM (L=2). **Disco izquierdo (Hard Disk — entrada):** Ocho bloques grises en dos grupos de cuatro separados por línea rosa gruesa. Grupo superior (resultado de la pasada anterior, dos runs de 2 bloques): Run A: [1, 2, 3, 5] y [5, 8, 9, 10]; Run B: [2, 3, 4, 5] y [6, 7, 8, 10]. Grupo inferior: Run C: [1, 2, 3, 4] y [5, 7, 10, 11]; Run D: [1, 2, 3, 4] y [5, 5, 7, 10]. **Centro — RAM (L=2):** Caja azul con «Input 1», «Input 2» y «Output» (buffers naranjas). **Disco derecho (Hard Disk — salida):** Ocho bloques naranjas en dos runs fusionados de 4 bloques cada uno. Grupo superior (fusión de Run A y Run B): [1, 2, 2, 3], [3, 4, 5, 5], [5, 6, 7, 8], [8, 9, 10, 10]. Grupo inferior (fusión de Run C y Run D): [1, 1, 2, 2], [3, 3, 4, 4], [5, 5, 5, 7], [7, 10, 10, 11].

(slide 10)

### Tercera pasada de merge binario (L=3)

**Figura:** Diagrama de una tercera pasada de merge binario con RAM (L=3). **Disco izquierdo (Hard Disk — entrada):** Ocho bloques grises en dos runs de 4 bloques. Run superior: [1, 2, 2, 3], [3, 4, 5, 5], [5, 6, 7, 8], [8, 9, 10, 10]. Run inferior: [1, 1, 2, 2], [3, 3, 4, 4], [5, 5, 5, 7], [7, 10, 10, 11]. **Centro — RAM (L=3):** Caja azul con «Input 1», «Input 2» y «Output» (3 buffers: 2 de entrada + 1 de salida). **Disco derecho (Hard Disk — salida):** Un único run completamente ordenado de 8 bloques naranjas: [1, 1, 1, 2], [2, 2, 2, 3], [3, 3, 3, 4], [4, 4, 5, 5], [5, 5, 5, 5], [6, 7, 7, 7], [8, 8, 9, 10], [10, 10, 10, 11].

(slide 11)

### Fusión de múltiples mezclas simultáneas

Sec. 4.2

● Pero es más eficiente hacer una fusión de múltiples mezclas, donde se está leyendo todos los bloques simultáneamente.

    ○ Abra todos los archivos de bloque simultáneamente y mantenga un búfer de lectura para cada uno y un búfer de escritura para el archivo de salida.

    ○ En cada iteración, seleccione el ID del término más bajo que no se haya procesado utilizando un min-heap.

    ○ Combine todas las listas de publicaciones para ese termID y escríbalo al disco.

**Figura:** Título «Two-Phase Multiway Merge Sort» en la parte superior. Bullet principal sobre fusión de múltiples mezclas leyendo todos los bloques simultáneamente, con tres sub-bullets sobre abrir archivos con buffers de lectura/escritura, seleccionar el termID más bajo con min-heap, y combinar listas de publicaciones escribiendo al disco. Acento triangular azul en la esquina superior izquierda. Referencia «Sec. 4.2» en la esquina superior derecha.

(slide 12)

### Fusión multiway con buffers en memoria principal

Sec. 4.2

● Pero es más eficiente hacer una fusión de múltiples mezclas, donde se está leyendo todos los bloques simultáneamente:

**Figura:** Slide con título «Two-Phase Multiway Merge Sort» y el bullet sobre fusión de múltiples mezclas leyendo bloques simultáneamente. Diagrama central: a la izquierda, un cilindro etiquetado «Disk» con segmentos horizontales (bloques de datos); flechas cargan bloques hacia el centro. En el centro, rectángulo «B main memory buffers» con $B-1$ buffers de entrada etiquetados «INPUT 1», «INPUT 2», «...», «INPUT B-1», cada uno conteniendo un bloque de un run distinto; flechas desde todos los inputs convergen hacia un único buffer «OUTPUT» donde se realiza el merge seleccionando el elemento mínimo. Flecha desde OUTPUT hacia un cilindro «Disk» a la derecha donde se escribe el resultado fusionado. A la derecha del disco de salida, texto en rojo «O(?)». En la parte inferior, referencia: «Algorithms and Data Structures for External Memory, Jeffrey Scott, Chapter 5» y enlace «TCSv2n4.qxd».

(slide 13)

### Merge de 4 vías

**Figura:** Diagrama de merge de 4 vías entre disco y RAM. **Disco izquierdo (Hard Disk — fuente):** Ocho bloques naranjas con 4 enteros cada uno, divididos en dos grupos de cuatro por línea rosa horizontal. Grupo superior: [3, 5, 9, 10], [1, 2, 5, 8], [4, 5, 8, 10], [2, 3, 6, 7]. Grupo inferior: [1, 3, 4, 10], [2, 5, 7, 11], [1, 2, 3, 5], [4, 5, 7, 10]. **Centro — RAM (L=1):** Caja azul con cuatro slots de entrada etiquetados «Input 1», «Input 2», «Input 3», «Input 4» (cada uno con bloque naranja vacío) y un slot «Output» (bloque naranja vacío), indicando configuración para merge de 4 vías. **Disco derecho (Hard Disk — destino):** Ocho bloques naranjas vacíos en la misma estructura de dos grupos de cuatro, representando el estado destino antes de completar la operación de merge.

(slide 14)

## External Hashing

**Figura:** las letras «UTEC» son visibles en el lado derecho de la fachada. Toda la imagen tiene una superposición semitransparente cian/azul claro. En el centro, el texto «External Hashing» en letras blancas grandes.

Sec. 4.2

### Fases del algoritmo

**Fase 1: Particionamiento**

● Aplicar función hash $h_p$ a la llave de cada tupla.

● Distribuir tuplas en $B - 1$ particiones en disco (usando $B - 1$ buffers de salida + 1 de entrada).

● Cada partición contiene tuplas con el mismo valor hash → candidatos a misma cubeta

**Fase 2: Construcción**

● Leer cada partición (una a la vez) en memoria.

● Construir tabla hash en RAM usando $h_2$ (segunda función hash diferente a $h_1$).

● Procesar la partición completa → colisiones manejadas con encadenamiento o probing.

**Figura:** Slide con título «External Hashing» y referencia «Sec. 4.2». Dos cajas con encabezado azul oscuro conectadas por flecha descendente. Caja superior «Fase 1: Particionamiento» con tres bullets sobre aplicar $h_p$, distribuir en $B-1$ particiones con $B-1$ buffers de salida + 1 de entrada, y tuplas con mismo hash como candidatos a misma cubeta. Caja inferior «Fase 2: Construcción» con tres bullets sobre leer particiones una a la vez, construir hash table con $h_2$ diferente de $h_1$, y procesar con encadenamiento o probing.

(slide 17)

### Particionamiento para GROUP BY

Sec. 4.2

**Fase 1: Particionamiento**

Interpretación para GROUP BY:

● Se crean B-1 particiones en disco

● Se hace:

```
partition = hp(R.a)
```

● Se escriben registros en cada partición

● Todas las tuplas con el mismo R.a caen en la misma partición

**Figura:** Slide con título «External Hashing», referencia «Sec. 4.2» y encabezado azul «Fase 1: Particionamiento». Cuatro bullets de interpretación para GROUP BY. Diagrama de flujo: a la izquierda, cilindro «Disk» con «Original Relation» (pila vertical de bloques naranjas representando páginas). Al centro, caja «B main memory buffers» con un buffer «INPUT» (lee un bloque del disco), función hash $h_p$ (subíndice p en rojo) que distribuye datos, y buffers de salida etiquetados «1», «2», «...», «B-1». Flechas desde los buffers de salida hacia la derecha, cilindro «Disk» con «Partitions»: Partition 1 (2 bloques), Partition 2 (3 bloques), «...», Partition B-1 (1 bloque).

(slide 18)

### Construcción para GROUP BY

**Fase 2: Construcción**

Interpretación para GROUP BY:

● Cada partición se carga en memoria

● Se construye una hash table ($h_r$) en RAM

```python
for tuple in partition:
   if dept in count:
      count[dept]++
   else:
      count[dept]=0
```

**Figura:** Slide con título «External Hashing» y encabezado azul «Fase 2: Construcción». Dos bullets de interpretación para GROUP BY y bloque de pseudocódigo Python. Diagrama a la derecha: cilindro «Disk» con grupos de bloques naranjas etiquetados «Partitions»; flecha hacia caja «Hash table for partition $R_i$ ($k \le B$ pages)» con rejilla interna de buckets (bloques naranjas organizados en tabla hash); sobre la flecha, texto «hash fn $h_r$». Debajo de la caja, «B main memory buffers». A la derecha, la palabra «Result».

(slide 19)

### Ejemplo

Ejemplo:

● Sean los datos en disco:

    ○ (A), (B), (A), (C), (D), (A), (C), (E), (F), (A), (C), (C)

● Después de aplicar $h_p$ se tiene la siguientes particiones

    ○ P0: A, A, A, A, E

    ○ P1: B, D

    ○ P2: C, C, C, C, F

● Construimos P0 con $h_r$

    ○ P0: A, A, A, A, E → A:4, E:1

    ○ Continuamos con las demás particiones

**Figura:** Slide con título «External Hashing» y subtítulo «Ejemplo:». Cuatro bullets con sub-bullets describiendo el ejemplo paso a paso: datos en disco (12 tuplas con letras A–F), particiones P0/P1/P2 tras aplicar $h_p$, construcción de P0 con $h_r$ produciendo conteos A:4 y E:1, y continuación con las demás particiones.

(slide 20)

### Extensiones

Como extender External hashing para:

```sql
SELECT * FROM R, S WHERE R.a = S.a;
```

```sql
SELECT DISTINCT name FROM users;
```

**Figura:** En el borde izquierdo hay un elemento decorativo triangular de color azul. El título «External Hashing» aparece en la parte superior en texto grande de color azul oscuro. Debajo, la pregunta «Como extender External hashing para:» en texto negro. A continuación, dos consultas SQL en fuente monoespaciada en negrita, listadas verticalmente: la primera une las tablas R y S por el atributo a; la segunda selecciona nombres distintos de la tabla users.

(slide 21)
