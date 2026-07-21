---
curso: SISCOMP
titulo: 04 - Semana 2/02b.RISC V Assembly
slides: 29
fuente: 04 - Semana 2/02b.RISC V Assembly.pdf
---

## Slide 1

Portada (decorativa). Título grande **COMPUTER SYSTEMS** y subtítulo **RISC V ASSEMBLY**. Fondo azul con silueta de un robot humanoide caminando por un túnel tecnológico.

## Slide 2

**Goals**

Analyze the assembly language and the instruction set architecture of RISC V.

(Imagen decorativa de una científica en laboratorio, lado izquierdo.)

## Slide 3

**Summary**

Índice del capítulo con íconos:

1. Conditional Statements
2. Loops
3. Arrays
4. Conclusions

(Imagen decorativa de mujer con visor de realidad virtual y un globo terráqueo digital de fondo.)

## Slide 4

**Summary**

- **Motivation:** Programs at high-level languages can be executed in modern processor systems.
- **Problem:** We need to understand the machine code and define its relationship with programming languages constructs.
- **Overview:**
  - Overview of conditional statements, loops, arrays and function calls.
  - ARM Assembly programming for high-level constructs.
  - Code and execute with an ARM emulator.
- **Conclusion:** We can create complex programs using assembly language by defining correct machine code instructions.

## Slide 5

Portada de sección (decorativa). **1. Conditional Statements**. Fondo con mano robótica tocando un globo digital.

## Slide 6

**If Statement**

Dos columnas: **High level Code** vs **RISC V Assembly Code**. La columna de assembly está vacía (recuadro celeste en blanco) — slide de planteamiento antes de mostrar la solución.

High level Code:
```c
if(a == m)
  f = g+h;
a = m - h;
```

## Slide 7

**If Statement**

Ahora con el assembly resuelto (recuadro celeste a la derecha).

High level Code:
```c
if(a == m)
  f = g + h;
a = m - h;
```

RISC V Assembly Code:
```asm
#s0 = a, s1 = m
#s2 = f, s3 = g, s4 = h

BNE s0, s1, L1
ADD s2, s3, s4
L1:
SUB s0, s1, s4
```

Nota inferior: **Assembly tests opposite case (i != j) of high-level code (i == j)** ("opposite case (i != j)" en naranja, "(i == j)" en azul).

## Slide 8

**If/Else Statement**

Dos columnas. La columna de assembly está vacía (recuadro celeste en blanco) — slide de planteamiento.

High level Code:
```c
if(a == m)
  f = g+h;
else
  a = m - h;
```

## Slide 9

**If/Else Statement**

Con el assembly resuelto.

High level Code:
```c
if(a == m)
  f = g + h;
else
  a = m - h;
```

RISC V Assembly Code:
```asm
#s0 = a, s1 = m
#s2 = f, s3 = g, s4 = h

  BNE s0, s1, L1
  ADD s2, s3, s4
  j L2
L1:
  SUB s0, s1, s4
L2:
```

## Slide 10

**Switch/Case Statement**

Dos columnas. La columna de assembly está vacía (recuadro celeste en blanco) — planteamiento.

High level Code:
```c
switch(button){
  case 1: am = 20; break;
  case 2: am = 50; break;
  case 3: am = 100; break;
  default: am = 0;
}
```

## Slide 11

**Switch/Case Statement**

Columna izquierda muestra la equivalencia con if/else. La columna de assembly (celeste) sigue vacía.

High level Code — **Equivalent with if/else**:
```c
if        (button == 1)   am = 20;
else if   (button == 2)   am = 50;
else if   (button == 3)   am = 100;
else                      am = 0;
```

## Slide 12

**Switch/Case Statement**

Con el assembly resuelto, dispuesto en dos sub-columnas dentro del recuadro celeste. OJO: en esta versión los valores de am son 20/40/60 (no 20/50/100).

High level Code:
```c
switch(sim){
  case 1: am = 20; break;
  case 2: am = 40; break;
  case 3: am = 60; break;
  default: am = 0;
}
```

RISC V Assembly Code:
```asm
#s0 = sim, s1 = am

case1:
   ADDI t0,zero, 1
   BNE s0, t0, case2
   ADDI s1,zero,20
   j done

case2:
   ADDI t0,zero, 2
   BNE s0, t0, case3
   ADDI s1,zero,40
   j done

case3:
   ADDI t0,zero, 3
   BNE s0, t0, def
   ADDI s1,zero,60
   j done

def:
   ADD s1,zero,zero
done:
```

## Slide 13

Portada de sección (decorativa). **2. Loops**. Fondo con mano robótica y globo digital.

## Slide 14

**While Loop**

Dos columnas. La columna de assembly está vacía (recuadro celeste) — planteamiento.

