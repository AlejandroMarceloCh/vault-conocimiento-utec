---
curso: SISCOMP
titulo: 03 - Semana 1/01.Data types and representation.pptx
slides: 28
fuente: 03 - Semana 1/01.Data types and representation.pptx.pdf
---

## Slide 1

Portada. Título **COMPUTER SYSTEMS**, subtítulo **DATA TYPES AND REPRESENTATION**. Imagen decorativa de fondo (túnel tecnológico azul con figura de robot humanoide caminando).

## Slide 2

**Goals**

Analyze the main topics associated with data types, data sorting, and numerical systems.

(Imagen decorativa lateral: persona en laboratorio con gafas de protección.)

## Slide 3

**Summary**

Índice del capítulo, en dos columnas con íconos:

1. Numerical Systems
2. Memory organization
3. Byte ordering
4. Boolean algebra
5. Sign/Zero/Shift Operations
6. Conclusions

(Imagen decorativa: persona con visor de realidad virtual y globo terráqueo digital.)

## Slide 4

Separador de sección: **1. Numerical Systems** (imagen decorativa de mano robótica tocando un globo digital).

## Slide 5

**Bits**

- Binary Digit
- Useful for instructions, represent and manipulate numbers, sets, strings, etc.
- Electronic implementation: Bistable elements.

**Diagrama (visual):** Señal eléctrica analógica (forma de onda) sobre un eje de voltaje, con bandas horizontales amarillas que marcan los rangos válidos. Umbrales de voltaje etiquetados: 0.0V, 0.2V (banda inferior = "0"), 0.9V, 1.1V (banda superior = "1"). La onda empieza baja (nivel "0"), sube a la banda alta ("1"), y vuelve a bajar ("0"). Arriba, flechas horizontales delimitan tres tramos rotulados `0`, `1`, `0`, mostrando cómo se interpretan los niveles de tensión como bits.

## Slide 6

**Numerical Systems**

- Decimal numbers

$$1348_{10} = 1 \times 10^3 + 3 \times 10^2 + 4 \times 10^1 + 8 \times 10^0$$

- Binary numbers

$$1011010_2 = 1 \times 2^6 + 0 \times 2^5 + 1 \times 2^4 + 1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 0 \times 2^0 = 90_{10}$$

- Hexadecimal numbers

$$1E2_{16} = 0x1E2 = 1 \times 16^2 + E \times 16^1 + 2 \times 16^0 = 482_{10}$$

## Slide 7

**Number Conversion**

- Decimal to binary conversion

$$\text{Convert } 37_{10} = 1 \times 32 + 0 \times 16 + 0 \times 8 + 1 \times 4 + 0 \times 2 + 1 \times 1 = 100101_2$$

- Binary to decimal conversion

$$\text{Convert } 11101_2 = 1 \times 2^4 + 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 29_{10}$$

- Hexadecimal to decimal conversion

$$\text{Convert } 1E2_{16} = 0x1E2 = 1 \times 16^2 + E \times 16^1 + 2 \times 16^0 = 482_{10}$$

(A la derecha, imagen decorativa tipo "Matrix": bloque de dígitos verdes sobre fondo negro.)

## Slide 8

**Range for binary and decimal values**

- N-digit binary number

$$2^n : [0; 2^n - 1] \qquad 2^4 : [0,15] = [0000_2; 1111_2]$$

- N-digit decimal number

$$10^n : [0; 10^n - 1] \qquad 10^3 : [0; 10^3 - 1] = [0; 999]$$

## Slide 9

**Bits, Bytes and nibbles**

Columna izquierda con tres conceptos: **Bits**, **Bytes & Nibbles**, **Bytes**.

**Diagramas (visual):**
- Junto a "Bits": el byte `10010110` con llaves señalando el bit más a la izquierda como **most significant bit** y el de más a la derecha como **least significant bit**.
- Junto a "Bytes & Nibbles": `10010110` con una llave superior que abarca los 8 bits rotulada **byte**, y una llave inferior sobre los últimos 4 bits rotulada **nibble** (nibble = 4 bits).
- Junto a "Bytes": la cadena hex `CEBF9AD7` con llaves marcando el byte de la izquierda (`CE`) como **most significant byte** y el de la derecha (`D7`) como **least significant byte**.

Columna derecha (bullets):
- 1 byte = 8 bits
- From 0 to 11111111 (binary)
- From 0 to 255 (decimal)
- From 0 to FF (hexadecimal)

## Slide 10

**Data Representation**

Tabla de tamaños de tipos de dato en C:

| Data Type (C programming) | Typical 32-bit | Typical 64-bit |
|---|---|---|
| char | 1 | 1 |
| short | 2 | 2 |
| int | 4 | 4 |
| long | 4 | 8 |
| float | 4 | 4 |
| double | 8 | 8 |
| pointer | 4 | 8 |

## Slide 11

Separador de sección: **2. Memory organization: Byte oriented** (imagen decorativa de mano robótica y globo digital).

## Slide 12

**Machine words**

Bullets (a la derecha, señalados con una flecha gris):
- Native unit of information.
- Machines have 64-bit word size.

**Diagrama izquierdo (visual):** Comparación de organización de memoria. Cuatro columnas alineadas:
- **32-bit Words**: bloques con direcciones de inicio Addr = 0000, 0004, 0008, 0012 (cada palabra = 4 bytes).
- **64-bit Words**: bloques con Addr = 0000, 0008 (cada palabra = 8 bytes).
- **Bytes**: columna de celdas individuales.
- **Addr.**: direcciones de byte consecutivas 0000, 0001, 0002, ... hasta 0015.

**Recuadro derecho "Byte - Oriented" (visual):** título "Byte - Oriented", texto "Data accessed by programs : Address", y una fila de celdas (bytes) que va desde la dirección `00...0` (izquierda) hasta `FF...F` (derecha), con "..." en el medio, ilustrando el espacio de direcciones byte a byte.

## Slide 13

Separador de sección: **3. Byte Ordering** (imagen decorativa de mano robótica y globo digital).

## Slide 14

**How bytes are ordered in memory**

- **Big Endian:** Least significant byte has highest address (Sun, Mac, Internet).
- **Little Endian:** Least significant byte has lowest address (x86, ARM, iOS, RISC-V).

**Recuadro Example (visual):** Variable `m` con valor de 4 bytes `0x19283746`, dirección `&m` es `0x200`. Dos tablas de memoria (direcciones 0x200, 0x201, 0x202, 0x203):

Big Endian:

| 0x200 | 0x201 | 0x202 | 0x203 |
|---|---|---|---|
| 19 | 28 | 37 | 46 |

Little Endian:

| 0x200 | 0x201 | 0x202 | 0x203 |
|---|---|---|---|
| 46 | 37 | 28 | 19 |

## Slide 15

**Negative Numbers Representation**

Two-complement encoding to represent signed numbers.

**Method**

1. Convert the unsigned number to binary.
2. After the least significative "1", invert all numbers.

**Example** (recuadro): The binary representation of -19 is:

1. $19 = 10011_2$
2. Unsigned number: $10011_2$ and invert: $01101_2$, so the two-complement of -19 is $\mathbf{01101_2}$

(Nota: la slide presenta este método/ejemplo tal cual; el resultado que muestra es 01101₂.)

## Slide 16

Separador de sección: **4. Boolean Algebra** (imagen decorativa de mano robótica y globo digital).

## Slide 17

**George Boole and his Algebra**

Algebraic representation of logic: "1" is true, "0" is false.

Some important operators are:

1. `A & B` : AND operator
2. `A | B` : OR operator
3. `~A` : NOT operator
4. `A^B` : XOR operator

Operators `&`, `|`, `~`, `^` are bitwise.
Operators `&&`, `||` are not bitwise.

## Slide 18

**George Boole and his Algebra**

Cuatro tarjetas, cada una con el **símbolo lógico de la compuerta** (visual) y su tabla de verdad.

**A & B — AND operator** (símbolo: compuerta AND, entradas A, B, salida S):

| A | B | A&B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

**A | B — OR operator** (símbolo: compuerta OR, entradas A, B, salida Q):

| A | B | A\|B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**~A — NOT operator** (símbolo: inversor/buffer con burbuja, entrada A, salida S):

| A | ~A |
|---|---|
| 0 | 0 |
| 1 | 1 |

(Nota: la columna de salida de la tabla NOT en la slide muestra 0→0 y 1→1; es el contenido literal impreso.)

**A^B — XOR operator** (símbolo: compuerta XOR, entradas A₁, A₂, salida B):

| A | B | A^B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

(Nota: la última fila de la tabla XOR en la slide muestra 1,1→1; es el contenido literal impreso.)

## Slide 19

Separador de sección: **5. Sign/Zero/Shift** (imagen decorativa de mano robótica y globo digital).

## Slide 20

**Sign Extension**

Number value is the same, sign bit is copied to most significant bits.

**Example**
- 2 in 4-bit representation: `0010`
- 2 in 8-bit sign-extended: `00000010`

**Example with signed numbers**
- -6 in 4-bit representation: `1010`
- -6 in 8-bit sign-extended: `11111010`

## Slide 21

**Zero Extension**

