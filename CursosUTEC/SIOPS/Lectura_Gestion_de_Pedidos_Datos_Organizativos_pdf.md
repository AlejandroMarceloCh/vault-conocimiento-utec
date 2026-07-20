---
curso: SIOPS
titulo: Lectura - Gestión de Pedidos (Datos Organizativos)
slides: 15
fuente: Lectura - Gestión de Pedidos (Datos Organizativos).pdf
---

Proceso de Gestión de Pedidos
GBI actualmente utiliza un proceso muy simple para satisfacer las órdenes de los
clientes. Este proceso, se reproduce en la ​Figura 1. El proceso comienza cuando GBI
recibe el pedido de compra del cliente, el cual valida y autoriza a través de un pedido
de cliente. El almacén prepara y envía el despacho, después de lo cual Contabilidad
remite una factura. El proceso termina cuando GBI recibe el pago del cliente.




Figura 1: Proceso de gestión de pedidos básico

En esta lectura, se describe el proceso de gestión de pedidos en detalle, con especial
énfasis en cómo el sistema SAP ERP apoya el proceso. Se comienza identificando los
niveles organizativos clave y los datos maestros relacionados con los procesos. En
seguida se examinan las etapas del proceso en detalle y se explica cómo el proceso de
gestión de pedidos se integra a otros procesos. Se concluye describiendo varios
informes relacionados al proceso de gestión de pedidos. Esta sección no incluye
conceptos claves. La razón de esto es que los conceptos básicos asociados al proceso
de gestión de pedidos, tales como movimiento de mercancías, se han tratado en
lecturas previas.

Para ilustrar los conceptos y etapas del proceso, se usará el siguiente escenario. Rocky
Mountain Bikes (RMB), un cliente de GBI ubicado en Denver, Colorado, ha realizado un
pedido por 40 bicicletas de turismo de lujo plateadas y 100 camisetas que piensan
vender en dos carreras en Colorado Springs; una a realizar el 15 de Mayo y la otra el 20
de Junio. Debido a que inventariar y almacenar bicicletas representa un gasto
significativo, RMB desea que GBI le envíe las bicicletas directamente al lugar de la
carrera solo unos días antes de cada carrera. Además, RMB prevé que la carrera de
Mayo atraerá a muchas más personas, por lo que espera vender más bicicletas y
camisetas en esa carrera. De esta forma, solicitó a GBI entregar 30 bicicletas el 10 de
Mayo y las 10 restantes el 10 de Junio. Sin embargo, le pidió entregar las 100
camisetas en Mayo de manera de vender las más posibles en la primera carrera y
luego vender las restantes en la segunda carrera. A diferencia de las bicicletas, las
camisetas son relativamente baratas y fáciles de almacenar entre una carrera y otra.


    ​DATOS ORGANIZATIVOS
Varios elementos organizativos son esenciales para el proceso de gestión de pedidos.
Estos son mandante, sociedad, área de ventas, centro, almacén, puesto de expedición
y área de control de créditos. Tres de estas – área de ventas, puesto de expedición y
área de control de créditos son propias del proceso de gestión de pedidos. El área de
ventas es una combinación de otros tres elementos organizacionales – organización de
ventas, canal de distribución y sector –que son también propias del proceso de gestión
de pedidos. En esta sección se describen todos estos elementos organizacionales.

Algunos elementos—específicamente el mandante, sociedad, centro y almacén- son
también relevantes a otros procesos y se han discutido anteriormente. En esta sección
se ha incluido una descripción de centro y almacén toda vez que se relacionan
específicamente con el proceso de gestión de pedidos. No es necesaria una descripción
adicional del mandante y sociedad.


ORGANIZACIÓN DE VENTAS
Una empresa (sociedad) se divide en varias ​ORGANIZACIONES DE VENTAS​, cada una de
las cuales es responsable por la venta y distribución de cada producto y servicio en un
área geográfica particular, tales como mercados regionales o nacionales.
Específicamente, una organización de ventas es:

   ●   Responsable de negociar los términos y condiciones de venta en el mercado.

   ●   Responsable de los clientes con respecto a las obligaciones y derechos de
       recursos en caso de disputas.

   ●   El mayor nivel de agregación en informes relativos a ventas. Es decir, los datos
       de ventas se pueden resumir hasta el nivel de la organización de ventas.

