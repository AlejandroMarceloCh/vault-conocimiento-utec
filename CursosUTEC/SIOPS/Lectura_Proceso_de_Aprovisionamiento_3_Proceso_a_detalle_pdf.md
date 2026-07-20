---
curso: SIOPS
titulo: Lectura - Proceso de Aprovisionamiento (3. Proceso a detalle)
slides: 23
fuente: Lectura - Proceso de Aprovisionamiento (3. Proceso a detalle).pdf
---

   PROCESO
Ahora que está familiarizado con los conceptos básicos involucrados en el
aprovisionamiento, se cambia el foco de atención al proceso mismo. Al comienzo de este
capítulo se introdujo un proceso de aprovisionamiento muy simple que incluía unas pocas
etapas claves. En esta sección se estudia un proceso más completo. Se examina también cada
etapa en detalle.

En esta sección, se discute la compra de una posición estándar. Las etapas utilizadas para
aprovisionarse de posiciones estándar se esquematizan en la Figura 4-12. La figura indica
que el proceso de aprovisionamiento se desencadena por algún evento que provoca una
necesidad de adquirir materiales. El desencadenante a menudo es el resultado de un evento
en otro proceso. Por ejemplo, la empresa no puede cumplir una orden de fabricación (una
etapa del proceso de producción) hasta que compre ciertos materiales necesarios. Por otra
parte, el proceso de planificación de materiales puede alertar a la empresa que necesita
aumentar su stock de algunos materiales. Independiente del desencadenante, el resultado es
una necesidad de obtener materiales. Esta necesidad normalmente toma la forma de una
solicitud de pedido.




                  Figura 4-12: Proceso de aprovisionamiento detallado

Tomado de:

Magal S. y Word J. (2017) Integración de Procesos de Negocio con Sistemas ERP. Epistemy
Press LLC. Adaptación al español de: Magal S. and Word J. (2012) Integrated Business
Processes with ERP Systems. John Wiley & Sons. Hoboken. NJ, USA.
Una vez que se crea una solicitud, la empresa debe seleccionar una fuente de
aprovisionamiento. Esta fuente puede ser externa (p.e., un proveedor) o interna (p.e., otro
centro en la empresa). Si la fuente es externa, entonces el proceso de selección puede incluir
etapas adicionales tales como solicitar y recibir ofertas o cotizaciones. Luego de que la
empresa recibe las cotizaciones, las evalúa y selecciona un proveedor. Luego emite un pedido
de compra. Una vez recibido el pedido, el proveedor confirma la recepción y puede
proporcionar información adicional tal como la fecha de envío esperada. El proveedor
entonces envía los materiales a la empresa que los recibe en existencias. El proveedor
también envía una factura. Una vez que la empresa verifica la factura, envía un pago al
proveedor.

Si la fuente de aprovisionamiento es interna entonces el proceso es algo diferente. Se usa un
pedido de traslado en lugar del pedido de compra. Se estudiarán los pedidos de traslado en
mayor detalle en el capítulo de gestión de stocks y almacenes.

Los párrafos anteriores presentan una visión muy simplificada de las etapas básicas del
proceso de aprovisionamiento. En realidad el aprovisionamiento es mucho más complejo. En
la siguiente sección se examinan en detalle las etapas que se muestran en la Figura 4-12. Se
discute cada etapa en términos de sus elementos claves, desencadenantes, datos, tareas y
salidas. Un desencadenante es algo que provoca que la etapa se ejecute. Los datos relevantes
generalmente incluyen datos organizativos, datos maestros, datos de transacciones y
entrada de usuario que son específicos para la etapa del proceso. Las salidas incluyen nuevos
datos de transacción y actualizaciones de los datos maestros, todo lo cual se almacena en la
base de datos. Adicionalmente, se crean documentos de contabilidad financiera (FI),
documentos de contabilidad administrativa o controlling (CO) y documentos de material.
Finalmente, se crean o actualizan documentos de transacción.

DETERMINACIÓN DE NECESIDADES
Los elementos de la etapa de determinación de necesidades o requerimientos se resumen en
la Figura 4-13. Los requerimientos de material surgen a partir de una necesidad que se
identifica automáticamente por otro proceso o manualmente por un individuo. El proceso
que más genera necesidades es el proceso de planificación de materiales. (Se discutirá este
proceso en profundidad en el capítulo de planificación de materiales.) Las necesidades se
generan también a partir de los procesos de producción y mantenimiento de centros. Para
completar estos procesos la empresa a veces debe comprar posiciones no de almacén o
servicios de otra organización. En tales casos, se crea una necesidad para el material o
servicio. En suma, la necesidad de enviar materiales para tratamiento externo durante la
producción (por ejemplo una pieza a ser reparada) se traducirá en un requisito para una
posición subcontratada.
Figura 4-13: Elementos de la etapa de determinación de necesidades

