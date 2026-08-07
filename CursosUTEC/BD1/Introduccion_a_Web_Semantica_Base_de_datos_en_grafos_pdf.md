---
curso: BD1
titulo: Introducción a Web Semantica "Base de datos en grafos"
slides: 165
fuente: Introducción a Web Semantica "Base de datos en grafos".pdf
---

## Slide 1
Portada del capítulo. Título "Introducción a Web Semántica 'Base de datos de grafos'", curso CS2041 Bases de Datos I, Ciclo 2023-2. Nombres de los profesores Teófilo Chambilla y Brenner Ojeda con sus correos institucionales (decorativa, chrome de curso).

## Slide 2
Diagrama de ubicación del tema dentro del curso: una línea de tiempo/mapa conceptual con los bloques "Introducción", "Modelo Relacional", "Álgebra Relacional & Cálculo Relacional", "SQL", "Formas Normales", "Planificación y Optimización de Consultas", "Transacciones y ACID", y a la derecha, resaltado, "NO SQL/GRAFOS" (el tema de este capítulo dentro de la malla del curso).

## Slide 3
"Agenda" del capítulo, lista con viñetas: Motivación; La web clásica; Nociones básicas y el modelo de datos RDF; La Web semántica; Nociones de URI; Nociones de Literal y Triple RDF; Grafo RDF; SPARQL; WikiData; Linked Data.

## Slide 4
Sección "MOTIVACIÓN". Ejemplo de consulta compleja: "Jugadores de fútbol que nacen en un país con más de 10 millones de habitantes, que jugaron como portero de un club que tiene un estadio con más de 30,000 asientos y el país del club es diferente al país de nacimiento."

## Slide 5
"Otro Ejemplo": "Muestre la lista de personajes educados en Universidades Peruanas. Se desea conocer el nombre de la persona y el de la universidad." Incluye referencia a https://query.wikidata.org/ como la herramienta que resuelve este tipo de consultas.

## Slide 6
Contraste conceptual (texto, sin tabla): "La web clásica es una red de documentos, interpretable por humanos, donde las relaciones entre documentos no tienen un significado" vs "La web de datos es una red de afirmaciones, interpretable por humanos y máquinas, donde las afirmaciones se relacionan y tienen un significado." Atribuido a Tim Berners-Lee (foto/nombre al pie).

## Slide 7
Encabezado de sección: "NOCIONES BÁSICAS Y EL MODELO DE DATOS RDF".

## Slide 8
"¡La Web es magnífica! ¿Pero puede ser mejor? … a veces es difícil encontrar información relevante." Slide de transición/pregunta retórica.

## Slide 9
"¡Pero Google es magnífico! Se pueden encontrar respuestas directas."

## Slide 10
Escenario: "Haciendo una tarea para su clase… Quiere encontrar cada: Ganadores del Premio Nobel en Literatura que han luchado en una guerra, el año que ganaron el premio, y el año que comenzó la guerra. ¿Cómo se puede encontrar esta información con la Web actual?"

## Slide 11
"Muchas pestañas de Wikipedia …" — probablemente una captura mostrando múltiples pestañas del navegador abiertas en artículos de Wikipedia, ilustrando lo tedioso de buscar manualmente.

## Slide 12
"La Web actual": definición — "La Web actual es un conjunto de documentos, en general páginas web escritas en HTML."

## Slide 13
"La Web actual": estas páginas HTML están formadas por Contenido y Enlaces. Diagrama de dos cajas: "Contenido" (texto, imágenes, videos, audios, etc.) y "Enlaces" (nos redirigen a otro documento/otra página web).

## Slide 14
"Un ejemplo de la Web actual" — captura de pantalla de una página web típica (sin texto adicional en la extracción, se asume screenshot ilustrativo de una web con contenido y enlaces).

## Slide 15
"Enlaces en una página Web" — captura de pantalla mostrando/resaltando los hipervínculos dentro de una página.

## Slide 16
"Desafíos de la Web Actual" — tabla/lista de 4 desafíos con su explicación:

| Desafío | Descripción |
|---|---|
| Heterogénea | Múltiples organizaciones generan datos, de forma independiente. |
| Masiva | La cantidad de información existente es enorme. |
| Cambia muy rápido | Cada día son publicados y borrados enormes volúmenes de información. |
| Hecha para humano | En general, sólo una persona puede interpretar la información de una página Web. |

## Slide 17
"La Web actual es heterogénea" — imagen ilustrativa (logos/íconos de múltiples organizaciones generando datos independientes).

## Slide 18
"La Web actual es masiva" — build 1: cifra destacada "= 5.9 TB de datos (aprox)".

## Slide 19
"La Web actual es masiva" — build 2: cifra destacada "= 235 TB de datos = 40 Wikipedias" con nota "(Biblioteca del Congreso de EEUU incluye Web Archive)".

## Slide 20
"La Web actual es muy rápida" — cifra destacada "= 160 TB/s transferidos = 27 Wikipedias/segundo" (fuente: Cisco).

## Slide 21
"La Web actual está hecha para humanos" — pregunta: "¿Cómo puede un computador entender esta Web?"

## Slide 22
Repite título "La Web actual está hecha para humanos" — pregunta: "¿Leyendo el texto disponible? ¿Cómo sabe una aplicación computacional qué texto leer?"

## Slide 23
Repite título "La Web actual está hecha para humanos" — pregunta: "¿Mirando el código HTML? ¿Es posible identificar el nombre de una persona en el código HTML?" (probablemente con una captura de código HTML de ejemplo).

