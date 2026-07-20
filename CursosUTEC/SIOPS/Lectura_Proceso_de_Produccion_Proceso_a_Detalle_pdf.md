---
curso: SIOPS
titulo: Lectura Proceso de Producción - Proceso a Detalle
slides: 27
fuente: Lectura Proceso de Producción - Proceso a Detalle.pdf
---

     PROCESO
En esta sección se tratará el proceso de producción detalladamente (Figura 16). El proceso
comienza con una solicitud de fabricación que normalmente lo desencadena otro proceso,
como gestión de pedidos, que necesita satisfacer un pedido de un cliente (estrategia de
fabricación contra pedido) o planificación de materiales, que ha determinado que la
empresa necesita aumentar los niveles de inventario (estrategia de fabricación contra
stock).

La solicitud entonces se autoriza para producción por el supervisor de producción. La
siguiente etapa es liberar la orden de fabricación de manera que los materiales necesarios
para fabricar las bicicletas se envíen desde el lugar de almacenamiento. Muy a menudo,
la fabricación implica el uso de sistemas externos, como los sistemas de captura de datos
de producción (CDP, o PDC del inglés Plant Data Collection), que usa datos del sistema
ERP para ejecutar la producción en el área de fabricación. En tales casos, los datos acerca
de la orden se transmiten al sistema externo. Después que los productos terminados se
hayan fabricado, la fabricación real se notifica en el sistema, señalando que las etapas
necesarias para fabricar los materiales se han llevado a cabo. Luego, los materiales se
trasladan a almacenamiento, y el sistema informa que ellos están disponibles para su
consumo por otros procesos (p.e., gestión de pedidos). Además, varias actividades se
llevan a cabo periódicamente durante el proceso, incluyendo la asignación de gastos
generales, determinación del trabajo en curso y la liquidación de la orden. Ahora que tiene
una comprensión general de las distintas etapas involucradas en producción, se examinan
estas etapas en términos de desencadenantes, datos, tareas y salidas.
Figura 16: El proceso de producción

El análisis usará el siguiente escenario de fabricación contra stock de GBI. El inventario
de bicicletas todo terreno de hombre (ORMN1000) ha caído bajo su nivel mínimo. En
consecuencia, GBI debe fabricar más de este modelo. Es más, la empresa ha determinado
que la cantidad óptima para un solo ciclo de producción es 25 bicicletas. Suponga que se
dispone, tanto de las materias primas necesarias para fabricar estas bicicletas como de la
capacidad requerida en los distintos puestos de trabajo.


SOLICITUD DE PRODUCCIÓN
La Figura 17 muestra los elementos de la etapa solicitud de producción. Una solicitud de
producción se desencadena por una necesidad de fabricar materiales. Típicamente, el
desencadenante es resultado de una actividad de otro proceso. Considere las dos
estrategias de fabricación presentadas previamente. Si la empresa ha adoptado una
estrategia de fabricación contra pedido, entonces la recepción de un pedido de cliente
(proceso de gestión de pedidos) desencadenará la necesidad de fabricar los materiales. Si
la empresa ha adoptado una estrategia de fabricación contra stock, entonces la fabricación
se desencadena por el proceso de planificación de materiales, que se encarga de asegurar
que cantidades suficientes de materiales estén siempre disponibles. Otros procesos
también pueden ejecutar fabricación. Por ejemplo, gestión de proyectos, que se ocupa de
construir productos complejos tales como un avión, puede ejecutar la fabricación de un
componente. Aunque las solicitudes de producción típicamente se desencadenan desde
otro proceso, también se puede crear manualmente cuando existe una necesidad de
fabricar materiales, independiente de otras necesidades. En el escenario de GBI, la
solicitud de fabricación se creó manualmente en base a una revisión de los niveles de
stock.




Figura 17: Elementos de la etapa solicitud de producción

Independiente del origen del desencadenante, la salida de esta etapa es una ORDEN
PREVISIONAL, la cual es una solicitud formal de fabricación que indica qué materiales se

necesitan, cuántas unidades se necesitan y cuándo se necesitan. Es similar a una solicitud
de pedido (vista en el Proceso de Aprovisionamiento) en que no se convierte en un
compromiso hasta que alguien actúa sobre la solicitud.

Datos
En una orden previsional se incluyen distintos datos organizativos, datos maestros y datos
especificados por el usuario. Los datos claves se presentan en la Figura 18. Quien crea la
solicitud de fabricación especifica qué materiales se necesitan, cuántos y cuándo se
necesitan. En ese momento el sistema ERP automáticamente incluye los datos maestros
relacionados con los materiales y la lista de materiales en la orden previsional. El sistema
usa estos datos, junto con las opciones de configuración especificadas en el sistema, para
calcular datos adicionales, tales como fechas de la orden y disponibilidad de material. Si
la orden previsional fue creada por otro proceso, entonces los datos especificados por el
usuario, explicados anteriormente, son proporcionados por el proceso que creó dicha
orden.
Tareas
La única tarea en esta etapa es crear la orden previsional. Las órdenes previsionales
permanecen en el sistema hasta que una persona autorizada dentro de la empresa, por lo
general el gerente de producción, actúa sobre ellas. El gerente de producción puede
rechazar la orden, modificarla, combinarla con otras órdenes o autorizar la fabricación.
Asuma que él o ella autorizan la fabricación. Se abordará la autorización de fabricación
en la siguiente sección.




