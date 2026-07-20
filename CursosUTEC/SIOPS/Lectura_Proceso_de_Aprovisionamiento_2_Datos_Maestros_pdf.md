---
curso: SIOPS
titulo: Lectura - Proceso de Aprovisionamiento (2. Datos Maestros)
slides: 14
fuente: Lectura - Proceso de Aprovisionamiento (2. Datos Maestros).pdf
---

   DATOS MAESTROS
En el Capítulo 2 se explicó que los procesos de negocio involucran múltiples tipos de datos
maestros. Los cuatro tipos de datos maestros que son relevantes para el proceso de
aprovisionamiento son maestro de materiales, maestro de proveedores, registros info de
compras y condiciones. Todos estos tipos se integran en diversas combinaciones a través de
todo el proceso de aprovisionamiento.

MAESTRO DE MATERIALES
En el Capítulo 2 se explicó que los datos del maestro de materiales se agrupan en diferentes
vistas que son relevantes para los distintos procesos. También se examinó una vista en
detalle, llamada datos básicos, porque estos datos se aplican a muchos procesos. Recuerde
que los datos básicos incluyen número de material, denominación y peso. Revise el Capítulo
2 para una lista completa de materiales que GBI utiliza. Además de los datos básicos, las
vistas relevantes para comprar son: contabilidad financiera, compras y datos de
centro/almacén.

Datos de Contabilidad Financiera
Los DATOS DE CONTABILIDAD FINANCIERA incluyen la moneda de valoración, la categoría de
valoración y el control de precios. La MONEDA DE VALORACIÓN es la moneda en la que los
materiales se valorarán, tales como dólares estadounidenses o euros.

La CATEGORÍA DE VALORACIÓN identifica las cuentas del libro mayor relacionadas con el material.
Las cuentas del libro mayor se utilizan para mantener el valor de las existencias en stock y
se actualizan en la medida que se compran, venden o usan los materiales en fabricación.
Puede revisar el anexo del Capítulo 3 para familiarizarse con las cuentas de materiales que
utiliza GBI. La categoría de valoración provee un importante punto de integración entre el
aprovisionamiento y la contabilidad financiera porque esta permite al sistema contabilizar
automáticamente en las cuentas de inventario o de existencias adecuadas del libro mayor.
Generalmente, todos los materiales con características similares se asignan a la misma
categoría de valoración. Consecuentemente, todas las transacciones financieras para estos
materiales se contabilizan en la misma cuenta del libro mayor. Por ejemplo, debido a que las
bicicletas todo terreno y bicicletas de turismo son productos terminados, sus transacciones
se podrían contabilizar en la misma cuenta de existencia de productos terminados. En
algunos casos, sin embargo, materiales con similares características se asignan a diferentes
categorías de valoración y, por lo tanto, a diferentes cuentas del libro mayor. En el ejemplo
anterior, las bicicletas se podrían asignar a la cuenta de existencias de bicicletas todo terreno
y a la cuenta de existencias de bicicletas de turismo, respectivamente. La asignación de
materiales con características similares a diferentes categorías de valoración es apropiada
cuando una empresa mantiene cuentas del libro mayor separadas para diferentes
materiales.

Tomado de:

Magal S. y Word J. (2017) Integración de Procesos de Negocio con Sistemas ERP. Epistemy
Press LLC. Adaptación al español de: Magal S. and Word J. (2012) Integrated Business
Processes with ERP Systems. John Wiley & Sons. Hoboken. NJ, USA.
La última y más simple opción es asignar estos materiales con diferentes características a la
misma categoría de valoración y, por lo tanto, a la misma cuenta de existencias. Esta
estrategia es adecuada cuando la empresa no necesita rastrear el valor de materiales
separadamente, tal es el caso, por ejemplo, de materiales o consumibles de oficina.