## Slide 24
"¿Cómo podemos aprovechar estos datos?" — build 1: "Los Computadores tienen la capacidad para poder analizar estos datos."

## Slide 25
Repite título — build 2: "Pero actualmente no son capaces de interpretarlos correctamente... (Las páginas que mostramos están pensadas para personas)."

## Slide 26
Repite título — build 3: "Hay que permitir que las aplicaciones computacionales entiendan los datos… ¿Cómo hacemos esto?"

## Slide 27
"Requisitos para una Web de datos efectiva" — build 1: "Primero, es necesario tener un lenguaje que permita especificar recursos en la Web y las relaciones entre ellos." Nota destacada: "Un requisito fundamental: este lenguaje debe ser procesable por un computador."

## Slide 28
Repite título — build 2: "Segundo, necesitamos poder consultar estos datos mediante aplicaciones computacionales." Dos requisitos fundamentales en lista: lenguaje de consulta procesable por computador; capacidad de sacar conclusiones de los datos de manera automática.

## Slide 29
Encabezado de sección: "La Web de Datos / La Web Semántica".

## Slide 30
"La Web Semántica" — cita textual: "La Web Semántica es una extensión de la Web actual en la cual se da un significado bien definido a la información, permitiendo mejorar la colaboración entre personas y computadores en la Web." — Tim Berners-Lee 2001.

## Slide 31
"La Web Semántica en la práctica" — "Es un conjunto de recomendaciones desarrolladas por el World Wide Web Consortium, cuyo objetivo es que los computadores sean capaces de entender los datos en la Web." Nota: una recomendación es una descripción formal de una tecnología usada por todos (lenguaje común); el W3C es el organismo regulador de la Web.

## Slide 32
"Los estándares para Web Semántica" — probablemente diagrama tipo "pila/pastel de capas" de los estándares W3C (RDF, RDFS, OWL, SPARQL, etc.), sin texto adicional extraído (mayormente visual).

## Slide 33
Encabezado de sección: "LA NOCIÓN DE URI".

## Slide 34
"¿Qué es la Web Semántica?" — repite la misma cita de Tim Berners-Lee 2001 vista antes, como recordatorio antes de introducir URI.

## Slide 35
"¿Cómo realizar la Web Semántica?" — diagrama de flujo: icono "</>" con la etiqueta "Construir Lenguaje" → "Requisito: Debe ser lenguaje procesable por un computador" → "que permita especificar Recursos en la Web y Relaciones entre recurso Web" → "Propuesta actual: Lenguaje RDF".

## Slide 36
"Características básicas de RDF" — "RDF es la propuesta del World Wide Web Consortium (W3C) para representar información sobre recursos en la Web." Diagrama de 3 columnas numeradas: (1) RDF está basada en el uso de grafos dirigidos y etiquetados; (2) Una especificación RDF puede ser procesada por un computador; (3) Las piezas básicas para construir una especificación RDF son los URIs y los literales. Al pie, leyenda "Figura: Ejemplo de un grafo" (imagen de un grafo de ejemplo, no descrita en el texto plano).

## Slide 37
"URI (Uniform Resource Identifier)" — "Un URI es un identificador de un recurso en la WEB." Diagrama tipo esquema con cajas "URI", "Identificador", "Recurso", "Web" interconectadas, y a la derecha lista de ejemplos de "Recurso": una página Web, una persona, un libro, una ciudad, un gen, una película.

## Slide 38
"Ejemplo y componentes de un URI" — desglose anotado del URI `http://dbpedia.org/resource/Lionel_Messi`: "http" = protocolo de acceso al recurso; "dbpedia.org" = autoridad del URI (similar al nombre de dominio); "resource/Lionel_Messi" = camino, la parte principal del URI.

## Slide 39
"Idea: Usar los identificadores de la Web" — comparación URL vs URI en lista:
- URL: Uniform Resource Location — la ubicación de un recurso de la Web (p.ej. una página Web) — ejemplo `http://ex.org/Dublín.html`
- URI: Uniform Resource Identifier (RDF 1.0) — un identificador de un recurso general (p.ej. una ciudad) — ejemplo `http://ex.org/Dublín`

## Slide 40
"Algunos ejemplos de URIs" — dos ejemplos destacados: `http://dbpedia.org/resource/Lionel_Messi` y `https://www.pcm.gob.pe`.

## Slide 41
"Usaremos URIs con prefijos" — mención de "Prefijos comunes" (probablemente una tabla de prefijos estándar como rdf:, rdfs:, xsd:, owl:, no capturada en el texto plano).

## Slide 42
Encabezado de sección: "LAS NOCIONES DE LITERAL Y TRIPLE RDF".

## Slide 43
"Una segunda pieza básica de RDF: Los literales" — "Un literal representa un valor concreto en una especificación RDF." Ejemplo: "Messi nació en la fecha '1987-06-24'".

## Slide 44
Repite título — "Un literal es simplemente una cadena de caracteres." Lista de ejemplos: "1987-06-24", "Lionel Messi", "157.38", "18:25:00".

## Slide 45
Repite título — "Un literal puede tener un tipo asociado." Ejemplos tipados: Fecha `"1987-06-24"^^xsd:date`; Número Real `"157.38"^^xsd:float`; Hora `"18:25:00"^^xsd:time`.

## Slide 46
"Un tiple en RDF" — explica que una relación entre dos recursos se da mediante un triple. Diagrama con tres cajas "Sujeto — Predicado — Objeto": Sujeto es un recurso identificado por un URI; Predicado está dado por un URI que representa una relación entre recursos (si el objeto es un recurso) o un atributo (si el objeto es un valor); Objeto es un recurso identificado por un URI o un valor dado por un literal.

