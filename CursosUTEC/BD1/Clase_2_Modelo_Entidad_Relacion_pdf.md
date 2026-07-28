---
curso: BD1
titulo: Clase_2_Modelo_Entidad_Relación
slides: 111
fuente: Clase_2_Modelo_Entidad_Relación.pdf
---

## Slide 1
Portada (decorativa: fondo de túnel digital con silueta, logos UTEC/DCC Universidad de Chile). Texto: "CLASE 2: ENTIDAD-RELACIÓN", "CS2041- Base de Datos I", "Ciclo 2024-1". Autores: Brenner Ojeda (bojeda@utec.edu.pe), Teófilo Chambilla (tchambilla@utec.edu.pe). Nota: "En colaboración Aidan Hogan de la Universidad de Chile".

## Slide 2
Índice del curso, lista con viñetas: Resumen clase I; Enfoque de la base de datos; Diseño conceptual: Diagrama Entidad Relación; Diagrama Entidad-Relación: Relaciones múltiples; Diagrama Entidad-Relación: Jerarquías de clases; Restricciones avanzadas; Entidad Débil; Entidad Virtual.

## Slide 3
Slide de transición. Título "CS2041 BASE DE DATOS I CICLO 2024-1", con mascota (personaje ninja/hechicero ilustrado, recurrente en todo el material) señalando la etiqueta "Entidad Relación". Barra de progreso del curso con 8 secciones (primera resaltada "Introducción", segunda "Modelo relacional" aún no alcanzada). Logo "TRANSFORMATEC" abajo.

## Slide 4
Transición "Resumen: Clase 1 — Introducción a base de datos y DBMS". Imagen decorativa de mano robótica sobre globo terráqueo digital.

## Slide 5
Diagrama "Componentes" del sistema de base de datos. Flujo: Usuarios/Programadores → Programas de Aplicación/Consultas → (dentro del recuadro "SOFTWARE DEL SGBD") Software para procesar Consultas/Programas → Software para tener acceso a los datos almacenados → flechas bidireccionales hacia dos cilindros (bases de datos): "Definición de la BD (Metadatos)" y "Base de Datos almacenada". Cita: "Sección 1.5 | Ramakrishnan / Gehrke".

## Slide 6
Slide de transición con mascota ninja señalando cono de luz con texto "Modelo de Datos". Cita "Sección 1.5 | Ramakrishnan / Gehrke".

## Slide 7
"Modelos de cervezas" — imagen decorativa de 9 botellas de cerveza en fila (Abraxas, Cristal, Pilsen Callao, San Juan, Pilsen Trujillo, Backus Ice, Cusqueña Roja, Arequipeña, Cusqueña). Slide introductoria sin más texto.

## Slide 8
"Modelo de datos (árbol/jerarquía)". Diagrama de árbol: raíz "Cervezas" → 4 ramas por `tipo`: Ale Ultra, Lager, Pilsener, Dark → cada una con `origen` (Lima/Cusco/Trujillo/Arequipa) → nombres de cervezas específicas → hoja `grados` (valor numérico). Datos: Ale Ultra/Lima/Abraxas/7,0; Lager/Lima/Cristal,Pilsen Callao,Backus ICE/4,6; Lager/Cusco/Cusqueña Dorada,Roja/4,8; Lager/Trujillo/Pilsen Trujillo/4,6; Pilsener/Arequipa/Arequipeña,San Juan/4,6; Dark/Cusco/Cusqueña Negra/5,5. Debajo, misma fila de 9 botellas de cerveza (decorativa).

## Slide 9
Mismo árbol jerárquico de la slide 8 repetido, con evaluación: "✓ Muy simple entender" (verde) y "✗ Repeticiones" / "✗ ¿Si no hay una jerarquía natural?" (rojo). Fila de botellas decorativa debajo.

## Slide 10
"Modelo de datos (grafo)". Diagrama de grafo con nodos-entidad (recuadros grises: Abraxas, Cristal, Pilsen, Lima, Ale Ultra, Cusqueña Dorada, Cusco, San Juan, Arequipeña, Pilsener, Arequipa, Dark, Cusqueña Negra) conectados por aristas etiquetadas (`tipo`, `origen`, `grados`) hacia valores (7,0 / 4,6 / 4,8 / 5,5). Estructura de grafo dirigido con más conexiones cruzadas que el árbol (p.ej. varios nodos apuntan al mismo valor "4,6"). Fila de botellas decorativa debajo.

