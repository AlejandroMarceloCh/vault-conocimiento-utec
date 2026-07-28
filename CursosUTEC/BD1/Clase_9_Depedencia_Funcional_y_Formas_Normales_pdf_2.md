---
curso: BD1
titulo: Clase 9 Depedencia Funcional y Formas Normales
slides: 85
fuente: Clase 9 Depedencia Funcional y Formas Normales.pdf
---

## Slide 1
Portada decorativa (fondo azul con figura de fotógrafo, textura de túnel). Título: "DEPENDENCIA FUNCIONAL Y FORMAS NORMALES". Subtítulo: "CS2041- Base de Datos I", "Ciclo 2024-1". Logos UTEC. Autores: Teófilo Chambilla (tchambilla@utec.edu.pe), Brenner Ojeda (bojeda@utec.edu.pe). Chrome decorativo, sin contenido académico.

## Slide 2
Título: "RESULTADOS DE APRENDIZAJE". Lista de 3 objetivos:
- Podrá explicar los conceptos de normalización de tablas.
- Podrá determinar si un modelo de base de datos es correcto usando dependencias funcionales.
- Podrá aplicar las formas normales 1FN, 2FN, 3FN, FNBC
Icono decorativo de check/engranajes a la derecha.

## Slide 3
Slide de portada de sección con texto "CS2041 / BASE DE DATOS I / CICLO 2024-1". Diagrama de línea de tiempo del curso (roadmap) mostrando los temas del curso como barras horizontales: Introducción, Modelo Relacional, Algebra Relacional & Cálculo Relacional, SQL, Actualización/Restricciones, Entidad-Relación, Optimización y Procesamiento, y **Formas Normales** (resaltado en un recuadro azul claro como el tema actual, con una mascota tipo ninja apuntando con un puntero). Icono decorativo de bandera de meta a la derecha.

## Slide 4
Título: "Las preguntas de hoy". Muestra tres tablas de ejemplo (dominio astronómico) para ilustrar diseño relacional:

**Tabla Planeta** (columnas: nombre, dist, radio, grav, días, años, temp, anillo) con 8 filas de datos de los planetas del sistema solar (Mercurio a Neptuno), incluyendo distancia, radio, gravedad, duración del día, años, temperatura y si tiene anillos (true/false).

**Tabla Satélite** (columnas: nombre, planeta, descubridor, año) con 7 filas (Luna, Ganímedes, Calisto, Europa, Ío, Titán, Tritón) y sus descubridores.

**Tabla Aterrizaje** (columnas: nave, planeta, país, año) con 7 filas de misiones espaciales (Messenger, Venera 3, Pioneer, Mars 2 lander, Viking 1, Beagle 2, Galileo).

Pregunta guía en recuadro: "¿Y cómo se puede saber si es un buen diseño relacional o no?"

## Slide 5
Título: "Directrices informales" / subtítulo "Directrices de diseño informales para los esquemas de relación". Texto: antes de la teoría formal, se verán 4 medidas informales de calidad para el diseño de un esquema de relación, listadas con viñetas de colores:
- La semántica de los atributos. (naranja)
- La reducción de información redundante en las tuplas. (verde)
- La reducción de los valores NULL en las tuplas. (azul)
- Prohibición de la posibilidad de generar tuplas falsas. (marrón)

## Slide 6
Título: "Directrices informales (Semántica)". Ejemplo con 4 esquemas de relación mostrados como tablas con atributos subrayados (PK) y anotación FK:

- **EMPLEADO**(NombreE, Dni[PK], FechaNac, Dirección, NumeroDpto[FK])
- **DEPARTAMENTO**(NombreDpto, NumeroDpto[PK], DniDirector[FK])
- **PROYECTO**(NombreProyecto, NumProyecto[PK], UbicaciónProyecto, NumDptoProyecto[FK])
- **LOCALIZACIONES_DPTO**(NumeroDpto[PK,FK], UbicaciónDpto[PK])
- **TRABAJA_EN**(Dni[PK,FK], NumProyecto[PK,FK], Horas)

Texto final: "La facilidad con la que se pueda explicar el significado de los atributos de una relación es una medida informal de lo bien que está diseñada esa relación."

## Slide 7
Título: "Directrices informales (tuplas falsas)". Ejemplo con dos tablas:

**Personas**: DniPersona | NomPersona | NomProyecto
- 8888888 | Ana | Proyecto 1
- 5555555 | Roberto | Proyecto 2

