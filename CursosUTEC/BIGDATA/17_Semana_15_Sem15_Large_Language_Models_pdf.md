---
curso: BIGDATA
titulo: 17 - Semana 15/Sem15_Large Language Models
slides: 44
fuente: 17 - Semana 15/Sem15_Large Language Models.pdf
---

## Slide 1

Portada (decorativa: fondo cian con patrón hexagonal, foto del edificio UTEC, cruz amarilla).

Título: **LLM y Optimización**
Mg. Aldo Lezama Benavides — Semana 15

## Slide 2

**Objetivo de la sesión** (lista dentro de un marco de corchetes blancos)

1. **Comprender** los fundamentos de los Large Language Models (LLM), su arquitectura Transformer y las características que les permiten procesar y generar lenguaje natural.
2. **Analizar** las principales técnicas de optimización de LLM, incluyendo Knowledge Distillation, Quantization y Pruning, identificando su funcionamiento y objetivos.
3. **Evaluar** el impacto de las técnicas de compresión de modelos en la reducción del consumo de memoria, el costo computacional y la latencia de inferencia, manteniendo un rendimiento competitivo.

## Slide 3

**Contenido de la sesión** — cuatro columnas numeradas, cada una dentro de corchetes blancos:

| 01. | 02. | 03. | 04. |
|---|---|---|---|
| Large Language Models | Distillation | Quantization | Pruning |

## Slide 4

Separador de sección: número grande **01.** entre corchetes + icono de portapapeles con checklist + título **Large Language Models**.

## Slide 5

**Large Language Models**

Un Large Language Model (LLM) es un modelo de inteligencia artificial entrenado sobre enormes volúmenes de texto con el objetivo de comprender y generar lenguaje natural.

Los LLMs están basados en arquitecturas Transformer y utilizan miles de millones de parámetros para aprender patrones lingüísticos, relaciones semánticas y conocimiento general contenido en grandes colecciones de documentos.

A diferencia de los modelos tradicionales de Machine Learning, los LLMs no siguen reglas predefinidas. En su lugar, aprenden representaciones estadísticas del lenguaje a partir de grandes cantidades de datos.

**Visual (derecha):** imagen sobre fondo azul oscuro con un nodo central rotulado "LLM / LARGE LANGUAGE MODEL" conectado por líneas a ~18 iconos circulares en red: micrófono, capas apiladas, documento, bocadillo de chat, gráfico de barras, base de datos, sobre de correo, bombilla, birrete, llave inglesa, red neuronal, cubo/estructura, estrella, flechas cruzadas, checklist, engranaje. Ilustra que un LLM alimenta múltiples tareas/modalidades.

## Slide 6

**Large Language Models**

**Características principales**
- Aprenden a partir de grandes corpus de texto.
- Comprenden el contexto de una conversación.
- Generan texto coherente y fluido.
- Pueden resolver múltiples tareas sin necesidad de entrenar un modelo diferente para cada una.

**Visual (derecha):** la misma imagen de red de iconos con el nodo central "LLM" de la slide anterior.

## Slide 7

**Arquitectura Transformer**

La mayoría de los modelos modernos, como GPT, Llama y Mistral, utilizan la arquitectura Transformer, propuesta en 2017. Sus componentes principales son:

- **Embeddings** — Transforman las palabras o tokens en vectores numéricos.
- **Self-Attention** — Permite que cada palabra analice la importancia de todas las demás palabras de la oración.
- **Feed Forward Network (FFN)** — Procesa la información obtenida por la atención mediante una red neuronal completamente conectada.
- **Capas Transformer** — Estos bloques se repiten decenas o cientos de veces para construir modelos de gran capacidad.

**Visual (derecha):** el diagrama canónico de "Attention Is All You Need", dos columnas (encoder izquierda, decoder derecha), ambas marcadas `N×`:

- **Encoder:** `Inputs` → `Input Embedding` → suma (⊕) con `Positional Encoding` → `Multi-Head Attention` → `Add & Norm` → `Feed Forward` → `Add & Norm`. Conexiones residuales dibujadas alrededor de cada subcapa.
- **Decoder:** `Outputs (shifted right)` → `Output Embedding` → ⊕ `Positional Encoding` → `Masked Multi-Head Attention` → `Add & Norm` → `Multi-Head Attention` (recibe flechas cruzadas desde la salida del encoder) → `Add & Norm` → `Feed Forward` → `Add & Norm` → `Linear` → `Softmax` → `Output Probabilities`.

Código de color: Add & Norm en amarillo, Feed Forward en celeste, atención en naranja, embeddings en rosa, Linear en violeta, Softmax en verde.

## Slide 8

**Millones de parámetros**

Los parámetros son los pesos que la red neuronal aprende durante el entrenamiento y representan el conocimiento almacenado por el modelo.

