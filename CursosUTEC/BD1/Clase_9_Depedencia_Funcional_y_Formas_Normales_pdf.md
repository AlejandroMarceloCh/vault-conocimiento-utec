---
curso: BD1
titulo: Clase 9 - Depedencia Funcional y Formas Normales
slides: 105
fuente: Clase 9 - Depedencia Funcional y Formas Normales.pdf
---

## Slide 1
Portada (decorativa: foto de edificio UTEC concreto). "Dependencia funcional y formas normales". CS2041, Bases de Datos I, Ciclo 2023-2. Profesores: Teófilo Chambilla (tchambilla@utec.edu.pe), Brenner Ojeda (bojeda@utec.edu.pe). Logo UTEC (decorativo).

## Slide 2
"RESULTADOS DE APRENDIZAJE" — 3 bullets con checkboxes: explicar conceptos de normalización de tablas; determinar si un modelo de BD es correcto usando dependencias funcionales; aplicar formas normales 1FN, 2FN, 3FN, FNBC. Icono decorativo de check.

## Slide 3
Roadmap del curso CS2041 Bases de Datos I (ciclo 2021-3): barra de progreso horizontal con módulos — Introducción, Modelo Relacional, Algebra Relacional & Cálculo Relacional, Entidad-Relación, SQL, Actualización/Restricciones, **Formas Normales** (resaltado como módulo actual, en azul claro), Optimización y Procesamiento. Mascota ninja apuntando al módulo actual. Bandera de meta al final.

## Slide 4
"Las preguntas de hoy". Muestra 3 tablas de ejemplo (esquema de sistema solar): tabla **Planeta** (nombre, dist, radio, grav, días, años, temp, anillo) con 8 filas (Mercurio a Neptuno); tabla **Satélite** (nombre, planeta, descubridor, año) con 7 filas; tabla **Aterrizaje** (nave, planeta, país, año) con 7 filas. Pregunta final: "¿Y cómo se puede saber si es un buen diseño relacional o no?"

## Slide 5
"Directrices informales — Directrices de diseño informales para los esquemas de relación". Lista de 4 medidas informales de calidad de diseño (con color distinto cada una): la semántica de los atributos (naranja); la reducción de información redundante en las tuplas (verde); la reducción de valores NULL en las tuplas (azul); prohibición de la posibilidad de generar tuplas falsas (marrón).

## Slide 6
"Directrices informales (Semántica)". Diagrama de 4 esquemas relacionales con atributos: EMPLEADO(NombreE, Dni[PK], FechaNac, Dirección, NumeroDpto[FK]); DEPARTAMENTO(NombreDpto, NumeroDpto[PK], DniDirector[FK]); PROYECTO(NombreProyecto, NumProyecto[PK], UbicaciónProyecto, NumDptoProyecto[FK]); LOCALIZACIONES_DPTO(NumeroDpto[PK,FK], UbicaciónDpto); TRABAJA_EN(Dni[PK,FK], NumProyecto[PK,FK], Horas). Texto: "La facilidad con la que se pueda explicar el significado de los atributos de una relación es una medida informal de lo bien que está diseñada esa relación."

## Slide 7
"Directrices informales (tuplas falsas)". Tabla **Personas** (DniPersona, NomPersona, NomProyecto) con 2 filas (Ana/Proyecto1, Roberto/Proyecto2) y tabla **Proyectos** (NroProy, NomProy) con 3 filas (21/Proyecto1, 55/Proyecto2, 32/Proyecto2). Se muestra el resultado del Join Personas-Proyectos: genera 3 filas, donde Roberto aparece dos veces (con NroProy 55 y 32) porque ambos proyectos se llaman "Proyecto 2" — resaltado en rojo punteado. Pregunta: "¿Ambas son correctas?"

## Slide 8
"Directrices informales (tuplas falsas)". Diagrama de descomposición: relación r(ABC) con 5 filas se proyecta (ρ) en r1(AB) y r2(BC); al recombinar con join natural (⊗) se obtiene r' con filas adicionales resaltadas en rojo marcadas como "tuplas falsas" (filas <1,0,1> y <2,0,4> que no estaban en la relación original). Observación: no todas las descomposiciones se pueden combinar con join natural para reproducir la tabla original.

## Slide 9
"Directrices informales (tuplas falsas)" — segundo ejemplo. Relaciones r1(ABC) con 4 filas y r2(BCD) con 3 filas; se calcula la unión natural r = r1⊗r2 (5 filas resultantes); luego se evalúan las proyecciones r1'=Π_ABC(r) y r2'=Π_BCD(r). Observación: las tablas r2 y r2' son iguales, sin embargo la tupla <2,2,6> está en r1 pero no en r1' (se pierde en la descomposición/recomposición).