Figura 18: Datos de una orden previsional


Salidas
La salida obvia de la etapa solicitud de producción es una orden previsional, que es un
documento de transacción. Debido a que esta etapa no provoca impacto financiero, no se
crean documentos FI o CO. Asimismo, dado que no hay movimiento de materiales, no se
crean documentos de materiales. En el ejemplo, la orden previsional indicará que se
requiere producir 25 bicicletas todo terreno de hombre (ORMN1000) en el centro Dallas
(DL00).
AUTORIZACIÓN DE PRODUCCIÓN
Mientras que una orden previsional es simplemente una solicitud, una ORDEN DE
FABRICACIÓN, que se     crea en la etapa autorización de producción, representa un
compromiso real de fabricar una cantidad específica de materiales en una fecha
determinada. Numerosos recursos, tales como materias primas, puestos de trabajo y
MAFs, se comprometen para fabricar los materiales especificados en la orden de
fabricación. Una orden de fabricación se crea normalmente mediante la conversión de
una orden previsional. Sin embargo, también se puede generar directamente, sin usar una
orden previsional. Este proceso es similar a crear un pedido de compra sin referencia a
una solicitud de pedido o crear un pedido de cliente sin referencia a una cotización. La
Figura 19 muestra los elementos claves de la etapa autorización de producción.

Datos
La Figura 20 muestra los datos claves necesarios para crear una orden de fabricación.
Note que gran parte de esta información también se incluye en la orden previsional. La
entrada de usuario es generalmente necesaria solo si no se utiliza una orden previsional
como referencia o si los datos de la orden previsional, tales como cantidad y fechas, se
deben cambiar.




Figura 19: Elementos de la etapa autorización de producción
Figura 20: Datos de una orden de fabricación

Por lo general, una orden de fabricación incluye referencias a una LMat, una hoja de ruta,
puestos de trabajo y MAFs que se utilizarán en la fabricación. Como se explicó, una LMat
identifica los materiales o componentes que se usarán en la fabricación y una hoja de ruta
identifica las operaciones necesarias para producir el material. Los puestos de trabajo son
espacios donde se desarrollarán las operaciones; definen los requisitos de capacidad para
la orden.




Figura 21: Estructura de una orden de fabricación

La Figura 21 muestra la estructura de una orden de fabricación. Los datos contenidos en
una orden de fabricación son bastante extensos. Las empresas usan estos datos para
planificar, programar y ejecutar la fabricación del material señalado. Específicamente,
una orden de fabricación incluye los siguientes datos.

   •   La cabecera de la orden incluye datos básicos tales como un número de orden
       único, el centro donde se producirá el material, la persona (programador)
       responsable de la programación de la producción y el status o estado de la orden.
       El status es importante porque determina qué actividades del proceso se pueden
       finalizar. Cuando la orden se guarda inicialmente, el status es “CREADA” (CRTD).
       A medida que la orden se ejecuta, se cambia el status de la orden para reflejar su
       status actual. Otros status de la orden de fabricación son PARCIALMENTE
       LIBERADA (PREL), LIBERADA (REL), PARCIALMENTE NOTIFICADA (PCNF),

       NOTIFICADA (CNF), PARCIALMENTE ENTREGADA (PDLV) y ENTREGADA (DLV).


   •   Una orden de fabricación incluye las operaciones específicas necesarias para
       fabricar el material, junto con los datos de los puestos de trabajo designados.
       También identifica las secuencias específicas para las operaciones. Note que una
       orden de fabricación debe incluir al menos una operación.

   •   Las particiones de capacidad se usan para determinar cómo el trabajo a realizar
       se distribuye o “divide” entre las máquinas y/o personas involucradas en la
       fabricación del material.

   •   La orden de fabricación identifica los componentes necesarios para fabricar la
       cantidad especificada de material. Normalmente, los componentes se obtienen de
       la LMat. Sin embargo, se pueden agregar o ajustar manualmente, en la medida
       que sea necesario.

   •   Se identifican los MAFs para realizar una o más operaciones.

   •   Como el nombre sugiere, los desencadenantes inician o ejecutan alguna actividad
       o función. Un ejemplo de un desencadenante es la realización de una operación
       especificada. Cuando esto ocurre, se liberan operaciones posteriores en la hoja de
       ruta para su ejecución o se desencadena alguna etapa en otro proceso.

   •   Una orden de fabricación incluye estimaciones preliminares de varios
       componentes de costo, tales como material y gastos generales. Estos costos están
       asociados a las cuentas correspondientes del libro mayor, tales como las cuentas
         por consumo de material. A medida que se ejecuta la fabricación, los costos reales
         también se incluyen como datos en la orden de fabricación junto con las
         estimaciones preliminares de costo. Estos datos se usan en el costo de productos,
         que es un proceso de la contabilidad administrativa.

   •     Después de finalizar la orden de fabricación, se deben liquidar los costos
         acumulados en ella. Durante la liquidación, los costos incurridos se asignan a
         objetos de costo en base a las reglas de liquidación especificadas. Se abordará la
         liquidación en mayor detalle más adelante en esta lectura.

   •     Una orden de fabricación puede contener referencias a varios documentos. Por
         ejemplo, la LMat puede incluir una posición documento, o un MAF puede
         referirse a un documento. En estos casos, la orden de fabricación incluye
         referencias a los documentos en el sistema de gestión de documentos (DMS). El
         uso de DMS asegura que se utilizan las versiones más recientes de los documentos
         durante la fabricación.

   •     Cuando la orden de fabricación se ha ejecutado y se han creado los materiales, los
         realmente fabricados se registran en la orden vía notificaciones. Se abordarán las
         notificaciones en mayor detalle más adelante en esta lectura.

