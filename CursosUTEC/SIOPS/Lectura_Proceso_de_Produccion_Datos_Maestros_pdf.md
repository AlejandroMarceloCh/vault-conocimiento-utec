---
curso: SIOPS
titulo: Lectura - Proceso de Produccion (Datos Maestros)
slides: 17
fuente: Lectura - Proceso de Produccion (Datos Maestros).pdf
---

                                                                CAPÍTULO 6
                                               El Proceso de Producción
El proceso de producción consiste en las diversas etapas y actividades involucradas en
la fabricación o ensamblaje de bienes terminados y semielaborados (o en proceso). Las
organizaciones implementan una diversidad de procesos de producción, dependiendo
del tipo de material producido y la estrategia de fabricación usada para producirlo.

Se reproduce un proceso de producción simplificado en la Figura 6-1. El proceso se
inicia por una solicitud de producción. La solicitud se autoriza, lo que permite que el
almacén suministre las materias primas. Producción utiliza estos materiales para
fabricar los productos solicitados, los que luego se llevan a almacenamiento.




Figura 6-1: Proceso de producción básico

En este capítulo, se analiza el proceso de producción en detalle. GBI utiliza un proceso
de fabricación contra stock. Además, emplea un proceso de producción discreto para
fabricar los diferentes tipos de bicicletas en cantidades específicas o lotes.

Se inicia el análisis identificando los datos maestros relacionados con el proceso de
producción. A continuación, se describe en detalle las etapas específicas del proceso.
Para concluir, se consideran los informes que se relacionan con producción. Los
principales datos organizativos relevantes para producción son mandante, sociedad,
centro y almacén. Todos estos datos se han abordado en capítulos previos. En
consecuencia, no se analizarán en este capítulo.


Tomado de:
Magal S. y Word J. (2017) Integración de Procesos de Negocio con Sistemas ERP.
Epistemy Press LLC. Adaptación al español de: Magal S. and Word J. (2012) Integrated
Business Processes with ERP Systems. John Wiley & Sons. Hoboken. NJ, USA.


                                           1
   DATOS MAESTROS
Los datos maestros relevantes para producción son listas de materiales, puestos de
trabajo, hojas de ruta de producto, maestro de materiales y herramientas auxiliares de
fabricación. Se verá cada uno de estos en mayor detalle.

LISTA DE MATERIALES
Una LISTA DE MATERIALES (LMAT. O BOM, DE BILL OF MATERIALS) identifica los componentes que
son necesarios para fabricar un material. En la fabricación discreta y repetitiva, LMat es
una lista completa de todos los materiales, materias primas y productos terminados,
que se necesitan para fabricar una cantidad específica del material. En industrias de
proceso, como las de productos químicos, petróleo y gasolina, y bebidas, la LMat, a
menudo, toma el nombre de fórmula o receta e incluye una lista de ingredientes
necesarios para crear una cantidad específica del producto. En este libro se limitará este
análisis a la fabricación discreta.

Una LMat es una descripción de los materiales requeridos para fabricar un producto
terminado o semielaborado (ver Figura 6-2). Las LMats varían desde muy simples a
muy complejas, dependiendo del material. Por ejemplo, una LMat para un bolígrafo
consta de sólo una media docena de materiales o ítems. Por el contrario, la LMat para
un avión Boeing 747 es extremadamente compleja, conteniendo más de 6 millones de
materiales. Además, las LMats pueden tener uno o múltiples niveles. Una LMat de un
nivel contiene solo un nivel en la jerarquía, mientras que una LMat multinivel tiene más
de uno. Una aeronave, por ejemplo, puede tener más de 50 niveles en su LMat.




Figura 6-2: LMats de uno y múltiples niveles




                                            2
