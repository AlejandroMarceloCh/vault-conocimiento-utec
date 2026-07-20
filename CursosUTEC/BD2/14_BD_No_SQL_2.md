---
curso: BD2
titulo: 14 BD No SQL 2
slides: 57
fuente: 14 BD No SQL 2.pdf
---

# 14 BD No SQL 2

## Índice

- [Bases de Datos de Documentos](#bases-de-datos-de-documentos)
  - [Características](#caracteristicas)
  - [Ejemplos de JSON](#ejemplos-de-json)
  - [Casos de uso](#casos-de-uso)
  - [Productos](#productos)
  - [CouchBase](#couchbase)
  - [MongoDB](#mongodb)
- [Instalación y Configuración de MongoDB](#instalacion-y-configuracion-de-mongodb)
  - [Instalación con Docker y Compass](#instalacion-con-docker-y-compass)
  - [MongoDB Atlas](#mongodb-atlas)
- [Estructura de MongoDB](#estructura-de-mongodb)
  - [Bases de datos, colecciones y documentos](#bases-de-datos-colecciones-y-documentos)
  - [Actividad](#actividad)
- [Operaciones CRUD en MongoDB](#operaciones-crud-en-mongodb)
  - [Insertar documentos](#insertar-documentos)
  - [Actualizar documentos](#actualizar-documentos)
  - [Actividad](#actividad)
  - [Eliminar documentos](#eliminar-documentos)
  - [Filtrado de datos](#filtrado-de-datos)
  - [Proyección de campos](#proyeccion-de-campos)
  - [Operadores lógicos y de comparación](#operadores-logicos-y-de-comparacion)
  - [Actividad](#actividad)
- [Comandos Avanzados en MongoDB](#comandos-avanzados-en-mongodb)
  - [Ordenar](#ordenar)
  - [Agregaciones](#agregaciones)
  - [Consultas en documentos anidados](#consultas-en-documentos-anidados)
  - [Consulta de elementos de un array](#consulta-de-elementos-de-un-array)
  - [Consultas de rango de fechas](#consultas-de-rango-de-fechas)
  - [Búsqueda textual](#busqueda-textual)
  - [Actividad](#actividad)
- [PyMongo: Conexión y CRUD con Python](#pymongo-conexion-y-crud-con-python)
  - [Conexión a MongoDB](#conexion-a-mongodb)
  - [Insertar documentos con Python](#insertar-documentos-con-python)
  - [Consultar documentos con Python](#consultar-documentos-con-python)
  - [Actualizar documentos con Python](#actualizar-documentos-con-python)
  - [Eliminar documentos con Python](#eliminar-documentos-con-python)
  - [Filtros avanzados y agregaciones con Python](#filtros-avanzados-y-agregaciones-con-python)
- [Indexación en MongoDB](#indexacion-en-mongodb)
  - [Concepto de indexación](#concepto-de-indexacion)
  - [Índices B+ Tree](#indices-b-tree)
  - [Llave primaria e índice de un solo campo](#llave-primaria-e-indice-de-un-solo-campo)
  - [Índice compuesto](#indice-compuesto)
  - [Índice Multikey](#indice-multikey)
  - [Índice único, consultar y eliminar índices](#indice-unico-consultar-y-eliminar-indices)
  - [Actividad](#actividad)
- [Alta Disponibilidad y Replicación](#alta-disponibilidad-y-replicacion)
  - [Falla física del sistema de BD](#falla-fisica-del-sistema-de-bd)
  - [MongoDB ReplicaSet](#mongodb-replicaset)
- [Escalabilidad](#escalabilidad)
  - [Escalamiento vertical y horizontal](#escalamiento-vertical-y-horizontal)
  - [Partición horizontal](#particion-horizontal)
  - [MongoDB Sharding](#mongodb-sharding)
- [Glosario](#glosario)

## Bases de Datos de Documentos

### Características

Características:
- Modelo basado en documentos: Almacenan datos en formato JSON, BSON o XML en lugar de tablas tradicionales.
- Estructura flexible: No requieren un esquema fijo, lo que permite cambios sin afectar toda la base de datos.
- Escalabilidad horizontal: Diseñadas para manejar grandes volúmenes de datos distribuidos.
- Alta velocidad de lectura/escritura: Son más eficientes en consultas sobre documentos específicos.
- Indexación avanzada: Permiten búsquedas rápidas dentro de documentos sin la complejidad de múltiples relaciones.
- Integración con APIs modernas: Ideales para aplicaciones web y móviles que trabajan con datos dinámicos.

```json
{
  "_id": "5cf0029caff5056591b0ce7d",
  "firstname": "Jane",
  "lastname": "Wu",
  "address": {
    "street": "1 Circle Rd",
    "city": "Los Angeles",
    "state": "CA",
    "zip": "90404"
  },
  "hobbies": ["surfing", "coding"]
}
```

**Figura:** En la parte superior derecha, un recuadro con borde azul claro muestra un documento JSON de ejemplo con campos `_id`, `firstname`, `lastname`, un objeto anidado `address` (street, city, state, zip) y un arreglo `hobbies`. En la parte inferior derecha, diagrama de escalabilidad horizontal: en la parte superior, un icono grande azul representa «Collection A» con tamaño total de 1 TB; cuatro flechas descendentes conectan con cuatro cajas teal etiquetadas «Shard A», «Shard B», «Shard C» y «Shard D», cada una con 250 GB, mostrando la partición de la colección en cuatro fragmentos iguales.

(slide 3)

### Ejemplos de JSON

Ejemplos de JSON

```json
{
  "nombre": "Juan",
  "edad": 30,
  "ciudad": "Madrid",
  "profesión": "Ingeniero"
}
```

```json
{
  "persona": {
    "nombre": "Ana",
    "edad": 28,
    "dirección": {
      "calle": "Gran Vía",
      "número": 12,
      "ciudad": "Barcelona"
    },
    "contacto": {
      "teléfono": "123456789",
      "email": "ana@email.com"
    }
  }
}
```

```json
{
  "texto_id": 101,
  "contenido": "La inteligencia artificial está revolucionando el mundo.",
  "autor": "Heider",
  "fecha_creacion": "2025-04-07",
  "categoria": "Tecnología",
  "idioma": "es",
  "embedding": [0.21, -0.45, 0.78, 0.36, -0.12, 0.67, -0.34, 0.89]
}
```

**Figura:** Tres bloques de código JSON dispuestos en paralelo sobre fondo gris claro. Bloque izquierdo: objeto plano con nombre, edad, ciudad y profesión. Bloque central: objeto con estructura anidada `persona` que contiene dirección y contacto. Bloque derecho: documento con metadatos (texto_id, contenido, autor, fecha_creacion, categoria, idioma) y un arreglo numérico `embedding` de 8 valores. Resaltado de sintaxis: claves y cadenas en rojo, números en verde.

(slide 4)

### Casos de uso

Algunos casos de uso:
- Aplicaciones web y móviles: Almacenan datos JSON para APIs y sistemas dinámicos. Soportan sincronización rápida y acceso eficiente a datos para apps con alta interacción.
- E-Commerce: Permite almacenar productos con atributos variables (colores, tallas, precios, etc.) sin esquema fijo.
- Sistemas de gestión de contenido (CMS): Flexibilidad en almacenamiento de artículos, páginas o bloques con estructuras flexibles.
- Redes sociales: Manejo de publicaciones, perfiles de usuario, historiales y mensajes con estructuras anidadas y dinámicas.
- Big Data y analítica: Procesamiento eficiente de grandes volúmenes de información.
- Inteligencia artificial: Almacenamiento de datasets para machine learning.

**Figura:** En el lado derecho de la slide, tres conjuntos de iconos ilustrativos. Arriba: pantalla de laptop con un globo azul junto a un smartphone con imagen de paisaje, representando aplicaciones web y móviles. En el centro: icono de tienda azul y blanca con monitor, bolsa de compras y monedas doradas, representando E-Commerce.

(slide 5)

### Productos

| Base de Datos | Año de Creación | Empresa | Escalabilidad | Características claves | Casos de Uso |
|---|---|---|---|---|---|
| MongoDB | 2009 | MongoDB Inc. | Escalabilidad horizontal con sharding y replicación | JSON/BSON, agregaciones, índices avanzados, Atlas (DBaaS) | Aplicaciones web, catálogos, IoT, sistemas CRM |
| CouchBase | 2010 | Couchbase Inc. | Escalabilidad horizontal nativa | Motor híbrido memoria-disco, N1QL (SQL-like), indexación flexible | Aplicaciones en tiempo real, móviles, analítica |
| Amazon DocumentDB | 2019 | Amazon Web Services | Escalabilidad automática en la nube (AWS) | Compatible con API de MongoDB, servicio gestionado, cifrado integrado | Aplicaciones en AWS, reemplazo de MongoDB |
| Firebase Firestore | 2017 | Google (Alphabet) | Escalabilidad automática global (multi-region) | Realtime updates, sincronización, SDKs móviles, almacenamiento cloud-native | Aplicaciones móviles, chats, apps colaborativas |

**Figura:** Tabla comparativa de cuatro bases de datos orientadas a documentos con seis columnas y cuatro filas de datos.

(slide 6)

### CouchBase

Sync | Couchbase Docs

**Figura:** Diagrama de arquitectura de Couchbase dividido en dos secciones. Sección superior — entornos cliente: a la izquierda, icono de laptop conectado a caja «APPLICATION SERVER» que contiene recuadro rojo «CLIENT LIBRARY», con línea punteada hacia la capa inferior; al centro, icono de desktop con la misma estructura (APPLICATION SERVER → CLIENT LIBRARY); a la derecha, iconos de tablet y smartphone (con símbolo de base de datos local en cada dispositivo) conectados mediante líneas punteadas rojas a dos cajas «SYNC GATEWAY» (cada una con icono circular de sincronización). Sección inferior — capa de base de datos: caja horizontal grande con cuatro cilindros rojos de base de datos en fila, con puntos suspensivos («...») entre el tercero y el cuarto indicando un clúster escalable; etiqueta inferior «Sync | Couchbase Docs». Las líneas punteadas rojas representan las rutas de comunicación entre componentes y el clúster.

(slide 7)

### MongoDB

- MongoDB es una base de datos NoSQL orientada a documentos, de código abierto, que almacena datos en formato BSON (una extensión de JSON).
- Fue diseñada para ofrecer alta escalabilidad, flexibilidad y rendimiento.
- Características claves:
  - Altamente escalable: soporta sharding y replicación
  - Consultas avanzadas con agregaciones y filtros
  - Índices personalizados y de texto completo

**Figura:** Título «BD de Documentos : MongoDB» en la parte superior. Términos clave resaltados en negrita: «BSON», «escalabilidad», «flexibilidad», «rendimiento», y los encabezados de características.

Modelo de Datos

```json
{
  "name": "Rubén Terceño",
  "title": "Senior Solutions Architect",
  "employee_number": 653,
  "location": {
    "type": "Point",
    "coordinates": [ 43.34, -3.26 ]
  },
  "expertise": [ "MongoDB", "Java", "Geospatial" ],
  "address": {
    "address1": "Rutilo 11",
    "address2": "Piso 1, Oficina 2",
    "zipcode": "28041"
  }
}
```

**Figura:** Documento JSON central con anotaciones mediante flechas azules y etiquetas. A la izquierda, etiqueta «Campos» con flechas apuntando a las claves `name`, `employee_number` y `address`. A la derecha, etiqueta «Tipo de Datos» con flechas: «string» apunta al valor `"Rubén Terceño"`, «number» apunta al valor `653`, «Geo-location» apunta al objeto `location` con `type` y `coordinates`. En la parte inferior derecha, etiqueta «Sub documentos» con corchete agrupando los campos internos del objeto `address` (`address1`, `address2`, `zipcode`).

(slides 8–9)

## Instalación y Configuración de MongoDB

### Instalación con Docker y Compass

- Instalación con Docker

```bash
docker pull mongo
```

- Levantar el contenedor

```bash
docker run --name mongo -d -p 27017:27017 mongo
```

- Descargar e instalar MongoDb Compass

https://www.mongodb.com/try/download/compass

**Figura:** Captura de pantalla de la interfaz «New Connection» de MongoDB Compass en la parte inferior derecha. Muestra el campo URI con valor `mongodb://localhost:27017/`, campos vacíos para «Name» y «Color», casilla «Favorite this connection», menú desplegable «Advanced Connection Options», y cajas de ayuda a la derecha sobre cadenas de conexión en Atlas y formato de connection strings.

(slide 10)

### MongoDB Atlas

Crear un servicio de MongoDB en la nube con Atlas

1. Después de configurar la Organización y el Proyecto, proceder a crear un Cluster gratuito.
2. En el apartado SECURITY\Network Access agregar 0.0.0.0/0 para permitir acceso desde cualquier IP.

**Figura:** Texto descriptivo: «Atlas only allows client connections to a cluster from entries in the project's IP Access List. Each entry should either be a single IP address or a CIDR-notated range of addresses.» Botones superiores: «ADD CURRENT IP ADDRESS» y «ALLOW ACCESS FROM ANYWHERE». Campo «Access List Entry» con valor `0.0.0.0/0`. Campo «Comment» con valor «Permitir Cualquier IP». Interruptor «This entry is temporary and will be deleted in» configurado en «6 hours» (apagado). Botones inferiores: «Cancel» y «Confirm» (verde).

Crear un servicio de MongoDB en la nube con Atlas

3. Configurar la conexión con cualquier IDE y probar la conexión.

MongoDB Compass

```
mongodb+srv://<user>:<password>@<host>/
```

DBeaver (jdbc)

```
mongodb+srv://<user>:<password>@<host>/admin?authSource=admin&retryWrites=true
```

**Figura:** Slide con las plantillas de cadena de conexión para MongoDB Compass (en texto azul monoespaciado) y DBeaver JDBC (en texto negro monoespaciado).

(slides 11–12)

## Estructura de MongoDB

### Bases de datos, colecciones y documentos

Crear una base de datos

```javascript
use miBaseDeDatos
```

Crear una colección

```javascript
db.createCollection("miColeccion")
```

Crear un documento

```javascript
db.miColeccion.insertOne(
{nombre: "Juan", edad: 30})
```

| MongoDB | SQL |
|---|---|
| Base de Datos | Base de Datos |
| Colecciones | Tablas |
| Documentos | Filas (registros) |
| Campos | Columnas |

**Figura:** Lado izquierdo: tres bloques de comandos MongoDB para crear base de datos, colección y documento. Lado derecho: tabla comparativa de terminología con cuatro filas; las etiquetas de MongoDB aparecen en recuadros naranjas y las de SQL en recuadros grises claros.

(slide 13)

### Actividad

Actividad
- Instalar y configurar un servidor MongoDB.
- Crear una base de datos llamada ecommerce y tres colecciones: productos, clientes y pedidos.

**Figura:** Recuadro con encabezado azul oscuro «Actividad» que contiene dos bullets con las tareas indicadas. Título «BD de Documentos: Estructura de MongoDB» en la parte superior.

(slide 14)

## Operaciones CRUD en MongoDB

### Insertar documentos

Insertar documentos:

Se utiliza los comandos insertOne() para insertar un solo documento y insertMany() para insertar varios documentos. Ejemplo:

```javascript
db.productos.insertOne({ "nombre": "Laptop", "precio": 1500, "categoria": "Electrónica" })
```

```javascript
db.productos.insertMany([ { "nombre": "Smartphone", "precio": 900, "categoria": "Electrónica" }, { "nombre": "Audifonos", "precio": 100, "categoria": "Accesorios" } ])
```

**Figura:** Bloque de código con borde azul claro que contiene los dos comandos de inserción. Resaltado de sintaxis: cadenas en rojo/naranja, números en verde.

(slide 15)

### Actualizar documentos

Actualizar documentos:

Se utiliza updateOne(), updateMany(), y operadores como $set y $inc de la siguiente manera:

```javascript
db.productos.updateOne({ "nombre": "Laptop" }, { $set: { "precio": 1400 } })
db.productos.updateMany({ "categoria": "Electrónica" }, { $inc: { "precio": 100 } })
```

El operador $inc incrementa o decrementa el valor numérico de todos los elementos que coinciden con el filtro aplicado.

**Figura:** Bloque de código con borde azul claro con dos comandos de actualización. Resaltado de sintaxis: claves y operadores en rojo/marrón, cadenas en naranja, valores numéricos en verde. Texto explicativo del operador `$inc` debajo del bloque.

(slide 16)

### Actividad

Actividad
- Insertar algunos productos con diferentes categorías y precios.
- Utilizar como ejemplo el archivo "productos.json" proporcionado por el docente.
- Incrementa en 10% el descuento de los productos de categoría "hogar".
- Agregar un nuevo campo a los televisores: {SistemaOperativo : "Android TV"}

**Figura:** Recuadro con encabezado azul oscuro «Actividad» que contiene cuatro bullets con las tareas indicadas. Título «BD de Documentos : CRUD» en la parte superior.

(slide 17)

### Eliminar documentos

Eliminar documentos:

Se utiliza deleteOne() y deleteMany() de la siguiente manera:

```javascript
db.productos.deleteOne({ "nombre": "Audifonos" })
db.productos.deleteMany({ "categoria": "Accesorios" })
```

**Figura:** Bloque de código con fondo gris claro que contiene los dos comandos de eliminación. Cadenas resaltadas en rojo.

(slide 18)

### Filtrado de datos

Filtrado de datos:

Se utiliza find(), findOne() para aplicar filtros.

```javascript
db.productos.find({ "categoria": "Electrónica" })
db.productos.findOne({ "nombre": "Laptop" })
```

**Figura:** Bloque de código con fondo gris claro que contiene los dos comandos de filtrado.

(slide 19)

### Proyección de campos

Proyección de campos:

Si solo desea mostrar algunos campos se le agrega un segundo parámetro al find:

```javascript
db.productos.find({}, {"nombre": 1, "categoria": 1 })
```

```javascript
db.productos.find({ "categoria": "Electrónica" },{ "stock": 0 })
```

- Esto último excluye "stock" pero muestra todos los demás campos.

**Figura:** Bloque de código con fondo gris claro que contiene dos ejemplos de proyección de campos: inclusión explícita (`nombre` y `categoria` con valor 1) y exclusión (`stock` con valor 0). Bullet explicativo debajo del bloque.

(slide 20)

### Operadores lógicos y de comparación

Operadores lógicos y de comparación:

Los operadores se utilizan dentro de un objeto de consulta en el método find para especificar criterios de búsqueda. Se puede combinar múltiples operadores para crear consultas más complejas

Ejemplo 1: consulta productos que son electrónicos o cuyo precio es mayor a 500.

Ejemplo 2: Consulta productos cuya categoría sea "Electrónica" o "Hogar".

```javascript
db.productos.find({
  $or: [
    { categoria: "Electrónica" },
    { precio: { $gt: 500 } }
  ]
})
```

```javascript
db.productos.find({
  categoria: {
    $in: ["Electrónica", "Hogar"]
  }
})
```

**Figura:** Slide con título «BD de Documentos : CRUD» y subtítulo «Operadores lógicos y de comparación:». Dos bloques de código dispuestos en paralelo (izquierda y derecha), cada uno precedido por su enunciado de ejemplo. El bloque izquierdo usa el operador `$or` con `$gt`; el bloque derecho usa `$in` sobre el campo `categoria`.

Operadores lógicos y de comparación:

| Operador | Descripción | Ejemplo de uso |
|---|---|---|
| $eq | Igual a. | `{ "edad": { "$eq": 30 } }` |
| $ne | No igual a. | `{ "edad": { "$ne": 30 } }` |
| $gt | Mayor que. | `{ "edad": { "$gt": 30 } }` |
| $gte | Mayor o igual que. | `{ "edad": { "$gte": 30 } }` |
| $lt | Menor que. | `{ "edad": { "$lt": 30 } }` |
| $lte | Menor o igual que. | `{ "edad": { "$lte": 30 } }` |
| $in | Está en una lista de valores. | `{ "edad": { "$in": [25, 30, 35] } }` |
| $nin | No está en una lista de valores. | `{ "edad": { "$nin": [25, 30, 35] } }` |
| $and | Lógica "y" para combinar condiciones. | `{ "$and": [{ "edad": { "$gt": 20 } }, { "edad": { "$lt": 40 } }] }` |
| $or | Lógica "o" para combinar condiciones. | `{ "$or": [{ "edad": { "$lt": 20 } }, { "edad": { "$gt": 40 } }] }` |
| $not | Niega una condición. | `{ "edad": { "$not": { "$gt": 30 } } }` |
| $exists | Verifica si un campo existe. | `{ "nombre": { "$exists": true } }` |

**Figura:** Tabla de tres columnas (Operador, Descripción, Ejemplo de uso) con 12 filas de operadores de consulta. Título «BD Clave-Valor: Comandos REDIS» y subtítulo «Operadores lógicos y de comparación:».

(slides 21–22)

### Actividad

Actividad

- Mostrar los productos sin stock
- Mostrar los productos con calificación mayor a 4.5
- Buscar productos con precio entre 700 y 900

**Figura:** Recuadro con encabezado azul «Actividad» que contiene tres bullets con las tareas indicadas. Título «BD de Documentos : CRUD» en la parte superior.

(slide 23)

## Comandos Avanzados en MongoDB

### Ordenar

Ordenar:

```javascript
//Ordenar de menor a mayor
db.productos.find({ categoria: "Electrónica" }).sort({ precio: 1 })

//Ordenar de mayor a menor
db.productos.find({ categoria: "Electrónica" }).sort({ precio: -1 })
```

**Figura:** Bloque de código con resaltado de sintaxis (comentarios en verde, campos en rojo, métodos en negro) dentro de un recuadro gris claro. Subtítulo «Ordenar:» seguido de dos ejemplos de ordenamiento ascendente (`precio: 1`) y descendente (`precio: -1`).

(slide 24)

### Agregaciones

Agregaciones:

```javascript
//Contar todos los documentos de una colección.
db.productos.aggregate({$count: "total"})

//Contar todos los productos de una categoria especifica.
db.productos.aggregate([
  { $match: { categoria: "Electrónica" } },
  { $count: "total" } ])

//Contar el total productos y sumar los precios agrupados por categoria.
//Mostrar el resultado ordenado por el total.
db.productos.aggregate([
  { $group: { _id: "$categoria",
              conteo: { $sum: 1 },
              sumaPrecio: { $sum: "$precio" } } },
  { $sort: {conteo: 1}} ])
```

**Figura:** Bloque de código con tres ejemplos de agregación en MongoDB: conteo total, conteo con `$match`, y agrupación con `$group` y `$sort`. Comentarios en verde, operadores de agregación en azul/morado, cadenas en rojo.

(slide 25)

### Consultas en documentos anidados

Consultas en documentos anidados:

Los documentos pueden contener otros documentos o arrays como parte de su estructura. Para consultar información dentro de documentos anidados se usa dot notation.

```javascript
db.productos.insertOne({
  "nombre": "Laptop",
  "categoria": "Electrónica",
  "detalles": {
    "fabricante": "Lenovo",
    "modelo": "XYZ-2019",
    "garantia": "2 años"
  }
})
//Consultar dentro de documentos anidados.
db.productos.find({ "detalles.fabricante": "Lenovo" })
```

**Figura:** Texto explicativo sobre dot notation seguido de un bloque de código con `insertOne` (documento con objeto anidado `detalles`) y `find` usando notación de punto `detalles.fabricante`.

(slide 26)

### Consulta de elementos de un array

Consulta de elementos de un array:

Busca documentos que contengan un valor específico dentro de un array.

```javascript
//Consulta productos que tengan "Pantalla táctil" en su lista de características.
db.productos.find({
  caracteristicas: "Pantalla táctil"
})

//Encuentra productos cuyo primer elemento en el array "características"
//sea "Cámara de 64MP".
db.productos.find({
  "caracteristicas.0": "Cámara de 64MP"
})
```

**Figura:** Dos ejemplos de consulta en bloque de código gris claro: búsqueda de valor en array y búsqueda por índice de array (`caracteristicas.0`).

(slide 27)

### Consultas de rango de fechas

Consultas de rango de fechas:

Ejemplo: Consulta productos lanzados entre el 1 de enero de 2023 y el 1 de enero de 2024.

```javascript
db.productos.find({
  fecha_lanzamiento: {
    $gte: ISODate("2023-01-01"),
    $lt:   ISODate("2024-01-01")
  }
})
```

**Figura:** Subtítulo «Consultas de rango de fechas:» con enunciado de ejemplo y bloque de código que usa `$gte` y `$lt` con `ISODate`.

(slide 28)

### Búsqueda textual

MongoDB soporta la búsqueda de texto completo con índices textuales. Para habilitarlo, necesitas crear un índice textual (text)

```javascript
db.productos.createIndex({ descripcion: "text" })
```

Consulta: Busca productos que contengan la palabra "Smart" en la descripción.

```javascript
db.productos.find({ $text: { $search: "Smart" } })

db.productos.find({ $text: { $search: "táctil led 4k" } })
```

Ordenar por relevancia: encontrar los documentos más relevantes que coincidan con todas las palabras clave proporcionadas.

```javascript
db.productos.find({ $text: { $search: "pulgadas" } })
            .sort({ score: { $meta: "textScore" } })
```

**Figura:** Tres secciones con bloques de código: creación de índice textual, consultas `$text`/`$search`, y ordenamiento por relevancia con `$meta: "textScore"`.

(slide 29)

### Actividad

Actividad

- Consultar el número total de productos agrupados por marca.
- Mostrar los 10 productos más recientes de acuerdo a su fecha de lanzamiento.
- Buscar los productos cuya descripción mencione RAM y CPU.

**Figura:** Recuadro con encabezado azul «Actividad» con tres bullets de tareas. Título «BD de Documentos : Comandos Avanzados».

(slide 30)

## PyMongo: Conexión y CRUD con Python

### Conexión a MongoDB

- Instalar la librería PyMongo con conda o pip:
  - `conda install pymongo`
- Crear un cliente que se conecte a MongoDB.
- Crear o seleccionar una base de datos y una colección.

```python
from pymongo import MongoClient

# Conexión a MongoDB en local
cliente = MongoClient('mongodb://localhost:27017/')
# Conexión a MongoDB en DeepNote
# cliente = MongoClient(os.environ["ATLAS_CONNECTION_STRING"])

# Crear o seleccionar una base de datos existente
base_datos = cliente['ecommerce'] # Se crea automáticamente si no existe

# Crear o seleccionar una colección
coleccion_productos = base_datos['productos']
```

**Figura:** Lista de tres bullets con instrucciones seguida de bloque de código Python para conexión local, conexión comentada a DeepNote/Atlas, selección de base de datos `ecommerce` y colección `productos`.

(slide 31)

### Insertar documentos con Python

Insertar documentos

```python
# Insertar un documento en la colección
nuevo_producto = {"nombre": "Portátil", "precio": 1500, "stock": 10}
coleccion_productos.insert_one(nuevo_producto)

# Insertar múltiples documentos
productos = [
    {"nombre": "Smartphone", "precio": 800, "stock": 50, "categoria": "Electrónica"},
    {"nombre": "Sillon", "precio": 1500, "stock": 2, "categoria": "Hogar"},
    {"nombre": "Camisa", "precio": 80, "stock": 50, "categoria": "Ropa"}
]
coleccion_productos.insert_many(productos)
```

**Figura:** Subtítulo «Insertar documentos» con dos bloques de código Python: `insert_one` para un documento y `insert_many` para una lista de tres productos.

(slide 32)

### Consultar documentos con Python

Consultar documentos

```python
# Leer un documento específico
producto = coleccion_productos.find_one({"nombre": "Portátil"})
print(producto)

# Leer todos los documentos con precio mayor a 1000
productos_caros = coleccion_productos.find({"precio": {"$gt": 1000}})
for producto in productos_caros:
   print(producto)
```

**Figura:** Subtítulo «Consultar documentos» con ejemplos de `find_one` y `find` con operador `$gt`, iterando resultados con un bucle `for`.

(slide 33)

### Actualizar documentos con Python

Actualizar documentos

```python
# Actualizar el stock de un producto
coleccion_productos.update_one({"nombre": "Portátil"},
                               {"$set": {"stock": 15}})

# Actualizar múltiples documentos
coleccion_productos.update_many({"precio": {"$lte": 100}},
                                {"$set": {"descuento": True}})
```

**Figura:** Subtítulo «Actualizar documentos» con ejemplos de `update_one` (campo `stock`) y `update_many` (campo `descuento` con filtro `$lte`).

(slide 34)

### Eliminar documentos con Python

Eliminar documentos

```python
# Eliminar un documento
coleccion_productos.delete_one({"nombre": "Portátil"})

# Eliminar múltiples documentos con stock bajo
coleccion_productos.delete_many({"stock": {"$lt": 5}})
```

**Figura:** Subtítulo «Eliminar documentos» con ejemplos de `delete_one` por nombre y `delete_many` con filtro de stock bajo (`$lt: 5`).

(slide 35)

### Filtros avanzados y agregaciones con Python

```python
# Productos cuyo precio esté entre 500 y 1000
productos_rango = coleccion_productos.find({"precio": {"$gte": 500, "$lte": 1000}})
for producto in productos_rango:
    print(producto)

# Productos que tengan 'Phone' en el nombre usando una expresión regular
consulta_regex = {"nombre": {"$regex": "/Phone/", "$options": "i"}} #*
productos_encontrados = coleccion_productos.find(consulta_regex)
for producto in productos_encontrados:
    print(producto)
```

**Figura:** Dos bloques de código Python: filtro por rango de precio con `$gte`/`$lte` y búsqueda con expresión regular `$regex` y `$options: "i"`, con marcador `#*` al final de la línea de `consulta_regex`.

Ejemplo de un pipeline de agregación para agrupar productos por categoría y contar cuántos hay en cada categoría:

```python
# Pipeline de agregación para contar productos por categoría
pipeline = [
     {"$group": {"_id": "$categoria", "total_productos": {"$sum": 1}}},
     {"$sort": {"total_productos": -1}}     # Ordenar de mayor a menor
]
resultados = coleccion_productos.aggregate(pipeline)
for resultado in resultados:
     print(resultado)
```

**Figura:** Texto introductorio seguido de bloque de código Python con pipeline de agregación (`$group` por categoría, `$sort` descendente por `total_productos`) y bucle de impresión de resultados.

(slides 36–37)

## Indexación en MongoDB

### Concepto de indexación

La indexación permite a MongoDB organizar los datos para realizar búsquedas más rápidas.

```javascript
db.users.find( { score: { "$lt": 30 } } ).sort( { score: -1 } )
```

Indexes - Database Manual v8.0 - MongoDB Docs

**Figura:** Diagrama que ilustra el uso de un índice en una consulta MongoDB. En la parte superior, código `db.users.find( { score: { "$lt": 30 } } ).sort( { score: -1 } )` con tres etiquetas señalando: «Collection» → `db.users.find(`, «Query Criteria» → `{ score: { "$lt": 30 } }`, «Sort order» → `.sort( { score: -1 } )`. Debajo, una barra horizontal azul etiquetada `{ score: 1 } Index` con marcadores `min`, `18`, `30`, `45`, `75`, `max`; un recuadro azul claro resalta el tramo desde `min` hasta `30` (correspondiente al criterio `$lt: 30`). En la parte inferior, una fila de documentos de la colección `users`: `{ score: 25, ... }`, `{ score: 56, ... }`, `{ score: 45, ... }`, `{ score: 75, ... }`, `{ score: 5, ... }`, `{ score: 40, ... }`, `{ score: 18, ... }`, `{ score: 30, ... }`. Flechas grises conectan los marcadores del índice con sus documentos correspondientes (p. ej. el marcador `18` apunta a `{ score: 18, ... }`, un punto entre `min` y `18` apunta a `{ score: 5, ... }`, un punto entre `18` y `30` apunta a `{ score: 25, ... }`). Pie de figura «Indexes - Database Manual v8.0 - MongoDB Docs».

(slide 39)

### Índices B+ Tree

MongoDB implementa principalmente índices B+ Tree para la mayoría de sus operaciones de indexación. Este tipo de índice permite búsquedas eficientes y ordenadas, ya que almacena los datos en una estructura de árbol balanceado.

**Figura:** Diagrama de un árbol B+ de tres niveles. Nivel raíz: un nodo con valor `13` y dos punteros (valores menores y mayores o iguales a 13). Nivel intermedio: nodo izquierdo con valores `9` y `11` (tres punteros hacia hojas) y nodo derecho con valor `16` (dos punteros hacia hojas). Nivel hoja (nodos verdes claros, enlazados horizontalmente con flechas de doble punta formando lista doblemente enlazada): `[1, 4]`, `[9, 10]`, `[11, 12]`, `[13, 15]`, `[16, 20, 25]`.

(slide 40)

### Llave primaria e índice de un solo campo

Tipos de Índices:

- Llave primaria:
  - MongoDB crea automáticamente un índice en el campo `_id` como llave primaria.

- Índice de un solo campo:
  - Se crea sobre un solo campo de un documento, permitiendo búsquedas rápidas en ese campo.

```javascript
db.user.createIndex({score: 1 })
```

**Figura:** En la parte superior derecha, una pila de tres rectángulos representa una colección de documentos; el documento superior muestra el campo `score: 30,`. En la parte inferior, una barra horizontal azul sólida representa el índice, etiquetada en la parte inferior como `{ score: 1 } Index`. A lo largo de la barra aparecen marcadores con los valores `min`, `18`, `30`, `45`, `75` y `max`. Una línea punteada vertical conecta el valor `30` del documento en la colección con el punto `30` en la barra del índice, ilustrando cómo el índice apunta a la ubicación de los datos según el valor del campo.

(slide 41)

### Índice compuesto

Tipos de Índices:

- Índice compuesto:
  - Se define sobre múltiples campos, mejorando el rendimiento de consultas que filtran por más de un criterio.

```javascript
// Crear índice
db.user.createIndex({ userid: 1, score: -1 })

// Aplicar consultas
db.user.find({ userid: 12345 }).sort({ score: -1 })
db.user.find({ userid: 12345, score: { $lt: 50 } })
db.user.find().sort({ userid: 1, score: -1 })
db.user.find({score: { $lt: 50 }, userid: 12345 })
db.user.find().sort({score: -1, userid: 1})
```

**Figura:** A la derecha, una representación de una colección de documentos donde un documento de ejemplo contiene campos como `{ score: 30, userid: ... }`. En la parte inferior, una barra horizontal azul representa el rango del índice de `min` a `max`, ilustrando el orden físico de los datos según el índice `{ userid: 1, score: -1 }`. Los datos se ordenan primariamente por `userid` (valores: `"aa1"`, `"ca2"`, `"nb1"`, `"xyz"`) y, para el `userid` duplicado `"ca2"`, secundariamente por `score` en orden descendente: `75`, luego `55`, luego `30`. Puntos específicos etiquetados debajo de la barra: `"aa1", 45`; `"ca2", 75`; `"ca2", 55`; `"ca2", 30`; `"nb1", 30`; `"xyz", 90`. Las dos últimas consultas (`db.user.find({ score: { $lt: 50 }, userid: 12345 })` y `db.user.find().sort({score: -1, userid: 1})`) aparecen resaltadas en texto rojo.

(slide 42)

### Índice Multikey

Tipos de Índices:

- Índice Multikey:
  - MongoDB permite la creación de índices para arrays o campos embebidos.

```javascript
// Crear índice
db.user.createIndex({ "addr.zip": 1})

// Aplicar consultas
db.user.find({ "addr.zip": "78610" })

db.user.find().sort({ "addr.zip": 1 })

db.user.find({ "addr.zip": { $gte: "10000", $lte: "20000" } })
```

**Figura:** A la derecha, una representación visual de un documento en una colección con la siguiente estructura:

```json
{
  "userid": "xyz",
  "addr": [
    { "zip": "10036", ... },
    { "zip": "94301", ... }
  ]
}
```

Esto ilustra un documento que contiene un array (`addr`) de objetos embebidos, donde cada objeto tiene un campo `zip`. En la parte inferior, una barra horizontal azul representa el almacenamiento del índice, mostrando cómo los valores de diferentes documentos y dentro de arrays se ordenan. Etiquetas en la línea de tiempo de izquierda a derecha: `min`, `"10036"`, `"78610"`, `"94301"`, `max`. Etiqueta debajo de la barra: `{ "addr.zip": 1 } Index`. Esto muestra que el índice Multikey extrae valores del array `addr` (como `"10036"` y `"94301"`) y los coloca individualmente en el índice ordenado.

(slide 43)

### Índice único, consultar y eliminar índices

Tipos de Índices:

- Índice de Campo Único (UNIQUE):
  - Estos índices aseguran que los valores en un campo (o combinación de campos) sean únicos en toda la colección.

```javascript
db.users.createIndex({ dni: 1 }, { unique: true })
```

- Consultar Índices:

```javascript
db.productos.getIndexes()
```

- Eliminar un índice:

```javascript
db.users.dropIndex("nombre_del_indice")
```

**Figura:** El título «Indexación en MongoDB» en la parte superior. Sección «Tipos de Índices:» seguida de tres subsecciones con viñetas: «Índice de Campo Único (UNIQUE)», «Consultar Índices» y «Eliminar un índice», cada una con su ejemplo de código en sintaxis de MongoDB shell.

(slide 44)

### Actividad

Actividad

- Sobre la tabla de pedidos y productos realizar las siguientes consultas frecuentes y proponer una indexación para que una mayor eficiencia:
  - Buscar pedidos de un cliente en un rango de fechas específico.
  - Retornar los productos electrónicos lanzados en 2023 con precio entre 500 y 1500.

**Figura:** Slide con título «Indexación en MongoDB» en texto gris en la parte superior izquierda. El contenido principal está dentro de un rectángulo blanco redondeado con una barra de encabezado azul oscuro etiquetada «Actividad». Dentro del recuadro, la instrucción principal y dos tareas con viñetas (marcadores cuadrados).

(slide 45)

## Alta Disponibilidad y Replicación

### Falla física del sistema de BD

¿Que hacemos ante una falla física del Sistema de BD?

**Figura:** Título en rojo en la parte superior: «¿Que hacemos ante una falla física del Sistema de BD?». Diagrama centrado en una falla de base de datos:

1. **Interacción de usuario (centro superior):** Un icono de una persona con un monitor de computadora y un smartphone. Una flecha azul apunta hacia abajo desde este icono hacia la base de datos primaria, representando que los usuarios acceden al sistema.
2. **Base de datos primaria (centro inferior):** Un icono grande de tres cilindros grises apilados (representando una base de datos). Una **X roja** grande está superpuesta sobre ella, indicando una falla física de este sistema.
3. **Recuperación/Backup (izquierda):** Una flecha azul apunta desde la base de datos central hacia un icono a la izquierda que representa un disco duro externo con una flecha circular de «refresh» o «backup», sugiriendo un proceso de recuperación por backup.
4. **Replicación (derecha):** Una flecha azul etiquetada «**REPLICATION**» apunta desde la base de datos central hacia un grupo de tres iconos de bases de datos más pequeños, representando el concepto de usar replica sets o nodos distribuidos para mantener la disponibilidad durante una falla del primario.

(slide 46)

### MongoDB ReplicaSet

**Figura:** Diagrama de arquitectura de un Replica Set de MongoDB con tres nodos:

- **Nodo Primary (centro superior):** Caja rectangular azul etiquetada «Primary» con un icono de cilindro de base de datos encima. Es el destino de una flecha azul entrante desde la derecha, etiquetada «**DRIVER**», que se origina en iconos que representan un usuario y sus dispositivos (monitor de computadora y smartphone). Esto indica que las operaciones de escritura de la aplicación se dirigen al nodo Primary.

- **Nodos Secondary (inferior izquierda e inferior derecha):** Dos nodos representados por cajas rectangulares verdes etiquetadas «Secondary», cada una con su icono de cilindro de base de datos correspondiente. Flechas azules gruesas apuntan desde el nodo «Primary» hacia abajo a cada nodo «Secondary», etiquetadas «**Replication**», mostrando que los datos se copian del Primary a los Secondaries.

- **Comunicación interna (Heartbeat):** Flechas negras de doble sentido conectan los tres nodos en forma triangular. La flecha horizontal entre los dos nodos Secondary está etiquetada «**Heartbeat**», representando la comunicación constante entre nodos para monitorear salud y disponibilidad.

Título «MongoDB: ReplicaSet» en fuente sans-serif gris grande en la parte superior. Elemento triangular azul en la esquina superior izquierda.

**Figura:** Diagrama técnico que ilustra la arquitectura y comunicación dentro de un Replica Set de MongoDB:

- **Capa de aplicación (superior):** Una caja rectangular blanca grande etiquetada «**APPLICATION**». Dentro de esta caja hay un rectángulo más pequeño con borde oscuro etiquetado «**MongoDB Driver**».

- **Conexión:** Una flecha negra sólida apunta hacia abajo desde el «MongoDB Driver» hacia el «Replica Set» de abajo.

- **Replica Set:** Un rectángulo redondeado verde claro contiene tres cajas redondeadas verdes más oscuras, cada una representando una instancia de MongoDB (`mongod`), dispuestas verticalmente:
  - La caja superior está etiquetada «**mongod Secondary**».
  - La caja del medio está etiquetada «**mongod Primary**». La flecha del driver de la aplicación apunta directamente a este nodo Primary.
  - La caja inferior está etiquetada «**mongod Secondary**».
  - Todo el grupo está etiquetado «**Replica Set**» en su lado izquierdo.

- **Procesos inter-nodo:**
  - **Heartbeat:** A la derecha, un globo de diálogo etiquetado «Heartbeat» está conectado al Primary y a ambos nodos Secondary mediante flechas de doble sentido, indicando verificaciones de salud bidireccionales constantes entre todos los miembros.
  - **Oplog replication:** A la izquierda, un globo de diálogo etiquetado «Oplog replication» tiene flechas que apuntan desde el nodo «mongod Primary» hacia ambos nodos «mongod Secondary» (superior e inferior), representando el flujo de replicación de datos del primario a los secundarios.

Título «MongoDB: ReplicaSet» en texto gris oscuro grande en la parte superior izquierda.

(slides 47–48)

## Escalabilidad

### Escalamiento vertical y horizontal

**Figura:** Slide dividida en dos secciones que comparan visualmente dos tipos de escalamiento:

### Escalamiento vertical (Scaling up) — Lado izquierdo

- **Visual:** Muestra dos racks de servidores. Un servidor más pequeño está al frente y un servidor significativamente más grande y alto está detrás.
- **Indicador:** Una flecha naranja apunta **hacia arriba** junto a los servidores.
- **Etiquetas:** Junto a la flecha ascendente aparecen tres etiquetas: **RAM**, **CPU** e **I/O**.
- **Concepto:** Ilustra aumentar la capacidad de una sola máquina agregando hardware más potente (más memoria, procesadores más rápidos, mejor entrada/salida).

### Escalamiento horizontal (Scaling out) — Lado derecho

- **Visual:** Muestra tres racks de servidores idénticos de tamaño mediano dispuestos en fila horizontal.
- **Indicador:** Una flecha naranja larga apunta **horizontalmente hacia la derecha** debajo de la fila de servidores.
- **Etiquetas:** En la punta de la flecha horizontal, el texto «**NODOS**» seguido del logo de UTEC.
- **Concepto:** Ilustra aumentar la capacidad agregando más máquinas (nodos) al sistema, en lugar de hacer una sola máquina más grande.

Título «Escalabilidad» en la parte superior.

(slide 50)

### Partición horizontal

**Figura:** Diagrama que ilustra el concepto de partición horizontal (sharding), donde un conjunto de datos central se divide y distribuye entre tres servidores MongoDB según el valor del campo `"sede"`.

### Servidor central (`central.server.com`)

Contiene ocho objetos JSON, cada uno representando un empleado con los campos `"name"`, `"sede"` y `"cargo"`:

```json
{"name": "Juan Perez", "sede": "Arequipa", "cargo":"Cajero"}
{"name": "Ana Vera", "sede": "Trujillo", "cargo":"Secretaria"}
{"name": "Felipe Alvarado", "sede": "Lima", "cargo":"Almacenero"}
{"name": "Marta Sanchez", "sede": "Trujillo", "cargo":"Cajero"}
{"name": "Pedro Torres", "sede": "Lima", "cargo":"Jefe Operaciones"}
{"name": "Cecilia Paz", "sede": "Arequipa", "cargo":"Supervisor"}
{"name": "Carlos Perez", "sede": "Lima", "cargo":"Supervisor"}
{"name": "Maria Briceño", "sede": "Arequipa", "cargo":"Cajero"}
```

### Servidores particionados

Tres flechas apuntan desde los datos centrales hacia tres iconos de servidor en la parte inferior:

- **Servidor 1: `mongo1.server.com`** (criterio: `sede: "Arequipa"`):
  - `{"name": "Juan Perez", "sede": "Arequipa", "cargo":"Cajero"}`
  - `{"name": "Cecilia Paz", "sede": "Arequipa", "cargo":"Supervisor"}`
  - `{"name": "Maria Briceño", "sede": "Arequipa", "cargo":"Cajero"}`

- **Servidor 2: `mongo2.server.com`** (criterio: `sede: "Trujillo"`):
  - `{"name": "Ana Vera", "sede": "Trujillo", "cargo":"Secretaria"}`
  - `{"name": "Marta Sanchez", "sede": "Trujillo", "cargo":"Cajero"}`

- **Servidor 3: `mongo3.server.com`** (criterio: `sede: "Lima"`):
  - `{"name": "Felipe Alvarado", "sede": "Lima", "cargo":"Almacenero"}`
  - `{"name": "Pedro Torres", "sede": "Lima", "cargo":"Jefe Operaciones"}`
  - `{"name": "Carlos Perez", "sede": "Lima", "cargo":"Supervisor"}`

**Figura:** Diagrama de partición horizontal con un servidor de configuración central que enruta datos a tres instancias de base de datos.

### Servidor de configuración (`config.server.com`)

- **Icono:** Un icono de cilindro de base de datos etiquetado `config.server.com`.
- **Lógica de mapeo:** Una caja junto al icono contiene un mapeo tipo JSON que define qué servidor maneja qué ubicación:

```json
{
  mongo1: {"sede":"Arequipa"},
  mongo2: {"sede":"Trujillo"},
  mongo3: {"sede":"Lima"},
}
```

### Instancias shard y datos

Un corchete grande conecta el servidor de configuración superior con los tres servidores distribuidos inferiores:

- **`mongo1.server.com`** (maneja «Arequipa»):
  - `{"name": "Juan Perez", "sede": "Arequipa", "cargo":"Cajero"}`
  - `{"name": "Cecilia Paz", "sede": "Arequipa", "cargo":"Supervisor"}`
  - `{"name": "Maria Briceño", "sede": "Arequipa", "cargo":"Cajero"}`

- **`mongo2.server.com`** (maneja «Trujillo»):
  - `{"name": "Ana Vera", "sede": "Trujillo", "cargo":"Secretaria"}`
  - `{"name": "Marta Sanchez", "sede": "Trujillo", "cargo":"Cajero"}`

- **`mongo3.server.com`** (maneja «Lima»):
  - `{"name": "Felipe Alvarado", "sede": "Lima", "cargo":"Almacenero"}`
  - `{"name": "Pedro Torres", "sede": "Lima", "cargo":"Jefe Operaciones"}`
  - `{"name": "Carlos Perez", "sede": "Lima", "cargo":"Supervisor"}`

**Figura:** Diagrama de partición horizontal que muestra cómo un servidor de configuración central enruta consultas al shard correspondiente.

### Servidor de configuración (`config.server.com`)

- Ubicado en la parte superior central, representado por un icono de base de datos.
- Contiene una tabla de enrutamiento (mapa tipo JSON) que define qué shard almacena datos para cada ubicación (`sede`):
  - `mongo1: {"sede": "Arequipa"}`
  - `mongo2: {"sede": "Trujillo"}`
  - `mongo3: {"sede": "Lima"}` (la línea de `mongo3` está resaltada en gris)

### Flujo de consulta del cliente

- En la parte superior derecha, un icono de usuario y computadora representan un cliente enviando una consulta.
- Una flecha azul en forma de globo de diálogo muestra la consulta: `{"sede": "Lima"}`.
- Esta consulta apunta al mapa de configuración, específicamente a la entrada resaltada `mongo3`.
- Otra flecha azul apunta desde el mapa de configuración hacia abajo a la base de datos `mongo3.server.com`, mostrando cómo el sistema enruta la solicitud al shard correcto.

### Shards de base de datos (fila inferior)

- **`mongo1.server.com` (izquierda):** Documentos con `sede` «Arequipa»:
  - `{"name": "Juan Perez", "sede": "Arequipa", "cargo": "Cajero"}`
  - `{"name": "Cecilia Paz", "sede": "Arequipa", "cargo": "Supervisor"}`
  - `{"name": "Maria Briceño", "sede": "Arequipa", "cargo": "Cajero"}`

- **`mongo2.server.com` (centro):** Documentos con `sede` «Trujillo»:
  - `{"name": "Ana Vera", "sede": "Trujillo", "cargo": "Secretaria"}`
  - `{"name": "Marta Sanchez", "sede": "Trujillo", "cargo": "Cajero"}`

- **`mongo3.server.com` (derecha):** Documentos con `sede` «Lima»:
  - `{"name": "Felipe Alvarado", "sede": "Lima", "cargo": "Almacenero"}`
  - `{"name": "Pedro Torres", "sede": "Lima", "cargo": "Jefe Operaciones"}`
  - `{"name": "Carlos Perez", "sede": "Lima", "cargo": "Supervisor"}`

(slides 51–53)

### MongoDB Sharding

**Figura:** Diagrama arquitectónico central que ilustra el concepto de sharding en MongoDB, mostrando cómo una sola colección lógica de datos se particiona entre múltiples servidores físicos (shards).

### Componentes del diagrama

1. **Single Collection:** En la parte superior, una caja amplia representa una sola colección lógica de datos tal como la ve la aplicación.

2. **Lógica de distribución (rangos de clave):** Cinco flechas apuntan desde «Single Collection» hacia rangos numéricos específicos basados en una shard key:
   - **Key Range 0.. 20**
   - **Key Range 21.. 40**
   - **Key Range 41.. 60**
   - **Key Range 61.. 80**
   - **Key Range 81.. 100**

3. **Chunks:** Debajo de cada rango de clave, hay dos cajas pequeñas etiquetadas «**CHUNK**». Los chunks son subconjuntos de datos shardados.

4. **Shards:** Cada conjunto de chunks reside en un shard específico, representado por cajas azules grandes en la parte inferior:
   - **SHARD 0** (contiene el rango 0..20)
   - **SHARD 1** (contiene el rango 21..40)
   - **SHARD 2** (contiene el rango 41..60)
   - **SHARD 3** (contiene el rango 61..80)
   - **SHARD 4** (contiene el rango 81..100)

5. **Replica Sets:** Dentro de cada caja de shard, hay una caja más pequeña etiquetada «**Replica Set**», indicando que cada shard típicamente se implementa como un replica set para asegurar alta disponibilidad y redundancia de datos.

6. **Ejemplo de enrutamiento de datos:** Un icono de documento que contiene el dato `{ x: 87 }`. Una flecha apunta desde este documento hacia el **Key Range 81.. 100**, ilustrando que un documento con un valor de shard key de 87 será enrutado y almacenado en **SHARD 4**.

### (a) Hashed Sharding

**Figura (izquierda):** Tres documentos de ejemplo con valores `{ x : 25 }`, `{ x : 26 }` y `{ x : 27 }` pasan por una caja central naranja etiquetada «**Hash Function**». Desde esta caja, flechas apuntan a diferentes segmentos a lo largo de un eje horizontal dividido en **Chunk 1, Chunk 2, Chunk 3 y Chunk 4**:
- El valor `{ x : 26 }` se mapea a Chunk 1.
- El valor `{ x : 25 }` se mapea a Chunk 3.
- El valor `{ x : 27 }` se mapea a Chunk 4.
Esto demuestra que claves con valores cercanos pueden distribuirse a shards muy diferentes.

**Figura (derecha):** Ejemplo simplificado de la lógica de hashing:
- Documentos `{ X : 25 }`, `{ X : 26 }` y `{ X : 27 }` son procesados por una «**HashFunction**».
- Tres shards de destino mostrados como óvalos verdes:
  - **Chunk A:** Lógica `X % 3 = 1`. Documento `{ X : 25 }` (25 mod 3 = 1) se mapea aquí.
  - **Chunk B:** Lógica `X % 3 = 2`. Documento `{ X : 26 }` (26 mod 3 = 2) se mapea aquí.
  - **Chunk C:** Lógica `X % 3 = 0`. Documento `{ X : 27 }` (27 mod 3 = 0) se mapea aquí.

### (b) Ranged Sharding

**Figura (izquierda):** Una barra rectangular azul grande representa el «**Key Space for x**». La barra se divide en cuatro chunks basados en límites de valor específicos:
- **Chunk 1:** Rango de `{ x : minKey }` a `{ x : -75 }`.
- **Chunk 2:** Rango de `{ x : -75 }` a `{ x : 25 }`.
- **Chunk 3:** Rango de `{ x : 25 }` a `{ x : 175 }`.
- **Chunk 4:** Rango de `{ x : 175 }` a `{ x : maxKey }`.

**Figura (derecha):** Documentos específicos mapeados a shards según rangos definidos:
- **Shard A:** Rango `minKey <= X < 10`. Documento `{ X : 5 }` se mapea aquí.
- **Shard B:** Rango `10 <= X < 20`. Documento `{ X : 12 }` se mapea aquí.
- **Shard C:** Rango `20 <= X < maxKey`. Documento `{ X : 23 }` se mapea aquí.

**Figura:** Diagrama de arquitectura de un clúster MongoDB distribuido con sharding y replica sets:

### Capa de aplicación

- En la parte superior, una caja grande etiquetada «**APPLICATION**» contiene una caja más pequeña para el «**MongoDB Driver**».
- Una flecha indica que el driver de la aplicación se conecta directamente al router **mongos**.

### Capa de enrutamiento (mongos)

- Una caja azul etiquetada «**mongos 27017**» actúa como punto de entrada, usando el puerto **27017**.
- Tiene flechas direccionales apuntando tanto hacia los shards como hacia los servidores de configuración, indicando su rol en el enrutamiento de consultas y obtención de metadatos.

### Shards (almacenamiento de datos)

- Dos grupos de shards principales etiquetados **SHARD 1** y **SHARD 2**.
- Cada shard se representa como un **Replica Set** (indicado por un corchete vertical a la izquierda).
- Dentro de cada caja de shard hay tres sub-cajas etiquetadas «**mongod 27018**», indicando que cada shard está compuesto por tres instancias de datos MongoDB ejecutándose en el puerto **27018**.

### Config Servers

- A la derecha, una pila de tres cajas naranjas etiquetadas «**config 27019**».
- Ejecutan en el puerto **27019**.
- Flechas de doble sentido entre estas cajas indican que se comunican entre sí (formando su propio replica set para almacenar los metadatos del clúster).

(slides 54–56)

## Glosario

- **BSON:** Extensión de JSON en la que MongoDB almacena los datos.
- **Colección:** Equivalente en MongoDB a una tabla en SQL.
- **Documento:** Equivalente en MongoDB a una fila (registro) en SQL.
- **Campo:** Equivalente en MongoDB a una columna en SQL.
- **Dot notation:** Notación de punto para consultar información dentro de documentos anidados.
- **Índice B+ Tree:** Tipo de índice que MongoDB implementa principalmente; permite búsquedas eficientes y ordenadas almacenando los datos en una estructura de árbol balanceado.
- **Índice compuesto:** Índice definido sobre múltiples campos, que mejora el rendimiento de consultas que filtran por más de un criterio.
- **Índice Multikey:** Índice que MongoDB permite crear para arrays o campos embebidos.
- **Índice de Campo Único (UNIQUE):** Índice que asegura que los valores en un campo (o combinación de campos) sean únicos en toda la colección.
- **N1QL:** Lenguaje SQL-like de CouchBase.
- **Primary:** Nodo del Replica Set al que se dirigen las operaciones de escritura de la aplicación.
- **Secondary:** Nodo del Replica Set que recibe copias de los datos del Primary mediante replicación.
- **Heartbeat:** Comunicación constante entre nodos del Replica Set para monitorear salud y disponibilidad.
- **Oplog replication:** Flujo de replicación de datos del nodo Primary hacia los nodos Secondary.
- **Chunk:** Subconjunto de datos shardados.
- **Shard key:** Clave sobre la que se basa la distribución de datos en rangos o mediante hashing.
- **mongos:** Router que actúa como punto de entrada en un clúster MongoDB con sharding, enrutando consultas y obteniendo metadatos.