## Slide 11
"Modelo de datos (grafo)" — evaluación: "✓ Muy flexible / simple" (verde), "✗ Difícil resumir los datos (no hay un esquema obvio)" (rojo). Fila de botellas decorativa debajo.

## Slide 12
"Modelo de datos (tabla)". Tabla "Cervezas":

| nombre | tipo | grados | ciudad-Origen |
|---|---|---|---|
| Abraxas | Ale Ultra | 7,0 | Lima |
| Pilsen Trujillo | Lager | 4,6 | Trujillo |
| Pilsen Callao | Lager | 4,8 | Lima |
| Cristal | Lager | 4,8 | Lima |
| Cusqueña Dorada | Lager | 4,8 | Cusco |
| Backus Ice | Lager | 4,25 | Lima |
| Arequipeña | Pilsener | 4,6 | Arequipa |
| San juan | Pilsener | 4,6 | Pucallpa |

Fila de botellas decorativa debajo.

## Slide 13
Misma tabla "Cervezas" de la slide 12, con evaluación: "✓ Muy simple de entender" (verde); "✗ ¿Si queremos agregar un nuevo atributo?" / "✗ ¿Si no sabemos los grados de algunas cervezas?" (rojo).

## Slide 14
"Diferentes modelos de datos tienen diferentes fortalezas y debilidades". Slide comparativa que muestra lado a lado los 3 modelos: el grafo (izquierda), la tabla "Cervezas" (con columna extra Cusqueña Roja/Trigo, arriba derecha) y el árbol jerárquico (abajo derecha) — mismos datos representados en las 3 formas simultáneamente. Fila de botellas decorativa debajo.

## Slide 15
"Pero el modelo (formal) más establecido es el del modelo relacional" — repite la tabla "Cervezas" (mismas 8 filas que slide 12). Fila de botellas decorativa debajo.

## Slide 16
Transición con mascota ninja, cono de luz "Enfoque de Base de Datos". Cita "Capítulo 2 | Ramakrishnan / Gehrke".

## Slide 17
Diagrama de flujo "Enfoque de base de datos": "Obtención y análisis de requerimientos" → ramifica en "requerimientos funcionales" hacia "Análisis funcional" (izquierda) y "Diseño Conceptual" (derecha, resaltado rosa). "Diseño Conceptual" → "Esquema conceptual" → "Diseño Lógico" (rosa) → "Esquema lógico" → "Diseño Físico" (rosa) → "Esquema interno" → converge con "Análisis funcional" → "Diseño de programa de aplicación" → "Implementación de transacciones" → "Programas de aplicación". Línea punteada horizontal separa "Independiente del DBMS" (arriba) de "Dependiente del DBMS" (abajo).

## Slide 18
Transición: "Diseño conceptual:" con mascota ninja, cono de luz "El diagrama Entidad Relación". Cita "Capítulo 2 | Ramakrishnan / Gehrke".

## Slide 19
"Una pregunta más general: Conceptualmente: ¿qué estamos describiendo?" Caso de ejemplo: "Una base de datos de una empresa de marketing necesita almacenar información de cada compañía asociada (identificada por nombre y su valor-acción en el mercado), y los productos que fabrica cada compañía (identificado por nombre, precio y categoría)." Slide solo texto (planteamiento del caso).

## Slide 20
Mismo enunciado del caso de marketing (slide 19). Se agregan íconos ER a la derecha: recuadro azul "Producto" y recuadro azul "Compañía" (bajo "Entidades:"); óvalo amarillo "nombre" (bajo "Atributos de entidades:"); rombo rojo "fabrica" (bajo "Relaciones entre entidades:").

## Slide 21
"Diagramas: Entidad–Relación (ER)". Diagrama: entidad "Producto" (recuadro azul) conectada a tres atributos (óvalos amarillos): "nombre" (subrayado = llave), "precio", "categoría".

## Slide 22
"ER: Llaves (son obligatorias para cada entidad)". Mismo diagrama de "Producto" con atributos nombre/precio/categoría; se resalta que "nombre" está subrayado como llave/identificador obligatorio.

## Slide 23
"ER: Relaciones Binarias (Dos entidades relacionadas)". Diagrama: "Producto" (recuadro) — línea — rombo "fabrica" — línea — "Compañía" (recuadro).

