---
curso: SISCOMP
titulo: 08 - Semana 6/06. Memory Cache
slides: 25
fuente: 08 - Semana 6/06. Memory Cache.pdf
---

## Slide 1

Portada (decorativa: fondo azul con silueta de robot/humano en túnel tecnológico).

**COMPUTING SYSTEMS**

Memory & Cache

## Slide 2

**Goals**

Learn about how computers **store information**, and the different memory levels are used to **improve performance**

(Imagen decorativa a la izquierda: científica de laboratorio con gafas de seguridad y tubos de ensayo, tintada de azul.)

## Slide 3

**Summary**

1. Memory Hierarchy (icono de portapapeles/checklist)
2. Cache Locality (icono de bombilla)
3. …. (icono de bombilla)

(Imagen decorativa a la izquierda: mujer usando gafas de realidad virtual; fondo de globo terráqueo digital.)

## Slide 4

Slide de sección (divisora).

**1.**

**Memory Hierarchy** (icono de portapapeles)

(Imagen decorativa a la derecha: mano robótica tocando un globo digital.)

## Slide 5

**RISC-V Pseudoinstructions**

- Not part of the instruction set (cannot be directly converted to machine code).
- They are useful to programmers and compilers.
- Their intended goal CAN be achieved with one or more "real" instructions.
- They are **converted** into CPU compatible instructions during assembly.

> Recuadro gris destacado: **Pseudoinstructions are useful when coding, but the CPU ends up executing something different** 😊

## Slide 6

**Computer performance depends on:**

- **Processor performance** (en verde)
- **Memory system performance** (en rojo)

**Diagrama (bloques y señales):** dos bloques rectangulares conectados.

- Bloque izquierdo **Processor**, con entrada de reloj **CLK** arriba.
- Bloque derecho **Memory**, con entrada de reloj **CLK** arriba y una entrada **WE** (write enable) en la esquina superior izquierda.
- Señales del Processor hacia Memory (flechas azules): **MemWrite** → entra al WE de Memory; **Address** → Memory; **WriteData** → Memory.
- Salida de Memory: **ReadData**, que se realimenta por un bus azul de vuelta a la entrada izquierda del Processor (lazo cerrado por debajo de ambos bloques).

## Slide 7

**Memory Hierarchy**

**Diagrama de pirámide** (a la izquierda). El eje vertical marca **Speed** (aumenta hacia arriba) y **Capacity** (aumenta hacia abajo); el eje horizontal en la base marca **Capacity**. La pirámide está dividida en niveles de arriba (punta) hacia abajo (base):
1. Cache
2. Main Memory
3. Virtual Memory

**Tabla** (a la derecha):

| Technology | Price / GB | Access Time (ns) | Bandwidth (GB/s) |
|------------|-----------|------------------|------------------|
| SRAM | $10,000 | 1 | 25+ |
| DRAM | $10 | 10 - 50 | 10 |
| SSD | $1 | 100,000 | 0.5 |
| HDD | $0.1 | 10,000,000 | 0.1 |

(La línea "Cache" de la pirámide se alinea con SRAM; "Main Memory" con DRAM; "Virtual Memory" con SSD/HDD.)

## Slide 8

**Memory Hierarchy**

Misma pirámide (Cache / Main Memory / Virtual Memory con ejes Speed y Capacity) y misma tabla que la Slide 7:

| Technology | Price / GB | Access Time (ns) | Bandwidth (GB/s) |
|------------|-----------|------------------|------------------|
| SRAM | $10,000 | 1 | 25+ |
| DRAM | $10 | 10 - 50 | 10 |
| SSD | $1 | 100,000 | 0.5 |
| HDD | $0.1 | 10,000,000 | 0.1 |

Añade el mensaje en la parte inferior:

**Fast Memory is Expensive**
**Cheap Memory is Slow**

## Slide 9

**Locality Principles**

Exploit **locality to make memory accesses fast**

1. **Temporal Locality:**
   - Locality in time
   - If data used recently, likely to use it again soon
   - **How to exploit:** keep recently accessed data in higher levels of memory hierarchy

2. **Spatial Locality:**
   - Locality in space
   - If data used recently, likely to use nearby data soon
   - **How to exploit:** when access data, bring nearby data into higher levels of memory hierarchy too

## Slide 10

**Memory Performance**

- **Hit:** data found in that level of memory hierarchy
- **Miss:** data not found (must go to next level)

**Hit Rate** = # hits / # memory accesses = 1 − Miss Rate

**Miss Rate** = # misses / # memory accesses = 1 − Hit Rate

- **Average memory access time (AMAT):** average time for processor to access data

$$AMAT = t_{cache} + MR_{cache}[t_{MM} + MR_{MM}(t_{VM})]$$

## Slide 11

**Example: Performance**

- A program has 2,000 loads and stores
- 1,250 of these data values in cache
- Rest supplied by other levels of memory hierarchy
- Suppose processor has 2 levels of hierarchy: cache and main memory: $t_{cache}$ = 1 cycle, $t_{MM}$ = 100 cycles
- **What are the hit and miss rates for the cache?**
- **What is the AMAT?**