Tareas
Como se ha comentado previamente, la principal tarea en la etapa autorización de
producción es crear una orden de fabricación. Existen varios escenarios posibles para
realizar esta tarea. Ya se ha visto que una orden de fabricación se puede crear con o sin
referencia a una orden previsional. Además, las órdenes previsionales se pueden convertir
individualmente, colectivamente, o parcialmente. En la conversión individual, una orden
previsional se convierte en una orden de fabricación. En la conversión colectiva, múltiples
órdenes previsionales se procesan a la vez, es decir, colectivamente. El resultado puede
ser una o múltiples órdenes de fabricación. Finalmente, en la conversión parcial, solo una
parte de las cantidades que aparecen en la orden previsional se incluyen en la orden de
fabricación. La conversión parcial a menudo genera múltiples órdenes de fabricación,
cada una refleja una parte de la cantidad del material presente en la orden previsional.

Otra tarea al crear una orden de fabricación es seleccionar los datos maestros apropiados,
tales como la LMat, la hoja de ruta y los MAFs. Recuerde que una hoja de ruta identifica
las operaciones necesarias para producir el material. En algunos casos el sistema ERP
automáticamente selecciona una hoja de ruta apropiada. El sistema entonces transfiere las
operaciones desde la hoja de ruta seleccionada a la orden de fabricación. Una hoja de ruta
también se puede seleccionar manualmente.

En estos casos el sistema despliega las listas de tareas u hojas de ruta disponibles para el
material y la persona que crea la orden de fabricación decide cuál es la más apropiada.
Cabe destacar que es posible crear una orden de fabricación sin especificar una hoja de
ruta. En este caso, el sistema genera automáticamente una operación por defecto, la que
se incorpora a la orden de fabricación.

Recuerde que la LMat identifica los componentes necesarios para producir el material.
Una vez más, el sistema selecciona automáticamente una LMat adecuada y transfiere los
componentes a la orden de fabricación. Si no está disponible una LMat, entonces los
componentes se deben agregar a la orden de fabricación manualmente.

Ahora considere un escenario en el que (1) la orden de fabricación se crea con referencia
a una orden previsional y (2) la orden previsional incluye los datos de la LMat y de la
hoja de ruta. En este caso, el sistema transfiere automáticamente estos datos a la orden de
fabricación. Tenga en cuenta que los datos reales de la LMat y de la hoja de ruta no se
recuperan nuevamente desde el maestro de materiales. Más bien, los datos relativos a los
componentes y las operaciones se copian directamente desde la orden previsional a la
orden de fabricación. Además, una vez que estos datos han sido incorporados en la orden
de fabricación, no se recuperan automáticamente desde el maestro de materiales de nuevo,
incluso cuando la LMat o la hoja de ruta cambien. Para reflejar cambios en los datos de
la LMat y de la hoja de ruta, se debe instruir manualmente al sistema para releer o
recuperar estos datos.

Una tarea final es asignar componentes y MAFs a operaciones específicas. Por ejemplo,
la hoja de ruta de la bicicleta de turismo de lujo, presentada anteriormente en la Figura
13, indica que diferentes componentes se asignan a diferentes operaciones. Por lo general,
el sistema ERP asigna los componentes basándose en los datos de la hoja de ruta. Sin
embargo, también se pueden asignar o reasignar manualmente a operaciones específicas
según sea necesario. Cualquier componente o MAF que no esté asignado a una operación
específica se asigna automáticamente a la primera operación.
Salidas
La creación de una orden de fabricación genera varias salidas, incluyendo
programaciones, verificaciones de disponibilidad, reservas, costeo preliminar y la
creación de las solicitudes de pedido requeridas. La función de programación calcula las
fechas en las que las distintas operaciones se van a realizar y las capacidades que se
requieren en los puestos de trabajo. La función de programación utiliza datos de la orden
de fabricación (p.e., cantidad y fechas) y parámetros del puesto de trabajo discutidos
previamente (p.e., claves de control y claves para valores preferidos) para completar esta
tarea. Si los datos de programación en la orden de fabricación (p.e., fechas) se cambian
posteriormente, el sistema se puede configurar para reprogramar automáticamente la
orden.

Además, el sistema realiza una verificación de disponibilidad para determinar si los
recursos (componentes, MAFs y capacidad) necesarios para ejecutar la orden de
fabricación están disponibles. Si es así, entonces el sistema crea reservas de material y
máquina para apartar los recursos necesarios, de manera que no puedan usarse para otros
propósitos. A diferencia de la programación, las verificaciones de disponibilidad
normalmente no se repiten automáticamente si se cambia la orden de fabricación. Más
bien, se debe instruir manualmente al sistema para realizar esta verificación.