## Slide 47
"Abreviación de URis" — ejemplo de prefijo: `@prefix dbpedia: http://dbpedia.org/resource` de modo que `dbpedia:Lionel_Messi` es abreviación de `http://dbpedia.org/resource/Lionel_Messi`.

## Slide 48
"Un primer ejemplo de tiple" — diagrama de triple: `dbpedia:Lionel_Messi` —(predicado `birthPlace`)→ `dbpedia:Argentina`. Texto: "indica que Messi nació en Argentina", relación entre ambos recursos.

## Slide 49
"Un segundo ejemplo de triple" — diagrama de triple: `dbpedia:Lionel_Messi` —(predicado `currentclub`)→ `dbpedia:FC_Barcelona`. "Indica que Messi juega en Barcelona".

## Slide 50
"Un tercer ejemplo de triple" — diagrama de triple: `dbpedia:Lionel_Messi` —(predicado `example:birthday`)→ literal `"1987-06-24"`. "Indica que Messi nació el 24 junio de 1987"; el valor del atributo `example:birthday` para el recurso es ese literal.

## Slide 51
Encabezado de sección: "EL CONCEPTO DE GRAFO RDF".

## Slide 52
"Un Grafo RDF" — "Un grafo RDF está formado por un conjunto de triples RDF."

## Slide 53
"Un primer ejemplo de triple" — grafo con un solo nodo-arco: `dbpedia:Lionel_Messi` —(`dbpprop:birthPlace`)→ `dbpedia:Rosario`. Nota: "Un grafo puede tener solo un triple".

## Slide 54
"Un segundo ejemplo de triple" — build 1: se agrega el triple `dbpedia:Lionel_Messi` —(`dbpprop:residence`)→ `dbpedia:Barcelona`, mostrando el grafo con 2 triples ("Messi vive en Barcelona").

## Slide 55
Repite título — build 2: se amplía el grafo agregando `dbpedia:Rosario` —(`dbpprop:isPartOf`)→ `dbpedia:Santa_Fe_Province`.

## Slide 56
Repite título — build 3 (grafo completo, 4 triples): se agrega además `dbpedia:Barcelona` —(`dbpprop:isPartOf`)→ `dbpedia:Province_of_Barcelona`. Diagrama final con 6 nodos y 4 aristas etiquetadas.

## Slide 57
"Un grado RDF en la Web" (grafo RDF en la Web) — resumen de las 4 afirmaciones construidas: Messi nació en Rosario; Messi vive en Barcelona; Rosario es parte de la Provincia de Santa Fe; Barcelona es parte de la Provincia de Barcelona. Pregunta: "¿Cómo se almacena este grafo en la Web?"

## Slide 58
"Un grado RDF como archivo" — "Un grafo RDF es almacenado como una secuencia de triples". Bloque de código con la serialización de los 4 triples:
```
dbpedia:Lionel_Messi dbpprop:birthPlace      dbpedia:Rosario.
dbpedia:Lionel_Messi dbpedia-owl:residence   dbpedia:Barcelona.
dbpedia:Rosario      dbpedia-owl:isPartOf    dbpedia:Santa_Fe_Province.
dbpedia:Barcelona    dbpedia-owl:isPartOf    dbpedia:Province_of_Barcelona.
```

## Slide 59
"Uso de prefijos en un grafo RDF" — declaración de los prefijos usados en el grafo anterior:
```
@prefix dbpedia: <http://dbpedia.org/resource>.
@prefix dbpprop: <http://dbpedia.org/property>.
@prefix dbpedia-owl: <http://dbpedia.org.ontology>.
```

## Slide 60
"Un grafo RDF complejo" — archivo completo combinando prefijos y los 4 triples en un solo bloque de código (mismo contenido que slides 58-59 unificado):
```
@prefix dbpedia: <http://dbpedia.org/resource>.
@prefix dbpprop: <http://dbpedia.org/property>.
@prefix dbpedia-owl: <http://dbpedia.org.ontology>.

dbpedia:Lionel_Messi dbpprop:birthPlace      dbpedia:Rosario .
dbpedia:Lionel_Messi dbpedia-owl:residence   dbpedia:Barcelona .
dbpedia:Rosario      dbpedia-owl:isPartOf    dbpedia:Santa_Fe_Province .
dbpedia:Barcelona    dbpedia-owl:isPartOf    dbpedia:Province_of_Barcelona.
```

## Slide 61
"Entonces: Los triples representan un grafo" — slide de cierre/transición conceptual antes de introducir SPARQL (probablemente con una imagen resumen del grafo construido).

## Slide 62
Encabezado: "Protocolo y Lenguaje de Consulta de RDF: SPARQL: SPARQL PROTOCOL AND RDF QUERY LANGUAGE".

## Slide 63
"SPARQL: Consultar Grafos en RDF" — consulta de ejemplo: "¿Quién protagoniza en la película 'Sharknado'?" (probablemente con un grafo/diagrama ilustrando la pregunta sobre datos de películas y actores).

## Slide 64
Repite título — muestra "Consulta:" junto a "Soluciones:", es decir una captura con la sintaxis SPARQL de la consulta y una tabla de resultados devueltos.

## Slide 65
"SPARQL Prefijos: Abreviaturas de IRIs" — captura de código mostrando declaraciones `PREFIX` típicas de una consulta SPARQL.

