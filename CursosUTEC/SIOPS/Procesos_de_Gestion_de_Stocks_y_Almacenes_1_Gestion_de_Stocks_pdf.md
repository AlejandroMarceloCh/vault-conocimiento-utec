---
curso: SIOPS
titulo: Procesos de Gestión de Stocks y Almacenes - 1. Gestión de Stocks
slides: 28
fuente: Procesos de Gestión de Stocks y Almacenes - 1. Gestión de Stocks.pdf
---

## Slide 1

Portada (decorativa: franjas de color naranja/rosa/gris, textura rayada de fondo).

**Proceso de Gestión de Stocks y Almacenes**

Prof. Carlos Villanueva Q.

## Slide 2

**Objetivos de aprendizaje**

1. Discutir los 4 movimientos asociados con la gestión de stocks

Slide solo texto, sin elementos visuales adicionales.

## Slide 3

**Antecedentes**

- El proceso de gestión de stocks y almacenes se relaciona con el almacenamiento y movimiento de los materiales en una organización.
- En el Proceso de Aprovisionamiento, se mostró la actividad básica de gestión de inventario (movimiento de mercancías)
- Los 4 tipos de movimientos de mercancías son:
  - Entrada de mercancías
  - Salida de mercancías
  - Traslado
  - Traspaso

Slide solo texto (lista con viñetas), sin diagramas.

## Slide 4

**Antecedentes**

- El proceso – Gestión de Almacenes permite a las empresas gestionar los materiales más eficientemente.
- Existe una vinculación entre la Gestión de Stocks (IM) y la Gestión de Almacenes (WM).

Slide solo texto.

## Slide 5

Slide separador de sección (texto centrado, sin bullets ni gráficos):

**Gestión de Stocks (IM)**

## Slide 6

**Gestión de Stocks (IM)**

- Las empresas desempeñan los movimientos de mercancías utilizando clases de movimiento específicos que determinan:
  - La información necesaria para ejecutar los traslados
  - Las cuentas del LM que son afectadas.
- Nivel organizativo clave: Almacén
- Los maestros de datos relevantes:
  - Maestro de materiales
  - La vista de datos centro/almacén

Slide solo texto.

## Slide 7

**Fig. 1: Movimientos de mercancías**

Diagrama de flujo con dos bloques principales, **Centro A** y **Centro B**, cada uno conteniendo sub-bloques de almacén con distintos estados de stock, conectados por flechas numeradas que representan los 4 tipos de movimiento:

- **Centro A** contiene el **Almacén A**, con tres estados de stock apilados verticalmente y conectados entre sí por flechas bidireccionales etiquetadas "Traspaso" (movimiento ④):
  - De libre utilización
  - En inspección de calidad
  - Bloqueado
- **Centro B** contiene dos almacenes:
  - **Almacén B**: "En tránsito" y "De libre utilización" (conectados por flecha "Traspaso" ④)
  - **Almacén C**: "De libre utilización"
  - Entre Almacén B y Almacén C hay una flecha "Traslado" (movimiento ③)

Flujo de entradas/salidas (izquierda a derecha):
- "Proceso de aprovisionamiento" → flecha "Entrada de mercancías" (①) → Almacén A "De libre utilización"
- "Proceso de producción" → flecha "Entrada de mercancías" (①) → Almacén A "En inspección de calidad"
- Entre Centro A y Centro B: flecha "Traslado" (③) que conecta "En inspección de calidad" de A con "En tránsito" de B
- Desde Centro B, "De libre utilización" (Alm. B) → flecha "Salida de mercancías" (②) → "Proceso de gestión de pedidos"
- Desde Centro B, "Alm. C - De libre utilización" → flecha "Salida de mercancías" (②) → "Proceso de producción"

Leyenda numérica implícita: ① = Entrada de mercancías, ② = Salida de mercancías, ③ = Traslado, ④ = Traspaso.

## Slide 8

**1) Entrada de mercancías (Goods Receipt)**

