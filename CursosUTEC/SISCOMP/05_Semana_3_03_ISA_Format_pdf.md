---
curso: SISCOMP
titulo: 05 - Semana 3/03. ISA Format
slides: 32
fuente: 05 - Semana 3/03. ISA Format.pdf
---

## Slide 1

Portada (decorativa). Título del curso: **COMPUTER SYSTEMS**. Subtítulo: **ISA FORMAT**. Fondo con silueta de robot humanoide en un túnel tecnológico azul. Logo UTEC y lema "Reinventa el mundo", marca TransformaTec.

## Slide 2

**Motivation**

We need to move to a higher abstraction level between the software and detailed hardware.

We need to understand the processor instructions to be able to give commands.

**Goals**

Understand the instruction cycle.

Identify the RISC V instruction types and instruction formats.

(Imagen lateral decorativa: científica de laboratorio con guantes y gafas de protección.)

## Slide 3

**Summary** — índice del capítulo, presentado en dos columnas con iconos:

1. Instruction Execution
2. Instruction Cycle
3. Instruction Types
4. Language Machine Code
5. Conclusions
6. (sin título)

(Fondo decorativo: mujer con visor de realidad virtual sobre un globo terráqueo digital.)

## Slide 4

Slide divisoria de sección. Número grande **1.** con icono de portapapeles. Título: **Instruction Execution**. (Fondo decorativo: mano robótica tocando un globo digital.)

## Slide 5

**Instruction Execution**

By using instructions we can speak the language of the computer

Thus, we now know how to tell the computer to:

- Execute computations in the ALU by using, for instance, an addition
- Access operands from memory by using the load word instruction

(Recuadro destacado en celeste, con la pregunta en naranja:)
**How are the instructions executed on the computer?**

The process of executing an instruction is called is **the instruction cycle or instruction phases**.

## Slide 6

Slide divisoria de sección. Número grande **2.** con icono de portapapeles. Título: **Instruction Cycle**. (Fondo decorativo: mano robótica.)

## Slide 7

**Instruction Cycle**

The instruction cycle is a sequence of steps or phases, that an instruction goes through to be executed

Lista numerada de las 6 fases (cada fase en un color distinto). A la izquierda hay un recuadro verde claro "Next Instruction" con una flecha verde curva que rodea la lista de arriba (fase 6) hacia abajo y sube de nuevo a la fase 1, indicando el ciclo que se repite:

1. **FETCH:** Take the instruction
2. **DECODE:** What is the instruction about?
3. **EVALUATE ADDRESS:** Does it need something (data) from mem.?
4. **FETCH OPERANDS:** Take all the operands
5. **EXECUTE:** Perform the instruction real job.
6. **STORE RESULT:** Save the result (if it is needed …)

E.g.: Intel x86 instruction `ADD [eax], edx` has six phases

**Not all instructions have the six phases. E.g:**

- LW does not require EXECUTE
- ADD does not require EVALUATE ADDRESS

## Slide 8

**1. Fetch**

The FETCH phase obtains the **instruction from** memory and loads it into the instruction register.

Tres recuadros celestes con los pasos:
- **Step 1: Load MAR and increment PC**
- **Step 2: Access memory**
- **Step 3: Load IR with the content of MBR**

**Diagrama (derecha):** arquitectura tipo von Neumann/IAS. Un bloque punteado "Central processing unit (CPU)" contiene arriba la "Arithmetic-logic unit (CA)" con registros AC y MQ conectados a "Arithmetic-logic circuits" y a MBR (memory buffer register); y abajo el "Program control unit (CC)" con PC, IBR, MAR, IR y "Control circuits" (emite Control signals). A la izquierda una columna "Main memory (M)" con celdas M(0)…M(4095), conectada por "Instructions and data" y "Addresses". A la derecha "Input-output equipment (I, O)". Sobre el diagrama hay resaltado en ROJO el flujo del FETCH: un "+1" junto a PC, la ruta PC → MAR → memoria → MBR → IR (los bloques PC, MAR e IR aparecen recuadrados en rojo).

Leyenda de registros: AC = Accumulator register, MQ = multiply-quotient register, MBR = memory buffer register, IBR = instruction buffer register, PC = program counter, MAR = memory address register, IR = instruction register.

## Slide 9