EL CONTROL DE PRECIOS identifica el método que se utiliza para valorizar los materiales. Las dos
opciones para control de precios son precio medio variable y precio estándar. Ambas
opciones definen el precio por unidad de materiales en stock, tales como cascos. En la opción
de precio medio variable (MAP), el valor total de los materiales se divide por la cantidad en
stock para determinar el precio medio por unidad. Por ejemplo, si una empresa tiene 1.000
cascos en stock y su costo de compra es $34.000, entonces el precio medio es $34
(34.000/1.000). A este precio se le llama “variable” debido a que se actualiza cada vez que
una etapa del proceso afecta el precio; representa un precio promedio de los materiales en
stock. Por lo tanto, si la empresa adquiere 100 cascos adicionales por $ 3.500, entonces el
nuevo precio variable aumenta levemente a $ 34,09 (($ 34.000 + $ 3.500) / (1.000 + 100)).

En cambio, el precio estándar es constante para un periodo específico de tiempo y no fluctúa,
aun cuando ocurra un evento que cause que el valor de los materiales cambie. El precio
estándar se actualiza periódicamente (por ejemplo, mensual o trimestralmente) para
considerar los cambios en el valor de los materiales. Así, en el ejemplo anterior, si la política
de la empresa es actualizar el precio estándar al final de cada mes, esto no hace que el precio
cambie cuando se compran cascos adicionales. En lugar de ello, el precio estándar se
actualiza al final del mes.

GBI usa precio medio variable como método de valoración para los materiales que compra
(mercaderías y materias primas) y precio estándar para los materiales que fabrica
(productos semielaborados y productos terminados).

Datos de compras
Otro componente clave del maestro de materiales son los datos o vista de compras. Los datos
clave en la vista de compras son los grupos de compras, el tiempo para tratamiento de
entradas de mercancías y las tolerancias de entrega. El grupo de compras, el cual se estudió
anteriormente como uno de los elementos organizativos de aprovisionamiento, es
responsable de comprar los materiales.

Cuando una empresa recibe materiales de un proveedor, requiere una cierta cantidad de
tiempo para recibirlos y acopiarlos en el almacén. Por ejemplo, se debe desempaquetar las
cajas, contar los materiales, inspeccionar su calidad y moverlos físicamente al almacén
apropiado. Esto es el TIEMPO PARA TRATAMIENTO DE ENTRADAS DE MERCANCÍAS. Una estimación de
este tiempo se incluye en el maestro de materiales. El sistema ERP utiliza esta estimación en
las actividades de planificación, por ejemplo, para determinar cuándo se debe ingresar un
pedido para que los materiales estén disponibles cuando se necesiten.
No es poco común que el envío de un proveedor incluya más o menos material que la
cantidad real ordenada. Cuando esto ocurre, la organización receptora puede o no aceptar el
envío, dependiendo de sus políticas y acuerdos con sus proveedores. Las TOLERANCIAS DE
ENTREGAS en el maestro de materiales, especifican cuánto sobre y bajo la entrega aceptará el
comprador. Si la cantidad entregada está dentro de estas tolerancias, entonces el comprador
acepta la entrega. Si la cantidad excede las tolerancias, entonces rechaza el envío y lo
devuelve al proveedor.

Algunos de los datos en el maestro de materiales pueden variar en cada nivel organizativo
relevante. En compras, el nivel organizativo relevante es el centro. Si una empresa tiene
múltiples centros, los materiales se deben definir para todos los centros en el que se
almacenan. Por ejemplo, el grupo de compras y el tiempo para tratamiento de entradas de
mercancías pueden variar en cada centro.

Datos del Centro/Almacén
La mayoría de los materiales que se compran a un proveedor o se producen internamente,
finalmente se reciben en existencias. Para que esta etapa ocurra, la vista datos del centro/
almacén se debe incluir en el maestro de materiales. La vista datos del centro/almacén
incluye datos que son necesarios para almacenar los materiales correctamente. Ejemplos de
estos datos son:
• Requisitos ambientales tales como temperatura y humedad
• Contenedores especiales que se requieran para almacenar
• Periodo de validez; es decir, el tiempo que un material se puede almacenar antes de que
    se vuelva obsoleto o inservible (común en las industrias farmacéuticas y de servicios
    alimenticios)