También se crean necesidades manualmente para posiciones que no se incluyen en la
planificación de materiales. Este proceso ocurre cuando un individuo administra el
inventario o cuando la empresa necesita una posición no de almacén (p.e., suministros) o un
servicio (p.e., limpieza o reparación). Sin importar el desencadenante o la fuente, la
necesidad de materiales se documenta en la forma de una SOLICITUD DE PEDIDO. Recuerde que
una solicitud de pedido es un documento que se usa para propósitos internos,
particularmente, para solicitar materiales requeridos. No es un compromiso de compra de
materiales o servicio. Más bien, el compromiso se genera cuando se crea un pedido de
compra en la siguiente etapa del proceso.

Datos
Los datos necesarios para crear una solicitud de pedido son los tipos de posición, cantidad,
fecha de entrega deseada y almacén de entrega o centro receptor deseado (vea la Figura 4-
14). Además, se necesita un número de material para las posiciones de almacén y se puede
necesitar un objeto de imputación dependiendo del tipo de posición seleccionado. El sistema
ERP utiliza el número de material para obtener datos adicionales desde el maestro de
materiales tales como la denominación, grupo de material, grupo de compras, unidad de
medida y el precio de valoración. La fecha y lugar de entrega las proporciona normalmente
el solicitante, pero también se pueden obtener del maestro de materiales.
Figura 4-14: Datos de una solicitud de pedido

Los datos organizativos requeridos para crear una solicitud de pedido son el grupo de
compras y el centro receptor. Estos datos se obtienen del maestro de materiales. La entrada
de usuario puede proveer o anular estos datos, a medida que se necesite.

Los datos del proveedor son opcionales. Cuando se incluyen, indican una preferencia por la
fuente de aprovisionamiento. Los datos del proveedor incluyen su número y su nombre.

También se puede necesitar materiales que no tienen datos en el maestro de materiales, pero
este procedimiento se debe llevar a cabo manualmente. Básicamente, el solicitante
proporciona una denominación del material en lugar de un número de material. Además,
proporciona datos que normalmente se obtienen del maestro de materiales, incluyendo el
lugar de entrega, grupo de material, grupo de compras y el tipo de imputación. Además,
dependiendo del tipo de imputación, se pueden incluir también datos adicionales tales como
centro de costo, número de activo fijo y cuentas del libro mayor. (En este punto puede que
desee revisar la discusión de determinación de cuentas al inicio del capítulo).

Tareas
La única tarea en esta etapa es crear la solicitud de pedido usando los datos especificados.

Salidas
El documento de transacción que resulta de esta etapa es la solicitud de pedido. El sistema
asignará un número único de solicitud a este documento, el que las partes interesadas
pueden utilizar para rastrear su progreso a través de las etapas del proceso. Es importante
considerar, que estas etapas no generan documentos de contabilidad financiera o interna
debido a que crear una solicitud no tiene impacto financiero8. Además, como no hay
movimiento de mercancías (es decir, no se reciben materiales), tampoco se crea un
documento de material.

En el ejemplo, el desencadenante del proceso de aprovisionamiento es un bajo stock de
camisetas. GBI ha determinado (a través de la planificación de materiales, la cual se discute
en el Capítulo 8) que las camisetas se deben reordenar cuando hay 50 o menos en stock.
Además, las camisetas se deben comprar en cantidades de 500. Un empleado del centro que
revisa los informes de stocks que se imprimen al inicio de cada día, alertó de la necesidad de
volver a ordenar camisetas. Este empleado observó que el stock de camisetas en el centro de
Miami había descendido bajo 50. Como resultado, él creo una solicitud de pedido por 500
camisetas para ser enviadas al centro de Miami en una cierta fecha.