Una sociedad debe tener al menos una organización de ventas, aunque podría tener
muchas. Esta última estructura es apropiada si los procesos de venta son
sustancialmente distintos en las diferentes organizaciones de ventas, por ejemplo,
para manejar diferencias regionales en prácticas y costumbres. En otros casos, una
empresa podría usar múltiples organizaciones de ventas simplemente para estar
seguro de que el área geográfica cubierta permanece manejable. Aunque la empresa
puede incluir múltiples organizaciones de ventas, una organización de ventas puede
pertenecer sólo a una sociedad. La organización de ventas para GBI se representa en la
Figura 2​. Tal como lo indica la figura, GBI US tiene dos organizaciones de ventas, una
para el Este y la otra para el Oeste de EE.UU. GBI de Alemania también tiene dos
organizaciones de ventas, una para el territorio Norte y otra para el territorio Sur.
Figura 2: Organizaciones de ventas de GBI

Procesos de Negocio en la Práctica 5.1: Estructura Organizacional de Intel
La Corporación Intel tiene 6 grupos operativos independientes que manufacturan
productos, cada uno de los cuales opera cuatro organizaciones de ventas:
Asia-Pacíﬁco, América, Europa, y Japón. Intel localiza sus organizaciones de ventas
cerca de sus agrupaciones de clientes más grandes. Cada una de las 24 organizaciones
de ventas, tiene dos canales de distribución directo y de revendedores. Así, existen 48
combinaciones a través de las cuales Intel vende globalmente sus productos a sus
clientes.

Fuente: Informes de la empresa Intel.

CANAL DE DISTRIBUCIÓN
Un ​CANAL DE DISTRIBUCIÓN (CD) ​es el medio por el cual la empresa distribuye sus
productos y servicios a sus clientes. Típicos canales son mayorista, minorista y en línea
(ventas por Internet). Así como una empresa puede tener muchas organizaciones de
ventas, también puede tener muchos CD. Cada canal tiene sus propias estrategias,
enfoques y restricciones para llevar los productos y servicios a los clientes. Más
específicamente, cada canal tiene responsabilidades, sistemas de precios, centros
propios desde los cuales se realizan los embarques y otras características. Por ejemplo,
un canal mayorista tiene las siguientes características (entre otras):

    ●   No incluye impuesto a las ventas al calcular los precios (en Estados Unidos.)

    ●   Requiere un volumen mínimo de compras y ofrece descuentos por volumen.

    ●   Puede designar un centro o centros específicos desde los que se realizan las
        entregas.
Además, la presentación de informes se puede consolidar al nivel de CD. Es decir, las
estadísticas se pueden resumir y agregar en base a un canal de distribución. Una
organización de ventas debe tener al menos un canal de distribución, aunque podría
tener más de uno. Asimismo, un canal de distribución puede ser asignado a múltiples
organizaciones de ventas.

Debido a que GBI es una empresa manufacturera, ha vendido históricamente sus
productos a través del canal mayorista. Sus clientes son minoristas quienes, a su vez,
venden los productos al cliente final. Recientemente, GBI ha comenzado a vender
directamente al cliente final a través de Internet. Aunque cualquier persona puede
acceder a la página web de GBI para comprar una bicicleta, factores como impuestos
complejos, gastos de envío y aranceles de importación hacen muy difícil a GBI operar
un canal de ventas global por Internet. Por lo tanto, GBI maneja los canales mayorista
e Internet juntos a nivel de país, tal como se ilustra en la ​Figura 3​. Esta política asegura
que la organización de ventas que envía el producto al cliente es también la
organización más familiarizada con las leyes tributarias para esa región.

Note que, aunque las cuatro organizaciones de ventas identificadas en la ​Figura 3
están involucradas con el comercio mayorista, solo dos están involucradas con ventas
por Internet. La organización de ventas del Oeste de EE.UU. gestiona las ventas por
Internet para todo Estados Unidos y la organización de ventas del Norte de Alemania
gestiona las ventas por Internet para toda Alemania. Si GBI se aventurase a vender a
minoristas en una fecha posterior, crearía un nuevo canal – minorista – para
administrar estas ventas toda vez que las estrategias para las ventas al por menor,
tales como precio, cantidades mínimas e impuestos, serán diferentes de los otros dos
canales.




Figura 3: Canales de distribución de GBI
La combinación única de organización de ventas y canal de distribución se llama
CADENA DE DISTRIBUCIÓN. ​Algunos datos maestros, tales como el maestro de
materiales y condiciones de precio, se mantienen al nivel de cadena de distribución.