• Instrucciones de manejo especial, por ejemplo, si el material es frágil o peligroso.

MAESTRO DE PROVEEDORES
Los DATOS DEL MAESTRO DE PROVEEDORES incluyen los datos necesarios para hacer negocios con
un proveedor y ejecutar transacciones relacionadas con el proceso de compras. Los datos del
maestro de proveedores se agrupan en tres segmentos: datos generales, datos contables y
datos de compras. Las relaciones entre estos tres segmentos y los dos departamentos
responsables de los datos, contabilidad y compras, se muestran en la Figura 4-6. La Figura
4-7 destaca los datos específicos que se incluyen en cada segmento.
               Figura 4-6: Segmentos de datos del maestro de proveedores




                Figura 4-7: Ejemplos de datos del maestro de proveedores

Los DATOS GENERALES incluyen el nombre del proveedor, dirección e información de
comunicación tales como números de teléfono y fax. Estos datos se definen a nivel del
mandante y son consistentes a través de todas las sociedades y de las organizaciones de
compras de la empresa global (mandante). Los datos generales son comunes en los
departamentos de compras y contabilidad y los puede mantener cualquiera de estos dos
departamentos.

Los DATOS CONTABLES incluyen datos relacionados con los impuestos, datos bancarios y
condiciones y métodos de pago. Estos datos se definen a nivel de sociedad (recuerde del
Capítulo 2 que la contabilidad financiera se mantiene a nivel de sociedad) y son relevantes
para todas las transacciones de compras de la sociedad. El departamento de contabilidad
generalmente completará este segmento del maestro de proveedores.

Los datos contables deben especificar también la cuenta asociada del libro mayor. Recuerde
del Capítulo 3 que una cuenta de proveedor es una cuenta de la contabilidad auxiliar y que
la cuenta asociada identifica la cuenta de acreedores del libro mayor asociada con el
proveedor.

Si el proveedor abastece a múltiples empresas (sociedades) dentro de la empresa global,
muy probablemente los datos variarán para cada empresa. La cuenta asociada será diferente
si cada empresa utiliza un plan de cuentas y cuentas del libro mayor diferentes. Los datos
bancarios y las condiciones de pago también pueden variar. Así, los datos contables se
mantienen separadamente para cada sociedad con la cual el proveedor tenga transacciones.

Finalmente, los DATOS DE COMPRAS incluyen varios aspectos relacionados con la determinación
de precios, creación y comunicación de pedidos de compra, verificación de facturas y otras
etapas involucradas en la ejecución de compras con el proveedor. El departamento de
compras generalmente completará este segmento. Los datos de compras se definen a nivel
de organización de compras y se aplican solo a esa organización. Si una empresa tiene
múltiples organizaciones de compras que tratan con el proveedor, debe mantener separados
los datos para cada una. Por ejemplo, las condiciones de entrega y pago pueden variar para
diferentes organizaciones de compras.

GBI US y GBI DE tienen 12 proveedores que suministran materias primas y mercaderías.
Estos proveedores se muestran en la Tabla 4-1.




Tabla 4-1: Lista de proveedores de GBI

