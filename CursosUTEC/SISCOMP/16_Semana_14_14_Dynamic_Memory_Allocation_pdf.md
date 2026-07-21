---
curso: SISCOMP
titulo: 16 - Semana 14/14. Dynamic Memory Allocation
slides: 39
fuente: 16 - Semana 14/14. Dynamic Memory Allocation.pdf
---

## Slide 1

Portada (decorativa). Título del curso: **COMPUTING SYSTEMS**. Subtítulo: "Dynamic Memory Allocation". Professor: Luz A. Adanaqué.

## Slide 2

**Motivation**

User programs need to perform tasks securely. Operating Systems has file management systems which involves Directories and Descriptors.

**Goals**

Understand how Files, Directories and Descriptors are managed in Operating Systems.

(Imagen de fondo decorativa: mujer en laboratorio.)

## Slide 3

**Summary**

1. Introduction
2. Background
3. System Calls

(Cada ítem con un icono a su izquierda; imagen de fondo decorativa: mujer con visor VR y un globo terráqueo.)

## Slide 4

Divisor de sección. **1. Dynamic Memory Allocation** (imagen decorativa de mano robótica).

## Slide 5

- Programmers use *dynamic memory allocators* (such as `malloc`) to acquire VM at run time.
  - For data structures whose size is only known at runtime.
- Dynamic memory allocators manage an area of process virtual memory known as the *heap*.

**Diagrama 1 (arriba):** pila de 3 bloques apilados verticalmente que muestra la relación de capas del software:
```
+-------------------------------+
|          Application          |
+-------------------------------+
|  Dynamic Memory Allocator     |  (resaltado en amarillo)
+-------------------------------+
|             Heap              |
+-------------------------------+
```

**Diagrama 2 (abajo):** layout de memoria virtual de un proceso, de arriba (alta dirección) hacia abajo (0):
```
+-------------------------------+
|          User stack           |
|   (flechas: crece hacia abajo)|   <- zona gris con flecha arriba y abajo
+-------------------------------+
|      Heap (via malloc)        |  <- rosado.  Flecha externa: "Top of heap (brk ptr)"
+-------------------------------+
|   Uninitialized data (.bss)   |
+-------------------------------+
|   Initialized data (.data)    |
+-------------------------------+
|     Program text (.text)      |
+-------------------------------+
0
```
El "Top of heap (brk ptr)" apunta al límite superior del Heap. La flecha del user stack y la del heap indican que ambos crecen hacia el centro.

## Slide 6

- Allocator maintains heap as collection of variable sized *blocks*, which are either *allocated* or *free*
- Types of allocators
  - ***Explicit allocator***: application allocates and frees space
    - E.g., `malloc` and `free` in C
  - ***Implicit allocator***: application allocates, but does not free space
    - E.g. garbage collection in Java, ML, and Lisp
- Will discuss simple explicit memory allocation today

## Slide 7

**Malloc Package**

```c
#include <stdlib.h>

void *malloc(size_t size)
```
- Successful:
  - Returns a pointer to a memory block of at least `size` bytes aligned to an 8-byte (x86) or 16-byte (x86-64) boundary
  - If `size == 0`, returns NULL
- Unsuccessful: returns NULL (0) and sets `errno`

```c
void free(void *p)
```
- Returns the block pointed at by `p` to pool of available memory
- `p` must come from a previous call to `malloc` or `realloc`

Other functions
- `calloc`: Version of `malloc` that initializes allocated block to zero.
- `realloc`: Changes the size of a previously allocated block.
- `sbrk`: Used internally by allocators to grow or shrink the heap

## Slide 8

**Malloc Example**

Bloque de código C (recuadro amarillo, con sintaxis coloreada):
```c
#include <stdio.h>
#include <stdlib.h>

void foo(int n) {
    int i, *p;

    /* Allocate a block of n ints */
    p = (int *) malloc(n * sizeof(int));
    if (p == NULL) {
        perror("malloc");
        exit(0);
    }

    /* Initialize allocated block */
    for (i=0; i<n; i++)
        p[i] = i;

    /* Return allocated block to the heap */
    free(p);
}
```

## Slide 9

**Allocation Example**

