---
curso: SIOPS
titulo: Procesos de Gestión de Stocks y Almacenes - 1. Gestión de Stocks
slides: 28
fuente: Procesos de Gestión de Stocks y Almacenes - 1. Gestión de Stocks.pdf
---

                Proceso de Gestión de
                 Stocks y Almacenes

                                              Prof. Carlos Villanueva Q.



Magal and Word | Integrated Business Processes with ERP Systems | © 2012
Traducido por Grandón, Pinto y Soto (2017), adaptado para UTEC por Juan Carlos Bueno
    Objetivos de aprendizaje
    1.     Discutir los 4 movimientos asociados con la gestión de
           stocks




    Magal and Word | Integrated Business Processes with ERP Systems | © 2012
2   Traducido por Grandón, Pinto y Soto (2017)
      Antecedentes
     El proceso de gestión de stocks y almacenes se relaciona con el
      almacenamiento y movimiento de los materiales en una
      organización.
     En el Proceso de Aprovisionamiento, se mostró la actividad básica
      de gestión de inventario (movimiento de mercancías)
     Los 4 tipos de movimientos de mercancías son:
       Entrada de mercancías
       Salida de mercancías
       Traslado
       Traspaso



     Magal and Word | Integrated Business Processes with ERP Systems | © 2012
3    Traducido por Grandón, Pinto y Soto (2017)
      Antecedentes
     El proceso – Gestión de Almacenes permite a las empresas
      gestionar los materiales más eficientemente.
     Existe una vinculación entre la Gestión de Stocks (IM) y la
      Gestión de Almacenes (WM).




     Magal and Word | Integrated Business Processes with ERP Systems | © 2012
4    Traducido por Grandón, Pinto y Soto (2017)
            Gestión de Stocks (IM)




    Magal and Word | Integrated Business Processes with ERP Systems | © 2011
5
    Gestión de Stocks (IM)
     Las empresas desempeñan los movimientos de mercancías
        utilizando clases de movimiento específicos que determinan:
         La información necesaria para ejecutar los traslados
         Las cuentas del LM que son afectadas.
     Nivel organizativo clave: Almacén
     Los maestros de datos relevantes:
         Maestro de materiales
         La vista de datos centro/almacén




    Magal and Word | Integrated Business Processes with ERP Systems | © 2012
6   Traducido por Grandón, Pinto y Soto (2017)
Fig. 1: Movimientos de mercancías




7
    1) Entrada de mercancías (Goods Receipt)
     Se traduce en un aumento del stock
     Puede tener lugar durante el proceso de producción
     Crea documentos de material y FI para ambos procesos
      Producción y IM-WM
     Se puede contabilizar entrada de mercancías sin una
      referencia a una orden
       Primera entrada al stock
       Entrada no planificada




8
    2) Salida de mercancías (Goods Issue)
     Se traduce en una disminución del stock
     En el proceso de Gestión de Pedidos esto indica una salida de
      productos terminados hacia un cliente mediante un pedido
      de compra.
     En el proceso de Producción esto refleja la salida de materias
      primas o productos semielaborados mediante una orden de
      fabricación
     Puede ser no planificada
     Los materiales pueden ser retirados para un consumo interno



9
     3) Traslado (Stock Transfer)
      Utilizado para mover físicamente material desde un nivel
       de organización o ubicación a otra.
      Un traslado puede involucrar movimientos bajo tres
       escenarios:
          Entre almacenes en un centro
          Entre centros en una sociedad
          Entre centros en diferentes sociedades




     Magal and Word | Integrated Business Processes with ERP Systems | © 2012
10   Traducido por Grandón, Pinto y Soto (2017)
     3) Traslado (cont.)
      Existen tres procedimientos disponibles para mover los
         materiales:
          Procedimiento de un paso
          Procedimiento de dos pasos
          Pedido de traslado de stock(Stock Transport Order)




     Magal and Word | Integrated Business Processes with ERP Systems | © 2012
11   Traducido por Grandón, Pinto y Soto (2017)
     Fig. 7-2: Procedimiento de uno y dos
     pasos




12
Traslado de almacén a almacén
      Traslado entre dos almacenes de un mismo centro.
      Razones de un traslado
         almacenamiento temporal
         control de calidad
      El traslado puede ser de uno o dos pasos:
           Procedimiento de un paso: un material puede estar en cualquier status
            (ubicación de entrega) y cualquier estado en el centro de recepción)
           Procedimiento de dos pasos: sólo es posible cuando los materiales en la
            ubicación de envío están en status de libre disposición




13
     Fig. 7-3: Opciones de traslado dentro
     de un centro




14
Traslado de almacén a almacén (cont.)
      El traslado entre almacenes de un mismo centro no afecta la
       valoración del material (misma valorización)
        No hay impacto financiero
        No hay documento FI
      Si los materiales en el almacen no tienen la misma
       valorización
        Hay impacto financiero
        Hay documento FI
        múltiples cuentas de material