REGISTROS INFO DE COMPRAS
Un REGISTRO INFO DE COMPRAS es una intersección o una combinación de datos de materiales y
proveedores, como se muestra en la Figura 4-8. Contiene datos específicos de un proveedor
y un material o un grupo de materiales. Los registros info de compras incluyen algunos datos
que están en el maestro de proveedores y en el maestro de materiales, así como datos que
son válidos para la combinación específica de proveedor y material. Estos datos se agrupan
en datos generales y datos de organización de compras. Los datos generales se aplican a
todos los grupos de compras e incluyen número de proveedor, número de material o grupo
y otros datos utilizados para comunicación (p.e., información de contacto, números
telefónicos y recordatorios). Por otro lado, los datos de compras son específicos para una
organización de compras, y se basan en acuerdos con el proveedor con respecto a los tiempos
de entrega, las tolerancias de entrega, cantidades y condiciones de precio. Las empresas
utilizan las condiciones de precio para determinar el costo de comprar el material de aquel
proveedor. El registro info normalmente define un número de CLASES DE CONDICIÓN diferente,
incluyendo el precio bruto, reducciones o descuentos y recargos, impuestos y transporte.
También incluye datos de texto que se usan para notas e instrucciones que acompañen el
pedido de compra y hacer seguimiento del último pedido de compra para la combinación
específica material-proveedor. Finalmente, la empresa usa datos del registro info de
compras como valores propuestos cuando crea un pedido de compra para una combinación
específica de material y proveedor.




                           Figura 4-8: Registro info de compras

La Figura 4-9 muestra un registro info de compras para el proveedor 107000 y el material
SHRT1000 para la organización de compras US00. Indica que a Spy Gear le toma cuatro días
enviar la camiseta. Además, Spy Gear tiene un precio de $15 por camiseta, pero ofrece un
descuento del 4% por pedidos mayores a $1.000.

CONDICIONES
El último tipo de datos maestros relevante para compras es CONDICIONES. Estos datos son muy
similares a las condiciones discutidas en la sección de registros info de compras y se usan
para determinar los precios, descuentos, impuestos, transporte, etc. apropiados para los
materiales. A diferencia de las condiciones en los registros info de compras, estas
condiciones no se definen para una combinación específica de proveedor y material. Más
bien, se basan en todos los acuerdos y contratos hechos con los proveedores. La empresa
utiliza estas condiciones para determinar el precio cuando crea pedidos de compra.
                      Figura 4-9: Ejemplo de registro info de compras

   CONCEPTOS CLAVES
Antes de abordar el proceso de aprovisionamiento en detalle, se hará una pausa para discutir
algunos conceptos claves que son esenciales para entender cómo funciona el proceso. Estos
conceptos se relacionan con la forma en que se compran los materiales (tipos de posición),
cómo se registra su impacto financiero (determinación de cuentas), usabilidad de los
materiales (tipo de stock) y el movimiento de los materiales a medida que se reciben,
almacenan y envían a los clientes (movimientos de mercancías).

TIPOS DE POSICIÓN
Los TIPOS DE POSICIÓN determinan qué etapas del proceso y datos se necesitan cuando una
empresa compra materiales o servicios. Los tipos de posición comunes son estándar,
consignación, subcontratación, terceros, traslado y servicios.

De estas categorías, las posiciones STANDARD son los más comunes y el proceso utilizado para
obtenerlas incluye las etapas representadas en la Figura 4-1. La etapa inicial es crear una
solicitud, la cual luego se convierte en un pedido de compra y se envía a un proveedor.
Cuando el proveedor recibe el pedido de compra, envía los materiales que el comprador
recibe a través de la etapa de entrada de mercancías, el comprador también recibe una
factura y la paga al proveedor. En cambio, cuando una empresa compra materiales en
CONSIGNACIÓN, paga al proveedor solo cuando utiliza o vende los materiales. Para esta
categoría de materiales, por lo tanto, no hay una etapa de recepción de factura. El PEDIDO PARA
TERCEROS se refiere a las posiciones que el proveedor envía directamente a un cliente. Las
empresas emplean pedidos para terceros para mercaderías, tales como cascos, que compran
y luego revenden a clientes sin llevar a cabo ellos mismos ninguna operación. Debido a que
el cliente recibe los productos directamente del proveedor, no hay entrada de mercancías
para la propia empresa.
Bajo un acuerdo de SUBCONTRATACIÓN, una empresa envía materiales a un proveedor, quien
los utiliza para crear productos semielaborados. El proveedor luego envía estos productos
de vuelta a la empresa que inició el proceso. En este caso, el proceso de aprovisionamiento
incluye la etapa adicional de envío de materiales al proveedor. Un TRASLADO es el proceso a
través del cual una organización utiliza el proceso de aprovisionamiento para obtener
materiales de otro centro dentro de la misma organización. Debido a que el proceso entero
toma lugar en una sola organización, no hay etapas de facturación ni pago. Finalmente,
SERVICIOS - tales como servicios de limpieza o paisajismo - generalmente no involucran la
recepción de materiales. En su lugar, se necesita un mecanismo - una hoja de servicio - para
registrar los servicios llevados a cabo.

