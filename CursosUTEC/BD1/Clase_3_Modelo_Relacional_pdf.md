---
curso: BD1
titulo: Clase 3_ Modelo Relacional
slides: 86
fuente: Clase 3_ Modelo Relacional.pdf
---

## Slide 1
Portada del curso. Título "CLASE 3: MODELO RELACIONAL" / "CS2041- Bases de Datos I" / "Ciclo 2024-1". Autores: Brenner Ojeda (bojeda@utec.edu.pe), Teófilo Chambilla (tchambilla@utec.edu.pe). Colaboración de Aidan Hogan (Universidad de Chile). Fondo decorativo de túnel tecnológico azul con figura humana caminando; logos UTEC, TransformaTEC y DCC Universidad de Chile — decorativo.

## Slide 2
Slide de progreso del curso "Base de Datos I, Ciclo 2024-1". Barra de progreso horizontal con 7 segmentos: Introducción, **Modelo Relacional** (resaltado en azul, sección actual), Algebra Relacional, y 4 segmentos vacíos sin etiqueta visible salvo "Entidad - Relación" debajo del segundo bloque. Ilustración decorativa de mascota ninja UTEC y pila de libros con bandera de meta.

## Slide 3
Slide de índice (fondo gris oscuro). Título "Índice". Lista:
- Resumen clase 2.
- Transformación de ER
- Modelo Relacional
- Ejemplos

## Slide 4
Slide de transición de sección. Título "Resumen: Clase ...2", subtítulo "Entidad Relación".

## Slide 5
"Resumen clase anterior" — Diagrama entidad-relación (ER) completo con 3 grupos:
1. Producto —(fabrica)— Compañía: Producto tiene atributos nombre (subrayado, clave), categoría, precio; relación "fabrica" (rojo) tiene atributo "desde"; Compañía tiene atributos nombre (subrayado) y valor-acción.
2. Película —(arriendo)— Local de videos —(arriendo)— Persona: relación ternaria "arriendo" conecta las tres entidades.
3. Bebida con atributos nombre (subrayado), origen, typo; dos triángulos "IsA" (verde) que la especializan en Vino (con atributo año) y Cerveza.

## Slide 6
"Conceptos". Presenta los símbolos gráficos del modelo ER con ejemplos: Entidades = rectángulos azules (Producto, Compañía); Atributos de entidades = óvalo amarillo (nombre); Relaciones entre entidades = rombo rojo (fabrica).

## Slide 7
"Otros tipos de atributos:" Diagrama tipo mapa mental centrado en un rectángulo "ENTIDAD" conectado a 4 óvalos: "Atributo" (arriba izq.), "Atributo Multivaluado" (óvalo doble, arriba der.), "Atributo de Entidad Débil" (abajo izq.), "Atributo Clave" (subrayado, abajo centro), "Atributo Derivado" (óvalo punteado, der.).

## Slide 8
Slide de transición con mascota ninja apuntando. Texto: "¿Para qué necesitamos E–R?" — sin contenido adicional, es pregunta introductoria.

## Slide 9
Imagen decorativa: fotograma de película de una clase magistral universitaria frente a una pizarra llena de fórmulas físico-matemáticas (referencia visual, no contenido del curso) — decorativa.

## Slide 10
"¿Para qué necesitamos E–R?" Lista con 4 puntos:
- Modelar los requerimientos de una aplicación (sub-punto: en forma menos técnica que usar tablas)
- Evitar redundancia / lograr un modelo conciso
- Documentar restricciones conceptuales
- Evitar problemas (p.ej. con llaves)

## Slide 11
"Modelo Relacional" — Presentación histórica. Texto: "Formalizado por Edgar F. Codd (IBM) en 1969". Fotografía en blanco y negro de Edgar F. Codd.

