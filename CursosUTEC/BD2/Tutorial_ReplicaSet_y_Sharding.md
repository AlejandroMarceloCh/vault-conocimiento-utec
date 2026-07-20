---
curso: BD2
titulo: Tutorial ReplicaSet y Sharding
slides: 10
fuente: Tutorial ReplicaSet y Sharding.pdf
---

# Tutorial ReplicaSet y Sharding

## Índice

- [Objetivos del tutorial](#objetivos-del-tutorial)
- [ReplicaSet con Docker](#replicaset-con-docker)
  - [Instalación y red Docker](#instalación-y-red-docker)
  - [Archivo docker-compose.yml](#archivo-docker-composeyml)
  - [Inicialización, verificación y conexión](#inicialización-verificación-y-conexión)
  - [Prueba de replicación](#prueba-de-replicación)
- [Sharding con Docker](#sharding-con-docker)
  - [Configuración general de un entorno sharded](#configuración-general-de-un-entorno-sharded)
  - [Docker Compose para sharding con Replica Sets](#docker-compose-para-sharding-con-replica-sets)
  - [Inicialización de Replica Sets](#inicialización-de-replica-sets)
  - [Agregar shards al enrutador mongos](#agregar-shards-al-enrutador-mongos)
  - [Habilitar sharding y monitorear el estado](#habilitar-sharding-y-monitorear-el-estado)
  - [Gestión de chunks](#gestión-de-chunks)
- [Conclusión](#conclusión)
- [Glosario](#glosario)

## Objetivos del tutorial

- Identificar y solucionar problemas en entornos distribuidos.
- Configurar y gestionar un Replica Set para alta disponibilidad y recuperación ante desastres.
- Entender el sharding y su propósito en la escalabilidad horizontal.
- Aprender a shardear una colección real y manejar el balanceo de chunks.

(slide 1)

## ReplicaSet con Docker

### Instalación y red Docker

Docker facilita la administración y despliegue de instancias de MongoDB y permite un entorno replicable y portable.

1. Instalar Docker: Si no tienes Docker instalado, puedes descargarlo desde docker.com.

2. Crear una red Docker: MongoDB necesita que todas las instancias del Replica Set se comuniquen entre sí. Para esto, creamos una red dedicada en Docker:

```bash
docker network create mongo-replica-set
```

3. Levantar los contenedores de MongoDB: Debes crear tres contenedores que representarán a los nodos del Replica Set. Vamos a usar Docker Compose para facilitar la configuración.

Crea un archivo llamado docker-compose.yml con el siguiente contenido:

(slides 1–2)

### Archivo docker-compose.yml

```yaml
services:
  mongo1:
    image: mongo:latest
    container_name: mongo1
    hostname: mongo1
    networks:
      - mongo-replica-set
    ports:
      - "27017:27017"
    volumes:
      - ./data/mongo1:/data/db
    command: >
      mongod --replSet rs0 --bind_ip localhost,mongo1

  mongo2:
    image: mongo:latest
    container_name: mongo2
    hostname: mongo2
    networks:
      - mongo-replica-set
    ports:
      - "27018:27017"
    volumes:
      - ./data/mongo2:/data/db
    command: >
      mongod --replSet rs0 --bind_ip localhost,mongo2

  mongo3:
    image: mongo:latest
    container_name: mongo3
    hostname: mongo3
    networks:
      - mongo-replica-set
    ports:
      - "27019:27017"
    volumes:
      - ./data/mongo3:/data/db
    command: >
      mongod --replSet rs0 --bind_ip localhost,mongo3

networks:
  mongo-replica-set:
    driver: bridge
```

En este archivo:

- Se definen tres contenedores (`mongo1`, `mongo2`, `mongo3`), cada uno con un puerto diferente para MongoDB (27017, 27018, 27019).
- Todos usan el mismo Replica Set (`rs0`) y están en la misma red de Docker (`mongo-replica-set`).

4. Iniciar los contenedores: En la carpeta donde está tu archivo docker-compose.yml, ejecuta:

(slide 2)

### Inicialización, verificación y conexión

```bash
docker-compose up -d
```

Esto levantará los tres contenedores de MongoDB en segundo plano.

5. Inicializar el Replica Set: Ahora que los tres nodos de MongoDB están ejecutándose en contenedores Docker, necesitas inicializar el Replica Set. Conéctate al contenedor mongo1:

```bash
docker exec -it mongo1 mongosh
```

Una vez dentro del shell de MongoDB, inicializa el Replica Set con el siguiente comando:

```javascript
rs.initiate(
  {
    _id : "rs0",
    members: [
      { _id: 0, host: "mongo1:27017" },
      { _id: 1, host: "mongo2:27017" },
      { _id: 2, host: "mongo3:27017" }
    ]
  }
)
```

6. Verificar el estado del Replica Set: Puedes verificar el estado del Replica Set ejecutando el siguiente comando:

```javascript
rs.status()
```

Esto mostrará el estado de los tres nodos, uno de los cuales será el primary y los otros dos serán secondary.

Si al ejecutar rs.status() todos los nodos aparecen como secondary, significa que ninguno de los nodos ha sido elegido como primary. A veces, reiniciar los nodos puede ayudar a resolver problemas de elección de primary.

```bash
docker exec -it mongo1 bash
mongod --replSet rs0
```

7. Conectar a la base de datos: Una vez configurado el Replica Set, puedes conectarte a MongoDB utilizando cualquier cliente de MongoDB, como mongosh o MongoDB Compass, con la URI de conexión similar a esta:

```
mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0
```

* Es probable que se requiera mapear los hosts en el archivo de configuración de red de windows:

Abrir el archivo hosts:

```
C:\Windows\System32\drivers\etc\hosts
```

Agregar las siguientes líneas:

```
127.0.0.1          mongo1
127.0.0.1          mongo2
127.0.0.1          mongo3
```

(slide 3)

### Prueba de replicación

8. Probar la replicación: Para verificar que la replicación esté funcionando, basta con crear un colección y agregar datos. Luego con MongoDB Compass crear conexiones individuales a cada miembro del cluster para verificar la existencia de los datos.

**Figura:** Captura de pantalla de MongoDB Compass que muestra dos conexiones de cluster en el panel lateral izquierdo: **Cluster-Central** y **Cluster-mongo2**. En **Cluster-Central**, expandido, se ven las bases de datos `admin`, `config`, `local` y `twitter`. Dentro de la base de datos `twitter` aparecen las colecciones `productos` y `tweet`, señaladas con flechas rojas. En **Cluster-mongo2**, también parcialmente expandido, se muestra la misma base de datos `twitter` con las colecciones `tweet` y `productos`, demostrando que los datos se replicaron entre ambos miembros del cluster.

(slide 4)

## Sharding con Docker

Sharding permite dividir los datos en diferentes servidores para manejar grandes cantidades de datos y mejorar la escalabilidad.

Para agregar Sharding a la configuración de un Replica Set en MongoDB utilizando Docker, necesitamos realizar algunos pasos adicionales.

(slide 4)

### Configuración general de un entorno sharded

Un entorno sharded en MongoDB típicamente consta de:

1. Mongos: Es el enrutador que se comunica con las bases de datos sharded.
2. Config Servers: Almacenan la metadata del clúster (información sobre los shards).
3. Shards: Son los servidores donde se almacenan los datos. Cada shard puede ser un Replica Set para asegurar alta disponibilidad.

(slide 4)

### Docker Compose para sharding con Replica Sets

1. Crear el archivo docker-compose.yml para Sharding

Este archivo define los config servers, shards (que son Replica Sets), y el router mongos.

```yaml
services:
  # Config Servers (metadata)
  configsvr1:
    image: mongo:latest
    container_name: configsvr1
    hostname: configsvr1
    command: --replSet configReplSet --configsvr --port 27019
    volumes:
      - ./data/configsvr1:/data/db
    networks:
      - mongo-cluster

  configsvr2:
    image: mongo:latest
    container_name: configsvr2
    hostname: configsvr2
    command: --replSet configReplSet --configsvr --port 27019
    volumes:
      - ./data/configsvr2:/data/db
    networks:
      - mongo-cluster

  configsvr3:
    image: mongo:latest
    container_name: configsvr3
    hostname: configsvr3
    command: --replSet configReplSet --configsvr --port 27019
    volumes:
      - ./data/configsvr3:/data/db
    networks:
      - mongo-cluster

  # Shard 1 - Replica Set 1
  shard1_1:
    image: mongo:latest
    container_name: shard1_1
    hostname: shard1_1
    command: --replSet shard1 --shardsvr --port 27017
    volumes:
      - ./data/shard1_1:/data/db
    networks:
      - mongo-cluster

  shard1_2:
    image: mongo:latest
    container_name: shard1_2
    hostname: shard1_2
    command: --replSet shard1 --shardsvr --port 27017
    volumes:
      - ./data/shard1_2:/data/db
    networks:
      - mongo-cluster

  shard1_3:
    image: mongo:latest
    container_name: shard1_3
    hostname: shard1_3
    command: --replSet shard1 --shardsvr --port 27017
    volumes:
      - ./data/shard1_3:/data/db
    networks:
      - mongo-cluster

  # Shard 2 - Replica Set 2
  shard2_1:
    image: mongo:latest
    container_name: shard2_1
    hostname: shard2_1
    command: --replSet shard2 --shardsvr --port 27017
    volumes:
      - ./data/shard2_1:/data/db
    networks:
      - mongo-cluster

  shard2_2:
    image: mongo:latest
    container_name: shard2_2
    hostname: shard2_2
    command: --replSet shard2 --shardsvr --port 27017
    volumes:
      - ./data/shard2_2:/data/db
    networks:
      - mongo-cluster

  shard2_3:
    image: mongo:latest
    container_name: shard2_3
    hostname: shard2_3
    command: --replSet shard2 --shardsvr --port 27017
    volumes:
      - ./data/shard2_3:/data/db
    networks:
      - mongo-cluster

  # Mongos (Router)
  mongos:
    image: mongo:latest
    container_name: mongos
    hostname: mongos
    command: mongos --configdb configReplSet/configsvr1:27019,configsvr2:27019,configsvr3:27019 --port 27017 --bind_ip_all
    ports:
      - "27017:27017"
    depends_on:
      - configsvr1
      - configsvr2
      - configsvr3
    networks:
      - mongo-cluster

networks:
  mongo-cluster:
    driver: bridge
```

Descripción del archivo:

- Config Servers (`configsvr1`, `configsvr2`, `configsvr3`): Son los nodos que almacenan la metadata del clúster, formando un Replica Set `configReplSet`.
- Shards: Hay dos shards (`shard1` y `shard2`), cada uno con tres réplicas, formando dos Replica Sets `shard1` y `shard2`.
- Mongos: Es el enrutador de MongoDB, que dirige las consultas al shard correcto.

2. Iniciar los contenedores:

Ejecuta el comando para levantar los contenedores:

```bash
docker-compose up -d
```

(slides 5–7)

### Inicialización de Replica Sets

3. Inicializar los Replica Sets:

Ahora, debes inicializar cada Replica Set (config servers y shards). Esto se puede hacer conectándose a cada instancia y ejecutando los comandos de `rs.initiate()`.

Inicializar Config Replica Set:

Conéctate al primer config server (`configsvr1`):

```bash
docker exec -it configsvr1 mongosh --port 27019
```

Luego, inicializa el Replica Set de los config servers:

```javascript
rs.initiate({
  _id: "configReplSet",
  configsvr: true,
  members: [
    { _id: 0, host: "configsvr1:27019" },
    { _id: 1, host: "configsvr2:27019" },
    { _id: 2, host: "configsvr3:27019" }
  ]
})
```

Inicializar los Shard Replica Sets:

Conéctate al primer nodo del primer shard (`shard1_1`):

```bash
docker exec -it shard1_1 mongosh --port 27017
```

Ejecuta el siguiente comando para inicializar el Replica Set del shard 1:

```javascript
rs.initiate({
  _id: "shard1",
  members: [
    { _id: 0, host: "shard1_1:27017" },
    { _id: 1, host: "shard1_2:27017" },
    { _id: 2, host: "shard1_3:27017" }
  ]
})
```

Repite lo mismo para el segundo shard conectándote a `shard2_1`:

```bash
docker exec -it shard2_1 mongosh --port 27017
```

Y ejecuta:

```javascript
rs.initiate({
  _id: "shard2",
  members: [
    { _id: 0, host: "shard2_1:27017" },
    { _id: 1, host: "shard2_2:27017" },
    { _id: 2, host: "shard2_3:27017" }
  ]
})
```

(slides 7–8)

### Agregar shards al enrutador mongos

4. Agregar los shards al enrutador (mongos):

Conéctate al contenedor mongos:

```bash
docker exec -it mongos mongosh --port 27017
```

Agrega los shards al sistema:

```javascript
sh.addShard("shard1/shard1_1:27017,shard1_2:27017,shard1_3:27017")
sh.addShard("shard2/shard2_1:27017,shard2_2:27017,shard2_3:27017")
```

Conectarse a los shards: Para conectarte a un cluster sharded de MongoDB se realiza a través del router mongos:

```
mongodb://localhost:27017/?directConnection=false
```

Importante:

- Conectarse siempre al puerto del mongos (27017 en nuestro caso)
- NO conectarse directamente a los shards
- La opción `directConnection=false` es importante porque permite que el cliente se comunique con todo el cluster.

(slide 8–9)

### Habilitar sharding y monitorear el estado

5. Habilitar sharding en una base de datos:

Finalmente, puedes habilitar el sharding en una base de datos. Por ejemplo, para la base de datos `ecommerce`:

```javascript
use ecommerce
sh.enableSharding("ecommerce")
```

También puedes shardear una colección dentro de la base de datos, definiendo una clave shard:

```javascript
sh.shardCollection("ecommerce.productos", { categoria: 1 })
```

Es recomendable que previamente se tenga creado un índice en la clave shard:

```javascript
db.productos.createIndex({ "categoria": 1 })
```

Ahora, puedes insertar productos en la colección:

```javascript
db.productos.insertMany([
  { "nombre": "Laptop", "categoria": "Electronics", "precio": 1200 },
  { "nombre": "Smartphone", "categoria": "Electronics", "precio": 800 },
  { "nombre": "Coffee Maker", "categoria": "Home Appliances", "precio": 150 },
  { "nombre": "Blender", "categoria": "Home Appliances", "precio": 100 },
  { "nombre": "Sofa", "categoria": "Furniture", "precio": 600 },
  { "nombre": "Dining Table", "categoria": "Furniture", "precio": 400 }
])
```

También es posible establecer el sharding basado en hash para distribuir los documentos uniformemente en el valor la clave.

```javascript
db.clientes.createIndex({ "email": "hashed" })
```

```javascript
sh.shardCollection("ecommerce.clientes", { "email": "hashed" })
```

6. Monitorear el estado del sharding:

Para ver el estado de tu clúster sharded y cómo se distribuyen los datos entre los shards, puedes usar el siguiente comando:

```javascript
sh.status()
```

Para ver la distribución de los datos en el sharding:

```javascript
db.productos.getShardDistribution()
```

(slide 9)

### Gestión de chunks

Si los datos no se reparten de forma automática, podemos forzarlo mediante las operaciones `sh.splitAt`, donde le indicamos el valor para dividir el fragmento en dos, y `sh.splitFind` que realiza la división por la mediana.

```javascript
sh.splitFind("twitter.tweets", {"date": 1})
sh.status()
```

Para ver el tamaño del chunk predeterminado (en MB)

```javascript
use config
db.settings.find({ "_id": "chunksize" })
```

Para modificar el tamaño del chunk (ejemplo: 8MB)

```javascript
use config
db.settings.updateOne(
  { _id: "chunksize" },
  { $set: { value: 8 } },
  { upsert: true }
)
```

(slide 10)

## Conclusión

Ahora tenemos un clúster MongoDB con Sharding y Replica Sets utilizando Docker. Esta configuración proporciona tanto replicación para alta disponibilidad y sharding para escalabilidad horizontal.

(slide 10)

## Glosario

- **Sharding:** Permite dividir los datos en diferentes servidores para manejar grandes cantidades de datos y mejorar la escalabilidad.
- **Mongos:** Es el enrutador que se comunica con las bases de datos sharded.
- **Config Servers:** Almacenan la metadata del clúster (información sobre los shards).
- **Shards:** Son los servidores donde se almacenan los datos. Cada shard puede ser un Replica Set para asegurar alta disponibilidad.
