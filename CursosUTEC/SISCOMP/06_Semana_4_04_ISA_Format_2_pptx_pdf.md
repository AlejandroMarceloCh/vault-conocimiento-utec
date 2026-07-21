---
curso: SISCOMP
titulo: 06 - Semana 4/04. ISA Format 2.pptx
slides: 34
fuente: 06 - Semana 4/04. ISA Format 2.pptx.pdf
---

## Slide 1

Portada (decorativa: fondo de túnel tecnológico con figura humanoide).

**COMPUTING SYSTEMS**

Subtítulo: **ISA FORMAT - MEMORY INSTRUCTIONS (LD/ST)**

## Slide 2

Portada de sección con foto decorativa (científica en laboratorio, tinte azul).

**Motivation**
- We need to move beyond registers and reach memory to make programs meaningful.
- Understanding processor instructions allows us to control data flow and program behavior.

**Goals**
- Manipulate memory directly with bare-metal load and store instructions.
- Understand how RISC-V addresses memory through base registers and offsets.

## Slide 3

**Summary** (índice con íconos, sobre fondo decorativo de globo y persona con VR).

1. Memory
2. Endianness
3. RISC-V instructions
4. Arrays
5. Conclusions
6. (sin texto)

## Slide 4

Slide divisoria de sección. Número grande **1.** con ícono de portapapeles y el título **Memory**. Imagen decorativa de mano robótica tocando un globo digital.

## Slide 5

**The memory stores**
- Data
- Programs
- The memory contains **bits**
  - Bits are grouped into **bytes** (8 bits) and **words** (e.g., 8, 16, 32 bits)
- How the bits are accessed determines the **addressability**
  - E.g., word-addressable
  - E.g., 8-bit addressable (or byte-addressable)
- The total number of addresses is the **address space**
  - In ARM, the address space is $2^{32}$ — 32-bit addresses
  - In x86-64, the address space is (up to) $2^{48}$ — 48-bit addresses
  - In RISC-V, the address space is commonly $2^{32}$ — 32-bit addresses

**Visual (diagrama de arquitectura tipo Von Neumann / IAS):** A la derecha, esquema del "Central processing unit (CPU)" (recuadro punteado) que contiene:
- **Arithmetic-logic unit (CA)**: registros AC y MQ arriba, conectados con flechas bidireccionales a los "Arithmetic-logic circuits", que se conectan hacia abajo al **MBR** (memory buffer register).
- **Program control unit (CC)** (abajo): registros PC e IBR arriba; MAR e IR debajo; IR alimenta los "Control circuits" que emiten "Control signals".
- A la izquierda, columna vertical **Main memory (M)** con celdas M(0), M(1), M(2), M(3), M(4)…M(4092), M(4093), M(4095). Flechas de "Instructions and data" entran/salen del MBR; "Addresses" entran al MAR.
- A la derecha, bloque **Input-output equipment (I, O)** conectado por "Instructions and data".
- Leyenda: AC=Accumulator register, MQ=multiply-quotient register, MBR=memory buffer register, IBR=instruction buffer register, PC=program counter, MAR=memory address register, IR=instruction register.

## Slide 6

**Accessing Memory**
- There are two ways of accessing memory
  - Reading or loading
  - Writing or storing
- Two registers are necessary to access memory
  - Memory Address Register (MAR)
  - Memory Data Register (MDR)
- To read
  - Step 1: Load the MAR with the address
  - Step 2: Data is placed in MDR
- To write
  - Step 1: Load the MAR with the address and the MDR with the data
  - Step 2: Activate Write Enable signal

**Visual:** mismo diagrama CPU/Main memory/I-O que la slide 5 (Von Neumann con AC, MQ, ALU, MBR, PC, IBR, MAR, IR, control circuits y columna de Main memory M(0)…M(4095)).

## Slide 7

**Word-Addressable Memory**
- Each **data word** has a **unique address**
  - In RISC-V, a unique address for each **32-bit data word**

**Visual (tabla de memoria RISC-V, palabras de 32 bits):**

