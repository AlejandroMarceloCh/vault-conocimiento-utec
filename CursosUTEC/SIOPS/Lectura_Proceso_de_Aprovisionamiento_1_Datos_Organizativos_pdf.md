---
curso: SIOPS
titulo: Lectura - Proceso de Aprovisionamiento (1. Datos Organizativos)
slides: 7
fuente: Lectura - Proceso de Aprovisionamiento (1. Datos Organizativos).pdf
---

                                                                        CAPÍTULO 4

                                     El Proceso de Aprovisionamiento
En el Capítulo 1, se presentó un proceso simple de aprovisionamiento, el cual se muestra en
la Figura 4-1. Este diagrama indica que la etapa inicial en este proceso es la creación de una
solicitud de pedido, la cual se convierte en un pedido de compra y se envía a un proveedor.
Cuando el proveedor recibe el pedido de compra, envía los materiales que el comprador
recibe en la etapa de recepción de materiales. El comprador también recibe una factura del
proveedor y luego realiza un pago al proveedor.




Figura 4-1: Proceso básico de aprovisionamiento

En este capítulo se estudia el proceso de aprovisionamiento, también conocido como el
proceso de compra o solicitud de pedido hasta el pago. Se comienza abordando los datos
organizativos y datos maestros relevantes para este proceso. Luego se examina algunos de
los conceptos claves intrínsecos al proceso de aprovisionamiento. Después de considerar los
conceptos, se discuten las etapas del proceso con mayor detalle de lo que se hizo en el
Capítulo 1. El capítulo concluye con una discusión de las opciones de presentación de
informes.

Para ilustrar los conceptos y las etapas del proceso, se usa el siguiente escenario a través de
todo el capítulo. GBI ha descubierto que el stock de camisetas (SHRT1000) en el centro de
distribución de Miami es bajo. En consecuencia, la empresa debe adquirir más camisetas
antes de que se agoten y comience a perder ventas (y quizás clientes). GBI se aprovisiona de
todas sus camisetas de la empresa llamada Spy Gear. Además, las compra en cantidades de
500 unidades.

Tomado de:

Magal S. y Word J. (2017) Integración de Procesos de Negocio con Sistemas ERP. Epistemy
Press LLC. Adaptación al español de: Magal S. and Word J. (2012) Integrated Business
Processes with ERP Systems. John Wiley & Sons. Hoboken. NJ, USA.
   DATOS ORGANIZATIVOS
El proceso de aprovisionamiento se ejecuta en el contexto de niveles organizativos
específicos. Los niveles organizativos relevantes para el proceso de aprovisionamiento
incluyen mandante, sociedad y centro. Se discutieron estos niveles en el Capítulo 2. Recuerde
de esa discusión que un mandante representa una empresa global que se compone de
muchas empresas o subsidiarias, cada una de las cuales se representa mediante una
sociedad. La mayoría de las actividades del proceso de aprovisionamiento ocurren dentro de
una sociedad. Recuerde también que un centro cumple muchas funciones en una empresa.
En el contexto del aprovisionamiento, un centro es el lugar donde se reciben los materiales.
Por lo tanto, se le denomina centro receptor, en lugar de, por ejemplo, un centro de
fabricación donde los productos se fabrican realmente. Para comprar son relevantes tres
datos organizativos adicionales: almacenes, organización de compras y grupo de compras.
Se presentan cada uno a continuación.

ALMACÉN
Los ALMACENES son espacios dentro de un centro donde se guardan materiales hasta que estos
se requieran. Un centro puede tener múltiples almacenes, cada uno de los cuales se designa
para un propósito diferente (p.e., área de preparación, área de inspección) o almacena tipos
específicos de materiales (p.e., productos semielaborados). Almacenes más específicos
incluyen estantes, contenedores, gabinetes y bandejas. Los almacenes varían desde
pequeños contenedores hasta edificios enteros, dependiendo del tamaño de los materiales
que se almacenan. Por ejemplo, el almacén para tuercas y pernos será un pequeño recipiente,
mientras que el almacén para una aeronave será un hangar. Las organizaciones con sistemas
de gestión de stocks sofisticados, pueden gestionar sus materiales con un mayor nivel de
detalle. Se abordarán estos sistemas en el capítulo de gestión de stocks y almacenes.

Dependiendo de la naturaleza del negocio, sin embargo, un centro debe tener al menos un
almacén si necesita realizar un seguimiento de la cantidad y valor de los materiales en su
inventario. Por ejemplo, un centro que sirve como una instalación de producción o
almacenamiento debe llevar un registro exacto de la cantidad y valor de las materias primas,
productos semielaborados y productos terminados. Un centro no puede realizar esta función
sin almacenes. En otros casos, sin embargo, esta función no es necesaria. Por ejemplo, una
empresa generalmente no realiza un seguimiento de la cantidad o el valor de los suministros
que compra para una oficina corporativa (un centro). Por lo tanto, un almacén no es esencial.
Es importante mencionar que, aunque un centro puede tener varios almacenes, cada
almacén puede pertenecer solo a un centro.

