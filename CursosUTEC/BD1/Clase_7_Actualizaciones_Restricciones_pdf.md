---
curso: BD1
titulo: Clase 7 Actualizaciones, Restricciones
slides: 54
fuente: Clase 7 Actualizaciones, Restricciones.pdf
---

## Slide 1

Portada del curso (decorativa: fondo con túnel digital azul y figura humana, logo UTEC, banda "Reinventa el mundo").

**CLASE 7: ACTUALIZACIONES, RESTRICCIONES (SQL)**
CS2041 - Base de Datos I
Ciclo 2024-1

Profesores: Teófilo Chambilla - tchambilla@utec.edu.pe · Brenner Ojeda - bojeda@utec.edu.pe

## Slide 2

Slide de índice. Fondo derecho: imagen decorativa de un brazo/mano robótica sobre mapa del mundo digital (decorativa).

**Índice:**
- Introducción
- Gestionar y crear tablas
- Esquema
- Privilegios
- Actualizar tablas
- Restricciones
- Definir dominios y tipos

## Slide 3

Diagrama de progreso del curso (línea de tiempo de temas, tipo "roadmap"). Muestra una barra horizontal segmentada con los temas del curso: Introducción, Modelo Relacional, Entidad-Relación, Algebra Relacional & Cálculo Relacional, SQL, "SQL II" (resaltado en un recuadro azul claro, indicando el tema actual — Clase 7), Formas Normales. Un ícono de "mago/ninja" apunta hacia el segmento actual (SQL II) y una bandera a cuadros marca la meta al final del camino. Los segmentos ya cubiertos (Introducción...SQL) están en azul oscuro; los pendientes (Formas Normales) en azul claro.

CS2041 Base de Datos I, Ciclo 2024-1.

## Slide 4

Slide de transición de texto simple: "Resumen: Clase 6" y debajo, en verde, "Structured Query Language (SQL)".

## Slide 5

**Agregación: GROUP BY y HAVING** — repaso de la clase anterior con diagrama detallado.

Código SQL (resaltado por colores: rojo=cláusulas, azul=WHERE):
```sql
SELECT A,
FROM T1,T2
WHERE C1
GROUP BY A,
HAVING SUM(c) = n;
```

Diagrama: dos tablas base T1 (columnas A, A2, A3; filas a, a1, a2, a3) y T2 (columnas B, B2, B3; filas b, b1, b2, b3). A la derecha, el producto cartesiano T1×T2 (tabla con columnas A,A2,A3,B,B2,B3) mostrando cómo cada fila de T1 se combina con cada fila de T2 (primero fila "a" combinada con b,b1,b2,b3; luego fila "a1" combinada con b,b1,b2,b3, etc.). Flechas azules conectan la cláusula WHERE C1 con el filtro sobre el producto cartesiano; llaves y flecha roja curva conectan GROUP BY/HAVING con la agrupación de filas repetidas de T1 y T2 dentro del producto cartesiano (mostrando visualmente cómo se agrupan las filas "a,a,a,a" y "a1,a1,a1,a1").

## Slide 6

**Las preguntas de hoy** — ejemplo de base de datos del sistema solar (mismo dataset usado en clases previas), fondo con imagen decorativa de estrellas/espacio.

Tabla **Planeta** (columnas: nombre, dist, radio, grav, días, años, temp, anillo):
| nombre | dist | radio | grav | días | años | temp | anillo |
|---|---|---|---|---|---|---|---|
| Mercurio | 0,39 | 0,38 | 2,8 | 58,646 | 0,241 | 440 | false |
| Venus | 0,72 | 0,95 | 8,9 | -243,019 | 0,615 | 730 | false |
| Tierra | 1,00 | 1,00 | 9,8 | 0,997 | 1,000 | 288 | false |
| Marte | 1,52 | 0,53 | 3,7 | 1,026 | 1,880 | 186 | false |
| Júpiter | 5,20 | 10,97 | 22,9 | 0,414 | 11,862 | 152 | true |
| Saturno | 9,54 | 9,14 | 9,1 | 0,444 | 29,447 | 134 | true |
| Urano | 19,19 | 3,98 | 7,8 | -0,719 | 84,017 | 76 | true |
| Neptuno | 30,07 | 3,86 | 11,0 | 0,671 | 164,791 | 53 | true |