Diagrama: una tira horizontal de ~18 celdas (memoria) por cada operación, mostrando cómo se van ocupando celdas. Cada malloc pinta N celdas contiguas de un color distinto.

| Operación | Celdas ocupadas (esquema) |
|-----------|----------------------------|
| `p1 = malloc(4)` | 4 celdas amarillas al inicio, resto libre |
| `p2 = malloc(5)` | 4 amarillas + 5 naranjas, resto libre |
| `p3 = malloc(6)` | 4 amarillas + 5 naranjas + 6 rosadas, resto libre |
| `free(p2)` | 4 amarillas, hueco de 5 libres, 6 rosadas |
| `p4 = malloc(2)` | 4 amarillas + 2 verdes (reusa parte del hueco) + 3 libres + 6 rosadas |

Ilustra que p4 (tamaño 2) se coloca dentro del hueco liberado por p2 (tamaño 5), dejando 3 celdas libres.

## Slide 10

**Constraints**

- Applications
  - Can issue arbitrary sequence of `malloc` and `free` requests
  - `free` request must be to a `malloc`'d block
- Allocators
  - Can't control number or size of allocated blocks
  - Must respond immediately to `malloc` requests
    - *i.e.*, can't reorder or buffer requests
  - Must allocate blocks from free memory
    - *i.e.*, can only place allocated blocks in free memory
  - Must align blocks so they satisfy all alignment requirements
    - 8-byte (x86) or 16-byte (x86-64) alignment on Linux boxes
  - Can manipulate and modify only free memory
  - Can't move the allocated blocks once they are `malloc`'d
    - *i.e.*, compaction is not allowed

## Slide 11

**Throughput**

- Given some sequence of `malloc` and `free` requests:
  - $R_0, R_1, ..., R_k, ..., R_{n-1}$
- Goals: maximize throughput and peak memory utilization
  - These goals are often conflicting
- Throughput:
  - Number of completed requests per unit time
  - Example:
    - 5,000 `malloc` calls and 5,000 `free` calls in 10 seconds
    - Throughput is 1,000 operations/second

## Slide 12

**Peak Memory Utilization**

- Given some sequence of `malloc` and `free` requests:
  - $R_0, R_1, ..., R_k, ..., R_{n-1}$
- *Def: Aggregate payload $P_k$*
  - `malloc(p)` results in a block with a *payload* of `p` bytes
  - After request $R_k$ has completed, the *aggregate payload* $P_k$ is the sum of currently allocated payloads
- *Def: Current heap size $H_k$*
  - Assume $H_k$ is monotonically nondecreasing
    - i.e., heap only grows when allocator uses `sbrk`
- *Def: Peak memory utilization after k+1 requests*
  - $U_k = \left( \max_{i \le k} P_i \right) / H_k$

## Slide 13

Divisor de sección. **2. Fragmentation** (imagen decorativa de mano robótica).

## Slide 14

**Internal Fragmentation**

- For a given block, *internal fragmentation* occurs if payload is smaller than block size

**Diagrama:** un bloque ("Block", con llave abarcando todo) compuesto de: una zona gris a la izquierda + zona amarilla central ("Payload") + zona gris a la derecha. Ambas zonas grises tienen flechas etiquetadas "Internal fragmentation". Es decir, la fragmentación interna es el espacio del bloque no usado por el payload (a ambos lados).

- Caused by
  - Overhead of maintaining heap data structures
  - Padding for alignment purposes
  - Explicit policy decisions (e.g., to return a big block to satisfy a small request)
- Depends only on the pattern of *previous* requests
  - Thus, easy to measure

## Slide 15

**External Fragmentation**

- Occurs when there is enough aggregate heap memory, but no single free block is large enough

**Diagrama:** tiras de memoria (18 celdas) por operación, igual formato que la slide 9:

| Operación | Esquema |
|-----------|---------|
| `p1 = malloc(4)` | 4 amarillas, resto libre |
| `p2 = malloc(5)` | 4 amarillas + 5 naranjas |
| `p3 = malloc(6)` | 4 amarillas + 5 naranjas + 6 rosadas |
| `free(p2)` | 4 amarillas + hueco 5 libres + 6 rosadas |
| `p4 = malloc(6)` | *Oops! (what would happen now?)* |

