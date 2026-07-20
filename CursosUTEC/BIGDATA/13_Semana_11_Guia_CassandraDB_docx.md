---
curso: BIGDATA
titulo: 13 - Semana 11/Guia CassandraDB
slides: 0
fuente: 13 - Semana 11/Guia CassandraDB.docx
---

**CMD**

\>\> docker –versión (debe aparecer la versión 28.5.1 o posterior)

\>\> docker ps

\>\> docker pull cassandra: latest

\>\> docker images

**REPOSITORY TAG IMAGE ID CREATED SIZE**

cassandra latest 8b55dd41d5d1 4 weeks ago 580MB

\>\> docker run -p 7000:7000 -p 7199:7199 -p 9042:9042 --name cassandra -d cassandra:latest

\>\> docker ps

CONTAINER ID IMAGE COMMAND CREATED STATUS PORT

7b0b164f6e60 cassandra:latest

\>\> docker exec -it 7b0b164f6e60 bash

root@7b0b164f6e60:/# cqlsh

Connected …

cqlsh\> create keyspace name with replication={‘class’:’SimpleStrategy’, ‘replication_factor’:1};

cqlsh\> desc keyspaces;

cqlsh\> use name;

cqlsh:name\> create table mitabla (ID int PRIMARY KEY, nombre text, edad varint)

cqlsh:name\> desc tables;

cqlsh:name\> select \* from mitabla;

cqlsh:name\> insert into mitabla(id, edad, nombre) values (1, 34, ‘Jorge’);

cqlsh:name\> select \* from mitabla;

**En otro CMD**

\#Creamos un environment en Python

\>\>conda create -n cassandra311 python=3.11

Proceed (\[y\]/n)? y

\>\>conda actívate cassandra311

(cassandra311) \>\> pip install cassandra-driver

(cassandra311) \>\> pip install notebook

\>\>jupyter notebook