Tabla **Satélite** (nombre, planeta, descubridor, año): Luna/Tierra/⊥/⊥, Ganímedes/Júpiter/Galileo Galilei/1610, Calisto/Júpiter/Galileo Galilei/1610, Europa/Júpiter/Galileo Galilei/1610, Ío/Júpiter/Galileo Galilei/1610, Titán/Saturno/Christiaan Huygens/1655, Tritón/Neptuno/William Lassell/1846.

Tabla **Aterrizaje** (nave, planeta, país, año): Messenger/Mercurio/EEUU/2015, Venera 3/Venus/URRS/1966, Pioneer/Venus/EEUU/1978, Mars 2 lander/Marte/URRS/1971, Viking 1/Marte/EEUU/1976, Beagle 2/Marte/ESA/2003, Galileo/Júpiter/EEUU/2003.

Debajo, dos preguntas guía en cajas punteadas: "¿Pero cómo se puede crear y actualizar las tablas?" y "¿Y cómo se puede saber si es un buen diseño relacional o no?"

## Slide 7

Slide de sección (decorativa: mismo personaje "ninja mago" sentado en trono escribiendo con lápiz mágico, usado como separador visual en varias slides).

**SQL: Gestionar y crear tablas**
Capítulo 3.1.1 | Ramakrishnan / Gehrke

## Slide 8

**SQL: Base de datos** — diagrama conceptual de jerarquía de objetos en Postgres.

Diagrama de círculos concéntricos: un ícono "PG Role" (persona) con flechas (marcadas con checks verdes) que apuntan hacia dentro de un círculo grande "Database", que contiene un círculo "Schema", que contiene un círculo interior azul "Schema Objects". Muestra la jerarquía Role → Database → Schema → Schema Objects.

Debajo, otro diagrama: una caja rosada "Database" que contiene dos círculos "Schema" independientes, cada uno con cajas blancas dentro (representando tablas), ilustrando que una base de datos puede tener múltiples esquemas, cada uno con sus propias tablas.

## Slide 9

**SQL: Base de datos** — sintaxis de creación.

```sql
CREATE DATABASE name
    [ [ WITH ] [ OWNER [=] user_name ]
           [ TEMPLATE [=] template ]
           [ ENCODING [=] encoding ]
           ...
           [ CONNECTION LIMIT [=] connlimit ] ]
```

Fuente: https://www.postgresql.org/docs/9.0/sql-createdatabase.html

## Slide 10

**SQL: Esquema** — fondo decorativo del sistema solar (sol con brillo, estrellas), etiqueta "SistemaSolar" en la esquina superior izquierda (indicando el contexto de ejemplo que se usará en las siguientes slides).

```sql
CREATE SCHEMA SistemaSolar; -- crear una agrupación de tablas
```

Preguntas guía en cajas: "¿Para que sirven los esquemas?" → "Podemos configurar agrupaciones de tablas usando esquemas ..."

## Slide 11

**SQL: Privilegios de Esquema**

```sql
CREATE SCHEMA SistemaSolar; -- crear una agrupación de tablas
GRANT USAGE ON SCHEMA SistemaSolar TO narmstrong; -- sólo lectura
GRANT ALL PRIVILEGES ON SCHEMA SistemaSolar TO csagan; -- todo
```

## Slide 12

**SQL: Crear tablas**

Tabla de ejemplo **Aterrizaje** (vacía, solo encabezados: nave, planeta, país, año).

```sql
CREATE SCHEMA SistemaSolar; -- crear una agrupación de tablas
CREATE TABLE SistemaSolar.Aterrizaje (
  nave VARCHAR (255),
  planeta VARCHAR (255),
  país VARCHAR (255),
  año SMALLINT
);
```

## Slide 13

**SQL: Borrar tablas**

```sql
CREATE SCHEMA SistemaSolar; -- crear una agrupación de tablas
CREATE TABLE SistemaSolar.Aterrizaje (
  nave VARCHAR (255),
  planeta VARCHAR (255),
  país VARCHAR (255),
  año SMALLINT
);
DROP TABLE SistemaSolar.Aterrizaje;
```