**2. Decode**

The DECODE phase **identifies the instruction.**

- A **4-to-16 decoder** identifies which of the **16 opcodes** is going to be processed.
- A **decoder**, the input is the four bits **IR[24:21]**

(Recuadro celeste:) DECODE identifies the instruction to be processed

**Diagrama:** el mismo diagrama CPU/memoria de la slide anterior. Aquí se resalta en ROJO únicamente el registro **IR** (instruction register), con una flecha roja de IR hacia "Control circuits", ilustrando que el IR alimenta al decodificador/control.

## Slide 10

**3. Evaluate Address**

The EVALUATE ADDRESS phase **computes the address of the memory location** that is needed to process the instruction.

**Examples:**

1. This phase **is necessary in LW.** It computes the **address of the data word** that is to be read from memory **by adding an offset** to the content of a register
2. But **not necessary in ADD.**

(Recuadro celeste:) LDR calculates the address by adding a **register** and an **immediate**

**Diagrama:** mismo diagrama CPU/memoria. Se agrega un bloque rojo "Reg File" (junto a MBR) y se resaltan en rojo AC, "Arithmetic-logic circuits", MBR e IR, con flechas rojas que muestran el cálculo de dirección (register + offset) pasando por la ALU.

## Slide 11

**4. Fetch Operands**

The FETCH OPERANDS phase **obtains the source operands** needed to process the instruction.

**Example:** In LW
- Step 1: **Load MAR** with the address calculated in EVALUATE ADDRESS
- Step 2: Read memory, placing **source operand in MBR**

**Example:** In ADD
- Obtain the source operands **from the register file**
- In most current microprocessors, this phase can be done **at the same time the instruction is being decoded**

(Recuadro celeste:) LDR loads MAR (step 1), and places the results in MBR (step 2)

**Diagrama:** mismo diagrama CPU/memoria. Resaltado en ROJO el flujo del caso LW: "Arithmetic-logic circuits" → MBR, y la ruta hacia MAR / Main memory (bloques Arithmetic-logic circuits, MBR y MAR recuadrados en rojo), con la trayectoria de direcciones hacia Main memory.

## Slide 12

**4. Fetch Operands** (segunda variante — enfatiza el caso ADD)

Mismo texto que la slide 11 (definición y ejemplos LW y ADD).

(Recuadro celeste:) ADD operands from **Register File.**

**Diagrama:** mismo diagrama CPU/memoria. Aquí se resaltan en ROJO el bloque "Reg File" (agregado junto a MBR) y "Arithmetic-logic circuits", con flecha roja del Reg File a la ALU, ilustrando que en ADD los operandos vienen del banco de registros.

## Slide 13

**5. Execute**

The EXECUTE phase **executes the instruction**

**Example:** In ADD, it **performs addition in the ALU**

(Recuadro celeste:) ADD adds **SR1 and SR2**

**Diagrama:** mismo diagrama CPU/memoria; en esta slide la parte superior (Arithmetic-logic unit: AC, MQ, Arithmetic-logic circuits, MBR) está sombreada en ROSA/rojo tenue para indicar que la actividad ocurre en la ALU durante la ejecución.

## Slide 14

**6. Store Results**

The STORE RESULT phase **writes to the designated destination.**

Once STORE RESULT is completed, **a new instruction cycle** starts (with the FETCH phase)

(Recuadro celeste:) Instruction writes to **RegFile** or **Memory**

**Diagrama:** mismo diagrama CPU/memoria. Resaltado en ROJO el bloque "Reg File" y MBR, con una flecha roja que sale desde MBR/CPU hacia abajo hasta M(0) en Main memory, mostrando la escritura del resultado en RegFile o en memoria.

## Slide 15

Slide divisoria de sección. Número grande **3.** con icono de portapapeles. Título: **Instructions Types**. (Fondo decorativo: mano robótica.)

## Slide 16

**RISC V Types of instructions**

**Three main types of instructions:**

1. **Data-processing Instructions**
   - A. Logical operations
   - B. Shifts / rotate
   - C. Arithmetic
     - c1. with conditional Execution
2. **Branches**
3. **Memory**

## Slide 17

**RISC V Types of instructions**