En el ejemplo, GBI utilizará el tipo de posición estándar para comprar las camisetas a Spy
Gear.




DETERMINACIÓN DE CUENTAS
Las empresas generalmente utilizan el proceso de aprovisionamiento para comprar
materiales que dejan en stock hasta que los necesiten. Por ejemplo, las empresas adquieren
materias primas para su uso posterior en el proceso de producción y las mercaderías para
ventas posteriores a clientes. A tales materiales se les denomina MATERIALES DE ALMACÉN.
Recuerde del Capítulo 3 sobre contabilidad financiera, que el libro mayor contiene múltiples
cuentas de existencias, tales como materias primas, mercaderías y productos terminados.
¿Cómo sabe un sistema ERP cuál de estas cuentas de existencias se deben actualizar cuando
se reciben materiales? En el caso de los materiales de almacén, para el cual se debe definir
un maestro de materiales, la DETERMINACIÓN DE CUENTAS - el proceso a través del cual el sistema
determina qué cuentas del libro mayor se usan en una situación dada - es automática y se
basa en los datos contenidos en el maestro de materiales, particularmente la categoría de
valoración.

Las empresas también utilizan el proceso de aprovisionamiento para adquirir MATERIALES DE
CONSUMO. Como el nombre lo sugiere, estos son materiales que se adquieren para ser
consumidos o usados dentro de la organización. Un ejemplo de materiales de consumo son
suministros de oficina, tales como lápices y papel, que las personas utilizan durante el
transcurso de su trabajo diario. Cuando una empresa compra materiales para consumo, la
transacción debe identificar el objeto de imputación al cual asignar la compra, así como las
cuentas del libro mayor que se deben cargar y abonar. Un OBJETO DE IMPUTACIÓN identifica el
portador del costo de la compra y es la entidad para la cual se compraron los materiales. Por
ejemplo, cuando una empresa adquiere suministros de oficina para el departamento de
marketing, se carga una cuenta de gasto (cuenta de gasto o de costo), tal como la cuenta de
gastos de suministros del libro mayor y carga la compra al centro de costo del departamento
de marketing. Recuerde que un centro de costo es un objeto de costo usado para acumular
costos de un departamento. En el ejemplo anterior, el objeto de imputación es el centro de
costo. Las empresas también usan el proceso de compras para adquirir activos como autos y
obtener materiales necesarios para apoyar procesos como producción, gestión de pedidos,
gestión de activos fijos y proyectos como construir una nueva fábrica. Los datos contables
específicos necesarios se determinan mediante el TIPO DE IMPUTACIÓN. Las categorías de
cuenta típicas se describen más abajo junto con los datos contables –específicamente, el
objeto de imputación a ser usado y el número de cuenta del libro mayor- que son necesarios
para cada categoría. Las letras en los paréntesis son los códigos usados en SAP ERP.

       1.   ACTIVO FIJO (A). Una empresa usa esta categoría cuando adquiere un activo fijo,
            como un auto o terreno. Recuerde del Capítulo 3 que el valor de los activos fijos
            se registra en cuentas separadas del libro auxiliar respectivo junto con los
            registros maestros de los activos fijos correspondientes. Cuando los activos se
            compran usando un pedido de compra (ver Capítulo 3 para otras formas de
            adquirir activos), el objeto de imputación a ser incluido en el pedido de compra
            es el registro del maestro de activo fijo.

       2.   ORDEN (F). Las empresas usan esta categoría cuando compran materiales para
            diferentes tipos de pedidos. Un ejemplo de una orden es una orden de fabricación
            que se usará para fabricar otro material. Cuando una empresa compra materiales
            para una orden, debe incluir el número de la orden (objeto de imputación) y un
            número de cuenta del libro mayor en el pedido de compra.

       3.   CENTRO DE COSTO (K). Cuando una empresa compra materiales (p.e., suministros)
            para consumo, el pedido de compra debe incluir el centro de costo al que se
            imputará (objeto de imputación) y el número de cuenta de gasto apropiado del
            libro mayor (p.e., gasto de suministros).

       4.   PEDIDO DE CLIENTE (C). Cuando la compra se asocia con un pedido de cliente
            específico (la cual es parte del proceso de gestión de pedidos), entonces se debe
            proporcionar el número del pedido de cliente y un número de cuenta del libro
            mayor.

       5.   PROYECTO (P). Cuando la compra se relaciona con un proyecto, se debe especificar
            el número de proyecto y un número de cuenta del libro mayor.

