---
curso: POWERBI
titulo: 13 - Semana 11/Introducción Modelo de Datos__pptx
slides: 29
fuente: 13 - Semana 11/Introducción Modelo de Datos__pptx.pdf
---

## Slide 1

Portada del capítulo. Texto: "Introducción / Modelo de Datos". Fondo decorativo (túnel digital azul con silueta de persona sosteniendo una cámara/trípode robótico), logo UTEC y "Reinventa el mundo" — decorativo.

## Slide 2

Título "Objetivo de *modelo de datos*". Lista de objetivos:
- Definición de modelo de datos.
- Qué es una granularidad.
- Tipos de relaciones y cardinalidad.

Imagen decorativa de dos personas trabajando (foto con overlay azul) — decorativa.

## Slide 3

Slide "Contenido" con lista numerada de los 4 temas del capítulo:
1. Modelo dimensional
2. Granularidad
3. Relaciones entre tablas
4. Cardinalidad entre tablas

Imagen decorativa de persona con visor VR — decorativa.

## Slide 4

Título "Modelo relacional". Texto: son los modelos de datos más comúnmente aplicados en aplicaciones de negocio, basados en múltiples tablas relacionadas mediante campos clave. La información está normalizada, evitando redundancia y optimizando inserción/edición/eliminación.

Diagrama: modelo entidad-relación completo de un sistema de restaurante/proveedores (captura de una herramienta de diseño de BD). Tablas visibles: `address`, `restaurant_table`, `customer`, `reservation`, `status`, `category`, `customer_order`, `customer_order_has_product`, `product`, `product_has_material`, `product_has_supplier`, `material`, `material_has_supplier`, `supplier`, `supplier_order`, `supplier_order_has_material`, `supplier_order_has_product`, `employee`, `role`, `area`, `report`. Cada tabla muestra sus columnas (id, claves foráneas, tipos VARCHAR/INT/DECIMAL/TEXT/DATE) conectadas por líneas de relación (llaves foráneas) entre sí, ilustrando un modelo relacional normalizado con múltiples tablas interconectadas.

## Slide 5

Título "Modelo plano". Texto: el modelo plano o FlatTable es cuando toda la información está en una sola tabla; cada registro contiene todos los campos, generando datos duplicados y redundantes.

Tabla de ejemplo (captura tipo hoja de cálculo) con columnas: Folio, Fecha, Número de cliente, Nombre de cliente, Ciudad, Estado, Vendedor, Forma de pago, Producto, Precio unitario, Cantidad, Ingresos. Filas de ejemplo (folios 1001-1011), mostrando repetición de datos de cliente/ciudad/vendedor en múltiples filas (ej. folio 1001 y 1002 ambos de "Empresa AA", Mazatlán, Sinaloa, Angela Andrade, con distinto producto/pago).

## Slide 6

Título "Modelo dimensional". Texto: técnica de estructura de datos optimizada para almacenamiento y análisis de información numérica; organiza los datos con tablas dimensión y tablas hecho.

Diagrama de esquema estrella: tabla central `VENTAS` (id_Cliente, id_Producto, id_Fecha, ImporteTotal, Utilidad) conectada con cardinalidad "n" a tres tablas dimensión con cardinalidad "1": `CLIENTES` (id_Cliente, NombreCliente), `PRODUCTOS` (id_Producto, Rubro, Tipo, NombreProducto) y `FECHAS` (id_Fecha, Año, Trimestre, Mes, Día).

## Slide 7

Título "Tabla dimensión". Texto: tablas organizadas para almacenar datos descriptivos/contextuales, parte del esquema estrella o copo de nieve. Características principales:
- Contienen atributos descriptivos (ej. tabla "Cliente" con nombre, dirección, edad, género).
- Relacionadas con tablas de hechos mediante claves foráneas.
- Facilitan el análisis (segmentar, filtrar, agrupar en reportes).