A mayor cantidad de parámetros:
- mayor capacidad de aprendizaje;
- mejor representación del lenguaje;
- mayor consumo de memoria;
- mayor costo computacional;
- mayor tiempo de inferencia.

No obstante, un mayor número de parámetros no garantiza siempre mejores resultados. Modelos más pequeños y bien optimizados pueden ofrecer un rendimiento comparable en tareas específicas.

**Tabla (derecha):**

| Modelo | Parámetros |
|---|---|
| BERT Base | 110 millones |
| GPT-2 Large | 774 millones |
| Llama 3 8B | 8 mil millones |
| Llama 3 70B | 70 mil millones |

## Slide 9

**Necesidad de optimización** (solo texto)

Los LLMs modernos requieren enormes recursos computacionales. Por ejemplo, un modelo de varios miles de millones de parámetros puede necesitar decenas o cientos de gigabytes de memoria para ejecutarse en formato FP32. Esto genera varios desafíos:
- alto consumo de memoria;
- elevada latencia de inferencia;
- mayor consumo energético;
- altos costos de infraestructura;

Para resolver estos problemas se emplean técnicas de compresión de modelos, entre ellas:
- **Pruning:** elimina conexiones o parámetros poco relevantes.
- **Quantization:** reduce la precisión numérica de los parámetros.
- **Knowledge Distillation:** transfiere el conocimiento de un modelo grande a uno más pequeño.

## Slide 10

Separador de sección: **02.** + icono de portapapeles + **Distillation**.

## Slide 11

**¿Qué es Knowledge Distillation?**

La Knowledge Distillation (KD) es una técnica de compresión de modelos en la que un modelo grande y complejo, denominado Teacher, transfiere su conocimiento a un modelo más pequeño y eficiente, denominado Student.

El objetivo no es copiar exactamente los parámetros del modelo grande, sino aprender su comportamiento, permitiendo que el modelo pequeño alcance un rendimiento similar con muchos menos recursos computacionales.

*Idea clave: Distillation no comprime directamente el modelo; aprende una versión compacta de la función que el modelo grande ha aprendido.*

**Visual (derecha):** diagrama en tres bloques punteados.
- **Teacher Model:** red neuronal densa y ancha (capas de nodos naranjas → verdes → amarillos → azules, muchas conexiones).
- **Knowledge Transfer:** caja central con etiqueta vertical "Knowledge"; flecha entrante rotulada **Distill** desde el Teacher y flecha saliente rotulada **Transfer** hacia el Student.
- **Student Model:** red mucho más pequeña (naranja → amarillo → azul, pocas neuronas).
- Debajo, un cilindro rosado **Data** con flechas que suben tanto al Teacher como al Student (ambos ven los mismos datos).

## Slide 12

**Arquitectura Teacher–Student y Aprendizaje**

En lugar de aprender únicamente la respuesta correcta, el Student aprende las probabilidades completas que produce el Teacher.

Estas probabilidades contienen información rica sobre la relación entre las distintas respuestas posibles. El Student aprende no solo qué respuesta es correcta, sino también qué respuestas son similares o plausibles según el Teacher.

**Visual (derecha):** dos esquemas comparados.
- **Learning from Teacher (LfT):** `Teacher LLM` (caja azul) --Generate--> `Teaching Materials` (caja gris) --Teach--> `Student LLM` (caja verde). Anotación roja: *Improve the student -- Inherit teacher knowledge*.
- **Learning by Teaching (LbT):** misma cadena Teacher → Teaching Materials → Student, pero el Student envía *Provide feedback* a una caja roja `Feedback`, que retroalimenta al Teacher con la anotación *Improve the teacher -- Build more rigorous and clear knowledge*; al lado, "e.g., exam results, questions".

## Slide 13

**Función de pérdida en Distillation**

El entrenamiento busca minimizar la diferencia entre las predicciones del Student y las del Teacher.

1. **Cross-Entropy Loss** — Compara las predicciones del Student con las etiquetas reales. Objetivo: aprender la respuesta correcta.
2. **KL Divergence** — Compara las probabilidades generadas por el Student con las del Teacher. Objetivo: que el Student imite el comportamiento del Teacher.
3. **Pérdida Combinada (la más utilizada)** — Combina Cross-Entropy + KL Divergence. Objetivo: aprender tanto de las etiquetas reales como del conocimiento del Teacher.

Formulación implícita: $\mathcal{L} = \mathcal{L}_{CE}(y, p_S) + \lambda\, D_{KL}(p_T \Vert p_S)$