Las LMats en SAP ERP se definen de un solo nivel. Sin embargo, SAP ERP puede
construir LMats multinivel mediante la anidación de varias LMats de un solo nivel. La
anidación se refiere a una jerarquía en la que un componente en una lista de materiales
tiene su propia lista de materiales. Esta estructura se ilustra en la Figura 6-2, donde una
LMat multinivel está conformada por tres LMats de un nivel. La LMat de los productos
terminados presenta tres ítems: dos de productos semielaborados y una de materias
primas. A su vez, cada producto semielaborado tiene una LMat compuesta por una o
más materias primas. (Las materias primas no tienen LMat y se adquieren de una fuente
externa).

Cabe destacar que, se define una LMat para un material a nivel de centro. En otras
palabras, diferentes centros pueden usar una LMat diferente para producir el mismo
material. Este es el caso cuando algunos de los materiales que se usan en la fabricación
del material son diferentes. Por ejemplo, un centro puede usar un perno ligeramente
diferente al de otro centro en la fabricación de un producto terminado.

Recuerde del Capítulo 1 que GBI fabrica bicicletas de turismo de lujo y profesionales. La
LMat para las bicicletas de turismo (Figura 6-3) presenta los materiales necesarios para
ensamblar las bicicletas. Las bicicletas de turismo profesionales incluyen un ensamble
de ruedas profesionales hechas de carbono, mientras que las bicicletas de turismo de
lujo incluyen un ensamble de ruedas de lujo hechas de aluminio. Los marcos para las
bicicletas profesionales y de lujo están hechos de fibra de carbono y vienen en tres
colores—rojo, negro y plateado.

GBI también fabrica bicicletas todo terreno para hombres y mujeres usando marcos y
ruedas de aluminio. El marco para las bicicletas de hombre tiene un tamaño diferente
al de las mujeres. La LMat para las bicicletas todo terreno se muestra en la Figura 6-4.

La Figura 6-3 y la Figura 6-4 representan LMats multinivel. En ambas figuras, el
ensamble de ruedas es un producto semielaborado que se fabrica usando varias
materias primas. Todos los demás componentes son materias primas. Si GBI decide
realizar el ensamble de pedales en lugar de comprarlo, entonces la LMat se modificará
para indicar que el ensamble de pedales es un producto semielaborado. Además, las
materias primas necesarias para hacer el ensamble de pedales se incluirán como un
segundo nivel en la LMat.




                                            3
Figura 6-3: Lista de materiales para bicicletas de turismo




                                           4
Figura 6-4: Lista de materiales para bicicletas todo terreno

La Figura 6-5 identifica los datos que aparecen en una lista de materiales para la
bicicleta de turismo de lujo (DXTR1000). La LMat consta de una sección cabecera y una
sección posiciones. La sección cabecera incluye datos que se aplican a la LMat completa,
tales como número de material, descripción, centro, utilización, validez, status, y cantidad
base. El número de material en la cabecera identifica el producto terminado o
semielaborado descrito en la LMat. Esta es válida desde la fecha especificada en la
cabecera. Una fecha de validez es apropiada cuando se planifican los cambios para una
fecha futura, por ejemplo, debido a modificaciones en el diseño del producto. En tales
casos la LMat actual es válida hasta que la nueva LMat entra en vigor. Debido a que una
LMat se puede usar en varios procesos, el campo utilización en la cabecera identifica el
propósito para el que dicha LMat se puede utilizar. Por ejemplo, la LMat en la Figura 6-
5 muestra un código de utilización 1, indicando que esta se usará en fabricación. Otros
propósitos para los cuales se usan las LMats son diseño, comercial, cálculo del costo y
mantenimiento.

Independiente de la utilización específica, una LMat puede tener el status activa o
inactiva. Una LMat activa se puede utilizar en la fabricación de un material; una LMat
inactiva no se puede utilizar. Finalmente, la cantidad base indica la cantidad de
productos que se pueden producir con los materiales especificados en la sección ítems.




                                             5
Por ejemplo, la LMat que se muestra en la Figura 6-5 identifica los materiales necesarios
para fabricar una bicicleta.

