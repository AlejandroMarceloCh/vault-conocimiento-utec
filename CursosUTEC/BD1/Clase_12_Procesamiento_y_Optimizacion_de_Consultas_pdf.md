---
curso: BD1
titulo: Clase 12 Procesamiento y Optimización de Consultas
slides: 111
fuente: Clase 12 Procesamiento y Optimización de Consultas.pdf
---

## Slide 1

Portada del curso. Título "PROCESAMIENTO Y OPTIMIZACIÓN DE CONSULTAS". CS2041 - Base de Datos I, Ciclo 2024-1. Profesores: Teófilo Chambilla (tchambilla@utec.edu.pe) y Brenner Ojeda (bojeda@utec.edu.pe). Imagen decorativa de fondo (silueta de persona con equipo topográfico sobre patrón tecnológico azul). Logo UTEC y frase "Reinventa el mundo" decorativos.

## Slide 2

Slide "Índice" con lista de temas del capítulo:
- Memoria
- Procesamiento de consulta
- Optimización sintáctica
- Optimización física (costos, indexs)
- Optimización semántica

Ilustración decorativa a la derecha: mano robótica sobre mapa/globo digital iluminado.

## Slide 3

Título "CS2041 Base de Datos I / Ciclo 2024-1". Diagrama del mapa curricular del curso: fila superior muestra "Introducción" y el bloque resaltado en azul "Planificación y Optimización de Consultas" (tema del día) con un ícono de bandera a cuadros (meta) a la derecha. Fila inferior lista los módulos del curso como barras horizontales de progreso (coloreadas en azul = ya vistos, celeste claro = pendientes): Modelo Relacional, Álgebra Relacional & Cálculo Relacional, SQL, Formas Normales, Transacciones, NoSQL; con sub-etiquetas Entidad-Relación, Actualización/Restricciones, Dependencias funcionales. Ícono de personaje ninja/mago (mascota del curso) señalando el bloque actual.

## Slide 4

"RESULTADOS DE APRENDIZAJE" — lista de checkboxes:
- Podrá explicar Optimización sintáctica, físico y semántico.
- Utilizar algoritmos de optimización de consultas SQL, como Hash-Join, Nested-Loop, Merge-Join.
- Podrá explicar y utilizar correctamente los índices Hash y Árboles B+.
Ícono decorativo de check verde sobre tablet.

## Slide 5

"Motivación". Diagrama con un ícono de ojo a la izquierda apuntando (líneas punteadas) hacia tres elementos: un ícono de mascota ninja (arriba), el texto "Modelo Relacional" (centro, línea punteada horizontal), y un ícono de engranajes/consola (abajo). A la derecha, cadena vertical de íconos con flechas: bombilla (idea) → portapapeles (requisitos) → "ER" → "Modelo Relacional" → "SQL" → ícono de archivo binario (010 100 010). Representa el flujo de diseño de BD hasta la ejecución física.

## Slide 6

"Las preguntas de hoy". Muestra tres tablas de ejemplo (dominio astronómico):
- Tabla **Planeta**: columnas nombre, dist, radio, grav, días, años, temp, anillo. Filas: Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano, Neptuno con sus valores numéricos.
- Tabla **Satélite**: nombre, planeta, descubridor, año (Luna/Tierra, Ganímedes/Júpiter/Galileo Galilei/1610, Calisto, Europa, Ío, Titán/Saturno/Christiaan Huygens/1655, Tritón/Neptuno/William Lassell/1846).
- Tabla **Aterrizaje**: nave, planeta, país, año (Messenger/Mercurio/EEUU/2015, Venera 3/Venus/URRS/1966, Pioneer/Venus/EEUU/1978, Mars 2 lander/Marte/URRS/1971, Viking 1/Marte/EEUU/1976, Beagle 2/Marte/ESA/2003, Galileo/Júpiter/EEUU/2003).
Debajo, dos preguntas guía en recuadros punteados: "¿Cómo se deberían guardar las tablas en memoria?" y "Y ¿cómo se pueden optimizar las consultas sobre estas tablas?".

## Slide 7

Slide separador de sección "1 Memoria". Fondo foto de un edificio de UTEC teñido de azul. Cita: "Capítulo 9.1 | Ramakrishnan / Gehrke" (decorativa/portada de sección).

## Slide 8

"Acceso a memoria". Dos diagramas de bloques de memoria numerados (1,2,3,4,5,6,…):
- **Secuencial**: flechas curvas conectan cada bloque con el siguiente en orden (1→2→3→4→5→6).
- **Aleatorio**: flechas curvas saltan entre bloques no consecutivos (patrón desordenado, ej. 1→3, 2→5, etc.), ilustrando accesos no secuenciales.

## Slide 9

"Costos de acceder a los datos (estimaciones)". Diagrama con un CPU al centro-superior y tres flechas de doble sentido hacia tres tipos de almacenamiento con su ancho de banda (transmisión) y latencia:
- Memoria Principal: 30 GB/s, latencia 50–150 ns (verde).
- Disco de Estado Sólido: 600 MB/s, latencia 10–100 μs (beige).
- Disco Duro: 100 MB/s, latencia 5–15 ms (rojo).
Recuadro rojo punteado: "¡El Disco Duro es muy lento! En particular para acceso aleatorio (latencia)".