**Tabla/diagrama de formatos de instrucción** (32 bits, divididos por rangos de bits). Encabezados de bits arriba: 31:25 | 24:20 | 19:15 | 14:12 | 11:7 | 6:0. Filas por tipo:

| 31:25 | 24:20 | 19:15 | 14:12 | 11:7 | 6:0 | Tipo |
|-------|-------|-------|-------|------|-----|------|
| funct7 | rs2 | rs1 | funct3 | rd | op | **R-Type** |
| imm₁₁:₀ | | rs1 | funct3 | rd | op | **I-Type** |
| imm₁₁:₅ | rs2 | rs1 | funct3 | imm₄:₀ | op | **S-Type** |
| imm₁₂,₁₀:₅ | rs2 | rs1 | funct3 | imm₄:₁,₁₁ | op | **B-Type** |
| imm₃₁:₁₂ | | | | rd | op | **U-Type** |
| imm₂₀,₁₀:₁,₁₁,₁₉:₁₂ | | | | rd | op | **J-Type** |
| fs3 | funct2 | fs2 | fs1 | funct3 | fd | op | **R4-Type** |

Tamaños de campo (abajo): 5 bits | 2 bits | 5 bits | 5 bits | 3 bits | 5 bits | 7 bits.
(Nota: los campos funct3 y op aparecen resaltados en azul en toda la tabla.)

## Slide 18

Slide divisoria de sección. Número grande **3.** con icono de portapapeles. Título: **Instructions Format**. (Fondo decorativo: mano robótica.)

## Slide 19

**R - Type Functions**

R-type (register-type) instructions use **three registers as operands**: two as sources and one as a destination

**Diagrama R-Type** (32 bits):

| 31:25 | 24:20 | 19:15 | 14:12 | 11:7 | 6:0 |
|-------|-------|-------|-------|------|-----|
| funct7 (7 bits) | rs2 (5) | rs1 (5) | funct3 (3) | rd (5) | op (7) |

**Tabla Assembly / Field Values / Machine Code:**

| Assembly | funct7 | rs2 | rs1 | funct3 | rd | op | Machine Code (hex) |
|----------|--------|-----|-----|--------|----|----|--------------------|
| add s2, s3, s4 (`add x18,x19,x20`) | 0 | 20 | 19 | 0 | 18 | 51 | 0000000 10100 10011 000 10010 0110011 (**0x01498933**) |
| sub t0, t1, t2 (`sub x5, x6, x7`) | 32 | 7 | 6 | 0 | 5 | 51 | 0100000 00111 00110 000 00101 0110011 (**0x407302B3**) |

## Slide 20

**R - Type Functions**

Translate the following RISC-V assembly instruction into machine language

`add t3, s4, s5`

**Tabla de resolución:**

| Assembly | funct7 | rs2 | rs1 | funct3 | rd | op | Machine Code |
|----------|--------|-----|-----|--------|----|----|--------------|
| add t3, s4, s5 (`add x28,x20,x21`) | 0 | 21 | 20 | 0 | 28 | 51 | 0000000 10101 10100 000 11100 0110011 (**0x015A0E33**) |

## Slide 21

**I - Type Functions**

- I-type (immediate) instructions use **two register operands and one immediate operand.**
- I-type instructions include addi, andi, ori, and xori, loads (lw, lh, lb, lhu, and lbu), and register jumps (jalr)

**Diagrama I-Type** (32 bits):

| 31:20 | 19:15 | 14:12 | 11:7 | 6:0 |
|-------|-------|-------|------|-----|
| imm₁₁:₀ (12 bits) | rs1 (5) | funct3 (3) | rd (5) | op (7) |

**Tabla Assembly / Field Values / Machine Code:**

| Assembly | imm₁₁:₀ | rs1 | funct3 | rd | op | Machine Code |
|----------|---------|-----|--------|----|----|--------------|
| addi s0, s1, 12 | 12 | 9 | 0 | 8 | 19 | 0000 0000 1100 01001 000 01000 0010011 (0x00C48413) |
| addi s2, t1, −14 | −14 | 6 | 0 | 18 | 19 | 1111 1111 0010 00110 000 10010 0010011 (0xFF230913) |
| lw t2, −6(s3) | −6 | 19 | 2 | 7 | 3 | 1111 1111 1010 10011 010 00111 0000011 (0xFFA9A383) |
| lb s4, 0x1F(s4) | 0x1F | 20 | 0 | 20 | 3 | 0000 0001 1111 10100 000 10100 0000011 (0x01FA0A03) |
| slli s2, s7, 5 | 5 | 23 | 1 | 18 | 19 | 0000 0000 0101 10111 001 10010 0010011 (0x005B9913) |
| srai t1, t2, 29 | (upper 7 bits = 32) 29 | 7 | 5 | 6 | 19 | 0100 0001 1101 00111 101 00110 0010011 (0x41D3D313) |

