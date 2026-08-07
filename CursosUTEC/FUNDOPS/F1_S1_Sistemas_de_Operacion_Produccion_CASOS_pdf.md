---
curso: FUNDOPS
titulo: F1-S1-Sistemas de Operacion-Producción - CASOS
slides: 13
fuente: F1-S1-Sistemas de Operacion-Producción - CASOS.pdf
---

## Slide 1

Portada del curso. Foto de fondo de un edificio de UTEC (decorativa) con overlay azul. Texto: "FUNDAMENTOS DE OPERACIONES" (título grande) y "Semana 1 – Entorno y Sistemas de producción" (subtítulo en franja blanca inferior). Logo UTEC en esquina superior derecha (decorativo).

## Slide 2

Slide de sección/portada, mismo fondo de edificio (decorativa). Texto centrado: "Análisis de casos".

## Slide 3

Slide de sección numerada. Fondo de edificio (decorativa). Texto: "1. ENTORNOS DE PRODUCCIÓN".

## Slide 4

Slide de texto, título "Caso: Cambio de Esquema MTS a ATO". Contenido:

Cuando una empresa decide cambiar a un esquema ATO (assemble-to-order) desde un esquema MTS (make-to-stock) es posible lograr una reducción significativa en el seguimiento y la cantidad de componentes que deben ser almacenados. Por ejemplo, una empresa ha decidido dejar de crear stock de computadoras ensambladas y moverse hacia el enfoque ATO (assemble-to-order). La empresa incluso ha invitado a los clientes al área de trabajo para que vean sus computadoras cuando están siendo ensambladas, la cual es considerada una gran estrategia de relación con el cliente. La empresa estima que existen 7 tipos diferentes de discos duros a elegir, 6 mother boards (incluyendo el procesador), 5 alternativas de CD/DVD, 3 sistemas operativos y 4 opciones adicionales.

Preguntas del caso:
- ¿Cuál es la cantidad posible total de productos terminados?
- Si el costo de generar el pronóstico de la demanda de cada ítem es de $10 por semana, ¿cuál sería el ahorro semanal de pronosticar solamente los componentes comparados con la cantidad potencial de productos terminados?

Solo texto, sin elementos visuales adicionales (aparte de logo UTEC decorativo).

## Slide 5

Slide con la tabla de solución del caso MTS→ATO (misma slide, título "Caso: Cambio de Esquema MTS a ATO"). Contiene una tabla/hoja de cálculo con celdas coloreadas (verde=encabezados, amarillo=datos, naranja=resultados destacados):

**Tabla: CAMBIO DE MTS A MTO**

| Componente | Cantidad |
|---|---|
| Discos Duros | 7 |
| Motherboards | 6 |
| Lectoras de DVD | 5 |
| Sistemas Operativos | 3 |
| Otras Opciones | 4 |

| Concepto | Valor | Nota |
|---|---|---|
| Número Potencial de Prod. Terminados | 2.520 | MTS |
| Costo de Pronóstico x Item (US$) | 10 | |
| Costo Total de Pronóstico de Prod. Terminados (US$) | 25.200 | |
| Costo Total de Pronóstico de Componentes (US$) | 250 | ATO |
| **Ahorro (US$)** | **24.950** | |

Nota: 2.520 = 7×6×5×3×4 (combinaciones de componentes = productos terminados potenciales bajo MTS). El pronóstico bajo ATO solo requiere pronosticar 25 componentes (7+6+5+3+4=25) en vez de 2.520 productos terminados, generando el ahorro de US$24.950/semana.

## Slide 6

Título: "Analice los siguientes casos e indique a que entorno corresponde:" — CASO 1 (resaltado en amarillo).

Texto: Suponga que su mejor amigo está próximo a contraer matrimonio y le ha pedido que sea su padrino de bodas. Para la ceremonia Ud. ha pensado en adquirir un smoking. Ud. ha encontrado una tienda que ofrece algunos modelos de smoking. La tienda dispone de un modelo que le agrada, en la talla exacta, por lo que Ud. decide comprarlo inmediatamente.

Imagen a la derecha: fotografía de una tienda de ropa formal, mostrando un smoking blanco con solapas negras exhibido en un maniquí sin cabeza, junto a un estante con accesorios (tirantes, moños, cinturones, calzado, pañuelos de bolsillo) sobre un fondo de pared azul oscuro. Ilustra el escenario de compra directa de un producto terminado en tienda (entorno tipo MTS/compra inmediata de stock).

## Slide 7

Título: "Analice los siguientes casos e indique a que entorno corresponde:" — CASO 2 (resaltado en verde).