## Slide 12
"Modelo Relacional: Conceptos". Tabla de ejemplo "Cervezas" con columnas nombre, tipo, grados, ciudad-Origen y 8 filas (Abraxas/Ale Ultra/7,0/Lima; Pilsen Trujillo/Lager/4,6/Trujillo; Pilsen Callao/Lager/4,8/Lima; Cristal/Lager/4,8/Lima; Cusqueña Dorada/Lager/4,8/Cusco; Backus Ice/Lager/4,25/Lima; Arequipeña/Pilsener/4,6/Arequipa; San juan/Pilsener/4,6/Pucallpa). Define: **Relación** = cada tabla (ej. Cervezas), **Atributo** = cada columna (nombre, tipo, grados, ciudad-origen), **Tupla** = cada fila (ej. fila de Cristal).

## Slide 13
"Modelo Relacional: Esquema". Misma tabla Cervezas. Notación de esquema: `Cervezas(nombre,tipo,grados,ciudad-origen)`. Un esquema es un conjunto de relaciones, ejemplo en recuadro naranja:
```
Cervezas(nombre,tipo,grados,ciudad-origen)
Vinos(nombre,tipo,año,grados,ciudad-origen)
En-Stock(nombre,cantidad,precio-unitario)
```

## Slide 14
"Modelo Relacional: Esquema" (continuación). Mismo esquema de 3 relaciones. Pregunta "¿La repetición de los nombres de atributos... es un problema?" Respuesta: No, pero se podría desambiguar con notación `Cervezas_nombre`, `Vinos_nombre`.

## Slide 15
"Modelo Relacional: Dominio". Tabla Cervezas repetida. Se anota que cada atributo tiene un dominio (tipo de dato), mostrado como:
```
Cervezas(nombre:string,tipo:string,grados:float,ciudad-origen:string)
Vinos(nombre:string,tipo:string,año:int,grados:float,ciudad-origen:string)
En-Stock(nombre:string,cantidad:int,precio-unitario:int)
```

## Slide 16
"Modelo Relacional: Instancia". Define: una instancia de un esquema es un conjunto de tuplas para cada relación. Muestra el esquema con dominios (recuadro naranja) y tres tablas de datos: Cervezas (6 filas, sin Cusqueña ni San Juan comparado con el original... en realidad tiene 6 filas: Abraxas, Pilsen Trujillo, Pilsen Callao, Cristal, Arequipeña, San juan), Vino (tabla nueva: Tarapacá/Carménère/2014/13,5/Maipo; Tarapacá/Merlot/2014/13,5/Maipo; Gato/Merlot/2016/14,0/Maule), y En-Stock (vacía, solo encabezados).

## Slide 17
"Modelo Relacional: Instancia" (continuación). Fotografía de una góndola de supermercado vacía con carteles de "Vodka" y ofertas — ilustra que el stock puede estar vacío. Debajo las mismas 3 tablas (Cervezas, Vino, En-Stock vacía) y la nota "el conjunto puede ser vacío" resaltada en amarillo junto a En-Stock.

## Slide 18
"Modelo Relacional: Instancia". Pregunta "¿Cuáles son las consecuencias de esta definición?" Respuesta en recuadro verde: 1. No hay orden en las filas. 2. No se puede tener filas duplicadas. Nota al pie: "(SQL hace algo diferente)".

## Slide 19
"Modelo Relacional: Instancia". Repite las 3 tablas con datos (Cervezas con 6 filas, Vino con 3 filas Tarapacá/Tarapacá/Gato, En-Stock vacía) como ejemplo consolidado de instancia.

## Slide 20
"Modelo Relacional: Restricciones". Definición formal: "Restricciones (de integridad): son restricciones formales que imponemos a un esquema que todas sus instancias deben satisfacer" — texto centrado con jerarquía visual en cascada.

## Slide 21
"Modelo Relacional: Restricciones (Llaves)". Imagen decorativa de una colección de llaves antiguas decorativas — decorativa (ilustra el tema "llaves" de forma metafórica).