## Slide 66
"SPARQL: cláusula de WHERE" — "Donde se produce la magia. Especifica un grafo de consulta." Se introduce el concepto de "Patrón triple" (un triple con variables), con una captura resaltando la cláusula WHERE de una consulta.

## Slide 67
Repite título "SPARQL: cláusula de WHERE" — continúa la explicación del patrón triple con variables (build/captura adicional, sin texto nuevo relevante).

## Slide 68
Repite título — consulta de ejemplo: "¿En cuáles (otras) películas han actuado los actores de Sharknado?" (captura de la consulta SPARQL correspondiente).

## Slide 69
Repite título — continúa mostrando la resolución de la consulta anterior (build adicional de la misma captura).

## Slide 70
Repite título — introduce el concepto de "Basic Graph Pattern" (un conjunto de patrones triples), con captura ilustrando varios patrones triple combinados en la cláusula WHERE.

## Slide 71
"SPARQL: Joins" — concepto de "Variable de Join" (una variable que aparece en múltiples lugares de la consulta, generando el join implícito), con captura de ejemplo.

## Slide 72
"SPARQL: Unión" — consulta de ejemplo: "¿Cuáles son los títulos de las dos primeras películas en la serie Sharknado?" usando la palabra clave UNION.

## Slide 73
Repite título "SPARQL: Unión" — build/captura adicional mostrando la sintaxis UNION y sus resultados.

## Slide 74
"SPARQL: Left-join (OPTIONAL)" — consulta de ejemplo: "¿Los títulos de películas y (cuando sea disponible) sus fechas de estreno?" usando OPTIONAL.

## Slide 75
Repite título — introduce el concepto de "Variable UNBOUND" (una variable sin una solución, resultado del left-join cuando no hay coincidencia).

## Slide 76
"SPARQL: Filtros" — consulta de ejemplo: "¿Cuáles películas estrenaron en 2014?" usando FILTER.

## Slide 77
Repite título "SPARQL: Filtros" — muestra "Resultados vacíos" como resultado de aplicar un filtro que no coincide con datos.

## Slide 78
Repite título "SPARQL: Filtros" — muestra "Una abreviatura" de sintaxis de filtro.

## Slide 79
"SPARQL: cláusula de WHERE (otro ejemplo)" — nuevo ejemplo de patrón WHERE (build 1, sin texto adicional relevante en la extracción).

## Slide 80
Repite título — se explica que el patrón funciona "Como NOT EXISTS/EXCEPT!" (filtro de negación).

## Slide 81
"SPARQL: SELECT con *" — ejemplo de proyección total de variables con `SELECT *`.

## Slide 82
"SPARQL: SELECT con proyección" — ejemplo de proyección de columnas específicas; nota: "Devuelve duplicados".

## Slide 83
"SPARQL: SELECT con DISTINCT" — mismo ejemplo con `DISTINCT`; nota: "(no hay duplicados)".

## Slide 84
"SPARQL: ASK" — explica que la consulta ASK devuelve "true si hay al menos un resultado, false si no."

## Slide 85
"SPARQL: CONSTRUCT" — explica que CONSTRUCT "Devuelve un grafo de RDF" en lugar de una tabla.

## Slide 86
"Modificadores: ORDER BY, LIMIT, OFFSET" — consulta de ejemplo: "La segunda película y la tercera película más recientes" usando estos modificadores combinados.

## Slide 87
Encabezado de sección: "GOOGLE'S KNOWLEDGE GRAPH".

## Slide 88
"Google: 'Info-box'" — captura de un resultado de búsqueda de Google mostrando el panel/infobox lateral con datos estructurados.

## Slide 89
"Google: Búsqueda Semántica" — "Datos estructurados como grafos…" (imagen ilustrativa de resultados enriquecidos por el Knowledge Graph).

## Slide 90
Encabezado de sección: "FACEBOOK: OPEN GRAPH PROTOCOL".

## Slide 91
"Mientras tanto en Facebook…" — "Facebook quiere saber alguna información de los documentos con enlaces en los comentarios."

## Slide 92
"Mientras tanto en la Web…" — "Facebook quiere saber alguna información sobre las cosas que uno puede 'Like' en la Web externa."

## Slide 93
"Facebook Open Graph Protocol" — probablemente captura de meta-tags Open Graph (`og:title`, `og:image`, etc.) en el código HTML de una página, no capturada en texto plano.

## Slide 94
Encabezado de sección: "LA WIKIPEDIA DE DATOS: WIKIDATA".

## Slide 95
"¿Qué es Wikidata?" — slide introductoria (contenido visual, poco texto extraído).

## Slide 96
"Wikipedia: Varios Idiomas" — ejemplo/captura mostrando cómo el mismo artículo se mantiene por separado en distintos idiomas de Wikipedia.

## Slide 97
"Wikipedia: Listas, etc." — ejemplo/captura de listas mantenidas manualmente en Wikipedia.

## Slide 98
"Farfán marcó un gol…" — ejemplo del problema de actualización manual: "Ahora un ejército de personas tienen que actualizar Wikipedia (texto, listas, idiomas, etc.)".

## Slide 99
"Una solución: Wikidata" — presenta Wikidata como la solución centralizada de datos estructurados.

## Slide 100
"Wikidata: datos estructurados" — captura de la interfaz de Wikidata mostrando propiedades y valores estructurados de un ítem.

## Slide 101
"Servicio de consulta (SPARQL):" — build 1, captura del Query Service de Wikidata (query.wikidata.org).

