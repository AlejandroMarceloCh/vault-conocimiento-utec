---
curso: SIOPS
titulo: Procesos de Gestión de Stocks y Almacenes - 4. Proceso de Gestión de Almacenes
slides: 17
fuente: Procesos de Gestión de Stocks y Almacenes - 4. Proceso de Gestión de Almacenes.pdf
---

## Slide 1

Portada (decorativa: banda naranja/rosa/gris, fondo rayado). Título: "Proceso de Gestión de Stocks y Almacenes". Autor: Prof. Carlos Villanueva Q. Créditos: Magal and Word | Integrated Business Processes with ERP Systems | © 2012. Traducido por Grandón, Pinto y Soto (2017), adaptado para UTEC por Juan Carlos Bueno.

## Slide 2

**Objetivos de aprendizaje**

1. Identificar y explicar las etapas claves en el proceso de gestión de almacenes.

Slide de solo texto, sin elementos visuales adicionales.

## Slide 3

Slide separadora/título de sección (decorativa, texto centrado sobre fondo blanco): "Proceso de Gestión de Almacenes (WM)". Sin contenido adicional.

## Slide 4

**Proceso de Gestión de Almacenes (WM)**

- El proceso de Gestión de Almacenes se desencadena normalmente por movimientos de mercancías en otros procesos tales como:
  - Aprovisionamiento
  - Gestión de Pedidos
  - Producción
  - Gestión de stocks
- Una **necesidad de transporte** se usa para planificar el movimiento de materiales hacia y desde las ubicaciones en un número de almacén.
- El movimiento de mercancías se acompaña con una **orden de transporte.**

Slide de solo texto (bullets), sin diagrama.

## Slide 5

**Fig. 7-18 Proceso de gestión de almacenes**

Diagrama de flujo de proceso en 5 etapas conectadas por flechas horizontales, dentro de un recuadro delimitador:

`(Desencadenantes) → [Planificación de movimiento] → [Ejecución de movimiento] → [Traslado de materiales] → [Confirmación de movimiento] → (Fin)`

- **Desencadenantes** (círculo naranja): Aprovisionamiento, Gestión de pedidos, Producción, Gestión de stocks
- **Planificación de movimiento**: Necesidad de transporte, Documento de entrega
- **Ejecución de movimiento**: Orden de transporte
- **Traslado de materiales** (sin sub-ítems)
- **Confirmación de movimiento**: Orden de transporte
- **Fin** (círculo azul)

Debajo del recuadro, conectados por flechas verticales:
- **Entrada de usuario** (flecha hacia arriba, hacia el bloque de Planificación)
- **Datos maestros / Datos de transacción** (cilindro de base de datos, flecha bidireccional hacia el proceso), que a su vez alimenta con una flecha lateral a un grupo de documentos de salida apilados: **Documentos FI**, **Documentos CO**, **Documentos de material**, **Documentos de transacción**.

## Slide 6

**Planificación de movimiento de almacén**

- Una **necesidad de transporte (NT)** se genera automáticamente cuando el movimiento de materiales involucra un almacén gestionado
- Una necesidad de transporte se crea manualmente para facilitar los movimientos internos de material
- Una **instrucción de traspaso** se usa para cambiar el status del material
- Origen de necesidad de movimiento de materiales en el almacén:
  - Documento de material
  - Documento de entrega
  - Orden de fabricación
- No hay impacto financiero

Slide de solo texto (bullets), sin diagrama.

## Slide 7

**Fig. 7-19: Elementos de la etapa de planificación de movimiento de almacén**

Diagrama de 4 cajas azules en secuencia horizontal conectadas por flechas, cada una con su lista de sub-elementos:

| Desencadenantes | Datos | Tareas | Salidas |
|---|---|---|---|
| Actividad gestión de stocks; Necesidad interna | Datos organizativos; Datos maestros; Entrada de usuario | Crear necesidad de transporte; Crear instrucción de traspaso | Necesidad de transporte; Instrucción de traspaso |

## Slide 8

**Fig. 7-20: Datos en una necesidad de transporte**

Diagrama de flujo: tres cajas de categorías de datos convergen (flechas hacia abajo/diagonales) en un círculo central "Necesidad de transporte":

- **Datos maestros**: Maestro de materiales; Ubicación
- **Datos organizativos**: Mandante; Sociedad; Centro; Almacén; Número de almacén
- **Datos de transacción**: Número de material; Cantidad; Fecha de transporte; Clase de transporte; Origen de necesidad

Las tres cajas apuntan con flechas hacia el círculo central "Necesidad de transporte".

## Slide 9

