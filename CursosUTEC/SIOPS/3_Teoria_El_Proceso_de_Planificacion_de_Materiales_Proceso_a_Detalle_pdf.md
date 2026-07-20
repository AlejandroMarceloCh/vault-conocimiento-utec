---
curso: SIOPS
titulo: 3. Teoria - El Proceso de Planificación de Materiales (Proceso a Detalle)
slides: 38
fuente: 3. Teoria - El Proceso de Planificación de Materiales (Proceso a Detalle).pdf
---

Proceso de Planificación de Materiales
                      (Proceso a Detalle)

                                                                       Profesor: Carlos Villanueva Q.




      Adaptado de: Magal and Word | Integrated Business Processes with ERP Systems | © 2011             1
                             Traducido por Grandón, Pinto y Soto ( 2017)
                          Objetivos de Aprendizaje

1.   Describir las etapas del proceso de Planificación de Materiales.
2.   Identificar etapas del proceso en el Sistema empresarial (S/4 HANA).




                                                                            2
Proceso de
planificación
de materiales




                Magal and Word | Integrated Business Processes with ERP Systems | © 2011 por Grandón,
                                                                                 Traducido
                                                         Pinto y Soto ( 2017)
                                                                                                        4
                                     Introducción

● SOP: herramienta de planeamiento y pronóstico que las empresas
  utilizan para generar un pronóstico de ventas, determinar
  requerimientos de inventario y generar un Plan de Operaciones
  (preliminar).
● SOP crea un Plan de Producción al nivel de Product Group.
● Disaggregation: Los requerimientos de SOP se traducen en PIRs para
  ese Product Group .
● Los PIRs se transfieren a Demand Management donde se afinan.
● MRP crea propuestas de aprovisionamiento para asegurar los
  materiales necesarios para el proceso productivo.

           Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                    Pinto y Soto ( 2017)
                                                                                                               9
Proceso de
planificación
de materiales




                Magal and Word | Integrated Business Processes with ERP Systems | © 2011 por Grandón,
                                                                                 Traducido
                                                         Pinto y Soto ( 2017)
                                                                                                        4
SALES AND OPERATIONS PLANNING




          Elementos de la etapa SOP



                                      37
SALES AND OPERATIONS PLANNING

 Triggers

● SOP se ejecuta periódicamente para revisar el Plan de Producción.
● Cambios en el entorno económico.
● Tipos: SOP standard, SOP flexible.
● Standard planning usa modelos o plantillas de planeamiento predefinidas.
● Flexible Planning usa modelos más complejos que descienden hasta calcular
  cantidades para cada centro.




            Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                     Pinto y Soto ( 2017)
                                                                                                                4
SALES AND OPERATIONS PLANNING
  Data




                                                                          Traducido por Grandón,
             Magal and Word | Integrated Business Processes with ERP Systems | © 2011              4
                                                      Pinto y Soto ( 2017)
SALES AND OPERATIONS PLANNING

  Tasks


 ● Crear Plan de Ventas
 ● Definir requerimientos de inventario
 ● Crear un Plan de Producción




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
SALES AND OPERATIONS PLANNING




    Standard SOP Planning Table
  SALES AND OPERATIONS PLANNING




● Sales: Plan de ventas
● Production: Plan de Producción calculado por el sistema.
● Stock level: Niveles de inventario generados por el sistema.
● Target stock: Niveles de stock deseados. Ingresado por usuario.
● Day’s supply: # días que la empresa espera cubrir ventas solo con el inventario
  existente. Lo calcula el sistema.
● Target day’s supply: El usuario ingresa el day’s supply en esta fila.


             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
● Esta fila contiene el plan de ventas.
Posible origen de esta data:
● Niveles deseados de rentabilidad provenientes de management accounting.
● Data histórica del SIS (Sales Information System)
● Un forecast basado en el histórico de ventas.
● Ingreso manual de empleados experimentados.
● Plantilla del plan usado para otro Product Group.


             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
El sistema genera un plan de producción basado en una de estas opciones:

● Synchronous to Sales: El sistema copia cantidades de la fila plan de ventas.
● Target stock level: La empresa especifica un nivel de stock deseado que se
  considera en el plan, además del plan de ventas.
● Target day’s supply: Similar al anterior, pero el nivel de inventario deseado se
  expresa en un número de días y no en cantidades.
● Stock level = 0: El nivel de stock deseado al final de cada periodo es cero.




              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  4
Ejemplo de SOP para GBI




                                Cálculo de Producción para el tercer mes (M03)




                          Ejemplo de cálculo del Day’s Supply – segundo mes (M02)
               SALES AND OPERATIONS PLANNING

 Outcomes

● La salida del SOP es una o más versiones del plan de producción.
● No se genera impacto financiero ni movimiento de materiales.




            Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                     Pinto y Soto ( 2017)
                                                                                                                4
Proceso de
planificación
de materiales




                Magal and Word | Integrated Business Processes with ERP Systems | © 2011 por Grandón,
                                                                                 Traducido
                                                         Pinto y Soto ( 2017)
                                                                                                        4
DISAGGREGATION


● El Plan de Ventas y Producción creado en SOP (a nivel de Product Group) se
  traduce en planes para los productos terminados que conforman el árbol
  jerárquico del grupo.




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
               DISAGGREGATION
  Data

● El sistema utiliza los proportion
  factors del Product Group para
  calcular los valores desagregados
  para cada elemento del Product
  Group.
● La salida de este paso es el cálculo
  de PIRs para cada periodo (semana
  o mes).
DISAGGREGATION




 Disaggregation para el Grupo de Producto PG-BIKE000
DISAGGREGATION




     Transferencia de PIRs a Demand Management

