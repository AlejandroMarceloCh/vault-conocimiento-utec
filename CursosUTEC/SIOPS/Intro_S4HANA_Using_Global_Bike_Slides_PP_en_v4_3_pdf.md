---
curso: SIOPS
titulo: Intro_S4HANA_Using_Global_Bike_Slides_PP_en_v4.3
slides: 59
fuente: Intro_S4HANA_Using_Global_Bike_Slides_PP_en_v4.3.pdf
---

## Slide 1

Portada del capítulo. Título "Production Planning and Execution (PP)". Subtítulo "Curriculum: Introduction to S/4HANA using Global Bike". Imagen decorativa de fondo: fotografía de un brazo robótico industrial naranja en una cabina de pintura/ensamblaje. Logos SAP UCC Magdeburg y SAP University Alliances (decorativos).

## Slide 2

"Teaching material - Information". Ícono decorativo (documentos con lápiz). Texto: Teaching material - Version 4.3 (July 2025). Software used: S/4HANA 20223, Fiori 3.0. Model: Global Bike. Prerequisites: No prerequisites needed. Al lado derecho, logo/banner "Global Bike" (verde, con silueta de ciclista) — decorativo, identifica el modelo de datos usado en todo el curso.

## Slide 3

"Module Information". Dos bloques con íconos decorativos: Authors (ícono lápiz) — Bret Wagner, Stefan Weidner, Babett Ruß. Target Audience (ícono personas) — Beginner.

## Slide 4

"Module Information" — Learning Objectives (ícono diana/target, decorativo). Lista:
- Understand a manufacturing process cycle
- Get familiar with the basics of a production plan

## Slide 5

"Functionality". Texto: SAP divides production into multiple processes:
- Production Planning
- Manufacturing Execution: Discrete Manufacturing, Repetitive Manufacturing, KANBAN
- Production – Process Industries: Integrated planning tool for batch-orientated process manufacturing; diseñado para industrias química, farmacéutica, alimentos/bebidas y electrónica orientada a lotes.

## Slide 6

"Unit Overview" — slide de agenda con 3 puntos, el primero resaltado en negro (activo) y el resto en gris (por venir):
- **PP Organizational Structure** (activo)
- PP Master Data
- PP Processes: Material Planning, Production Planning, Manufacturing Execution Process

## Slide 7

"PP Organizational Structure". Lista jerárquica de conceptos organizacionales SAP:
- Client: An independent environment in the system
- Company Code: Smallest org unit for which you can maintain a legal set of books
- Plant: Operating area or branch within a company (manufacturing, distribution, purchasing or maintenance facility)
- Storage Location: organizational unit para diferenciar stocks de un material en una planta
- Work Center Locations (en SAP = master data): unidad organizacional que define dónde y cuándo se realiza una operación; tiene capacidad disponible; actividades valuadas por charge rates determinados por cost centers y activity types; pueden ser máquinas, personas, líneas de producción o grupos de personas.

## Slide 8

"Global Bike Structure for Production Planning" — diagrama organigrama jerárquico (visual clave). Estructura en árbol de arriba hacia abajo, con etiquetas de nivel a la derecha:
- Nivel Client: "Global Bike" (caja azul superior)
- Nivel Company Code: dos cajas — "Global Bike Inc." y "Global Bike Germany GmbH"
- Nivel Plant: bajo Global Bike Inc. → "Dallas"; bajo Global Bike Germany GmbH → "Heidelberg"
- Nivel Storage Location (bajo cada plant, 4 cajas idénticas en ambos lados): Raw Materials, Semi-fin. Goods, Finished Goods, Miscellaneous
- Nivel Work Center Location (bajo cada plant, 3 cajas): Assembly, Packaging, Inspection

Refleja 1:1 la jerarquía Client → Company Code → Plant → Storage Location / Work Center Location descrita en el slide anterior, instanciada con los datos del modelo Global Bike.

## Slide 9

