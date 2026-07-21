---
curso: SISCOMP
titulo: 07 - Semana 5/05. Pseudo Instructions.pptx
slides: 19
fuente: 07 - Semana 5/05. Pseudo Instructions.pptx.pdf
---

## Slide 1

Portada. Título "COMPUTING SYSTEMS" con subtítulo "RISC-V Pseudoinstructions". Imagen de fondo decorativa (silueta de robot humanoide en un túnel tecnológico). Chrome UTEC / TransformaTec / "Reinventa el mundo" decorativo.

## Slide 2

**Goals**

Learn about **RISC-V Pseudo-Instructions** (not part of the ISA Format) and how they are assembled into actual Machine Code instructions.

(Imagen lateral decorativa de una investigadora de laboratorio.)

## Slide 3

**Summary**

1. Recall: ISA
2. Pseudoinstructions

(Cada ítem con un ícono: portapapeles para el 1, bombilla para el 2. Imagen de fondo decorativa: persona con visor VR sobre globo terráqueo.)

## Slide 4

Slide divisoria de sección.

**1. Recall: RISC-V Instructions**

(Ícono de portapapeles + imagen decorativa de mano robótica tocando un globo digital.)

## Slide 5

**Recall: RISC-V Instructions**

Tabla del formato de instrucciones RISC-V. Reparte los 32 bits de la instrucción en campos por rango de bits, y muestra los 7 formatos:

| 31:25 | 24:20 | 19:15 | 14:12 | 11:7 | 6:0 | Tipo |
|-------|-------|-------|-------|------|-----|------|
| funct7 | rs2 | rs1 | funct3 | rd | op | **R-Type** |
| imm[11:0] (ocupa 31:20) | | rs1 | funct3 | rd | op | **I-Type** |
| imm[11:5] | rs2 | rs1 | funct3 | imm[4:0] | op | **S-Type** |
| imm[12,10:5] | rs2 | rs1 | funct3 | imm[4:1,11] | op | **B-Type** |
| imm[31:12] (ocupa 31:12) | | | | rd | op | **U-Type** |
| imm[20,10:1,11,19:12] (ocupa 31:12) | | | | rd | op | **J-Type** |
| fs3 | funct2 | fs2 | fs1 | funct3 | fd | op | **R4-Type** |

Anchos de campo (fila inferior): 5 bits · 2 bits · 5 bits · 5 bits · 3 bits · 5 bits · 7 bits.

## Slide 6

**Recall: RISC-V Instructions**

Texto destacado en celeste: **ONLY THESE SIX INSTRUCTION TYPES EXIST!**

Se repite la misma tabla de formatos de la Slide 5 (R, I, S, B, U, J y R4 con sus campos y anchos de bits idénticos).

## Slide 7

**Recall: RISC-V Instructions**

**However: We could use some other useful instructions!**

Examples:

1. **mv** - (move) to copy values from one register to another.
2. **li** - (load immediate) load an immediate value to a register.
3. **not** - logical not.
4. **call** - jump to a function in \<label\> and save return.
5. **ret** - (return) return to caller.
6. **j** - unconditional jump.
7. **jr** - jump to address in reg.
8. **nop** - do nothing.
   and many more…

None of these are part of the RISC-V INSTRUCTION FORMAT
**But a RISC-V CPU could easily do them, using existing instructions!**

## Slide 8

Slide divisoria de sección.

**2. Pseudoinstructions**

(Ícono de portapapeles + imagen decorativa de mano robótica.)

## Slide 9

**RISC-V Pseudoinstructions**

- Not part of the instruction set (cannot be directly converted to machine code).
- They are useful to programmers and compilers.
- Their intended goal CAN be achieved with one or more "real" instructions.
- They are **converted** into CPU compatible instructions during assembly.

Caja resaltada: **Pseudoinstructions are useful when coding, but the CPU ends up executing something different** ☺

## Slide 10

Tabla grande (recuadrada en rojo) de pseudoinstrucciones RISC-V y su traducción a instrucciones reales. Columnas: **Pseudoinstruction · RISC-V Instructions · Description · Operation**.