La Figura 4-2 muestra almacenes para los cinco centros de GBI. El centro de Dallas tiene
cuatro almacenes. Almacena las materias primas (RM00), productos semielaborados (SF00),
productos terminados (FG00) y materiales varios (MI00). Los centros de Miami y San Diego,
que son centros de distribución (DCs), tienen tres almacenes para almacenar productos
terminados (FG00), mercaderías (TG00) y materiales varios (MI00). La estructura de los
almacenes en Alemania es similar a la de la empresa de EE.UU. La fábrica en Heidelberg tiene
una estructura similar a la de Dallas y la del centro en Hamburg a los centros en Miami y San
Diego. Tenga en cuenta que si bien los nombres de los almacenes son los mismos en los
diferentes centros (por ejemplo, el almacén FG00 existe en los cinco centros) ellos son
diferentes niveles organizativos. La combinación de centro y almacén debe ser única. Por lo
tanto, el centro de Dallas no puede tener otro almacén con el nombre FG00. Es común usar
los mismos nombres en los centros y sociedades si ellos representan el mismo tipo de
almacén, tales como materias primas y productos terminados.




Figura 4-2: Almacenes de GBI

ORGANIZACIÓN DE COMPRAS
Una ORGANIZACIÓN DE COMPRAS es la unidad de la empresa que realiza las actividades
estratégicas relacionadas con el aprovisionamiento de uno o más centros. Evalúa e identifica
proveedores, y negocia contratos y acuerdos, precios y otras condiciones. Una empresa
puede tener una o más organizaciones de compras. Normalmente hay tres modelos de
organizaciones de compras: a nivel de empresa global, a nivel de sociedad y a nivel de centro.
Estos modelos van desde altamente centralizados hasta altamente descentralizados. A
continuación, se detalla de cada uno de ellos.

Organización de compras a nivel de sociedad
La ORGANIZACIÓN DE COMPRAS A NIVEL DE SOCIEDAD, también conocida como organización de
compras entre sociedades, es el modelo más centralizado. Hay sólo una organización de
compras para toda la empresa y todos los centros que esta tenga. La Figura 4-3 muestra la
estructura organizacional de GBI usando el modelo a nivel de empresa global. Hay solo una
organización de compras corporativa, GL00, esta maneja todas las compras de los cinco
centros en ambas sociedades (US00 y DE00). En este modelo, se asigna la organización de
compras a cada centro, pero no a la sociedad.




Figura 4-3: Organización de compras a nivel de global




Organización de compras a nivel de sociedad
Con la ORGANIZACIÓN DE COMPRAS A NIVEL DE SOCIEDAD, también conocida como modelo entre
centros, una única organización de compras es responsable por los múltiples centros de una
sociedad. La Figura 4-4 muestra un modelo de este tipo para GBI. En la figura hay dos
organizaciones de compras: US00 y DE00. US00 es responsable de los tres centros de EE.UU.
y DE00 es responsable de los dos centros en Alemania. Este enfoque es menos centralizado
que el modelo a nivel de empresa global. En este modelo la organización de compras se
asigna al centro y a la sociedad. Sin embargo, una organización de compras se puede asignar
solo a una sociedad.
Figura 4-4: Organización de compras a nivel de sociedad

GBI tiene una empresa en los Estados Unidos y una en Alemania, cada una de ellas tiene su
propia organización de compras. Si GBI tuviese empresas en otros países europeos, cada país
podría tener una organización de compras por separado. Alternativamente, una
organización de compras podría administrar las compras de varios países. De hecho, es muy
común configurar organizaciones de compras distintas para cada país con el fin de hacer
frente al conjunto de leyes, impuestos y prácticas de negocios de dichos países.

Organización de compras a nivel de centro
El modelo más descentralizado es la ORGANIZACIÓN DE COMPRAS A NIVEL DE CENTRO, también
conocido como organización de compras específica de centro, en la cual cada centro cuenta
con su propia organización de compras. La Figura 4-5 muestra un modelo específico de
centro para GBI. Observe que cada centro tiene su propia organización de compras que es
responsable del aprovisionamiento de materiales de ese centro. Como en el caso del modelo
entre centros, en este escenario la organización de compras se asigna al centro y a su
sociedad.
Figura 4-5: Organización de compras a nivel de centro

