---
curso: SIOPS
titulo: 3. Teoría - Proceso de Gestión de Pedidos a detalle
slides: 45
fuente: 3. Teoría - Proceso de Gestión de Pedidos a detalle.pdf
---

## Slide 1

Portada del capítulo. Título "Proceso de Gestión de Pedidos". "Profesor: Carlos Villanueva Q." Créditos: "Adaptado de: Magal and Word | Integrated Business Processes with ERP Systems | © 2011. Traducido por Grandón, Pinto y Soto (2017)". Decorativa (portada institucional), sin contenido técnico adicional.

## Slide 2

**Objetivos de Aprendizaje**
1. Identificar las etapas claves en el proceso de Gestión de Pedidos, sus datos, documentos e información asociada a cada etapa.
2. Utilizar SAP S/4HANA para ejecutar las etapas claves en el proceso de Gestión de Pedidos.

Solo texto, sin elementos visuales adicionales.

## Slide 3

Slide separador de sección (fondo azul sólido, texto blanco centrado): "EL PROCESO DE GESTIÓN DE PEDIDOS". Decorativa, funciona como portada de la sección teórica.

## Slide 4

**Etapas del proceso** — Diagrama de flujo de proceso end-to-end de Gestión de Pedidos, con 5 cajas azules en fila superior conectadas por flechas horizontales:
1. **Actividad pre-ventas**: Contactos, Ofertas, Contratos, Acuerdos
2. **Gestión de pedidos de cliente**: Pedido de cliente
3. **Expedición**: Documento de picking, Entrega de salida, Salida de mercancías
4. **Facturación**: Factura cliente
5. **Pago**: Pago cliente → termina en círculo "Fin"

Debajo, dos círculos "Desencadenantes" alimentan con flechas cruzadas (dobles, en X) hacia las dos primeras cajas (Actividad pre-ventas y Gestión de pedidos de cliente):
- **Desencadenantes (acción del cliente)**: Consulta, Solicita oferta, Pedido de compra
- **Desencadenantes (acción del vendedor)**: Propuestas, Contactos, Campañas

Más abajo, un paralelogramo "Entrada de usuario" apunta hacia arriba al círculo de desencadenantes del cliente. En el centro, un cilindro de base de datos con dos secciones ("Datos maestros" / "Datos de transacción") intercambia flechas bidireccionales con la fila superior de procesos, y a la derecha alimenta (flecha) un conjunto de documentos apilados en cascada: **Documentos FI**, **Documentos CO**, **Documentos de material**, **Documentos de transacción**.

## Slide 5

Repetición del mismo diagrama de la Slide 4 (misma "Etapas del proceso": cadena Actividad pre-ventas → Gestión de pedidos de cliente → Expedición → Facturación → Pago → Fin, con desencadenantes cruzados, entrada de usuario, cilindro de datos maestros/transacción y documentos FI/CO/material/transacción en cascada). Sin título de slide visible (probablemente build/animación de la slide anterior sin el encabezado "Etapas del proceso").

## Slide 6

**Escenario de GBI** (caso de estudio usado en todo el capítulo):
- Cliente: RMB, Denver, CO.
- Bicicletas de turismo de lujo plateadas: 40
  - Repartos: 30 el 10 de Mayo, 10 el 10 de Junio
- Camisetas: 100 (califica para un descuento de un 10%)
  - Reparto: 10 el 10 de mayo
- Entrega específica en Colorado Springs

Tabla de precios:

| | Precio de Venta | Precio Costo |
|---|---|---|
| Bicicletas de turismo de lujo plateadas | $2,800 | $1,400 |
| Camisetas | $30 | $15 |

## Slide 7

**Actividades de Pre-venta**
- CRM liviano – establecer y mantener relaciones con los clientes
- Desencadenante: consulta o petición de oferta del cliente
- Incluye actividades:
  - Creación y seguimiento de contactos con los clientes
  - Campañas de mailing
  - Respuestas a clientes por consultas y cotizaciones
  - Cotización
  - Contrato Marco
    - Contratos
    - Planes de entrega

