---
curso: SIOPS
titulo: Lectura - El Proceso de Planificacion de Materiales
slides: 40
fuente: Lectura - El Proceso de Planificacion de Materiales.pdf
---

                                                                         CAPÍTULO 8

                        El Proceso de Planificación de Materiales
La planificación de materiales está relacionada con la respuesta a tres preguntas básicas:
(1) ¿Qué materiales se solicitan?, (2) ¿cuántos se solicitan? y (3) ¿cuándo se solicitan?
La incapacidad de responder a cualquiera de estas tres preguntas con precisión dará lugar a
ineficiencias, pérdida de ingresos y la insatisfacción de los clientes. El principal objetivo de
la planificación de materiales es balancear la demanda de materiales con el suministro de
materiales y así disponer de una cantidad apropiada de materiales cuando estos se necesiten.

La primera parte de esta ecuación –la demanda de materiales –es motivada
mayoritariamente por otros procesos. Por ejemplo, el proceso de gestión de pedidos utiliza
mercaderías y productos terminados y el proceso de producción utiliza materias primas y
productos semielaborados. Si los materiales no están disponibles cuando se necesitan, estos
procesos no funcionarán efectivamente. Por ejemplo, si las materias primas no están
disponibles, entonces la empresa no puede fabricar productos terminados de manera
oportuna. Por consiguiente, será incapaz de cumplir con los pedidos de cliente porque no se
tienen los materiales necesarios en stock. Esta situación se conoce como desabastecimiento.
Un desabastecimiento puede provocar pérdida de ventas si los clientes no están dispuestos
a aceptar despachos tardíos.

La parte suministro de la ecuación oferta-demanda es, normalmente, dominio de los
procesos de aprovisionamiento y producción. Es decir, los materiales generalmente se
compran o se fabrican. Comprar o fabricar más materiales de los que sean necesarios causará
un exceso de stock, lo cual inmoviliza el efectivo hasta que dichos materiales sean
eventualmente utilizados. El dinero invertido en stock representa un costo de oportunidad
para la empresa. Costos adicionales se relacionan con el costo de almacenamiento, seguros
y el riesgo de obsolescencia. Además, el valor de algunos materiales, tales como componentes
de un computador, p.e., memoria y discos duros, pueden disminuir rápidamente. Así,
mientras más tiempo permanezcan los materiales en la bodega, mayor será la cantidad de
dinero que la empresa pierda.

Un proceso simplificado de planificación de materiales se presenta en la Figura 8-1. El
proceso comienza con la planificación de ventas y operaciones (SOP), el cual utiliza objetivos
estratégicos de ingresos y ventas establecidos por la alta gerencia para crear planes de
operaciones específicos. La etapa de gestión de demanda traduce estos planes en necesidades
de materiales individuales. Las necesidades especifican cuántos de estos materiales se
necesitan y cuándo. Estas solicitudes se utilizan en la etapa de planificación de necesidades
(MRP, del inglés material requirements planning) para generar la propuesta final de pedidos
de todos los materiales. Estas propuestas ejecutan los procesos de producción o
aprovisionamiento que fabrican o compran los materiales que se necesitan. Por último, la
empresa utiliza estos materiales para ejecutar el proceso de gestión de pedidos.




Figura 8-1: Proceso básico de planificación de materiales

Los datos organizativos relevantes para el proceso de planificación de materiales son
mandante, sociedad, centro y almacén. Debido a que todos estos conceptos se han
considerado en los capítulos previos, no se abordarán en este capítulo. La siguiente sección
describe los datos maestros relacionados con el proceso de planificación de materiales. Esta
sección continúa con una discusión detallada de las etapas del proceso. Se concluye el
capítulo con una discusión de los informes relacionados con la planificación de materiales.

   DATOS MAESTROS
Los datos maestros relevantes para la planificación de materiales son la lista de materiales,
la hoja de ruta de producto, el maestro de materiales y el grupo de productos. Se discutió en
detalle la lista de materiales y hoja de ruta de producto en el Capítulo 6. Recuerde que los
materiales se utilizan en casi todos los procesos y que los datos del maestro de materiales se
agrupan por procesos, tipo de material y nivel organizativo. También se ha discutido varios
datos (vistas) del maestro de materiales en capítulos previos. En el Capítulo 6, se introdujo
las vistas MRP y preparación de trabajo, pero no se examinaron en profundidad. En esta
sección se discutirán estas vistas más ampliamente ya que son más relevantes en la
planificación de los materiales. Además, se discutirán los grupos de producto toda vez que
se relacionan con la planificación de materiales.

MAESTRO DE MATERIALES
Los datos relacionados con MRP y preparación de trabajo se presentan en la Figura 8-2. Los
datos MRP pueden ser bastante extensos. Por consiguiente, se dividen en cuatro vistas o
pestañas, MRP 1, MRP 2, MRP 3 y MRP 4, para que los datos sean más fáciles de leer. Estos
datos son relevantes tanto para la fabricación discreta como repetitiva (explicado en el
Capítulo 6). Esta discusión se limita a los datos relevantes para la fabricación discreta. Los
datos de MRP y preparación de trabajo se definen a nivel de centro. Esto significa que son
específicos para cada centro. Estos datos determinan qué estrategias y técnicas utilizará la
empresa cuando planifique los materiales. Cada vista MRP proveerá un conjunto específico
de datos, tal como lo indica la siguiente lista:




Figura 8-2: Datos del maestro de materiales para la planificación de materiales

       •   La vista MRP 1 define la estrategia global de planificación utilizada para los
           materiales y determina cuántos materiales debería adquirir la empresa.

       •   La vista MRP 2 identifica los tiempos que el sistema puede utilizar para
           programar y comunicar datos que el sistema utiliza para determinar cómo
           obtener materiales (fabricar versus comprar).

       •   La vista MRP 3 identifica la estrategia que el sistema utilizará para calcular
           cuántos materiales están disponibles, y determina cómo se fabricará el material.

       •   La vista MRP 4 contiene los datos que el sistema utiliza para seleccionar la lista
           de materiales (LMat) correcta.

La vista de preparación de trabajo contiene los datos que determinan el tiempo de
fabricación tales como tiempo de preparación, el desmontaje y el tiempo de tratamiento.
Estos tiempos se discutieron en el Capítulo 6 en el contexto de los puestos de trabajo.
La siguiente sección presenta una discusión detallada de los datos claves incluidos en las
vistas MRP y preparación de trabajo del maestro de materiales.

Clase de Aprovisionamiento
La salida del proceso de planificación de materiales es una, o más propuestas de pedido, las
que pueden ejecutar ya sea procesos de producción o aprovisionamiento. La CLASE DE
APROVISIONAMIENTO indica si el material es de fabricación propia o se fabrica internamente (vía
el proceso de producción) o se obtiene externamente (vía el proceso de aprovisionamiento),
ambos, o ninguno. Las mercaderías y las materias primas se compran generalmente a los
proveedores. Por consiguiente, la clase de aprovisionamiento para dichos materiales se
especifica como externo. Por el contrario, los productos terminados y semielaborados se
fabrican generalmente en la empresa. Como resultado, la clase de aprovisionamiento para
este tipo de materiales es, normalmente, de fabricación propia. En ocasiones, sin embargo,
cuando una empresa no tiene materiales u otros recursos para fabricar materiales de manera
interna, los compra externamente. En tales casos, la clase de aprovisionamiento se establece
como ambos. La clase de aprovisionamiento ninguno es apropiado para materiales
descontinuados.

En GBI, la clase de aprovisionamiento se define como ambos para productos terminados,
como externo para mercaderías y materias primas y fabricación propia para productos
semielaborados.

Característica de Planificación de Necesidades
La CARACTERÍSTICA DE PLANIFICACIÓN DE NECESIDADES especifica la técnica de control de
producción utilizada en la planificación. Las técnicas de control de producción comunes son
planificación de necesidades sobre consumo, planificación de necesidades de material14 (MRP)
y plan maestro de producción (MPS). La característica de planificación de necesidades se
puede establecer también como “sin planificar”, en cuyo caso los materiales no se incluyen
en el proceso de planificación.

La PLANIFICACIÓN DE NECESIDADES SOBRE CONSUMO calcula las necesidades de un material basado
en los datos de consumo histórico. Manipula estos datos para proyectar o pronosticar un
consumo futuro. La empresa entonces obtiene materiales en base a esta proyección. La
Figura 8-3 muestra un tipo de planificación de necesidades sobre consumo denominada
planificación de necesidades por punto de pedido. El eje vertical representa el stock o nivel de
stock y el eje horizontal indica los periodos de tiempo relevantes. Note que el nivel de stock
disminuye constantemente en el tiempo. La línea diagonal que representa los cambios en el
nivel de stock es la línea de consumo.
Figura 8-3: Planificación de necesidades por punto de pedido

La Figura 8-3 también indica el STOCK DE SEGURIDAD, el cual es el nivel mínimo de stock
deseado. Un desabastecimiento ocurrirá si la empresa tiene insuficiente stock para satisfacer
un pedido de cliente o para fabricar un producto terminado. Como se discutió anteriormente
en este capítulo, un desabastecimiento puede provocar una fabricación insuficiente y
pérdida de ventas. En consecuencia, una empresa normalmente mantiene un stock de
seguridad para evitar esta situación. El proceso de planificación de materiales monitorea los
niveles de existencias para evitar que caigan por debajo del stock de seguridad. El stock de
seguridad se especifica en el maestro de materiales.

