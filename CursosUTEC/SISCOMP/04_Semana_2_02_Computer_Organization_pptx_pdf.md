---
curso: SISCOMP
titulo: 04 - Semana 2/02.Computer Organization.pptx
slides: 25
fuente: 04 - Semana 2/02.Computer Organization.pptx.pdf
---

## Slide 1

Portada. Título grande "COMPUTER SYSTEMS" con subtítulo "GENERAL INFORMATION". Fondo decorativo (túnel tecnológico azul con silueta de robot/humano). Chrome UTEC / TransformaTec / "Reinventa el mundo".

## Slide 2

**Goals**

- Understand the computer organization.
- Identify the computer architectures and the Instruction Set Architecture.

Foto decorativa a la izquierda (científica en laboratorio).

## Slide 3

**Summary** (índice del capítulo, con iconos por cada punto)

| # | Tema |
|---|------|
| 1 | Computer architecture (icono portapapeles) |
| 2 | Memory (icono bombilla) |
| 3 | CPU (icono bombilla) |
| 4 | Input / Output (icono libros/dispositivos) |
| 5 | First Concepts (icono grupo/diana) |
| 6 | Conclusions (icono grupo/diana) |

Foto decorativa: mujer con visor de realidad virtual sobre globo terráqueo.

## Slide 4

**Computer Functions and Components**

1. **Data processing** — Multiple types of data and processing requirements.
2. **Data storage** — Short-term / Long-term
3. **Data movement**
   - Input-output (I/O): when data are received from or delivered to a device (peripheral) that is directly connected to the computer
   - Data communications: when data are moved over longer distances, to or from a remote device
4. **Control** — A control unit manages the computer's resources in response to commands (instructions).

**Visual (diagrama de círculos anidados / zoom sucesivo, lado derecho):** Tres burbujas conectadas por líneas punteadas que hacen "zoom":
- Burbuja 1 **COMPUTER**: contiene círculos I/O, Main memory, System Bus y (resaltado verde) **CPU**.
- Línea punteada expande CPU → Burbuja 2 **CPU**: contiene Registers, ALU, Internal Bus y (resaltado verde) **Control Unit**.
- Línea punteada expande Control Unit → Burbuja 3 **CONTROL UNIT** (fondo verde): contiene Sequencing Logic, Control Unit Registers and Decoders, Control Memory.

Cada nivel resalta en verde el componente que se expande en el siguiente nivel.

## Slide 5

**RISC V Architecture**

- First **open-source** instruction set architecture with broad commercial support.
- Defined in **2010** by Krste Asanovic, Andrew Waterman, David Patterson.
- **Comparable** in capabilities to commercial architectures such as ARM and x86.
- Commercial **chips**: SiFive and Western Digital

Recuadro gris destacado (cita): "Once you've learned one architecture, **it's easier to learn a different one** 🙂"

## Slide 6

Portada de sección. Número grande **1.** con icono portapapeles y título **Computer Architecture**. Fondo decorativo (mano robótica señalando globo).

## Slide 7

**Von Neumann Architecture**

- After Turing Machine (1936).
- Memory: Data memory / Instruction memory
- CPU: Arithmetic Logic Unit / Registers / Control

Pie: "Proposed by [Burks, Goldstein and von Neumann, 1946] in *Preliminary discussion of the logical design of an electronic computing instrument*"

**Visual (diagrama de bloques, izquierda):** flujo horizontal
`input` → **Memory** (cajas apiladas: `instructions`, `data`) ↔ **CPU** (`registers` como filas apiladas + `ALU` dibujada como trapecio) → `output`. Flechas dobles entre Memory y CPU. Foto decorativa pequeña a la derecha (hombre frente a rack de válvulas, estilo Alan Turing).

## Slide 8

**Von Neumann Model**

5 parts:
- Memory
- Processing Unit
- Input
- Output
- Control Unit

**BottleNeck:** Total time for access data can be higher than the execute program time.

**Visual (diagrama detallado clásico de Von Neumann, derecha):** rectángulo punteado = **Central processing unit (CPU)** que contiene:
- **Arithmetic-logic unit (CA)** (fondo amarillo): registros `AC` y `MQ` en la parte superior, ambos alimentando `Arithmetic-logic circuits`, que conecta con `MBR`.
- **Program control unit (CC)** (fondo morado): registros `PC` e `IBR`, `MAR` e `IR`, y `Control circuits` que emite `Control signals`.
A la izquierda, **Main memory (M)** dibujada como columna de celdas: M(0), M(1), M(2), M(3), M(4), …, M(4092), M(4093), M(4095); intercambia "Instructions and data" con el CPU y recibe "Addresses". A la derecha, caja **Input-output equipment (I, O)** (verde). Leyenda de siglas: AC=Accumulator register, MQ=multiply-quotient register, MBR=memory buffer register, IBR=instruction buffer register, PC=program counter, MAR=memory address register, IR=instruction register.

