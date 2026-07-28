---
curso: BD1
titulo: Clase 12 Transacciones y ACID
slides: 80
fuente: Clase 12 Transacciones y ACID.pdf
---

## Slide 1

Portada (decorativa: fondo azul futurista, logo UTEC, foto de persona con cámara/trípode silueteada, logo dcc Universidad de Chile). Título "TRANSACCIONES Y ACID". Curso CS2041 - Base de Datos I, Ciclo 2024-1. Autores: Teófilo Chambilla - tchambilla@utec.edu.pe, Brenner Ojeda - bojeda@utec.edu.pe. Colaboración de Aidan Hogan de la Universidad de Chile.

## Slide 2

Índice del capítulo (fondo gris oscuro, logo UTEC decorativo). Lista:
- Transacciones
- Garantías de ACID
- Implementación ACID (LOGGING)
- Implementación ACID (Secuenciabilidad)
- Bloqueos

## Slide 3

Slide de contexto curricular "CS2041 Bases de Datos I, Ciclo 2023-2". Diagrama de línea de tiempo del curso con bloques de progreso (barras azules) bajo los temas: Modelo Relacional, Algebra Relacional & Cálculo Relacional, SQL, Planificación y Optimización de Consultas, NO SQL/GRAFOS; y debajo Entidad-Relación, Actualización/Dependencias/Restricciones funcionales. Un recuadro azul resalta "Transacciones y ACID" como el tema actual, junto a un ícono de mago/ninja (mascota del curso) y una bandera de meta a la derecha indicando el final del recorrido.

## Slide 4

"Motivación". Cita de J. Gray y A. Reuter: "El concepto de transacción es el equivalente computacional de un contrato legal. Imagínese una sociedad sin ley de contratos. Eso es lo que sería un sistema computacional sin transacciones. Si nada nunca sale mal, los contratos son sólo un overhead. Pero si algo no funciona bien, el contrato especifica cómo limpiar la situación."

## Slide 5

"Una cuenta bancaria ...". Muestra 4 tablas de ejemplo de una base de datos bancaria:
- **Ingreso**: cuenta, comentario, fecha, hora, monto, saldo, id — 2 filas (Depósito inicial 300000/saldo 300000; C0°0°L Designs 50000/saldo 325000).
- **Gasto**: cuenta, comentario, fecha, hora, monto, saldo, id — 4 filas (Electricidad 8200/saldo 291800; Calefacción 600/saldo 291200; Moviestar 16200/saldo 275000; Cajero 100000/saldo 225000).
- **Cuenta**: número, rut, tipo, saldo_clp=225000, saldo_usd=344,42.
- **Divisa**: d1, d2, valor (CLP→USD 0,0001533; USD→CLP 652,2750000).
- **Cliente**: rut, nombre (Kelvin), fono, dirección.

## Slide 6

Misma tabla que slide 5, titulada "Una cuenta bancaria ... integridad". Los valores de la columna `saldo` en Ingreso y Gasto, y `saldo_clp` en Cuenta, aparecen resaltados/circulados en morado para indicar que deben mantenerse consistentes entre tablas (el saldo final 225000 en Cuenta debe coincidir con la secuencia de sumas/restas en Ingreso/Gasto).

## Slide 7

"Restricciones sobre varias tablas (!!)". Repite las tablas Ingreso, Gasto, Cuenta. Debajo, código SQL de creación de tabla:
```sql
CREATE TABLE Cuenta (
  número INTEGER PRIMARY KEY,
  rut VARCHAR(12) NOT NULL,
  tipo VARCHAR(12) NOT NULL,
  saldo_clp BIGINT NOT NULL,
  saldo_usd FLOAT NOT NULL,
  CHECK (
    (SELECT SUM(monto) FROM Ingreso WHERE cuenta=número)
    - (SELECT SUM(monto) FROM Gasto WHERE cuenta=número)
    = saldo_clp
  )
)
```
Junto al código hay una foto decorativa de un bloque de madera cortado a la mitad (ilustra "restricción/consistencia"). A la derecha, tres cajas rojas con un ícono de "prohibido" marcan que `INSERT INTO Ingreso ...`, `INSERT INTO Gasto ...` y `UPDATE Cuenta SET saldo_clp ...` individualmente fallarían el CHECK si se ejecutan por separado (porque el CHECK depende de varias tablas a la vez, y Postgres no evalúa CHECKs entre tablas de forma diferida).