Para prevenir que los niveles de stock disminuyan por debajo de los niveles de stock de
seguridad, la empresa debe recibir un suministro de materiales en el momento en que el
nivel de stock alcance el nivel de seguridad (punto A en la figura). Toma algún tiempo
procesar un pedido y recibir un despacho. El intervalo de tiempo entre realizar un pedido –
la fecha de pedido en la figura –y recibir los materiales –la fecha de entrega en la figura – se
denomina tiempo de re-aprovisionamiento. Para asegurar que la empresa recibe los
materiales en la fecha de entrega deseada, debe realizar el pedido con anticipación con el fin
de darle al proveedor tiempo suficiente para entregar los materiales.

La mayoría de las empresas consideran más valioso determinar cuándo realizar un pedido
en términos de nivel de stock que en términos de un punto en el tiempo. Específicamente,
estas realizan pedidos de materiales cuando el nivel de stock alcanza un nivel
predeterminado, conocido como punto de pedido. El punto de pedido se calcula dibujando
una línea vertical desde la fecha de pedido a la línea de consumo (hasta el punto B) y después
una línea horizontal al eje vertical (hasta el punto C).

Las otras dos grandes categorías de planificación de necesidades sobre consumo, son la
planificación estocástica y la planificación periódica. La planificación estocástica utiliza los
datos históricos para estimar o pronosticar futuros consumos. Las organizaciones utilizan el
pronóstico para determinar cuándo realizar un pedido de materiales. La ventaja de esta
técnica por sobre la planificación de necesidades por punto de pedido es que puede
considerar los patrones de consumo que son más complejos que una línea de tendencia. La
planificación periódica es similar a la planificación estocástica. Se utiliza en casos en donde
los proveedores despachan solo en días específicos de la semana.

Pese a lo específico de la técnica, la planificación de necesidades sobre consumo es
relativamente simple comparada con la planificación de necesidades de material. Asume que
el consumo futuro seguirá el mismo patrón que en el pasado. Además, no toma en cuenta las
dependencias entre los distintos materiales. Por ejemplo, la necesidad de ruedas depende de
la necesidad de fabricar bicicletas. En este caso, la planificación de necesidades sobre
consumo no es apropiada. Esto es porque la necesidad de ruedas no se basa en su consumo
anterior; en vez de esto, se basa en la necesidad de fabricar bicicletas. Las empresas
generalmente reservan la planificación de necesidades sobre consumo para los materiales
de bajo valor o importancia, tales como tuercas y tornillos.

GBI utiliza la planificación de necesidades sobre consumo para materiales clasificados como
accesorios, por ejemplo, los cascos de bicicleta (OHMT1000). La Figura 8-4 presenta el
escenario de planificación para obtener cascos. En este ejemplo el tiempo de
reaprovisionamiento es de 3 días y el stock de seguridad es de 50 unidades. La línea de
consumo, calculada a partir de los datos históricos de ventas, proyecta que el stock llegará al
nivel de stock de seguridad el día 7 (punto A). Para asegurarse de que los cascos lleguen en
la fecha estipulada, GBI debe iniciar el proceso de aprovisionamiento el día 4 (7 menos el
tiempo de reaprovisionamiento), la fecha de pedido. El punto de pedido se calcula dibujando
una línea desde la fecha de pedido a la línea de consumo (al punto B) y después una línea
horizontal al eje vertical (al punto C). Así, GBI debe realizar un pedido por cascos cuando
queden 125 o menos en stock.




Figura 8-4: Ejemplo de planificación de necesidades por punto de pedido
A diferencia de la planificación de necesidades sobre consumo, la técnica MRP calcula las
necesidades de material en base a su dependencia de otros materiales. Para comprender las
especificidades de la técnica MRP, primero se deben considerar dos conceptos relacionados,
necesidades primarias y secundarias. Los términos secundaria y primaria se refieren a la
fuente de necesidades. Un material tiene una NECESIDAD SECUNDARIA si su necesidad es
dependiente de las necesidades de otro material. Por ejemplo, una bicicleta se fabrica a partir
de varios componentes tales como ensambles de rueda y un asiento. La necesidad de
ensambles de ruedas y asientos es dependiente de la necesidad de bicicletas. Por lo tanto, los
ensambles de rueda y asientos tienen una necesidad secundaria. Generalmente, los
productos semielaborados (p.e., ensambles de rueda) y las materias primas (p.e., asientos)
tienen necesidades secundarias porque se utilizan para fabricar otros materiales (productos
terminados u otros productos semielaborados). Por el contrario, la necesidad de bicicletas,
un producto terminado, no es dependiente de ningún otro material. En su lugar, se basa en
la demanda de los clientes. De este modo, las bicicletas, y los productos terminados en
general, tienen NECESIDADES PRIMARIAS.

La técnica MRP se utiliza para calcular y planificar necesidades de materiales en todos los
niveles de la LMat. Este procedimiento, conocido como explosión de la LMat, se presenta en
la Figura 8-5. La entrada a MRP es la necesidad primaria para los productos terminados, los
cuales se calculan en la etapa de planificación de ventas y operaciones del proceso de
planificación de materiales. Se examinará esta técnica con mayor detalle en la sección de
proceso de este capítulo. Por ahora, es suficiente comprender que las necesidades primarias
se determinan en base a los pronósticos y venta actuales. Estas necesidades calculadas se
denominan NECESIDADES PRIMARIAS PLANIFICADAS. Por el contrario, los pedidos de cliente
actuales se conocen como NECESIDADES PRIMARIAS DE CLIENTE, o simplemente necesidades de
cliente. Las necesidades primarias planificadas manejan los cálculos de las necesidades para
cada nivel sucesivo en la LMat. Más aún, las necesidades para cada nivel son dependientes
de las necesidades de los niveles superiores del material. Por ejemplo, si las necesidades
primarias planificadas por bicicletas son 100 y cada bicicleta utiliza 2 ensambles de rueda y
1 asiento, entonces el cálculo de MRP creará necesidades secundarias de 200 ensambles de
ruedas y 100 asientos.

Una variación de MRP es el PLAN MAESTRO DE PRODUCCIÓN (MPS) el cual utiliza un proceso similar
a MRP pero enfocado exclusivamente en las necesidades de los ítems de nivel superior de la
LMat. Las empresas utilizan MPS para los productos terminados más críticos y así asegurar
que los recursos y las capacidades estén disponibles para estos materiales antes de que se
planifique para otros materiales. MPS es una etapa opcional del proceso de planificación y es
normalmente seguido por MRP, el cual completa el proceso de planificación para los
materiales restantes.
Figura 8-5: MRP versus MPS

Clave de Tamaño de Lote
Un TAMAÑO DE LOTE es la cantidad de materiales que se especifica en las propuestas de pedidos
generadas en el proceso de planificación de materiales. La CLAVE DE TAMAÑO DE LOTE especifica
el procedimiento que se utiliza para determinar el tamaño del lote. Existe una variedad de
procedimientos disponibles para determinar el tamaño del lote. Los procedimientos más
básicos son; cálculos estocásticos de tamaño de lote, el cual especifica una cantidad fija
basada ya sea en un valor predeterminado (tamaño de lote fijo) o en la cantidad exacta
necesaria (lote por lote). Por ejemplo, cuando se utiliza el procedimiento lote por lote, si las
necesidades calculadas para los asientos son 100, entonces la cantidad propuesta del pedido
es también 100. Los cálculos periódicos de tamaño de lote combinan las necesidades de
múltiples periodos de tiempo, tales como días o semanas, en un solo lote. El cálculo del
tamaño de lote óptimo toma en cuenta los costos de pedir y almacenar los materiales
utilizando técnicas tales como cálculos de cantidad económica de pedido y lote económico de
producción. Por ejemplo, si las necesidades calculadas de asientos son 100, la cantidad
propuesta del pedido puede ser 500 si es más económico comprar los asientos en mayor
cantidad. GBI utiliza el procedimiento de lote por lote para determinar el tamaño de lote de
todos sus materiales.

Tiempos de Planificación
Una tarea que se debe realizar en el proceso de planificación es estimar el tiempo requerido
para comprar los materiales necesarios. Este cálculo se basa en estimaciones del tiempo
requerido para realizar varias tareas que se incluyen en el maestro de materiales y en la hoja
de ruta del producto. Estimaciones de tiempo común incluyen:

        •   Tiempo de fabricación propia, el cual es el tiempo necesario para fabricar
            materiales internamente.
        •   Plazo de entrega previsto, el cual es el tiempo necesario para obtener los
            materiales si se adquieren externamente.

        •   Tiempo de tratamiento de EM (entrada de mercancías), el cual es la cantidad de
            tiempo necesario para situar los materiales recibidos en bodega, de modo que
            puedan estar listos para su utilización.

El tiempo de fabricación propia y el tiempo de tratamiento de EM se utilizan para determinar
el tiempo de aprovisionamiento de los materiales que se obtienen internamente. Para los
materiales aprovisionados externamente se utiliza el plazo de entrega previsto y el tiempo
de tratamiento de EM.

El tiempo de fabricación propia se divide además en tres elementos de tiempo: preparación,
tratamiento y tránsito. Recuerde la discusión de algunos de estos elementos del Capítulo 6.

        •   El tiempo de preparación es el tiempo requerido para instalar los puestos de
            trabajo utilizados para la fabricación.

        •   El tiempo de tratamiento es el tiempo requerido para completar las operaciones
            en los puestos de trabajo.

        •   El tiempo de tránsito es el tiempo requerido para trasladar los materiales desde
            un centro de trabajo a otro.

Los tiempos pueden ser dependientes o independientes del tamaño de lote. Los tiempos
independientes del tamaño de lote permanecen igual sin importar la cantidad de material que
está siendo adquirido. En cambio, los tiempos dependientes del tamaño de lote varían de
acuerdo al tamaño del lote o cantidad. Ejemplos de tiempos independientes del tamaño de
lote son el tiempo de preparación, de fabricación propia y de tratamiento de EM. Por el
contrario, el tiempo de tratamiento es generalmente dependiente del tamaño de lote.