## Slide 10
Slide divisoria: "DEPENDENCIAS FUNCIONALES". Referencia: Capítulo 19 | Ramakrishnan / Gehrke.

## Slide 11
"Conceptos básicos". Las DF son un tipo particular de restricción. Permiten expresar hechos acerca de la realidad que se está modelando con la BD.

## Slide 12
"Dependencias funcionales" — definición formal: dada una relación R y dos conjuntos de atributos X∈R, Y∈R, X determina funcionalmente a Y si y sólo si dos tuplas que tienen el mismo valor de X deben por fuerza tener el mismo valor de Y. Nota: X e Y pueden ser atributos compuestos.

## Slide 13
"Dependencias funcionales" — notación X → Y. Lectura: "X determina funcionalmente a Y" o "Y depende funcionalmente de X". Nota en rojo: esto no supone que Y→X en R.

## Slide 14
Slide con fondo oscuro (estilo distinto/código). "Dependencia Funcional {". Izquierda: definición "Una DF es una relación entre atributos". Ejemplo: A→B, donde A="Fecha de nacimiento", B="Edad" — B depende funcionalmente de A (A=determinante, B=dependiente). Derecha: "Un ejemplo más amplio" — captura tipo tabla de código con columnas IDSUC, DIRECCION, TELEFONO, IDGERENTE, 10 filas de datos de sucursales (Miraflores, El Alto, Villa Fatima, etc.). DF: IDSUC → DIRECCION, TELEFONO, IDGERENTE.

## Slide 15
Fondo oscuro, continuación del ejemplo. Tabla con 14 filas: IDSUC, DIRECCION, TELEFONO, IDGERENTE, NOMBRE, SEXO. Flechas naranjas grandes muestran que IDSUC determina todas las demás columnas; flechas verdes resaltan filas con mismo IDGERENTE(31)=mismo NOMBRE(Camila Prieto)/SEXO. DFs mostradas: IDSUC → DIRECCION, TELEFONO, IDGERENTE, NOMBRE, SEXO; IDGERENTE → NOMBRE, SEXO. Fórmula genérica abajo (en gris, ejemplo abstracto): X → Y,Z,W,H,K ; W → H,K.

## Slide 16
Fondo oscuro. "Dependencia Funcional Transitiva {". Dos tablas: EMPLEADO (IDEMP, NOMBRE, APELLIDO, SEXO, FECHA_NAC, FECHA_ING, IDSUC) con 8 filas, y la tabla de sucursales (IDSUC, DIRECCION, TELEFONO, IDGERENTE) con 8 filas. Flechas rojas conectan filas de empleados a la fila 3 (Villa Fatima) de sucursales. DFs: IDEMP → IDSUC; IDSUC → DIRECCION, TELEFONO, IDGERENTE. Fórmula abstracta abajo: X→Y, Y→A,B,C (dependencia transitiva).

## Slide 17
Fondo oscuro. "CLAVES {". Definición de **CLAVE**: dado un esquema R y un conjunto F de DFs, X→R es clave si (1) F implica X→A1,A2,...,An (o sea X→R) y (2) no existe ningún Z⊆X tal que F implica Z→R (condición de minimalidad). Definición de **SUPERCLAVE**: aquella donde X→R, es decir los datos de las columnas X determinan el contenido de las demás columnas. Nota explicativa: la diferencia entre superclave y clave es que la clave es mínima en cantidad de atributos.

## Slide 18
Fondo oscuro. "Reglas {". **AXIOMAS DE ARMSTRONG**: 1. Reflexividad: Si Y⊆X, entonces X→Y. 2. Aumento: {X→Y}⊨XZ→YZ. 3. Transitividad: {X→Y, Y→Z}⊨X→Z. **REGLAS DE INFERENCIA ADICIONALES**: 4. Descomposición: {X→YZ}⊨X→Y y X→Z. 5. Unión: {X→Y, X→Z}⊨X→YZ. 6. Pseudo-transitividad: {X→Y, WY→Z}⊨WX→Z.

## Slide 19
"Ejemplo". Tabla A,B,C,D con 5 filas (a1b1c1d1, a1b2c1d2, a2b2c2d2, a2b3c2d3, a3b3c2d4). Texto: "Consideremos la relación r y veamos qué DF se satisfacen."

## Slide 20
Análisis de A→C: se satisface. Las dos tuplas con valor a1 en A tienen el mismo valor en C (c1); las dos tuplas con a2 tienen el mismo valor en C (c2); no existen otros pares de tuplas con mismo valor en A.

## Slide 21
Análisis de C→A: no se satisface. Contraejemplo: t1=(a2,b3,c2,d3) y t2=(a3,b3,c2,d4) tienen mismo valor en C (c2) pero distintos valores en A (a2 y a3).

