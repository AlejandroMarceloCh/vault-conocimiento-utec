---
curso: POWERBI
titulo: 12 - Semana 10/Introducción DAX__pptx
slides: 21
fuente: 12 - Semana 10/Introducción DAX__pptx.pdf
---

## Slide 1

Portada. Título "Introducción DAX" sobre fondo celeste con foto del edificio UTEC (decorativa) y logo UTEC + "Reinventa el mundo".

## Slide 2

Título "Objetivo de sesión". Texto dentro de un marco decorativo (corchetes blancos):
"Comprender de manera integral los fundamentos teóricos y prácticos del lenguaje DAX (Data Analysis Expressions), con el propósito de desarrollar habilidades que permitan a los participantes crear y aplicar expresiones y cálculos personalizados dentro del entorno de Power BI."

## Slide 3

Título "Contenido de sesión aquí". Cuatro bloques numerados 01-04 con marco de corchetes:
- 01: Introducción del lenguaje DAX
- 02: Funciones de agregación
- 03: texto de relleno ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been.")
- 04: mismo texto de relleno que 03

Los bloques 03 y 04 son placeholders sin contenido real definido aún.

## Slide 4

Título "Modelo relacional". Texto: "Son los modelos de datos mas comúnmente aplicados en nuestras aplicaciones de negocio. Este modelo está basado en la creación de múltiples tablas de datos relacionadas entre si a través de campos claves. La información está normalizada lo que permite que la información no sea redundante y esté optimizado para los procesos de inserción, edición y eliminación."

Diagrama: diagrama entidad-relación (ER) de una base de datos de restaurante/pedidos, con tablas conectadas: `address`, `customer`, `restaurant_table`, `reservation`, `status`, `category`, `product`, `product_has_material`, `material_has_supplier`, `supplier`, `customer_order`, `product_has_supplier`, `material`, `supplier_order_has_material`, `employee`, `supplier_order`, `customer_order_has_product`, `role`, `report`, `area`, `supplier_order_has_product`. Cada tabla muestra sus columnas (id, claves foráneas) conectadas por líneas de relación (llaves primarias/foráneas típicas de un modelo relacional normalizado).

## Slide 5

Título "Modelo plano". Texto: "Modelo plano o FlatTable, es cuando toda la información de nuestra base de datos se encuentra en una sola tabla. Cada registro de la tabla que forma el modelo contiene todos los campos de la base de datos, por lo que existen grandes cantidades de información duplicada y redundante."

Tabla de ejemplo (captura estilo Excel) con columnas: Folio | Fecha | Número de cliente | Nombre de cliente | Ciudad | Estado | Vendedor | Forma de pago | Producto | Precio unitario | Cantidad | Ingresos

| Folio | Fecha | N° cliente | Nombre cliente | Ciudad | Estado | Vendedor | Forma pago | Producto | Precio unit. | Cantidad | Ingresos |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1001 | 27/01/22 | 27 | Empresa AA | Mazatlán | Sinaloa | Angela Andrade | transferencia | A4 | $13.50 | 65 | $877.50 |
| 1002 | 27/01/22 | 27 | Empresa AA | Mazatlán | Sinaloa | Angela Andrade | cheque | sobres oficio | $8.75 | 22 | $192.50 |
| 1003 | 04/01/22 | 4 | Empresa D | Querétaro | Querétaro | Pedro Puértolas | transferencia | opalina | $18.20 | 43 | $782.60 |
| 1004 | 04/01/22 | 4 | Empresa D | Querétaro | Querétaro | Pedro Puértolas | tarjeta de crédito | A4 | $13.50 | 11 | $148.50 |
| 1005 | 04/01/22 | 4 | Empresa D | Querétaro | Querétaro | Pedro Puértolas | efectivo | sobres oficio | $8.75 | 73 | $638.75 |
| 1006 | 12/01/22 | 12 | Empresa L | Mazatlán | Sinaloa | Angela Andrade | efectivo | A4 | $13.50 | 14 | $189.00 |
| 1007 | 12/01/22 | 12 | Empresa L | Mazatlán | Sinaloa | Angela Andrade | tarjeta de crédito | cascarón | $15.00 | 98 | $1,470.00 |
| 1008 | 08/01/22 | 8 | Empresa H | Monterrey | Nuevo León | Romina Rosales | efectivo | opalina | $18.20 | 15 | $273.00 |
| 1009 | 04/01/22 | 4 | Empresa D | Querétaro | Querétaro | Pedro Puértolas | cheque | opalina | $18.20 | 20 | $364.00 |
| 1010 | 29/01/22 | 29 | Empresa CC | Puerto Vallarta | Jalisco | Mónica Menéndez | transferencia | sobres oficio | $8.75 | 56 | $490.00 |
| 1011 | 03/01/22 | 3 | Empresa C | Acapulco | Guerrero | Angela Andrade | transferencia | cascarón | $15.00 | 36 | $540.00 |

