---
curso: POWERBI
titulo: 11 - Semana 9/Data Storytelling 1__pptx
slides: 23
fuente: 11 - Semana 9/Data Storytelling 1__pptx.pdf
---

## Slide 1

Portada. Título "Data Storytelling" sobre fondo celeste/cian con foto arquitectónica del edificio UTEC (decorativa). Logo UTEC y tagline "Reinventa el mundo" (chrome decorativo).

## Slide 2

Título "Objetivo". Texto dentro de un recuadro con corchetes decorativos:
"Comprender, diseñar y aplicar de técnicas de narración con datos (data storytelling) para comunicar hallazgos de manera clara, convincente y orientada a la acción.
Se busca transformar la manera en que se presentan los datos pasando de simples informes numéricos o visuales a historias que conecten emocionalmente con la audiencia y faciliten la toma de decisiones informadas."

## Slide 3

Título "Contenido de sesión aquí". Diagrama de 4 bloques numerados (01-04), cada uno con un corchete decorativo, en línea horizontal:
- 01: ¿Qué es visualización de datos?
- 02: Herramientas de visualización de datos
- 03: ¿Qué es Data Storytelling?
- 04: Pasos para crear Data Storytelling

## Slide 4

Slide separador de sección "01. ¿Qué es Visualización de datos?" con ícono de portapapeles/checklist. Fondo celeste degradado.

## Slide 5

Título "¿Qué es visualización de datos?". Dos citas textuales enmarcadas:
- "La representación gráfica de datos o conceptos, que tiene como resultado una imagen mental o un artefacto externo que ayude a la toma de decisiones" — Colin Ware
- "La representación visual de información diseñada para permitir la comunicación, el análisis, el descubrimiento y la exploración" — Alberto Cairo

## Slide 6

Título "¿Qué es visualización de datos?". Captura de pantalla de un dashboard de ejemplo (marca "solver", Healthcare - Clinical Dashboard) con filtros de Month=October y Year=2021 resaltados en un recuadro rojo. El dashboard muestra 6 gráficos: "# of Admissions by DRG" (barras verdes por categoría clínica), "# of Readmissions by DRG" (barras azules), "Average Charge by DRG" (barras verdes), "Admissions & Readmissions - Trend" (barras apiladas verde/azul por mes, enero-diciembre), "Average Length of Stay" (barras verdes por mes), "Count by Patient Type" (gráfico de torta: Emergency Room, Inpatient, Outpatient con valores 3031/3027/1315). A la derecha, lista numerada:
1. Buenas prácticas de visualización de datos.
2. Uso moderado del color.
3. Análisis y exploración.
3. (repetido en el original) Intervienen 2 elementos: Los datos y la visualización

## Slide 7

Título "¿Qué es visualización de datos?". Subtítulo "Texto descriptivo:" con bullets:
- Se utilizan en tableros exploratorios.
- Son fáciles de detectar porque no enfatizan la conclusión.
- Ejemplo: Devoluciones por motivo.

Gráfico de barras horizontales "Devoluciones por motivo" (color azul oscuro):
| Motivo | % |
|---|---|
| Descripción errónea de los productos en la web | 64% |
| Cambio de talla | 15% |
| Producto defectuoso | 9% |
| Por ser regalo | 7% |
| No especifica | 5% |

## Slide 8

Título "Beneficios de la visualización de datos". Diagrama de proceso horizontal con 5 flechas/chevrones numerados (cian degradado), conectados por una línea punteada con círculos:
- 01: Transformar texto y números en el elemento visual
- 02: Provoca respuestas emocionales
- 03: Se comparte con más facilidad
- 04: Se permite comparaciones sencillas
- 05: Ayuda a la toma de decisiones

## Slide 9

Título "Errores comunes:" — subtítulo "No identificar la necesidad". Lista de 6 necesidades/requerimientos de ejemplo (estilo lista de requisitos de negocio):
1. Poder ver por año el total de nuevas y malas contrataciones, divididos por género.
2. Identificar la evaluación mensual de nuevas contrataciones.
3. Poder comparar las nuevas contrataciones con el año anterior.
4. Analizar las nuevas contrataciones por rango de edad y género.
5. Por región analizar las nuevas y malas contrataciones.
6. Identificar las contrataciones por Grupo económico.