## Slide 22
r satisface muchas otras DF: AB→D, A→A y las demás DF triviales. Definición: una DF de la forma α→β es trivial si β⊆α.

## Slide 23
"Dependencias funcionales: Ejemplo" — relación EMP_PROY(DNI, NumProyecto, Horas, NombreE, NombreProyecto, UbicacionProyecto). Diagrama con líneas azules que conectan atributos determinantes con determinados (DF1, DF2, DF3). DFs listadas en recuadros verdes: {DNI, NumProyecto}→{Horas}; {DNI}→{NombreE}; {NumProyecto}→{NombreProyecto, UbicacionProyecto}.

## Slide 24
"Dependencias funcionales: Ejemplo" — caso de negocio: empresa de alquiler de vehículos. Vehículos identificados por matrícula (marca, color, modelo, año). Clientes identificados por cédula (nombre, dirección, teléfono). Contrato de alquiler identificado por número de contrato, entre cliente y vehículo en una fecha (período en días, precio). Restricción: en una misma fecha no se puede alquilar más de una vez el mismo vehículo al mismo cliente.

## Slide 25
Repetición del mismo texto de la slide 24 (mismo caso de negocio del alquiler de vehículos), sin cambios.

## Slide 26
Mismo texto que slides 24-25 pero con resaltado de colores: entidades en naranja (vehículos, clientes, contrato), atributos en verde (matrícula, marca/color/modelo/año, cédula, nombre/dirección/teléfono, número de contrato, fecha, cliente, vehículo, periodo, precio), restricción de negocio resaltada en azul.

## Slide 27
"Dependencias funcionales: Ejemplo" — DFs obtenidas del caso de alquiler: matrícula → {marca, color, modelo, año}; cédula → {nombre, dirección, teléfono}; nroContrato → {fecha, cédula, matrícula, período, precio}; {fecha, cédula, matrícula} → nroContrato.

## Slide 28
"Dependencias funcionales:" Una DF es una propiedad del esquema, no de la instancia. No puede ser inferida automáticamente a partir de una instancia. Una instancia por sí sola es insuficiente para determinar si una DF se cumple (a menos que sea representativa), pero sí puede mostrar que una DF NO se cumple.

## Slide 29
"Dependencias funcionales — Inferencia, deducción". Sea F el conjunto de DFs especificadas en un esquema R. Habitualmente se especifican DFs semánticamente obvias; otras DFs pueden encontrarse/derivarse y satisfacer las dependencias de F — se dice que se infieren o deducen de F.

## Slide 30
Ejemplo de inferencia: si NroDpto→DniDirector y DniDirector→TeléfonoDirector, entonces ambas dependencias juntas suponen NroDpto→TeléfonoDirector. Es una DF inferida que no tiene que declararse explícitamente.

## Slide 31
"Clausura (F+)". Es el conjunto de todas las dependencias que incluye F, junto con las que pueden inferirse de F. El cierre de F (F+) es el conjunto de DF que F implica lógicamente. Dado F, se puede calcular F+ directamente de la definición formal de DF. Nota en rojo: las DF en F+ deben cumplirse para todas las instancias donde se cumpla F.

## Slide 32
"Dependencias funcionales: Reglas de Inferencias" — repite las 6 reglas (RI1 Reflexiva, RI2 Aumento, RI3 Transitiva, RI4 Descomposición/proyección, RI5 Unión/aditiva, RI6 Pseudotransitiva) con las mismas notaciones que slide 18. Nota roja: Reglas de Armstrong RI1-RI3 son minimales, las demás se derivan de ellas.

## Slide 33
"Ejemplo" — Sea R=(A,B,C,G,H,I) y F={A→B, A→C, CG→H, CG→I, B→H}. Se demuestra A→H como miembro de F+: como A→B y B→H, se aplica la regla de transitividad. Comentario: es más fácil usar Axiomas de Armstrong que deducir directamente de las definiciones.

## Slide 34
Continuación del mismo ejemplo (R y F idénticos). Se demuestra CG→HI: como CG→H y CG→I, la regla de unión implica CG→HI.

## Slide 35
Continuación del mismo ejemplo. Se demuestra AG→I en varios pasos: primero A→C se cumple; usando regla de aumento, AG→CG; como CG→I, por transitividad AG→I.

## Slide 36
"Dependencias funcionales: Reglas de Inferencias" — slide solo con el título "Demostración" en cursiva, sin contenido adicional visible (probablemente slide de transición para explicación oral/pizarra).