## Slide 102
Repite título "Servicio de consulta (SPARQL):" — build 2 (marcada como "Hidden slide" en el material original), muestra la consulta SPARQL completa contra Wikidata para encontrar ganadores del Nobel de Literatura que participaron en guerras:
```sparql
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?laureateName ?awardYear ?warName ?warYear
WHERE {
  ?laureate p:P166 ?award .              # Winner of some prize
  ?award ps:P166 wd:Q37922 .             # Prize is Nobel Pr. in Lit.
  ?award pq:P585 ?awardDate .            # Get the date of the award
  BIND(YEAR(?awardDate) as ?awardYear)   # Get the year of the award
  ?laureate wdt:P607 ?war .              # Find war(s) laureate was in
  ?war rdfs:label ?warName .             # Get name(s) of war(s)
  ?war wdt:P580 ?warStart .              # Get year the war started
  BIND(YEAR(?warStart) as ?warYear)
  ?laureate rdfs:label ?laureateName .   # Get name of laureate
  FILTER(lang(?warName)="en"
   && lang(?laureateName)="en")
} ORDER BY ?awardYear
```
Referencia: https://query.wikidata.org/

## Slide 103
Encabezado de sección: "LINKED (OPEN) DATA".

## Slide 104
"Esto también pasa con los datos abiertos y sus metadatos" — "No alcanza con publicarlos en formatos abiertos para poder relacionarlos y que su significado sea procesable por máquinas. Necesitamos algo más..."

## Slide 105
"Linked Data + Open Data = Linked Open Data" — introduce el esquema visual de estrellas (icono de estrellas apiladas ★ hasta ★★★★★).

## Slide 106
"5★ Datos Abiertos" — "Tim Berners-Lee, el inventor de la Web e iniciador de los Datos Enlazados (Linked Data), sugirió un esquema de desarrollo de 5 estrellas para Datos Abiertos." Anuncia que a continuación se verán ejemplos, costos y beneficios de cada nivel.

## Slide 107
"Las 5 ★'s de Linked Open Data" — lista progresiva con nivel de estrellas y su requisito:

| Estrellas | Requisito |
|---|---|
| ★ | Publicar datos bajo licencia abierta |
| ★★ | Hacer los datos "legibles a máquina" (ej. hoja de cálculo mejor que tabla PDF) |
| ★★★ | Utilizar formatos no propietarios (ej. CSV mejor que Excel) |
| ★★★★ | Usar URIs para nombrar los objetos (sugerencia: RDF); identificadores inequívocos vinculables |
| ★★★★★ | Proporcionar enlaces a otro contenido (sugerencia: Linked Data), para que los consumidores sigan enlaces |

Nota final: "Cada estrella mejora la interoperabilidad de los datos."

## Slide 108
"ESQUEMA 5★ DATOS ABIERTOS" — diagrama visual (pirámide o escalera) resumiendo el mismo esquema de estrellas de la slide anterior con las mismas explicaciones distribuidas gráficamente. Fuente citada: http://5stardata.info/en/

## Slide 109
"¿Qué necesitamos para lograr las 5?" — lista de 3 tecnologías necesarias: RDF (modelo de datos basado en triplas que permite representar relaciones); SPARQL (lenguaje de consultas sobre RDF); RDF-S y OWL (para representar metadatos y darles significado — ontologías).

## Slide 110
"Ontología de Escuela Profesionales de Computación" — probablemente un diagrama de ejemplo de ontología (jerarquía de clases/relaciones), sin texto adicional capturado.

## Slide 111
Encabezado de sección: "Linked Open DATASETS".

## Slide 112
"Crecimiento de LINKED DATA CLOUD" — build 1 del diagrama de burbujas (LOD cloud): un único conjunto de datos visible, con la fecha "Oct. 2007" resaltada en la línea de tiempo lateral.

## Slide 113
Repite título — build 2: se agregan más burbujas al diagrama, línea de tiempo hasta "Nov. 2007".

## Slide 114
Repite título — build 3: más datasets conectados, línea de tiempo hasta "Feb. 2008".

## Slide 115
Repite título — build 4: línea de tiempo hasta "Sep. 2008".

## Slide 116
Repite título — build 5: línea de tiempo hasta "Mar. 2009" (resaltada en rojo). Diagrama de burbujas grande y denso conectando datasets como DBpedia, GeoNames, MusicBrainz, PubMed, etc. (visto directamente en la imagen de la slide 121 original — corresponde a este punto de la serie).

## Slide 117
Repite título — línea de tiempo hasta "Jul. 2009", diagrama con más nodos añadidos (BBC Music, Linked GeoData, National Science Foundation, CORDIS, etc.).

## Slide 118
Repite título — línea de tiempo hasta "Sep. 2010", diagrama considerablemente más denso (cientos de burbujas pequeñas conectadas, DBpedia como nodo central).

## Slide 119
Repite título — línea de tiempo hasta "Sep. 2011", diagrama aún más denso con un segundo clúster grande a la derecha (bioinformática/genómica).

## Slide 120
Repite título — línea de tiempo hasta "Sep. 2012", diagrama con más nodos añadidos respecto al anterior.

## Slide 121
Repite título "Crecimiento de LINKED DATA CLOUD" — línea de tiempo lateral con 5 fechas (Oct. 2007, Nov. 2007, Feb. 2008, Sep. 2008, Mar. 2009 resaltada en rojo). Diagrama circular grande de burbujas ("LOD cloud") con decenas de datasets etiquetados (DBpedia, GeoNames, MusicBrainz, FOAF profiles, DBLP, PubMed, UniProt, GeneID, ChEBI, etc.) conectados por flechas que representan enlaces entre conjuntos de datos.

