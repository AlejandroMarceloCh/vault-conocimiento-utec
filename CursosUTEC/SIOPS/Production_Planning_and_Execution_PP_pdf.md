---
curso: SIOPS
titulo: Production Planning and Execution - PP
slides: 6
fuente: Production Planning and Execution - PP.pdf
---

## Slide 1

**Título:** Proceso de Producción Básico

Diagrama de flujo horizontal con 5 pasos alternando roles Almacén/Producción, cada uno con un icono (persona + caja para Almacén, persona + engranajes para Producción), unidos por flechas:

1. **Almacén** — Solicita producción
2. **Producción** — Autoriza producción
3. **Almacén** — Salida de materias primas
4. **Producción** — Crea producto
5. **Almacén** — Recibe productos terminados

## Slide 2

**Título:** Proceso de Producción Básico

Slide de solo texto (lista con viñetas), sin diagrama:

- Listas de Materiales (LMat)
- Puesto de Trabajo
- Hojas de ruta de productos
- Maestro de materiales
- Medios auxiliares de fabricación (MAF)

Pie de página: "Magal and Word | Integrated Business Processes with ERP Systems | © 2012. Traducido por Grandón, Pinto y Soto (2017)" — decorativa/crédito.

## Slide 3

**Título:** Production Planning & Execution

Diagrama de flujo de proceso end-to-end con iconos estilo clip-art (personas, documentos, cajas apiladas), organizado en dos filas:

- Fila superior (procesos, forma de flecha/chevron): **Sales and Operations Planning** → **Demand Management** → **Materials Requirements Planning**, encabezados por un icono de "Operational Management" (persona guiando a un grupo).
- Desde "Materials Requirements Planning" el flujo se bifurca en dos ramas paralelas que confluyen en un icono de **Inventory** (cajas apiladas):
  - Rama superior: **Procurement Process** (3 chevrons) → Inventory
  - Rama inferior: **Production Process** (3 chevrons) → Inventory
- De Inventory sale una flecha hacia **Fulfillment Process** (3 chevrons finales).
- Fila inferior (documentos, iconos de hoja con esquina doblada) debajo de los 3 procesos iniciales: **Operations Plan**, **Requirements**, **Procurement Proposals** — representan las salidas documentales de cada etapa.

Pie de página igual al de la slide 2 (decorativo).

## Slide 4

**Título:** Production Planning & Execution

Layout de dos columnas: texto a la izquierda, diagrama de bloques a la derecha.

**Texto (izquierda) — "Players in the Game":**
- Strategic Planning
  - CEO, COO, CIO, CFO, Controller, Marketing Director
- Detailed Planning
  - Line Managers, Production Scheduler, MRP Controller, Capacity Planners
- Execution
  - Line Workers, Shop Floor Supervisors

**Diagrama (derecha):** flujo vertical de arriba hacia abajo, agrupado en 3 franjas grises con etiqueta lateral:

- **Strategic Planning** (franja gris superior): dos hexágonos grises "SIS" y "CO/PA" apuntan ambos hacia un bloque azul central "Forecasting"; de Forecasting baja una flecha a "Sales & Operations Planning" (bloque azul).
- Fuera de las franjas, entre Strategic y Detailed Planning: bloque verde claro "Demand Management".
- **Detailed Planning** (franja gris media): bloque dorado "MPS" → flecha hacia abajo → bloque dorado "MRP".
- Desde "MRP" el flujo se bifurca en dos flechas hacia la franja inferior.
- **Manufacturing Execution** (franja gris inferior): a la izquierda dos óvalos amarillos apilados "Manufacturing Execution" → "Order Settlement" (conectados por flecha); a la derecha un óvalo gris "Procurement Process".

## Slide 5

**Título:** Production Planning and Execution (PP) – Case Study

**Learning Objective:** Understand and perform a manufacturing process cycle.

Diagrama de "swimlane" (carriles) con dos filas de bloques diagonales (paralelogramos tipo flecha inclinada) representando pasos de un proceso SAP, organizados en carriles por módulo (**PP**, **MM**, **CO**), coloreados según el módulo que ejecuta cada paso (azul=PP, dorado=MM, verde=CO):

**Bloque superior (Planificación):**
PP: Change Material Master Record → Change Routing → Display Product Group → Create Sales and Operations Plan → Transfer SOP to Demand Management → Review Demand Management → Run MPS with MRP → Review Stock/Requirements List
(carriles MM y CO vacíos en este bloque, solo líneas punteadas indicando el paso a través de ellos)

**Bloque inferior (Ejecución):**
PP: Convert Planned Order into Production Order
MM: Receive Goods in Inventory → Issue Goods to Production Order
PP: Review Production Order Status and Documents → Confirm Production Completion
MM: Receive Goods from Production Order
CO: Review Costs Assigned to Production Order → Settle Costs of Production Order

Los pasos están conectados secuencialmente de izquierda a derecha, cruzando entre carriles según qué rol/módulo ejecuta cada actividad.

## Slide 6

Slide en blanco / vacía (sin contenido visible en la imagen ni en el texto extraído). Posible slide de transición o error de renderizado del PDF.