| Word Address | Data | |
|---|---|---|
| . . . | . . . | . . . |
| 00000003 | D1617A1C | Word 3 |
| 00000002 | 13C81755 | Word 2 |
| 00000001 | F2F1F0F7 | Word 1 |
| 00000000 | 89ABCDEF | Word 0 |

Cada dirección de palabra incrementa de 1 en 1 (word-addressable); cada celda almacena 4 bytes.

## Slide 8

**Byte-Addressable Memory**
- Each **byte** has a **unique address**
  - Actually, RISC-V is byte-addressable

**Visual (tabla ARM memory, cada palabra dividida en 4 bytes):**

| Byte Address (of the Word) | Data (D3 D2 D1 D0) | |
|---|---|---|
| . . . | . . . | . . . |
| 0000000C | D1 · 61 · 7A · 1C | Word 3 |
| 00000008 | 13 · C8 · 17 · 55 | Word 2 |
| 00000004 | F2 · F1 · F0 · F7 | Word 1 |
| 00000000 | 89 · AB · CD · EF | Word 0 |

Nota resaltada (recuadro naranja sobre Word 0): "How are these four bytes addressed?". Las direcciones de palabra incrementan de 4 en 4 (0, 4, 8, C).

## Slide 9

Slide divisoria de sección. Número grande **2.** con ícono de portapapeles y título **Endianness**. Imagen decorativa de mano robótica y globo.

## Slide 10

**Byte-Addressable Memory** (repetición de la slide 8, misma tabla).
- Each byte has a unique address
  - Actually, RISC-V is byte-addressable

**Visual:** misma tabla ARM memory que slide 8 (0000000C…00000000, bytes D3 D2 D1 D0, con recuadro naranja "How are these four bytes addressed?").

## Slide 11

**Big Endian vs Little Endian**
- Jonathan Swift's **Gulliver's Travels**
  - Little Endians broke their eggs on the little end of the egg
  - Big Endians broke their eggs on the big end of the egg
- **How to number bytes within a word?**
  - Little-endian: byte numbers start at the little (least significant) end
  - Big-endian: byte numbers start at the big (most significant) end

**Visual:** dos huevos naranjas caricaturizados; el izquierdo con leyenda "BIG ENDIAN - The way people always broke their eggs in the Lilliput land", el derecho "LITTLE ENDIAN - The way the king then ordered the people to break their eggs". A la derecha, portada del libro "Gulliver's Travels by Jonathan Swift" (decorativa).

## Slide 12

**Big Endian vs Little Endian**

Banda naranja destacada que atraviesa la slide: "It doesn't really matter which addressing type used – except when two systems share data".

**Visual (dos tablas comparativas, con columna central de Word Address):**

Big Endian (Byte Address) — columnas ordenadas MSB→LSB:

| C | D | E | F |
|---|---|---|---|
| 8 | 9 | A | B |
| 4 | 5 | 6 | 7 |
| 0 | 1 | 2 | 3 |

Word Address (centro): C, 8, 4, 0

Little Endian (Byte Address) — columnas ordenadas MSB→LSB:

| F | E | D | C |
|---|---|---|---|
| B | A | 9 | 8 |
| 7 | 6 | 5 | 4 |
| 3 | 2 | 1 | 0 |

Bajo ambas tablas: MSB (Most Significant Byte) a la izquierda, LSB (Least Significant Byte) a la derecha. En big-endian el byte con número más bajo queda en el MSB; en little-endian el byte con número más bajo queda en el LSB.

## Slide 13

Slide divisoria de sección. Número grande **3.** con ícono de portapapeles y título **RISC-V instructions**. Imagen decorativa de mano robótica y globo.

## Slide 14

**Operands: Memory** (texto en colores)
- Too much data to fit in only 32 registers
- Store more data in memory
- Memory is large, but slow
- Commonly used variables still kept in registers

## Slide 15

**Recall: Byte-Addressable Memory**
- Each data **byte** has unique address
- 32-bit word = 4 bytes, so word address increments by 4

**Visual (tabla de memoria, bytes en hex):**

| Byte address (D3 D2 D1 D0) | Word address |
|---|---|
| 13 · 12 · 11 · 10 | 00000010 |
| F · E · D · C | 0000000C |
| B · A · 9 · 8 | 00000008 |
| 7 · 6 · 5 · 4 | 00000004 |
| 3 · 2 · 1 · 0 | 00000000 |