El tiempo de fabricación propia independiente del tamaño de lote es una estimación del
tiempo total necesario para la fabricación incluyendo los tiempos de preparación,
tratamiento y tránsito. Aunque el tiempo de tratamiento normalmente depende del número
de unidades que se fabrican, el tiempo de fabricación propia independiente del tamaño de
lote se utiliza cuando (1) el tamaño de lote es fijo, así el tiempo de tratamiento es constante,
o (2) el tiempo de tratamiento es muy breve comparado con los tiempos de preparación y
tránsito. Cuando el tiempo de tratamiento es grande en comparación con los tiempos de
preparación y tránsito, o cuando la cantidad de material a fabricar varía, se calcula un tiempo
de fabricación propia dependiente del tamaño de lote utilizando los tres elementos de
tiempo (preparación, tratamiento y tránsito).

Debido a que las empresas utilizan estas diversas estimaciones de tiempo en el proceso de
planificación para programar el aprovisionamiento y la producción, los valores inexactos
causarán problemas significativos. Las programaciones inexactas requieren intervención
manual, y, si los usuarios encuentran que no pueden confiar en los datos del sistema, ellos
aprenderán a ignorarlos y crear sus propias soluciones. De este modo, es imperativo que una
organización analice cuidadosamente y monitoree sus procesos para determinar los tiempos
de programación.

Horizonte de Planificación Fijo
El proceso de planificación de materiales, a menudo, tiene que ajustar las cantidades y
programaciones que crea para las propuestas de pedido. Por ejemplo, el consumo de materia
prima puede ser inesperadamente alto debido a una demanda mayor a la esperada. En tales
casos el proceso de planificación puede incrementar las cantidades planificadas de
aprovisionamiento, o puede programarlas para que los materiales lleguen antes. Los
cambios en las propuestas de pedidos de largo plazo, generalmente, no son una gran
preocupación, pero los cambios en las propuestas de corto plazo pueden causar problemas
debido a que otros departamentos o procesos de la organización pueden tener incorporadas
las propuestas originales en sus planificaciones. Por esta razón, las empresas establecen un
periodo de tiempo dentro del cual no le está permitido al sistema ERP cambiar
automáticamente las propuestas de pedido. Este periodo de tiempo se conoce como
HORIZONTE DE PLANIFICACIÓN FIJO. Si el horizonte de planificación fijo es de 30 días, por ejemplo,
entonces las solicitudes de pedido con fecha de 30 días o menos desde la fecha actual no se
podrán cambiar de forma automática mediante el sistema. Si se necesitan cambios, estos se
deben realizar manualmente.

Método de Selección de LMat
Recuerde del Capítulo 6 que una lista de materiales (LMat) identifica los materiales
necesarios para fabricar un producto terminado. En algunos casos un simple material puede
tener múltiples LMat. Por ejemplo, una empresa puede utilizar diferentes LMat para
diferentes centros o diferentes tamaños de lote. Las empresas también generan múltiples
LMat cuando actualizan sus productos. Por ejemplo, si GBI planea actualizar el modelo de la
bicicleta de turismo con una nueva llanta a partir del 1 de enero, entonces debe crear con
antelación una nueva LMat para la bicicleta con fecha de validez a partir del 1 de enero. Al
mismo tiempo, se debe establecer el 31 de diciembre como fecha de término de la validez de
la LMat actual.

Debido a que pueden existir varias LMat para el mismo material, el sistema ERP debe tener
un método para determinar cuál LMat utilizar. El MÉTODO DE SELECCIÓN DE LA LMAT en el maestro
de materiales identifica el criterio que el sistema ERP debería utilizar para seleccionar la
LMat. Ejemplos de criterio son el tamaño de lote y la fecha de validez.

Grupo de Verificación de Disponibilidad
El GRUPO DE VERIFICACIÓN DE DISPONIBILIDAD define la estrategia que el sistema utiliza para
determinar si la cantidad de un material estará disponible en una fecha específica. El método
más común, denominado ATP (available-to-promise), considera un amplio rango de
elementos representando el suministro y la demanda del material. Los elementos de
suministro incluyen el stock existente, las solicitudes de pedido, los pedidos de compra y las
órdenes de fabricación. Los elementos de demanda incluyen reservas de material, stock de
seguridad y pedidos de cliente. El grupo de verificación de disponibilidad informa al sistema
qué elementos de suministro y demanda tomar en cuenta al momento de determinar la
disponibilidad. Dado que la disponibilidad de materiales concierne a muchas partes de una
organización, el grupo de verificación de disponibilidad se utiliza en múltiples procesos. Por
ejemplo, el proceso de gestión de pedidos lo utiliza para asegurar que los materiales se
puedan entregar al cliente en la fecha requerida y el proceso de producción lo utiliza para
asegurar que los materiales estén disponibles antes que las órdenes de fabricación sean
liberadas.

Grupo de estrategias
El GRUPO DE ESTRATEGIAS específica las estrategias de planificación de alto nivel utilizadas en
producción. Las estrategias de planificación de la producción caen en tres grandes
categorías: “fabricación contra stock”, “fabricación contra pedido” y “montaje según catálogo”.
Se presentó las primeras dos estrategias en el Capítulo 6, en el contexto del proceso de
producción. Procesos de Negocio en la Práctica 6-2 en ese capítulo presenta ejemplos de
cómo Dell y Apple utilizan estrategias de fabricación contra pedido y fabricación contra
stock, respectivamente. En esta sección, se extenderá la discusión de estas estrategias de
planificación.

En la estrategia FABRICACIÓN CONTRA STOCK (MTS), los pedidos de los clientes se cumplen usando
un stock existente de productos terminados. La estrategia MTS la emplean generalmente las
empresas que fabrican grandes volúmenes de productos idénticos. Esta estrategia reduce el
tiempo requerido para cumplir los pedidos de cliente porque no hay necesidad de esperar
hasta que los materiales se fabriquen. Además, permite a la empresa fabricar bienes a un
ritmo constante y con tamaños de lote óptimos, independiente de la demanda de los clientes.
En SAP ERP, la estrategia más simple de fabricación contra stock es la planificación de
necesidades netas (estrategia 10), en la cual el sistema genera propuestas de pedidos en base
a necesidades primarias planificadas calculadas sin preocuparse de las necesidades
primarias de cliente.

Una variante común de la estrategia de fabricación contra stock es la planificación con
montaje final (estrategia 40). Esta estrategia también se basa en necesidades primarias
planificadas. A diferencia de la estrategia MTS, sin embargo, esta aproximación toma en
cuenta los actuales pedidos de cliente a través de un procedimiento denominado
compensación. Se discutirá los modos de compensación en la siguiente sección.

A diferencia de MTS, en una estrategia de FABRICACIÓN CONTRA PEDIDO (MTO) la fabricación de
productos terminados y de cualquier producto semielaborado necesario se desencadena por
pedidos de cliente. La empresa no mantiene un stock de estos productos. A MTO también se
le denomina fabricación basada en pedidos de cliente. A diferencia de MTS, MTO se utiliza
cuando cada producto es único. Por ejemplo, si GBI introduce una línea de bicicletas de
carrera de alto desempeño diseñadas individualmente para cada ciclista, utilizaría MTO para
estos productos. Las bicicletas no se fabricarían hasta que se recibiera un pedido.
Una variación de la estrategia MTO es MONTAJE SEGÚN CATÁLOGO (ATO), en el cual se aprovisiona
o fabrica una cantidad de componentes (productos semielaborados) necesarios para fabricar
productos terminados para mantener en stock. La fabricación de productos terminados se
desencadena por los pedidos de cliente y, por lo tanto, utiliza una estrategia MTO. ATO se
emplea generalmente en ambientes en donde hay un gran número de configuraciones
posibles de elementos finales. Por ejemplo, es posible crear diferentes configuraciones de
computador utilizando distintas opciones de monitores, dispositivos de almacenamiento y
memoria. Un pedido de cliente por productos terminados se puede cumplir, por lo general,
rápidamente porque solo se tiene que ejecutar el montaje final. (Los componentes ya están
en stock). En SAP ERP, la estrategia ATO también se conoce como planificación sin montaje
final (Estrategia 50) o preplanificación de conjuntos. Las variaciones de las estrategias MTO
y MTS ofrecen mayor flexibilidad para satisfacer las necesidades de los clientes.

Modo de compensación
Un punto clave que surge de la discusión de los grupos de estrategias es que la estrategia de
planificación determina la manera en la cual interactúan necesidades primarias planificadas
y necesidades primarias de cliente (pedidos reales de cliente). Por otro lado, en una
estrategia MTS tal como la planificación de necesidades netas, necesidades primarias de
cliente y necesidades primarias planificadas son independientes unas de otras y las
propuestas de pedidos generadas por el proceso de planificación de materiales se basan
únicamente en necesidades primarias planificadas. Las necesidades primarias de cliente se
cumplen en su totalidad mediante el stock existente. Por otro lado, bajo el enfoque de la
planificación con montaje final, las propuestas de pedidos toman en cuenta las necesidades
primarias planificadas y necesidades primarias de cliente. Sin embargo, las propuestas de
pedidos no se crean simplemente sumando la cantidad de necesidades primarias
planificadas y necesidades primarias de cliente. Esto se debe a que las necesidades primarias
planificadas se crean anticipándose a los pedidos de los clientes y se espera que las
necesidades primarias de cliente compensen las necesidades primarias planificadas. En
otras palabras, se espera que los pedidos de cliente se cumplan con las necesidades
planificadas. Cuando una necesidad primaria de cliente compensa necesidades primarias
planificadas, se reduce la cantidad de necesidades primarias planificadas en la cantidad de
las necesidades primarias de cliente. Este proceso se conoce como compensación.