## Slide 37
"Clausura de X bajo F+" — Algoritmo para determinar X+ bajo F, en pseudocódigo con anotaciones: X+ := X (asigna todos los atributos de X); repetir { antiguaX+ := X+; para cada df Y→Z en F hacer si Y⊆X+ entonces X+ := X+ ∪ Z (agrega atributos a X+) } hasta que antiguaX+ = X+ (no hay más cambios).

## Slide 38
"Clausura de X bajo F+ (Ejemplo)". Relación R(A,B,C,D,E,F), F={AB→C; BC→AD; D→E; CF→B}. Pregunta: ¿cuál es la cerradura de {A,B}? A la derecha se muestra el resultado paso a paso: X=A,B; X[0]=A,B; X[1]=A,B,C; X[2]=A,B,C,D; X[3]=A,B,C,D,E; {A,B}+ = A,B,C,D,E.

## Slide 39
Continuación (slide "...", solución en texto de párrafo tipo LaTeX/serif): explica en prosa el algoritmo aplicado paso a paso al ejemplo de la slide 38, confirmando que {A,B}+ = A,B,C,D,E y que CF→B nunca puede aplicarse porque su lado izquierdo (CF) nunca queda contenido en X.

## Slide 40
"Clausura de X bajo F+ (Ejemplo)" — segundo ejemplo con relación EMP_PROY(NSS, NumProy, Horas, NomEmp, NomProy, LugarProy) y F={NSS→NomEmp; NumProy→NomProy,LugarProy; NSS,NumProy→Horas}. Clausuras resultantes: {NSS}+={NSS,NomEmp}; {NumProy}+={NumProy,NomProy,LugarProy}; {NSS,NumProy}+={NSS,NumProy,NomEmp,NomProy,LugarProy,Horas}.

## Slide 41
"Equivalencia de conjuntos". Dos conjuntos de DFs E y F son equivalentes sii E+=F+. Entonces todas las DFs en E se pueden inferir de F y viceversa (E cubre a F y F cubre a E). Pregunta: ¿cómo determinamos si F cubre a E? Para cada X→Y∈E, se calcula X+ respecto a F y se verifica que X+ incluya los atributos en Y.

## Slide 42
"Equivalencia de conjuntos — Ejemplo": F={AB→C, B→D, D→GC, CG→H}; F1={D→H, B→C, AD→GH}. Preguntas: ¿F1 cubre a F? ¿F cubre a F1? ¿F es equivalente a F1?

## Slide 43
Continuación con F2 añadido: F2={B→D, D→G, D→C, CG→H}. Preguntas: ¿qué pasa entre F2 y F? ¿qué pasa entre F1 y F2?

## Slide 44
"Cobertura mínimo" — definición: una cobertura mínima de un conjunto de DFs E es un conjunto mínimo F que satisface: (1) toda dependencia en F tiene un solo atributo en su parte derecha; (2) no se puede reemplazar X→A por Y→A con Y subconjunto propio de X manteniendo equivalencia; (3) no se puede quitar ninguna DF de F manteniendo equivalencia. Nota roja: un conjunto mínimo está en forma estándar/canónica y sin redundancia.

## Slide 45
"Cobertura mínimo — Algoritmo para localizar cobertura mínima F para E", en 4 pasos con anotaciones de color: 1. Establecer F:=E. 2. Reemplazar cada df X→{A1,...,An} en F por las n dfs X→A1,...,X→An (nota: "reemplazar dependencias"). 3. Por cada df X→A en F, por cada atributo B∈X, si (X-B)+ respecto a F contiene a A entonces reemplazar X→A por (X-{B})→A (nota: "atributos redundantes"). 4. Por cada df X→A sobrante, si {F-{X→A}} es equivalente a F entonces eliminar X→A de F (nota: "dependencias redundantes").

## Slide 46
Slide con fondo tipo apunte universitario/watermark institucional (posible captura de otro material). "Algoritmo para obtener el recubrimiento no redundante" en 3 pasos: 1. Obtener implicados simples (aplicar axioma de proyectividad hasta que todo implicado conste de un solo atributo). 2. Eliminar atributos superfluos en implicantes. 3. Eliminar dependencias redundantes.

## Slide 47
Fondo con watermark institucional. Ejercicio: calcular el recubrimiento no redundante de L. T={A,B,C,D,E,F}; L={A→BC, C→D, AC→E, AB→C, F→A}.

## Slide 48
Continuación del ejercicio. Paso 1: obtener implicados simples. L1={A→B, A→C, C→D, AC→E, AB→C, F→A} (se descompuso A→BC en A→B y A→C).

## Slide 49
Paso 2: eliminar atributos superfluos en implicantes. Pregunta: ¿es redundante C en AC→E? Se calcula L1-{AC→E}.

## Slide 50
Continuación: se calcula A+ respecto a L1-{AC→E} = ABCD. Como C∈A+, entonces C es redundante en AC→E y se obtiene L2.

