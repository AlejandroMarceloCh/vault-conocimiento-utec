---
curso: SIOPS
titulo: 2. Teoria - El Proceso de Planificación de Materiales (Datos maestros)
slides: 26
fuente: 2. Teoria - El Proceso de Planificación de Materiales (Datos maestros).pdf
---

## Slide 1

Portada del curso. Título "Proceso de Planificación de Materiales (Datos Maestros)". "Profesor: Carlos Villanueva Q." Pie de página con crédito a Magal and Word (decorativo, se repite en todas las slides posteriores).

## Slide 2

"Objetivos de Aprendizaje". Lista numerada:
1. Describir los datos maestros asociados al proceso de Planificación de Materiales.
2. Identificar Datos Maestros en el Sistema empresarial (S/4HANA).

## Slide 3

"La Planificación de Materiales". Bullets:
- Busca responder a 3 preguntas clave: ¿Qué materiales se necesitan? / ¿Cuántos se necesitan? / ¿Cuándo se necesitan?
- El principal objetivo es balancear la demanda y la oferta.
- Quiebre de stock vs. Inventario en exceso.
- Genera propuestas de compra: Solicitudes de compra / Órdenes de Producción planificadas.

## Slide 4

"Proceso básico de planificación de materiales". Diagrama de flujo horizontal:
- Un ícono de "Operational Management" (persona empujando un grupo de personas) se conecta hacia abajo a la fila de procesos.
- Fila superior de flechas encadenadas: **Sales and Operations Planning** → **Demand Management** → **Materials Requirements Planning**, cada una con un documento debajo (**Operations Plan**, **Requirements**, **Procurement Proposals** respectivamente).
- Desde "Materials Requirements Planning" el flujo se bifurca en dos ramas paralelas:
  - Rama superior: **Procurement Process** (3 flechas encadenadas) → confluye en **Inventory** (ícono de cajas apiladas).
  - Rama inferior: **Production Process** (3 flechas encadenadas) → también confluye en **Inventory**.
- Desde Inventory sale una cadena de 3 flechas hacia **Fulfillment Process** (proceso final, a la derecha).

## Slide 5

"Maestro de Materiales" — diagrama jerárquico (árbol) tipo organigrama:
- Nodo raíz: **Basic data** (campos: Material, Description, Unit of measure).
- De Basic data se despliegan 5 nodos hijos, cada uno representado como una pila de 3 tarjetas apiladas (Plant A / Plant B / Plant C, indicando que la vista existe por planta):
  - **MRP 1**: MRP type, Planning time fence, MRP controller, Lot size key, Reorder point.
  - **MRP 2**: Procurement type, In-house production time, GR processing time, Safety stock.
  - **MRP 3**: Strategy group, Consumption mode, Consumption period, Availability check.
  - **MRP 4**: BOM selection method.
  - **Work Scheduling**: In-house production time, Tolerance data.

## Slide 6

"Maestro de Materiales (Vistas)". Texto (sin imagen adicional, solo texto):
- **Vistas MRP:**
  - MRP 1: Define estrategia general de planificación y cantidad a adquirir.
  - MRP 2: Identifica scheduling y cómo obtener materiales (fabricar vs comprar).
  - MRP 3: Estrategia para calcular el material disponible y cómo se fabricará el material.
  - MRP 4: Datos para seleccionar la LMat adecuada.
- **Vista Work Scheduling (Preparación de Trabajo):**
  - Datos para determinar el tiempo de fabricación (setup, procesamiento, desmontaje).

## Slide 7

"Procurement Type (Clase de Aprovisionamiento)". Bullets:
- Indica si la provisión de un material es: Fabricación propia o interna / Externa (compra) / Ambas / Ninguna de las dos.
- En Global Bike: FG->ambas, TG, RM ->externa, SF-> interna.

## Slide 8

"MRP Type (Planificación de Necesidades)". Solo texto:
Especifica la técnica de control de producción utilizada en el planeamiento. Son 3: 1. Consumption-based planning, 2. Materials Requirement Planning (MRP), 3. Master Production Scheduling (MPS).

## Slide 9