## Slide 10

"Costos de acceder a los datos (estimaciones)" (continuación). Pregunta en recuadro punteado: "¿Por qué usamos el disco duro entonces?". Comparación visual: Memoria Principal (imagen de RAM, verde) marcada "Más rápida ✔" vs Disco Duro (imagen de HDD, rojo) marcado "✔ Más barato, ✔ Persistente, ✔ Capacidad".

## Slide 11

"Alta latencia de los discos duros". Pregunta: "¿Por qué la latencia de discos duros es tan alta?". Fotografía real de un disco duro abierto mostrando el brazo mecánico/cabezal de lectura y el plato. Pie: "Tiene un brazo mecánico que tiene que moverse para cambiar el bloque".

## Slide 12

"Bloques en el disco duro". Captura de pantalla real de una herramienta de desfragmentación de Windows: tabla con columnas Drive, Name, Action, Status, Total files, Frag. files, Degree of fragmentation, Size, Free, File system (discos C:, D:, E: con % de fragmentación) y debajo un mapa visual de clusters/bloques coloreado en rojo/azul (fragmentados/contiguos). Recuadro amarillo: "Más eficiente al nivel de hardware. Evite espacio no usable." Foto decorativa de autos estacionados en paralelo (metáfora de bloques ordenados).

## Slide 13

Slide separador "2 Procesamiento de consultas". Fondo edificio UTEC azul (mismo estilo que slide 7).

## Slide 14

"SQL es un lenguaje declarativo" (resaltado en verde). Texto: "Uno dice lo que quiere, no cómo debería ser computado". Diagrama: 4 tarjetas de código SQL a la izquierda mostrando 4 formas equivalentes de escribir la misma consulta (1) Selección/producto, (2) Join explícito, (3) Consulta anidada FROM, (4) Consulta anidada WHERE/IN — todas apuntan con flechas hacia un ícono central de "Caja Negra" (cubo dorado con base de datos), que a su vez produce una tabla de resultados (terminal negra) con columnas nombre/genero (lista de nombres tipo Abbott, Acevedo, etc.).

## Slide 15

Repetición de "SQL es un lenguaje declarativo" con bullets: "Uno dice lo que quiere...", "Idealmente, el motor puede elegir el mejor plan...", "El usuario no tiene que preocuparse...". Meme decorativo: perro dorado frente a computadoras con texto "NO TENGO IDEA / DE LO QUE ESTOY HACIENDO" (humor sobre la caja negra del optimizador). Las 4 tarjetas de código y la tabla de resultados aparecen atenuadas de fondo.

## Slide 16

"Procesamiento de consultas". Mismo diagrama de las 4 tarjetas SQL → Caja Negra → tabla resultado, ahora en primer plano (sin atenuar), reforzando el concepto.

## Slide 17

"Procesamiento y optimización de consultas". Diagrama de flujo vertical del pipeline de ejecución de una consulta SQL:
Consulta (SQL) → [Análisis léxico y sintáctico / Validación] (anotado "Compilador") → Forma intermedia (anotado "Árbol o grafo de consulta") → [Optimizador] (morado, anotado "Verifica Índices") → Plan de ejecución → [Generador de Código] (naranja, anotado "Modo compilado o interpretado") → Código (anotado "Tipo de ejecución") → [Procesador de BD] (marrón) → Resultado (anotado "Si hay error, el mensaje correspondiente"). Mascota ninja señalando el diagrama.

## Slide 18

"¿Cómo evaluar una consulta SQL?". Lista:
- Análisis sintáctico: ¿está bien escrita?
- Análisis semántico: ¿qué sentido tiene?
- ¿qué posibilidades tenemos para ejecutarla?
- ¿Cuál es la posibilidad más conveniente (más rápida, más "barata", etc)?
- Tomar la decisión.
Captura de pantalla decorativa de un editor SQL con anotaciones tipo "Column Alias", "Table Alias", "Table Alias Usage For Join" señalando partes de una consulta SELECT...FROM...INNER JOIN...ON.

## Slide 19

Slide separador "3 Optimización Sintáctica". Fondo edificio UTEC azul.

## Slide 20

"Traducción de SQL al álgebra relacional". Ejemplo: consulta SQL `SELECT APELLIDO, NOMBRE FROM EMPLEADO WHERE SALARIO > (SELECT MAX(SALARIO) FROM EMPLEADO WHERE NUMD=5);` etiquetada como "Bloque de consulta 1" (la externa) y "Bloque de consulta 2" (la subconsulta). Se traduce a álgebra relacional:
- Bloque 1: π_APELLIDO,NOMBRE(σ_SALARIO>C(EMPLEADO))
- Bloque 2: F_MAX(SALARIO)(σ_NUMD=5(EMPLEADO))
Nota: "Se evalúa sólo una vez. El resultado se trata como una constante (>C)". Ambos bloques etiquetados "Elegir plan de consulta".

## Slide 21