| Pseudoinstruction | RISC-V Instructions | Description | Operation |
|---|---|---|---|
| `nop` | `addi x0, x0, 0` | no operation | |
| `li rd, imm[11:0]` | `addi rd, x0, imm[11:0]` | load 12-bit immediate | rd = SignExtend(imm[11:0]) |
| `li rd, imm[31:0]` | `lui rd, imm[31:12]*` / `addi rd, rd, imm[11:0]` | load 32-bit immediate | rd = imm[31:0] |
| `mv rd, rs1` | `addi rd, rs1, 0` | move (also called "register copy") | rd = rs1 |
| `not rd, rs1` | `xori rd, rs1, -1` | one's complement | rd = ~rs1 |
| `neg rd, rs1` | `sub rd, x0, rs1` | two's complement | rd = -rs1 |
| `seqz rd, rs1` | `sltiu rd, rs1, 1` | set if = 0 | rd = (rs1 == 0) |
| `snez rd, rs1` | `sltu rd, x0, rs1` | set if ≠ 0 | rd = (rs1 ≠ 0) |
| `sltz rd, rs1` | `slt rd, rs1, x0` | set if < 0 | rd = (rs1 < 0) |
| `sgtz rd, rs1` | `slt rd, x0, rs1` | set if > 0 | rd = (rs1 > 0) |
| `beqz rs1, label` | `beq rs1, x0, label` | branch if = 0 | if (rs1 == 0) PC = label |
| `bnez rs1, label` | `bne rs1, x0, label` | branch if ≠ 0 | if (rs1 ≠ 0) PC = label |
| `blez rs1, label` | `bge x0, rs1, label` | branch if ≤ 0 | if (rs1 ≤ 0) PC = label |
| `bgez rs1, label` | `bge rs1, x0, label` | branch if ≥ 0 | if (rs1 ≥ 0) PC = label |
| `bltz rs1, label` | `blt rs1, x0, label` | branch if < 0 | if (rs1 < 0) PC = label |
| `bgtz rs1, label` | `blt x0, rs1, label` | branch if > 0 | if (rs1 > 0) PC = label |
| `ble rs1, rs2, label` | `bge rs2, rs1, label` | branch if ≤ | if (rs1 ≤ rs2) PC = label |
| `bgt rs1, rs2, label` | `blt rs2, rs1, label` | branch if > | if (rs1 > rs2) PC = label |
| `bleu rs1, rs2, label` | `bgeu rs2, rs1, label` | branch if ≤ (unsigned) | if (rs1 ≤ rs2) PC = label |
| `bgtu rs1, rs2, label` | `bltu rs2, rs1, offset` | branch if > (unsigned) | if (rs1 > rs2) PC = label |
| `j label` | `jal x0, label` | jump | PC = label |
| `jal label` | `jal ra, label` | jump and link | PC = label, ra = PC + 4 |
| `jr rs1` | `jalr x0, rs1, 0` | jump register | PC = rs1 |
| `jalr rs1` | `jalr ra, rs1, 0` | jump and link register | PC = rs1, ra = PC + 4 |
| `ret` | `jalr x0, ra, 0` | return from function | PC = ra |
| `call label` | `jal ra, label` | call nearby function | PC = label, ra = PC + 4 |
| `call label` | `auipc ra, offset[31:12]*` / `jalr ra, ra, offset[11:0]` | call far away function | PC = PC + offset, ra = PC + 4 |
| `la rd, symbol` | `auipc rd, symbol[31:12]*` / `addi rd, rd, symbol[11:0]` | load address of global variable | rd = PC + symbol |
| `l{b\|h\|w} rd, symbol` | `auipc rd, symbol[31:12]*` / `l{b\|h\|w} rd, symbol[11:0](rd)` | load global variable | rd = [PC + symbol] |
| `s{b\|h\|w} rs2, symbol, rs1` | `auipc rs1, symbol[31:12]*` / `s{b\|h\|w} rs2, symbol[11:0](rs1)` | store global variable | [PC + symbol] = rs2 |
| `csrr rd, csr` | `csrrs rd, csr, x0` | read CSR | rd = csr |
| `csrw csr, rs1` | `csrrw x0, csr, rs1` | write CSR | csr = rs1 |

(El asterisco `*` marca los casos donde el immediate/offset alto se ajusta por el signo del bit 11.)

## Slide 11

**LI (LOAD IMMEDIATE)**

Diagrama de decisión (a la izquierda): partiendo de `li rd, imm` se pregunta **"Is imm > 12 bits?"**
- Rama **No** → `addi rd, x0, imm[11:0]`
- Rama **Yes** → `lui rd, imm[31:12]` seguido de `addi rd, x0, imm[11:0]`

Texto (a la derecha):
- Allows loading an immediate value into a destination register.
- If the **immediate is up to 12 bits** (verde), the instruction `addi rd, x0, imm` is used.
- If the **immediate is larger than 12 bits** (rojo), it is split into two parts:
  - The upper part is loaded with `lui rd, imm[31:12]`.
  - Then it is adjusted with `addi rd, rd, imm[11:0]`.

## Slide 12

**NOP (NO OPERATION)**

Diagrama (izquierda): `nop` → (flecha hacia abajo) → `addi x0, x0, 0`, con la nota **"x0 always be 0"**.

Texto (derecha):
- Indicates a "no operation" instruction, **whose execution does not produce any changes in the registers or memory**.
- It is mainly used to create delay loops or to resolve data dependencies.

## Slide 13

**NOT**

Diagrama (izquierda): `not rd, rs1` → (flecha hacia abajo) → `xori rd, rs1, -1`.

Texto (derecha):
- Indicates a bitwise logical negation (inverts all bits of a register).
- It is implemented using an immediate XOR, since an XOR with a number composed of all '1's (which is -1) **inverts each bit of the operand.**

Fórmula (Recall: XOR properties):

$$a \oplus 1 = \sim a, \quad \text{where } \sim \text{ is bit complement.}$$

## Slide 14

