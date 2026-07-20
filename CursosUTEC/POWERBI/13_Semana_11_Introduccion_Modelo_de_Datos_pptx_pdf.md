---
curso: POWERBI
titulo: 13 - Semana 11/Introducción Modelo de Datos__pptx
slides: 29
fuente: 13 - Semana 11/Introducción Modelo de Datos__pptx.pdf
---

Introducción
Modelo de Datos
Objetivo de modelo de
                        Definición de modelo de datos.
                        Qué es una granularidad.
                        Tipos de relaciones y cardinalidad.




        datos
Contenido

1.   Modelo dimensional



2.   Granularidad



3.   Relaciones entre tablas



4.   Cardinalidad entre
     tablas
                                             Modelo relacional
Son los modelos de datos mas comúnmente aplicados en nuestras aplicaciones de negocio. Este modelo está basado en la creación de
múltiples tablas de datos relacionadas entre si a través de campos claves.
La información está normalizada lo que permite que la información no sea redundante y esté optimizado para los procesos de inserción,
edición y eliminación.
                                                  Modelo plano
Modelo plano o FlatTable, es cuando toda la información de nuestra base de datos se encuentra en una sola tabla.
Cada registro de la tabla que forma el modelo contiene todos los campos de la base de datos, por lo que existen grandes cantidades de
información duplicada y redundante.
                                          Modelo dimensional
Es una técnica de estructura de datos optimizada para herramientas de almacenamiento de datos. Está diseñado para leer, resumir y
analizar información numérica. En otras palabras, el modelado dimensional organiza y estructura los datos de manera que facilite el
análisis y la obtención de información a partir de ellos.
Los modelos dimensionales trabajan con los conceptos de tablas dimensiones y tablas hechos.
                                               Tabla dimensión
Son tablas organizadas para organizar y almacenar datos descriptivos o contextuales que ayudan a analizar información. Forman parte
del diseño de esquemas en estrella o copo de nieve, comunes en el modelado de datos para análisis.

Características principales:

• Contienen atributos descriptivos: Por ejemplo, en una tabla de dimensiones "Cliente" podrías tener columnas como nombre, dirección,
  edad, género, etc.

• Relacionadas con tablas de hechos: Se conectan a tablas de hechos (que almacenan datos numéricos o métricas, como ventas) a
  través de claves foráneas.
• Facilitan el análisis: Permiten segmentar, filtrar o agrupar datos en reportes (por ejemplo, ventas por región, por fecha, etc.).
                                                   Tabla Hecho
Almacenan eventos, y pueden ser pedidos de venta, saldos de existencias, tipos de cambio, temperaturas, etc. Una tabla de hechos
contiene columnas clave de dimensiones que se relacionan con tablas de dimensiones y columnas de medidas numéricas.
Normalmente, las tablas de dimensiones contienen un número relativamente pequeño de filas. Por otro lado, las tablas de hechos pueden
contener un gran número de filas y seguir creciendo con el tiempo.
                                                       Granularidad
Es el nivel de detalle máximo de información almacenado en las tablas.
Determinar el nivel de granularidad es el primer criterio que debemos enfrentar cuando desarrollamos un modelo de datos.

Ejemplo: En este caso el nivel de granularidad de esta tabla es: Cliente. Fecha y producto.




                                        * Cada fila determina de forma única una venta con un atributo específico.
                                                  Granularidad
Pero qué pasaría si nuestros datos están agrupados por filas repetidas por el nivel de granularidad que hemos definido, por ejemplo, que
un mismo cliente haya realizó 2 transacciones en el mismo día, comprando el mismo producto.
¿Qué proponen para poder visualizar las 2 transacciones?
                                   Relaciones entre tablas
Cuando tenemos un conjunto de tablas y queremos que haya un funcionamiento lógico entre ella, es necesario establecer relaciones.

Las relaciones van a definir cómo será la lógica de funcionamiento de nuestro modelo de datos ya que a partir de ellas podremos definir
la dirección de filtrado y el tipo de carnalidad.

Power BI acepta datos de múltiples orígenes y gracias a las relaciones, podremos conectarlos.
                                   Relaciones entre tablas
Requisitos para relacionar 2 tablas:

1. Solamente es posible relacionar 2 tablas a través de 1 solo campo: No es posible las relaciones compuestas formadas por más de un
campo a la vez. En los casos donde no sea posible utilizar un campo para relacionar 2 tablas debido a que la clave principal es
compuesta, debemos generar una nueva columna (clave subrogada) que permita identificar de forma única a cada registro.

2. Solamente existe una relación activa entre 2 tablas: En caso de que entre 2 tablas exista más de una relación, solamente una de estas
relaciones será considerada como activa, las demás serán inactivas.

3. Solamente será posible la relación entre 2 campos que tengan el mismo tipo de dato: No será posible relacionar, por ejemplo, un
campo de tipo texto con un campo de tipo numérico.

4. No es necesario que los nombres de los campos que se van a relacionar tengan el mismo nombre.
                                    Relaciones entre tablas
Relaciones automáticas:

Por defecto Power BI tiene activa su configuración de auto detectar relaciones entre tablas.
                                 Relaciones entre tablas
Crear relaciones entre tablas:

Ahora que hemos deshabilitado la detección automática de relaciones, si volvemos a cargar las mismas tablas en la pestaña de
modelado veríamos lo siguiente:

1. Arrastrando campos.
                                 Relaciones entre tablas
Crear relaciones entre tablas:

Ahora que hemos deshabilitado la detección automática de relaciones, si volvemos a cargar las mismas tablas en la pestaña de
modelado veríamos lo siguiente:

2. Administrador relaciones
                                                Cardinalidad
Una vez que ya se ha establecido una relación entre 2 tablas, el siguiente paso consiste en definir cuál es la cardinalidad de esta
relación.
                                                 Cardinalidad
Cardinalidad 1 a 1: Las relaciones que tienen una cardinalidad de 1 a 1 son relaciones entre 2 tablas donde existe una correspondencia
única entre cada registro de las tablas.
En este caso ambas tablas son candidatas para poderlas combinar y generar entre las 2 tablas una única que contenga toda la
información.
                                                 Cardinalidad
Cardinalidad 1 a 1: Las relaciones que tienen una cardinalidad de 1 a 1 son relaciones entre 2 tablas donde existe una correspondencia
única entre cada registro de las tablas.
En este caso ambas tablas son candidatas para poderlas combinar y generar entre las 2 tablas una única que contenga toda la
información.
                                              Cardinalidad
Cardinalidad varios a varios: Cuando se crea una relación de varios a varios se le conoce como relación débil o limitada. Esta
cardinalidad generalmente aparece cuando tenemos valores duplicados en una tabla donde no deberíamos tenerlos.
Este tipo de relaciones no son recomendadas en Power BI.
                                                       Cardinalidad
Cardinalidad varios a varios: Cuando se crea una relación de varios a varios se le conoce como relación débil o limitada. Esta
cardinalidad generalmente aparece cuando tenemos valores duplicados en una tabla donde no deberíamos tenerlos.
Este tipo de relaciones no son recomendadas en Power BI.




                        * Obviamente, esta relación no es correcta. Solo se creó para términos
                        académicos, lo correcto es eliminar los registros repetidos.

                                                 Cardinalidad
Cardinalidad 1 a varios o varios a 1: Este tipo de cardinalidad son las más habituales y las que se utilizarán en el modelo estrella.
En Power BI no tenemos ninguna opción para indicar cual de nuestras tablas es dimensión o hecho, pero la cardinalidad nos ayudará; la
tabla que tiene la cardinalidad de 1 es dimensión y la tabla con la cardinalidad varios es hecho.
                                     Dirección de filtrado
La definición de la dirección de una relación es un factor clave en la creación de nuestro modelo ya que las direcciones definidas
determinarán hacia dónde y cómo se propagarán los filtros que aplicaremos en nuestros informes.




                                                             Esta dirección nos indica que los registros de la tabla Cliente filtrarán los
                                                             registros de la tabla Ventas
           Dirección de filtrado
Ejemplo:
           Dirección de filtrado
Ejemplo:
             Dirección de filtrado
Ejemplo 2:
             Dirección de filtrado
Ejemplo 2:
             Dirección de filtrado
Ejemplo 2:
Conclusiones aquí

  Conocer los diferentes tipos de relaciones y cuál se debe utilizar.




  La importancia de la dirección del filtro cruzado.
GRACIAS
 David Chira Siaden

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