## Slide 22

**I - Type Functions**

Translate the following assembly instruction into machine language.

`lw t3, −36(s4)`

**Tabla de resolución:**

| Assembly | imm₁₁:₀ | rs1 | funct3 | rd | op | Machine Code |
|----------|---------|-----|--------|----|----|--------------|
| lw t3, −36(s4) (`lw x28, −36(x20)`) | −36 | 20 | 2 | 28 | 3 | 1111 1101 1100 10100 010 11100 000 0011 (**0xFDCA2E03**) |

## Slide 23

**I - Type Functions** (repetición de la slide 21)

Mismo contenido de la Slide 21: definición de I-type, diagrama I-Type y la misma tabla de ejemplos (addi, addi, lw, lb, slli, srai) con Field Values y Machine Code idénticos.

## Slide 24

**S/B Type Functions**

Like I-type instructions, S/B-type (store/branch) instructions use two register operands and one immediate operand. However, both of the register operands are **source registers (rs1 and rs2)** in S/B-type, whereas I-type instructions use one source register (rs1) and one destination register (rd)

**Diagrama S-Type y B-Type** (32 bits):

| 31:25 | 24:20 | 19:15 | 14:12 | 11:7 | 6:0 | Tipo |
|-------|-------|-------|-------|------|-----|------|
| imm₁₁:₅ | rs2 | rs1 | funct3 | imm₄:₀ | op | **S-Type** |
| imm₁₂,₁₀:₅ | rs2 | rs1 | funct3 | imm₄:₁,₁₁ | op | **B-Type** |

(7 bits | 5 | 5 | 3 | 5 | 7)

**Tabla Assembly / Field Values / Machine Code (S-Type stores):**

| Assembly | imm₁₁:₅ | rs2 | rs1 | funct3 | imm₄:₀ | op | Machine Code |
|----------|---------|-----|-----|--------|--------|----|--------------|
| sw t2, −6(s3) | 1111111 | 7 | 19 | 2 | 11010 | 35 | 1111111 00111 10011 010 11010 0100011 (0xFE79AD23) |
| sh s4, 23(t0) | 0000000 | 20 | 5 | 1 | 10111 | 35 | 0000000 10100 00101 001 10111 0100011 (0x01429BA3) |
| sb t5, 0x2D(zero) | 0000001 | 30 | 0 | 0 | 01101 | 35 | 0000001 11110 00000 000 01101 0100011 (0x03E006A3) |

## Slide 25

**S/B Type Functions**

Branches (beq, bne, blt, bge, bltu, and bgeu) use the B-type instruction format. For B-type instructions, rs1 and rs2 are the two source registers, and the 13-bit immediate branch offset, imm12:0, gives the number of bytes between the branch instruction and the BTA.

**Ejemplo de código (address / RISC-V Assembly)** con llaves que marcan la distancia:

```
#Address    # RISC-V Assembly
0x70        beq  s0, t5, L1   ⌉1
0x74        add  s1, s2, s3   ⌉2
0x78        sub  s5, s6, s7   ⌉3
0x7C        lw   t0, 0(s1)    ⌉4
0x80   L1:  addi s1, s1, -15
```

`L1` is 4 instructions (i.e., **16 bytes**) past `beq`

**Descomposición del inmediato:**

```
imm12:0 = 16 →  0   0 0 0 0   0 0 0 1   0 0 0 0
bit number     12  11 10 9 8  7 6 5 4   3 2 1 0
```
(el bit 0 se descarta/tacha; el valor 16 = bit 4 en 1)

**Tabla Assembly / Field Values / Machine Code (B-Type):**