## Slide 8

Slide de transición temática: mascota ninja/mago (personaje recurrente del curso) sentado en un sillón sosteniendo un lápiz gigante como si fuera una espada, con el texto "TRANSACCIONES" en azul. Decorativa.

## Slide 9

"Transacciones". Definición: "Una transacción es una unidad lógica de procesamiento en una BASE DE DATOS conformada por una secuencia de operaciones de acceso a los datos (lectura, inserción, eliminación, modificación, recuperación)."

## Slide 10

"Operaciones". Diagrama con 4 cajas azules etiquetadas:
- R(X) → "Lectura del elemento X"
- W(X) → "Escritura del elemento X"
- C → "Confirmación/compromiso"
- A → "Aborto/Rollback"

## Slide 11

"Ejemplo 1". Dos transacciones T1 y T2 leen/escriben elementos X, Y. Tabla de entrelazamiento temporal:
| tiempo | T1 | T2 |
|---|---|---|
| t1 | | R(X) |
| t2 | | W(X) |
| t3 | R(Y) | |
| t4 | W(Y) | |
| t5 | R(X) | |
| t6 | | W(Y) |
| t7 | | A |
| t8 | C | |

Notación equivalente: `R2(X); W2(X); R1(Y); W1(Y); R1(X); W2(Y); A2; C1;` (subíndice = número de transacción).

## Slide 12

Continúa "Ejemplo 1", repite la notación `R2(X); W2(X); R1(Y); W1(Y); R1(X); W2(Y); A2; C1;`. Explica que cada operación de escritura consta de suboperaciones: encontrar la dirección del bloque que contiene X, copiar el bloque a un buffer en memoria principal, copiar X con el nuevo valor en el buffer, y almacenar el bloque actualizado desde buffer a disco.

## Slide 13

"Varios tipos de conflictos cuando hay muchos usuarios operando concurrentemente (especialmente cuando se escribe)". Lista con 3 tipos:
- **Actualización perdida (conflicto WW)**: una transacción sobreescribe los datos que otra tx ya había escrito.
- **Lectura sucia (conflicto WR)**: una tx lee lo que otra tx escribió pero no se había confirmado aún.
- **Lectura no repetible (conflicto RW)**: una tx sobreescribe un dato que otra ya había leído antes pero no había confirmado.

## Slide 14

"Ejemplo de actualización perdida (WW)". Diagrama de línea de tiempo con dos hilos T1/T2 y burbujas de diálogo tipo chat: T1 hace R(X) ("¿Está libre el asiento 24? Sí") y luego W(X) ("Reserve el 24"); en paralelo T2 hace R(X) ("¿Está libre el asiento 24? Sí") antes y W(X) después ("Reserve el 24, pero estaba ocupado!!!" en rojo, indicando el conflicto: T2 sobreescribe la reserva de T1 sin saberlo).

## Slide 15

"Ejemplo de lectura sucia (WR)". Mismo formato de línea de tiempo con burbujas: T1 hace R(X) ("¿Cuántos asientos hay? No hay más") y W(X) ("Reserve entonces en primera clase"); T2 hace W(X) ("Reserve el 24") y luego A/aborto (roja: "...pero sí habían!!!") — T1 leyó un dato escrito por T2 antes de que T2 confirmara, y T2 termina abortando.

## Slide 16

"Ejemplo de lectura no repetible (RW)". Línea de tiempo: T1 hace W(X) ("Reserve el 24"); T2 hace R(X) dos veces ("¿Cuántos asientos hay? A ver..." y luego en rojo "...ahora sí. ¿Cuáles asientos?") — la segunda lectura de T2 da un resultado distinto porque T1 escribió en medio.

## Slide 17

"Vacaciones ...". Foto decorativa (dos muñecos de nieve vestidos de bikini/vacacionista tomando sol en la nieve, junto a una parrilla) — imagen humorística de transición sin contenido técnico.

## Slide 18

"Transacciones: START TRANSACTION/COMMIT". Repite las tablas Gasto/Cuenta/Divisa/Cliente con una nueva fila en Gasto ("Noruega", monto 400000, saldo -175000) y Cuenta con saldo_clp=-175000, saldo_usd=-268,29. Código SQL:
```sql
START TRANSACTION;
  INSERT INTO Gasto VALUES
    (7873698669,'Noruega','2020-02-12','02:14:20',400000,-175000,'TRCLK9K24KS');
  UPDATE Cuenta SET saldo_clp=-175000, saldo_usd=-268.29 WHERE número=7873698669;
COMMIT;
```
Recuadro amarillo: "START TRANSACTION (o a veces BEGIN) inicia la transacción. COMMIT realiza/guarda los cambios."