"GBI Enterprise Structure in SAP ERP (Logistics)" — diagrama 3D isométrico en capas tipo "pirámide/plataformas apiladas" (visual complejo, colores azul/gris/amarillo/verde/naranja). De abajo hacia arriba:
- **Client GBI** (base)
- **Company Code**: CC US00, CA00, CC DE00, AU00 — con Plants debajo: Dallas DL00, Miami MI00, S. Diego SD00 (bajo US00); Toronto TO00 (bajo CA00); Heidelb. HD00, Hamburg HH00 (bajo DE00); Perth PE00 (bajo AU00)
- **Central Purchasing Organization (global) GL00**, con Purchasing Org. US00 → Purchasing Group North America N00; PO DE00 → PGr Europe E00; y Asia A00
- **Storage Location** (capa superior), por cada shipping point: combinaciones de RM00 (raw material), SF00 (semi-finished), FG00 (finished goods), MI00 (miscellaneous), TG00
- **Shipping Point** (capa más alta): DL00, MI00, SD00, TO00, HD00, HH00, PE00

Es la vista logística completa de la estructura organizativa de Global Bike Inc. (GBI) en SAP, cruzando compras, plantas y almacenamiento por región (Norteamérica, Canadá, Alemania, Australia/Asia).

## Slide 10

"Unit Overview" — slide de agenda, ahora con el segundo punto resaltado en negro:
- PP Organizational Structure (gris, completado)
- **PP Master Data** (activo)
- PP Processes: Material Planning, Production Planning, Manufacturing Execution Process (gris)

## Slide 11

"PP Master Data" — lista de los 5 tipos de datos maestros de PP:
- Material
- Bill of Materials (BOM)
- Routing — con nota: "BOM and routing are like a cooking recipe" → BOM = ingredients, Routing = steps in the recipe
- Work Center
- Product Group

## Slide 12

"Material Master Record" — captura de pantalla de Fiori/SAP GUI: "Display Material DXTR1000 (Finished Product)". Menú superior con Additional Data, Org. Levels, Services for Object. Pestañas: Basic data 1 (activa), Basic data 2, Sales: sales org. 1/2, Sales: General/Plant. Campos visibles:
- Material: DXTR1000, Descr.: Deluxe Touring Bike (black)
- General Data: Base Unit of Measure EA (each), Material Group BIKES, Division BI, GenItemCatGroup NORM (Standard item)
- Material authorization group: (vacío)
- Dimensions/EANs: Gross Weight 8.510, Net Weight 8.510, Unit of Weight G, Volume 0.000

## Slide 13

"Bill of Materials (BOM)" — texto: "List of components that make up a product or assembly". Dos columnas de componentes de una bicicleta (Global Bike), sin diagrama, lista simple:
Columna izquierda: Wheel Assembly (Tire, Tube, Wheel, Hex Nut, Lock Washer, Socket Head Bolt), Frame, Derailleur Gear Assembly.
Columna derecha: Seat Kit, Handle Bar, Pedal Assembly, Chain, Brake Kit, Warranty Document, Packaging.

## Slide 14

"Bill of Materials (BOM)" — "Single-Level". Dos visuales lado a lado:
- Izquierda: captura de pantalla SAP "Material: ORMN1000 (Men's Off Road Bike)", Plant: DL00, Alternative BOM: 1, pestaña Material con tabla de componentes (Item, ICt, Component, Component description, Quantity, UoM): 0010 L ORWA1000 "Off Road Aluminum Wheel Assembly" qty 2 EA; 0020 L OFFR1000 "Men's Off Road Frame" qty 1; 0030 L DGAM1000 "Derailleur Gear Assembly" qty 1; 0040 L ORSK1000 "Off Road Seat Kit" qty 1; 0050 L ORHB1000 "Off Road Handle Bar" qty 1; 0060 L PEDL1000 "Pedal Assembly" qty 1; 0070 L CHAN1000 "Chain" qty 1; 0080 L BRKT1000 "Brake Kit" qty 1; 0090 L WDOC1000 "Warranty Document" qty 1; 0100 L PCKG1000 "Packaging" qty 1.
- Derecha: diagrama de árbol "Single-Level" (recuadro punteado) — nodo raíz "Finished Bike" conectado hacia abajo con 6 pares de cajas azules conectadas entre sí horizontalmente por flechas dobles: Wheel Assembly↔Pedal Assembly, Frame↔Chain, Derailleur Gear Assembly↔Brake Kit, Seat Kit↔Warranty Doc., Handle Bar↔Packaging.

## Slide 15

