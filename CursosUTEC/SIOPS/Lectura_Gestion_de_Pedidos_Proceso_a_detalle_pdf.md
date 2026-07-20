---
curso: SIOPS
titulo: Lectura - Gestión de Pedidos (Proceso a detalle)
slides: 31
fuente: Lectura - Gestión de Pedidos (Proceso a detalle).pdf
---

    ​PROCESO
La ​Figura 19 ​muestra las etapas del proceso de gestión de pedidos. El proceso
comienza con actividades de preventa y concluye con el recibo de pago del cliente. Las
actividades de preventa son opcionales y se diseñan para identificar y desarrollar
relaciones con el cliente. Muy a menudo, el proceso comienza con el procesamiento
del pedido de cliente, el que se ejecuta con el recibo del pedido de compra del cliente.
Como el nombre sugiere, el procesamiento del pedido de cliente involucra crear un
pedido de cliente, el cual es un documento interno usado para manejar y seguir el
pedido a medida que fluye a través del proceso. Después que una empresa crea el
pedido de cliente, prepara una expedición o despacho y lo envía al cliente. La próxima
etapa es la facturación al cliente por los materiales despachados. Finalmente, la
empresa recibe un pago del cliente. Como se puede ver en la ​Figura 19​, cada etapa
involucra varias tareas. Además, dependiendo de las circunstancias, pueden ser
necesarias etapas adicionales, incluyendo actividades que otros procesos en la
organización deben completar. Note que, en este ejemplo, no se ha incluido
explícitamente la gestión de créditos. Se asumirá que el cliente tiene suficiente crédito
y que el pedido será procesado.
Durante el proceso de gestión de pedidos se crea una variedad de documentos. Como
se mencionó previamente, los documentos se categorizan como documentos de
materiales, documentos de contabilidad financiera (FI), documentos de contabilidad
administrativa (CO) y documentos de transacción. Recuerde que todos los documentos
se pueden imprimir o pueden existir en forma electrónica. Los datos contenidos en
estos documentos se categorizan como datos organizativos, datos maestros y datos de
transacción. Algunos datos los provee el usuario, mientras que otros se recuperan
automáticamente de los datos maestros pertinentes y de los documentos de
transacción existentes.
Este resumen del proceso de gestión de pedidos es muy simplificado. La siguiente
discusión aborda cada etapa del proceso en detalle en términos de sus elementos
claves: desencadenantes, datos, tareas y salidas.
Figura 19: Etapas del proceso de gestión de pedidos

ACTIVIDAD DE​ ​PREVENTA
Las actividades de preventa a menudo se desencadenan por la comunicación de un
cliente tal como una consulta o una petición de oferta (RFQ de Request For Quotation).
La salida es una oferta que se envía al cliente que hace la consulta. Los elementos
claves de esta actividad consulta-oferta se muestran en la ​Figura 20​. ​Una CONSULTA
es una solicitud de información acerca de un potencial pedido que el cliente podría
realizar. En el ejemplo, RMB consulta si GBI puede entregar 40 bicicletas de turismo de
lujo plateadas y 100 camisetas en una fecha específica. Si puede, entonces RMB
solicita información de precio, costos de expedición y descuentos. En respuesta, GBI
crea una oferta y la envía a RMB. Una OFERTA es un acuerdo vinculante para vender al
cliente productos específicos bajo términos de entrega y precio claramente definidos.
Debido a que estos términos pueden cambiar, una oferta típicamente incluirá una
fecha de validez, esto es, una fecha hasta la cual la oferta tiene efecto.
Figura 20: Elementos de la actividad de preventa
Además de enviar ofertas en respuesta a consultas, las actividades de preventa
pueden incluir gestionar los contactos de los clientes y crear contratos marco (que se
explican en el siguiente párrafo). SAP ERP provee algunas capacidades para realizar un
seguimiento de los datos pertenecientes a los clientes establecidos, tales como sus
preferencias e historial de compras. Las empresas pueden analizar estos datos para
crear estrategias de marketing y ventas diseñadas para alentar a los clientes a realizar
pedidos adicionales. Además, el sistema puede realizar un seguimiento a potenciales
clientes. Típicamente, los sistemas ERP manejan actividades básicas de preventas. Las
empresas utilizan sistemas de gestión de las relaciones con el cliente (CRM) para
manejar actividades muy detalladas de preventas, flujo de ventas, prospectos de
ventas y marketing que generan una oferta en el sistema ERP. El paso entre los
procesos de preventa en un sistema CRM y el proceso de oferta hasta el cobro en un
sistema ERP es un punto crítico de integración para la mayoría de las empresas debido
a que fallas, tales como pérdidas de oportunidades de ventas, pueden reducir
significativamente los ingresos por venta.
Así como las ofertas son acuerdos vinculantes hechos por los vendedores, los
CONTRATOS MARCO son acuerdos vinculantes hechos por los clientes para comprar
cantidades o montos específicos de materiales. Un ejemplo es un cliente de GBI quien
suscribe un contrato marco para comprar 1.000 bicicletas de turismo estándar en un
periodo de seis meses por un precio específico. Alternativamente, el acuerdo puede
especificar monto en vez de cantidad. En este caso, el cliente acuerda comprar
bicicletas valoradas en $300.000 en los próximos seis meses. Estos tipos de contratos
marco se llaman CONTRATOS. Otra forma de contrato marco incluye programación de
entregas específicas. Por ejemplo, un cliente de GBI podría acordar comprar 1.200
bicicletas en los próximos seis meses y aceptar la entrega de estas bicicletas en un plan
específico de entregas. En este caso, el acuerdo se denomina PLAN DE ENTREGA.
Datos
Se necesitan muchos tipos de datos organizativos y maestros para procesar una
consulta y crear una oferta. Estos datos se presentan en la ​Figura 21​. Particularmente
importante son los datos concernientes al cliente, los materiales y el precio. La entrada
de usuario consiste en el número de cliente, números de material, cantidades y fechas.
El sistema SAP ERP usa estas entradas para obtener los datos organizativos necesarios,
tales como área de ventas y datos maestros en el sistema. Recuerde que el maestro de
materiales y el maestro de clientes se asocian con elementos organizativos específicos.
SAP ERP también usa el número de cliente para obtener datos necesarios del cliente,
como información de contacto del maestro de clientes. Finalmente, el sistema usa los
números de material para obtener los datos de disponibilidad y precio de las
condiciones de precio disponible o del registro info cliente-material.
El párrafo anterior se refiere a clientes existentes. Si la consulta es de un nuevo cliente,
entonces el sistema no contendrá ni los datos maestros ni un registro info
cliente-material para ese cliente. En esos casos, la empresa debe primero crear los
datos maestros del cliente en el sistema. El registro info no es esencial porque los
datos de precio están disponibles en las condiciones de precio.
Figura 21: Datos en una oferta
La oferta se puede crear con o sin referencia a documentos existentes. Si la oferta se
crea sin referencia, entonces todos los datos necesarios se deben proporcionar cuando
se crea la oferta. Sin embargo, si se usa un documento de referencia, tal como una
consulta, oferta, pedido de cliente o contrato marco creado previamente, entonces los
datos de estos documentos se incluyen automáticamente en la oferta. Estos datos se
actualizan según se necesite antes de que la oferta se complete. La ​Figura 22 ​diagrama
el proceso de incorporar datos existentes en la oferta.
Figura 22: Documentos de referencia para una oferta
Tareas
Las tareas claves en la etapa de preventas son recibir las consultas y crear las ofertas.
Tareas adicionales incluyen realizar seguimiento de los clientes y sus patrones de
compra y crear acuerdos a largo plazo con ellos.
Salidas
La actividad de preventas frecuentemente resulta en la creación de dos documentos
de transacción: la consulta y la oferta. El documento de consulta es simplemente un
registro de la consulta del cliente en el sistema SAP ERP. Aunque crear una consulta no
es esencial, provee ciertos beneficios. Por ejemplo, la empresa puede usar la consulta
como un documento de referencia cuando crea una oferta. Más aún, puede analizar
los datos de la consulta para identificar ventas potenciales perdidas y después diseñar
estrategias para prevenir pérdidas similares en el futuro.
La actividad de preventas puede también generar documentos de contratos y plan de
entregas. No se crean documentos de material porque no hay movimiento de
materiales. No se crean documentos contables (FI o CO) porque las actividades de
preventa no tienen impacto en la posición financiera de la empresa.
La salida final de la actividad de preventas es la comunicación de la oferta al cliente. La
manera en la cual la oferta se comunica se determina por las condiciones de mensaje
asociadas a la oferta. Recuerde de la discusión anterior que las condiciones de
mensajes determinan los siguientes elementos:

   ●      El medio de salida por el cual se envía la oferta (p.e., impresora, fax o EDI)
   ● El receptor, significa la empresa con la función de interlocutor pertinente quien
     recibe la oferta
   ● La fecha en la cual se envía la oferta