## Slide 51
Se muestra L2={A→B, A→C, C→D, A→E, AB→C, F→A} (AC→E se reemplazó por A→E).

## Slide 52
Resumen combinado de los pasos 1 y 2 en una sola slide (recapitulación visual: T, L, Paso 1 con L1, Paso 2 con L1-{AC→E}, A+ = ABCD, L2).

## Slide 53
Continuación paso 2: ¿es redundante A en AB→C? Se calcula L2-{AB→C}={A→B, A→C, C→D, A→E, F→A}.

## Slide 54
Continuación: B+ respecto a L2-{AB→C} = B. Como A∉B+, entonces A NO es redundante en AB→C. Pregunta siguiente: ¿es redundante B en AB→C?

## Slide 55
Continuación: A+ respecto a L2-{AB→C} = ABCDE. Como B∈A+, entonces B es redundante en AB→C y se obtiene L3={A→B, A→C, C→D, A→E, A→C, F→A} (AB→C se reemplazó por A→C, quedando duplicado con A→C existente).

## Slide 56
Paso 3: eliminar dependencias redundantes. ¿Es redundante A→B? Se calcula L3-{A→B}={A→C, C→D, A→E, B→C, F→A}, A+ respecto a esto = ACDE. Como B∉A+, entonces A→B NO es redundante. Pregunta siguiente: ¿es redundante A→C? A+ respecto a L3-{A→C} = ABCDE.

## Slide 57
Continuación: como C∈A+ respecto a L3-{A→C}, entonces A→C es redundante y se obtiene L4={A→B, C→D, A→E, A→C, F→A} (cobertura mínima final del ejercicio).

## Slide 58
"Cobertura mínimo: Ejemplo" (fondo watermark, tipo apunte formal en serif). Ejemplo: E={B→A, D→A, AB→D}, hallar el cubrimiento minimal. Pasos con anotaciones de color: no hay DF con varios atributos a la derecha (reemplazar dependencias); atributos redundantes en AB→D: {A}+={A}, {B}+={B,A,D} → se obtiene E1={B→A, D→A, B→D} (sin atributos redundantes); DFs redundantes en E1: en E1-{B→A}, {B}+={B,D,A} → B→A es redundante y se elimina → E2={D→A, B→D} (sin DFs redundantes). Conclusión: {D→A, B→D} es cubrimiento minimal de E.

## Slide 59
"Modelo Relacional: Restricciones (Llaves)". Ejemplo con esquema Persona(rut, nombre, fecha-de-nacimiento, madre-rut, padre-rut) repetido en 3 recuadros verdes: (1) súper-llave (identifica cada fila, todos los atributos subrayados); (2) llave candidata (súper llave mínima, con subconjunto subrayado: rut, nombre, fecha-de-nacimiento, madre-rut, padre-rut con distinto subrayado parcial); (3) se escoge una llave candidata como llave primaria (solo rut subrayado).

## Slide 60
"Modelo Relacional: Restricciones (Dependencias funcionales)". Tabla **Cervezas** (nombre, tipo, grados, ciudad-origen) con 7 filas (Austral Lager, Austral Yagan, etc.). Pregunta: ¿hay una dependencia funcional aquí? Se listan 4 posibles DFs en recuadros verdes: {nombre}→{tipo,grados,ciudad-origen}; {nombre}→{tipo,nombre} (trivial); {grados}→{grados} (trivial); {grados}→{tipo,ciudad-origen} (pregunta implícita a evaluar, continúa "...").

## Slide 61
Continuación: se evalúa {ciudad-origen}→{tipo}. Se resalta en la tabla que Austral Lager (tipo Lager) y Austral Yagan (tipo Ale) comparten ciudad-origen (Punta Arenas) pero tienen tipos distintos — marcado con recuadros rojos punteados. Conclusión: "¡No!" es una dependencia funcional.

## Slide 62
"Modelo Relacional: Restricciones (Dependencias funcionales)". Misma tabla Cervezas pero ahora con columnas reordenadas: marca, nombre, tipo, grados, ciudad-origen (7 filas). Pregunta: ¿hay una DF aquí usando la llave primaria {marca,nombre}? DFs: {marca,nombre}→{tipo,grados,ciudad-origen}; {marca,nombre}→{marca,nombre,tipo,grados,ciudad-origen} (trivial, incluye todos los atributos).

## Slide 63
"Modelo Relacional: Restricciones (Dependencias funcionales)". Texto explicativo: "Una llave (súper o candidata) de una relación determina funcionalmente a todos los atributos de la relación" (frase con palabras resaltadas en colores distintos por rol semántico).