Procesos de Negocio en la Práctica 5.2: Canales de Distribución de Apple
Apple Inc. presenta un buen ejemplo de una empresa que utiliza múltiples canales de
distribución. Vende sus productos a través de su tienda en línea (Internet), sus tiendas
Apple (ventas al por menor) y terceros minoristas (al por mayor). Apple usa cada uno
de estos canales para resolver diferentes problemas dentro del proceso de gestión de
pedidos.

Debido a que Apple da prioridad a la experiencia de compra del cliente, trata de
establecer ya sea una tienda minorista propiedad de Apple o una tienda minorista de
mercado masivo en cada uno de sus principales mercados. Esta política asegura que la
mayoría de los clientes en los países más desarrollados se ubiquen a corta distancia de
una tienda minorista que vende productos Apple.

Aunque las tiendas minoristas ofrecen la mejor oportunidad para que el cliente
examine los productos antes de comprarlos, mantener una extensa red de tiendas
físicas conlleva muchos gastos importantes, incluyendo bienes raíces, impuestos locales
y personal de venta. Por lo tanto, Apple evalúa muy cuidadosamente las nuevas
ubicaciones de sus tiendas basado principalmente en los datos demográficos locales de
los consumidores que son potenciales compradores.

Cuando no es factible para Apple establecer una tienda minorista en una zona con una
fuerte base de potenciales consumidores, la compañía tiene que asociarse con otra
tienda minorista que revenda sus productos. Aunque esta estructura elimina muchos de
los costos identificados anteriormente por Apple, también reduce su utilidad por
unidad, ya que debe compartir sus ingresos por venta con el revendedor.

Las ventas en línea eliminan gran parte de los costos asociados a las operaciones
físicas de la tienda. Además, debido a que el canal en línea vende directamente a los
consumidores, Apple no tiene que compartir sus utilidades con el revendedor. Sin
embargo, debido a que el minorista en línea vende a cualquier número de lugares
alrededor del mundo, tiene que lidiar con los costos de envío, de impuestos y de
importación que el canal de venta al por menor no tiene. Además, deben invertir en la
infraestructura técnica que apoya un sitio global minorista en línea. Las operaciones
minoristas en línea de Apple, incluyendo la tienda de Apple y iTunes, se basan en SAP
ERP.
Fuente: Informes de la empresa Apple.

SECTOR
La mayoría de las empresas combinan materiales y servicios con características
similares dentro de una unidad conocida como ​SECTOR​. Por lo general, cada sector se
asocia con la línea de productos de una empresa. Un producto o material puede ser
asignado solo a un sector. Cada sector puede emplear sus propias estrategias de
ventas, tales como acuerdos de precios con los clientes. Además, es posible consolidar
informes a nivel de sector.

Una organización de ventas debe tener al menos un sector. Un sector puede ser
asignado a múltiples organizaciones de ventas y una organización de ventas puede
tener muchos sectores.

Actualmente, GBI tiene dos sectores, el sector de bicicletas y el sector de accesorios.
Recuerde que la lista de materiales de GBI incluye diferentes tipos de materiales. Los
productos terminados—a saber, las bicicletas—son manejados por el sector de
bicicletas, mientras que las mercancías, como los cascos—son manejados por el sector
de accesorios. En el futuro, si GBI se expande a otras líneas de producto, tales como
skateboards, creará sectores adicionales. Los sectores para GBI EE.UU. y GBI DE se
ilustran en la​ ​Figura 4​ ​y 5, respectivamente.




Figura 4: Sectores de GBI en EE.UU.
Figura 5: Sectores de GBI en DE

Procesos de Negocio en la Práctica 5.3: Múltiples Sectores en una Gran
Empresa Editorial

John Wiley & Sons, empresa editora líder internacionalmente, tiene tres grandes
sectores que atienden diferentes mercados de lectores alrededor del mundo. Wiley
publica libros universitarios a través de su sector de Educación Superior. El sector
Profesional/Comercio contiene las series For Dummies, CliffsNotes, y los Diccionarios
Webster, como también otras marcas reconocidas. El tercer sector de Wiley es la
Científica, Técnica, Médica y Académica (STMS), la cual es la editora

más grande de revistas profesionales y académicas y de libros del mundo. Aunque los
productos físicos (libros y revistas) y las regiones geográficas son similares para los tres
sectores, la audiencia, autores, y canales de distribución para cada sector varían
enormemente. Wiley ha aprendido que agrupando sus marcas y los empleados que son
responsables de su éxito en los tres sectores, pueden lograr mayores sinergias y operar
más eficientemente.

Fuente: Reportes de la empresa John Wiley & Sons