En el caso de Rocky Mountain Bikes, GBI recibe una solicitud de oferta por 40 bicicletas
y 100 camisetas. En respuesta, crea una oferta. Elige no usar ningún documento
existente como referencia. Por lo tanto, debe ingresar el número del cliente de RMB
directamente o buscar RMB en la lista de clientes para su área de ventas. Debe
también proveer una fecha de validez para la oferta y después ingresar los números y
cantidades de material para los materiales que RMB ha solicitado. Cuando el cliente y
los materiales se asocian en la oferta, el sistema automáticamente importa los datos
de los registros maestros pertinentes—clientes, materiales, condiciones de precio y
registros de info cliente-material – en la oferta. Cuando GBI completa la oferta y está
lista para enviarla a RMB, las condiciones de mensajes indican que RMB prefiere recibir
ofertas inmediatamente a través de correo electrónico.


PROCESAMIENTO DE PEDIDOS DE CLIENTE
Uno de los objetivos de las actividades de preventas es animar al cliente a realizar un
pedido de materiales o servicios. Estos pedidos típicamente toman la forma de un
pedido de compra (PC) enviado por el cliente a la empresa. EL PC de un cliente
desencadena la etapa de gestión de procesamiento de pedidos de clientes, la cual
resulta en la creación de un pedido de cliente en el sistema SAP ERP. Un PEDIDO DE
CLIENTE es un documento interno que contiene la información necesaria para cumplir
un pedido de cliente en una forma estandarizada. La ​Figura 23 muestra los elementos
claves de la etapa de procesamiento de pedidos de cliente.




Figura 23: Elementos de un pedido de cliente
En el ejemplo, RMB ha recibido una oferta de GBI y varios otros proveedores. Luego de
evaluar, ha decidido realizar el pedido con GBI. En consecuencia, RMB prepara un un
pedido de compra usando su proceso de aprovisionamiento y lo comunica a GBI a
través de correo electrónico, fax u otros medios. Note que si RMB hubiese
seleccionado otro proveedor, entonces la oferta que recibió de GBI habría expirado en
la fecha de validez sin impacto en GBI o RMB. El PC representa un compromiso para
comprar los materiales establecidos bajo los términos y condiciones especificadas.
Cuando GBI recibe el pedido de compra, recupera la oferta que se envió previamente a
RMB y crea un pedido de cliente usando los datos de la oferta. Como parte de este
proceso verifica los datos copiados de la oferta y modifica el pedido de cliente para
que coincida con los datos del pedido de compra.