## Slide 22
"Modelo Relacional: Restricciones (Llaves)". Define súper llave: "Un conjunto de atributos de una relación forma una súper llave si no permitimos que existan dos (o más) tuplas para esa relación con los mismos valores en todos los atributos de la llave" — texto en cascada con colores por concepto.

## Slide 23
Tabla Cervezas (8 filas completa). Pregunta "¿Una súper llave?" (sin responder aún en esta slide).

## Slide 24
Misma tabla Cervezas. Pregunta "¿Entonces la siguiente es una súper llave? {nombre, tipo, grados, ciudad-origen}" Respuesta: "Sí."

## Slide 25
Tabla Cervezas con columnas reordenadas (nombre, tipo, grados, ciudad-Origen). Pregunta "¿Ok, entonces la siguiente es una súper llave? {tipo, grados, ciudad-origen}" Respuesta: "No." (porque Pilsen Trujillo y ninguna otra fila comparte tipo/grados/ciudad, pero el ejemplo remarca que esto no identifica de forma única, ya que otras combinaciones repiten valores).

## Slide 26
Define llave candidata: "Un conjunto de atributos de una relación forma una llave candidata si es una súper llave y no hay un subconjunto propio de esos atributos que es una súper llave."

## Slide 27
Tabla Cervezas. Pregunta "¿Cuál es la llave candidata más natural aquí?" (sin resolver en esta slide).

## Slide 28
Tabla Cervezas. Pregunta "¿Entonces la siguiente es una llave candidata? {nombre,tipo,grados,ciudad-origen}" Respuesta: "¡No! Es una súper llave pero hay un subconjunto propio que es una súper llave. Entonces no es una llave candidata."

## Slide 29
Tabla Cervezas. Pregunta "¿Hay otra llave candidata?" Respuesta: "No. ... no es una llave candidata." (continuación del razonamiento sobre {nombre,tipo,grados,ciudad-origen}).

## Slide 30
Tabla "Vino" con columnas nombre, tipo, año, grados, ciudad-origen y 3 filas (Tarapacá/Carménère/2014/13,5/Maipo; Tarapacá/Merlot/2014/13,5/Maipo; Gato/Merlot/2016/14,0/Maule). Pregunta "¿Cuál es la llave candidata aquí?" Respuesta: `Vino(nombre,tipo,año,grados,ciudad-origen)` (todos los atributos juntos). Pregunta abierta al pie: "¿Algún problema aquí?"

## Slide 31
Misma tabla Vino, con una fila nueva resaltada en naranja (Tarapacá/Merlot/2015/13,5/Maipo — mismo nombre y tipo que otra fila pero año distinto). Se remarca que la llave candidata podría ser también `{nombre,tipo,año,grados,ciudad-origen}` y la lección: "¡Una llave es una restricción definida, no una descripción de los datos actuales!"

## Slide 32
Recuadro naranja con el esquema `Vino(nombre,tipo,año,grados,ciudad-origen)`. Tabla Vino con las dos primeras filas idénticas en nombre resaltadas con rectángulo rojo punteado (Tarapacá/Carménère/2014 y Tarapacá/Merlot/2014 — mismo nombre "Tarapacá" pero distinto tipo). Pregunta "¿Es una instancia del esquema?" Respuesta: "No." (porque {nombre} solo no sería suficiente si fuera la llave, pero aquí se ilustra un caso límite).

## Slide 33
Ejemplo con esquema `Persona(dni,nombre,fecha-de-nacimiento,madre-dni,padre-dni)`. Pregunta "¿Intuitivamente, hay otra llave candidata?" Dos posibles respuestas mostradas en recuadros: "Probablemente..." con {nombre,fecha-de-nacimiento,madre-dni} subrayado como llave candidata alternativa a dni; "...o puede ser..." con {nombre,fecha-de-nacimiento,padre-dni}, con nota "(si no tenemos un tipo como Gengis Kan)" — chiste sobre gente con múltiples hijos/madres compartidas rompiendo la unicidad.

