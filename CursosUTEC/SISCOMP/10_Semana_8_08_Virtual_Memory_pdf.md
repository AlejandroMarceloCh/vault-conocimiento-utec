---
curso: SISCOMP
titulo: 10 - Semana 8/08. Virtual Memory
slides: 20
fuente: 10 - Semana 8/08. Virtual Memory.pdf
---

## Slide 1

Portada decorativa. Título grande "COMPUTING SYSTEMS" con subtítulo "Paging & Virtual Memory" sobre imagen de un robot/androide caminando por un túnel tecnológico azul. Logo UTEC y "Reinventa el mundo".

## Slide 2

**Goals** (portada de sección, imagen decorativa de laboratorista a la izquierda)

Learn about how computers **manage memory, for efficient allocation of user programs data.**

## Slide 3

**Summary** (imagen decorativa de mujer con visor VR y globo terráqueo)

1. (icono de checklist) Paging
2. (icono de bombilla) Virtual Memory

## Slide 4

Portada de sección decorativa (mano robótica tocando un globo). Número **1.** con icono de checklist y título **Paging**.

## Slide 5

# Paging: Physical Memory in Fixed Size Chunks

Slide solo de texto (sin figura). Contenido con bullets:

- Solution to fragmentation from segments?
  - **Allocate physical memory in fixed size chunks ("pages")**
  - **Every chunk of physical memory is equivalent**
    - Can use simple vector of bits to handle allocation: `00110001110001101 … 110010`
    - Each bit represents page of physical memory: `1 ⇒ allocated, 0 ⇒ free`
- Should pages be as big as our previous segments?
  - **No:** Can lead to lots of internal fragmentation
    - **Typically have small pages (1K-16K)**
  - Consequently: need multiple pages/segment

## Slide 6

# How to Implement Paging?

**Diagrama de traducción de dirección virtual a física (arriba):**
- Dirección virtual dividida en dos campos: **VP#** (rojo) + **Offset** (celeste).
- El **VP#** entra como índice a una tabla de páginas (Page Table, dibujada como tabla verde de varias filas con dos columnas). Una fila destacada en azul es la entrada seleccionada.
- Dos cajas rosadas a la izquierda alimentan el chequeo: una caja superior (base de la tabla) apunta a la Page Table; **PageTableSize** entra a un comparador (círculo rosado) que puede disparar **Access Error** (flecha hacia abajo) si el VP# excede el tamaño.
- De la entrada seleccionada (azul) sale (flecha roja) el número de página física, que forma la **Physical Address** = campo rojo (physical page) + **Offset** (celeste, copiado directamente desde la dirección virtual arriba). Debajo, una caja rosada representa la memoria física accedida.

**Texto (bullets):**
- **Page Table (One per process)**
  - Resides in physical memory
  - Contains physical page and permission for each virtual page
    - Permissions include: Valid bits, Read, Write, etc
- **Virtual address mapping**
  - Offset from Virtual address copied to Physical Address
    - Example: 10 bit offset Þ 1024-byte pages
  - Virtual page # is all remaining bits
    - Example for 32-bits: 32-10 = 22 bits, i.e. 4 million entries
    - Physical page # copied from table into physical address
  - Check Page Table bounds and permissions

## Slide 7

# Simple Paging

Slide de texto (sin figura). Recuadros de color como resaltado.

**Description:**
- **Physical address space of a process can be noncontiguous:** process is allocated physical memory if available
  - **Avoids external fragmentation**
  - **Avoids problem of varying sized memory chunks**

**Characteristics:**
- **Divide physical memory into fixed-sized blocks** called **frames**
  - **Size is power of 2**, between 512 bytes and 16 Mbytes
- **Divide logical memory into blocks of same size** called **pages**
  - **Backing store likewise split into pages**
- **Keep track** of all **free frames**
  - E.g: To run a program of size **N** pages, need to find **N** free frames and load program
- **Set up a page table** to translate logical to physical addresses
- Still have Internal fragmentation

## Slide 8

# Address Translation

- Address generated: by CPU is divided into:
  - **Page number (p) used as an index into a page table** which contains base address of each page in physical memory
  - **Page offset (d): combined with base address** to define the physical memory address that is sent to the memory unit

**Tabla (diagrama del formato de dirección lógica):** una fila con dos celdas encabezadas `p` y `page_of`; debajo los valores `p` y `d`; y las anchuras en bits `m - n` (para p) y `n` (para el offset).

Recuadro verde inferior: **For given logical address space 2^m and page size 2^n**