Finalmente, se realizan los precálculos de costo de la orden de fabricación. Los costos
típicos incluyen costos directos, tales como materiales y la fabricación, y costos
indirectos en la forma de costos generales. Los costos de material se basan en los costos
de los componentes asignados a la orden de fabricación; estos costos se mantienen en el
maestro de materiales de cada material. Los costos de fabricación se basan en los datos
del puesto de trabajo, tales como tipos de actividad y fórmulas que identifican qué
actividades (p.e., mano de obra y preparación) se requieren y en qué cantidades.

Si la orden de fabricación requiere de artículos especiales, tales como materiales de
consumo, entonces el sistema genera automáticamente solicitudes de pedido para
adquirirlos. Se aborda la compra de materiales de consumo en el Proceso de
Aprovisionamiento, en la sección sobre tipos de imputación. Recuerde que, para comprar
materiales de consumo se requiere un tipo de imputación en el pedido de compra. En
producción, el tipo de imputación apropiado es la orden de fabricación (F), y el número
de la orden de fabricación se incluye en la solicitud de pedido. La orden de fabricación
actúa como un objeto de costo. Recuerde del Proceso de Contabilidad, que un objeto de
costo es algo que absorbe costos o al que se le pueden asignar costos.

Además, a veces la fabricación incluye operaciones que desarrolla otra empresa. Por
ejemplo, un componente se podría tener que pintar o pulir por una empresa que se
especializa en esas tareas. Para estas operaciones la empresa emite una solicitud de
pedido. La solicitud indicará subcontratación como tipo de posición (ver Proceso de
Aprovisionamiento para una discusión sobre tipos de posición). Nuevamente, la orden de
fabricación se incluye en la solicitud como el objeto de costo.

En el ejemplo, GBI crea una orden de fabricación para las 25 bicicletas solicitadas.
Cuando la orden se guarda, el sistema reserva los materiales necesarios, así como
capacidad en los tres puestos de trabajo ubicados en el centro Dallas, basado en la LMat
y la hoja de ruta para las bicicletas. La orden de fabricación también incluye una
estimación inicial de costos. La Figura 22 presenta las estimaciones de costo de los
materiales necesarios para construir una bicicleta. Por cada bicicleta, se espera que las
materias primas cuesten $350, los ensambles de ruedas (productos semielaborados) $230
y la mano de obra $25. De este modo, el costo estimado de la orden de fabricación es
$15.125. (Por simplicidad, en este ejemplo solo se incluirán costos por material y mano
de obra, no se tomarán en cuenta otros costos directos [p.e., maquinaria y preparación] o
costos generales indirectos.) Cuando se crea la orden de fabricación, estas estimaciones
se copian en ella (Figura 23). Las otras columnas en la ﬁgura (real, objetivo y desviación)
se discutirán en las etapas posteriores del proceso de producción.




Figura 22: Estimaciones de costos de fabricación para bicicleta todo terreno de hombre
Figura 23: Estimaciones de costo en una orden de fabricación


LIBERACIÓN DE ORDEN
El status creada de una orden limita las etapas del proceso que se pueden ejecutar. Por
ejemplo, no se pueden realizar movimientos de productos, ni notificaciones. Se debe
liberar una orden para fabricación antes que se puedan llevar a cabo las etapas que siguen.
El sistema se puede configurar para liberar automáticamente una orden tan pronto como
se cree. Sin embargo, si la empresa necesita tiempo para verificar la orden o prepararse
para la fabricación, entonces la orden se mantiene en el status creada hasta que esté lista
para liberarse. En este caso, la orden se debe liberar manualmente. La Figura 24 grafica
los elementos de la etapa liberación de orden.

Datos
Los datos que se requieren para liberar una orden son el número de la(s) orden(es) y los
parámetros del sistema que determinan qué actividades se desarrollan automáticamente y
cuáles necesitan intervención manual.




Figura 24: Elementos de la etapa liberación de orden
Tareas
Una orden de fabricación se puede liberar a nivel de cabecera o a nivel de operaciones.
Esta decisión también se determina según la configuración del sistema. Cuando la orden
se libera a nivel de cabecera, se liberan asimismo todas las operaciones. Cuando la
liberación ocurre a nivel de operaciones, sin embargo, solo se afectan ciertas operaciones.
Estas operaciones tendrán el status liberada y la orden tendrá un status parcialmente
liberada. Las operaciones restantes se pueden liberar manualmente según sea necesario o
automáticamente, basado en los desencadenantes. En el ejemplo de GBI, la orden se libera
a nivel de cabecera, lo que significa que todas las operaciones pueden continuar.

Recuerde que los datos de la LMat y de la hoja de ruta no se reingresan automáticamente
en la orden de fabricación si se modifican después que esta se ha creado. En su lugar, el
sistema se debe instruir manualmente para reingresar estos datos. Sin embargo, si la LMat
o la hoja de ruta se reingresan en la orden de fabricación después de haber sido liberada,
entonces el status de la orden se revierte a creada y se debe liberar nuevamente.

Las órdenes de fabricación se pueden liberar individual o colectivamente. Varias órdenes
con similares características, tales como material, instalación (centro) y fechas, se pueden
seleccionar y liberar juntas.