Se ve que ciudad/estado/vendedor se repiten en cada fila (redundancia propia del modelo plano).

## Slide 6

Título "Modelo dimensional". Texto: "Es una técnica de estructura de datos optimizada para herramientas de almacenamiento de datos. Está diseñado para leer, resumir y analizar información numérica. En otras palabras, el modelado dimensional organiza y estructura los datos de manera que facilite el análisis y la obtención de información a partir de ellos. Los modelos dimensionales trabajan con los conceptos de tablas dimensiones y tablas hechos."

Diagrama de esquema estrella con 4 tablas:
- **CLIENTES** (id_Cliente [PK], NombreCliente) — relación 1 a n con VENTAS.
- **PRODUCTOS** (id_Producto [PK], Rubro, Tipo, NombreProducto) — relación 1 a n con VENTAS.
- **VENTAS** (tabla de hechos, centro): id_Cliente [FK], id_Producto [FK], id_Fecha [FK], ImporteTotal, Utilidad.
- **FECHAS** (id_Fecha [PK], Año, Trimestre, Mes, Día) — relación 1 a n con VENTAS.

Las cardinalidades marcadas son 1 en las tablas dimensión y n en la tabla de hechos VENTAS.

## Slide 7

Título "Tabla dimensión". Texto: "Son tablas organizadas para organizar y almacenar datos descriptivos o contextuales que ayudan a analizar información. Forman parte del diseño de esquemas en estrella o copo de nieve, comunes en el modelado de datos para análisis."

Características principales (bullets):
- Contienen atributos descriptivos: por ejemplo, en una tabla de dimensiones "Cliente" podrías tener columnas como nombre, dirección, edad, género, etc.
- Relacionadas con tablas de hechos: se conectan a tablas de hechos (que almacenan datos numéricos o métricas, como ventas) a través de claves foráneas.
- Facilitan el análisis: permiten segmentar, filtrar o agrupar datos en reportes (por ejemplo, ventas por región, por fecha, etc.).

Sin diagrama en esta slide.

## Slide 8

Título "Tabla Hecho". Texto: "Almacenan eventos, y pueden ser pedidos de venta, saldos de existencias, tipos de cambio, temperaturas, etc. Una tabla de hechos contiene columnas clave de dimensiones que se relacionan con tablas de dimensiones y columnas de medidas numéricas. Normalmente, las tablas de dimensiones contienen un número relativamente pequeño de filas. Por otro lado, las tablas de hechos pueden contener un gran número de filas y seguir creciendo con el tiempo."

Diagrama: esquema en estrella con la tabla de hechos "Sales" (fact table) en el centro (forma de estrella morada) conectada a 5 tablas de dimensión en los picos: "Product" (dimension table, arriba), "Date" (dimension table, derecha), "Reseller" (dimension table, abajo derecha), "Employee" (dimension table, abajo izquierda), "Sales Territory" (dimension table, izquierda). Cada tabla lleva un ícono de tabla/grid.

## Slide 9