MSB a la izquierda, LSB a la derecha. Los valores de byte address avanzan de a 1 dentro de cada palabra; el word address salta de 4 en 4.

## Slide 16

**Reading Memory**

Recuadro verde (esquina): "**Important:** Memory Instructions".

- Memory reads are called **load**

```
lw rd, imm12(rs1)     # load word to rd
```

**Address calculation:**
- add base address (rs1) to the offset (imm12)
- address = (rs1 + imm12)

**Result:**
- rd holds the data at memory address [rs1 + imm12]
- Any register may be used as base address

$$rd \leftarrow Memory[rs1 + imm12]$$

## Slide 17

**Reading Memory**

**Load Variations (16 or 8 bytes)** [sic: se refiere a 16 u 8 bits]

Sign-Extended (if MSB=1, extend with 1s):
- `lh rd, imm(rs1)` — Half-Word (16-bit)
- `lb rd, imm(rs1)` — Byte (8-bit)

Unsigned (Zero-extended):
- `lhu rd, imm(rs1)` — Half-Word Unsigned (16-bit)
- `lbu rd, imm(rs1)` — Byte Unsigned (8-bit)

## Slide 18

**Reading Memory**
- Load Instructions use **I-Type** Format (op=0x03)
- lw, lh, lb, …, depend on funct3
- Offset can only be Immediate

**Visual (formato I-Type de 32 bits):**

| bits 31:20 | 19:15 | 14:12 | 11:7 | 6:0 |
|---|---|---|---|---|
| imm[11:0] | rs1 | funct3 | rd | op |
| 12 bits | 5 bits | 3 bits | 5 bits | 7 bits |

**Assembly / Field Values:**

| Assembly | imm[11:0] | rs1 | funct3 | rd | op |
|---|---|---|---|---|---|
| `lw t2, -6(s3)` (`lw x7, -6(x19)`) | -6 | 19 | 2 | 7 | 3 |
| `lb s4, 0x1F(s4)` (`lb x20, 0x1F(x20)`) | 0x1F | 20 | 0 | 20 | 3 |

## Slide 19

**Reading Memory**
- **Example:** Read a word of data at memory address 8 into x3
  - Address = (x0 + 8) = (0 + 8) = 8
  - x3 = 0x01EE2842 after load

**RISC-V - Assembly Code:**
```
lw x3, 8(x0)
```

**Visual (tabla de memoria, bytes por palabra, Width = 4 bytes):**

| Word address | Data | Word number |
|---|---|---|
| 00000010 | CD 19 A6 5B | Word 4 |
| 0000000C | 40 F3 07 88 | Word 3 |
| **00000008** | **01 EE 28 42** | **Word 2** ← x3 (resaltado en rojo) |
| 00000004 | F2 F1 AC 07 | Word 1 |
| 00000000 | AB CD EF 78 | Word 0 |

La fila de la dirección 00000008 (Word 2) está encerrada en un recuadro rojo y una flecha `x3 ←` la señala.

## Slide 20

**Writing Memory**

Recuadro verde (esquina): "**Important:** Memory Instructions".

- Memory writes are called **stores**

```
sw rd, imm12(rs1)     # store word to rd
```

**Address calculation:**
- add base address (rs1) to the offset (imm12)
- address = (rs1 + imm12)

**Result:**
- rd holds the data at memory address [rs1 + imm12]
- Any register may be used as base address

$$rd \rightarrow Memory[rs1 + imm12]$$

## Slide 21

**Writing Memory**
- Write Instructions use **S-Type** Format (op=0x23)
- sw, sh, sb, …, depend on funct3
- Offset can only be Immediate

**Visual (formato S-Type de 32 bits):**

| bits 31:25 | 24:20 | 19:15 | 14:12 | 11:7 | 6:0 |
|---|---|---|---|---|---|
| imm[11:5] | rs2 | rs1 | funct3 | imm[4:0] | op |
| 7 bits | 5 bits | 5 bits | 3 bits | 5 bits | 7 bits |

**Assembly / Field Values:**

