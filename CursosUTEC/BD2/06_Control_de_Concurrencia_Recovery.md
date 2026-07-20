---
curso: BD2
titulo: 06  Control de Concurrencia - Recovery
slides: 104
fuente: 06  Control de Concurrencia - Recovery.pdf
---

# 06  Control de Concurrencia - Recovery

## Índice

- [Control de Concurrencia](#control-de-concurrencia)
  - [¿Qué es concurrencia?](#qué-es-concurrencia)
  - [Transacciones](#transacciones)
  - [Planificación de Transacciones](#planificación-de-transacciones)
  - [Problemas de la Concurrencia](#problemas-de-la-concurrencia)
  - [Planificación Serializable](#planificación-serializable)
  - [Técnicas de control de concurrencia](#técnicas-de-control-de-concurrencia)
  - [Técnicas de Bloqueo](#técnicas-de-bloqueo)
  - [Interbloqueos](#interbloqueos)
  - [Prevención de Interbloqueos](#prevención-de-interbloqueos)
- [Database Recovery](#database-recovery)
  - [Acceso a datos por una transacción](#acceso-a-datos-por-una-transacción)
  - [DB Recovery](#db-recovery)
  - [Recuperación basado en Log](#recuperación-basado-en-log)
  - [Estrategias de modificación](#estrategias-de-modificación)
  - [Proceso de recuperación](#proceso-de-recuperación)
  - [Proceso de recuperación con checkpoints](#proceso-de-recuperación-con-checkpoints)
  - [Ejercicio de recuperación](#ejercicio-de-recuperación)
  - [Recuperación en fallas de almacenamiento](#recuperación-en-fallas-de-almacenamiento)
  - [Componentes de un Sistema Administrador de Base de Datos](#componentes-de-un-sistema-administrador-de-base-de-datos)
- [Glosario](#glosario)

## Control de Concurrencia

### ¿Qué es concurrencia?

**Figura:** Slide con título central «Concurrencia» en letras grandes negras. La slide está dividida en dos secciones visuales principales.

**Sección superior — Acceso multiusuario a la base de datos:** Tres personas etiquetadas «USUARIO 3», «USUARIO 2» y «USUARIO 1» trabajan en computadoras. Una persona etiquetada «ADMINISTRADOR» aparece de pie con un maletín. En el centro, un cilindro etiquetado «DB Física» representa la base de datos física compartida. Líneas punteadas conectan a los usuarios con la base de datos a través de círculos intermedios etiquetados «sub 1», «sub 2» y «sub 3» (sub-esquemas o vistas de usuario). El administrador se conecta a un círculo etiquetado «Esquema», representando la estructura global de la base de datos.

**Sección inferior — Ejemplo de concurrencia transaccional:** Dos bloques de código SQL representan transacciones concurrentes sobre el mismo registro:

Transacción 1:
```sql
SQL> UPDATE employees
   2 SET salary=salary+100
   3 WHERE employee_id=100;
```
Debajo de esta transacción, un icono de candado amarillo representa un bloqueo sobre el registro.

Transacción 2:
```sql
SQL> UPDATE employees
   2 SET salary=salary*1.1
   3 WHERE employee_id=100;
```
Encima de esta transacción, un icono de reloj de arena (estado de espera); debajo, un icono de marca de verificación verde (finalización exitosa eventual).

Entre ambas transacciones, un documento azul con un signo de interrogación grande flotando encima, simbolizando la ambigüedad o el conflicto potencial cuando dos transacciones modifican la misma fila (`employee_id=100`) simultáneamente.

✔ Coordinación de la ejecución simultanea de transacciones en un SGBD que soporta multiprocesamiento.
  - Aumenta la productividad por la mejor utilización de recursos y produce que el tiempo de los usuarios se reduzca en promedio

❖ Cuando se ejecutan transacciones de manera concurrente puede haber interferencias entre ellas que produzcan resultados no correctos.
  - Una transacción individual producirá un estado correcto de la BD si se ejecuta de forma aislada.

**Figura:** Título «¿Qué es concurrencia?» en la parte superior. Lista de puntos con viñetas: el primer punto con marca de verificación verde (✔) describe la coordinación de ejecución simultánea; el subpunto con círculo vacío (○) indica los beneficios de productividad. El segundo punto con viñeta de diamante (❖) advierte sobre interferencias; el subpunto con círculo vacío (○) enfatiza el principio de ejecución aislada.

(slides 3–4)

### Transacciones

- Un conjunto de operaciones de acceso a base de datos que conforman una unidad lógica de trabajo.
- El SGBD debe garantizar que se realicen adecuadamente a pesar de la existencia de fallos.
- Puede iniciar con una instrucción BEGIN TRANSACTION (depende del SGBD).
- Hay dos operaciones obligatorias:
  - COMMIT: transacción exitosa, los cambios se deben hacer efectivos (persistencia)
  - ROLLBACK: transacción no exitosa, los cambios se deben deshacer.

**Figura:** Título «¿Qué es una transacción?» en la parte superior. Cuatro viñetas con círculos negros describen la definición, la responsabilidad del SGBD, el inicio con BEGIN TRANSACTION, y las dos operaciones obligatorias COMMIT y ROLLBACK con sus subpuntos indentados.

| Propiedad | Descripción |
|---|---|
| Atómica | Se realizan todas las acciones o no se realiza ninguna |
| Consistente | La base de datos satisfacen todas las restricciones después de una transacción. |
| Aislada | Una transacción no puede afectar otra aunque se ejecuten concurrentemente. |
| Durable | Una vez que hace COMMIT, la base de datos debe persistir los cambios. |

**Figura:** Slide con título «Propiedades de una transacción: ACID» en la parte superior izquierda. Cuatro filas horizontales, cada una representando una propiedad ACID: a la izquierda, una etiqueta en recuadro azul oscuro con el nombre de la propiedad (Atómica, Consistente, Aislada, Durable); a la derecha, un recuadro gris claro con la descripción correspondiente. La palabra «concurrentemente» en la propiedad Aislada aparece en negrita. Chevrón decorativo azul en el borde izquierdo.

**Figura:** Diagrama de transición de estados de una transacción. Los estados se representan como óvalos azules conectados por flechas:

- **Inicio de una transacción:** flecha de entrada hacia el estado **Activa**.
- **Activa:** estado inicial donde la transacción realiza operaciones. Bucle de auto-transición etiquetado «Leer, Escribir», indicando que pueden ocurrir múltiples operaciones de lectura/escritura en este estado.
- Desde **Activa**, siguiendo «Ultima instrucción», la transacción pasa a **Parcialmente confirmada**.
- Desde **Activa**, si ocurre un error o se ejecuta **ROLLBACK**, pasa directamente a **Fallida**.
- Desde **Parcialmente confirmada**, una operación **COMMIT** lleva a **Confirmada**; un **ROLLBACK** lleva a **Fallida**.
- Desde **Confirmada**, tras «Persistencia», la transacción pasa a **Terminada**.
- Desde **Fallida**, la operación «Deshacer» lleva a **Terminada**.
- **Terminada:** estado final del ciclo de vida de la transacción.

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100.00
WHERE name = 'Alice';
UPDATE branches SET balance = balance - 100.00
WHERE name = (SELECT branch_name FROM accounts
WHERE name = 'Alice');
UPDATE accounts SET balance = balance + 100.00
WHERE name = 'Bob';
UPDATE branches SET balance = balance + 100.00
WHERE name = (SELECT branch_name FROM accounts
WHERE name = 'Bob');
COMMIT;
```

¿Cómo gestionar dos transacciones que acceden a los mismos recursos?

**Figura (adicional):** En la esquina inferior izquierda, un bloque de código SQL que ilustra una transferencia atómica de $100 de Alice a Bob, actualizando tanto los saldos individuales de las cuentas como los totales de las sucursales correspondientes dentro de un bloque de transacción definido por `BEGIN;` y `COMMIT;`. En la parte inferior central, un recuadro resaltado en naranja contiene la pregunta: «¿Cómo gestionar dos transacciones que acceden a los mismos recursos?».

(slides 5–7)

### Planificación de Transacciones

- Para $n$ transacciones $T1, T2, …, Tn$, una planificación:
  - Representa el orden cronológico en el que se ejecutan las instrucciones de dichas transacciones en el sistema.
  - La secuencia debe conservar el orden dentro de cada transacción individual.
- Dadas las siguientes transacciones:

| $T1$ | $T2$ |
|---|---|
| READ(X) | READ(X) |
| X = X – 50 | TEMP = A * 0.1 |
| WRITE(X) | A = A – TEMP |
| READ(Y) | WRITE(A) |
| Y = Y + 50 | READ(Y) |
| WRITE(Y) | Y = Y + TEMP |
| | WRITE(Y) |

**Figura:** Título «Planificación de Transacciones» en la parte superior. Dos viñetas con definiciones de planificación. Debajo, dos tablas verticales con encabezados azules «$T1$» y «$T2$» en columnas separadas, cada una listando las operaciones de la transacción correspondiente en filas con fondo azul claro.

- Se pueden definir las siguientes planificaciones secuenciales:

**Planificación 1 ($T1$ luego $T2$):**

| $T1$ | $T2$ |
|---|---|
| READ(X) | |
| X = X – 50 | |
| WRITE(X) | |
| READ(Y) | |
| Y = Y + 50 | |
| WRITE(Y) | |
| | READ(X) |
| | TEMP = A * 0.1 |
| | A = A – TEMP |
| | WRITE(A) |
| | READ(Y) |
| | Y = Y + TEMP |
| | WRITE(Y) |

**Planificación 2 ($T2$ luego $T1$):**

| $T1$ | $T2$ |
|---|---|
| | READ(X) |
| | TEMP = A * 0.1 |
| | A = A – TEMP |
| | WRITE(A) |
| | READ(Y) |
| | Y = Y + TEMP |
| | WRITE(Y) |
| READ(X) | |
| X = X – 50 | |
| WRITE(X) | |
| READ(Y) | |
| Y = Y + 50 | |
| WRITE(Y) | |

- Cada transacción se ejecuta completamente antes de la siguiente.
- Para un conjunto de $n$ transacciones hay $n!$ planificaciones secuenciales.

**Figura:** Slide con título «Planificación de Transacciones» en la parte superior. Dos tablas lado a lado que ilustran las dos planificaciones secuenciales posibles: a la izquierda, $T1$ completa seguida de $T2$ completa; a la derecha, $T2$ completa seguida de $T1$ completa. Cada tabla tiene columnas con encabezados azules «$T1$» y «$T2$». Debajo de las tablas, dos viñetas resumen que cada transacción se ejecuta completamente antes de la siguiente y que para $n$ transacciones hay $n!$ planificaciones secuenciales.

- Pero se pueden definir un numero $m \gg n!$ de planificaciones concurrentes.

| $T1$ | $T2$ |
|---|---|
| READ(X) | |
| X = X – 50 | |
| | READ(X) |
| | TEMP = A * 0.1 |
| WRITE(X) | |
| READ(Y) | |
| | A = A – TEMP |
| | WRITE(A) |
| | READ(Y) |
| Y = Y + 50 | |
| WRITE(Y) | |
| | Y = Y + TEMP |
| | WRITE(Y) |

**Figura:** A la derecha de la tabla, dos círculos concéntricos ilustran la diferencia de cardinalidad entre tipos de planificación: un círculo gris pequeño etiquetado «Planificacion es secuenciales» y un círculo azul grande que lo rodea etiquetado «Planificaciones concurrentes», representando visualmente que el conjunto de planificaciones concurrentes es mucho mayor que el de secuenciales.

(slides 9–11)

### Problemas de la Concurrencia

#### Actualización perdida

- Actualización perdida: se asume modificación inmediata.

| $T1$ | Tiempo | $T2$ | X=100 |
|---|---|---|---|
| | t1 | READ(X) | |
| READ(X) | t2 | | |
| | t3 | X=X+100 | |
| X=X-10 | t4 | | |
| | t5 | WRITE(X) | |
| WRITE(X) | t6 | | |
| | t7 | COMMIT | |
| COMMIT | t8 | | |

**Figura:** Slide con título «Problemas de la Concurrencia» y subtítulo «Actualización perdida: se asume modificación inmediata». Tabla central con cuatro columnas: $T1$, Tiempo, $T2$ y X=100 (valor inicial del dato). La tabla muestra la ejecución entrelazada de dos transacciones desde t1 hasta t8. Encabezados de columna en azul; filas alternan entre blanco y gris azulado.

- Actualización perdida: se asume modificación inmediata.

| $T1$ | Tiempo | $T2$ | X |
|---|---|---|---|
| | t1 | READ(X) | 100 |
| READ(X) | t2 | | 100 |
| | t3 | X=X+100 | |
| X=X-10 | t4 | | |
| | t5 | WRITE(X) | |
| WRITE(X) | t6 | | |
| | t7 | COMMIT | |
| COMMIT | t8 | | |

1. Ambas transacciones guardan su copia de X.

**Figura:** Misma estructura de tabla que la slide anterior, pero con una cuarta columna «X» que muestra el valor del dato en cada paso. En t1 y t2, X=100. A la derecha de la tabla, una anotación numerada «1. Ambas transacciones guardan su copia de X.» explica que ambas transacciones leen y almacenan localmente el valor inicial de 100.

- Actualización perdida: se asume modificación inmediata.

| $T1$ | Tiempo | $T2$ | X |
|---|---|---|---|
| | t1 | READ(X) | 100 |
| READ(X) | t2 | | 100 |
| | t3 | X=X+100 | 100 |
| X=X-10 | t4 | | 100 |
| | t5 | WRITE(X) | |
| WRITE(X) | t6 | | |
| | t7 | COMMIT | |
| COMMIT | t8 | | |

1. Ambas transacciones guardan su copia de X.
2. T1 y T2 realizan modificaciones diferentes en X.

**Figura:** Misma tabla con columna X mostrando 100 en t1, t2, t3 y t4 (el valor en memoria principal no cambia mientras las transacciones modifican sus copias locales). Las operaciones `X=X+100` en T2 (t3) y `X=X-10` en T1 (t4) están resaltadas con círculos azules. A la derecha, dos anotaciones numeradas: «1. Ambas transacciones guardan su copia de X.» y «2. T1 y T2 realizan modificaciones diferentes en X.»

- Actualización perdida: se asume modificación inmediata.

| $T1$ | Tiempo | $T2$ | X |
|---|---|---|---|
| | t1 | READ(X) | 100 |
| READ(X) | t2 | | 100 |
| | t3 | X=X+100 | 100 |
| X=X-10 | t4 | | 100 |
| | t5 | WRITE(X) | 200 |
| WRITE(X) | t6 | | |
| | t7 | COMMIT | |
| COMMIT | t8 | | |

1. Ambas transacciones guardan su copia de X.
2. T1 y T2 realizan modificaciones diferentes en X.
3. T2 actualiza su valor en memoria principal.

**Figura:** Misma tabla; en t5, T2 ejecuta `WRITE(X)` (resaltado con círculo azul) y el valor de X en la columna derecha cambia a 200 (escrito en rojo). A la derecha, tres anotaciones numeradas, la tercera indica: «3. T2 actualiza su valor en memoria principal.»

- Actualización perdida: se asume modificación inmediata.

| $T1$ | Tiempo | $T2$ | X |
|---|---|---|---|
| | t1 | READ(X) | 100 |
| READ(X) | t2 | | 100 |
| | t3 | X=X+100 | 100 |
| X=X-10 | t4 | | 100 |
| | t5 | WRITE(X) | 200 |
| WRITE(X) | t6 | | 90 |
| | t7 | COMMIT | 90 |
| COMMIT | t8 | | 90 |

1. Ambas transacciones guardan su copia de X.
2. T1 y T2 realizan modificaciones diferentes en X.
3. T2 actualiza su valor en memoria principal.
4. T1 actualiza y se pierde la actualización de T2.

**Figura:** Tabla completa del escenario de actualización perdida. En t5, T2 escribe X=200 (en rojo). En t6, T1 ejecuta `WRITE(X)` (resaltado con círculo azul) y X pasa a 90 (en rojo), sobrescribiendo la actualización de T2. En t7 y t8, X permanece en 90 tras los COMMIT de ambas transacciones. A la derecha, cuatro anotaciones numeradas; la cuarta indica: «4. T1 actualiza y se pierde la actualización de T2.»

(slides 12–16)

#### Dependencia no confirmada

- Dependencia no confirmada: lectura no confirmada.

| $T1$ | Tiempo | $T2$ | X=100 |
|---|---|---|---|
| | t1 | READ(X) | |
| | t2 | X=X+100 | |
| | t3 | WRITE(X) | |
| READ(X) | t4 | | |
| X=X-10 | t5 | | |
| | t6 | ROLLBACK | |
| WRITE(X) | t7 | | |
| COMMIT | t8 | | |

**Figura:** Slide con título «Problemas de la Concurrencia» y subtítulo «Dependencia no confirmada: lectura no confirmada». Tabla central con cuatro columnas: $T1$, Tiempo, $T2$ y X=100 (valor inicial). La tabla muestra la ejecución entrelazada desde t1 hasta t8, donde T2 modifica X y luego hace ROLLBACK mientras T1 lee el valor modificado no confirmado. Encabezados en azul; filas alternan blanco y gris azulado.

- Dependencia no confirmada: lectura no confirmada.

| $T1$ | Tiempo | $T2$ | X |
|---|---|---|---|
| | t1 | READ(X) | 100 |
| | t2 | X=X+100 | 100 |
| | t3 | WRITE(X) | 200 |
| READ(X) | t4 | | |
| X=X-10 | t5 | | |
| | t6 | ROLLBACK | |
| WRITE(X) | t7 | | |
| COMMIT | t8 | | |

1. T2 actualiza X a 200.

**Figura:** Misma estructura de tabla con columna X. En t3, T2 ejecuta `WRITE(X)` (resaltado con círculo azul) y X cambia a 200 (en rojo). A la derecha, anotación numerada: «1. T2 actualiza X a 200.»

- Dependencia no confirmada: lectura no confirmada.

| $T1$ | Tiempo | $T2$ | X |
|---|---|---|---|
| | t1 | READ(X) | 100 |
| | t2 | X=X+100 | 100 |
| | t3 | WRITE(X) | 200 |
| READ(X) | t4 | | 200 |
| X=X-10 | t5 | | 200 |
| | t6 | ROLLBACK | |
| WRITE(X) | t7 | | |
| COMMIT | t8 | | |

1. T2 actualiza X a 200.
2. T1 lee el nuevo valor de X.

**Figura:** Misma tabla; en t4, T1 ejecuta `READ(X)` (resaltado con círculo azul) y lee X=200 (en rojo). En t5, X permanece en 200. A la derecha, dos anotaciones numeradas: «1. T2 actualiza X a 200.» y «2. T1 lee el nuevo valor de X.»

- Dependencia no confirmada: lectura no confirmada.

| $T1$ | Tiempo | $T2$ | X |
|---|---|---|---|
| | t1 | READ(X) | 100 |
| | t2 | X=X+100 | 100 |
| | t3 | WRITE(X) | 200 |
| READ(X) | t4 | | 200 |
| X=X-10 | t5 | | 200 |
| | t6 | ROLLBACK | 100 |
| WRITE(X) | t7 | | |
| COMMIT | t8 | | |

1. T2 actualiza X a 200.
2. T1 lee el nuevo valor de X.
3. T2 hace rollback por lo que la actualización previa se deshace.

**Figura:** Tabla completa del escenario de dependencia no confirmada (lectura sucia). En t3, X=200 (en rojo). En t4 y t5, X=200 (en rojo) mientras T1 opera sobre el valor no confirmado. En t6, T2 ejecuta `ROLLBACK` (resaltado con círculo azul) y X revierte a 100 (en rojo). T1 continúa en t7 con `WRITE(X)` y en t8 con `COMMIT`, basándose en el valor ya invalidado. A la derecha, tres anotaciones numeradas; la tercera indica: «3.

- Dependencia no confirmada: lectura no confirmada.

| T1 | Tiempo | T2 | X |
|---|---|---|---|
| | t1 | READ(X) | 100 |
| | t2 | X=X+100 | 100 |
| | t3 | WRITE(X) | 200 |
| READ(X) | t4 | | 200 |
| X=X-10 | t5 | | 200 |
| | t6 | ROLLBACK | 100 |
| WRITE(X) | t7 | | 190 |
| COMMIT | t8 | | 190 |

1. T2 actualiza X a 200.
2. T1 lee el nuevo valor de X.
3. T2 hace ROLLBACK por lo que la actualización previa se deshace.
4. T1 continua trabajando con el valor actualizado por lo que el nuevo valor de X es incorrecto.

**Figura:** Tabla de ejecución intercalada de dos transacciones T1 y T2 sobre el dato X, con cuatro columnas (T1, Tiempo, T2, X). Los valores 200 en t3 y t4, 100 en t6 tras el ROLLBACK, y 190 en t7 y t8 aparecen resaltados en rojo. La operación WRITE(X) de T1 en t7 está rodeada con un círculo azul. A la derecha de la tabla, una lista numerada del 1 al 4 explica paso a paso el problema de lectura no confirmada.

(slides 17–21)

#### Suma incorrecta y lectura no repetible

- Suma incorrecta:
  - Si una transacción esta calculando una suma sobre varios registros, mientras otras transacciones están actualizando algunos de estos registros, la función suma puede tomar algunos valores antes que sean actualizados y otros después de ser actualizados.
    - Ejemplo: compras en líneas .

- Lectura no repetible:
  - En dos lecturas sucesivas de un elemento, la transacción $T_i$ recibe respuestas distintas.

Los problemas de concurrencia generan inconsistencias en la base de datos.

**Figura:** Slide con dos bullets principales (Suma incorrecta y Lectura no repetible), cada uno con sub-bullets.

(slide 22)

### Planificación Serializable

- ¿Cómo asegurar que una planificación concurrente es correcta?
  - Debe tener el mismo efecto que una planificación secuencial.

Una planificación serializable es una planificación concurrente equivalente a una secuencial.

A
C
I
D

**Figura:** Recuadro azul centrado con la definición de planificación serializable; la palabra «equivalente» aparece subrayada y en negrita. Una flecha gris apunta desde «equivalente» hacia el acrónimo ACID escrito verticalmente (A, C, I, D) en el lado derecho del recuadro.

- Dado el conjunto de todas las planificaciones concurrentes posibles.

**Figura:** Diagrama tipo diagrama de Venn con tres conjuntos etiquetados. A la izquierda, un círculo gris pequeño etiquetado «Planificaciones secuenciales». A la derecha, un círculo azul grande etiquetado «Planificaciones concurrentes». Dentro del círculo azul, un círculo amarillo más pequeño etiquetado «Planificaciones serializables». Una flecha gruesa de doble punta de color azul claro conecta el círculo gris («Planificaciones secuenciales») con el círculo amarillo («Planificaciones serializables»), indicando equivalencia entre planificaciones secuenciales y serializables.

- ¿Cómo saber si una planificación es serializable?

- Precedencia
  - Se tiene que una transacción $T_A$ precede a una transacción $T_B$, si $T_B$ lee un dato que $T_A$ modificó o si $T_A$ lee un dato que $T_B$ modificará.
  - Se denota como $T_A \to T_B$

- Seriabilidad
  - Proceso de determinar que una planificación concurrente es equivalente a una secuencial, es decir si $T_A \to T_B$ o $T_B \to T_A$.

**Figura:** Slide con pregunta principal en la parte superior, seguida de dos secciones con bullets: «Precedencia» (con definición de precedencia entre transacciones y notación $T_A \to T_B$) y «Seriabilidad» (con definición del proceso de determinar equivalencia secuencial).

- Serialización por Conflictos

Se dice que dos instrucciones $I_i$ e $I_j$ (de las transacciones $T_i$ y $T_j$ respectivamente, $i \neq j$) están en conflicto si: son de distintas transacciones, operan sobre el mismo elemento de datos, y al menos una de ellas actualiza dicho dato.

Para probar si un plan es serializable por conflictos se usa un grafo de precedencia o grafo de serialización.

**Figura:** Definición de conflicto entre instrucciones centrada en un recuadro, con las frases «distintas transacciones», «mismo elemento» y «actualiza» en negrita. En la parte inferior, un recuadro con borde punteado gris oscuro contiene la frase sobre el uso del grafo de precedencia o grafo de serialización.

- Grafo de precedencia

Determina si una planificación es serializable por conflicto.

Cada transacción es un nodo.

Los arcos determinan la precedencia, determinada por los conflictos definidos antes.

Si existe un ciclo, la planificación no es serializable.

**Figura:** Plantilla de diagrama vacía con cuatro niveles verticales. En cada nivel, un círculo vacío a la izquierda conectado por una línea corta vertical al nivel siguiente, y un rectángulo horizontal largo vacío que se extiende hacia la derecha desde el círculo. Los círculos y rectángulos están sin etiquetar, representando la estructura base de un grafo de precedencia.

- Grafo de precedencia
  - Se representa como un grafo dirigido $G = (N, A)$, con $N = \{T_1, T_2, \dots, T_n\}$, y $A = \{a_1, a_2, \dots, a_m\}$.
  - Donde cada arco tiene la forma $a_i = (T_j \to T_k)$, $T_j$ es el nodo inicial de $a_i$ y $T_k$ es el nodo final.
  - El arco se crea si una de las operaciones de $T_j$ aparece en el plan antes que alguna operación en conflicto de $T_k$.

**Figura:** Slide con bullet «Grafo de precedencia» y tres sub-bullets que definen formalmente el grafo dirigido $G = (N, A)$, la forma de los arcos $a_i = (T_j \to T_k)$, y la regla para crear arcos según el orden de operaciones en conflicto.

- Algoritmo para crear el grafo de precedencia

**Figura:** Tres filas horizontales, cada una mostrando un par de operaciones en conflicto seguido de una flecha gruesa hacia el arco resultante en el grafo:

1. **Conflicto Write-Read:** $T_i$: `WRITE(X)` → $T_j$: `READ(X)` → arco dirigido $T_i \to T_j$.
2. **Conflicto Read-Write:** $T_j$: `READ(X)` → $T_i$: `WRITE(X)` → arco dirigido $T_j \to T_i$.
3. **Conflicto Write-Write:** $T_i$: `WRITE(X)` → $T_j$: `WRITE(X)` → arco dirigido $T_i \to T_j$.

Cada fila presenta las operaciones de transacciones distintas sobre el mismo elemento $X$, con flechas indicando el orden temporal, y una flecha más gruesa hacia la derecha que indica la arista a añadir al grafo de precedencia.

- Grafo de precedencia: Ejemplo 1.

| T1 | T2 | T3 |
|---|---|---|
| | READ(Z) | |
| | READ(Y) | |
| | WRITE(Y) | |
| | | READ(Y) |
| | | READ(Z) |
| READ(X) | | |
| WRITE(X) | | |
| | | WRITE(Y) |
| | | WRITE(Z) |
| | READ(X) | |
| READ(Y) | | |
| WRITE(Y) | | |
| | WRITE(X) | |

**Figura:** A la izquierda, tabla de planificación concurrente con tres columnas (T1, T2, T3) y las operaciones intercaladas de arriba hacia abajo en el orden indicado en la tabla. A la derecha, tres nodos circulares etiquetados T1 (arriba izquierda), T2 (arriba derecha) y T3 (abajo centro), dispuestos en forma triangular, sin aristas dibujadas aún.

- Grafo de precedencia: Ejemplo 1.

| T1 | T2 | T3 |
|---|---|---|
| | READ(Z) | |
| | READ(Y) | |
| | WRITE(Y) | |
| | | READ(Y) |
| | | READ(Z) |
| READ(X) | | |
| WRITE(X) | | |
| | | WRITE(Y) |
| | | WRITE(Z) |
| | READ(X) | |
| READ(Y) | | |
| WRITE(Y) | | |
| | WRITE(X) | |

**Figura:** Misma tabla de planificación que en el slide anterior. En la tabla, dos flechas azules indican dependencias entre T2 y T3: una desde READ(Z) de T2 hacia WRITE(Z) de T3, y otra desde WRITE(Y) de T2 hacia WRITE(Y) de T3. A la derecha, el grafo de precedencia muestra tres nodos (T1, T2, T3) con un único arco dirigido de T2 a T3 etiquetado «Y, Z». El nodo T1 permanece aislado sin aristas.

- Grafo de precedencia: Ejemplo 1.

| T1 | T2 | T3 |
|---|---|---|
| | READ(Z) | |
| | READ(Y) | |
| | WRITE(Y) | |
| | | READ(Y) |
| | | READ(Z) |
| READ(X) | | |
| WRITE(X) | | |
| | | WRITE(Y) |
| | | WRITE(Z) |
| | READ(X) | |
| READ(Y) | | |
| WRITE(Y) | | |
| | WRITE(X) | |

**Figura:** Misma tabla de planificación. Una flecha azul apunta desde WRITE(Y) de T2 hacia READ(Y) de T1. El grafo de precedencia a la derecha muestra tres nodos con dos aristas: T2 → T1 etiquetada «Y», y T2 → T3 etiquetada «Y, Z».

- Grafo de precedencia: Ejemplo 1.

| T1 | T2 | T3 |
|---|---|---|
| | READ(Z) | |
| | READ(Y) | |
| | WRITE(Y) | |
| | | READ(Y) |
| | | READ(Z) |
| READ(X) | | |
| WRITE(X) | | |
| | | WRITE(Y) |
| | | WRITE(Z) |
| | READ(X) | |
| READ(Y) | | |
| WRITE(Y) | | |
| | WRITE(X) | |

**Figura:** Misma tabla de planificación. Una flecha azul diagonal apunta desde READ(Y) de T3 hacia WRITE(Y) de T1. El grafo de precedencia muestra tres aristas: T2 → T1 etiquetada «Y», T2 → T3 etiquetada «Y, Z», y T3 → T1 etiquetada «Y».

- Grafo de precedencia: Ejemplo 1.

| T1 | T2 | T3 |
|---|---|---|
| | READ(Z) | |
| | READ(Y) | |
| | WRITE(Y) | |
| | | READ(Y) |
| | | READ(Z) |
| READ(X) | | |
| WRITE(X) | | |
| | | WRITE(Y) |
| | | WRITE(Z) |
| | READ(X) | |
| READ(Y) | | |
| WRITE(Y) | | |
| | WRITE(X) | |

**Figura:** Misma tabla de planificación. Una flecha azul apunta desde WRITE(X) de T1 hacia WRITE(X) de T2. El grafo de precedencia completo muestra cuatro aristas: T1 → T2 etiquetada «X», T2 → T1 etiquetada «Y», T2 → T3 etiquetada «Y, Z», y T3 → T1 etiquetada «Y».

- Grafo de precedencia: Ejemplo 1.

| T1 | T2 | T3 |
|---|---|---|
| | READ(Z) | |
| | READ(Y) | |
| | WRITE(Y) | |
| | | READ(Y) |
| | | READ(Z) |
| READ(X) | | |
| WRITE(X) | | |
| | | WRITE(Y) |
| | | WRITE(Z) |
| | READ(X) | |
| READ(Y) | | |
| WRITE(Y) | | |
| | WRITE(X) | |

Hay un ciclo => No es serializable

**Figura:** Misma tabla de planificación con flecha azul desde WRITE(X) de T1 hacia WRITE(X) de T2. El grafo de precedencia muestra cuatro aristas: T1 → T2 etiquetada «X» (en rojo), T2 → T1 etiquetada «Y» (en rojo), T2 → T3 etiquetada «Y, Z» (en gris), y T3 → T1 etiquetada «Y» (en gris). Las aristas rojas T1 ↔ T2 forman un ciclo. En la parte inferior derecha, un recuadro con borde rojo punteado contiene el texto «Hay un ciclo => No es serializable».

- Grafo de precedencia: Ejemplo 2.

| T1 | T2 | T3 |
|---|---|---|
| | READ(Z) | |
| | READ(Y) | |
| | WRITE(Y) | |
| | | READ(Y) |
| | | READ(Z) |
| | | WRITE(Y) |
| READ(Y) | | |
| WRITE(Y) | | |
| | | WRITE(Z) |
| | READ(X) | |
| | WRITE(X) | |
| READ(X) | | |
| WRITE(X) | | |

**Figura:** Tabla de planificación concurrente con tres columnas (T1, T2, T3) y operaciones en el orden indicado en la tabla (difiere del Ejemplo 1: T3 ejecuta WRITE(Y) antes de las operaciones de T1 sobre Y, y T2 completa READ(X)/WRITE(X) antes de T1). A la derecha, tres nodos circulares T1 (arriba izquierda), T2 (arriba derecha) y T3 (abajo centro) sin aristas dibujadas.

- Grafo de precedencia: Ejemplo 2.

| T1 | T2 | T3 |
|---|---|---|
| | READ(Z) | |
| | READ(Y) | |
| | WRITE(Y) | |
| | | READ(Y) |
| | | READ(Z) |
| | | WRITE(Y) |
| READ(Y) | | |
| WRITE(Y) | | |
| | | WRITE(Z) |
| | READ(X) | |
| | WRITE(X) | |
| READ(X) | | |
| WRITE(X) | | |

**Figura:** Misma tabla del Ejemplo 2. A la derecha, grafo de precedencia con tres nodos y tres aristas: T2 → T1 etiquetada «Y, X», T2 → T3 etiquetada «Y, Z», y T3 → T1 etiquetada «Y». Debajo del grafo, dos recuadros: el superior lista las dependencias $T_2 \to T_1$, $T_2 \to T_3$, $T_3 \to T_1$; el inferior indica «Planificación secuencial equivalente» con el orden $T_2 \to T_3 \to T_1$.

- Grafo de precedencia: Ejemplo 2.

**Tabla izquierda — Planificación concurrente:**

| T1 | T2 | T3 |
|---|---|---|
| | READ(Z) | |
| | READ(Y) | |
| | WRITE(Y) | |
| | | READ(Y) |
| | | READ(Z) |
| | | WRITE(Y) |
| READ(Y) | | |
| WRITE(Y) | | |
| | | WRITE(Z) |
| | READ(X) | |
| | WRITE(X) | |
| READ(X) | | |
| WRITE(X) | | |

**Tabla derecha — Planificación secuencial equivalente:**

| T1 | T2 | T3 |
|---|---|---|
| | READ(Z) | |
| | READ(Y) | |
| | WRITE(Y) | |
| | READ(X) | |
| | WRITE(X) | |
| | | READ(Y) |
| | | READ(Z) |
| | | WRITE(Y) |
| | | WRITE(Z) |
| READ(Y) | | |
| WRITE(Y) | | |
| READ(X) | | |
| WRITE(X) | | |

$T_2 \to T_3 \to T_1$

Planificación secuencial equivalente

**Figura:** Dos tablas lado a lado. La tabla izquierda muestra la planificación concurrente original (mismas operaciones intercaladas del Ejemplo 2). La tabla derecha reorganiza las mismas operaciones en orden secuencial: primero todas las de T2, luego todas las de T3, y finalmente todas las de T1. Debajo, un recuadro con borde naranja punteado contiene $T_2 \to T_3 \to T_1$, y debajo del recuadro el texto «Planificación secuencial equivalente».

1. Crear la estructura de grafo a partir de la planificación concurrente de transacciones.

1. Algoritmo para verificar si se arma al menos un ciclo dentro del grafo.

1. Caso que no haya ciclos, algoritmo debe indicar al menos una planificación secuencial equivalente.

**Figura:** Tres pasos numerados (cada uno con el número «1.»), cada uno acompañado de diagramas:

- **Paso 1:** Grafo con nodos T1, T2, T3 y aristas T2 → T1, T2 → T3, T3 → T1 (sin ciclos).
- **Paso 2:** El mismo grafo con una arista adicional en rojo T1 → T2, formando un ciclo entre T1 y T2.
- **Paso 3:** Dos recuadros verdes con borde punteado: el superior lista $T_2 \to T_1$, $T_2 \to T_3$, $T_3 \to T_1$; el inferior muestra el orden secuencial $T_2 \to T_3 \to T_1$.

(slides 23–39)

### Técnicas de control de concurrencia

- El objetivo es garantizar que la ejecución de un conjunto de transacciones sea serializable:
  - Bloqueos
  - Marcas de tiempo
  - Validación

**Figura:** A la derecha de la lista de técnicas, un corchete azul agrupa **Bloqueos** y **Marcas de tiempo** bajo la etiqueta **Pesimistas**. Una flecha azul apunta desde **Validación** hacia la etiqueta **Optimista**.

- Pesimistas: Garantizan la seriabilidad antes de la ejecución.
- Optimistas: Se ejecutan y luego se verifica si la ejecución es serializable.

(slide 41)

### Técnicas de Bloqueo

- El bloqueo regula el acceso concurrente a objetos compartidos (buffer de datos).
  - Granularidad: pueden aplicarse a diferentes unidades de dato.

**Figura:** A la izquierda, diagrama de cuatro óvalos concéntricos anidados que representan niveles de granularidad, de mayor a menor (de afuera hacia adentro):

1. **Base de datos** (óvalo exterior)
2. **Tabla**
3. **Registro**
4. **Campo** (óvalo interior)

Una flecha azul apunta hacia abajo desde el nivel más externo hacia el más interno. A la derecha de la flecha, una lista de consecuencias al moverse hacia un grano más fino:

- Grano más fino
- Mayor concurrencia
- Mayores posibilidades de interbloqueo
- Más costos de manejo de concurrencia

- Bloqueo Exclusivo (Protocolo PX)

**Figura:** Diagrama con los siguientes componentes:

- **Memoria Principal (compartida):** recuadro grande a la izquierda con varias filas horizontales. Una fila superior contiene una barra naranja dividida en cuatro segmentos verticales. Una fila inferior contiene una barra naranja etiquetada con la letra **B**.
- **Área de trabajo $T_i$:** recuadro vacío a la derecha de la memoria principal, que representa el área de trabajo de la transacción $T_i$.
- **Concurrence Manager:** recuadro con doble borde en la parte inferior central.
- Una flecha azul parte del texto **$T_i$: XREAD(R)** y apunta hacia el **Concurrence Manager**, indicando que la transacción $T_i$ solicita una lectura exclusiva del recurso $R$.

- Bloqueo Exclusivo (Protocolo PX)

**Figura:** Diagrama con los siguientes componentes y flujo:

- **Memoria Principal (compartida):** recuadro grande a la izquierda. Una fila superior contiene una barra naranja dividida en segmentos; un segmento específico está resaltado. Una fila inferior contiene una barra naranja etiquetada **B**.
- **Área de trabajo $T_i$:** recuadro a la derecha que contiene un círculo con borde verde etiquetado **$R_i$**, representando una copia local del recurso.
- **Concurrence Manager:** recuadro con doble borde en la parte inferior central.
- Flecha desde **$T_i$: XREAD(R)** hacia el **Concurrence Manager** (solicitud de bloqueo exclusivo).
- Flecha desde el **Concurrence Manager** hacia el segmento bloqueado en la **Memoria Principal** (concesión del bloqueo).
- Flecha azul desde el segmento bloqueado en la **Memoria Principal** hacia el círculo **$R_i$** en el **Área de trabajo $T_i$** (lectura del dato a la copia local).

- Bloqueo Exclusivo (Protocolo PX)

**Figura:** Diagrama con los siguientes componentes y flujo:

- **Memoria Principal (compartida):** recuadro grande a la izquierda con filas horizontales. Una fila superior contiene una barra naranja dividida en segmentos (un segmento bloqueado). Una fila inferior contiene una barra naranja etiquetada **B**.
- **Área de trabajo $T_i$:** recuadro a la derecha con un círculo etiquetado **$R_i$**. Flecha azul desde el segmento bloqueado en memoria hacia **$R_i$**.
- **Concurrence Manager:** recuadro con doble borde en la parte inferior central. Flecha desde **$T_i$: XREAD(R)** hacia el manager; flecha desde el manager hacia el segmento bloqueado en memoria.
- **Cola de espera:** a la derecha del Concurrence Manager, una línea horizontal etiquetada **$T_j, \dots, T_n$** con el texto **Cola de espera** debajo, indicando que otras transacciones esperan mientras $T_i$ mantiene el bloqueo exclusivo.

- Bloqueo Exclusivo (Protocolo PX)

| T1 | Tiempo | T2 |
|---|---|---|
| XREAD(R) | t1 | |
| COPY R.F INTO ATEMP | | |
| | t2 | XREAD(R) |
| XWRITE(R): | t3 | wait |
| REPLACE R.F BY ATEMP + 1 | | |
| XRELEASE(R) | t4 | wait |
| | t5 | (reinicia XREAD(R)) |
| | | COPY R.F INTO BTEMP |
| | t6 | XWRITE(R): |
| | | REPLACE R.F BY BTEMP*2 |
| | t7 | XRELEASE(R) |

- Bloqueo Compartido (Protocolo PS)

**Figura:** Diagrama con los siguientes componentes:

- **Memoria Principal (compartida):** recuadro grande a la izquierda con filas horizontales. Una fila superior contiene una barra naranja dividida en cuatro segmentos. Una fila inferior contiene una barra naranja etiquetada **B**.
- **Área de trabajo $T_i$:** recuadro vacío a la derecha de la memoria principal.
- **Concurrence Manager:** recuadro con doble borde en la parte inferior central.
- Una flecha apunta desde el texto **$T_i$: SREAD(R)** hacia el **Concurrence Manager**, indicando que la transacción $T_i$ solicita una lectura compartida del recurso $R$.

- Bloqueo Compartido (Protocolo PS)

**Figura:** Diagrama con los siguientes componentes y flujo:

- **Memoria Principal (compartida):** recuadro grande a la izquierda. Una fila superior contiene una barra naranja dividida en segmentos; un segmento específico está resaltado. Una fila inferior contiene una barra naranja etiquetada **B**.
- **Área de trabajo $T_i$:** recuadro a la derecha que contiene un círculo con borde verde etiquetado **$R_i$**.
- **Concurrence Manager:** recuadro con doble borde en la parte inferior central.
- Flecha desde **$T_i$: SREAD(R)** hacia el **Concurrence Manager**.
- Flecha desde el **Concurrence Manager** hacia el segmento en la **Memoria Principal**.
- Flecha azul desde el segmento en la **Memoria Principal** hacia el círculo **$R_i$** en el **Área de trabajo $T_i$**.

- Bloqueo Compartido (Protocolo PS)

**Figura:** Diagrama con los siguientes componentes:

- **Memoria Principal (compartida):** recuadro grande a la izquierda. Una fila superior contiene una barra naranja dividida en cuatro segmentos; una flecha azul parte de uno de ellos. Una fila inferior contiene una barra naranja etiquetada **B**.
- **Área de trabajo $T_i$:** recuadro superior a la derecha, actualmente vacío.
- **Área de trabajo $T_s$:** recuadro inferior a la derecha, actualmente vacío.
- **Concurrence Manager:** recuadro con doble borde en la parte inferior central.
- Dos flechas apuntan hacia el **Concurrence Manager**:
  - **$T_i$: SREAD(R)**
  - **$T_s$: SREAD(R)**
- Flecha bidireccional entre el **Concurrence Manager** y el segmento correspondiente en la **Memoria Principal**.

- Bloqueo Compartido (Protocolo PS)

**Figura:** Diagrama con los siguientes componentes y flujo:

- **Memoria Principal (compartida):** recuadro grande a la izquierda. Una fila superior contiene una barra naranja dividida en cuatro segmentos. Una fila inferior contiene una barra naranja etiquetada **B**.
- **Área de trabajo $T_i$:** recuadro superior a la derecha que contiene un círculo con borde verde etiquetado **$R_i$**. Flecha desde un segmento de la memoria hacia **$R_i$**.
- **Área de trabajo $T_s$:** recuadro inferior a la derecha que contiene un círculo con borde verde etiquetado **$R_s$**. Flecha desde otro segmento de la misma barra en memoria hacia **$R_s$**.
- **Concurrence Manager:** recuadro con doble borde en la parte inferior central, con flecha hacia el segmento en memoria.
- Dos solicitudes apuntan al manager:
  - **$T_i$: SREAD(R)**
  - **$T_s$: SREAD(R)**

- Bloqueo Compartido (Protocolo PS)

**Figura:** Diagrama con los siguientes componentes y flujo:

- **Memoria Principal (compartida):** recuadro grande a la izquierda. Una fila superior contiene una barra naranja dividida en segmentos. Una fila inferior contiene una barra naranja etiquetada **B**.
- **Área de trabajo $T_i$:** recuadro superior a la derecha con un círculo etiquetado **$R_i$**. Flecha desde el segmento en memoria hacia **$R_i$**.
- **Área de trabajo $T_s$:** recuadro inferior a la derecha con un círculo etiquetado **$R_s$**. Flecha desde el mismo segmento en memoria hacia **$R_s$**.
- **Concurrence Manager:** recuadro con doble borde en la parte inferior derecha. Flechas desde **$T_i$: SREAD(R)** y **$T_s$: SREAD(R)** hacia el manager; flecha desde el manager hacia el segmento en memoria.
- **Cola de espera de bloqueo exclusivo:** debajo de las solicitudes activas, una línea horizontal etiquetada **$T_j, \dots, T_n$** con el texto **Cola de espera de bloqueo exclusivo**, indicando transacciones que esperan un bloqueo exclusivo mientras los bloqueos compartidos están activos.

- Bloqueo Compartido (Protocolo PS)

ACC1=40
ACC2=50
ACC3=30

| T1 | Tiempo | T2 |
|---|---|---|
| SREAD(ACC1) | t1 | |
| SUM = SUM + ACC1 (40) | | |
| SREAD(ACC2) | t2 | |
| SUM = SUM + ACC2 (90) | | |
| | t3 | XREAD(ACC3) |
| | | ACC3 = ACC3 – 10 |
| | | XWRITE(ACC3) |
| SREAD(ACC3) | t4 | |
| wait | | |
| wait | t5 | XRELEASE(ACC3) |
| | | SREAD(ACC1) |
| SUM = SUM + ACC3 (110) | t6 | |
| | t7 | COMMIT |

- Bloqueo Compartido (Protocolo PS)

¿Qué pasa aquí?

| T1 | Tiempo | T2 |
|---|---|---|
| SREAD(ACC1) | t1 | |
| SUM = SUM + ACC1 | | |
| SREAD(ACC2) | t2 | |
| SUM = SUM + ACC2 | | |
| | t3 | XREAD(ACC3) |
| | | ACC3 = ACC3 – 10 |
| | | XWRITE(ACC3) |
| | t4 | SREAD(ACC1) |
| | t5 | XWRITE(ACC1) |
| SREAD(ACC3) | t6 | |
| | t7 | |

- Bloqueo Compartido (Protocolo PS)

¿Qué pasa aquí?

| T1 | Tiempo | T2 |
|---|---|---|
| SREAD(ACC1) | t1 | |
| SUM = SUM + ACC1 | | |
| SREAD(ACC2) | t2 | |
| SUM = SUM + ACC2 | | |
| | t3 | XREAD(ACC3) |
| | | ACC3 = ACC3 – 10 |
| | | XWRITE(ACC3) |
| | t4 | SREAD(ACC1) |
| | t5 | XWRITE(ACC1) |
| | | wait |
| SREAD(ACC3) | t6 | wait |
| wait | | |
| wait | t7 | wait |

- Bloqueo Actualización (Protocolo PU)

**Figura:** Diagrama con los siguientes componentes y flujo:

- **Memoria Principal (compartida):** recuadro grande a la izquierda con filas horizontales. Una fila superior contiene una barra naranja dividida en cinco segmentos verticales. Una fila inferior contiene una barra naranja etiquetada **B**.
- **Área de trabajo $T_i$:** recuadro pequeño en la parte superior derecha que contiene un círculo etiquetado **$R_i$**.
- Flecha azul desde un segmento de la memoria principal hacia el círculo **$R_i$**.
- **Concurrence Manager:** recuadro con doble borde en la parte inferior central.
- Texto **$T_i$: UREAD(R)** con flecha azul apuntando hacia el **Concurrence Manager**.
- Flecha azul desde el segmento resaltado en la **Memoria Principal** hacia el **Concurrence Manager**.

- Bloqueo Actualización (Protocolo PU)

**Figura:** Diagrama con los siguientes componentes y flujo:

- **Memoria Principal (compartida):** recuadro grande a la izquierda. Una fila superior contiene una barra naranja dividida en cuatro segmentos. Una fila inferior contiene una barra naranja etiquetada **B**.
- **Área de trabajo $T_i$:** recuadro superior a la derecha con un círculo con borde verde etiquetado **$R_i$**. Flecha desde un segmento en memoria hacia **$R_i$**.
- **Área de trabajo $T_s$:** recuadro inferior a la derecha con un círculo con borde verde etiquetado **$R_s$**. Flecha desde el mismo segmento en memoria hacia **$R_s$**.
- **Concurrence Manager:** recuadro con doble borde en la parte inferior central.
- Dos solicitudes apuntan al manager:
  - **$T_i$: UREAD(R)**
  - **$T_s$: SREAD(R)**
- Flecha desde el **Concurrence Manager** hacia el segmento en la **Memoria Principal**.

- Bloqueo Actualización (Protocolo PU)

**Figura:** Diagrama con los siguientes componentes y flujo:

- **Memoria Principal (compartida):** recuadro grande a la izquierda. Una fila superior contiene una barra naranja dividida en cuatro segmentos, con flechas hacia las áreas de trabajo. Una fila inferior contiene una barra naranja etiquetada **B**.
- **Área de trabajo $T_i$:** recuadro superior a la derecha con un círculo etiquetado **$R_i$**. Operación: **$T_i$: UREAD(R)**.
- **Área de trabajo $T_s$:** recuadro inferior a la derecha con un círculo etiquetado **$R_s$**. Flecha desde **$R_s$** de vuelta al segmento en memoria. Operación: **$T_s$: SREAD(R)**.
- **Concurrence Manager:** recuadro con doble borde en la parte inferior central, con flecha hacia el segmento activo en memoria.
- **Cola de espera de bloqueo de actualización:** a la izquierda del manager, línea horizontal etiquetada **$T_o, \dots, T_q$** con el texto **Cola de espera de bloqueo de actualización**.
- **Cola de espera de bloqueo exclusivo:** a la derecha del manager, línea horizontal etiquetada **$T_j, \dots, T_n$** con el texto **Cola de espera de bloqueo exclusivo**.

- Bloqueo Actualización (Protocolo PU)

| T1 | Tiempo | T2 |
|---|---|---|
| SREAD(R) | t1 | |
| COPY R.F INTO ATEMP | | |
| | t2 | SREAD(R) |
| | | COPY R.F INTO BTEMP |
| XWRITE(R) | t3 | |
| wait | | |
| wait | t4 | XWRITE(R) |
| | | wait |
| wait | t5 | wait |

**Figura:** En la parte inferior, un recuadro con borde azul redondeado etiquetado **Interbloqueo (deadlock)**. Dos flechas azules parten de este recuadro:

- Una flecha apunta hacia la operación **XWRITE(R) / wait** de **T1** en **t3**.
- Otra flecha apunta hacia la operación **XWRITE(R) / wait** de **T2** en **t4**.

- Bloqueo Actualización (Protocolo PU)

| T1 | Tiempo | T2 |
|---|---|---|
| UREAD(R) | t1 | |
| COPY R.F INTO ATEMP | | |
| | t2 | UREAD(R) |
| | | wait |
| UWRITE(R) | t3 | |
| REPLACE R.F BY ATEMP + 1 | | wait |
| COMMIT | t4 | reinicia |
| | | COPY R.F INTO BTEMP |
| | t5 | UWRITE(R) |
| | | REPLACE R.F BY BTEMP + 1 |
| | t5 | COMMIT |

- Algoritmo para bloqueo exclusivo:

```
Datos: Un elemento X de la base de datos.
Resultado: Actualización de la variable BLOCK(X).

B: if BLOCK(X) = 0 then
       BLOCK(X) ← 2;
   else
       wait(until BLOCK(X) = 0 and DBMS wakes up the transaction);
       go to B;
   end
```

- Algoritmo para bloqueo compartido:

```
Datos: Un elemento X de la base de datos.
Resultado: Actualización de la variable BLOCK(X).

B: if BLOCK(X) = 0 then
     BLOCK(X) ← 1;
     num_read ← 1;
   else
     if BLOCK(X) = 1 then
       num_read ← num_read + 1;
     else
       wait(until BLOCK(X) = 0 and DBMS wakes up the transaction);
       go to B;
     end
   end
```

**Figura:** A la derecha del algoritmo, un recuadro con borde naranja contiene la pregunta: «¿Cómo modificamos este algoritmo para incluir el caso de bloqueo con protocolo PU?»

- Algoritmo de desbloqueo:

```
Datos: Un elemento X de la base de datos.
Resultado: Actualización de la variable BLOCK(X).

B: if BLOCK(X) = 2 then
     BLOCK(X) ← 0;
     Wake up the waiting transactions;
   else
     if BLOCK(X) = 1 then
       num_read = num_read - 1;
       if num_read = 0 then
         BLOCK(X) ← 0;
         Wake up the waiting transactions;
       end
     end
   end
```

**Figura:** A la derecha del algoritmo, un recuadro con borde naranja contiene la pregunta: «¿Cómo modificamos este algoritmo para incluir el caso de desbloqueo con protocolo PU?»

**Figura:** En el centro de la slide, un recuadro con fondo rosa claro y borde discontinuo rojo contiene el siguiente texto:

> El problema de las técnicas de bloqueo es que puede producirse un interbloqueo o bloqueo mortal.
>
> Esto es cuando dos o más transacciones están esperando cada una de ellas que la otra libere algún objeto antes de seguir.

(slides 42–63)

### Interbloqueos

- Se dice que un sistema esta en estado de interbloqueo si para cada transacción $T_i$ en un conjunto de dos o más transacciones, espera por la liberación de un recurso que esta bloqueado por alguna otra transacción $T_j$ ($i \neq j$).

- Los interbloqueos pueden ser **prevenidos** o **detectados**.

**Figura:** En la parte inferior, un grafo de espera cíclico etiquetado «Grafo de espera cíclico (interbloqueo)». Tres nodos circulares representan transacciones: **T1** (abajo a la izquierda), **T2** (arriba al centro) y **T3** (abajo a la derecha). Flechas azules indican dependencias de espera formando un ciclo:

- Flecha de **T1** hacia **T2**. Cerca de **T1** aparecen las etiquetas **PX(X)** y **PX(Z)**; cerca de **T2** aparece **PX(X)**.
- Flecha de **T2** hacia **T3**. Cerca de **T2** aparece **PX(Y)**; cerca de **T3** aparece **PX(Y)**.
- Flecha de **T3** de vuelta hacia **T1**. Cerca de **T3** aparece **PX(Z)**.

La estructura circular indica que **T1** espera un recurso bloqueado por **T2**, **T2** espera un recurso bloqueado por **T3**, y **T3** espera un recurso bloqueado por **T1**.

(slide 65)

### Prevención de Interbloqueos

- Planificación de transacciones.

- Rechazo de requerimientos

- Retroceso de la transacción (rollback)
  - Con marcas de tiempo
  - Sin marcas de tiempo

- Planificación de transacciones.
  - Se asegura que dos transacciones no serán ejecutadas concurrentemente si sus requerimientos de datos están en conflicto (interbloqueo).
  - Exige que cada transacción bloquee todos sus elementos de datos en un paso (de manera atómica), antes de su ejecución. Esto conlleva a dos inconvenientes principales:
    - Es difícil predecir antes que comience la transacción cuales elementos de datos deben bloquearse.
    - La utilización de elementos puede ser muy baja, ya que muchos pueden estar bloqueados pero sin usar.

- Rechazo de requerimientos
  - Implica rechazar cualquier requerimiento de bloqueo, si al ser aceptado genera interbloqueo.
  - Se implementa un grafo de espera, si un requerimiento produce un ciclo, este requerimiento se descarta y se retrocede la transacción que lo generó total o parcialmente.

**Figura:** Grafo de espera cíclico etiquetado «Grafo de espera cíclico (interbloqueo)». Tres nodos circulares: **T1** (abajo a la izquierda), **T2** (arriba al centro) y **T3** (abajo a la derecha).

- Flecha de **T1** hacia **T2**. Cerca de **T1**: **PX(X)**; cerca de **T2**: **PX(X)**.
- Flecha de **T2** hacia **T3**. Cerca de **T2**: **PX(Y)**; cerca de **T3**: **PX(Y)**.
- Flecha de **T3** hacia **T1** (esta arista está marcada con un círculo rojo con una X, indicando rechazo del requerimiento). Cerca de **T3**: **PX(Z)**; cerca de **T1**: **PX(Z)** (en rojo).

El símbolo de rechazo sobre la arista T3→T1 indica que el requerimiento que completaría el ciclo se descarta para prevenir el interbloqueo.

- Retroceso de transacciones.
  - Esta técnica requiere que alguna de las transacciones implicadas en un bloqueo deba hacer ROLLBACK y ser reiniciada. Existen dos enfoques:
    - Con marcas de tiempo
    - Sin marcas de tiempo

- Retroceso con marcas de tiempo.
  - Una marca de tiempo es un identificador unívoco creado por el SGBD para identificar el tiempo de inicio relativo de cada transacción.
  - Se pueden generar:
    - Mediante el uso del valor del reloj del sistema en el instante en que comienza la transacción.
    - O incrementando un contador lógico cada vez que comience una nueva transacción.
  - Si la transacción $T1$ comienza antes que la transacción $T2$, entonces $MT(T1) < MT(T2)$, donde $MT$ es la marca de tiempo de la transacción.

- Retroceso con marcas de tiempo.

**Figura:** En la parte superior derecha, un diagrama pequeño muestra dos transacciones en conflicto: **$T_i$** y **$T_j$**, cada una con un bloque etiquetado **$XW(X)$** debajo, representando que ambas intentan adquirir un bloqueo exclusivo de escritura sobre el mismo elemento $X$.

- Supongamos que $T_i$ intenta bloquear un elemento $X$ que ya está bloqueado por $T_j$ con un bloqueo en conflicto:

1. **Esperar-Morir (Wait-Die)**
   - Si $MT(T_i) < MT(T_j)$ ($T_i$ es más antigua que $T_j$), entonces $T_i$ puede esperar.
   - En caso contrario ($T_i$ es más reciente que $T_j$) $T_i$ se aborta ($T_i$ muere) y se reinicia posteriormente con la misma marca de tiempo.

2. **Herir-Esperar (Wound-Wait)**
   - Si $MT(T_i) < MT(T_j)$, se aborta $T_j$ ($T_i$ hiere a $T_j$) y se reinicia posteriormente con la misma marca de tiempo.
   - En caso contrario ($T_i$ es más reciente que $T_j$), $T_i$ puede esperar.

- Retroceso sin marcas de tiempo.
  - **No-espera (No-wait):** Si una transacción no puede obtener un bloqueo, no espera. En su lugar, reinicia tras un cierto tiempo sin comprobar si realmente se ha producido un interbloqueo.
  - **Espera-cautelosa (Cautious-wait):** Se desarrolló debido a los retrocesos innecesarios del esquema No-espera. El protocolo sigue estas reglas cuando una transacción $T_i$ solicita un recurso $X$ que está bloqueado por otra transacción $T_j$:
    - Si $T_j$ está en espera entonces $T_i$ retrocede.
    - Caso contrario, $T_i$ espera.

- http://www.mathcs.emory.edu/~cheung/Courses/554/Syllabus/8-recv+serial/deadlock-compare.html
- https://www.tutorialspoint.com/dbms/dbms_deadlock.htm

(slides 66–72)

## Database Recovery

### Acceso a datos por una transacción

**Figura:** Diagrama con tres componentes principales:

- **Memoria Secundaria** (cilindro en la parte inferior): contiene dos bloques de datos etiquetados **A** y **B**.
- **Memoria Principal** (recuadro grande en el centro): contiene dos filas horizontales con barras naranjas divididas en segmentos, representando buffers en memoria.
- **Área de trabajo $T_i$** (recuadro vacío a la derecha): espacio de trabajo privado de la transacción $T_i$.

Flujo de datos:

- Flecha **Input(A)** desde el bloque **A** en Memoria Secundaria hacia un buffer en Memoria Principal (lectura desde disco).
- Flecha **Output(B)** desde un buffer en Memoria Principal hacia el bloque **B** en Memoria Secundaria (escritura a disco).

**Figura:** Diagrama con los mismos tres componentes de la slide anterior, ampliado con el flujo de una transacción sobre un dato $X$:

- **Memoria Secundaria** (cilindro inferior): bloques **A** y **B**. Flecha **Input(A)** desde **A** hacia Memoria Principal; flecha **Output(B)** desde Memoria Principal hacia **B**.
- **Memoria Principal** (recuadro central): buffers representados como barras naranjas. Un slot en la fila superior está conectado bidireccionalmente con la variable $X_i$ en el área de trabajo.
- **Área de trabajo $T_i$** (recuadro derecho): contiene un círculo etiquetado **$X_i$**, copia local del dato.
- Flecha **READ(X)** desde el slot $X$ en Memoria Principal hacia **$X_i$** en el área de trabajo.
- Flecha **WRITE(X)** desde **$X_i$** de vuelta al slot $X$ en Memoria Principal.

Recuadro azul con dos viñetas:

- La salida a disco de X no es inmediato.
- Depende de la política de sustitución de memoria principal: RANDOM, FIFO, LIFO, etc.

Recuadro rojo con la pregunta:

- ¿Qué pasa si se cae el sistema antes que se copie X a disco?
- Database Recovery

(slides 74–75)

### DB Recovery

- En un sistema gestor de base de datos, restaurar la BD significa:
  - Re-almacenar la base de datos en un estado correcto, lo más reciente posible, si la falla ha hecho que la BD quede en un estado incorrecto.
  - Implica redundancia (almacenar los estados correctos) de manera que la BD pueda ser reconstruida con estos.

- Tipo de fallas en un SGBD:

| Fallas locales a la transacción | Fallas en el sistema | Fallas en los medio de almacenamiento |
|---|---|---|
| a) Son detectados por el código de la aplicación y son manejados por este. Ej. Condición de fondos insuficiente en la transferencia. | • Afectan a todas las transacciones que se están realizando en ese momento, pero no daña la BD (física). Ej. Falla del CPU, falla eléctrico, falla del software. | • Dañan en la BD o una porción de esta y afectan a todas las transacciones que estaban usando esa porción en el momento de la falla. Ej. Cabeza lectora que raya el disco. |
| b) No son explícitamente manejadas por el código de aplicación. Ej. Overflow aritmético. | | |

(slides 76–77)

### Recuperación basado en Log

- Registro de Log:
  - Es una secuencia de eventos que documentan cada operación crítica (INSERT, UPDATE, DELETE).
- Estrategias de modificación
  - Modificación diferida
  - Modificación inmediata
- Proceso de recuperación con Log
  - Tres pasadas y Dos pasadas
  - Basado en Checkpoints

**Figura:** Diagrama de **Write-Ahead Logging (WAL)** a la derecha. Un recuadro central etiquetado **DBMS** contiene dos componentes internos:

- **DB buffer (cache):** conectado por flecha al **Permanent database** (icono de disco).
- **Log buffer:** con flechas hacia tres destinos de almacenamiento:
  1. **Log file** (icono de disco)
  2. **Archive log** (icono de disco)
  3. **Archive copy (dump)** (icono de disco)

Debajo del diagrama: **Log = Registro histórico**

- Estructura de los registros de Log
  - Inicio de la transacción $T_i$: $\langle T_i, BT \rangle$
  - Fin de la transacción $T_i$: $\langle T_i, ET \rangle$ o $\langle T_i, Commit \rangle$ culminación exitosa o $\langle T_i, Abort \rangle$ culminación fallida.
  - Cambios en los registros de la BD: $\langle T_i, X, IA, ID \rangle$

**Figura:** Recuadro azul en la parte inferior con las definiciones de las variables:

- $T_i$: Identificador de la transacción
- $IA$: Imagen o estado antes de la modificación.
- $ID$: imagen o estado después de la modificación.

**Figura:** Diagrama completo del flujo de datos y logging entre memoria, área de trabajo y almacenamiento:

- **Memoria Principal** (recuadro grande superior): grid con barras naranjas representando buffers.
  - Flecha **Input(A)** desde Memoria Secundaria hacia un slot en Memoria Principal.
  - Flecha **Output(B)** desde un slot en Memoria Principal hacia Memoria Secundaria.
- **Área de trabajo $T_i$** (recuadro a la derecha): contiene un círculo etiquetado **$X_i$**.
  - Flecha **READ(X)** desde el slot $X$ en Memoria Principal hacia **$X_i$**.
  - Flecha **WRITE(X)** desde **$X_i$** de vuelta al slot $X$ en Memoria Principal.
- **Buffer del Log** (barra naranja horizontal en Memoria Principal): contiene registros pendientes **R1, R2,**.
- **Memoria Secundaria** (cilindro inferior izquierdo): bloques **A** y **B**.
- **Log** (cilindro inferior derecho): etiquetado «Log heap, mucho mas rápido», representando el archivo de log persistente en disco, más rápido que escrituras aleatorias a la base de datos.

**Figura:** Diagrama de arquitectura de recuperación basada en log con los siguientes componentes y flujos:

- **Memoria Principal:** recuadro grande en la parte superior con una cuadrícula de celdas. Una celda específica está etiquetada **$X$**.
- **Área de trabajo $T_i$:** recuadro a la derecha de la Memoria Principal que contiene una copia local del dato etiquetada **$X_i$**.
- **READ($X$):** flecha desde la celda **$X$** en Memoria Principal hacia **$X_i$** en el Área de trabajo.
- **WRITE($X$):** flecha desde **$X_i$** de vuelta hacia la celda **$X$** en Memoria Principal.
- **Escribir_reg_log($R_n$):** flecha que indica la acción de escribir un registro de log a partir de la actividad de la transacción.
- **Buffer del Log:** recuadro naranja horizontal que contiene el texto **R1, R2, (Ti, X, IA, ID)**, representando registros de log temporales en memoria.
- **Output(C):** flecha desde el Buffer del Log hacia el **Log** en disco.
- **Memoria Secundaria:** cilindro naranja en la parte inferior izquierda que contiene dos bloques etiquetados **A** y **B**.
- **Input(A):** flecha desde el bloque **A** en Memoria Secundaria hacia la Memoria Principal.
- **Output(B):** flecha desde la Memoria Principal hacia el bloque **B** en Memoria Secundaria.
- **Log:** cilindro naranja en la parte inferior derecha que contiene un bloque etiquetado **C**. Junto al cilindro aparece la nota: *heap, mucho mas rápido*.

**Figura:** Dos pares de recuadros alineados horizontalmente, cada uno con una etiqueta a la izquierda y su definición a la derecha:

- **Deshacer transacción:** recuadro azul redondeado a la izquierda. Definición en recuadro gris claro a la derecha: *Acción de colocar las imágenes antes (estado anterior) de los registros modificados por una transacción.*
- **Rehacer transacción:** recuadro gris oscuro redondeado a la izquierda. Definición en recuadro gris claro a la derecha: *Acción de escribir la imagen después (estado posterior) de los registros modificados por una transacción.*

(slides 78–82)

### Estrategias de modificación

- Modificación inmediata:
  - Permite las operaciones WRITE de una transacción mientras ésta está activa (modificación no comprometidas)
  - Si el sistema falla se debe usar los valores del Log para restaurar los elementos de datos de los valores anteriores a la transacción.
  - En el Log
    - Los registros de actualización son de la forma `<Ti, X, IA, ID>`
    - Se realizan los cambios en el Log antes de la actualización real a la BD.

- Modificación diferida:
  - Retarda las operaciones WRITE de una transacción hasta que se compromete parcialmente.
  - Si el sistema falla antes de que la transacción se complete, se ignora en el proceso de recuperación.
  - En el Log no se registra las imágenes antes, por lo que:
    - Los registros de actualización son de la forma `<Ti, X, ID>`
    - No se deshace.

(slides 83–84)

### Proceso de recuperación

- Tres pasadas:

**Figura:** Diagrama con dos componentes principales: una línea de tiempo de transacciones en la parte superior y una secuencia de entradas del LOG en la parte inferior.

**Línea de tiempo (parte superior):** eje horizontal de tiempo con eje vertical de transacciones. Cinco transacciones representadas como barras horizontales:

- **$t_1$:** comienza primero y termina (commit) temprano.
- **$t_2$:** comienza después de $t_1$, termina (commit) antes de la falla.
- **$t_3$:** comienza después de que $t_2$ inicia; su barra continúa más allá de la línea de falla (activa/no confirmada).
- **$t_4$:** comienza después de que $t_3$ inicia; termina (commit) justo antes de la falla.
- **$t_5$:** comienza después de que $t_4$ termina; su barra continúa más allá de la línea de falla (activa/no confirmada).
- **$t_f$ (falla el sistema):** línea vertical ondulada en el extremo derecho que marca el momento de la falla.

**LOG (parte inferior):** secuencia horizontal de 16 registros de log, de izquierda a derecha:

1. `T1, BT`
2. `T1, X, A1, D1`
3. `T2, BT`
4. `T2, Y, A2, D2`
5. `T1, Z, A1, D1`
6. `T1, COM` — flecha hacia el final de la barra $t_1$
7. `T3, BT`
8. `T2, X, A2, D2`
9. `T3, Z, A3, D3`
10. `T4, BT`
11. `T4, W, A4, D4`
12. `T2, COM` — flecha hacia el final de la barra $t_2$
13. `T5, BT`
14. `T4, X, A4, D4`
15. `T4, COM` — flecha hacia el final de la barra $t_4$
16. `T5, W, A5, D5`

Debajo del log: flecha **REDO** apuntando hacia la derecha (inicio del log) y flecha **UNDO** apuntando hacia la izquierda (final del log).

- Tres pasadas:

**Figura:** Secuencia horizontal de 16 registros de log (misma secuencia que en la slide 85). Debajo del log: flecha **REDO** apuntando hacia la derecha al inicio del log y flecha **UNDO** apuntando hacia la izquierda al final del log. El registro `T2, COM` (posición 12) está **circulado en naranja**, con una flecha naranja que apunta desde el texto de la slide hacia ese círculo.

- Se recorre el log del fin al inicio para crear dos listas
  - REDO para transacciones terminadas

- Tres pasadas:

**Figura:** Secuencia horizontal de 16 registros de log (misma secuencia que en la slide 85). Debajo del log: flecha **REDO** apuntando hacia la derecha y flecha **UNDO** apuntando hacia la izquierda. El registro `T3, Z, A3, D3` (posición 9) está **circulado en rojo**, con una flecha roja que apunta desde el texto de la slide hacia ese círculo.

- Se recorre el log del fin al inicio para crear dos listas
  - REDO para transacciones terminadas
  - UNDO para transacciones no terminadas

- Tres pasadas:

**Figura:** Secuencia horizontal de 16 registros de log (misma secuencia que en la slide 85), terminando en una línea vertical ondulada a la derecha que indica la falla del sistema. Debajo del log: flecha **REDO** apuntando hacia la derecha (inicio a fin) y flecha **UNDO** apuntando hacia la izquierda (fin a inicio).

- Se recorre el log del fin al inicio para crear dos listas
  - REDO para transacciones terminadas
  - UNDO para transacciones no terminadas
- Se recorre el log de inicio a fin para Rehacer las transacciones en REDO
- Se recorre el log de fin a inicio para Deshacer las transacciones en UNDO.

- Tres pasadas:

**Figura:** Secuencia horizontal de 16 registros de log (misma secuencia que en la slide 85). Debajo del log: flecha **REDO** apuntando hacia la derecha y flecha **UNDO** apuntando hacia la izquierda. A la derecha del diagrama, un recuadro azul contiene la nota: *En modificación diferida las transacciones en UNDO solo se procede a anularlas, ya que ninguna de sus operaciones de escritura afectaron a la base de datos*.

- Se recorre el log del fin al inicio para crear dos listas
  - REDO para transacciones terminadas
  - UNDO para transacciones no terminadas
- Se recorre el log de inicio a fin para Rehacer las transacciones en REDO
- Se recorre el log de fin a inicio para Deshacer las transacciones en UNDO.

- Dos pasadas

**Figura:** Secuencia horizontal de 16 registros de log (misma secuencia que en la slide 85), terminando en una línea vertical ondulada a la derecha que indica la falla del sistema. Debajo del log: flecha **REDO** apuntando hacia la derecha y flecha **UNDO** apuntando hacia la izquierda. En la parte inferior, un recuadro con borde rojo punteado contiene la nota: *El Log puede llegar a tener muchos registros para Rehacer. Muchas de estas transacciones para rehacer ya están en la BD*.

- Se recorre el log del fin al inicio para :
  - Crear lista REDO
  - Deshacer las transacciones no terminadas
- Se recorre el log de inicio a fin para Rehacer las transacciones en REDO

- Problemas:
  - Cuando se realiza el proceso de restauración
    - Recorrer el Log consume tiempo
    - La mayoría de las transacciones a Rehacer (de acuerdo al algoritmo) ya tienen sus actualizaciones escritas en la BD.
  - ¿Cómo hacer para no recorrer el log completo?

(slides 85–91)

### Proceso de recuperación con checkpoints

- Algunos papers

✓ Fukumoto, S., Kaio, N., & Osaki, S. (1992). A study of checkpoint generations for a database recovery mechanism. Computers & Mathematics with applications, 24(1-2), 63-70.

✓ Gray, J., McJones, P. R., Blasgen, M. W., Lindsay, B. G., Lorie, R. A., Price, T. G., ... & Traiger, I. L. (1981). The recovery manager of the System R database manager. ACM Computing surveys, 13(2), 223-242.

✓ Haerder, T., & Reuter, A. (1983). Principles of transaction-oriented database recovery. ACM computing surveys (CSUR), 15(4), 287-317.

**Figura:** Diagrama de arquitectura de checkpoint con los siguientes componentes:

- **Memoria Compartida:** recuadro grande con cuadrícula de celdas. Una celda contiene el dato **$X$**.
- **Área de trabajo $T_i$:** recuadro a la derecha que contiene una copia local **$X_i$**.
- **READ($X$):** flecha desde **$X$** en Memoria Compartida hacia **$X_i$**.
- **WRITE($X$):** flecha desde **$X_i$** de vuelta hacia **$X$** en Memoria Compartida.
- **Buffer del Log:** recuadro naranja horizontal que contiene la entrada **$(T_i, X, IA, ID)$**.
- **Memoria Secundaria:** cilindro naranja en la parte inferior izquierda con bloques **A** y **B**.
- **Log:** cilindro naranja en la parte inferior derecha con bloque **C**.
- A la derecha del diagrama, texto grande: **Proceso de chekpoint**.

**Figura:** Diagrama de arquitectura de checkpoint — **Paso 1**, con los siguientes componentes:

- **Memoria Compartida:** recuadro con cuadrícula; celda etiquetada **$X$**.
- **Área de trabajo $T_i$:** recuadro con copia local **$X_i$**.
- **READ($X$):** flecha desde **$X$** hacia **$X_i$**.
- **WRITE($X$):** flecha desde **$X_i$** hacia **$X$**, **tachada con una X roja** (operación bloqueada). Hexágono azul con el número **1** debajo de la operación WRITE.
- **Buffer del Log:** recuadro naranja con entrada **$(T_i, X, IA, ID)$**.
- **Memoria Secundaria:** cilindro con bloques **A** y **B**.
- **Log:** cilindro con bloque **C**.
- Recuadro azul a la derecha con el número **1** y el texto: *Se impide que las transacciones realicen actualizaciones.*

**Figura:** Diagrama de arquitectura de checkpoint — **Paso 2**, con los siguientes componentes:

- **Memoria Compartida:** recuadro con cuadrícula; celda etiquetada **$X$**.
- **Área de trabajo $T_i$:** recuadro con copia local **$X_i$**.
- **READ($X$):** flecha desde **$X$** hacia **$X_i$**.
- **WRITE($X$):** flecha tachada con X roja (operación bloqueada). Hexágono azul con el número **1** debajo.
- **Buffer del Log:** recuadro naranja con dos entradas:
  1. **$(T_i, X, IA, ID)$**
  2. **$(CP, L)$** — hexágono azul con el número **2** junto a esta entrada.
- **Memoria Secundaria:** cilindro con bloques **A** y **B**.
- **Log:** cilindro con bloque **C**.
- Recuadro azul a la derecha con el número **2** y el texto: *Se crea un registro en el Log con la lista de transacciones activas al momento del Check Point.*

**Figura:** Diagrama de arquitectura de checkpoint — **Paso 3**, con los siguientes componentes:

- **Memoria Compartida:** recuadro con cuadrícula; celda etiquetada **$X$**.
- **Área de trabajo $T_i$:** recuadro con copia local **$X_i$**.
- **READ($X$):** flecha desde **$X$** hacia **$X_i$**.
- **WRITE($X$):** flecha tachada con X roja. Hexágono azul con el número **1** debajo.
- **Buffer del Log:** recuadro naranja horizontal. Hexágono azul con el número **2** encima del buffer.
- **Output(A):** flecha desde Memoria Compartida hacia bloque **A** en Memoria Secundaria.
- **Output(B):** flecha desde Memoria Compartida hacia bloque **B** en Memoria Secundaria.
- **Output(C):** flecha desde Buffer del Log hacia bloque **C** en el Log.
- **Memoria Secundaria:** cilindro con bloques **A** y **B**.
- **Log:** cilindro con bloque **C**. Hexágono azul con el número **3** entre los dos cilindros.
- Recuadro azul a la derecha con el número **3** y el texto: *Se fuerza la salida de los buffers de datos y del Log.*

**Figura:** Diagrama de arquitectura de checkpoint — **Paso 4**, con los siguientes componentes:

- **Memoria Compartida:** recuadro con cuadrícula; celda etiquetada **$X$**.
- **Área de trabajo $T_i$:** recuadro con copia local **$X_i$**.
- **READ($X$):** flecha desde **$X$** hacia **$X_i$**.
- **WRITE($X$):** flecha tachada con X roja. Hexágono azul con el número **1** debajo.
- **Buffer del Log:** recuadro naranja horizontal. Hexágono azul con el número **2** encima.
- **Output(A):** flecha hacia bloque **A** en Memoria Secundaria.
- **Output(B):** flecha hacia bloque **B** en Memoria Secundaria.
- **Output(C):** flecha hacia bloque **C** en el Log. Hexágono azul con el número **3** junto a esta flecha.
- **Memoria Secundaria:** cilindro con bloques **A** y **B**.
- **Log:** cilindro con bloque **C**.
- **Archivo de recomienzo:** icono de documento a la derecha del Log con una lista de entradas.
- Flecha etiquetada **\*CP** desde el Log hacia el Archivo de recomienzo. Hexágono azul con el número **4** junto a esta flecha.
- Recuadro azul a la derecha con el número **4** y el texto: *Se actualiza el puntero del CP del Log en el archivo de recomienzo.*

- Proceso de recuperación ante una falla

**Figura:** Diagrama de flujo con cinco recuadros naranjas numerados conectados por flechas azules:

1. **Paso 1:** *Se obtiene en el archivo de recomienzo la direccion del ultimo CP en el Log.*
2. **Paso 2:** *Se crean dos listas UNDO = L, REDO = [ ]*
3. **Paso 3:** *Se recorre el Log desde el CP al final y se completan las listas.*
4. **Paso 4:** *Se recorre el Log desde el final hasta el inicio de c/u de las transacciones en UNDO para deshacer.*
5. **Paso 5:** *Se recorre el Log desde el CP hasta el final para rehacer.*

Flujo de flechas: **1 → 2 → 3 → 4 → 5** (desde el paso 3 baja al paso 4, y desde el paso 4 va hacia la izquierda al paso 5).

- Proceso de recuperación ante una falla

**Figura:** Diagrama de flujo con recuadros naranjas numerados conectados por flechas azules:

1. **Paso 1:** *Se obtiene en el archivo de recomienzo la direccion del ultimo CP en el Log.*
2. **Paso 2:** *Se crean dos listas UNDO = L, REDO = [ ]*
3. **Paso 3:** *Se recorre el Log desde el CP al final y se completan las listas.*
4. **Recuadro azul (sin número):** *En modificación diferida las transacciones en UNDO solo se procede a anularlas.*
5. **Paso 5:** *Se recorre el Log desde el CP hasta el final para rehacer.*

Flujo de flechas: **1 → 2 → 3 → (recuadro azul) → 5**. No hay recuadro numerado **4**.

- Ejemplo de recuperación:

**Figura:** Diagrama de línea de tiempo horizontal orientada de izquierda a derecha. Dos líneas verticales marcan eventos clave: la primera, etiquetada **CP** (Checkpoint), situada aproximadamente en el tercio central de la línea; la segunda, etiquetada **Falla del sistema**, situada en el extremo derecho. Cinco transacciones se representan como barras horizontales paralelas, de arriba hacia abajo:

- **T1:** barra que comienza y termina completamente antes de la línea **CP**.
- **T2:** barra que comienza después de **CP** y termina antes de la línea **Falla del sistema**.
- **T3:** barra que comienza antes de **CP** y termina antes de **Falla del sistema**.
- **T4:** barra que comienza antes de **CP** y se extiende hasta la línea **Falla del sistema** (sigue activa en el momento de la falla).
- **T5:** barra que comienza después de **CP** y se extiende hasta la línea **Falla del sistema** (sigue activa en el momento de la falla).

- Ejemplo de recuperación:

**Figura:** Diagrama de línea de tiempo horizontal orientada de izquierda a derecha, con la etiqueta implícita de flujo temporal. Dos líneas verticales marcan eventos clave: la primera, etiquetada **CP** (Checkpoint), situada aproximadamente en el tercio central de la línea; la segunda, etiquetada **Falla del sistema**, situada en el extremo derecho. Cinco transacciones se representan como barras horizontales paralelas, de arriba hacia abajo:

- **T1:** barra que comienza y termina completamente antes de la línea **CP** (transacción finalizada antes del checkpoint).
- **T2:** barra que comienza después de **CP** y termina antes de la línea **Falla del sistema**.
- **T3:** barra que comienza antes de **CP** y termina antes de **Falla del sistema**.
- **T4:** barra que comienza antes de **CP** y se extiende hasta la línea **Falla del sistema** (sigue activa en el momento de la falla).
- **T5:** barra que comienza después de **CP** y se extiende hasta la línea **Falla del sistema** (sigue activa en el momento de la falla).

Debajo del diagrama, cinco recuadros numerados describen el proceso de recuperación:

1. `(CP, [T3, T4])` — En el checkpoint, las transacciones activas eran **T3** y **T4**.
2. `UNDO= [T3, T4]` / `REDO=[ ]` — Listas iniciales a partir de la información del checkpoint.
3. `UNDO= [~~T3~~, T4, T5]` / `REDO=[T2, T3]` — Tras escanear el log hacia adelante desde el checkpoint: **T2** y **T3** finalizaron con éxito antes de la falla, por lo que se añaden a **REDO**; **T3** se elimina de la lista **UNDO** (aparece tachado en rojo); **T5** inició pero no finalizó, por lo que se añade a **UNDO**.
4. `Deshacer UNDO` — Ejecutar las operaciones de deshacer para las transacciones en la lista UNDO (**T4** y **T5**).
5. `Rehacer REDO` — Ejecutar las operaciones de rehacer para las transacciones en la lista REDO (**T2** y **T3**).

A la derecha, en un recuadro con borde azul, aparece la nota: *No es necesario hacer REDO a T1 pues esto ocurrió antes del último checkpoint*.

(slides 92–101)

### Ejercicio de recuperación

**Figura:** Diagrama de línea de tiempo horizontal con la etiqueta **tiempo** en el extremo izquierdo. Dos líneas verticales marcan eventos: **Checkpoint** (línea vertical azul, aproximadamente en el centro de la línea) y **Falla del sistema** (línea vertical roja, en el extremo derecho). Cinco transacciones se representan como barras horizontales:

- **T1:** comienza y realiza **commit** completamente antes del Checkpoint.
- **T2:** comienza después de T1 y realiza **abort** completamente antes del Checkpoint.
- **T3:** comienza antes del Checkpoint y permanece activa a través del Checkpoint hasta la Falla del sistema.
- **T4:** comienza después del Checkpoint y realiza **commit** antes de la Falla del sistema.
- **T5:** comienza después del inicio de T4 y permanece activa cuando ocurre la Falla del sistema.

Debajo del diagrama, cinco recuadros numerados describen el proceso de recuperación:

1. `(CP, [T3])` — En el Checkpoint, la única transacción activa era **T3**.
2. `UNDO= [T3]` / `REDO=[ ]` — Estado inicial de las listas tras analizar el checkpoint.
3. `UNDO= [T3, T5]` / `REDO=[T4]` — Clasificación final tras analizar el log hasta la falla: **UNDO** incluye **T3** y **T5** (activas/no confirmadas al fallar); **REDO** incluye **T4** (confirmó después del último checkpoint y antes de la falla).
4. `Deshacer UNDO` — Deshacer las transacciones en la lista UNDO.
5. `Rehacer REDO` — Rehacer las transacciones en la lista REDO.

A la derecha, en un recuadro con borde azul, aparece la nota: *No es necesario hacer REDO a T1 pues esto ocurrió antes del último checkpoint*.

(slide 102)

### Recuperación en fallas de almacenamiento

- Backups
  - Copias de la BD completa o parcial hasta una fecha dada.
  - El Administrador de BD debe programar respaldos periódicos.
  - Para la recuperación se usa el respaldo y el Log para las actualizaciones posteriores.

- Replicación
  - Mantener una BD en otra localización o nodo, que se actualiza a la par de la original, como consecuencia:
    - Aumenta la disponibilidad de la BD en caso de fallas
    - Aumenta también los costos de almacenamiento y comunicación.

(slide 103)

### Componentes de un Sistema Administrador de Base de Datos

**Figura:** Diagrama arquitectónico de alto nivel titulado «Componentes de una Sistema Administrador de Base de Datos», organizado en tres capas horizontales apiladas de arriba hacia abajo:

**Capa superior — Procesador de Consultas** (etiqueta lateral izquierda «S M», recuadros verdes):

- **Consultas DML** (recuadro con borde punteado) alimenta al **Compilador del DML**.
- **Compilador del DML** se comunica con el **Motor de evaluación de consultas** y con el **Diccionario de datos** (en la capa de almacenamiento).
- **Interprete del DDL** procesa sentencias DDL y actualiza el **Diccionario de datos**.
- **Precompilador del DML** procesa sentencias DML embebidas en programas de aplicación; interactúa con **Código objeto de programas de aplicación**.
- **Código objeto de programas de aplicación** interactúa con el **Gestor de transacciones** (capa intermedia).
- **Motor de evaluación de consultas** es la unidad central de ejecución que coordina con los componentes del gestor de almacenamiento.

**Capa intermedia — Gestor de Almacenamiento** (etiqueta lateral izquierda «B D», recuadros morados):

- **Gestor de transacciones** gestiona la ejecución de transacciones (propiedades ACID); se conecta al **Gestor de memoria intermedia**.
- **Gestor de autorización e integridad** verifica permisos de usuario y restricciones de integridad.
- **Gestor de memoria intermedia** (Buffer Manager) trae datos del disco a memoria principal y decide qué datos cachear.
- **Gestor de archivos** administra la asignación de espacio en disco y las estructuras de datos que representan la información en disco.

**Capa inferior — Almacenamiento en disco** (cilindro rojo grande):

- Dentro del almacenamiento principal se encuentran: **Archivos de Datos**, **Índices**, **Datos estadísticos** y **Diccionario de datos**.
- A la izquierda del almacenamiento principal, un cilindro naranja separado etiquetado **Log** — registro persistente de todas las transacciones, fundamental para el proceso de recuperación.

Flechas y conexiones entre los componentes indican el flujo de datos y control entre las capas.

(slide 104)

## Glosario

| Término | Definición |
|---|---|
| Concurrencia | Coordinación de la ejecución simultánea de transacciones en un SGBD que soporta multiprocesamiento. |
| Transacción | Conjunto de operaciones de acceso a base de datos que conforman una unidad lógica de trabajo. |
| Atómica | Propiedad ACID: se realizan todas las acciones o no se realiza ninguna. |
| Consistente | Propiedad ACID: la base de datos satisfacen todas las restricciones después de una transacción. |
| Aislada | Propiedad ACID: una transacción no puede afectar otra aunque se ejecuten concurrentemente. |
| Durable | Propiedad ACID: una vez que hace COMMIT, la base de datos debe persistir los cambios. |
| Planificación | Orden cronológico en el que se ejecutan las instrucciones de transacciones en el sistema, conservando el orden dentro de cada transacción individual. |
| Planificación serializable | Planificación concurrente equivalente a una secuencial. |
| Precedencia | Relación $T_A \to T_B$ cuando $T_B$ lee un dato que $T_A$ modificó o $T_A$ lee un dato que $T_B$ modificará. |
| Seriabilidad | Proceso de determinar que una planificación concurrente es equivalente a una secuencial. |
| Conflicto | Dos instrucciones de distintas transacciones operan sobre el mismo elemento de datos y al menos una actualiza dicho dato. |
| Grafo de precedencia | Grafo dirigido $G = (N, A)$ donde cada transacción es un nodo y los arcos determinan precedencia por conflictos; si existe un ciclo, la planificación no es serializable. |
| Bloqueo | Técnica que regula el acceso concurrente a objetos compartidos (buffer de datos). |
| Bloqueo Exclusivo (Protocolo PX) | Protocolo de bloqueo exclusivo mediante operaciones XREAD, XWRITE y XRELEASE. |
| Bloqueo Compartido (Protocolo PS) | Protocolo de bloqueo compartido mediante operaciones SREAD. |
| Bloqueo Actualización (Protocolo PU) | Protocolo de bloqueo de actualización mediante operaciones UREAD y UWRITE. |
| Interbloqueo | Estado en el que cada transacción de un conjunto de dos o más espera por la liberación de un recurso bloqueado por otra transacción. |
| Marca de tiempo | Identificador unívoco creado por el SGBD para identificar el tiempo de inicio relativo de cada transacción. |
| Esperar-Morir (Wait-Die) | Si $MT(T_i) < MT(T_j)$, $T_i$ puede esperar; en caso contrario, $T_i$ se aborta y se reinicia con la misma marca de tiempo. |
| Herir-Esperar (Wound-Wait) | Si $MT(T_i) < MT(T_j)$, se aborta $T_j$; en caso contrario, $T_i$ puede esperar. |
| No-espera (No-wait) | Si una transacción no puede obtener un bloqueo, no espera; reinicia tras un cierto tiempo. |
| Espera-cautelosa (Cautious-wait) | Si $T_j$ está en espera entonces $T_i$ retrocede; caso contrario, $T_i$ espera. |
| Restaurar la BD | Re-almacenar la base de datos en un estado correcto, lo más reciente posible, si la falla ha hecho que la BD quede en un estado incorrecto. |
| Registro de Log | Secuencia de eventos que documentan cada operación crítica (INSERT, UPDATE, DELETE). |
| Deshacer transacción | Acción de colocar las imágenes antes (estado anterior) de los registros modificados por una transacción. |
| Rehacer transacción | Acción de escribir la imagen después (estado posterior) de los registros modificados por una transacción. |
| Modificación inmediata | Permite las operaciones WRITE de una transacción mientras ésta está activa; los registros de log son `<Ti, X, IA, ID>`. |
| Modificación diferida | Retarda las operaciones WRITE hasta que la transacción se compromete parcialmente; los registros de log son `<Ti, X, ID>` y no se deshace. |
| Checkpoint | Proceso que impide actualizaciones, registra transacciones activas en el log, fuerza la salida de buffers y actualiza el puntero del CP en el archivo de recomienzo. |
| Backup | Copia de la BD completa o parcial hasta una fecha dada. |
| Replicación | Mantener una BD en otra localización o nodo, actualizada a la par de la original. |