Caja de pregunta: "¿Hay que poner el esquema cada vez?"

## Slide 14

**SQL: Camino de esquema** (search_path)

```sql
SET search_path = my_schema, "$user", public; -- For current session only

ALTER ROLE your_role SET search_path = my_schema, "$user", public; -- Persistent, for role
```

```sql
CREATE SCHEMA SistemaSolar; -- crear una agrupación de tablas
SHOW search_path; -- public
ALTER USER csagan SET search_path TO SistemaSolar,public;
CREATE TABLE Aterrizaje ( ... );
DROP TABLE Aterrizaje;
```

Nota destacada en caja amarilla: "Seleccionará el primer esquema en el camino. P. ej., si hay SistemaSolar.Aterrizaje y public.Aterrizaje, leerá de la primera tabla".

## Slide 15

Slide de sección (decorativa: personaje ninja mago sentado).

**SQL: Actualizar tablas**
Capítulo 3.1.1 | Ramakrishnan / Gehrke

## Slide 16

**SQL: Insertar tuplas**

Tabla **Aterrizaje** con una fila: Messenger/Mercurio/EEUU/2015.

```sql
...
CREATE TABLE Aterrizaje ( ... );
INSERT INTO Aterrizaje VALUES ('Messenger','Mercurio','EEUU',2015);
```

## Slide 17

**SQL: Insertar tuplas** (segunda inserción)

Tabla **Aterrizaje** con dos filas: Messenger/Mercurio/EEUU/2015, Venera 3/Venus/URRS/1966.

```sql
...
CREATE TABLE Aterrizaje ( ... );
INSERT INTO Aterrizaje VALUES ('Messenger','Mercurio','EEUU',2015);
INSERT INTO Aterrizaje VALUES ('Venera 3','Venus','URRS',1966);
```

## Slide 18

**SQL: Insertar tuplas** (tercera inserción)

Tabla **Aterrizaje** con tres filas (se agrega Pioneer/Venus/EEUU/1978).

```sql
...
CREATE TABLE Aterrizaje ( ... );
INSERT INTO Aterrizaje VALUES ('Messenger','Mercurio','EEUU',2015);
INSERT INTO Aterrizaje VALUES ('Venera 3','Venus','URRS',1966);
INSERT INTO Aterrizaje VALUES ('Pioneer','Venus','EEUU',1978);
```

## Slide 19

**SQL: Insertar tuplas** (inserción con error de tipo)

Tabla **Aterrizaje** sin cambios visibles (la inserción falla).

```sql
...
INSERT INTO Aterrizaje VALUES ('Messenger','Mercurio','EEUU',2015);
INSERT INTO Aterrizaje VALUES ('Venera 3','Venus','URRS',1966);
INSERT INTO Aterrizaje VALUES ('Pioneer','Venus','EEUU',1978);
INSERT INTO Aterrizaje VALUES ('Mars 2 lander','Marte','URRS','1971'); -- error
```
(el error es porque '1971' se pasa como string en vez de entero para la columna año)

## Slide 20

**SQL: Insertar tuplas** (insertar con columnas nombradas, dejando año nulo)

Tabla **Aterrizaje** ahora con 4 filas, la última "Mars 2 lander / Marte / EEUU / ⊥" (símbolo ⊥ = NULL, año no especificado).

```sql
...
INSERT INTO Aterrizaje VALUES ('Mars 2 lander','Marte','URRS','1971'); -- error
INSERT INTO Aterrizaje (país,nave,planeta) VALUES ('EEUU','Mars 2 lander','Marte');
```
Muestra que se puede especificar el orden/subconjunto de columnas explícitamente en el INSERT.

## Slide 21

**SQL: Insertar tuplas** (INSERT ... SELECT, crear tabla filtrada)

Dos tablas lado a lado: **AterrizajeEEUU** (nave, planeta, país, año) con 3 filas (Messenger/Mercurio/EEUU/2015, Pioneer/Venus/EEUU/1978, Mars 2 lander/Marte/EEUU/⊥) y **Aterrizaje** (4 filas, incluye también Venera 3/Venus/URRS/1966).