## Slide 64
Misma tabla Cervezas (marca, nombre, tipo, grados, ciudad-origen). Pregunta: ¿cómo podemos encontrar las llaves candidatas usando las DFs? Se muestra {marca,nombre}→{marca,nombre,tipo,grados,ciudad-origen} con explicación: si la parte derecha contiene todos los atributos, la parte izquierda es una súper llave; además, si la parte izquierda es mínima, es una llave candidata.

## Slide 65
Slide divisoria: "FORMAS NORMALES". Referencia: Capítulo 19 | Ramakrishnan / Gehrke.

## Slide 66
"Normalización de las relaciones". Definiciones con mascota ninja ilustrativa: Normalización = proceso de descomponer relaciones "malas" insatisfactorias dividiendo sus atributos en relaciones más pequeñas. Forma normal = condición mediante uso de claves y DF para certificar si un esquema se encuentra en una forma normal particular.

## Slide 67
"Normalización de las relaciones" — diagrama con 3 círculos: (1FN, 2FN) → MALAS; (3FN, Boyce-Codd) conectado por llave {Dependencias funcionales} → BUENAS; (4FN, 5FN) conectado por llave {Dependencias Multivaluadas, Dependencias de JOIN} → BUENAS.

## Slide 68
"Normalización de las relaciones". 2NF, 3NF, BCNF basadas en claves y DF de un esquema de relación. 4NF basado en claves y dependencias de múltiples valores (MVDs); 5NF basado en claves y join dependencies. Nota: puede necesitarse propiedades adicionales (unión sin pérdida, conservación de dependencia; Capítulo 11).

## Slide 69
"Normalización de las relaciones". Un dominio es atómico si sus elementos son unidades indivisibles. Un esquema R está en 1NF si los dominios de todos los atributos de R son atómicos (texto en rojo, definición clave).

## Slide 70
"Normalización de las relaciones". 1NF no permite: atributos compuestos, atributos multivaluados, relaciones anidadas (atributos cuyos valores para una tupla individual no son atómicos). Considerado parte de la definición de relación. La mayoría de RDBMS solo permiten definir relaciones en Primera Forma Normal.

## Slide 71
"Normalización de las relaciones". Diagrama tipo entidad-relación (notación Chen) mostrando ENTIDAD conectada a: Atributo, Atributo Multivaluado (doble elipse), Atributo de Entidad Débil, Atributo Clave (subrayado), Atributo Derivado (elipse punteada) — ilustra los tipos de atributos que 1NF prohíbe.

## Slide 72
"Normalización de las relaciones". Esquema Matricula(dni, nombres, ApePat, ApeMat, cursos) — "cursos" sería multivaluado. Pregunta: ¿algún problema aquí?

## Slide 73
"Normalización de las relaciones". Solución: crear otra tabla con Alumnos y Matrícula. Alumnos(dni, nombres, ApePat, ApeMat); Matricula(dni, curso).

## Slide 74
"Todo bien". Tabla Cliente(rut, nombre, fono, dirección) con 1 fila de ejemplo (Kelvin, +56976698463, Campo de Hielo Sur Depto 273). Pregunta: ¿pero si un cliente puede tener varios números de teléfono?

## Slide 75
"UNF: Forma No Normalizada (UnNormalised Form)". Tabla Cliente con 2 filas, la segunda (Rankine) tiene 2 valores de teléfono en una sola celda ("+56991324842,+56223491234"). Definición UNF: varias multiplicidades de valores en una columna de la tabla.

## Slide 76
"1NF: Primera Forma Normal (First Normal Form)". Misma tabla pero ahora Rankine aparece en 2 filas separadas, una por cada teléfono (3 filas totales). Definición 1NF: un valor en cada celda de la tabla.

## Slide 77
"¿Todo bien con sola la 1NF?" — misma tabla de 3 filas. Pregunta: ¿algún problema aquí?

## Slide 78
"¿Todo bien con sola la 1NF? No". Se identifica el problema: **Redundancia** (rut, nombre y dirección de Rankine se repiten). Nota amarilla: soluciones con nulos no cuentan aquí. Se explican 3 anomalías: **Anomalía de actualización** (se puede actualizar la dirección en un lugar sin actualizar todos los valores); **Anomalía de inserción** (no se puede insertar un cliente nuevo hasta tener un teléfono); **Anomalía de borrado** (si el teléfono es inválido, hay que borrar toda la fila con la dirección, etc.).

## Slide 79
"¿Todo bien con sola la 1NF? No". Solución: crear otra tabla con rut y fono. Pregunta: ¿pero cómo podemos definir el problema aquí?

## Slide 80
Slide decorativa: solo un ícono de reloj con flecha (símbolo de "recordar"/timer), sin texto.