$$\text{dirección lógica: } [\underbrace{p}_{m-n\text{ bits}} \mid \underbrace{d}_{n\text{ bits}}]$$

## Slide 9

# Paging

**Bullets izquierda:**
- **Example:** Calculating internal fragmentation
  - Page size = 2,048 bytes
  - Process size = 72,766 bytes
  - 35 pages + 1,086 bytes
  - Internal fragmentation of 2,048 - 1,086 = 962 bytes
  - Worst case fragmentation = 1 frame − 1 byte
  - On average fragmentation = 1 / 2 frame size
- **So small frame sizes desirable?**
  - But each page table entry takes memory to track
- **Page sizes growing over time**
  - Solaris supports two page sizes: 8 KB and 4 MB
  - **Linux:** default 4KB, huge pages from 2MB to GB order
- Process view and physical memory now very different
- **Process can only access its own memory**

**Diagrama derecha (ejemplo clásico n=2, m=4, memoria de 32 bytes y páginas de 4 bytes):**
- **Logical memory:** columna de 16 celdas (0..15) con letras a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p (una letra por celda, agrupadas en 4 páginas de 4 bytes).
- **Page table:** entradas 0→5, 1→6, 2→1, 3→2.
- **Physical memory:** columna con marcas 0,4,8,12,16,20,24,28. Contiene: en el frame 4 → i,j,k,l; en el frame 8 → m,n,o,p; en el frame 20 → a,b,c,d; en el frame 24 → e,f,g,h. (Cada página lógica mapeada al frame indicado por la page table.)
- Leyenda: "E.g.: n=2 and m=4  32-byte memory and 4-byte pages"

## Slide 10

# Effective Access Time

Recuadro amarillo (fórmula):

$$EAT = (1 + \varepsilon)\,\alpha + (2 + \varepsilon)(1 - \alpha) = 2 + \varepsilon - \alpha$$

- Associative Lookup = ε time unit
  - Can be < 10% of memory access time
- Hit ratio = α
  - **Hit ratio:** percentage of times that a page number is found in the associative registers; ratio related to number of associative registers

**Example:**
- Consider α = 80%, ε = 20ns for TLB search, 100ns for memory access
  - EAT = 0.80 × 100 + 0.20 × 200 = 120ns
- Consider more realistic hit ratio -> α = 99%, ε = 20ns for TLB search, 100ns for memory access
  - EAT = 0.99 × 100 + 0.01 × 200 = 101ns

## Slide 11

Portada de sección decorativa (mano robótica y globo). Número **2.** con icono de checklist y título **Virtual Memory**.

## Slide 12

# Virtual Memory

Slide de texto (sin figura).

- **Definition:** separation of user logical memory from physical memory
  - **Only part of the program needs to be in memory for execution**
- **Logical address space can therefore be much larger than physical address space**
- **Allows address spaces to be shared by several processes**
- **Allows for more efficient process creation**
- **More programs running concurrently**
- **Less I/O needed to load or swap processes**

## Slide 13

# Virtual Address Space

**Texto izquierda:**
- **Definition:** logical view of how process is stored in memory
  - Usually start at address 0, contiguous addresses until end of space
  - Meanwhile, physical memory organized in page frames
  - MMU must map logical to physical
- **Virtual memory can be implemented via:**
  - Demand paging
  - Demand segmentation

**Diagrama derecha:** columna "virtual memory" con page 0, page 1, page 2 … page v (páginas consecutivas). Flechas desde la memoria virtual a una columna "memory map" (mapa de memoria) y de ahí a "physical memory" (frames), que a su vez conecta con un cilindro (disco/backing store). Las flechas indican que páginas virtuales se mapean a frames físicos y algunas residen en disco.

## Slide 14

# Virtual Address Space

**Texto (recuadro amarillo arriba):**
- **Usually design logical address space for stack to start at Max logical address and grow "down" while heap grows "up"**
  - **Maximizes address space use**
  - **Unused address space between the two is hole**
    - No physical memory needed until heap or stack grows to a given new page
- **Enables sparse address spaces with holes left for growth,** dynamically linked libraries, etc

**Texto (abajo):**
- System libraries shared via mapping into virtual address space
- Shared memory by mapping pages read-write into virtual address space
- Pages can be shared during `fork()`, speeding process creation

**Diagrama derecha (layout del address space de un proceso, de Max arriba a 0 abajo):**
- **stack** (arriba, en Max) con flecha hacia abajo (crece "down").
- zona vacía/hole en el medio (celeste).
- flecha hacia arriba desde **heap** (crece "up").
- **heap**, luego **data**, luego **code** en la base (dirección 0).