"Bill of Materials (BOM)" — "Single-Level vs. Multi-Level". Diagrama combinado (visual clave): recuadro exterior punteado etiquetado "Single-Level" (gris) que contiene nodo raíz "Finished Bike" con 10 hijas en fila (Wheel, Frame, Derailleur, Seat, Handle Bar, Pedal, Chain, Brake, Doc., Pack.). Dentro, anidado bajo "Wheel", un segundo recuadro punteado etiquetado "Single-Level" (más pequeño) que despliega los subcomponentes de Wheel: Tire, Tube, Wheel, Hex nut, Lock, Bolt (cajas amarillas) — este segundo nivel junto con el primero forma el recuadro exterior gris claro etiquetado "Multi-Level" en la esquina inferior derecha. Ilustra que un BOM multinivel es la composición recursiva de BOMs de un solo nivel.

## Slide 16

"Bill of Materials (BOM)" — "Variant Bill of Materials (BOM)": "Several products with a large proportion of identical parts." Dos diagramas de árbol single-level superpuestos/lado a lado (visual): "Deluxe Bike (red)" con componentes Aluminum Wheel↔Pedal Assembly, Frame red↔Chain, Derailleur Gear Assembly↔Brake Kit, Seat Kit↔Warranty Doc., Handle Bar↔Packaging (componentes específicos de la variante en amarillo: Aluminum Wheel, Frame red). "Professional Bike (black)" con la misma estructura pero Carbon Wheel, Frame black (en amarillo) y el resto de componentes idénticos compartidos (Pedal Assembly, Chain, Brake Kit, Warranty Doc., Packaging, Derailleur Gear Assembly, Seat Kit, Handle Bar). Ilustra cómo dos variantes de producto comparten casi todos los componentes salvo 2 piezas específicas.

## Slide 17

"BOM – Item Categories". Texto: "An object that defines items in a BOM according to criteria, such as the object type of the component, for example, material master record or document info record." The item category controls: Screen sequence, Field selection, Default values, Material entry, Inventory management, Subitems. Item Categories: Stock item, Non-stock item, Variable material – Sheet of steel, Document item, Text item.

## Slide 18

"Routing". Columna izquierda: Routings enable the planning of the production of materials (products); Routings are used as a template for production orders and run schedules; Routings are also used as a basis for product costing; Series of sequential steps (operations) that must be carried out to produce a given product; Routings contain: What, Where, When, How.

Columna derecha: "Example: Routing – Operation 20": Attach seat to frame; Work Center – ASSY1000: Assembly Work Center; Time: 1 minute. Debajo, captura tipo tarjeta azul estilo "index card": "20 | ASSY1000 | 1 MIN | Attach seat to frame" (representación estilizada de una operación de routing).

Abajo, tira horizontal de 6 tarjetas azules encadenadas con flechas (secuencia completa de la routing del "Finished Bike"): 10 ASSY1000 0.667 MIN "Material staging" → 20 ASSY1000 1 MIN "Attach seat to frame" → 30 ASSY1000 2 MIN "Attach handle bar assembly" → 40 ASSY1000 2 MIN "Attach derailleur gear assm. to wheel" → 50 ASSY1000 5 MIN "Attach front and rear wheels to chain" → 60 (cortada, texto no visible completo).

## Slide 19

"Routing" — captura de pantalla SAP "Operation Overview" para el routing del Finished Bike, con anotaciones/etiquetas superpuestas señalando cada columna (diagrama explicativo con flechas apuntando a la tabla):
- Operation → columna "Op..." (0010, 0020, 0030)
- Work Center → columna "Work Ce..." (ASSY1000)
- Plant → columna "Plant" (DL00)
- Description → columna "Description" (Material staging; Attach seat to frame; Attach handle bar assembly)
- Activity Type (explicado: "unit in a controlling area that classifies the activities performed in a cost center. Examples in production cost centers are machine hours or finished units.") → columna "Activit..." (LABOR)
- Control Key (explicado: "key that specifies how an operation or a sub-operation is processed in functions such as orders, costing or capacity planning.") → columna "Con..." (ASSY)
- Time and Unit of Measure → columnas "Base Quantity" (15, 1, 1), "Un..." (EA), "Setup" (0), "Unit" (MIN)

## Slide 20

"Work Center". Texto: A location within a plant where Value-added work (operations or activities) is performed. Work Centers can represent: People or Groups of people, Machines or Groups of machines, Assembly Lines. Work Center used to define capacities: Labor, Machine, Output, Emissions. Capacities used in: Capacity requirements planning (CRP), Detailed scheduling, Costing.