"MRP Type (Planificación de Necesidades)" — continuación sobre Consumption-based planning. Texto: "1. Consumption-based planning: Calcula requerimientos de material basándose en la data histórica de consumo. Se realiza un pronóstico del consumo futuro."

Gráfico de línea (ejes: eje Y "Quantity in stock", eje X "Time"):
- Línea de "Consumption line" descendente (diente de sierra) que baja desde un nivel máximo de stock hasta cero, repitiéndose en ciclos.
- Líneas horizontales punteadas marcan "Reorder point" (nivel intermedio) y "Safety stock" (nivel bajo, cerca de cero).
- Puntos marcados A, B, C sobre la línea de consumo: C y B están en el nivel de reorder point (con flecha horizontal conectándolos), A está más abajo cerca de safety stock.
- Se marca "Reorder date" y "Delivery date" en el eje de tiempo, con el intervalo entre ambos etiquetado "Replenishment lead time".

## Slide 10

"MRP Type (Planificación de Necesidades)" — subtipos de Consumption-based planning. Bullets:
- 1.1 Reorder point planning: Se basa en el stock de seguridad.
- 1.1 Forecast-based planning: Utiliza data histórica para estimar o pronosticar consumo futuro. Puede considerar patrones más complejos.
- 1.2 Time-phased planning es similar al forecast based planning. Se usa cuando los proveedores hacen entregas sólo algunos días de la semana.

## Slide 11

"MRP Type (Planificación de Necesidades)". Texto: "GBI usa consumption-based planning para mercaderías (Ej. cascos)".

Mismo gráfico diente-de-sierra que en Slide 9 pero ahora con valores numéricos concretos (ejemplo aplicado a GBI):
- Eje Y "Quantity in stock" con marcas 0, 50, 100, 125, 150, 200.
- Eje X "Time in days" con marcas 1 a 10.
- Reorder point = 125, Safety stock = 50.
- Puntos C y B en 125 (reorder point); punto A en 50 (safety stock), ubicado en el día 7.
- Reorder date = día 4, Delivery date = día 7, Replenishment lead time = 3 días (indicado explícitamente).

## Slide 12

"MRP Type (Planificación de Necesidades)" — Técnica MRP. Texto:
"2. Técnica MRP: Calcula requerimientos de un material, basado en su dependencia de otros materiales (LMat)"
- **Dependent Requirement**: Su requerimiento depende del requerimiento de otro material. (Necesidades Secundarias)
- **Independent Requirement**: No depende de otro material, sino de la demanda del cliente. (Necesidades Primarias)

"Calcula y planifica requerimientos para materiales en todos los niveles de la LMat (BOM). Este procedimiento es: **BOM explosion**"

## Slide 13

"MRP Type (Planificación de Necesidades)" — Técnica MPS. Texto: "3. Técnica MPS: (Master production scheduling). Proceso similar a MRP pero enfocado en niveles superiores. Es opcional."

Diagrama de árbol jerárquico de BOM (explosión de materiales), 4 niveles:
- Nivel superior: **Finished good**, recibe una flecha desde "Independent requirement" (entrada externa).
- Nivel 2 (línea divisoria marcada MRP/MPS entre nivel 1-2 y niveles inferiores): tres nodos **Semi-finished good**, **Semi-finished good**, **Raw material**.
- Nivel 3: bajo cada semi-finished good del nivel 2, más nodos **Semi-finished good** y **Raw material**.
- Nivel 4 (más bajo): cuatro nodos **Raw material**.
- Etiqueta lateral izquierda indica que MPS solo opera en los niveles superiores (por encima de la línea) mientras MRP opera en todos los niveles (flechas "MRP"/"MPS" verticales a la izquierda).
- Anotaciones de texto junto al diagrama: "MRP calculates requirements for all levels of the BOM. MPS only calculates requirements for the first level items in the BOM" y "Requirements for all levels below the finished good are dependent on material at the next higher level".

## Slide 14

"MRP Type (Planificación de Necesidades)". Texto: "El input para el MRP es el Independent Requirement de Productos Terminados (PIR), el cual es calculado por el paso Sales and Operations Planning del Proceso de Planificación de Materiales."