## Slide 34
Resumen de conceptos de llaves con el ejemplo Persona repetido tres veces (súper-llave, llave candidata, llave primaria):
- Súper-llave identifica cada fila: `Persona(dni,nombre,fecha-de-nacimiento,madre-dni,padre-dni)` (dos variantes subrayadas distintas)
- Llave candidata es una súper llave mínima (mismo esquema, subrayados distintos)
- Se escoge una de las llaves candidatas como llave primaria: `Persona(dni,...)` con dni subrayado

## Slide 35
Slide de transición, texto centrado: "Un problema con el vino" — introduce la sección siguiente.

## Slide 36
"Modelo Relacional: Restricciones". Tabla En-Stock (solo encabezados: nombre, cantidad, precio-unitario). Pregunta "¿Cuál es la llave primaria más natural? (Hay que pensar en el futuro también)" y propuesta `En-Stock(nombre,cantidad,precio-unitario)`. Debajo, resaltado en rojo con bordes punteados, se muestran las tablas Cervezas y Vino con las filas "Tarapacá" repetidas (incluyendo cerveza sin nombre en la fila subrayada) marcando el problema: el nombre no es único entre cervezas y vinos combinados.

## Slide 37
Slide de transición semitransparente (fade), repite el contenido de la slide 36 desvanecido, con el texto destacado "¿Cómo podemos solucionar este problema?" — muestra ejemplo adicional con cervezas "Austral Lager", "Austral Yagan", "Kross Golden", "Kross Pilsner" de Punta Arenas y Curacaví para ilustrar más colisiones de nombres.

## Slide 38
"Solución 1: ¿Un nombre de vino más específico?" Esquema:
```
Cervezas(nombre,tipo,grados,ciudad-origen)
Vinos(nombre,tipo,año,grados,ciudad-origen)
En-Stock(nombre,cantidad,precio-unitario)
```
Tabla Vino con nombres compuestos: "Tarapacá Carménère 2014", "Tarapacá Merlot 2014", "Gato Merlot 2016". Tabla En-Stock con una fila: "Tarapacá Carménère 2014" / 200 / 6000.

## Slide 39
"Solución 2: ¿Un atributo nuevo: id? (¿p.ej., el código de barras?)". Esquema con id agregado a las 3 tablas. Tabla Cervezas con columna id (CAuL00, CAuY00...). Tabla Vino con id (VTTC14, VTTM14, VTGM16). Tabla En-Stock con id (CAuL00/600/2000, VTTC14/200/6000).

## Slide 40
"Solución 3: ¿Una tabla "En-Stock" para vino y cerveza?" Esquema separado en 4 tablas: Cervezas, Vinos, Cerveza-En-Stock, Vino-En-Stock (cada una con su propia clave nombre/tipo/año). Tablas de ejemplo: Cervezas-En-Stock (Pilsen Trujillo/600/2000), Vino-En-Stock (Tarapacá/Carménère/2014/200/6000).

## Slide 41
"Solución 4: ¿Combinemos las tablas?" Esquema: `Cervezas(nombre,tipo,grados,ciudad-origen,cantidad,precio-unitario)` y `Vinos(nombre,tipo,año,grados,ciudad-origen,cantidad,precio-unitario)`. Tablas muestran el problema: Pilsen Trujillo tiene cantidad=0 y precio-unitario="?" (en rojo) porque no hay dato; igual para Tarapacá Merlot 2014 (cantidad 0, precio "?").

## Slide 42
"Solución 5: ¿Tomar todo el vino en stock?" Imagen humorística: una mujer (actriz de la serie Scandal) tomando una botella de vino directo, con frutas al fondo — chiste visual sobre la solución "trivial" de no tener stock cero.

## Slide 43
Slide de transición de sección. Título "Del Modelo Entidad–Relación: Al Modelo Relacional". Pie: "Capítulo 3.5 | Ramakrishnan / Gehrke".