Organización de compras de referencia
Cada modelo de organización de compras tiene sus ventajas y desventajas. Un modelo
altamente centralizado permite a la empresa negociar acuerdos favorables debido a que
compra materiales en grandes volúmenes. Sin embargo, la empresa puede no ser capaz de
tomar ventaja de las prácticas y relaciones locales con las que no está familiarizada. Además,
puede no reaccionar rápidamente a los cambios en las condiciones locales. Por el contrario,
se prefiere un modelo altamente descentralizado cuando los proveedores atienden
principalmente a un área geográfica local y el conocimiento de las prácticas y condiciones
locales permite a la empresa alcanzar acuerdos favorables. Finalmente, las empresas con
frecuencia adoptan un modelo híbrido que consiste en una organización de compras
centralizada que puede evaluar necesidades y oportunidades para toda la empresa y
negociar contratos globales, los que las organizaciones de compras de las sociedades utilizan.
Tal organización de compras se conoce como organización de compras de referencia.

GBI ha adoptado un modelo híbrido para incluir una única organización de compras de
referencia global (GL00), como se indica en la Figura 4-3, más múltiples organizaciones de
compras específicas para cada sociedad, tal como se indica en la Figura 4-4. En los Estados
Unidos, la organización de compras (US00) está físicamente ubicada en las instalaciones de
Miami y en Alemania la organización de compras (DE00) está físicamente ubicada en las
instalaciones de Heidelberg.
GRUPO DE COMPRAS
Mientras que la organización de compras es responsable de aspectos estratégicos del
aprovisionamiento, tales como negociación de contratos con proveedores, los grupos de
compras llevan a cabo las actividades de compra del día a día. Un GRUPO DE COMPRAS es una
persona o grupo de personas quiénes son responsables de las actividades de compra de
materiales o grupos de materiales. Estas actividades incluyen planificar, crear solicitudes de
pedidos, solicitar ofertas o cotizaciones a proveedores y crear y monitorear pedidos de
compra. Un PEDIDO DE COMPRA (PC) es una comunicación formal con el proveedor que
representa un compromiso de compra de los materiales indicados bajo los términos
establecidos. El grupo de compras también sirve como el principal punto de contacto con los
proveedores.

Un grupo de compras no siempre es una entidad dentro de la empresa. Algunas empresas
externalizan las actividades del grupo. Considere, por ejemplo, un caso en el cual una
empresa necesita adquirir terrenos o un edificio. La empresa muy probablemente contrate
un agente de bienes raíces para encontrar la propiedad que mejor se adapte a sus
necesidades. En este caso, el agente de bienes raíces sirve como el grupo de compras. Del
mismo modo, muchas empresas utilizan los servicios de agentes de compra para encontrar
proveedores adecuados y comprarles materiales, debido a que estos agentes están más
familiarizados con estos proveedores. GBI tiene un grupo de compras para América del Norte
(N00) y uno para Europa (E00).

Procesos de Negocio en la Práctica 4.1: Dell & Intel
Dell Computers e Intel Corporation muestran cómo las organizaciones de compras administran
las estrategias de compra locales y globales. Dell tiene instalaciones de fabricación en los
Estados Unidos, Brasil, Irlanda, Polonia, China, Malasia e India. La empresa compra grandes
cantidades de microprocesadores Intel para sus diversas líneas de computadores (portátiles,
ordenadores de escritorio y servidores). A su vez, Intel mantiene una fuerza de ventas dedicada
en la oficina central de Dell para negociar contratos de compra y gestionar la relación. Dell
tiene una organización de compras central que consolida globalmente requerimientos de
compra y negocia los precios centralmente con Intel. Sin embargo, los pedidos de compra se
crean en las instalaciones de fabricación locales de Dell en cada región. En otras palabras, Dell
EE.UU. compra chips a Intel EE.UU., Dell China compra chips a Intel China y así sucesivamente.
Todas las compras se basan en el contrato y en las condiciones de precios negociados
globalmente entre Dell e Intel, pero ellas se ejecutan localmente por los grupos de compras para
los distintos centros. Este acuerdo asegura que Dell recibe los mejores precios y condiciones
debido a la demanda acumulada y la supervisión estratégica de la organización de compras
centralizada. Al mismo tiempo, sin embargo, las instalaciones de fabricación locales mantienen
el control sobre las actividades tácticas de compra, debido a que la organización de compras se
encuentra en las mismas instalaciones. Intel también se beneficia de este acuerdo al tener
visibilidad global de las compras de Dell, de este modo la empresa puede ajustar mejor su
capacidad de fabricación para proporcionar la cantidad correcta de chips a Dell cuando y
donde se necesiten.

Fuente: Informes de Dell & Intel
