---
curso: BIGDATA
titulo: 12 - Semana 10/Sem10_MongoDB
slides: 34
fuente: 12 - Semana 10/Sem10_MongoDB.pdf
---

MongoDB
Mg. Aldo Lezama Benavides


Semana 10
  Objetivo de la sesión
• Comprender los fundamentos de MongoDB como base de datos NoSQL

  orientada a documentos, su estructura de colecciones y documentos, y

  las diferencias con los sistemas relacionales

• Aplicar los principales comandos de MongoDB para crear bases de

  datos, colecciones y realizar operaciones CRUD (crear, leer, actualizar y

  eliminar).

• Analizar cómo las características de escalabilidad, flexibilidad y

  rendimiento de MongoDB permiten su aplicación en entornos de Big

  Data, nube y desarrollo ágil.
Contenido de la sesión

      01.            02.

    Introducción   Operaciones
01.   Introducción a MongoDB
                                         MongoDB




• MongoDB es una base de datos multiplataforma
 orientada a documentos que ofrece alto rendimiento, alta
 disponibilidad y fácil escalabilidad.
• MongoDB se basa en el concepto de colección y
 documento.
                                      Base de datos



Database


• Una base de datos es un contenedor físico para
  colecciones. Cada base de datos obtiene su propio
  conjunto de archivos en el sistema de archivos. Un solo
  servidor MongoDB suele tener varias bases de datos.
                                          Colecciones


Collection


• Una colección es un grupo de documentos MongoDB. Es
  el equivalente a una tabla RDBMS. Una colección existe
  dentro de una única base de datos. Las colecciones no
  imponen un esquema. Los documentos dentro de una
  colección     pueden      tener     diferentes   campos.
  Normalmente, todos los documentos de una colección
  tienen una finalidad similar o relacionada.
                                     Documentos


• Un documento es un conjunto de pares clave-valor. Los
  documentos tienen un esquema dinámico.
• Un esquema dinámico significa que los documentos de
  una misma colección no necesitan tener el mismo
  conjunto de campos o estructura, y los campos comunes
  de los documentos de una colección pueden contener
  diferentes tipos de datos.
                                              Ventajas


• Sin esquema: MongoDB es una base de datos documental donde una colección contiene diferentes documentos.
  El número de campos, el contenido y el tamaño del documento pueden variar de un documento a otro.
• La estructura de un solo objeto es clara.
• Sin uniones complejas.
• Fácil escalabilidad: MongoDB es fácil de escalar.
• Gran capacidad de consulta. MongoDB admite consultas dinámicas en documentos mediante un lenguaje de
  consulta basado en documentos casi tan potente como SQL.
• No se requiere la conversión ni el mapeo de objetos de la aplicación a objetos de la base de datos.
• Utiliza memoria interna para almacenar el conjunto de trabajo (en ventanas), lo que permite un acceso más rápido
  a los datos.
                             ¿Por qué usar MongoDB?


• Almacenamiento Orientado a Documentos: Los datos se almacenan en formato JSON.
• Indexación por atributo.
• Replicación y Alta Disponibilidad.
• Fragmentación Automática.
• Consultas enriquecidas.
• Actualizaciones rápidas in situ.
• Soporte profesional de MongoDB.
                                   Donde usar MongoDB?


• Big Data
• Gestión y distribución de contenido
• Infraestructura móvil y social
• Gestión de datos de usuarios
• Centro de datos
02.   Operaciones en MongoDB
                   Sentencia de creación en MongoDB


• El comando use
• El comando use DATABASE_NAME de MongoDB se utiliza para crear una base de datos. El comando creará una
  nueva base de datos; si no existe, devolverá la base de datos existente.
• Sintaxis:
– La sintaxis básica de la instrucción use DATABASE es la siguiente:
                                           Database


• Para comprobar la base de datos seleccionada actualmente, utilice el comando db