Título "Relaciones entre tablas" (con tachado decorativo estilo subrayado en "tablas"). Texto: "Cuando tenemos un conjunto de tablas y queremos que haya un funcionamiento lógico entre ella, es necesario establecer relaciones. Las relaciones van a definir cómo será la lógica de funcionamiento de nuestro modelo de datos ya que a partir de ellas podremos definir la dirección de filtrado y el tipo de carnalidad [cardinalidad]. Power BI acepta datos de múltiples orígenes y gracias a las relaciones, podremos conectarlos."

Captura de pantalla: cinta de Power BI, pestañas "Archivo | Inicio | Insertar | Modelado" (pestaña Inicio activa). Grupo "Portapapeles" (Pegar, cortar, copiar, pincel de formato) y grupo "Datos" con botones "Obtener datos", "Libro de Excel", "Centro de datos de OneLake", "SQL Server". Debajo, panel lateral izquierdo de Power BI con 3 íconos verticales (Informe/gráfico de barras, Tabla, Modelo/relaciones); una flecha azul señala el tercer ícono (vista de Modelo, resaltado con recuadro azul) indicando dónde se gestionan las relaciones entre tablas.

## Slide 10

Título "Relaciones entre tablas" (mismo estilo tachado). Subtítulo en negrita: "Requisitos para relacionar 2 tablas:"

Lista numerada:
1. Solamente es posible relacionar 2 tablas a través de 1 solo campo: No es posible las relaciones compuestas formadas por más de un campo a la vez. En los casos donde no sea posible utilizar un campo para relacionar 2 tablas debido a que la clave principal es compuesta, debemos generar una nueva columna (clave subrogada) que permita identificar de forma única a cada registro.
2. Solamente existe una relación activa entre 2 tablas: en caso de que entre 2 tablas exista más de una relación, solamente una de estas relaciones será considerada como activa, las demás serán inactivas.
3. Solamente será posible la relación entre 2 campos que tengan el mismo tipo de dato: no será posible relacionar, por ejemplo, un campo de tipo texto con un campo de tipo numérico.
4. No es necesario que los nombres de los campos que se van a relacionar tengan el mismo nombre.

## Slide 11

Título "Introducción DAX". Texto: "DAX (Data Analysis Expressions) es un lenguaje de fórmulas que se utiliza en Microsoft Power BI, Power Pivot en Excel y Analysis Services para realizar cálculos y análisis de datos. Permite crear nuevas columnas calculadas, medidas y otras operaciones sobre los datos de un modelo de datos."

Diagrama de flujo tipo "flechas apiladas" (4 categorías que confluyen en un resultado):
1. "Añade columnas con cálculos basados en otras columnas." → **Columnas Calculadas**
2. "Calcula agregaciones específicas como totales o promedios." → **Medidas**
3. "Realiza cálculos complejos con funciones avanzadas." → **Análisis Complejos**
4. "Compara y analiza datos a través del tiempo." → **Inteligencia Temporal**

Las 4 flechas convergen en un bloque final: **Informes y Paneles Personalizados** (con ícono de gráfico/dashboard).

## Slide 12

Título "Introducción DAX". Dos columnas comparativas con íconos:

**Columna izquierda — ícono de calculadora — "Nueva medida"**
1. Se calcula al momento de la consulta (on-the-fly), es decir, cada vez que interactúas con un visual que la utiliza.
2. No se almacena. El resultado no se guarda en ningún sitio. Lo único que se almacena en el modelo es la definición DAX.
3. Puedes tener cientos de medidas en tu modelo sin que afecte el tamaño del archivo.
4. Sintaxis:
```
Venta Total = SUM(fVenta[MontoFacturado])
```

**Columna derecha — ícono de tabla/columna — "Nueva columna"**
1. Se calcula una sola vez, durante el proceso de actualización (refresh) de los datos.
2. El resultado de cada fila se almacena físicamente en el modelo de datos, dentro de la tabla.
3. Consume memoria RAM (porque el motor VertiPaq de Power BI es in-memory) y aumenta el tamaño de tu archivo .pbix.

**Cuando usarla:**
- Usar el resultado en un **eje** de un gráfico.
- Usar el resultado en un **slicer** (segmentador de datos).

## Slide 13