## Slide 19

"Transacciones (por defecto)". Mismas tablas. Código SQL con los `COMMIT;` comentados (`-- COMMIT;`) tras cada INSERT/UPDATE. Recuadro amarillo: "Si no hay una transacción explícita, por defecto, Postgres hace un COMMIT después de cada sentencia (pero se puede cambiar la configuración)."

## Slide 20

"Transacciones: ROLLBACK". Tablas Gasto/Cuenta/Divisa/Cliente vueltas al estado original (sin la fila "Noruega", saldo_clp=225000). Código:
```sql
START TRANSACTION;
  INSERT INTO Gasto VALUES
    (7873698669,'Noruega','2020-02-12','02:14:20',400000,-175000,'TRCLK9K24KS');
ROLLBACK;
```
Recuadro amarillo: "ROLLBACK deshace/borra los cambios desde el inicio de la transacción."

## Slide 21

"Transacciones: SAVEPOINT". Mismas tablas base (estado con Noruega insertado, saldo_clp=-175000). Código:
```sql
START TRANSACTION;
  INSERT INTO Gasto VALUES
    (7873698669,'Noruega','2020-02-12','02:14:20',400000,-175000,'TRCLK9K24KS');
  UPDATE Cuenta SET saldo_clp=-175000, saldo_usd=-268.25 WHERE número=7873698669;
  SAVEPOINT CompraNoruega;
  INSERT INTO Gasto VALUES
    (7873698669,'BOSE','2020-02-12',200000,-375000,'TRCASD8PNAK');
  ROLLBACK TO SAVEPOINT CompraNoruega;
COMMIT;
```
Recuadro amarillo: "ROLLBACK puede deshacer/borrar los cambios desde un punto específico con SAVEPOINT."

## Slide 22

"Una transacción con valores dinámicos". Código SQL:
```sql
START TRANSACTION;
  INSERT INTO Gasto VALUES
    (7873698669,'Noruega','2020-02-12','02:14:20',400000,-175000,'TRCLK9K24KS');
  UPDATE Cuenta SET saldo_clp=(saldo_clp-400000) WHERE número=7873698669;
  UPDATE Cuenta SET saldo_usd=(A.saldo_clp/valor)
    FROM (SELECT valor FROM Divisa WHERE d1='USD' AND d2='CLP') T,
         (SELECT saldo_clp FROM Cuenta WHERE número=7873698669) A
    WHERE número=7873698669;
COMMIT;
```
Pregunta al pie: "¿Valor final de saldo_usd en Cuenta?" (sin responder aún — tablas muestran el estado previo, saldo_clp=225000, saldo_usd=344,94).

## Slide 23

Continuación de slide 22, misma consulta SQL. Se muestra la respuesta: "¿Valor final de saldo_usd en Cuenta? −268,28 (Se lee el valor actual de la misma transacción)". Tablas actualizadas: saldo_clp=-175000, saldo_usd=-268,28 (resaltado en verde).

## Slide 24

"Una transacción con CHECK". Mismo código SQL de las 2 UPDATE anteriores dentro de una transacción, pero ahora la tabla Cuenta tiene un CHECK: `saldo_clp = saldo_usd * (SELECT valor FROM Divisa WHERE d1='USD' AND d2='CLP')`. Un ícono rojo de "prohibido" marca el primer UPDATE. Pregunta "¿Funciona?" → respuesta "¡No!" (el CHECK falla porque valida saldo_clp vs saldo_usd en un punto intermedio antes de que ambos campos estén actualizados coherentemente, y Postgres no soporta CHECKs diferibles).

## Slide 25

Slide de transición: mascota ninja con lápiz, texto "Atomicidad, Consistencia, Aislamiento, Durabilidad (Atomicity, Consistency, Isolation, Durability)" y título grande "LAS GARANTÍAS DE ACID". Referencia bibliográfica: Capítulo 8.1 | Ramakrishnan / Gehrke.

## Slide 26