**Visual (derecha):** diagrama de destilación por capas entre dos CNNs. Arriba, **Teacher CNN (Pre-Trained)** en naranja: `Input Image` → Conv Group1 → Pooling → Conv Group2 → Pooling → Conv Group3 → … Abajo, **Student CNN (Pruned From Teacher CNN)** en azul con la misma secuencia Conv Group1/2/3 y Poolings. Entre ambas ramas, en cada nivel, un bloque **MSE Loss**; los MSE Loss se suman (`+ … +`) y desembocan en una caja punteada **Distill Loss**.

## Slide 14

Dos tarjetas grandes.

**Ventajas** (marco verde, texto verde)
- Reduce significativamente el número de parámetros.
- Disminuye el consumo de memoria.
- Reduce el costo de inferencia.
- Mejora la velocidad de respuesta.
- Facilita el despliegue en dispositivos Edge y móviles.

**Aplicaciones** (marco azul, texto azul)
- Versiones compactas de modelos GPT.
- Asistentes virtuales.
- Chatbots empresariales.
- Modelos para smartphones.
- Sistemas de búsqueda y recomendación

## Slide 15

**Casos de Knowledge Distillation** — tabla con cabecera en beige:

| Modelo Teacher | Modelo Student | Parámetros | Reducción | Rendimiento aproximado |
|---|---|---|---|---|
| BERT Base | DistilBERT | 110 M → 66 M | 40% menos parámetros | Conserva aproximadamente **97%** del rendimiento de BERT y es **~60% más rápido** en inferencia. |
| BERT Large | TinyBERT | 340 M → 14.5 M | ≈96% menos parámetros | Mantiene entre **96% y 97%** del rendimiento de BERT en múltiples tareas NLP. |
| BERT Base | MobileBERT | 110 M → 25 M | ≈77% menos parámetros | Conserva alrededor del **99%** del desempeño en tareas de comprensión del lenguaje y ofrece una inferencia mucho más rápida en dispositivos móviles. |
| RoBERTa Large | MiniLM | 355 M → 33 M | ≈91% menos parámetros | Conserva más del **99%** del rendimiento en tareas de recuperación y comprensión del lenguaje, siendo varias veces más rápido. |
| GPT-3 | Modelos GPT destilados (investigación) | 175 B → 1–13 B | Más del 90% de reducción | Mantienen buena calidad para tareas específicas, reduciendo significativamente el costo de inferencia. No existe una versión oficial destilada de GPT-3 publicada por OpenAI. |

## Slide 16

Separador de sección: **03.** + icono de portapapeles + **Quantization**.

## Slide 17

**Quantization**

Es una técnica de compresión de modelos que consiste en reducir la precisión numérica utilizada para representar los pesos y las activaciones de una red neuronal. En lugar de almacenar los parámetros utilizando números de alta precisión, como 32 bits, se emplean representaciones de menor precisión, como 16, 8 o incluso 4 bits. La cuantización no elimina parámetros ni modifica la arquitectura del modelo. Todos los pesos permanecen presentes; únicamente cambia la forma en que son representados en memoria.

El objetivo principal es disminuir el consumo de memoria, reducir el costo computacional y acelerar la inferencia, manteniendo una pérdida mínima de precisión.

*Idea clave: La Quantization no reduce el número de parámetros; reduce el número de bits utilizados para representar cada parámetro.*

**Visual (derecha):** esquema de cuantización absmax FP32 → INT8.
- Fila superior de celdas moradas con valores FP32: `5.47 | 3.08 | -7.59 | 0 | -1.95 | -4.57 | 10.8`; la última celda (10.8) resaltada en cian y anotada **highest absolute value (α)**.
- Debajo, una recta numérica morada de `min = -α = -10.8` a `max = α = 10.8` con puntos en -7.59, -4.57, -1.95, 0, 3.08, 5.47.
- Líneas punteadas mapean cada punto a una segunda recta rosada que va de `min = -127` a `max = 127` con el 0 alineado en el centro.
- Fila inferior de celdas rosadas con los enteros resultantes: `64 | 36 | -89 | 0 | -23 | -54 | 127`; la celda 127 anotada **highest value INT8 can take**.
- Pie: **0 in FP32 = 0 in INT8**.

## Slide 18

**¿Por qué funciona la Quantization?**

Durante el entrenamiento, los pesos de una red neuronal se almacenan normalmente en formato Float32 (32 bits). Sin embargo, numerosos estudios han demostrado que no siempre es necesario utilizar una precisión tan elevada para realizar inferencias.

Al reducir la cantidad de bits por parámetro:
- disminuye el tamaño del modelo;
- se reduce el tráfico de memoria;
- aumentan las operaciones por segundo que puede realizar el hardware.

La mayoría de procesadores modernos (CPU, GPU y aceleradores de IA) incorporan instrucciones optimizadas para operaciones en INT8, lo que permite ejecutar los modelos significativamente más rápido.