## Slide 122
Repite título — línea de tiempo con 6 fechas (agrega "Jul. 2009" resaltada en rojo). Mismo diagrama de burbujas, ahora con más nodos (BBC Music, Linked GeoData, National Science Foundation, CORDIS, ReSIST Project wiki, etc.).

## Slide 123
Repite título — línea de tiempo con 7 fechas ("Sep. 2010" resaltada). Diagrama considerablemente más denso, con cientos de burbujas pequeñas alrededor de un núcleo central (DBpedia).

## Slide 124
Repite título — línea de tiempo con 8 fechas ("Sep. 2011" resaltada). Diagrama aún más denso, con un segundo gran clúster a la derecha (datasets de ciencias de la vida/genómica).

## Slide 125
Repite título — línea de tiempo con 9 fechas ("Sep. 2012" resaltada). Diagrama con más nodos añadidos.

## Slide 126
Repite título — línea de tiempo con 10 fechas ("Sep. 2013" resaltada). Diagrama de burbujas aún más poblado.

## Slide 127
Repite título — línea de tiempo con 11 fechas ("Ago. 2014" resaltada en verde, estilo de caja invertido —fondo azul oscuro—). Versión final del diagrama de burbujas en un estilo de renderizado distinto (líneas azules finas sobre fondo blanco), con DBpedia y "Central Names" como nodos centrales.

## Slide 128
"Linked Open Data hasta 2018-08-22" — diagrama circular de burbujas coloreadas por dominio temático, con leyenda lateral: Publicaciones (crema), Redes Sociales (gris), Generado por el usuario (magenta), Dominio cruzado (marrón), Geografía (celeste), Gobierno (naranja), Ciencias de la vida (rosado/rojo), Lingüística (verde), Medios de Comunicación (verde azulado). Leyenda de colores de línea: rojo = "Incoming Links", verde = "Outgoing Links". Fuente: http://lod-cloud.net/

## Slide 129
"Ejemplos de LINKED OPEN DATA" — slide de portada de subsección con imagen decorativa de fondo (manos sobre un smartphone con overlay de red de datos/globo terráqueo, textos superpuestos "Business Strategy" — decorativa).

## Slide 130
"Ejemplos de LINKED OPEN DATA" — tres consultas SPARQL sobre Wikidata mostradas en paneles grises lado a lado:
1) "Las universidades que están en Perú": `SELECT ?nom WHERE { ?uni wdt:P31 wd:Q3918 . ?uni rdfs:label ?nom . ?uni wdt:P17 wd:Q419 . FILTER(lang(?nom)="es") }`
2) "La lista de personajes educados en universidades peruanas... nombre de la persona y de la universidad": `SELECT ?unom ?pnom WHERE { ?uni wdt:P31 wd:Q3918. ?uni rdfs:label ?unom. ?uni wdt:P17 wd:Q419. ?person wdt:P69 ?uni. ?person rdfs:label ?pnom. FILTER((LANG(?unom))="es") FILTER((LANG(?pnom))="es") }`
3) "Encuentre la causa de muerte más común para las personas educadas en universidades peruanas. Retorne el nombre de la causa de muerte y la cuenta": `SELECT ?muerte (count(?muerte) as ?count) WHERE { ?pe wdt:P31 wd:Q5. ?uni wdt:P31 wd:Q3918. ?pe wdt:P69 ?uni. ?uni wdt:P17 wd:Q419. ?uni rdfs:label ?nomuni . ?pe rdfs:label ?nom. ?pe wdt:P570 ?death. ?pe wdt:P509 ?causa. ?causa rdfs:label ?muerte FILTER(lang(?nom)="es") FILTER(lang(?nomuni)="es") FILTER(lang(?muerte)="es") } group by ?muerte order by desc(?count) limit 10`
Enlace: https://query.wikidata.org

## Slide 131
"Ejemplos de LINKED OPEN DATA" — captura de pantalla del sitio LinkedGeoData.org ("Adding a spatial dimension to the Web of Data"), mostrando su menú lateral (About/News, Downloads, Online Access, RDF Mapping, Use Cases, LGD Browser, etc.), noticias del proyecto AKSW, y un mapa lateral con un punto de interés (iglesia "Lukaskirche") con sus propiedades RDF (highway, religion, amenity, denomination, etc.).

## Slide 132
"Ejemplos de LINKED OPEN DATA" — captura de pantalla de GeoNames sobre un mapa satelital de Creta (Grecia), mostrando un popup con datos del lugar "Kalamaki" (tipo PPL, jerarquía Greece > Crete > Irákleion > Faistos, coordenadas, ID 7874338) y enlaces a `.kml`/`.rdf`.

## Slide 133
"Ejemplos de LINKED OPEN DATA" — captura de pantalla de data.gov.uk, sección archivada "UKGovLD" describiendo el grupo de trabajo de Linked Data del gobierno del Reino Unido, con panel lateral "10 Second Tour" (Overview of Linked Data, What is Linked Data?, List of Linked Datasets & Vocabularies).

## Slide 134
"Ejemplos de LINKED OPEN DATA" — captura de pantalla de datos.gob.es ("reutiliza la información pública"), listando noticias sobre datos enlazados (Biblioteca Nacional de España, Fundación Land Portal, Pubby y LODI).