DETERMINACIÓN DE FUENTE DE APROVISIONAMIENTO
Una vez más, una solicitud es simplemente una solicitud de material; no representa una
obligación legal para comprar. Por el contrario, un PEDIDO DE COMPRA constituye una
obligación para comprar. Como muestra la Figura 4-15, existen tres formas para crear un
pedido de compra, dependiendo de si la fuente de aprovisionamiento es conocida. Si lo es,
entonces la solicitud se puede convertir en un pedido de compra sin pasos adicionales (Ruta
1). En tales casos la empresa selecciona un proveedor de una lista de potenciales
proveedores, llamada LIBRO DE PEDIDOS. Si el libro de pedidos contiene solo una fuente de
pedidos, entonces el sistema automáticamente asignará el proveedor a la solicitud. Sin
embargo, si el libro de pedidos identifica múltiples fuentes, entonces el sistema mostrará una
lista de proveedores para que el usuario pueda elegir. Alternativamente, la solicitud se puede
concretar a través de CONTRATOS MARCO, los cuales son acuerdos a largo plazo entre una
organización y un proveedor con respecto al suministro de materiales o la prestación de
servicios dentro de un periodo especificado de acuerdo a términos y condiciones
predefinidas. Los acuerdos marco se dividen en PEDIDOS ABIERTOS y PLANES DE ENTREGA. Durante
el periodo de validez del pedido abierto, se emiten (se liberan) ciertas cantidades o servicios
mediante el pedido abierto cuando sea necesario emitiendo pedidos de compra. Tales
pedidos de compra se denominan órdenes de entrega para pedido abierto o simplemente
órdenes de entrega. En algunos sistemas que no son SAP, también se conocen como pedidos
de compras bajo demanda. En un plan de entregas, la entrega de la cantidad total del material
especificado en el plan se extiende durante un cierto período de tiempo de acuerdo con un
plan de entrega. El plan de entrega especifica las cantidades con sus fechas de entrega
previstas correspondientes.
Figura 4-15: Conversión de una solicitud de pedido en un pedido de compra

Si no se conoce una fuente de aprovisionamiento, entonces la empresa debe enviar una
solicitud de oferta o cotización (RFQ) a varios proveedores potenciales, recibir y evaluar las
cotizaciones y luego realizar una selección final. Una RFQ es una invitación a proveedores de
parte de una organización para presentar una cotización para el suministro de materiales o
servicios. Una cotización es legalmente vinculante para el proveedor por un cierto periodo.
Identifica materiales o servicios para las cuales se especifican cantidades y fechas de entrega.
En este caso, la organización utiliza una oferta para crear un pedido de compra (ruta 2).
Finalmente, en algunos casos, la RFQ se convierte directamente en un pedido de compra sin
una oferta (ruta 3). Este puede ser el caso cuando un proveedor proporciona una cotización
verbalmente y la empresa no considera necesario ingresar los datos de la cotización en el
sistema.

En el ejemplo, Spy Gear es el único proveedor de camisetas. Esta información se determina
a partir de un libro de pedidos que se mantiene en el sistema ERP. Debido a que existe un
proveedor establecido, no es necesario para GBI solicitar y evaluar cotizaciones de
potenciales proveedores.



TRATAMIENTO DE PEDIDO DE COMPRA
Tal como se explicó anteriormente, un PEDIDO DE COMPRA es una comunicación enviada a un
proveedor en el cual una empresa se compromete a comprar los materiales especificados
bajo los términos establecidos. La Figura 4-16 resume los elementos de la etapa de
tratamiento de pedido de compra.
Figura 4-16: Elementos de la etapa de tratamiento de pedido de compra

Un pedido de compra generalmente se crea con referencia a una solicitud, un RFQ, una oferta
o un pedido de compra creada previamente. Cuando se utilizan documentos de referencia
para crear un pedido de compra, se copian muchos de los datos necesarios de estos
documentos. Además, un pedido de compra se puede crear sin referencia a algún documento.
En este caso, todos los datos necesarios se ingresan manualmente.

Datos
Un pedido de compra incluye datos de variadas fuentes, como se muestra en la Figura 4-17.
Además de los documentos fuente, se incluyen también datos de varios registros maestros,
tales como maestro de materiales, maestro de proveedores, registros info de compras y
condiciones. Adicionalmente, se pueden incorporar datos de acuerdos y contratos
específicos con el proveedor seleccionado.

La mayoría de los datos en una solicitud de pedido (Figura 4-14) se incluyen en el pedido de
compra. Además, el pedido de compra contendrá otros datos dependiendo de cómo se creó
el pedido y cuáles documentos de referencia se utilizaron. Por ejemplo, las características de
los materiales, tales como el peso, se obtienen del maestro de materiales. Los datos de
proveedores, tales como métodos de comunicación, persona de contacto y dirección, se
obtienen del maestro de proveedores o de la oferta. Los datos de precios, las condiciones de
pago e Incoterms®9 se obtienen de la oferta, del registro info de compras, de otros registros
de condición o de contratos y acuerdos específicos con el proveedor, dependiendo de cómo
se configura el proceso en cada empresa.
                       Figura 4-17: Datos de un pedido de compra

Si los datos necesarios no están disponibles en el documento de referencia, entonces el
usuario debe proporcionar esta información manualmente cuando esté creando el pedido de
compra.