"No hay un solo usuario ...". Foto decorativa (campo lleno de muchos muñequitos de nieve pequeños, representando "muchos usuarios"). Texto: "... hay que tener cuidado con la concurrencia".

## Slide 27

"Una cuenta con varios usuarios". Ilustración: dos muñecos de nieve (usuarios) a los costados de una tarjeta de banco ficticio "Banco de Chi..." con N° Cuenta 7873698669, Saldo (CLP) 225000, Límite de crédito 200000, Disponible 425000. Código: `CREATE TABLE Cuenta (..., CHECK (saldo_clp > -200000))`. Dos transacciones concurrentes mostradas en paralelo: `COMPRA(Islas de Caimán, 300000)` a la izquierda con `INSERT INTO Gasto ...` / `UPDATE Cuenta ...`, y `COMPRA(Noruega, 400000)` a la derecha con las mismas operaciones. Pregunta: "¿Cuál será el resultado final?..."

## Slide 28

"Caos" — slide de transición decorativa (texto rojo cursivo grande "Caos" + foto de muñecos de nieve manchados de rojo, estética humorística).

## Slide 29

"Esta vez con transacciones ...". Repite la escena del banco (misma tarjeta/CHECK). Ahora ambas compras (Islas de Caimán 300000 e Noruega 400000) están envueltas en `START TRANSACTION ... COMMIT;`. Pregunta "¿Cuál será el resultado final?" → Respuesta: "Se rechazará una transacción." (porque ambas juntas violarían el CHECK saldo_clp > -200000, pero al ser transacciones atómicas, el sistema puede rechazar una completa en vez de dejar un estado inconsistente).

## Slide 30

"Garantías de ACID". Lista con colores (Atomicidad=verde, Consistencia=azul, Aislamiento=naranja, Durabilidad=morado):
- **Atomicidad**: la ejecución de cada transacción es atómica — se realizan todas las acciones o no se realiza ninguna.
- **Consistencia**: cada transacción debe preservar la integridad — la base de datos satisface todas las restricciones después de una transacción.
- **Aislamiento (Isolation)**: una transacción no puede afectar otra.
- **Durabilidad**: una vez que haya un COMMIT, la base de datos debe persistir los cambios.

## Slide 31

"ACID: Un ejemplo más limpio". Código SQL:
```sql
CREATE TABLE Balance (
  cuenta BIGINT PRIMARY KEY,
  total_gasto BIGINT,
  total_ingreso BIGINT,
  saldo BIGINT,
  CHECK (total_ingreso - total_gasto = saldo)
)
```
Nota en recuadro amarillo: "Usaremos restricciones con CHECK porque dan ejemplos más claros pero es importante tener en cuenta que Postgres no soporta CHECKs diferibles."

## Slide 32

"ACID: Atomicidad". Misma tabla Balance del slide 31. Código:
```sql
START TRANSACTION
  UPDATE Balance SET saldo=saldo-10 WHERE Cuenta=7873698669;
  UPDATE Balance SET total_gasto=total_gasto+10 WHERE Cuenta=7873698669;
COMMIT;
```
Recuadro verde: "Atomicidad — No se puede actualizar el saldo sin actualizar el gasto directamente después. (Si alguna actualización falla, ambas fallan.)"

## Slide 33

"ACID: Consistencia". Mismo esquema. Código con un ícono rojo de "prohibido" marcando la primera UPDATE:
```sql
START TRANSACTION
  UPDATE Balance SET saldo=saldo-100 WHERE Cuenta=7873698669;
  UPDATE Balance SET total_gasto=total_gasto+10 WHERE Cuenta=7873698669;
COMMIT;
```
(los montos -100 y +10 no cuadran con el CHECK). Recuadro azul: "Consistencia — Si el resultado de la transacción no satisface todas las restricciones, fallará."

## Slide 34

"ACID: Aislamiento (Isolation)". Dos transacciones T1 y T2 en paralelo:
```sql
-- T1
START TRANSACTION
  UPDATE Balance SET saldo=saldo-10 WHERE Cuenta=7873698669;   -- (1)
  UPDATE Balance SET total_gasto=total_gasto+100 WHERE Cuenta=7873698669;  -- (3) FALLA
COMMIT;
(4) ROLLBACK;

-- T2
START TRANSACTION
  UPDATE Balance SET saldo=saldo+100 WHERE Cuenta=7873698669;  -- (2)
  UPDATE Balance SET total_ingreso=total_ingreso+100 WHERE Cuenta=7873698669; -- (5)
COMMIT;  -- (6)
```
Los pasos están numerados (1)-(6) indicando el orden real de ejecución intercalado. Recuadro amarillo: "Aislamiento — Una transacción no puede interferir con otra transacción. En (4), hay que tener cuidado con el ROLLBACK: no se puede restaurar el valor de saldo antes del paso (1) porque el valor ya fue cambiado por (2)."