## Slide 9

Dos diagramas comparativos lado a lado.

**Harvard Architecture** (izquierda):
- Bloques: `I/O device` ↔ **Processor** (contiene `Control unit`, `Registers`, `ALU`) ↔ `I/O device`.
- `Instruction memory` → Processor (flecha unidireccional).
- Processor ↔ `Data memory` (flecha doble).
- Bullets: Complete separation of Instruction and Data memory regions. / *Rarely used in modern computers.*

**Modified Harvard Architecture** (derecha):
- Mismo esquema, pero `Instruction memory` y `Data memory` aparecen en una **sola caja dividida por línea punteada** que conecta al Processor.
- Bullets: Some degree of separation between Instruction and Data memory regions. / *Modern Processors.*

Diferencia clave dibujada: separación total (Harvard) vs. separación parcial / memoria compartida particionada (Modified Harvard).

## Slide 10

Portada de sección. Número grande **2.** con icono portapapeles y título **Memory**. Fondo decorativo (mano robótica).

## Slide 11

**Memory** (infografía de 5 nodos en línea, cada uno con icono circular azul y tarjeta debajo)

| Physically | Logically | ROM vs RAM | Data Memory | Instruction Memory |
|---|---|---|---|---|
| Linear sequence of **REGISTERS** — Addressable, Fixed-size | **To Store**: Data, Instructions. **HOW?** Sequence of bits | **Read Only Memory:** Sequential occupation of locations. **Random Access Memory:** Every register can be reached instantaneously. | High-level program. Variables, arrays, etc. HW level: Binary values. Reading/Writing memory registers. | Before high-level. Low-level instructions. Binary values. Executable (binary). Load to disk for running a program. |

Iconos: diana, cohete, lupa, calendario, cadena/enlace (conectados por línea horizontal).

## Slide 12

**Memory**

1. The memory **stores** — Data/Programs
2. The memory contains **bits** — Bits are grouped into bytes (8 bits) and words (e.g., 8, 16, 32 bits)
3. How the bits are accessed determines the **addressability**
   - E.g., word-addressable
   - E.g., 8-bit addressable (or byte-addressable)
   - The total **number of addresses** is the address space
     - In x86, the address space is $2^{32}$ y $2^{64}$.
     - In ARM, the address space is $2^{32}$. (32-bit addresses)
     - In x86-64, the address space is (up to) $2^{48}$. (48-bit addresses)

*(Nota: el texto plano muestra "232" y "248" — son $2^{32}$ y $2^{48}$; la slide los escribe con superíndice.)*

**Visual (derecha):** el mismo diagrama detallado de Von Neumann de la slide 8 (Main memory M(0)…M(4095), ALU con AC/MQ/MBR en caja amarilla, Program control unit con PC/IBR/MAR/IR, Input-output equipment, leyenda de siglas).

## Slide 13

**Accessing Memory**

1. There are two ways of accessing memory — Reading or loading / Writing or storing
2. Two registers are necessary to access memory — Memory Address Register (MAR) / Memory Data Register (MDR)
3. To read — Step 1: Load the MAR with the address / Step 2: Data is placed in MDR
4. To write — Step 1: Load the MAR with the address and the MDR with the data / Step 2: Activate Write Enable signal

**Visual (derecha):** de nuevo el diagrama detallado de Von Neumann (Main memory, CPU con ALU/MBR/AC/MQ y Program control unit PC/IBR/MAR/IR, Input-output equipment, leyenda de siglas).

## Slide 14

Portada de sección. Número grande **3.** con icono portapapeles y título **Control Processing Unit**. Fondo decorativo (mano robótica).

## Slide 15

**Central Processing Unit** (infografía en zigzag de 5 nodos circulares con iconos)

**Execute the instructions:**
- **Instructions** — Tells the CPU which computation to perform
- **Instructions** — Tells the CPU which registers to access
- **Instructions** — Which execute next
- **All Embedded**

**Main Elements:**
- ALU
- Set of registers
- Control Unit

Los nodos (lupa, diana, cohete, calendario, cadena) están dispuestos en cascada diagonal conectados por una línea curva; cada uno enlaza a un bloque de texto a izquierda o derecha.

## Slide 16

**Processing Unit**

- The processing unit can consist of many functional units.
- We start with a simple Arithmetic and Logic Unit (ALU), which executes computations
  - ARM: add, sub, mult, and, nor, …
- The ALU processes quantities that are referred to as **words**
  - Word length In ARM it is 32 bits
- Temporary storage: **Registers**:
  - E.g., to calculate (A+B)*C, the intermediate result of A+B is stored in a register

**Visual (derecha):** diagrama detallado de Von Neumann (ALU en caja amarilla con AC/MQ/MBR, Program control unit con PC/IBR/MAR/IR, Main memory M(0)…M(4095), Input-output equipment verde, leyenda de siglas).