ÁREA DE VENTAS
El ​ÁREA DE VENTAS ​es una combinación única de organización de ventas, canal de
distribución y sector. En otras palabras, define cúal canal de distribución utiliza una
organización de ventas para vender los productos asociados a un sector particular. Un
área de ventas puede ser asignada solo a una sociedad. Todos los documentos
asociados con el proceso de gestión de pedidos, tales como ofertas y listas de
embalaje, pertenecen a un área de ventas.

La ​Figura 6 ilustra las seis áreas de ventas para GBI EE.UU. Por ejemplo, un área de
ventas (UE00+WH+BI) es responsable por la venta de productos en el sector bicicletas
para la organización de ventas EE.UU. a través del canal comercio al por mayor. Esta
área de ventas se presenta en la figura. Una segunda área de ventas (UW00+WH+AS)
administra las ventas de productos en el sector de accesorios de la organización de
ventas EE.UU. Oeste a través del canal mayorista. Como tercer ejemplo, el área de
ventas UW00+IN+BI administra las ventas de productos en el sector bicicletas de la
organización de ventas EE.UU. Oeste a través del canal de distribución de Internet. La
empresa alemana también tiene seis áreas de ventas. Sin embargo, estas no se
muestran en la figura.




Figura 6: Áreas de ventas de GBI

Procesos de Negocio en la Práctica 5.4: La Estructura de Ventas de Apple

Como se discutió en un ejemplo previo, Apple vende sus productos a través de una
combinación de tiendas en línea, tiendas minoristas y revendedoras. Apple tiene varios
sectores de hardware, incluyendo los computadores Mac, iPods, iPhones, servidores, y
accesorios. Apple también opera varias áreas de ventas para diferentes tipos de
clientes, tales como educacionales, gobierno, empresas, y consumidores. Cada uno de
estos segmentos de clientes tiene sus propias necesidades y requiere un método de
vender distinto, aunque ellos estén comprando los mismos productos. Por lo tanto,
Apple debe planificar sus estrategias de ventas por producto en forma global aunque
poniendo mucha atención a las características únicas de los canales de distribución
(minorista, en línea y revendedor) y a sus clientes (educacionales, gobierno, empresas, y
consumidores). Esta estrategia se refleja en una matriz, la cual permite a Apple
identificar oportunidades y manejar sus esfuerzos de venta global efectivamente.

Fuente: Reportes de la empresa Apple

CENTRO
Se ha descrito los centros en el contexto de otros procesos. En el proceso de gestión
de pedidos un centro suministrador es una instalación desde la cual la empresa
entrega sus productos y servicios a sus clientes. En el caso de productos, un centro es
típicamente una instalación de almacenamiento o manufactura. En el caso de los
servicios, puede ser simplemente una oficina. Un centro se puede asignar a más de un
canal de distribución. Recuerde que una cadena de distribución es una combinación
única de una organización de ventas y un canal de distribución. A la inversa, una
cadena de distribución puede estar asociada a más de un centro.

En la ​Figura 7​, el centro 1 entrega solo a la cadena de distribución 1 y el centro 3 solo a
la cadena de distribución 3. En cambio, el centro 2 entrega a las tres cadenas de
distribución. Visto desde una perspectiva diferente, las cadenas de distribución 1 y 3
usan dos centros para entregar materiales a sus clientes, mientras que la cadena de
distribución 2 usa solo un centro.

Recuerde que GBI tiene tres centros en los Estados Unidos y dos en Alemania. En
Estados Unidos, el centro de Dallas es solo de manufactura, mientras que los centros
de San Diego y Miami sirven como centros de distribución. Los productos terminados
se despachan desde la instalación de Dallas hacia las otras dos instalaciones según se
necesite. Al contrario, las mercancías se entregan directamente a los dos centros de
distribución regional a través de los proveedores. El centro de Dallas no mantiene
stock de mercancías. Normalmente, el centro de Miami entrega productos a los
clientes en el Este de Estados Unidos y el de San Diego en el Oeste de Estados Unidos.
Sin embargo, el centro de Dallas sirve como una instalación de excedentes para los
otros centros y puede despachar productos terminados a cualquier parte en el país,
según se necesite. En Alemania, el centro de Heidelberg despacha a los locales en el
Sur y el centro de Hamburg a locales en el Norte.
Figura 7: Centros