## Slide 24
Mismo diagrama binario Producto–fabrica–Compañía, ahora con atributos: Producto tiene nombre (subrayado), precio, categoría; Compañía tiene nombre (subrayado), valor-acción.

## Slide 25
"ER: Relaciones Binarias — Atributos de Relaciones". Mismo diagrama, se agrega atributo "desde" colgando del rombo "fabrica" (atributo de la relación, no de las entidades). Recuadro de nota: "Relaciones tienen atributos descriptivos (no se pueden usar como parte de una llave)".

## Slide 26
"ER: Relaciones Binarias: Multiplicidad de relaciones". Cuatro variantes del diagrama Producto–fabrica–Compañía mostrando distintas puntas de flecha:
- n a n: sin flechas (líneas simples). Nota: "n significa 0 o más".
- n a 0 o 1: flecha apuntando de Producto hacia fabrica.
- 0 o 1 a n: flecha apuntando de Compañía hacia fabrica.
- 0 o 1 a 0 o 1: flechas en ambos lados apuntando hacia fabrica.

## Slide 27
"De hecho, hay muchas convenciones — Según Wikipedia:" Tabla/comparativa de notaciones ER (imagen tipo captura) mostrando la relación "Person – Birthplace – Location" en 6 convenciones distintas: Chen (rombo "Birthplace" con cardinalidades N y 1), IDEF1X (línea punteada con símbolo diamante), Bachman (flecha con círculo, etiquetas "Born in"/"Birthplace of"), Martin/IE/Crow's Foot (símbolos de "pata de cuervo"), Min-Max/ISO (etiquetas (1,1) y (0,N)), UML (estereotipos <<Entity>>/<<Relationship>> con multiplicidades 0..N y 1).

## Slide 28
"Pero sólo utilizaremos esta convención:" Diagrama Producto→fabrica—Compañía con flecha (punta triangular) de Producto hacia fabrica. Bullets: "Un Producto se fabrica por como máximo una Compañía"; "Una Compañía puede fabricar varios Productos". Recuadro nota: "No significa que hay solo 0 o 1 Compañía. Significa que un Producto se fabrica por 0 o 1 Compañía."

## Slide 29
"Las flechas son difíciles de recordar, pero..." Imagen decorativa/humorística: fotos de Pedro Pablo Kuczynski (Ciudadano) y de un presidente (Presidente) rodeadas de manos señalando en círculo (efecto "todos apuntan"), más una tercera persona (mujer) abajo. Diagrama: Ciudadano → tiene — Presidente (flecha de Ciudadano hacia "tiene"). Nota: "Dice que un ciudadano puede tener al máximo un presidente (Si consideráramos personas con dos ciudadanías, no aplicaría)".

## Slide 30
"ER: Relaciones Binarias (Dos entidades relacionadas)" — diagrama más completo: Producto (nombre, precio, categoría) →fabrica→ Compañía (nombre, valor-acción; "desde" en fabrica); además Persona (dirección, nombre, dni) con relación "compra" hacia Producto y relación "emplea" hacia Compañía (flecha de Persona hacia "emplea"). Pregunta "¿Multiplicidad de atributos?" con recuadro verde: "Siempre a 1"; "1 a 1 (e.g., dni)"; "n a 1 (e.g., categoría)".

## Slide 31
Transición: "DIAGRAMA ENTIDAD–RELACIÓN: RELACIONES MÚLTIPLES". Cita "Capítulo 2 | Ramakrishnan / Gehrke".

## Slide 32
"ER: Relaciones". Recuadro con pregunta: "¿Cómo se puede modelar un alquiler que involucra Personas, Películas y Locales de Videos?" Fotografía decorativa de un local Blockbuster cerrando ("STORE CLOSING").

## Slide 33
"ER: Relaciones Múltiples". Mismo enunciado (alquiler de Personas/Películas/Locales de Videos), ahora con diagrama: relación ternaria — rombo central "arriendo" conectado a tres entidades: "Película" (arriba izq.), "Local de videos" (arriba der.), "Persona" (abajo).

## Slide 34
"ER: Relaciones Múltiples — ¿Por qué no un atributo?" Mismo diagrama ternario Película–arriendo–Local de videos–Persona; nota amarilla apuntando a "Película": "Relaciones tienen atributos descriptivos (no se puede usar como parte de una llave)". Recuadro verde: "Si Película no es un 'valor simple' (tiene varios atributos) y/o si se necesita Película en la llave de la relación".