**Visual (derecha):** panel titulado **Quantization** con dos ejemplos.
- Escalar: **Floating Point** `1231.4531` --flecha verde--> **Integer** `1231`.
- Matricial: bajo **32 bit** una matriz 3×3 `0.21, -0.37, -2.54 / 4.5, 4.37, -0.78 / 5.1, 0.01, 9.6`; flecha verde rotulada *Quantization* hacia **8 bit** con la matriz `21, 37, 25 / 45, 43, 78 / 51, 23, 96`.

## Slide 19

**Comparación de Métodos de Quantization** — dos flujogramas lado a lado.

**Post-Training Quantization (PTQ)** (izquierda)
`Train Model with FP32` (verde) → `Trained FP32 Model` (azul) → `Apply Quantization (8-bit INT)` (rosa), que también recibe `Calibration Dataset` (amarillo) → `Quantized INT8 Model` (rojo).
Bullets: Fast process (minutes) · No retraining needed · Small calibration dataset · Simple implementation. Contras (gris): Potential accuracy loss · Less optimization flexibility · Not ideal for sensitive models.

**Quantization-Aware Training (QAT)** (derecha)
`Optional: Pre-train with FP32` → `Train with Fake Quantization Nodes` (verde) → `Forward: Simulated Q/DQ, Backward: STE` (azul), alimentado por `Full Training Dataset` (amarillo) → `Quantized INT8 Model` (rojo).
Bullets: Better accuracy preservation · Model adapts to quantization · Finer control over trade-offs. Contras (gris): Time-consuming (days/weeks) · Full retraining required · More complex implementation.

Texto al pie:
- **PTQ:** La cuantización se aplica después de que el modelo ha sido entrenado. No requiere volver a entrenar la red. Es rápida y sencilla de implementar. **Ventaja:** ideal cuando ya se dispone de un modelo entrenado.
- **QAT:** Durante el entrenamiento se simula el efecto de la cuantización. El modelo aprende desde el inicio a trabajar con baja precisión. **Ventaja:** generalmente consigue mayor precisión que PTQ. **Desventaja:** requiere volver a entrenar el modelo.

## Slide 20

**Proceso de Quantization** — solo texto.

**Etapa 1: Modelo entrenado (FP32)**
El proceso de cuantización parte de un modelo previamente entrenado, cuyos pesos y activaciones se encuentran representados normalmente en formato Float32 (FP32). Esta representación utiliza 32 bits por cada parámetro, proporcionando una alta precisión numérica durante el entrenamiento.

Aunque FP32 ofrece excelentes resultados, también implica un elevado consumo de memoria y una mayor cantidad de operaciones aritméticas durante la inferencia. Por esta razón, el modelo constituye el punto de partida para aplicar técnicas de cuantización que reduzcan estos requerimientos sin modificar la arquitectura de la red neuronal.

## Slide 21

**Proceso de Quantization** — solo texto.

**Etapa 2: Análisis del rango de valores**
En esta etapa se analiza la distribución de los pesos y activaciones del modelo para determinar los valores mínimo y máximo que deberán representarse con menor precisión. Este análisis permite conocer el rango real de los datos y definir cómo serán transformados al nuevo formato numérico. En algunos métodos también se emplean percentiles para evitar que valores atípicos (outliers) afecten la calidad de la cuantización. El objetivo es conservar la mayor cantidad posible de información utilizando un rango de representación mucho más reducido.

## Slide 22

**Proceso de Quantization** — solo texto.

**Etapa 3: Cálculo del factor de escala (Scale) y punto cero (Zero Point)**
Una vez conocido el rango de valores, se calculan dos parámetros fundamentales:
- **Scale** (factor de escala): determina la relación entre los valores reales y los valores enteros que representarán esos datos.
- **Zero Point** (punto cero): establece qué valor entero representa el cero en la nueva escala numérica.

Estos parámetros permiten transformar los números de punto flotante (FP32) en valores enteros (INT8, INT4, etc.) preservando, en la medida de lo posible, la información contenida en los pesos originales.

## Slide 23

**Proceso de Quantization** — solo texto.

**Etapa 4: Cuantización (Conversión)**
En esta etapa se realiza la conversión propiamente dicha. Cada peso y activación del modelo se transforma desde su representación en punto flotante (FP32) hacia una representación de menor precisión, como INT8 o INT4. Durante este proceso, los valores son escalados y redondeados al entero más cercano dentro del rango permitido. Como consecuencia, el modelo ocupa considerablemente menos memoria y puede ejecutarse utilizando operaciones enteras, que son mucho más eficientes en la mayoría del hardware moderno. Aunque esta conversión introduce una pequeña pérdida de precisión numérica, generalmente el impacto sobre el rendimiento del modelo es reducido.