## Slide 35

"ACID: Durabilidad". Mismo esquema Balance. Código igual al de atomicidad (saldo-10, total_gasto+10, COMMIT), con un ícono de disquete al margen. Recuadro morado: "Durabilidad — Una vez que haya un COMMIT exitoso, se persisten los cambios. (Normalmente la persistencia aquí significa en el disco duro. Sin persistencia, en el caso de que la máquina falla y toda la evidencia de los cambios está en memoria principal, el sistema de base de datos olvidará los cambios silenciosamente.)"

## Slide 36

"Entonces con las garantías de ACID ... todo está tranquilo." Foto decorativa: muñeco de nieve sentado tranquilamente en una banca de parque con edificios de fondo.

## Slide 37

"... pero si uno tiene que implementar ACID ... es más difícil ...". Foto decorativa humorística: muñeco de nieve oscuro con texto "kill me" en la imagen.

## Slide 38

"¿Cuándo no tenemos ACID?". Lista con marcas ✗ rojas:
- **Atomicidad**: una transacción se ejecuta solamente a medias pero afecta el estado de la base de datos.
- **Consistencia**: al ejecutar la transacción, la base de datos no satisface las restricciones de integridad.
- **Aislamiento (Isolation)**: el resultado final de dos transacciones no es equivalente a correr cada transacción en serie.
- **Durabilidad**: la base de datos se actualiza momentáneamente y luego vuelve al estado anterior.

## Slide 39

"Modelando una transacción". Recuadro amarillo define notación: `LEER(X)`: leer un objeto X de la base de datos a memoria principal; `ESCRIBIR(X)`: escribir un objeto de memoria principal a la base de datos; un objeto X puede ser un valor, una fila, una tabla. Ejemplo de transferencia bancaria T:
$$\text{LEER}(A);\quad A \leftarrow A-100;\quad \text{ESCRIBIR}(A);\quad \text{LEER}(B);\quad B \leftarrow B+100;\quad \text{ESCRIBIR}(B)$$
Nota: "Dejamos el COMMIT implícito al fin de la transacción."

## Slide 40

Slide de transición: mascota ninja con lápiz. Título "IMPLEMENTANDO ACID: REGISTROS (LOGGING)". Decorativa salvo el título de sección.

## Slide 41

"Mantener un registro de la transacción". Repite el ejemplo de transferencia (LEER/ESCRIBIR A y B) a la izquierda. A la derecha, un ícono de archivo/carpeta con un log `./registro.log`:
```
T begin
T leer A 400
T escribir A 300
T leer B 200
T escribir B 300
T commit
```

## Slide 42

"Si hay un problema, revertir el registro". Recuadro amarillo: "La información en el registro debe bastar para revertir el estado de la base de datos sin ambigüedad." Mismo ejemplo pero con un ícono de "prohibido" en el último `ESCRIBIR(B)` (falla), y el log muestra `T rollback` en vez de `T commit`.

## Slide 43

"Registros ayudan con ...". Lista igual a slide 38 pero con iconos de pulgar arriba (✓ verde) en Atomicidad, Consistencia y Durabilidad, y pulgar abajo (✗ rojo) en Aislamiento (Isolation), indicando que el logging soluciona atomicidad/consistencia/durabilidad pero no aislamiento. Pregunta al pie: "¿Cuáles problemas podemos evitar con alguna forma de registro?..."

## Slide 44

Slide de transición: mascota ninja. Título "IMPLEMENTANDO ACID: SECUENCIABILIDAD (SERIALIZABILITY)". Referencia: Capítulo 8.3 (es)/16.3 (en) | Ramakrishnan / Gehrke.

## Slide 45

"Registros no ayudan con ...". Repite la lista de slide 43 pero con solo "Aislamiento (Isolation)" resaltado en negro/naranja y un pulgar abajo grande; el resto atenuado (gris). Pregunta: "...entonces qué podemos hacer con respecto a aislamiento/concurrencia?..."