## Slide 44
"Modelo E–R: Entidad (con atributos y llaves) → Modelo Relacional: Tabla". Diagrama ER: entidad Producto con atributos nombre (subrayado), precio, categoría. Traducción: `Producto(nombre:string,precio:int,categoría:string)` con nota "(Hay que agregar el dominio)". Tabla de ejemplo Producto con filas: Tarapacá Carménère 2014/4000/Vino; Austral Calafate 330ml/2000/Cerveza; Austral Yagar 330ml/2200/Cerveza; Pall Mall Rojo 20/2500/Tabaco.

## Slide 45
Misma slide anterior, añade segunda entidad Compañía con atributos nombre (subrayado), año-fundada. Esquema añade `Compañía(nombre:string,año-fundada:int)`. Tabla Compañía: British American Tobacco/1902; Viña Tarapacá/1874; Cervecería Austral/1896.

## Slide 46
"Modelo E–R: Relación (con atributos) → Modelo Relacional: Tabla". Diagrama ER completo: Producto —(fabrica)— Compañía, con atributo "desde" en la relación. Nota lateral: "Las llaves de las entidades juntas forman una súper llave para la relación". Esquema añade `Fabrica(p-nombre:string,c-nombre:string,desde:date)`. Tabla Fabrica: Austral Calafate 300ml/Cervecería Austral/1983; Austral Yagar 300ml/Cervecería Austral/2006; Pall Mall Rojo 20/British American Tobacco/1907.

## Slide 47
Repetición idéntica de la slide 46 (mismo diagrama y contenido).

## Slide 48
"Modelo E–R: Relación (con valor único) → Modelo Relacional: Tabla". Mismo diagrama con flecha naranja de Producto a "fabrica" indicando cardinalidad de valor único. Nota: "Con esta restricción no se necesita c-nombre para la llave. p-nombre forma una llave candidata."

## Slide 49
"Modelo E–R: Relación (llaves foráneas) → Modelo Relacional: Tabla". Mismo diagrama con anotaciones: "También una llave primaria" (sobre las llaves de Producto/Compañía) y "Una llave foránea: Una llave primaria en otra tabla" (dos veces, apuntando a p-nombre y c-nombre en Fabrica).

## Slide 50
"Modelo E–R: Relación (llaves foráneas) → Modelo Relacional: Tabla". Nota: "Llaves foráneas: Las escribiremos así (a veces abreviadas como C.)". Esquema Fabrica reescrito con notación de llave foránea: `Fabrica(Producto.nombre:string,Compañía.nombre:string,desde:date)`.

## Slide 51
Misma slide con pregunta añadida: "¿Algún problema aquí? La misma llave, pero... un producto no tiene que ser fabricado por una compañía?" — introduce el problema de participación opcional.

## Slide 52
Continuación: se explica que "Si intentáramos combinar las tablas, tendríamos un problema con productos sin información de su fabricación". Tabla Producto extendida con columnas "compañía" y "desde" muestra "???" en rojo para el producto "Tarapacá Carménère 2014" que no tiene compañía fabricante.

## Slide 53
Pregunta: "¿Hay algún caso que puede generar una tabla redundante? ..." — pregunta abierta sin resolver en la slide (mismo diagrama base).

## Slide 54
"Modelo E–R: Relación (con participación) → Modelo Relacional: Tabla". Pregunta "¿Ahora?" Diagrama con flecha naranja de Producto a "fabrica" (participación total). Esquema fusiona: `Producto(nombre:string,precio:int,categoría:string,C.nombre:string,desde:date)` y `Compañía(nombre:string,año-fundada:int)`. Tabla Producto con columna compañía llena para todas las filas (Tarapacá Carménère 2014 → Viña Tarapacá/2014 en verde).