"Plan de Ejecución". Consulta SQL: `SELECT C.Comprador FROM Producto P, Compra C, Persona Q WHERE P.categoria='telefono' AND C.comprador=Q.nombre AND C.prod=P.nombre;`. A la derecha, árbol del plan de ejecución (de abajo hacia arriba):
```
π comprador
  σ categoria='telefono'
    |x| comprador=nombre (Hash Join)
      |x| prod=pnombre (B+ Tree)
        Compra    Producto
      Persona
```
Definición: "Plan: Árbol de operadores de álgebra relacional con la elección de algoritmos por cada operador." Nota roja: "Lo ideal es conseguir el mejor plan. En la práctica se evitan los peores."

## Slide 22

"Optimización sintáctica: Heurística". Bullets:
- Objetivo: reducir el tamaño de las tablas intermedias.
- Optimizador: Reglas heurísticas (modifican la representación interna de la consulta); después se genera un plan de ejecución (para ejecutar grupos de operaciones, según los caminos de acceso que tengan los ficheros).
- Regla principal: Primero ejecutar seleccionar (σ) y proyectar (π); al final ejecutar reunir (|×|, *) y otras operaciones binarias.

## Slide 23

"Árbol de consulta". Consulta SQL de ejemplo con PROYECTO, DEPARTAMENTO, EMPLEADO (P.NÚMD=D.NÚMEROD AND D.NSS_JEFE=E.NSS AND P.LOCALIZACIÓN='Stafford'). Árbol de operadores ya optimizado (orden de ejecución de abajo hacia arriba, indicado con flecha vertical):
```
π P.NÚMEROP,P.NÚMD,E.APELLIDO,E.DIRECCIÓN,E.FECHA_NCTO
  |×| D.NSS_JEFE=E.NSS
    |×| P.NÚMD=DNÚMEROD  —  E
      σ P.LOCALIZACIÓN='Stafford'  —  D
        P
```

## Slide 24

"Árbol de consulta inicial o canónico". Misma consulta SQL que slide 23. Recuadro verde con notas: "Lo genera el analizador sintáctico de manera estándar", "Sin optimizar", "Primero los ×, luego condiciones de σ y |×|. Por último π.", "Muy ineficiente (debido a los ×)" (en rojo). Árbol canónico (sin optimizar):
```
π P.NÚMEROP,...
  σ D.NSS_JEFE=E.NSS Y P.NÚMD=DNÚMEROD Y P.LOCALIZACIÓN='Stafford'
    ×
      ×  — E
    P — D
```

## Slide 25

"Optimización con árboles: ejemplo". Consulta SQL sobre EMPLEADO, TRABAJA_EN, PROYECTO (apellidos de empleados que trabajan en proyecto 'Acuario' nacidos después de 1957). Árbol canónico sin optimizar a la derecha (π APELLIDO → σ con todas las condiciones AND → × → × → Empleado, Trabaja_En, Proyecto). Notas: "Transformar el árbol en uno de ejecución eficiente", "Basada en reglas de equivalencia (r.e.)...", "Reglas heurísticas: guían la aplicación de las r.e". Globo de texto: "Los × crean un fichero muy grande. Sólo se necesita usar la tupla del proyecto Acuario. Sólo reunir los empleados nacidos después de 1957." y "Mejor primero los σ".

## Slide 26

"Optimización con árboles: ejemplo(2)". Comparación lado a lado de dos versiones del árbol (paso 1 → paso 2), transformación "Mejor primero los σ": el árbol 1 (σ único con todas las condiciones) se transforma en árbol 2 donde las condiciones σ se separan y se empujan hacia abajo, cerca de sus tablas hoja respectivas (σNSSE=NSS, σNOMBREP='Acuario', σFECHA_NCTO>'31-DIC-1957'). Nota verde: "Mejor que el primer × sea con el proyecto Acuario que sólo obtiene una tupla (NOMBREP es clave)".

## Slide 27

"Optimización con árboles: ejemplo(3)". Continúa la transformación (paso 2→3): recoloca el primer × para que sea con Proyecto (tupla única) en vez de Empleado×Trabaja_En. Nota: "Mejor primero × con proyecto Acuario" y "Mejor |×| que × más σ" (combinar producto cartesiano + selección en join).

## Slide 28

"Optimización con árboles: ejemplo(4)". Transformación final (paso 3→4): los × se convierten en |×| (joins) combinando cada σ con su producto cartesiano correspondiente. Nota: "Mejor |×| que × más σ" y "Hay otras formas más...".

## Slide 29