## Slide 35
"ER: Relaciones Múltiples — ¿Las multiplicidades?" Mismo diagrama ternario, sin líneas de multiplicidad aún dibujadas; recuadro "…".

## Slide 36
"ER: Relaciones Múltiples". Mismo diagrama ternario, ahora con flecha desde "Persona" hacia el rombo "arriendo" (indicando multiplicidad hacia Persona).

## Slide 37
"ER: Relaciones Múltiples — ¿Qué significa ésta (exactamente)?" Mismo diagrama con flecha Persona→arriendo; nota amarilla: "Persona es 'una llave' de la relación". Recuadro verde: "Una Persona puede arrendar una sola Película en un solo Local de videos. Puede ser que haya varias Locales de videos con varias Películas, etc."

## Slide 38
"ER: Relaciones Múltiples — ¿Si quisiéramos decir que una Persona puede alquilar varias Películas de varios Locales de videos?" Mismo diagrama (sin la flecha, vuelve a línea simple Persona–arriendo). Recuadro "…".

## Slide 39
"ER: Relaciones Múltiples — ¿Si quisiéramos decir que una Persona puede alquilar varias Películas pero de un solo Local de videos?" Mismo diagrama ternario base. Recuadro: "Regresaremos."

## Slide 40
"ER: Relaciones Múltiples — ¿Es un diagrama ER?" Mismo diagrama ternario Película–arriendo–Local de videos–Persona (sin atributos ni llaves dibujadas). Recuadro verde: "Formalmente no. No tenemos llaves de entidades. (Pero a menudo, se omiten los atributos para ser conciso)".

## Slide 41
"ER: Relaciones Múltiples — ¿Se puede hacerlo usando relaciones binarias?" Mismo diagrama ternario base (Película/Local de videos/Persona–arriendo). Recuadro "…".

## Slide 42
"ER: Relaciones Múltiples". Nuevo diagrama: entidad "Arriendo" (recuadro, ahora modelada como entidad) conectada mediante rombo "cliente" (con flecha Arriendo→cliente) a "Persona"; Arriendo conectada mediante rombo "película" hacia entidad "Película"; Arriendo conectada mediante rombo "vendedor" (con flecha Arriendo→vendedor) hacia "Local de videos". Es la alternativa de modelar el arriendo como entidad con 3 relaciones binarias en vez de una relación ternaria.

## Slide 43
"ER: Relaciones Múltiples — ¿Cuál es preferible?" Comparación lado a lado: a la izquierda el diagrama de Arriendo-como-entidad con 3 relaciones binarias (cliente/película/vendedor), etiquetado "Más flexible (p.ej., restricciones)"; a la derecha la relación ternaria simple Película–arriendo–Local de videos–Persona, etiquetado "Mucho más conciso".

## Slide 44
"ER: Relaciones Múltiples — ¿Si quisiéramos decir que una Persona puede alquilar varias Películas pero de un solo Local de videos?" Retoma el diagrama de Arriendo-como-entidad (cliente/película/vendedor) agregando flecha naranja de Persona hacia el rombo "cliente" (indicando la restricción de multiplicidad solicitada). Recuadro "…".

## Slide 45
"DER: Relaciones Múltiples: Arcos Etiquetados (Roles)". Vuelve a la relación ternaria Película–arriendo–Local de videos–Persona, pero con DOS arcos etiquetados entre "arriendo" y "Persona": uno etiquetado "cliente" y otro etiquetado "cajero" (Persona participa en dos roles distintos dentro de la misma relación).

## Slide 46
Transición: "DIAGRAMA ENTIDAD–RELACIÓN: JERARQUÍAS DE CLASES". Cita "Capítulo 2 | Ramakrishnan / Gehrke".

## Slide 47
"E–R: Jerarquías de clases — IsA: es Un(a) en inglés". Diagrama: entidad "Bebida" (con atributos origen, nombre —subrayado—, typo) en la raíz; dos triángulos verdes etiquetados "IsA" conectan Bebida hacia "Vino" y hacia "Cerveza"; Vino tiene además el atributo propio "año". Nota: "…los atributos origen, nombre y tipo se heredan por Vino y Cerveza".

## Slide 48
"E–R: Jerarquías de clases — Superclases y subclases". Mismo diagrama IsA (Bebida/Vino/Cerveza). Nota: "…Bebida es una superclase … Vino y Cerveza son subclases".