## Slide 24

**Proceso de Quantization** — solo texto.

**Etapa 5: Ejecución en baja precisión**
Una vez cuantizado, el modelo realiza la inferencia utilizando operaciones de baja precisión, como INT8 o INT4, en lugar de operaciones de punto flotante. Esto permite disminuir significativamente el tiempo de ejecución, el consumo energético y el uso de memoria. Además, muchos procesadores modernos incorporan aceleradores especializados para operaciones enteras, lo que incrementa aún más la velocidad de inferencia. Esta etapa es especialmente importante en aplicaciones donde se requiere responder en tiempo real o ejecutar modelos en dispositivos con recursos limitados.

## Slide 25

**Proceso de Quantization** — solo texto.

**Etapa 6: Validación**
Después de la cuantización, es necesario evaluar el comportamiento del modelo para verificar que la reducción de precisión no haya afectado significativamente su desempeño. Para ello, se comparan métricas como la precisión (Accuracy), la pérdida (Loss), la latencia y el consumo de memoria respecto al modelo original. Si la pérdida de rendimiento se encuentra dentro de un margen aceptable, el modelo cuantizado puede utilizarse en producción. En caso contrario, será necesario ajustar el proceso de cuantización o emplear técnicas más avanzadas, como Quantization-Aware Training (QAT).

## Slide 26

**Proceso de Quantization** — solo texto.

**Etapa 7: Modelo cuantizado listo para despliegue**
La etapa final consiste en obtener un modelo optimizado para su utilización en entornos de producción. El modelo mantiene la misma arquitectura y realiza exactamente la misma tarea que el modelo original, pero requiere menos memoria, consume menos energía y ejecuta la inferencia con mayor rapidez. Gracias a estas características, la cuantización se ha convertido en una técnica fundamental para desplegar Large Language Models (LLMs) en servidores, computadoras personales, dispositivos móviles y sistemas embebidos, permitiendo reducir los costos de infraestructura sin comprometer significativamente la calidad de las predicciones.

## Slide 27

**Flujo de Proceso de Quantization** — infografía de 7 tarjetas numeradas conectadas por flechas de izquierda a derecha:

1. **MODELO ENTRENADO (FP32)** — dibujo de red neuronal densa. "El modelo ha sido entrenado usando precisión de 32 bits (punto flotante)." Etiqueta: *Pesos y activaciones en FP32*.
2. **ANÁLISIS DEL RANGO DE VALORES** — histograma amarillo (eje Y "Frecuencia", eje X "Valor" de mín a máx) con forma acampanada. "Se analizan los pesos y activaciones para determinar sus valores mínimos y máximos (rango)." Etiqueta: *Rango detectado: [min, max]*.
3. **CÁLCULO DE SCALE Y ZERO POINT** — caja verde con fórmulas (ejemplo INT8):

$$\text{scale} = \frac{max - min}{qmax - qmin} \qquad \text{zero\_point} = qmin - \frac{min}{scale}$$

   donde qmin y qmax son los límites del tipo entero (ej. INT8: −128 y 127). Etiqueta: *Obtención de: scale y zero point*.
4. **QUANTIZATION (CONVERSIÓN)** — tabla FP32 → INT8 con flecha "escalar + redondear":

   | FP32 | INT8 |
   |---|---|
   | 2.51 | 127 |
   | -1.23 | -62 |
   | 0.05 | 3 |
   | 1.78 | 90 |
   | -2.30 | -116 |
   | … | … |

   Etiqueta: *Rango INT8: [-128, 127]*.
5. **EJECUCIÓN EN BAJA PRECISIÓN** — iconos: chip = "Operaciones enteras (INT8/INT4)", velocímetro = "Mayor velocidad de inferencia", batería = "Menor uso de memoria y energía".
6. **VALIDACIÓN** — icono de portapapeles con tres checks rojos. "Si la pérdida de precisión es aceptable, se aprueba para despliegue. Si no, se ajusta el proceso (p. ej., QAT u otra configuración)."
7. **MODELO CUANTIZADO LISTO PARA DESPLIEGUE** — icono de base de datos con check. Lista: Menor tamaño · Mayor velocidad · Menor consumo · Listo para producción.

Al pie, una flecha punteada de retorno del paso 7 al paso 1: "Este flujo puede iterarse ajustando la configuración de cuantización hasta alcanzar el mejor equilibrio entre precisión y eficiencia."

## Slide 28

**Ventajas y limitaciones** (de la Quantization) — dos columnas.

**VENTAJAS**
- Reduce considerablemente el tamaño del modelo.
- Disminuye el consumo de memoria.
- Acelera la inferencia.
- Reduce el consumo energético.
- Facilita el despliegue en dispositivos móviles y Edge.
- No modifica la arquitectura de la red neuronal

