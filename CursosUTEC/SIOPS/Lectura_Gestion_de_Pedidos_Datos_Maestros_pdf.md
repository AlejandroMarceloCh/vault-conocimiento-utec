---
curso: SIOPS
titulo: Lectura - Gestión de Pedidos (Datos Maestros)
slides: 7
fuente: Lectura - Gestión de Pedidos (Datos Maestros).pdf
---

     DATOS MAESTROS
En el Proceso de aprovisionamiento se discutió el maestro de materiales, las
condiciones de precio, y las condiciones de salida desde la perspectiva del
aprovisionamiento. En esta sección se exploran estos datos maestros asociados al
proceso de gestión de pedidos. Además, se discuten los datos maestros que son
relevantes solo al proceso de gestión de pedidos, a saber, maestro de clientes, registro
de información para cliente y material y maestro de gestión de créditos.

MAESTRO DE MATERIALES
Los elementos organizativos claves en el proceso de gestión de pedidos para los cuales
se define el maestro de materiales son el mandante, la organización de ventas, canal
de distribución y centro. Recuerde que los datos del maestro de materiales se agrupan
en vistas y que cada vista es relevante a uno o más procesos y definidos para niveles
organizativos específicos. Las tres vistas relevantes al proceso de gestión de pedidos
son datos básicos, datos de organización de ventas y datos de ventas de centro.
Los datos básicos, los cuales son relevantes para todos los procesos, se definen a nivel
de mandante. Los DATOS DE ORGANIZACIÓN DE VENTAS se definen por
combinaciones de organización de ventas y canales de distribución. Ejemplos de datos
de organización de ventas son centro suministrador, unidades de venta y cantidades
mínimas. El centro suministrador es el centro preferido desde el cual se hacen las
entregas para una organización de ventas y canal de distribución particular (por
ejemplo, cadena de distribución). Las unidades de medida de venta son las unidades
de medida, tales como cartones, barriles, contenedores, estuches, pallets y cajas, en
las cuales se venden los materiales. Cantidades incluyen cantidades mínimas a ordenar
y cantidades de entrega. Además, está disponible un enlace a las condiciones de precio
(discutido más tarde). Debido a que los datos se definen para cada combinación de
organización de ventas y CD, cada CD puede tener diferentes valores para estos datos
para apoyar diferentes estrategias de ventas. Los DATOS DE VENTAS DE CENTROS
proveen detalles de cómo el material se enviará desde el centro suministrador.
Ejemplos son requerimientos de transporte específico (por ejemplo, refrigeración) y
los métodos de carga del material (por ejemplo, carretillas, elevadores o grúas). Note
que es necesario definir materiales para cada combinación de organización de ventas y
canales de distribución, al igual que para cada centro para los cuales los materiales son
relevantes. Muy a menudo, los datos de materiales no se modificarán entre centros y
canales de distribución.