Solo texto (lista jerárquica), sin diagrama.

## Slide 8

**Elementos de una actividad de pre-venta** — Diagrama de flujo horizontal de 4 cajas conectadas por flechas:
1. **Desencadenantes**: Consulta del cliente/RFQ
2. **Datos**: Datos organizativos, Datos maestros, Entrada de usuario
3. **Tareas**: Crea oferta, Crea contrato marco
4. **Salidas**: Oferta, Contratos, Plan de entrega

## Slide 9

**Datos de una oferta** — Diagrama radial: círculo central "Oferta" rodeado por 6 cajas conectadas con flechas hacia el centro:
- **Datos organizativos**: Mandante, Sociedad, Área de ventas
- **Condiciones de precio**: Condiciones
- **Maestro de clientes**: Número cliente, Nombre cliente, Información de contacto
- **Registro info cliente-material**: Condiciones
- **Maestro de materiales**: Denominación de material, Unidad de medida
- **Entrada de usuario**: Número cliente, Número material, Cantidad, Fechas

## Slide 10

**Documentos de referencia para una oferta** — Diagrama: cuatro cajas de entrada (Consulta del cliente, Oferta, Pedido de cliente, Acuerdos) convergen mediante líneas hacia un conector común que apunta con una flecha a una caja de salida "Oferta". Ilustra que estos 4 tipos de documentos pueden servir como referencia para crear una oferta.

## Slide 11

**Elementos de un pedido de cliente** — Diagrama de flujo horizontal de 4 cajas:
1. **Desencadenantes**: PC cliente
2. **Datos**: Datos organizativos, Datos maestros, Entrada de usuario, Contratos
3. **Tareas**: Crear pedido de cliente, Ejecutar verificación de crédito, Seguimiento de contratos
4. **Salidas**: Pedido de cliente, Contratos actualizados, Verificación de disponibilidad, Plan de entrega, Necesidad de transporte

## Slide 12

**Datos de un pedido de cliente** — Diagrama radial: círculo central "Pedido de cliente" rodeado por 6 cajas:
- **Datos organizativos**: Mandante, Sociedad, Área de ventas, Centro de entrega
- **Condiciones de precio**: Condiciones
- **Contratos**: Número de contrato, Número de material, Cantidad, Fechas de entrega
- **Maestro de clientes**: Información de contacto, Datos de expedición, Datos de facturación, Funciones de interlocutor
- **Registro info cliente-material**: Condiciones, Datos de expedición, Datos de facturación
- **Maestro de materiales**: Denominación del material, Unidad de medida
- **Entrada de usuario**: Funciones de interlocutor, Número de material, Cantidad, Fechas

## Slide 13

**Relación entre oferta y pedidos de cliente** — Dos diagramas lado a lado:
- Izquierda: "Oferta 1" y "Oferta 2" convergen (muchas ofertas) hacia un solo "Pedido de cliente".
- Derecha: una sola "Oferta" se ramifica hacia "Pedido de cliente 1" y "Pedido de cliente 2" (una oferta origina múltiples pedidos).

Ilustra relación muchos-a-uno y uno-a-muchos entre ofertas y pedidos.

## Slide 14

**Estructura de un pedido de cliente** — Dos versiones del mismo documento "Pedido Estándar" lado a lado:
- Izquierda (esquema genérico): Cabecera, Posición 1 (con Reparto 1), Posición 2 (con Reparto 1 y Reparto 2).
- Derecha (ejemplo con datos, caso GBI): Cabecera con Fecha 23.01.2015, Número PC 45932, Solicitante RMB, Destinat. mcía. Lugar carrera. Tabla de posiciones:

| Posición | Material | Cantidad |
|---|---|---|
| 10 | Camiseta | 100 |
| — 1 (reparto) | 10 May | 100 |
| 20 | Bicicleta | 40 |
| — 1 (reparto) | 10 May | 30 |
| — 2 (reparto) | 10 Jun | 10 |

## Slide 15