Datos
Si se compara la ​Figura 21 ​con la ​Figura 24 de abajo, se notará que gran parte de los
datos contenidos en el pedido de cliente se encuentra también en la oferta. Además, el
pedido de cliente incluye datos relacionados con expedición, facturación, funciones de
interlocutor, y, si es relevante, datos de contratos con clientes. Los datos de expedición
y facturación se obtienen del maestro de clientes o del registro info cliente-material.
Las funciones de interlocutor se obtienen del maestro de clientes en base a un
solicitante específico. Recuerde que los contratos son acuerdos hechos por los clientes
para comprar una cantidad específica o monto de materiales durante un cierto periodo
de tiempo. Por lo tanto, los datos acerca de cantidades, precio y fechas de entrega se
obtienen de los contratos. Además, el centro de entrega se obtiene del registro info
cliente-material, el maestro de clientes o el maestro de materiales, en ese orden.




Figura 24: Datos de un pedido de cliente

Tareas
La tarea clave en esta etapa es crear un pedido de cliente. Al igual que una oferta, un
pedido de cliente se puede crear usando uno de varios documentos de referencia. La
ilustración en la Figura 22 se aplica también a un pedido de cliente. Así, un pedido de
cliente se puede crear con referencia a una consulta, una oferta, un acuerdo o a un
pedido de cliente creado previamente. Los datos de múltiples documentos de
referencia se pueden combinar para crear un pedido de cliente. Por el contrario, un
único documento de referencia puede generar varios pedidos de cliente. La Figura 25
muestra esta relación para el caso de las ofertas. En el ejemplo, la oferta recibida de
RMB se usa como documento fuente para crear el pedido de cliente. Esto es, un
pedido de cliente se crea de una oferta.




Figura 25: Relación entre ofertas y pedidos de cliente
Si las capacidades de gestión de créditos del sistema ERP están habilitadas, entonces
se lleva a cabo la comprobación del crédito del cliente. Si el crédito se aprueba,
entonces el proceso de gestión de pedidos continúa. Si no, se requieren etapas
adicionales. Las etapas relacionadas con la gestión de créditos se discuten más
adelante. Si el pedido de cliente se relaciona con un contrato de cliente entonces una
tarea adicional es vincular las compras del cliente con los términos del contrato. Esta
acción permite a la empresa y al cliente monitorear y realizar un seguimiento de las
ventas para asegurar que se cumplan los términos del contrato.
La F​igura 26 representa un pedido de cliente estándar. El lado izquierdo muestra la
estructura de un pedido de cliente y el lado derecho indica algunos de los datos
contenidos en el pedido de cliente que GBI creó para RMB.
La cabecera de un pedido de cliente incluye datos que son válidos para todo el pedido
de cliente. Ejemplos son datos del cliente tales como funciones de interlocutor y
número de PC de cliente, fechas y total del pedido. Cada documento de ventas puede
incluir uno o más posiciones de documento de ventas, los cuales contienen datos
acerca de cada posición incluida en el pedido de cliente. Ejemplos de datos de
posiciones son número de material, denominación y cantidad. Cada posición se puede
asociar con diferentes TIPOS DE POSICIÓN, tales como posición normal, posición de
texto y posición sin cargo, el cual determina cómo la posición se maneja con respecto a
la fijación de precio, facturación y expedición. Por ejemplo, no hay cobro para
posiciones sin cargo. Finalmente, cada posición de documento puede incluir uno o más
REPARTOS, los cuales especifican las fechas y cantidades de entrega.
Figura 26: Estructura de un pedido de cliente

Algunos de los datos en el ejemplo se muestran en el lado derecho de la ​Figura 26​. ​Por
ejemplo, la figura muestra la fecha y el número de PC para el pedido de RMB. Indica
también dos funciones de interlocutor, solicitante y destinatario de mercancías. RMB
es el solicitante y el lugar de la carrera donde los materiales van a ser despachados es
el destinatario de mercancías. El pedido consta de dos posiciones, una para las 40
bicicletas y una para las 100 camisetas. Las bicicletas tienen dos repartos, uno por 30
bicicletas para ser entregadas el 10 de mayo y el otro por 10 bicicletas para ser
entregadas el 10 de junio. Por el contrario, las camisetas tienen un reparto porque
RMB solicitó que GBI entregue las 100 camisetas el 10 de mayo.

Salidas
Un pedido de cliente es el único documento de transacción generado en esta etapa.
No se crean documentos de material o contables. Si un contrato se asocia con el
pedido de cliente, entonces se actualiza para incluir la cantidad o monto de la venta.
Hay tres consecuencias adicionales—verificación de disponibilidad, plan de entregas, y
necesidades de transporte—las cuales se consideran a continuación.

LA ​VERIFICACIÓN DE DISPONIBILIDAD es un procedimiento para determinar si los
materiales solicitados están disponibles o estarán disponibles a tiempo para la fecha
de entrega deseada (por reparto). Si los materiales no están disponibles, la verificación
de disponibilidad determinará la fecha de entrega más próxima posible. La decisión de
llevar a cabo una verificación de disponibilidad, así como la clase y alcance de la
verificación, se basa en la configuración del maestro de materiales. Por ejemplo, el
sistema se puede configurar para calcular la disponibilidad en base a los niveles de
stock actual, así como de las entradas planificadas de material de aprovisionamiento o
producción. Además, el sistema puede crear una reserva de material, el cual reserve
los materiales que se necesitan de modo que no se puedan utilizar para cumplir con
otros requerimientos.