Solo texto, sin imagen adicional.

## Slide 8

Título "Tabla Hecho". Texto: almacenan eventos (pedidos de venta, saldos de existencias, tipos de cambio, temperaturas). Contienen columnas clave de dimensiones y columnas de medidas numéricas. Las tablas de dimensiones tienen pocas filas; las de hechos crecen mucho.

Diagrama de esquema en estrella (ilustración tipo Microsoft): tabla de hechos central `Sales fact table` conectada en forma de estrella a 5 tablas dimensión: `Product dimension table`, `Date dimension table`, `Reseller dimension table`, `Employee dimension table`, `Sales Territory dimension table`.

## Slide 9

Título "Granularidad". Texto: es el nivel de detalle máximo almacenado en las tablas; determinar la granularidad es el primer criterio al desarrollar un modelo de datos. Ejemplo: nivel de granularidad = Cliente, Fecha y producto.

Tabla de ejemplo:

| idCliente | Fecha | idProducto | Unidades | Precio | Importe |
|---|---|---|---|---|---|
| 1 | 15/03/2024 | P01 | 3 | 5 | 5 |
| 3 | 15/03/2024 | P01 | 2 | 5 | 10 |
| 3 | 15/03/2024 | P02 | 2 | 10 | 20 |
| 2 | 15/03/2024 | P02 | 2 | 10 | 20 |
| 2 | 15/03/2024 | P03 | 1 | 25 | 25 |
| 2 | 15/03/2024 | P04 | 1 | 15 | 15 |
| 4 | 15/03/2024 | P02 | 2 | 10 | 20 |
| 5 | 16/03/2024 | P04 | 3 | 15 | 45 |
| 5 | 16/03/2024 | P02 | 2 | 10 | 20 |
| 6 | 16/03/2024 | P03 | 1 | 25 | 25 |

Nota al pie: cada fila determina de forma única una venta con un atributo específico.

## Slide 10

Continuación de "Granularidad". Texto: qué pasaría si los datos están agrupados por filas repetidas según la granularidad definida, por ejemplo un mismo cliente con 2 transacciones el mismo día comprando el mismo producto. Pregunta abierta: ¿qué proponen para visualizar las 2 transacciones?

Tabla de ejemplo con columna adicional "Hora" respecto al slide anterior:

| idCliente | Fecha | Hora | idProducto | Unidades | Precio | Importe |
|---|---|---|---|---|---|---|
| 1 | 15/03/2024 | 10:00 | P01 | 1 | 5 | 5 |
| 1 | 15/03/2024 | 17:12 | P01 | 2 | 5 | 10 |
| 3 | 15/03/2024 | 09:00 | P01 | 2 | 5 | 10 |
| 3 | 15/03/2024 | 09:00 | P02 | 2 | 10 | 20 |
| 2 | 15/03/2024 | 11:23 | P02 | 2 | 10 | 20 |
| 2 | 15/03/2024 | 11:23 | P03 | 1 | 25 | 25 |
| 2 | 15/03/2024 | 11:23 | P04 | 1 | 15 | 15 |
| 4 | 15/03/2024 | 13:00 | P02 | 2 | 10 | 20 |
| 5 | 16/03/2024 | 14:28 | P04 | 3 | 15 | 45 |
| 5 | 16/03/2024 | 14:28 | P02 | 2 | 10 | 20 |
| 6 | 16/03/2024 | 16:00 | P03 | 1 | 25 | 25 |

Las dos primeras filas (idCliente=1, mismo producto P01, mismo día, distinta hora) están resaltadas con un recuadro rojo, ilustrando el caso de las 2 transacciones del mismo cliente/producto/día.

## Slide 11

Título "Relaciones entre tablas". Texto: cuando se tiene un conjunto de tablas y se quiere un funcionamiento lógico entre ellas, es necesario establecer relaciones. Las relaciones definen la dirección de filtrado y el tipo de cardinalidad. Power BI acepta datos de múltiples orígenes y las relaciones permiten conectarlos.