Nótese que en varias de estas categorías se necesita una cuenta del libro mayor. El sistema
se puede configurar para determinar automáticamente la cuenta apropiada a través de los
procedimientos de determinación de cuenta. No siempre es necesario para el usuario
proveer estos datos.

La Figura 4-10 muestra la relación entre materiales de almacén y consumo y categorías de
cuenta. Se presentan varios escenarios relacionados con el aprovisionamiento - compra de
material de almacén, compra de material de consumo (con y sin maestro de materiales) y
compra de material de almacén para consumo. El lado izquierdo de la figura muestra que
para material de almacén, la asignación de cuenta es automática y se basa en los datos
(categoría de valoración) del maestro de materiales requerido. Estos datos determinan qué
cuentas (p.e., cuál cuenta de existencias) se usarán durante el proceso de aprovisionamiento.
     Figura 4-10: Compra para almacén versus Consumo y su relación con los tipos de
                                     imputación

El lado derecho de la figura muestra que, para materiales de consumo, se debe proporcionar
tipos y objetos de imputación específicos tales como un centro de costo cuando se crea el
pedido de compra. Los datos ingresados por el usuario determinan qué cuentas del libro
mayor (p.e., cuenta de gasto) se usará durante el proceso. Los materiales de consumo pueden
o no estar en el maestro de materiales. Si los datos en el maestro de materiales existen,
entonces hay dos opciones. En una, la empresa no hace un seguimiento de la cantidad del
material en existencia; en la otra, sí lo hace. Es importante recordar, sin embargo, que la
empresa solo puede hacer seguimiento de la cantidad en existencia. El valor de existencias
no se puede rastrear debido a que durante el proceso de aprovisionamiento se utiliza una
cuenta de gasto (refiérase al Capítulo 3), tal como gastos por suministros, en lugar de una
cuenta de existencias.

Finalmente, en el centro de la figura se muestra el escenario en el cual los materiales que
típicamente se compran para almacenamiento a veces se compran para consumo. Por
ejemplo, GBI normalmente compra cascos para revendérselos a sus clientes; eso es, los
compra para almacenar. Sin embargo, GBI ocasionalmente compra cascos para ser regalados
en ferias comerciales. En estos casos las transacciones se consideran compras para consumo
en vez de ser para almacenar. En consecuencia, un tipo de imputación K (centro de costo) se
proporciona para anular los datos que se incluyen en el maestro de materiales, el cual de otra
forma podría definir los cascos como material de almacén. Debido a que se usa la categoría
K, se requiere una cuenta de gasto específica (p.e., gastos de publicidad) y un centro de costo
asociado con la feria.
En el ejemplo, las camisetas se compran para almacenar. Ya que los datos del maestro de
materiales para las camisetas se definen en el sistema ERP, los datos necesarios para la
asignación de cuenta se obtendrán automáticamente del maestro de materiales.