```sql
...
INSERT INTO Aterrizaje (país,nave,planeta) VALUES ('EEUU','Mars 2 lander','Marte');
CREATE TABLE AterrizajeEEUU ( ... ); -- misma definición que Aterrizaje
INSERT INTO AterrizajeEEUU ( SELECT * FROM Aterrizaje WHERE país='EEUU' );
```

## Slide 22

**SQL: Editar tuplas** (UPDATE)

Tabla **AterrizajeEEUU** sin cambios (3 filas) y tabla **Aterrizaje** actualizada: la fila "Mars 2 lander/Marte" ahora muestra país=URRS, año=1971 (antes era EEUU/⊥).

```sql
...
UPDATE Aterrizaje SET año=1971,país=URRS WHERE nave='Mars 2 lander';
```

## Slide 23

**SQL: Borrar tuplas** (DELETE)

Tabla **AterrizajeEEUU** reducida a 2 filas (se eliminó la fila con año NULL: "Mars 2 lander"). Tabla **Aterrizaje** sin cambios (4 filas).

```sql
...
DELETE FROM AterrizajeEEUU WHERE año IS NULL;
```

## Slide 24

**SQL: Borrar columnas** (ALTER TABLE DROP COLUMN)

Tabla **AterrizajeEEUU** ahora sin la columna país (solo nave, planeta, año). Tabla **Aterrizaje** sin cambios.

```sql
...
ALTER TABLE AterrizajeEEUU DROP COLUMN país;
```

## Slide 25

**SQL: Crear columnas** (ALTER TABLE ADD COLUMN)

Tabla **AterrizajeEEUU** ahora con columna nueva "despegue" (valores NULL/⊥ en ambas filas). Tabla **Aterrizaje** sin cambios.

```sql
...
ALTER TABLE AterrizajeEEUU ADD COLUMN despegue DATE;
```

## Slide 26

**SQL: Modificar columnas** (ALTER TABLE ALTER COLUMN TYPE)

```sql
...
ALTER TABLE AterrizajeEEUU ALTER COLUMN despegue VARCHAR(255);
```

Nota destacada en texto negro grande: "PSQL: ALTER TABLE AterrizajeEEUU ALTER COLUMN despegue TYPE VARCHAR(255)" — corrigiendo la sintaxis correcta de Postgres (requiere la palabra TYPE).

## Slide 27

**Postgres: Cargar datos** (COPY)

Tabla **Aterrizaje** ahora con 8 filas completas (Messenger, Venera 3, Pioneer, Messenger otra vez repetido/duplicado, Venera 3 repetido, Pioneer repetido, Mars 2 lander/Marte/URRS/1971, Viking 1/Marte/EEUU/1976, Beagle 2/Marte/ESA/2003, Galileo/Júpiter/EEUU/2003) — nótese datos duplicados/concatenados.

```sql
...
COPY Aterrizaje FROM '/home/csagan/aterrizaje.tsv' DELIMITER E'\t';
```

Cajas de nota: "¿Algún problema aquí?" → "Específico de Postgres" y "Concatena los datos" (advierte que COPY es específico de Postgres y que si se ejecuta de nuevo duplica/concatena los datos ya existentes en vez de reemplazarlos).

## Slide 28

Slide de sección (decorativa: personaje ninja mago sentado).

*(Integrity Constraints)*
**SQL: Restricciones**
Capítulo 5.7 | Ramakrishnan / Gehrke

## Slide 29

"Abre una cuenta" — imagen decorativa humorística: un muñeco de nieve sentado frente a una laptop y monitor sobre una mesa nevada, con logo ficticio "Banco de ABC" abajo a la derecha. Slide de transición/humor, sin contenido técnico.

## Slide 30

**SQL: Esquema** (nuevo ejemplo bancario)

```sql
CREATE SCHEMA SistemaBancario;
```

## Slide 31

**Y (por supuesto) hay una base de datos** — presenta el dataset bancario completo que se usará en el resto de la clase. Fondo con marca de agua decorativa "Banco de Chilly".