**Proyectos**: NroProy | NomProy
- 21 | Proyecto 1
- 55 | Proyecto 2
- 32 | Proyecto 2

Se muestra el resultado del Join Personas-Proyectos (5 columnas: DniPersona, NomPersona, NomProyecto, NroProy, NomProy) con 3 filas resultantes; la fila de Ana es correcta, pero Roberto aparece dos veces (con NroProy 55 y 32) resaltado en rojo/rectángulo punteado, generando tuplas ambiguas. Pregunta en banner rojo: "¿Ambas son correctas?"

## Slide 8
Título: "Directrices informales (tuplas falsas)". Diagrama de descomposición: relación r(ABC) con 5 filas se proyecta (ρ) en r1(AB) y r2(BC); luego se combinan con join natural (⊗) para producir r' (ABC). El resultado r' tiene MÁS filas que la r original (incluye filas espurias resaltadas en rojo: (1,0,1) y (2,0,4), marcadas como "tuplas falsas"). Observación en verde: "No todas las descomposiciones de una tabla se pueden combinar utilizando la combinación natural para reproducir la tabla original."

## Slide 9
Título: "Directrices informales (tuplas falsas)". Diagrama con relaciones r1(ABC) (4 filas) y r2(BCD) (3 filas) que se combinan por join natural (⊗) para formar r=r1⊗r2 (5 filas, columnas A,B,C,D). Luego se proyectan r1'=ΠABC(r) y r2'=ΠBCD(r). Observación en verde: "Las tablas r2 y r2' son iguales, sin embargo, la tupla <2,2,6> está en r1 pero no está presente en r1'" — ejemplo de pérdida de información al descomponer/recomponer.

## Slide 10
Slide de transición/portada de sección: "DEPENDENCIAS FUNCIONALES". Referencia: "Capítulo 19 | Ramakrishnan / Gehrke". Fondo blanco, solo texto.

## Slide 11
Título: "Conceptos básicos". Texto:
- Las DF son un tipo particular de restricción.
- Permiten expresar hechos acerca de la realidad que se está modelando con la BD.

## Slide 12
Título: "Dependencias funcionales". Definición formal: "Dada una relación R y dos conjuntos de atributos X∈R, Y∈R, X determina funcionalmente a Y si y sólo si dos tuplas que tienen el mismo valor de X deben por fuerza tener el mismo valor de Y." Nota: "X y Y pueden ser atributos compuestos" (resaltado en rojo).

## Slide 13
Título: "Dependencias funcionales". Notación: **X → Y**. Lectura: "X determina funcionalmente a Y" o "Y depende funcionalmente de X". Nota en rojo: "Esto no supone que Y→X en R."

## Slide 14
Título: "Ejemplo". Tabla de ejemplo r con columnas A, B, C, D y 5 filas de datos con subíndices:
| A | B | C | D |
|---|---|---|---|
| a1 | b1 | c1 | d1 |
| a1 | b2 | c1 | d2 |
| a2 | b2 | c2 | d2 |
| a2 | b3 | c2 | d3 |
| a3 | b3 | c2 | d4 |
Se usará para analizar qué DFs se satisfacen.

## Slide 15
Análisis: "A ➜ C se satisface." Explicación: las dos tuplas con valor a1 en A tienen el mismo valor en C (c1); las dos tuplas con valor a2 en A tienen el mismo valor en C (c2); no existen otros pares de tuplas distintos que tengan el mismo valor en A.

## Slide 16
Análisis: "C ➜ A no se satisface." Contraejemplo: t1=(a2, b3, c2, d3) y t2=(a3, b3, c2, d4) tienen el mismo valor en C (c2) pero distintos valores en A (a2 y a3). Conclusión: t1[C]=t2[C] pero t1[A]≠t2[A].

## Slide 17
Texto: "r satisface muchas otras DF." Ejemplos: AB ➜ D; A ➜ A (trivial); y las demás DF triviales. Definición en negrita: "una DF de la forma α➜β es trivial si β⊆α".

## Slide 18
Título: "Dependencias funcionales: Ejemplo". Tabla EMP_PROY con columnas: DNI, NumProyecto, Horas, NombreE, NombreProyecto, UbicacionProyecto. Diagrama con flechas etiquetadas DF1, DF2, DF3 conectando columnas origen a destino. Las DFs resultantes en recuadros verdes punteados:
- {DNI, NumProyecto} → {Horas}
- {DNI} → {NombreE}
- {NumProyecto} → {NombreProyecto, UbicacionProyecto}