TIPO O STATUS DE STOCK
El stock o existencia de materiales se clasifica en diferentes TIPOS DE STOCK o status de stock,
los cuales son estados que determinan el uso del material –es decir cómo la empresa puede
usar los materiales en sus distintos procesos. Cuatro tipos de stock comunes son de libre
utilización, en inspección de calidad, bloqueado y en tránsito. Los materiales que se clasifican
como DE LIBRE UTILIZACIÓN, como el nombre implica, se pueden usar de cualquier manera que
la dirección estime beneficiará a la empresa. Se pueden consumir internamente (por
ejemplo, para producir otros productos) o externamente para satisfacer la demanda del
cliente. Por otro lado, los materiales definidos como EN INSPECCIÓN DE CALIDAD o BLOQUEADOS se
pueden retirar solo para muestreo o como desecho. Una empresa utiliza el estado inspección
de calidad cuando los productos que recibe de un proveedor se deben someter a inspección
antes de ser liberados para consumo. El estado bloqueado se utiliza típicamente para
materiales dañados o inutilizados por alguna razón, como cuando el proveedor entrega los
materiales incorrectos. Finalmente, cuando los materiales se están trasladando de un centro
a otro, se clasifican como STOCK EN TRÁNSITO.

MOVIMIENTO DE MERCANCÍAS
Una etapa del proceso que cambia el stock constituye un MOVIMIENTO DE MERCANCÍAS. El
movimiento de mercancías se asocia a recibir materiales de un proveedor, enviarlos a un
cliente o “moverlos” de un lugar a otro dentro de la empresa. Los cuatro movimientos de
mercancías comunes son entrada de mercancías, salida de mercancías, traslado y traspaso.
Los primeros tres movimientos involucran el movimiento físico de materiales de un lugar a
otro. El cuarto, traspaso, se utiliza para cambiar el tipo de stock del material (p.e., de
inspección de calidad a libre utilización) o para reclasificar el material a un tipo de material
diferente.

Una ENTRADA DE MERCANCÍAS registra la entrada de materiales en el almacén, la que provoca un
incremento de la cantidad en existencias. Una empresa normalmente genera una entrada de
mercancías cuando recibe materiales de un proveedor o del proceso de producción. El
documento de material creado como resultado de una entrada de mercancías mostrará la
ubicación (centro y almacén) donde los materiales se reciben, así como el tipo de
movimiento específico utilizado. El documento contable identificará las distintas cuentas del
libro mayor que se actualizan.

A diferencia de una entrada de mercancías, una empresa utiliza una SALIDA DE MERCANCÍAS
cuando los materiales se retiran del almacén en cuyo caso, el stock se reduce. Una empresa
típicamente genera una salida de mercancías cuando (a) envía materiales a un cliente (b) los
utiliza para consumo interno (p.e., para producir otro material) o (c) los asigna para
muestreo o como desecho. El documento de material creado por la salida de mercancías
registrará el lugar desde el cual los materiales fueron enviados así como la cantidad
involucrada. El documento contable indicará las cuentas del libro mayor y los montos
correspondientes. Por ejemplo, cuando GBI envía materiales a un cliente, retira los
materiales del stock y registra una salida de mercancías en su sistema SAP ERP.