• Si desea consultar su lista de bases de datos, utilice el comando show dbs
                                           Database


• La base de datos que creó (bigdata) no aparece en la lista. Para mostrarla, debe insertar al menos un documento.
                            Eliminación de Database


• El comando db.dropDatabase() de MongoDB se utiliza para eliminar una base de datos existente.
• Sintaxis:
• – La sintaxis básica del comando dropDatabase() es la siguiente:
• db.dropDatabase()
– Eliminará la base de datos seleccionada. Si no ha seleccionado ninguna base de datos, eliminará la base de datos
de prueba predeterminada.
                                   Crear Colecciones
El método createCollection():

• MongoDB db.createCollection(nombre, opciones) se utiliza para crear una colección.

Sintaxis:

– La sintaxis básica del comando createCollection() es la siguiente:

db.createCollection(name, options)

– En el comando, nombre es el nombre de la colección que se va a crear. Opciones es un documento y se utiliza

para especificar la configuración (tamaño de memoria e indexación) de la colección.
                                     Crear Colecciones
El método drop():

• El comando db.collection.drop() de MongoDB se utiliza para eliminar una colección de la base de datos.

Sintaxis:

– La sintaxis básica del comando drop() es la siguiente:

db.COLLECTION_NAME.drop()
                                        Tipos de Datos


❑ String: Este es el tipo de dato más comúnmente utilizado para almacenar datos. En MongoDB, las cadenas deben

   ser UTF-8 válido.

❑ Integer: Este tipo se utiliza para almacenar un valor numérico. Un entero puede ser de 32 o 64 bits, según el

   servidor.

❑ Boolean: Este tipo se utiliza para almacenar un valor booleano (verdadero/falso).

❑ Double: Este tipo se utiliza para almacenar valores de punto flotante.

❑ Mín/Máx Keys: Este tipo se utiliza para comparar un valor con los elementos BSON más bajos y más altos.

❑ Arrays: Este tipo se utiliza para almacenar matrices, listas o múltiples valores en una sola clave.
                                        Tipos de Datos


❑ Timestamp: ctimestamp. Esto puede ser útil para registrar cuándo se ha modificado o añadido un documento.

❑ Object: Este tipo de dato se utiliza para documentos incrustados.

❑ Null: Este tipo se utiliza para almacenar un valor nulo.

❑ Symbol: Este tipo de dato se utiliza de forma idéntica a una cadena, pero generalmente se reserva para idiomas

   que utilizan un tipo de símbolo específico.

❑ Date: Este tipo de dato se utiliza para almacenar la fecha u hora actual en formato UNIX. Puede especificar su

   propia fecha y hora creando un objeto de fecha y pasándole el día, el mes y el año.

                                       Tipos de Datos


❑ Object ID: Este tipo de dato se utiliza para almacenar el ID del documento.

❑ Binary data: Este tipo de dato se utiliza para almacenar datos binarios.

❑ Code: Este tipo de dato se utiliza para almacenar código JavaScript en el documento.

❑ Regular expression: Este tipo de dato se utiliza para almacenar expresiones regulares.
                                     Insert Document


El método insert():

• Para insertar datos en una colección de MongoDB, debe usar el método insert() o save() de MongoDB.

Sintaxis:

• La sintaxis básica del comando insert() es la siguiente:

db.COLLECTION_NAME.insertOne(document)

db.COLLECTION_NAME.insertMany(documents)
                                      Query Document

El método find():

Para consultar datos de una colección de MongoDB, debe usar el método find().

Sintaxis:

– La sintaxis básica del método find() es la siguiente:

db.COLLECTION_NAME.find()

El método find() mostrará todos los documentos de forma no estructurada.
                                 Query Document


El método pretty():

• Para mostrar los resultados con formato, puede usar el

método pretty().

Sintaxis:

db.COLLECTION_NAME.find().pretty()

Además del método find(), existe el método findOne(), que