**LIMITACIONES**
- Puede disminuir ligeramente la precisión.
- Algunos modelos son más sensibles que otros a la reducción de precisión.
- La mejora en velocidad depende del hardware disponible.
- Cuantizaciones muy agresivas (INT4 o INT2) pueden degradar significativamente el rendimiento.

## Slide 29

Separador de sección: **04.** + icono de portapapeles + **Pruning**.

## Slide 30

**Pruning en Modelos de Lenguaje**

Los modelos de lenguaje actuales contienen miles de millones de parámetros. Aunque esta enorme cantidad de parámetros les permite aprender relaciones muy complejas, también provoca que:
- ocupen mucha memoria;
- requieran gran capacidad de procesamiento;
- consuman más energía;
- tengan mayor costo de inferencia

Sin embargo, numerosos estudios han demostrado que no todos los parámetros son igualmente importantes. Muchos contribuyen muy poco a la predicción final.

**Idea clave:** *Si eliminamos los parámetros poco importantes, el modelo puede seguir funcionando casi igual, pero con menor costo computacional.*

**Visual (derecha):** figura **Neuron Pruning** — a la izquierda "before pruning": red densa de nodos azules totalmente conectada; flecha gris; a la derecha "after pruning": la misma red donde dos neuronas están marcadas en rojo y sus conexiones se dibujan en rojo (las eliminadas), quedando menos aristas negras.

## Slide 31

**¿Qué es el Pruning?**

Pruning (poda) consiste en eliminar conexiones, pesos o incluso neuronas que aportan muy poca información al modelo.
La idea proviene de la jardinería.
Así como se poda un árbol para eliminar ramas innecesarias y permitir que crezca de manera más eficiente, en una red neuronal se eliminan conexiones redundantes.
No se agregan parámetros nuevos.
Simplemente se eliminan los menos útiles.

**Visual (derecha):** diagrama clásico de poda. Izquierda **before pruning**: red de 4 capas (5→4→3→2 nodos) totalmente conectada con flechas. Dos etiquetas con flechas punteadas —*pruning synapses* y *pruning neurons*— apuntan a la derecha, **after pruning**: la misma topología pero con muchas menos aristas y varias neuronas intermedias desaparecidas.

## Slide 32

**¿Cómo decide el algoritmo qué eliminar?** — solo texto.

Una de las preguntas más importantes en el proceso de Pruning es determinar qué parámetros pueden eliminarse sin afectar significativamente el rendimiento del modelo. Aunque una red neuronal puede contener millones o incluso miles de millones de pesos, no todos contribuyen de igual manera a la generación de las predicciones. Algunos parámetros capturan patrones fundamentales de los datos, mientras que otros tienen una influencia muy reducida y resultan prácticamente redundantes.

El objetivo del algoritmo de Pruning es asignar un nivel de importancia a cada peso o conjunto de pesos. Aquellos considerados poco relevantes serán candidatos para su eliminación. Existen diversos métodos para medir esta importancia, entre los cuales destacan los siguientes:

a) Magnitud del peso (Weight Magnitude)
b) Sensibilidad del modelo
c) Gradientes
d) Métodos basados en importancia estructural

## Slide 33

**Pruning - Magnitud del peso**

Es el criterio más sencillo y ampliamente utilizado debido a su bajo costo computacional. Parte del supuesto de que un peso con un valor absoluto muy pequeño tiene una influencia limitada sobre la salida del modelo.

Matemáticamente, si un peso $w_i$ cumple

$$|w_i| < \tau$$

donde $\tau$ representa un umbral predefinido, dicho peso puede eliminarse. Este método es muy eficiente porque únicamente requiere inspeccionar el valor de cada parámetro, sin realizar cálculos adicionales. Por ello, es uno de los algoritmos más utilizados para comprimir modelos de gran tamaño.

**Visual (derecha):** esquema con una caja **MODEL WEIGHTS** que contiene una matriz 2×5 de celdas naranjas: fila 1 `2.1 | 0.6 | 0.8 | 5.6 | 3.2`, fila 2 `0.1 | 2.5 | 1.9 | 2.5 | 0.3`. A la izquierda una etiqueta amarilla **PRUNING RATIO = 0.4** que entra a la matriz; a la derecha **MINIMUM MAGNITUDE THRESHOLD** con una etiqueta amarilla **1.0**. Flecha hacia abajo rotulada **PRUNE** hacia la caja **PRUNED WEIGHTS**: fila 1 `2.1 | 0 | 0 | 5.6 | 3.2`, fila 2 `0 | 2.5 | 1.9 | 2.5 | 0` (todos los valores menores a 1.0 pasaron a cero).

## Slide 34