Tabla **Ingreso** (cuenta, comentario, fecha, hora, monto, saldo, id):
| cuenta | comentario | fecha | hora | monto | saldo | id |
|---|---|---|---|---|---|---|
| 7873698669 | Deposito inicial | 2020-21-01 | 20:02:02 | 300000 | 300000 | TRCXGU8JSHD |
| 7873698669 | C0°0°L Designs | 2020-02-06 | 09:15:33 | 50000 | 325000 | TRCCIA2J8A0 |

Tabla **Gasto** (cuenta, comentario, fecha, hora, monto, saldo, id):
| cuenta | comentario | fecha | hora | monto | saldo | id |
|---|---|---|---|---|---|---|
| 7873698669 | Electricidad | 2020-02-02 | 20:00:01 | 8200 | 291800 | TRCJASJDA9A |
| 7873698669 | Calefacción | 2020-02-02 | 20:00:02 | 600 | 291200 | TRC81KAQWAS |
| 7873698669 | Moviestar | 2020-02-02 | 20:00:03 | 16200 | 275000 | TRCK8J7JA8D |
| 7873698669 | Cajero | 2020-02-08 | 16:05:02 | 100000 | 225000 | TRCPM8A45AD |

Tabla **Cuenta** (número, rut, tipo, saldo_clp, saldo_usd): 7873698669 / 32.000.273-K / Estacional / 225000 / 344,94

Tabla **Divisa** (d1, d2, valor): CLP/USD/0,0001533, USD/CLP/652,2750000

Tabla **Cliente** (rut, nombre, fono, dirección): 32.000.273-K / Kelvin / +56976698463 / Campo de Hielo Sur, Depto 273

## Slide 32

**Modelo Relacional: Restricciones** — slide conceptual con ícono del personaje ninja mago apuntando con un puntero.

"**Restricciones** (*de integridad*): son **restricciones** formales que imponemos a **un esquema** que **todas** sus instancias deben satisfacer" (texto con jerarquía de color: rojo para "restricciones", naranja para "un esquema", gris para "sus instancias").

## Slide 33

**Restricciones básicas: llaves, nulos, domino**

Tabla **Cuenta** con una fila de ejemplo.

```sql
CREATE TABLE Cuenta (
  número BIGINT PRIMARY KEY,
  rut VARCHAR (12) NOT NULL,
  tipo VARCHAR (12) NOT NULL,
  saldo_clp BIGINT NOT NULL,
  saldo_usd DOUBLE PRECISION NOT NULL
)
```

Tres ejemplos de operaciones RECHAZADAS (marcadas con ícono ❌ rojo):
```sql
INSERT INTO Cuenta VALUES (7873698669, '28.923.123-7', 'Estacional', 1000, 1.53)  -- viola PK duplicada
UPDATE Cuenta SET tipo=NULL WHERE número=7873698669  -- viola NOT NULL
INSERT INTO Cuenta VALUES (7273697679, '28.923.0123-7', 'Estacional', 1000, 1.53)  -- viola dominio (formato rut)
```

## Slide 34

**Restricciones básicas: valores por defecto** (DEFAULT)

Tabla **Cuenta** ahora con 2 filas: la original y una nueva (7273697679 / 28.923.123-7 / Estacional / 0 / 0,00 — resaltada en verde, mostrando los valores por defecto aplicados).

```sql
CREATE TABLE Cuenta (
  número BIGINT PRIMARY KEY,
  rut VARCHAR (12) NOT NULL,
  tipo VARCHAR (12) NOT NULL,
  saldo_clp BIGINT NOT NULL DEFAULT 0,
  saldo_usd DOUBLE PRECISION NOT NULL DEFAULT 0
)
```
```sql
INSERT INTO Cuenta (número, rut, tipo)
VALUES (7273697679, '28.923.123-7', 'Estacional')
```
(resaltado en verde/oliva: al omitir saldo_clp y saldo_usd, toman el valor DEFAULT 0)

## Slide 35

**Restricciones de unicidad** (UNIQUE)

Tabla **Cuenta** con 2 filas (igual a la anterior).