High level Code:
```c
int pow = 1
int x = 0;

while(pow != 128){
  pow = pow*2;
  x = x + 1;
  }
```

Pregunta al pie: **What does the code do?**

## Slide 15

**While Loop**

Con el assembly resuelto.

High level Code:
```c
int pow = 1
int x = 0;

while(pow != 128){
  pow = pow*2;
  x = x + 1;
  }
```

RISC V Assembly Code:
```asm
#s0 = pow, s1 = x

  ADDI s0,zero,1
  ADDI s1,zero,zero
  ADDI t0,zero,128
while:
  BEQ s0,t0,done
  SLLI s0,s0,1
  ADDI s1,s1,1
  J while
done:
```

Pregunta: **What does the code do?**

Nota inferior: **Assembly tests for the opposite case (pow == 128) of the C code (pow != 128).**

## Slide 16

**For Loop**

Solo texto, definición de la estructura del for:

`For (initialization; condition; loop operation) statement`

- **Initialization:** executes before the loop begins.
- **Condition:** is tested at the beginning of each iteration.
- **Loop operation:** executes at the end of each iteration.
- **Statement:** executes each time the condition is met.

## Slide 17

**Do/While Loop**

Dos columnas. La columna de assembly está vacía (recuadro celeste) — planteamiento.

High level Code:
```c
int pow = 1
int x = 0;

do{
  pow = pow*2;
  x = x + 1;
  } while(pow != 128);
```

## Slide 18

**Do/While Loop**

Con el assembly resuelto.

High level Code:
```c
int pow = 1
int x = 0;

do{
  pow = pow*2;
  x = x + 1;
  } while(pow != 128);
```

RISC V Assembly Code:
```asm
#s0 = pow, s1 = x

  ADDI s0,zero,1
  ADD s1,zero,zero
  ADDI t0,zero,128

while:
  SLLI s0,s0,1
  ADDI s1,s1,1
  BNE s0,t0,while
done:
```

(A diferencia del while, aquí no hay chequeo de condición al inicio: el cuerpo se ejecuta primero y BNE al final decide si repetir.)

## Slide 19

**For Loop**

Dos columnas. La columna de assembly está vacía (recuadro celeste) — planteamiento.

High level Code:
```c
int sum = 0;
int i;

for(i = 0; i < 10; i = i + 1){
  sum = sum + i;
  }
```

## Slide 20

**For Loop**

Con el assembly resuelto.

High level Code:
```c
int sum = 0;
int i;

for(i = 0; i < 10; i = i + 1){
  sum = sum + i;
  }
```

RISC V Assembly Code:
```asm
#s0 = i, s1 = sum

  ADDI s1,zero,0
  ADDI s0,zero,0
  ADDI t0,zero,10
for:
  BGE s0,t0,done
  ADD s1,s1,s0
  ADDI s0,t0,1
  J for
done:
```

## Slide 21

**For Loop**

Misma slide del for resuelto (repite el contenido de la Slide 20), pero agrega una pregunta grande al pie: **How to do a decremental loop?**

RISC V Assembly Code:
```asm
#s0 = i, s1 = sum

  ADDI s1,zero,0
  ADDI s0,zero,0
  ADDI t0,zero,10
for:
  BGE s0,t0,done
  ADD s1,s1,s0
  ADDI s0,t0,1
  J for
done:
```

## Slide 22

Portada de sección (decorativa). **3. Arrays**. Fondo con mano robótica y globo digital.

## Slide 23

**Arrays**

Texto explicativo:

Access large amounts of similar data:
- **Index:** access to each element
- **Size:** number of elements

**Example:** 5-element array

Base address = 0x14000000 (address of first element, scores[0])

Array elements accessed relative to base address.

A la derecha, **diagrama de memoria principal (Main memory)** con dos columnas (Address | Data), de arriba hacia abajo:

| Address    | Data         |
|------------|--------------|
| 1400031C   | scores[199]  |
| 14000318   | scores[198]  |
| ...        | ...          |
| 14000004   | scores[1]    |
| 14000000   | scores[0]    |

(Las direcciones crecen hacia arriba; scores[0] en la base 0x14000000, cada elemento ocupa 4 bytes.)

## Slide 24

**For Loop to access an array**

High level Code:
```c
int i;
int scores[200];

for(i = 0; i < 200; i = i + 1)
  scores[i] = scores[i] + 10
```

RISC V Assembly Code:
```asm
#s0 = scores base address, s1 = i

ADDI s1,zero,0
ADDI t2,zero,200

for:
BGE s1,t2,done
SLLI t0,s1,2
ADD t0,t0,s0
LW t1, 0(t0)
ADDI t1,t1,10
SW t1, 0(t0)
ADDI s1,s1,1
J fo
done:
```

(SLLI t0,s1,2 multiplica el índice por 4 —desplazamiento en bytes—; ADD suma la base; LW carga el elemento, +10, SW lo almacena. Nota: en la slide aparece `J fo`, truncado; debería ser `J for`.)