| Assembly | imm[11:5] | rs2 | rs1 | funct3 | imm[4:0] | op |
|---|---|---|---|---|---|---|
| `sw t2, -6(s3)` (`sw x7, -6(x19)`) | 1111 111 | 7 | 19 | 2 | 11010 | 35 |
| `sh s4, 23(t0)` (`sh x20, 23(x5)`) | 0000 000 | 20 | 5 | 1 | 10111 | 35 |
| `sb t5, 0x2D(zero)` (`sb x30, 0x2D(x0)`) | 0000 001 | 30 | 0 | 0 | 01101 | 35 |

(El inmediato se parte en imm[11:5] e imm[4:0]; op=0x23=35.)

## Slide 22

**Recap: Accessing Memory**
- Address of a memory **word** must be multiplied by 4
- **Examples:**
  - Address of memory word 2 = 2 × 4 = 8
  - Address of memory word 10 = 10 × 4 = 40

## Slide 23

**Recap: Big-Endian and Little-Endian Memory**
- **How to number bytes within a word?**
  - Little-endian: byte numbers start at the little (least significant) end
  - Big-endian: byte numbers start at the big (most significant) end

**Visual (dos tablas + columna central de Word Address):**

Big-Endian (Byte Address):

| C | D | E | F |
|---|---|---|---|
| 8 | 9 | A | B |
| 4 | 5 | 6 | 7 |
| 0 | 1 | 2 | 3 |

Word Address (centro): C, 8, 4, 0

Little-Endian (Byte Address):

| F | E | D | C |
|---|---|---|---|
| B | A | 9 | 8 |
| 7 | 6 | 5 | 4 |
| 3 | 2 | 1 | 0 |

Ambas con MSB a la izquierda, LSB a la derecha.

## Slide 24

**Big-Endian and Little-Endian Example**

**Suppose x2 and x5 hold the values 8 and 0x23456789**
- After following code runs on big-endian system, what value is in R7?
- In a little-endian system?

```
sw x5, 0(x2)
lb x7, 1(x2)
```

**Visual:** dos representaciones del word almacenado (data value 23 45 67 89):
- Big-Endian: Byte Address 8 9 A B → 23 45 67 89 (MSB izq, LSB der). El byte en dirección 9 (offset 1) = 45.
- Little-Endian: Byte Address B A 9 8 → 23 45 67 89 (MSB izq, LSB der). El byte en dirección 9 (offset 1) = 67.

Respuestas (a la derecha):
- **Big-endian:** 0x00000045
- **Little-endian:** 0x00000067

## Slide 25

**Byte Addressing - Example**

**Visual (Memory + Registers):**

Memory (Byte Address D3 D2 D1 D0):

| D3 | D2 | D1 | D0 |
|---|---|---|---|
| F7 | 8C | 42 | 03 |

Registers (resultado de cada instrucción):

| Reg | Contenido | Instrucción |
|---|---|---|
| s1 | 00 00 00 **8C** | `lbu s1, 2(s4)` |
| s2 | FF FF FF **F7** | `lb s2, 3(s4)` |
| s3 | xx xx xx **9B** | `sb s3, 1(s4)` |

(lbu byte 2 = 8C, zero-extended; lb byte 3 = F7 con MSB=1 → sign-extended a FFFFFFF7; s3 contiene 9B en su byte bajo, listo para el sb.)

## Slide 26

**Byte Addressing - Example** (misma Memory y Registers que slide 25).

Pregunta añadida a la derecha: "How will Mem[s4] look after executing **sb s3, 1(s4)**?"

## Slide 27

**Byte Addressing - Example** (misma Memory/Registers; resuelve la pregunta de la slide 26).

**Visual (respuesta, Memory tras el store):**

Byte Address D3 D2 D1 D0:

| D3 | D2 | D1 | D0 |
|---|---|---|---|
| F7 | 8C | **9B** | 03 |

Anotación manuscrita en rojo: flecha señalando D1 con la etiqueta "s4+1". Es decir, `sb s3, 1(s4)` escribe el byte bajo de s3 (9B) en la dirección s4+1 (posición D1), reemplazando el 42 original.

## Slide 28

Slide divisoria de sección. Número grande **4.** con ícono de portapapeles y título **Arrays**. Imagen decorativa de mano robótica y globo.