La sección posiciones de una LMat identifica todos los materiales requeridos para
fabricar un producto terminado o semielaborado indicado en la cabecera. La Figura 6-
5 incluye algunos de los elementos de la LMat para la bicicleta de turismo de lujo.
Ejemplos de datos para cada posición son: número de material, denominación, cantidad,
y tipo de posición. El número y la denominación del material identifican los materiales
necesarios. La cantidad indica cuántos de estos materiales se requieren. Por ejemplo,
se necesitan 2 ensambles de rueda para una bicicleta. Una LMat puede contener
diferentes tipos de posiciones, los que se distinguen por el tipo de posición. El TIPO DE
POSICIÓN indica el tipo de material e influye en el modo en que se debe usar el material
en la LMat.




Figura 6-5: Estructura de una LMat

Los tipos de posición comunes son: posición de almacén, posición no de almacén,
posición de dimensión bruta, posición de texto, posición de documento, posición de clase,
e intramaterial.

       •   Una POSICIÓN DE ALMACÉN (L) es un material para el que se mantienen
           existencias o inventario; por lo tanto, debe tener un maestro de materiales.

       •   Una POSICIÓN NO DE ALMACÉN (N) es aquella para la que no se mantienen
           existencias; por lo tanto, no se necesita definir datos en el maestro de
           materiales.

       •   Si un material está disponible en diferentes tamaños, tales como láminas de
           metal o piezas de tela, los diferentes tamaños se pueden representar con el


                                           6
           mismo número de serie. En estos casos el tipo de posición que se usa es
           POSICIÓN DE DIMENSIÓN BRUTA (R), y se deben especificar los datos relativos a
           tamaño o dimensión.

       •   Una POSICIÓN DE TEXTO (T) se usa para incluir notas y comentarios en la LMat.
           Las notas pueden explicar cómo usar el material o identificar algunos
           requisitos inusuales de ensamble.

       •   Una POSICIÓN DE DOCUMENTO (D) se usa para incluir documentos tales como
           diseños de ingeniería, instrucciones de ensamble y fotografías.

       •   Las POSICIONES DE CLASE (K) se usan en las listas de materiales configurables
           para reservar espacio para posiciones seleccionables. Las empresas usan
           LMats variantes para crear múltiples versiones o variantes del mismo
           material en lugar de preparar una LMat por separado para cada versión. Una
           posición de clase es un marcador para una posición real que se debe
           especificar cuando la LMat se utilice. Por ejemplo, GBI podría usar una
           posición de clase para identificar los diferentes colores de los marcos usados
           en las bicicletas de turismo. El color específico del marco se debería
           seleccionar durante la fabricación para una LMat de producción o durante
           la venta para una LMat de ventas.

       •   Los INTRAMATERIAL (M) son un conjunto de materiales lógicamente agrupados
           que se podrían considerar, colectivamente, como un único material. El
           material se crea temporalmente durante la fabricación, entre dos etapas de
           tratamiento, y se consume inmediatamente a medida que continúa la
           fabricación. En el caso de GBI, una bicicleta siempre necesitará dos ruedas—
           una delantera y una trasera. Las dos ruedas se podrían considerar
           lógicamente un conjunto, de este modo, GBI podría usar una posición ficticia
           para representar este conjunto. Sin embargo, este tipo de posición solo se
           permite en la fabricación por proceso.

PUESTO DE TRABAJO
Un PUESTO DE TRABAJO es un lugar donde se realiza trabajo de valor agregado necesario
para producir un material. Es donde se llevan a cabo operaciones específicas, tales como
perforación, ensamble y pintado. Un puesto de trabajo puede ser también una máquina
o un grupo de máquinas; una línea entera de producción; un área de trabajo, tal como
un área de ensamble; o una persona o grupo de personas que son responsables de
completar las operaciones en diferentes lugares del centro. Independientemente de su
composición, sin embargo, es un recurso que se puede usar para una variedad de
propósitos y por múltiples procesos. Para los fines de este capítulo, se definirá un
puesto de trabajo como un recurso usado para producir un material.