Captura de pantalla de la cinta de opciones de Power BI Desktop: pestañas Archivo/Inicio/Insertar/Modelado, con grupo "Datos" (Obtener datos, Libro de Excel, Centro de datos de OneLake, SQL Server). Debajo, el panel lateral de vistas (Informe, Datos, Modelo) con una flecha azul señalando el ícono de "Modelo" (el tercer ícono, de esquema de tablas), indicando dónde acceder a la vista de modelado.

## Slide 12

Continuación "Relaciones entre tablas". Texto: "Requisitos para relacionar 2 tablas":
1. Solamente es posible relacionar 2 tablas a través de 1 solo campo (no relaciones compuestas); si la clave principal es compuesta, se debe generar una clave subrogada.
2. Solamente existe una relación activa entre 2 tablas; las demás quedan inactivas.
3. Solamente es posible relacionar campos del mismo tipo de dato (no texto con numérico).
4. No es necesario que los nombres de los campos relacionados coincidan.

Solo texto, sin imagen adicional.

## Slide 13

Continuación "Relaciones entre tablas" — "Relaciones automáticas". Texto: por defecto Power BI tiene activa la configuración de auto-detectar relaciones entre tablas.

Captura de pantalla de Power BI: ventana "Opciones", panel izquierdo con categorías (Global: Carga de datos, Editor de Power Query, DirectQuery, Script de R, etc.; Archivo actual). Panel derecho muestra sección "Relaciones" resaltada con recuadro rojo, con checkboxes: "Importar relaciones de orígenes de datos en la primera carga" (activado), "Actualizar o eliminar las relaciones al actualizar los datos" (desactivado), "Detectar automáticamente nuevas relaciones cuando se carguen los datos" (activado). También se ven secciones "Detección de tipos", "Inteligencia de tiempo", "Datos en segundo plano", "Carga de tablas en paralelo". Botones Aceptar/Cancelar.

## Slide 14

Continuación "Relaciones entre tablas" — "Crear relaciones entre tablas: 1. Arrastrando campos". Texto: con la detección automática deshabilitada, al cargar las mismas tablas en la pestaña de modelado se ve el siguiente diagrama.

Diagrama de vista de modelo de Power BI: tabla `Cliente` (CódigoCliente, RazónSocial) y tabla `Tienda` (CódigoTienda, RazónSocialTienda) conectadas a la tabla central `Ventas` (Cantidad, Cliente, CódigoCliente, CódigoModelo, CódigoOperador, CódigoPaís, CódigoTienda, CódigoVendedor, Costo). Tienda también conectada a tabla `Vendedor` (CódigoVendedor, NombreVendedor). Las relaciones muestran cardinalidad "1" del lado de Cliente/Tienda/Vendedor y "*" del lado de Ventas.

## Slide 15

Continuación "Relaciones entre tablas" — "Crear relaciones entre tablas: 2. Administrador relaciones". 

Captura de pantalla: ícono "Administrar relaciones" de Power BI, y ventana "Administrar relaciones" con tabla que lista relaciones activas (checkbox verde en columna "Activo"):

| Activo | Desde: tabla (columna) | A: tabla (columna) |
|---|---|---|
| ✓ | Ventas (CódigoCliente) | Cliente (CódigoCliente) |
| ✓ | Ventas (CódigoTienda) | Tienda (CódigoTienda) |
| ✓ | Ventas (CódigoVendedor) | Vendedor (CódigoVendedor) |

Botones: Nuevo..., Detección automática..., Editar..., Eliminar, Cerrar.

## Slide 16

Título "Cardinalidad". Texto: una vez establecida una relación entre 2 tablas, el siguiente paso es definir la cardinalidad de dicha relación.