## Slide 25

**ASCII Code and Cast of Characters**

Texto:
- American Standard Code for Information Interchange (ASCII)
- Each text character has unique byte value
  - For example, S = 0x53, a = 0x61, A = 0x41
  - Lower-case and upper-case differ by 0x20 (32)

A la derecha, **tabla ASCII** (hex → char) en 6 pares de columnas (#, Char). Rango 0x20–0x7E:

| #  | Char  | #  | Char | #  | Char | #  | Char | #  | Char | #  | Char |
|----|-------|----|------|----|------|----|------|----|------|----|------|
| 20 | space | 30 | 0    | 40 | @    | 50 | P    | 60 | `    | 70 | p    |
| 21 | !     | 31 | 1    | 41 | A    | 51 | Q    | 61 | a    | 71 | q    |
| 22 | "     | 32 | 2    | 42 | B    | 52 | R    | 62 | b    | 72 | r    |
| 23 | #     | 33 | 3    | 43 | C    | 53 | S    | 63 | c    | 73 | s    |
| 24 | $     | 34 | 4    | 44 | D    | 54 | T    | 64 | d    | 74 | t    |
| 25 | %     | 35 | 5    | 45 | E    | 55 | U    | 65 | e    | 75 | u    |
| 26 | &     | 36 | 6    | 46 | F    | 56 | V    | 66 | f    | 76 | v    |
| 27 | '     | 37 | 7    | 47 | G    | 57 | W    | 67 | g    | 77 | w    |
| 28 | (     | 38 | 8    | 48 | H    | 58 | X    | 68 | h    | 78 | x    |
| 29 | )     | 39 | 9    | 49 | I    | 59 | Y    | 69 | i    | 79 | y    |
| 2A | *     | 3A | :    | 4A | J    | 5A | Z    | 6A | j    | 7A | z    |
| 2B | +     | 3B | ;    | 4B | K    | 5B | [    | 6B | k    | 7B | {    |
| 2C | ,     | 3C | <    | 4C | L    | 5C | \    | 6C | l    | 7C | \|   |
| 2D | -     | 3D | =    | 4D | M    | 5D | ]    | 6D | m    | 7D | }    |
| 2E | .     | 3E | >    | 4E | N    | 5E | ^    | 6E | n    | 7E | ~    |
| 2F | /     | 3F | ?    | 4F | O    | 5F | _    | 6F | o    |    |      |

## Slide 26

**Load & Store in an array**

Bullets:
- RISC-V also defines lh, lhu, and sh half-word loads and stores that operate on 16-bit data.
- Memory addresses for these instructions must be half-word aligned.

**Diagrama 1 (izquierda): Memory + Registers.**
- Memory: fila "Byte Address / Data" con celdas D3 D2 D1 D0 conteniendo F7 | 8C | 42 | 03.
- Registers (muestra cómo quedan tras loads/stores de byte):
  - `s1` = 00 00 00 8C ← `lbu s1, 2(s4)` (load byte unsigned: rellena con ceros)
  - `s2` = FF FF FF F7 ← `lb s2, 3(s4)` (load byte con signo: extiende el signo del byte F7)
  - `s3` = xx xx xx 9B ← `sb s3, 1(s4)` (store byte)

**Recuadro central (celeste): "Hello!"** — valores ASCII de cada carácter:
```
H    = 0x48
e    = 65
l    = 6C
l    = 6C
o    = 6F
!    = 21
Null = 00
```
(Los valores aparecen mezclando hex sin prefijo: 65, 6C, 6F, 21 son hexadecimales.)

**Diagrama 2 (derecha): distribución en memoria (Word Address | Data), little-endian.**

| Word Address | Data (MSB → LSB) |
|--------------|------------------|
| 1522FFF4     | 00 | 21 | 6F     |
| 1522FFF0     | 6C | 6C | 65 | 48 |

En 1522FFF0: 48('H') 65('e') 6C('l') 6C('l') como bytes de la palabra; en 1522FFF4 sigue 6F('o') 21('!') 00(Null). MSB a la izquierda, LSB a la derecha.

## Slide 27

**Conclusions**

- We reviewed fundamentals concepts in programming languages constructs.
- We reviewed assembly implementation for conditional statements, loops, arrays.
- We coded and executed high-level constructs using ARM syntax and instructions.
- We conclude that complex programs have a direct implementation in machine code that allows to execute them in the processor.

(Imagen decorativa de un profesor escribiendo en pizarra, lado derecho.)

## Slide 28

**Reference Books**

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann.
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press.
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). *Operating system concepts* (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).

## Slide 29

Cierre (decorativa). Título grande **Questions?** sobre fondo de dos estudiantes trabajando en un laboratorio con maquinaria.