## Slide 19
Título: "Dependencias funcionales: Ejemplo". Enunciado de caso de negocio (empresa de alquiler de vehículos): vehículos identificados por matrícula (marca, color, modelo, año); clientes identificados por cédula (nombre, dirección, teléfono); contrato de alquiler identificado por número de contrato, con fecha, cliente, vehículo, período en días y precio. Restricción: en una misma fecha no se puede alquilar más de una vez el mismo vehículo al mismo cliente.

## Slide 20
Repite el mismo enunciado del slide 19 pero con resaltado de colores (naranja para entidades: vehículos, clientes, contrato; verde para atributos: matrícula, marca/color/modelo/año, cédula, nombre/dirección/teléfono, número de contrato, fecha/cliente/vehículo/periodo/precio; azul para la restricción de unicidad fecha+vehículo+cliente).

## Slide 21
Título: "Dependencias funcionales: Ejemplo". Continuación: DFs obtenidas del caso de alquiler de vehículos:
- matrícula → {marca, color, modelo, año}
- cédula → {nombre, dirección, teléfono}
- nroContrato → {fecha, cédula, matrícula, período, precio}
- {fecha, cédula, matrícula} → nroContrato

## Slide 22
Título: "Dependencias funcionales:". Texto: una DF es una propiedad del esquema, no de la instancia. No puede ser inferida automáticamente a partir de una instancia. Una instancia por sí sola es insuficiente para determinar si una DF se cumple (salvo muestra representativa), pero sí puede mostrar que una DF NO se cumple.

## Slide 23
Título: "Dependencias funcionales / Inferencia, deducción". Recuadro: "Sea F el conjunto de DFs especificadas en un esquema de relación R." Texto: habitualmente se especifican DFs semánticamente obvias; sin embargo otras DFs pueden derivarse y satisfacer las dependencias de F; esas se dice que se infieren o deducen de F.

## Slide 24
Título: "Dependencias funcionales / Inferencia, deducción". Ejemplo: si NroDpto determina de forma única DniDirector (NroDpto → DniDirector), y un director tiene un único TelDirector (DniDirector → TeléfonoDirector), entonces ambas dependencias juntas suponen NroDpto → TeléfonoDirector. Esta DF inferida no tiene que declararse explícitamente.

## Slide 25
Título: "Dependencias funcionales / Clausura (F+)". Definición: F+ es el conjunto de todas las dependencias que incluye F, junto con las que pueden inferirse de F. El cierre de F (F+) es el conjunto de DF que F implica lógicamente; se puede calcular directamente de la definición formal de DF. Nota roja: las DF en F+ deben cumplirse para todas las instancias de la relación donde se cumpla F.

## Slide 26
Título: "Dependencias funcionales: Reglas de Inferencias". Lista de 6 reglas de inferencia (con notación formal):
- RI1: Reflexiva: Si Y ⊆ X, entonces X → Y (DF trivial).
- RI2: Aumento: {X → Y} ⊨ XZ → YZ
- RI3: Transitiva: {X → Y, Y → Z} ⊨ X → Z
- RI4: Descomposición o proyección: {X → YZ} ⊨ X → Y
- RI5: Unión o aditiva: {X → Y, X → Z} ⊨ X → YZ
- RI6: Pseudotransitiva: {X → Y, WY → Z} ⊨ WX → Z
Nota roja: Reglas de Armstrong (RI1-RI3) son minimales; las demás se derivan de estas tres.

## Slide 27
Título: "Ejemplo" (Reglas de Inferencia). Sea R=(A,B,C,G,H,I) y F={A→B, A→C, CG→H, CG→I, B→H}. Demostración de que A→H es miembro de F+: como A→B y B→H, se aplica regla de transitividad. Nota: es más fácil usar Axiomas de Armstrong que deducir directamente de las definiciones.

## Slide 28
Título: "Ejemplo" (continuación, mismo R y F). Demostración de CG → HI: como CG→H y CG→I, la regla de unión implica CG→HI.

## Slide 29
Título: "Ejemplo" (continuación, mismo R y F). Demostración de AG → I: pasos — A→C se cumple; por regla de aumento AG→CG; como CG→I, por transitividad AG→I.