**Hit Rate** = 1250/2000 = **0.625**

**Miss Rate** = 750/2000 = **0.375** = 1 − Hit Rate

## Slide 12

**Example: Performance** (misma que Slide 11, ahora con la resolución del AMAT).

- A program has 2,000 loads and stores
- 1,250 of these data values in cache
- Rest supplied by other levels of memory hierarchy
- Suppose processor has 2 levels of hierarchy: cache and main memory: $t_{cache}$ = 1 cycle, $t_{MM}$ = 100 cycles
- **What are the hit and miss rates for the cache?**
- **What is the AMAT?**

**Hit Rate** = 1250/2000 = **0.625**

**Miss Rate** = 750/2000 = **0.375** = 1 − Hit Rate

$$AMAT = t_{cache} + MR_{cache}(t_{MM})$$
$$= [1 + 0.375(100)] \text{ cycles}$$
$$= \textbf{38.5 cycles}$$

## Slide 13

Slide de sección (divisora).

**2.**

**Cache Organization** (icono de portapapeles)

(Imagen decorativa a la derecha: mano robótica tocando un globo digital.)

## Slide 14

**What data is held in the cache?**

- Ideally, cache anticipates needed data and puts it in cache
- **But impossible to predict future**

> Recuadro destacado (fondo crema):
> - **Recall:** Use past to predict future: temporal and spatial locality
>   - **Temporal locality:** copy newly accessed data into cache
>   - **Spatial locality:** copy neighboring data into cache too

## Slide 15

**Cache Terminology**

- **Capacity (C):**
  - number of data bytes in cache
- **Block size (b) (a.k.a. line size):** (fila resaltada en azul)
  - bytes of data brought into cache at once
- **Number of blocks (B = C/b):**
  - number of blocks in cache: B = C/b
- **Degree of associativity (N):**
  - number of blocks in a set
- **Number of sets (S = B/N):**
  - each memory address maps to exactly one cache set

## Slide 16

**Cache Overview**

- Example:
- **Multi-level:**
  - Level 1 cache (64KB)
  - Level 2 cache (256KB)
  - Level 3 cache (>10MB)
- Block size: 64B
- High associativity.

> Nota (recuadro verde): **For educational purposes, we analyze a system with only 1 level cache and a few-Bytes of line size.**

**Captura/imagen (derecha):** fotografía de un die de microprocesador (vista de chip a color, verdes/naranjas/rojos). Regiones etiquetadas sobre el chip:
- **256 KB Level 2 Unified Cache** (bloque grande verde-amarillo a la izquierda, resaltado en franja azul).
- **16 KB Level 1 Data Cache** (bloque naranja arriba a la derecha, resaltado en franja rosada).
- **16 KB Level 1 Instruction Cache** (bloque naranja abajo a la derecha).

## Slide 17

**Cache Organization: How is data found?**

> Recuadro destacado (fondo verde claro):
> - Cache organized into **S** sets
> - Each memory address maps to exactly one set
> - **Caches categorized by # of blocks in a set:**
>   1. **Direct mapped:** 1 block per set
>   2. **N-way set associative:** N blocks per set
>   3. **Fully associative:** all cache blocks in 1 set

- **Example:** Examine each organization for a (small) cache with:
  - Capacity (C = 8 words)
  - Block size (b = 1 word)
  - So, number of blocks (B = 8)

## Slide 18

**Direct Mapped Cache**

**Diagrama de mapeo memoria → cache.** A la izquierda una columna **Address** (direcciones binarias) junto a una tabla vertical de **2³⁰ Word Main Memory** con celdas etiquetadas por su contenido `mem[0x...]`; a la derecha una tabla pequeña de **2³ Word Cache** con **Set Number** 0..7 (en binario 000..111).

Direcciones de memoria (de arriba a abajo), con los bits de índice de set en negrita:

```
11...11111100   mem[0xFF...FC]
11...11111000   mem[0xFF...F8]
11...11110100   mem[0xFF...F4]
11...11110000   mem[0xFF...F0]   (resaltada)
11...11101100   mem[0xFF...EC]
11...11101000   mem[0xFF...E8]
11...11100100   mem[0xFF...E4]   (resaltada)
11...11100000   mem[0xFF...E0]
        ⋮              ⋮
00...00100100   mem[0x00...24]   (resaltada)
00...00100000   mem[0x00..20]
00...00011100   mem[0x00..1C]
00...00011000   mem[0x00...18]
00...00010100   mem[0x00...14]
00...00010000   mem[0x00...10]   (resaltada)
00...00001100   mem[0x00...0C]
00...00001000   mem[0x00...08]
00...00000100   mem[0x00...04]   (resaltada)
00...00000000   mem[0x00...00]
```