| Assembly | imm₁₂,₁₀:₅ | rs2 | rs1 | funct3 | imm₄:₁,₁₁ | op | Machine Code |
|----------|-----------|-----|-----|--------|-----------|----|--------------|
| beq s0, t5, L1 (`beq x8, x30, 16`) | 0000000 | 30 | 8 | 0 | 10000 | 99 | 0000000 11110 01000 000 10000 1100011 (**0x01E40863**) |

## Slide 26

**S/B Type Functions** (repetición de la slide 24)

Mismo contenido de la Slide 24: definición S/B-type, diagramas S-Type y B-Type, y la misma tabla de ejemplos de stores (sw, sh, sb) con Field Values y Machine Code idénticos.

## Slide 27

**U/J Type Functions**

U/J-type (upper immediate/jump) instructions have one destination register operand rd and a 20-bit immediate field. In U-type instructions, the remaining bits specify the most significant 20 bits of a 32-bit immediate. In J-type instructions, the remaining 20 bits specify the most significant 20 bits of a 21-bit immediate jump offset.

**Diagrama U-Type y J-Type** (32 bits):

| 31:12 | 11:7 | 6:0 | Tipo |
|-------|------|-----|------|
| imm₃₁:₁₂ | rd | op | **U-Type** |
| imm₂₀,₁₀:₁,₁₁,₁₉:₁₂ | rd | op | **J-Type** |

(20 bits | 5 bits | 7 bits)

**Tabla Assembly / Field Values / Machine Code (U-Type):**

| Assembly | imm₃₁:₁₂ | rd | op | Machine Code |
|----------|----------|----|----|--------------|
| lui s5, 0x8CDEF (`lui x21,0x8CDEF`) | 0x8CDEF | 21 | 55 | 1000 1100 1101 1110 1111 10101 0110111 (**0x8CDEFAB7**) |

(Nota gris en recuadro:) `jalr` is an I-type (*not* J-type!) instruction. `jal` is the only J-type instruction.

## Slide 28

Slide divisoria de sección. Número grande **4.** con icono de portapapeles. Título: **Language Machine Code**. (Fondo decorativo: mano robótica.)

## Slide 29

**Interpreting Machine Language Code**

To interpret machine language, one must decipher the fields of each 32-bit instruction word. Different instructions use different formats, but all formats share a 7-bit opcode field.

Thus, the best place to begin is to look at the opcode to determine if it is an R-, I-, S/B-, or U/J-type instruction.

E.g. Translate the following machine language code into assembly language.

```
0x41FE83B3  →  0100 0001 1111 1110 1000 0011 1011 0011  (0x41FE83B3)
0xFDA48293  →  1111 1101 1010 0100 1000 0010 1001 0011  (0xFDA48293)
```

**Tabla de decodificación (Machine Code → Field Values → Assembly):**

Primera instrucción (R-Type, opcode 51):

| funct7 | rs2 | rs1 | funct3 | rd | op | | funct7 | rs2 | rs1 | funct3 | rd | op | Assembly |
|--------|-----|-----|--------|----|----|-|--------|-----|-----|--------|----|----|----------|
| 0100000 | 11111 | 11101 | 000 | 00111 | 0110011 | | 32 | 31 | 29 | 0 | 7 | 51 | sub x7, x29,x31 / **sub t2, t4, t6** |

Segunda instrucción (I-Type, opcode 19):

| imm₁₁:₀ | rs1 | funct3 | rd | op | | imm₁₁:₀ | rs1 | funct3 | rd | op | Assembly |
|---------|-----|--------|----|----|-|---------|-----|--------|----|----|----------|
| 1111 1101 1010 | 01001 | 000 | 00101 | 001 0011 | | −38 | 9 | 0 | 5 | 19 | addi x5, x9, −38 / **addi t0, s1, −38** |

## Slide 30

**Conclusions**

Now we can **speak** the language of the computer

Thus, we now know **how to tell** the computer to:

- **Execute** computations in the ALU by using, for instance, an addition
- **Access** operands from memory by using the load word instruction

(Recuadro celeste, en naranja:) **Now we know the Instruction Cycle**

## Slide 31

**Reference Books**

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).

(Imagen lateral decorativa: profesor escribiendo en una pizarra frente a estudiantes.)

## Slide 32

Slide de cierre (decorativa). Texto grande: **Questions?**. (Fondo: dos estudiantes con gafas de protección trabajando con maquinaria en un laboratorio.)