PUESTO DE EXPEDICIÓN
Un ​PUESTO DE EXPEDICIÓN ​es un lugar en un centro desde el cual se despachan las
entregas de salida. Este puede ser una ubicación física, tal como un muelle de carga,
una estación de tren, o una sala de correo. Puede ser también un grupo de empleados
designados quienes, por ejemplo, maneja entregas rápidas o despachos especiales. Un
puesto de expedición se asocia a uno o más centros, y un centro puede tener más de
un punto de expedición. Un centro debe tener al menos un puesto de expedición
desde el cual procesar entregas, aunque un puesto de expedición no tiene que estar
localizado físicamente dentro de un centro.

La ​Figura 8 ​diagrama un escenario en el cual múltiples centros acceden a un puesto de
expedición. La figura representa un campus de una empresa que incluye una fábrica y
dos instalaciones de almacenamiento, todas las cuales son centros. Note que el único
centro que tiene un puesto de expedición es la instalación de almacenamiento
localizada en la oficina. Por lo tanto, todos los materiales de la fábrica y de la
instalación de almacenamiento principal se tienen que mover primero a esta
instalación y después despacharse a sus destinos.

Al contrario, la ​Figura 9 ​ilustra un escenario en el cual algunos centros comparten tres
puestos de expedición. La instalación de almacenamiento #1 tiene un puesto de
expedición, y la instalación #3 tiene dos. La instalación de almacenamiento #2 no tiene
ninguno, entonces utiliza los puestos de expedición ubicados en otros centros. En la
instalación de almacenamiento #3, uno de los puestos de expedición maneja las
entregas regulares, mientras que la otra se reserva para entregas rápidas o para
entregas que requieren un manejo especial.
Figura 8: Puestos de expedición compartidos




Figura 9: Puestos de expedición múltiples

En GBI, cada uno de los cinco centros tiene un único puesto de expedición. Todas las
entregas de los clientes se despachan desde una de estas ubicaciones. Cada puesto de
expedición es un muelle de carga, el cual es una instalación en que los camiones
pueden retroceder para ser cargados. La Figura 10 ilustra un muelle de carga. Otras
instalaciones que pueden operar como puestos de expedición incluyen las estaciones
de tren (​Figura 11​) y los astilleros o puertos (​Figura 12​). En el caso de una estación de
tren, los vagones se acercan a la instalación y se cargan. Cuando la instalación de
almacenamiento se ubica cerca de una vía navegable, un astillero sirve al mismo
propósito.




Figura 10: Un muelle de carga como puesto de expedición. ©iStockphoto




Figura 11: Una estación de tren como puesto de expedición. ©iStockphoto
Figura 12: Un puerto como puesto de expedición. ©iStockphoto

ÁREA DE CONTROL DE CRÉDITOS
Un ​ÁREA DE CONTROL DE CRÉDITOS es el nivel organizativo responsable por los
créditos de los clientes. Específicamente, determina la solvencia de los clientes,
establece el límite de crédito y monitorea y maneja las prórrogas de crédito de los
clientes. Una empresa puede elegir manejar el crédito ya sea de forma centralizada o
descentralizada. En un sistema centralizado, una única área de control de créditos
maneja el crédito para los clientes a través de todas las sociedades de una empresa
global. Este arreglo es particularmente útil si los clientes conducen negocios con
múltiples sociedades dentro de una empresa global. La ​Figura 13 ilustra un modelo
centralizado que GBI utiliza para los clientes que compran bicicletas y accesorios de
GBI EE.UU y DE. En estos casos, GBI maneja el límite de crédito a nivel de empresa, lo
que significa que asigna todas las sociedades a una sola área de control de créditos.
Figura 13: Área de control de créditos centralizada
En contraste, una empresa global que utiliza un modelo descentralizado mantiene
múltiples áreas de control de créditos, cada una de las cuales maneja el crédito para
una o más empresas dentro de una empresa global. Por ejemplo, en el hipotético
escenario ilustrado en la Figure 5-14, GBI tiene dos áreas de control de créditos, una
para todas las empresas en Norte América (GBI EE.UU., GBI Canadá, y GBI México) y
una para todas las empresas en Europa (GBI Alemania y GBI Gran Bretaña). Si GBI
expandiera sus operaciones a la región Asia-Pacífico, probablemente creará una
tercera área de control de créditos para supervisar el crédito de los clientes de estas
empresas. Incluso cuando se usa un enfoque descentralizado, sin embargo, es
posible—y prudente—establecer límites de crédito para clientes a nivel de la empresa
global y para cada área de control de créditos. Esta política asegura que las compras de
empresas pertenecientes a diferentes áreas de control de créditos (por ejemplo GBI
EE.UU. y GBI DE en la Figura 14) no excedan el límite de crédito en toda la empresa
global.
La Figura 14: Área de control de créditos descentralizada