**Documento pedido de cliente**
- Cabecera
  - Fechas, términos, datos de cliente, etc.
- Posiciones
  - Número de posición
  - Cantidad
  - Repartos
    - Fecha
    - Cantidad ordenada
    - Cantidad enviada

Solo texto (lista jerárquica).

## Slide 16

**Programación regresiva** — Diagrama de línea de tiempo con 6 hitos representados por iconos (calendario "1" con check, caja de embalaje, teléfono, montacargas, camión, calendario "6"):
1. Pedidos de entrada — Fecha pedido
2. Puesta a disposición del material — Fecha disponibilidad del material
3. Planificación del transporte — Fecha planificación del transporte
4. Carga — Fecha de carga
5. Salida de mercancías — Fecha salida de mercancías
6. Entrega — Fecha requerida de entrega

Debajo de la línea de tiempo, flechas retrospectivas (de derecha a izquierda) muestran los tramos de tiempo que el sistema calcula hacia atrás desde la fecha de entrega:
- "Tiempo de tránsito" (desde salida de mercancías hasta entrega)
- "Tiempo de carga" (desde fecha de carga hasta salida de mercancías)
- "Tiempo de realización de picking y embalar" (desde fecha de disponibilidad hasta fecha de carga)
- "Tiempo de planificación de transporte" (desde fecha de planificación del transporte hasta fecha de carga)

Nota en cuadro de texto: "El sistema utiliza el mayor de estos dos tiempos al programar las entregas" (refiriéndose a tiempo de picking/embalaje vs. tiempo de planificación de transporte).

## Slide 17

**Fuente de inventario**
- Solicitud de traslado (gestión de materiales / planificación de material)
- Desde stock
  - Gestión de material
- Compra interna
  - Proceso de producción en casa
- Compra externa
  - Proceso de aprovisionamiento

Solo texto (lista jerárquica), sin diagrama.

## Slide 18

**Expedición**
- Crear documento de entrega
- Picking (opcional)
- Embalar (opcional)
- Necesidad de transporte (si WM está disponible)
- Contabilizar salida de mercancías

Solo texto, sin diagrama.

## Slide 19

**Elementos de la etapa de expedición** — Diagrama de flujo horizontal de 4 cajas:
1. **Desencadenantes**: Pedidos de entrega pendientes
2. **Datos**: Datos organizativos, Datos maestros, Datos de transacción, Entrada de usuario
3. **Tareas**: Crear documento de entrega, Picking, Embalar, Necesidad de transporte, Contabilizar salida de mercancías
4. **Salidas**: Pedido de cliente/maestro de materiales/lista de facturas pendientes actualizados, Documento de material, Documento FI, Documento CO

## Slide 20

**Datos de un documento de entrega** — Diagrama radial: círculo central "Documento de entrega" rodeado por 6 cajas:
- **Maestro de clientes**: Información de contacto, Datos de expedición, Funciones de interlocutor
- **Datos organizativos**: Mandante, Sociedad, Área de ventas, Centro de entrega, Puesto de expedición
- **Registro info cliente-material**: Datos de expedición
- **Maestro de materiales**: Denominación del material, Unidad de medida, Peso, Datos de expedición
- **Pedido de cliente**: Repartos
- **Entrada de usuario**: Cantidad, Fechas

## Slide 21

**Estructura de un documento de entrega** — Dos versiones del documento "Entrega" lado a lado:
- Izquierda (genérico): Cabecera, Posición 1, Posición 2, Posición 3.
- Derecha (ejemplo GBI): Fecha 05.05.2015, Destinat. mcía. Lugar carrera. Tabla de posiciones:

| Posición | Material | Cantidad |
|---|---|---|
| 10 | Bicicletas | 30 |
| 20 | Camisetas | 100 |

## Slide 22

**Relación entre repartos y posiciones de entrega** — Diagrama: "Cabecera pedido de cliente" con Posición 1 (Reparto 1, Reparto 2) y Posición 2 (Reparto 1). Flechas horizontales conectan Posición 1 → "Posición 1 de entrega" y Posición 2 → "Posición 2 de entrega", ambas bajo "Cabecera entrega". Muestra cómo los repartos de un pedido se traducen en posiciones de un documento de entrega.