Texto: Una empresa que fabrica equipos médicos recibe un pedido para un dispositivo específico que debe ser ajustado a las necesidades de un paciente en particular. La producción del dispositivo comienza solo después de recibir las especificaciones del médico. La producción se realiza bajo pedido, permitiendo la personalización y asegurando que el equipo cumpla con los requisitos específicos del paciente.

Imagen a la derecha: ilustración/clipart de equipos médicos variados — estetoscopio, tensiómetro (esfigmomanómetro azul), frasco de medicina, tijeras quirúrgicas, curitas, jeringa, termómetro digital, ampollas, gotero, blíster de pastillas y mascarilla con cruz médica. Refuerza el contexto de fabricación de dispositivos médicos personalizados (entorno tipo ETO/MTO).

## Slide 8

Título: "Analice los siguientes casos e indique a que entorno corresponde:" — CASO 3 (resaltado en celeste).

Texto: Suponga que su mejor amigo está próximo a contraer matrimonio. La novia es una persona que le gusta estar muy a la moda y tiene una obsesión por un modelo exclusivo. Desde niña ha soñado en casarse con un vestido similar a un cuento de hadas. Ninguna tienda tiene algo parecido a lo que ella desea y un sastre le ha dicho que lo que ella desea es algo muy complicado. La novia no se rinde y decide encargar la confección de su vestido a un famoso diseñador de Nueva York.

Imagen a la derecha: fotografía de una modelo con vestido de novia de encaje blanco con cola larga, posando frente a una chimenea de mármol decorada con flores, en un ambiente elegante. Ilustra el escenario de un producto único, diseñado y confeccionado a medida (entorno tipo ETO — engineer-to-order).

## Slide 9

Título: "Analice los siguientes casos e indique a que entorno corresponde:" — CASO 4 (resaltado en celeste).

Texto: Una empresa de muebles modulares ofrece a los clientes la posibilidad de elegir diferentes módulos y acabados para crear un mueble personalizado. Los módulos se mantienen en inventario y se ensamblan según el pedido del cliente. Los módulos están pre-fabricados y en inventario, y el ensamblaje final se realiza tras recibir el pedido.

Imagen debajo del texto: fotografía de un taller/almacén de carpintería con piezas de madera y módulos de mueble sin terminar (estantes, cajones, paneles) apilados y en proceso, marca de agua "dreamstime" visible en varias partes de la imagen. Ilustra componentes prefabricados en inventario listos para ensamblar según pedido (entorno tipo ATO — assemble-to-order).

## Slide 10

Slide de sección numerada. Fondo de edificio (decorativa). Texto: "3. SISTEMAS DE PRODUCCIÓN".

## Slide 11

Título: "Analice los siguientes casos e indique a que SISTEMA corresponde:" — CASO 1 (resaltado en verde).

Texto: "Fabricación de Ropa de Temporada": Una empresa de moda produce grandes cantidades de ropa de temporada basándose en pronósticos de demanda. La producción se realiza antes de que los pedidos lleguen a las tiendas. La producción se basa en previsiones de demanda y se realiza antes de recibir pedidos específicos.

Preguntas (en color celeste, para discusión):
- ¿Sistema PUSH?
- ¿Sistema PULL?

Sin imágenes, solo texto.

## Slide 12

Título: "Analice los siguientes casos e indique a que SISTEMA corresponde:" — contiene CASO 2 y CASO 3 (ambos resaltados en verde).

**CASO 2 — Fabricación de Automóviles Bajo Pedido** (subtítulo resaltado en gris):
Un fabricante de automóviles produce vehículos solo después de recibir pedidos específicos de los clientes, permitiendo la personalización de características como el color y los accesorios. La producción se basa en pedidos específicos y se realiza en respuesta a la demanda real.

Preguntas (en celeste): ¿Sistema PUSH? / ¿Sistema PULL?

**CASO 3 — Producción de Alimentos en Conserva:**
Una fábrica de alimentos en conserva produce grandes lotes de productos como sopas y vegetales enlatados, anticipando la demanda futura y almacenándolos hasta que se distribuyan a los minoristas. La producción se realiza en grandes lotes basándose en previsiones de demanda.

Sin imágenes, solo texto (dos casos en una misma slide).

## Slide 13

Slide de cierre/contraportada institucional (decorativa). Fotografía de una escalera de concreto azul dentro de un edificio de UTEC, con overlay de color turquesa semitransparente sobre parte de la imagen. Logo UTEC "Universidad de Ingeniería y Tecnología" centrado. En la pared del fondo se leen nombres de carreras de ingeniería (Mecatrónica, Bioingeniería, Ciencia de la Computación, Ambiental, Energía, Industrial, Electrónica — parcialmente visibles, decorativo). No contiene contenido académico del capítulo.
