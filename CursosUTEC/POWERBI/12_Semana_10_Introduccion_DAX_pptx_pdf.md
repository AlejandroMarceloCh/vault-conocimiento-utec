---
curso: POWERBI
titulo: 12 - Semana 10/Introducción DAX__pptx
slides: 21
fuente: 12 - Semana 10/Introducción DAX__pptx.pdf
---

Introducción
DAX
  Objetivo de sesión


Comprender de manera integral los fundamentos teóricos y prácticos
del lenguaje DAX (Data Analysis Expressions), con el propósito de
desarrollar habilidades que permitan a los participantes crear y
aplicar expresiones y cálculos personalizados dentro del entorno de
Power BI.
                   Contenido de sesión aquí
    01                     02                03                    04
      .                      .                 .                     .
                                         Lorem Ipsum is        Lorem Ipsum is
                                       simply dummy text     simply dummy text
Introducción del        Funciones de   of the printing and   of the printing and
 lenguaje DAX            agregación        typesetting           typesetting
                                         industry. Lorem       industry. Lorem
                                        Ipsum has been.       Ipsum has been.
Modelo relacional
Son los modelos de datos mas comúnmente aplicados en nuestras aplicaciones de negocio. Este modelo está basado en la creación de múltiples tablas de datos
relacionadas entre si a través de campos claves.
La información está normalizada lo que permite que la información no sea redundante y esté optimizado para los procesos de inserción, edición y eliminación.
Modelo plano
Modelo plano o FlatTable, es cuando toda la información de nuestra base de datos se encuentra en una sola tabla.
Cada registro de la tabla que forma el modelo contiene todos los campos de la base de datos, por lo que existen grandes cantidades de información duplicada y
redundante.
Modelo dimensional
Es una técnica de estructura de datos optimizada para herramientas de almacenamiento de datos. Está diseñado para leer, resumir y analizar información numérica.
En otras palabras, el modelado dimensional organiza y estructura los datos de manera que facilite el análisis y la obtención de información a partir de ellos.
Los modelos dimensionales trabajan con los conceptos de tablas dimensiones y tablas hechos.
Tabla dimensión
Son tablas organizadas para organizar y almacenar datos descriptivos o contextuales que ayudan a analizar información. Forman parte del
diseño de esquemas en estrella o copo de nieve, comunes en el modelado de datos para análisis.

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
Relaciones entre
tablas
Cuando tenemos un conjunto de tablas y queremos que haya un funcionamiento lógico entre ella, es necesario establecer relaciones.

Las relaciones van a definir cómo será la lógica de funcionamiento de nuestro modelo de datos ya que a partir de ellas podremos definir la
dirección de filtrado y el tipo de carnalidad.

Power BI acepta datos de múltiples orígenes y gracias a las relaciones, podremos conectarlos.
Relaciones entre
tablas
Requisitos para relacionar 2 tablas:

1. Solamente es posible relacionar 2 tablas a través de 1 solo campo: No es posible las relaciones compuestas formadas por más de un
campo a la vez. En los casos donde no sea posible utilizar un campo para relacionar 2 tablas debido a que la clave principal es compuesta,
debemos generar una nueva columna (clave subrogada) que permita identificar de forma única a cada registro.

2. Solamente existe una relación activa entre 2 tablas: En caso de que entre 2 tablas exista más de una relación, solamente una de estas
relaciones será considerada como activa, las demás serán inactivas.

3. Solamente será posible la relación entre 2 campos que tengan el mismo tipo de dato: No será posible relacionar, por ejemplo, un campo
de tipo texto con un campo de tipo numérico.

4. No es necesario que los nombres de los campos que se van a relacionar tengan el mismo nombre.
Introducción DAX
DAX (Data Analysis Expressions) es un lenguaje de fórmulas que se utiliza en Microsoft Power BI, Power Pivot en Excel y Analysis Services para realizar cálculos y
análisis de datos. Permite crear nuevas columnas calculadas, medidas y otras operaciones sobre los datos de un modelo de datos.
    Introducción DAX



                                                                  1. Se calcula una sola vez, durante el proceso de
1. Se calcula al momento de la consulta (on-the-fly), es decir,      actualización (refresh) de los datos.
cada vez que interactúas con un visual que la utiliza.
                                                                  2. El resultado de cada fila se almacena físicamente en el
2. No se almacena. El resultado no se guarda en ningún sitio.     modelo de datos, dentro de la tabla.
Lo único que se almacena en el modelo es la definición DAX.
                                                                  3. Consume memoria RAM (porque el motor VertiPaq de
3. Puedes tener cientos de medidas en tu modelo sin que           Power BI es in-memory) y aumenta el tamaño de tu
afecte el tamaño del archivo.                                     archivo .pbix.

4. Sintaxis:                                                      Cuando usarla:

Venta Total = SUM(fVenta[MontoFacturado])                         • Usar el resultado en un eje de un gráfico.
                                                                  • Usar el resultado en un slicer (segmentador de datos).
   Medidas
    Agregación            Lógicas         Filtro         Tiempo                Tabla


SUM              IF                 CALCULATE       SAMEPERIODLASTYEAR   VALUES
AVERAGE          SWITCH             FILTER          DATEADD              ADDCOLUMNS
MAX              TRUE               ALL             DATESYTD             INTERSECT
MIN              NOT                ALLSELECTED     DATESQTD             EXCEPT
COUNTROWS        AND                SELECTEDVALUE   PREVIOUSYEAR         SUMMARIZE
                 OR                                 PREVIOUSMONTH        UNION
SUMX                                                DATESBETWEEN
AVERAGEX                                            DATESINPERIOD
MAXX
MINX
  Ejemplo
Crear una columna calculada para obtener la venta total.
  Ejemplo
Crear una columna calculada para obtener la gasto y ganancia total.
  Ejemplo
Error de cálculo, creemos una columna para obtener el margen de ganancia.
  Ejemplo
Error de cálculo, creemos una columna para obtener el margen de ganancia.
  Funciones Related y
  Relatedtable
Estas funciones no generan un contexto de Fila, pero si usan un contexto de Fila.
La función Related, requiere estar ubicada en el lado múltiple de la relación y la función Relatedtable requiere estar ubicada en el lado
individual de la relación.

Ejercicio: En la tabla fvVentas, se desea agregar el precio de lista que está en la tabla dimProducto.
Funciones Related y
Relatedtable
Creamos una columna calculada.




                                 *


                                     1
   Funciones Related y
   Relatedtable
Ejercicio: Crear una medida, donde pueda obtener el monto de venta a precio de lista.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