Como se representa en la Figura 4-18, un documento de pedido de compra consta de una
sección cabecera y una o más posiciones (o detalle). La cabecera incluye datos tales como
número del pedido de compra, proveedor, moneda, fechas y condiciones de pago. Estos datos
se aplican a todo el documento, incluyendo todas las posiciones. La sección de posiciones
(detalle) incluye datos específicos para cada posición del pedido de compra, tales como
número de material, denominación, cantidad, fecha de entrega y precio.




                     Figura 4-18: Estructura de un pedido de compra
Tareas
La primera tarea en esta etapa es crear y enviar el pedido de compra al proveedor. Además,
pueden ser necesarias otras etapas, dependiendo de cómo se crea el pedido. Las etapas
adicionales más comunes involucran seleccionar un proveedor y luego comunicarse con él
para confirmar detalles de logística y entrega.

Salidas
El documento principal creado en esta etapa es el pedido de compra. Si el pedido incluye
datos obtenidos de documentos de referencia, entonces se pueden usar múltiples
documentos para generar un pedido. Al contrario, se puede usar un único documento de
referencia para crear múltiples órdenes. De este modo, como se puede observar en la Figura
4-19, una o más solicitudes pueden generar uno o más pedidos de compra. Por ejemplo,
considere los siguientes escenarios. Un administrador de compras recibe múltiples
solicitudes para los mismos materiales y decide consolidarlas en un solo pedido de compra
y envía el pedido a un proveedor, tal vez para aprovechar descuentos por volumen. Por otra
parte, las solicitudes pueden incluir una cantidad de materiales diferentes que se deben
comprar a distintos proveedores. En este caso, el administrador de compras crea un pedido
de compra diferente para cada proveedor que incluye los materiales correspondientes.




                   Figura 4-19: Solicitud de pedido a pedido de compra

Las solicitudes de pedido se actualizan para reflejar el número(s) de pedido de compra
asignado(s) a ellas. Este proceso permite al solicitante determinar fácilmente el estado de
cada solicitud. También puede hacer clic en el número de documento PC ahora referenciado
en la solicitud de pedido para ver el pedido de compra y su estado.

Aunque el pedido de compra es una obligación para adquirir materiales de un proveedor, no
se crean documentos de contabilidad financiera porque esta etapa no tiene impacto en la
condición financiera de la organización. (A pesar del compromiso de compra, no se ha
intercambiado dinero ni productos). Recuerde, sin embargo, la nota acerca de compromisos
en la contabilidad administrativa en el caso de una solicitud para materiales de consumo. Si
un pedido de compra se crea sin referencia a una solicitud, entonces se crea un compromiso
cuando se crea el pedido de compra. Además, no se crean documentos de material porque
no ha ocurrido ningún movimiento de mercancías (entrada de mercancías).

Una vez que el pedido de compra se crea, se debe comunicar al proveedor. Esta comunicación
se realiza utilizando las capacidades de mensajería de SAP ERP, como se muestra en la Figura
4-20. SAP ERP utiliza una variedad de medios, incluyendo la impresión, correo, EDI, servicios
web y fax. Las empresas también utilizan las capacidades de mensajería del sistema para
enviar recordatorios y para solicitar que se acelere el proceso de entrega. A su vez, el
proveedor usa estas capacidades tanto para aceptar como para rechazar el pedido.




                       Figura 4-20: Comunicación con proveedores

La Figura 4-21 muestra las distintas opciones relacionadas con la etapa del pedido de
compra. En resumen, una empresa crea un pedido de compra usando una variedad de
documentos fuente (o ninguno) y entradas de usuario y luego lo comunica a un proveedor
externo o a otro centro en la empresa mediante diversas herramientas de comunicación.
              Figura 4-21: Opciones de tratamiento de un pedido de compra

ENTRADA DE MERCANCÍAS
La próxima etapa en el proceso de aprovisionamiento es la entrada de mercancías, que
registra la recepción de los materiales desde el proveedor. Los elementos de esta etapa se
resumen en la Figura 4-22.




               Figura 4-22: Elementos de la etapa de entrada de mercancías
El envío de materiales desde el proveedor se acompaña de un DOCUMENTO DE ENTREGA, también
conocido como una LISTA DE EMBALAJE, que identifica los materiales incluidos en la entrega y
el número de pedido de compra asociado con la entrega. El receptor usa este documento para
verificar que se hayan enviado los materiales correctos en las cantidades correctas.