## Slide 15

"MRP Type (Planificación de Necesidades)". Bullets:
- **Planned Independent Requirement (PIR)**: Se basa en las ventas proyectadas.
- **Customer Independent Requirements (CIR)**: Se basa en Requerimientos del Cliente ú Ordenes de Venta actuales.

## Slide 16

"Clave de Tamaño de Lote (Lot Size Key)". Bullets:
- Un tamaño de lote es la cantidad de material que figura en las propuestas de compra generadas en el proceso de planificación de materiales.
- La clave del tamaño de lote (Lot size key) es el procedimiento que determina el tamaño de lote:
  - **Cálculos estocásticos**: Procedimientos que especifican una cantidad fija basada en un valor predeterminado (tamaño de lote fijo) o en la cantidad exacta requerida (lote por lote).
  - **Cálculos periódicos**: Procedimientos que combinan los requerimientos de múltiples periodos de tiempo, como días o semanas en un lote.
  - **Tamaño de lote óptimo**: Procedimientos que consideran el costo de comprar y almacenar materiales, utilizando técnicas de cálculo como economic order quantity y economic production quantity.
- GBI usa el procedimiento lote por lote para determinar el tamaño de lote de todos sus materiales.

## Slide 17

"Tiempos de Planificación (Scheduling Times)". Texto:
Una tarea del Proceso de Planificación de Materiales es estimar el tiempo necesario para adquirir materiales necesarios.
El cálculo se basa en estimaciones del tiempo requerido para realizar tareas del maestro de materiales y hoja de ruta del producto. Incluye:
- **Tiempo de fabricación propia**, tiempo necesario para fabricar material internamente.
- **Plazo de Entrega previsto**, tiempo necesario para obtener el material cuando es aprovisionado externamente.
- **Tiempo de procesamiento de EM (Entrada de Mercancías)**, tiempo necesario para colocar los materiales en el almacén, disponibles para uso.

## Slide 18

"Horizonte de Planificación Fijo (Planning Time Fence)". Bullets:
- Periodo de tiempo donde el ERP no puede cambiar automáticamente las propuestas de compra planificadas.
- Ej: Si el planning time fence es 30 días, entonces ninguna orden de compra con fecha menor a 30 días podrá ser cambiada automáticamente por el Sistema, si se requieren cambios deben ser hechos manualmente.

## Slide 19

"Grupo de Verificación de Disponibilidad (Availability Check Group)". Bullets:
- Define la estrategia que usa el sistema para determinar si una cantidad del material estará disponible en una fecha específica.
- Método Available-To-Promise (ATP).
  - Es el método más común. Considera elementos de suministro y demanda.
  - Suministro: inventario actual, solicitudes de compra, órdenes de compra, órdenes de fabricación.
  - Demanda: reservas de material, stock de seguridad, pedidos de clientes.
- Es utilizado por varios procesos:
  - Ventas: asegurar entrega al cliente en la fecha solicitada.
  - Producción: asegurar disponibilidad de materiales cuando la orden de fabricación sea aprobada.

## Slide 20

"Grupo de Estrategias (Strategy Group)". Bullets:
- Especifica la estrategia de planificación de alto nivel usada en Producción.
- Categorías: Fabricación contra stock (make-to-stock / MTS) / Fabricación contra pedido (make-to-order / MTO) / Montaje según catálogo (assemble-to-order / ATO).

## Slide 21

"Strategy Group -> Make-to-stock (MTS)". Bullets:
- Los pedidos de los clientes se atienden usando un stock existente de productos terminados.
- La estrategia MTS la emplean generalmente las empresas que fabrican grandes volúmenes de productos idénticos.
- Esta estrategia reduce el tiempo requerido para cumplir los pedidos de cliente porque no hay necesidad de esperar hasta que los materiales se fabriquen.
- En SAP S/4HANA la estrategia más simple de MTS es planificación de necesidades netas (**strategy 10**), en la que el sistema genera propuestas de compra basadas en los PIRs únicamente, ignorando los CIRs.
- Una variante de la anterior es planificación con montaje final (**strategy 40**). Se basa en PIRs, pero también toma en cuenta los CIR a través del procedimiento llamado compensación (consumption).

