---
curso: FUNDOPS
titulo: F1-S2-Configuraciones de Producción
slides: 18
fuente: F1-S2-Configuraciones de Producción.pdf
---

## Slide 1

Portada. "FUNDAMENTOS DE OPERACIONES / Semana 2 – Configuraciones de producción". Fondo: foto del edificio UTEC con overlay azul (decorativa), logo UTEC.

## Slide 2

Índice:
1. Entornos de producción
2. Configuraciones de proceso-producto

## Slide 3

Slide separadora de sección "1 — Entornos de producción: ¿Cuál es nuestro contexto?". Fondo foto edificio UTEC con overlay celeste (decorativa). Encabezado "Inventory Management", autor "José Antonio Larco".

## Slide 4

**Decoupling Stock – Punto de desacople.**

Diagrama de cadena de suministro (fuente: Naylor et al., 1999) con 4 etapas conectadas por flechas "MATERIAL": Raw Material Supplier → Manufacturers/Assemblers → Retailer → End-Users. Cada etapa tiene un icono de fábrica con contenedores.

Debajo, 5 líneas horizontales que representan distintas configuraciones, cada una con un triángulo invertido (símbolo "A Stockholding Decoupling Point") ubicado en distinta posición a lo largo de la cadena, con flechas "Pull" apuntando hacia atrás desde el triángulo hasta el punto de origen:
- Buy to order: triángulo justo después de Raw Material Supplier (casi al inicio)
- Make to order: triángulo un poco más adelante, entre supplier y manufacturer
- Assemble to order: triángulo a mitad de camino, en manufacturer/assembler
- Make to stock: triángulo cerca de retailer
- Ship to stock: triángulo justo antes de end-users (casi al final)

Esto ilustra que a medida que el punto de desacople (stock) se mueve hacia el cliente, la configuración pasa de "a pedido" a "para stock".

Texto lateral derecho:
- "En qué punto de la cadena trabajamos bajo pedido"
- "Si trabajo bajo pedido o para Stock depende de:"
  - Volumen del producto
  - Tiempo de entrega (lead time)
  - Variedad/personalización

## Slide 5

**Decoupling Stock – Punto de desacople** (continuación).

Diagrama grande "[FIGURE 2] FACTORS IN SUPPLY CHAIN PROCESSES" (fuente: Supply Chain Roadmap, 2012), con flujo de 3 grandes flechas: Sourcing → Manufacturing → Delivery.

Etiquetas sobre el diagrama (de izquierda a derecha):
- "Zone of sourcing buffering: Inventory, time, and/or pool of suppliers"
- "Decoupling point (or order penetration point), where order is received to configure product according to the customer's specific requirements. Defines the customization level."
- "Zone of demand buffering: Inventory, time and/or excess capacity"
- "Demand profile: Variation of average level of demand over time"

Etiquetas debajo:
- "Workload leveling (takt): Variation of workload over time"
- "Asset-utilization rate: Average level of utilization of key assets"
- "Production cycle: Time required to produce whole portfolio"
- "Order cycle: Time from order entry to receipt by customer"
- "Production cycle after order entry" y "Transport lead time" (recuadradas cerca de Delivery)

Dentro de las flechas hay líneas onduladas de colores (naranja en Sourcing, roja y verde en Manufacturing/Delivery) representando variabilidad/fluctuación.

Anotaciones a mano (flechas naranjas) agregadas por el profesor:
- "Costos de intermediación: Cómo ajustar a fluctuaciones en la demanda" apuntando a varios puntos del diagrama.
- "Trabajamos con stock: MTS" (izquierda) y "Trabajamos a pedido: MTO" (derecha), con una flecha doble azul entre ambos textos indicando el espectro.
- "Punto de desacople" con flecha apuntando al círculo gris central entre Manufacturing y Delivery (el decoupling point).

A los costados, dos fotos (decorativas/ilustrativas): engranajes metálicos (izquierda, representa materia prima/componentes) y un auto rojo Audi (derecha, representa producto terminado).

## Slide 6

**Entornos de Producción (penetración de orden) — Make to Stock (MTS).**
"Fabricación para almacenamiento"
- Se almacenan productos terminados
- El cliente decide adquirir o no el producto
- Requiere espacio de almacenamiento
- Aumenta el inventario
- **Objetivos:** evitar roturas de stock, evitar inventarios excesivos