15
       Traslado centro-a-centro
      Movimientos de mercaderías entre dos centros dentro de una
       misma sociedad
      Se puede utilizar procedimientos de uno o dos pasos.
        La diferencia está en el status del stock en el centro receptor (“libre
         utilización” en un paso y “en tránsito” en dos pasos
      Típicamente, sólo las mercaderías en status de libre utilización
       (disponibles) se pueden mover entre centros.
      Se crean documentos de material.
      Hay impacto financiero (documento FI)




16
     Fig. 7-4: Traslado de centro-a-centro




17
     Traslado sociedad-a-sociedad
       Los movimientos de materiales entre dos centros de
        diferentes sociedades
       Se puede utilizar procedimiento de uno o dos pasos
       Se crean dos documentos FI, uno por cada sociedad
           Una partida individual es para la cuenta de material
           La otra es para la cuenta de compensación creada para registrar
              dicho traslado




      Magal and Word | Integrated Business Processes with ERP Systems | © 2012
18    Traducido por Grandón, Pinto y Soto (2017)
     Pedido de traslado (Stock Transport Orders)
       Movimientos de centro-a-centro tienen limitaciones
       En los pedidos de traslado (STO) un centro “compra”
        materiales y otro centro las “vende”
       Puede involucrar etapas de los procesos de
        Aprovisionamiento, Gestión de Pedidos y Gestión de Stocks.
       Existen 3 tipos de pedido de traslado
         Pedido de traslado sin documento de entrega
         Pedido de traslado con documento de entrega
         Pedido de traslado con documento de entrega y facturación




19
 Pedido de traslado (STO) sin documento de
 entrega
      Involucra etapas de aprovisionamiento y gestión de stocks
      Un STO se crea directamente o referencia a otro documento (SP)
      Sólo se puede utilizar el procedimiento de dos pasos
      Se crea un documento de material para registrar el movimiento
      Se pueden crear uno o dos documentos FI
      Cuentas del LM.
        cuenta de material
        cuenta de compensación




20

 Fig. 7-5: Pedido de traslado sin entrega




     Magal and Word | Integrated Business Processes with ERP Systems | © 2012
21   Traducido por Grandón, Pinto y Soto (2017)
Pedido de traslado con entrega
      Se crea un documento de entrega(picking y embalaje) previo
       a la salida de mercancías.
      El pedido de traslado se trata igual que un pedido de cliente
      Se puede usar procedimiento de uno o dos pasos.
        Procedimiento de un paso: se crea sólo un documento de
         material y los materiales se registran en status de libre
         utilización en el centro receptor.
        Procedimiento de dos pasos: movimiento de materiales e
         impacto financiero se tratan idénticamente que un STO sin
         entrega



      Magal and Word | Integrated Business Processes with ERP Systems | © 2012
22    Traducido por Grandón, Pinto y Soto (2017)
 Fig. 7-6: Pedido de traslado con entrega




     Magal and Word | Integrated Business Processes with ERP Systems | © 2012
23   Traducido por Grandón, Pinto y Soto (2017)
     Pedido de traslado con entrega y facturación
       Un STO incluye un documento de entrega (etapa de expedición) y la
        etapa de facturación desde el proceso de gestión de pedidos en el
        centro emisor
       Un STO incluye la etapa de verificación de factura desde el proceso
        de aprovisionamiento en el centro receptor.
       Se incluye un precio de compra en el STO basado en las condiciones
        de precio y registros info.
       El centro suministrador crea un documento de entrega autorizando el
        envío.
       Una salida de mercancías se contabiliza en el centro suministrador.
       Una entrada de mercancías se contabiliza en el centro receptor.

24
Fig. 7-7: Pedido de traslado con entrega y
facturación




     Magal and Word | Integrated Business Processes with ERP Systems | © 2012
25   Traducido por Grandón, Pinto y Soto (2017)
     Ventajas de utilizar un STO (Pedido de Traslado)
     para mover materiales entre Centros

       Cuando se crea un STO, la empresa puede llevar a cabo una
        verificación de disponibilidad para evaluar la disponibilidad de
        material en el centro suministrador.
       Se pueden agregar al STO los costos de la entrega y de la
        empresa de transporte seleccionada.
       Se pueden incluir en la planeación de materiales de los dos
        centros las cantidades en el STO, las entregas y entradas planificadas.
       Las solicitudes de pedido se pueden convertir en STOs en vez de PCs.
       Se puede monitorear el historial de distintas tareas asociadas con
        el STO vía la sección historial de pedido del STO.

26
Fig. 1: Movimientos de mercancías




27
     4) Traspaso (Transfer Posting)
      Se utiliza para cambiar el estado o tipo de material en stock.
      Los cuatro estados típicos son:
        De libre utilización
        En inspección de calidad
        Bloqueado
        En tránsito
      Se puede utilizar en otras situaciones que no necesariamente
       involucre un movimiento físico de material.




28

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
