---
curso: BIGDATA
titulo: 12 - Semana 10/Sem10_MongoDB
slides: 34
fuente: 12 - Semana 10/Sem10_MongoDB.pdf
---

## Slide 1
Portada. Título "MongoDB", autor "Mg. Aldo Lezama Benavides", subtítulo "Semana 10". Fondo cian con edificio de UTEC (decorativa).

## Slide 2
**Objetivo de la sesión**

- **Comprender** los fundamentos de MongoDB como base de datos NoSQL orientada a documentos, su estructura de colecciones y documentos, y las diferencias con los sistemas relacionales.
- **Aplicar** los principales comandos de MongoDB para crear bases de datos, colecciones y realizar operaciones CRUD (crear, leer, actualizar y eliminar).
- **Analizar** cómo las características de escalabilidad, flexibilidad y rendimiento de MongoDB permiten su aplicación en entornos de Big Data, nube y desarrollo ágil.

## Slide 3
**Contenido de la sesión**

Dos bloques enmarcados en corchetes decorativos:
- **01.** Introducción
- **02.** Operaciones

## Slide 4
Slide divisoria de sección. Número grande "01." entre corchetes, ícono de portapapeles, título "Introducción a MongoDB".

## Slide 5
**MongoDB**

- MongoDB es una base de datos multiplataforma orientada a documentos que ofrece alto rendimiento, alta disponibilidad y fácil escalabilidad.
- MongoDB se basa en el concepto de colección y documento.

Visual: banner con el logo oficial de MongoDB (hoja verde + wordmark "MongoDB") sobre fondo verde oscuro.

## Slide 6
**Base de datos**

**Database**

- Una base de datos es un contenedor físico para colecciones. Cada base de datos obtiene su propio conjunto de archivos en el sistema de archivos. Un solo servidor MongoDB suele tener varias bases de datos.

Visual: captura de pantalla de MongoDB Atlas "Database Deployments". Muestra el cluster **MyFirstCluster** (etiquetas FREE / SHARED) con botones Connect, View Monitoring, Browse Collections. Panel de métricas (Reads/Writes 100.0/s, Connections 100.0, In/Out 100.0 B/s, Data Size 512.0 MB) y recuadro "Upgrade for $9/month" (2 GB storage, Daily backups, More API endpoints). Barra inferior con metadatos:

| VERSION | REGION | CLUSTER TIER | TYPE | BACKUPS | LINKED APP SERVICES | ATLAS SEARCH |
|---------|--------|--------------|------|---------|---------------------|--------------|
| 5.0.12 | GCP / Belgium (europe-west1) | M0 Sandbox (General) | Replica Set - 3 nodes | Inactive | None Linked | Create Index |

## Slide 7
**Colecciones**

**Collection**

- Una colección es un grupo de documentos MongoDB. Es el equivalente a una tabla RDBMS. Una colección existe dentro de una única base de datos. Las colecciones no imponen un esquema. Los documentos dentro de una colección pueden tener diferentes campos. Normalmente, todos los documentos de una colección tienen una finalidad similar o relacionada.

Visual: diagrama de tres documentos JSON apilados (recuadros verdes solapados) etiquetado "Collection". El documento del frente muestra:
```json
{
  name: "al",
  age: 18,
  status: "D",
  groups: [ "politics", "news" ]
}
```

## Slide 8
**Documentos**

- Un documento es un conjunto de pares clave-valor. Los documentos tienen un esquema dinámico.
- Un esquema dinámico significa que los documentos de una misma colección no necesitan tener el mismo conjunto de campos o estructura, y los campos comunes de los documentos de una colección pueden contener diferentes tipos de datos.

Visual: documento JSON con flechas apuntando a cada línea rotuladas "field: value":
```json
{
  name: "sue",
  age: 26,
  status: "A",
  groups: [ "news", "sports" ]
}
```

## Slide 9
**Ventajas**

- Sin esquema: MongoDB es una base de datos documental donde una colección contiene diferentes documentos. El número de campos, el contenido y el tamaño del documento pueden variar de un documento a otro.
- La estructura de un solo objeto es clara.
- Sin uniones complejas.
- Fácil escalabilidad: MongoDB es fácil de escalar.
- Gran capacidad de consulta. MongoDB admite consultas dinámicas en documentos mediante un lenguaje de consulta basado en documentos casi tan potente como SQL.
- No se requiere la conversión ni el mapeo de objetos de la aplicación a objetos de la base de datos.
- Utiliza memoria interna para almacenar el conjunto de trabajo (en ventanas), lo que permite un acceso más rápido a los datos.

## Slide 10
**¿Por qué usar MongoDB?**

- Almacenamiento Orientado a Documentos: Los datos se almacenan en formato JSON.
- Indexación por atributo.
- Replicación y Alta Disponibilidad.
- Fragmentación Automática.
- Consultas enriquecidas.
- Actualizaciones rápidas in situ.
- Soporte profesional de MongoDB.