Captura de pantalla de dashboard "mSoluciona — Proyecto de análisis de empleados" con selector de Año, que muestra: donut "Nuevas contrataciones" (125.1), barras "Nuevas contrataciones por tipo", gráfico de línea "Nuevas contrataciones Vs Nuevas contrataciones AA" (dos líneas: naranja y roja), barras agrupadas "Nuevas contrataciones por edad y sexo", donut "Malas contrataciones" (125.1), barras "Nuevas contrataciones Vs Malas contrataciones por región", barras "Nuevas contrataciones Vs Malas contrataciones". El dashboard sirve de ejemplo de exceso de gráficos sin necesidad clara.

## Slide 10

Título "Errores comunes:" — subtítulo "Filtros complejos". Comparación de dos wireframes de dashboard lado a lado:
- Izquierda: "Dashboard" con 10 íconos de embudo (filtro) visibles arriba, 4 bloques de contenido gris debajo. Texto: "Al enfrentarse con demasiados filtros, los usuarios tendrán una lucha para la toma de decisiones."
- Derecha: "Dashboard" con un solo ícono de embudo naranja resaltado en un panel lateral (con ícono de cursor/click), 4 bloques de contenido. Texto: "Para filtros complejos, manténgalos detrás de un panel de filtros expandibles."

## Slide 11

Título "Errores comunes:" — subtítulo "Filtros complejos" (continuación). Texto: "Cuando el propósito no está claro, los filtros intervienen para llenar el vacío. Un tablero siempre debe tener un propósito que debería: Sea claro, conciso y preciso."

Dos diagramas comparativos BEFORE/AFTER:
- Diagrama izquierdo (estilo boceto/notas): BEFORE muestra flujo "DATA SELECTION (900M rows, 250 fields) → PURPOSE ('quiero ver rendimiento de 30 indicadores cruzados con 14 dimensiones sobre todo el dataset') → PROTOTYPE (dashboard con 14 filtros)". AFTER (flujo invertido, orden correcto): PURPOSE ('quiero ver qué proveedor entregó sus envíos a tiempo o no') → DATA SELECTION (Metrics: On-time delivery, Delivery time, Avg days late → Dimensions: Date, Country, Supplier, Shipment ID) → PROTOTYPE (dashboard eficiente con pocos filtros: "Supplier performance", trend line, comparison by supplier, port to whole, details by supplier).
- Diagrama derecho: esquema de arquitectura de datos. BEFORE: 3 cilindros de base de datos que confluyen en múltiples conectores hacia un dashboard con ícono de filtro y de carga (loading). AFTER: los mismos 3 cilindros pasan primero por íconos de filtro/embudo individuales antes de confluir en un dashboard limpio de 4 paneles.

## Slide 12

Título "Errores comunes:" — subtítulo "Márgenes". Comparación de dos capturas del mismo dashboard "PRODUCT SALES OVERVIEW" (KPIs: Sales 14.354€, Quantity 2.456, Customers 180, Deliveries 1.735; gráfico de barras por producto, gráfico de líneas por año 2017-2019, barras horizontales por categoría A-D, tabla de calor por día de semana):
- Izquierda: dashboard pegado al borde del contenedor, sin márgenes — marcado con una X roja (incorrecto).
- Derecha: mismo dashboard con márgenes/espaciado alrededor, con flechas indicando el espacio en los 4 bordes — marcado con un check verde (correcto).

## Slide 13

Título "Errores comunes:" — subtítulo "Uso excesivo del color". Comparación de dos gráficos de barras horizontales "Ventas por subcategoría" con los mismos datos:
- Izquierda: cada barra en un color distinto (verde, teal, gris, magenta, verde claro, rojo, azul, etc.) — marcado con X roja.
- Derecha: todas las barras en un solo tono azul/gris (monocromático) — marcado con check verde.

Datos (iguales en ambos gráficos):
| Subcategoría | Ventas |
|---|---|
| Copiadoras | 3.2M |
| Librerías | 3.0M |
| Sillas | 3.0M |
| Teléfonos | 2.9M |
| Electrodomésticos | 1.8M |
| Mesas | 1.4M |
| Almacenamiento | 1.4M |
| Accesorios | 1.4M |
| Mobiliario | 0.6M |
| Carpetas | 0.4M |
| Suministros | 0.4M |
| Sobres | 0.4M |
| Arte | 0.4M |
| Máquinas | 0.4M |
| Papel | 0.4M |
| Grapas | 0.2M |
| Etiquetas | 0.1M |