- Se traduce en un aumento del stock
- Puede tener lugar durante el proceso de producción
- Crea documentos de material y FI para ambos procesos Producción y IM-WM
- Se puede contabilizar entrada de mercancías sin una referencia a una orden
  - Primera entrada al stock
  - Entrada no planificada

Slide solo texto.

## Slide 9

**2) Salida de mercancías (Goods Issue)**

- Se traduce en una disminución del stock
- En el proceso de Gestión de Pedidos esto indica una salida de productos terminados hacia un cliente mediante un pedido de compra.
- En el proceso de Producción esto refleja la salida de materias primas o productos semielaborados mediante una orden de fabricación
- Puede ser no planificada
- Los materiales pueden ser retirados para un consumo interno

Slide solo texto.

## Slide 10

**3) Traslado (Stock Transfer)**

- Utilizado para mover **físicamente** material desde un nivel de organización o ubicación a otra.
- Un traslado puede involucrar movimientos bajo tres escenarios:
  - Entre almacenes en un centro
  - Entre centros en una sociedad
  - Entre centros en diferentes sociedades

Slide solo texto.

## Slide 11

**3) Traslado (cont.)**

- Existen tres procedimientos disponibles para mover los materiales:
  - Procedimiento de un paso
  - Procedimiento de dos pasos
  - Pedido de traslado de stock (Stock Transport Order)

Slide solo texto.

## Slide 12

**Fig. 7-2: Procedimiento de uno y dos pasos**

Diagrama con dos columnas: "Nivel organizativo de envío" (bloque azul con el rótulo "Stock") y "Nivel organizativo de recepción" (dos bloques: "En tránsito" arriba y "Stock" abajo).

- Ruta **"Un paso"**: flecha directa desde "Stock" (envío) hacia "Stock" (recepción), etiquetada con los pasos ① y ② juntos.
- Ruta **"Dos pasos"**: flecha ① desde "Stock" (envío) hacia "En tránsito" (recepción); luego flecha ② desde "En tránsito" hacia "Stock" (recepción).

Leyenda lateral "Pasos":
- ① Retira desde almacén (salida)
- ② Coloca en almacén (entrada)

## Slide 13

**Traslado de almacén a almacén**

- Traslado entre dos almacenes de un mismo centro.
- Razones de un traslado
  - almacenamiento temporal
  - control de calidad
- El traslado puede ser de uno o dos pasos:
  - Procedimiento de un paso: un material puede estar en cualquier status (ubicación de entrega) y cualquier estado en el centro de recepción)
  - Procedimiento de dos pasos: sólo es posible cuando los materiales en la ubicación de envío están en status de libre disposición

Incluye en la esquina inferior derecha una miniatura (thumbnail) de la Fig. 7-3 que se muestra completa en la slide siguiente (dos diagramas pequeños: "Procedimiento de un paso" y "Procedimiento de dos pasos").

## Slide 14

**Fig. 7-3: Opciones de traslado dentro de un centro**

Dos diagramas lado a lado, ambos dentro de "Centro A":

**Procedimiento de un paso** (izquierda): Almacén A con tres estados (De libre utilización, En inspección de calidad, Bloqueado) conectados mediante flechas cruzadas (todas las combinaciones posibles) hacia los mismos tres estados en Almacén B, cada flecha etiquetada con una clase de movimiento:
- De libre utilización → De libre utilización: **311**
- De libre utilización → En inspección de calidad: **321**
- En inspección de calidad → De libre utilización: **323** (cruzada)
- En inspección de calidad → En inspección de calidad: **323**
- Bloqueado → En inspección de calidad: **349**
- Bloqueado → Bloqueado: **325**

(Las flechas se cruzan entre los tres estados de Almacén A y Almacén B, indicando que cualquier estado origen puede ir a cualquier estado destino en un solo paso.)

**Procedimiento de dos pasos** (derecha): Almacén A "De libre utilización" → flecha **313** → Almacén B "Stock en tránsito" → flecha **315** → Almacén B "De libre utilización".

## Slide 15

**Traslado de almacén a almacén (cont.)**

- El traslado entre almacenes de un mismo centro no afecta la valoración del material (misma valorización)
  - No hay impacto financiero
  - No hay documento FI
