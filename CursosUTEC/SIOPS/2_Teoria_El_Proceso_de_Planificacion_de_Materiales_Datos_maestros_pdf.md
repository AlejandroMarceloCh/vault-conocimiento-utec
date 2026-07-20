---
curso: SIOPS
titulo: 2. Teoria - El Proceso de Planificación de Materiales (Datos maestros)
slides: 26
fuente: 2. Teoria - El Proceso de Planificación de Materiales (Datos maestros).pdf
---

Proceso de Planificación de Materiales
                        (Datos Maestros)

                                                                       Profesor: Carlos Villanueva Q.




      Adaptado de: Magal and Word | Integrated Business Processes with ERP Systems | © 2011             1
                             Traducido por Grandón, Pinto y Soto ( 2017)
                          Objetivos de Aprendizaje

1.   Describir los datos maestros asociados al proceso de Planificación de
     Materiales.
2.   Identificar Datos Maestros en el Sistema empresarial (S/4HANA).




                                                                             2
                              La Planificación de Materiales

● Busca responder a 3 preguntas clave:
   ○ ¿Qué materiales se necesitan?
   ○ ¿Cuántos se necesitan?
   ○ ¿Cuándo se necesitan?
● El principal objetivo es balancear la demanda y la oferta.
● Quiebre de stock vs. Inventario en exceso
● Genera propuestas de compra:
   ● Solicitudes de compra
   ● Órdenes de Producción planificadas

             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 9
   Proceso básico de planificación de materiales




Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                         Pinto y Soto ( 2017)
                                                                                                    4
Maestro de Materiales




                        37
                       Maestro de Materiales (Vistas)

Vistas MRP:
● MRP 1: Define estrategia general de planificación y cantidad a adquirir.
● MRP 2: Identifica scheduling y cómo obtener materiales (fabricar vs comprar)
● MRP 3: Estrategia para calcular el material disponible y cómo se fabricará el
  material.
● MRP 4: Datos para seleccionar la LMat adecuada.

Vista Work Scheduling (Preparación de Trabajo):
● Datos para determinar el tiempo de fabricación (setup, procesamiento,
  desmontaje)

                                                                                  37
Procurement Type (Clase de Aprovisionamiento)

● Indica si la provisión de un material es:
   ● Fabricación propia o interna
   ● Externa (compra)
   ● Ambas
   ● Ninguna de las dos.

● En Global Bike:
  ● FG->ambas
  ● TG, RM ->externa
  ● SF-> interna

              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  4
MRP Type (Planificación de Necesidades)

Especifica la técnica de control de producción utilizada en el planeamiento.

Son 3:
  1. Consumption-based planning
  2. Materials Requirement Planning (MRP)
  3. Master Production Scheduling (MPS)




              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  4
MRP Type (Planificación de Necesidades)

1. Consumption-based planning: Calcula requerimientos de material basándose
en la data histórica de consumo. Se realiza un pronóstico del consumo futuro.




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
MRP Type (Planificación de Necesidades)

1. Consumption-based planning:
● 1.1 Reorder point planning: Se basa en el stock de seguridad.
● 1.1 Forecast-based planning: Utiliza data histórica para estimar o pronosticar
   consumo futuro. Puede considerar patrones más complejos.
● 1.2 Time-phased planning es similar al forecast based planning. Se usa cuando
   los proveedores hacen entregas sólo algunos días de la semana.




              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  4
MRP Type (Planificación de Necesidades)
GBI usa consumption-based planning para mercaderías (Ej. cascos)




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
MRP Type (Planificación de Necesidades)

2. Técnica MRP: Calcula requerimientos de un material, basado en su
dependencia de otros materiales (LMat)
• Dependent Requirement: Su requerimiento depende del requerimiento de otro
   material. (Necesidades Secundarias)
• Independent Requirement: No depende de otro material, sino de la demanda
   del cliente. (Necesidades Primarias)

Calcula y planifica requerimientos para materiales en todos los niveles de la LMat
(BOM). Este procedimiento es: BOM explosion



              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  4
MRP Type (Planificación de Necesidades)

3. Técnica MPS:
(Master production
scheduling)
Proceso similar a
MRP            pero
enfocado         en
niveles superiores.
Es opcional.




              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  4
MRP Type (Planificación de Necesidades)

  El input para el MRP es el Independent Requirement de Productos
  Terminados (PIR), el cual es calculado por el paso Sales and
  Operations Planning del Proceso de Planificación de Materiales.




           Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                    Pinto y Soto ( 2017)
                                                                                                               4
MRP Type (Planificación de Necesidades)

● Planned Independent Requirement (PIR): Se basa en las ventas proyectadas

● Customer Independent Requirements (CIR): Se basa en Requerimientos del
  Cliente ú Ordenes de Venta actuales.




            Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                     Pinto y Soto ( 2017)
                                                                                                                4
Clave de Tamaño de Lote (Lot Size Key)

● Un tamaño de lote es la cantidad de material que figura en las propuestas de compra
  generadas en el proceso de planificación de materiales.
