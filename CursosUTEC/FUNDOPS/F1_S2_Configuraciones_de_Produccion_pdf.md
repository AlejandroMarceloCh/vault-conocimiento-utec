---
curso: FUNDOPS
titulo: F1-S2-Configuraciones de Producción
slides: 18
fuente: F1-S2-Configuraciones de Producción.pdf
---

FUNDAMENTOS DE OPERACIONES
Semana 2 – Configuraciones de producción
Índice



1. Entornos de producción
2. Configuraciones de proceso-producto
Inventory Management                                    José Antonio Larco




                       1   Entornos de producción:
                           ¿Cuál es nuestro contexto?
Decoupling Stock – Punto de desacople
                                        En qué punto de la cadena
                                        trabajamos bajo pedido

                                        Si trabajo bajo pedido o para
                                        Stock depende de:

                                        -   Volúmen del producto
                                        -   Tiempo de entrega (lead time)
                                        -   Variedad/personalización
                                                                                          José Antonio Larco




Decoupling Stock – Punto de desacople
                             Costos de intermediación:
            Trabajamos       Cómo ajustar a fluctuaciones en la demanda   Trabajamos
            con stock: MTS                                                a pedido: MTO




                                                                             Punto de
                                                                             desacople
                                                José Antonio Larco




Entornos de Producción (penetración de orden)

 Make to Stock (MTS)
 Fabricación para almacenamiento
 ▪ Se almacenan productos
   terminados
 ▪ El cliente decide adquirir o no el
   producto
 ▪ Requiere espacio de
   almacenamiento
 ▪ Aumenta el inventario
 ▪ Objetivos: evitar roturas de stock,
   evitar inventarios excesivos
                                                José Antonio Larco




Entornos de Producción (penetración de orden)

 Assemble to Order (ATO)
 Armado bajo pedido
 ▪ Existen módulos o sub-armados,
   que el cliente puede elegir para un
   paquete.
 ▪ Requiere espacio de
   almacenamiento de partes mas no
   de productos terminados
 ▪ Objetivos: evitar roturas de stock,
   evitar inventarios de partes
   excesivos
                                                José Antonio Larco




Entornos de Producción (penetración de orden)

 Engineer to Order (ETO)
 Ingeniería a pedido
 ▪ Se produce a pedido
 ▪ El cliente especifica el diseño
 ▪ Requiere mínimo espacio
 ▪ Objetivos: minimizar tiempos de
   entrega, tener capacidad de
   respuesta disponible, flexibilidad,
   control de cambios
                                                José Antonio Larco




Entornos de Producción (penetración de orden)

 Make to Order (MTO)
 Fabricación a pedido
 ▪ Se produce a pedido, normalmente
   existe catálogo preexistente
 ▪ El cliente decide adquirir o no el
   producto
 ▪ Requiere mínimo espacio
 ▪ Objetivos: minimizar tiempos de
   entrega, tener capacidad de
   respuesta disponible, flexibilidad
                                                        José Antonio Larco




Actividad 2

 Brindar ejemplos de por lo menos 4 productos para
 cada categoría.

 Indicar las ventajas y desventajas para cada tipo de
 configuración.
Inventory Management                                     José Antonio Larco




                       2   Configuraciones de proceso-
                           producto
                                                                       José Antonio Larco




Matriz producto / proceso: Entender el contexto


                               Proyecto

                               El proyecto sucede cuando se producen bienes únicos
                               altamente configurables.
                               Generalmente suceden en contextos de ETO y MTO.
                                                                                José Antonio Larco




    Matriz producto / proceso: Entender el contexto




                                                                           Job Shop




Se tienen múltiples rutas de producción con baja utilización de equipos.
Se ofrece mucha variedad de productos.

Se puede usar para ETO, MTO, ATO o MTS
                                                                                                José Antonio Larco




Matriz producto / proceso: Entender el contexto




                                                                                           Batch Shop




   Trabajo por lotes, se tiene inventario en proceso y algunas rutas de producción definidas.
   Se ofrece una variedad de productos intermedia.

   Usualmente se usa para ATO /MTS.
                                                                                                  José Antonio Larco




Matriz producto / proceso: Entender el contexto




                                                                                       Flow Shop




  Se trabaja una pieza a la vez o un lote fijo a la vez.
  Se utiliza un ritmo de producción balanceado en la línea utilizando el concepto de Takt-time.
  Los productos son discretos y usualmente se usa para ATO/MTS.
                                                  José Antonio Larco




Matriz producto / proceso: Entender el contexto
                                                                  José Antonio Larco




       Matriz producto / proceso: Entender el contexto
                                               Calidad/
                                               Flexibilidad/
                                               Tempo de entrega

   MTO




 MTS



Calidad/
                                               Eficiencia/
Flexibilidad/
                                               Costo
Tiempo de enrtrega
                                                                     José Antonio Larco



  Mensajes finales

1. Entender qué tipo de configuración de operaciones tenemos determina
   qué objetivos son más importantes y qué tipo de decisiones de gestión
   de operaciones son más críticas.
3. Dos posibles criterios son:
   a. Por punto de desacople (describe qué operación se realiza)
   b. Por tipología de proceso (describe el tipo de proceso)

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