## Slide 23

**Relación entre pedidos de cliente y entregas** — Dos diagramas lado a lado:
- Izquierda: "Pedido de cliente 1" y "Pedido de cliente 2" convergen hacia una sola "Entrega".
- Derecha: un solo "Pedido de cliente" se ramifica hacia "Entrega 1" y "Entrega 2".

Ilustra relaciones muchos-a-uno y uno-a-muchos entre pedidos y entregas.

## Slide 24

**Expedición**
- Una orden >> múltiples entregas
- Múltiples órdenes >> una entrega
  - Limitaciones?
    - Algunos maestros
    - Algún punto de expedición
    - Alguna fecha de entrega
    - La misma dirección de entrega

Solo texto, sin diagrama.

## Slide 25

**Relación entre documentos de entrega y orden de transporte** — Dos diagramas lado a lado:
- Izquierda: "Entrega 1" y "Entrega 2" convergen hacia una sola "Orden de transporte".
- Derecha: un solo "Documento de entrega" se ramifica hacia "Orden de transporte 1" y "Orden de transporte 2".

## Slide 26

**Cantidad de entrega versus cantidad de picking** — Diagrama de flujo cíclico entre 3 cajas: "Documento de entrega" → (flecha "Cantidad de entrega") → "Orden de transporte" → (flecha vertical "Cantidad de picking") → "Proceso de gestión de almacenes" → (flecha "Cantidad tomada") de regreso a "Documento de entrega". Muestra el ciclo de retroalimentación de cantidades entre el documento de entrega, la orden de transporte y el almacén.

## Slide 27

**Opciones de embalaje** — Diagrama jerárquico de empaquetado dentro de una "Entrega":
- Columna "Posición/Material/Ctd": posición 1 (DXTR1000, 20), posición 2 (DXTR2000, 10), posición 3 (DXTR3000, 10), posición 4 (PRTR1000, 40).
- Columna "Elemento de expedición (SU)": SU1, SU2, SU3, SU4, cada uno empacado en "Caja 1" (icono de caja). Las posiciones 2 y 3 comparten una misma caja.
- Siguiente nivel: SU5 y SU6 agrupan las cajas en "Pallet 1" (icono de pallet) cada uno.
- Nivel final: SU7 agrupa los pallets en "Contenedor 1" (icono de contenedor).

Ilustra la jerarquía de unidades de embalaje: material → caja → pallet → contenedor.

## Slide 28

**Salidas de expedición (salida de mercancías)** — 3 cajas de salidas:
- **Contabilidad**: Cuentas de inventario, Coste de productos vendidos
- **Documentos**: Documento FI, Documento CO, Documento de material
- **Actualizaciones**: Listado de facturas pendientes, Documentos de ventas, Maestro de materiales

## Slide 29

**Impacto FI de la etapa de expedición** — Diagrama de asientos contables tipo "T" (cuentas T) para 6 cuentas: Existencias-productos terminados, Existencias-mercaderías, Costo de productos vendidos, Cliente, Banco, Ingresos por ventas, y Deudores (asociada). Se muestra el asiento marcado con círculo "1 Expedición":
- Existencias-productos terminados: Haber $42.000
- Existencias-mercaderías: Haber $1.500
- Costo de productos vendidos: Debe $43.500

Las cuentas Cliente, Banco, Ingresos por ventas y Deudores quedan sin movimiento en esta etapa.

Nota al pie: "Los valores de existencias y costo de productos vendidos se basan en los costos, no en el precio de venta. Costo de bicicletas: $1.400 por bicicleta (30 bicicletas). Costo de camisetas: $15 por camiseta (100 camisetas)."

## Slide 30