● La clave del tamaño de lote (Lot size key) es el procedimiento que determina el tamaño de lote:
   ➢ Cálculos estocásticos: Procedimientos que especifican una cantidad fija basada en un
       valor predeterminado (tamaño de lote fijo) o en la cantidad exacta requerida (lote por lote).
   ➢ Cálculos periódicos: Procedimientos que combinan los requerimientos de múltiples
       periodos de tiempo, como días o semanas en un lote.
   ➢ Tamaño de lote óptimo: Procedimientos que consideran el costo de comprar y almacenar
       materiales, utilizando técnicas de cálculo como economic order quantity y economic
       production quantity

     GBI usa el procedimiento lote por lote para determinar el tamaño de lote de todos sus
     materiales

                 Magal and Word | Integrated Business Processes with ERP Systems | © 2011
                                                          Pinto y Soto ( 2017)                     4
Tiempos de Planificación (Scheduling Times)

Una tarea del Proceso de Planificación de Materiales es estimar el tiempo necesario para
adquirir materiales necesarios.


El cálculo se basa en estimaciones del tiempo requerido para realizar tareas del maestro de
materiales y hoja de ruta del producto.
Incluye:
• Tiempo de fabricación propia, tiempo necesario para fabricar material internamente.
• Plazo de Entrega previsto, tiempo necesario para obtener el material cuando es
aprovisionado externamente.
• Tiempo de procesamiento de EM (Entrada de Mercancías), Tiempo necesario para colocar
los materiales en el almacén, disponibles para uso.




                Magal and Word | Integrated Business Processes with ERP Systems | © 2011
                                                         Pinto y Soto ( 2017)                 4
Horizonte de Planificación Fijo (Planning Time Fence)

● Periodo de tiempo donde el ERP no puede cambiar automáticamente las
  propuestas de compra planificadas.

● Ej: Si el planning time fence es 30 días, entonces ninguna orden de compra con
  fecha menor a 30 días podrá ser cambiada automáticamente por el Sistema, si
  se requieren cambios deben ser hechos manualmente.




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
Grupo de Verificación de Disponibilidad (Availability Check Group)

● Define la estrategia que usa el sistema para determinar si una cantidad del
  material estará disponible en una fecha específica.
● Método Available-To-Promise (ATP).
  ● Es el método más común. Considera elementos de suministro y demanda
  ● Suministro: inventario actual, solicitudes de compra, órdenes de compra,
     órdenes de fabricación.
  ● Demanda: reservas de material, stock de seguridad, pedidos de clientes.
● Es utilizado por varios procesos:
  ● Ventas: asegurar entrega al cliente en la fecha solicitada
  ● Producción: asegurar disponibilidad de materiales cuando la orden de
     fabricacion sea aprobada.
             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
Grupo de Estrategias (Strategy Group)

● Especifica la estrategia de planificación de alto nivel usada en Producción.
● Categorías:
  ● Fabricación contra stock (make-to-stock / MTS)
  ● Fabricación contra pedido (make-to-order / MTO)
  ● Montaje según catálogo (assemble-to-order / ATO)




              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  4

Strategy Group -> Make-to-stock (MTS)

● Los pedidos de los clientes se atienden usando un stock existente de productos
  terminados.
● La estrategia MTS la emplean generalmente las empresas que fabrican
  grandes volúmenes de productos idénticos.
● Esta estrategia reduce el tiempo requerido para cumplir los pedidos de cliente
  porque no hay necesidad de esperar hasta que los materiales se fabriquen.

● En SAP S/4HANA la estrategia más simple de MTS es planificación de
  necesidades netas (strategy 10), en la que el sistema genera propuestas de
  compra basadas en los PIRs únicamente, ignorando los CIRs.
● Una variante de la anterior es planificación con montaje final (strategy 40). Se
  basa en PIRs, pero también toma en cuenta los CIR a través del procedimiento
  llamado compensación              (consumption).
             Magal and Word | Integrated Business Processes with ERP Systems | © 2011
                                                      Pinto y Soto ( 2017)
                                                                                      Traducido por Grandón,
                                                                                                           4
  Strategy Group -> Make-to-order (MTO)

● La estrategia de producción de productos terminados y semiterminados es
  motivada por una orden de venta.
● La empresa no mantiene inventarios de productos terminados.
● MTO se utiliza cuando cada producto es único.




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
  Strategy Group -> Assemble-to-order (ATO)

● Es una variación de la estrategia MTO
● Se mantiene un inventario de componentes (semiterminados) necesarios para
  la fabricación de productos terminados.
● La producción de los productos terminados se desencadena por los pedidos de
  cliente (estrategia MTO)
● Ejemplo: pedidos de diferentes configuraciones de computadoras. Solo se debe
  ejecutar el ensamblaje final de componentes para atender pedidos de clientes.




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
  Modo de compensación (Consumption mode)

● Consumption es el proceso por el cual los CIRs consumen los PIRs.




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
  Consumption mode

● Dos   modos    conocidos   son
  backward consumption y forward
  consumption.     Se     pueden
  combinar ambos también.




            Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                     Pinto y Soto ( 2017)
                                                                                                                4
  Grupos de Productos (Product Groups)

● El planeamiento de materiales
  agrupa productos similares para
  mayor eficiencia.
● Aggregation: Agrupación de
  productos desde el nivel de
  material más bajo hasta el nivel
  más alto.
● Proportion factor: Medida de
  influencia del ítem en el Product
  Group.


                                                                   Traducido por Grandón,

                                      Magal and Word | Integrated Business Processes with ERP Systems | © 2011 Pinto y Soto ( 2017)

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