Number value is the same, zeros are copied to most significant bits.

**Example**
- 2 in 4-bit representation: `0010`
- 2 in 8-bit zero-extended: `00000010`

**Example with signed numbers**
- -6 in 4-bit representation: `1010`
- -6 in 8-bit zero-extended: `00001010`

## Slide 22

**Shift operations**

Dos recuadros:

**Left Shift: x << y**
- Shift x left y positions
- Throw away extra bits on left
- Fill with 0's on right

Tabla (visual):

| | |
|---|---|
| X | 01100010 |
| << 3 | 00010000 |
| Log. >> 2 | 00011000 |
| Arith. >> 2 | 00011000 |

**Right Shift: x >> y**
- Shift x right y positions
- Throw away extra bits on right
- Fill with 0's on left

Tabla (visual):

| | |
|---|---|
| X | 10100010 |
| << 3 | 00010000 |
| Log. >> 2 | 00101000 |
| Arith. >> 2 | 11101000 |

**Arithmetic Shift: Repeat MSB on left** (el shift aritmético a la derecha replica el bit más significativo por la izquierda, preservando el signo).

## Slide 23

**Operations with Overflow**

Overflow is when the result is too big to fit in the bit size.

**Addition with Overflow** (visual, suma binaria con acarreo):

```
   111    (acarreos)
   1011
 + 0110
 ------
 10001    (el 1 más a la izquierda es el overflow)
```

**Negation: Complement and add 1** (recuadro):

$$X + \sim X = 1111...111_2 = -1$$
$$\sim X + 1 = -X$$

Tabla para **x = 0**:

| | Decimal | Hex | Binary |
|---|---|---|---|
| 0 | 0 | 00 00 | 00000000 00000000 |
| ~0 | -1 | FF FF | 11111111 11111111 |
| ~0+1 | 0 | 00 00 | 00000000 00000000 |

Tabla para **x = 15213**:

| | Decimal | Hex | Binary |
|---|---|---|---|
| x | 15213 | 3B 6D | 00111011 01101101 |
| ~x | -15214 | C4 92 | 11000100 10010010 |
| ~x+1 | -15213 | C4 93 | 11000100 10010011 |
| y | -15213 | C4 93 | 11000100 10010011 |

## Slide 24

**Operations with Overflow**

Integer subtraction: **Add negation of second operand**

**Subtraction with Overflow** (izquierda, ejemplo $7 - 6 = 7 + (-6)$):

```
+7:   0000 0000 ... 0000 0111
-6:   1111 1111 ... 1111 1010
      -----------------------
+1:   0000 0000 ... 0000 0001
```

**Subtraction with Overflow** (derecha, reglas):
- Subtraction of two + or two - : **No overflow**
- Subtraction + from - : **Overflow if sign is 0**
- Subtraction - from + : **Overflow if sign is 1**

## Slide 25

**Signed/Unsigned representation**

Tabla/diagrama de 3 columnas para 4 bits, con relación entre patrones de bits, interpretación con signo (complemento a dos) y sin signo. Codificado por color: verde para valores idénticos (0–7) y rojo para los que difieren (patrones con MSB=1).

| Bits | Signed | Unsigned |
|---|---|---|
| 0000 | 0 | 0 |
| 0001 | 1 | 1 |
| 0010 | 2 | 2 |
| 0011 | 3 | 3 |
| 0100 | 4 | 4 |
| 0101 | 5 | 5 |
| 0110 | 6 | 6 |
| 0111 | 7 | 7 |
| 1000 | -8 | 8 |
| 1001 | -7 | 9 |
| 1010 | -6 | 10 |
| 1011 | -5 | 11 |
| 1100 | -4 | 12 |
| 1101 | -3 | 13 |
| 1110 | -2 | 14 |
| 1111 | -1 | 15 |

Anotaciones entre las columnas Signed y Unsigned: en la zona verde (0–7) una flecha doble marca `=` (mismos valores); en la zona roja una flecha doble marca `+/- 16` (los valores con signo y sin signo difieren en 16).

## Slide 26

**Conclusions**

- Data representation is fundamental to understand how computers work.
- Numerical systems allow to express big numbers amounts and operations.
- Signed numbers allow negative values to be represented in a computer system.
- Boolean algebra translates logical operations (usually verbal) into mathematical expressions that the computer can execute based on instructions.

(Imagen decorativa lateral: profesor escribiendo en pizarra frente a estudiantes.)

## Slide 27

**Reference Books**

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann.
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press.
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). *Operating system concepts* (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).

## Slide 28

Cierre: **Questions?** (imagen decorativa de fondo: dos personas en laboratorio con equipo técnico).