Slide divisoria de sección.

**3. Directives**

(Ícono de portapapeles + imagen decorativa de mano robótica.)

## Slide 15

Tabla de directivas del ensamblador. Columnas: **Assembler Directive · Description**.

| Assembler Directive | Description |
|---|---|
| `.text` | Text section |
| `.data` | Global data section |
| `.bss` | Global data initialized to 0 |
| `.section .foo` | Section named `.foo` |
| `.align N` | Align next data/instruction on 2^N-byte boundary |
| `.balign N` | Align next data/instruction on N-byte boundary |
| `.globl sym` | Label `sym` is global |
| `.string "str"` | Store string "str" in memory |
| `.word w1,w2,...,wN` | Store N 32-bit values in successive memory words |
| `.byte b1,b2,...,bN` | Store N 8-bit values in successive memory bytes |
| `.space N` | Reserve N bytes to store variable |
| `.equ name, constant` | Define symbol `name` with value `constant` |
| `.end` | End of assembly code |

## Slide 16

Texto (izquierda):
The program in the Code begins by making the main label global (`.globl main`) so that the main function can be called from outside this file, typically by the OS or bootloader.

The value N is then set to 5 (`.equ N, 5`).

**What else?**

Captura de código ensamblador RISC-V (derecha):

```asm
.globl main            # make the main label global
.equ N, 5              # N = 5

.data                  # global data segment
A: .word 5, 42, -88, 2, -5033, 720, 314
str1: .string "RISC-V"
.align 2               # align next data on 2^2-byte boundary
B: .word 0x32A

.bss                   # bss segment - variables initialized to 0
C: .space 4
D: .space 1

.balign 4              # align next instruction on 4-byte boundary
.text                  # text segment (code)
main:
  la  t0, A            # t0 = address of A            = 0x2150
  la  t1, str1         # t1 = address of str1         = 0x216C
  la  t2, B            # t2 = address of B            = 0x2174
  la  t3, C            # t3 = address of C            = 0x2188
  la  t4, D            # t4 = address of D            = 0x218C
  lw  t5, N*4(t0)      # t5 = A[N] = A[5] = 720       = 0x2D0
  lw  t6, 0(t2)        # t6 = B = 810                 = 0x32A
  add t5, t5, t6       # t5 = A[N] + C = 720 + 810 = 1530 = 0x5FA
  sw  t5, 0(t3)        # C   = 1530                   = 0x5FA
  lb  t5, N-1(t1)      # t5 = str1[N-1] = str1[4] = '-' = 0x2D
  sb  t5, 0(t4)        # D   = str1[N-1]              = 0x2D
  la  t5, str2         # t5 = address of str2         = 0x140
  lb  t6, 8(t5)        # t6 = str2[8] = 'r'           = 0x72
  sb  t6, 0(t1)        # str1[0] = 'r'                = 0x72
  jr  ra               # return
.section .rodata
str2: .string "Hello world!"
.end                   # end of assembly file
```

## Slide 17

Dos diagramas de mapa de memoria lado a lado (Word Address / Data (MSB…LSB) / Variable).

**Memory allocation of global variables** (estado inicial, izquierda):

| Word Address | Data (MSB→LSB) | Variable |
|---|---|---|
| 218C | -- -- -- 00 | D |
| 2188 | 00 00 00 00 | C |
| 2184 | (vacío) | |
| 2180 | (vacío) | |
| 217C | (vacío) | |
| 2178 | (vacío) | |
| 2174 | 00 00 03 2A | B |
| 2170 | -- 00 56 2D | str1 |
| 216C | 43 53 49 52 | str1 |
| 2168 | 00 00 01 3A | A |
| 2164 | 00 00 02 D0 | A |
| 2160 | FF FF EC 57 | A |
| 215C | 00 00 00 02 | A |
| 2158 | FF FF FF A8 | A |
| 2154 | 00 00 00 2A | A |
| 2150 | 00 00 00 05 | A |

**Final values of global variables** (estado tras ejecución, derecha) — muestra las celdas que cambiaron (resaltadas):

| Word Address | Data (MSB→LSB) | Variable |
|---|---|---|
| 218C | -- -- -- **2D** | D |
| 2188 | **00 00 05 FA** | C |
| 2184 | (vacío) | |
| 2180 | (vacío) | |
| 217C | (vacío) | |
| 2178 | (vacío) | |
| 2174 | 00 00 03 2A | B |
| 2170 | -- 00 56 2D | str1 |
| 216C | 43 53 49 **72** | str1 |

Cambios respecto al estado inicial: D pasa de 00 a 2D, C pasa de 00000000 a 000005FA (1530), y el byte bajo de str1[0] pasa de 52 ('R') a 72 ('r').

## Slide 18

**Reference Books**

- Patterson, D. A., & Hennessy, J. L. (2020). Computer Organization and Design RISC-V Edition: The Hardware Software Interface. Morgan Kaufmann
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). Operating system concepts (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).

## Slide 19

Cierre. Texto grande "**Questions?**" sobre imagen decorativa de laboratorio.