## Slide 21

"Work Center" — continuación. Work Centers capture and use the following Resource related data:
- Basic Data: Person Responsible, Location of Work Center
- Scheduling Information: Queues and Move Times (interoperation), Formula Keys
- Costing Data: Cost Center, Activity Types
- Personnel Data: People, Positions, Qualifications
- Capacity Planning: Available Capacity, Formulas, Operating Time
- Default Data: Control Key, Standard Text Key

## Slide 22

"Product Group". Aggregate planning that groups together materials or other product groups (Product Families). Multi- or Single-Level Product Groups; the lowest level must always consist of materials.

## Slide 23

"PP Processes" — slide de transición/lista, sin diagrama. Production Planning & Execution: Forecasting, Sales and Operations Planning (SOP), Demand Management, Master Production Scheduling (MPS), Material Requirement Planning (MRP). Production Order.

## Slide 24

"Production Planning & Execution" — diagrama de flujo vertical en 3 bandas grises horizontales (visual clave, reutilizado en slides 25 y 30):
- Banda "Strategic Planning" (gris): dos formas hexagonales grises (SIS, CO/PA) apuntando ambas hacia el centro con flechas → caja azul "Forecasting" → flecha abajo → caja azul "Sales & Operations Planning"
- Flecha baja hacia caja verde "Demand Management" (fuera de las bandas, entre Strategic y Detailed Planning)
- Banda "Detailed Planning" (gris): caja dorada "MPS" → flecha abajo → caja dorada "MRP", que se ramifica en dos flechas (izquierda y derecha)
- Banda "Manufacturing Execution" (gris): rama izquierda de MRP → óvalo amarillo "Manufacturing Execution" → flecha abajo → óvalo amarillo "Order Settlement"; rama derecha de MRP → óvalo gris oscuro "Procurement Process"

## Slide 25

"Production Planning & Execution" — mismo diagrama de la slide 24, ahora con etiquetas adicionales de roles ("Players in the Game") a la izquierda:
- Strategic Planning: CEO, COO, CIO, CFO, Controller, Marketing Director
- Detailed Planning: Line Managers, Production Scheduler, MRP Controller, Capacity Planners
- Execution: Line Workers, Shop Floor Supervisors

El diagrama a la derecha es idéntico en estructura al de la slide 24 (SIS/CO/PA→Forecasting→SOP→Demand Management→MPS→MRP→Manufacturing Execution/Order Settlement + Procurement Process), reetiquetando las 3 bandas con su nivel organizacional correspondiente.

## Slide 26

"Forecasting". Texto: Forecasting is the foundation of a reliable SOP; Accurate forecasts are essential in the manufacturing sector; Overstocked & understocked warehouses result in the same issue: A loss in profits; Forecasts are ALWAYS WRONG. Ilustración decorativa estilo clip-art en blanco y negro: un hombre con anteojos sosteniendo varios gráficos de pronóstico contradictorios entre sí ("Forecast #1" tendencia ascendente, "Forecast #2" curva descendente, "Forecast #3" curva en U, "Forecast #4" espiral) — refuerza visualmente la idea de que los forecasts son inconsistentes/siempre equivocados.

## Slide 27

"Forecasting" — Forecasting Models: Trend, Seasonal, Trend and Seasonal, Constant. Selecting a Model: Automatically, Manually. Captura de pantalla SAP: "Forecast: Parameters for Automatic Model Selection", modelo "Exponential smoothing, first-order with test for" con opciones de radio button: Trend (Alpha factor 0.20, Beta factor 0.20), Season (Alpha 0.20, Gamma 0.20, Periods per season 12), **Trend and season** (seleccionado), Seasonal model and test for trend, Trend model and test fro season (Alpha/Beta/Gamma 0.20, Periods per season 12), Forecast model sel. using procedure 2 (Periods per season 12). Botones inferiores: Forecasting, Historical..., Cancelar (X roja).

## Slide 28

"Sales and Operations Planning (SOP)". Information Origination: Sales, Marketing, Manufacturing, Accounting, Human Resources, Purchasing. Intra-firm Collaboration: Institutional Common Sense. Ilustración decorativa estilo clip-art: tres "castillos de arena" con banderas etiquetadas BUYING, PLANNING/PRODUCTION/SALES — metáfora visual de silos departamentales desconectados dentro de la empresa.