La Tabla 8-1 presenta la compensación bajo la estrategia de planificación con montaje final.
En el Ejemplo 1 una necesidad primaria planificada de 50 existe cuando se crea una
necesidad primaria de cliente de 60. Dado que la necesidad primaria de cliente es mayor que
la necesidad primaria planificada, se compensa la necesidad primaria planificada completa.
Por lo tanto, luego de la compensación la cantidad de necesidades primarias planificadas es
cero. El proceso de planificación creará una propuesta de pedidos para la cantidad de
necesidades primarias de cliente correspondiente a 60 unidades. En el Ejemplo 2 existe una
necesidad primaria planificada de 50 cuando se crea una necesidad primaria de cliente de
40. Luego de la compensación, 10 de las 50 iniciales permanecen en las necesidades
primarias planificadas. El proceso de planificación creará dos propuestas de pedidos: una
para la cantidad de necesidades primarias planificadas de 10 unidades y una para la cantidad
de necesidades primarias de cliente de 40 unidades.
Tabla 8-1: Ejemplo de Compensación

Así, cuando las necesidades primarias planificadas no se compensan con necesidades
primarias de cliente (porque no hay suficientes pedidos de cliente), las propuestas de
pedidos incrementarán el stock del material. En la situación opuesta, cuando las necesidades
primarias de cliente exceden a las necesidades primarias planificadas disponibles en el
intervalo de compensación –esto es, que los pedidos de cliente exceden las necesidades
planificadas –entonces el proceso de planificación generará propuestas de pedidos
adicionales para cubrir la diferencia.

La forma en la cual las necesidades primarias de cliente consumen a las necesidades
primarias planificadas está determinada por el modo de compensación. Los modos de
compensación comúnmente utilizados son la compensación hacia adelante y la compensación
hacia atrás. También es posible una combinación de ambas compensaciones. Estas
alternativas se grafican en la Figura 8-6. La parte superior de la Figura presenta una
compensación hacia atrás (modo 1); la parte media, una compensación hacia adelante (modo
3); y en la parte inferior, una compensación hacia atrás y hacia adelante (modos 2 y 4). En
estos gráficos el eje horizontal es la línea de tiempo, el área sobre la línea de tiempo
representa las necesidades primarias planificadas y el área bajo la línea de tiempo indica las
necesidades de cliente. El plan (necesidades primarias planificadas) es fabricar o
aprovisionar 40 bicicletas en cada periodo de tiempo. En cada caso la empresa debe
satisfacer la necesidad de un cliente que requiere 60 bicicletas.
Figura 8-6: Modos de compensación

En la compensación hacia atrás, las necesidades de cliente compensan las necesidades
primarias planificadas que tienen fecha anterior al de dichas necesidades de cliente. Así, para
alcanzar las necesidades primarias de cliente de 60 bicicletas, las necesidades primarias
planificadas inmediatamente antes se compensan. Ya que esta cantidad (40) no es suficiente
para satisfacer las necesidades primarias de cliente (60), se compensan 20 bicicletas de las
necesidades primarias planificadas inmediatamente antes. En la compensación hacia
adelante, las necesidades de cliente compensan las necesidades primarias planificadas que
ocurren después de la fecha de las necesidades primarias de cliente. Así, para satisfacer la
necesidad de 60 bicicletas, se compensan las necesidades primarias planificadas
inmediatamente después de las necesidades primarias de cliente de acuerdo a la necesidad
–40 bicicletas de las primeras necesidades primarias planificadas y 20 de las siguientes. Los
modos 2 y 4 utilizan compensación hacia adelante y hacia atrás. El modo 2 utiliza primero la
compensación hacia atrás seguida por la compensación hacia adelante; el modo 4 utiliza la
compensación hacia adelante seguida por la compensación hacia atrás.

El intervalo de compensación indica el número de días, antes o después, de las necesidades
primarias de cliente que pueden compensar necesidades primarias planificadas. Fuera del
intervalo de compensación, las necesidades primarias de cliente no pueden compensar
necesidades primarias planificadas. El supuesto es que, debido a consideraciones de
programación y capacidad, sólo necesidades primarias planificadas en el mismo período de
tiempo que los pedidos de cliente se deberían compensar por necesidades primarias de
cliente.

Demo 8.1: Revisión de vistas MRP y preparación de trabajo de un material

GRUPOS DE PRODUCTOS
Cuando una empresa fabrica o vende varios productos similares, tales como mobiliario de
una empresa con decenas de miles de diferentes tipos de sillas y escritorios, no es necesario
ni eficiente planificar separadamente cada material. Por esta razón, las empresas
generalmente ubican productos con similares características de planificación, tales como
tipo o proceso de manufactura similar, en un GRUPO DE PRODUCTOS o una familia de productos.
La agrupación de productos, desde el material en el nivel inferior (producto terminado o
mercadería) hasta el grupo de productos en el nivel superior, se denomina agregación. Es
decir, los productos se agregan en grupos. Más aún, un grupo de productos de nivel superior
se puede anidar, es decir, se compone de grupos de productos de nivel inferior. El grupo de
productos más bajo en cualquier jerarquía se compone de materiales, ya sean productos
terminados o mercaderías.

La Figura 8-7 muestra el grupo de productos bicicletas de GBI. El grupo de productos
bicicletas (PG-BIKE000) consiste en un número de grupos de productos anidados. Cada uno
de estos grupos representa una línea de productos diferente tales como las bicicletas de
turismo (PG-TOUR000) y bicicletas todo terreno (PG-ORBK000). Las ocho cajas del nivel
inferior de la jerarquía son todos materiales que representan los distintos modelos de
bicicletas.

Los materiales y grupos de productos pueden ser miembros de más de un grupo para
diferentes escenarios de planificación. Por ejemplo, una empresa podría planificar por
separado los mercados nacional y extranjero, porque implican diferentes patrones de ventas.
Además, a cada miembro de un grupo de productos se le asigna un factor proporcional. Un
factor proporcional es una medida de cuánto influye el componente en el grupo de productos.
Por ejemplo, en la Figura 8-7, el grupo de productos bicicletas todo terreno incluye las
bicicletas de mujer y las de hombre, con factores proporcionales de 35% y 65%,
respectivamente. Así, las bicicletas de hombre son más influyentes que las bicicletas de
mujeres en la planificación del grupo bicicletas todo terreno. Los factores proporcionales se
utilizan en el proceso de planificación de materiales para derivar planes detallados de
pronósticos de alto nivel. Los pronósticos y planes para los grupos de productos de niveles
superiores se desagregan en planes para los niveles inferiores utilizando los factores
proporcionales. Por ejemplo, si el plan indica 1.000 bicicletas todo terreno, entonces el
sistema automáticamente traduce esta información en un plan por 650 bicicletas de hombre
y 350 de mujer. Se abordará la agregación y desagregación con mayor detalle en la sección
de proceso de este capítulo. Procesos de Negocio en la Práctica 8-2 describe los grupos de
productos de Apple Inc.
Figura 8-7: Grupos de productos de GBI

   PROCESO
En esta sección se discutirá el proceso de planificación de materiales, el cual se presenta en
la Figura 8-9. La primera etapa en el proceso es generalmente planificación de ventas y
operaciones (SOP). SOP es una herramienta de pronóstico y planificación que las empresas
utilizan para ingresar o generar una previsión de ventas, especificar necesidades de stock y
después generar un plan de operaciones. SOP normalmente supone productos terminados.
Así, el plan de operaciones es, en efecto, un plan de producción para estos materiales. El plan
generado por SOP se le conoce como plan global ya que la planificación es generalmente a un
alto nivel de agregación y no es muy preciso.
Figura 8-9: El proceso de planificación de materiales

Que se requiera SOP depende de la estrategia de planificación de producción utilizada para
los materiales. La fabricación MTO no requiere un plan de producción ya que la fabricación
se desencadena por los pedidos de cliente. Por lo tanto, SOP no es necesario. Por el contrario,
la fabricación MTS requiere de un plan de producción basado en una previsión de ventas
porque los pedidos de cliente se cumplen con materiales que ya están en un almacén. En
consecuencia, SOP es relevante para los materiales con la estrategia MTS. Se deben crear
planes de producción para las variaciones de MTO, tales como ATO, en el cual los productos
semielaborados se fabrican anticipadamente y luego se almacenan.

SOP crea un plan de producción a nivel del grupo de productos. A su vez, estas necesidades
se deben traducir en necesidades primarias planificadas para materiales individuales en el
grupo de productos. Esta tarea se realiza en la etapa de desagregación. Las necesidades
primarias planificadas para los materiales individuales se transfieren a la gestión de
demanda, en donde se revisan y refinan en base a las estrategias específicas de planificación
que se discutieron anteriormente. La etapa final, planificación de necesidades, crea
propuestas específicas de aprovisionamiento para asegurar que estarán disponibles los
materiales suficientes para cubrir cada necesidad.

La etapa de planificación de ventas y operaciones requiere entradas desde muchas partes de
una organización y, generalmente, la ejecuta el grupo de planificación o de pronóstico. Luego
que el plan de producción se transfiere a la gestión de demanda, pasa a ser responsabilidad
del planificador de necesidades. El planificador de necesidades es la persona o personas en
una organización responsables de crear propuestas de pedidos y monitorear la
disponibilidad de material. Todos los materiales que se utilizan en el proceso de planificación
se deben asignar a un planificador de necesidades en el maestro de materiales.