```sql
CREATE TABLE Cuenta (
  número INTEGER PRIMARY KEY,
  rut VARCHAR (12) NOT NULL,
  tipo VARCHAR (12) NOT NULL,
  saldo_clp BIGINT NOT NULL DEFAULT 0,
  saldo_usd FLOAT NOT NULL DEFAULT 0,
  UNIQUE (rut,tipo)
)
```
Ejemplo rechazado (❌): `INSERT INTO Cuenta (número, rut, tipo) VALUES (8079766582, '28.923.123-7', 'Estacional')` — viola UNIQUE(rut,tipo) porque ya existe esa combinación.

Nota destacada: "La llave primaria implica una restricción de unicidad. La unicidad representa una llave candidata: se pueden tener varias llaves candidatas pero una sola llave primaria."

## Slide 36

**Nombrar (y borrar) restricciones** (CONSTRAINT ... nombre)

```sql
CREATE TABLE Cuenta (
  número INTEGER,
  rut VARCHAR (12) NOT NULL,
  tipo VARCHAR (12) NOT NULL,
  saldo_clp BIGINT NOT NULL DEFAULT 0,
  saldo_usd FLOAT NOT NULL DEFAULT 0,
  CONSTRAINT Cuenta_uni_rt UNIQUE (rut,tipo),
  CONSTRAINT Cuenta_pk PRIMARY KEY (número)
)
```
```sql
ALTER TABLE Cuenta
DROP CONSTRAINT Cuenta_uni_rt
```
Nota: "Más fácil cambiar restricciones posteriormente. Si hay una violación, el mensaje de error será más intuitiva si las restricciones tienen nombres intuitivos."

## Slide 37

**Restricciones de llaves foráneas** (FOREIGN KEY / REFERENCES)

Tabla **Ingreso** (2 filas) y tabla **Cuenta** (1 fila, 7873698669).

```sql
CREATE TABLE Ingreso (
 cuenta BIGINT REFERENCES Cuenta(número),
 comentario VARCHAR (255),
 fecha DATE NOT NULL,
 hora TIME NOT NULL,
 monto BIGINT NOT NULL,
 saldo INT NOT NULL,
 id VARCHAR (12) PRIMARY KEY
)
```
Ejemplo rechazado (❌): `INSERT INTO Ingreso VALUES (7273697679, ..., ...)` — la cuenta 7273697679 no existe en Cuenta.número.

Nota: "Cada cuenta en Ingreso tiene que estar en Cuenta.número."

## Slide 38

**Restricciones de llaves compuestas** (composite PRIMARY KEY / FOREIGN KEY)

Tabla **Divisa** (d1, d2, valor) con 4 filas: CLP/USD/0,0001533, USD/CLP/652,2750000, CLP/EUR/0,0001498, EUR/CLP/735,9700000.

Tabla **Cambio** (id, D.venta, D.compra, monto): CA0121312393/CLP/USD/100000,00; CA0121312393/CLP/EUR/20000,00; CA2134812341/EUR/CLP/4815,16.

```sql
CREATE TABLE Divisa (
 d1 VARCHAR (3),
 d2 VARCHAR (3),
 valor DOUBLE PRECISION,
 PRIMARY KEY (d1, d2)
)

CREATE TABLE Cambio (
 id VARCHAR (12),
 venta VARCHAR (3),
 compra VARCHAR (3),
 monto DOUBLE PRECISION,
 FOREIGN KEY (venta, compra) REFERENCES Divisa (d1, d2),
 PRIMARY KEY (id, venta, compra)
)
```

## Slide 39

**Restricciones sobre varias columnas** (CHECK)

Tabla **Cuenta** con 1 fila.

```sql
CREATE TABLE Cuenta (
  número BIGINT PRIMARY KEY,
  rut VARCHAR (12) NOT NULL,
  tipo VARCHAR (12) NOT NULL,
  saldo_clp BIGINT NOT NULL,
  saldo_usd DOUBLE PRECISION NOT NULL,
  CHECK ( ROUND ( (saldo_clp/saldo_usd)::NUMERIC - 652.275 , 1 ) = 0 )
)
```
Ejemplo rechazado (❌): `INSERT INTO Cuenta VALUES (7273697679, '28.923.123-7', 'Estacional', 100, 0.99)` — el ratio clp/usd no coincide con 652.275, viola el CHECK.

## Slide 40