## Slide 135
"Ejemplos de LINKED OPEN DATA" — captura de pantalla de InfoLobby (Consejo para la Transparencia de Chile), portal de "Audiencias de Lobby, Viajes y Donativos" con buscador y contadores (Audiencias=233989, Viajes=244086, Donativos=22607). URL: http://www.infolobby.cl/#!/inicio

## Slide 136
"Ejemplos de LINKED OPEN DATA" — captura de pantalla del sitio BBC Music, mostrando un carrusel destacado ("Stormzy to headline Glastonbury Festival 2019") y una fila de artículos/artistas relacionados (ejemplo de Linked Data aplicado a metadatos musicales de la BBC).

## Slide 137
"Ejemplos de LINKED OPEN DATA" — captura de pantalla del Endpoint SPARQL de la Biblioteca del Congreso Nacional de Chile (datos.bcn.cl), con texto explicando qué es un Endpoint SPARQL y su base en la especificación SPROT del W3C. URL: http://datos.bcn.cl/es/

## Slide 138
"Linked Government Data:" — captura de pantalla de datos.gob.cl, portal de datos abiertos del gobierno de Chile, con un banner de "Energía Abierta" y buscador de datasets con etiquetas populares (estadísticas, salud, presupuesto, educación, etc.).

## Slide 139
"Linked Government Data:" — captura de pantalla de catalog.data.gov (EE.UU.), mostrando "233,707 datasets found" con ejemplos como "Demographic Statistics By Zip Code" (formatos CSV, RDF, JSON, XML), "College Scorecard" y "ZIP Code Data".

## Slide 140
"Life Sciences" — captura de pantalla de HealthData.gov, con panel de búsqueda de datos, datasets recientes y categorías (Medicare, Medicaid, Epidemiology, Treatments, Population Statistics); incluye un diagrama de red de agencias de salud en el encabezado (AHRQ, CDC, CMS, FDA, NIH, etc.).

## Slide 141
"E-Commerce" — captura de pantalla del sitio GoodRelations ("The Web Vocabulary for E-commerce"), describiéndose como "el vocabulario más poderoso para publicar detalles de productos y servicios", con lista de empresas que lo usan (Google, Yahoo!, BestBuy, sears.com, kmart.com y más de 10,000 adicionales).

## Slide 142
"Ejemplos de LINKED OPEN DATA" — captura de la página de bienvenida de Poképedia (enciclopedia Pokémon colaborativa en francés, "22 683 articles en français"), con ilustración de numerosos Pokémon como ejemplo curioso de wiki/datos comunitarios enlazados.

## Slide 143
"Aplicaciones de LINKED DATA" — slide de portada de subsección con imagen decorativa de fondo (líneas de código y red de nodos sobre fondo azul oscuro — decorativa).

## Slide 144
"Entonces, ¿quién está utilizando estos conjuntos de datos (y para qué)?" — repite el diagrama de burbujas del LOD cloud (coloreado, similar al de la slide 128) junto a la línea de tiempo completa de fechas (Oct.2007 … Nov.2018), como transición hacia ejemplos de aplicaciones reales.

## Slide 145
"Google's Knowledge Graph" — captura de un resultado de búsqueda de Google para "Sully Prudhomme" mostrando el panel lateral de Knowledge Graph (foto, ocupación "Poet", biografía breve, datos de nacimiento/muerte, libros, premios, sección "People also search for" con otras personas relacionadas).

## Slide 146
"Apple's Siri" — captura de un titular de noticia: "Siri Erroneously Told People Stan Lee Was Dead" (artículo de Beth Elderkin), ejemplo de un error de un asistente basado en datos estructurados/Knowledge Graph.

## Slide 147
"IBM's" — fotografía del programa de TV Jeopardy! con Watson de IBM compitiendo contra dos concursantes humanos (Ken Jennings y Brad Rutter), marcadores en pantalla ($24,000 / $77,147 / $21,600) respondiendo "Who is Bram Stoker?"; a la izquierda, logos de Freebase y DBpedia como fuentes de conocimiento de Watson.

## Slide 148
"En conclusión" — slide de transición de sección, solo texto de encabezado (sin contenido adicional).

## Slide 149
"Una área de investigación aquí…" — fotografía editada de un grupo de personas vestidas de astronautas (montaje humorístico de profesores/investigadores), con un logo superpuesto "Center for Semantic Web Research" (globo terráqueo estilizado con red de nodos). Fondo gris (decorativa/humorística, cierre del bloque de motivación e investigación).

## Slide 150
"Datos ≠ Datos Relacionales" — imagen de un letrero de neón con forma de cabeza humana y la palabra "OPEN" iluminada dentro, sobre fondo negro (decorativa, ilustra la idea de "mente abierta" para pensar datos más allá del modelo relacional).

## Slide 151
Portada de sección: "Semantic Web Agents", con una ilustración tipo ninja/mago sosteniendo un lápiz como espada, sentado en un sillón (decorativa, mascota del curso).

## Slide 152
"Agente Inteligente" — definición: "Un agente inteligente (o agente racional) es una entidad autónoma que observa y actúa sobre un entorno (es decir, es un agente) y dirige su actividad hacia el logro de objetivos (es decir, es racional)." Con la misma ilustración de mascota apuntando con el lápiz.

## Slide 153
"Agentes Inteligentes" — lista de características: están situados en algún entorno y son capaces de percibir ese ambiente; son capaces de actuar de manera autónoma (deciden y ejecutan acciones sin intervención humana); tienen algún tipo de tarea u objetivo; pueden interactuar con otros agentes; son un tema clásico de Inteligencia Artificial (IA).