## Slide 81
"Modelo Relacional: Restricciones (Llaves)". Repite definición de llave candidata: un conjunto de atributos forma una llave candidata si es una súper llave y no hay un subconjunto propio de esos atributos que sea una súper llave.

## Slide 82
"Modelo Relacional: Restricciones (Llaves)". Esquema Persona(rut, nombre, fecha-de-nacimiento, madre-rut, padre-rut). Pregunta: ¿hay otra llave candidata? Respuestas sugeridas: probablemente {nombre, fecha-de-nacimiento, madre-rut, padre-rut} o {nombre, fecha-de-nacimiento, padre-rut} (si no hay homónimos exactos, nota jocosa "si no tenemos un tipo como Gengis Kan").

## Slide 83
"Modelo Relacional: Restricciones (Llaves)". Definición: un atributo es primo si está en alguna llave candidata.

## Slide 84
Slide decorativa: ícono de reloj con flecha en sentido opuesto (símbolo "adelantar"/redo), sin texto.

## Slide 85
"Como obtener clave candidatas desde las Dependencias funcionales". Repite frase: una llave (súper o candidata) de una relación determina funcionalmente a todos los atributos de la relación.

## Slide 86
Fondo watermark institucional. "Algoritmo para el cálculo de una clave de un esquema R(T,L)": L debe ser no redundante. Se definen conjuntos: I (atributos que aparecen solo como implicantes/izquierda), D (solo como implicados/derecha), ID (aparecen a ambos lados), N (no aparecen en ninguna dependencia). Z=I∪N es el núcleo (intersección de todas las claves). Si Z+=T, Z es clave única; si no, se añaden atributos de ID hasta que el cierre sea T.

## Slide 87
Fondo watermark. Ejemplo: T={A,B,C,D,E,F}; L={A→B, C→D, A→E, A→C, F→A}. L es no redundante. I={F}, D={B,D,E}, ID={A,C}, N={}. Z=I∪N={F}. Z+=F+=ABCDEF=T. Conclusión: F es clave única de R(T,L).

## Slide 88
Fondo watermark. Segundo ejemplo: T={A,B,C,D,E,F,G}; L={AB→C, CD→E, C→A, DE→F}. I={B,D}, D={F}, ID={A,C,E}, N={G}. Z=I∪N={B,D,G}. Z+=(BDG)+=BDG≠T. Como Z+≠T, se prueban añadir elementos de ID: ABDG+=ABCDEFG=T → ABDG es clave candidata; BCDG+=ABCDEFG=T → BCDG también es clave candidata (nota: no tiene por qué ser única).

## Slide 89
"Como obtener clave candidatas — Heurística de solución". Sea la relación R, conjunto de DFs F, S conjunto de llaves candidatas: 1. Para cada atributo atómico Ai de R, si {Ai}+=R entonces Ai es llave candidata (S=S∪Ai). 2. Para cada par de atributos Ai∉S y Aj∉S, si {AiAj}+=R entonces S=S∪{AiAj}. 3. Continuar para tres atributos...

## Slide 90
"Como obtener clave candidatas — Heurística de solución: Ejemplo". Relación R(A,B,C,D,E), F={BD→E, CD→AB, E→C, B→D}. Se calculan: {E}+={E,C}; {B}+={B,D,E,C,A} (llave candidata, en negrita); {CD}+={C,D,A,B,E} (llave candidata, en negrita); {AC}+={A,C}; {AD}+={A,D}.

## Slide 91
"Descomposición — Definición". Sea la relación R y su conjunto de DFs F. Una descomposición R1 y R2 sin pérdida debe: (1) conservar los atributos de R (R=R1∪R2); (2) conservar las dependencias funcionales (F+={F1∪F2}+); (3) no generar tuplas falsas, para lo cual {R1∩R2}→R1 ó {R1∩R2}→R2 (la intersección genera una DF válida en F).

## Slide 92
"Descomposición — Ejemplo". R(A,B,C,D,E), F={AB→C, C→D, C→E}. Descomposición R1(A,B,C,D) y R2(C,E) genera F1={AB→C, C→D} y F2={C→E}. Se verifica: conserva atributos, conserva DFs, no genera tuplas falsas ya que {R1∩R2}→R2: C→E⊂F+.

## Slide 93
"Descomposición — Ejemplo 2". R(A,B,C,D,E,F), F={AB→D, AC→E, ABD→F}. Descomposición R1(A,B,D,F) y R2(A,C,E) genera F1={AB→D, ABD→F} y F2={AC→E}. Se verifica: conserva atributos y DFs, pero **SÍ genera tuplas falsas** ya que {R1∩R2}→R1: A→BDF⊄F+ y {R1∩R2}→R2: A→CE⊄F+.