## Slide 29

"Sales and Operations Planning (SOP)" — continuación, sin imagen. Flexible forecasting and planning tool. Usually consists of three layers: Sales Plan, Production Plan, Rough Cut Capacity Plan. Planned at an aggregate level in time buckets.

## Slide 30

"Demand Management". The planning of requirement quantities and requirement dates for finished products and important assemblies. Definition of the strategy for planning and producing or procuring a finished product. Link between Strategic Planning (SOP) & Detailed Planning (MPS/MRP). Demand management can be done manually or based on previous planning results such as sales planning, SOP, and forecast. The results of Demand Management is called the Demand Program, generado de PIR (Planned Independent Requirements) y CIR (Customer Independent Requirements).

## Slide 31

"Demand Management" — diagrama de flujo (visual): íconos decorativos "Forecast" (gráfico ascendente) y "Sales" (caja registradora), cada uno alimentando una caja dorada respectiva — "Planned Independent Requirements" (bajo Forecast) y "Customer Independent Requirements" (bajo Sales) — ambas convergen con flechas diagonales hacia una caja dorada central "Demand Program", que a su vez fluye con una flecha hacia abajo hacia "MPS / MRP".

## Slide 32

"Planning Strategies". Planning strategies represent the business procedures for: The planning of production quantities, Dates. Wide range of strategies. Multiple types of planning strategies based upon environment: Make-To-Stock (MTS); Make-To-order (MTO) — driven by sales orders; Configurable materials — mass customization of one; Assembly orders.

## Slide 33

"Planning Strategies for Make-to-Stock and Make-to-Order" — tabla comparativa en dos columnas (sin bordes de tabla, formato de texto paralelo):

| Make-to-Stock | Make-to-Order |
|---|---|
| Planning takes place using Independent Requirements | Planning takes place using Customer Orders |
| Sales are covered by make-to-stock inventory | Sales are covered by make-to-order production |
| Strategies: 10 – Net Requirements Planning; 11 – Gross Requirements Planning; 30 – Production by Lot Size; 40 – Planning with Final Assembly | Strategies: 20 – Make to Order Production; 50 – Planning without Final Assembly; 60 – Planning with Planning Material |

## Slide 34

"Master Production Scheduling (MPS)". Texto único: MPS allows a company to distinguish planning methods between materials that have a strong influence on profit or use critical resources and those that do not.

## Slide 35

"Material Requirement Planning (MRP)". In MRP, the system calculates the net requirements while considering available warehouse stock and scheduled receipts from purchasing and production. During MRP, all levels of the bill of material are planned. The output of MRP is a detailed production and/or purchasing plan. Detailed planning level: Execute primary functions, Monitor inventory stocks, Determine material needs (Quantity, Timing), Generate purchase or production orders.

## Slide 36

"Demand-Independent vs. Dependent". Independent Demand – Original source of the demand (demand for a finished product, such as a computer, bicycle, or pizza). Dependent Demand – Source of demand resides at another level (demand for component parts or subassemblies, e.g. microchips in the computer, wheels on the bicycle, or cheese on the pizza).

## Slide 37

"Material Requirement Planning (MRP)" — continuación. MRP is used to ensure the availability of materials based on the need generated by MPS or the Demand Program. 5 Logical Steps: Net Requirements Calculation, Lot Size Calculation, Procurement Type, Scheduling, BOM Explosion.

## Slide 38

"Net Requirements" — diagrama de dos columnas rectangulares apiladas (visual):
- Columna izquierda (de arriba a abajo): "Procurement Proposal" (gris) — con flecha "Shortage" apuntando hacia ella desde la derecha —, "Firmed Receipts" (azul), "Firmed Orders or Purchase Requisitions" (azul), "Stock" (gris claro, base).
- Columna derecha (de arriba a abajo): "Requirements – Planned Ind. Req., Reservations, Sales Orders, Etc." (dorado, bloque grande), "Safety Stock" (gris, base).
La flecha "Shortage" conecta el nivel de Requirements con el Procurement Proposal, indicando que la escasez neta entre columnas dispara una propuesta de aprovisionamiento.

## Slide 39

"Lot sizing". Static: Based on fixed values in the Material Master. Periodic: Groups net requirements together from multiple periods. Optimized: Calculates the optimum lot size for a several periods of net requirements.

## Slide 40