Un único pedido de compra puede dar lugar a múltiples entregas. Esto puede ocurrir, por
ejemplo, cuando los materiales son muy voluminosos o las cantidades son demasiado
grandes para un solo embarque. Por otro lado, los materiales ordenados en múltiples
pedidos de compra se pueden enviar en un solo embarque. En el ejemplo, el proveedor, Spy
Gear, entrega las 500 camisetas en un solo embarque. El documento de entrega asociado
indica que hay 5 cajas de 100 camisetas.

Cuando se recibe un embarque, se compara con el (los) pedido(s) de compra indicado(s).
Revisar la entrega con su pedido de compra ofrece varios beneficios. Primero, permite a la
empresa que recibe verificar que los materiales enviados son los que ordenaron. Segundo,
los datos relevantes del pedido de compra, tales como datos de materiales y cantidades, se
copian automáticamente en el DOCUMENTO DE ENTRADA DE MERCANCÍAS que se crea en esta etapa.
Esto hace que la etapa de entrada de mercancías sea más eficiente y menos propensa a
errores. Por supuesto, los datos copiados en la entrada de mercancías se pueden editar si la
cantidad entregada no es la misma que la ordenada. Una empresa puede aceptar una entrega
sin requerir un pedido de compra. En estos casos, sin embargo, no contará con los beneficios
indicados anteriormente.

Datos
La mayoría de los datos necesarios para completar la tarea de entrada de mercancías se
encuentran en el documento de entrega y el pedido de compra. Estos datos se muestran en
la Figura 4-23. El pedido de compra proporciona datos acerca de los materiales que la
empresa ordenó y el documento de entrega contiene datos acerca de los materiales que
realmente recibió. También son necesarios datos adicionales sobre el lugar donde se
almacenarán los materiales (centro y almacén) y la clase de movimiento específica. El
sistema sugerirá valores para estos datos y el usuario podrá modificarlos si es necesario.
                  Figura 4-23: Datos de la etapa de entrada de mercancías

Tareas
La principal tarea en la etapa de entrada de mercancías es verificar y registrar los materiales
incluidos en el embarque en el documento de entrada de mercancías. El usuario ingresará al
sistema y creará un documento de entrada de mercancías proporcionando el número de
pedido de compra. El sistema recuperará el pedido de compra y automáticamente agregará
los datos relevantes al documento de entrada de mercancías. El usuario verificará entonces
que los datos sean correctos. Es decir, que los materiales y cantidades enviadas coincidan
con lo que la empresa ordenó. Como se explicó anteriormente, un pedido de compra puede
generar múltiples entregas. En tales casos, el usuario modificará los datos para reflejar los
materiales y cantidades que la empresa realmente recibió. Cuando se registran entregas
parciales, el pedido de compra se puede usar nuevamente cuando se entregue el resto de los
materiales.

Recuerde de la explicación anterior sobre los tipos de stocks que los productos se pueden
recibir y asignarles uno de tres estados: de libre utilización, en inspección de calidad y
bloqueado. La opción por defecto es recibir materiales de libre utilización. Recibir los
materiales en el estado de inspección de calidad se puede lograr de varias formas. Si los
materiales están normalmente sujetos a inspección de calidad, entonces se habilita
(verificado) el indicador “contabilizar en el stock de inspección de calidad” en la vista de
pedidos del maestro de materiales. Esto automáticamente se traducirá en una entrada de
mercancías en el estado de inspección de calidad. También causará que se incluya el status
de stock en el pedido de compra y en el documento de entrada de mercancías para el
material. Si la inspección se requiere solo en casos específicos, entonces el status de stock se
puede especificar en el pedido de compra o durante la entrada de mercancías. Finalmente,
los materiales se pueden designar como bloqueados si no corresponde a lo que la empresa
ordenó o si no son aceptables por cualquier razón.

En el ejemplo, GBI ha recibido un embarque de Spy Gear. El embarque incluye un documento
de entrega que indica que hay 5 cajas, cada una conteniendo 100 camisetas. Un empleado de
GBI verifica los contenidos contra el documento de entrega y registra la recepción en el
sistema ERP. Lo hace recuperando el pedido de compra identificado en el documento de
entrega e indicando que los materiales ordenados fueron recibidos.