## Slide 49
"E–R: Jerarquías de clases — Generalización y especialización". Mismo diagrama IsA, ahora con flecha naranja apuntando hacia abajo etiquetada "Bebida generaliza Vino y Cerveza" (a la izquierda) y flecha morada apuntando hacia arriba etiquetada "Vino y Cerveza especializan Bebida" (a la derecha).

## Slide 50
"DER: Jerarquías de clases — Restricciones: Solapamiento". Mismo diagrama IsA Bebida/Vino/Cerveza. Definición: "Solapamiento (Overlap): ¿se permite que dos subclases contengan la misma entidad?" Pregunta "¿Hay Solapamiento aquí?" → Respuesta: "No (con suerte)."

## Slide 51
"DER: Jerarquías de clases — Restricciones: Solapamiento (dicho de otra manera)". Diagrama genérico: entidad "Z" con 3 IsA hacia "A", "B", "C" (izquierda); a la derecha diagrama de Venn de 3 círculos (A rojo, B amarillo, C azul) con intersecciones marcadas "¿●?" en las 3 zonas de solapamiento. Bullets: "¿Se puede tener una entidad en A y B o B y C o A y C? ¿Sí? entonces se permite Solapamiento [por defecto]. ¿No? entonces no se permite Solapamiento".

## Slide 52
"DER: Jerarquías de clases — Restricciones: Solapamiento — No Solapamiento." Mismo diagrama Z/A/B/C + Venn de 3 círculos, ahora sin intersección entre A y B (separados), nota amarilla "No Solapamiento" apuntando a esa zona. Fórmula matemática: A ∩ B ∩ C = ∅.

## Slide 53
"DER: Jerarquías de clases — Restricciones: Cobertura". Retoma diagrama Bebida/Vino/Cerveza (con atributos origen/nombre/typo, año en Vino). Definición: "Cobertura (Covering): ¿todas las subclases cubren la superclase?" Pregunta "¿Hay Cobertura aquí?" → "No (con suerte)." Imagen decorativa de botella de vino "Demonio de los Andes" a la derecha.

## Slide 54
"DER: Jerarquías de clases — Restricciones: Cobertura (dicho de otra manera)". Diagrama Z/A/B/C + Venn de 3 círculos con anotación "¿● ∈ Z?" a la derecha (pregunta si existe un punto en Z fuera de A∪B∪C). Bullets: "¿Se puede tener una entidad en Z que no está en A, ni B, ni C? ¿Sí? entonces no se puede afirmar cobertura [por defecto]. ¿No? entonces se puede afirmar cobertura".

## Slide 55
"DER: Jerarquías de clases — Restricciones: Cobertura (dicho de manera más matemática)". Mismo diagrama Z/A/B/C + Venn (ahora los 3 círculos coloreados en tonos verdes, etiqueta "Z" fuera indicando que Z = la unión). Fórmula: Z = A ∪ B ∪ C.

## Slide 56
"DER: Jerarquías de clases — Restricciones". Ejemplo aplicado: entidad "Alumno" (atributos género, rut —subrayado—, nombre) con 2 IsA hacia "Postgrado" y "Pregrado"; Postgrado tiene atributo "oficina". Preguntas/respuestas: "¿Hay Solapamiento aquí? → Depende (¿datos históricos?)"; "¿Hay Cobertura aquí? → Sí (de alumnos universitarios)".

## Slide 57
"DER: Jerarquías de clases — Restricciones". Segundo ejemplo: entidad "Persona" (género, rut, nombre) con 2 IsA hacia "Empleado" (atributo sueldo) y "Alumno" (atributo carrera). Preguntas/respuestas: "¿Hay Solapamiento aquí? → Sí (p.ej., auxiliar ->TAs)"; "¿Hay Cobertura aquí? → Depende (¿visitantes?)".

## Slide 58
Transición: "DIAGRAMA ENTIDAD–RELACIÓN — Restricciones avanzadas" con mascota ninja y cono de luz. Cita "Capítulo 2 | Ramakrishnan / Gehrke".

## Slide 59
"ER: Restricciones — (Hemos visto) Multiplicidad de relaciones". Diagrama Profesor→trabaja—Universidad (flecha de Profesor hacia "trabaja"); recuadro "O?"; debajo, mismo diagrama pero con flecha invertida (de Universidad hacia "trabaja").