La verificación de disponibilidad también debe tomar en cuenta la cantidad de tiempo
necesaria para ejecutar actividades relevantes tales como puesta a disposición del
material, planificación de transporte, carga y salida de mercancías. La puesta a
disposición del material se refiere a preparar el material para expedición o despacho.
Involucra realizar el picking de los materiales desde el almacén y embalarlos en
recipientes adecuados. La planificación de transporte es el proceso por medio del cual
las empresas determinan cómo transportar mejor los materiales al cliente en base al
peso, volumen, modo de transporte (p.e., camión, tren) y otras variables. Carga
involucra mover los materiales desde el centro al interior del camión. La salida de
mercancías se trata, en gran medida, de registrar el impacto financiero de despachar
las mercancías. Se discutirá la salida de mercancías más adelante en la etapa de
expedición. El tiempo necesario para completar estas etapas se calcula usando
PROGRAMACIÓN REGRESIVA​, en la cual la empresa comienza con la fecha de entrega
requerida y luego trabaja en orden inverso para determinar cuándo se debe ejecutar
cada etapa del proceso. La ​Figura 27 ​muestra el proceso de programación regresiva.
Note que la carga es precedida por el picking/embalaje y la planificación del
transporte, las cuales son a su vez precedidas por la puesta a disposición del material.
Es importante hacer notar que estas etapas pueden superponerse como lo muestra la
figura. En consecuencia, el mayor de estos dos tiempos (tiempo de planificación del
transporte y tiempo de picking/embalaje) se incluye en el cálculo.

Finalmente, crear un pedido de cliente puede generar una ​NECESIDAD DE TRANSPORTE
para el proceso de planificación de materiales. Estos datos se usan en el proceso de
planificación de materiales para planificar la adquisición y producción de materiales.
Figura 27: Programación regresiva

En el ejemplo, después que GBI crea el pedido de cliente para RMB, el sistema
automáticamente ejecuta una verificación de disponibilidad para determinar si los
materiales se pueden despachar según lo solicitado. Además, transfiere los datos de
venta al proceso de planificación de materiales para asegurar que los materiales estén
disponibles según se necesiten de modo que sean enviados a RMB oportunamente.




EXPEDICIÓN
La etapa de expedición se desencadena cuando los pedidos se hacen exigibles para la
entrega. La expedición consta de varias tareas que son necesarias para preparar y
enviar los despachos. Específicamente, se crea un documento de entrega de salida el
cual autoriza la entrega de los pedidos que están listos para enviarse. Entonces, los
materiales necesarios se toman del almacén y se ubican en una zona de puesta a
disposición del material donde se puedan embalar apropiadamente. Si estas tareas se
realizan a través del proceso de gestión de almacenes, entonces se ejecutan etapas
adicionales en ese proceso. Después que el pedido se despacha, una salida de
mercancías se registra en el sistema, la cual ejecuta procesos en contabilidad. Estos
elementos de la etapa de expedición se diagraman en la​ ​Figura 28​.
Figura 28: Elementos en la etapa de expedición

Datos
El documento central en la etapa de expedición es el ​DOCUMENTO DE ENTREGA​, el cual
define qué materiales se deben enviar a qué interlocutor (destinatario de mercancías)
y desde qué centro. El documento de entrega además identifica los almacenes para
estos materiales. Los datos en el documento de entrega se compilan a través de
múltiples fuentes (ver ​Figura 29​). Debido a que la expedición se desencadena cuando
un pedido de cliente se hace exigible para entrega, los pedidos de cliente
–particularmente los repartos— son una buena fuente de datos. Otras fuentes son
similares a las que se han visto en etapas previas. Como se esperaría, los datos
relativos a la expedición son los más relevantes. Por el contrario, los datos para la
fijación de precios normalmente no son relevantes durante esta etapa.




Figura 29: Datos de un documento de entrega
La ​Figura 30 ​muestra la estructura de un documento de entrega (lado izquierdo) y
algunos datos en el documento de entrega del ejemplo de GBI (lado derecho). La
cabecera incluye datos aplicables a todo el documento, tales como destinatario de
mercancías, dirección de expedición, fechas y totales (pesos, número de posiciones).
Datos acerca de cada posición de la expedición o despacho, tales como número de
material, cantidad entregada y peso, aparecen como líneas de posición separadas.
Cada reparto en un pedido de cliente es una partida en el documento de entrega. La
Figura 31​ ​muestra la relación entre repartos y posiciones del documento de entrega.




Figura 30: Estructura de un documento de entrega

La ​Figura 31 muestra un pedido con dos posiciones. La posición 1 en el pedido de
cliente tiene dos repartos y la posición 2 tiene uno. El documento de entrega incluye
un reparto para la posición 1 y un reparto para la posición 2. Note que una entrega
puede incluir repartos de diferentes pedidos. Los requisitos para combinar posiciones
de entregas múltiples se discuten en la siguiente sección.
Figura 31: Relación entre repartos y posiciones de entrega

En el ejemplo, se crea una entrega separada para cada fecha. La entrega para el 10 de
mayo, la cual se recrea en la ​Figura 30​, muestra dos posiciones, una para 30 bicicletas
y otra para 100 camisetas. Note que los materiales se envían el 5 de mayo para que
lleguen a Colorado Springs en la fecha deseada del 10 de mayo. Así, las posiciones de
esta entrega se asocian con repartos de dos posiciones en un pedido de cliente. Este
principio se muestra en la ​Figura 31​. La otra entrega incluirá solo una posición, 10
bicicletas, a ser entregadas el 10 de junio.

Tareas
Como se identificó antes, las tareas específicas realizadas durante la etapa de
expedición son (1) crear un documento de entrega, (2) picking, (3) embalar y (4)
contabilizar la salida de mercancías. Crear un documento de entrega sirve como una
autorización para la entrega. Como la ​Figura 32 muestra, repartos de múltiples
pedidos de cliente con similares características se pueden combinar en un despacho o
entrega. Específicamente, los pedidos de cliente deben tener la misma dirección de
entrega, puesto de expedición y fecha de vencimiento. A la inversa, posiciones en un
pedido se pueden dividir en más de un despacho.




