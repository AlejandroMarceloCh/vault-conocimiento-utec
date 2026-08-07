---
curso: SIOPS
titulo: 2.0 Teoría Proceso Aprovisionamiento - Proceso a Detalle
slides: 35
fuente: 2.0 Teoría Proceso Aprovisionamiento - Proceso a Detalle.pdf
---

## Slide 1

Portada del capítulo (decorativa: logo UTEC, franja azul degradada).
- Título: "El Proceso de Aprovisionamiento"
- Subtítulo: "Proceso a detalle"
- Profesor: Carlos Villanueva Q.

## Slide 2

Título: "Un Proceso de Aprovisionamiento Básico"

Diagrama de flujo horizontal con 4 iconos de personas/documentos conectados por flechas, y debajo de cada icono una tarjeta con área responsable y tarea:
1. Icono persona + caja → tarjeta **Almacén**: "Crea solicitud de pedido"
2. Icono persona + orden de compra ("PURCHASE ORDER") → tarjeta **Compra**: "Crea y envía orden de pedido"
3. Icono persona + caja → tarjeta **Almacén**: "Recibe materiales"
4. Icono persona + factura ("INVOICE") → tarjeta **Contabilidad**: "Recibe factura"
5. Icono persona + factura ("INVOICE") → tarjeta **Contabilidad**: "Envía pago"

Secuencia: Almacén (crea solicitud) → Compra (crea/envía OP) → Almacén (recibe materiales) → Contabilidad (recibe factura) → Contabilidad (envía pago).

## Slide 3

Slide de contenidos (texto plano, sin resaltar ninguna sección). Lista:
- Datos organizativos
- Datos maestros
- Conceptos claves
- Proceso
- Informes

## Slide 4

Slide de contenidos idéntica a la anterior, pero con el ítem **"Proceso"** resaltado con un recuadro rosado/borde azul, indicando que es la sección que se va a tratar en este capítulo.

## Slide 5

Título: "Proceso de Aprovisionamiento Detallado"

Diagrama de flujo de proceso central (recuadro azul claro de fondo) con las siguientes cajas y conexiones:
- **Desencadenante** (círculo azul, izquierda-abajo): "Proceso de cumplimiento", "Proceso de producción", "Proceso de planificación de materiales" → alimenta a "Determinación de necesidades"
- **Determinación de necesidades**: "Procesos de venta / Solicitud de pedido" → conecta a decisión romboidal
- Rombo de decisión: **"¿Fuente de aprovisionamiento conocido?"**
  - Si **Sí** → salta directo a "Selección y evaluación de proveedor"
  - Si **No** → pasa por "Determinación fuente de aprovisionamiento" ("Solicita propuesta", "Oferta") → luego "Selección y evaluación de proveedor"
- "Selección y evaluación de proveedor" → "Tratamiento orden de pedido" ("Orden de pedido") → "Entrada de Mercancías" ("Documento de envío") → "Verificación factura" ("Factura") → "Gestión de pagos" ("Pagos") → círculo **Fin**

Debajo del diagrama, tres elementos conectados con flechas verticales hacia la caja central del proceso:
- **Entrada de usuario** (trapecio) → alimenta el proceso
- **Datos maestros / Datos de transacción** (cilindro de base de datos) → intercambia con el proceso y genera documentos
- A la derecha del cilindro, cuatro "hojas" apiladas: **Documentos FI**, **Documentos CO**, **Documentos de material**, **Documentos de transacción**

## Slide 6

Título: "Etapas del Proceso"

Lista simple (plantilla de las 4 categorías que se repetirán en cada etapa del proceso a lo largo del capítulo):
- Desencadenante
- Datos
- Detalle de tareas
- Salidas

## Slide 7

Título: "Historia de GBI" (caso de estudio usado en todo el capítulo)