Captura de pantalla de vista de modelo Power BI: tabla `Ventas` (con columnas Cantidad, Cliente, CódigoCliente, CódigoModelo, CódigoOperador, CódigoPaís, CódigoTienda, CódigoVendedor, Costo) conectada a tabla `Vendedor` (CódigoVendedor, NombreVendedor). En el punto de conexión se resaltan con recuadros azules el símbolo "*" (lado de Ventas, "muchos") y el símbolo "1" (lado de Vendedor, "uno"), ilustrando los indicadores de cardinalidad de la relación.

## Slide 17

Continuación "Cardinalidad" — "Cardinalidad 1 a 1". Texto: relaciones donde existe correspondencia única entre cada registro de las tablas; ambas tablas son candidatas a combinarse en una sola con toda la información.

Dos tablas de ejemplo lado a lado:

Tabla izquierda (Cliente - datos personales):
| idcliente | nombre | apPaterno | apMaterno |
|---|---|---|---|
| 1 | Juan | López | Gonzales |
| 2 | Pedro | Pérez | Fuentes |
| 3 | Luis | Garcia | Rodriguez |
| 4 | Ana | Sanchez | Soto |

Tabla derecha (Dirección):
| idcliente | direccion | ciudad | pais |
|---|---|---|---|
| 1 | av. Diagonal 125 | Sevilla | España |
| 2 | jr. Salaverry 345 | Madrid | España |
| 3 | Av. Brazil 927 | Lima | Perú |
| 4 | C. Balmes 40 | Quito | Ecuador |

Ambas comparten idcliente como clave, ilustrando la correspondencia 1 a 1.

## Slide 18

Continuación "Cardinalidad 1 a 1" (repite el mismo texto explicativo). Incluye dos capturas de pantalla de Power BI:

Izquierda: diagrama de modelo con tabla `Cliente_Direccion` (ciudad, direccion, idcliente, pais) conectada con cardinalidad "1"-"1" a tabla `Cliente` (apMaterno, apPaterno, idcliente, nombre).

Derecha: ventana "Editar relación" mostrando ambas tablas con sus datos (Cliente_Direccion: idcliente, direccion, ciudad, pais con 3 filas de ejemplo; Cliente: idcliente, nombre, apPaterno, apMaterno con 3 filas). Configuración inferior: "Cardinalidad" = "Uno a uno (1:1)", "Dirección del filtro cruzado" = "Ambas", checkbox "Activar esta relación" marcado, checkbox "Asumir integridad referencial" sin marcar. Botones Aceptar/Cancelar.

## Slide 19

Continuación "Cardinalidad" — "Cardinalidad varios a varios". Texto: se conoce como relación débil o limitada; aparece cuando hay valores duplicados en una tabla donde no deberían existir. **No son recomendadas** en Power BI.

Dos tablas de ejemplo con flechas de colores conectando registros duplicados:

Tabla izquierda (Cliente, con fila duplicada idCliente=1 "Juan López"):
| idCliente | nombre | apellido |
|---|---|---|
| 1 | Juan | López |
| 2 | Pedro | Pérez |
| 1 | Juan | López |
| 3 | Ana | Sanchez |

Tabla derecha (Boletas):
| NroBoleta | idCliente | Unidades | Precio | Monto |
|---|---|---|---|---|
| 100 | 1 | 1 | 10 | 10 |
| 101 | 2 | 2 | 15 | 30 |
| 102 | 3 | 2 | 20 | 40 |
| 103 | 1 | 3 | 5 | 15 |
| 104 | 1 | 1 | 10 | 10 |

Flechas azules y amarillas conectan ambas filas "1-Juan-López" duplicadas con varias filas de NroBoleta que tienen idCliente=1, ilustrando la ambigüedad de la relación varios a varios.

## Slide 20

Continuación "Cardinalidad varios a varios" (mismo texto). Incluye:

Diagrama de modelo Power BI: tabla `Cliente` (apellido, idCliente, nombre) conectada con cardinalidad "*"-"*" a tabla `Ventas1` (idCliente, Monto, NroBoleta, Precio, Unidades). Nota al pie: "Obviamente, esta relación no es correcta. Solo se creó para términos académicos, lo correcto es eliminar los registros repetidos."

Captura de pantalla "Nueva relación" de Power BI: muestra tabla Cliente (con fila duplicada idCliente=1 "Juan López") y tabla Ventas1 con sus datos. Configuración: "Cardinalidad" = "Varios a varios (*:*)", "Dirección del filtro cruzado" = "Ambas", checkboxes "Activar esta relación" (marcado) y "Aplicar filtro de seguridad en ambas direcciones" (sin marcar), "Asumir integridad referencial" sin marcar. Mensaje de advertencia en amarillo: "Esta relación tiene una cardinalidad de varios a varios. Esto solo debe usar si se espera que ninguna columna (idCliente y idCliente) contenga valores únicos y que se entienda el comportamiento significativamente diferente de relaciones de varios a varios." Botones Aceptar/Cancelar.

## Slide 21

Continuación "Cardinalidad" — "Cardinalidad 1 a varios o varios a 1". Texto: son las más habituales y las que se utilizan en el modelo estrella. Power BI no indica explícitamente cuál tabla es dimensión o hecho, pero la cardinalidad ayuda: la tabla con cardinalidad "1" es dimensión y la tabla con cardinalidad "varios" es hecho.

Diagrama de modelo Power BI (esquema estrella completo): tabla central `Ventas` (Cantidad, Cliente, CódigoCliente, CódigoModelo, CódigoOperador, CódigoPaís, CódigoTienda, CódigoVendedor, Costo) conectada con cardinalidad "*" (muchos, lado de Ventas) a 4 tablas dimensión con cardinalidad "1": `Cliente` (CódigoCliente, RazónSocial), `Vendedor` (CódigoVendedor, NombreVendedor), `Tienda` (CódigoTienda, RazónSocialTienda) y `Modelo` (CódigoMarca, CódigoModelo, Costo, DescripciónModelo, Marca, Precio).

## Slide 22

Título "Dirección de filtrado". Texto: la definición de la dirección de una relación determina hacia dónde y cómo se propagan los filtros en los informes.

Diagrama de modelo Power BI: tabla `Cliente` (CódigoCliente, RazónSocial) conectada con cardinalidad "1" a tabla `Ventas` (Cantidad, Cliente, CódigoCliente, CódigoModelo, CódigoOperador, CódigoPaís, CódigoTienda, CódigoVendedor, Costo) con cardinalidad "*". En el punto de la relación se resalta con recuadro azul una flecha de dirección única apuntando de Cliente hacia Ventas. Texto al costado: "Esta dirección nos indica que los registros de la tabla Cliente filtrarán los registros de la tabla Ventas".

## Slide 23

Continuación "Dirección de filtrado" — "Ejemplo". Dos tablas con flecha roja indicando el filtrado:

Tabla izquierda (Cliente):
| IdCliente | Nombre | Apellidos |
|---|---|---|
| 1 | Juan | López |
| 2 | Pedro | Pérez |
| 3 | Ana | Sanchez |

(fila IdCliente=2 "Pedro Pérez" resaltada con recuadro rojo)

Tabla derecha (Ventas):
| IdVenta | IdCliente | Unidades | Importe |
|---|---|---|---|
| 100 | 2 | 2 | 100 |
| 101 | 3 | 4 | 150 |
| 102 | 1 | 1 | 50 |
| 103 | 2 | 1 | 200 |
| 104 | 1 | 2 | 80 |
| 105 | 2 | 4 | 50 |
| 106 | 3 | 2 | 20 |
| 107 | 1 | 1 | 100 |

