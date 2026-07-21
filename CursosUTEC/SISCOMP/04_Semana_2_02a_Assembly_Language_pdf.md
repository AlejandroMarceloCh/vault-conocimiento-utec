---
curso: SISCOMP
titulo: 04 - Semana 2/02a.Assembly Language
slides: 24
fuente: 04 - Semana 2/02a.Assembly Language.pdf
---

## Slide 1

Portada. Título "COMPUTER SYSTEMS", subtítulo "ASSEMBLY LANGUAGE". Fondo decorativo (túnel de datos futurista con silueta de robot humanoide). Logos UTEC / TransformaTec y lema "Reinventa el mundo" (decorativo).

## Slide 2

Título "Goals".

Texto: "Analyze the assembly language and the instruction set architecture of RISC V".

Imagen lateral decorativa (científica en laboratorio con tubos de ensayo).

## Slide 3

Título "Summary". Índice de contenidos en dos columnas, cada ítem con un ícono:

1. Numerical Systems
2. Memory organization
3. Byte ordering
4. Boolean algebra
5. Sign/Zero/Shift Operations
6. Conclusions

Imagen lateral decorativa (persona con visor VR y globo terráqueo de datos).

## Slide 4

Portada de sección. Número grande "1." y título "Instructions" (con ícono de portapapeles). Imagen lateral decorativa (mano robótica tocando un mapa/globo de datos).

## Slide 5

Título "RISC V Architecture".

- An instruction the most basic unit of computer processing:
  - Instructions are words in the language of a computer
  - Instruction Set Architecture (ISA) is the vocabulary
- RISC V is a Reduced Instruction Set Computer (RISC), with a small number of simple instructions. Other architectures, such as Intel's x86, are Complex Instruction Set Computers (CISC)

Solo texto (sin figuras aparte del chrome decorativo).

## Slide 6

Título "Sequential Execution".

- Instructions and data are stored in memory: Typically the instruction length is the word length
- Instructions: Commands in a computer's language
  - Assembly language: human-readable format of instructions
  - Machine language: computer-readable format (1's and 0's)
- The processor fetches instructions from memory sequentially (first one instruction, then the next one)
- The address of the current instruction is stored in the program counter (PC)
  - If word-addressable memory, the processor increments the PC by 1.
  - If byte-addressable memory, the processor increments the PC by the word length (4 in ARM)

E.g: OS sets the PC to 0x00400000 (start of a program), increment from this address value.

Solo texto.

## Slide 7

Título "Program Stored in Memory".

- 4 instructions stored in consecutive words in memory
- No need to understand the program now. We will get back to it

La slide muestra tres columnas alineadas: código ensamblador, su traducción a código máquina, y un diagrama de la memoria principal.

**Assembly code:**
```
add  s2, s3, s4
sub  t0, t1, t2
addi s2, t1, -14
lw   t2, -6(s3)
```

**Machine code:**
```
0x01498933
0x407302B3
0xFF230913
0xFFA9A383
```

**Diagrama "Main memory"** (tabla Address / Instructions, direcciones descendentes de arriba hacia abajo, con "..." arriba y abajo). Cada instrucción máquina se muestra byte a byte:

| Address   | Instructions      |
|-----------|-------------------|
| 0000083C  | F F A 9 A 3 8 3   |
| 00000838  | F F 2 3 0 9 1 3   |
| 00000834  | 4 0 7 3 0 2 B 3   |
| 00000830  | 0 1 4 9 8 9 3 3   ← PC |

Una flecha azul con la etiqueta **PC** apunta a la fila 0x00000830 (la primera instrucción `add`). Las direcciones aumentan de 4 en 4 (memoria byte-addressable, palabra de 4 bytes).

## Slide 8

Título "Memory Map".

**Diagrama de mapa de memoria** (tabla vertical Address / Segment), direcciones altas arriba, bajas abajo. De arriba hacia abajo:

| Address     | Segment                        |
|-------------|--------------------------------|
| 0xFFFFFFFC  | Operating System & I/O (sombreado gris) |
| 0xC0000000  | (límite)                       |
| 0xBFFFFFF0  | Stack  ← **sp**                |
|             | ↓ (stack crece hacia abajo)    |
|             | Dynamic Data                   |
|             | ↑ Heap (crece hacia arriba)    |
| 0x10001000  | (límite)                       |
| 0x10000FFC  |                                |
|             | Global Data  ← **gp**          |
| 0x10000000  | (límite)                       |
|             | Text                           |
| 0x00010000  | ← **PC**                       |
|             | Exception Handlers (sombreado gris) |
| 0x00000000  | (base)                         |

Flechas azules apuntan a: **sp** (stack pointer) en el tope del Stack, **gp** (global pointer) en Global Data, y **PC** al inicio del segmento Text (0x00010000).

## Slide 9

Título "ADD Instruction".

Comparación en dos recuadros azules:

**C Code:**
```c
a = b + c;
```

**RISC V Assembly Code:**
```
add a, b, c
```

- **ADD:** mnemonic – indicates operation to perform
- **b, c:** source operands
- **a:** destination operand

## Slide 10

Título "SUB Instruction".

**C Code:**
```c
a = b + c;
```

**RISC V Assembly Code:**
```
SUB a, b, c
```

- **SUB:** mnemonic – indicates operation to perform
- **b, c:** source operands
- **a:** destination operand

(Nota: la slide muestra el C Code como `a = b + c;`, tal cual aparece en el original, aunque conceptualmente para SUB correspondería `a = b - c;`.)

## Slide 11

Título "Multiple Instructions".

Texto: "More complex code handled by multiple RISC V instructions".

**C Code:**
```c
a = b + c - d;
```

**RISC V assembly code:**
```
ADD t, b, c   # t = b + c
SUB a, t, d   # a = t - d
```

## Slide 12

Título "Instructions with Registers". Subtítulo subrayado "ADD Instruction".

**C Code:**
```c
a = b + c
```

**RISC V Assembly Code:**
```
# R0 = a, R1 = b, R2 = c

ADD R0, R1, R2
```

## Slide 13

Título "Operands: Constants and Immediates".

- Many instructions can use constants or *immediate* operands
- For example: ADD and SUB
- Value is *immediately* available from instruction

**C Code:**
```c
a = a + 4;
b = a - 12;
```

**RISC V Assembly Code:**
```
#R0 = a, R1 = b
addi R0, R0, 4
addi R1, R0, -12
```

## Slide 14

Título "Generating Constants". Subtítulo azul: "Constant must have < 8 bits of precision".

**C Code:**
```c
a = 23;
b = -78;
```

**RISC V Assembly Code:**
```
# R0 = a, R1 = b
addi R0, zero, 23
addi R1, zero, -78
```

## Slide 15

Título "Generating Larger Constants". Subtítulo azul: "load upper immediate (lui) < 20-bit (MSB)".

**C Code:**
```c
a = 0xABCDE123
```

**RISC V Assembly Code:**
```
lui s2, 0xABCDE
addi s2, s2, 0x123
```

## Slide 16

Título "Memory".

Texto: "RISC V uses 32-bit memory addresses and 32-bit data words in byte-addressable memory".

**Diagrama de memoria** con cuatro columnas: Byte Address, Word Address, Data, Word Number. Con "..." arriba (direcciones más altas). De arriba hacia abajo:

Panel (a) — **Byte Address** (4 bytes por fila, de MSB a la izquierda a LSB a la derecha):

| Byte Address (MSB→LSB) | Word Address | Data (MSB→LSB) | Word # |
|------------------------|--------------|-----------------|--------|
| 13 12 11 10            | 00000010     | CD 19 A6 5B     | Word 4 |
| F  E  D  C             | 0000000C     | 40 F3 07 88     | Word 3 |
| B  A  9  8             | 00000008     | 01 EE 28 42     | Word 2 |
| 7  6  5  4             | 00000004     | F2 F1 AC 07     | Word 1 |
| 3  2  1  0             | 00000000     | AB CD EF 78     | Word 0 |