## Slide 30
Título: "Dependencias funcionales: Reglas de Inferencias". Slide de transición con solo la palabra "Demostración" en cursiva, sin contenido adicional (probablemente introduce un ejercicio en vivo o video no capturado).

## Slide 31
Título: "Dependencias funcionales: Clausura de X bajo F+". Pseudocódigo del algoritmo para determinar X+ bajo F, con anotaciones explicativas en recuadros:
```
X+ := X                        [Asigna todos los atributos de X]
repetir
   antiguaX+ := X+;
   para cada df Y→Z en F hacer
        si Y ⊆ X+ entonces      [Agrega atributos a X+]
            X+ := X+ U Z;
hasta que (antiguaX+ = X+);     [No hay más cambios en X+]
```

## Slide 32
Título: "Dependencias funcionales: Clausura de X bajo F+ (Ejemplo)". Relación R(A,B,C,D,E,F) con F = {AB→C; BC→AD; D→E; CF→B}. Pregunta: ¿cuál es {A,B}+? Se muestra al costado el desarrollo paso a paso: X=A,B; X[0]=A,B; X[1]=A,B,C; X[2]=A,B,C,D; X[3]=A,B,C,D,E; resultado {A,B}+ = A,B,C,D,E.

## Slide 33
Continuación (slide de solución en texto corrido, tipografía tipo documento): explica en prosa el desarrollo del algoritmo aplicado al ejemplo anterior — cómo X pasa de {A,B} a {A,B,C} (por AB→C), luego se analiza BC→AD (abreviatura de BC→A y BC→D), se agrega D quedando {A,B,C,D}, luego con D→E se agrega E, resultando {A,B,C,D,E}. CF→B no se puede aplicar porque su lado izquierdo nunca está contenido en X. Conclusión: {A,B}+ = A,B,C,D,E.

## Slide 34
Título: "Dependencias funcionales: Clausura de X bajo F+ (Ejemplo)". Relación EMP_PROY(NSS, NumProy, Horas, NomEmp, NomProy, LugarProy) y F={NSS→NomEmp; NumProy→NomProy,LugarProy; NSS,NumProy→Horas}. Resultado de aplicar el algoritmo:
- {NSS}+ = {NSS, NomEmp}
- {NumProy}+ = {NumProy, NomProy, LugarProy}
- {NSS, NumProy}+ = {NSS, NumProy, NomEmp, NomProy, LugarProy, Horas}

## Slide 35
Título: "Dependencias funcionales: Equivalencia de conjuntos". Definición: dos conjuntos de DFs E y F son equivalentes sii E+=F+. Esto implica: todas las DFs en E se pueden inferir de F y viceversa; E cubre a F y F cubre a E. Pregunta: ¿cómo determinamos si F cubre a E? Para cada X→Y ∈ E, se calcula X+ respecto a F y se verifica que X+ incluya los atributos en Y.

## Slide 36
Título: "Dependencias funcionales: Equivalencia de conjuntos / Ejemplo". F = {AB→C, B→D, D→GC, CG→H}; F1 = {D→H, B→C, AD→GH}. Preguntas: ¿F1 cubre a F? ¿F cubre a F1? ¿F es equivalente a F1?

## Slide 37
Continuación del ejemplo anterior, agrega F2 = {B→D, D→G, D→C, CG→H}. Preguntas: ¿Qué pasa entre F2 y F? ¿Qué pasa entre F1 y F2?

## Slide 38
Título: "Dependencias funcionales: Cobertura mínimo". Definición: una cobertura mínima de un conjunto de DFs E es un conjunto mínimo de DFs F que satisface: (1) toda dependencia en F tiene un solo atributo en su parte derecha; (2) no se puede reemplazar ninguna X→A en F por Y→A donde Y es subconjunto propio de X y seguir siendo equivalente; (3) no se puede quitar ninguna DF de F y seguir siendo equivalente. Nota roja: "Un conjunto mínimo está en forma estándar o canónica y sin redundancia."

## Slide 39
Título: "Dependencias funcionales: Cobertura mínimo". Algoritmo de 4 pasos para localizar cobertura mínima F para E, con anotaciones:
1. Establecer F := E [Reemplazar dependencias]
2. Reemplazar cada df X→{A1,A2,...,An} en F por las n dfs X→A1, X→A2,...,X→An
3. Por cada df X→A en F, por cada atributo B elemento de X: si {(X-B)+ respecto a F, contiene a A} entonces reemplazar X→A por (X-{B})→A en F [Atributos redundantes]
4. Por cada df X→A sobrante en F: si {F-{X→A}} es equivalente a F, entonces eliminar X→A de F [Dependencias redundantes]