Lista de contexto del escenario:
- El inventario de camisetas (SHRT10##) es bajo (<=50) en el centro de Miami
- Por lo tanto, es necesario comprar más camisetas
- Spy Gear es el único proveedor de camisetas
- La cantidad comprada es de 500 camisetas
- El precio de compra por camiseta es de $15

## Slide 8

Título: "Elementos de la etapa de Solicitud de Pedido"

Diagrama de flujo horizontal con 4 cajas conectadas por flechas (esquema "Desencadenantes → Datos → Tareas → Salidas" que se repite en cada etapa):
- **Desencadenantes**: "Requerimiento de otros procesos", "Determinado manualmente"
- **Datos**: "Datos maestros", "Entrada de usuario"
- **Tareas**: "Crea solicitud"
- **Salidas**: "Solicitud de pedido"

## Slide 9

Título: "Datos de una Solicitud de Pedido"

Diagrama tipo "hub and spoke": un círculo central **"Solicitud de pedido"** recibe flechas desde 4 tarjetas alrededor:
- **Datos organizativos** (arriba): Mandante, Sociedad, Centro receptor, Grupo de compras
- **Maestro de proveedores** (izquierda arriba): Número proveedor
- **Registro info de compras** (derecha arriba): Número registro info, Número proveedor
- **Maestro de materiales** (izquierda abajo): Descripción material, Grupo de material, Unidad de medida, Precio de valoración
- **Entrada de usuario** (derecha abajo): Tipo de posición, Categoría de cuenta, Número de material, Cantidad, Fechas, Centro receptor

## Slide 10

Título: "Convirtiendo una Solicitud de Pedido en una Orden de Pedido"

Diagrama de flujo con 3 cajas superiores en línea: **Solicitud de pedido** → **Solicitud de oferta** → **Oferta**. Debajo, una caja **Orden de pedido** que recibe 3 flechas numeradas:
- Círculo "1": desde Solicitud de pedido directamente hacia Orden de pedido
- Círculo "2": desde Oferta directamente hacia Orden de pedido
- Círculo "3": desde Solicitud de oferta directamente hacia Orden de pedido

Es decir, la Orden de pedido puede generarse por 3 caminos distintos: directo desde la solicitud, desde una oferta, o desde una solicitud de oferta.

## Slide 11

Título: "Escenario GBI"

Continuación del caso de estudio:
- El proceso de planificación de materiales ha determinado:
  - Punto de pedido = 50
  - Cantidad pedida = 500
- Un empleado del centro de Miami revisa el informe de inventario y determina que es necesario realizar un pedido
- Solicitud: 500 SHRT1000 se entregarán en el centro de Miami en una cierta fecha

## Slide 12

Título: "Demo 4-7: Creación de una Solicitud de Pedido"

Slide de texto (solo bullet, sin gráfico):
- Crea una solicitud de pedido para material de almacén

## Slide 13

Título: "Elementos de la etapa Orden de Pedido"

Diagrama de flujo horizontal (mismo esquema Desencadenantes → Datos → Tareas → Salidas):
- **Desencadenantes**: Solicitud de pedido, RFQ, Oferta, Orden de pedido
- **Datos**: Datos maestros, Documentos de transacción, Entrada de usuario
- **Tareas**: Determina fuente de aprovisionamiento, Crea orden de pedido
- **Salidas**: Orden de pedido, Solicitud de pedido actualizadas, Contacto con proveedor

## Slide 14

Título: "Datos de una Orden de Pedido"

Diagrama hub-and-spoke: círculo central **"Orden de pedido"** con flechas desde:
- **Documentos de transacción** (izquierda): Solicitud, RFQ, Oferta
- **Datos maestros** (arriba): Materiales, Proveedores, Condiciones, Contratos y acuerdos, Registro info de compras
- **Entrada de usuario** (derecha): Verifica datos

## Slide 15

Título: "Estructura de una Orden de Pedido"

Dos tarjetas lado a lado (sin flechas entre ellas, solo desglose de la estructura del documento):
- **Cabecera**: Número orden de pedido, Datos orden de pedido, Términos de pago, Proveedor, Moneda
- **Posiciones (detalle)**: Material, Cantidad, Fecha de entrega, Precio

## Slide 16

Título: "Solicitud de Pedido a Orden de Pedido"

Diagrama de flujo N a N: a la izquierda 3 documentos apilados "Solicitud de pedido" convergen (mediante línea vertical) hacia una caja central **"Se convierte en"**, que a su vez se ramifica hacia 3 documentos "Orden de pedido" a la derecha. Ilustra que varias solicitudes de pedido pueden consolidarse/convertirse en varias órdenes de pedido (relación de conversión N:M, no necesariamente 1:1).

## Slide 17

Título: "Comunicación con los Proveedores"

Diagrama circular de flujo bidireccional entre el proceso de aprovisionamiento y el proveedor:
- **Proceso de aprovisionamiento** → **Orden de pedido**
- De Orden de pedido hacia el icono de **Proveedor** (persona): "Envía OP, agiliza solicitud, recordatorio" — "Medio de contacto: Correo, e-mail, fax, Servicio web, EDI"
- De vuelta del Proveedor hacia Orden de pedido: "Envía acuse de recibo, notificación de rechazo, notificación de despacho" — se muestra un documento "Acuse de recibo" junto al icono del proveedor

## Slide 18

Título: "Opciones de Tratamiento de Órdenes de Pedido"

Diagrama de flujo: en la parte superior, 3 documentos en línea **Solicitud de pedido → Solicitud de oferta → Oferta**, ambos convergen mediante línea vertical hacia una caja central **Orden de pedido**. También converge desde la izquierda un documento **Orden de pedido previa**, y desde abajo un documento **Documento sin referencia** (marcado con un ícono "X", indicando que no tiene documento de referencia previo). Desde la caja central **Orden de pedido**, dos flechas de salida van hacia:
- Icono **Proveedor** (persona con acuse de recibo)
- Icono **Otro centro** (edificio industrial)

Ilustra las distintas fuentes que pueden originar una orden de pedido (con o sin documento de referencia) y sus dos destinos posibles (proveedor externo u otro centro interno).

## Slide 19

Título: "Escenario GBI"

Continuación del caso, datos concretos para crear la orden de pedido:
- Cree una orden de pedido
  - Material: SHRT1000
  - Cantidad: 500
  - Proveedor: Spy Gear (de la lista de pedidos o entrada manual)
  - Centro receptor: Miami
  - Documento de referencia: solicitud de pedido
  - Precio: $15 cada una (desde el registro info)
  - Valor total de la OP: $7.500

## Slide 20

Título: "Demo 4-8: Conversión de una Solicitud de Pedido en una Orden de Pedido"

Slide de texto (bullets, sin gráfico):
- Convierte una solicitud de pedido creada previamente en una orden de pedido
- Revisa los datos de una solicitud de pedido

## Slide 21

Título: "Elementos de la Etapa de Entrada de Mercancías"

Diagrama de flujo horizontal (Desencadenantes → Datos → Tareas → Salidas):
- **Desencadenantes**: Entrega desde el proveedor
- **Datos**: Datos organizativos, Datos maestros, Documentos de transacción, Entrada de usuario
- **Tareas**: Verifica recepción de material, Crea documento de entrada de mercancías
- **Salidas**: Documento de material, Documento FI, Cuentas libro mayor actualizado, Orden de pedido actualizada, Maestro materiales actualizado, Lotes inspeccionados (QM), Necesidad de transporte (IWM), Contacto, Otras salidas

## Slide 22

Título: "Datos de la Etapa de Entrada de Mercancías"

Diagrama hub-and-spoke: círculo central **"Entrada de mercancías"** recibe flechas de:
- **Orden de pedido** (izquierda): Número OP, Materiales solicitados, Cantidad solicitada
- **Documento de entrega** (arriba): Número OP, Materiales entregados, Cantidad entregada
- **Entrada de usuario** (derecha): Verificación, Cambios necesarios, Centro receptor, Almacén, Clase de movimiento

## Slide 23

Título: "Impacto Financiero de la Entrada de Mercancías"

Diagrama contable de cuentas en "T" (Debe/Haber), mostrando el asiento contable generado por la entrada de mercancías:
- **Existencias**: Debe $7.500
- **EM/RF** (Entrada de mercancías/Recepción de factura): Haber $7.500
- **Banco**: sin movimiento (vacía)
- **Proveedor**: sin movimiento (vacía)
- **Acreedores**: sin movimiento (vacía)

Es decir, el asiento es: Existencias (Debe) $7.500 contra EM/RF (Haber) $7.500; las demás cuentas aún no se afectan en esta etapa.

## Slide 24

Título: "Documentos de Material y Contable de una Entrada de Mercancías"

Dos tablas conectadas por una flecha, replicando pantallas/documentos del sistema:

**Documento de material** (tabla)
Cabecera del documento:
| Campo | Valor |
|---|---|
| Doc. de material | 5000000757 |
| Fecha | 04.06.2015 |
| Nota de entrega | LS-1147 |

Posiciones del documento:
| # | Cantidad | Material | Centro | CMO |
|---|---|---|---|---|
| 001 | 500 EA | Camiseta | MI00 | 101 |

**Documento contable** (tabla, generado a partir del anterior)
Cabecera del documento:
| Campo | Valor |
|---|---|
| Doc. contable | 5000000642 |
| Fecha | 04.06.2015 |
| Referencia | LS-1147 |
| Moneda | USD |

Posiciones del documento:
| # | Cuenta | Texto breve | Monto USD |
|---|---|---|---|
| 1 | 200200 | Existencias-Mds. | 7.500+ |
| 2 | 310000 | Cuenta EM/RF | 7.500- |

## Slide 25

Título: "Demo 4-9: Recibiendo mercancías mediante una orden de pedido abierta"

Slide de texto (bullets, sin gráfico):
- Registra la recepción de materiales para una orden de pedido creada previamente
- Revisa los datos de la solicitud de pedido asociada
- Revisa los datos de la orden de pedido asociada

## Slide 26

Título: "Proceso de Aprovisionamiento" (encabezado del diagrama; en el texto plano corresponde a "Elementos de la Etapa de Verificación de Factura" pero visualmente esta slide 26 es el diagrama BPMN completo, distinto del resto)

**Captura/diagrama BPMN completo del proceso de aprovisionamiento**, organizado en 4 carriles (swimlanes) horizontales rotulados a la izquierda: **Contabilidad**, **Compra** (ambos agrupados bajo "GBI"), **Almacén**, **Proveedor**.

Flujo (de izquierda a derecha, con conectores continuos y punteados representando mensajes/documentos):
- **Almacén**: círculo de inicio (verde) → "Crear Solicitud de Pedido" (genera documento "Solicitud de pedido") → evento intermedio "Espera de Pedido" (envelope) → "Entrada de Mercancías" (usa "Documento de Material (Stock)" y "Orden de Pedido", genera "Documento entrada mercancías") → evento intermedio "Espera Factura"
- **Compra**: "Recepciona Solicitud de Pedido" → "Selección y Evaluación del Proveedor" → "Generar orden de pedido" (genera documento "Orden de Pedido") → "Enviar Orden de pedido" (tarea de envío, ícono de sobre)
- **Contabilidad**: "Recepcionar Factura de Compra" (usa documento "Factura" y "Documento Contable") → "Verificar Factura" (genera "Documento Contable", usa "Orden de Pedido", "Factura", "Documento de material") → "Pagar Factura" (genera "Documento Contable") → círculo de fin (rojo)
- **Proveedor**: carril vacío de contraparte externa, con documentos de interfaz en la parte inferior del diagrama: "Orden de Pedido", "Lista de Embalaje", "Factura" (conectan con eventos de envío/recepción entre Compra/Almacén/Contabilidad y el proveedor externo mediante círculos con sobre)

Es el mapa de proceso end-to-end (notación tipo BPMN) que integra visualmente todas las etapas cubiertas por separado en el resto del capítulo: solicitud → orden de pedido → entrada de mercancías → verificación de factura → pago.

## Slide 27

Título: "Elementos de la Etapa de Verificación de Factura"

Diagrama de flujo horizontal (Desencadenantes → Datos → Tareas → Salidas):
- **Desencadenantes**: Factura del proveedor
- **Datos**: Datos maestros, Documentos de transacción, Entrada de usuario
- **Tareas**: Triple verificación, Crear factura
- **Salidas**: Factura, Orden de pedido actualizada, Documento FI, Maestro de materiales actualizado

## Slide 28

Título: "Datos necesarios para la Verificación de Factura"

Diagrama hub-and-spoke: círculo central **"Verificación factura"** recibe flechas de 4 tarjetas:
- **Documento de material** (arriba izq): Número OP, Materiales entregados, Cantidades entregadas
- **Factura** (arriba der): Número proveedor, Fecha, Cantidad, Monto
- **Orden de pedido** (abajo izq): Número OP, Número proveedor, Materiales solicitados, Cantidades solicitadas, Precio
- **Entrada de usuario** (abajo der): Verificar datos

## Slide 29

Título: "Impacto Financiero de la Verificación de Factura"

Diagrama contable en "T" (Debe/Haber) con pasos numerados en círculos azules:
- **Existencias (Mercaderías)**: ① Debe $7.500 (de la entrada de mercancías previa)
- **EM/RF**: ② Debe $7.500 | Haber $7.500 ① (se cierra/compensa)
- **Banco**: sin movimiento
- **Proveedor**: Haber $7.500 ②
- **Acreedores (asociada)**: Haber $7.500 ②

Leyenda al pie: ① Entrada de mercancías, ② Verificación factura. Las flechas curvas conectan Proveedor(Haber) con Acreedores(Haber), mostrando que la verificación de factura mueve el pasivo de "Proveedor" genérico a la cuenta de "Acreedores" asociada específica.

## Slide 30

Título: "Demo 4-10: Recepción y Verificación de una Factura"

Slide de texto (bullets, sin gráfico):
- Verifica y registra una factura recibida de un proveedor.
- Revisa los datos de la orden de pedido asociada

## Slide 31

Título: "Elementos de la Etapa de Pago"

Diagrama de flujo horizontal (Desencadenantes → Datos → Tareas → Salidas):
- **Desencadenantes**: Factura verificada
- **Datos**: Datos maestros, Documentos de transacción, Entrada de usuario
- **Tareas**: Seleccionar método, Seleccionar banco, Seleccionar posiciones, Calcular monto, Contabilizar pago, Imprimir
- **Salidas**: Pago (cheque o pago electrónico), Documento FI

## Slide 32

Título: "Datos necesarios para el Pago a Proveedor"

Diagrama hub-and-spoke: círculo central **"Pago a proveedor"** recibe flechas de 3 tarjetas:
- **Factura** (izquierda): Número proveedor, Fecha, Cantidad
- **Maestro de proveedores** (arriba): Condiciones de pago, Método de pago, Dirección de pago
- **Entrada de usuario** (derecha): Verifica datos

## Slide 33

Título: "Impacto Financiero del Pago a Proveedor"

Diagrama contable en "T" con pasos numerados (continuación acumulada de los asientos previos):
- **Existencias (Mercaderías)**: ① Debe $7.500
- **EM/RF**: ② Debe $7.500 | Haber $7.500 ①
- **Banco**: Haber $7.500 ③
- **Proveedor**: ③ Debe $7.500 | Haber $7.500 ②
- **Acreedores (asociada)**: ③ Debe $7.500 | Haber $7.500 ②

Leyenda: ① Entrada de mercancías, ② Verificación factura, ③ Gestión de pagos. Flechas curvas cruzadas conectan Proveedor(Debe) con Acreedores(Haber) y viceversa, cerrando el ciclo contable completo: Existencias → EM/RF → Proveedor/Acreedores → Banco.

## Slide 34

Título: "Demo 4-11: Pago a proveedor"

Slide de texto (bullet, sin gráfico):
- Registra el pago hecho a un proveedor para una factura previamente registrada

## Slide 35

Título: "Integración con otros procesos"

Diagrama tipo "rueda" con un círculo central **"Aprovisionamiento"** conectado mediante líneas a 8 círculos periféricos dispuestos alrededor (formando un anillo):
- Planificación de materiales
- Ejecución de producción
- Cumplimiento (ventas)
- Mantenimiento
- Contabilidad financiera
- Contabilidad interna
- Gestión de stocks y almacenes
- Gestión de proyectos

Ilustra que el proceso de Aprovisionamiento se integra e intercambia información con estos 8 procesos/módulos del ERP.