**Pruning – Sensibilidad del modelo** — solo texto.

En este enfoque, la importancia de un peso se mide evaluando cuánto cambia el rendimiento del modelo cuando dicho parámetro es eliminado.

Si al eliminar un peso la función de pérdida (Loss Function) apenas aumenta, significa que ese parámetro tiene poca relevancia para la tarea y puede eliminarse con un impacto mínimo. En cambio, si su eliminación provoca un incremento considerable del error, el peso debe conservarse.

Aunque este método suele producir mejores resultados que el criterio basado únicamente en la magnitud, requiere realizar un mayor número de evaluaciones, incrementando el costo computacional.

## Slide 35

**Pruning – Gradientes**

Otra estrategia consiste en analizar el gradiente asociado a cada peso durante el entrenamiento.

El gradiente indica cuánto contribuye un parámetro a la reducción del error del modelo. Cuando un peso presenta gradientes muy pequeños durante varias iteraciones, significa que modificar dicho parámetro apenas mejora el aprendizaje, por lo que puede considerarse un candidato para el Pruning.

Este enfoque incorpora información sobre el proceso de entrenamiento y permite identificar parámetros que, aunque no sean pequeños en magnitud, tienen poca influencia en la optimización del modelo.

**Visual (derecha):** dos figuras.
- Izquierda: bloque `fc or conv` con flechas rojas de retropropagación: $\frac{dL}{dO}$ entrando desde arriba, $\frac{dL}{dW}$ saliendo hacia la caja gris `W` y $\frac{dL}{dI}$ hacia la caja rosada `D`.
- Derecha: ecuación gráfica $\frac{dL}{dO} \times W^{T} = \frac{dL}{dI}$ y, debajo, un recuadro punteado **SDGP for 2:4 Sparsity**: una matriz "dense" verde con varias celdas marcadas con ✗ rojas → flecha rosada "after pruning" → matriz "2:4 sparse" donde esas celdas quedan en blanco. Leyenda: verde = nonzero, blanco = zero.

## Slide 36

**Pruning – Métodos basados en importancia estructural** — solo texto.

En los modelos Transformer utilizados por los LLMs, el análisis no siempre se realiza sobre pesos individuales. En muchos casos se calcula la importancia de componentes completos, tales como:

- Cabezas de atención (Attention Heads).
- Neuronas de la red Feed Forward (FFN).
- Capas Transformer.
- Bloques completos del modelo.

Si un componente aporta poca información durante la inferencia, puede eliminarse por completo. Este tipo de evaluación es especialmente útil cuando el objetivo es acelerar la ejecución del modelo en hardware especializado.

## Slide 37

**Tipos de Pruning**

Existen diversas formas de realizar el Pruning, dependiendo del nivel de la red neuronal sobre el que se aplique la eliminación de parámetros. En términos generales, las técnicas de poda se clasifican en:

- Pruning no estructurado (Unstructured Pruning) y
- Pruning estructurado (Structured Pruning).

La principal diferencia entre ambas radica en si se eliminan pesos individuales o estructuras completas de la red.

**Visual (derecha):** una red neuronal densa de nodos azules a la izquierda se bifurca mediante dos flechas amarillas:
- **Unstructured Pruning** (arriba): la red conserva todas las neuronas pero varias conexiones aparecen atenuadas/borradas.
- **Structured Pruning** (abajo): dos neuronas aparecen en gris (eliminadas por completo) junto con todas sus conexiones.

## Slide 38

**Unstructured Pruning**

El Unstructured Pruning elimina pesos individuales considerados poco importantes, sin modificar la arquitectura general del modelo. Es decir, las neuronas y capas permanecen intactas, pero algunas conexiones entre ellas desaparecen.

Como resultado, la matriz de pesos se vuelve dispersa (Sparse Matrix), ya que contiene numerosos valores iguales a cero.

**Visual (derecha):** "before pruning" (red densa 5→4→3→2) → dos flechas verdes segmentadas rotuladas *pruning synapses* y *pruning neurons* → "after pruning" con notablemente menos aristas.

## Slide 39

**Structured Pruning**

El Structured Pruning elimina estructuras completas de la red neuronal, en lugar de pesos individuales. Dependiendo del modelo, estas estructuras pueden ser:
- Neuronas completas.
- Canales (Channels).
- Filtros en redes convolucionales.
- Cabezas de atención (Attention Heads).
- Capas Transformer.
- Bloques completos del modelo.

Al eliminar componentes enteros, la arquitectura del modelo se simplifica de manera explícita, reduciendo tanto el número de parámetros como la cantidad de operaciones necesarias durante la inferencia.