**Restricciones sobre varias tablas** (CHECK con subconsulta a otra tabla)

Tabla **Cuenta** y tabla **Divisa** (2 filas: CLP/USD, USD/CLP).

```sql
CREATE TABLE Cuenta (
  número BIGINT PRIMARY KEY,
  rut VARCHAR (12) NOT NULL,
  tipo VARCHAR (12) NOT NULL,
  saldo_clp BIGINT NOT NULL,
  saldo_usd DOUBLE PRECISION NOT NULL,
  CHECK ( ROUND((saldo_clp/saldo_usd)::NUMERIC -
    ( SELECT valor FROM Divisa
      WHERE d1='USD' AND d2='CLP' ) , 1 ) = 0
  )
)
```
Ejemplo rechazado (❌) igual al anterior. Muestra CHECK que consulta otra tabla (Divisa) dinámicamente en vez de un valor fijo.

## Slide 41

**Restricciones sobre varias tablas (!)** — plantea el problema de restricciones que involucran 2 tablas simétricamente (Ingreso y Gasto).

Tablas **Ingreso** y **Gasto** (mismos datos de la slide 31).

```sql
CREATE TABLE Ingreso (
 cuenta INTEGER,
 ...,
 CHECK(
  ( SELECT COUNT(*) FROM Ingreso I
    WHERE I.fecha=fecha AND I.cuenta=cuenta ) +
  ( SELECT COUNT(*) FROM Gasto G
    WHERE G.fecha=fecha AND G.cuenta=cuenta ) < 1000
 )
)
```
Preguntas/notas: "¿Algún problema aquí? ... ¿Por qué la ponemos en Ingreso cuando involucra Gasto igualmente? Por ejemplo, si agregáramos la milésima tupla (con la misma cuenta y fecha) a Gasto, ¡no tendríamos una violación!" y "¿Alguna solución? Duplicar la restricción en Gasto o ..."

## Slide 42

**Asertos: Restricciones independientes** (CREATE ASSERTION)

Tablas **Ingreso** y **Gasto** (mismos datos).

```sql
CREATE ASSERTION MaxTransferenciasDiarias
CHECK (
 ( SELECT MAX(num)
   FROM
    ( SELECT COUNT(*) AS num
      FROM
       ( SELECT * FROM Ingreso
         UNION
         SELECT * FROM Gasto ) Trans
      GROUP BY fecha, cuenta ) TransC ) < 1000 )
```
Notas: "Rechazará alguna operación en el esquema que violaría la restricción". "La restricción no depende de ni una tabla ni la otra." "... pero puede ser más costosa/compleja así."

## Slide 43

**¡Garantizar integridad con restricciones!** — slide de cierre visual de la sección de restricciones, mostrando todas las tablas del ejemplo bancario con círculos/óvalos resaltando en color naranja/oliva los valores de saldo interconectados (Ingreso.saldo, Gasto.saldo, Cuenta.saldo_clp) y en verde los de saldo_usd/Divisa.valor, ilustrando visualmente la coherencia/integridad de los datos entre tablas relacionadas.

Incluye las tablas Ingreso, Gasto, Cuenta, Divisa, Cliente ya vistas, con marcas circulares de resaltado a mano alzada sobre los valores numéricos vinculados.

## Slide 44

Cartel de advertencia (imagen decorativa tipo señal "WARNING" amarilla y negra):

"**WARNING** — Postgres no permite consultas anidadas en CHECK ni asertos (son caros!)"

## Slide 45

Slide de sección (decorativa: personaje ninja mago sentado).

**Definir dominios y tipos**

## Slide 46

**Crear dominios: VARCHAR** (CREATE DOMAIN)

Tablas **Ingreso** y **Gasto** (mismos datos de ejemplo).

```sql
CREATE DOMAIN tr_str VARCHAR (12)
  CHECK ( VALUE LIKE 'TRC%' );

CREATE TABLE Ingreso (
  ... ,
  id tr_str PRIMARY KEY );

CREATE TABLE Gasto (
  ... ,
  id tr_str PRIMARY KEY );
```
Ejemplos rechazados (❌):
```sql
UPDATE Ingreso SET id='XJ1' WHERE id='TRCXGU8JSHD'
UPDATE Gasto SET id='8AS' WHERE id='TRCPM8A45AD'
```
(ambos violan el dominio porque no empiezan con 'TRC')