El punto: hay 5+resto celdas libres en total, pero ningún hueco contiguo de 6, así que `malloc(6)` no puede satisfacerse aunque haya suficiente memoria agregada.

- Depends on the pattern of *future* requests
  - Thus, difficult to measure

## Slide 16

**How much to free?**

- Standard method
  - Keep the length of a block in the word preceding the block.
    - This word is often called the ***header field*** or ***header***
  - Requires an extra word for every allocated block

**Diagrama:** tres tiras de memoria mostrando el mismo heap en tres momentos:
- Fila 1 (estado inicial): celdas con algunas ocupadas (grises) y libres (blancas).
- Fila 2 (`p0 = malloc(4)`): se marca una celda "5" (rosada) = header con "block size", seguida de 4 celdas verdes = "payload". El puntero `p0` apunta a la primera celda del payload (justo después del header). Flechas etiquetan "block size" (la celda 5) y "payload" (las 4 verdes).
- Fila 3 (`free(p0)`): las celdas vuelven a estado libre.

El header "5" indica que el bloque total ocupa 5 words (1 header + 4 payload).

## Slide 17

**Keeping Track of free blocks**

- Method 1: *Implicit list* using length—links all blocks

  **Diagrama:** tira de memoria con headers etiquetados con su tamaño: bloque `5`, luego `4` (celdas grises = allocated), luego `6`, luego `2`. Flechas curvas conectan cada header con el siguiente (5→4→6→2), formando una lista implícita donde el tamaño de cada bloque permite saltar al siguiente.

- Method 2: *Explicit list* among the free blocks using pointers

  **Diagrama:** misma tira (`5`, `4` gris allocated, `6`, `2` gris), pero ahora solo una flecha curva conecta los bloques *libres* (5→6), saltando los allocated.

- Method 3: *Segregated free list*
  - Different free lists for different size classes
- Method 4: *Blocks sorted by size*
  - Can use a balanced tree (e.g. Red-Black tree) with pointers within each free block, and the length used as a key

## Slide 18

**Method 1: Implicit List**

- For each block we need both size and allocation status
  - Could store this information in two words: wasteful!
- Standard trick
  - If blocks are aligned, some low-order address bits are always 0
  - Instead of storing an always-0 bit, use it as a allocated/free flag
  - When reading size word, must mask out this bit

**Diagrama — Format of allocated and free blocks:** un bloque vertical de 1 word de ancho:
```
+-----------------+---+
|      Size       | a |   <- 1 word (rosado)
+-----------------+---+
|                     |
|      Payload        |   (verde)
|                     |
+---------------------+
|   Optional padding  |   (gris)
+---------------------+
```
Leyenda:
- `a = 1`: Allocated block
- `a = 0`: Free block
- Size: block size
- Payload: application data (allocated blocks only)

El bit `a` es el bit bajo del word de tamaño (aprovechando el alineamiento).

## Slide 19

**Detailed Implicit Free List Example**

**Diagrama:** una tira larga de memoria etiquetada "Start of heap" a la izquierda, dividida en bloques con headers de la forma *tamaño/bit*:
- `Unused` (word inicial de relleno, rayado)
- `8/0` (bloque libre de 8 bytes)
- `16/1` (bloque allocated de 16 bytes, celdas grises)
- `32/0` (bloque libre de 32 bytes)
- `16/1` (bloque allocated de 16 bytes, celdas grises)
- `0/1` (bloque terminador de tamaño 0, allocated — marca fin del heap, rayado)

Flechas curvas conectan cada header al siguiente (lista implícita). Línea punteada abajo: "Double-word aligned".

Leyenda:
- Allocated blocks: shaded (sombreados)
- Free blocks: unshaded (sin sombra)
- Headers: labeled with size in bytes/allocated bit

## Slide 20

**Implicit List: Finding a free block**

- *First fit:*
  - Search list from beginning, choose *first* free block that fits:

  Bloque de código (recuadro amarillo):
  ```c
  p = start;
  while ((p < end) &&        \\ not passed end
         ((*p & 1) ||        \\ already allocated
          (*p <= len)))      \\ too small
     p = p + (*p & -2);      \\ goto next block (word addressed)
  ```
  - Can take linear time in total number of blocks (allocated and free)
  - In practice it can cause "splinters" at beginning of list