La discusión del proceso de planificación de materiales utilizará como ejemplo el grupo de
productos bicicletas de GBI (Figura 8-7). GBI inicia su proceso de planificación de materiales
cuando desarrolla su plan estratégico general. Este plan incluye ventas esperadas para el
grupo de productos bicicletas (PG-BIKE000).

PLANIFICACIÓN DE VENTAS Y OPERACIONES
La Figura 8-10 presenta los elementos de la etapa de planificación de ventas y operaciones.
SOP se desencadena cuando la organización desea revisar su plan de producción. La mayoría
de las organizaciones ejecutan esta tarea en intervalos programados dependiendo de su
proceso de planificación. Por ejemplo, una organización podría requerir revisiones
trimestrales de pronósticos de venta y planes de producción. SOP también se puede
desencadenar por eventos inesperados tales como cambios en el panorama económico
global. Por ejemplo, la crisis financiera del 2008 causó que muchas empresas revisaran sus
bajas previsiones de ventas y, por consiguiente, redujeran sus niveles de producción. SOP
utiliza datos de una variedad de fuentes para generar un plan de producción.




Figura 8-10: Elementos de la etapa SOP

SOP puede generar varias versiones de un plan de producción basado en diferentes
supuestos relativos al crecimiento de la economía global. Cada plan incorpora diferentes
previsiones de ventas y niveles de stock deseados. La empresa entonces evalúa estos planes
para determinar su factibilidad en términos de capacidad de producción. Generar múltiples
versiones permite a la organización considerar diferentes escenarios de planificación.
Después de evaluar varios planes, la empresa selecciona un escenario como base para
planificaciones futuras.

SOP puede ser estándar o flexible. Con la planificación estándar una empresa utiliza modelos
de planificación predefinidos. Estos modelos son relativamente simples y toman en cuenta
los valores totales de ventas, producción y niveles de stock para toda la organización. Por lo
tanto, la planificación estándar se puede emplear solo para planificación altamente agregada.
Sin embargo, es fácil de usar y no requiere preparación.
Por el contrario, con la planificación flexible una empresa utiliza herramientas para
desarrollar modelos de planificación más complejos que contienen niveles de detalle más
amplios. Por ejemplo, una organización puede crear un modelo que desglose las ventas a
nivel de canal de distribución y calcule volúmenes de producción para centros individuales.
Sin embargo, la planificación flexible requiere datos más detallados que los utilizados en la
planificación estándar y los modelos de planificación deseada se deben crear primero. La
discusión de este libro se limita a la planificación estándar.

Datos
La Figura 8-11 muestra los datos utilizados en la etapa de planificación de ventas y
operaciones. Los datos más importantes son un plan de ventas, niveles de stock existente y
las necesidades de stock. Los niveles de stock existentes se pueden transferir desde gestión
de stocks y almacenes. Las necesidades de stock más frecuentes se determinan en base a
criterios económicos y financieros tales como costos de almacenamiento, variaciones en la
demanda esperada de clientes y capacidades de producción. Ellos se pueden calcular como
parte del proceso de planificación estratégica global.




Figura 8-11: Datos en la etapa SOP

Las organizaciones ejecutan planificaciones para niveles organizativos y datos maestros
específicos –por ejemplo, para grupos de productos y centros específicos.

Tareas
Las tareas de la etapa de planificación de ventas y operaciones incluyen crear un plan de
ventas, especificar las necesidades de stock y crear un plan de producción. La interface para
realizar estas tareas en SOP es una herramienta que consiste en una hoja de cálculo simple
denominada tabla de planificación. La Figura 8-12 presenta una tabla de planificación
estándar de SOP. El área de encabezado de la tabla indica el grupo de productos y el centro
para el cual se genera el plan, así como el número de la versión de dicho plan. (Recuerde que
se pueden generar múltiples versiones del mismo plan para diferentes escenarios de
planificación). Por defecto, las columnas representan meses, pero los usuarios pueden
especificar otros periodos de tiempo. La tabla incluye las siguientes filas:




Figura 8-12: Tabla de planificación estándar SOP

       •   Ventas: Esta fila contiene el plan de ventas

       •   Producción: Esta fila contiene el plan de producción, el cual normalmente calcula
           el sistema.

       •   Stock de almacén: Esta fila contiene niveles de stock, los cuales genera el sistema
           cuando calcula el plan de producción.

       •   Stock de almacén destino: En esta fila se ingresan los niveles de stock deseados.

       •   Cobertura: Es el número de días que la organización puede esperar para cubrir
           las ventas utilizando solo el stock existente. Este número se calcula dividiendo el
           stock por las ventas diarias (días laborables) en el periodo. El número de días
           laborables se especifica cuando el sistema se configura inicialmente. El sistema
           calcula esta fila.

       •   Cobertura prevista: En esta fila se ingresa el número de días que se desea cubrir.

Primero se ingresa el plan de ventas. Los datos para el plan de ventas se pueden obtener de
diversas fuentes:

       •   Desde la cuenta de resultados, que es uno de los procesos de la contabilidad
           administrativa, se puede importar un plan de ventas basado en niveles de
           rentabilidad deseados.

       •   Si la empresa anticipa que las ventas futuras serán iguales a las ventas pasadas,
           entonces puede transferir los datos de ventas históricas desde el sistema de
           información de ventas (SIS), el cual se discutió en el Capítulo 5.

       •   Por el contrario, si la empresa espera que las ventas futuras difieran de las ventas
           pasadas, pero cree que puede predecirlas basándose en estas últimas, entonces
           puede crear una previsión introduciendo datos históricos del SIS en uno de varios
           modelos de previsión disponibles en SOP.

       •   Los empleados pueden ingresar un plan de ventas manualmente basándose en
           sus experiencias o en una previsión de otro programa.

       •   Se puede copiar un plan de ventas del plan generado para otro grupo de
           productos.

Sin importar qué procedimiento utilice la empresa, después de ingresar el plan de ventas, el
sistema genera un plan de producción en base a una de las siguientes opciones:

       •   Sincronizado con el volumen de ventas: En este escenario, el sistema simplemente
           copia las cantidades desde la fila del plan de ventas a la fila del plan de
           producción. Así, las cantidades en ambas filas son idénticas.

       •   Stock de almacén destino: En este escenario, la empresa especifica un nivel de
           stock deseado y el sistema determina los volúmenes de producción necesarios
           para satisfacer el plan de ventas y lograr el stock de almacén destino.

       •   Cobertura prevista: Este escenario es similar al de stock de almacén destino. La
           diferencia es que los niveles de stock deseado se expresan en términos de
           cobertura en vez de cantidades específicas. La cobertura prevista la especifica el
           usuario y el sistema calcula, en la fila de producción, las cantidades requeridas
           para alcanzar esa cobertura.

       •   Nivel de Stock = 0: En este escenario el nivel de stock deseado al final de cada
           periodo es cero. El sistema utiliza el stock existente para cubrir las ventas hasta
           que el nivel de stock llega a cero. Mientras exista stock, la empresa no fabricará
           nuevos materiales. Cuando el stock llega a cero, el sistema calcula los volúmenes
           de producción que cubrirán solo los volúmenes de ventas sin excesos de stock.
           Así, la fila de stock de almacén será cero para cada periodo.
La Figura 8-13 muestra la tabla de planificación para el grupo de productos bicicletas en el
centro de Dallas de GBI. El tiempo de planificación es de 4 meses. El escenario de
planificación es uno en el cual el sistema calculará el plan de producción necesario para
lograr el plan de ventas especificado y el stock de almacén destino deseado. La figura anterior
presenta la tabla de planificación después de que el plan de ventas y el stock de almacén
destino se han ingresado. La siguiente tabla muestra los resultados después que el sistema
ha calculado el plan de producción necesario. Los datos de producción se obtienen
calculando las necesidades totales (ventas + stock de almacén destino) y restando el stock
disponible (el nivel de stock del mes anterior).

La Figura 8-13 muestra que el plan de producción para el grupo de productos bicicletas para
los cuatro meses es 1.100, 1.300, 900 y 850, respectivamente. La Tabla 8-2 muestra el cálculo
para el tercer mes.

Para calcular la cobertura, el sistema primero determina las necesidades diarias dividiendo
las ventas por el número de días laborables de un mes. Después divide el nivel de stock de
almacén destino por las necesidades diarias. El cálculo para el segundo mes se presenta en
la Tabla 8-3 (asumiendo 30 días laborables en el mes 2).

La fila de la cobertura prevista en la Figura 8-13 está vacía porque el usuario debería ingresar
los valores correspondientes solo si el método del cálculo del plan de producción se basara
en la cobertura prevista.




Figura 8-13: Ejemplo SOP de GBI
Tabla 8-2: Ejemplo de cálculo de plan de producción




Tabla 8-3: Ejemplo de cálculo de cobertura

Salidas
La salida de SOP es una o más versiones del plan de producción. No hay impactos financieros
y ningún movimiento de materiales. Por consiguiente, no se crea ningún documento FI, CO o
de material.

DESAGREGACIÓN
La etapa SOP crea planes de ventas y producción a nivel de grupo de productos. Después que
se realiza esta etapa, los planes se deben traducir en planes para productos terminados en la
jerarquía del grupo. Esta etapa del proceso se denomina DESAGREGACIÓN. (Se presentó la
desagregación en la discusión de los grupos de productos). Los elementos de la etapa de
desagregación se presentan en la Figura 8-14. La desagregación se desencadena cuando se
crea un nuevo plan de producción. Los datos organizativos (p.e., centro) y los datos maestros
(p.e., grupos de producto) del plan de producción se utilizan para calcular las necesidades de
materiales en el grupo de productos. Estas necesidades se transfieren a la etapa de gestión
de demanda para futuras planificaciones.