## Slide 29

**Arrays in Memory**

**Array: Contiguous Memory**

$$arr[i] = \&arr + (i \times 4) \quad // \text{ 4 Byte}$$

**Visual (tabla Address 32-bit / Memory Content):**

| Address (32-bit) | Memory Content | |
|---|---|---|
| 0x028 | ??? | |
| 0x024 | 9 | arr[8] |
| 0x020 | 8 | arr[7] |
| 0x01C | 7 | arr[6] |
| 0x018 | 6 | arr[5] |
| 0x014 | 5 | arr[4] |
| 0x010 | 4 | arr[3] |
| 0x00C | 3 | arr[2] |
| 0x008 | 2 | arr[1] |
| **0x004** | 1 | arr[0] ← **Base Address &arr =** |
| 0x000 | ??? | |

Código de referencia:
```
arr[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(&arr) // 0x004
```

## Slide 30

**Arrays in Memory**

**Multidimensional: Stored the same as 1D Array!!!**

**Visual (tabla Address 32-bit / Memory Content para arreglo 2D):**

| Address (32-bit) | Memory Content | |
|---|---|---|
| 0x028 | ??? | |
| 0x024 | 9 | arr[2][2] |
| 0x020 | 8 | arr[2][1] |
| **0x01C** | 7 | arr[2][0] ← **&arr[2] =** |
| 0x018 | 6 | arr[1][1] |
| 0x014 | 5 | arr[1][1] [sic; debería ser arr[1][2]] |
| **0x010** | 4 | arr[1][0] ← **&arr[1] =** |
| 0x00C | 3 | arr[0][2] |
| 0x008 | 2 | arr[0][1] |
| **0x004** | 1 | arr[0][0] ← **&arr = &arr[0] =** |
| 0x000 | ??? | |

Código de referencia:
```
arr[3][3] = {{1, 2, 3},{4, 5, 6}, {7, 8, 9}}
print(&arr)    // 0x004
print(&arr[0]) // 0x004
print(&arr[1]) // 0x010
print(&arr[2]) // 0x01C
```

Pregunta (abajo izq, en rojo): "Are there any relation between 1D and 2D array addressings? A[i] =? B[x][y]"

## Slide 31

**Iterating Over Array (For Loop)**

**Visual (dos columnas de código + tabla de memoria):**

High-Level Code:
```c
int i;
int scores[200];

for (i = 0; i < 200; i = i + 1)

  scores[i] = scores[i] + 10;
```

RISC-V Assembly Code:
```asm
# s0 = scores base address, s1 = i

  addi s1, zero, 0    # i = 0
  addi t2, zero, 200  # t2 = 200

for:
  bge  s1, t2, done   # if i >= 200 then done
  slli t0, s1, 2      # t0 = i * 4
  add  t0, t0, s0     # address of scores[i]
  lw   t1, 0(t0)      # t1 = scores[i]
  addi t1, t1, 10     # t1 = scores[i] + 10
  sw   t1, 0(t0)      # scores[i] = t1
  addi s1, s1, 1      # i = i + 1
  j    for            # repeat
done:
```

Tabla Main Memory (Figure 6.4, scores[200] empezando en base address 0x174300A0):

| Address | Data |
|---|---|
| 174303BC | scores[199] |
| 174303B8 | scores[198] |
| . . . | . . . |
| 174300A4 | scores[1] |
| 174300A0 | scores[0] |

## Slide 32

**Conclusions**

**Memory** lets us build more complex programs, without being limited only by registers.
- It allows storing much more data, giving programs state and persistence beyond registers.
- It is not only for data, memory can also be used for controlling or accessing more things (network, external inputs, video buffers, etc).

Cita destacada (banda azul): *"Computers are really, basically, computing elements and a lot of memory. They are pretty easy to understand…" - Paul Allen*

## Slide 33

**Reference Books**
- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann.
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).

(Imagen decorativa: profesor escribiendo en pizarra, tinte azul.)

## Slide 34

Slide de cierre. **Questions?** sobre imagen decorativa (dos estudiantes en laboratorio con lentes de seguridad, tinte azul).