Etiquetas: bajo la columna de byte address, "MSB" a la izquierda y "LSB" a la derecha; el panel (a) es la numeración de bytes/palabras. Panel (b) es la columna de datos, con una flecha doble abajo que indica "width = 4 bytes".

## Slide 17

Título "Endianness".

Texto (izquierda): "RISC V uses 32-bit memory addresses and 32-bit data words in byte-addressable memory".

**Diagrama comparativo Big-Endian vs Little-Endian.** Ambas tablas muestran el mismo dato en cuatro palabras (Word Address 0, 4, 8, C) pero con distinto orden de bytes dentro de cada palabra (MSB izquierda, LSB derecha):

**Big-Endian** (Byte Address):
| C | D | E | F |
| 8 | 9 | A | B |
| 4 | 5 | 6 | 7 |
| 0 | 1 | 2 | 3 |

**Word Address** (columna central): C, 8, 4, 0.

**Little-Endian** (Byte Address, orden invertido dentro de la palabra):
| F | E | D | C |
| B | A | 9 | 8 |
| 7 | 6 | 5 | 4 |
| 3 | 2 | 1 | 0 |

En big-endian el byte más significativo tiene la dirección más baja dentro de la palabra; en little-endian el byte menos significativo tiene la dirección más baja. Ambas etiquetadas MSB (izq) / LSB (der).

## Slide 18

Título "Reading Memory". Subtítulo azul: "load word (lw)".

**C Code:**
```c
a = mem[2]
```

**RISC V Assembly Code:**
```
#s5 = a
lw s5, 8(zero)
```

Texto explicativo: "The code loads memory word 2, located ad address 8 into a (s5)". **zero: base register**.

## Slide 19

Título "Writing Memory". Subtítulo azul: "store word (sw)".

**C Code:**
```c
mem[5] = 42
```

**RISC V Assembly Code:**
```
addi t3, zero, 42   #t3 = 42
sw t3, 20(zero)
```

Texto explicativo: "Code writes the value 42 from register t3 into memory word 5, located at address 20".

## Slide 20

Título "Ada Lovelace".

- British mathematician, 1815-1852
- Wrote the first computer program
- Her program calculated the Bernoulli numbers on Charles Babbage's Analytical Engine
- She was a child of the poet Lord Byron

Subtítulo azul: "At her time, no high-level languages:"
- e.g., C, Java, Python
- Written at higher level of abstraction

Imagen lateral: retrato fotográfico histórico en blanco y negro de Ada Lovelace.

## Slide 21

Título "Types of Instructions and Programming Blocks".

Texto: "Three main types of instructions:"
1. Data-processing Instructions
2. Branches
3. Memory

"High-level Constructs:"
- if/else statements
- for loops
- while loops
- arrays
- function calls

Recuadro destacado (caja gris a la derecha): "**We study how to implement high-level programs using low-level definitions**".

## Slide 22

Título "How are these instructions executed?".

- By using instructions we can speak the language of the computer
- Thus, we now know how to tell the computer to
  - **Execute** computations in the ALU by using, for instance, an addition
  - **Access** operands from memory by using the load word instruction
- But, **how are these instructions executed on the computer**?
  - The process of executing an instruction is called is the instruction cycle

(Las palabras "Execute", "Access" y la pregunta final aparecen resaltadas en celeste.)

## Slide 23

Título "Reference Books". Lista de referencias (cada una con una flecha azul):

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). *Operating system concepts* (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).

Imagen lateral decorativa (profesor escribiendo en pizarra ante alumnos).

## Slide 24

Cierre. Título "Questions?" sobre imagen de fondo decorativa (dos estudiantes con bata y gafas de laboratorio trabajando con equipo). Logos UTEC / TransformaTec (decorativo).