Texto: "Dificultando la identificación de las métricas importantes. Causa fatiga visual, especialmente con colores brillantes."

## Slide 14

Slide separador de sección "02. ¿Qué es Data Storytelling?" con ícono de portapapeles/checklist. Fondo celeste degradado (mismo estilo que slide 4).

## Slide 15

Título "¿Qué es data storytelling?". Texto: "No es más que un enfoque estructurado sobre cómo comunicamos insights a partir de los datos, e involucra una combinación de tres elementos: datos, visualización y narrativa."

Diagrama de Venn de 3 círculos (Narrative naranja, Visuals rojo, Data azul) que se intersectan en el centro con la etiqueta "CHANGE"; las intersecciones de a pares llevan las etiquetas "Engage" (Narrative-Visuals), "Explain" (Narrative-Data), "Enlighten" (Visuals-Data). Flechas punteadas desde cada círculo apuntan a ejemplos:
- Desde "Narrative": texto "En Colombia la clase media aumenta en un 20% y la tasa de pobreza disminuye en más del 30%"
- Desde "Visuals": captura de infografía médica ("MEDICAL INFOGRAPHIC") con silueta humana e íconos de colores.
- Desde "Data": captura de tabla/gráfico "Total Units by Month and Manufacturer" con líneas de colores por fabricante (Alqui, Natura, Pirum, VanArdel).

## Slide 16

Título "¿Qué es data storytelling?". Subtítulo "Texto explicativo:" con bullets:
- Se utilizan en tableros exploratorios.
- Ayudar a poner en contexto a la audiencia y resaltar el Insight.
- Ejemplo: El 64% de las devoluciones se debe a la descripción errónea de los productos en la web.

Texto destacado sobre el gráfico: "Debido a las devoluciones por descripción errónea de los productos en la web, se tuvo una pérdida de 5.6 M" (con "descripción errónea de los productos en la web" resaltado en azul y negrita).

Mismo gráfico de barras horizontales "Devoluciones por motivo" que en slide 7, ahora con la barra principal (64%, Descripción errónea) en azul oscuro y el resto en gris claro para enfatizar el insight:
| Motivo | % |
|---|---|
| Descripción errónea de los productos en la web | 64% |
| Cambio de talla | 15% |
| Producto defectuoso | 9% |
| Por ser regalo | 7% |
| No especifica | 5% |

## Slide 17

Título "¿Qué es data storytelling?". Diagrama de línea de tiempo horizontal con 6 nodos circulares conectados por una línea: Datos, Maquetar, Explorar, Insight, Historia, Audiencia. Los nodos "Datos", "Explorar" e "Historia" están resaltados en azul/cian (con "Historia" además destacado con fondo azul sólido); "Maquetar", "Insight" y "Audiencia" están en gris. Encima, una flecha curva marcada con una X va desde "Explorar" hasta "Audiencia", saltándose "Insight" e "Historia" — ilustra el error de pasar directo de explorar datos a la audiencia sin construir insight ni historia.

## Slide 18

Slide de pregunta/transición: "¿Por qué los datos necesitan una historia?" en texto grande dentro de un recuadro con corchetes decorativos. Fondo celeste degradado.

## Slide 19