Un TRASLADO se usa para mover mercancías de un lugar a otro dentro de la organización. Los
materiales se pueden transferir entre almacenes, entre centros dentro de la misma sociedad
y entre centros de distintas sociedades. En todos los casos, se crea uno o más documentos de
material para registrar el traslado. Además, para traslados entre centros o sociedades, se
crean también documentos contables. Recuerde que anteriormente en el capítulo se definió
el traslado como un tipo de posición. Entonces, ¿por qué es también un movimiento de
mercancías? La razón es que el proceso de aprovisionamiento se puede usar para trasladar
materiales de un lugar a otro. Sin embargo, los materiales también se pueden trasladar fuera
del proceso de aprovisionamiento. En estos casos, el traslado se puede registrar
simplemente vía un movimiento de mercancías. Este enfoque es más rápido y más directo
que usar el proceso de aprovisionamiento, pero tiene limitaciones. Se discute los traslados
en mayor detalle en el capítulo de gestión de stocks y almacenes.

Finalmente, una empresa usa un TRASPASO para cambiar el estado o tipo de un material. Por
ejemplo, se puede usar un traspaso para redefinir un material desde inspección de calidad a
de libre utilización o cambiar un tipo de material de materias primas a productos
terminados. Un traspaso puede o no involucrar el movimiento físico de materiales de un
lugar a otro. En cualquiera de estos casos, se crea un documento de material para registrar
el cambio de estado. Por ejemplo, cuando la empresa recibe materiales de un proveedor, los
almacena y asigna como en inspección de calidad. Luego que ellos pasen la inspección, emite
un traspaso para “moverlos” a un estado de libre utilización. En este caso, se crea un
documento de material, pero no un documento contable. Al igual que con los traslados, se
examinará en mayor detalle los traspasos en el capítulo de gestión de stocks y almacenes.

Un movimiento de mercancías siempre terminará en la creación de un documento de
material. Adicionalmente, se crea un documento de contabilidad financiera si el movimiento
provoca un cambio de valoración. Como se vio en el Capítulo 2 y Capítulo 3, los documentos
de contabilidad financiera registran el impacto de un proceso o etapa de proceso en cuentas
relevantes del libro mayor.

Un DOCUMENTO DE MATERIAL registra datos relacionados con movimiento de mercancías, tal
como la entrada de mercancías de un proveedor. Como se muestra en la Figura 4-11, el
documento de material consta de una cabecera y de una o más posiciones o detalle. La
cabecera incluye datos tales como la fecha, el nombre de la persona que creó el documento
y la fuente del documento, esto es, qué etapa del proceso o transacción se usó para crearlo.
Las posiciones identifican los materiales involucrados, cantidades, ubicación, el tipo de
movimiento utilizado y otros datos relevantes.
                   Figura 4-11: Estructura de un Documento de Material

CLASES DE MOVIMIENTO
Los cuatro movimientos de mercancías que se acaban de discutir se pueden realizar a través
de un número específico de CLASES DE MOVIMIENTO. Cada movimiento de mercancías requiere
una clase de movimiento. La clase de movimiento determina qué categoría de movimiento
se está ejecutando (p.e., entrada de mercancías o salida de mercancías), qué información se
debe proporcionar cuando se ejecuta el movimiento (p.e., almacén) y qué cuentas del libro
mayor se actualizarán (p.e., existencias de productos terminados). También determina cómo
se verá afectada la cantidad de stock (p.e., aumento o disminución). Debido a que distintas
clases de movimiento requieren información diferente, también determinan la disposición
de la pantalla utilizada para registrar el movimiento. Cada clase de movimiento tiene una
correspondiente clase de movimiento de cancelación o anulación que se utiliza para anular
su impacto. Por ejemplo, la clase de movimiento 101 se utiliza para registrar la recepción de
materiales para un pedido de compra y la clase de movimiento 102 se utiliza para anular la
entrada. Las anulaciones se usan típicamente para corregir un error en el registro. Si los
materiales son defectuosos y se deben devolver al proveedor, entonces se usa una clase de
movimiento diferente, 122, para registrar este movimiento. Tabla 4-2 muestra ejemplos de
clases de movimiento en SAP ERP.
Tabla 4-2: Ejemplos de clases de movimiento