## Slide 11
**Donde usar MongoDB?**

- Big Data
- Gestión y distribución de contenido
- Infraestructura móvil y social
- Gestión de datos de usuarios
- Centro de datos

## Slide 12
Slide divisoria de sección. Número grande "02." entre corchetes, ícono de portapapeles, título "Operaciones en MongoDB".

## Slide 13
**Sentencia de creación en MongoDB**

- El comando **use**
- El comando **use DATABASE_NAME** de MongoDB se utiliza para crear una base de datos. El comando creará una nueva base de datos; si no existe, devolverá la base de datos existente.
- Sintaxis:
- La sintaxis básica de la instrucción **use DATABASE** es la siguiente:

Visual: captura de terminal (mongosh):
```
test> use bigdata
switched to db bigdata
bigdata> db.curso.insertOne({"nombre":"MongoDB"})
{
  acknowledged: true,
  insertedId: ObjectId('68f6ae5f49faeee176cebea4')
}
```

## Slide 14
**Database**

- Para comprobar la base de datos seleccionada actualmente, utilice el comando **db**

Visual: terminal:
```
bigdata> db
bigdata
```

- Si desea consultar su lista de bases de datos, utilice el comando **show dbs**

Visual: terminal:
```
test> show dbs;
admin     40.00 KiB
config   100.00 KiB
demo     184.00 KiB
local     72.00 KiB
test      72.00 KiB
```

## Slide 15
**Database**

- La base de datos que creó (bigdata) no aparece en la lista. Para mostrarla, debe insertar al menos un documento.

Visual: dos capturas de terminal. Primera (insertar documento):
```
bigdata> db.curso.insertOne({"nombre":"MongoDB"})
{
  acknowledged: true,
  insertedId: ObjectId('68f6b016f873b6783bcebea4')
}
```
Segunda (ahora bigdata sí aparece):
```
bigdata> show dbs;
admin     40.00 KiB
bigdata    8.00 KiB
config    96.00 KiB
demo     184.00 KiB
local     72.00 KiB
test      72.00 KiB
```

## Slide 16
**Eliminación de Database**

- El comando **db.dropDatabase()** de MongoDB se utiliza para eliminar una base de datos existente.
- Sintaxis:
- La sintaxis básica del comando dropDatabase() es la siguiente:
- `db.dropDatabase()`
- Eliminará la base de datos seleccionada. Si no ha seleccionado ninguna base de datos, eliminará la base de datos de prueba predeterminada.

Visual: terminal:
```
bigdata> db.dropDatabase()
{ ok: 1, dropped: 'bigdata' }
bigdata> show dbs;
admin     40.00 KiB
config   108.00 KiB
demo     184.00 KiB
local     72.00 KiB
test      72.00 KiB
```

## Slide 17
**Crear Colecciones**

El método **createCollection()**:

- MongoDB db.createCollection(nombre, opciones) se utiliza para crear una colección.

**Sintaxis:**

- La sintaxis básica del comando **createCollection()** es la siguiente:

`db.createCollection(name, options)`

- En el comando, nombre es el nombre de la colección que se va a crear. Opciones es un documento y se utiliza para especificar la configuración (tamaño de memoria e indexación) de la colección.

Visual: terminal:
```
test> use universidad
switched to db universidad
universidad> db.createCollection("cursos")
{ ok: 1 }
```

## Slide 18
**Crear Colecciones**

El método **drop()**:

- El comando db.collection.drop() de MongoDB se utiliza para eliminar una colección de la base de datos.

**Sintaxis:**

- La sintaxis básica del comando drop() es la siguiente:

`db.COLLECTION_NAME.drop()`

Visual: terminal:
```
universidad> db.cursos.drop()
true
```

## Slide 19
**Tipos de Datos**

- **String**: Este es el tipo de dato más comúnmente utilizado para almacenar datos. En MongoDB, las cadenas deben ser UTF-8 válido.
- **Integer**: Este tipo se utiliza para almacenar un valor numérico. Un entero puede ser de 32 o 64 bits, según el servidor.
- **Boolean**: Este tipo se utiliza para almacenar un valor booleano (verdadero/falso).
- **Double**: Este tipo se utiliza para almacenar valores de punto flotante.
- **Mín/Máx Keys**: Este tipo se utiliza para comparar un valor con los elementos BSON más bajos y más altos.
- **Arrays**: Este tipo se utiliza para almacenar matrices, listas o múltiples valores en una sola clave.

## Slide 20
**Tipos de Datos**

