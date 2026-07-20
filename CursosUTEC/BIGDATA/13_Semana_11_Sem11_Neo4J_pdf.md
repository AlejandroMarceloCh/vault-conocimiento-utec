---
curso: BIGDATA
titulo: 13 - Semana 11/Sem11_Neo4J
slides: 22
fuente: 13 - Semana 11/Sem11_Neo4J.pdf
---

Neo4J
Mg. Aldo Lezama Benavides


Semana 11
        Objetivo de la sesión

1. Comprender los conceptos fundamentales de las bases de datos de
   grafos, identificando los componentes principales: nodos (vertices),
   relaciones (edges), etiquetas y propiedades.
2. Aplicar el lenguaje Cypher para crear, consultar y analizar relaciones
   entre entidades, utilizando patrones de conexión y comandos básicos
   como MATCH, WHERE y RETURN.
3. Analizar cómo la representación de datos basada en grafos permite
   modelar relaciones complejas del mundo real (como redes sociales o
   sistemas de recomendación) de forma más natural que en los modelos
   relacionales.
Contenido de la sesión

      01.         02.

   Introducción   Cypher
01.   Introducción a Graph Database
             Introducción a las Bases de Datos de Grafos


• Las    bases     de   datos   tradicionales   (relacionales)
  almacenan información en tablas con filas y columnas.
• Sin embargo, muchas relaciones del mundo real no se
  representan fácilmente con tablas: redes sociales,
  sistemas   de    recomendación,     o   conexiones    entre
  personas, empresas o productos.
• Una base de datos de grafos representa los datos como
  un    conjunto   de   nodos    (entidades)    y   relaciones
  (conexiones entre entidades).
• Cada nodo y relación puede tener propiedades, es decir,
  pares clave–valor..
                                 Componentes de un grafo
Node (Vertex)
Un vertex (o nodo, en español) es una entidad o punto dentro de
un grafo.
Es el objeto principal que representa cosas del mundo real:
personas, lugares, productos, transacciones, etc.
En otras palabras, un vertex es como una fila en una tabla          Tania   TIENE   Carro

relacional, pero con mucha más flexibilidad.

Relation(Edge)
Enlace entre dos nodos. Tiene:
• Dirección
• Tipo
Se permite un nodo sin relaciones. No se permite una relación sin
nodos.
                                              Estructura


Node (Vertex)
Relation(Edge)
Label
• Indica el tipo de nodo
                                                                   :Persona              TIENE          :Vehiculo
Properties
• Pares clave-valor que describen atributos
                                                           {name: "Tania", born: 2000}           {name: “Toyota", model: 2024}
Identificador Interno
• ID único que usa Neo4j internamente
02.   Cypher
                                             Cypher


El lenguaje Cypher (usado en Neo4j) tiene las siguientes características clave:

1. Declarativo

• Cypher es un lenguaje declarativo, lo que significa que tú indicas qué quieres obtener, no

  cómo hacerlo.

• Neo4j se encarga internamente de decidir cómo ejecutar la consulta de manera eficiente.

  MATCH (a:Actor)-[:ACTED_IN]->(m:Movie)
  RETURN a.name, m.title

• Aquí solo declaras el resultado que quieres (actores y películas), sin decir cómo recorrer

  el grafo o qué índices usar.
                                          Cypher


2. Expresivo

• Cypher permite expresar consultas complejas de manera clara y legible, similar a cómo

  escribirías una oración en inglés.

  MATCH (d:Director)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Actor)
  RETURN d.name AS Director, collect(a.name) AS Actores

• Esta consulta compleja (director → película → actores) se entiende fácilmente por su

  sintaxis intuitiva.
                                              Cypher


3. Basado en patrones

• Cypher está basado en el reconocimiento de patrones dentro del grafo.

• Los patrones se describen con nodos ( ) y relaciones [ ], conectados por flechas --> o <--.

  MATCH (p:Person)-[:FRIEND_OF]->(f:Person)
  RETURN p.name, f.name

• El patrón (p)-[:FRIEND_OF]->(f) busca todas las personas conectadas por una relación

  de amistad.
Laboratorio
Laboratorio
Visualización del Esquema
Comando MATCH – Vista Graph
Comando MATCH – Vista Table
Comando WHERE
COUNT y ORDER BY
Usando Relationship Types
FOREARCH

                      Conclusiones

01.   Neo4j permite modelar datos de manera relacional y visual, priorizando las
      conexiones entre entidades y facilitando el análisis de redes complejas.




02.   El lenguaje Cypher es declarativo, expresivo y basado en patrones, lo que permite
      construir consultas intuitivas y eficientes para explorar los grafos.


      Las bases de datos de grafos representan una alternativa poderosa a los sistemas
03.   relacionales cuando el valor analítico se encuentra en las relaciones y no solo en
      los datos individuales.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