Figura 8-14: Elementos de la etapa de desagregación.
Datos
Los datos utilizados en la etapa de desagregación incluyen los datos del grupo de productos,
los planes de producción desde el SOP y la entrada del usuario (Figura 8-15). El sistema
utiliza los factores proporcionales del grupo de productos para calcular los valores de
desagregación para cada miembro del grupo. Recuerde que los productos miembros del
grupo son otros grupos de productos o, a más bajo nivel, materiales. El usuario proporciona
parámetros para determinar cómo se desagrega el plan.

Tareas
La tarea esencial en esta etapa es traducir los planes generados en la etapa SOP para grupos
de productos en planes para los materiales contenidos en esos grupos. La desagregación se
puede realizar para toda la jerarquía del grupo de productos o solo para uno o más niveles
de la jerarquía. Además, se pueden desglosar el plan de producción o el plan de ventas. Por
consiguiente, en esta etapa se dispone de múltiples opciones.

       •   Desagregar el plan de producción para uno o más niveles o bajar hasta el nivel de
           materiales.

       •   Desagregar el plan de ventas bajando al siguiente nivel del grupo de productos.
           El plan desagregado es el plan de ventas para ese nivel y se utiliza para
           determinar un plan de producción, tal como se explicó en la etapa SOP. Luego,
           continuar hasta el nivel de materiales.

       •   Desagregar el plan de ventas bajando hasta el nivel de materiales y determinar el
           plan de producción para cada material.




Figura 8-15: Datos de la etapa de desagregación

Una opción para GBI es desagregar el plan de ventas para el grupo de productos bicicletas
hasta los grupos de productos bicicleta de turismo y bicicleta todo terreno, y luego utilizar
SOP para crear planes de producción para estos grupos de productos. O bien, GBI puede
elegir desagregar el plan de producción para el grupo de productos bicicletas hasta llegar a
los productos terminados en el último nivel de la jerarquía del grupo de productos.

En el ejemplo que se ha estado desarrollando, GBI selecciona la segunda opción. Recuerde
que como resultado de la etapa SOP en el ejemplo, el plan de producción para el primer mes
es de 1.100 unidades para el grupo de productos bicicletas. La etapa de desagregación
traduce este valor a través de la jerarquía del grupo de productos, tal como lo muestra la
Figura 8-16.

Las 1.100 bicicletas se convierten en 660 bicicletas de turismo y 440 bicicletas todo terreno
utilizando los factores proporcionales 60% y 40%, respectivamente. Las 660 bicicletas de
turismo se convierten a su vez en 462 bicicletas de turismo de lujo y 198 bicicletas de turismo
profesionales (70% y 30%). Finalmente, las bicicletas de turismo de lujo se convierten en
184 bicicletas de turismo de lujo negras, 139 bicicletas de turismo de lujo plateadas y 139
bicicletas de turismo de lujo rojas. Estos valores del plan de producción son las necesidades
primarias planificadas para las tres bicicletas de turismo de lujo para el primer mes. GBI
completa una desagregación similar para todos los miembros de la jerarquía del grupo de
productos y para todos los meses.

Salidas
La salida de la etapa de desagregación son las necesidades primarias planificadas para cada
periodo de planificación (p.e., semana o mes). Estas necesidades se trasfieren entonces a la
gestión de demanda, como lo muestra la Figura 8-17. La figura indica que el plan para la
fabricación de bicicletas de turismo de lujo se desagrega hasta los tres materiales del grupo
como necesidades primarias planificadas específicas de material por centro. Estos datos se
transfieren entonces a la gestión de demanda.
Figura 8-16: Ejemplo de desagregación de GBI
Figura 8-17: Transferencia de necesidades primarias planificadas a la gestión de demanda

Al igual que en la etapa SOP, ningún documento FI, CO o de material se crea porque la
desagregación no tiene impactos financieros y no involucra ningún movimiento de
materiales.

GESTIÓN DE DEMANDA
La GESTIÓN DE DEMANDA calcula necesidades primarias planificadas revisadas para los
materiales utilizando las necesidades primarias planificadas de SOP (después de la
desagregación), pedidos reales de cliente (necesidades primarias de cliente) del proceso de
gestión de pedidos y datos del maestro de materiales en relación con las estrategias de
planificación. La Figura 8-18 presenta los elementos específicos de la etapa gestión de
demanda.
Figura 8-18: Elementos de la etapa gestión de demanda

Datos
La gestión de demanda (Figura 8-19) utiliza datos de necesidades de SOP (necesidades
primarias planificadas) y del proceso de gestión de pedidos (necesidades primarias de
cliente). También utiliza la estrategia de planificación definida en el maestro de materiales
por el grupo de estrategias.




Figura 8-19: Datos de la etapa de gestión de demanda

Tareas
La tarea fundamental de la gestión de demanda es crear necesidades primarias planificadas
revisadas para los materiales. Qué procedimiento utiliza una empresa para calcular estas
necesidades depende de la estrategia de planificación de la producción definida por el grupo
de estrategias en el maestro de materiales. Como se discutió anteriormente, la estrategia de
planificación de la producción determina si la producción se desencadena por necesidades
primarias planificadas o necesidades de clientes, o si la interacción de estos dos tipos de
necesidades afecta el proceso de planificación a través de la compensación.

El sistema ERP lleva a cabo automáticamente la etapa de gestión de demanda. Sin embargo,
el planificador de necesidades monitorea los resultados utilizando diversos informes y hace
ajustes cuando se necesite. Por ejemplo, si el proceso utiliza una estrategia de planificación
con compensación, entonces se pueden requerir cambios en la programación cuando se
crean nuevas necesidades de clientes. Con una estrategia de planificación MTO, el
planificador de necesidades debe monitorear los stocks de conjuntos o ensambles
cuidadosamente ya que los pedidos de cliente aparecen a intervalos impredecibles.

Salidas
Los resultados de la gestión de demanda son necesidades primarias planificadas para cada
material incluido en la planificación. Estas necesidades primarias planificadas representan
las necesidades de materiales para cantidades y fechas específicas. Ellos se utilizan entonces
en la etapa de planificación de necesidades. No hay implicaciones financieras ni movimientos
de material asociados con la gestión de demanda, así es que tampoco se crean documentos
FI, CO ni de materiales.

PLANIFICACIÓN DE NECESIDADES DE MATERIAL
La etapa final del proceso de planificación de materiales es la planificación de necesidades
(MRP), la cual calcula las necesidades netas para los materiales y crea propuestas de pedidos
–para fabricar o comprar los materiales necesarios –que aseguren que la organización tendrá
suficientes materiales disponibles para cubrir sus necesidades. La Figura 8-20 presenta los
elementos de la etapa de planificación de necesidades.




Figura 8-20: Elementos de la etapa de planificación de necesidades

Recuerde que SOP genera planes a nivel de grupo de productos y la gestión de demanda
genera planes a nivel de material. La planificación de necesidades genera planes para los
materiales, así como para los componentes y materias primas que se utilizarán para fabricar
un material. Esto es, se planifica para todos los niveles de la LMat.
Múltiples actividades pueden afectar la disponibilidad de materiales en los distintos
procesos como lo muestra la siguiente lista:

       •   Aprovisionamiento: solicitudes de pedido, pedidos de compra y entradas de
           mercancías.

       •   Gestión de pedidos: pedidos de cliente, entregas y salidas de mercancías.

       •   Producción: órdenes previsionales, órdenes de fabricación, reservas de material
           y entradas y salidas de mercancías.

Estas actividades se denominan ELEMENTOS DE PLANIFICACIÓN y se utilizan para calcular las
necesidades netas y generar las propuestas de pedido. Las necesidades netas utilizan todos
los elementos de planificación relevantes para calcular las cantidades de las propuestas de
pedido. Se explicará el cálculo de las necesidades netas más tarde en esta sección.

La etapa de planificación de necesidades se puede ejecutar manualmente. Sin embargo,
debido a que numerosas actividades en otros procesos pueden afectar la planificación de
necesidades, la situación de planificación está constantemente cambiando. Por lo tanto, las
empresas configuran frecuentemente sus sistemas ERP para ejecutar periódicamente la
etapa de planificación de necesidades de forma automática. El planificador de necesidades
es generalmente responsable de monitorear los resultados del proceso de planificación a
través de una variedad de informes que se discuten más tarde en este capítulo. Él o ella deben
entonces tomar acciones apropiadas para desencadenar los procedimientos necesarios. Por
ejemplo, órdenes previsionales se deben convertir en órdenes de fabricación o solicitudes
de pedido. Las órdenes de fabricación se deben liberar para que la fabricación pueda
comenzar. Las órdenes previsionales podrían tener que reprogramarse para resolver
problemas asociados a programación o capacidad. Como es de imaginar, en centros que
utilizan cientos o incluso miles de materiales, el planificador de necesidades puede estar muy
ocupado.

La planificación de necesidades se puede ejecutar para un centro, para múltiples centros o
dentro de un área de planificación de necesidades. Un área de planificación de necesidades
puede incluir un centro entero o almacenes específicos de un centro. Ejecutar la planificación
de necesidades para áreas individuales permite a la empresa planificar para un grupo de
materiales en un centro independiente de otros grupos. Por ejemplo, la empresa puede
planificar los materiales de poco valor por separado de los de alto valor.

El plan maestro de producción (MPS) es una forma especializada de planificación de
necesidades que las organizaciones utilizan para planificar materiales altamente rentables o
para materiales que utilizan recursos críticos. Los materiales planificados mediante MPS son
generalmente productos terminados en el nivel más alto de la jerarquía de la LMat. Se llaman
piezas principales y tienen prioridad sobre recursos tales como capacidad y transporte.
Después de planificar las piezas principales, MPS crea necesidades secundarias para los
componentes de esas piezas. Sin embargo, no las planifica ni a ningún material bajo estas.
Después que MPS termina, se utiliza la planificación de necesidades (MRP) para planificar
los materiales restantes. En muchos casos, solo se utiliza la planificación de necesidades.

