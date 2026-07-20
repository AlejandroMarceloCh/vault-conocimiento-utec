---
curso: BIGDATA
titulo: 13 - Semana 11/Actividad 11.2 Cypher
slides: 0
fuente: 13 - Semana 11/Actividad 11.2 Cypher.txt
---

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row
RETURN row
LIMIT 10;

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row
RETURN row.usuario
LIMIT 20;

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row
RETURN count(row);

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row
RETURN keys(row)
LIMIT 1;

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row
RETURN DISTINCT row.pelicula;

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row

MERGE (:Usuario {nombre:row.usuario});

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row

MERGE (:Pelicula {titulo:row.pelicula});

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row

MERGE (:Genero {nombre:row.genero});

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row

MERGE (:Actor {nombre:row.actor});

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row

MERGE (:Director {nombre:row.director});


LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row

MATCH (u:Usuario {nombre:row.usuario})
MATCH (p:Pelicula {titulo:row.pelicula})

MERGE (u)-[:VIO]->(p);

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row

MATCH (u:Usuario {nombre:row.usuario})
MATCH (p:Pelicula {titulo:row.pelicula})

MERGE (u)-[r:CALIFICO]->(p)
SET r.rating=toInteger(row.rating);

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row

MATCH (p:Pelicula {titulo:row.pelicula})
MATCH (g:Genero {nombre:row.genero})

MERGE (p)-[:PERTENECE_A]->(g);


LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row

MATCH (a:Actor {nombre:row.actor})
MATCH (p:Pelicula {titulo:row.pelicula})

MERGE (a)-[:ACTUO_EN]->(p);

LOAD CSV WITH HEADERS
FROM 'https://raw.githubusercontent.com/ALezamaB/datasets/refs/heads/main/peliculas1.csv'
AS row

MATCH (d:Director {nombre:row.director})
MATCH (p:Pelicula {titulo:row.pelicula})

MERGE (d)-[:DIRIGIO]->(p);