## Slide 60
Mismo diagrama Profesor—trabaja—Universidad, ahora etiquetado con cardinalidades "N" (lado Profesor) y "1" (lado Universidad) sobre las líneas; recuadro azul con flechas: "Hace referencia a la MULTIPLICIDAD".

## Slide 61
"ER: Restricciones — Participación". Diagrama Profesor—trabaja—Universidad con doble línea Profesor–trabaja y notación "(1, )" sobre el lado Universidad, flecha hacia recuadro "Hace referencia a una PARTICIPACIÓN TOTAL". Texto: "…cada profesor trabaja en al menos una universidad".

## Slide 62
"ER: Restricciones — Participación + Multiplicidad". Mismo diagrama con "(1, N)" sobre el lado Universidad; dos recuadros con flechas: "MULTIPLICIDAD" (apunta a la N) y "PARTICIPACIÓN" (apunta al 1). Texto: "…cada profesor trabaja en al menos una universidad".

## Slide 63
"ER: Restricciones — Participación + Multiplicidad". Diagrama con "(0,N)" en lado Profesor y "(1,N)" en lado Universidad. Texto: "…cada profesor trabaja en al menos una universidad".

## Slide 64
Mismo tipo de diagrama con "(0,N)" en Profesor y "(1,1)" en Universidad (flecha hacia trabaja del lado Universidad). Texto: "…cada profesor trabaja en una (sola) universidad".

## Slide 65
Tres diagramas apilados mostrando combinaciones de participación/multiplicidad:
- (0,N)—(0,1): "…cada profesor trabaja en 0 o 1 universidad"
- (0,N)—(1,N): "…cada profesor trabaja en 1 o más universidades"
- (0,N)—(1,1): "…cada profesor trabaja en 1 (sola) universidad"

## Slide 66
Transición: "DIAGRAMA ENTIDAD–RELACIÓN — Entidades Débiles". Cita "Capítulo 2 | Ramakrishnan / Gehrke".

## Slide 67
"E–R: Entidades débiles". Diagrama: "Evaluación" (atributos fecha, nombre —subrayado—) —de→ "Curso" (atributos código, nombre —subrayado—); un símbolo X rojo tachando una línea diagonal extra entre Evaluación y el atributo "código" de Curso, indicando que no se puede compartir llaves entre entidades así. Texto: "¡No se puede compartir llaves así!"

## Slide 68
Mismo diagrama Evaluación–de–Curso, ahora con "Evaluación" resaltada con doble borde (entidad débil) y su atributo "nombre" con subrayado punteado (llave parcial). Nota azul: "¡Se llama una llave parcial!" Texto: "…entidades cuya llave dependa de la llave de otra entidad".

## Slide 69
"E–R: Entidades débiles — ¿Cuándo se usan? Tres características". Mismo diagrama con anotaciones: "(1) Dependencia de llave" (apunta a nombre de Evaluación y código de Curso); "(2) Varias (débiles) a una (3) Participación total" (apunta a la relación "de", doble línea del lado Evaluación).

## Slide 70
"E–R: Entidades débiles — Un ejemplo más complejo". Mismo diagrama Evaluación(fecha, nombre)–de–Curso(código, nombre). Pregunta: "¿Ahora, si queremos modelar notas de alumnos?"

## Slide 71
"E–R: Entidades débiles — Una cadena de entidades débiles". Diagrama ampliado: "Nota" (entidad débil, doble borde; atributos dni_alumno —subrayado punteado— y valor) —eval→ "Evaluación" (doble borde; atributos nombre —subrayado punteado— y fecha) —de→ "Curso" (atributos código —subrayado— y nombre). Pregunta: "¿Y si queremos guardar el nombre del alumno?"

## Slide 72
Mismo diagrama, con atributo extra "nombre_alumno" agregado a Nota, marcado con X roja (inválido). Nota negra: "¡Repeticiones del nombre del alumno para cada nota! (Redundante con el DNI)". Pregunta: "¿Algún problema aquí?"

## Slide 73
"E–R: Entidades débiles — Varias dependencias". Diagrama con X roja sobre "Nota" (indicando que ya no tiene llave parcial propia); nota negra: "¡No hay llave parcial!"; se agrega nueva relación "autor" (flecha desde Nota) hacia entidad "Alumno" (atributos dni —subrayado—, nombre). Pregunta: "¿Podemos simplificar el modelo?"