- Si los materiales en el almacen no tienen la misma valorización
  - Hay impacto financiero
  - Hay documento FI
  - múltiples cuentas de material

Slide solo texto.

## Slide 16

**Traslado centro-a-centro**

- Movimientos de mercaderías entre dos centros dentro de una misma sociedad
- Se puede utilizar procedimientos de uno o dos pasos.
  - La diferencia está en el status del stock en el centro receptor ("libre utilización" en un paso y "en tránsito" en dos pasos
- Típicamente, sólo las mercaderías en status de libre utilización (disponibles) se pueden mover entre centros.
- Se crean documentos de material.
- Hay impacto financiero (documento FI)

Slide solo texto.

## Slide 17

**Fig. 7-4: Traslado de centro-a-centro**

Diagrama bajo el encabezado "Sociedad 1", con **Centro A** (Almacén A: "De libre utilización") y **Centro B** (Almacén B: "Stock en tránsito" y "De libre utilización").

- Ruta **"Un paso"**: flecha directa (clase de movimiento **301**) desde "De libre utilización" (Alm. A) hacia "De libre utilización" (Alm. B), marcada con pasos ① y ② juntos.
- Ruta **"Dos pasos"**: flecha ① (clase **303**) desde "De libre utilización" (Alm. A) hacia "Stock en tránsito" (Alm. B); luego flecha ② (clase **305**) desde "Stock en tránsito" hacia "De libre utilización" (Alm. B).

Leyenda lateral "Pasos": ① Retira desde el almacén (salida); ② Coloca en almacén (entrada).

## Slide 18

**Traslado sociedad-a-sociedad**

- Los movimientos de materiales entre dos centros de diferentes sociedades
- Se puede utilizar procedimiento de uno o dos pasos
- Se crean dos documentos FI, uno por cada sociedad
  - Una partida individual es para la cuenta de material
  - La otra es para la cuenta de compensación creada para registrar dicho traslado

Slide solo texto.

## Slide 19

**Pedido de traslado (Stock Transport Orders)**

- Movimientos de centro-a-centro tienen limitaciones
- En los pedidos de traslado (STO) un centro "compra" materiales y otro centro las "vende"
- Puede involucrar etapas de los procesos de Aprovisionamiento, Gestión de Pedidos y Gestión de Stocks.
- Existen 3 tipos de pedido de traslado
  - Pedido de traslado sin documento de entrega
  - Pedido de traslado con documento de entrega
  - Pedido de traslado con documento de entrega y facturación

Slide solo texto.

## Slide 20

**Pedido de traslado (STO) sin documento de entrega**

- Involucra etapas de aprovisionamiento y gestión de stocks
- Un STO se crea directamente o referencia a otro documento (SP)
- Sólo se puede utilizar el procedimiento de dos pasos
- Se crea un documento de material para registrar el movimiento
- Se pueden crear uno o dos documentos FI
- Cuentas del LM.
  - cuenta de material
  - cuenta de compensación

Slide solo texto.

## Slide 21

**Fig. 7-5: Pedido de traslado sin entrega**

Diagrama con dos columnas: **Centro suministrador ("vendedor")** y **Centro receptor ("comprador")**, con flujo vertical descendente en la columna receptora y una flecha horizontal cruzada:

- Centro receptor: "Necesidad de material" → flecha hacia atrás → "Pedido de traslado" (bloque central compartido entre ambas columnas)
- "Pedido de traslado" → flecha hacia abajo en el centro suministrador → "Salida de mercancías"
- "Salida de mercancías" (suministrador) → flecha horizontal → "Stock en tránsito" (receptor)
- "Stock en tránsito" → "Entrada de mercancías" → "De libre utilización" (cadena vertical descendente en el centro receptor)

## Slide 22

**Pedido de traslado con entrega**

- Se crea un documento de entrega (picking y embalaje) previo a la salida de mercancías.
- El pedido de traslado se trata igual que un pedido de cliente
- Se puede usar procedimiento de uno o dos pasos.
  - Procedimiento de un paso: se crea sólo un documento de material y los materiales se registran en status de libre utilización en el centro receptor.
  - Procedimiento de dos pasos: movimiento de materiales e impacto financiero se tratan idénticamente que un STO sin entrega

Slide solo texto.

## Slide 23

**Fig. 7-6: Pedido de traslado con entrega**

Diagrama con dos columnas, **Centro suministrador ("vendedor")** y **Centro receptor ("comprador")**:

- Centro receptor: "Necesidad de material" → "Pedido de traslado" (compartido)
- "Pedido de traslado" → "Crea entrega" (centro suministrador)
- "Crea entrega" → "Salida de mercancías" (flujo descendente en suministrador)
- "Salida de mercancías" → flecha horizontal → "Stock en tránsito" (receptor)
- "Stock en tránsito" → "Entrada de mercancías" → "De libre utilización" (cadena descendente en receptor)

(Igual que la Fig. 7-5 pero agrega el paso "Crea entrega" antes de la salida de mercancías.)

## Slide 24

**Pedido de traslado con entrega y facturación**

- Un STO incluye un documento de entrega (etapa de expedición) y la etapa de facturación desde el proceso de gestión de pedidos en el centro emisor
- Un STO incluye la etapa de verificación de factura desde el proceso de aprovisionamiento en el centro receptor.
- Se incluye un precio de compra en el STO basado en las condiciones de precio y registros info.
- El centro suministrador crea un documento de entrega autorizando el envío.
- Una salida de mercancías se contabiliza en el centro suministrador.
- Una entrada de mercancías se contabiliza en el centro receptor.

Slide solo texto.

## Slide 25

**Fig. 7-7: Pedido de traslado con entrega y facturación**

Diagrama con dos columnas, **Centro suministrador ("vendedor")** y **Centro receptor ("comprador")**:

- Centro receptor: "Necesidad de material" → "Pedido de traslado" (compartido)
- "Pedido de traslado" → "Crea entrega" (suministrador)
- "Crea entrega" → "Salida de mercancías" (descendente en suministrador)
- "Salida de mercancías" → flecha horizontal → "Stock en tránsito" (receptor)
- "Stock en tránsito" → "Entrada de mercancías" → "De libre utilización" (descendente en receptor)
- Adicionalmente: "Salida de mercancías" → flecha descendente → "Facturación" (suministrador)
- "Facturación" → flecha horizontal → "Verificación factura" (receptor)

(Extiende la Fig. 7-6 agregando el bloque de facturación/verificación de factura al final del flujo, en paralelo con la rama física de mercancías.)

## Slide 26

**Ventajas de utilizar un STO (Pedido de Traslado) para mover materiales entre Centros**

- Cuando se crea un STO, la empresa puede llevar a cabo una **verificación de disponibilidad** para evaluar la disponibilidad de material en el centro suministrador.
- Se pueden **agregar al STO los costos de la entrega** y de la empresa de transporte seleccionada.
- Se pueden **incluir en la planeación de materiales** de los dos centros las cantidades en el STO, las entregas y entradas planificadas.
- Las solicitudes de pedido se pueden convertir en STOs en vez de PCs.
- Se puede **monitorear el historial** de distintas tareas asociadas con el STO vía la sección historial de pedido del STO.

Slide solo texto (frases clave resaltadas en negrita en el original).

## Slide 27

**Fig. 1: Movimientos de mercancías**

Repetición exacta del diagrama de la Slide 7 (mismo contenido: Centro A / Centro B, almacenes A/B/C con estados de stock, flechas numeradas ①-④ de Entrada de mercancías, Salida de mercancías, Traslado y Traspaso). Se reutiliza aquí como transición hacia el último movimiento (Traspaso).

## Slide 28

**4) Traspaso (Transfer Posting)**

- Se utiliza para cambiar el estado o tipo de material en stock.
- Los cuatro estados típicos son:
  - De libre utilización
  - En inspección de calidad
  - Bloqueado
  - En tránsito
- Se puede utilizar en otras situaciones que no necesariamente involucre un movimiento físico de material.

Slide solo texto (cierre del capítulo, sin pie de página de créditos visible).