MAESTRO DE CLIENTE
DATOS DEL MAESTRO DE CLIENTE incluyen los datos necesarios para llevar a cabo
negocios con los clientes y ejecutar transacciones que se relacionan específicamente
con el proceso de gestión de pedidos. Los datos del maestro de clientes se dividen en
tres segmentos – datos generales, datos contables y datos de área de ventas. Las
relaciones entre estos tres segmentos y los dos departamentos de una organización
responsable de estos datos (contabilidad y ventas) se representan en la ​Figura 15​.
Figura 15: Segmentos de datos del maestro de clientes
Los DATOS GENERALES se definen a nivel del mandante. Ellos son válidos para todas
las áreas de ventas y sociedades de un mandante. Ejemplos de datos generales son el
nombre, dirección y número de cuenta de un cliente. Los DATOS CONTABLES son
específicos para una sociedad e incluyen datos tales como términos de pago y cuenta
asociada del libro mayor. Recuerde que (1) cuentas de clientes son cuentas de
terceros, (2) cuentas de terceros se enlazan al libro mayor a través de cuentas
asociadas, y (3) la cuenta clientes se usa típicamente como una cuenta asociada para
los clientes. El departamento de contabilidad típicamente completará esta parte de los
datos del maestro de clientes. Los DATOS DEL ÁREA DE VENTAS son específicos a una
área de ventas particular, la cual, como se discutió antes está formada por una
organización de ventas, un canal de distribución y un sector. Los datos del área de
ventas se relacionan con ventas, expedición, factura y funciones de interlocutor.
Ejemplos son la oficina de ventas y la moneda en la cual se lleva a cabo la transacción.
Los datos de expedición especifican el centro suministrador preferido, prioridades y
métodos. Ellos tambien definen las tolerancias de entrega y las políticas para hacer
frente a las entregas parciales. Los datos de factura incluyen condiciones de
facturación y datos relacionados con impuestos.
Si un cliente es atendido por múltiples áreas de ventas, entonces los datos se deben
definir separadamente para cada área de ventas. Este arreglo permite a la empresa
aplicar distintas condiciones a diferentes áreas. La Figura 16 ilustra este enfoque para
un cliente hipotético con oficinas en Estados Unidos y Alemania. El cliente compra
materiales de las empresas de GBI en EE.UU y Alemania. Los datos generales del
cliente aplican en las dos empresas GBI—esto es, la empresa global GBI que es
representada por el mandante. Sin embargo, los datos contables del cliente se deben
definir separadamente para cada empresa GBI. Recuerde que un dato en el registro
maestro de clientes es la cuenta asociada, la cual se halla en el plan de cuentas. Si GBI
EE.UU. y GBI DE usan diferentes planes de cuentas, entonces ellos podrían tener
diferentes números de cuentas asociadas. Además, las monedas y los datos tributarios
(fiscales) son diferentes también. Por lo tanto, los datos contables son diferentes para
cada país (sociedad).
Finalmente, el cliente compra material para sus instalaciones en todo Estados Unidos.
Por consiguiente, trata con las dos organizaciones de ventas de EE.UU. (UE00 y UW00).
Además, los clientes compran exclusivamente como mayoristas. Por lo tanto, los datos
maestros para este cliente deben ser definidos para dos áreas de venta en Estados
Unidos UE00+WH+BI y UW00+WH+BI (ver Figura 16).




Figura 16: Definiciones múltiples para un cliente
En cambio, el cliente en Alemania trata solo con la parte norte del país y compra
exclusivamente a través de Internet. Por lo tanto, solo se define un conjunto de datos
de área de ventas para este cliente en Alemania.
Los clientes pueden jugar diferentes roles o FUNCIONES DE INTERLOCUTOR en el
proceso de gestión de pedidos. Las cuatro funciones de interlocutor son: solicitante,
destinatario de mercancías, destinatario de factura y pagador. Un cliente podría jugar
los cuatro roles o cada rol podría ser jugado por diferentes clientes. El cliente que
envía la orden es el SOLICITANTE. Este es el principal tipo de interlocutor comercial. La
orden podría indicar que los materiales se deben entregar en diferentes ubicaciones o
que la factura se debe enviar a otra persona. Estas son las funciones de DESTINATARIO
DE MERCANCÍAS y DESTINATARIO DE FACTURA, respectivamente. Por ejemplo, el
cliente podría requerir que el material sea enviado a uno de sus clientes. En este caso,
el interlocutor que realmente recibe el despacho se considera destinatario de las
mercancías. Sin embargo, la factura se remitirá al cliente que ordenó los materiales –
esto es, el destinatario de factura. Alternativamente, el destinatario de factura puede
ser otra empresa que procesa facturas para el cliente. Otro ejemplo, una gran empresa
puede estar compuesta por un número de otras empresas, tales como franquicias. Una
orden puede ser puesta por la oficina central, el solicitante, con instrucciones para
entregar los materiales a muchas franquicias, los destinatarios de las mercancías. La
factura se puede enviar a la oficina central, la cual tambien sirve como el destinatario
de factura. Finalmente, el pago se puede externalizar a otra empresa, la cual puede ser
el PAGADOR de la factura.
GBI EE.UU. tiene 12 clientes y GBI DE tiene 7. Estos clientes se listan en la ​Figura 17​.
Detalles adicionales de los datos maestros para cada cliente se proporcionan en el
Anexo 5A​. Rocky Mountain Bikes (RMB), el cliente usado en este ejemplo, se localiza
en Denver, Colorado y por lo tanto, se atiende a través de la organización de ventas de
GBI del Oeste de EE.UU. Además, RMB compra a través del canal mayorista. Por lo
tanto, se asocia con el área de ventas conformada por la organización de ventas del
Oeste de EE.UU. (UW00), el canal de distribución mayorista (WH) y el sector bicicletas
(BI) (observe la ​Figura 6​). Más aún, debido a que RMB es una empresa pequeña, todas
sus funciones de interlocutor se localizan generalmente en la misma dirección. Sin
embargo, no es raro para RMB solicitar que los materiales se envíen directamente a
varios eventos de carreras o a sus clientes minoristas. En el ejemplo, RMB solicita que
los materiales se entreguen en el stand de RMB en la ubicación de la carrera en
Colorado Springs, no en su oficina principal en Denver. En este caso, RMB es un
solicitante, destinatario de factura, y pagador, pero el destinatario de mercancía es la
ubicación de la carrera. Finalmente, debido a que los materiales se deben entregar en
Colorado, ellos se entregarán desde el centro de San Diego.