## Slide 94
"Recordando! Dependencias parciales". Definición: dependencia parcial = un atributo no primo depende funcionalmente de parte de una clave candidata. Ejemplo: R{ABCD}, DFs AB→CD y A→C. La única clave candidata es AB; C y D son no primos; C depende de A (parte de la clave candidata) — dependencia parcial. Diagrama: tabla PROGRAM(codProgramador[subrayado], codModulo[subrayado], nomProgramador, nomModulo, horasTrab) con flechas de colores mostrando dependencia funcional completa (azul, desde {codProgramador,codModulo} a horasTrab), dependencia funcional parcial (amarillo, desde codModulo a nomModulo) y dependencia funcional parcial (rojo/naranja, desde codProgramador a nomProgramador).

## Slide 95
"Normalización en 2FN — Definición": está en 1FN; cada atributo no primo depende funcionalmente de manera total de toda clave de R. "Descomposición": las DF parciales (no totales) se llevan a nuevas tablas; en la tabla original queda la clave y los atributos que dependen totalmente de ella.

## Slide 96
"Normalización en 2FN — Ejemplo". R(A,B,C,D,E), F={AB→CE, B→D}. No está en 2FN. Descomposición: DF parcial AB→CE, entonces R1(A,B,C,E) y R2(B,D); verificación (R1∩R2→R2)⊂F+.

## Slide 97
"Normalización en 3FN — Definición": está en 2FN; una tabla está en 3FN ssi para toda DF no trivial X→Y en R: X es superclave o Y es atributo primo. Diagrama con dos esquemas tabulares (ABCDEFG) ilustrando caso (1) X es superllave y caso (2) Y es parte de una llave. "Descomposición": R(A,X,Y,B) donde X→Y incumple 3FN; crear otra relación con X+ (donde X es clave); eliminar Y de R.

## Slide 98
"Normalización en 3FN — Ejemplo". R(A,X,Y,B), F={A→XB, X→Y}. No es 3FN, X no es superclave. Descomposición usando F: R1(A,X,B), R2(X,Y); verificación (R1∩R2→R2)⊂F+.

## Slide 99
"Normalización en 3FN — Descomposición (usando F⁻)": calcular F mínimo; convertir cada dependencia en una relación (X→Y ⟹ Ri(XY)); si no está la llave en una relación, agregarla.

## Slide 100
"Normalización en 3FN — Ejemplo". R(A,B,C,D,E), F={A→B, A→C, C→D, B→E}. F es mínimo. {A}+={A,B,C,D,E} ⟹ A es clave única. Tomando las 4 DFs: R1(A,B) preserva la clave; R2(A,C) preserva la clave; R3(C,D); R4(B,E).

## Slide 101
"Normalización en FNBC — Definición": está en 3FN (válido desde 1FN); para toda DF X→Y en R: X es superclave. Diagrama tabular (ABCDEFG) mostrando X como superllave que determina el resto. "Descomposición": R(A,X,Y,B) donde X→Y incumple FNBC; crear dos relaciones R1=R-Y y R2(X,Y). Nota roja: esta estrategia de normalización no asegura preservar dependencias, pero sí asegura la recuperación de la información por join.

## Slide 102
"Normalización en FNBC — Ejemplo". R(A,B,C,D,E), F={A→BC, C→D, B→E}. Paso 1: R no está en FNBC, C→D incumple → se parte en R1(A,B,C,E) y R2(C,D). Paso 2: R1 no está en FNBC, B→E incumple → se parte en R3(A,B,C) y R4(B,E). Resultado final: R2(C,D), R3(A,B,C) y R4(B,E).

## Slide 103
"Ejercicio". R(A,B,C,D,E), F={A→B, A→D, C→E}. Normalizar en 3FN y FNBC. Desarrollo: AC→ABCDE, AC es superllave. No hay atributos primos y tampoco está en 3FN. A→B y A→D ⟹ A→BD. C→E viola FNBC → se parte R1(ABCD) y R2(CE). A→BD viola FNBC → se parte R3(AC) y R4(ABD).

## Slide 104
"Resumen" (primera versión breve): 1. Buen diseño evita anomalías. 2. Las dependencias funcionales ayudan a un buen diseño. 3. Ideal es FNBC, pero no siempre se logra. 4. Pero siempre se puede 3FN.

## Slide 105
Slide de cierre "Gracias" (con logo UTEC, decorativa). Contiene además un "Resumen" final ampliado con 4 bullets con flechas: es importante conocer el contexto del negocio para determinar las Dependencias funcionales; un buen diseño del modelo de base de datos evitará anomalías; otra manera de generar modelos de datos es usando dependencias funcionales; mediante las formas normales se puede terminar un buen diseño de la base de datos. Nota: la imagen de fondo del cierre (edificio de concreto UTEC) es decorativa.