Salidas
Cuando una orden de fabricación se libera para fabricación, se pueden ejecutar las etapas
posteriores identificadas en la Figura 16. Además, se pueden imprimir los documentos de
fabricación que se necesitan para ejecutar los pasos en el puesto de trabajo. Ejemplos de
documentos de fabricación son vales de toma de material, que se utilizan para obtener los
materiales necesarios para la fabricación; hojas de salario, usadas para registrar la
cantidad de tiempo requerido para realizar distintas operaciones; y listas de operaciones,
que especifican las operaciones necesarias para producir el material. Imprimir
documentos de fabricación es otra tarea que se pueda automatizar. Además, el sistema
SAP ERP puede comunicarse directamente con sistemas externos de captura de datos de
producción o sistemas CDP que automatizan el intercambio de datos entre los sistemas
SAP ERP y otros sistemas que controlan la actividad física en el área de fabricación y en
los puestos de trabajo.
SALIDA DE MERCANCÍAS
La siguiente etapa en el proceso es SALIDA DE MERCANCÍAS, en la que se envían, desde
almacén, materiales o componentes para la orden de fabricación. La Figura 25 ilustra los
elementos de esta etapa. El desencadenante es la liberación de la orden de fabricación.
Los datos, tareas y salidas de la etapa salida de mercancías son el foco de esta sección.




Figura 25: Elementos de la etapa salida de mercancías


Datos
Los datos necesarios para realizar la etapa de salida de mercancías (Figura 26) son el
número de la orden de fabricación, datos sobre los materiales a sacar, datos organizativos
respecto de los lugares involucrados y entrada de usuario.




Figura 26: Datos de una etapa salida de mercancías
En esencia, el sistema debe saber qué materiales o componentes saldrán, las cantidades
deseadas y las operaciones a las que se van a asignar. Recuerde que cuando se crea una
orden de fabricación, se reservan los materiales requeridos para la fabricación. En este
punto los únicos materiales a los que se les puede dar salida son aquellos (1) incluidos en
las reservas y (2) asignados a operaciones que se han liberado. La orden de fabricación
incluye muchos de los datos relacionados con la salida de mercancías. La entrada de
usuario especifica los materiales y las cantidades reales sacadas. Los materiales,
cantidades y ubicación (centro, almacén) se pueden cambiar según sea necesario durante
esta etapa.

Tareas
La tarea principal en la etapa de salida de mercancías es sacar materiales desde bodega
para la orden de fabricación. A veces es necesaria una etapa adicional, puesta a
disposición del material, si los materiales se deben preparar para su uso.

Muchas empresas no hacen seguimiento explícito de la salida de materiales para cada
orden de fabricación. En su lugar, emplean TOMA RETROACTIVA, una técnica que registra
automáticamente la salida de mercancías cuando se notifica la orden. Por lo tanto, los
materiales que salen no se registran en el momento en que ellos se toman de inventario.
Por consiguiente, existe un retraso entre la salida real de materiales y el registro de la
salida en el sistema ERP. Aun así, muchas empresas prefieren esta técnica porque elimina
una etapa y puede hacer más eficiente el proceso de producción. La toma retroactiva se
puede especificar en el maestro de materiales, la hoja de ruta o los datos del puesto de
trabajo.

Salidas
Existen diversas consecuencias significativas como resultado de una salida de mercancías
para una orden de fabricación.

   •     El maestro de materiales se actualiza para reflejar una reducción en la cantidad y
         en el valor de stock del material de salida.

   •     Las cuentas del libro mayor se actualizan. Específicamente, se actualizan la(s)
         cuenta(s) de consumo de materiales y la(s) cuenta(s) de existencias
         correspondientes para reflejar un aumento del consumo y una reducción del stock.
   •   Las reservas de material se actualizan. Concretamente, se reducen las cantidades
       reservadas en el número de materiales salientes.

   •   Debido a que esta etapa implica un movimiento de productos, se crea un
       documento de material para registrar los datos asociados con el movimiento.

   •   Ya que se ven afectadas cuentas del libro mayor, se crea un documento FI para
       registrar los datos de la contabilidad financiera.

   •   Se calculan los costos reales asociados con el consumo de material y se agregan a
       la orden de fabricación. Recuerde que la orden de fabricación es un objeto de costo
       y sirve como un receptor de los costos incurridos durante la fabricación. Durante
       la etapa de salida de mercancías, los costos del material se cargan en la orden de
       fabricación.   Se    crea   un    documento     de   contabilidad   administrativa
       correspondiente.

   •   Se puede crear un documento de salida de mercancías que registre los materiales
       y cantidades salientes, aunque no es obligatorio. Este documento se agrega a otros
       documentos de trabajo ya impresos y sirve como registro de los productos que
       salieron. Tome en cuenta que un documento de salida de mercancías no es lo
       mismo que un documento de material. El primero se usa cuando se mantienen
       registros en papel del proceso.

