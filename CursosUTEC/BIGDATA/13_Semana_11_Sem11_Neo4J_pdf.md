---
curso: BIGDATA
titulo: 13 - Semana 11/Sem11_Neo4J
slides: 22
fuente: 13 - Semana 11/Sem11_Neo4J.pdf
---

## Slide 1

Portada (decorativa). Título grande: **Neo4J**. Subtítulo: **Semana 11**. Autor: Mg. Aldo Lezama Benavides. Chrome UTEC ("Reinventa el mundo", foto del edificio UTEC).

## Slide 2

**Objetivo de la sesión**

1. **Comprender** los conceptos fundamentales de las bases de datos de grafos, identificando los componentes principales: nodos (vertices), relaciones (edges), etiquetas y propiedades.
2. **Aplicar** el lenguaje Cypher para crear, consultar y analizar relaciones entre entidades, utilizando patrones de conexión y comandos básicos como MATCH, WHERE y RETURN.
3. **Analizar** cómo la representación de datos basada en grafos permite modelar relaciones complejas del mundo real (como redes sociales o sistemas de recomendación) de forma más natural que en los modelos relacionales.

## Slide 3

**Contenido de la sesión**

Dos secciones enmarcadas en corchetes:
- **01.** Introducción
- **02.** Cypher

## Slide 4

Portada de sección (decorativa): **01. Introducción a Graph Database**. Ícono de clipboard/checklist.

## Slide 5

**Introducción a las Bases de Datos de Grafos**

- Las bases de datos tradicionales (relacionales) almacenan información en tablas con filas y columnas.
- Sin embargo, muchas relaciones del mundo real no se representan fácilmente con tablas: redes sociales, sistemas de recomendación, o conexiones entre personas, empresas o productos.
- Una base de datos de grafos representa los datos como un conjunto de nodos (entidades) y relaciones (conexiones entre entidades).
- Cada nodo y relación puede tener propiedades, es decir, pares clave–valor.

**Visual (diagrama a la derecha, "Graph Database"):** grafo de nodos coloreados agrupados por dominios de negocio. Nodos etiquetados y conectados por flechas dirigidas:
- **PEOPLE**: HUMAN RESOURCES, FINANCE, OPERATIONS, CUSTOMER SERVICE.
- **APPLICATION**: DESIGN, WEBSITE, ERP.
- **PROCESS**: MANAGE RISKS, MANAGE STRATEGIC INITIATIVES, INCREASE REVENUE.
- **INFRASTRUCTURE**: NETWORKS, STORAGE, DATA CENTERS.
Las flechas conectan los dominios entre sí (p. ej. OPERATIONS/CUSTOMER SERVICE → MANAGE RISKS → MANAGE STRATEGIC INITIATIVES → INCREASE REVENUE → NETWORKS/STORAGE/DATA CENTERS), ilustrando que el valor está en las conexiones cruzadas entre áreas.

## Slide 6

**Componentes de un grafo**

**Node (Vertex)**
Un vertex (o nodo, en español) es una entidad o punto dentro de un grafo. Es el objeto principal que representa cosas del mundo real: personas, lugares, productos, transacciones, etc. En otras palabras, un vertex es como una fila en una tabla relacional, pero con mucha más flexibilidad.

**Relation (Edge)**
Enlace entre dos nodos. Tiene:
- Dirección
- Tipo

Se permite un nodo sin relaciones. No se permite una relación sin nodos.

**Visual (diagrama a la derecha):** dos nodos circulares azules — **Tania** y **Carro** — unidos por una relación dirigida (flecha) con recuadro de etiqueta **TIENE** apuntando de Tania a Carro.

## Slide 7

**Estructura**

- **Node (Vertex)**
- **Relation (Edge)**
- **Label** — Indica el tipo de nodo
- **Properties** — Pares clave-valor que describen atributos
- **Identificador Interno** — ID único que usa Neo4j internamente

**Visual (diagrama a la derecha):** dos nodos azules **:Persona** y **:Vehiculo** unidos por relación dirigida **TIENE**. Debajo de cada nodo, sus propiedades:
- :Persona → `{name: "Tania", born: 2000}`
- :Vehiculo → `{name: "Toyota", model: 2024}`

## Slide 8

Portada de sección (decorativa): **02. Cypher**. Ícono de clipboard/checklist.

## Slide 9

**Cypher**

El lenguaje Cypher (usado en Neo4j) tiene las siguientes características clave:

**1. Declarativo**
- Cypher es un lenguaje declarativo, lo que significa que tú indicas qué quieres obtener, no cómo hacerlo.
- Neo4j se encarga internamente de decidir cómo ejecutar la consulta de manera eficiente.

```cypher
MATCH (a:Actor)-[:ACTED_IN]->(m:Movie)
RETURN a.name, m.title
```

- Aquí solo declaras el resultado que quieres (actores y películas), sin decir cómo recorrer el grafo o qué índices usar.

## Slide 10

**Cypher**

**2. Expresivo**
- Cypher permite expresar consultas complejas de manera clara y legible, similar a cómo escribirías una oración en inglés.

```cypher
MATCH (d:Director)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Actor)
RETURN d.name AS Director, collect(a.name) AS Actores
```

- Esta consulta compleja (director → película → actores) se entiende fácilmente por su sintaxis intuitiva.

## Slide 11

**Cypher**

**3. Basado en patrones**
- Cypher está basado en el reconocimiento de patrones dentro del grafo.
- Los patrones se describen con nodos `( )` y relaciones `[ ]`, conectados por flechas `-->` o `<--`.

```cypher
MATCH (p:Person)-[:FRIEND_OF]->(f:Person)
RETURN p.name, f.name
```

- El patrón `(p)-[:FRIEND_OF]->(f)` busca todas las personas conectadas por una relación de amistad.

## Slide 12

**Laboratorio**

**Captura de pantalla:** navegador en `neo4j.com/sandbox/`. Landing page de Neo4j Sandbox. Barra negra superior: "Join Us on Nov 6 for 24 Hours of Live Sessions at NODES 2025 | Register Today". Menú de navegación (Products, Use Cases, Developers, AI Systems, Learn, Pricing) y botón **Get Started Free**. Sección hero morada: **"Get started with Neo4j Sandbox while your coffee is still brewing"** con texto "Neo4j is a native graph database, purpose-built to leverage data relationships..." y botón azul **Launch the Free Sandbox**. Abajo: **"Experience Neo4j in a click with the Sandbox — Pick a project and get started in less than 60 seconds. No download required."**

## Slide 13

**Laboratorio**

**Captura de pantalla:** UI de Neo4j Sandbox (`sandbox.neo4j.com`), diálogo **"Select a project"**. Filtros: For Developers (17), For Data Scientists (3). Sección **Featured Dataset** con tarjetas:
- **Movies** (Beginner, For Developers) — seleccionada (check azul). "A guide to common graph query patterns involving connections between movies, actors, and directors."
- **OpenStreetMap** (For Developers) — "A graph solution to the shortest-path problem... Central Park in New York City." Libraries Enabled: GraphQL.
- **Graph Data Science** (Beginner, For Data Scientists) — "Leverage Neo4j Graph Data Science library..." Libraries Enabled: Graph Data Science.
- **ICIJ Offshoreleaks** (For Developers, New) — "The Offshore leaks dataset and guide from the International Consortium of Investigative Journalists (ICIJ)."

Abajo: sección "Your own data", Project: **Movies**, botón azul **Create and Download credentials**.

## Slide 14

**Visualización del Esquema**

**Captura de pantalla (Neo4j Browser):** consulta ejecutada:
```cypher
CALL db.schema.visualization()
```
**Grafo del esquema:** nodo naranja **Person** con auto-relación (loop) **FOLLOWS** sobre sí mismo, y varias relaciones dirigidas hacia un nodo morado **Movie**: DIRECTED, WROTE, PRODUCED, REVIEWED, ACTED_IN.

Panel **Overview** a la derecha:
- **Node labels:** * (2), Movie (1), Person (1)
- **Relationship types:** * (6), ACTED_IN (1), REVIEWED (1), PRODUCED (1), WROTE (1), FOLLOWS (1), DIRECTED (1)
- "Displaying 2 nodes, 6 relationships."

## Slide 15

**Comando MATCH – Vista Graph**

**Captura de pantalla (Neo4j Browser):** consulta:
```cypher
MATCH (n1:Person) RETURN n1;
```
**Grafo:** ~133 nodos naranjas (personas) dispersos en un patrón circular, mayormente sin conexiones visibles.

Panel **Overview:**
- **Node labels:** * (133), Person (133)
- **Relationship types:** * (3), FOLLOWS (3)
- "Displaying 133 nodes, 0 relationships."

## Slide 16

**Comando MATCH – Vista Table**

