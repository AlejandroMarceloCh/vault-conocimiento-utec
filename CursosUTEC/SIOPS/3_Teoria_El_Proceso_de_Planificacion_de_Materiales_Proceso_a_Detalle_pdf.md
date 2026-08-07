---
curso: SIOPS
titulo: 3. Teoria - El Proceso de Planificación de Materiales (Proceso a Detalle)
slides: 38
fuente: 3. Teoria - El Proceso de Planificación de Materiales (Proceso a Detalle).pdf
---

## Slide 1

Portada (decorativa: logo/plantilla UTEC). Título: "Proceso de Planificación de Materiales (Proceso a Detalle)". Profesor: Carlos Villanueva Q. Crédito: Adaptado de Magal and Word | Integrated Business Processes with ERP Systems © 2011, traducido por Grandón, Pinto y Soto (2017).

## Slide 2

Objetivos de Aprendizaje:
1. Describir las etapas del proceso de Planificación de Materiales.
2. Identificar etapas del proceso en el Sistema empresarial (S/4 HANA).

## Slide 3

Diagrama de flujo general del "Proceso de planificación de materiales" (imagen central, se repite como referencia en varias slides posteriores con círculo rojo resaltando la etapa activa). Estructura del diagrama:
- Fila superior (dentro de un recuadro celeste grande), 4 cajas azules conectadas con flechas en secuencia:
  1. **Sales and operations planning**: Sales plan, Operations plan (production plan for product group)
  2. **Disaggregation**: Sales plan, Operations plan (PIR for materials)
  3. **Demand management**: PIR, CIR, PIR (revised)
  4. **Materials requirements planning**: Planned orders, Purchase requisitions → flecha hacia un círculo "End"
- Debajo, un círculo "Triggers" (Periodic requirement, External events) alimenta con flecha ascendente a la primera caja (Sales and operations planning) y también hacia Disaggregation.
- Debajo del recuadro celeste: "User input" (paralelogramo) y un cilindro de base de datos "Master data / Transaction data" que se conecta con "Transaction documents" (documento con forma de nube/onda). Ambos alimentan con flechas ascendentes las cajas del proceso.

## Slide 4

Slide de texto "Introducción":
- SOP: herramienta de planeamiento y pronóstico que las empresas utilizan para generar un pronóstico de ventas, determinar requerimientos de inventario y generar un Plan de Operaciones (preliminar).
- SOP crea un Plan de Producción al nivel de Product Group.
- Disaggregation: Los requerimientos de SOP se traducen en PIRs para ese Product Group.
- Los PIRs se transfieren a Demand Management donde se afinan.
- MRP crea propuestas de aprovisionamiento para asegurar los materiales necesarios para el proceso productivo.

## Slide 5

Repite el diagrama de flujo de la Slide 3, con la etapa **"Sales and operations planning"** resaltada con un círculo/óvalo rojo grueso (indicando que es la etapa que se va a detallar a continuación).

## Slide 6

Título: SALES AND OPERATIONS PLANNING. Miniatura del diagrama general en la esquina superior derecha (con SOP resaltado en rojo). Diagrama principal: secuencia de 4 cajas azules conectadas por flechas, "Elementos de la etapa SOP":
- **Triggers**: Periodic planning need, Events affecting demand
- **Data**: Organizational data, Master data, Transaction data, User input, Sales plan
- **Tasks**: Create/import sales plan, Generate production plan, Evaluate feasibility
- **Outcomes**: Operations plan (production plan)

## Slide 7

SALES AND OPERATIONS PLANNING → Triggers:
- SOP se ejecuta periódicamente para revisar el Plan de Producción.
- Cambios en el entorno económico.
- Tipos: SOP standard, SOP flexible.
- Standard planning usa modelos o plantillas de planeamiento predefinidas.
- Flexible Planning usa modelos más complejos que descienden hasta calcular cantidades para cada centro.

## Slide 8

SALES AND OPERATIONS PLANNING → Data. Diagrama con un círculo central "Operations plan (production plan)" alimentado por flechas desde 5 cajas azules alrededor:
- **Master data**: Material master, Product groups
- **Transaction data**: Historical sales data
- **Other processes**: Profitability analysis, Inventory and warehouse management
- **Organizational data**: Sales organization, Distribution channel, Plant
- **User input**: Verify data, Sales plan, Planning assumptions and parameters