Imágenes (ejemplos ilustrativos de productos MTS): carretes de cinta/ribbon de colores variados, resmas de papel blanco, calculadora científica Casio.

## Slide 7

**Entornos de Producción (penetración de orden) — Assemble to Order (ATO).**
"Armado bajo pedido"
- Existen módulos o sub-armados, que el cliente puede elegir para un paquete.
- Requiere espacio de almacenamiento de partes mas no de productos terminados
- **Objetivos:** evitar roturas de stock, evitar inventarios de partes excesivos

Imágenes (ejemplos): logo de Bembos con hamburguesas (comida armada a pedido con ingredientes predefinidos), auto sedán oscuro BMW, laptop con dock/base de conexión.

## Slide 8

**Entornos de Producción (penetración de orden) — Engineer to Order (ETO).**
"Ingeniería a pedido"
- Se produce a pedido
- El cliente especifica el diseño
- Requiere mínimo espacio
- **Objetivos:** minimizar tiempos de entrega, tener capacidad de respuesta disponible, flexibilidad, control de cambios

Imagen: estructura metálica de nave industrial en construcción, con grúas y andamios (obra civil hecha a medida).

## Slide 9

**Entornos de Producción (penetración de orden) — Make to Order (MTO).**
"Fabricación a pedido"
- Se produce a pedido, normalmente existe catálogo preexistente
- El cliente decide adquirir o no el producto
- Requiere mínimo espacio
- **Objetivos:** minimizar tiempos de entrega, tener capacidad de respuesta disponible, flexibilidad

Imagen: mueble/cómoda de madera tallada estilo clásico en un ambiente decorado (producto de catálogo fabricado a pedido).

## Slide 10

**Actividad 2** (slide de texto, sin elementos visuales relevantes más allá del layout estándar):
"Brindar ejemplos de por lo menos 4 productos para cada categoría."
"Indicar las ventajas y desventajas para cada tipo de configuración."

## Slide 11

Slide separadora de sección "2 — Configuraciones de proceso-producto". Fondo foto edificio UTEC con overlay celeste (decorativa). Encabezado "Inventory Management", autor "José Antonio Larco".

## Slide 12

**Matriz producto / proceso: Entender el contexto — Proyecto.**
"El proyecto sucede cuando se producen bienes únicos altamente configurables. Generalmente suceden en contextos de ETO y MTO."

Imagen: fotografía aérea de un astillero/dique donde se construye un barco (casco naranja sobre andamios), ejemplo de producción tipo "Proyecto".

## Slide 13

**Matriz producto / proceso: Entender el contexto — Job Shop.**

Diagrama de flujo de un job shop: 6 máquinas ("Machine 1" a "Machine 6") organizadas en 2 filas de 3, conectadas entre sí por flechas de colores (naranja, roja, verde, azul) que muestran múltiples rutas posibles entre máquinas — no un flujo lineal único. Entradas representadas por círculos de colores (naranja, azul, verde, rojo = "Travail en attente"/trabajo en espera) y salidas por cuadrados de colores (= "Travail fini"/trabajo terminado). Las flechas cruzadas entre Machine 1-2-3 (fila superior) y Machine 4-5-6 (fila inferior) ilustran que cada pedido puede seguir una ruta distinta según sus necesidades.

Imagen: taller de carpintería con máquinas dispersas (sierras, prensas) sin línea fija, ejemplo real de job shop.

Texto: "Se tienen múltiples rutas de producción con baja utilización de equipos. Se ofrece mucha variedad de productos. Se puede usar para ETO, MTO, ATO o MTS"

## Slide 14

**Matriz producto / proceso: Entender el contexto — Batch Shop.**

Diagrama de proceso por lotes: 3 estaciones de trabajo (A, B, C) con un operario en cada una, conectadas linealmente. Entre estaciones hay pilas de inventario en proceso ("work-in-process") representadas como cajas apiladas. Flujo: raw material → estación A → work-in-process → estación B → work-in-process → estación C → finished goods.

Imagen: planta textil con máquina de teñido/proceso y conos de hilo de colores (naranja, azul, verde) apilados, ejemplo de producción por lotes.

Texto: "Trabajo por lotes, se tiene inventario en proceso y algunas rutas de producción definidas. Se ofrece una variedad de productos intermedia. Usualmente se usa para ATO/MTS."

## Slide 15

**Matriz producto / proceso: Entender el contexto — Flow Shop.**