Figura 32: Relación entre pedidos de cliente y entregas

La etapa de picking es opcional y es parte del proceso de gestión de almacenes. Sin
embargo, aunque el picking es parte del proceso de gestión de almacenes, se ejecuta
durante la etapa de expedición cuando se crea un documento de

entrega. El documento de entrega sirve como una solicitud de picking. El documento
de entrega se convierte en una orden de transporte en el proceso de gestión de
almacenes y la orden de transporte se utiliza para completar el movimiento físico de
los materiales a despachar.
Figura 33: Relación entre documentos de entrega y orden de transporte

En una única orden de transporte se pueden incluir posiciones de múltiples
documentos de entrega, como se muestra en el lado izquierdo de la ​Figura 33​. Este
enfoque puede optimizar el trabajo de los responsables del picking en el almacén
agrupando solicitudes de materiales que están ubicadas en la misma área.
Alternativamente, un documento de entrega puede generar múltiples órdenes de
transporte, como se muestra en el lado derecho de la figura. Los datos de los
documentos de entrega se copian a la orden de transporte, como se muestra en la
Figura 34​. La cantidad de entrega del documento de entrega pasa a ser la cantidad de
picking, la cual es la cantidad que se debe tomar del almacén. Cuando el picking se
completa, la cantidad que ha sido objeto de picking se transfiere automáticamente de
nuevo al documento de entrega.
Figura 34: Cantidad de entrega versus cantidad de picking

Después que el picking se ha completado, los materiales se ubican en una zona de
puesta a disposición del material donde ellos se embalan apropiadamente. Los
materiales se embalan usando una variedad de elementos de expedición tales como
cajas, pallets y contenedores. Cada elemento de expedición se puede embalar en otro
elemento de expedición para consolidar el despacho. Normalmente, GBI despacha
cada bicicleta en una caja individual y combina 20 cajas en una caja más grande.
Después embala varias de estas últimas en un pallet. Los pallets son usualmente
demasiado pesados para levantarlos a mano, entonces los trabajadores deben usar
pallet jack o elevadores para cargarlas en el contenedor de envío.

El embalaje se diagrama en la ​Figura 35​, la cual muestra una entrega consistente de
cuatro posiciones o materiales. La posición 1 se embala en una caja, las posiciones 2 y
3 se combinan y embalan en una caja y la posición 4 se debe separar y poner en dos
cajas. Dos cajas se cargan una después de la otra en un pallet y las otras dos cajas en
un segundo pallet. Finalmente, los dos pallets se ubican en un solo contenedor.
Figura 35: Opciones de embalaje

La tarea final en expedición es ​REGISTRAR SALIDAS DE MERCANCÍAS ​en el sistema ERP.
La salida de mercancías indica que el despacho ha dejado la instalación. También
produce varias salidas, las cuales se tratan en la siguiente sección.

Salidas
La etapa de expedición, la cual termina con la salida de mercancías, tiene varias salidas
(ver ​Figura 36​). Estas salidas se dividen en tres grandes categorías: (1) impactos
contables (2) creación de documentos para registrar datos de transacción y (3)
actualización de datos maestros y documentos creados previamente.




Figura 36: Salidas de expedición (salida de mercancías)

La expedición es la primera etapa del proceso de gestión de pedidos que tiene un
impacto financiero. Específicamente, las cuentas de existencias de materiales
despachados se abonan y la cuenta de costo de productos vendidos se carga. Estos
montos se basan en el costo de hacer o comprar los materiales. En el caso de
mercancías, el monto se basa en el precio medio variable del material. En el caso de
productos terminados, el monto se basa en el precio estándar el cual considera los
costos de producción tales como material, mano de obra y gastos generales. Un
documento FI se crea para registrar estos datos. La ​Figura 37 muestra estas salidas
para el ejemplo de GBI después que la salida de mercancías para la primera entrega se
ha contabilizado. Como la figura lo indica, el costo de cada bicicleta es de $1.400 y el
costo de cada camiseta de $15. Por lo tanto, las cuentas de existencias para bicicletas y
camisetas se crean por $42.000 ($1.400 X 30) y $1.500 ($15 X 100) respectivamente, y
la cuenta costo de productos vendidos se carga por la suma de las dos, $43.500. Un
impacto similar se registrará después que la salida de mercancías se contabilice para el
segundo despacho en junio. Note que las otras cuentas listadas en la ​Figura 37 ​son
relevantes en etapas posteriores del proceso. Además, si se lleva a cabo una actividad
relevante de contabilidad administrativa (controlling), tal como análisis de
rentabilidad, se puede crear un documento CO.




Figura 37: Impacto FI de la etapa de expedición

La expedición involucra un movimiento de materiales que reduce la cantidad de estos
materiales en inventario. Por lo tanto, además de la reducción del valor del inventario
en el libro mayor, la cantidad del inventario se reduce también en el maestro de
materiales para el centro suministrador. Un documento de material se crea para
registrar este movimiento.

Documentos relevantes de ventas, tales como ofertas y pedidos de clientes, se
actualizan con los detalles del despacho. Finalmente, el listado de facturas pendientes
se actualiza. El listado de facturas pendientes es una lista de entregas para las cuales la
etapa de facturación se puede ejecutar. Ahora se centra la atención en la etapa de
facturación.
FACTURACIÓN
El propósito de la etapa de facturación es crear una variedad de documentos tales
como facturas para productos o servicios como también notas de débito y crédito. La
etapa de facturación se usa también para cancelar documentos creados previamente.
La facturación se puede basar ya sea en entregas que han sido despachadas a clientes
o en pedidos que todavía no han sido despachados. Esta etapa utiliza datos
organizativos, maestros y de transacción de etapas previas del proceso. Al igual que la
expedición, la facturación tiene varias salidas, algunas de las cuales impactan otros
procesos. La​ ​Figura 38​ ​muestra los elementos de la etapa de facturación.