- *Next fit:*
  - Like first fit, but search list starting where previous search finished
  - Should often be faster than first fit: avoids re-scanning unhelpful blocks
  - Some research suggests that fragmentation is worse
- *Best fit:*
  - Search the list, choose the *best* free block: fits, with fewest bytes left over
  - Keeps fragments small—usually improves memory utilization
  - Will typically run slower than first fit

## Slide 21

**Allocating in free block**

- Allocating in a free block: *splitting*
  - Since allocated space might be smaller than free space, we might want to split the block

**Diagrama (antes):** tira con bloques `4` (libre), `4` (allocated gris), `6` (libre, con puntero `p` apuntando a él), `2` (allocated gris). Flechas conectan headers.

`addblock(p, 4)`

**Diagrama (después):** el bloque `6` libre se divide en `4` (ahora allocated, verde claro) + `2` (remanente libre). Resultado: `4`, `4`(gris), `4`(verde/allocated), `2`(remanente), `2`(gris).

Código (recuadro amarillo):
```c
void addblock(ptr p, int len) {
    int newsize = ((len + 1) >> 1) << 1;  // round up to even
    int oldsize = *p & -2;                // mask out low bit
    *p = newsize | 1;                     // set new length
    if (newsize < oldsize)
        *(p+newsize) = oldsize - newsize; // set length in remaining
}                                         //   part of block
```

## Slide 22

**Freeing a block**

- Simplest implementation:
  - Need only clear the "allocated" flag
    ```c
    void free_block(ptr p) { *p = *p & -2 }
    ```
  - But can lead to "false fragmentation"

**Diagrama (antes de free):** tira con `4`, `4`(gris allocated), `4`(verde, con puntero `P`), `2`, `2`(gris). 

`free(p)`

**Diagrama (después):** el bloque de `P` queda libre, pero el bloque `4` de al lado también estaba libre — quedan dos bloques `4` libres adyacentes sin fusionar: `4`, `4`(gris), `4`(libre), `2`, `2`(gris).

`malloc(5)` → ***Oops!***

*There is enough free space, but the allocator won't be able to find it* (porque los dos bloques libres de 4 no se combinaron en uno de 8).

## Slide 23

**Coalescing**

- Join *(coalesce)* with next/previous blocks, if they are free
  - Coalescing with next block

**Diagrama (antes):** tira `4`, `4`(gris), `4`(verde, puntero `P`), `2`(libre), `2`(gris). El bloque `2` que sigue a P está libre.

`free(p)`

**Diagrama (después):** el bloque de P (4) se fusiona con el siguiente bloque libre (2) → un bloque `6`. El resto: `4`, `4`(gris), `6`, `2`(gris). Una flecha roja etiquetada "*logically gone*" señala el header del bloque `2` que desapareció al fusionarse.

Código (recuadro amarillo):
```c
void free_block(ptr p) {
    *p = *p & -2;          // clear allocated flag
    next = p + *p;         // find next block
    if ((*next & 1) == 0)
        *p = *p + *next;   // add to this block if
}                          //   not allocated
```

- But how do we coalesce with *previous* block?

## Slide 24

**Bidirectional Coalescing**

- *Boundary tags* [Knuth73]
  - Replicate size/allocated word at "bottom" (end) of free blocks
  - Allows us to traverse the "list" backwards, but requires extra space
  - Important and general technique!

**Diagrama:** tira de memoria donde cada bloque tiene su tamaño replicado al inicio (header) y al final (footer): `4 ... 4 | 4 ... 4 | 6 ... 6 | 4 ... 4`. Flechas curvas hacia adelante (arriba) y hacia atrás (abajo) muestran que se puede recorrer la lista en ambos sentidos.

**Format of allocated and free blocks:** bloque vertical:
```
+-----------+---+
| Header:   |   |
|   Size    | a |   (rosado)
+-----------+---+
|               |
| Payload and   |   (verde)
|   padding     |
+-----------+---+
| Boundary  |   |
| tag(foot):|   |
|   Size    | a |   (rosado)
+-----------+---+
```
Leyenda:
- `a = 1`: Allocated block
- `a = 0`: Free block
- Size: Total block size
- Payload: Application data (allocated blocks only)