Flechas: varias direcciones de memoria (con el mismo índice de set) apuntan al mismo bloque de cache. Ejemplo mostrado: `mem[0xFF...F0]` y `mem[0x00...10]` (índice 100) → **Set 4 (100)**; `mem[0xFF...E4]`, `mem[0x00...24]` y `mem[0x00...04]` (índice 001) → **Set 1 (001)**. Idea: cada dirección mapea a exactamente un set (los bits de índice de set determinan la posición).

## Slide 19

**Direct Mapped Cache Performance**

**RISC-V Assembly Code** (recuadro azul, izquierda):
```asm
        li  x1, 5
        li  x2, 0
LOOP:
        beq x1, x0, DONE
        lw  x2, 4(x1)
        lw  x3, 12(x1)
        lw  x4, 8(x1)
        addi x1,x1,-1
        j   LOOP
DONE:
```

**Diagrama (derecha):** descomposición de la **Memory Address** en campos: **Tag** = `00...00`, **Set** = `001` (3 bits), **Byte Offset** = `00`. Los 3 bits del set indexan la tabla de cache.

Tabla de cache (columnas **V | Tag | Data**), con **Set Number** 0..7 (111..000):

| Set | V | Tag | Data |
|-----|---|-----|------|
| Set 7 (111) | 0 | | |
| Set 6 (110) | 0 | | |
| Set 5 (101) | 0 | | |
| Set 4 (100) | 0 | | |
| Set 3 (011) | 1 | 00...00 | mem[0x00...0C] |
| Set 2 (010) | 1 | 00...00 | mem[0x00...08] |
| Set 1 (001) | 1 | 00...00 | mem[0x00...04] |
| Set 0 (000) | 0 | | |

**Miss Rate = 3/15 = 20%**

**Temporal Locality**
**Compulsory Misses**

## Slide 20

**N-Way Set Associative Cache**

**Diagrama de hardware** de una cache asociativa por conjuntos de 2 vías.

- **Memory Address** dividida en campos: **Tag**, **Set**, **Byte Offset** (`00`). El Tag sale con ancho de **28** bits; el Set con **2** bits (indexa las filas de la tabla).
- La tabla central tiene dos vías: **Way 1** y **Way 0**, cada una con columnas **V | Tag | Data**.
- Los Tag almacenados (28 bits) de cada vía se comparan (comparadores **=**) con el Tag de la dirección. Cada comparación, AND con el bit V, produce **Hit₁** (Way 1) y **Hit₀** (Way 0).
- **Hit₁** y **Hit₀** entran a una compuerta OR → señal **Hit**.
- Los datos de cada vía (32 bits) entran a un **MUX**, seleccionado por la señal de hit (**Hit₁**), que produce la salida **Data** (32 bits).

## Slide 21

**N-Way Set Associative Performance**

**RISC-V Assembly Code** (recuadro azul, izquierda):
```asm
        li   x1, 5
        li   x2, 0
LOOP:
        beq  x1, x0, DONE
        lw   x3, 4(x2)
        lw   x4, 36(x2)
        addi x1, x1, -1
        j    LOOP
DONE:
```

**Miss Rate = 2/10 = 20%**

**Associativity reduces conflict misses**

**Tabla de cache** de 2 vías (**Way 1** | **Way 0**), columnas **V Tag Data**, Sets 0..3:

| Set | Way 1: V | Tag | Data | Way 0: V | Tag | Data |
|-----|----------|-----|------|----------|-----|------|
| Set 3 | 0 | | | 0 | | |
| Set 2 | 0 | | | 0 | | |
| Set 1 | 1 | 00...10 | mem[0x00...24] | 1 | 00...00 | mem[0x00...04] |
| Set 0 | 0 | | | 0 | | |

(Las dos direcciones que colisionarían en el mismo set — 0x24 y 0x04 — ahora conviven, una en cada vía.)

## Slide 22

**Full Associativity**

- **Fully associative cache**
  - A block can be placed in **any** cache location

**Diagrama:** una fila de **Tag store** con 8 entradas de tag en la parte superior. Cada entrada se compara (comparador **=?**) con el tag buscado; las 8 salidas van a un bloque **Logic** que produce **Hit?**.

Debajo, **Data store** con 8 entradas de datos; todas alimentan un **MUX** grande; su salida entra a un segundo **MUX** cuya selección es **byte in block**. La salida de Logic controla la selección del MUX de datos.

## Slide 23

**Fully Associative Cache**

**Diagrama:** una única fila (un solo set) con 8 bloques, cada uno con campos **V | Tag | Data** repetidos en línea (todos los bloques de la cache en un mismo set).

> Recuadro destacado (fondo azul):
> **Reduces conflict misses**
> **Expensive to build**

## Slide 24

**Reference Books**

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). *Operating system concepts* (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).

(Imagen decorativa a la derecha: profesor escribiendo en pizarra, tintado de azul.)

## Slide 25

Slide de cierre (decorativa: fondo de laboratorio con dos personas trabajando, tintado de azul).

**Questions?**