Figura 38: Elementos de la etapa de facturación

Datos
La facturación, con referencia a documentos de entrega, utiliza datos del documento
de entrega y del pedido de cliente, tales como número y cantidades de material
(​Figura 39​). Los datos maestros, tales como maestro de clientes y condiciones de
precio, son la fuente de los datos de determinación de precio y funciones de
interlocutor (destinatario de factura). Además, la facturación utiliza datos
organizativos relevantes para el proceso de gestión de pedidos, mandante, sociedad y
área de ventas.
Figura 39: Datos de un documento de facturación

Tareas
La tarea clave en la etapa de facturación es generar un documento de facturación,
normalmente una factura por materiales o servicios. Tal como se mencionó
previamente, la factura se puede crear en base ya sea a una entrega o a un pedido de
cliente. La ​Figura 19 ​representa un escenario en el cual el despacho se envía antes de
la facturación. Sin embargo, si la empresa desea que se le facture antes de despachar
los materiales—lo cual es frecuentemente el caso cuando el cliente es nuevo o tiene
un deficiente historial de pago—entonces el proceso se puede modificar de manera
que la facturación se realice antes que el envío. Esta discusión se enfoca en facturación
basada en entregas.

Otros documentos de facturación que a veces se crean son notas de crédito y débito.
Una nota de crédito es un reembolso que la empresa emite si el cliente devuelve los
materiales o si en la factura inicial se le cobró más. La empresa usa una nota de débito
cuando al cliente se le cobró menos en la factura original. Una nota de débito aumenta
el monto adeudado por el cliente.

Como puede ver en la ​Figura 40​, se pueden combinar múltiples entregas para crear un
documento de facturación. Este proceso se puede emplear solo cuando las entregas
comparten las mismas características con respecto al pagador (función de
interlocutor), fecha de facturación y país de destino. A la inversa, una entrega puede
generar múltiples facturas. Este es el caso cuando los términos de pago para las
posiciones en la entrega son diferentes. En estos casos, se debe crear un documento
de facturación diferente para cada término de pago. Note que cuando se combinan

entregas, la función de interlocutor pagador es relevante, no quien realizó el pedido
(solicitante) ni quien recibió el despacho (destinatario de mercancías).




Figura 40: Relación entre entregas y facturación

Volviendo al ejemplo de RMB, GBI tiene dos opciones para facturar: puede enviar una
factura después de que se envía cada despacho, o puede esperar hasta que los dos
despachos se envíen y entonces preparar una sola factura acumulada. GBI ha elegido
enviar facturas separadas para cada despacho.

La ​Figura 41 muestra la estructura de un documento de facturación (lado izquierdo).
La cabecera del documento de facturación consiste en la identificación del interlocutor
tal como el solicitante y pagador, fecha de facturación, moneda del documento,
términos de pago y el total. Cada documento de facturación incluye datos tales como
número de material, cantidad y precio. La figura también muestra algunos de los datos
que se incluyen en el documento de facturación generados por GBI para el despacho
inicial (30 bicicletas y 100 camisetas). Posteriormente, GBI generará otro documento
de facturación para las restantes 10 bicicletas.




Figura 41: Estructura de un documento de facturación
Salidas
Como en la expedición, la facturación tiene varias salidas asociadas a contabilidad,
creación de documentos y actualización de datos maestros y documentos. Estos
impactos se presentan en la​ ​Figura 42​.




Figura 42: Salidas de la etapa de facturación

Cuando la etapa de facturación se completa, se actualizan la cuenta asociada deudores
(conciliación) y la cuenta ingresos por ventas en el libro mayor. La cuenta deudores se
carga por el monto de la factura, el cual es el monto que el cliente adeuda y la cuenta
ingresos por ventas se abona por el mismo monto. Recuerde, sin embargo, que debido
a que la cuenta deudores es una cuenta asociada, el monto de la factura no se puede
contabilizar directamente a la cuenta deudores. En su lugar, el monto se contabiliza a
través de la correspondiente cuenta del libro auxiliar, en este caso, la cuenta del
cliente. Se crea una partida abierta en la cuenta del cliente a través de una anotación
al debe, el cual automáticamente actualiza el total en la cuenta deudores. Además de
contabilizar en el libro mayor, se crea un documento FI para registrar estos datos.
Finalmente, debido a que la etapa de facturación incrementa el monto a cobrar por
parte del cliente, el crédito disponible disminuye por el monto correspondiente.

La ​Figura 43 muestra el impacto financiero de la factura enviada en el ejemplo. La
factura incluye 30 bicicletas y 100 camisetas. Las bicicletas se facturan a $2.800 cada
una y las camisetas a $27 cada una ($30 menos 10% de descuento por volumen), por
un total de $86.700 ($84.000 + $2.700). Este total se carga a la cuenta de RMB, la cual
resulta en una contabilización automática en la cuenta deudores. Finalmente, la
cuenta ingresos por ventas se abona por el monto de $86.700. Vale la pena señalar
que el inventario y el costo de productos vendidos se actualizan durante la etapa de
expedición, mientras que ingresos por venta y cliente/deudores se actualizan en la
facturación. Además, se calcula la ganancia bruta como los ingresos por ventas menos
el costo de productos vendidos. Si el ingreso por ventas es menor que el costo de
productos vendidos, entonces el resultado es una pérdida en lugar de una ganancia. En
el ejemplo, GBI tiene una ganancia bruta de $43.200 ($86.700 - $43.500).
Figura 43: Impacto financiero (FI) de la etapa de facturación