## Slide 47

**Crear dominios: INTEGER**

Tablas **Ingreso** y **Cuenta**.

```sql
CREATE DOMAIN c_no BIGINT
  CHECK ( VALUE > 999999999
    AND VALUE <= 9999999999);

CREATE TABLE Ingreso (
 cuenta c_no, ... );

CREATE TABLE Cuenta (
 número c_no PRIMARY KEY, ... );
```
Ejemplos rechazados (❌):
```sql
UPDATE Ingreso SET cuenta=65537 WHERE id='TRCXGU8JSHD'
UPDATE Cuenta SET número=691 WHERE número=7873698669
```
(ambos violan el dominio porque el número de cuenta debe tener 10 dígitos, entre 999999999 y 9999999999)

## Slide 48

**Dominios: compatibles con el tipo base**

Tablas **Ingreso** y **Cuenta**.

```sql
CREATE DOMAIN c_no BIGINT
  CHECK ( VALUE > 999999999
    AND VALUE <= 9999999999);

CREATE TABLE Ingreso (
 cuenta c_no, ... );

CREATE TABLE Cuenta (
 número c_no PRIMARY KEY, ... );
```
Consulta permitida (resaltada en verde, funciona correctamente):
```sql
SELECT rut FROM Cuenta
WHERE número > saldo_clp
```
Resultado: rut = 32.000.273-K

Nota: "Se puede comparar valores del domino con otros valores como fuera del tipo base" — un DOMAIN es compatible/comparable con su tipo base y otros valores del mismo tipo base.

## Slide 49

**Tipos: son distintos a otros tipos** (CREATE TYPE ... UNDER)

Tablas **Ingreso** y **Cuenta**.

```sql
CREATE TYPE c_no_t UNDER BIGINT;

CREATE TABLE Ingreso (
 cuenta c_no_t, ... );

CREATE TABLE Cuenta (
 número c_no_t PRIMARY KEY, ... );
```
Consulta rechazada (❌):
```sql
SELECT rut FROM Cuenta
WHERE número > saldo_clp
```
Nota: "No se pueden comparar valores del nuevo tipo con valores de otros tipos (solo entre sí)." — a diferencia del DOMAIN, un TYPE (subtipo) nuevo NO es comparable directamente con el tipo base.

## Slide 50

**Tipos: son distintos a otros tipos** (funciones no compatibles)

Mismas tablas y mismo CREATE TYPE que la slide anterior.

Consulta rechazada (❌):
```sql
SELECT número, (número+1) AS siguiente
FROM Cuenta
```
Nota: "No se pueden usar funciones del tipo base con valores del nuevo tipo." — la suma (+1), función del tipo base BIGINT, no aplica directamente sobre el nuevo tipo c_no_t.

## Slide 51

Cartel de advertencia (imagen decorativa "WARNING" amarilla/negra):

"Tipos son estándares (en SQL). Pero Postgres solo suporte tipos compuestos ..."

## Slide 52

**Tipos: un tipo compuesto** (CREATE TYPE AS, tipo fila/struct)

Tabla **Cuenta** con columna "saldo" ahora mostrando un valor compuesto: (clp:225000, usd:344,94).

```sql
CREATE TYPE valor AS (
  clp     BIGINT,
  usd     DOUBLE PRECISION
);
CREATE TABLE Cuenta AS (
  número ... ,
  saldo valor
);
INSERT INTO Cuenta VALUES (7873698669, '32.000.273-K', 'Estacional', ROW(225000, 344.94));
```

## Slide 53

**Tipos: un tipo compuesto** (acceso a campos internos con notación punto)

Tabla resultado con una columna **saldo.usd** = 344,49.

```sql
...
SELECT saldo.usd FROM Cuenta;
```
Muestra cómo acceder a un campo interno del tipo compuesto usando notación de punto (saldo.usd).

## Slide 54

Slide de cierre. "Preguntas?" con imagen decorativa de un muñeco de nieve con bufanda amarilla frente a una casa nevada (misma familia visual humorística que la slide 29).