## Slide 22

"Strategy Group -> Make-to-order (MTO)". Bullets:
- La estrategia de producción de productos terminados y semiterminados es motivada por una orden de venta.
- La empresa no mantiene inventarios de productos terminados.
- MTO se utiliza cuando cada producto es único.

## Slide 23

"Strategy Group -> Assemble-to-order (ATO)". Bullets:
- Es una variación de la estrategia MTO.
- Se mantiene un inventario de componentes (semiterminados) necesarios para la fabricación de productos terminados.
- La producción de los productos terminados se desencadena por los pedidos de cliente (estrategia MTO).
- Ejemplo: pedidos de diferentes configuraciones de computadoras. Solo se debe ejecutar el ensamblaje final de componentes para atender pedidos de clientes.

## Slide 24

"Modo de compensación (Consumption mode)". Texto: "Consumption es el proceso por el cual los CIRs consumen los PIRs."

Tabla reproducida:

| | Before Consumption PIR | Before Consumption CIR | After Consumption PIR | After Consumption CIR |
|---|---|---|---|---|
| Example 1 | 50 | 60 | 0 | 60 |
| Example 2 | 50 | 40 | 10 | 40 |

## Slide 25

"Consumption mode". Texto: "Dos modos conocidos son backward consumption y forward consumption. Se pueden combinar ambos también."

Tres diagramas apilados (ejes: PIRs arriba de la línea de tiempo, CIRs abajo; barras azul claro = PIR, barras azul oscuro = consumo de PIR/CIR), cada uno etiquetado "Time" en el eje horizontal:
- **Mode 1**: barras PIR de 20/20 al inicio, luego barra de consumo 40, CIR de 60 debajo; se marca el rango "Backward consumption period" (abarca desde el inicio hasta el punto de consumo, mirando hacia atrás en el tiempo).
- **Mode 3**: barras PIR iniciales, luego barra de consumo 40 y CIR de 60 debajo, seguido de barras PIR 20/20; se marca el rango "Forward consumption period" (abarca desde el punto de consumo hacia adelante).
- **Mode 2/4**: combina ambos — barra de consumo 40 antes y CIR 60 en el centro, con barras 20/20 después; se marcan ambos rangos "Bwd per." y "Fwd per." (combinación backward + forward).
- Nota al pie del diagrama: "The dark blue boxes show CIR (below the line) and consumption of PIR (above the line). Light blue boxes are PIR."

## Slide 26

"Grupos de Productos (Product Groups)". Bullets:
- El planeamiento de materiales agrupa productos similares para mayor eficiencia.
- **Aggregation**: Agrupación de productos desde el nivel de material más bajo hasta el nivel más alto.
- **Proportion factor**: Medida de influencia del ítem en el Product Group.

Diagrama de árbol jerárquico (ejemplo de bicicletas GBI) con flechas de agregación (izquierda, hacia arriba) y desagregación (derecha, hacia abajo):
- Nivel 1 (raíz): **PG-BIKE000 Bicycles**.
- Nivel 2: **PG-TOUR000 Touring (60%)** y **PG-ORBK000 Off-Road (40%)** (porcentajes = proportion factor respecto al padre).
- Bajo PG-TOUR000: **PG-DXTR000 Deluxe (70%)** y **PG-PRTR000 Professional (30%)**.
- Bajo PG-DXTR000: **DXTR1000 Black (40%)**, **DXTR2000 Silver (30%)**, **DXTR3000 Red (30%)**.
- Bajo PG-PRTR000: **PRTR1000 Black (40%)**, **PRTR2000 Silver (30%)**, **PRTR3000 Red (30%)**.
- Bajo PG-ORBK000: **ORMN1000 Men's (65%)** y **ORWN1000 Women's (35%)**.
- Flecha lateral izquierda etiquetada "Aggregation" (apunta hacia arriba, agrupando de nivel bajo a alto); flecha lateral derecha etiquetada "Disaggregation" (apunta hacia abajo, desde el nivel alto hacia los niveles bajos).