## Slide 46

"La solución más simple: ejecución serial". Ejemplo: dos transferencias bancarias entre cuentas A y B (A+B no debe cambiar, A inicia con 400, B con 200). T1 (ejecución serial completa antes que T2): LEER(A), A←A-100, ESCRIBIR(A), LEER(B), B←B+100, ESCRIBIR(B). T2 debajo: LEER(A), v←A×0,1, A←A-v, ESCRIBIR(A), LEER(B), B←B+v, ESCRIBIR(B). Una flecha vertical central etiquetada "EJECUCIÓN" indica el orden temporal top-to-bottom. Pregunta "¿Cuánto es A+B después?" → 270+330=600 (correcto). Notas: "¿Hay un problema aquí? ¡Ejecución serial es lenta!" y "¿Se pueden ejecutar partes de T1 y T2 en paralelo?..."

## Slide 47

"¿Ejecución paralela?" Mismo ejemplo de transferencias, T1 y T2 lado a lado sin operaciones aún desplegadas (recuadros vacíos/atenuados con la flecha "EJECUCIÓN" en medio). Pregunta "¿Cuánto es A+B después? ¯\\_(ツ)_/¯" con nota: "Por simplicidad asumiremos un orden de ejecución en el caso paralelo..."

## Slide 48

Continúa "¿Ejecución paralela?" con ✓ verde arriba a la derecha. Muestra el primer intercalado: T1 completo primero (LEER A, A←A-100, ESCRIBIR(A) / LEER B, B←B+100, ESCRIBIR(B)) y T2 completo después (mismo patrón con v=A×0,1). Resultado: A+B después = 270+330=600 (correcto, orden T1→T2).

## Slide 49

Continúa, con ✗ rojo (pulgar abajo) arriba a la derecha. Ahora el orden intercalado es T2 primero, T1 después. Resultado: A+B después = 260+340=600 (también correcto en este caso particular, aunque el orden cambió).

## Slide 50

"¡Cuidado cuando el orden importe!" Repite el intercalado T2-antes-T1 con resultado 260+340=600. Indica "No tenemos ningún problema con la restricción, pero el orden de ejecución puede afectar el resultado. Dependiendo de la aplicación, a veces puede ser necesario preservar el orden de transacciones y/o aplicar ejecución serial."

## Slide 51

Continúa "¡Cuidado cuando el orden importe!" con el mismo diagrama, ahora atenuado/fantasma salvo el recuadro amarillo destacado: "No tenemos ningún problema con la restricción, pero el orden de ejecución puede afectar el resultado. Dependiendo de la aplicación, a veces puede ser necesario preservar el orden de transacciones y/o aplicar ejecución serial."

## Slide 52

"¿Ejecución paralela?" con ✗ rojo (pulgar abajo). Nuevo intercalado: LEER(A) de T1 ocurre, luego intercalado con T2 de forma que hay un READ-WRITE conflict. Resultado: A+B después = 300+340=640 (¡INCORRECTO! debería ser 600). Pregunta: "¿Dónde está el problema?"

## Slide 53

Repite el mismo diagrama de slide 52 (300+340=640, incorrecto) con el recuadro rojo/pulgar abajo destacado y la pregunta "¿Dónde está el problema?" sin responder aún — mismo contenido, transición para la siguiente explicación.

## Slide 54

"Planificaciones: Secuenciables vs. No Secuenciables". Dos ejemplos de intercalado en paneles verde (arriba, "Secuenciable" con ✓) y rojo (abajo, "No secuenciable"). Panel verde: T1 completo antes que T2 (equivalente a plan serial T1→T2). Panel rojo: intercalado no equivalente a ningún orden serial. Definición: "Equivalente a ejecutar transacción T1 y después transacción T2 (serial)".

## Slide 55

Continúa, mismo diagrama pero con recuadro amarillo destacado definiendo: "Una planificación es una lista de acciones de un conjunto de transacciones en el orden de ejecución." y "Una planificación secuenciable tendrá el mismo efecto que una planificación serial (en algún orden de las transacciones)."

## Slide 56

"Equivalencia por conflictos". Diagrama con dos planificaciones P1 y P2, cada una con operaciones W(X), R(Y), W(Y) de T1 y T2 numeradas 1-4, conectadas con flechas curvas rojas mostrando cómo se pueden reordenar/intercambiar operaciones no conflictivas entre P1 y P2 para demostrar equivalencia por conflictos (mismo efecto aunque el orden textual difiera).

