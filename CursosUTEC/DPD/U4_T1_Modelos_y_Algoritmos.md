---
curso: DPD
titulo: U4_T1_Modelos y Algoritmos.pptx
slides: 47
fuente: U4_T1_Modelos y Algoritmos.pptx.pdf
---

# U4_T1_Modelos y Algoritmos.pptx

DS-3022

Modelo y Algoritmos

**Figura:** En el centro-izquierda, en texto grande y negrita, el código de curso **DS-3022**; debajo, en cursiva, el título **Modelo y Algoritmos**, seguido de una línea horizontal cian. En la esquina inferior izquierda hay un robot caricaturesco gris con un solo ojo grande y cúpula transparente que muestra circuitos electrónicos, saludando con la mano; debajo del robot aparece el texto estilizado **DS3022** en azul con contorno negro. En una de las fotos se lee **UTEC Universidad de Ingeniería y Tecnología**.

(slide 1)

## Índice

| Sección | Subtemas |
|---|---|
| Objetivo de la Sesión | |
| Introducción a Modelos de Aprendizaje para DPD | Datos dinámicos y tipos de sistemas ML; Batch monolítico; ML en tiempo real; Pipeline ML; ML con Feature Store; Ejemplo de un Modelo ML funcionando; Ejemplo de Inspección visual y Concept Drift/Data Drift; Selection Policy: Estimate confidence; Qué es X y qué es Y; Caso de Estudio: Reconocimiento de Voz |
| Modelamiento | Desarrollo de IA centrado en el modelo / Desarrollo de IA centrado en los Datos; Machine Learning ≈ Aproximación de una función; Tipos de Machine Learning; Aprendizaje supervisado; La mayoría de las investigaciones se enfocan en; Arquitecturas para diferentes tipos de entradas |
| Ciclo de Vida | Model Development / Training / Inference; Model Development — manejo de datos; Andrej Karpathy (Tesla Auto Pilot Team); Model Development — ingeniería de características y modelado; Hiperparámetros; ¿Qué es la salida?; El pipeline captura las dependencias del Código y datos; Model Development / Training; Training / Inference; Inference; Ciclo de vida completo: Model Development / Training / Inference |
| Ejemplos prácticos | Now, its your turn; Resumen de Cierre |

01 Introducción a Modelos de aprendizaje

02 Modelamiento

03 Ciclo de Vida

04 Ejemplos prácticos

**Figura:** Título **Índice** en negrita con línea cian horizontal encima. Lista numerada de cuatro temas, cada número en un cuadrado redondeado cian (01–04). A la derecha del título, robot caricaturesco gris con antena roja y texto **DS3022** en fuente estilizada azul.