La Figura 6-6 muestra los datos relacionados con un puesto de trabajo. La sección de
datos básicos incluye nombre y descripción del puesto de trabajo y la persona o personas


                                           7
responsables de mantener sus datos maestros. Identifica también qué listas de tareas
pueden usar el puesto de trabajo. Una LISTA DE TAREAS es, simplemente, una lista de
operaciones que se requieren para llevar a cabo una tarea. Las OPERACIONES son los
trabajos específicos que se deben realizar, tales como perforar, cortar, pintar,
inspeccionar y ensamblar. Diferentes tipos de listas de tareas se asocian con diferentes
procesos.

En producción una lista de tareas toma la forma de una hoja de ruta de producto o una
receta de planificación. Se abordarán las hojas de rutas de producto más adelante en
este capítulo ya que se usan en la fabricación discreta y repetitiva. Las recetas de
planificación se usan en la fabricación de proceso y, por lo tanto, no se tratarán en este
capítulo. Hay muchos otros tipos de listas de tareas. Se discuten algunas de ellas en los
últimos capítulos en el contexto de otros procesos. Otras están más allá del ámbito de
este libro. Finalmente, las claves para los valores prefijados se utilizan para asignar
valores propuestos o planificados a los elementos de tiempo normales—es decir, las
actividades que consumen tiempo—asociadas con el puesto de trabajo. Elementos de
tiempo típicos son el tiempo de preparación, el tiempo de tratamiento (máquina y mano
de obra), y el tiempo de desmontaje. Las claves utilizan fórmulas específicas para
calcular cuánto tiempo se debe asignar a cada uno de estos elementos.




Figura 6-6: Datos de un puesto de trabajo




                                            8
Los datos del puesto de trabajo incluyen también valores propuestos para las
operaciones desarrolladas en él. Ejemplos de valores propuestos son las claves de
control y los datos sobre salarios. Las claves de control especifican cómo se planifica una
operación o una sub-operación, cómo se calcularán los costos y cómo se notificarán las
operaciones una vez terminadas en el puesto de trabajo. Por ejemplo, una clave de
control puede indicar que se requiere la notificación de una operación y que se debe
imprimir antes de poder desarrollar la siguiente operación. Los datos sobre salarios se
asocian con procesos de gestión de capital humano, tales como la nómina.

La capacidad disponible define la cantidad de trabajo que se puede desarrollar en el
puesto de trabajo durante un tiempo especificado. Un puesto de trabajo puede incluir
más de un recurso o capacidad, por ejemplo, mano de obra y máquina. En este caso, la
base de programación determina la capacidad específica a ser utilizada para la
fabricación.

Un puesto de trabajo está asociado a un centro de costo. Recuerde del Capítulo 3 que un
centro de costo es un contenedor o cubo que acumula costos que luego se asignan o
utilizan adicionalmente por procesos de contabilidad administrativa. Los costos
asociados a operaciones finalizadas en un puesto de trabajo se calculan usando
fórmulas que utilizan los costos y los valores prefijados asociados a cada tipo de
actividad (p.e., mano de obra).

GBI tiene tres puestos de trabajo, como se muestra en la Figura 6-7 y Figura 6-8. La
Figura 6-7 muestra el diseño del centro de fabricación en Dallas. Identifica los tres
puestos de trabajo (ASSY1000, INSP1000, y PACK1000) y los cuatro almacenes (RM00,
FG00, SF00, y MI00). Los tres puestos de trabajo se asocian a un centro de costo, el
centro de costo de fabricación (NAPR1000).