**Elementos de la etapa de facturación** — Diagrama de flujo horizontal de 4 cajas:
1. **Desencadenantes**: Entregas pendientes para facturación, Pedidos pendientes para facturación
2. **Datos**: Datos organizativos, Datos maestros, Datos de transacción, Entrada de usuario
3. **Tareas**: Crear documento de facturación (factura) (notas de crédito) (notas de débito), Cancelar documentos de facturación
4. **Salidas**: Entradas en el LM, Documento FI, Pedidos de cliente/documento de entrega/gestión de crédito del cliente y sistema de información de ventas, Documento CO (análisis de rentabilidad), Crédito de cliente reducido

## Slide 31

**Datos de un documento de facturación** — Diagrama radial: círculo central "Documento de facturación" rodeado por 5 cajas:
- **Maestro de clientes**: Información de contacto, Datos envío, Funciones de interlocutor
- **Datos organizativos**: Mandante, Sociedad, Área de ventas
- **Documento de entrega**: Número de material, Cantidad, Fechas
- **Pedido de cliente**: Datos de interlocutor, Número material, Cantidad, PC cliente
- **Entrada de usuario**: Fechas

## Slide 32

**Relación entre entregas y facturación** — Dos diagramas lado a lado:
- Izquierda: "Entrega 1" y "Entrega 2" convergen hacia un solo "Documento de facturación".
- Derecha: una sola "Entrega" se ramifica hacia "Documento de facturación 1" y "Documento de facturación 2".

## Slide 33

**Facturación**
- Muchas entregas >> un documento factura
  - Mismo pagador, fecha factura y país de destino
- Una entrega >> muchos documentos factura

Solo texto, sin diagrama.

## Slide 34

**Estructura de un documento de facturación** — Dos versiones lado a lado:
- Izquierda (genérico): Cabecera, Posición 1, Posición 2, Posición 3.
- Derecha (ejemplo GBI): Responsable de pago RMB. Tabla:

| Posición | Material | Cantidad facturada |
|---|---|---|
| 10 | Bicicleta de ruta | 30 |
| 20 | Camiseta | 100 |

## Slide 35

**Estructura del documento de facturación**
- Cabecera
  - Pagador, fecha de facturación, total
- Partidas
  - Número posición
  - Material
  - Cantidad de facturación
  - Precio

Solo texto (lista jerárquica).

## Slide 36

**Salidas de la etapa de facturación** — 3 cajas:
- **Contabilidad**: Cuenta del cliente, Deudores (cuenta asociada), Ingresos por ventas
- **Documentos**: Documento FI, Documento CO, Factura
- **Actualizaciones**: Documentos de ventas, Crédito del cliente (reducido), Maestro de materiales (cantidad), Sistema de información de ventas (estructuras)

## Slide 37

**Impacto financiero (FI) de la etapa de facturación** — Diagrama de cuentas T ampliado respecto a la slide de expedición, agregando el asiento marcado "2 Facturación":
- Rocky Mountain Bikes (cuenta cliente): Debe $86.700
- Ingresos por ventas: Haber $86.700
- Deudores (asociada): Debe $86.700 (reflejo del movimiento en Rocky Mountain Bikes)

Las cuentas de existencias y costo de productos vendidos (del asiento 1 Expedición) permanecen igual: Existencias-productos terminados Haber $42.000, Existencias-mercaderías Haber $1.500, Costo de productos vendidos Debe $43.500. Banco sin movimiento aún.

Nota: "Las cantidades de las cuentas de ingresos por ventas, cliente y deudores se basan en el precio de venta. Precio venta de bicicletas: $2.800 por bicicleta. Precio venta de camisetas: $27 por camiseta ($30-10% descuento)."

## Slide 38

**Elementos de la etapa de pago** — Diagrama de flujo horizontal de 4 cajas:
1. **Desencadenantes**: Pagos recibidos
2. **Datos**: Datos organizativos, Datos maestros, Datos de transacción, Entrada de usuario
3. **Tareas**: Registrar pagos, Imputar pagos a partidas abiertas
4. **Salidas**: Asientos contables en LM, Crédito del cliente (aumenta), Documento FI

## Slide 39