## Slide 55
Misma slide, con preguntas añadidas: "¿Hay un problema con el diagrama? ¿Hay un mejor diagrama?"

## Slide 56
Misma slide con respuesta: "¡Sí! Pero no cambia la traducción: a veces, hay que considerar la posibilidad de combinar algunas tablas." — el diagrama ahora muestra "desde" conectado directamente a Producto en vez de a la relación fabrica.

## Slide 57
"Modelo E–R: Relaciones Múltiples → Modelo Relacional: Tabla". Diagrama ER ternario: Película —(arriendo)— Local de videos, y Persona —(arriendo)— con atributo dni destacado y fecha en la relación. Esquemas: `Película(título:string,año:int,categoria:string)`, `Local de videos(id:int,direccion:string)`, `Persona(dni:string,nombre:string)`, `Arriendo(Pl.titulo:string,Pl.año:int,Pr.dni:string,L.id:int,fecha:date)`.

## Slide 58
Mismo diagrama ternario reorganizado visualmente (Película y Local de videos arriba, Persona abajo) con los mismos 4 esquemas listados en texto plano debajo.

## Slide 59
"Modelo E–R: Relación (con papeles) → Modelo Relacional: Columnas distintas". Mismo diagrama pero con roles "cliente" y "cajero" etiquetados en las dos conexiones de Persona a "arriendo". Esquema Arriendo ahora tiene dos columnas para dni: `Arriendo(Pl.titulo:string,Pl.año:int,Pr.dni-cli:string,Pr.dni-caj:string,L.id:int,fecha:date)`.

## Slide 60
"Modelo E–R: Jerarquías de clases". Diagrama: Persona (dni subrayado, nombre, género) con dos triángulos IsA hacia Empleado (sueldo) y Cliente (vip). Pregunta: "¿Qué vamos hacer aquí?"

## Slide 61
"Modelo E–R: Jerarquías de clases → Modelo Relacional: Opción 1: Tablas solo para las subclases". Mismo diagrama. Esquema: `Empleado(dni:string,nombre:string,género:string,sueldo:string)` y `Cliente(dni:string,nombre:string,género:string,vip:boolean)` (atributos de Persona duplicados en cada subclase).

## Slide 62
"Opción 2: Tabla para la superclase". Esquema: `Persona(dni:string,nombre:string,género:string)`, `Empleado(P.dni:string,sueldo:int)`, `Cliente(P.dni:string,vip:boolean)` (llave foránea a Persona).

## Slide 63
"Eligiendo una opción". Compara opción 1 y 2 lado a lado. Pregunta: "¿Cuál sea la mejor opción... con mucho solapamiento entre Cliente y Empleado?" Respuesta: "Mucho solapamiento sugiere 2 (con menos o no solapamiento sugiere 1)" con explicación de por qué (evitar duplicar atributos generales).

## Slide 64
Misma comparación 1 vs 2. Pregunta: "...sin cobertura... si hay Personas que no son Empleados ni Clientes?" Respuesta: "Hay que elegir 2" (opción 1 no puede representar personas que no son ni empleados ni clientes).

## Slide 65
Misma comparación. Pregunta: "...con muchas consultas para el nombre de una Persona dado el DNI?" Respuesta: "Sugiere 2" (con 1 habría que consultar dos tablas, con 2 basta una).

## Slide 66
Misma comparación, conclusión general: "En general... Hay que considerar las tablas, los atributos, los datos, las restricciones, el control de acceso, etcétera, y aplicar algo "prudente"." (con emoji sonriente).

## Slide 67
"Modelo E–R: Jerarquías de clases → Modelo Relacional". Nuevo ejemplo: entidad Alumno (dni, nombre, año, género) con IsA hacia Pregrado y Postgrado. Pregunta: "¿Cuáles son las opciones en este caso?"