Filas con IdCliente=2 (100, 103, 105) resaltadas con recuadros rojos, ilustrando cómo el filtro aplicado sobre "Pedro" en Cliente se propaga y filtra las filas correspondientes en Ventas.

## Slide 24

Continuación "Dirección de filtrado" — "Ejemplo" (continuación con resultado en Power BI). Captura de pantalla del panel de Power BI Desktop:

Panel "Visualizaciones" con íconos de tipos de gráfico; ícono de tabla resaltado con recuadro rojo (visual seleccionado: tabla). Panel "Datos" con árbol expandido: `Cliente1` (Apellidos, IdCliente, Nombre — checkbox "Nombre" marcado) y `Ventas2` (IdCliente, IdVenta, Importe — checkbox "Importe" marcado, Unidades). Panel "Columnas" con campos "Nombre" y "Suma de Importe" arrastrados (flechas rojas señalando el arrastre desde el árbol de datos hacia esta zona).

Resultado (tabla visual generada):
| Nombre | Suma de Importe |
|---|---|
| Ana | 170 |
| Juan | 230 |
| Pedro | 350 |
| **Total** | **750** |

## Slide 25

Continuación "Dirección de filtrado" — "Ejemplo 2". Diagrama de modelo Power BI: tabla `Cliente` (iCliente, nombre) conectada con cardinalidad "1"-"*" a tabla central `Ventas` (fecha, idCliente, idPRoducto, Unidades), que a su vez conecta con cardinalidad "*"-"1" a tabla `Producto` (Categoria, idProducto, Nombre). En el punto de conexión Ventas-Producto se resalta con recuadro rojo un símbolo de flecha de dirección única (apuntando de Producto hacia Ventas).

Resultado (tabla visual):
| nombre | Recuento de Categoria |
|---|---|
| Ana | 5 |
| Juan | 5 |
| Luis | 5 |
| Pedro | 5 |
| **Total** | **5** |

Nota: con filtro unidireccional, el recuento de Categoría es el mismo (5) para todos los clientes, porque el filtro de Cliente no se propaga hacia Producto a través de Ventas en esa dirección.

## Slide 26

Continuación "Ejemplo 2" (misma configuración, pero ahora con filtro bidireccional). Mismo diagrama de modelo que el slide 25, pero en el punto de conexión Ventas-Producto se resalta con recuadro rojo un símbolo de flecha bidireccional (doble flecha, "Ambas").

Resultado (tabla visual, valores distintos al slide anterior):
| nombre | Recuento de Categoria |
|---|---|
| Ana | 2 |
| Juan | 1 |
| Luis | 2 |
| Pedro | 2 |
| **Total** | **5** |

Fila "Ana" resaltada. Ilustra que con dirección de filtro "Ambas" el recuento de Categoría sí varía por cliente, reflejando el efecto real de la dirección de filtrado bidireccional.

## Slide 27

Continuación "Ejemplo 2" (mismo diagrama y resultado que el slide 26, filtro bidireccional resaltado en rojo). Se añade una fórmula DAX debajo de la tabla de resultados:

```dax
NroCategoria = CALCULATE(DISTINCTCOUNT(Producto[Categoria]),
    CROSSFILTER(Ventas[idPRoducto], Producto[idProducto], Both))
```

Esta medida usa `CROSSFILTER` con el parámetro `Both` para forzar el filtrado bidireccional entre Ventas y Producto, replicando en DAX el efecto visual mostrado en el diagrama.

## Slide 28

Slide "Conclusiones aquí" con dos puntos (flechas azules):
- Conocer los diferentes tipos de relaciones y cuál se debe utilizar.
- La importancia de la dirección del filtro cruzado.

Imagen decorativa de fondo (persona escribiendo en pizarra) — decorativa.

## Slide 29

Slide de cierre "GRACIAS", con el nombre del profesor "David Chira Siaden". Imagen decorativa de fondo (personas trabajando en laboratorio/taller) — decorativa.