- [Objetivo de la Sesión](#objetivo-de-la-sesión)
- [Introducción a Modelos de Aprendizaje para DPD](#introducción-a-modelos-de-aprendizaje-para-dpd)
  - [Datos dinámicos y tipos de sistemas ML](#datos-dinámicos-y-tipos-de-sistemas-ml)
  - [Batch monolítico](#batch-monolítico)
  - [ML en tiempo real](#ml-en-tiempo-real)
  - [Pipeline ML](#pipeline-ml)
  - [ML con Feature Store](#ml-con-feature-store)
  - [Ejemplo de un Modelo ML funcionando](#ejemplo-de-un-modelo-ml-funcionando)
  - [Ejemplo de Inspección visual y Concept Drift/Data Drift](#ejemplo-de-inspección-visual-y-concept-driftdata-drift)
  - [Selection Policy: Estimate confidence](#selection-policy-estimate-confidence)
  - [Qué es X y qué es Y](#qué-es-x-y-qué-es-y)
  - [Caso de Estudio: Reconocimiento de Voz](#caso-de-estudio-reconocimiento-de-voz)
- [Modelamiento](#modelamiento)
  - [Desarrollo de IA centrado en el modelo / Desarrollo de IA centrado en los Datos](#desarrollo-de-ia-centrado-en-el-modelo--desarrollo-de-ia-centrado-en-los-datos)
  - [Machine Learning ≈ Aproximación de una función](#machine-learning--aproximación-de-una-función)
  - [Tipos de Machine Learning](#tipos-de-machine-learning)
  - [Aprendizaje supervisado](#aprendizaje-supervisado)
  - [La mayoría de las investigaciones se enfocan en](#la-mayoría-de-las-investigaciones-se-enfocan-en)
  - [Arquitecturas para diferentes tipos de entradas](#arquitecturas-para-diferentes-tipos-de-entradas)
- [Ciclo de Vida](#ciclo-de-vida)
  - [Model Development / Training / Inference](#model-development--training--inference)
  - [Model Development — manejo de datos](#model-development--manejo-de-datos)
  - [Andrej Karpathy (Tesla Auto Pilot Team)](#andrej-karpathy-tesla-auto-pilot-team)
  - [Model Development — ingeniería de características y modelado](#model-development--ingeniería-de-características-y-modelado)
  - [Hiperparámetros](#hiperparámetros)
  - [¿Qué es la salida?](#qué-es-la-salida)
  - [El pipeline captura las dependencias del Código y datos](#el-pipeline-captura-las-dependencias-del-código-y-datos)
  - [Model Development / Training](#model-development--training)
  - [Training / Inference](#training--inference)
  - [Inference](#inference)
  - [Ciclo de vida completo: Model Development / Training / Inference](#ciclo-de-vida-completo-model-development--training--inference)
- [Ejemplos prácticos](#ejemplos-prácticos)
  - [Now, its your turn](#now-its-your-turn)
  - [Resumen de Cierre](#resumen-de-cierre)
- [Glosario](#glosario)

## Objetivo de la Sesión

**Tipos de Modelos:** Identificar y diferenciar entre los principales tipos de modelos de datos, entendiendo sus aplicaciones y limitaciones.

**Selección de Algoritmos:** Identificar las necesidades específicas para la selección inicial de algoritmos apropiados.

**Figura:** Título **Objetivo de la Sesión** en negrita con una línea cian encima. Dos objetivos con iconos en cuadrados azules: el primero con icono de diagrama de flujo/red (**Tipos de Modelos**), el segundo con icono de cabeza humana con engranaje (**Selección de Algoritmos**). En la esquina superior derecha, robot caricaturesco con texto **DS302S**. una sección tiene overlay cian.

(slide 2)

## Introducción a Modelos de Aprendizaje para DPD

**Figura:** Número grande **1.** con subrayado negro grueso. Debajo, título en cursiva cian: *Introducción a Modelos de Aprendizaje para DPD*. la forma superior tiene tinte cian intenso, las inferiores muestran concreto en color natural.

(slide 4)

### Datos dinámicos y tipos de sistemas ML

La parte más importante de este viaje es trabajar con datos dinámicos.

**Figura:** Diagrama de tres círculos concéntricos alineados sobre un eje vertical etiquetado **Business Value** (línea punteada vertical a la izquierda, valor creciente hacia arriba).

- **Círculo interior (amarillo/tan) — Static Data:** vinculado a la caja **One-Off ML Experiments** con subtexto **no pipelines**. Representa el nivel base de valor de negocio.
- **Círculo medio (azul verdoso pálido) — Batch Data:** vinculado a la caja **Batch ML Systems** con subtexto **batch pipelines**. Nivel intermedio de valor de negocio.
- **Círculo exterior (verde claro) — Real-Time Data:** vinculado a la caja **Real-Time ML Systems** con subtexto **streaming/inference pipelines**. Representa el nivel más alto de valor de negocio.

(slides 5)

### Batch monolítico

Batch monolítico

**Figura:** Diagrama de arquitectura de pipeline de ML monolítico por lotes. Componente central: rectángulo grande **`monolithic-batch-pipeline.py`** con tres pasos secuenciales numerados:

1. **Create Features** — recibe **Historical Data** (cilindro con borde rojo punteado, flujo TRAIN) y **New Data** (cilindro azul sólido, flujo INFERENCE).
2. **Train Model** — recibe **features/labels** (flecha roja punteada desde paso 1).
3. **Predict with model** (caja verde) — recibe **features** (flecha azul desde paso 1) y **model** (flecha azul desde Model Registry).

**Entidades externas:**
- **Model Registry** (caja beige, arriba): recibe **model** (flecha roja punteada desde Train Model) y provee **model** (flecha azul sólida hacia Predict with model).
- **Prediction Consumer** (caja verde, derecha): recibe **predictions** (flecha azul desde paso 3).

**Codificación de colores:** líneas rojas punteadas = TRAIN; líneas azul/teal sólidas = INFERENCE.

(slide 6)

### ML en tiempo real

(real-time) ML

**Figura:** Diagrama de arquitectura de ML en tiempo real con dos fases separadas.

**Fase de entrenamiento (flechas rojas):**
- **Historical Data** (cilindro rojo punteado, izquierda) → flecha **data** → caja **`training-pipeline.py`** con dos pasos:
  - **Create Features** → flecha **features/labels** → **Train Model**
- **Train Model** → flecha **model** (roja) → **Model Registry** (caja beige, arriba).

**Fase de inferencia (flechas teal):**
- **Model Registry** → flecha **model** (teal) → caja **`online-inference-pipeline.py`** (teal claro) con:
  - **Create Features** (arriba)
  - **model** (abajo)
- **Prediction Consumer** (caja verde, derecha):
  - envía **request** → Create Features
  - Create Features → model
  - model → **prediction** → Prediction Consumer

Muchos sistemas de ML interactivos en tiempo real también requieren historial y contexto para hacer predicciones personalizadas.

El Feature Store permite recuperar estos datos con baja latencia como características pre-calculadas para modelos en línea.

**Figura:** Diagrama de arquitectura de ML en tiempo real con **Feature Store** central.

**Fase de entrenamiento (flechas rosadas, etiqueta TRAIN):**
- **Train Data** (cilindro punteado, izquierda) → bloque gris con:
  - **Create Features** (caja azul) → **Feature Store** (cilindro verde sólido, abajo-centro)
  - **Train Model** (caja blanca) ← Feature Store
- **Train Model** → flecha **model** (roja) → **Model Registry** (arriba).

**Fase de inferencia (flechas azules):**
- **Model Registry** → flecha **model** (azul) → **Model Serving / `inference-pipeline.py`** (caja verde grande) con sub-bloque **Get/Create Features**
- **Feature Store** → flecha (rosada) → Get/Create Features
- **Results** (caja gris, derecha):
  - **request** (azul) → Model Serving
  - **prediction response** (azul) ← Model Serving

(slides 7–8)

### Pipeline ML

Pipeline ML

Un pipeline de ML tiene entradas y salidas bien definidas.

Las salidas de los pipelines de ML pueden ser entradas para otros pipelines de ML o para sistemas externos de ML que utilizan las predicciones y registros de predicciones para hacerlos 'habilitados para IA'.

**Figura:** Diagrama de pipeline de ML. Entrada izquierda: flecha **Batch Data or Real-Time Data** hacia contenedor **ML Pipelines** (rectángulo verde claro) con tres nodos circulares en secuencia:

1. **Feature Pipeline** → produce **Features/Labels** (hacia Training Pipeline) y **Features** (bypass directo hacia Inference Pipeline).
2. **Training Pipeline** → recibe Features/Labels → produce **Models** → Inference Pipeline.
3. **Inference Pipeline** → recibe Models y Features.

**Salidas desde Inference Pipeline:**
- Flecha **Predictions** (arriba) → caja **AI-Enabled App** (verde).
- Flecha **Logs** (derecha) → caja **Monitoring & Debugging** (verde).

(slide 9)

### ML con Feature Store

ML con Feature Store

Un sistema de ML con Feature Store soporta 3 tipos de pipelines fundamentales para la operatividad y observabilidad.

Pipelines: Características, Entrenamiento e Inferencia.

Logs: Los pipelines de logs son críticos para implementar la observabilidad en sistemas de ML.

**Figura:** Diagrama de arquitectura de sistema ML con Feature Store. Tres pipelines fundamentales con leyenda de colores:

- **Operational (verde):** Feature Pipeline e Inference Pipeline.
- **On-Demand (naranja):** Training Pipeline.

**Componentes y flujos:**

1. **Feature Pipeline** (verde, Operational) — "Transform data into features & labels": **Data Sources** → Data → **Feature Store** (rectángulo grande en la base).
2. **Training Pipeline** (naranja, On-Demand) — "Train models with features & labels": Feature Store → Data → **Model Registry** (caja sobre Feature Store) con **Models**.
3. **Inference Pipeline** (verde, Operational) — "Make predictions with models & new features":
   - Model Registry → Models → Inference Pipeline
   - Feature Store → Data → Inference Pipeline
   - Inference Pipeline → predictions → **AI Powered Product & Services**
   - AI Powered Product & Services → Data (retroalimentación) → Inference Pipeline
   - Inference Pipeline → **Logs** → Feature Store

(slide 10)

### Ejemplo de un Modelo ML funcionando

Ejemplo de un Modelo ML funcionando

¿Nuestro modelo en Prueba de Concepto, funcionará en Producción?

**Figura:** Diagrama de arquitectura cliente-servidor para análisis de imágenes médicas (detección de lesiones cutáneas).

- **Izquierda — Imagen de entrada:** Fotografía de la espalda desnuda de una persona con numerosos lunares/manchas. Cajas blancas semitransparentes superpuestas sobre muchas manchas; una mancha enmarcada en **caja roja** y otra en **caja amarilla** (clasificaciones o niveles de alerta del modelo).
- **Centro — Prediction Server:** Icono de nube azul con servidor interno etiquetado **Prediction Server**.
- **Derecha — Edge device:** Diagrama con dos componentes:
  - **Inspection Software:** iconos de código binario (`10101`) y **Camera**.
  - **Control Software:** icono de mano haciendo clic en interfaz.

**Flujo de datos (flechas azules):**
- Edge device → **API** → Prediction Server
- Prediction Server → **Predicción** → Edge device

(slide 11)

### Ejemplo de Inspección visual y Concept Drift/Data Drift

Ejemplo de Inspección visual

Concept Drift/Data Drift

**Figura:** Tres smartphones dispuestos horizontalmente ilustrando inspección visual y drift.

1. **Teléfono izquierdo (referencia/normal):** Smartphone negro con borde exterior azul claro delgado. Pantalla oscura en perfecto estado. Debajo de la pantalla, tres iconos de navegación tenues (flecha atrás, casa, lupa).
2. **Teléfono central (anomalía/defecto):** Mismo diseño con borde azul claro. Pantalla con grieta diagonal blanca prominente desde el centro superior hacia la esquina inferior izquierda.
3. **Teléfono derecho (ejemplo de drift):** Borde exterior ahora gris oscuro/negro en lugar de azul claro. Renderizado significativamente más oscuro y de menor contraste. Misma grieta diagonal presente pero menos visible por la oscuridad general.

Texto inferior derecho: **Concept Drift/Data Drift**.

(slide 12)

### Selection Policy: Estimate confidence

Selection Policy: Estimate confidence

**Figura:** Diagrama de pipeline de estimación de confianza mediante ensemble de modelos.

- **Entrada (izquierda):** Fotografía de un gatito con chaqueta universitaria amarilla y azul detrás de un setup de DJ miniatura con dos tornamesas y un mixer.
- **Stack de modelos (centro):** Cuatro unidades apiladas verticalmente, cada una con diagrama de nodo de red neuronal (entradas conectando a círculo con curva sigmoide):
  1. Logo **scikit-learn**, texto **Version 2** → salida **"CAT"** (naranja)
  2. Logo **scikit-learn**, texto **Version 3** → salida **"CAT"** (naranja)
  3. Logo **TensorFlow** → salida **"CAT"** (naranja)
  4. Logo **Caffe** → salida **"CAT"** (naranja)
- **Policy** (rectángulo redondeado vertical, derecha): recibe las cuatro predicciones **"CAT"**.
- **Salida final:** **"CAT"** (naranja, grande) y **CONFIDENT** (teal/verde azulado).

**Figura:** Diagrama de pipeline de estimación de confianza con predicciones discordantes.

- **Entrada (izquierda):** Fotografía de un hombre con camiseta que muestra un gato con corona y moño azul sobre fondo espacial tipo nebulosa.
- **Stack de modelos (centro):** Cuatro unidades apiladas:
  1. Logo **scikit-learn** → **"CAT"** (naranja)
  2. Logo **TensorFlow** → **"MAN"** (morado)
  3. Logo **Caffe** → **"CAT"** (naranja)
  4. Logo **scikit-learn** → **"SPACE"** (rojo)
- **Policy** (rectángulo redondeado): recibe las cuatro predicciones divergentes.
- **Salida final:** **"CAT"** (naranja, grande) y **UNSURE** (naranja).

(slides 13–14)

### Qué es X y qué es Y

Qué es X y qué es Y

- Generalmente después del despliegue los datos pueden cambiar

**Figura:** Diagrama de flujo del ciclo de vida de un proyecto de machine learning con cuatro etapas horizontales en forma de chevrón, flujo de izquierda a derecha:

1. **Scoping** (verde): **Define project**
2. **Data** (azul): **Define data and establish baseline** → **Label and organize data**
3. **Modeling** (naranja/marrón claro): **Select and train model** → **Perform error analysis**
4. **Deployment** (rosa/magenta): **Deploy in production** → **Monitor & maintain system**

Debajo de las etapas Scoping/Data: pregunta **Qué es X y qué es Y**. Debajo de Modeling/Deployment: viñeta sobre cambio de datos tras el despliegue.

(slide 15)

### Caso de Estudio: Reconocimiento de Voz

Caso de Estudio: Reconocimiento de Voz

- ¿Los datos están etiquetados de forma consistente?
- ¿Cuánto silencio se considera antes y después del clip?
- ¿Cómo se hará la normalización del volumen?

"Hum, entendí"

"Hum…, entendí"

"Entendí"

**Figura:** Slide de caso de estudio con diagrama de ciclo de vida ML (cuatro etapas en chevrón: Scoping, **Data** resaltada en azul, Modeling, Deployment) con los mismos sub-pasos que en Slide 15.

**Ilustraciones (arriba derecha):**
- Pantalla/dispositivo inteligente moderno con icono circular de cara: **"Hi, my name is Watson."**

**Ejemplos de etiquetado (abajo derecha):** Icono de altavoz junto a tres variaciones de transcripción del mismo clip de audio (listadas arriba).

Las 3 entradas principales a nuestro modelo son:

- Código (Algoritmo/modelo)
- Hiperparámetros
- Datos

Research/Academia

Product Team

**Figura:** Slide con diagrama de ciclo de vida ML (etapa **Modeling** resaltada en naranja).

**Diagrama de entradas al modelo:**
- Tres viñetas con flechas apuntando a caja azul **Modelo ML** $X \rightarrow y$:
  - Código (Algoritmo/modelo)
  - Hiperparámetros
  - Datos

**Asociaciones por color:**
- **Research/Academia** (subrayado rojo): bracket rojo que abarca las tres entradas; subrayado rojo específico bajo **Datos**.
- **Product Team** (subrayado teal): subrayado teal bajo **Código (Algoritmo/modelo)**.

**Ilustraciones (arriba derecha):** Computadora vintage **"Hello. I am Eliza. >>"** y dispositivo moderno **"Hi, my name is Watson."**

Problemas de entrenamiento. Ejem. Entrenado solo con voces de

**Figura:** Slide con diagrama de ciclo de vida ML (etapa **Deployment** resaltada en rosa).

**Diagrama de arquitectura del sistema:**

- **Lado nube:** Icono de nube con caja **Prediction Server** en su interior.
- **Lado edge — Mobile phone (edge device):** Caja con:
  - **VAD module** (Voice Activity Detection)
  - **Microphone** (entrada al VAD module)
  - **Frontend code**
  - Etiqueta vertical externa: **Voice Activity Detection**

**Flechas de comunicación:**
- Mobile phone → **Speech API** → Prediction Server (nube)
- Prediction Server → **Transcript** → Mobile phone
- Prediction Server → **Search Result** → Mobile phone

**Ilustraciones (arriba derecha):** Computadora vintage **"Hello, I am Eliza."** y dispositivo Watson **"Hi, my name is Watson."**

Texto inferior cortado: **"Problemas de entrenamiento. Ejem. Entrenado solo con voces de"**

- ¿Qué pasa si cambian los datos?
- ¿Qué pasa si cambia el algoritmo?

**Figura:** Slide con diagrama de ciclo de vida ML (cuatro etapas: Scoping, Data, Modeling en gris; **Deployment** y sus sub-pasos resaltados en rosa).

**Ilustraciones (arriba derecha):**
- Computadora beige vintage con pantalla: **"Hello, I am Eliza. >> |"**
- Pantalla vertical azul moderna con cara estilizada luminosa: **"Hi, my name is Watson."**

**Preguntas (abajo):** Dos viñetas en español (listadas arriba).

Concept drift y Data drift (cambio de concepto – cambio de datos)

- Conjunto de entrenamiento
  - Datos adquiridos, datos históricos de usuarios con transcripciones
- Conjunto de Test
  - Datos de hace unos meses

¿Cómo Cambiarán los datos?

- Gradual - Cambio en la forma de hablar de las personas
- Repentino – Ejemplo Covid y fraude de tarjetas

**Figura:** Slide con diagrama de ciclo de vida ML completo (cuatro etapas en chevrón: Scoping, Data, Modeling en gris; **Deployment** en rosa/magenta con sub-pasos **Deploy in production** y **Monitor & maintain system**).

**Ilustraciones (abajo derecha):**
- Computadora de escritorio vintage con burbuja: **"Hello, I am ELIZA."**
- Altavoz inteligente moderno (cilindro negro con anillo azul luminoso) con burbuja: **"Hi, my name is Watson."**

(slides 16–20)

## Modelamiento

**Figura:** En el centro-izquierda, el número de sección **"2."** en tipografía grande negra y negrita, con una línea horizontal gruesa negra debajo. Debajo de la línea, el título **"Modelamiento"** en fuente sans-serif azul claro e itálica. una de las formas superiores tiene superposición de color cian/azul translúcido; en una sección interior se lee texto grabado en un muro de concreto.

(slide 21)

### Desarrollo de IA centrado en el modelo / Desarrollo de IA centrado en los Datos

Desarrollo de IA centrado en el modelo

Desarrollo de IA centrado en los Datos

   - **Define project** (caja gris)

   - **Define data and establish baseline** (caja gris)
   - **Label and organize data** (caja gris)

   - **Select and train model** (caja naranja)
   - **Perform error analysis** (caja naranja)

   - **Deploy in production** (caja gris)
   - **Monitor & maintain system** (caja gris)

Debajo del diagrama, dos leyendas en español: a la izquierda **"Desarrollo de IA centrado en el modelo"** y a la derecha **"Desarrollo de IA centrado en los Datos"**. La fase Modeling y sus subtareas están resaltadas en naranja brillante, mientras las demás fases son grises.

(slide 22)

### Machine Learning ≈ Aproximación de una función

Machine Learning ≈ Aproximación de una función

**Figura:** Slide dividida en cuatro cuadrantes que ilustran distintas tareas de machine learning como aproximación de funciones (input → output):

### Cuadrante superior izquierdo — Reconocimiento de objetos

- **Input:** Fotografía de un gatito naranja con la boca abierta.
- **Proceso:** Flecha azul gruesa apuntando hacia la derecha.
- **Output:** Texto **"Label: Cat"**.

### Cuadrante superior derecho — Reconocimiento de voz

- **Proceso:** Flecha azul gruesa apuntando hacia la derecha.
- **Output:** Texto transcrito entre comillas: **"El gato en el sombrero"**.

### Cuadrante inferior izquierdo — Control

- **Input:** Imagen etiquetada **"raw pixels"** que muestra un juego estilo Atari (Pong).
- **Proceso:** Diagrama de red neuronal simple: los píxeles crudos se conectan a una **"hidden layer"** de cinco nodos circulares azules; todos convergen en un único nodo de salida rosa.
- **Output:** Texto junto al nodo rosa: **"probability of moving UP"**.

### Cuadrante inferior derecho — Traducción

- **Input:** Frase en inglés **"The cat in the hat."** debajo de una secuencia de cuatro bloques verticales, cada uno con tres nodos circulares negros conectados por flechas horizontales.
- **Proceso:** Modelo secuencia-a-secuencia donde la secuencia de entrada fluye hacia una secuencia de salida.
- **Output:** Frase en español **"El gato en el sombrero"** sobre una secuencia de cinco bloques verticales similares de nodos conectados por flechas.

(slide 23)

### Tipos de Machine Learning

**Figura:** Diagrama jerárquico o mapa mental que categoriza los tipos de Machine Learning. En el centro superior, ilustración de un robot blanco sosteniendo un libro y señalando su cabeza. Desde esta figura central parten tres ramas principales hacia abajo:

#### 1. Aprendizaje Supervisado

- **Etiqueta de conexión:** "Labeled Data"
- Se divide en dos subcategorías:
  - **Regresión:** Conectada por la etiqueta **"Quantitative Response"**. Debajo, gráfico 3D de dispersión con puntos azules y un plano rojo inclinado representando el modelo de regresión.
- **Clasificación:** Conectada por la etiqueta **"Categorical Response"**.

#### 2. Aprendizaje por refuerzo

- **Etiqueta de conexión:** "Reward"
- Debajo del título, fotografía de dos hombres jugando una partida de Go, etiquetada **"Alpha Go"**.

#### 3. Aprendizaje no Supervisado

- **Etiqueta de conexión:** "Unlabeled Data"
- Se divide en dos subcategorías:
  - **Reducción de Dimensionalidad:** Debajo, dos gráficos de sistemas de coordenadas 3D mostrando una nube de puntos siendo proyectada o transformada.
  - **Clustering:** Debajo, gráfico de dispersión 2D donde los puntos se agrupan en tres clusters de colores distintos: azul, verde y rojo.

Títulos de categorías principales en fuente azul brillante.

(slide 24)

### Aprendizaje supervisado

Aprendizaje supervisado

Dado los datos que contienen inputs y outputs

#### Data

| Input | Output |
|-------|--------|
| $X_1$ (imagen de gatito) | $Y_1$: cat |
| $X_2$ (imagen de bebé) | $Y_2$: baby |
| $\ldots$ | $\ldots$ |
| $X_n$ (imagen de bebé) | $Y_n$: baby |

#### Modelo

$$f_\theta(x) \to y$$

- **Parámetros** ($\theta$): parámetros del modelo.

#### Objetivo

$$\theta^* = \arg \min_\theta \mathbb{E}_D [L(f_\theta(x), y)]$$

- **Loss** ($L$): función de pérdida.
- **Sobre datos futuros** ($\mathbb{E}_D$): expectativa sobre la distribución de datos.

#### Entrenamiento (aproxima el objetivo sobre el conjunto de entrenamiento):

$$\hat{\theta} = \arg \min_\theta \frac{1}{n} \sum_{i=1}^n L(f_\theta(x_i), y_i)$$

**Figura:** Slide con tres columnas conceptuales conectadas. A la izquierda, tabla de datos con columnas Input y Output: $X_1$ es una imagen de gatito con etiqueta "cat", $X_2$ y $X_n$ son imágenes de bebés con etiqueta "baby". En el centro, bajo el encabezado **"Modelo"**, la función $f_\theta(x) \to y$ con un recuadro azul señalando $\theta$ como **"Parámetros"**. A la derecha, bajo **"Objetivo"**, la fórmula de minimización de riesgo esperado con recuadros azules señalando $L$ como **"Loss"** y $\mathbb{E}_D$ como **"Sobre datos futuros"**. En la parte inferior, la fórmula de entrenamiento empírico (minimización del riesgo sobre el conjunto de entrenamiento).

(slide 25)

### La mayoría de las investigaciones se enfocan en

La mayoría de las investigaciones se enfocan en:

$$f_\theta(x) \rightarrow y$$

#### Expresividad

¿Cómo hacemos que nuestras funciones sean lo suficientemente expresivas?

#### Bias Inductivo

Capturar conocimiento del dominio y suposiciones clave del problema.

#### Eficiencia

Desarrollar modelos que sean fáciles de entrenar y optimizar computacionalmente.

**Figura:** Debajo del título, expresión matemática prominente dentro de un recuadro gris redondeado: $f_\theta(x) \rightarrow y$. En la mitad inferior, tres tarjetas lado a lado:

1. **Expresividad** — icono de perfil de cabeza azul con un engranaje en el interior.
2. **Bias Inductivo** — icono de bombilla azul.
3. **Eficiencia** — icono de velocímetro azul.

(slide 26)

### Arquitecturas para diferentes tipos de entradas

Arquitecturas para diferentes tipos de entradas

#### Convolutional Networks

spatial reasoning tasks

#### Recurrent Networks

Sequential reasoning tasks

**Figura:** Slide dividida en dos secciones principales por una línea vertical azul:

##### Sección izquierda — Convolutional Networks

Etiquetada **"Convolutional Networks"** con subtítulo **"spatial reasoning tasks."**

- **Procesamiento de imágenes:** Fotografía grande de la cara de un gatito naranja. Sobre el ojo y la nariz hay un cuadrado naranja translúcido (ventana deslizante o kernel). Líneas conectan las esquinas del cuadrado a un punto azul arriba, ilustrando extracción de características de una capa convolucional.
- **Procesamiento de audio/señales:** Debajo del gatito, imagen de una forma de onda de audio. Dos triángulos azules (kernels) apuntan a partes específicas de la onda, cada uno conectado a un punto azul arriba, mostrando convolución 1D aplicada a señales.

##### Sección derecha — Recurrent Networks

Etiquetada **"Recurrent Networks"** con subtítulo **"Sequential reasoning tasks."**

- **Traducción automática (secuencia-a-secuencia):** Diagrama de tarea de traducción. Comienza con la frase en inglés **"The cat in the hat."** debajo de cuatro nodos verticales (cada uno con tres puntos). Flechas horizontales conectan estos nodos mostrando flujo de información a través del tiempo. Una flecha conduce a un segundo conjunto de seis nodos que producen la traducción al español: **"El gato en el sombrero."**
- **Reinforcement Learning:** Captura de pantalla de un videojuego clásico 2D de plataformas (personaje en una escalera en entorno verde y negro), etiquetado **"Reinforcement Learning"**.
- **Speech recognition:** En la parte inferior, otra forma de onda de audio. Encima, secuencia de cinco cajas verdes, cada una con tres puntos verticales. Flechas verdes apuntan desde la forma de onda hacia cada caja, y flechas horizontales conectan las cajas entre sí, ilustrando procesamiento secuencial de audio en el tiempo. Etiquetado **"Speech recognition."**

#### Graph Networks

Operating on graph data

**Figura:** Slide dividida en tres columnas principales, cada una correspondiente a un tipo de arquitectura de red neuronal:

##### Columna 1 — Convolutional Networks (parcialmente visible a la izquierda)

- **Encabezado:** "Convolutional Networks"
- **Caso de uso:** "spatial reasoning tasks"
- **Visual:** Imagen de un gatito naranja. Hay un recuadro azul alrededor de su ojo izquierdo y un puntero triangular azul en su barbilla. Debajo, texto **"The quick brown fox…"**. Representa arquitecturas para datos tipo grilla como imágenes.

##### Columna 2 — Recurrent Networks

- **Encabezado:** "Recurrent Networks"
- **Subtítulo:** "Sequential reasoning tasks"
- **Visual 1 (Traducción):** Secuencia de nodos de entrada azules procesando la frase en inglés **"The cat in the hat."** que alimentan una secuencia de nodos de salida naranja que producen la traducción al español **"El gato en el sombrero."** Flechas negras indican flujo secuencial de información.
- **Visual 2 (Reinforcement Learning):** Captura de pantalla de un videojuego clásico 2D de plataformas (similar a *Pitfall!*), etiquetado **"Reinforcement Learning."**
- **Visual 3 (Speech recognition):** Conjunto de nodos verdes de red neuronal procesando una forma de onda digital, etiquetado **"Speech recognition."**

##### Columna 3 — Graph Networks

- **Encabezado:** "Graph Networks"
- **Subtítulo:** "Operating on graph data"
- **Visual 1 — Link Prediction:**
  - **Input:** Diagrama de un grafo con nodos (círculos) y enlaces (líneas).
  - **Proceso:** El grafo de entrada pasa por **"Graph convolutions"** (bloque trapezoidal naranja), **"Activation function"** (gráfico de línea simple) y **"Regularization e.g., dropout"** (bloque gris con elementos omitidos), llevando a otro bloque **"Graph convolutions"**.
  - **Output:** Bocadillo de diálogo con el resultado: **"Output: Drugs C, D lead to a side effect $r_2$"**, sugiriendo predicción de relaciones entre entidades (drogas y efectos secundarios).
- **Visual 2 — Graph Embedding:**
  - **Proceso:** Muestra un grafo moviéndose a través de varias **"Hidden layers"**. Entre estas capas se aplica activación **"ReLU"**. En cada paso, nodos específicos del grafo se resaltan en púrpura, representando cómo el modelo procesa o "embebe" la estructura del grafo en una representación diferente.
  - **Resultado:** Termina con un grafo de **"Output"**.

(slides 27–28)

## Ciclo de Vida

**Figura:** En el centro-izquierda, el número de sección **"3."** en tipografía grande negra y negrita, con una línea horizontal gruesa negra debajo. Debajo de la línea, el título **"Ciclo de vida de Machine Learning"** en fuente sans-serif azul claro e itálica. Una de las formas superiores tiene superposición cian/azul translúcida. En una foto del extremo derecho, un muro tiene la palabra **"INNGENIECIABLE"** impresa verticalmente.

(slide 29)

### Model Development / Training / Inference

**Figura:** Diagrama de flujo en blanco y negro que ilustra un ciclo de vida de machine learning de tres etapas, dispuesto horizontalmente de izquierda a derecha, cada etapa separada por líneas verticales delgadas:

#### 1. Model Development

- **Offline Training Data:** En el extremo izquierdo, tres iconos de cilindros (bases de datos) etiquetados **"Offline Training Data."**
- **Ciclo iterativo:** Una flecha conduce desde los datos a un bucle rectangular con cuatro pasos:
  1. **Data Collection** (arriba-izquierda)
  2. **Cleaning & Visualization** (arriba-derecha)
  3. **Feature Eng. & Model Design** (abajo-derecha)
  4. **Training & Validation** (abajo-izquierda)
- Flechas indican un ciclo continuo en sentido horario entre estos cuatro pasos. Una flecha de entrada desde **"Offline Training Data"** apunta al paso **"Training & Validation."**

#### 2. Training

- **Training Pipelines:** Una flecha desde la etapa de desarrollo conduce a **"Training Pipelines"**, representados por líneas horizontales con nodos (puntos), uno de los cuales se ramifica.
- **Live Data:** Debajo de los pipelines, dos iconos de cilindros etiquetados **"Live Data"** con flecha ascendente alimentando los pipelines.
- **Trained Models:** La salida de los training pipelines conduce a **"Trained Models"**, representados como un conjunto de cuatro iconos de diagramas de red neuronal simple (círculos conectados por líneas).

#### 3. Inference

- **Prediction Service:** Un rectángulo grande contiene varios componentes interconectados: iconos de capas de red neuronal, icono de base de datos y una caja en forma de diamante etiquetada **"Logic."**
- **Interacción con usuarios:** A la derecha del servicio, icono de pantalla de computadora etiquetado **"End User Application."**
  - Flecha **"Query"** desde la aplicación hacia el Prediction Service.
  - Flecha **"Prediction"** desde el Prediction Service de vuelta hacia la aplicación.
- **Feedback Loop:** Flecha negra gruesa etiquetada **"Feedback"** sale de la parte inferior del cuadro Prediction Service y viaja de regreso hacia la izquierda a la etapa Training.
  - Una rama del bucle de feedback va al almacén **"Live Data."**
  - Otra rama, etiquetada **"Validation,"** apunta de regreso hacia la pila **"Trained Models."**

(slide 30)

### Model Development — manejo de datos

Model Development

Identificando posibles fuentes de datos

Uniendo datos de múltiples fuentes

Corrigiendo **missing values** y **outliers**

Visualización de tendencias para detectar **anomalías**

**Figura:** Diagrama titulado **"Model Development"** dividido en flujograma gráfico a la izquierda y lista de tareas descriptivas en español a la derecha, separados por una línea vertical negra:

#### Sección izquierda — Flujograma

- **Fuente de datos:** Tres iconos de cilindros negros (bases de datos) etiquetados **"Offline Training Data."** Una flecha apunta desde estos cilindros hacia el proceso principal.
- **Ciclo de desarrollo:** Flujo circular de cuatro etapas:
  1. **Data Collection** y **Cleaning & Visualization**: agrupados dentro de un único rectángulo redondeado naranja claro. Flecha indica flujo de recolección a limpieza.
  2. **Feature Eng. & Model Design**: flecha descendente desde la etapa de limpieza.
  3. **Training & Validation**: flecha hacia la izquierda desde feature engineering.
  4. Flecha ascendente desde Training & Validation de vuelta a Data Collection, completando el bucle.
- **Persona:** Debajo del ciclo, silueta negra de una persona etiquetada **"Data Scientist."**

#### Sección derecha — Lista de tareas

Cuatro puntos describiendo actividades de manejo de datos:
1. **Identificando** posibles fuentes de datos
2. **Uniendo** datos de múltiples fuentes
3. Corrigiendo **missing values** y **outliers**
4. **Visualización** de tendencias para detectar **anomalías**

Model Development

Identificando posibles fuentes de datos

Uniendo datos de multiples fuentes

Corrigiendo **missing values** y **outliers**

Visualización de tendencias para detector **anomalías**

**Figura:** Slide titulada **"Model Development"** dividida en dos secciones por una línea vertical negra: diagrama de proceso a la izquierda y lista de puntos clave en español a la derecha.

#### Sección izquierda — Diagrama de proceso

- **Fuente de datos:** Tres cilindros apilados etiquetados **"Offline Training Data"** con flecha hacia el ciclo principal.
- **Ciclo de trabajo:** Cuatro pasos conectados por flechas en bucle horario:
  1. **Data Collection** (arriba-izquierda)
  2. **Cleaning & Visualization** (arriba-derecha) — ambos dentro de un fondo rectangular naranja claro
  3. **Feature Eng. & Model Design** (abajo-derecha)
  4. **Training & Validation** (abajo-izquierda) — flecha de regreso a Data Collection
- **Personal:** Silueta negra de persona etiquetada **"Data Scientist"** en la parte inferior izquierda, fuera del ciclo.

#### Sección derecha — Lista de puntos

1. **Identificando** posibles fuentes de datos
2. **Uniendo** datos de múltiples fuentes
3. Corrigiendo **missing values** y **outliers**
4. **Visualización** de tendencias para detector **anomalías**

(slides 31–33)

### Andrej Karpathy (Tesla Auto Pilot Team)

Andrej Karpathy (Tesla Auto Pilot Team)

¿Cuántos data scientists han trabajado alguna vez con datos reales?

**Figura:** Fotografía de una slide de presentación (conferencia o charla) con el mensaje sobre la diferencia entre trabajo académico e industrial en ciencia de datos.

#### Contenido de la slide fotografiada

- **Título:** **"Amount of lost sleep over…"**
- **Dos gráficos circulares lado a lado** comparando entorno **"PhD"** vs entorno **"Tesla":**
  - **Leyenda (ambos gráficos):**
    - **Rojo:** datasets
    - **Azul:** models and algorithms
  - **Gráfico izquierdo (PhD):** Casi enteramente **azul** (~95%+). Muy delgada franja **roja**. Significado: en un entorno PhD, la mayor parte del esfuerzo se enfoca en modelos y algoritmos, muy poco en datasets.
  - **Gráfico derecho (Tesla):** Predominantemente **rojo** (~75%). Porción restante (~25%) **azul**. Significado: en un entorno de producción como Tesla, la mayor parte del trabajo proviene de gestionar y limpiar datasets.

Texto del encabezado de la slide del curso en azul claro: **"Andrej Karpathy (Tesla Auto Pilot Team)"**. Pregunta a la derecha en texto negro: **"¿Cuántos data scientists han trabajado alguna vez con datos reales?"**

(slide 32)

### Model Development — ingeniería de características y modelado

Model Development

Identificando funciones de características informativas

Diseñando nuevas **arquitecturas y modelos**

**Ajuste** hiperparámetros

**Validar** el modelo

Nací para esto!

**Figura:** Slide titulada **"Model Development"** con diagrama de flujo iterativo a la izquierda e ilustración, y lista de tareas en español a la derecha, separados por línea vertical negra.

#### Lado izquierdo — Diagrama e ilustración

- **Fuente de datos:** Tres iconos cilíndricos negros etiquetados **"Offline Training Data"** con flecha hacia un bucle central.
- **Bucle iterativo** con cuatro etapas:
  1. **Data Collection**
  2. **Cleaning & Visualization** (flecha descendente desde Data Collection)
  3. **Feature Eng. & Model Design** (flecha hacia la izquierda desde Cleaning & Visualization)
  4. **Training & Validation** (flecha de regreso hacia arriba a Data Collection)
- **Resaltado:** Los pasos **"Feature Eng. & Model Design"** y **"Training & Validation"** están agrupados dentro de un rectángulo redondeado naranja claro.
- **Ilustración Data Scientist:** Silueta negra de persona con cara sonriente, etiquetada **"Data Scientist"**.

#### Lado derecho — Lista de tareas

1. **Identificando** funciones de características informativas
2. **Diseñando** nuevas **arquitecturas y modelos**
3. **Ajuste** hiperparámetros
4. **Validar** el modelo

(slide 34)

### Hiperparámetros

Hiperparámetros

- los parámetros y, en general, los detalles de configuración que no se determinan directamente a través del entrenamiento
- establecidos manualmente o ajustados usando validación cruzada
- ¿por qué no aprender directamente?

Encontrar los hiperparámetros:

#### Objetivo:

$$\arg \min_{\theta} \frac{1}{n} \sum_{i=1}^{n} L_{\alpha}(f_{\theta}(x_i), y_i) + \lambda R(\theta)$$

- Hiperparámetros resaltados: $\alpha$ (dentro de la función de pérdida $L$), $\lambda$ (coeficiente de regularización).

#### Algoritmo de entrenamiento

$$u^{(t)} \leftarrow \beta u^{(t-1)} + \eta \sum_{i \in \mathcal{B}} \nabla_{\theta} (L_{\alpha}(f_{\theta}(x_i), y_i)) \bigg|_{\theta^{(t)}}$$

- Hiperparámetros resaltados: $\beta$ (coeficiente de momentum), $\eta$ (learning rate), $\mathcal{B}$ (batch size o conjunto de índices del mini-batch).

#### Architecture:

Generalmente las arquitecturas se tratan aparte de los hiperparámetros

**Figura:** Slide educativa con definición de hiperparámetros y dos fórmulas principales con variables específicas resaltadas en círculos verdes:

- **Diagrama de arquitectura (abajo-izquierda):** Esquema de una Red Neuronal Convolucional (CNN) similar a LeNet-5:
  - **Input:** imagen 32×32 (de la letra 'A')
  - **Layer C1:** Feature maps 6@28×28 (Convolutions)
  - **Layer S2:** Feature maps 6@14×14 (Subsampling)
  - **Layer C3:** Feature maps 16@10×10 (Convolutions)
  - **Layer S4:** Feature maps 16@5×5 (Subsampling)
  - **Layer C5:** Capa fully connected con 120 unidades
  - **Layer F6:** Capa fully connected con 84 unidades
  - **Output:** 10 unidades (Gaussian connections)
  - Bocadillo azul señala el diagrama: *"Generalmente las arquitecturas se tratan aparte de los hiperparámetros"*

- **Stochastic Gradient Descent (abajo-derecha):** Gráfico de contornos representando un paisaje de pérdida con ejes $\theta_1$ y $\theta_2$. Línea naranja dentada con flechas ilustra la trayectoria del algoritmo de optimización moviéndose hacia el centro (mínimo) de las elipses concéntricas azules.

(slide 35)

### ¿Qué es la salida?

¿Qué es la salida?

Model Development

(insights …)

Training Pipelines

**Figura:** Slide titulada **"¿Qué es la salida? Model Development"** que ilustra el proceso de desarrollo de un modelo de machine learning y sus salidas resultantes, dividida en dos secciones por una línea vertical punteada:

#### Lado izquierdo — Model Development

- **Offline Training Data:** Tres iconos de cilindros representando almacenamiento de datos etiquetados **"Offline Training Data."** Flecha hacia el ciclo de desarrollo.
- **Ciclo iterativo** con cuatro etapas en flujo circular horario:
  1. **Data Collection** (arriba)
  2. **Cleaning & Visualization** (derecha)
  3. **Feature Eng. & Model Design** (abajo)
  4. **Training & Validation** (izquierda)
- Flechas indican bucle continuo entre las cuatro etapas.

#### Lado derecho — Las salidas

Flecha desde la etapa **"Cleaning & Visualization"** cruza la línea punteada hacia las salidas finales. Dos categorías de resultados:

1. **Reportes:** Captura de pantalla de un dashboard con múltiples visualizaciones de datos: gráficos de líneas, barras y gráficos circulares. Debajo, texto **"(insights …)"** indicando que un objetivo es obtener comprensión de los datos.
2. **Training Pipelines:** Diagrama abstracto de líneas horizontales con nodos y ramificaciones, simbolizando los flujos de trabajo automatizados o estructuras de código usadas para entrenar modelos sistemáticamente.

¿Qué es la salida?

Model Development

(insights …)

Training Pipelines

**Figura:** Slide titulada **"¿Qué es la salida? Model Development"** que ilustra un flujo de trabajo de desarrollo de modelos de machine learning, desde datos crudos hasta salidas finales, dividida por una línea vertical discontinua:

#### Lado izquierdo — El proceso de desarrollo

1. **Fuente de datos:** Tres cilindros negros etiquetados **"Offline Training Data."** Flecha hacia un proceso cíclico.
2. **Ciclo iterativo** de cuatro pasos conectados por flechas:
   - **Data Collection** (punto de inicio del bucle)
   - **Cleaning & Visualization** (segundo paso)
   - **Feature Eng. & Model Design** (tercer paso, ingeniería de características y arquitectura de modelos)
   - **Training & Validation** (cuarto paso, retroalimenta a Data Collection)
3. Flecha desde el ciclo central cruza la línea discontinua hacia el lado derecho.

#### Lado derecho — Las salidas

Dos resultados principales del proceso de desarrollo:

1. **Reportes:** Captura de pantalla de un dashboard de datos con múltiples tipos de visualizaciones: gráficos de líneas, barras y varios gráficos circulares. Debajo, texto **"(insights …)"**.
2. **Training Pipelines:** Ubicado en la parte inferior derecha. Representado por diagrama de tres tuberías/líneas horizontales negras con nodos circulares. La tubería superior se ramifica en dos caminos separados, simbolizando una arquitectura de pipeline para entrenamiento automatizado.

(slides 36–38)

### El pipeline captura las dependencias del Código y datos

El pipeline captura las dependencias del Código y datos

- Basicamente es una descripción de como entrenar el modelo desde diferentes fuentes de datos.

Training Pipelines 🡪 Code

Trained Models 🡪 Binaries

**Figura:** Slide explicando el concepto de un pipeline de entrenamiento de machine learning con diagrama de flujo central de tres partes conectadas por flechas de bloque grandes, de izquierda a derecha:

1. **Izquierda — Input:** Tres cilindros negros apilados etiquetados **"Training Data"**, representando bases de datos o fuentes de datos.
2. **Centro — Proceso:** Etiquetado **"Training Pipelines"**. Representado por un esquema de tres líneas horizontales paralelas. Las líneas superior y media están conectadas por caminos ramificados con nodos circulares negros, sugiriendo un grafo acíclico dirigido (DAG) o serie de pasos computacionales dependientes.
3. **Derecha — Output:** Etiquetado **"Trained Models"**. Representado por un clúster de cuatro círculos superpuestos con líneas y puntos emanando de ellos, sugiriendo visualmente nodos de red neuronal o modelos matemáticos complejos.

- **Training Pipelines** 🡪 **Code**
- **Trained Models** 🡪 **Binaries**

(slide 37)

### Model Development / Training

**Figura:** Diagrama de flujo de machine learning dividido en dos secciones principales: **Model Development** (izquierda) y **Training** (derecha), separadas por una línea vertical delgada. Iconos y texto en blanco y negro.

#### Sección 1 — Model Development (lado izquierdo)

- **Offline Training Data:** El proceso comienza con tres cilindros apilados representando base de datos o almacén de datos etiquetado **"Offline Training Data."**
- **Ciclo iterativo:** Flecha desde la fuente de datos hacia un flujo circular de cuatro pasos:
  1. **Data Collection** (punto de inicio del bucle interno)
  2. **Cleaning & Visualization** (flecha hacia la derecha desde Data Collection)
  3. **Feature Eng. & Model Design** (flecha descendente desde Cleaning)
  4. **Training & Validation** (flecha hacia la izquierda, completando el bucle con flecha ascendente de regreso a Data Collection)

#### Sección 2 — Training (lado derecho)

- **Training Pipelines:** Flecha desde **"Model Development"** conduce a un diagrama de tres líneas horizontales con nodos y ramificaciones, representando **"Training Pipelines."**
- **Live Data:** Debajo de los pipelines, dos iconos de cilindros etiquetados **"Live Data"** con flecha ascendente hacia los Training Pipelines, sugiriendo que los pipelines usan datos frescos para entrenamiento continuo o final.
- **Trained Models:** A la derecha de los pipelines, flecha apunta a un clúster de círculos con flechas salientes (red neuronal), representando **"Trained Models."**
- **Bucle de validación:** Flecha gruesa etiquetada **"Validation"** se origina en la base del área de training y curva hacia arriba apuntando a **"Trained Models"**, indicando paso de evaluación final antes de considerar los modelos listos.

**Figura:** Diagrama de flujo en blanco y negro titulado **"Model Development"** (izquierda) y **"Training"** (derecha), separados por una línea vertical punteada. Ilustra un flujo de trabajo de machine learning.

#### Sección izquierda — Model Development

- **Fuente de datos:** Tres cilindros representando **"Offline Training Data"** conducen al ciclo de desarrollo.
- **Bucle de desarrollo:** Proceso cíclico en sentido horario de cuatro pasos:
  1. **Data Collection** (arriba-izquierda)
  2. **Cleaning & Visualization** (arriba-derecha)
  3. **Feature Eng. & Model Design** (abajo-derecha)
  4. **Training & Validation** (abajo-izquierda)
- Flechas muestran flujo: Collection → Cleaning → Feature Engineering → Training → de regreso a Collection.
- Flecha también sale del paso **"Cleaning & Visualization"** cruzando el divisor vertical hacia la sección Training.

#### Sección derecha — Training

- **Training Pipelines:** Representados por tres barras horizontales paralelas con nodos y ramificaciones. Reciben entrada de la sección Model Development y de una fuente **"Live Data"** (dos cilindros debajo).
- **Trained Models:** Los Training Pipelines conducen a una etapa final representada por diagrama de red neuronal (nodos conectados por líneas).
- **Validation:** Flecha gruesa curva etiquetada **"Validation"** se origina cerca de Live Data y apunta directamente hacia arriba al diagrama **"Trained Models"**, indicando paso de validación final para modelos listos para producción.

(slides 39–40)

### Training / Inference

**Figura:** Diagrama de flujo en blanco y negro que ilustra el ciclo de vida de un sistema de machine learning, dividido en dos secciones principales por una línea vertical punteada: **Training** (izquierda) e **Inference** (derecha).

#### Sección Training (lado izquierdo)

- **Live Data:** En la parte inferior izquierda, dos iconos de cilindros representan fuentes de datos.
- **Training Pipelines:** Una flecha apunta desde "Live Data" hacia un conjunto de líneas horizontales con nodos y ramificaciones, etiquetado "Training Pipelines".
- **Trained Models:** Una flecha conduce desde los pipelines hacia un clúster de círculos con líneas internas (redes neuronales), etiquetado "Trained Models".
- **Validation:** Una flecha etiquetada "Validation" curva desde el área de "Live Data" hacia la entrada de "Trained Models".

#### Sección Inference (lado derecho)

- **Prediction Service:** Un rectángulo grande etiquetado "Prediction Service" contiene un flujo interno con flechas de entrada, nodos de red neuronal, un icono de almacenamiento de datos (cilindro) y un diamante etiquetado **"Logic"** que dirige las salidas.
- **End User Application:** A la derecha, un icono rectangular que representa una interfaz de aplicación.
- **Query:** Una flecha etiquada "Query" apunta desde la End User Application hacia el Prediction Service.
- **Prediction:** Una flecha etiquetada "Prediction" apunta desde el Prediction Service de vuelta hacia la End User Application.

#### Flujo del sistema y feedback

- **Deployment:** Una flecha central apunta desde la sección "Training" cruzando la línea punteada hacia el "Prediction Service", indicando el despliegue del modelo entrenado.
- **Feedback Loop:** Una flecha gruesa en negrita etiquetada **"Feedback"** se origina en la parte inferior del cuadro Prediction Service y viaja de regreso cruzando la línea central, uniéndose a la flecha "Validation" para retroalimentar el proceso de construcción del modelo.

(slide 41)

### Inference

Objetivo: Hacer una predicción en ~10ms

**Figura:** Diagrama técnico titulado "**Inference**" que ilustra el flujo de trabajo entre una aplicación de usuario final y un servicio de predicción backend.

#### Componentes y flujo de datos

1. **Título:** La palabra "**Inference**" aparece centrada en la parte superior en fuente sans-serif grande y negrita.
2. **Prediction Service (caja izquierda):** Un rectángulo grande etiquetado "Prediction Service" contiene un esquema simplificado de la lógica interna de un modelo de machine learning.
   - **Nodos de red neuronal:** Iconos circulares con múltiples líneas de entrada y una línea de salida, representando neuronas artificiales o capas.
   - **Base de datos:** Un icono de cilindro negro (base de datos o feature store) con una flecha apuntando hacia el primer nodo, sugiriendo recuperación de datos para el proceso de inferencia.
   - **Componente Logic:** Una caja en forma de diamante etiquetada "**Logic**" recibe entrada de dos nodos neuronales separados y produce salidas finales.
   - **Feedback:** Una línea negra gruesa etiquetada "**Feedback**" entra por la parte inferior del cuadro "Prediction Service" desde la izquierda, haciendo un bucle de regreso desde una fuente externa.
3. **End User Application (caja derecha):** Un icono rectangular vertical que representa una interfaz de aplicación móvil o web.
4. **Flechas de interacción:**
   - Una flecha de derecha a izquierda etiquetada "**Query**" muestra una solicitud enviada desde la End User Application hacia el Prediction Service.
   - Una flecha de izquierda a derecha etiquetada "**Prediction**" muestra el resultado enviado de vuelta desde el Prediction Service hacia la aplicación.

En la parte inferior de la imagen, un texto grande y negrita en español indica el objetivo: **"Objetivo: Hacer una predicción en ~10ms"**.

(slide 42)

### Ciclo de vida completo: Model Development / Training / Inference

**Figura:** Diagrama de flujo en blanco y negro que ilustra un ciclo de vida estándar de machine learning, dividido en tres secciones horizontales principales: **Model Development**, **Training** e **Inference**.

#### 1. Model Development (sección izquierda)

- **Offline Training Data:** El proceso comienza con un conjunto de tres iconos de cilindros que representan almacenamiento de datos.
- **Bucle iterativo:** Una flecha conduce desde los datos hacia un proceso circular con cuatro pasos:
  - **Data Collection** (arriba-izquierda del bucle)
  - **Cleaning & Visualization** (arriba-derecha del bucle)
  - **Feature Eng. & Model Design** (abajo-derecha del bucle)
  - **Training & Validation** (abajo-izquierda del bucle)
- Una flecha única apunta desde toda esta sección hacia la sección central.

#### 2. Training (sección central)

- **Training Pipelines:** Representados por una serie de líneas horizontales con nodos y caminos ramificados.
- **Live Data:** Dos iconos de cilindros etiquetados "Live Data" se sitúan debajo de los pipelines, con una flecha apuntando hacia arriba hacia el proceso de entrenamiento.
- **Trained Models:** Una flecha conduce desde los pipelines hacia un conjunto de cuatro iconos de red neuronal (círculos con líneas ramificadas) etiquetados "Trained Models".
- **Validation:** Una flecha etiquetada "Validation" conduce desde los trained models de regreso hacia la unión de live data/pipelines, creando un bucle de retroalimentación dentro de esta etapa.

#### 3. Inference (sección derecha)

- **Prediction Service:** Un rectángulo grande que contiene un diagrama interno complejo de nodos, un icono de base de datos y una forma de diamante etiquetada **Logic**. Representa la infraestructura del modelo desplegado.
- **End User Application:** A la derecha, un icono de ventana representa la interfaz de usuario.
  - Una flecha etiquetada **Query** apunta desde la aplicación hacia el Prediction Service.
  - Una flecha etiquetada **Prediction** apunta desde el Prediction Service de vuelta hacia la aplicación.
- **Feedback Loop:** Una flecha gruesa y oscura etiquetada **Feedback** conduce desde la parte inferior del cuadro Prediction Service de regreso hacia la flecha "Validation" en la sección Training, indicando que los datos de rendimiento en el mundo real se usan para mejorar modelos futuros.

(slide 43)

## Ejemplos prácticos

**Figura:** En el lado izquierdo central, un número grande y negrita **"4."** con un subrayado negro grueso. Debajo, el texto **"Ejemplos Prácticos"** en fuente sans-serif azul claro. Una de las formas superiores tiene una superposición de color cian/azul sobre la fotografía arquitectónica. Las fotos muestran distintos ángulos de vigas de concreto, escaleras y espacios abiertos del edificio.

(slide 44)

### Now, its your turn

Now, its your turn

#### Esquina superior izquierda

#### Lado izquierdo (ilustración)

- **Personajes:** Dos robots esféricos rojos idénticos y pequeños. Cada robot tiene:
  - Una línea horizontal negra con dos puntos como ojos.
  - Franjas decorativas verdes a los lados de sus "cabezas".
  - Una hélice en la parte superior de la cabeza, mostrada en movimiento.
  - Brazos flexibles, segmentados, metálicos y grises que terminan en pinzas rojas.
- **Acción (robot izquierdo):** El robot de la izquierda dobla ordenadamente una tela de color beige claro sobre una pila de ropa doblada. La pila consiste en una prenda verde, una azul claro y una azul oscuro.
- **Texto:** Encima del robot de la derecha, la frase **"Now, its your turn"** aparece en fuente cursiva azul claro (sin apóstrofo en "its").

#### Lado derecho (collage arquitectónico)

- **Diseño:** Una serie de fotografías dispuestas dentro de una forma grande en zigzag con contorno cian/azul claro que apunta hacia la derecha.
  - La sección superior muestra la parte inferior de vigas de concreto.
  - La sección central tiene una foto con tinte cian del interior de concreto con escaleras o balcones.
  - Las secciones inferiores muestran pilares verticales de concreto, ventanas y una pared interior con letras negras estilizadas que leen "I O NN GEVEN NIECI RABLE".

(slide 45)

### Resumen de Cierre

#### Modelos y Algoritmos: Puntos Clave

**Ciclo de Vida del Modelo**

- Desde la recolección de datos hasta la inferencia y el feedback continuo.

**Aplicación Práctica**

- Uso de algoritmos en casos reales y su impacto en la toma de decisiones.

**Tu Turno**

- Capacidad de implementar y refinar modelos de manera autónoma.

¡Gracias por participar en la sesión de hoy!

**Figura:** Slide titulada "**Resumen de Cierre**" del curso de UTEC. El título principal "Resumen de Cierre" aparece en fuente sans-serif grande, negrita y negra. El subtítulo "Modelos y Algoritmos: Puntos Clave" aparece en azul brillante. Tres puntos de resumen, cada uno con un icono azul:

1. **Ciclo de Vida del Modelo** — icono de engranaje/engranaje azul. Descripción: "Desde la recolección de datos hasta la inferencia y el feedback continuo."
2. **Aplicación Práctica** — icono de bombilla azul. Descripción: "Uso de algoritmos en casos reales y su impacto en la toma de decisiones."
3. **Tu Turno** — icono de portapapeles con marca de verificación azul. Descripción: "Capacidad de implementar y refinar modelos de manera autónoma."

una de las secciones fotográficas tiene una superposición de color azul brillante.

(slide 46)

## Glosario

- **Static Data:** datos estáticos vinculados a experimentos ML puntuales (**One-Off ML Experiments**, sin pipelines). Nivel base de valor de negocio.
- **Batch Data:** datos por lotes vinculados a **Batch ML Systems** con **batch pipelines**. Nivel intermedio de valor de negocio.
- **Real-Time Data:** datos en tiempo real vinculados a **Real-Time ML Systems** con **streaming/inference pipelines**. Nivel más alto de valor de negocio.
- **TRAIN / INFERENCE:** codificación de flujos en diagramas de pipelines — líneas rojas punteadas = TRAIN; líneas azul/teal sólidas = INFERENCE.
- **Feature Store:** permite recuperar historial y contexto con baja latencia como características pre-calculadas para modelos en línea.
- **Feature Pipeline (Operational):** transforma datos en características y etiquetas; alimenta el Feature Store.
- **Training Pipeline (On-Demand):** entrena modelos con características y etiquetas desde el Feature Store hacia el Model Registry.
- **Inference Pipeline (Operational):** realiza predicciones con modelos y nuevas características.
- **Concept Drift / Data Drift:** cambio de concepto y cambio de datos; ilustrado con inspección visual donde cambian condiciones de referencia (p. ej., borde de color del dispositivo).
- **Selection Policy:** política que estima confianza (**Estimate confidence**) a partir de predicciones de múltiples modelos; produce **CONFIDENT** o **UNSURE**.
- **X y Y:** variables de entrada y salida del modelo ($X \rightarrow y$); se definen en las etapas Scoping y Data del ciclo de vida.
- **Parámetros** ($\theta$): parámetros del modelo aprendidos durante el entrenamiento.
- **Loss** ($L$): función de pérdida.
- **Sobre datos futuros** ($\mathbb{E}_D$): expectativa sobre la distribución de datos.
- **Expresividad:** capacidad de hacer que las funciones $f_\theta(x) \rightarrow y$ sean lo suficientemente expresivas.
- **Bias Inductivo:** capturar conocimiento del dominio y suposiciones clave del problema.
- **Eficiencia:** desarrollar modelos fáciles de entrenar y optimizar computacionalmente.
- **Aprendizaje Supervisado:** aprendizaje con datos etiquetados (**Labeled Data**); incluye **Regresión** (respuesta cuantitativa) y **Clasificación** (respuesta categórica).
- **Aprendizaje por refuerzo:** aprendizaje guiado por **Reward**.
- **Aprendizaje no Supervisado:** aprendizaje con **Unlabeled Data**; incluye **Reducción de Dimensionalidad** y **Clustering**.
- **Convolutional Networks:** arquitecturas para tareas de razonamiento espacial (**spatial reasoning tasks**).
- **Recurrent Networks:** arquitecturas para tareas de razonamiento secuencial (**Sequential reasoning tasks**).
- **Graph Networks:** arquitecturas que operan sobre datos de grafos (**Operating on graph data**).
- **Hiperparámetros:** parámetros y detalles de configuración que no se determinan directamente a través del entrenamiento; se establecen manualmente o se ajustan usando validación cruzada. Ejemplos resaltados en el deck: $\alpha$ (función de pérdida), $\lambda$ (regularización), $\beta$ (momentum), $\eta$ (learning rate), $\mathcal{B}$ (batch size).
- **Training Pipelines → Code:** los pipelines de entrenamiento se materializan como código.
- **Trained Models → Binaries:** los modelos entrenados se materializan como binarios.

**Figura:** Gráfico de marca de UTEC (Universidad de Ingeniería y Tecnología), probablemente usado como slide de cierre o portada. La imagen está dividida verticalmente.

#### Sección izquierda (marca)

- **Color de fondo:** Cian brillante que ocupa aproximadamente el 60% del ancho.
  - **Texto:** "UTEC" en fuente serif mayúscula y negrita. Debajo, en fuente sans-serif más pequeña: "UNIVERSIDAD DE INGENIERÍA Y TECNOLOGÍA".

#### Sección derecha (imagen)

  - **Sujeto:** Una escalera amplia de concreto con barandilla blanca elegante.
  - **Tinte de color:** Uno de los marcos geométricos centrales tiene un filtro de color cian sobre las escaleras; los demás muestran los tonos naturales gris cálido del concreto.
  - **Arquitectura:** El edificio tiene muros y pilares altos de concreto. En un pilar del marco superior derecho, texto vertical negro parcialmente visible que termina en "CATRÓNICA" (probablemente "MECATRÓNICA").

(slide 47)