## Slide 68
Misma slide, muestra la opción 1 aplicada: `Pregado(dni:string,nombre:string,género:string,año:int)` y `Postgrado(dni:string,nombre:string,género:string,año:int)` (nota: "Pregado" es un typo original de la slide, no "Pregrado"). Pregunta: "¿Pero hay otra opción aquí?"

## Slide 69
Muestra ambas opciones (1 y 2): la opción 2 con `Alumno(dni,nombre,género,año)`, `Pregado(A.dni:string)`, `Postgrado(A.dni:string)`. Pregunta: "¿Hay otra opción?"

## Slide 70
"Una opción implícita: Quitar la jerarquía". Diagrama comparativo: a la izquierda el árbol de jerarquía completo (Alumno→Pregrado/Postgrado), a la derecha una única entidad Alumno con atributo adicional "tipo" (sin jerarquía).

## Slide 71
Continuación: esquema resultante `Alumno(dni:string,nombre:string,género:string,año:int,tipo:string)`. Pregunta "¿Algún problema aquí?" Respuesta: "Tendremos mucha repetición en la columna tipo. (Pero es más sencillo, el sistema puede comprimirla, etcétera.)"

## Slide 72
"Modelo E–R: Entidades débiles → Modelo Relacional: Cuidado con las llaves". Diagrama: Evaluación (entidad débil, doble borde) —(de, rombo doble borde)— Curso. Atributos: fecha, nombre (punteado=parcial) en Evaluación; codigo (subrayado), nombre en Curso. Pregunta "¿Alguien quiere "adivinar"?" Esquema propuesto (marcado con X roja como INCORRECTO):
```
Curso(código:string,nombre:string)
Evaluación(nombre:string,C.código:string,fecha:date)
De(E.nombre:string,C.código:string)
```
Problema señalado: "La tabla De(.,.) es redundante ... y es un nombre terrible para una tabla."

## Slide 73
"Modelo E–R: Entidades débiles → Modelo Relacional: No se necesita una tabla para la relación débil". Mismo diagrama. Esquema corregido (marcado con check verde):
```
Curso(código:string,nombre:string)
Evaluación(nombre:string,C.código:string,fecha:date)
```
Nota amarilla al pie: "Observación: En el libro de R&G, se mencionan atributos sobre relaciones débiles (p.ej. Figura 3.14) y por eso, se necesita una tabla para la relación. No estoy de acuerdo con eso: atributos en tales relaciones siempre pueden ser asociados con la entidad débil dado su relación 1:n."

## Slide 74
Slide en blanco (sin contenido visible) — probablemente transición u error de exportación del PDF.

## Slide 75
"Modelo E–R: Entidades débiles → Modelo Relacional". Diagrama extendido: Nota (entidad débil, con atributo pregunta) —(eval)— Evaluación —(de)— Curso; Nota también conectada vía (autor) a Alumno (dni, nombre). Pregunta "¿Las relaciones?" Esquema completo:
```
Curso(código:string,nombre:string)
Evaluación(nombre:string,C.código:string,fecha:date)
Nota(pregunta:int,E.nombre:string,C.código:string,A.dni:string,valor:float)
Alumno(dni:string,nombre:string)
```
(con flechas rojas mostrando cómo cada llave foránea referencia a su tabla).

## Slide 76
"Modelo E–R: Agregación → Modelo Relacional". Diagrama con recuadro punteado agrupando Película—(stock)—Local-de-Video (agregación) que a su vez se relaciona (arriendo) con Persona. Pregunta "¿Alguien quiere "adivinar"?" Esquema:
```
Película(año:int,título:string)
Local-de-Video(id:int,dirección:string)
Stock(Pl.año:int,Pl.título:string,L.id:int,precio-por-noche:int)
Persona(dni:string,nombre:string)
Arriendo(Pl.año:int,Pl.título:string,L.id:int,Pr.dni:string,fecha:date)
```