**Datos de un documento de pago** — Diagrama radial reducido: círculo central "Documento de pago" con 3 cajas:
- **Maestro de clientes**: Cuenta del cliente
- **Datos organizativos**: Mandante, Sociedad
- **Entrada de usuario**: Fechas, Monto a pagar

## Slide 40

**Impacto FI en la etapa de pago** — Diagrama de cuentas T con el asiento marcado "3 Pago" añadido:
- Rocky Mountain Bikes: Haber $86.700 (3), saldando el Debe $86.700 (2) previo
- Banco: Debe $86.700 (3)
- Deudores (asociada): Haber $86.700 (3), saldando el Debe $86.700 (2) previo

Cuentas anteriores (Existencias-productos terminados $42.000, Existencias-mercaderías $1.500, Costo de productos vendidos $43.500, Ingresos por ventas $86.700) se mantienen sin cambios. Leyenda: "1 Expedición, 2 Facturación, 3 Pago".

## Slide 41

**Pago del cliente con descuento** — Variante del diagrama de cuentas T de la slide 40, incorporando un descuento por pronto pago:
- Rocky Mountain Bikes: Debe $86.700 (2), Haber $86.700 (3)
- Banco: Debe $85.833 (3) — monto neto tras descuento
- Descuentos sobre venta (nueva cuenta): Debe $867 (3)
- Deudores (asociada): Debe $86.700 (2), Haber $86.700 (3)

Cuentas de existencias, costo de productos vendidos e ingresos por ventas se mantienen igual que en slides anteriores. Leyenda: "1 Expedición, 2 Facturación, 3 Pago". Ilustra que el pago neto ($85.833) más el descuento otorgado ($867) suman el monto adeudado ($86.700).

## Slide 42

**Tratamiento de pago del cliente** — Diagrama de flujo (diagrama de decisión) con forma de diamante:
1. Inicio: "Pago del cliente"
2. Decisión: "¿Pago completo?"
   - Sí → "Cuentas de cliente y asociadas saldadas"
   - No → Decisión: "¿Saldo adeudado (dentro de lo tolerado)?"
     - Sí → "Cuentas de cliente y asociadas saldadas"
     - No → se bifurca en dos opciones: "Contabiliza pago parcial" o "Genera una partida por el saldo"

Debajo de cada rama final se muestra un ejemplo de cuenta T "Rocky Mountain bikes":
- Contabiliza pago parcial: Debe $92.700, Haber $50.000 (marcado "Pago parcial")
- Genera partida por saldo: Debe $92.700, Haber $92.700, con nota "Saldo deuda → $42.700"

## Slide 43

**Proceso de Gestión de Créditos**
- Utilizado para evaluar si el crédito debe concederse al cliente (ej., ¿debe continuar el proceso?)
- Crédito se puede evaluar en 3 puntos:
  - Cuando el pedido del cliente se crea o cambia
  - Cuando la entrega se autoriza o cambia
  - Cuando se contabiliza la salida de mercancías
- Riesgo del crédito = suma de pedidos pendientes, entregas, facturas pendientes y valor del pedido.
- Salidas:
  - Advertir y continuar
  - Error y terminar
  - Bloquear la entrega

Solo texto (lista jerárquica), sin diagrama.

## Slide 44

**Proceso de gestión de créditos** — Diagrama de flujo de decisión:
1. "Crea pedido de cliente" → "Ejecuta revisión del crédito" → decisión en forma de diamante "¿Crédito por debajo del límite?"
   - Sí → "Continúa el proceso de gestión de pedidos"
   - No → "Bloquea entrega" → "Revisa crédito" → decisión "¿Libera?"
     - Sí → vuelve a "Continúa el proceso de gestión de pedidos"
     - No → "Informa al cliente"

## Slide 45

**Integración con otros procesos** — Diagrama radial: círculo central "Gestión de pedidos" conectado por líneas a 7 círculos periféricos que representan procesos relacionados: Contabilidad financiera, Contabilidad administrativa, Planificación de materiales, Gestión de stocks y almacenes, Sistemas de proyectos, Aprovisionamiento, Producción.