## Slide 17

**REGISTERS**

- **Memory** is big but slow
- **Registers** — Registers are faster than memory / Ensure fast access to operands / Typically one register contains one word
- **Register set or file** — RISC-V has 32 registers / Each register is 32 bits (RV32I)

**Visual (tabla del ABI de RISC-V, derecha):**

| Register | ABI Name | Description |
|---|---|---|
| x0 | zero | Hard-wired zero |
| x1 | ra | Return address |
| x2 | sp | Stack pointer |
| x3 | gp | Global pointer |
| x4 | tp | Thread pointer |
| x5–7 | t0–2 | Temporaries |
| x8 | s0/fp | Saved register/frame pointer |
| x9 | s1 | Saved register |
| x10–11 | a0–1 | Function arguments/return values |
| x12–17 | a2–7 | Function arguments |
| x18–27 | s2–11 | Saved registers |
| x28–31 | t3–6 | Temporaries |

## Slide 18

Portada de sección. Número grande **4.** con icono portapapeles y título **Input / Output**. Fondo decorativo (mano robótica).

## Slide 19

**Input and Output**

- Many devices can be used for input and output
- They are called **peripherals**
- Input: Keyboard, Mouse, Scanner, Disks, Etc.
- Output: Monitor, Printer, Disks, Etc.

**Visual (derecha):** diagrama detallado de Von Neumann (mismo de slides anteriores: Main memory, ALU/MBR/AC/MQ en caja amarilla resaltada verde, Program control unit PC/IBR/MAR/IR, Input-output equipment, leyenda de siglas).

## Slide 20

**Control Unit**

- The control unit is similar to the conductor of an orchestra
- It conducts the **step-by-step** process of executing (every instruction in) a program
- It keeps track of the instruction being executed with an **instruction register** (IR), which contains the instruction
- Another register contains the address of the next instruction to execute. It is called **program counter** (PC) or **instruction pointer** (IP)

**Visual (derecha):** diagrama detallado de Von Neumann; en esta slide el **Program control unit (CC)** aparece resaltado en morado (contiene PC, IBR, MAR, IR, Control circuits) para enfatizar la unidad de control. Main memory M(0)…M(4095), ALU en caja, Input-output equipment, leyenda de siglas.

## Slide 21

**Programmer Visible (Architectural) State**

Tres componentes ilustrados:

- **Memory** (columna verde de celdas M[0], M[1], M[2], M[3], M[4], …, M[N-1]) — "Array of storage locations indexed by an address"
- **Registers** (pila de rectángulos azules) — given special names in the ISA (as opposed to addresses); general vs. special purpose
- **Program Counter** (barra amarilla) — memory address of the current instruction

Recuadro gris a la derecha: "**Instructions (and programs)** specify **how to transform the values of programmer visible state**"

## Slide 22

**Von Neumann Model**

Also called **stored program computer** (instructions in memory). It has two key properties:

1. **Stored program**
   - Instructions stored in a linear memory array
   - Memory is unified between instructions and data.
   - The interpretation of a stored value depends on the control signals
2. **Sequential instruction processing**
   - One instruction processed (fetched, executed, completed) at a time
   - Program counter (instruction pointer) identifies the current instruction
   - Program counter is advanced sequentially except for control transfer instructions

**Visual (derecha):** diagrama detallado de Von Neumann completo (ALU en caja amarilla con AC/MQ/MBR, Program control unit morado con PC/IBR/MAR/IR/Control circuits, Main memory azul M(0)…M(4095), Input-output equipment verde, leyenda de siglas).

## Slide 23

**Arithmetic Logic Unit**

- Low-level arithmetic and logical operations featured by the computer.
- ALU functionality: Manufacturer design.
- **HW Implementations:** Efficient but more expensive hardware.
- **SW Implementations:** Inexpensive and less efficient.

**Visual (derecha):** captura/diagrama de un datapath RISC-V con ALU personalizada. Arriba una caja con los campos de instrucción `funct7 | rs2 | rs1 | funct3 | rd | opcode`, cuyos campos alimentan el **Register File** y un bloque **ALU** (trapecio azul) con línea `bypass`. A la derecha una franja vertical **Pipeline Control / Custom Instruction Plugin** con señales `comman_valid`, `comman_ready`, `input1`, `input0`, `function`, `output`, `response_valid`, `response_ready` que conectan a un bloque **Custom ALU** (trapecio naranja). Ilustra la extensibilidad de la ALU con instrucciones personalizadas.

## Slide 24

**Reference Books**

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). *Operating system concepts* (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).

Foto decorativa a la derecha (profesor escribiendo en pizarra).

## Slide 25

Cierre. Título grande "**Questions?**" sobre foto decorativa (dos estudiantes en laboratorio). Chrome UTEC / TransformaTec.