## Slide 57

"Otro ejemplo de Plan secuenciable". Dos tablas lado a lado comparando Usuario 1 / Usuario 2:
Izquierda: t0 X=1;Y=0, t1 Read(X) [U1], t2 Read(Y) [U2], t3 X=X+1 [U1], t4 Y=Y+1 [U2].
Derecha (equivalente serial reordenado, resaltado en rojo/rosa): t0 X=1;Y=0, t1 Read(X) [U1], t2 X=X+1 [U1], t3 Read(Y) [U2], t4 Y=Y+1 [U2].
Ambos planes son equivalentes porque operan sobre variables distintas (X vs Y), sin conflicto real.

## Slide 58

"Otro ejemplo de No Plan secuenciable". Misma estructura de tabla comparativa:
Izquierda: t0 X=1, t1 Read(X) [U1], t2 Read(X) [U2], t3 X=X+1 [U1], t4 X=X+1 [U2].
Derecha: t0 X=1, t1 Read(X) [U1], t2 X=X+1 [U1], t3 Read(X) [U2], t4 X=X+1 [U2].
Aquí ambos usuarios leen y escriben la misma variable X, generando un conflicto real (actualización perdida) — los dos órdenes producen resultados distintos, por lo que no es secuenciable.

## Slide 59

Slide de transición: mascota ninja con lápiz, título "RECUPERABILIDAD". Decorativa salvo el título.

## Slide 60

"Recuperabilidad". Lista de causas por las que una tx puede interrumpirse: fallas (caídas) del computador, error (externo) de la transacción o del sistema, errores (internos) o condiciones de excepción de la transacción, imposición de control de concurrencia (dead-locks, etc.), falla de disco, catástrofes (externas), etc.

## Slide 61

"Recuperabilidad". Definición: "Un plan P es recuperable si ninguna tx T de P se confirma antes de que se hayan confirmado todas las tx T' que han escrito un elemento que T lee posteriormente." Diagrama de línea de tiempo P1: T1 hace W(X) y luego C (commit); T2 hace R(X) (marcado "Se leyó antes"), luego W(X) y C — el R(X) de T2 ocurre después de que T1 escribió pero antes de que T1 confirme.

## Slide 62

"Plan No recuperable". Diagrama de línea de tiempo: T1 hace W(X) ... C (al final, tarde). T2 hace R(X) (nota: "Ojo: se leyó algo no confirmado"), W(X), C — T2 confirma ANTES que T1. Texto en rojo: "¡Si T1 fallara se dificultará la recuperación!"

## Slide 63

"Plan recuperable". Título con nota: "T2 TIENE QUE ESPERAR QUE T1 HAGA COMMIT". Diagrama: T1 hace W(X) y C (temprano); T2 hace R(X), W(X), C (después del commit de T1). Texto en verde: "Si T1 falla, T2 también falla en cascada."

## Slide 64

Slide de transición: mascota ninja con lápiz, título "Solución: Bloqueos (Locks)". Decorativa salvo título.

## Slide 65

"Un protocolo: Bloqueo en 2 fases". Explica reglas: si una transacción T quiere leer un objeto O, debe conseguir un bloqueo compartido sobre O (varias tx pueden leer el mismo objeto simultáneamente); si una transacción T quiere modificar un objeto O, debe conseguir un bloqueo exclusivo sobre O (un bloqueo exclusivo excluye bloqueos compartidos, T puede leer O, y nadie más puede leer ni modificar O mientras T tenga el bloqueo exclusivo).

## Slide 66

"Conflicto de Lectura–Escritura" (con ícono pulgar abajo rojo). Repite el ejemplo de transferencias bancarias T1/T2 con el mismo intercalado problemático de slides 52-53 (resultado A+B=300+340=640, incorrecto), como caso base antes de introducir bloqueos.

## Slide 67

"... con bloqueos". Mismo ejemplo pero con operaciones `EXC(A)` (bloqueo exclusivo) antes de LEER/ESCRIBIR, y `REL(A)` (liberar) después de cada ESCRIBIR. T1: EXC(A), LEER(A), A←A-100, ESCRIBIR(A). T2: EXC(A) marcado con ✗ rojo (bloqueado porque T1 aún no libera A), LEER(A), etc. en gris/pendiente. Pregunta: "¿Cómo sería la planificación final?"