La Figura 6-8 proporciona detalles de los tres puestos de trabajo. ASSY1000 es el puesto
de trabajo de ensamblaje. Cuenta con 8 horas de capacidad de mano de obra. Esta se
usa para realizar tres operaciones, poner a disposición o preparar los materiales,
ensamblar la rueda y ensamblar la bicicleta terminada. INSP1000 es el puesto de
trabajo de inspección. Aquí la bicicleta se ubica en una máquina que prueba su
suspensión y balance. Mientras tanto, el empleado inspecciona visualmente la bicicleta
completa, buscando defectos. A diferencia del puesto de trabajo de ensamblaje, el
puesto de trabajo de inspección utiliza capacidad de mano de obra y de máquina. Una
vez finalizada la prueba, la bicicleta se desmonta en el ensamble del marco y los
ensambles de rueda. Luego, los componentes se embalan por separado en el puesto de
trabajo final (PACK1000), que, al igual que el ensamblaje, involucra solo mano de obra.
El ensamblaje final se lleva a cabo normalmente en las instalaciones del comerciante
minorista o lo hace el cliente después de comprar la bicicleta.




                                            9
Figura 6-7: Centro de fabricación de GBI en Dallas




Figura 6-8: Puestos de trabajo de GBI




                                          10
HOJAS DE RUTA DE PRODUCTOS
En la discusión sobre puestos de trabajo, se definió una HOJA DE RUTA DE PRODUCTO como
una lista de operaciones que una empresa debe ejecutar para fabricar un material
(Figura 6-10). Además, la hoja de ruta de producto especifica la secuencia en la que estas
operaciones se deben llevar a cabo, el puesto de trabajo donde se ejecutarán y el tiempo
necesario para realizarlas. También puede enumerar recursos adicionales, conocidos
como medios auxiliares de fabricación, los que la empresa necesita para realizar las
operaciones.




Figura 6-10: Estructura de una hoja de ruta

El lado izquierdo de la Figura 6-10 ilustra la estructura general de una hoja de ruta. Al
igual que una LMat, una hoja de ruta incluye una cabecera que contiene datos aplicables
a la hoja de ruta completa, tales como status y validez. La hoja de ruta muestra dos
secuencias, cada una de las cuales identifica las operaciones requeridas y el orden en
que se llevan a cabo. Todas las operaciones en una hoja de ruta se deben ejecutar en
algún tipo de secuencia, y muchas operaciones se pueden desarrollar en una variedad
de secuencias. Esta hoja de ruta, por ejemplo, despliega una secuencia estándar, en la



                                           11
que Operación 1 se ejecuta antes que Operación 2, y una secuencia alternativa, en la que
Operación 2 se ejecuta primero.

El lado derecho de la Figura 6-10 muestra la hoja de ruta de la bicicleta de turismo de
lujo de GBI. La hoja de ruta indica que las operaciones necesarias para fabricar esta
bicicleta solo se pueden ejecutar en una secuencia posible (estándar). Por ejemplo,
primero se fija el asiento al marco, luego el manillar.

GBI usa componentes prefabricados tales como el kit de frenos y el ensamble de pedal
que compra a proveedores. Si GBI produjera estos dos componentes, entonces tendría
que ensamblarlos a partir de materia prima antes de fijarlos al marco de la bicicleta. Es
significativo que GBI no tenga que construir uno de estos componentes antes que el
otro. En lugar de ello, se podrían construir simultáneamente o en paralelo. A este
proceso se le conoce como secuencias paralelas. Como sucede con las otras secuencias,
las secuencias paralelas se incluyen en la hoja de ruta.

Dadas todas estas opciones, ¿cuándo y cómo una empresa decide cuál aproximación
usar? La respuesta es que selecciona la secuencia apropiada cuando realmente se lleva
a cabo la fabricación. Basa esta decisión en factores tales como las cantidades deseadas
del producto y el equipamiento y otros recursos que estén disponibles al momento de
la fabricación.

Como se comentó en la sección anterior, las operaciones se llevan a cabo en puestos de
trabajo. Por lo tanto, se debe asignar un puesto de trabajo a una operación. Recuerde
que los puestos de trabajo tienen claves para los valores prefijados y fórmulas a fin de
calcular el tiempo requerido para completar los pasos en cada operación. Hay tres
elementos básicos de tiempo en el proceso de producción: tiempo de preparación,
tiempo de tratamiento y tiempo de desmontaje. El tiempo de preparación supone
configurar el puesto de trabajo y el equipamiento. El tiempo de tratamiento se puede
referir tanto a tiempo de máquina, que implica el uso de una máquina en una operación,
como al tiempo de mano de obra, que es el trabajo humano necesario para desarrollar
la operación. Por último, durante el tiempo de desmontaje, los trabajadores regresan las
máquinas a su estado original, es decir, el anterior a la preparación.