## Slide 9

SALES AND OPERATIONS PLANNING → Tasks:
- Crear Plan de Ventas
- Definir requerimientos de inventario
- Crear un Plan de Producción

## Slide 10

Tabla "Standard SOP Planning Table" (captura de tabla del sistema SAP):

| | M01 | M02 | M03 | M04 | M05 |
|---|---|---|---|---|---|
| Sales | 100 | 110 | 130 | 140 | 140 |
| Production | 100 | 110 | 150 | 132 | 128 |
| Stock level | | | 20 | 12 | |
| Target stock | | | 20 | 12 | |
| Day's supply | | | 3 | 1 | |
| Target day's supply | | | | | |

Encabezado: Product group = PG-BIKE000, Plant = DL00, Version = A00 (Active version, con nota "Planning in multiple version possible"). Anotaciones: flecha hacia fila Sales indica "Forecasts can be transferred"; flecha hacia fila Production indica "Production plan can be created sychronous to sales, according to target day's supply or target stock level".

## Slide 11

SALES AND OPERATIONS PLANNING (continuación de la tabla del slide anterior, mostrada en miniatura arriba a la derecha):
- Sales: Plan de ventas
- Production: Plan de Producción calculado por el sistema.
- Stock level: Niveles de inventario generados por el sistema.
- Target stock: Niveles de stock deseados. Ingresado por usuario (subrayado).
- Day's supply: # días que la empresa espera cubrir ventas solo con el inventario existente. Lo calcula el sistema.
- Target day's supply: El usuario ingresa el day's supply en esta fila (subrayado).

## Slide 12

Fila "Sales" de la tabla (100/110/130/140/140) mostrada arriba como referencia. Texto:
- Esta fila contiene el plan de ventas.
- Posible origen de esta data: Niveles deseados de rentabilidad provenientes de management accounting; Data histórica del SIS (Sales Information System); Un forecast basado en el histórico de ventas; Ingreso manual de empleados experimentados; Plantilla del plan usado para otro Product Group.

## Slide 13

Fila "Production" de la tabla (100/110/150/132/128) mostrada arriba como referencia. Texto — El sistema genera un plan de producción basado en una de estas opciones:
- Synchronous to Sales: El sistema copia cantidades de la fila plan de ventas.
- Target stock level: La empresa especifica un nivel de stock deseado que se considera en el plan, además del plan de ventas.
- Target day's supply: Similar al anterior, pero el nivel de inventario deseado se expresa en un número de días y no en cantidades.
- Stock level = 0: El nivel de stock deseado al final de cada periodo es cero.

## Slide 14

"Ejemplo de SOP para GBI" — combina dos tablas y dos recuadros de cálculo:

Tabla superior izquierda (antes de calcular producción):
| | M01 | M02 | M03 | M04 |
|---|---|---|---|---|
| Sales | 1000 | 1200 | 1000 | 900 |
| Production | | | | |
| Stock level | | | | |
| Target stock | 100 | 200 | 100 | 50 |
| Day's supply | | | | |
| Target day's supply | | | | |

Recuadro derecho "Cálculo de Producción para el tercer mes (M03)":
```
Sales                1,000 units
Target stock      +    100 units
Previous inventory -   200 units
Production            900 units
```