Diagrama: 4 máquinas en línea recta y secuencial ("Machine 1" → "Machine 2" → "Machine 3" → "Machine 4"), encerradas en un recuadro, representando una línea de flujo fija sin rutas alternativas.

Imagen: render 3D de una línea de ensamblaje robotizada/automatizada con operarios en distintas estaciones consecutivas.

Texto: "Se trabaja una pieza a la vez o un lote fijo a la vez. Se utiliza un ritmo de producción balanceado en la línea utilizando el concepto de Takt-time. Los productos son discretos y usualmente se usa para ATO/MTS."

## Slide 16

**Matriz producto / proceso: Entender el contexto — Matriz Producto-Proceso (Hayes & Wheelwright).**

Tabla/matriz 2D con eje horizontal "Product Structure & Product Life Cycle Stage" (columnas: I. Low volume-low standardization/one of a kind; II. Multiple products, low volume; III. Few major products, higher volume; IV. High volume-high standardization, commodities) y eje vertical "Process Structure & Process Life Cycle Stage" (filas: I. Jumbled flow (job shop); II. Disconnected line flow (batch); III. Connected line flow (assembly line); IV. Continuous flow).

La matriz forma una diagonal de celdas válidas (fondo celeste) donde se ubican ejemplos reales con círculos etiquetados:
- Fila I × Columna I: "Commercial Printer"
- Fila II × Columna II: "Heavy Equipment"
- Fila III × Columna III: "Automobile Assembly"
- Fila IV × Columna IV: "Sugar Refinery"

Flechas azules diagonales conectan los círculos en secuencia (Commercial Printer → Heavy Equipment → Automobile Assembly → Sugar Refinery), mostrando la progresión natural diagonal de la matriz.

Las esquinas superior-derecha e inferior-izquierda están marcadas en azul oscuro como "No Companies" (combinaciones que no ocurren en la práctica: bajo volumen con proceso continuo, o alto volumen con job shop).

## Slide 17

**Matriz producto / proceso: Entender el contexto — Matriz Producto-Proceso aplicada (caso Lynchburg/TI).**

Misma matriz que en la slide 16 ("Product-Process Matrix*", adaptada de Hayes & Wheelwright, Exhibit 2, p.137), pero ahora con ejemplos de una empresa (círculos amarillos "Lynchburg #1", "Lynchburg #2 & 3", "Lynchburg #4", "Lynchburg #5") y de un competidor/comparación (círculos verdes "TI old watch", "TI new watch"), distribuidos en distintas celdas de la matriz mostrando cómo diferentes líneas de producto de una misma empresa ocupan distintas posiciones proceso-producto.

Ejes rotulados con las dimensiones estratégicas:
- Eje vertical (arriba hacia abajo, lado izquierdo): "MTO" (arriba) → "MTS" (abajo), y a la izquierda "Calidad/Flexibilidad/Tiempo de entrega" (arriba) → hacia "Eficiencia/Costo" (abajo, vía columna derecha "Dependability-Cost")
- A la derecha: "Calidad/Flexibilidad/Tempo de entrega" (arriba, con "Key management tasks" detallados: fast reaction, loading plant, estimating capacity, estimating costs and delivery times, breaking bottlenecks; luego systematizing diverse elements, developing standards, balancing process; luego managing large specialized operations; luego meeting material requirements, running equipment at peak efficiency, raising required capital) y "Eficiencia/Costo" (abajo)
- Fila inferior de la tabla: "Dominant competitive mode" por columna — Custom design/General purpose/High margins (col I); Custom design/Quality control/Service & High margins (col II); Standardized design/Volume production/Finished goods Inv/Back up suppliers (col III); Vertical integration/Long runs/Specialized equipment & processes/Economies of scale (col IV)
- Eje horizontal inferior: "Flexibility-Quality" (izquierda) → "Dependability-Cost" (derecha)

Este slide combina el marco teórico de la matriz producto-proceso con las implicancias estratégicas de dónde se posiciona cada línea de producto.

## Slide 18

**Mensajes finales** (slide de texto, sin elementos visuales):
1. Entender qué tipo de configuración de operaciones tenemos determina qué objetivos son más importantes y qué tipo de decisiones de gestión de operaciones son más críticas.
3. Dos posibles criterios son:
   a. Por punto de desacople (describe qué operación se realiza)
   b. Por tipología de proceso (describe el tipo de proceso)

(Nota: la numeración original salta de 1 a 3, sin ítem 2 — se transcribe tal cual aparece en la slide.)