La facturación tiene potenciales consecuencias en la contabilidad administrativa o
controlling. Por ejemplo, el análisis de rentabilidad usa datos de ingresos por ventas de
la etapa de facturación que se registran a través de un documento CO. Finalmente, la
facturación genera actualizaciones para varios documentos de ventas, tales como
pedidos de cliente y entregas, cuenta de crédito del cliente y estadística (estructuras
de información) en el sistema de información de ventas.




PAGO
La etapa final en el proceso de gestión de pedidos es el recibo de pago del cliente. El
pago se imputa a las partidas abiertas pertinentes- esto es, partidas que aún no han
sido pagadas en la cuenta del cliente. Los elementos de la etapa de pago se muestran
en ​Figura 44​.




Figura 44: Elementos de la etapa de pago
Datos
Cuando una empresa recibe el pago del cliente, recupera la cuenta del cliente para
identificar las partidas abiertas. Aplica entonces el pago a estas partidas. Por lo tanto,
la etapa de pago involucra datos del maestro de clientes como también datos
organizativos.




Figura 45: Datos de un documento de pago

Tareas
Las tareas en la etapa de pago son identificar las partidas abiertas e imputar el pago a
estas partidas. Los clientes realizan el pago basados en los términos que ya han sido
acordados previamente. Además, los clientes pueden pagar múltiples facturas de una
sola vez, o, a la inversa, dividir una factura en múltiples pagos.

Salidas
Cuando se registra el pago de un cliente, se actualizan las cuentas pertinentes del libro
mayor, y se crea un documento FI asociado. En el ejemplo, RMB ha enviado un pago
para la primera factura por un monto de $86.700. La ​Figura 46 ​muestra el impacto de
este pago en el libro mayor. La cuenta de banco se carga y la cuenta de RMB se abona
por el monto del pago. Esta operación salda las partidas abiertas en la cuenta del
cliente que se creó durante la etapa de facturación. Debido a que la cuenta del cliente
es una cuenta del libro auxiliar, la correspondiente cuenta asociada, clientes, se abona
también automáticamente. Finalmente, debido a que el pago reduce el monto recibido
del cliente, el límite de crédito del cliente aumenta por el monto correspondiente.
Figura 46: Impacto financiero (FI) en la etapa de pago

En el ejemplo anterior, el cliente paga el monto total adeudado. Muy a menudo, sin
embargo, el monto pagado no es el monto adeudado. Este es el caso, por ejemplo,
cuando el cliente tiene derecho a descuentos en base a los términos de pago. Bajo los
términos 1%10/Neto 30, por ejemplo, el pago se debe realizar no mas tarde de 30 días
desde la recepción de la factura y el cliente tiene derecho a un 1% de descuento si
realiza el pago dentro de 10 días. Si el cliente cumple con las condiciones para el
descuento, el pago recibido será menor que el monto facturado.

En consecuencia, se incluyen contabilizaciones adicionales para reflejar el descuento.
Específicamente, la cuenta de banco se carga por el monto del pago y la cuenta
descuentos sobre ventas se carga por el monto del descuento. La cuenta del cliente y
la cuenta asociada deudores se abonan por el monto de la factura, como se muestra
en la ​Figura 47​. Las únicas diferencias entre la ​Figura 47 ​y la ​Figura 46 son que en la
Figura 47 la cuenta de banco se carga por un monto más pequeño (monto adeudado
menos el descuento) y la diferencia (descuento) se carga a la cuenta descuentos sobre
ventas. La cuenta del cliente y la cuenta deudores se abonan por el monto adeudado.
Figura 47: Pago del cliente con descuento

En casos donde el pago no es igual al monto de la factura y no hay descuentos
aplicables, entonces son posibles dos escenarios. En un escenario, el monto de la
diferencia es tan pequeño que es insignificante. En estos casos, la empresa ya sea
cancela o anula la diferencia usando una cuenta apropiada del libro mayor y la factura
se considera pagada. Una diferencia generalmente se considera pequeña si cae dentro
de los límites de tolerancia especificados en el sistema. Cuando la diferencia cae fuera
de los límites de tolerancia y, por lo tanto, se considera significativa, el pago se maneja
ya sea a través de la técnica de pago parcial o la técnica de partida por el saldo. Bajo la
técnica del pago parcial, el pago se contabiliza en la cuenta del cliente y la partida de la
factura original permanece abierta. Bajo la técnica de partida por el saldo, la partida
original se cierra y una nueva partida por el saldo se contabiliza en la cuenta del cliente
(y en la correspondiente cuenta asociada). La ​Figura 48 ​representa todos estos
escenarios.
Figura 48: Tratamiento de pago del cliente


    ​PROCESO DE GESTIÓN DE CRÉDITOS
En la discusión sobre el proceso de gestión de pedidos, se asumió que el cliente tiene
suficiente crédito. En esta sección, se discute brevemente el proceso de gestión de
créditos, el cual las empresas utilizan para evaluar si a un cliente debe concedérsele
crédito para comprar y recibir productos antes del pago. El proceso de gestión de
créditos se puede configurar para hacer esta evaluación en tres puntos durante el
proceso de gestión de pedidos: (1) cuando el pedido de cliente se crea o cambia, (2)
cuando la entrega se autoriza o se cambia (documento de entrega creado) y (3) cuando
la contabilización de la salida de mercancías se ejecuta durante la expedición. El
proceso puede además ser configurado para considerar una variedad de criterios
cuando se hace esta evaluación, incluyendo el monto de los créditos actuales del
cliente y el número y monto de los pedidos de cliente pendientes, entregas
planificadas y facturas pendientes. Además, también se pueden utilizar datos de
crédito provenientes de terceros, como Dunn & Bradstreet™. El riesgo de crédito total
se calcula como la suma del valor de los pedidos pendientes, entregas planificadas,
facturas pendientes y el valor del pedido de cliente actual. Si el riesgo de crédito
excede el límite, entonces la empresa debe seleccionar una de las tres posibles salidas:
(1) advertir al usuario y permitir que el proceso continúe, (2) mostrar un error y no
permitir que el proceso continúe y (3) bloquear la entrega del pedido. Las tres salidas
son posibles cuando el pedido de cliente o documento de entrega se están creando o
cambiando. Durante la contabilización de la salida de mercancías, sin embargo, la
única opción es bloquear la salida de mercancías para que no sea contabilizada.