**Visual (derecha):** diagrama convolucional: pila de mapas `features` × una columna de 4 `filters` (cubos azules); uno de los filtros está marcado como **pruned** con líneas que apuntan a él y al mapa de salida correspondiente, que aparece dibujado en línea punteada dentro de la pila de `features` de salida (flecha verde entre ambas).

## Slide 40

**Flujo del Proceso de Pruning** (pasos 1–4, tarjetas con flechas)

1. **Modelo original** — "Modelo denso con todos los parámetros". Dibujo de red densa con leyenda: azul = Entrada, morado = Capa oculta / Neuronas, verde = Salida, línea = Conexión / Peso.
2. **Entrenamiento** — "El modelo aprende a partir de los datos". Icono de base de datos + gráfico de línea ascendente; abajo caja verde `Datos de entrenamiento`.
3. **Identificar pesos poco importantes** — "Se calcula la importancia de cada peso (ej. magnitud, gradiente, sensibilidad) y se marcan los menos importantes". Red con aristas rojas resaltadas; caja **Criterio de importancia**: Magnitud del peso · Gradientes · Sensibilidad · Otros métodos.
4. **Eliminar pesos** — "Se eliminan (ponen a cero) los pesos menos importantes según el umbral definido". Red con ✗ rojas; leyenda: ✗ = Peso eliminado, — = Peso conservado.

Textos al pie (uno por paso):
- Es la red neuronal completa, con todos sus parámetros y conexiones. Ofrece el máximo rendimiento, pero también requiere mayor memoria y capacidad de cómputo.
- El modelo aprende a partir de los datos ajustando sus pesos para minimizar el error y realizar correctamente la tarea para la que fue diseñado.
- Se evalúa la importancia de cada peso mediante criterios como su magnitud, gradiente o sensibilidad, identificando aquellos que aportan muy poco al resultado.
- Después del pruning, el modelo suele perder algo de precisión porque se han eliminado conexiones que, aunque poco importantes, aún contribuían al rendimiento.

## Slide 41

**Flujo del Proceso de Pruning** (pasos 5–7)

5. **Modelo degradado** — "Después del pruning, el modelo puede perder parte de su rendimiento." Red con conexiones faltantes.
6. **Fine-Tuning (Ajuste fino)** — "Se reentrena el modelo podado con los datos para recuperar la mayor parte del rendimiento." Icono de base de datos + gráfico ascendente (`Datos de entrenamiento`) → flecha → red podada.
7. **Modelo comprimido** — "Modelo final más pequeño, más rápido y con rendimiento cercano al original." Red reducida en marco verde.

Textos al pie:
- Después del pruning, el modelo suele perder algo de precisión porque se han eliminado conexiones que, aunque poco importantes, aún contribuían al rendimiento.
- Se reentrena el modelo podado utilizando los datos originales para recuperar la mayor parte de la precisión perdida sin volver a aumentar su tamaño.
- Se obtiene un modelo más pequeño, con menos parámetros, menor consumo de memoria y menor costo computacional, manteniendo un rendimiento muy cercano al modelo original.

## Slide 42

Dos tarjetas: **Ventajas** (marco y texto verde) y **Desventajas** (marco y texto rojo) del Pruning.

**Ventajas**
- **Menor tamaño del modelo** — Hay menos parámetros que almacenar.
- **Menor cantidad de operaciones** — Se realizan menos multiplicaciones. Disminuyen los FLOPs.
- **Menor latencia** — La inferencia puede ejecutarse más rápidamente. Especialmente con lotes pequeños (batch pequeño).
- **Menor consumo energético** — Al realizar menos operaciones, disminuye el consumo eléctrico. Muy útil en dispositivos Edge.

**Desventajas**
- **Puede perder precisión** — Si se elimina demasiada información.
- **Requiere Fine-Tuning** — Normalmente no basta con eliminar parámetros. Debe reentrenarse.
- **No siempre acelera la inferencia** — En hardware convencional, los pesos eliminados pueden seguir ocupando espacio lógico. Por ello el hardware especializado aprovecha mucho mejor el pruning estructurado.

## Slide 43

**Conclusiones** — tres bloques numerados entre corchetes cian.

**01.** Los LLMs ofrecen una gran capacidad para comprender y generar lenguaje natural, pero su elevado número de parámetros implica altos requerimientos de memoria, procesamiento y energía.

**02.** Knowledge Distillation, Quantization y Pruning son técnicas complementarias de optimización que permiten reducir el tamaño y el costo de los modelos sin afectar significativamente su desempeño.

**03.** La optimización de LLMs es fundamental para su despliegue en entornos reales, ya que facilita la ejecución eficiente en servidores, dispositivos móviles y sistemas con recursos limitados.

## Slide 44

Slide de cierre decorativa: logo UTEC centrado sobre fondo cian con patrón hexagonal. Sin contenido.