En el ejemplo, la cantidad de cada uno de los materiales componentes en el maestro de
materiales se reduce de acuerdo a la cantidad que se mueve. También se realiza una
reducción correspondiente en el valor. La cuenta consumo de materias primas (720000)
se carga por el valor total de las materias primas que salen, y se abona la cuenta de
existencias de materias primas (200000). Se realizan contabilizaciones similares en la
cuenta de gasto de productos semielaborados y en la cuenta de existencias de productos
semielaborados por los ensambles de rueda sacadas para la orden de fabricación. El costo
real de las materias primas necesarias para producir una bicicleta es de US$369,50 y cada
ensamble de rueda cuesta US$115,00. Para 25 bicicletas, el costo de las materias primas
es US$9.237,50 y el de los ensambles de rueda US$5.750. (Una bicicleta requiere 2
ensambles de rueda). Por lo tanto, el costo total de materiales de la orden de fabricación
es de US$14.987,50 (ver Figura 27). Estos costos de material también se cargan en la
orden de fabricación como costos reales.
Figura 27: Impacto financiero de una salida de mercancías


NOTIFICACIONES
Una vez que los materiales se sacan para la orden de fabricación, se lleva a cabo la
fabricación real en los puestos de trabajo ubicados en el área de fabricación. Cuando se
han fabricado los productos terminados, la persona que finaliza el trabajo registra una
notificación del trabajo terminado en el sistema SAP ERP. Una NOTIFICACIÓN indica
cuánto trabajo se terminó, dónde se terminó (puesto de trabajo) y quién lo terminó. La
Figura 28 muestra los elementos de la etapa de notificación.
Figura 28: Elementos de la etapa de notificación


Datos
Los datos incluidos en una notificación se destacan en la Figura 29 y explican a
continuación.




Figura 29: Datos de una notificación

   •    Cantidades: Cuántos artículos se fabricaron, cuántos se descartaron y cuántos
        requirieron reelaboración.

   •    Operaciones terminadas: Qué operaciones se terminaron, tales como las
        relacionadas con preparación y máquinas.

   •    Duraciones: Las fechas y horas en que se iniciaron y finalizaron las operaciones
        o la duración de las actividades.

   •    Puesto de trabajo: La ubicación física en que se llevaron a cabo las operaciones.
   •     Datos del personal: Quién terminó las operaciones.

   •     Motivo de la desviación: Un motivo por el cual la cantidad notificada difiere de
         la cantidad planificada, si es el caso.

Tareas
Se pueden registrar notificaciones para toda la orden o para operaciones o sub-
operaciones específicas. Cuando se registra una notificación para toda la orden, entonces
todas las operaciones en la orden se notifican automáticamente. Las notificaciones a nivel
de operaciones se pueden registrar de varias maneras, como se explica a continuación.

   •     Notificaciones de evento temporal registran tiempos de preparación, tratamiento
         y desmontaje. Se pueden registrar notificaciones para tiempo de máquina y tiempo
         de mano de obra.

   •     Notificaciones de hoja de salario registran notificaciones periódicamente. Una
         operación se puede notificar parcial o completamente. Las notificaciones parciales
         consisten en datos acumulados desde la notificación anterior. Considere, por
         ejemplo, una orden de fabricación en la que se van a procesar 30 unidades. El
         empleado del puesto de trabajo decide ingresar dos notificaciones. Si la primera
         notificación es por 20 unidades, entonces la segunda reflejará la cantidad
         producida posteriormente, es decir, 10 unidades.

   •     Notificaciones de entrada colectiva y rápida notifican múltiples operaciones al
         mismo tiempo.

   •     En la notificación de hito, la notificación de una operación notifica
         automáticamente las operaciones precedentes. Imagine, por ejemplo, que una de
         las operaciones en una secuencia es una operación de inspección. Aquellas
         unidades que pasan la inspección se notifican, mientras que las unidades restantes
         se envían para ser reelaboradas. En este caso, las operaciones precedentes se
         notifican para la cantidad que pasó la inspección.

   •     Notificación de progreso indica, periódicamente, el progreso total de una
         operación al momento de la notificación. Revisando el ejemplo de 30 unidades de
         un material, al usar notificación de progreso, la notificación inicial indicará 20
         unidades y la segunda indicará 30 unidades.

La discusión anterior supone que las notificaciones se ingresan en el sistema
manualmente. Como se estableció previamente, el proceso de producción puede
involucrar el uso de sistemas externos tales como sistemas CDP. En tales casos, el sistema
CDP proporciona automáticamente los datos de notificación.

Salidas
La salida obvia del paso de notificación es que se registran los datos asociados con el
trabajo realmente terminado. Además, la orden de fabricación se actualiza para reflejar la
cantidad de materiales que se fabricaron, las actividades y operaciones que se terminaron
y las fechas en que se realizó el trabajo. El status de la orden se establece como totalmente
notificada o parcialmente notificada, dependiendo de si se fabricó la cantidad total de la
orden. En los casos de notificación parcial, los empleados del puesto de trabajo pueden
realizar notificaciones adicionales en la medida que fabriquen más material. Debido a que
la notificación indica que ha finalizado la fabricación en uno o más puestos de trabajo,
las reservas de capacidad de estos se reducen. Los puestos de trabajo se pueden usar para
otros propósitos.