**Fig. 7-21: Documentos de referencia para una necesidad de transporte**

Diagrama: tres cajas de origen (apiladas verticalmente) conectadas mediante líneas que convergen en una flecha hacia una caja de destino:

- Documento de material →
- Orden de fabricación →  } → **Necesidad de transporte**
- Sin documento de origen →

## Slide 10

**Ejecución de movimiento de almacén**

- Movimientos comunes en el almacén:
  - Picking
  - Entrada en stock
  - Traspasos
- Una **orden de transporte** se utiliza para ejecutar estos movimientos de almacén.
- Una orden de transporte se puede crear directamente desde una necesidad de transporte o por una instrucción de traspaso
- Una orden de transporte también se puede crear manualmente para facilitar transportes internos en el almacén
- Una orden de transporte consiste en una cabecera y una o mas posiciones
- No hay impacto financiero

Slide de solo texto (bullets), sin diagrama.

## Slide 11

**Fig. 7-22: Elementos de la etapa de ejecución de movimiento de almacén**

Diagrama de 4 cajas azules en secuencia horizontal conectadas por flechas:

| Desencadenantes | Datos | Tareas | Salidas |
|---|---|---|---|
| Necesidad de transporte; Necesidad interna de traslado de almacén; Documento de entrega | Datos organizativos; Datos maestros; Entrada de usuario | Crear orden de transporte | Orden de transporte; Necesidad de transporte actualizada |

## Slide 12

**Fig. 7-23: Datos de una orden de transporte**

Diagrama de flujo: cuatro cajas de categorías de datos convergen (flechas diagonales) en un círculo central "Orden de transporte":

- **Datos organizativos**: Mandante; Sociedad; Centro; Almacén; Número de almacén
- **Datos de transacción**: Documento de origen; Ubicación de origen; Ubicación de destino
- **Datos maestros**: Maestro de materiales; Ubicación
- **Entrada de usuario**: Número de documento de origen; Número de ubicación de destino

Las cuatro cajas apuntan con flechas hacia el círculo central "Orden de transporte".

## Slide 13

**Fig. 7-24: Estructura de una orden de transporte**

Diagrama de dos cajas paralelas lado a lado (sin flechas entre ellas, muestran la composición de la orden de transporte):

- **Cabecera**: Número de OT; Número de documento de referencia; Fechas; Clase de movimiento de almacén
- **Posición**: Número de material; Centro/almacén; Tipo de almacén, ubicación y cuanto de origen; Tipo de almacén, ubicación y cuanto de destino; Cantidad objetivo; Cantidad real

## Slide 14

**Fig. 7-25: Documentos de referencia para una orden de transporte**

Diagrama: cinco cajas de origen apiladas verticalmente, todas conectadas mediante líneas que convergen en una flecha hacia una caja de destino única:

- Necesidad de transporte
- Instrucción de traspaso
- Documento de material → **Orden de transporte**
- Documento de entrega
- Sin documento de origen

## Slide 15

**Confirmación movimiento de almacén**

- La orden de transporte autoriza a los empleados del almacén mover físicamente los materiales desde las ubicaciones de origen a las ubicaciones de destino
  - Cuando los materiales han sido movidos, el movimiento se confirma
  - La misma orden de transporte creada para autorizar el movimiento físico de materiales se usa para la confirmación
  - El Sistema ERP automáticamente actualiza los documentos de referencia asociados:
    - Documento de entrega
    - Necesidad de transporte
    - Instrucción de traspaso

Slide de solo texto (bullets), sin diagrama.

## Slide 16

**Fig. 7-26: Elementos de la etapa de confirmación de movimiento de almacén**

Diagrama de 4 cajas azules en secuencia horizontal conectadas por flechas:

| Desencadenantes | Datos | Tareas | Salidas |
|---|---|---|---|
| Transporte de materiales finalizado | Datos organizativos; Datos maestros; Entrada de usuario | Actualizar orden de transporte | Orden de transporte actualizada; Documentos de origen actualizados |

## Slide 17

**Orden de contabilizaciones en WM e IM**

- El orden de la contabilización en la gestión de almacenes y stocks mediante la cual se realizan de las actividades de gestión de almacenes y stocks puede variar de un escenario a otro.
  - La salida de mercancías en IM por un pedido de cliente u orden de fabricación se contabiliza antes que se registren las actividades de WM.
  - Se realiza la entrada en stock de WM antes que se registre la entrada de mercancías de IM

Slide de solo texto (bullets), sin diagrama. Nota: el pie de página de esta slide indica © 2011 (a diferencia del resto del capítulo que indica © 2012), consistente con el texto extraído.