Datos
Los datos en la etapa de planificación de necesidades se presentan en la Figura 8-21. Los
datos maestros utilizados en la etapa de planificación de necesidades incluyen el maestro de
materiales, la LMat del material y –opcionalmente –la hoja de ruta. Las LMat de los materiales
se utilizan para determinar las necesidades secundarias. Recuerde que cuando existen
múltiples LMat para un material, el método para determinar qué LMat se utilizará se define
en el maestro de materiales. Generalmente, la planificación de necesidades utiliza los
tiempos de planificación del maestro de materiales para ejecutar la programación y para
determinar la fecha de inicio y término de los pedidos. Estas fechas indican cuándo debe
comenzar y terminar la fabricación. Sin embargo, la planificación de necesidades no puede
determinar los detalles de las operaciones individuales de la fabricación utilizando los
tiempos del maestro de materiales. Si se necesita una programación más detallada que
incluya datos a nivel de operaciones, la planificación de necesidades utiliza datos de
programación de la hoja de ruta del producto. La hoja de ruta contiene las operaciones y
tiempos requeridos para la fabricación, de manera que la planificación de necesidades puede
programar cada operación individual en detalle. Este tipo de programación, llamado
programa de ciclo de fabricación, normalmente no se ejecuta hasta que la orden previsional
se convierte en una orden de fabricación.




Figura 8-21: Datos de la etapa de planificación de necesidades

Tareas
La Figura 8-22 muestra las tareas de la etapa de planificación de necesidades. Estas tareas
se ejecutan automáticamente.
Figura 8-22: Método de la planificación de necesidades

Verificación del Fichero para Petición de Planificación
La primera tarea en la planificación de necesidades es determinar qué materiales se deben
planificar. Cualquier cambio a un material MRP-relevante genera una entrada en el fichero
para petición de planificación. Ejemplos de cambios relevantes son modificaciones en los
tiempos de planificación en el maestro de materiales y modificaciones a los elementos de
planificación tales como niveles de stock, solicitudes de pedido y pedidos de compra. Los
materiales del archivo para petición de planificación se codifican de manera que los
productos terminados se planifican primero, luego siguen los componentes de estos en la
LMat y así sucesivamente. Las materias primas individuales, que se hallan al final de la
jerarquía de la LMat, se planifican al final.

Cálculo de Necesidades Netas
La siguiente tarea es determinar si existe una necesidad de aprovisionamiento de material.
Esta tarea se realiza ejecutando el cálculo de necesidades netas, el cual toma en cuenta todos
los elementos relevantes de la planificación de necesidades para determinar si existe escasez
de materiales. Si se necesitan más materiales, entonces se generan propuestas de pedidos
para cubrir el déficit.

El desencadenante de este cálculo y la elección del método de cálculo dependen de la
característica de planificación de necesidades especificada en el maestro de materiales. Si la
característica es planificación de necesidades sobre consumo, entonces el cálculo de
necesidades netas determina el stock disponible de acuerdo a la siguiente fórmula:

                       Stock Disponible = Stock inicial + Entradas
Las entradas son el resultado de un pedido de compra, solicitudes de pedido fijas, órdenes
previsionales fijas y órdenes de fabricación. Una solicitud de pedido u orden previsional es
fija si está dentro del horizonte de planificación. Si el stock disponible cae por debajo del
punto de pedido, entonces el material se debe comprar. Otro método de planificación de
necesidades sobre consumo utiliza cálculos similares. Note que ni las necesidades primarias
ni las secundarias son relevantes para estos materiales.

Si la característica de planificación de necesidades es Planificación de necesidades
determinista o Plan maestro de producción (MPS), se desencadena el cálculo de necesidades
netas cuando existe una necesidad primaria o secundaria. Para cada necesidad, la
planificación de necesidades ejecuta el cálculo de necesidades netas para determinar si
existe suficiente material para satisfacer las necesidades. El cálculo es como sigue:

       Stock Disponible = Stock inicial - Stock de seguridad + Entradas – Salidas

El cálculo toma en cuenta el stock sumando el stock actual del centro y restando el stock de
seguridad. El sistema también toma en cuenta todas las entradas y salidas de mercancías.
Las entradas de mercancías son el resultado de los pedidos de compra, solicitudes de pedido
fijas, órdenes previsionales fijas y órdenes de fabricación. Las salidas de mercancías son el
resultado de las necesidades de cliente, necesidades primarias planificadas y reservas de
material. Si el stock disponible en este cálculo es negativo, entonces se genera una propuesta
de pedidos.

Determinación del tamaño de lote
Si se necesita una propuesta de pedidos, el sistema utiliza el cálculo de tamaño de lote para
determinar cuánto material comprar. El cálculo del tamaño de lote se define mediante la
clave de tamaño de lote del maestro de materiales.

Ejecución de la Programación
Después que la planificación de necesidades determina el tamaño de lote, ejecuta la
programación para determinar si el material se puede adquirir en la fecha requerida. La
planificación de necesidades puede utilizar dos tipos de programación: programación
regresiva y programación progresiva. El sistema inicialmente utiliza la programación
regresiva y emplea la programación progresiva solo si la programación regresiva no
funciona. La programación regresiva se presenta en la Figura 8-23.
Figura 8-23: Programación Regresiva

En la programación regresiva, el sistema comienza en la fecha requerida y resta el tiempo de
aprovisionamiento para determinar la fecha en la cual el proceso de aprovisionamiento debe
comenzar. Los tiempos utilizados son los tiempos de planificación definidos en el maestro
de materiales, dependiendo de la clase de aprovisionamiento. Si la clase de
aprovisionamiento del material es de fabricación propia, entonces se utilizan el tiempo de
fabricación propia y el tiempo de entrada de mercancías. Por el contrario, si la clase de
aprovisionamiento es externo, entonces se usa el tiempo de tratamiento del departamento de
compras, el plazo de entrega previsto y el tiempo de la entrada de mercancías. A diferencia de
los otros tiempos, el tiempo de tratamiento del departamento de compras no se incluye en
el maestro de materiales porque generalmente no depende de los materiales. Estos datos se
definen en otra parte del sistema.

Finalmente, MRP programará todas las propuestas de pedidos hasta que haya programado
las materias primas del nivel más bajo de la LMat. Si la fecha de inicio más temprana cae
antes de la fecha actual, entonces el sistema realizará programación progresiva. En esencia,
se desplaza el material con la fecha de inicio más temprana a la primera fecha futura
disponible y luego se programan todos los otros materiales desde esa fecha en adelante
utilizando los mismos tiempos de planificación. Si la programación resultante no es
aceptable, entonces el planificador de necesidades puede ajustar manualmente el programa.

Determinación de Propuestas de pedidos
Después que el sistema ha finalizado la programación, la próxima tarea es determinar la clase
de propuesta de pedidos a generar. La Figura 8-24 presenta las posibilidades. Para los
materiales con clase de aprovisionamiento propio (interno), la planificación de necesidades
siempre genera órdenes previsionales. Las órdenes previsionales se deben convertir en
órdenes de fabricación por el planificador de necesidades. Esta acción desencadena el
proceso de producción descrito en el Capítulo 6.

Para el aprovisionamiento externo de materiales existen tres opciones. Qué opciones se
seleccionan depende de los parámetros definidos en la etapa de planificación de necesidades.
La primera opción es que el sistema cree solicitudes de pedido. El segundo es que el sistema
cree órdenes previsionales, las cuales se convierten manualmente en solicitudes de pedido.
La ventaja de crear órdenes previsionales es que le permiten al planificador de necesidades
un mayor control sobre los procesos de planificación. Cuando el sistema genera una solicitud
de pedido, el departamento de compras es responsable de actuar sobre esta para crear un
pedido de compra y el planificador de necesidades no podrá modificar la solicitud. Por el
contrario, cuando el sistema genera una orden previsional, entonces el planificador de
necesidades puede tener la certeza de que esta se convertirá, a tiempo, en una solicitud de
pedido para que el departamento de compras la procese y para que el proveedor entregue
los materiales en el plazo estipulado. Una variación de esta opción es crear solicitudes de
pedido dentro del horizonte de apertura y luego las órdenes previsionales más allá del
horizonte de apertura. El horizonte de apertura es el tiempo durante el cual el planificador
de necesidades puede convertir órdenes previsionales en órdenes de fabricación o
solicitudes de pedido. El proceso de programación, además, da al planificador de necesidades
flexibilidad respecto de la fecha exacta en que se hará la conversión de las órdenes
previsionales. En el sistema se define la duración del horizonte de apertura. Esta estrategia
agiliza el proceso de aprovisionamiento en el corto plazo y al mismo tiempo proporciona
flexibilidad para programar a largo plazo.
Figura 8-24: Propuestas de pedidos

La última opción es crear repartos. Esta opción es relevante si la organización utiliza planes
de entrega. Recuerde del Capítulo 5 que los planes de entrega son un tipo de contrato en el
cual el proveedor acuerda despachar materiales según una programación específica. El
reparto creado por la planificación de necesidades es similar al reparto del pedido de cliente
por cuanto ambas especifican que una cierta cantidad de material se despachará en una fecha
determinada. Una gran diferencia, sin embargo, es que los repartos generados durante la
venta indican las necesidades de entrega del cliente. En cambio, los repartos creados por la
planificación de necesidades identifican las necesidades de la empresa a su proveedor.
Debido a que las entregas siguen programas predeterminados, los planificadores de
necesidades no pueden reprogramarlas.