## Slide 74
"E–R: Entidades débiles — Relación con una entidad débil". Diagrama simplificado: "Alumno" (dni, nombre) —nota→ "Evaluación" (doble borde; nombre, fecha) —de→ "Curso" (código, nombre). La relación "nota" ahora conecta directamente Alumno con Evaluación (con atributo "valor"). Pregunta: "¿Si tenemos notas por pregunta?"

## Slide 75
Mismo diagrama, se agrega atributo "pregunta" a la relación "nota", marcado con X roja (inválido porque un atributo de relación no puede depender así). Nota negra: "¡Un alumno puede tener varias notas para varias preguntas en la misma evaluación!" Pregunta: "¿Algún problema aquí?"

## Slide 76
"E–R: Entidades débiles — Varias dependencias y una cadena". Diagrama final correcto: "pregunta" ahora es atributo/llave parcial de la entidad débil "Nota" (doble borde); Nota conecta mediante "eval" hacia "Evaluación" (doble borde) y mediante "autor" hacia "Alumno" (dni, nombre); Evaluación conecta mediante "de" hacia "Curso". Pregunta "¿Algún problema aquí?" → Respuesta: "¡Todo bien! 😊" (recuadro verde).

## Slide 77
Transición: "DIAGRAMA ENTIDAD–RELACIÓN — Agregación". Cita "Capítulo 2 | Ramakrishnan / Gehrke".

## Slide 78
"E–R: Agregación — ¿Cuándo se necesita agregación?" Entidades sueltas: "Profesor" (dni, nombre) arriba; abajo "Auxiliar" (dni, nombre) y "Curso" (nombre, código), sin conectar entre sí. Pregunta: "¿Cómo se puede conectar Auxiliar (TA) y Curso?"

## Slide 79
Mismo layout, ahora con relación "aux-de" conectando Auxiliar y Curso (sin atributos). Pregunta: "¿Cómo se puede conectar Profesor y Curso?"

## Slide 80
Se agrega relación "prof-de" (con doble línea, indicando participación total) entre Profesor y Curso, además de "aux-de" entre Auxiliar y Curso. Preguntas: "¿Cómo se puede conectar Auxiliar(TA) y Profesor?" / "¿Están implícitamente conectados por Curso?"

## Slide 81
Mismo diagrama de 3 entidades (Profesor–prof-de–Curso–aux-de–Auxiliar). Pregunta: "¿Si hay varios Profesores en cada Curso con sus propios Auxiliares(TAs)?"

## Slide 82
La relación "prof-de" (Profesor–Curso) se reemplaza por "controla" conectando Profesor con Auxiliar y con Curso directamente (rombo "controla" en el centro superior, conectado a los 3: Profesor arriba, Auxiliar y Curso abajo). Pregunta: "¿Si queremos decir cuántas horas el Auxiliar(TA) trabaja con cada Profesor en el Curso?"

## Slide 83
Se agrega atributo "horas" a la relación "controla" (rombo central conectando Profesor, Auxiliar, Curso). Pregunta: "¿Si queremos decir el sueldo total del Auxiliar(TA) en el Curso (independientemente de los Profesores)?"

## Slide 84
Atributo "horas" renombrado a "horas-con-prof"; se agrega atributo "sueldo" a la relación "aux-de" (Auxiliar–Curso), marcado con X roja la conexión entre "controla" y "aux-de" (indicando que no se puede conectar una relación a otra relación directamente). Pregunta: "¿Se puede tener relaciones entre relaciones?" → Respuesta: "No directamente, pero…"

## Slide 85
"E–R: Agregación: crear una entidad virtual encapsulando una relación". Recuadro punteado azul rodea la relación "aux-de" completa (Auxiliar–aux-de–Curso, con atributo sueldo) convirtiéndola en una "entidad virtual"; fuera del recuadro, "controla" (con atributo horas-con-prof) conecta Profesor con esa entidad virtual.

## Slide 86
"E–R: Agregación — ¿Cuándo se usa? Un caso típico". Mismo diagrama con anotaciones: nota amarilla "(1) (0,n) a (0,n)" apuntando a la conexión Profesor–controla; nota amarilla "o (2) Atributos diferentes" apuntando a los atributos horas-con-prof y sueldo (dentro/fuera del recuadro virtual).