## Slide 25

**Constant time coalescing**

Tabla de 4 casos según el estado (allocated/free) de los bloques vecinos al "Block being freed". El bloque central (amarillo) es el que se libera; arriba está el bloque previo, abajo el siguiente:

| | Case 1 | Case 2 | Case 3 | Case 4 |
|--|--------|--------|--------|--------|
| Bloque previo (arriba) | Allocated | Allocated | Free | Free |
| Bloque liberado (centro) | *(freed)* | *(freed)* | *(freed)* | *(freed)* |
| Bloque siguiente (abajo) | Allocated | Free | Allocated | Free |

## Slide 26

**Constant time coalescing (case 1)** — vecinos ambos allocated.

**Diagrama (izquierda, antes):** bloques verticales con header/footer:
```
m1 | 1      (allocated, previo)
   |
m1 | 1
n  | 1      (bloque a liberar, amarillo)
   |
n  | 1
m2 | 1      (allocated, siguiente)
   |
m2 | 1
```

→ (flecha) →

**Diagrama (derecha, después):**
```
m1 | 1
   |
m1 | 1
n  | 0      (ahora libre, blanco)
   |
n  | 0
m2 | 1
   |
m2 | 1
```
Solo cambia el bit del bloque n de 1 a 0; el tamaño no cambia (no hay fusión porque ambos vecinos están allocated).

## Slide 27

**Constant time coalescing (case 2)** — previo allocated, siguiente free.

**Diagrama (antes):**
```
m1 | 1
   |
m1 | 1
n  | 1     (a liberar, amarillo)
   |
n  | 1
m2 | 0     (siguiente, libre)
   |
m2 | 0
```

→

**Diagrama (después):** el bloque n se fusiona con el siguiente (m2), formando un bloque libre de tamaño `n+m2`:
```
m1   | 1
     |
m1   | 1
n+m2 | 0     (header)
     |
     |
n+m2 | 0     (footer)
```

## Slide 28

**Constant time coalescing (case 3)** — previo free, siguiente allocated.

**Diagrama (antes):**
```
m1 | 0     (previo, libre)
   |
m1 | 0
n  | 1     (a liberar, amarillo)
   |
n  | 1
m2 | 1     (siguiente, allocated)
   |
m2 | 1
```

→

**Diagrama (después):** el bloque n se fusiona con el previo (m1) → bloque libre `n+m1`:
```
n+m1 | 0     (header)
     |
     |
n+m1 | 0     (footer)
m2   | 1
     |
m2   | 1
```

## Slide 29

**Constant time coalescing (case 4)** — ambos vecinos free.

**Diagrama (antes):**
```
m1 | 0     (previo, libre)
   |
m1 | 0
n  | 1     (a liberar, amarillo)
   |
n  | 1
m2 | 0     (siguiente, libre)
   |
m2 | 0
```

→

**Diagrama (después):** los tres bloques se fusionan en uno solo libre de tamaño `n+m1+m2`:
```
n+m1+m2 | 0     (header)
        |
        |
n+m1+m2 | 0     (footer)
```

## Slide 30

**Boundary Tags**

- Internal fragmentation
- Can it be optimized?
  - Which blocks need the footer tag?
  - What does that mean?

## Slide 31

**Key Allocator Policies**

- Placement policy:
  - First-fit, next-fit, best-fit, etc.
  - Trades off lower throughput for less fragmentation
  - ***Interesting observation***: segregated free lists (next lecture) approximate a best fit placement policy without having to search entire free list
- Splitting policy:
  - When do we go ahead and split free blocks?
  - How much internal fragmentation are we willing to tolerate?
- Coalescing policy:
  - ***Immediate coalescing:*** coalesce each time `free` is called
  - ***Deferred coalescing:*** try to improve performance of `free` by deferring coalescing until needed. Examples:
    - Coalesce as you scan the free list for `malloc`
    - Coalesce when the amount of external fragmentation reaches some threshold

## Slide 32

**Implicit Lists**

- Implementation: very simple
- Allocate cost:
  - linear time worst case
- Free cost:
  - constant time worst case
  - even with coalescing