**Captura de pantalla (Neo4j Browser):** consulta:
```cypher
MATCH (n2:Movie) RETURN n2;
```
Vista **Table** mostrando resultados en JSON. Primer registro:
```json
{
  "identity": 0,
  "labels": [
    "Movie"
  ],
  "properties": {
    "tagline": "Welcome to the Real World",
    "title": "The Matrix",
    "released": 1999
  },
  "elementId": "4:2ebf52ab-f85f-4841-94ff-d275cfde451b:0"
}
```
Segundo registro comienza con `{ "identity": 9, "labels": [ ...`

## Slide 17

**Comando WHERE**

**Captura de pantalla (Neo4j Browser):** consulta:
```cypher
MATCH (n1:Movie) WHERE n1.released>1990 RETURN n1;
```
**Grafo:** 34 nodos morados (películas), sin relaciones.

Panel **Overview:**
- **Node labels:** * (34), Movie (34)
- "Displaying 34 nodes, 0 relationships."

## Slide 18

**COUNT y ORDER BY**

**Captura 1 (Neo4j Browser):**
```cypher
MATCH (n1:Movie) WHERE n1.released>1990 RETURN COUNT(n1) AS TotalPelis;
```
Vista Table: columna **TotalPelis** = **34**. "Started streaming 1 records after 14 ms and completed after 15 ms."

**Captura 2 (Neo4j Browser):**
```cypher
MATCH (n1:Person)-[r:ACTED_IN]->(n2:Movie) RETURN n2.title, count(n1) as num_actores
ORDER BY num_actores desc limit 3;
```
Vista Table (columnas n2.title / num_actores):

| n2.title | num_actores |
|----------|-------------|
| "A Few Good Men" | 12 |
| "Jerry Maguire" | 9 |
| "The Green Mile" | 8 |

## Slide 19

**Usando Relationship Types**

**Captura 1 (Neo4j Browser):**
```cypher
MATCH (n1:Person)-[r:ACTED_IN]->(:Movie {title: "Apollo 13"}) RETURN n1.name;
```
Vista Table, columna **n1.name**: "Tom Hanks", "Ed Harris", "Gary Sinise", "Kevin Bacon", "Bill Paxton".

**Captura 2 (Neo4j Browser):**
```cypher
MATCH (n1:Person)-[:DIRECTED]->(m:Movie)
WHERE m.title IN ["Apollo 13", "V for Vendetta", "Top Gun"]
RETURN n1.name, m.title;
```
Vista Table (n1.name / m.title):

| n1.name | m.title |
|---------|---------|
| "Ron Howard" | "Apollo 13" |
| "James Marshall" | "V for Vendetta" |
| "Tony Scott" | "Top Gun" |

## Slide 20

**FOREARCH** (sic; FOREACH)

**Captura 1 (Neo4j Browser):** crea relaciones WORKED_WITH entre directores y actores de una misma película:
```cypher
MATCH (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person)
WITH m, collect(DISTINCT d) AS directores, collect(DISTINCT a) AS actores
FOREACH (dir IN directores |
  FOREACH (act IN actores |
    MERGE (dir)-[:WORKED_WITH]->(act)
  )
);
```
Resultado: "Created 175 relationships, completed after 557 ms."

**Captura 2 (Neo4j Browser):**
```cypher
MATCH (d:Person)-[:WORKED_WITH]->(a:Person) RETURN d.name, a.name;
```
Vista Table (d.name / a.name), filas 85–90:

| d.name | a.name |
|--------|--------|
| "Werner Herzog" | "Marshall Bell" |
| "Werner Herzog" | "Zach Grenier" |
| "Vincent Ward" | "Annabella Sciorra" |
| "Vincent Ward" | "Robin Williams" |
| "Vincent Ward" | "Max von Sydow" |
| "Vincent Ward" | "Cuba Gooding Jr." |

## Slide 21

**Conclusiones**

01. Neo4j permite modelar datos de manera relacional y visual, priorizando las conexiones entre entidades y facilitando el análisis de redes complejas.

02. El lenguaje Cypher es declarativo, expresivo y basado en patrones, lo que permite construir consultas intuitivas y eficientes para explorar los grafos.

03. Las bases de datos de grafos representan una alternativa poderosa a los sistemas relacionales cuando el valor analítico se encuentra en las relaciones y no solo en los datos individuales.

## Slide 22

Cierre (decorativa): logo **UTEC — Universidad de Ingeniería y Tecnología** sobre fondo celeste. Sin contenido textual adicional.