"Reglas de transformación". Lista numerada de 6 reglas de equivalencia del álgebra relacional:
1. Descomponer σ_C si C tiene ANDs en varias σ en cascada: σ_c1 AND c2...AND cn(R) ≡ σ_c1(σ_c2(...(σ_cn(R)...)
2. Mover las σ_C lo más abajo posible (lo que admitan los atributos de C), ya que σ es conmutativa con otras operaciones.
3. Recolocar las hojas para que los σ más restrictivos se ejecuten antes (producen relación con menos tuplas). Válido para operadores conmutativos y asociativos: ×, |×|, ∪, ∩.
4. Combinar × y σ en |×|.
5. Por cada π_lista descomponer lista y mover los π_sublista lo más abajo posible. Crear nuevas π si es necesario.
6. Identificar grupos de operaciones ejecutables con un solo algoritmo (un solo recorrido a los ficheros).

## Slide 30

"Ejemplo" (ejercicio propuesto). Consulta SQL sobre Ingrediente, Art_Ingr, Artículo (nombre de artículo "Pizza Marinera" con ingrediente de precio > 1000). Se pide: "A partir de la siguiente consulta SQL el optimizador llega, en un paso intermedio, al árbol de consulta que figura a continuación. Obtén un árbol optimizado posible". Árbol intermedio mostrado:
```
π Artículo.NomArt
  σ Art_Ingr.NomArt = Artículo.NomArt
    ×
      σ Ingrediente.NomIngr=Art_Ingr.NomIngr    σ NomArt="Pizza Marinera"
        ×                                         Articulo
          σ Precio>1000    Art_Ingr
            Ingrediente
```
Flecha lateral indica "Orden de ejecución" ascendente.

## Slide 31

Preguntas de transición: "¿Es suficiente la transformación?" y en amarillo "¿Cuál es el costo del plan estimado?" — introduce el tema de optimización física/costos.

## Slide 32

"Recordar". Repite definición: "Plan: Árbol de operadores de álgebra relación con la elección de algoritmos por cada operador." Recuadro: "Entonces lo que faltaría para convertir un árbol en plan de ejecución: Algoritmos básicos por cada operador (hay uno o varios por cada operación del álgebra). Algunos algoritmos exigen una organización de datos determinada (por ejemplo que haya índice primario)."

## Slide 33

Slide de transición decorativa "OPTIMIZACIÓN FÍSICA" (texto pequeño, mascota ninja sentada en un trono con una pluma/lápiz gigante, ilustración fantástica). Mayormente espacio en blanco.

## Slide 34

Slide separador "4 Optimización Física". Fondo edificio UTEC azul (mismo estilo que slides 7, 13, 19).

## Slide 35

Slide de transición con solo el título "SISTEMA DE COSTOS" en la parte inferior izquierda; resto en blanco (decorativa).

## Slide 36

"Componentes del coste". Bullets con colores:
- Bloques transferidos (morado): depende de las estructuras de acceso y de la colocación de los bloques (contiguos, mismo cilindro, dispersos).
- Ficheros intermedios generados (verde).
- Cómputos en memoria sobre los ficheros intermedios (azul): búsqueda, ordenación, fusión, cálculos.
- Comunicación (rojo): envío de la consulta y recepción del resultado.
Recuadro verde: "Coste principal: BD grandes → bloques transferidos; BD pequeñas (entran en memoria) → cómputos; BD distribuidas → comunicación." Globo rojo: "Generalmente se usa este" (apuntando a bloques transferidos).

## Slide 37

"Memoria Principal vs. Memoria Secundaria". Comparación con imágenes: Disco duro (rojo, "Memoria Secundaria") con bullets "Datos guardados en memoria secundaria", "La lectura se hace por bloques", "Un bloque tiene un tamaño de B tuplas". Módulos RAM (verde, "Memoria Principal") con bullets "Los datos son llevados a memoria principal", "La memoria tiene una capacidad de M tuplas".

## Slide 38

"Sistema de Costos". Misma comparación visual que slide 37, con recuadro amarillo añadido en el centro: "Sistema de Costos: Cuenta los accesos a la memoria secundaria. Cada vez que se lee o escribe, se suma 1 al costo. Asume que las operaciones en memoria principal toman un tiempo despreciable."

## Slide 39

"Transferencia de bloques y tuplas a RAM". Diagrama: ícono de RAM conectado por una línea curva a un cilindro de disco duro que contiene cuadrados naranjas (tuplas) organizados en bloques. Etiqueta: "Capacidad: 1 Bloque = B tuplas".

## Slide 40

"Sistema de Costos" — fórmulas fundamentales, en recuadros pregunta/respuesta:
- "¿Cuánto cuesta leer n tuplas desde la memoria secundaria?" → ⌈n/B⌉
- "¿Cuántos bloques caben en memoria?" → ⌊M/B⌋
- "¿Cuántos bloques usa una relación R?" → ⌈|R|/B⌉
Recuadro superior azul recuerda: "Un bloque tiene un tamaño de B tuplas. La memoria tiene una capacidad de M tuplas."

## Slide 41

Slide de transición "BÚSQUEDA" (título abajo a la izquierda, decorativa).

## Slide 42

"Búsqueda". Definición: "Devolver todas las tuplas de una relación que satisfagan alguna condición". Tabla Planeta (misma que slide 6) con ejemplo SQL `SELECT * FROM Planeta WHERE nombre='Venus'` y resultado (fila de Venus resaltada en verde) mostrado abajo.

## Slide 43

"Búsqueda Secuencial". Bullets: "Se leen todas las tuplas de la relación R", "Se seleccionan las que cumplan la condición". Tabla Planeta repetida. Preguntas con respuestas:
- "¿Cuántas tuplas se leen?" → |R|
- "¿Cuánto cuesta en términos de bloques?" → ⌈|R|/B⌉
- "¿Cómo podemos optimizar la búsqueda?" (sin responder, abre siguiente tema: índices).

## Slide 44

Slide de transición "ÍNDICES", subtítulo "Capítulo 9.3 | Ramakrishnan / Gehrke" (decorativa, mayormente blanco).

## Slide 45

"Búsqueda de registro sin índice". Comparación entre archivo "Desordenado" (columna de números sin orden: 9,5,13,8,6,15,3,17,21,11,16,2 — costo O(n)) y archivo "Ordenado" (tabla con columnas Nombre, FNac, Salario, depart; nombres ordenados alfabéticamente: Aron/Aboot/Acosta/Alfred/Alvez/Arce/Avilez/Avaro/Azen — costo O(log₂n)).

## Slide 46

Diagrama tomado de libro de texto (Figura 18.1, Ramakrishnan/Elmasri): "Índice Primario". Muestra un archivo índice (Index file) con pares <block anchor primary key value, block pointer> a la izquierda (Aaron Ed, Adams John, Alexander Ed, Allen Troy, Anderson Zach, Arnold Mack) con flechas apuntando a bloques de datos ordenados a la derecha (tabla Name, Ssn, Birth_date, Job, Salary, Sex), cada bloque conteniendo varios registros ordenados alfabéticamente.

## Slide 47

Diagrama de libro de texto (Figura 18.2): "Índice Agrupado" (clustering index). Archivo índice con pares <clustering field value, block pointer> (valores 1,2,3,4,5,6,8) apuntando a bloques del Data file ordenados por Dept_number (campo no clave, se repite en varias tuplas por bloque).

## Slide 48

Diagrama de libro de texto (Figura 18.4): "Índice Secundario (unique)". Archivo índice denso con field value 1-24 y block pointers apuntando individualmente a cada registro disperso en los bloques de datos (campo secundario no ordena físicamente los datos, por eso las flechas cruzan mucho — patrón denso tipo maraña de líneas).

## Slide 49

Diagrama de libro de texto (Figura 18.5): "Índice Secundario (campo no clave)". Muestra un nivel adicional de indirección: Index file (field value 1,2,3,4,5,6,8) → "Blocks of record pointers" (bloques intermedios con múltiples punteros por cada valor repetido) → Data file (Dept_number no único, cada bloque de punteros agrupa todos los registros con ese valor).

## Slide 50

"Índice". Definición: "Estructura los datos para facilitar búsquedas". Fotografía de una página real de guía telefónica en papel ("Wood River Valley", listado alfabético con nombres y teléfonos) como analogía de índice físico.

## Slide 51

"Índice Hash". Diagrama de 4 columnas: Llaves (Saturno, Mercurio, Venus, Marte, Tierra, …) → Función Hash (caja naranja) → Cajones (bins numerados 000-255, algunos resaltados en verde: 001, 003, 127, 254) → Datos (registros de la tabla Planeta apuntados por los cajones verdes: Tierra, Mercurio, Marte, Saturno, Venus). Recuadro amarillo: "La llave puede ser cualquier conjunto de atributos de la tabla."

## Slide 52

"Ejemplo función hash". Fórmula h(K) = K mod m. Ejemplo con tabla de 8 ranuras (m=8): inserta 36,18,72,43,6 en orden. Cálculos: 36%8=4, 18%8=2, 72%8=0, 43%8=3, 6%8=6. Tabla resultante de 8 casillas [0]-[7]: [0]=72, [2]=18, [3]=43, [4]=36, [6]=6 (resto vacías).

## Slide 53

"Índice Hash" (continuación, mismo diagrama de slide 51 atenuado de fondo). Pregunta: "¿El costo de búsqueda con un índice hash?" Respuestas: Caso ideal: O(1) para devolver una tupla; Peor caso: O(⌈|R|/B⌉). Nota adicional: "Asumiremos una búsqueda que devuelva una sola tupla. Para devolver k tuplas, hay que 'sumar' ⌈k/B⌉ al costo." Caso ideal para k tuplas: O(max(1,⌈k/B⌉)).

## Slide 54

"Índice Hash" (continuación). Mismas fórmulas de costo. Nueva pregunta: "Pero ¿qué tipo de búsqueda?" Recuadro: "¡Hemos asumido que se sabe el valor exacto de la llave!" con ejemplo SQL `SELECT * FROM Planeta WHERE nombre='Venus'` (búsqueda exacta).

## Slide 55

"Índice Hash" (continuación). Nueva pregunta: "¿Qué pasa con las búsquedas por rango?" Ejemplo SQL `SELECT * FROM Planeta WHERE temp>100 AND temp<200`. Respuesta: Buscar n valores (ideal): O(n); Leer todo: O(⌈|R|/B⌉) — el hash no sirve bien para rangos.

## Slide 56

"Índice Árbol B". Tabla Planeta con columna "temp" resaltada (valores 440,730,288,186,152,134,76,53,44). Diagrama de árbol B de 3 niveles: raíz [186], nivel medio [53,134] y [440], hojas [44],[76],[152],[288],[730]. Definiciones: "Árbol B: Árbol ordenado, balanceado." "a–b Árbol B: Los nodos internos tienen entre a y b hijos (a≥⌈b/2⌉)." Pregunta: "¿Este caso? → 2–3 Árbol B".

## Slide 57

"Índice Árbol B+". Mismo árbol de 3 niveles pero ahora las hojas contienen pares (llave, nombre de planeta, ...) y están enlazadas entre sí (flechas horizontales): [44 Pluto...]→[53 Neptuno, 76 Urano...]→[134 Saturno, 152 Júpiter...]→[186 Marte, 288 Tierra...]→[440 Mercurio, 730 Venus...]. Definición: "Árbol B+: Árbol B donde se guardan las tuplas en las hojas del árbol. Las hojas guardan todas las llaves y sus valores. Se conectan las hojas para poder hacer búsquedas por rango más eficientes."

## Slide 58

"Índice Árbol B+" (continuación, mismo árbol atenuado de fondo). Pregunta: "¿El costo de búsqueda con un árbol B+?" Respuesta: "Depende…"

## Slide 59

"Índice Árbol B+" (continuación). Árbol B+ dentro de un rectángulo rojo con ícono de disco duro (representa que está en memoria secundaria). Pregunta: "¿El costo en términos de bloques leídos de memoria secundaria?" Respuesta: "Si se guarda cada nodo como un bloque en memoria secundaria: O(log_b(⌈|R|/B⌉)) para devolver una tupla" y para k tuplas: O(log_b(⌈|R|/B⌉) + ⌈k/B⌉).

## Slide 60

"Índice Árbol B+" (continuación). Mismo árbol pero la parte superior (raíz+internos) dentro de rectángulo verde con ícono de RAM (cacheados en memoria principal) y las hojas en rectángulo rosado con ícono de disco. Respuesta: "Si se cachean la raíz y los nodos internos en memoria principal: O(⌈k/B⌉), O(1) para devolver una tupla".

## Slide 61

"Índices: Hash vs. Árbol B+". Comparación visual lado a lado (diagrama hash de slide 51 vs árbol B+ de slide 57) con un gran "VS" decorativo de fondo. Textos: "Levemente más eficiente para búsquedas exactas asumiendo una función de hash ideal" (lado hash), recuadro amarillo "Árbol B+ es más popular", "Mucho más eficiente para búsquedas por rango" (lado árbol B+).

## Slide 62

"Crear Índices: SQL". Bullets: "Por defecto, se crea un índice para la llave primaria de la tabla." "Para crear/borrar índices sobre otros atributos:" con código SQL:
```sql
CREATE INDEX nombre ON tabla (atr1,atr2) -- btree por defecto
CREATE INDEX nombre ON tabla USING hash (atr1,atr2)
DROP INDEX nombre
```

## Slide 63

Slide de transición "JOINS" (título abajo a la izquierda, decorativa, mayormente blanco).

## Slide 64

"Reunir tablas: (EQUI) JOIN". Tablas Planeta y Aterrizaje (ver slide 6) mostradas de nuevo. Consulta SQL `SELECT nave, nombre, dist, año FROM Planeta, Aterrizaje WHERE nombre=planeta` con resultado esperado mostrado abajo (tabla con nave, nombre, dist, año para cada aterrizaje). Pregunta en recuadro punteado: "¿Cómo deberíamos ejecutar el join?"

## Slide 65

"Loop anidado (sin índices)" — primer frame de una animación. Pseudocódigo: "R ⋈ S: Para cada tupla r∈R: Para cada tupla s∈S: Si r y s satisfacen el join: escribir {r}×{s}". Dos arreglos de bloques R:[4,2,2,6,3,1,...] y S:[5,3,2,4,7,4,...] con flechas/punteros iniciales apuntando al primer elemento de cada uno (r=4, s=5). Resultado R⋈S vacío aún.

## Slide 66

"Loop anidado (sin índices)" — frame 2: puntero de S avanza a la posición 2 (s=3), puntero de R sigue en r=4. Sin coincidencia todavía.

## Slide 67

"Loop anidado (sin índices)" — frame 3: puntero de S avanza a posición 3 (s=2), r=4 sigue fijo. Sin coincidencia.

## Slide 68

"Loop anidado (sin índices)" — frame 4: puntero de S llega a posición 4 (s=4), coincide con r=4. Resultado parcial R⋈S muestra el primer par {4,4}.

## Slide 69

"Loop anidado (sin índices)" — frame 5: mismo estado, resultado {4,4} se mantiene mostrado (repetición de frame anterior, avance de animación).

## Slide 70

"Loop anidado (sin índices)" — frame 6: se agrega una segunda fila {4,4} al resultado R⋈S (duplicado, indicando otra coincidencia o repaso visual de la animación).

## Slide 71

"Loop anidado (sin índices)" — frame 7: puntero de S avanza a posición 6 (s=4, el último "4" visible antes de "..."), R⋈S sigue mostrando {4,4} repetido.

## Slide 72

"Loop anidado (sin índices)" — frame 8: puntero de R avanza a posición 2 (r=2), puntero de S reinicia a posición 1 (s=5). Resultado acumulado se mantiene {4,4}.

## Slide 73

"Loop anidado (sin índices)" — frame 9: puntero de S avanza a posición 2 (s=3), r=2 fijo. Sin nueva coincidencia.

## Slide 74

"Loop anidado (sin índices)" — frame 10: puntero de S en posición 3 (s=2), coincide con r=2. Resultado R⋈S ahora tiene 3 filas: {4,4},{4,4},{2,2}.

## Slide 75

"Loop anidado (sin índices)" — frame 11: puntero de S avanza a posición 4 (s=4), r=2 sigue fijo. Resultado sigue con 3 entradas ({4,4}x2, {2,2}) y aparece "…" indicando que el proceso continúa para el resto de las tuplas.

## Slide 76

"Loop anidado (sin índices)" — resumen de costos. Preguntas y respuestas:
- ¿Costo? → ⌈|R|/B⌉ + |R|·⌈|S|/B⌉
- ¿Memoria? → 2B tuplas
- ¿Elegir R y S? → |R|<|S| (para ahorrar tiempo)

## Slide 77

"Loop anidado (con índices)" — frame 1. Pseudocódigo actualizado: "Para cada tupla r∈R: Buscar s∈S en el índice tal que r y s satisfagan el join: escribir {r}×{s}". R:[6,3,4,2,3,1,...], S:[1,2,4,4,6,7,...] con una barra "ÍNDICE" debajo de S. r=6, puntero de búsqueda en S apunta a la posición del valor 4 (posición central, buscando por índice, no secuencial).

## Slide 78

"Loop anidado (con índices)" — frame 2: coincidencia encontrada r=6 con s=6 (vía índice). Resultado R⋈S: {6,6}.

## Slide 79

"Loop anidado (con índices)" — frame 3: mismo resultado {6,6} mostrado (frame de transición de animación).

## Slide 80

"Loop anidado (con índices)" — frame 4: mismo estado {6,6}, el puntero de búsqueda en S permanece en la posición del valor 4.

## Slide 81

"Loop anidado (con índices)" — frame 5: el puntero de búsqueda en S se mueve a la posición inicial (valor 1), preparándose para la siguiente búsqueda por índice. Resultado sigue {6,6}.

## Slide 82

"Loop anidado (con índices)" — frame 6: puntero avanza a posición del valor 2 en S. Resultado {6,6}.

## Slide 83

"Loop anidado (con índices)" — frame 7: puntero de R avanza a r=3, puntero de búsqueda en S en posición valor 4. Resultado sigue {6,6} (sin match aún para r=3, ya que S no tiene 3).

## Slide 84

"Loop anidado (con índices)" — frame 8: puntero de R avanza a r=4, encuentra coincidencia con s=4 vía índice. Resultado R⋈S ahora: {6,6},{4,4}.

## Slide 85

"Loop anidado (con índices)" — frame 9: mismo estado, {6,6},{4,4} (repetición de animación, puntero de búsqueda posicionado en el segundo "4" de S).

## Slide 86

"Loop anidado (con índices)" — frame 10: puntero de R avanza a r=2 (sin coincidencia en S, que no tiene valor 2 en este segmento mostrado). Resultado se mantiene {6,6},{4,4}. Aparece "…" indicando continuación del proceso.

## Slide 87

"Loop anidado (con índices)" — resumen de costos. B(S) = costo de buscar en S. Fórmula general: ⌈|R|/B⌉ + |R|·B(S). Casos:
- Peor caso: ⌈|R|/B⌉ + |R|·⌈|S|/B⌉
- Mejor caso (Árbol B+ en disco): ⌈|R|/B⌉ + |R|·O(log_b(⌈|S|/B⌉))
- Mejor caso (Hash/Árbol B+ en memoria principal): ⌈|R|/B⌉ + |R|·O(1)
Nota: "El 'mejor caso' aquí asume que, para cada tupla r, las tuplas s1,…,sk que sean compatibles con r estén en un número constante de bloques."

## Slide 88

"Loop anidado (con índices)" — continuación del resumen: se agregan ¿Memoria? → 2B tuplas y ¿Elegir R y S? → |R|<|S| (para ahorrar tiempo).

## Slide 89

"Hash-join" — frame 1. Pseudocódigo: "Guardar S en memoria principal. Para cada tupla r∈R: Buscar s en memoria principal tal que r y s satisfagan el join: escribir {r}×{s}". R:[6,3,4,2,3,1,...], S completo cargado en un recuadro "MEM. P." (memoria principal): [1,2,4,4,6,7,...]. r=6 apunta a s=6 en la tabla hash en memoria.

## Slide 90

"Hash-join" — frame 2: coincidencia r=6 con s=6. Resultado R⋈S: {6,6}.

## Slide 91

"Hash-join" — frame 3: puntero de R avanza a r=3 (sin match en S). Resultado se mantiene {6,6}.

## Slide 92

"Hash-join" — frame 4: puntero de R avanza a r=4, coincide con s=4 en memoria. Resultado R⋈S: {6,6},{4,4}.

## Slide 93

"Hash-join" — frame 5: mismo estado {6,6},{4,4},{4,4} (dos coincidencias con el 4 repetido en S), aparece "…" indicando continuación.

## Slide 94

"Hash-join" — resumen de costos. ¿Costo? → ⌈|R|/B⌉+⌈|S|/B⌉. ¿Memoria? → |S|+B tuplas. ¿Elegir R y S? → |S|<|R| (para ahorrar memoria, S es la que se carga completa en RAM).

## Slide 95

"Sort-merge-join" — frame 1. Pseudocódigo: "Ordenar R y S por los atributos del join. Aplicar un merge-sort y para cada tupla r y s que satisfagan el join: escribir {r}×{s}". R:[6,3,4,2,3,1,...] etiquetado "ORDENAR", S:[6,2,4,7,6,1,...] etiquetado "ORDENAR" (antes de ordenar).

## Slide 96

"Sort-merge-join" — frame 2: R y S ya ordenados: R:[1,2,3,3,4,6,...], S:[1,2,4,6,6,7,...]. Punteros al inicio de ambos (r=1, s=1), coincidencia encontrada. Resultado R⋈S: {1,1}.

## Slide 97

"Sort-merge-join" — frame 3: mismo estado {1,1} (repetición de animación).

## Slide 98

"Sort-merge-join" — frame 4: ambos punteros avanzan a la posición 2 (r=2, s=2), coincidencia. Resultado R⋈S: {1,1},{2,2}.

## Slide 99

"Sort-merge-join" — frame 5: mismo estado {1,1},{2,2} (transición de animación).

## Slide 100

"Sort-merge-join" — frame 6: puntero de R avanza a posición 3 (r=3), puntero de S se mantiene en posición 2 (s=2, sin match ya que S no tiene 3 aún visible). Resultado sigue {1,1},{2,2}.

## Slide 101

"Sort-merge-join" — frame 7: puntero de R en posición 4 (r=3, segundo 3), S sigue en posición 2. Resultado se mantiene {1,1},{2,2}.

## Slide 102

"Sort-merge-join" — frame 8: puntero de R avanza a posición 5 (r=4), puntero de S avanza a posición 3 (s=4), coincidencia. Resultado R⋈S: {1,1},{2,2},{4,4}.

## Slide 103

"Sort-merge-join" — frame 9: mismo estado {1,1},{2,2},{4,4}, aparece "…" indicando que el proceso continúa.

## Slide 104

"Sort-merge-join" — resumen de costos. O = costo de ordenamiento. ¿Costo? → O + ⌈|R|/B⌉+⌈|S|/B⌉. ¿Memoria? → 2B tuplas (una vez que estén ordenadas). ¿Elegir R y S? → No importa. Nota verde: "Puede ser que las relaciones ya estén ordenadas por los atributos del join, en cual caso ¡es una buena opción!"

## Slide 105

"Joins: Comparación". Recuadro con las 4 opciones: 1. Loop anidado (sin índice), 2. Loop anidado (con índice), 3. Hash-join, 4. Sort-merge-join. Recomendaciones:
- Loop anidado (sin índice): Nunca es bueno (rojo).
- Loop anidado (con índice): Cuando el índice está disponible y pocas tuplas en S satisfacen el join (verde).
- Hash-join: Cuando R cabe en memoria y muchas tuplas en S satisfacen el join (verde).
- Sort-merge-join: Cuando R y S ya están ordenados por los atributos del join y muchas tuplas en ambos satisfacen el join (verde).

## Slide 106

"Lo que vimos hoy". Repite mensaje de SQL declarativo con bullets. Nota: "Video Sugerido: https://www.youtube.com/watch?v=1HH4ZYXhJYE". Meme del perro decorativo de fondo atenuado.

## Slide 107

Slide separador "5 Optimización semántica". Fondo edificio UTEC azul (mismo estilo de secciones anteriores).

## Slide 108

"OBJETIVO: SIMPLIFICAR LA PREGUNTA INICIAL". Ejemplo: consulta SQL `SELECT E.APELLIDO FROM EMPLEADO AS E INNER JOIN EMPLEADO AS S ON E.NSS_SUPERV=S.NSS WHERE E.SALARIO>S.SALARIO` (empleados que ganan más que su supervisor). Recuadro azul: "Supongamos que existe la siguiente restricción de integridad semántica: 'ningún empleado puede ganar más que su supervisor directo'". Nota roja: "No hace falta procesar la consulta anterior ya que no devolverá ninguna tupla" — ejemplo de optimización semántica usando restricciones de integridad para evitar ejecutar consultas que no producirán resultados.

## Slide 109

"Resumen" final del capítulo. Bullets:
- Es importante considerar que la memoria es Limitada y por ello debemos escribir consultas optimizadas.
- El uso reglas heurísticas para la optimización sintáctica es crucial.
- Hace uso de los índices sea HASH, BTree es importante para grandes volúmenes de datos.
- El uso de los algoritmos de optimización depende del tipo de índice y sobre el atributo que se le aplicó.

## Slide 110

Slide "GRACIAS" de cierre. Subtítulo "TEÓFILO CHAMBILLA". Fondo fotográfico decorativo de estudiantes en laboratorio, teñido azul. Logo UTEC y frase "Reinventa el mundo" decorativos.

## Slide 111

Repetición del diagrama de "SQL es un lenguaje declarativo" (idéntico a slide 15: bullets sobre plan de ejecución óptimo y el usuario no preocupándose de la optimización, con el meme del perro "NO TENGO IDEA / DE LO QUE ESTOY HACIENDO" y el link al video sugerido https://www.youtube.com/watch?v=1HH4ZYXhJYE). Nota: aparece como slide duplicada/de repaso al final del set, no como cierre nuevo de contenido.