Salidas
Además de crear el documento de entrada de mercancías, la etapa de entrada de mercancías
tiene varias consecuencias para múltiples áreas de la organización. Cabe destacar, que es la
primera etapa en el proceso de aprovisionamiento que tiene un impacto en la contabilidad
financiera, específicamente, en las cuentas del libro mayor. La Figura 4-24 muestra el
impacto financiero de recibir 500 camisetas en el ejemplo. La cuenta de existencias
(mercaderías) se carga por el valor de los productos recibidos, es decir, $7.500. El abono
correspondiente se contabiliza en la cuenta de entrada de mercancías/recepción de factura
(EM/RF). Se abona esta cuenta en lugar de la de acreedores para reflejar que se ha recibido
la mercadería, pero aún no se ha recibido la factura, documento que establece formalmente
la obligación de pago al proveedor. Si la compra es por un material de consumo, entonces se
carga la cuenta de gasto que corresponda, tal como la cuenta de gasto por suministros, en
lugar de una cuenta de existencias.




                Figura 4-24: Impacto financiero de la entrada de mercancías

Se crean también un documento de material y un documento contable; ellos se muestran en
la Figura 4-25. En el documento de material la cabecera incluye el número de documento de
material, la fecha y el número de documento de entrega asociado. Las posiciones identifican
los materiales recibidos, la cantidad recibida, el lugar (centro) y la clase de movimiento. En
el documento contable la sección de la cabecera consta del número de documento, fecha,
moneda y una referencia al documento de entrega. La sección de posiciones (o detalle)
muestra las dos cuentas del libro mayor que se ven afectadas por la entrada de mercancías,
un cargo en la cuenta de existencia (mercaderías) y un abono en la cuenta EM/RF. El
documento contable es un registro de las imputaciones hechas en las cuentas del libro
mayor.




      Figura 4-25: Documentos de material y contable de una entrada de mercancías

La etapa de entrada de mercancías también se traduce en actualizaciones del pedido de
compra y del maestro de materiales. El historial de pedidos de compra se modifica para
incluir el número de documento de material. Un usuario es capaz de recuperar el pedido de
compra (o la solicitud de pedido, la cual, si recuerda incluye un enlace al pedido de compra)
y desplegar la historia del pedido de compra. Dicho historial mostrará el número de
documento de material, al cual el usuario puede acceder para ver detalles. En el maestro de
materiales, se actualiza la cantidad, valor y el precio medio variable.

La etapa de entrada de mercancías puede ser seguida por varias etapas opcionales,
incluyendo la creación de lotes de inspección, necesidades de transporte, notificaciones y
salidas. Cabe destacar que, SAP ERP incluye ciertas capacidades opcionales que permite a las
empresas implementar estas etapas. Una de estas capacidades, gestión de calidad, crea un
lote de inspección de los productos recibidos y desencadena varias etapas del proceso de
gestión de calidad. Un lote de inspección es una solicitud para una inspección de calidad de
los materiales recibidos. Incluye detalles tales como cuántos materiales y qué características
se inspeccionarán. Por el contrario, la gestión de almacenes, otra capacidad opcional, genera
una necesidad de transporte. Una necesidad de transporte documenta la necesidad de
almacenar o retirar materiales de un almacén. Por lo tanto, sirve como desencadenante para
los procesos de gestión de almacenes. Se discutirá la gestión de almacenes en el Capítulo 7.
Un ejemplo de una notificación es cuando a las personas que corresponda de la organización,
tales como el solicitante original, se les informa que los materiales se han recibido.
Finalmente, un ejemplo de una salida es un vale de entrada de mercancías, el cual es un
documento que utiliza el personal del centro para asegurarse que almacenan los materiales
en los lugares correctos.



VERIFICACIÓN DE FACTURA
La siguiente etapa en el proceso es VERIFICACIÓN DE FACTURA, que se resume en la Figura 4-26.
Cuando una empresa recibe la factura de un proveedor, verifica que la factura sea correcta
antes de hacer el pago. El método más común para verificar una factura es la TRIPLE
VERIFICACIÓN entre el pedido de compra, el documento de entrada de mercancías y la factura.
El objetivo es asegurar que las cantidades y los precios en los tres documentos sean
consistentes. Una alternativa es una doble verificación entre un pedido de compra y el
documento de entrada de mercancías. Este método no es muy común, y requiere un alto
grado de confianza y cooperación entre socios. En el ejemplo, GBI colocó un pedido de
compra por 500 camisetas de Spy Gear. El centro de Miami recibió el envío de Spy Gear de 5
cajas de 100 camisetas (500 en total). Spy Gear envió a GBI una factura por 500 camisetas.
Además, el precio en el pedido de compra y en la factura es el mismo. De este modo, GBI
puede hacer una triple verificación entre las 500 unidades ordenadas por $15 cada una, las
500 unidades recibidas y las 500 unidades facturadas por $15 cada una.




Figura 4-26: Elementos de la etapa de verificación de factura