Título "Medidas". Tabla/listado de funciones DAX organizado en 5 categorías con encabezados en cajas celestes:

| Agregación | Lógicas | Filtro | Tiempo | Tabla |
|---|---|---|---|---|
| SUM | IF | CALCULATE | SAMEPERIODLASTYEAR | VALUES |
| AVERAGE | SWITCH | FILTER | DATEADD | ADDCOLUMNS |
| MAX | TRUE | ALL | DATESYTD | INTERSECT |
| MIN | NOT | ALLSELECTED | DATESQTD | EXCEPT |
| COUNTROWS | AND | SELECTEDVALUE | PREVIOUSYEAR | SUMMARIZE |
| SUMX | OR | | PREVIOUSMONTH | UNION |
| AVERAGEX | | | DATESBETWEEN | |
| MAXX | | | DATESINPERIOD | |
| MINX | | | | |

## Slide 14

Título "Ejemplo". Texto: "Crear una columna calculada para obtener la venta total."

Código DAX:
```
Venta Total = 
    FVentas[Cantidad] * FVentas[PrecioUnid]
```

Captura de resultado: columna "Venta Total" con valores de ejemplo: 227351.91, 38153.27, 29341.41, 32743.56, 99612.76, 4398.52, 130646.7

## Slide 15

Título "Ejemplo". Texto: "Crear una columna calculada para obtener la gasto y ganancia total."

Código DAX:
```
Gasto total = 
FVentas[CostoUnid] + FVentas[ComisionUnid]

Ganancia = 
FVentas[Venta Total] - FVentas[Gasto total]
```

Capturas de resultado, dos columnas lado a lado:

"Gasto total": 5870.61522371958, 1005.62374264733, 1065.47116971366, 2252.57210534337, 10845.5450510508, 289.619189855626, 20591.5449493325

"Ganancia": 221481.29, 37147.65, 28275.94, 30490.99, 88767.21, 4108.90

## Slide 16

Título "Ejemplo". Texto: "Error de cálculo, creemos una columna para obtener el margen de ganancia."

Código DAX:
```
Margen de Ganancia = 
FVentas[Ganancia] / FVentas[Venta Total]
```

Dos tablas de resultado lado a lado mostrando el mismo dato en dos formatos (decimal sin formato vs. formateado en porcentaje):

| Margen de Ganancia (decimal) | Margen de Ganancia (%) |
|---|---|
| 0.974178289402893 | 97.4% |
| 0.973642528080887 | 97.4% |
| 0.963687117636349 | 96.4% |
| 0.931205644549848 | 93.1% |
| 0.891122933938887 | 89.1% |
| 0.934155309091325 | 93.4% |
| 0.842387561650371 | 84.2% |

La slide ilustra que el cálculo es correcto pero el "error" está en el formato de visualización (decimal vs. porcentaje).

## Slide 17

Título "Ejemplo". Texto: "Error de cálculo, creemos una columna para obtener el margen de ganancia." (repite el enunciado de la slide 16, ahora mostrando el problema a nivel de tabla agregada/resumen).

Tabla resumen por Subcategoría:

| Subcategoria | Suma de Venta Total | Suma de Ganancia | Suma de Margen de Ganancia |
|---|---|---|---|
| Computador | 328,342,448.06 | 309871925.14 | 212893.4% |
| DVD | 206,909,914.94 | 195517852.82 | 137525.8% |
| Fone | 76,494,125.86 | 72845658.05 | 46443.6% |
| Gravador | 36,235,722.38 | 34332012.32 | 22979.9% |
| Home Theater | 195,949,673.97 | 185022334.39 | 128782.3% |
| MP4 e MP3 | 64,590,020.12 | 60917894.50 | 43928.4% |
| Notebook | 266,890,085.22 | 252095498.93 | 174577.9% |
| Projetor | 290,367,393.45 | 274387186.94 | 193432.1% |
| Scanner | 153,801,981.40 | 144892846.75 | 110024.0% |
| Televisão | 98,416,506.43 | 93323887.07 | 69868.6% |
| **Total** | **1,717,997,871.81** | **1623207096.91** | **1140456.0%** |