"Procurement Type". External Procurement: Purchase Requisition, Purchase Order, Schedule Line. Internal Procurement: Planned Order, Production Order, Process Order.

## Slide 41

"Multi-Level Scheduling" — diagrama tipo escalera ascendente (visual) sobre un eje horizontal "Time". Leyenda: azul = Planned Order, dorado = Purchase Requisition. De abajo hacia arriba y de izquierda a derecha en el tiempo: "Component" (dorado) y "Raw Material" (dorado) en el nivel más bajo/temprano → "Semi-Finished Good" (dorado) → "Assembly 1" (azul) → "Finished Product" (azul) en el nivel más alto/tardío, terminando en la fecha marcada "Required Date" (flecha verde apuntando hacia abajo sobre el extremo derecho). Ilustra cómo cada nivel de BOM se programa hacia atrás en el tiempo desde la fecha requerida del producto terminado.

## Slide 42

"MRP vs. Consumption-Based". Whether or not a material is planned using MRP or Consumption Based is determined by the MRP Type on the MRP1 screen of the Material Master. Dos columnas de cajas (visual simple, sin conectores): MRP → PD – MRP, VSD – Seasonal MRP. Consumption Based → VB – Reorder-Point, VV – Forecast Based, RP – Replenishment.

## Slide 43

"Consumption-Based" — diagrama de sierra dentada (gráfico de inventario en el tiempo, visual clásico de reorder point), sin ejes numerados explícitos. Muestra 3 ciclos de consumo en diagonal descendente desde un nivel alto hasta el nivel de "Safety Stock" (línea punteada dorada inferior), cruzando en cada ciclo la línea punteada verde "Reorder Point". Al llegar a Safety Stock, el stock se repone verticalmente (línea recta hacia arriba) reiniciando el ciclo. Etiquetas: "Lot Size" (llave que mide la altura de la reposición en el último ciclo), "Replenishment Lead Time" (flecha horizontal bajo el eje, midiendo el tiempo entre que se cruza el reorder point y se repone el stock).

## Slide 44

"Output of MRP" — diagrama de flujo (visual): caja dorada central "MRP" con flechas hacia dos bloques grandes: izquierda "In-House Production" (gris) y derecha "External Procurement" (gris), ambos con cajas hijas azules/blancas. Bajo MRP: caja dorada "Planned Order" → flecha abajo → caja dorada "Convert to", que se ramifica hacia "Production Orders" y "Process Orders" (dentro de In-House Production, cajas azules) y hacia "Purchase Requisitions" (dentro de External Procurement) → que a su vez fluye a "Purchase Orders" y "Schedule Lines" (cajas azules). El bloque "External Procurement" también recibe flecha directa desde MRP hacia "Schedule Lines".

## Slide 45

"Orders, orders, orders". Planned Order (planning): A request created in the planning run for a material in the future (converts to either a production or purchase order). Production Order (execution): A request or instruction internally to produce a specific product at a specific time. Purchase Order (execution): A request or instruction to a vendor for a material or service at a specific time.

## Slide 46

"Manufacturing Execution Process" — diagrama circular/ciclo (visual clave, flecha curva azul gruesa en sentido antihorario alrededor de un ícono central decorativo de fábrica embotelladora). Etapas del ciclo en sentido antihorario desde arriba: Capacity Planning → Schedule and Release → Shop Floor Documents → Goods Issue → Completion Confirmation → Goods Receipt → Order Settlement → Production Proposal (Planning/Other) → (vuelve a Capacity Planning, cerrando el círculo).

## Slide 47

"Production Order". Production orders are used to control production operations and associated costs. Production orders define the following: Material produced, Quantity, Location, Timeline, Work involved, Resources used, Cost settlement.

## Slide 48

"Production Order" — captura de pantalla SAP "Production order Display: Header" con anotaciones (diagrama explicativo con flechas hacia cada campo):
- Order: 1000001, Type: PP01, Material: DXTR1000 "Deluxe Touring Bike (black)", Plant: HD00, Status: REL MSPT CNF PRC SETC
- Etiquetas: "What" → apunta a Material; "How many" → apunta a Quantities (Total Qty: 1 EA, Delivered: 0, Scrap Portion: 0, Short/Exc. Rcpt: 0); "How" → apunta a botón "Components"; "Timeline" → apunta a Dates/Times (End 06/06/2025, Start 06/03/2025, Release 06/03/2025, con columnas Basic Dates/Scheduled/Confirmed, ej. Confirmed Start 06/03/2025 18:44)
- Sección Scheduling: Type "2 Backwards", Reduction "Reduction level 2", Note "Automatically carried out today scheduling"; Sección Floats: Sched. Margin Key 001, Float Bef. Prdn 1 Workdays, Float After Prdn 1 Workdays, Release Period 1 Workdays
- Botones de menú superior: Operations, Components, Documents, Sequences, Services for Object