- **Timestamp**: ctimestamp. Esto puede ser útil para registrar cuándo se ha modificado o añadido un documento.
- **Object**: Este tipo de dato se utiliza para documentos incrustados.
- **Null**: Este tipo se utiliza para almacenar un valor nulo.
- **Symbol**: Este tipo de dato se utiliza de forma idéntica a una cadena, pero generalmente se reserva para idiomas que utilizan un tipo de símbolo específico.
- **Date**: Este tipo de dato se utiliza para almacenar la fecha u hora actual en formato UNIX. Puede especificar su propia fecha y hora creando un objeto de fecha y pasándole el día, el mes y el año.

## Slide 21
**Tipos de Datos**

- **Object ID**: Este tipo de dato se utiliza para almacenar el ID del documento.
- **Binary data**: Este tipo de dato se utiliza para almacenar datos binarios.
- **Code**: Este tipo de dato se utiliza para almacenar código JavaScript en el documento.
- **Regular expression**: Este tipo de dato se utiliza para almacenar expresiones regulares.

## Slide 22
**Insert Document**

El método **insert()**:

- Para insertar datos en una colección de MongoDB, debe usar el método insert() o save() de MongoDB.

Sintaxis:

- La sintaxis básica del comando insert() es la siguiente:

`db.COLLECTION_NAME.insertOne(document)`

`db.COLLECTION_NAME.insertMany(documents)`

Visual: terminal:
```
universidad> db.cursos.insertOne({"nombre":"Big Data", "creditos":4})
{
  acknowledged: true,
  insertedId: ObjectId('68f6bc6ff873b6783bcebea6')
}
```

## Slide 23
**Query Document**

El método **find()**:

Para consultar datos de una colección de MongoDB, debe usar el método find().

**Sintaxis:**

- La sintaxis básica del método find() es la siguiente:

`db.COLLECTION_NAME.find()`

El método find() mostrará todos los documentos de forma no estructurada.

Visual: terminal:
```
universidad> db.cursos.find()
[
  {
    _id: ObjectId('68f6bc9ff873b6783bcebea7'),
    nombre: 'Big Data',
    creditos: 4
  }
]
```

## Slide 24
**Query Document**

El método **pretty()**:

- Para mostrar los resultados con formato, puede usar el método pretty().

**Sintaxis:**

`db.COLLECTION_NAME.find().pretty()`

Además del método find(), existe el método findOne(), que reejecuta solo un documento.

Visual: terminal con tres documentos:
```
universidad> db.cursos.find().pretty()
[
  {
    _id: ObjectId('68f6bd2bf873b6783bcebea8'),
    nombre: 'Big Data',
    creditos: 4,
    profesor: 'Aldo Lezama',
    modalidad: 'Presencial'
  },
  {
    _id: ObjectId('68f6bd5af873b6783bcebea9'),
    nombre: 'Deep Learning',
    creditos: 3,
    profesor: 'Juan Perez',
    modalidad: 'Virtual'
  },
  {
    _id: ObjectId('68f6bd99f873b6783bcebeaa'),
    nombre: 'Inteligencia Artificial',
    creditos: 4,
    profesor: 'Dr. Perez',
    modalidad: 'Presencial'
  }
]
```

## Slide 25
**Operaciones AND OR**

En el método **find()**, si se pasan varias claves separándolas por ',' entonces MongoDB las trata como una condición AND.

La **sintaxis** básica de AND:

`db.mycol.find({key1:value1, key2:value2}).pretty()`

- Para consultar documentos según la condición OR, se debe usar la palabra clave **$or**.

La **sintaxis** básica de OR:

`db.mycol.find({$or: [{key1: value1}, {key2:value2}]})`

Visual: terminal con consulta AND ($and: modalidad Presencial + creditos 4), devuelve dos documentos:
```
universidad> db.cursos.find({$and:[{"modalidad":"Presencial"},{"creditos":4}]})
[
  {
    _id: ObjectId('68f6bd2bf873b6783bcebea8'),
    nombre: 'Big Data',
    creditos: 4,
    profesor: 'Aldo Lezama',
    modalidad: 'Presencial'
  },
  {
    _id: ObjectId('68f6bd99f873b6783bcebeaa'),
    nombre: 'Inteligencia Artificial',
    creditos: 4,
    profesor: 'Dr. Perez',
    modalidad: 'Presencial'
  }
]
```

## Slide 26
**Update Documents**

Los métodos **update()** y **save()** de MongoDB se utilizan para actualizar un documento en una colección. El método update() actualiza los valores del documento existente, mientras que el método save() reemplaza el documento existente con el documento pasado en el método save().

Método **Update()** de MongoDB:

- El método update() actualiza los valores del documento existente.

**Sintaxis:**

`db.COLLECTION_NAME.update(SELECTION_CRITERIA,UPDATED_DATA)`