reejecuta solo un documento.
                                   Operaciones AND OR

En el método find(), si se pasan varias claves separándolas por

‘,’ entonces MongoDB las trata como una condición AND.

La sintaxis básica de AND:

db.mycol.find({key1:value1, key2:value2}).pretty()

• Para consultar documentos según la condición OR, se debe

usar la palabra clave $or.

La sintaxis básica de OR:

db.mycol.find({$or: [{key1: value1}, {key2:value2}]}
                                   Update Documents
Los métodos update() y save() de MongoDB se utilizan para actualizar un documento en una colección. El método

update() actualiza los valores del documento existente, mientras que el método save() reemplaza el documento

existente con el documento pasado en el método save().

Método Update() de MongoDB:

– El método update() actualiza los valores del documento existente.

Sintaxis:

db.COLLECTION_NAME.update(SELECTION_CRITERIA,UPDATED_DATA)
                                     Borrar Documents
El método remove():
• El método remove() de MongoDB se utiliza para eliminar documentos de la colección. Acepta dos parámetros: el
criterio de eliminación y el indicador justOne.
1. Criterios de eliminación: (Opcional) Se eliminarán los criterios de eliminación según los documentos.
2. JustOne: (Opcional) Si se establece en verdadero o 1, se elimina solo un documento.
Sintaxis:
db.COLLECTION_NAME.remove(DELETION_CRITERIA)
                                     Limit Registros
El método limit():

Para limitar los registros en MongoDB, debe usar el método limit(). Este método acepta un argumento numérico, que

corresponde al número de documentos que desea mostrar.

Sintaxis:

db.COLLECTION_NAME.find().limit(NUMBER)
                                     Skip Registros


El método skip():

Además del método limit(), existe otro método, skip(), que también acepta argumentos de tipo número y se utiliza

para omitir un número determinado de documentos.

Sintaxis:

db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)
                                    Sort Documents


El método sort():

Para ordenar documentos en MongoDB, se utiliza el método sort().

Este método acepta un documento que contiene una lista de campos y su orden de clasificación.

Para especificar el orden de clasificación, se utilizan 1 y -1. 1 se usa para orden ascendente y -1 para orden

descendente.

Sintaxis:

db.COLLECTION_NAME.find().sort({KEY:1})
                                        Indexando

Los índices facilitan la resolución eficiente de consultas. Sin índices, MongoDB debe escanear cada documento de

una colección para seleccionar aquellos que coinciden con la consulta. Este escaneo es altamente ineficiente y

requiere que MongoDB procese un gran volumen de datos.

Los índices son estructuras de datos especiales que almacenan una pequeña porción del conjunto de datos de forma

fácil de navegar. El índice almacena el valor de un campo o conjunto de campos específicos, ordenados por el valor

del campo especificado en el índice.

El método ensureIndex():

• Para crear un índice, debe usar el método ensureIndex() de MongoDB.

• db.COLLECTION_NAME.ensureIndex({KEY:1})
                                       Agregación

Las operaciones de agregación procesan registros de datos y devuelven resultados calculados. Las operaciones de

agregación agrupan valores de varios documentos y pueden realizar diversas operaciones con los datos agrupados

para devolver un único resultado.

• En SQL, count(*) y con group by es equivalente a la agregación en MongoDB.

• El método added():

Sintaxis:

db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)
                     Conclusiones

01.   MongoDB ofrece una alternativa moderna a las bases de datos relacionales,
      priorizando la ﬂexibilidad de esquemas y la escalabilidad horizontal.



02    Su estructura basada en documentos JSON facilita la integración con aplicaciones

  .
      modernas y la gestión eﬁciente de datos no estructurados.



03    MongoDB es ampliamente utilizado en soluciones empresariales y de Big Data por
      su alto rendimiento, facilidad de uso y compatibilidad con entornos en la nube

  .   como GCP o MongoDB Atlas.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