Datos
La Figura 4-27 muestra los datos que son necesarios para completar la etapa de verificación
de factura. Los datos proporcionados por la factura incluyen el número de proveedor, fecha
de la factura, cantidad y el monto de la factura. Los datos del pedido de compra incluyen el
número de proveedor, materiales, cantidades y precio. Finalmente, los materiales y
cantidades recibidas se obtienen del documento de material creado durante la etapa de
entrada de mercancías.
                Figure 4-27: Datos necesarios para la verificación de factura

Tareas
Para completar esta etapa, el usuario proporcionará los datos de la factura (proveedor, fecha
y cantidad) y el número del pedido de compra. El sistema entonces recuperará todos los
datos necesarios del pedido de compra (proveedor, materiales, cantidades y precio).
También recuperará los datos de la entrada de mercancías para el pedido de compra. El
usuario verificará que los datos son correctos y, si lo son, aprobará la factura.
Ocasionalmente, habrá discrepancias entre los tres conjuntos de datos. Por ejemplo, la
cantidad entregada o el precio pueden variar un poco. Si estas discrepancias son aceptables,
dependerá de las políticas de compras y contabilidad la organización, las cuales se
especifican en el maestro de materiales u otros datos maestros como sobre y bajo las
tolerancias. Si las discrepancias se encuentran dentro de las tolerancias, entonces la factura
se aprueba para pago. Si no, la factura será bloqueada, y se requerirá una acción adicional
del departamento de contabilidad o del departamento de compras, antes de que se pueda
liberar.

Salidas
Como se puede ver en la Figura 4-28, la verificación de factura tiene un impacto en el libro
mayor. La Figura muestra los datos para el ejemplo. Específicamente, un cargo por $7.500 se
contabiliza en la cuenta EM/RF, y la cuenta del proveedor se abona por el mismo monto.
Debido a que la cuenta del proveedor es una cuenta del libro auxiliar, se abona también
automáticamente la cuenta asociada correspondiente del libro mayor—la cuenta asociada
acreedores. Se crea el documento de contabilidad financiera correspondiente. Además, se
crea un documento de factura.
                Figura 4-28: Impacto financiero de la verificación de factura

El historial del pedido de compra también se actualiza y se agrega un enlace al documento
de factura. Finalmente, si el precio de la factura es diferente del precio del pedido de compra,
entonces el maestro de materiales se debe actualizar para reflejar esta discrepancia, siempre
que el control de precio utilice el precio medio variable. Recuerde que cuando se registra una
entrada de mercancías, la cantidad, valor y precio medio variable se actualizan en el maestro
de materiales. Cuando se recibe una factura y el precio es diferente al del pedido de compra,
el valor del material y el precio medio variable se deben ajustar para reflejar los nuevos
valores.

La verificación de factura realiza el enlace entre la gestión de materiales y la contabilidad.
Esta autoriza el pago de la factura al proveedor, que es la siguiente, y última, etapa en el
proceso de aprovisionamiento.

GESTIÓN DE PAGOS
La Figura 4-29 muestra los elementos de la etapa final en el proceso de aprovisionamiento –
en particular, pagar al proveedor. Esta etapa se desencadena por la recepción y verificación
de una factura.
                       Figura 4-29: Elementos de la etapa de pago

Los pagos se pueden realizar manual o automáticamente a través de un programa de pagos.
Generalmente, una organización tendrá un número de facturas por pagar, y el método más
común es ejecutar un programa de pago periódicamente, ya sea diario o semanal. El
programa recuperará todas las facturas autorizadas durante un periodo de tiempo
especificado y creará automáticamente pagos.

Datos
La Figura 4-30 destaca los datos necesarios para procesar pagos al proveedor. Los datos de
la factura incluyen la fecha, el número de proveedor y el monto de la factura. Además,
condiciones y método de pago y dirección se obtienen del maestro de proveedores. Los datos
de la factura se comparan con las condiciones de pago y la fecha de la próxima ejecución
proyectada del programa de pagos con el fin de determinar cuáles son las facturas
pendientes de pago.




                 Figura 4-30: Datos necesarios para el pago al proveedor
Tareas
El proceso de pago involucra varias etapas: seleccionar un método de pago y un banco,
decidir qué facturas están listas para ser pagadas, calcular montos de pago, contabilizar los
documentos de pago e imprimir el medio de pago. Cuando los pagos se hacen manualmente,
el usuario elegirá el método de pago y el banco, y proporcionará el número de proveedor y
el monto del pago. El sistema entonces presentará una lista de facturas abiertas para ese
proveedor. Luego, el usuario seleccionará las facturas a pagar. A continuación se aplican los
descuentos que correspondan de acuerdo a las condiciones de pago. Por ejemplo, si la
condición de pago es 2%/10Net3010 y el pago se realiza dentro de los 10 días especificados,
el sistema aplicará un descuento del 2%. Una vez que el pago se contabiliza en el libro mayor,
se puede enviar el pago real. Si el pago se realiza electrónicamente, el sistema enviará
automáticamente el pago. Si se hace a través de un cheque impreso, el usuario imprimirá y
enviará el cheque al proveedor.