Figura 17: Clientes de GBI


REGISTRO DE INFORMACIÓN (INFO) CLIENTE-MATERIAL
Un REGISTRO DE INFORMACIÓN CLIENTE-MATERIAL se compone de datos maestros
específicos para un cliente y un material. A diferencia de los datos del maestro de
materiales, los cuales se aplican a todos los clientes y a los datos en un maestro de
clientes, los cuales se aplican a todas las compras realizadas por un cliente en
particular, los datos del registro info cliente-material se relacionan con las compras de
un material específico por un cliente específico.
Algunos datos del registro info cliente-material no se encuentran en ninguna otra
parte. Un ejemplo es el número cliente material, el cual es una referencia cruzada
entre el número de material de la empresa y los números de material del cliente. La
Figura 18 provee algunos ejemplos de números de material usados por GBI y su cliente
RMB. Los números de material de RMB se anotan como el número de material del
cliente en el registro info. Esta referencia cruzada de los números de material habilita
al cliente a realizar un pedido basado en sus números de material internos, los cuales
el registro info luego traduce a los números de material de la empresa. Recuerde que
la mayoría de los clientes también tienen sistemas empresariales que administran sus
procesos de gestión de pedidos. Por consiguiente, el número de material del cliente es
un enlace entre los datos maestros del vendedor y los datos maestros del comprador.




Figura 18: Números de material de RMB y GBI
En ciertos casos los datos en el registro info cliente-material reemplazan los datos
encontrados en otros datos maestros, tales como el maestro de materiales y el
maestro de clientes. Por ejemplo, preferencias relacionadas con el envío, tales como el
centro suministrador, tolerancias, y entregas parciales que se incluyen en el maestro
de clientes aplican a todos los materiales comprados por el cliente. Sin embargo, si
estas preferencias varían para distintos materiales, entonces ellas se incluyen en el
registro info cliente-material. Por ejemplo, si las entregas se envían normalmente a un
centro específico, pero las entregas de un material particular se deben enviar a un
centro distinto, entonces esta preferencia se anota en el registro info cliente-material
para ese material, no en el maestro de clientes.
El registro info cliente-material de RMB también da cuenta que RMB prefiere que las
bicicletas se envíen a través de un transporte especial terrestre (camión) debido al
peso y tamaño de las cajas de envío. En cambio, la empresa require que GBI envíe las
camisetas a través de transporte aéreo estándar (FedEx o UPS 2-días). Finalmente, el
registro info indica que RMB aceptará entregas parciales de camisetas pero no de
bicicletas, debido a que las camisetas tienen un tiempo de aprovisionamiento muy
corto y se pueden volver a solicitar muy rápidamente si es necesario.