Determinación de Necesidades Secundarias
Para los materiales fabricados internamente, la planificación de necesidades genera
necesidades secundarias para los componentes incluidos en la LMat mediante la explosión
de la LMat o mediante el cálculo de las necesidades para los niveles sucesivos de la LMat.
(Recuerde que se discutió la explosión de la LMat anteriormente en este capítulo). La Figura
8-25 muestra las opciones para la explosión de la LMat.
Figura 8-25: Explosión de una LMat

Si la empresa elige utilizar la planificación de necesidades de un nivel, entonces el proceso
termina después de esta etapa inicial. Si se escoge un enfoque de varios niveles, entonces la
planificación de necesidades realiza los cálculos para todos los niveles. Si se ensamblan
algunos de los componentes que poseen necesidades secundarias –es decir, si es que ellos
tienen sus propios LMats –entonces la planificación de necesidades crea necesidades
secundarias para los componentes en su LMat. El proceso continúa hasta que el sistema haya
explosionado todas las LMats hasta el nivel de materias primas individuales.

Después que se realiza la planificación para todos los niveles seleccionados de la LMat del
material, la planificación de necesidades regresa al fichero para petición de planificación y
repite el proceso para el siguiente material que requiere planificación. Note que las acciones
que realiza la planificación de necesidades, tal como la creación de necesidades secundarias,
puede crear también una entrada en el fichero para petición de planificación, la cual
provocará procesamiento adicional. El proceso continúa hasta que no existen más materiales
que planificar.

En el ejemplo de GBI, el sistema creó necesidades primarias planificadas para ocho
materiales cuando se desagregó el plan de producción para el grupo de productos bicicletas
y se transfirió a la gestión de demanda. Los materiales, representados por cajas al final de la
jerarquía en la Figura 8-16, incluyen seis tipos de bicicletas de turismo y dos tipos de
bicicletas todo terreno. Debido a que estos materiales son productos terminados, el sistema
ejecutará primero las etapas de la planificación de necesidades para cada uno de estos
materiales y creará necesidades secundarias para los componentes de sus LMats. La Figura
8-26 muestra la LMat para las bicicletas todo terreno. Cuando el sistema ha realizado las
tareas de la planificación de necesidades para esta bicicleta, crea necesidades secundarias
para cada material en la primera fila de su LMat. Luego que el sistema ha llevado a cabo las
tareas de la planificación de necesidades para los ocho productos terminados, ejecuta las
tareas de la planificación para los materiales con necesidades secundarias—esto es, los
componentes del primer nivel de productos terminados tales como el ensamble de rueda
todo terreno de aluminio (ORWA1000) en la Figura 8-26. Cuando el sistema ERP ha
finalizado las tareas de la planificación de necesidades para los componentes del primer
nivel, crea necesidades secundarias adicionales para sus componentes. Así, en el ejemplo,
cuando el sistema lleva a cabo las tareas de la planificación de necesidades para la
ORWA1000, crea necesidades secundarias para ORTR1000, ORTB1000 y ORWH1000.




Figura 8-26: LMat de bicicletas todo terreno

Un número de parámetros de control determina cómo se realizan las tareas del método de
planificación de necesidades. Uno de estos parámetros de control, la clave de tratamiento,
determina cómo se procesan los materiales en el fichero para petición de planificación.
Existen tres claves de tratamiento disponibles:

       •   PLANIFICACIÓN REGENERATIVA (NEUPL): La planificación regenerativa planifica todos
           los materiales relevantes para la planificación de necesidades. Todos los datos de
           las ejecuciones previas de planificación se descartan y se generan nuevos datos.
           En este escenario se procesa cada material, no solo aquellos en el fichero para
           petición de planificación. Por lo tanto, cuando hay un gran número de materiales,
           este proceso puede consumir mucho tiempo. Por esta razón rara vez se usa.
       •   PLANIFICACIÓN POR CAMBIO NETO (NETCH): En la planificación por cambio neto solo se
           planifican los materiales para los que ha habido una modificación relevante para
           la planificación de necesidades. Recuerde de la discusión anterior en este capítulo
           que una modificación relevante para la planificación de necesidades es cualquier
           actividad en el sistema que afecta la disponibilidad de materiales; tales como
           cambios en los elementos de planificación para el material; y estos cambios se
           identifican por una entrada en el fichero para petición de planificación.

       •   PLANIFICACIÓN POR CAMBIO NETO EN EL HORIZONTE DE PLANIFICACIÓN (NETPL).        La
           planificación por cambio neto en el horizonte de planificación solo planifica los
           materiales para los cuales ha habido una modificación relevante para la
           planificación de necesidades dentro de un período de tiempo específico llamado
           horizonte de planificación. El horizonte de planificación se define durante la
           configuración del sistema ERP como número de días laborables. El horizonte de
           planificación se especifica, generalmente, con una extensión superior al del
           tiempo de re-aprovisionamiento para la mayor parte de los materiales.

Los siguientes parámetros de control adicionales determinan la salida del método de
planificación de necesidades:

       •   Crear solicitudes de pedido. Este parámetro determina si la planificación de
           necesidades (1) siempre crea solicitudes de pedido para materiales
           aprovisionados externamente, (2) crea órdenes previsionales o (3) crea
           solicitudes de pedido solo en el horizonte de apertura y crea órdenes
           previsionales después del horizonte de apertura.

       •   Orden de entrega. Similar al ítem previo, este parámetro se aplica a los planes de
           entrega. Las opciones son (1) no crear repartos, (2) crearlos solo durante el
           horizonte de apertura, (3) crearlos solo durante el horizonte de planificación.

       •   Crear listas MRP. Este parámetro determina si el sistema creará una lista MRP, la
           cual se explicará más tarde en este capítulo. Otra opción es crear una lista MRP
           solo para materiales para los cuales se generan mensajes de excepción. El sistema
           ERP genera un mensaje de excepción cuando encuentra problemas con la
           programación. Por ejemplo, si el sistema determina una fecha de inicio que está
           en el pasado y tras no encontrar alternativa, se creará un mensaje de excepción.

       •   Modo de Planificación. El parámetro modo de planificación determina cómo se
           manejarán las propuestas de pedidos previamente creadas. Las opciones son
           ajustar las cantidades y fechas de las propuestas existentes o descartar las
           propuestas y crear nuevas.

       •   Programación. Este parámetro determina si el sistema debería calcular solo las
           fechas básicas utilizando los tiempos de planificación del maestro de materiales
           o si debe ejecutar el programa del ciclo de fabricación utilizando los tiempos más
           detallados en la hoja de ruta.
Salidas
El resultado de la etapa de planificaciones de necesidades son las propuestas de pedidos,
usualmente en la forma de solicitudes de pedido y órdenes previsionales, las cuales
desencadenan procesos de aprovisionamiento y producción, respectivamente. Esta etapa no
tiene implicaciones financieras, por lo que no se crea ningún documento FI o CO. Además,
debido a que no ocurre ningún movimiento de materiales, no se crea ningún documento de
material. Procesos de Negocio en la Práctica 8.3 describe planificaciones en SteelCase, Inc.

Procesos de Negocio en la Práctica 8.3: Planificación en Steelcase.
Para asegurarse de que los materiales adecuados son entregados en las instalaciones de
fabricación en el momento adecuado en las cantidades adecuadas, Steelcase debe vigilar y
gestionar constantemente los niveles de stock en el almacén y en el almacenamiento de las
líneas de producción mientras planifica constantemente cambios en los niveles de consumo de
las líneas de fabricación. La mayoría de los productos de Steelcase se fabrican para un pedido
de cliente específico (fabricación sobre pedido), así que hay una gran variabilidad en lo que un
centro debe fabricar de un día para otro. Steelcase también ha optimizado cada centro para la
fabricación de un tipo o conjunto específico de productos. Por ejemplo, un centro podría
especializarse en la fabricación de sillas de oficina mientras que otro enfocarse en cubículos y
archivadores manufacturados. Aunque esta estrategia permite a Steelcase maximizar sus
recursos de capital, también presenta un gran nivel de complejidad en el proceso de
planificación de manufactura porque los pedidos de cliente deben dividirse entre múltiples
centros y consolidarse en el centro de distribución regional (RDC) para la entrega final al
cliente.

El tiempo de aprovisionamiento estándar (desde que se genera un pedido hasta la entrega)
para un pedido de cliente es, generalmente, entre dos a tres semanas. Este programa genera
aproximadamente 14 días de visibilidad general de las necesidades de fabricación desde los
cuales se puede derivar la planificación de materias primas. Sin embargo, cada centro
típicamente tiene solo seis días de visibilidad de lo que se fabricará antes que se necesite
despachar al RDC. Así, cada centro de fabricación debe, normalmente, comprar, recibir y
mantener suficientes materiales para realizar la fabricación del pedido de cliente en menos de
una semana. Además, los centros de fabricación pueden recibir varias entregas de materias
primas diariamente de los proveedores. Esta modalidad reduce costos de movimiento de stock
y optimiza el uso del espacio de almacenamiento limitado. Para gestionar este ambiente de
planificación dinámico, Steelcase utiliza capacidades avanzadas de planificación en su sistema
SAP ERP para evaluar y planificar las necesidades de materiales. Cada instalación de
fabricación de Steelcase tiene alrededor de siete empleados de planificación que
constantemente administran este proceso. Cada centro de fabricación ejecuta MPS y MRP al
menos tres veces al día para evaluar el estado y las necesidades de todos los pedidos de cliente,
materiales, listas de materiales y cambios en el stock.

Fuente: Steelcase, Inc.