Recuerde que un puesto de trabajo está asociado a un centro de costo e incluye varias
actividades, tales como mano de obra y preparación. En la medida que estas actividades
se realizan durante la fabricación y los tiempos se registran en la orden de fabricación
(p.e., horas de mano de obra y horas de preparación), los costos asociados con las
actividades se asignan a la orden de fabricación, la que, como se explicó anteriormente,
sirve como un acumulador de costos. Tome en cuenta que no hay impacto en la
contabilidad financiera en este punto. El impacto FI se produce cuando se paga a los
empleados del área de fabricación (p.e., semanalmente). En ese momento los costos de
mano de obra se asignan a los centros de costo asociados a los puestos de trabajo donde
los empleados finalizaron el trabajo. De este modo, los centros de costo están acumulando
costos de mano de obra (y otros costos directos). Cuando se notifica una orden de
fabricación, los costos se transfieren desde el centro de costo a la orden de fabricación -
los centros de costo se abonan y la orden de fabricación que consume la mano de obra se
carga.

Finalmente, si las claves de control de la última operación permiten registrar una entrada
de mercancías automáticamente, entonces esto sucede cuando se notifica la última
operación. Se discutirá la entrada de mercancías en la sección siguiente.

En el ejemplo, se registra una notificación para las 25 bicicletas. Los costos de mano de
obra se cargan en la orden de fabricación y se abona el centro de costo donde se terminó
el trabajo (puestos de trabajo) (Figura 30). El tiempo real (de mano de obra) requerido
para fabricar las bicicletas fue de 775 minutos. Por lo tanto, la orden de fabricación se
carga por $645,83, que es el costo total de mano de obra a una tasa de pago de $50 (775/60
* 50), fijada previamente. Note que producir cada bicicleta tomó 31 minutos y, por lo
tanto, el costo fue mayor que el planificado. La orden de fabricación ha acumulado un
total de $15.633,33 debido al material y mano de obra consumida.




Figura 30: Impacto financiero de una notificación


ENTRADA DE MERCANCÍAS
Después que la fabricación se ha terminado y notificado, los materiales producidos se
colocan en el inventario de productos terminados. Esta etapa se lleva a cabo mediante una
ENTRADA DE MERCANCÍAS contra la orden de fabricación. La Figura 31 destaca los

elementos de la etapa de entrada de mercancías.
Figura 31: Elementos de una entrada de mercancías


Datos
Los datos asociados a una entrada de mercancías se muestran en la Figura 32. El número
de la orden de fabricación, cantidad que entra, fecha y lugar (centro y almacén) son
proporcionadas por el usuario en base al trabajo notificado. Los datos organizativos
asociados con la ubicación y los datos maestros asociados con el material se obtienen
automáticamente del sistema. El maestro de materiales se usa para determinar la cuenta
de inventario que se necesita actualizar y cómo se valorará (p.e., precio estándar o precio
medio variable). Indica también si el material se puede almacenar en un lugar específico
y si existen requerimientos especiales de almacenaje.




Figura 32: Datos de una entrada de mercancías
Tareas
La tarea fundamental de la entrada de mercancías es recibir físicamente los materiales
desde el área de fabricación y ubicarlos en el almacén apropiado. Si el almacén emplea
un sistema de gestión de stocks (WM, del inglés Warehouse Management), entonces se
crea un requerimiento de traslado para ejecutar las etapas restantes de WM. Se abordarán
los procesos de WM en el Proceso de Gestión de Stocks y Almacenes.

Salidas
La etapa de entrada de mercancías genera varias salidas significativas. Para comenzar la
cantidad disponible y el valor de los stocks se actualizan en el maestro de materiales. El
campo control de precios en el maestro de materiales determina cómo se valorará el
material (es decir, precio estándar o precio medio variable). Las cuentas adecuadas del
libro mayor también se actualizan para reflejar los impactos financieros de la entrada de
mercancías. Por ejemplo, la cuenta de existencias, determinada por los datos del maestro
de materiales, se carga y la cuenta liquidación de fabricación se abona. Si el control de
precios del maestro de materiales se fija en precio estándar y los costos reales de
fabricación difieren de este precio, entonces esta diferencia o desviación se contabiliza
cuando la orden se liquida. (Se abordará la liquidación de órdenes en la sección siguiente.)
Se crea un documento FI correspondiente. La cuenta liquidación de fabricación representa
una cuenta de “costo de productos fabricados”. Otros nombres para esta cuenta son
“cuenta de actividad de centro” y “cuenta de fabricación”. Si control de precios se fija en
precio medio variable, entonces el material se valora a un precio que se determina
mediante el sistema de acuerdo a cómo esté configurado. Los detalles de esta técnica están
más allá del alcance del curso.

Las contabilizaciones relacionadas con el ejemplo se presentan en la Figura 33. Las
contabilizaciones se basan en el costo objetivo de la orden de fabricación. Recuerde que
el costo planificado es el costo en que se espera incurrir cuando la cantidad planificada
se fabrique. Al contrario, el costo objetivo es el costo en que se espera incurrir por la
cantidad real fabricada. Note, sin embargo, que ambos costos, el planificado y el objetivo,
se basan en estimaciones de costo estándar, cuando el control de precios en el maestro de
materiales es costo estándar. En el ejemplo, el costo objetivo es el mismo que el costo
planificado debido a que la cantidad real producida es igual a la cantidad planificada. Sin
embargo, si la cantidad real producida hubiera sido 20 en lugar de 25, el costo objetivo
habría sido menor al costo planificado. En concreto, el costo objetivo del material habría
sido $11.600 y el de mano de obra $500 (revisar Figura 22, que presenta el cálculo del
costo de 25 bicicletas).