CONDICIONES DE PRECIO
Las CONDICIONES DE PRECIO son datos maestros que las empresas utilizan para
determinar los precios de venta de sus productos. Las empresas crean condiciones
para varios componentes del precio de venta final, incluyendo precios brutos,
reducciones, portes, recargos e impuestos. Las condiciones pueden ser cantidades o
porcentajes fijos o basarse en escalas variables y pueden ser independientes o estar
relacionadas con otras condiciones. Por ejemplo, el precio de un producto puede ser
específico a un material e independiente del cliente, lo que significa que el vendedor
cobra el mismo precio a todos sus clientes. Alternativamente, el precio puede ser
específico a un cliente, en cuyo caso la empresa cobra a diferentes clientes diferentes
precios, basado tal vez en algún acuerdo entre la empresa y el cliente. Del mismo
modo, los descuentos pueden ser uniformes o se pueden basar en la cantidad o valor
de la compra. Por ejemplo, GBI ofrece un 10% de descuento (reducción) por las
compras entre 100 y 500 unidades y un 20% de descuento por las compras de más de
500 unidades. El transporte generalmente se basa en el peso del envío y puede ser
obviado para compras mayores a una cantidad predeterminada. Así, el precio final
para el cliente es una función de, o está condicionado por numerosas variables.
Debido a que se definen numerosas condiciones para un producto, una empresa debe
tener un procedimiento para determinar qué condiciones se aplican a un pedido de un
cliente particular. Este procedimiento, denominado la técnica de condiciones, consiste
en identificar las clases de condición disponibles (precio bruto, precio específico de un
cliente, reducciones, portes, recargos, etc.) y determinar cual de ellos aplica a las
circunstancias particulares del pedido.
Recuerde que en el ejemplo, RMB desea comprar 40 bicicletas y 100 camisetas. Las
bicicletas no califican para reducciones o descuentos, por lo que GBI cobrará el precio
estándard de $2.800 por bicicleta. Sin embargo, las camisetas califican para un 10% de
descuento, por lo que el precio será de $27 por camiseta, reducido del precio
estándard de $30.


CONDICIONES DE MENSAJES
Una variedad de mensajes o salidas que se generan durante el proceso de gestión de
pedidos, tales como las ofertas, confirmaciones y facturas, se deben comunicar a los
clientes. Los datos requeridos para ejecutar esta tarea se incluyen en las CONDICIONES
DE MENSAJES. La técnica de la condición usada para determinar el precio se utiliza
también para determinar cómo las salidas del proceso se comunican al cliente.
La condiciones de mensajes se definen separadamente para los diferentes tipos de
mensajes (ofertas, facturas, etc.). Los datos en el maestro de condiciones incluyen el
medio de salida (p. ej. impresora, fax, EDI), las funciones de interlocutor (p.e.,
solicitante, destinatario) y el tiempo de transmision (p. ej. inmediatamente o
periódicamente usando un programa).
RMB prefiere recibir confirmaciones de pedido a través de correo electrónico dentro
de 4 horas de aceptación o despacho de un pedido. También prefiere recibir facturas
en papel. GBI debe mantener todas estas condiciones de mensajes en su sistema ERP.
REGISTRO MAESTRO GESTIÓN DE CRÉDITOS
El REGISTO MAESTRO GESTIÓN DE CRÉDITOS es una extensión del registro maestro de
clientes que incluye datos relevantes para gestionar el crédito de ese cliente. Los datos
contenidos en este registro se agrupan en tres segmentos: datos generales, datos del
área de control de créditos y resumen. El segmento de datos generales incluye los
datos que se aplican a nivel de mandante, esto es, a través de múltiples áreas de
control de créditos. Ejemplos de datos generales son dirección, datos de comunicación
y crédito total concedido a un cliente en la empresa global. El segmento de área de
control de créditos incluye datos que se aplican a una sola área de control de créditos.
Ejemplos son el crédito concedido al cliente para empresas, en un área de control de
créditos y la clase de riesgo específico. La clase de riesgo es una clasificación usada
para determinar qué tan arriesgado es extender el crédito al cliente. Las empresas
usan esta clasificación para evaluar la probabilidad de que el cliente pague sus
facturas. Finalmente, el segmento resumen incluye datos claves de otros segmentos
del registro maestro de créditos. Las empresas usan el segmento resumen para
acceder a los datos más importantes que necesitan para tomar decisiones relativas a
extender el crédito de los clientes.