- Memory usage:
  - will depend on placement policy
  - First-fit, next-fit or best-fit
- Not used in practice for `malloc/free` because of linear-time allocation
  - used in many special purpose applications
- However, the concepts of splitting and boundary tag coalescing are general to *all* allocators

## Slide 33

**Method 2: Explicit free lists**

**Diagrama — formato de bloques:** dos bloques verticales lado a lado:

Allocated:
```
Size | a   (rosado)
Payload and
  padding   (verde)
Size | a   (rosado, footer)
```

Free:
```
Size | a   (rosado)
Next        (naranja)
Prev        (naranja)
(espacio libre)
Size | a   (rosado, footer)
```
En los bloques libres, el área de payload se reutiliza para guardar los punteros Next y Prev.

- Maintain list(s) of *free* blocks, not *all* blocks
  - The "next" free block could be anywhere
    - Need to store forward/back pointers, not just sizes
  - Still need boundary tags for coalescing
  - We track only free blocks, so we can use payload area

## Slide 34

**Explicit free lists**

- Logically:

  **Diagrama:** lista doblemente enlazada de 3 nodos: `A ⇄ B ⇄ C`, con flechas verdes (forward/next) hacia adelante y flechas rojas (back/prev) hacia atrás.

- Physically: blocks can be in any order

  **Diagrama:** tira de memoria con bloques dispersos. Los bloques libres A, B, C están en posiciones no consecutivas. Flechas verdes ("Forward (next) links") conectan A→B→C en orden lógico saltando por el heap; flechas rojas ("Back (prev) links") los conectan en sentido inverso. Ilustra que el orden físico en memoria es independiente del orden lógico de la lista enlazada.

## Slide 35

**Insertion Policy**

- *Insertion policy*: Where in the free list do you put a newly freed block?
- **LIFO (last-in-first-out) policy**
  - Insert freed block at the beginning of the free list
  - *Pro:* simple and constant time
  - *Con:* studies suggest fragmentation is worse than address ordered
- **Address-ordered policy**
  - Insert freed blocks so that free list blocks are always in address order:
    - $addr(prev) < addr(curr) < addr(next)$
  - *Con:* requires search
  - *Pro:* studies suggest fragmentation is lower than LIFO

## Slide 36

**Summary**

- Comparison to implicit list:
  - Allocate is linear time in number of *free* blocks instead of *all* blocks
    - *Much faster* when most of the memory is full
  - Slightly more complicated allocate and free since needs to splice blocks in and out of the list
  - Some extra space for the links (2 extra words needed for each block)
    - Does this increase internal fragmentation?
- Most common use of linked lists is in conjunction with segregated free lists
  - Keep multiple linked lists of different size classes, or possibly for different types of objects

## Slide 37

**Segregated List Allocators**

- Each *size class* of blocks has its own free list

**Diagrama:** array de free lists, una por clase de tamaño. Cada fila es una lista enlazada horizontal de bloques (con flechas →):
- `1-2`: lista de bloques de 2 celdas (4 nodos)
- `3`: lista de bloques de 3 celdas (varios nodos)
- `4`: lista de bloques de 4 celdas
- `5-8`: lista de bloques de ~6 celdas
- `9-inf`: lista de un bloque grande

El tamaño de las celdas de cada nodo corresponde a su clase de tamaño.

- Often have separate classes for each small size
- For larger sizes: One class for each two-power size

## Slide 38

**Segregated List Allocators**

- Given an array of free lists, each one for some size class
- To allocate a block of size *n*:
  - Search appropriate free list for block of size *m > n*
  - If an appropriate block is found:
    - Split block and place fragment on appropriate list (optional)
  - If no block is found, try next larger class
  - Repeat until block is found
- If no block is found:
  - Request additional heap memory from OS (using `sbrk()`)
  - Allocate block of *n* bytes from this new memory
  - Place remainder as a single free block in largest size class.

## Slide 39

**Segregated List Allocators**

- To free a block:
  - Coalesce and place on appropriate list
- Advantages of segregated list allocators:
  - Higher throughput
    - log time for power-of-two size classes
  - Better memory utilization
    - First-fit search of segregated free list approximates a best-fit search of entire heap
    - Extreme case: giving each block its own size class is equivalent to best-fit