## Slide 154
"Ejemplo de Agente Inteligente" — ejemplo del termostato como agente reactivo simple: percibe mediante un sensor de temperatura; tiene un conjunto limitado de acciones (encender/apagar calefacción); las acciones tienen condiciones previas ("¡Demasiado frío! → Calefacción encendida", "Temperatura OK! → Calefacción apagada"), dependientes del estado percibido por los sensores.

## Slide 155
"Descripción de Agente Termostato" — especificación formal en pseudocódigo:
- Activación: cada 5 minutos — query: obtenga temperatura ambiente del sensor.
- Acción 1: `if (temperatura ambiente < temperatura deseada) and (calentándose) -> ¡Encienda la calefacción!`
- Acción 2: `if (temperatura ambiente >= temperatura deseada) and (calefacción encendida) -> ¡Apague la calefacción!`

## Slide 156
"Arquitectura simple de un agente" — diagrama de caja "Agent" conectado a un recuadro "Environment": el Agente recibe "Precepts" a través de "Sensors" → bloque "What the world is like now" → bloque "What action I should do now" (alimentado también por "Condition-action rules") → "Actuators" que emiten "Actions" hacia el Environment. Cita [RN02] (Russell & Norvig). Nota: "Los agentes simples actúan sólo en función de sus percepciones actuales."

## Slide 157
"Agentes basados en el conocimiento" — todo el conocimiento del agente reactivo simple está en la lógica del programa; en cambio, los agentes basados en conocimiento se benefician de una base de conocimiento (KB) expresada de forma general, separada de la lógica del programa; pueden agregar conocimiento nuevo, consultar lo que se sabe y hacer inferencia; solo se especifica qué sabe el agente y qué objetivos tiene.

## Slide 158
"Descripción de un agente de taxi basado en el conocimiento" — especificación en pseudocódigo:
- Activación: cada vez que un cliente ingresa un destino — query: obtener ubicación actual y encontrar la ruta entre ubicación actual y destino.
- Acción 1: `if (ubicación actual != Destino) and (la ruta existe) -> ¡Manejar! Actualiza la ubicación actual.`
- Acción 2: `if (ubicación actual == destino) -> ¡Obtenga dinero del cliente!`
- Acción 3: `if not (la ruta existe) -> ¡Dígale al cliente que ingrese un nuevo destino!`

## Slide 159
"Agente web semántico" — definición: "Un agente es un programa que actúa en nombre de una persona u organización." [W3C]

## Slide 160
"Definición visionaria: Agente web semántico" — cita extensa de Berners-Lee et al. 2001: "El verdadero poder de la Web Semántica se hará realidad cuando las personas creen muchos programas que recopilan contenido web de diversas fuentes, procesan la información e intercambian los resultados con otros programas... La Web Semántica promueve esta sinergia: incluso agentes que no fueron diseñados expresamente para trabajar juntos pueden transferir datos entre ellos mismos cuando los datos vienen con semántica."

## Slide 161
"Agentes basados en conocimiento VS Agentes Web Semánticos" — tabla comparativa en dos columnas:

| Agentes basados en conocimiento | Agentes Web Semánticos |
|---|---|
| Cómo es el conocimiento representado no es específico. | La web semántica proporciona estándares para representar el conocimiento. |
| Los agentes usan su conocimiento para elegir la acción que los acerca más a su objetivo y la ejecutan. | Los agentes SW utilizan su conocimiento para elegir un conjunto de posibles acciones, pero el usuario decide qué acción tomar. |
| Amplia variedad de tipos de agente y tecnologías usadas. | Los agentes de SW siempre están basados en el conocimiento y usan tecnologías SW. |

## Slide 162
"¿Qué necesita un agente Web semántico?" (parte 1) — lista: una base de conocimiento (RDF, RDFS, OWL); capacidad de hacer preguntas a la base de conocimiento (SPARQL); capacidad de hacer inferencia sobre el conocimiento (reglas de inferencia RDFS, razonadores OWL, p.ej. "cuadros"); capacidad de activarse en un punto determinado; capacidad de comunicarse con otros agentes; capacidad de comunicarse con el usuario; nota de que los marcos de agentes (p.ej. JADE) no son un área propia de la Web Semántica, sino tecnología existente mejorada con recomendaciones SW.

## Slide 163
"¿Qué necesita un agente Web semántico?" (parte 2) — ejemplos de tipos de agentes: un agente de recuperación que busca conocimiento en la Web Semántica; un agente personal que usa el conocimiento formal de la Web Semántica para reservar vacaciones o citas médicas; un sistema multiagente capaz de construir y mantener conjuntos de datos vinculados adicionales, por ejemplo actualizando datos basados en Wikipedia.

## Slide 164
"Descripción de un Agente de Pizza Web Semántica (incompleto)" — especificación en pseudocódigo con una consulta SPARQL embebida:
```
Activation  User activation.
Query       One group for each $TOPPING the user likes.

SELECT DISTINCT ?pizza
WHERE {
  ?pizza rdfs:subClassOf pz:NamedPizza .
  {
    ?pizza rdfs:subClassOf ?restrictionTopping1 .
    ?restrictionTopping1 owl:onProperty pz:hasTopping .
    ?restrictionTopping1 owl:someValuesFrom $TOPPING .
  }
  ...
}

Action  if Result list is not empty.
        -> Recommend the resulting pizza(s) to the user.
```

## Slide 165
"¿Preguntas?" — slide de cierre del capítulo, con una imagen decorativa de fondo de una red de nodos conectados en tonos azules sobre fondo negro.