Nota inferior: "This will be explored in more detail later in the course." (con emoji de ojos).

## Slide 15

# Recall: Demand Paging

**Texto:**
- **Could bring entire process into memory at load time**
- **Or bring a page into memory only when it is needed**
  - Less I/O needed, no unnecessary I/O
  - Less memory needed
  - Faster response
  - More users
- **Page is needed ⇒ reference to it** (recuadro rosado)
  - **invalid reference ⇒ abort**
  - **not-in-memory ⇒ bring to memory**
- **Similar to paging system with swapping (see Figure)**
- **Lazy swapper:** never swaps a page into memory unless page will be needed
  - Swapper that deals with pages is a **pager**

**Diagrama derecha (paginación con swapping):** columna "main memory" con bloques de program A y program B. Flecha "swap out" desde main memory hacia un cilindro/backing store dividido en 24 celdas numeradas 0-23 (páginas 4,5,6,7 y 16,17,18,19 sombreadas). Flecha "swap in" desde el disco de vuelta a memoria. Ilustra intercambio de páginas entre memoria principal y disco.

## Slide 16

# Basic Concepts

Slide de texto (sin figura).

- **With swapping, pager guesses which pages will be used before swapping out again**
- **Instead, pager brings in only those pages into memory**
- **How to determine that set of pages?**
  - Need new MMU functionality to implement demand paging
- **If pages needed are already memory resident**
  - No difference from non demand-paging
- **If page needed and not memory resident**
  - Need to detect and load the page into memory from storage
    - Without changing program behavior
    - Without programmer needing to change code

## Slide 17

# Recall: Valid-Invalid Bit

**Texto:**
- **With each page table entry a valid–invalid bit is associated:** (**v** ⇒ in-memory – **memory resident**, **i** ⇒ not-in-memory)
- **Initially** valid–invalid bit is set to **i** on all entries
- **During MMU address translation**, if valid–invalid bit in page table entry is **i** ⇒ page fault

**Diagrama derecha (page table):** tabla con dos columnas "Frame #" y "valid-invalid bit". Las filas muestran valores en la columna de bit: v, v, v, i, … (fila con "…"), i, i. Ilustra qué entradas están en memoria (v) y cuáles no (i).

## Slide 18

# Page Table: What if Some Pages Are Not in Main Memory?

Slide casi enteramente gráfica. Pie: "CS2S01-OPERATING SYSTEMS".

**Diagrama (ejemplo con páginas A–H):**
- **logical memory:** celdas 0..7 con A,B,C,D,E,F,G,H. Las filas B, D, E, G, H están resaltadas en rojo (no residentes en memoria).
- **page table:** 8 entradas con (frame, valid-invalid bit): 0→4 **v**, 1→**i**, 2→6 **v**, 3→**i**, 4→**i**, 5→9 **v**, 6→**i**, 7→**i**. Encabezados "frame" y "valid–invalid bit".
- **physical memory:** columna 0..15. A en frame 4, C en frame 6, F en frame 9 (las páginas válidas, en gris).
- **cilindro (backing store):** contiene las páginas A, B (rojo), C, D (rojo), E (rojo), F, G (rojo), H (rojo) — las inválidas están solo en disco.

Muestra que las páginas con bit **v** están en memoria física y las de bit **i** residen únicamente en el backing store.

## Slide 19

# Page Fault

**Texto (recuadro verde, pasos numerados):**
- **First reference to a page will trap to operating system: page fault**
1. **Operating system looks at another table to decide:**
   - Invalid reference ⇒ abort
   - Just not in memory
2. **Find free frame**
3. **Swap page into frame via scheduled disk operation**
4. **Reset tables to indicate page now in memory. Set validation bit = v**
5. **Restart the instruction that caused the page fault**

**Diagrama derecha (flujo del page fault numerado 1-6):**
1. instrucción "load M" hace **reference** a la page table.
2. la entrada tiene bit **i** → **trap** al operating system.
3. **page is on backing store** (el SO consulta el cilindro/disco).
4. **bring in missing page** desde el disco a un **free frame** en physical memory.
5. **reset page table** (actualizar la entrada de la tabla).
6. **restart instruction** (reejecutar "load M").
El diagrama conecta CPU/load M → page table → operating system (trap) → backing store → free frame en physical memory → de vuelta a la page table.

## Slide 20

**Reference Books** (slide de cierre, imagen decorativa de profesor escribiendo en pizarra)

- Patterson, D. A., & Hennessy, J. L. (2020). Computer Organization and Design RISC-V Edition: The Hardware Software Interface. Morgan Kaufmann
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). Operating system concepts (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).