## Slide 77
"Modelo E–R: Ejercicio → Modelo Relacional". Diagrama complejo de dominio "pizzería": Oferta —(rebaja)— agrupa Local de Pizza y Tipo de Pizza —(vende)—; Local de Pizza tiene IsA hacia Restaurante (capacidad) y Delivery (tarifa). Atributos: descuenta/código en Oferta; dirección/teléfono en Local de Pizza; tamaño/vegetariano/nombre en Tipo de Pizza; precio en vende. Pregunta "¿Alguien quiere "adivinar"?" (sin resolver aún).

## Slide 78
Mismo diagrama de pizzería, con esquema completo resuelto:
```
Oferta(código:int,descuenta:float)
Tipo de Pizza(nombre:string,tamaño:int,vegentariano:int)
Local de Pizza(dirección:string,teléfono:int)
Restaurante(dirección:string,capacidad:int)
Delivery(dirección:string,tarifa:float)
Vende(LdP.dirección:string,TdP.nombre:string,TdP.tamaño:int,precio:float)
Rebaja(O.codigo,LdP.direccion,TdP.nombre,TdP.tamaño)
```

## Slide 79
"Modelo E–R: Ejercicio → Modelo Relacional". Nuevo diagrama: Conferencia (año, nombre) —(publicado)— Paper (título, páginas) —(autor-de, con atributo orden)— Autor (afiliación, nombre). Pregunta "¿Alguien quiere "adivinar"?" (sin resolver aún).

## Slide 80
Mismo diagrama resuelto:
```
Conferencia(nombre,año)
Paper(título,C.nombre,C.año,páginas)
Autor(nombre,afiliación)
AutorDe(A.nombre,P.título,C.nombre,C.año,orden)
```
Nota: "Una tabla Publicado sería redundante" (análogo al caso de entidades débiles).

## Slide 81
"Modelo E–R: Ejercicio → Modelo Relacional". Diagrama grande de dominio médico: Clínica (nombre,dirección) —(trabaja, con atributo horas)— Médico (nombre,rut,especialización), agrupados en un recuadro punteado; esta agregación se relaciona (cita, con atributo hora) con Paciente (correo,nombre,rut), que tiene IsA hacia ConSeguro (póliza) y SinSeguro (cuotas). Sin resolver aún en esta slide.

## Slide 82
Mismo diagrama médico, resuelto con esquema completo y notas de diseño:
```
Clínica(nombre,dirección)
Médico(rut,nombre)
Trabaja(C.nombre,C.dirección,M.rut,horas)
Paciente(rut,nombre,correo)
ConSeguro(P.rut,póliza)
SinSeguro(P.rut,cuotas)
Cita(T.nombre,T.dirección,T.rut,P.rut,hora)
```
Notas: "Mejor tener una tabla Paciente para representar la relación Cita con llave foránea (aunque no hay solapamiento)" y "Está bien si se define Cita con llave foránea a Clínica y Médico en vez de Trabaja (pero el último caso representa mejor la semántica de la agregación)".

## Slide 83
"Modelo E–R: Relación → Modelo Relacional: Tabla". Texto: "Aparte de jerarquías de clases la traducción es más o menos determinística". Recuadro morado con pregunta de discusión: "¿Qué piensan ustedes? ¿Cuál es mejor... diseñar tablas directamente o diseñar un modelo E-R antes?"

## Slide 84
Slide de cierre de sección con imagen de pizarra llena de fórmulas y texto superpuesto en verde estilo código: "</Modelo-ER>" — marca fin de la sección de transformación ER→Relacional. Decorativa.

## Slide 85
Slide de transición. Texto: "La próxima vez, continuaremos con: El Álgebra Relacional". Pie: "Capítulo 4 | Ramakrishnan / Gehrke".

## Slide 86
Slide de cierre "¿Preguntas?" con imagen decorativa de un bote a la deriva en un mar embravecido hecho de código binario (0s y 1s), con un ícono de "base de datos" (cilindros dorados apilados) dentro del bote — metáfora visual de fin de clase. Decorativa.