## Slide 49

"Schedule". Calculates the production dates and capacity requirements for all operations within an order. Determines a Routing: Operation specific timelines, Material Consumption Points. Material Master: Scheduling Margin Key (Floats). Work Center: Formulas, Standard Inter-operation Times.

## Slide 50

"Release". Two release processes: Header Level (Entire order and all operations are released for processing, order is given a REL status); Operation Level (Individual operations within an order are released, Order is given a PREL status, Not until the last operation is released does the order obtain a REL status). Automatic vs. manual.

## Slide 51

"Availability Check". Automatic check to determine whether the component, production resource tools, or capacities in an order are available: Can be automatic or manually executed; Determines availability on the required date. Generates an availability log: Displays results of the check, Missing parts list, Reservations that could not be verified.

## Slide 52

"Schedule & Release". The time between scheduling and releasing an order is used for company checks and any preparation needed for the processing of the order. Once an order has been released it is ready for execution, we can at this time: Print shop floor documents, Execute goods movements, Accept confirmations against the order.

## Slide 53

"Shop Floor Documents". Shop Floor Documents are printed upon release of the Production Order, examples would be: Operation-based Lists (Time Tickets, Confirmation Slips); Component-based Lists (Material Withdrawal Slips, Pull List/consumption list); PRT Lists (Overview of PRT's used with their respective operations); Multi-Purpose Lists (Operation Control Ticket, Object Overview).

## Slide 54

"Material Withdrawal". When a production order is created it references a BOM to determine the necessary components to produce the material. It then places a reservation on each of the components. Upon release of the order (or operation) you can withdraw the reserved materials from inventory: Reservation is updated, Inventory is updated, Costs are assigned to the order as actual costs.

## Slide 55

"Confirmations". Confirmations are used to monitor and track the progression of an order through its production cycle (confirmation puede ser a nivel operación u orden). Exact confirmation shortly after completion of an operation is essential for realistic production planning and control. Data that needs confirmation include: Quantities (yield, scrap, rework), Activity data (setup time, machine time), Dates (setup, processing, teardown started or finished), Personnel data (empleado, número de empleados involucrados), Work center, Goods movements (planned and unplanned), Variance reasons, PRT usage.

## Slide 56

"Goods Receipt". Acceptance of the confirmed quantity of output from the production order into stock. Effects of the Goods Receipt: Updates stock quantity, Updates stock value, Changes price stored for future valuation, Updates production order. Three documents are created: Material document, Accounting document, Controlling document.

## Slide 57

"Order Settlement". Consists of settling the actual costs incurred in the order to one or more receiver cost objects (receivers could include: a material, a cost center, an internal order, a sales order, a project, a network, a fixed asset). Parameters for Order Settlement: Settlement Profile (specifies the receivers, distributions rules and method), Settlement Structure (determines how the debit cost elements are assigned to the settlement cost elements). Settlement Rule: automatically assigned on creation of order; has one or more distribution rule assigned to it; distribution rules define cost receiver, settlement share, settlement type.

## Slide 58

"Order Settlement" — continuación con ejemplo numérico (diagrama tipo cuenta T contable, visual): Settling a Production Order to Stock. Debit posting is made to the Production Order with the value of the material*; difference between the debit posting and credit posting is posted to a price difference account. Tres cuentas en forma de "T" mostrando el asiento: **Material** 80 (debe) | **Prod. Order** 100 (haber) | **Price Diff.** 20 (debe). Nota al pie: "* Material Price is determined by the quantity produced times the Standard Price in the Material Master."

## Slide 59

"Order Settlement" — cierre del capítulo. Costs analyzed: Primary (Materials, External Processing), Secondary (Production, Material, and Administrative Overhead; Labor). Cost Analysis Reporting: Calculate and analyze planned costs, target costs, and actual costs of the production order; Calculate and analyze variances.