Yendo más lejos, estos elementos de tiempo pueden ser fijos o variables. Los elementos
de tiempo fijo son independientes de cuántas unidades del material se producen,
mientras que los elementos de tiempo variable representan el tiempo necesario para
producir una unidad del material. Por ejemplo, la preparación de material, operación
por medio de la cual los materiales componentes se trasladan desde el almacenamiento
y se preparan para su uso, toma la misma cantidad de tiempo para 10 bicicletas que
para 15. Al contrario, el tiempo necesario para producir el ensamble de ruedas depende
de cuántos ensambles se van a realizar. La Figura 6-11 ilustra la relación entre
Operación 80 (probar bicicleta) e INSP1000, el puesto de trabajo de inspección. Indica
los tiempos de preparación, de tratamiento, máquina y mano de obra, de la operación
(pero no de desmontaje). Recuerde que INSP1000 tiene dos capacidades—máquina y



                                           12
mano de obra (001 y 002 en la figura). Cuando más de una capacidad está disponible
en un puesto de trabajo, la empresa usa la base de programación para determinar qué
capacidad se utilizará para finalizar la orden de fabricación.

La Figura 6-12 muestra la hoja de ruta del ensamble de rueda de turismo de GBI. La
figura identifica las operaciones necesarias, el puesto de trabajo donde se realizará la
operación, los tiempos asociados a la operación y los componentes asignados a cada
operación. El ensamble de rueda tiene tres operaciones: poner a disposición material,
ensamblar componentes en ensambles de rueda y trasladar a almacén (operaciones que
se completan en el puesto de trabajo ASSY1000). Las ruedas se ensamblan en grupos o
lotes de 50. Toma 5 minutos poner a disposición los materiales de 50 ruedas, 3 minutos
ensamblar cada rueda y otros 5 minutos trasladar los 50 ensambles de rueda al
almacén. Debido a que estas operaciones se realizan de forma manual, no implican
ningún tiempo de preparación. En consecuencia, todo el tiempo dedicado a estas
operaciones es tiempo de mano de obra. En general, toma 160 minutos (5 + 50 * 3 + 5)
ensamblar 50 ruedas, un promedio de 3,2 minutos por rueda.




Figura 6-11: Hojas de ruta y puestos de trabajo




                                          13
Figura 6-12: Hoja de ruta del ensamble de rueda de turismo de lujo

La Figura 6-13 presenta la hoja de ruta de la bicicleta de turismo de lujo. A diferencia
del ensamble de rueda, esta hoja de ruta incluye 11 pasos. Además, las operaciones se
completan en tres puestos de trabajo diferentes: ASSY1000, INSP1000 y PACK1000.
Finalmente, la operación #80, Probar bicicleta, incluye un tiempo de preparación de 2
minutos. Esta es la cantidad de tiempo que se necesita para colocar la bicicleta
completamente ensamblada en la máquina de pruebas. Las bicicletas se producen en
lotes de 10 o 15. Para ambas cantidades la operación poner a disposición material y la
operación trasladar a almacén necesitan la misma cantidad de tiempo (10 minutos y 5
minutos, respectivamente). Los otros tiempos en la figura son por bicicleta. Por lo tanto,
toma 305 minutos13 hacer 10 bicicletas, un promedio de 30,5 minutos por bicicleta, y
450 minutos hacer 15 bicicletas, un promedio de 30 minutos. Para efectos de
planificación, GBI usa los siguientes datos:
        • Ensamble de rueda: 3 horas por 50 ensambles de ruedas (3,6 minutos por
            ensamble de rueda).
        • Ensamble de bicicleta: 5 horas por 10 bicicletas (30 minutos por bicicleta).
        • Los días en que se ensamblan ruedas, solo se ensamblan 10 bicicletas; los
            otros días, se ensamblan 15 bicicletas.




                                           14