## Slide 68

Continúa "... con bloqueos". Ahora T1 completa: EXC(A), LEER(A), A←A-100, ESCRIBIR(A), REL(A), EXC(B), LEER(B), B←B+100, ESCRIBIR(B), REL(B). T2 empieza después: EXC(B), LEER(B), B←B+v, ESCRIBIR(B), REL(B). Nota en rojo: "Todavía permite conflictos ..."

## Slide 69

"... conflicto". Mismo diagrama. Pregunta "¿Qué tipo de conflicto hay?" → Respuesta en amarillo: "¡Escritura-lectura!" Pregunta "¿Una solución?..."

## Slide 70

"... bloqueo estricto". Solución: "Liberar los bloqueos solo cuando la transacción haya terminado (bloqueo estricto)...". Diagrama actualizado con la flecha "EJECUCIÓN" central.

## Slide 71

"Un protocolo: Bloqueo en 2 fases estricto". Repite las reglas del slide 65 (bloqueo compartido para lectura, bloqueo exclusivo para escritura) agregando la regla final: "(Solo) cuando T haya terminado, liberará sus bloqueos."

## Slide 72

Repite el mismo contenido del slide 71 pero con un recuadro amarillo superpuesto destacando: "La forma más popular de garantizar secuenciabilidad." (el resto del texto atenuado/fantasma).

## Slide 73

"... pero cuidado!" con nota "Hay que evitar interbloqueos (deadlocks)". Diagrama: T1 hace EXC(A), LEER(A), A←A-100, ESCRIBIR(A) (completo); T2 intenta EXC(B) y luego EXC(A) marcado con ✗ rojo — situación de deadlock potencial donde T1 espera un recurso que tiene T2 y viceversa. Recuadro verde con dos soluciones: "Solución 1: Plazos para terminar o ..." y "Solución 2: Detectar ciclos en transacciones esperando o ..."

## Slide 74

"Bloqueo en 2 fases conservativo". Recuadro verde: "Solución 3: La transacción adquieren todos los bloqueos necesarios al inicio y de una forma atómica..." Diagrama: T1 hace `EXC(A,B)` (bloqueo conjunto al inicio), luego LEER(A), A←A-100, ESCRIBIR(A), LEER(B), B←B+100, ESCRIBIR(B), REL(A,B) (libera todo al final). T2 espera y hace lo mismo con v. Pregunta "¿Es estricto?" → "No..."

## Slide 75

"Bloqueo en 2 fases estricto/conservativo". Recuadro amarillo: "Solo se pueden paralelizar transacciones que no compartan objetos (lo más 'fácil' pero lo menos paralelizable)". Mismo diagrama de T1/T2 con EXC(A,B) al inicio y REL(A,B) al final de cada una, ejecutándose de forma prácticamente serial porque comparten A y B.

## Slide 76

"Ejemplo en APP". Captura de código fuente real (C#/lenguaje similar) sobre fondo oscuro tipo editor, mostrando una cadena de validaciones `if (flag) { flag = _ITS_DO...InsertTransVenta...(..., oSqlTransaction); ...}` anidadas para insertar detalle de venta, cabecera, pago, actualizar stock, y manejo de vale/crédito cliente, terminando con `oSqlTransaction.Commit();` en el bloque `if (flag)` final y un `else` (manejo de rollback implícito, cortado). Ilustra el patrón de transacción anidada con flags de éxito en una aplicación real de ventas.

## Slide 77

"Pero para un usuario ...". Foto decorativa: muñeco de nieve sentado tranquilo en una banca de parque (misma imagen que slide 36), simbolizando que toda la complejidad de bloqueos/transacciones es invisible para el usuario final.

## Slide 78

"Hemos terminado con bases de datos relacionales". Foto/captura decorativa de un ganador de deletreo (spelling bee) celebrando con confeti, con cartel "ARVIND". Marca el cierre del bloque temático de bases de datos relacionales del curso.

## Slide 79

Diapositiva de cierre del capítulo: 3 fotos decorativas de un muñeco de nieve triste con guantes negros (mismo motivo repetido en 3 crops distintos), sin texto adicional (transición hacia "Preguntas?").

## Slide 80

"Preguntas?" Slide de cierre estándar con foto decorativa de un muñeco de nieve con bufanda amarilla frente a una casa.