Tabla inferior izquierda (resultado, con Production y Day's supply ya calculados):
| | M01 | M02 | M03 | M04 |
|---|---|---|---|---|
| Sales | 1000 | 1200 | 1000 | 900 |
| Production | 1100 | 1300 | 900 | 850 |
| Stock level | 100 | 200 | 100 | 50 |
| Target stock | 100 | 200 | 100 | 50 |
| Day's supply | 3 | 5 | 3 | 1 |
| Target day's supply | | | | |

Recuadro derecho "Ejemplo de cálculo del Day's Supply – segundo mes (M02)":
$$\text{Day's supply} = \frac{\text{Target stock}}{\text{Daily requirements}} = \frac{200\ \text{units}}{(1{,}200\ \text{units} / 30\ \text{working days})} = 5\ \text{Day's supply}$$

## Slide 15

SALES AND OPERATIONS PLANNING → Outcomes:
- La salida del SOP es una o más versiones del plan de producción.
- No se genera impacto financiero ni movimiento de materiales.

## Slide 16

Repite el diagrama de flujo general (igual al de la Slide 3), ahora con la etapa **"Disaggregation"** resaltada con círculo rojo.

## Slide 17

Título: DISAGGREGATION. Miniatura del diagrama general arriba a la derecha (con Disaggregation resaltado). Texto:
- El Plan de Ventas y Producción creado en SOP (a nivel de Product Group) se traduce en planes para los productos terminados que conforman el árbol jerárquico del grupo.

Diagrama de 4 cajas en secuencia:
- **Triggers**: New operations plan (production plan)
- **Data**: Organizational data, Master data, User input, Sales and operations plan
- **Tasks**: Disaggregate operations plan, Transfer to demand management
- **Outcomes**: Planned independent requirements (PIR)

## Slide 18

DISAGGREGATION → Data. Diagrama con círculo central "Planned independent requirements (PIR)" alimentado por 3 cajas:
- **Master data**: Product groups, Proportion factors
- **Operations plan**: Sales plan, Production plan, Stock levels
- **User input**: Disaggregation parameters

Texto:
- El sistema utiliza los proportion factors del Product Group para calcular los valores desagregados para cada elemento del Product Group.
- La salida de este paso es el cálculo de PIRs para cada periodo (semana o mes).

## Slide 19

DISAGGREGATION — Diagrama jerárquico "Disaggregation para el Grupo de Producto PG-BIKE000" (árbol de desagregación proporcional):

```
PG-BIKE000 Bicycles — Total production = 1100 units
├── PG-TOUR000 Touring 60% → 0.60×1100=660
│   ├── PG-DXTR000 Deluxe 70% → 0.70×660=462
│   │   ├── DXTR1000 Black (40%) → 0.40×462=184*
│   │   ├── DXTR2000 Silver (30%) → 0.30×462=139*
│   │   └── DXTR3000 Red (30%) → 0.30×462=139*
│   └── PG-PRTR000 Professional 30% → 0.30×660=198
│       ├── PRTR1000 Black (40%) → 0.40×198=79*
│       ├── PRTR2000 Silver (30%) → 0.30×198=59*
│       └── PRTR3000 Red (30%) → 0.30×198=60*
└── PG-ORBK000 Off-Road 40% → 0.40×1100=440
    ├── ORMN1000 Men's (65%) → 0.65×440=286
    └── ORWN1000 Women's (35%) → 0.35×440=154
```
Nota al pie: "*: Rounded to ensure that totals are correct".

## Slide 20

DISAGGREGATION — Diagrama "Transferencia de PIRs a Demand Management". Dos recuadros apilados:

Recuadro superior "Demand planning data": "Planning data at product group level" apunta a caja "Product Group PG-DXTR000". Abajo, flecha "Disaggregation" desciende a "Planning data at material level" que se reparte en 3 cajas con porcentajes: Material DXTR1000 (40%), Material DXTR2000 (30%), Material DXTR3000 (30%).

Las 3 cajas de material bajan con flechas gruesas a través de una barra "Transfer to Demand Management" hacia el recuadro inferior "Operative planning data", que contiene la caja "Planned independent requirements (at material-plant level) in demand management".

## Slide 21

Repite el diagrama de flujo general, ahora con la etapa **"Demand management"** resaltada con círculo rojo.

## Slide 22

Título: DEMAND MANAGEMENT. Miniatura del diagrama general arriba a la derecha (Demand management resaltado). Texto:
- Calcula los revised PIRs, considerando PIRs del SOP (después del disaggregation), CIRs y data del Material Master respecto a estrategias de planeamiento (vistas MRP).

Diagrama de 4 cajas en secuencia:
- **Triggers**: Changes in PIR (from SOP after disaggregation)
- **Data**: Organizational data, Master data, Transaction data, User input, PIR, CIR
- **Tasks**: Create revised PIRs
- **Outcomes**: Revised PIRs

## Slide 23

DEMAND MANAGEMENT → Data. Diagrama con círculo central "Revised PIRs" alimentado por 4 cajas:
- **Master data**: Material master
- **Transaction data**: CIRs, MRP elements
- **Organizational data**: Plant, Storage location
- **SOP**: PIRs

## Slide 24

DEMAND MANAGEMENT → Outcomes:
- PIRs para cada material incluido en el planeamiento, incluyendo cantidades y fechas específicas.
- No implica movimientos financieros ni de materiales.

## Slide 25

Repite el diagrama de flujo general, ahora con la etapa **"Materials requirements planning"** resaltada con círculo rojo.

## Slide 26

Título: MATERIAL REQUIREMENTS PLANNING. Miniatura del diagrama general arriba a la derecha (MRP resaltado). Texto:
- Calcula el net requirements para materiales y crea propuestas de compra o producción de materiales para todos los niveles del LMat (BOM).

Diagrama de 4 cajas en secuencia:
- **Triggers**: Changes to MRP elements
- **Data**: Master data, Transaction data, MRP elements, User input
- **Tasks**: Calculate net requirements, Monitor exceptions, Adjust schedules
- **Outcomes**: Purchase requisitions, Planned orders, Dependent requirements

## Slide 27

MATERIAL REQUIREMENTS PLANNING (texto, sin imagen adicional relevante):
- El MRP Controller es responsable del monitoreo de resultados del proceso de planeamiento. Las órdenes planificadas deben convertirse en órdenes de producción o solicitudes de compra. Las órdenes de producción deben liberarse, podrían necesitar reagendarse debido a problemas de scheduling o capacidad, etc.
- MRP se puede ejecutar de forma selectiva.
- MPS es un MRP especializado.

## Slide 28

MATERIAL REQUIREMENTS PLANNING — "Procedimiento MRP". Diagrama de 6 cajas en secuencia horizontal, con una flecha punteada gris que regresa desde la última caja hacia la primera (indicando ciclo/iteración):

Check planning file → Calculate net requirements → Determine lot size → Perform scheduling → Determine procurement proposals → Determine dependent requirements (y de vuelta, punteado, a Check planning file)

## Slide 29

MATERIAL REQUIREMENTS PLANNING → "Check Planning File" (primera caja del diagrama de 6 pasos resaltada en rojo, cadena completa mostrada arriba). Texto:
- Primera tarea: determinar materiales a planificarse.
- Cualquier cambio a un material relevante al MRP, se registra en este archivo.
- Cambios relevantes pueden ser: scheduling times en material master o elementos MRP (niveles de inventario, solicitudes u órdenes de compra).

## Slide 30

MATERIAL REQUIREMENTS PLANNING → "Calculate Net Requirements" (segunda caja resaltada en rojo, cadena completa mostrada arriba). Texto:
- Identifica faltas de material y genera propuestas de aprovisionamiento.
- El método de cálculo depende del MRP Type indicado en el material master.
- Si el MRP Type es MRP ó MPS, el cálculo es motivado por la existencia de un requerimiento dependiente o independiente.
- Para cada requerimiento, calcula si hay material suficiente. Si el resultado es negativo se genera una propuesta de aprovisionamiento.

Fórmula (destacada en negrita/cursiva):
$$\text{Available stock} = \text{Plant stock} - \text{Safety stock} + \text{Receipts}^1 - \text{Issues}^2$$

Notas al pie:
1. Good Receipts: Purchase Orders, firmed purchased requisitions, firmed planned orders, production orders.
2. Good Issues: CIRs, PIRs, material reservations.

## Slide 31

MATERIAL REQUIREMENTS PLANNING → "Determine Lot Size" (tercera caja resaltada en rojo, cadena completa mostrada arriba). Texto:
- Este # lo define el Lot Size Key del maestro de materiales.

## Slide 32

MATERIAL REQUIREMENTS PLANNING → "Perform Scheduling" (cuarta caja resaltada en rojo, cadena completa mostrada arriba). Texto:
- Lo hace a través del forward scheduling y backward scheduling.

## Slide 33

MATERIAL REQUIREMENTS PLANNING → "Determine Procurement Proposals" (quinta caja resaltada en rojo, cadena completa mostrada arriba). Texto:
- Se determina el tipo de propuesta de aprovisionamiento a generar.

Diagrama con dos columnas "In-house (internal) procurement" y "External procurement":
- In-house: MRP material A → Planned order → Convert → (flecha ancha hacia) Production order.
- External: MRP material A → dos ramas: (a) "Directly possible only with materials that are externally procured" → Purchase requisition o Schedule lines; (b) Convert → Purchase requisition → Purchase order.
- La caja "Convert" central conecta hacia Production order (izquierda, in-house) y hacia Purchase requisition (derecha, external) mediante una flecha ancha bidireccional.

## Slide 34

MATERIAL REQUIREMENTS PLANNING → "Determine Dependent Requirements" (sexta caja resaltada en rojo, cadena completa mostrada arriba). Texto:
- Para materiales producidos in-house, MRP genera requerimientos dependientes para cada material vía el BOM explosion.

Diagrama de explosión de BOM en niveles (con etiquetas "Single-item, multilevel planning" a la izquierda y "Single-item, single-level planning" a la derecha):
```
Sales order, planned independent requirements
        ↓
   MRP Finished good
        ↓
     Planned order
     ↙          ↘
Dependent      Dependent
requirements   requirements
   ↓                ↓
MRP              MRP
Semifinished good  Raw material
   ↓                ↓
Planned order    Purchase requisitions
   ↓
Dependent requirements
   ↓
MRP Semifinished good
```

## Slide 35

MATERIAL REQUIREMENTS PLANNING — Repite el árbol de desagregación PG-BIKE000 (igual al de la Slide 19), con el texto:
- El sistema crea PIRs para 8 materiales.

(Mismo diagrama jerárquico: PG-BIKE000 → Touring 60%/Off-Road 40% → Deluxe 70%/Professional 30% → colores Black/Silver/Red 40/30/30%, y rama Off-Road → Men's 65%/Women's 35%, con cifras absolutas calculadas: 660, 440, 462, 198, 184, 139, 139, 79, 59, 60, 286, 154).

## Slide 36

MATERIAL REQUIREMENTS PLANNING — Texto: "El Processing Key determina cómo se completan los pasos del MRP."

Diagrama de árbol de BOM (Bill of Materials) del producto "Off-road bike": la caja raíz "Off-road bike" se descompone en 10 componentes de primer nivel: ORWA1000 Off-road aluminum wheel assembly (2), OFFR1000/OFFR2000 Frame, EDGAM1000 Derailleur gear assembly, ORSK1000 Off-road seat kit, ORHB1000 Off-road handle bar, PEDL1000 Pedal assembly, CHAN1000 Chain, BRKT1000 Brake kit, WDOC1000 Warranty document, PCKG1000 Packaging. El componente "ORWA1000" se desagrega a su vez en: ORTR1000 Off-road tire, ORTB1000 Off-road tube, ORWH1000 Off-road aluminum wheel.

Recuadro de texto inferior "Off-road bikes":
- Off-road bikes are available in two models — men's (ORMN1000) and women's (ORWN1000).
- Men's bikes use a men's frame (OFFR1000) and women's bikes use a women's frame (OFFR2000).
- Both men's and women's bikes use off-road wheel aluminum assemblies (ORWA1000) which use off-road aluminum wheels.

## Slide 37

MATERIAL REQUIREMENTS PLANNING (solo texto). "Existen parámetros de control que determinan cómo se completan los pasos en el MRP":
- El parámetro Processing Key determina cómo se procesan los materiales del Planning File. Hay 3 Processing Keys:
- Regenerative planning (NEUPL): Planifican todos los materiales relevantes a MRP, se descarta data de planificaciones previas (Very time consuming). Poco usado.
- Net change planning (NETCH): Se planifican solo aquellos materiales que han tenido un cambio MRP relevante (cualquier actividad que afecta la disponibilidad del material).
- Net change planning in the planning horizon (NETPL): Se planifican solo aquellos materiales que han tenido un cambio MRP relevante dentro de un periodo de tiempo específico denominado planning horizon.

## Slide 38

MATERIAL REQUIREMENTS PLANNING (solo texto). "Existen parámetros de control adicionales que determinan la salida del procedimiento MRP":
- Create purchase requisitions: determina si MRP (1) siempre crea solicitudes de compra, (2) crea órdenes planificadas, ó (3) crea solicitudes de compra en la apertura del periodo y órdenes planificadas después de la apertura.
- Delivery Schedules: Aplica a los Scheduling agreements. Opciones: (1) no crear Schedule lines, (2) Crearlas solo en apertura de periodo o (3) crearlos solo dentro del planning horizon.
- Create MRP list: Determina si el sistema creará la lista MRP.
- Planning mode: Determina cómo se tratarán las propuestas de aprovisionamiento creadas previamente. Se descartan o consideran.
- Scheduling: Determina si el sistema calcula fechas básicas o lo hace a mayor detalle consultando la hoja de ruta.