Figura 6-13: Hoja de ruta de la bicicleta de turismo de lujo

La hoja de ruta indica cómo fabricar un producto específico. La LMat indica qué
materiales se usan para fabricar ese producto. Existe, por lo tanto, una relación obvia
entre una LMat y una hoja de ruta. Esta relación se define a través de la ASIGNACIÓN DE
COMPONENTES, una técnica que asigna componentes de una LMat a una hoja de ruta o a
una operación específica dentro de la hoja de ruta.

La Figura 6-14 presenta una asignación de componentes que incluye tres operaciones
en la hoja de ruta y tres materiales en la LMat. El Material A se asigna a la Operación 20,
mientras que los materiales B y C se asignan a la Operación 30. El lado derecho de la
figura indica que los materiales se consumen al inicio de las operaciones. Todos los
materiales que no se asignan explícitamente a una operación, se asignan
automáticamente a la primera operación y se consumen al inicio de esa operación.




                                            15
Figura 6-14: Asignación de materiales a hoja de ruta

Además de indicar cómo y con qué materiales se fabrican los productos terminados o
semielaborados, los datos contenidos en las listas de materiales, puestos de trabajo y
hojas de ruta se utilizan para determinar la capacidad de producción. La CAPACIDAD DE
PRODUCCIÓN es una medida de la cantidad de unidades de un material que un centro
puede producir en un plazo determinado. Por ejemplo, el centro de Dallas de GBI puede
producir ya sea 15 o 10 bicicletas y 50 ensambles de rueda por día. La Figura 6-15
presenta un ejemplo de un plan de producción del centro Dallas, utilizando su
capacidad total.




Figura 6-15: Ejemplo de plan de producción de GBI




                                         16
MAESTRO DE MATERIALES
Se introdujo el concepto de maestro de materiales en el Capítulo 2. Recuerde que los
datos maestros de materiales se agrupan en diferentes vistas o segmentos en base a
tres factores: (1) el proceso que utiliza los materiales (por ejemplo, aprovisionamiento,
gestión de pedidos), (2) el tipo de material (por ejemplo, materias primas, productos
terminados) y (3) nivel organizativo (por ejemplo, los diferentes centros que utilizan el
material de manera diferente). Además, la vista de datos básica contiene datos que se
pueden aplicar a todos los procesos, tipos de materiales y niveles organizativos. En esta
sección se presentan dos vistas adicionales pertinentes a la producción;
específicamente, la planificación de necesidades de materiales (MRP) y la preparación
de trabajo. Tanto los datos de MRP y preparación de trabajo se deben definir a nivel de
centro. Es decir, son específicos para cada centro. Aunque los datos en estas vistas se
deben definir en el maestro de materiales para ejecutar el proceso de producción, son
más relevantes para el proceso de planificación de materiales, que determina qué
materiales se deben producir y cuándo se deben producir. En consecuencia, no se
discutirán los detalles de estos datos en este capítulo. En su lugar, se tratarán estos
datos en el capítulo sobre planificación de materiales (Capítulo 8).

MEDIOS AUXILIARES DE FABRICACIÓN
Los últimos datos maestros relevantes para producción son los MEDIOS AUXILIARES DE
FABRICACIÓN (MAF). Los MAF son recursos móviles que se comparten entre los diferentes
puestos de trabajo. Ejemplos de MAF son instrumentos de calibración o medición,
plantillas y dispositivos y documentos tales como diseños de ingeniería. No es factible
o económico mantener estos medios auxiliares en cada puesto de trabajo, ya que no se
utilizan muy a menudo. En cambio, un número limitado están disponibles para su uso
en los puestos de trabajo a medida que se necesiten.




                                           17