Nota: la columna "Suma de Margen de Ganancia" da valores absurdos (>100,000%) porque el error de cálculo es que Power BI está sumando el margen de ganancia fila por fila (columna calculada) en vez de recalcular el ratio Ganancia/Venta al nivel agregado — ejemplo clásico de por qué el margen debe implementarse como medida (con CALCULATE/SUMX) y no como columna calculada sumada directamente.

## Slide 18

Título "Funciones Related y Relatedtable" (con tachado decorativo en la segunda línea del título). Texto: "Estas funciones no generan un contexto de Fila, pero si usan un contexto de Fila. La función Related, requiere estar ubicada en el lado múltiple de la relación y la función Relatedtable requiere estar ubicada en el lado individual de la relación."

Ejercicio planteado: "En la tabla fvVentas, se desea agregar el precio de lista que está en la tabla dimProducto."

## Slide 19

Título "Funciones Related y Relatedtable". Texto: "Creamos una columna calculada."

Código DAX:
```
Precio Lista = 
RELATED(dimProducto[Precio Lista])
```

Capturas de dos tablas relacionadas con anotaciones (asterisco * y "1" indicando la relación "muchos a uno"):

Tabla superior "fvVentas" (lado muchos, marcado con *):
| ID_Tienda | ID_Producto | ID_Cliente | Fecha Orden | Unidades | Precio Unitario | Costo Unitario | VentaTotal |
|---|---|---|---|---|---|---|---|
| 307 | 1297 | 6 | 07/07/2018 | 3 | 25 | 11.5 | 75 |
| 307 | 904 | 6 | 07/07/2018 | 2 | 75.99 | 38.74 | 151.98 |
| 307 | 1870 | 6 | 27/12/2018 | 2 | 1599 | 815.22 | 3198 |
| 307 | 1870 | 7 | 27/12/2018 | 1 | 1599 | 815.22 | 1599 |

Tabla inferior "dimProducto" (lado uno, marcado con 1):
| ID_Producto | Nombre Producto | Fabricante | Marca | Costo Unitario | Precio Lista |
|---|---|---|---|---|---|
| 1727 | MGS Rise of Nations: Gold Edition M300 | Tailspin Toys | Tailspin Toys | 25.75 | 67.2 |
| 1743 | MGS Combat Flight Simulator 3 E119 | Tailspin Toys | Tailspin Toys | 14.28 | 33.6 |
| 1753 | MGS Racing Madness 2 M370 | Tailspin Toys | Tailspin Toys | 40.93 | 106.8 |

La flecha conecta el campo ID_Producto de fvVentas (muchos) con dimProducto (uno), ilustrando cómo RELATED trae el Precio Lista desde el lado "uno" hacia el lado "muchos".

## Slide 20

Título "Funciones Related y Relatedtable". Ejercicio (negrita "Ejercicio:"): "Crear una medida, donde pueda obtener el monto de venta a precio de lista."

Código DAX:
```
5. Monto de venta-Precio lista = 
SUMX(fctVentas,
    fctVentas[Unidades]*RELATED(dimProducto[Precio Lista])
)
```

Captura de tabla resultado:
| ID_Tienda | ID_Producto | ID_Cliente | Unidades | Precio Unitario | 5. Monto de venta-Precio lista |
|---|---|---|---|---|---|
| 199 | 904 | 16 | 1 | 75.99 | 91.19 |
| 199 | 1297 | 16 | 2 | 25.00 | 60.00 |
| 199 | 1686 | 16 | 1 | 6.99 | 8.39 |
| 199 | 1727 | 16 | 2 | 56.00 | 134.40 |
| 199 | 1727 | 17 | 1 | 56.00 | 67.20 |
| 199 | 1743 | 17 | 1 | 28.00 | 33.60 |

## Slide 21

Slide de cierre. Solo logo UTEC grande centrado y texto "UNIVERSIDAD DE INGENIERÍA Y TECNOLOGÍA" sobre fondo celeste degradado (decorativa).