## Slide 40
Título: "Dependencias funcionales: Cobertura mínimo: Ejemplo". Ejemplo resuelto paso a paso: E={B→A, D→A, AB→D}, hallar cubrimiento minimal.
- ¿Hay DF con varios atributos a la derecha? Ninguna.
- ¿Hay atributos redundantes? En AB→D: {A}+={A}, {B}+={B,A,D} → se obtiene E1={B→A, D→A, B→D} (sin atributos redundantes).
- ¿Hay DFs redundantes? En E1-{B→A}, se calcula {B}+={B,D,A} → B→A es redundante y se elimina → E2={D→A, B→D}.
- Resultado: {D→A, B→D} es cubrimiento minimal de E.

## Slide 41
Título: "Modelo Relacional: Restricciones (Llaves)". Ejemplo con esquema Persona(rut, nombre, fecha-de-nacimiento, madre-rut, padre-rut) mostrado 2 veces en recuadros verdes punteados para ilustrar 3 conceptos: súper-llave identifica cada fila (todos los atributos subrayados); llave candidata es súper llave mínima (solo rut subrayado); se escoge una llave candidata como llave primaria (rut subrayado, resto normal).

## Slide 42
Título: "Modelo Relacional: Restricciones (Dependencias funcionales)". Tabla Cervezas con columnas nombre, tipo, grados, ciudad-origen y 7 filas de cervezas chilenas (Austral Lager, Austral Yagan, Austral Pale Ale, Kuntsmann Torobayo, Kross 5, Kross Golden, Kross Pilsner) con sus datos. Pregunta: "¿Hay una dependencia funcional aquí?" Opciones evaluadas en recuadros verdes:
- {nombre} → {tipo, grados, ciudad-origen}
- {nombre} → {tipo, nombre}
- {grados} → {grados}
- {grados} → {tipo, ciudad-origen}

## Slide 43
Continuación de la tabla Cervezas (misma data). Evalúa específicamente {ciudad-origen} → {tipo}. Se resaltan en rojo punteado las filas donde Austral Lager (Lager, Punta Arenas) y Austral Yagan (Ale, Punta Arenas) comparten ciudad-origen pero difieren en tipo. Conclusión en banner rojo: "¡No!" — no es una dependencia funcional.

## Slide 44
Continuación, tabla Cervezas ahora con columna adicional "marca" (Austral, Kuntsmann, Kross) además de nombre/tipo/grados/ciudad-origen, 7 filas. Pregunta: "¿Hay una dependencia funcional aquí usando la llave primaria (a la izquierda)?" Respuestas en recuadros verdes:
- {marca,nombre} → {tipo, grados, ciudad-origen}
- {marca,nombre} → {marca, nombre, tipo, grados, ciudad-origen}

## Slide 45
Título: "Modelo Relacional: Restricciones (Dependencias funcionales)". Definición central resaltada por colores: "Una llave (súper o candidata) de una relación determina funcionalmente a todos los atributos de la relación."

## Slide 46
Continuación con tabla Cervezas (marca, nombre, tipo, grados, ciudad-origen, 7 filas). Pregunta: "¿Cómo podemos encontrar las llaves candidatas usando las dependencias funcionales?" Muestra la DF {marca,nombre} → {marca,nombre,tipo,grados,ciudad-origen} con explicación: "Si la parte derecha contiene todos los atributos, la parte izquierda es una súper llave. Además, si la parte izquierda es mínima en este respecto, es una llave candidata."

## Slide 47
Slide de transición/portada de sección: "FORMAS NORMALES". Referencia: "Capítulo 19 | Ramakrishnan / Gehrke".

## Slide 48
Título: "Normalización de las relaciones". Definiciones con mascota ninja ilustrativa:
- Normalización: el proceso de descomponer las relaciones "malas" insatisfactorias dividiendo sus atributos en relaciones más pequeñas.
- Forma normal: condición mediante el uso de claves y DF de una relación para certificar si un esquema de relación se encuentra en una forma normal particular.