Figura 33: Impacto financiero de una entrada de mercancías

En el ejemplo, el costo objetivo es el mismo que el costo planificado y la orden de
fabricación se abona por $15.125. Al mismo tiempo, la cuenta de existencias de productos
terminados se carga por este monto y la cuenta de liquidación de fabricación se abona.
Estos pasos dejan un saldo de $508,33 en la orden de fabricación. Este monto, que es la
diferencia entre los cargos (costo real) y abonos (costo objetivo) en la orden de
fabricación, constituye una desviación. En la siguiente sección se tratarán las
desviaciones.

Después de finalizar la etapa de entrada de mercancías, se actualiza el status de la orden
de fabricación a entregada o parcialmente entregada. Al igual que la salida de mercancías,
la entrada de mercancías se puede automatizar para ahorrar tiempo y mejorar la eficiencia.
En tales casos, el sistema ERP registra automáticamente una entrada de mercancías al
momento de la notificación.
OPERACIONES PERIÓDICAS
Varias etapas relacionadas con la fabricación finalizan periódicamente durante el proceso.
A las operaciones periódicas se les conoce también como cierre de período. Las
empresas definen períodos específicos, tales como meses o trimestres, cuando finalizan
ciertas etapas de la contabilidad para actualizar los datos de los estados financieros. El
cierre de período incluye imputación de gastos generales, determinación del trabajo en
curso y liquidación de la orden.

La orden de fabricación acumula los costos directos asociados con la fabricación. Otros
costos que no están directamente asociados con la fabricación, se les llama costos
indirectos o gastos generales. Ejemplos son los costos asociados con las instalaciones
tales como servicios públicos y mantenimiento, y los salarios de personas tales como
supervisores y gerentes que no están involucrados directamente en la fabricación en los
puestos de trabajo. Estos costos se acumulan en centros de costo determinados y se
imputan periódicamente a las órdenes de fabricación en base a reglas preestablecidas.

Cuando los materiales se sacan para fabricación, se registra una reducción en el inventario
de estos materiales. Sin embargo, los productos terminados no se han completado y
ubicado en inventario sino que esto ocurrirá con posterioridad (al momento de la entada
de mercancías). Durante este período de transición, ni los productos terminados ni los
materiales que los componen aparecen como elementos del inventario en el balance
general. En lugar de ello, se clasifican como inventario de TRABAJO EN CURSO (WIP, del
inglés work in process). WIP no es algo significativo si el proceso de producción es
relativamente corto y el valor de los materiales no es alto, como en el caso de GBI. Sin
embargo, para productos tales como aviones y edificios, la fabricación puede tomar meses
o incluso años y el valor del inventario involucrado en la fabricación es bastante
significativo. En tales casos, los materiales utilizados en la fabricación se consideran
inventario WIP y se debe contabilizar apropiadamente en el libro mayor. Para llevar a
cabo esta tarea, una empresa calcula periódicamente el valor de WIP y realiza las
contabilizaciones en el libro mayor de manera que los estados financieros reflejen de
manera precisa el inventario actual. Una empresa puede usar varias técnicas para
determinar WIP. Sin embargo, una discusión de estas técnicas está más allá del ámbito
de este curso.
Anteriormente, se señaló que la diferencia entre cargos y abonos totales de la orden de
fabricación se llama desviación. Estas desviaciones se liquidan periódicamente o cuando
la orden de fabricación se termina, esto significa que se deben contabilizar en las cuentas
que correspondan del libro mayor. La cuenta de liquidación de fabricación se abona por
el monto de la desviación. Recuerde que esta cuenta se abonó en la etapa de entrada de
mercancías y, por lo tanto, refleja el costo total de fabricación. Se realiza una
contrapartida en una cuenta de desviación, tal como una cuenta de desviación de
liquidación de fabricación o a una cuenta de diferencia de precios. En el ejemplo, la
desviación de $508,33 se liquidó usando las cuentas indicadas en la Figura 34.




Figura 34: Impacto financiero de la liquidación


TERMINACIÓN
La etapa final del proceso de producción, TERMINACIÓN de la orden, se puede ver tanto
desde un punto de vista de la logística (técnicamente cerrada) como contable (cerrada).
Una orden de fabricación se fija a un status TÉCNICAMENTE CERRADA (TECO) cuando ya
no es necesario o posible continuar con la fabricación. En este punto, no es posible la
ejecución de etapas de producción adicionales. Todas las reservas de recursos que aún
están abiertas se eliminan. Todas las consecuencias que afectan a otros procesos, tales
como solicitudes de pedido por materiales requeridos para la fabricación, también se
eliminan. No se espera fabricar los materiales pendientes de la orden y ya no se incluyen
en ninguna planificación. Sin embargo, todavía se pueden hacer contabilizaciones
relacionadas con la orden, como las correspondientes a la liquidación.

Después que una orden de fabricación se termina y liquida, se fija a un status CERRADA
(CLSD). Antes de que pueda llevarse a cabo esta etapa, la orden debe tener el status

liberada o técnicamente cerrada y estar completamente liquidada. Después que la orden
se cierra, no es posible realizar procesamiento o contabilizaciones adicionales.

Periódicamente, las órdenes de fabricación se archivan con el propósito de conservar
registro y se borran del sistema.