## Slide 87
"E–R: Agregación: Mejor ejemplo". Nuevo ejemplo con recuadro punteado azul (entidad virtual) que engloba "Película"(código, nombre) –tiene– "Local de video"(nombre, código), con atributo "precio-por-noche" en la relación "tiene". Fuera del recuadro, relación "arrienda" (atributo "hasta") conecta esa entidad virtual con "Persona" (dni, nombre). Nota amarilla: "La relación no está entre relaciones (hay un hueco). La relación conecta Persona y una entidad virtual." Fotografía decorativa de Blockbuster cerrando.

## Slide 88
Mismo diagrama; pregunta "¿Todavía tiene sentido sin hasta?" → Respuesta: "¡Sí! (Si un local puede tener películas no arrendadas)".

## Slide 89
Mismo diagrama; pregunta "¿Todavía tiene sentido sin precio-por-noche?" → Respuesta: "¡Sí! (Si un local puede tener películas no arriendadas)".

## Slide 90
Mismo diagrama; pregunta "¿Todavía tiene sentido sin ambos atributos?" → Respuesta: "¡Sí! (Si un local puede tener películas no arriendadas)".

## Slide 91
Mismo diagrama con doble línea (participación total) entre la entidad virtual "tiene" y la relación "arrienda". Pregunta "¿Todavía tiene sentido con participación?" → Respuesta: "¡No!" (recuadro rojo).

## Slide 92
Diagrama final simplificado: sin recuadro de entidad virtual, la relación "arrienda" (con doble línea de participación total) conecta directamente Película, Local de video y Persona en una relación ternaria (con atributo "hasta"). Pregunta "¿Todavía tiene sentido con participación?" → Respuesta: "…más conciso con una relación ternaria!"

## Slide 93
"E–R: Relaciones: Binaria vs. Agregación vs. Ternaria". Tres diagramas comparativos en fila, con flecha "Más flexible" (izquierda) y "Más conciso" (derecha): (1) modelo binario completo (Arriendo–cliente–Persona, Arriendo–película–Película, Arriendo–vendedor–Local de videos); (2) modelo con agregación (recuadro Película–tiene–Local de video, luego arrienda–Persona); (3) modelo ternario directo (Película–arrienda–Local de videos–Persona). Texto: "¡Es importante intentar ser tan conciso como sea posible (pero no muy conciso)!"

## Slide 94
"E–R: Relaciones: Agregación vs. Binaria + Ternaria". Comparación lado a lado: izquierda = versión con agregación (recuadro punteado Película-tiene-Local de video, con precio-por-noche, más arrienda-hasta-Persona); derecha = versión ternaria directa (Película-Local de video-Persona conectados a "arrienda" con hasta). Nota amarilla: "Una persona podría arrendar una película de cualquier local, incluso un local que no tenga la película". Pregunta: "¿Cuál es la diferencia entre las dos opciones aquí?"

## Slide 95
Transición: "¿PARA QUÉ NECESITAMOS E–R?" con mascota ninja sosteniendo un puntero, apuntando al texto.

## Slide 96
Imagen decorativa de pantalla completa: fotografía de una clase magistral universitaria con una pizarra llena de fórmulas matemáticas y físicas, un profesor de pie frente a estudiantes tomando apuntes. Sin texto adicional.

## Slide 97
"¿Para qué necesitamos E–R?" Lista con viñetas: "Modelar los requerimientos de un aplicación – En una forma menos técnica que usar tablas"; "Evitar redundancia / lograr un modelo conciso"; "Documentar restricciones conceptuales"; "Evitar problemas (p.ej. con llaves)".

## Slide 98
Transición: "EJEMPLO: VINO, CERVEZA" (solo texto, sin diagrama).

## Slide 99
"Modelando vinos y cervezas". Enunciado del caso: "Vendemos vinos y cervezas. Cada vino tiene año, tipo, grados y ciudad-origen. Cada cerveza tiene ciudad-origen, tipo, grados. Vinos y cervezas tienen un precio unitario y una cantidad 'en stock' cada día." (Slide solo con el enunciado, sin diagrama aún.)

## Slide 100
Mismo enunciado, ahora con diagrama ER completo: entidad "Stock" (atributos fecha, precio-unitario, cantidad) conectada mediante relación "en-stock" hacia "Cerveza" (nombre, tipo, grados, ciudad-origen) y mediante otra relación "en-stock" hacia "Vino" (año, tipo, nombre, grados, ciudad-origen). Nota roja: "No tenemos llaves …"