## Slide 49
Título: "Normalización de las relaciones". Diagrama jerárquico: dos círculos agrupan las formas normales — círculo superior "1FN, 2FN" apunta a "MALAS"; círculo del medio "3FN, Boyce-Codd" (relacionado con "Dependencias funcionales") apunta a "BUENAS"; círculo inferior "4FN, 5FN" (relacionado con "Dependencias Multivaluadas" y "Dependencias de JOIN") también apunta a "BUENAS".

## Slide 50
Título: "Normalización de las relaciones". Texto con mascota ninja:
- 2NF, 3NF, BCNF: basadas en claves y DF de un esquema de relación.
- 4NF: basado en claves, dependencias de múltiples valores (MVDs); 5NF basado en claves, dependencias de unión.
Nota morada: es posible que se necesiten propiedades adicionales para garantizar un buen diseño relacional (unión sin pérdida, conservación de la dependencia; Capítulo 11).

## Slide 51
Título: "Normalización de las relaciones". Definiciones: un dominio es atómico si sus elementos se consideran unidades indivisibles. Un esquema relacional R está en primera 1NF si los dominios de todos los atributos de R son atómicos.

## Slide 52
Título: "Normalización de las relaciones". 1NF no permite: atributos compuestos; atributos multivaluados; relaciones anidadas (atributos cuyos valores para una tupla individual no son atómicos). Considerado parte de la definición de una relación. La mayoría de RDBMS solo permiten definir relaciones en 1NF.

## Slide 53
Título: "Normalización de las relaciones". Diagrama entidad-relación tipo mapa conceptual: nodo central "ENTIDAD" conectado a 4 tipos de atributo: "Atributo" (óvalo simple), "Atributo Multivaluado" (óvalo doble), "Atributo de Entidad Débil" (óvalo con línea punteada), "Atributo Clave" (óvalo subrayado), "Atributo Derivado" (óvalo con borde punteado).

## Slide 54
Título: "Normalización de las relaciones". Ejemplo: Matricula(dni, nombres, ApePat, ApeMat, cursos). Pregunta: "¿Algún problema aquí?" (el atributo "cursos" es multivaluado, viola 1NF — implícito).

## Slide 55
Continuación. Solución: crear otra tabla con Alumnos y Matrícula:
- Alumnos(dni, nombres, ApePat, ApeMat)
- Matricula(dni, curso)

## Slide 56
Título: "Todo bien". Tabla Cliente con columnas rut, nombre, fono, dirección; 1 fila (Kelvin, +56976698463, Campo de Hielo Sur Depto 273). Pregunta: "¿Pero si un cliente puede tener varios números de teléfono?"

## Slide 57
Título: "UNF: Forma No Normalizada (UnNormalised Form)". Tabla Cliente con 2 filas: Kelvin (1 teléfono) y Rankine (2 teléfonos en la misma celda: +56991324842,+56223491234). Definición en banner amarillo: "UNF: Varias multiplicidades de valores en una columna de la tabla."

## Slide 58
Título: "1NF: Primera Forma Normal (First Normal Form)". Misma tabla Cliente pero Rankine ahora aparece en 2 filas separadas (una por cada teléfono), duplicando nombre y dirección. Definición en banner amarillo: "1NF: Un valor en cada celda de la tabla."

## Slide 59
Título: "¿Todo bien con sola la 1NF?". Repite la tabla en 1NF (3 filas, Rankine duplicado). Pregunta: "¿Algún problema aquí?"

## Slide 60
Título: "¿Todo bien con sola la 1NF? No". Misma tabla. Se identifica el problema: "Redundancia". Pregunta: "¿Pero por qué es un problema? ¿Sólo espacio?" Se listan 3 anomalías:
- Anomalía de actualización: se puede actualizar la dirección de Rankine en un lugar sin actualizar todos los valores.
- Anomalía de inserción: no se puede insertar un nuevo cliente hasta tener un número de teléfono.
- Anomalía de borrado: si el número de teléfono queda inválido, hay que borrar la fila entera con la dirección, etc.
Nota amarilla: "Soluciones con nulos no cuentan aquí."

## Slide 61
Continuación (misma tabla). Solución: "Crear otra tabla con rut y fono". Pregunta: "¿Pero cómo podemos definir el problema aquí?"

## Slide 62
Slide decorativa: solo un icono de reloj con flecha circular (símbolo de "rebobinar"/tiempo), sin texto. Chrome decorativo — probablemente una transición de la presentación.