Título "Data Storytelling". Comparación de dos dashboards reales sobre personas desaparecidas (Perú, Ministerio del Interior):
- Izquierda, etiquetado "Dashboard Exploratorios": "PROYECTO PERSONAS DESAPARECIDOS" (año 2022). KPIs: Total Desaparecidos 11,005 (-45%), Hombres Desaparecidos 4,217 (-41%), Mujeres Desaparecidas 6,788 (-48%), Menores Desaparecidos 6,206 (-49%). Gráfico de línea+barras "Evolutivo Desaparecidos" por mes (Ene-Dic). Gráfico de barras divergentes "Desaparecidos por sexo y rango de edad" (Femenino rojo / Masculino azul) por rango: 0-5, 6-11 (6%), 12-17 (25%/69%), 18-29 (23%/16%), 30-59 (30%/8%), 60+ (15%). Scatter plot "Desaparecidos Vs % Desaparecidos" con eje X "Nro Denuncia por Desaparecidos" (log, 1-10,000) y eje Y "Tasa de denuncias por cada 10 mil habitantes" (0-40), puntos coloreados por riesgo (medio=amarillo, bajo=verde), con etiquetas Madre de Dios (1.7), Huancavelica (3.7), Ica (2.4), Lambayeque (4.2), Lima (3.6), línea de "Tasa Prom: 3.3".
- Derecha, etiquetado "Dashboard Aclaratorios": "Personas Desaparecidas — Período de enero a julio del 2022". Dos secciones con conclusiones accionables: "Continuar con el plan de acción — Las personas desaparecidas del 2022 ha disminuido un 4%" (con gráfico de línea doble mostrando evolución mensual Ene-Jul) y "Brindar capacitaciones integrales en los colegios — En los últimos años el 69% de desaparecidos son mujeres de 12 a 17 años" (con barras por rango de edad: 0-5=1%, 6-11=3%, 12-17=69% resaltado en rosa/rojo con nota "Aumentar los efectivos policiales en los colegios", 18-29=16%, 30-59=8%, 60+=4%). Nota adicional: "Que en los últimos 7 meses NO existan departamentos en Riesgo Alto."

## Slide 20

Infografía de ejemplo "Tour de France" (fondo gris oscuro, estilo boceto a mano con tipografía tipo tiza amarilla/blanca), decorada con silueta de bicicleta de fondo. Dos gráficos radiales tipo "sunburst"/reloj:
- Izquierda "Average Pace": muestra el ritmo promedio del ganador cada año 1913-2018 (radios negros distribuidos en círculo, años marcados alrededor: 1913, 1950, 1970, 1990, 2018). Radio cian resalta 1924 = 23.97 km/h (más lento) y radio naranja resalta 1999 = 42.22 km/h (más rápido). Nota al pie: "1924 tuvo el ritmo más lento de 23.97 km/hora" y "1999 tuvo el ritmo más rápido de 42.22 km/hora", con mini gráfico de línea de tendencia debajo.
- Derecha "Total Distance": mismo estilo radial, muestra distancia total del tour por año. Radio cian resalta 1926 = 5,745 km (más largo) y radio naranja resalta 2002 = 3,278 km (más corto). Notas: "1926 fue el Tour de Francia más largo con 5,745 km" y "2002 fue el Tour de Francia más corto con 3,278 km", con mini gráfico de línea de tendencia debajo.

Nota: esta slide no tiene anclas de texto extraído en los chunks (es una infografía en inglés, posiblemente ejemplo de referencia de dataviz insertado como imagen suelta).

## Slide 21

Título "Data Storytelling". Ejemplo de reporte "Netflix — Tamaño del mercado a lo largo del tiempo" (dashboard oscuro estilo Netflix). Gráfico de línea de "Ventas ($USD Billones)" eje Y 0.00-2.50, eje X meses E-D de dos años (2018 y 2019) más forecast: valores anotados $1.87bn, $1.54bn, $1.80bn, $1.96bn, y una proyección punteada roja hasta $2.37bn con etiqueta "FORECAST". Debajo, dos cajas de texto explicativo por año:
- 2018: "Ene-Jun fue un período de estabilidad, con un crecimiento bastante constante (promedio de +3% por mes). Hubo una disminución de casi el 20% en julio, cuando el Producto X fue retirado del mercado." — recuadro rojo: "Las ventas totales se mantuvieron en un volumen reducido durante el resto del año."
- 2019: "$1600 millones, pero aumentó notablemente en febrero, cuando se publicó un nuevo estudio. Las ventas totales han aumentado constantemente desde entonces y se prevé que esto continúe." — recuadro rojo: "El pronóstico más reciente es de $2.400 millones en ventas mensuales para fin de año."

## Slide 22

Título "Conclusiones". Lista de 3 puntos numerados (01-03) con corchetes decorativos dobles (izquierda y derecha):
- 01: Conocer la definición y los beneficios de la visualización de datos.
- 02: Errores comunes al realizar visualización de datos.
- 03: Definición de data storytelling (dashboard aclaratorios)

## Slide 23

Slide de cierre: logo UTEC grande centrado (Universidad de Ingeniería y Tecnología) sobre fondo celeste degradado con patrón hexagonal decorativo. Decorativa, sin contenido de curso.