Proceso de
planificación
de materiales




                Magal and Word | Integrated Business Processes with ERP Systems | © 2011 por Grandón,
                                                                                 Traducido
                                                         Pinto y Soto ( 2017)
                                                                                                        4
DEMAND MANAGEMENT


● Calcula los revised PIRs, considerando PIRs del SOP(después del
  disaggregation), CIRs y data del Material Master respecto a estrategias de
  planeamiento (vistas MRP).




              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  4
DEMAND MANAGEMENT




          Data utilizada en este paso
                 DEMAND MANAGEMENT
Outcomes


● PIRs para cada material incluido en el planeamiento, incluyendo cantidades y
  fechas específicas.
● No implica movimientos financieros ni de materiales.




              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  4
Proceso de
planificación
de materiales




                Magal and Word | Integrated Business Processes with ERP Systems | © 2011 por Grandón,
                                                                                 Traducido
                                                         Pinto y Soto ( 2017)
                                                                                                        4
MATERIAL REQUIREMENTS PLANNING


● Calcula el net requirements para materiales y crea propuestas de compra o
  producción de materiales para todos los niveles del LMat(BOM).




              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
MATERIAL REQUIREMENTS PLANNING

● El MRP Controller es responsable del monitoreo de resultados del proceso de
  planeamiento. Las órdenes planificadas deben convertirse en órdenes de
  producción o solicitudes de compra. Las órdenes de producción deben
  liberarse, podrían necesitar reagendarse debido a problemas de scheduling o
  capacidad, etc.
● MRP se puede ejecutar de forma selectiva.
● MPS es un MRP especializado.




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
MATERIAL REQUIREMENTS PLANNING




         Procedimiento MRP
MATERIAL REQUIREMENTS PLANNING

Check Planning File


● Primera tarea: determinar materiales a planificarse.
● Cualquier cambio a un material relevante al MRP, se registra en este archivo.
● Cambios relevantes pueden ser: scheduling times en material master o
  elementos MRP (niveles de inventario, solicitudes u órdenes de compra)




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
MATERIAL REQUIREMENTS PLANNING

Calculate Net Requirements


● Identifica faltas de material y genera propuestas de aprovisionamiento.
● El método de cálculo depende del MRP Type indicado en el material master.
● Si el MRP Type es MRP ó MPS, el cálculo es motivado por la existencia de un
  requerimiento dependiente o independiente.
● Para cada requerimiento, calcula si hay material suficiente. Si el resultado es
  negativo se genera una propuesta de aprovisionamiento.

                Available stock = Plant stock - Safety stock + Receipts¹ - Issues²
     1 Good Receipts: Purchase Orders, firmed purchased requisitions, firmed planned orders, production orders,
     2 Good Issues: CIRs, PIRs, material reservations,
                                                                                                                  4
MATERIAL REQUIREMENTS PLANNING

Determine Lot Size


● Este # lo define el Lot Size Key del maestro de materiales.




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
MATERIAL REQUIREMENTS PLANNING

Perform Scheduling


● Lo hace a través del forward scheduling y backward scheduling




             Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                      Pinto y Soto ( 2017)
                                                                                                                 4
MATERIAL REQUIREMENTS PLANNING

Determine Procurement Proposals


● Se determina el tipo
  de propuesta de
  aprovisionamiento a
  generar.




              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  4
MATERIAL REQUIREMENTS PLANNING

Determine Dependent Requirements


● Para materiales
  producidos in-house,
  MRP genera
  requerimientos
  dependientes para
  cada material vía el
  BOM explosion.




              Magal and Word | Integrated Business Processes with ERP Systems | © 2011   Traducido por Grandón,
                                                       Pinto y Soto ( 2017)
                                                                                                                  4
MATERIAL REQUIREMENTS PLANNING




● El sistema crea PIRs
  para 8 materiales
MATERIAL REQUIREMENTS PLANNING




● El Processing Key
  determina cómo se
  completan los pasos
  del MRP.
  MATERIAL REQUIREMENTS PLANNING
Existen parámetros de control que determinan cómo se completan los pasos en
el MRP.

● El parámetro Processing Key determina cómo se procesan los materiales del
  Planning File. Hay 3 Processing Keys:
● Regenerative planning (NEUPL): Planifican todos los materiales relevantes a
  MRP, se descarta data de planificaciones previas. (Very time consuming).
  Poco usado.
● Net change planning (NETCH): Se planifican solo aquellos materiales que han
  tenido un cambio MRP relevante (cualquier actividad que afecta la
  disponibilidad del material).
● Net change planning in the planning horizon (NETPL): Se planifican solo
  aquellos materiales que han tenido un cambio MRP relevante dentro de un
  periodo de tiempo específico denominado planning horizon.
MATERIAL REQUIREMENTS PLANNING
Existen parámetros de control adicionales: que determinan la salida del
procedimiento MRP:
● Create purchase requisitions: determina si MRP (1) siempre crea solicitudes
   de compra, (2) crea órdenes planificadas, ó (3) crea solicitudes de compra en
   la apertura del periodo y órdenes planificadas después de la apertura.
● Delivery Schedules: Aplica a los Scheduling agreements. Opciones: (1) no
   crear Schedule lines, (2) Crearlas solo en apertura de periodo o (3) crearlos
   solo dentro del planning horizon.
● Create MRP list: Determina si el sistema creará la lista MRP.
● Planning mode: Determina cómo se tratarán las propuestas de
   aprovisionamiento creadas previamente. Se descartan o consideran.
● Scheduling: Determina si el sistema calcula fechas básicas o lo hace a mayor
   detalle consultando la hoja de ruta.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