## Slide 63
Título: "Modelo Relacional: Restricciones (Llaves)". Definición: "Un conjunto de atributos de una relación forma una llave candidata si es una súper llave y no hay un subconjunto propio de esos atributos que es una súper llave." (Icono de reloj decorativo en la esquina.)

## Slide 64
Título: "Modelo Relacional: Restricciones (Llaves)". Ejemplo con esquema Persona(rut, nombre, fecha-de-nacimiento, madre-rut, padre-rut). Pregunta: "¿Hay otra llave candidata?" Respuesta "Probablemente..." muestra Persona con {nombre, madre-rut, padre-rut} subrayados como posible llave candidata; y "...o puede ser..." muestra {nombre, padre-rut} subrayados, con nota "(si no tenemos un tipo como Gengis Kan)".

## Slide 65
Título: "Modelo Relacional: Restricciones (Llaves)". Definición: "Un atributo es primo si está en alguna llave candidata." (Icono de reloj decorativo.)

## Slide 66
Slide decorativa: icono de reloj con flecha circular hacia adelante (avance rápido), sin texto.

## Slide 67
Título: "Como obtener clave candidatas desde las Dependencias funcionales". Repite la definición: "Una llave (súper o candidata) de una relación determina funcionalmente a todos los atributos de la relación."

## Slide 68
Título: "Como obtener clave candidatas / Heurística de solución". Algoritmo: sea R con conjunto de DFs F, y S el conjunto de llaves candidatas:
1. Para cada atributo atómico Ai de R: si {Ai}+=R, entonces Ai es llave candidata, S=S∪Ai.
2. Para cada par de atributos Ai∉S y Aj∉S: si {AiAj}+=R, entonces S=S∪{AiAj}.
3. Continuar para tres atributos...

## Slide 69
Título: "Como obtener clave candidatas / Heurística de solución: Ejemplo". Relación R(A,B,C,D,E) y F={BD→E, CD→AB, E→C, B→D}. Cálculos de clausuras:
- {E}+ = {E,C}
- {B}+ = {B,D,E,C,A}
- {CD}+ = {C,D,A,B,E}
- {AC}+ = {A,C}
- {AD}+ = {A,D}

## Slide 70
Título: "Descomposición / Definición". Sea R con conjunto de DFs F. Una descomposición R1 y R2 sin pérdida debe: (1) conservar los atributos de R (R=R1∪R2); (2) conservar las dependencias funcionales (F+={F1∪F2}+); (3) no generar tuplas falsas, para lo cual {R1∩R2}→R1 o {R1∩R2}→R2 (la intersección genera una DF válida en F).

## Slide 71
Título: "Descomposición / Ejemplo 1". R(A,B,C,D,E) y F={AB→C, C→D, C→E}. Descomposición R1(A,B,C,D) y R2(C,E) genera F1={AB→C, C→D} y F2={C→E}. Se verifica: conserva atributos, conserva DFs, no genera tuplas falsas porque {R1∩R2}→R2 (C→E ⊂ F+).

## Slide 72
Título: "Descomposición / Ejemplo 2". R(A,B,C,D,E,F) y F={AB→D, AC→E, ABD→F}. Descomposición R1(A,B,D,F) y R2(A,C,E) genera F1={AB→D, ABD→F} y F2={AC→E}. Se verifica en rojo: SÍ genera tuplas falsas, porque ni {R1∩R2}→R1 (A→BDF ⊄ F+) ni {R1∩R2}→R2 (A→CE ⊄ F+) se cumplen.

## Slide 73
Título: "Recordando! Dependencias parciales". Definición: dependencia parcial significa que un atributo no primo depende funcionalmente de parte de una clave candidata (atributo no primo = no forma parte de ninguna clave candidata). Ejemplo: R{ABCD} con AB→CD y A→C; la única clave candidata es AB; C y D son atributos no primos; C depende de A (parte de la clave) → dependencia parcial. Diagrama: tabla PROGRAM con columnas codProgramador, codModulo, nomProgramador, nomModulo, horasTrab, con flechas de colores mostrando: dependencia funcional completa (azul, de codProgramador+codModulo → nomModulo y horasTrab), dependencia funcional parcial (amarillo, codProgramador+codModulo → nomProgramador) y dependencia funcional parcial (roja/naranja, codProgramador → nomProgramador).