Si la empresa tiene un programa de pago automatizado, entonces el programa recuperará y
procesará todas las facturas que están pendientes de pago utilizando parámetros que se
especifican en el programa de pago. Normalmente, los usuarios solo se involucran si hay
excepciones que requieren resolución especial.

Salidas
Una salida obvia de esta etapa es el pago al proveedor, ya sea electrónicamente o por medio
de un cheque. Las cuentas pertinentes del libro mayor se actualizan, como se muestra en la
Figura 4-31 y se crea el documento de contabilidad financiera correspondiente. Como indica
la figura, la cuenta banco se abona por el monto del pago y la cuenta del proveedor se carga,
así como la cuenta asociada acreedores.

                  Figura 4-31: Impacto financiero del pago a proveedores

INTEGRACIÓN CON OTROS PROCESOS
Debería quedar claro, a partir de la discusión anterior, que el proceso de aprovisionamiento
está fuertemente integrado con varios otros procesos dentro de una organización. Algunos
de estos puntos de integración, tales como con la contabilidad financiera, se explicaron en
detalle, mientras que otros fueron mencionados brevemente. Explicamos en detalle estos
otros puntos de integración en los capítulos siguientes. A continuación, se resume
brevemente cómo aprovisionamiento se vincula con los otros procesos. La Figura 4-32
muestra estos vínculos.

El registro del maestro de proveedores lo mantienen conjuntamente compras y contabilidad.
Además, varias etapas del proceso de aprovisionamiento, tales como entrada de mercancías,
verificación de facturas y gestión de pagos, afectan las cuentas del libro mayor. Más aún,
cuando una empresa compra materiales para consumo, utiliza un objeto de controlling, tal
como un centro de costo, el cual se relaciona con la contabilidad administrativa, para imputar
la compra a grupos o departamentos.

Actividades de la planificación de materiales, producción, gestión de pedidos, gestión de
activos fijos de la empresa y gestión de proyectos, generan solicitudes de pedido que se
procesan dentro del proceso de aprovisionamiento. Objetos de estos procesos, tales como
pedidos de clientes y órdenes de fabricación, se imputan con las compras de los materiales.
Finalmente, el aprovisionamiento involucra movimientos de materiales e inspecciones de
calidad que son el dominio de la gestión de stocks y almacenes.




                        Figura 4-32: Integración con otros procesos



RESUMEN DEL CAPÍTULO
El proceso de aprovisionamiento involucra las actividades requeridas para comprar, recibir
y pagar los productos y servicios que una organización necesita para sus operaciones. El
proceso de aprovisionamiento de una empresa normalmente se optimiza para los tipos de
bienes y servicios que compra y la ubicación y uso de esos productos por otros procesos, tal
como producción. Debido a que el proceso de aprovisionamiento involucra una intensa
colaboración e intercambio comercial con los proveedores, se debe vincular
estratégicamente con los procesos de producción y planificación de materiales para asegurar
que la cantidad apropiada de los materiales adecuados se adquieren a un precio justo, en el
momento oportuno. Además, dado el monto de dinero que las empresas gastan durante el
proceso de aprovisionamiento, muchos de los datos y requisitos asociados con este proceso
se definen para asegurar se cumple adecuadamente con la contabilidad financiera y
administrativa.
El proceso de aprovisionamiento consiste en seis etapas claves: determinación de
necesidades, selección del proveedor, tratamiento de pedidos, entrada de mercancías,
verificación de factura y gestión de pagos. Para funcionar apropiadamente, el
aprovisionamiento requiere datos organizativos tales como centro, almacenes, organización
de compras y grupo de compras. Asimismo, se necesitan datos maestros para contabilizar el
valor de los productos y servicios que se compran así como para propósitos de controlling a
fin de gestionar el proceso eficientemente. Tolerancias, controles y condiciones son
cualidades predeterminadas de los datos que permiten al proceso de aprovisionamiento
operar en una forma más automatizada. Los materiales que ha recibido la empresa se deben
asignar a una cuenta de materiales en orden para registrar apropiadamente el impacto
financiero de la compra y uso del material. Además, los materiales que han ingresado a stock
se deben clasificar de acuerdo a su estado de disponibilidad para asegurar que se asignen
correctamente a los procesos que los utilizan.