La ​Figura 49 ​muestra las etapas adicionales de la gestión de créditos que se inician
cuando se crea el pedido de cliente. Primero, la empresa ejecuta una revisión del
crédito. Si el riesgo de crédito cae por debajo del límite, entonces el proceso de gestión
de pedidos continúa. Si el crédito excede el límite, la figura muestra la salida donde se
bloquea la entrega del pedido. El pedido se guarda, pero permanecerá en el status o
estado de entrega bloqueada hasta que se revise por el gerente de crédito, quien lo
aprobará o rechazará. Si el gerente aprueba el pedido, entonces se elimina el bloqueo
de la entrega y el pedido se libera para procesamiento posterior. Contrariamente, si el
gerente declina extender el crédito, entonces se rechaza el pedido y se informa al
cliente de esta decisión.




Figura 49: Proceso de gestión de créditos
     ​INTEGRACIÓN CON OTROS PROCESOS
El proceso de gestión de pedidos está estrechamente integrado con muchos otros
procesos. Se identificó numerosos puntos de integración en la discusión de las etapas
del proceso y se profundizará sobre ellos más adelante. Más abajo se resume los
puntos de integración claves, los cuales se presentan en la ​Figura 50​.




Figura 50: Integración con otros procesos

Debido a que el proceso de gestión de pedidos involucra ingresos y pagos, existe una
clara relación entre gestión de pedidos y contabilidad financiera. Por ejemplo, algunos
de los datos maestros utilizados en gestión de pedidos, tales como maestro de clientes
y maestro de materiales, los que se modifican por los departamentos de ventas y
contabilidad. Además, las etapas de despacho, facturación y pago tienen un impacto
en el libro mayor. El proceso de gestión de pedidos puede también impactar el proceso
de análisis de rentabilidad en la contabilidad administrativa, la cual utiliza los datos de
ingresos por ventas.

Más aún, durante la gestión del pedido de cliente, cuando la empresa ejecuta una
verificación de disponibilidad usa datos de gestión de stocks, producción y compras,
los cuales originan el despacho de materiales. Los datos de ventas los usa también
planificación de materiales para planificar el aprovisionamiento y producción. Otra
etapa del proceso de gestión de pedidos, movimiento de mercancías, se relaciona con
la gestión de stocks. Adicionalmente, los procesos de gestión de almacenes (tal como
el picking) se pueden iniciar durante el despacho.

La gestión de pedidos se relaciona también con los sistemas de proyecto. que la
empresa global usa proyectos para crear productos complejos para los clientes, tales
como un avión. Los pedidos de los clientes para tales productos se procesan utilizando
el proceso de gestión de pedidos. Sin embargo, en vez de preparar y enviar despachos,
como se describió, las solicitudes del cliente se transfieren al proceso de gestión de
proyectos. A su vez, los sistemas de proyecto influyen las entregas y la facturación.

Finalmente, en la sección de procesos se exploró la relación entre el proceso de
gestión de pedidos de GBI y el proceso de aprovisionamiento de RMB. Estos procesos
se ejecutaron en empresas diferentes utilizando distintos sistemas ERP. Sin embargo,
para que ambos procesos operen eficientemente, las dos empresas se deben integrar
a un nivel de proceso y un nivel técnico en múltiples etapas.

 ​INFORMES
Como se discutió, SAP ERP provee varias opciones de informes incluyendo listas en
línea, pools de trabajo y análisis. Una opción de informe adicional en el proceso de
gestión de pedidos, es el flujo de documentos, el cual identifica todos los documentos
relacionados con un pedido del cliente. Estas opciones se examinan en esta sección.

FLUJO DE DOCUMENTOS
Se han examinado muchos de los documentos asociados con el proceso de gestión de
pedidos, incluyendo consultas, pedidos de cliente, documentos de entrega,
documentos de facturación y documentos de pago. Es importante notar que todos los
documentos relacionados con una consulta o pedido de cliente se relacionan en un
flujo de documentos. Un ​FLUJO DE DOCUMENTOS muestra todos los documentos
asociados con las etapas que han finalizado para una consulta o pedido de un cliente.
El flujo de documentos se actualiza después que se termina cada etapa del proceso. La
Figura 51 ​muestra un flujo de documentos para un proceso terminado que comenzó
con un pedido de cliente (en lugar de una consulta). El flujo de documentos muestra la
historia y el status o estado del pedido de cliente. Por ejemplo, si el documento de
entrega se incluye en el flujo de documentos, pero no la salida de mercancías,
entonces se puede concluir que la entrega está en progreso y el despacho todavía no
ha dejado el puesto de expedición. Esta conclusión asume, por supuesto, que los datos
en el sistema ERP están actualizados y reflejan exactamente la actividad en el sistema
físico. Cualquiera de los documentos subyacentes, tales como el pedido de cliente o
factura, se pueden recuperar y desplegar desde el flujo de documentos, si es necesario
más detalle.
Figura 5-51: Flujo de documentos. Copyright SAP AG 2012