## Slide 74
Título: "Normalización en 2FN". Definición: está en 1FN; cada atributo no primo depende funcionalmente de manera total de toda clave de R. Descomposición: las DF parciales (no totales) se llevan a nuevas tablas; en la tabla original queda la clave y los atributos que dependen totalmente de ella.

## Slide 75
Título: "Normalización en 2FN / Ejemplo". R(A,B,C,D,E) y F={AB→CE, B→D}; no está en 2FN. Descomposición: DF parcial AB→CE, entonces R1(A,B,C,E) y R2(B,D), donde (R1∩R2→R2) ⊂ F+.

## Slide 76
Título: "Normalización en 3FN". Definición: está en 2FN; una tabla está en 3FN ssi para toda DF no trivial X→Y en R: X es superclave o Y es atributo primo. Diagrama con dos tablas de ejemplo (columnas A,B,C,D,E,F,G) ilustrando (1) X es superllave y (2) Y es parte de una llave. Descomposición: R(A,X,Y,B) donde X→Y incumple 3FN; crear otra relación con X+ (X es clave); eliminar Y de R.

## Slide 77
Título: "Normalización en 3FN / Ejemplo". Sea R(A,X,Y,B) y F={A→XB, X→Y}; no es 3FN porque X no es superclave. Tomando las F como base: R1(A,X,B) y R2(X,Y), donde (R1∩R2→R2) ⊂ F+.

## Slide 78
Título: "Normalización en 3FN / Descomposición (usando F⁻)". Pasos: calcular F mínimo; convertir cada dependencia en una relación (X→Y ⇒ Ri(XY)); si no está la llave en una relación, agregarla.

## Slide 79
Título: "Normalización en 3FN / Ejemplo". R(A,B,C,D,E) y F={A→B, A→C, C→D, B→E}; F es mínimo. {A}+={A,B,C,D,E} ⇒ A es clave única. Tomando las 4 DFs: R1(A,B) preserva la clave; R2(A,C) preserva la clave; R3(C,D); R4(B,E).

## Slide 80
Título: "Normalización en FNBC". Definición: está en 3FN (válido desde 1FN); para toda DF X→Y en R, X es superclave. Diagrama de tabla (columnas A-G) mostrando la relación X→Y. Descomposición: R(A,X,Y,B) donde X→Y incumple FNBC; crear R1=R-Y y R2(X,Y). Nota roja: esta estrategia de normalización no asegura preservar dependencias, pero sí asegura la recuperación de la información por join.

## Slide 81
Título: "Normalización en FNBC / Ejemplo". R(A,B,C,D,E) y F={A→BC, C→D, B→E}. Paso 1: R no está en FNBC (C→D incumple), se parte en R1(A,B,C,E) y R2(C,D). Paso 2: R1 no está en FNBC (B→E incumple), se parte en R3(A,B,C) y R4(B,E). Resultado final: R2(C,D), R3(A,B,C), R4(B,E).

## Slide 82
Título: "Ejercicio". R(A,B,C,D,E) y F={A→B, A→D, C→E}; normalizar en 3FN y FNBC. Desarrollo: AC→ABCDE, AC es una superllave; no hay atributos primos y tampoco está en 3FN; A→B y A→D ⇒ A→BD; C→E viola FNBC, se parte R1(ABCD) y R2(CE); A→BD viola FNBC, se parte R3(AC) y R4(ABD).

## Slide 83
Título: "Resumen". 4 puntos: (1) Buen diseño evita anomalías; (2) Las dependencias funcionales ayudan a un buen diseño; (3) Ideal es FNBC, pero no siempre se logra; (4) Pero siempre se puede 3FN.

## Slide 84
Título: "Resumen" (con encabezado "CS2041 Base de datos I / Computer Science" y logo UTEC). 4 puntos con flechas:
- Es importante conocer el contexto del negocio para determinar las Dependencias funcionales.
- Un buen diseño del modelo de base de datos evitará anomalías.
- Otra manera de generar modelos de datos es usando dependencias funcionales.
- Mediante las formas normales se puede terminar un buen diseño de la base de datos.

## Slide 85
Slide de cierre decorativa: "GRACIAS" sobre fondo azul con foto de dos personas en laboratorio. Autor: "Teófilo Chambilla". Logos UTEC y "Reinventa el mundo". Chrome decorativo, sin contenido académico adicional.
