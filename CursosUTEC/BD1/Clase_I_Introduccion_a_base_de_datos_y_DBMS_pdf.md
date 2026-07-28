---
curso: BD1
titulo: Clase I - Introducción a base de datos y DBMS
slides: 94
fuente: Clase I - Introducción a base de datos y DBMS.pdf
---

## Slide 1

Portada del curso. Título "CLASE 1: INTRODUCCIÓN", "CS2041- Bases de Datos I", "Ciclo 2024-1". Datos de contacto: Brenner Ojeda (bojeda@utec.edu.pe), Teófilo Chambilla (tchambilla@utec.edu.pe). Menciona "Server Discord" y colaboración con Aidan Hogan de la Universidad de Chile (https://aidanhogan.com/). Decorativa (portada institucional, logo UTEC).

## Slide 2

Slide de agenda con diagrama numerado de 6 puntos dispuestos en 2 columnas x 3 filas, cada uno con su número grande:
1. Metodología del curso
2. ¿Por qué necesitan este curso?
3. ¿Qué es una "base de datos"?
4. ¿Por qué se necesitan sistemas de "bases de datos"?
5. ¿Una base de datos siempre modela datos como tablas?
6. ¿Qué vamos a aprender?

Pie con datos de contacto de los profesores y Server Discord (repetido del slide 1).

## Slide 3

Divisor de sección "1. Acerca del curso — CS2041-Base de datos I". Encabezado "CS2041 Bases de Datos I — Computer Science". Lista de resultados de aprendizaje (4 bullets con checkbox ❏):
- Aplicar conceptos de álgebra relacional y teoría de grafos para generar y optimizar consultas SQL.
- Demostrar optimización de consultas, indexación y transacción con motores open source (PostgreSQL, MongoDB, Cassandra).
- Construir Base de Datos mediante Entidad-Relación, Modelo Relacional, optimización, transacciones y recuperación de información.
- Utilizar algoritmos de optimización de consultas SQL (Hash-Join, Nested-Loop, Merge-Join) mediante índices Hash y Árboles B+.

## Slide 4

Divisor "2. Metodología del curso". Diagrama: "2 horas teoría" + "2 horas Laboratorio" + "2 horas Laboratorio" (tres bloques sumados con signos "+"), ilustrando la carga horaria semanal.

## Slide 5

"Semi-flipped classroom": una cátedra + dos sesiones de laboratorio (ejercicios escritos o con computadoras).

## Slide 6

Detalle de sesiones prácticas: primer laboratorio con archivos de texto plano; en algunos labs se trabaja en grupos de 3-4 (solo en el lab presencial, si no se asiste se trabaja solo); a veces se necesita computador (labs 507/603/301 o notebook personal).

## Slide 7

Sección "Material": las diapositivas se suben antes de cada cátedra a Canvas y son el material canónico. Libro recomendado: "Database Management Systems", Ramakrishnan/Gehrke, Third Edition.

## Slide 8

Política sobre tareas y copias (texto extenso): tareas individuales, prohibido copiar/examinar/alterar trabajo ajeno. Se permite conversar bajo "política de pizarra": no tomar notas/grabar/fotografiar, borrar la pizarra después, y esperar 4 horas antes de empezar la tarea. Recrear de memoria = evidencia de comprensión. Violaciones se reportan a las autoridades.

## Slide 9

"Si todo sale bien…. El profesor pone la pizza". Slide breve/humorística, sin elementos visuales complejos adicionales.

## Slide 10

Tabla "Sistema de Evaluación" con fórmula del promedio final:

| | TEORÍA (T) | LABORATORIO (L) |
|---|---|---|
| | Práctica Calificada PC1 (12%) | Evaluación Continua C1 (7%) |
| | Práctica Calificada PC2 (14%) | Evaluación Continua C2 (8%) |
| | Práctica Calificada PC3 (14%) | Proyecto P1 (10%) |
| | Examen E1 (20%) | Proyecto P2 (15%) |
| **Total** | **60%** | **40%** |

Suma general: 100%. Nota: la ponderación se aplica si ambas partes (T y L) están aprobadas.

## Slide 11

Línea de tiempo de Prácticas Calificadas (tentativa) sobre eje de semanas: PC1 en semana 5 (12%), PC2 en semana 9 (14%), PC3 en semana 13 (14%).

## Slide 12

Línea de tiempo del Proyecto del Curso sobre eje de semanas 1-15: Hito 1 (10%) hacia semana 7, Hito 2 (15%) hacia semana 15.

## Slide 13

Línea de tiempo de Evaluación Continua (semana 7 a 15): incluye Tareas, Ejercicios, Laboratorio, y "Desempeño en clase 15%".

## Slide 14

Advertencia: "No está permitido subir archivos ZIP, no se revisará y es como si no hubiese entregado, su nota es 0."

## Slide 15

Divisor "3. ¿Por qué necesitan este curso?".

## Slide 16

"Un día cualquiera:" — slide título que introduce la secuencia narrativa siguiente (sin imagen propia, es un separador).

## Slide 17

"Un día cualquiera: 09:00 — Despierto". Imagen decorativa (foto de niño bostezando). Texto: "(Bostezo.)"

## Slide 18

"Un día cualquiera: 09:35 — Reviso el avance del COVID-19". Fuente citada: gisanddata.maps.arcgis.com (dashboard de ArcGIS de casos COVID-19), representando interacción con datos/base de datos web.

## Slide 19

"Un día cualquiera: 09:40 — Reviso el correo". Texto: "Nada urgente, ¡uf!"

## Slide 20

"Un día cualquiera: 09:50 — Café: pago con tarjeta". Texto: "Es debito."

## Slide 21

"Un día cualquiera: 10:15 — Me meto al banco (¿me pagaron?)". Texto: "Sí. Me pagaron." (banca online = interacción con base de datos).

## Slide 22

"Un día cualquiera: 10:20 — Reviso canvas (¿alguna tarea?)". Texto: "No, salvo ..."

## Slide 23

"Un día cualquiera: 10:30 — IMDb (The Leftovers... ¿es bueno?)". Texto: "Sí."

## Slide 24

"Un día cualquiera: 10:35 — Amazon (The Leftovers... ¿cuánto cuesta?)". Texto: "Demasiado."

## Slide 25

"Un día cualquiera: 10:36 — ThePirateBay (me pagaron pero...)". Texto: "Listo. Pero tengo hambre..."

## Slide 26

"Un día cualquiera: 10:52 — Al supermercado (¿cuánto cuesta?)". Texto: "Luca."

## Slide 27

"Un día cualquiera: 10:55 — Al supermercado (esperando en la fila...)". Texto: "¿Cero likes?" (revisando redes sociales en el celular).

## Slide 28

"Un día cualquiera: 10:57 — Al supermercado (uso mi tarjeta OH!)". Texto: "¿Acumulas puntos? Sí."

## Slide 29

"Un día cualquiera: 11:00 — Desayuno". Imagen decorativa de sándwich. Texto: "…"

## Slide 30

"Un día cualquiera: antes de las 11:00 — ¿Estas actividades tienen algo en común?" Slide de transición/pregunta retórica que cierra la secuencia narrativa.

## Slide 31

"Bases de datos: Interactuamos con bases de datos todo el tiempo, todos los días". Lista con viñetas, "especialmente con la Web":
- Búsqueda (Google, Bing, Yahoo!, …)
- Tiendas (Amazon, eBay, …)
- Redes sociales (Facebook, Twitter, …)
- Enciclopedias (Wikipedia, IMDb, …)
- Bancos
- Aerolíneas
- Canvas/EDU

## Slide 32

"Un buen mercado laboral — 'Data Scientist': Ofertas de Trabajo". Referencia a imagen/gráfico de ofertas laborales para Data Scientist, fuente citada: CrowdFlower Data Science Report 2016 (visit.crowdflower.com).

## Slide 33

"¿Cúal es la tendencia?" Dato destacado: "En 2020, cada persona generó 1,7 megabytes de datos en solo un segundo."

## Slide 34

Divisor "4. ¿Qué es una 'base de datos'?".

## Slide 35

"¿Una base de datos?" con subtítulo "Un ejemplo de una base de datos?" — slide de transición sin contenido visual adicional relevante (repetido varias veces como pregunta retórica antes de mostrar ejemplos).

## Slide 36

"¿Una base de datos?" — repetición de la pregunta (slide de transición, sin contenido visual nuevo).

## Slide 37

"¿Una base de datos?" — repetición de la pregunta (slide de transición).

## Slide 38

"¿Una base de datos?" — repetición de la pregunta (slide de transición).

## Slide 39

"¿Una base de datos?" — repetición de la pregunta (slide de transición).

## Slide 40

"¿Una base de datos?" — repetición de la pregunta (slide de transición).

## Slide 41

"¿QUÉ ES UNA 'BASE DE DATOS'?" con respuesta grande: "DEPENDE…" Slide de énfasis tipográfico (texto grande centrado), sin diagramas.

## Slide 42

"Aquí, una base de datos es:" — definición con jerarquía visual por color:
- "Una colección de datos" (subrayado, en azul, como hipervínculo/énfasis)
  - "(típicamente datos estructurados)"
  - "(típicamente datos electrónicos)"
- "organizada" (en naranja) "en alguna forma"
- "para facilitar" "hacer consultas" (en verde)
- "de" "una forma eficiente" (en morado)

## Slide 43

"¿Una base de datos?" — captura de pantalla de una tabla de datos tipo hoja de cálculo/base de datos con columnas PersonID, Address (duplicada), City (duplicada), FirstName (duplicada), LastName — 16 filas de datos de personas con direcciones en San Francisco (Plateau City, Excelsior, Embarcadero, Tenderloin, Cow Hollow, North Beach, Miraloma Park, etc.). Interfaz con barra de herramientas (íconos de edición). Al pie, en verde grande: "(hablando de los datos, no la aplicación …) ¡Aquí, sí!" — indica que ESTA tabla de datos SÍ cuenta como "base de datos".

## Slide 44

"¿Una base de datos?" — logos de sistemas de gestión de bases de datos: Oracle, MySQL (delfín), SQLite, MongoDB (hoja verde), Cassandra (ojo). Al pie en rojo: "(es un sistema de base de datos entonces …) Aquí, no!" — distingue que estos son SISTEMAS (DBMS), no la base de datos en sí.

## Slide 45

Divisor de transición "Un sistema de bases de datos es:" — introduce la definición formal, texto plano preparatorio antes del slide de definición completa.

## Slide 46

"Un sistema de bases de datos es:" definición completa con jerarquía de color:
- "Un sistema" "(de software)" "general" (azul) para "manejar" (naranja) "bases de datos" (verde) …
- "Facilitan (en una forma general):" (rojo) representar/cargar/organizar/definir/actualizar/consultar datos…
- "DBMS: (DataBase Management System)"

## Slide 47

"Un sistema general implica que podamos resolver un problema general …" — slide de transición textual.

## Slide 48

"¿Una base de datos?" — captura de pantalla de la web de IMDb (barra de navegación, sección "Opening This Week" con trailers de películas 'Max Steel', 'Mascots', 'Shut In', panel "Now Playing / Box Office" con recaudación). Al pie en rojo: "(es una aplicación de base de datos entonces …) Aquí, no!" — la app IMDb no es la base de datos en sí.

## Slide 49

"¿Una base de datos?" — captura de pantalla del buscador de Google (logo, caja de búsqueda, botones "Buscar con Google"/"Me siento con suerte"). Al pie en rojo: "(es una aplicación de base de datos entonces …) Aquí, no!"

## Slide 50

"¿Una base de datos?" — foto de un quipu andino (cuerdas anudadas de colores colgando, sistema de registro incaico). Al pie: "???" en naranja — pregunta abierta sobre si un quipu cuenta como base de datos (sistema de registro de datos no digital).

## Slide 51

Divisor de sección con fondo foto de edificio UTEC en tono azul: "¿POR QUÉ SE NECESITAN SISTEMAS DE 'BASES DE DATOS'?" Encabezado "CS2041 Bases de Datos I — Teófilo Chambilla Aquino".

## Slide 52

"Sé programar en C++, sé programar en Python, … ¡puedo programar algo sin problema!" Imagen meme de un "hacker" con laptop mostrando texto invertido "3133t H4x0r" y "FREE KEVIN" (referencia a Kevin Mitnick), tono humorístico sobre sobreconfianza técnica.

## Slide 53

"Intentemos implementar una aplicación sin un sistema de bases de datos (p.ej., en C++)". Ilustración: ícono de base de datos (cilindros apilados) junto al logo de C++.

## Slide 54

"Tenemos información de profesores, auxiliares, alumnos y notas parciales en cada curso" — presenta 4 tablas CSV en recuadros de colores distintos:

**profesores.csv** (borde rojo)
| Dni | Nombre | Curso |
|---|---|---|
| 40142153 | Ernesto Cuadros Vargas | CS1100 |
| 42440124 | Teófilo Chambilla Aquino | CS2701 |
| 45142154 | Heider Sanchez Enriquez | CS1102 |
| 45142154 | Maria Hilda Bermejo Rios | CS2701 |

**alumnos.csv** (borde azul)
| Código | Nombre | Curso |
|---|---|---|
| 201710042 | Molina Orellana Diego | CS1100 |
| 201710043 | Paredes Sanchez Bruno | CS2701 |
| 201710044 | Perez Fu Luis Adrian | CS1102 |
| 201710044 | Perez Fu Luis Adrian | CS2701 |

**auxiliares.csv** (borde verde)
| Código | Nombre | Curso |
|---|---|---|
| 201710001 | Peña Mendoza Alejandro | CS1100 |
| 201710033 | Quesada Velarde Luis | CS2701 |
| 201710066 | Quispe Roldan Enrique | CS1102 |
| 201710077 | Peña Cordova Diana | CS2701 |

**cursos.csv** (borde gris)
| Código | Nombre |
|---|---|
| CS2701 | Base de datos I |
| CS1102 | Programación Orientada a O |
| CS1100 | Introducción a ciencia de la C. |

**notas.csv** (borde naranja)
| Código | Nombre | Eval | Nota |
|---|---|---|---|
| 201710043 | CS2701 | Lab 1 | 17 |
| 201710043 | CS2701 | Lab 2 | 18 |
| 201710044 | CS1102 | Examen | 11 |
| 201710045 | CS2701 | Proyecto | 15 |

También incluye un screenshot pequeño de la interfaz de Canvas (bandeja de mensajes/foro).

## Slide 55

"Queremos saber todos los códigos del cursos que toma el alumno '201710044'". Tabla **alumnos.csv** (misma estructura que slide 54: Código/Nombre/Curso, mostrando 201710042-201710044). Texto: "En C++, podemos leer todo el archivo, filtrar todas las filas con otros códigos y entregar sola la información relevante". Recuadro punteado: "¿Algún problema aquí?"

## Slide 56

"Bueno, si los usuarios son impacientes y los archivos grandes …" Diagrama "Mapa en memoria principal de alumnos.csv" — tabla Clave→Valor:
| Clave | Valor |
|---|---|
| 201710042 | { (Molina Orellana Diego, CS1100) } |
| 201710043 | { (Paredes Sanchez Bruno, CS2701) } |
| 201710044 | { (Perez Fu Luis Adrian, CS1102), (Perez Fu Luis Adrian, CS2701) } |

Texto: "En C++, podemos cargar los datos en memoria principal, y utilizar un índice con códigos como claves (p.e., un 'map')". Recuadro: "¿Algún problema aquí?"

## Slide 57

"Bueno, si los usuarios son impacientes y los archivos no caben en memoria …" Diagrama con dos tablas conectadas por flechas: **Índice (m. principal)** [Código→Bloque: 201710042→1, 201710044→2] apunta a **alumnos.csv** (bloques de filas ordenadas por Código). Texto: "En C++, podemos crear bloques de datos ordenados por Código, y utilizar un índice con el primer Código en cada bloque". Recuadro: "¿Algún problema aquí?"

## Slide 58

"Bueno, si tenemos que actualizar la tabla con datos nuevos …" Diagrama con **Índice (m. principal)** apuntando a **alumnos.csv** que ahora tiene columna adicional "Del?" (marca "x" para filas borradas lógicamente), más un recuadro aparte **Inserciones (m. principal)** con fila nueva (201710044, Perez Fu Luis Adrian, CS2804). Texto: "En C++, podemos crear un bloque en memoria principal, o podemos dejar espacio en los bloques para datos nuevos o …". Recuadro: "¿Algún problema aquí?"

## Slide 59

"Bien, si a veces hay que consultar por el nombre del alumno entonces …" Diagrama con el índice anterior (por Código) atenuado/en segundo plano, y un nuevo **Índice (m. principal)** por Nombre→Bloque (Molina Diego→1, Paredes Bruno→2) apuntando a la tabla alumnos.csv con columna Del?. Texto: "En C++, podemos crear otro índice ordenado por nombre …". Recuadro: "¿Algún problema aquí?"

## Slide 60

"ok ok, si a veces hay que consultar por el nombre de los cursos del alumno entonces …" Dos tablas lado a lado: **alumnos.csv** (indexado por Código y Nombre) y **cursos.csv** (indexado por Código). Texto: "En C++, podemos crear otro índice para cursos.csv e implementar 'joins' entre ambos índices". Recuadro: "¿Algún problema aquí?"

## Slide 61

"… uum, si hay que verificar que los alumnos solo tengan cursos que aparecen en cursos.csv …" Mismas dos tablas indexadas. Ejemplo de código/pseudocódigo:
```
INSERT alumnos.csv   (201710044, Perez Fu Luis Adrian, CS1100)   ✓
INSERT alumnos.csv   (201710044, Perez Fu Luis Adrian, CS2801)   ✗
```
Texto: "En C++, antes de hacer una inserción a alumnos.csv, podemos consultar a cursos.csv para verificar que el curso exista." Recuadro: "¿Algún problema aquí?"

## Slide 62

"… pues, si hay que permitir quitar cursos …" Mismas tablas indexadas. Pseudocódigo:
```
DELETE alumnos.csv   (201710044, Perez Fu Luis Adrian, CS1100)
DELETE cursos.csv    (CS2701, Base de datos I)
```
Texto: "En C++, podemos agrupar inserciones y/o borrados para mantener la consistencia de los datos (transacciones)". Recuadro: "¿Algún problema aquí?"

## Slide 63

"… si hay múltiplos usuarios actualizando la base de datos al mismo tiempo …" Mismas tablas indexadas con un ícono de rayo (⚡, conflicto) entre dos secuencias concurrentes de operaciones:
```
DELETE alumnos.csv (201710044,Perez Fu Luis Adrian, CS1100)   |   INSERT alumnos.csv (201710044,Perez Fu Luis Adrian, CS1100)
DELETE cursos.csv (CS2701, Base de datos I)
```
Texto: "En C++, hay que aislar transacciones para evitar este tipo de situación (y otras similares)". Recuadro: "¿Algún problema aquí?"

## Slide 64

"… si hay que contar el número de cursos que cada alumno toma u otra formas de consultas …" Mismas tablas indexadas. Consulta SQL de ejemplo con ícono de engranajes:
```sql
SELECT codigo, COUNT(curso) FROM alumnos GROUP BY codigo
```
Texto: "En C++, podemos implementar un lenguaje de consulta general que cubre los rasgos más necesitados". Recuadro: "¿Algún problema aquí?"

## Slide 65

"… si el rendimiento de consultas no basta para los usuarios, podemos optimizar …" Mismo diagrama y consulta SQL que slide 64 (repetido), con ícono de engranajes. Texto: "En C++, podemos implementar varias optimizaciones en un planificador de ejecución". Recuadro: "¿Algún problema aquí?"

## Slide 66

Slide de remate cómico: emoticon ASCII "(╯°□°）╯︵ ┻━┻" (mesa volteada de frustración) y "¡Sí!". Recuadro naranja con mensaje de error real: `'utf-8' codec can't decode byte 0xed in position 417: invalid continuation byte` (simula un error de encoding real). Lista extensa de problemas adicionales que van apareciendo al intentar programar todo a mano en C++:
- A veces, faltan valores en las tablas
- Cursos pueden tener más que un nombre
- Hay valores como fechas, booleanos, etc. que se quieren comparar, ordenar, manipular, sumar
- El rendimiento de algunas consultas todavía es terrible
- La carga de datos todavía es demasiado lento
- No hay suficiente memoria para mantener los índices
- Los administradores quieren agregar columnas nuevas como la carrera de los alumnos
- Los alumnos no deberían tener acceso para cambiar sus notas
- Hay "l33t h4cker$" que quieren "pwnear" la base de datos para cambiar sus notas
- Tenemos que mantener respaldos en una forma segura
- "You won't see this so I can write it in English." (broma del profesor)

## Slide 67

"… y si pudiéramos solucionar estos problemas de una forma general …" Dos imágenes: ícono de base de datos con engranaje (izquierda) y una bicicleta con ruedas triangulares (derecha, imagen absurda que simboliza "reinventar la rueda" mal). Texto grande: "… habríamos implementado un sistema de bases de datos".

## Slide 68

"Estos son problemas generales que se encuentran en muchas aplicaciones" — repite el collage de 12 fotos "Un día cualquiera" (mismo grid que slide 17-29, con cilindros de base de datos superpuestos a cada foto), reforzando que cada interacción cotidiana usa una base de datos.

## Slide 69

"… muchas aplicaciones importantes". Screenshot del homebanking BBVA Continental ("Un día cualquiera: 10:15 — Me meto al banco (me pagaron?)", con login DNI/contraseña, ofertas de tarjeta de crédito) y, a la derecha, de nuevo la imagen de la bicicleta de ruedas triangulares.

## Slide 70

"Un sistema de bases de datos es:" — repetición exacta de la definición formal del slide 46 (mismo texto y jerarquía de color): sistema general para manejar bases de datos, facilita representar/cargar/organizar/definir/actualizar/consultar datos, DBMS.

## Slide 71

"Con un DBMS …" — "Los usuarios se encargan de:" diseñar la estructura de la base de datos, escribir consultas, actualizar los datos, etc. Texto en naranja: "… solo las cosas específicas en el contexto de la aplicación específica."

## Slide 72

"Con un DBMS …" — "Por debajo, el DBMS se encarga de:" Almacenaje optimizado, Indexación, Procesamiento de consultas, Optimización de consultas, Manejo de transacciones, Manejo de acceso concurrente, Seguridad, "¡y mucho más!". Texto en azul: "… las cosas generales que se necesitan en muchas aplicaciones."

## Slide 73

"Hay implementaciones con décadas de desarrollo por miles de expertos". Imagen decorativa de una motocicleta futurista/muy elaborada (Dodge Tomahawk) con palmeras de fondo, metáfora visual de sofisticación técnica acumulada.

## Slide 74

"Pero DBMS están siempre evolucionando: tecnología cambia". Diagrama con flechas azules mostrando evolución del almacenamiento: cinta magnética (unidad HP StorageWorks) → disco duro mecánico (Seagate, abierto mostrando platos y cabezal) → memoria flash SSD (placa con chips de memoria).

## Slide 75

"Pero DBMS están siempre evolucionando: los requisitos de las aplicaciones cambian". Grid de logos "rotos"/agrietados (efecto gráfico de rajadura) de aplicaciones: entre otros, Facebook, Google, LinkedIn, Flickr, Waze, Uber, y un logo de "Sistema Académico" — simboliza la presión de nuevos requisitos sobre los DBMS.

## Slide 76

Divisor de sección con fondo de mano robótica sobre mapa del mundo (imagen de stock genérica "Reinventa el mundo"): "5. ¿Una base de datos siempre modela datos como tablas?"

## Slide 77

"… ¿son siempre modelados así?" — repite las 4 tablas CSV (profesores, alumnos, auxiliares, cursos, notas) igual que en slide 54, más el screenshot de Canvas, para reforzar el modelo tabular ya visto.

## Slide 78

"¿Se puede modelar una base de datos como un mapa?" Diagrama Clave→Valor (repetido del slide 56) a la izquierda. A la derecha, tabla de ejemplos genéricos de sistemas clave-valor:

| Contexto | Key | Value |
|---|---|---|
| Directory | Company (Algo-Logic) | Phone # ((408) 707-3740) |
| Forwarding Tables | IP Address (204.2.34.5) | Interface:MAC Address (Eth6:02:33:29:F2:AB:CC) |
| Data De-duplication | Content Hash (XYZ) | Storage Block ID (948830038411) |
| Stock Trading | Order ID (ATY11217911101) | Symbol,Side,Price (AAPL,B,126.75) |
| Graph Search | Vertex (v140) | Edge List (v201,v206,v225) |

Respuesta en verde: "¡Sí!"

## Slide 79

"¿Se puede modelar una base de datos como un árbol?" Diagrama de árbol jerárquico de HTML: `<html>` → `<head>`/`<body>`; `<head>`→`<title>`; `<body>`→`<h1>`,`<p>`,`<h2>`,`<table>`,...; `<table>`→`<tr>`,`<tr>`,...; `<tr>`→`<th>`,`<td>`. A la derecha, ejemplos de código JSON y XML representando la misma estructura de "siblings" (Anna/Alex Clayton):
```json
{"siblings": [{"firstName":"Anna","lastName":"Clayton"}, {"lastName":"Alex","lastName":"Clayton"}]}
```
```xml
<siblings><sibling><firstName>Anna</firstName><lastName>Clayton</lastName></sibling>
<sibling><firstName>Alex</firstName><lastName>Clayton</lastName></sibling></siblings>
```
Respuesta en verde: "¡Sí!"

## Slide 80

"¿Se puede modelar una base de datos como un grafo?" Diagrama de grafo de conocimiento (knowledge graph): nodo "WilliamGolding" conectado por relaciones "awarded"→"NLP1983"→("year"→"1983", "type"→"NobelLiteraturePrize", "accepted"→"true"); "fought"→"NormandyInv"→"partOf"→"OpOverlord"→"partOf"→"WorldWarII". Superpuesto, una red social de nodos con fotos de personas conectadas por líneas (visualización de grafo social multicolor). Respuesta en verde: "¡Sí!"

## Slide 81

"Bases de Datos Relacional" — texto sobre fondo atenuado (watermark) de las tablas CSV anteriores. Bullets: Tablas = un modelo de bases de datos (bases de datos relacionales); el modelo más establecido; el enfoque del curso; se hablará brevemente de otros modelos.

## Slide 82

Divisor de sección (mismo estilo visual que slide 76, mano robótica sobre mapa): "6. Una diversidad de tipos de (sistemas de) bases de datos".

## Slide 83

"Los sistemas más utilizados en la práctica …" Captura de tabla del ranking DB-Engines (marzo 2022, 388 sistemas en el ranking), columnas Rank (Mar/Feb/Mar), DBMS, Database Model, Score (Mar/Feb/Mar con variación). Primeras filas relevantes:

| Rank | DBMS | Modelo | Score Mar 2022 |
|---|---|---|---|
| 1 | Oracle | Relational, Multi-model | 1251.32 |
| 2 | MySQL | Relational, Multi-model | 1198.23 |
| 3 | Microsoft SQL Server | Relational, Multi-model | 933.78 |
| 4 | PostgreSQL | Relational, Multi-model | 616.93 |
| 5 | MongoDB | Document, Multi-model | 485.66 |
| 6 | Redis | Key-value, Multi-model | 176.76 |
| 7 | IBM Db2 | Relational, Multi-model | 162.15 |
| 8 | Elasticsearch | Search engine, Multi-model | 159.95 |
| 9 | Microsoft Access | Relational | 135.43 |
| 10 | SQLite | Relational | 132.18 |
| 11 | Cassandra | Wide column | 122.14 |
| 19 | Neo4j | Graph | 59.67 |

(tabla continúa hasta rank 36; incluye también MariaDB, Splunk, Snowflake, Azure SQL, DynamoDB, Hive, Teradata, Solr, SAP HANA, FileMaker, BigQuery, HBase, Cosmos DB, PostGIS, InfluxDB, Couchbase, Firebird, Redshift, Memcached, Informix, Spark SQL, Azure Synapse, Vertica). Fuente: http://db-engines.com/en/ranking

## Slide 84

Divisor de sección (mismo estilo mano robótica): "7. ¿Qué vamos a aprender?".

## Slide 85

"Una introducción a bases de datos:" Lista numerada de 3 tipos de usuarios de un sistema de bases de datos: 1. Usuarios finales (azul), 2. Administradores del sistema (naranja), 3. Desarrolladores de un sistema (verde). Ícono decorativo de un personaje "ninja" con laptop. Texto: el curso se enfoca en el primer tipo (incluye desarrolladores de aplicaciones de bases de datos), y se hablará un poco de los tipos 2 y 3.

## Slide 86

"En este curso, aprenderán": cómo generalizar consulta/indexación/gestión de datos; modelos de bases de datos (énfasis en el modelo relacional; otros modelos: grafos, árboles, NoSQL); usar y manejar sistemas de bases de datos (cargar datos, escribir consultas, actualizar datos).

## Slide 87

"No aprenderán (específicamente)": rasgos específicos de todos los sistemas; cómo implementar un sistema de bases de datos en detalle; minería de datos; sistemas distribuidos en detalle; Datalog/lógica/teoría en detalle; Big data en detalle.

## Slide 88

"La estructura del curso" — lista del temario: Introducción/Motivación, Entidades/Relaciones, El Modelo Relacional, El Álgebra Relacional, SQL (consultas), Indexación/Optimización, SQL (actualizaciones), Formas Normales, Transacciones, Otros Modelos (Base de datos no relacional: JSON; Base de datos en Grafos: SPARQL). Ícono decorativo del personaje ninja cargando una pila de libros.

## Slide 89

"¿Preguntas?" Imagen decorativa de un bote a la deriva en un mar tormentoso hecho de números binarios (0s y 1s), con un ícono dorado de base de datos dentro del bote — metáfora visual de "navegar" el mundo de los datos.

## Slide 90

Slide final de cierre: "GRACIAS" sobre fondo azul con foto de dos personas trabajando en laboratorio (decorativa). Incluye un código QR (bitly) para el Server Discord. Datos de contacto: Brenner Ojeda (bojeda@utec.edu.pe), Teófilo Chambilla (tchambilla@utec.edu.pe). Créditos: "En colaboración Aidan Hogan de la Universidad de Chile" con logo del Departamento de Ciencias de la Computación (DCC) de dicha universidad. Nota: aunque el índice de imágenes numera hasta 94 páginas, el contenido sustantivo de la presentación termina en esta slide de agradecimiento (página física 90); las páginas 91-94 corresponden a slides adicionales detectadas en el archivo de imágenes, documentadas a continuación.

## Slide 91

"No aprenderán (específicamente)" — mismo contenido que slide 87 (rasgos específicos de todos los sistemas; implementación de un DBMS en detalle; minería de datos; sistemas distribuidos en detalle; Datalog/lógica/teoría en detalle; Big data en detalle). Aparente duplicado/reordenamiento de slide en el PDF exportado.

## Slide 92

"La estructura del curso" — mismo contenido que slide 88 (temario completo con ícono del ninja cargando libros). Duplicado.

## Slide 93

"¿Preguntas?" — mismo contenido que slide 89 (bote a la deriva en mar de números binarios con ícono dorado de base de datos). Duplicado.

## Slide 94

Slide final "GRACIAS" — mismo contenido que slide 90 (fondo azul, foto de laboratorio, QR de Discord, contactos de los profesores, crédito a Aidan Hogan y logo DCC Universidad de Chile). Duplicado, cierre definitivo de la presentación.