Visual: terminal (nótese el DeprecationWarning):
```
universidad> db.cursos.update({"nombre":"Big Data"}, {$set: {"modalidad":"Virtual"}})
DeprecationWarning: Collection.update() is deprecated. Use updateOne, updateMany, or bulkWrite.
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
```

## Slide 27
**Borrar Documents**

El método **remove()**:

- El método remove() de MongoDB se utiliza para eliminar documentos de la colección. Acepta dos parámetros: el criterio de eliminación y el indicador justOne.
1. Criterios de eliminación: (Opcional) Se eliminarán los criterios de eliminación según los documentos.
2. JustOne: (Opcional) Si se establece en verdadero o 1, se elimina solo un documento.

**Sintaxis:**

`db.COLLECTION_NAME.remove(DELETION_CRITERIA)`

Visual: terminal (con DeprecationWarning) elimina "Big Data" y el find() posterior muestra los dos documentos restantes:
```
universidad> db.cursos.remove({"nombre":"Big Data"})
DeprecationWarning: Collection.remove() is deprecated. Use deleteOne, deleteMany, findOneAndDelete, or bulkWrite.
{ acknowledged: true, deletedCount: 1 }
universidad> db.cursos.find()
[
  {
    _id: ObjectId('68f6bd5af873b6783bcebea9'),
    nombre: 'Deep Learning',
    creditos: 3,
    profesor: 'Juan Perez',
    modalidad: 'Virtual'
  },
  {
    _id: ObjectId('68f6bd99f873b6783bcebeaa'),
    nombre: 'Inteligencia Artificial',
    creditos: 4,
    profesor: 'Dr. Perez',
    modalidad: 'Presencial'
  }
]
```

## Slide 28
**Limit Registros**

El método **limit()**:

Para limitar los registros en MongoDB, debe usar el método limit(). Este método acepta un argumento numérico, que corresponde al número de documentos que desea mostrar.

**Sintaxis:**

`db.COLLECTION_NAME.find().limit(NUMBER)`

Visual: terminal, limit(1) devuelve un solo documento:
```
universidad> db.cursos.find().limit(1)
[
  {
    _id: ObjectId('68f6bd5af873b6783bcebea9'),
    nombre: 'Deep Learning',
    creditos: 3,
    profesor: 'Juan Perez',
    modalidad: 'Virtual'
  }
]
```

## Slide 29
**Skip Registros**

El método **skip()**:

Además del método limit(), existe otro método, skip(), que también acepta argumentos de tipo número y se utiliza para omitir un número determinado de documentos.

**Sintaxis:**

`db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)`

(Slide solo texto, sin captura.)

## Slide 30
**Sort Documents**

El método **sort()**:

Para ordenar documentos en MongoDB, se utiliza el método sort().

Este método acepta un documento que contiene una lista de campos y su orden de clasificación.

Para especificar el orden de clasificación, se utilizan 1 y -1. 1 se usa para orden ascendente y -1 para orden descendente.

Sintaxis:

`db.COLLECTION_NAME.find().sort({KEY:1})`

(Slide solo texto, sin captura.)

## Slide 31
**Indexando**

Los índices facilitan la resolución eficiente de consultas. Sin índices, MongoDB debe escanear cada documento de una colección para seleccionar aquellos que coinciden con la consulta. Este escaneo es altamente ineficiente y requiere que MongoDB procese un gran volumen de datos.

Los índices son estructuras de datos especiales que almacenan una pequeña porción del conjunto de datos de forma fácil de navegar. El índice almacena el valor de un campo o conjunto de campos específicos, ordenados por el valor del campo especificado en el índice.

El método **ensureIndex()**:

- Para crear un índice, debe usar el método **ensureIndex()** de MongoDB.
- `db.COLLECTION_NAME.ensureIndex({KEY:1})`

(Slide solo texto, sin captura.)

## Slide 32
**Agregación**

Las operaciones de agregación procesan registros de datos y devuelven resultados calculados. Las operaciones de agregación agrupan valores de varios documentos y pueden realizar diversas operaciones con los datos agrupados para devolver un único resultado.

- En SQL, count(*) y con group by es equivalente a la agregación en MongoDB.
- El método added():

**Sintaxis:**

`db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)`

(Slide solo texto, sin captura.)

## Slide 33
**Conclusiones**

- **01.** MongoDB ofrece una alternativa moderna a las bases de datos relacionales, priorizando la flexibilidad de esquemas y la escalabilidad horizontal.
- **02.** Su estructura basada en documentos JSON facilita la integración con aplicaciones modernas y la gestión eficiente de datos no estructurados.
- **03.** MongoDB es ampliamente utilizado en soluciones empresariales y de Big Data por su alto rendimiento, facilidad de uso y compatibilidad con entornos en la nube como GCP o MongoDB Atlas.

## Slide 34
Slide de cierre. Logo UTEC centrado sobre fondo cian (decorativa).
