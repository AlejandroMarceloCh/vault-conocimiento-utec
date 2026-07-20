---
curso: DPD
titulo: U4_T2_Machine Learning In production.pptx
slides: 65
fuente: U4_T2_Machine Learning In production.pptx.pdf
---

# U4_T2_Machine Learning In production.pptx

## Índice

- Introducción a Modelos de Aprendizaje para DPD
- Servidor de Modelos
- Arquitectura de un servicio de predicción
- Recursos y Requerimientos
- Herramientas para despliegue
- Contrafactuales
- Glosario

**Figura:** En el centro-izquierda, en texto grande y negrita, el código de curso **DS-3022**; debajo, en cursiva, el título **Modelos de ML en Producción**. En la esquina inferior izquierda hay un robot caricaturesco con cabeza transparente que muestra una estructura tipo cerebro, saludando con la mano; debajo del robot aparece el texto estilizado **DS3022** en azul. En una de las fotos se lee parcialmente el nombre de la universidad.

## Introducción a Modelos de Aprendizaje para DPD

**Figura:** Número grande **1.** con subrayado negro grueso. Debajo, título en cursiva cian: *Introducción a Modelos de Aprendizaje para DPD*. En el tercio derecho, collage geométrico de fotografías arquitectónicas del campus recortadas en formas hexagonales con bordes cian; una sección superior tiene tinte cian intenso.

### Objetivo de la Sesión

El   objetivo   es   proporcionar   a   los   estudiantes   una
comprensión clara y práctica de cómo llevar un modelo de
Machine Learning desde su fase de desarrollo hasta su
implementación y uso en un entorno de producción.

**Figura:** Slide con fondo cian claro. Título centrado en blanco y negrita: **Objetivo de la Sesión**. Debajo, el párrafo del objetivo en texto blanco. una sección tiene overlay azul cian.

(slides 2)

### Seguimiento de Métricas Comunes

Seguimiento de Métricas Comunes

**Métricas de Software**

- Memoria,
- Latencia,
- Demora de Carga,

**Métricas de entrada**

- Cantidad de datos por segundo
- Número de datos faltantes,
- Volumen de datos,
- Naturaleza de los datos

**Métricas de Salida**

- # Veces retorna "" (null)
- # Veces que el usuario inicia la búsqueda
  (operación)

**Figura:** Título en la parte superior izquierda: **Seguimiento de Métricas Comunes**. Tres bloques de texto organizados verticalmente con encabezados en negrita: **Métricas de Software** (izquierda), **Métricas de entrada** (centro) y **Métricas de Salida** (derecha), cada uno con sus bullets correspondientes.

(slides 4)

### Speech Recognition

**Figura (flujo superior):** Pipeline horizontal de reconocimiento de voz básico. De izquierda a derecha: icono **Audio** (forma de onda sonora azul con nota musical en círculo rojo) → flecha → caja redondeada **Speech Recognition** → flecha → icono **Transcript** (documento azul con nota musical).

**Figura (flujo inferior):** Pipeline con VAD. De izquierda a derecha: icono **Audio** → flecha → caja redondeada **VAD** → flecha → caja redondeada **Speech Recognition** → flecha → icono **Transcript**.

**Figura (esquina superior derecha):** Ilustración comparativa de dos sistemas: a la izquierda, computadora antigua con pantalla verde que muestra *"Hello. I am Eliza."*;

- Solo para audio de
  voz humana

(slides 5)

### User Data → Recommender system → Product recommendations

**Figura:** Diagrama de flujo lineal horizontal de cuatro etapas conectadas por flechas negras de izquierda a derecha:

1. **User Data** — etiqueta sobre un icono de documento (teal y rojo).
2. **User Profile** — caja rectangular redondeada con borde granate que contiene el texto "User Profile".
3. **Recommender system** — caja rectangular redondeada con borde granate que contiene el texto "Recommender system".
4. **Product recommendations** — etiqueta de texto plano como salida final.

(slides 6)

### Proceso Iterativo

Proceso Iterativo

- Código (Algoritmo/modelo)

- Hiperparámetros

- Datos

      Research/Academia

      Product Team

**Figura:** En el lado izquierdo, ciclo iterativo formado por flechas azul claro en bucle circular. En la parte superior del ciclo: **Model + Hyperparameters + Data**. A la derecha del ciclo: **Training**. A la izquierda del ciclo: **Error analysis**. Desde la parte inferior de **Error analysis**, una flecha adicional apunta hacia la etiqueta **Audit performance**. En el centro, tres bullets (Código, Hiperparámetros, Datos) con tres flechas negras que apuntan hacia una caja azul redondeada a la derecha que contiene **Modelo ML** y la notación $X \rightarrow y$. Debajo de los bullets, dos etiquetas apiladas: **Research/Academia** y **Product Team**.

(slides 7)

### Retos del desarrollo del modelo

Retos del desarrollo del modelo

1. Tener un buen desempeño en el conjunto de entrenamiento (generalmente
medido por el error de entrenamiento).

2. Tener buen desempeño con el Test/Dev test

3. Tener un buen desempeño con las métricas/objetivos del negocio.

**Figura:** A la derecha de los puntos 1 y 2, gráfico de dispersión sin título con ejes etiquetados: eje Y **Price**, eje X **Size**. Seis marcas rojas en forma de "X" muestran correlación positiva aproximadamente lineal (a mayor Size, mayor Price).

(slides 8)

### ¿Por qué entrenar un buen rendimiento en el test set no es suficiente?

¿Por qué entrenar un buen rendimiento en el test set no es suﬁciente?

**Ejemplo de Búsqueda web**

"Receta de pie de Limon" "últimas películas"

"Planes de datos"

"UTEC"       "Reddit"     "Youtube"

Consulta    de
Información y
transacción

Consulta   de
Navegación

**Figura:** Título en azul en la parte superior izquierda. Icono de lupa sobre ventana de navegador etiquetado **Ejemplo de Búsqueda web**. Tres consultas de ejemplo agrupadas con llave azul a la derecha bajo la etiqueta **Consulta de Información y transacción**: "Receta de pie de Limon", "últimas películas", "Planes de datos". Tres consultas agrupadas con llave azul bajo la etiqueta **Consulta de Navegación**: "UTEC", "Reddit", "Youtube".

(slides 9)

### Rendimiento en segmentos clave del conjunto de datos

Rendimiento en segmentos clave del conjunto de datos

**Ejemplo: ML para la aprobación de préstamos.**

Asegúrate de no discriminar por etnia, género, ubicación, idioma u
otros atributos protegidos.

**Ejemplo: Recomendaciones de productos de minoristas**

Ten cuidado de tratar de manera justa todas las principales
categorías de usuarios, minoristas y productos.

**Figura:** Título en texto cian claro en la parte superior. Dos secciones con subencabezados en negrita y texto de cuerpo debajo.

(slides 10)

### Distribución sesgada de los datos

Distribución sesgada de los datos

En ejemplo médico: La mayoría de pacientes no padece una enfermedad por tanto
tenemos 99% de clase saludable y 1% de clase enferma

```python
print("0")
```

ya daría un buen resultado para un 99% de acuracia

(slides 11)

### La conversación en muchas empresas

La conversación en muchas empresas

- Funcionó correctamente con el Test set

- Pero no está funcionando con nuestra aplicación

- Pero… funcionó correctamente con el test set

1. Icono de desarrollador (persona detrás de laptop con símbolo `</>`) junto al texto: **"Funcionó correctamente con el Test set"**.
2. Icono de profesional de negocios (mujer) junto al texto: **"Pero no está funcionando con nuestra aplicación"**.
3. Mismo icono de desarrollador junto al texto: **"Pero... funcionó correctamente con el test set"**.

(slides 12)

### Cuando se está iniciado con el modelamiento

Cuando se está iniciado con el modelamiento

- Búsqueda bibliográﬁca para ver qué es posible
  (cursos, blogs, proyectos abiertos).

- Buscar implementaciones de código abierto si están
  disponibles.

- Un algoritmo razonable con buenos datos a menudo
  superará a un gran algoritmo con datos no tan
  buenos.

**Figura:** Título en la parte superior. Tres bullets con el contenido indicado. Icono azul y gris en la esquina inferior derecha.

(slides 13)

### Sanity-Check el algoritmo

Sanity-Check el algoritmo

Intenta ajustar un pequeño conjunto de datos de entrenamiento antes de
entrenar con uno grande.

**Ejemplo #1: Speech recognition**

**Ejemplo #2: Image segmentation**

**Ejemplo #3: Image classiﬁcation**

**Figura (Ejemplo #1):** Esquema pequeño que muestra entrada **X (audio)** con flecha hacia salida **Y (transcript)**, seguido de guiones bajos que representan los espacios de palabras en la transcripción.

**Figura (Ejemplo #2 y #3):** Dos imágenes lado a lado de dos gatitos (uno gris tabby y uno blanco) sentados en hierba. La imagen izquierda es la foto original. La imagen derecha muestra el resultado de segmentación de imagen: los gatitos cubiertos por máscaras de colores (el tabby en naranja/amarillo y el blanco en verde) separados del fondo.

(slides 14)

## Servidor de Modelos

**Figura:** Número grande **2.** con subrayado negro grueso. Debajo, título en cursiva cian: *Servidor de Modelos*. En el lado derecho, collage geométrico de fotografías arquitectónicas del campus en formas de diamante y hexágono; una forma central tiene overlay cian azul transparente.

### ¿Qué es un servidor de Modelos?

¿Qué es un servidor de Modelos?

Entrenar un
Modelo es solo la
primera parte

Proveer un                           Disponibilizar el
servicio/App para                       modelo para el
la interacción                            usuario

**Figura:** Diagrama triangular con tres cajas rectangulares azules redondeadas conectadas por flechas negras formando un ciclo en sentido horario:

1. **Caja superior:** "Entrenar un Modelo es solo la primera parte" — con icono circular de proceso iterativo con nodos hexagonales. Flecha hacia abajo-derecha.
2. **Caja derecha:** "Disponibilizar el modelo para el usuario" — con icono de silueta de persona (usuario). Flecha hacia la izquierda.
3. **Caja izquierda:** "Proveer un servicio/App para la interacción" — con icono de mano haciendo clic en un cuadrado. Flecha hacia arriba, completando el ciclo.

(slides 16)

### Métricas importantes en ambientes reales — Latencia

Métricas importantes en ambientes reales

Latencia

Métricas

Costo

Rendimiento

**Figura:** Diagrama central con un círculo azul sólido en el centro etiquetado **Métricas** (texto blanco). Tres círculos periféricos conectados al centro: arriba, círculo con borde naranja etiquetado **Latencia**; abajo-izquierda, círculo con borde azul etiquetado **Costo**; abajo-derecha, círculo con borde teal etiquetado **Rendimiento**.

Métricas importantes en ambientes reales

Latencia:

Latencia:

Métricas

Costo

Rendimiento

100ms

200ms

Latencia = 100ms + 200ms = 300ms

- Tiempo de respuesta entre la acción del usuario y la respuesta del
  servidor a esta acción

- Latencia de todo el proceso, empezando el envío de los datos al servidor,
  calcular la respuesta (inferencia) usando un modelo y enviar la
  respuesta

- La latencia es crucial para mantener la satisfacción del usuario

Ejemplo: Sistema de recomendación de búsqueda de hotel

**Figura (diagrama central):** Icono de laptop a la izquierda (usuario) e icono de nube/base de datos a la derecha (servidor). Flecha de laptop a servidor etiquetada **100ms**. Flecha de servidor a laptop etiquetada **200ms**. Debajo del servidor: **Latencia = 100ms + 200ms = 300ms**.

**Figura (esquina superior derecha):** Diagrama de Venn con tres círculos superpuestos etiquetados **Latencia** (arriba), **Costo** (abajo-izquierda) y **Rendimiento** (abajo-derecha). La intersección central es un círculo azul sólido etiquetado **Métricas**.

(slides 17, 18)

### ¿Por qué la latencia es difícil?

¿Por qué la latencia es difícil?

Conseguir Baja latencia (< 10ms) para predicciones complejas

Modelo                              Querie    Features

Top K

```sql
SELECT * FROM
users JOIN items,
click_logs, pages
WHERE …
```

Considerando Muchos datos y con fallas de
sistema

**Figura:** Tres columnas que representan componentes que contribuyen a la latencia:

1. **Modelo (columna izquierda):** Diagrama superior de árbol de decisión azul con dados rojos en las ramas; diagrama inferior de red neuronal con capa de entrada, tres capas ocultas y capa de salida con nodos interconectados.

2. **Querie (columna central):** Barras horizontales azules apiladas con llave etiquetada **Top K** indicando selección de los mejores resultados;

3. **Features (columna derecha):** Fragmento SQL mostrando join de múltiples tablas grandes.

Texto inferior: **"Considerando Muchos datos y con fallas de sistema"**.

(slides 19)

### Modelos Lineales Básicos (generalmente de alta dimensión)

Modelos Lineales Básicos (generalmente de alta ﬁmensión)

- Común para modelos de filtros de texto (spam)
- Consulta x codificada en Bolsa-de-Palabras dispersa:
  $x = \text{"El Zorro veloz"} = \{(\text{"zorro"}, 1), (\text{"el"}, 1), (\text{"veloz"}, 1)\}$

- Generando la predicción:

$$\text{Predict}(x) = \sigma \left( \sum_{(w, c) \in x} \theta_{w} \, c \right)$$

- $\theta$ es un vector grande de pesos para cada palabra posible o
  combinación de palabras

**Figura:** Título en la parte superior. Tres bullets con el contenido indicado; el segundo bullet muestra el ejemplo de codificación Bolsa-de-Palabras; el tercer bullet precede a la fórmula matemática central de predicción con función de activación $\sigma$ y sumatoria sobre pares $(w, c)$ con pesos $\theta_w$.

(slides 20)

### Métricas importantes en ambientes reales — Rendimiento

**Rendimiento:**

- Número de respuestas satisfactorias por unidad de tiempo (1 segundo)
- En algunas aplicaciones solo el rendimiento es importante, no la latencia (ejemplo de cámaras de seguridad)

**Figura:** En la esquina superior derecha, diagrama circular de tres métricas relacionadas. En el centro hay un círculo sólido azul etiquetado **Métricas**. Alrededor, tres círculos con contorno conectados al centro: arriba, círculo con contorno naranja etiquetado **Latencia**; abajo a la izquierda, círculo con contorno azul etiquetado **Costo**; abajo a la derecha, círculo con contorno verde azulado etiquetado **Rendimiento**.

(slides 21)

### Baja latencia, alto rendimiento

Los modelos se vuelven más complejos

Usar hardware especializado para la predicción

[1] Deep Residual Learning for Image Recognition. He et al. CVPR 2015.

**Figura (parte superior):** Diagrama arquitectónico grande de una red neuronal profunda que fluye de izquierda a derecha. Comienza con un nodo **input** a la izquierda. La arquitectura muestra múltiples ramas paralelas de operaciones: convoluciones (cajas azules), pooling (cajas rojas) y concatenaciones (cajas verdes) que se fusionan y dividen repetidamente. Hay múltiples puntos terminales etiquetados con **softmax** en cajas amarillas. La estructura visual es característica de una arquitectura tipo Inception.

**Figura (parte inferior derecha):** Fotografía de una GPU NVIDIA Tesla (modelo antiguo tipo K80), representando hardware de computación de alto rendimiento.

(slides 22)

### Métricas importantes en ambientes reales — Costo

**Costo:**

- Costo asociado con cada inferencia (tendría que ser minimizado)
- Algunos requerimientos de infraestructura pueden ser caros:
- CPU
- Aceleradores de hardware como GPU
- Otra infraestructura.

**Figura:** En la esquina superior derecha, el mismo diagrama circular de métricas: círculo central azul sólido **Métricas**, rodeado por tres círculos con contorno conectados — arriba **Latencia** (contorno naranja), abajo izquierda **Costo** (contorno azul), abajo derecha **Rendimiento** (contorno verde azulado). Debajo del texto de bullets, icono en línea de una mano agarrando una bolsa de dinero.

(slides 23)

### Minimizar Latencia / Maximizar Rendimiento

**Minimizar Latencia**

Sistema de recomendación de Aerolineas

Reducir latencia para satisfacción de Usuarios

**Maximizar Rendimiento**

Sistema de recomendación de Aerolineas

Reciben grandes cantidades de requerimiento de inferencias por segundo

Escala de infraestructura (número de servidores) para satisfacer los requerimientos

**Figura:** En la esquina superior izquierda, icono de balanza (equilibrio) en línea negra. Dos bloques horizontales apilados con etiquetas teal a la izquierda:

- Bloque superior: etiqueta redondeada teal **Minimizar Latencia** → rectángulo teal grande con texto *Sistema de recomendación de Aerolineas* y *Reducir latencia para satisfacción de Usuarios*.
- Bloque inferior: etiqueta redondeada teal **Maximizar Rendimiento** → rectángulo teal grande con texto *Sistema de recomendación de Aerolineas* y *Reciben grandes cantidades de requerimiento de inferencias por segundo*.

En la parte inferior, flecha azul larga apuntando a la derecha que abarca todo el ancho, con el texto *Escala de infraestructura (número de servidores) para satisfacer los requerimientos*.

(slides 24)

### En nuestro contexto

**Figura:** Diagrama técnico de pipeline de Machine Learning dividido en tres etapas de izquierda a derecha, separadas por líneas verticales punteadas:

1. **Model Development** (sección izquierda): Comienza con **Offline Training Data** (tres iconos de cilindros de base de datos apilados). Flecha hacia un ciclo iterativo de cuatro pasos en bucle circular: **Data Collection** → **Cleaning & Visualization** → **Feature Eng. & Model Design** → **Training & Validation** (que retroalimenta a Data Collection). Flecha final hacia la siguiente etapa.

2. **Training** (sección central): **Training Pipelines** representados por líneas horizontales con nodos circulares e iconos de engranaje. Recibe entrada de Model Development y también **Live Data** (otro conjunto de iconos de base de datos). Las pipelines producen **Trained Models** (varios diagramas de redes neuronales con nodos circulares interconectados).

3. **Inference** (sección derecha, etiquetada **Inferenc**): **Prediction Service** — caja grande con lógica interna: modelos entrenados (iconos de nodos), almacén de datos local (icono de cilindro) y nodo central en forma de diamante etiquetado **Logic**. A la derecha, **End User Application** (icono de pantalla de computadora con UI) envía **Query** al servicio y recibe **Prediction**. Flecha gruesa etiquetada **Feedback** desde la parte inferior del Prediction Service de vuelta a la etapa Training; la flecha se divide, con un camino etiquetado **Validation** que retroalimenta a **Trained Models**.

(slides 25)

### Predicción

Objetivo: Hacer la predicción en ~10ms bajo carga intermitente

Adicionalmente "complicado" con Deep Neural Networks

→ Nuevos Algoritmos ML y Sistemas

**Figura:** Diagrama de flujo de **Predicción**. Caja izquierda **Prediction Service** con elementos internos: varios iconos de nodos de red neuronal (círculos con líneas ramificadas), flechas de flujo de información, un icono de cilindro de base de datos, y nodo en forma de diamante etiquetado **Logic** que procesa la salida. Flecha gruesa negra etiquetada **Feedback** desde la parte inferior de la caja hacia un icono de silueta humana abajo a la izquierda. Centro/derecha: dos flechas horizontales entre el servicio y **End User Application** (icono de UI con bloques rectangulares): flecha **Query** desde la aplicación hacia el servicio; flecha **Prediction** desde el servicio hacia la aplicación.

(slides 26)

### Benchmark Analysis of Representative Deep Neural Network Architectures

TitanXP

Mobile (Jetson TX1)

**Figura:** Dos gráficos de dispersión lado a lado titulados *Benchmark Analysis of Representative Deep Neural Network Architectures*.

**Ejes comunes:**
- Eje Y: **Top-1 accuracy [%]**, escala lineal de 55% a 85%, con eje roto entre 60% y 65%.
- Eje X: **Images per second [FPS]**, escala logarítmica.
- Puntos de datos: círculos de colores representando arquitecturas específicas (AlexNet, ResNet, VGG, MobileNet, Inception, NASNet-A-Large, SENet-154, Inception-ResNet-v2, SqueezeNet-v1.1, DenseNet-121, GoogLeNet, etc.).
- Curva de frontera de Pareto: curva negra sólida conectando los modelos más eficientes en cada nivel de precisión.
- Gradiente de fondo: transición de naranja/rojo (baja velocidad, izquierda) a amarillo y verde claro (alta velocidad, derecha).

**Gráfico (a) — TitanXP:**
- Rango eje X: aproximadamente 10 a 1000 FPS.
- Modelos de alta precisión (NASNet-A-Large, SENet-154, Inception-ResNet-v2) agrupados arriba a la izquierda, >80% precisión, ~20–40 FPS.
- Modelos de alta velocidad (AlexNet, SqueezeNet-v1.1, MobileNet-v1) a la derecha; AlexNet ~800 FPS, ~57% precisión.
- Rango medio: ResNet-50, DenseNet-121, GoogLeNet con ~70–75% precisión y ~150–300 FPS.

**Gráfico (b) — Mobile (Jetson TX1):**
- Rango eje X: aproximadamente 1 a 100 FPS (desplazado a la izquierda respecto a TitanXP).
- Todos los modelos significativamente más lentos; NASNet-A-Large <3 FPS.
- MobileNet-v1 y SqueezeNet-v1.1 alcanzan 60–90 FPS con 60–70% precisión.
- ResNet-50 cae a ~25 FPS.

**Pie de figura:** FIGURE 3: Top-1 accuracy vs. number of images processed per second (with batch size 1) using the Titan Xp (a) and Jetson TX1 (b).

(slides 27)

### Google Translate Servicio

140 billion palabras al día¹

82,000 GPUs corriendo 24/7

"Si cada uno de los teléfonos Android del mundo usara la nueva búsqueda por voz de Google solo durante tres minutos al día, estos ingenieros se dieron cuenta de que la compañía necesitaría el doble de centros de datos" — Wired

¡Diseñaron Hardware!

Tensor Processing Unit (TPU)

[1] https://www.nytimes.com/2016/12/14/magazine/the-great-ai-awakening.html

**Figura:** Slide dividida en dos columnas.

**Columna izquierda:** Captura de pantalla de la interfaz web de Google Translate. Caja teal con estadística **140 billion palabras al día¹**. Texto **82,000 GPUs corriendo 24/7**.

**Columna derecha:** Captura del encabezado del paper *Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation* (Yonghui Wu, Mike Schuster, Zhifeng Chen, et al.). Cita de Wired sobre teléfonos Android y centros de datos. Rectángulo negro redondeado grande con texto **¡Diseñaron Hardware! Tensor Processing Unit (TPU)**.

(slides 28)

### Modelo De predicción — Dos enfoques

Dos enfoques

- Offline: Pre-Calcular las predicciones
- Online: Calcular las predicciones en tiempo real

**Figura:** Diagrama de flujo en la mitad superior. debajo del círculo la etiqueta **Model**. Derecha: icono de interfaz de usuario etiquetado **Aplicación** (con botón de reproducción rojo y bloques de contenido). Entre modelo y aplicación: flecha azul **Query** desde la aplicación hacia el modelo; flecha verde **Decisión** desde el modelo hacia la aplicación. En la mitad inferior, título **Dos enfoques** con dos ítems; la línea **Offline: Pre-Calcular las predicciones** resaltada con fondo naranja claro.

Dos enfoques

- Offline: Pre-Calcular las predicciones
- Online: Calcular las predicciones en tiempo real

**Figura:** etiqueta **Model** debajo. Derecha: icono de interfaz **Aplicación**. Flecha azul **Query** desde aplicación hacia modelo; flecha verde **Decisión** desde modelo hacia aplicación. Abajo, título **Dos enfoques** con dos ítems; **Offline: Pre-Calcular las predicciones** resaltado con fondo naranja claro.

Dos enfoques

- Offline: Pre-Calcular las predicciones
- Online: Calcular las predicciones en tiempo real

**Figura:** icono **Aplicación** a la derecha; flechas **Query** (azul) y **Decisión** (verde). Abajo, **Dos enfoques** con dos ítems; en esta slide la línea **Online: Calcular las predicciones en tiempo real** resaltada con fondo naranja claro.

(slides 29, 37, 38)

### Pre-Calcular las predicciones

**Figura:** Diagrama de flujo de alto nivel dividido en dos secciones por línea vertical punteada: **Training** (izquierda) e **Inference** (derecha).

**Sección Training (izquierda):**
- Abajo izquierda: dos iconos de cilindros de base de datos etiquetados **Live Data**; flecha hacia arriba a las pipelines.
- **Training Pipelines**: líneas horizontales con nodos y camino ramificado.
- Flecha hacia **Trained Models**: grupo de cuatro círculos superpuestos con líneas radiantes.
- Flecha gruesa negra etiquetada **Validation** desde **Live Data** curvándose hacia **Trained Models**.

**Transición:** Flecha horizontal desde **Trained Models** cruzando la línea divisoria hacia **Prediction Service**.

**Sección Inference (derecha):**
- **Prediction Service**: caja rectangular grande con sub-diagrama interno — varios iconos de modelos (círculos con líneas), icono de base de datos pequeño, nodo central en diamante etiquetado **Logic**, flechas de flujo de datos.
- Flecha gruesa negra etiquetada **Feedback** desde la parte inferior de Prediction Service de vuelta a la sección Training.
- Derecha: icono **End User Application**.
- Flecha superior **Query** desde la aplicación hacia Prediction Service.
- Flecha inferior **Prediction** desde Prediction Service hacia la aplicación.

(slides 30)

### Predicciones pre-calculadas — Training

Training

**Figura:** Diagrama de la fase de Training para predicciones pre-calculadas.

- Abajo izquierda: dos cilindros negros **Live Data**.
- Arriba: icono **Training Pipelines** (líneas horizontales con nodos y caminos ramificados); flecha ascendente desde Live Data.
- Derecha de pipelines: icono **Trained Models** (grupo de círculos con líneas radiantes); flecha desde Training Pipelines.
- Flecha gruesa negra **Validation** curvándose desde Live Data hacia Trained Models.
flecha desde Trained Models hacia el framework.
- Abajo derecha: cilindro negro grande **Todas las posibles consultas**; flecha ascendente hacia Training Framework.

(slides 31)

### Predicciones pre-calculadas — Batch Scoring y almacenamiento

**Figura:** Diagrama de flujo de predicciones pre-calculadas de izquierda a derecha.

**Etapa Training y Validación (izquierda):**
- Sección parcialmente etiquetada **Training**.
- Sliders horizontales **Pipelines** → icono de red neuronal **Trained Models**.
- Flecha negra **Validation** en bucle desde pipelines hacia trained models.

**Etapa Batch Scoring (centro):**
- Desde abajo: cilindro negro **All Possible Queries** con flecha hacia Training Framework.
- Flecha de salida etiquetada **(Scoring)**.

**Etapa Almacenamiento (derecha):**
- **Sistema de Base de datos** — icono verde grande de base de datos con tabla interna de dos columnas **X** (consulta) y **Y** (predicción pre-calculada).

**Figura:** Diagrama de flujo completo de predicciones pre-calculadas.

**Etapa inicial — Datos y Training:**
- Abajo izquierda: dos iconos de base de datos negros **Live Data** → **Training Pipelines** (líneas ramificadas con nodos).
- Flecha **Validation** desde Live Data directamente a **Trained Models** (nodos circulares interconectados).

**Etapa central — Motor de Scoring:**
- Abajo: icono de base de datos negro **All Possible Queries** con flecha hacia el framework.
- El framework recibe Trained Models y All Possible Queries para scoring.

**Etapa final — Almacenamiento:**
- Flecha **(Scoring)** desde Spark hacia **Data Management System**.
- Tabla interna simplificada con columnas **X** (input/query) y **Y** (output predicho).

(slides 32, 33)

### Predicciones pre-calculadas — Servicio de baja latencia

Servicio de baja latencia

**Figura:** Diagrama arquitectónico organizado en tres secciones de izquierda a derecha.

**Fase de Pre-cálculo / Scoring (izquierda):**
- Cilindro negro abajo izquierda: **All Possible Queries**.
- Flecha etiquetada **(Scoring)** hacia el sistema de base de datos central.

**Sistema de Almacenamiento (centro):**
- Cilindro verde grande **Sistema de base de datos** con tabla interna de columnas **X** y **Y**.

**Fase de Aplicación / Serving (derecha):**
- Icono de interfaz web/móvil **Aplicación** (con botón de reproducción y bloques de contenido).
- Flecha verde **Query** desde Aplicación hacia la base de datos.
- Flecha naranja **Decisión** desde la base de datos hacia Aplicación.

**Contexto de rendimiento:** En la parte inferior, bracket naranja grande abarcando base de datos y aplicación, con texto **Servicio de baja latencia**.

(slides 34)

### Predicciones pre-calculadas — Ventajas

**Ventajas:**

- Aprovechar la infraestructura existente de servicio de datos y entrenamiento de modelos.
- Mejora el rendimiento de hardware.
- Consultas más rápidas
- Rendimiento más predecible

**Figura (fondo atenuado):** Diagrama arquitectónico difuminado de sistema de predicción batch. Elementos visibles: **Data Management System**, **Spark / Batch Training / (Scoring)**, icono de base de datos **MySQL**, caja **Application**, flecha **Low-Latency Serving** desde MySQL hacia la aplicación, caja **Decision** entre base de datos y aplicación.

(slides 35)

### Predicciones pre-calculadas — Problemas

**Problemas:**

- Requiere todas las posibles consultas antes
  - Dominio de entrada pequeño y acotado.
- Requiere un aumento sustancial en espacio
  - Ejemplo: Ranking de contenido para cada usuario!
- Update Costoso → Recalcular los rankings

**Figura (fondo atenuado):** Diagrama arquitectónico difuminado. Lado izquierdo: caja con **(Spark) Batch training** y cilindro **All Possible Queries** abajo. Centro: icono de base de datos **MySQL** dentro de bloque **Data Management System**; debajo texto **Low-Latency Serving**. Derecha: flecha hacia caja **Decision** → icono de navegador **Application**.

(slides 36)

### Sistema de Predicción

Sistemas especializados que generan predicciones en tiempo de consulta

**Figura:** Caja grande marrón claro titulada **Sistema de Predicción** (esquina superior izquierda de la caja: **Prediction Service**). Elementos internos: icono de cilindro de **Database**; múltiples iconos de círculos con líneas ramificadas representando **Logic** o nodos de modelo; icono en forma de diamante; flechas de flujo de datos de izquierda a derecha hacia la salida de predicción. Palabra **Logic** impresa dentro de la caja. Derecha: icono de ventana de software **End User Application** (bloques negros y líneas horizontales). Flecha negra **Query** desde Application hacia Prediction Service; flecha negra **Prediction** desde Prediction Service hacia Application. Línea gruesa negra etiquetada **Feedback** desde la parte inferior de la caja curvándose hacia la izquierda.

(slides 39)

### Edge / Cloud

**Figura:** Diagrama de arquitectura técnica de un sistema de Machine Learning en producción, organizado de izquierda a derecha en capas **Edge** y **Cloud**.

**Capas de alto nivel:**
- **Edge** (extremo izquierdo): lado del cliente.
- **Cloud** (resto del diagrama), subdividido en:
  - **Infraestructura/Gateway**: Load Balancer y capa Cache.
  - **Aplicación**: capa de procesamiento principal con múltiples servicios.
  - **Base de datos** (extremo derecho): capa de almacenamiento.

**Componentes:**
- **Client**: pila de iconos verdes representando múltiples clientes.
- **Load Balancer**: barra vertical azul que recibe tráfico entrante.
- **Cache**: barras verticales grises después del load balancer y frente a la base de datos.
- **Node.js**: pila de contenedores rosas en la capa Aplicación (servidor web/API gateway).
- **Django (Python)**: otra pila de contenedores rosas en Aplicación, etiquetada para **Feedback**.
- **Prediction Service**: pila de contenedores naranjas en Aplicación, dedicada a inferencia ML.

**Flujo principal de Request/Predicción (círculos negros 1–9):**
1. Client envía request al Load Balancer.
2. Load Balancer enruta (pasando por Cache) al servicio **Node.js**.
3. Node.js se comunica con **Database** (PostgreSQL).
4. Database retorna datos a Node.js.
5. Node.js envía request al **Prediction Service**.
6. Prediction Service puede interactuar con **Database**.
7. Database retorna datos al Prediction Service.
8. Prediction Service retorna resultado (inferencia) a Node.js.
9. Node.js envía respuesta final al **Client**.

**Flujo de Feedback (círculos morados 10–12):**
- **10 (Feedback)**: Client envía datos de feedback directamente al servicio **Django**.
- **11**: Django se comunica con **Prediction Service**.
- **12**: Django envía datos a **Database**.

(slides 40)

## Arquitectura de un servicio de predicción

### Diseño simple de un Sistema de predicción

Diseño simple de un Sistema de predicción

Predicción

Fortalezas

- Usamos tecnologías ya existentes
- Facil de desarrollar

Tecnologías web ya existentes

https://web.eecs.umich.edu/~mosharaf/Readings/Clipper.pdf

**Figura:** Título en la parte superior izquierda en azul: «Arquitectura de un servicio de predicción». En el lado izquierdo, un recuadro naranja claro con borde redondeado etiquetado «Diseño simple de un Sistema de predicción». Debajo del recuadro, el texto «Tecnologías web ya existentes». En el lado derecho, la sección «Fortalezas» con dos viñetas: «Usamos tecnologías ya existentes» y «Facil de desarrollar». En la parte inferior derecha, la URL de referencia: `https://web.eecs.umich.edu/~mosharaf/Readings/Clipper.pdf`.

(slides 41)

## Recursos y Requerimientos

**Figura:** En el centro-izquierda, el numeral grande y en negrita «3.» con una línea horizontal negra gruesa debajo. Debajo, el texto «Recursos y Requerimientos» en fuente sans-serif azul claro e itálica. marco central apuntando hacia abajo con espacio interior de concreto; marcos inferiores inclinados con fachada de ventanas verticales estrechas y muro interior de concreto con letras grandes dispuestas verticalmente formando partes de palabras: «IN», «GENIE», «NIECI», «RABLE».

### Limitaciones de recursos y costos

Limitaciones de recursos y costos

- Tamaño del modelo
- Funciones complejas
- Latencia
- Acuracia de la predicción

**Figura:** Título en la parte superior izquierda en azul: «Limitaciones de recursos y costos». En el centro, una flecha vertical grande de color gris apuntando hacia arriba, indicando un aumento en la demanda de recursos y costos. A la derecha de la flecha, tres factores listados de arriba hacia abajo, cada uno con un icono en blanco y negro: (1) icono de red neuronal con el texto «Tamaño del modelo / Funciones complejas»; (2) icono de dos nubes conectadas por una línea con un reloj, con el texto «Latencia»; (3) icono de diana con dos dardos en el centro, con el texto «Acuracia de la predicción». A la izquierda de la flecha central, un icono más pequeño dentro de un cuadrado redondeado con un patrón circular tipo laberinto y una flecha pequeña apuntando hacia arriba.

Limitaciones de recursos y costos

- GPU
- TPU
- Modelo

**Figura:** Título en la parte superior izquierda en azul: «Limitaciones de recursos y costos». En el centro, una ecuación visual: lado izquierdo, un cuadrado redondeado gris claro que contiene un icono circular de procesador o chip con una flecha grande apuntando hacia arriba, simbolizando un aumento en la demanda de recursos computacionales; en el centro, un signo de igualdad grande y en negrita «=»; lado derecho, un icono de gráfico de barras con una línea ascendente terminada en flecha y un signo de dólar ($) en un círculo, simbolizando el aumento de costos financieros. A la derecha, una llave vertical grande «{» agrupa tres etiquetas apiladas verticalmente: «GPU», «TPU», «Modelo».

(slides 43, 44)

## Herramientas para despliegue

**Figura:** En el centro-izquierda, el numeral grande y en negrita «3.» con una línea horizontal negra gruesa debajo. Debajo, el texto «Herramientas para despliegue» en fuente sans-serif azul claro e itálica. marco central apuntando hacia abajo con espacio interior de concreto; marcos inferiores inclinados con fachada de ventanas verticales estrechas y muro interior de concreto con letras grandes dispuestas verticalmente formando partes de palabras: «INN», «GEVE», «NIE», «CI», «RABLE».

### Casos de estudio - Iris — Carga del dataset

Casos de estudio - Iris

```python
# load dependencies
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# load the dataset
url = "iris.data"

# column names to use
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# read the dataset from the URL
dataset = pd.read_csv(url, names=names)

# check the first few rows of iris-classification data
dataset.head()
```

**Figura:** Título en la parte superior izquierda en azul: «Casos de estudio - Iris». En el centro, un bloque de código con fondo oscuro y resaltado de sintaxis, numerado de la línea 1 a la 19, que importa dependencias (`pandas`, `train_test_split`, `StandardScaler`, `KNeighborsClassifier`, `classification_report`, `confusion_matrix`), define la URL `"iris.data"`, los nombres de columnas `['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']`, lee el dataset con `pd.read_csv` y muestra las primeras filas con `dataset.head()`.

(slides 46)

### Casos de estudio - Iris — Preprocesamiento

Casos de estudio - Iris

```python
# load dependencies
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# load the dataset
url = "iris.data"

# column names to use
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# read the dataset from the URL
dataset = pd.read_csv(url, names=names)

# check the first few rows of iris-classification data
dataset.head()
```

```python
# separate the independent and dependent features
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Split dataset into random training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, test_size=0.20)
# feature standardization
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
```

**Figura:** Título en la parte superior izquierda en azul: «Casos de estudio - Iris». Bloque superior (líneas 1–19): carga de dependencias y dataset Iris, idéntico al de la slide 46. Bloque inferior (líneas 1–13): separación de características independientes (`X`) y dependientes (`y`), división train/test con `test_size=0.20`, y estandarización con `StandardScaler` aplicada a `X_train` y `X_test`.

(slides 48)

### Casos de estudio - Iris — Entrenamiento y evaluación

Casos de estudio - Iris

```python
# load dependencies
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

# load the dataset
url = "iris.data"

# column names to use
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# read the dataset from the URL
dataset = pd.read_csv(url, names=names)

# check the first few rows of iris-classification data
dataset.head()
```

```python
# separate the independent and dependent features
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# split dataset into random training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, test_size=0.20)

# feature standardization
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
```

```python
# training a KNN classifier
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# make predictions on the testing data
y_predict = model.predict(X_test)

# check results
print(confusion_matrix(y_test, y_predict))
print(classification_report(y_test, y_predict))
```

**Figura:** Título en la parte superior izquierda en azul: «Casos de estudio - Iris». Bloque superior izquierdo (líneas 1–19): carga de dependencias y dataset Iris. Bloque superior derecho (líneas 1–14): separación de características, división train/test y estandarización. Bloque inferior (líneas 1–10): entrenamiento de un clasificador KNN con `n_neighbors=5`, predicción sobre `X_test` y evaluación con `confusion_matrix` y `classification_report`.

(slides 49)

### Guardar el Modelo Usando Pickle

Guardar el Modelo Usando Pickle

El módulo pickle puede ser utilizado para serializar y deserializar los objetos de Python. El "pickling" es el proceso de convertir una jerarquía de objetos de Python en un flujo de bytes, mientras que el "unpickling" es el proceso de convertir un flujo de bytes (de un archivo binario u otro objeto que parezca estar hecho de bytes) de nuevo a una jerarquía de objetos.

```python
import pickle

# save the iris classification model as a pickle file
model_pkl_file = "iris_classifier_model.pkl"

with open(model_pkl_file, 'wb') as file:
    pickle.dump(model, file)
```

**Figura:** Título en la parte superior izquierda en azul: «Guardar el Modelo Usando Pickle», con la palabra «Pickle» subrayada en naranja. Párrafo explicativo en español sobre el módulo pickle, el proceso de «pickling» (convertir una jerarquía de objetos de Python en un flujo de bytes) y «unpickling» (convertir un flujo de bytes de vuelta a una jerarquía de objetos). En el centro, bloque de código con fondo oscuro que importa `pickle`, define `model_pkl_file = "iris_classifier_model.pkl"` y guarda el modelo con `pickle.dump(model, file)` en modo `'wb'`.

Guardar el Modelo Usando Pickle

El módulo pickle puede ser utilizado para serializar y deserializar los objetos de Python. El "pickling" es el proceso de convertir una jerarquía de objetos de Python en un flujo de bytes, mientras que el "unpickling" es el proceso de convertir un flujo de bytes (de un archivo binario u otro objeto que parezca estar hecho de bytes) de nuevo a una jerarquía de objetos.

```python
import pickle

# save the iris classification model as a pickle file
model_pkl_file = "iris_classifier_model.pkl"

with open(model_pkl_file, 'wb') as file:
    pickle.dump(model, file)
```

```python
# load model from pickle file
with open(model_pkl_file, 'rb') as file:
    model = pickle.load(file)

# evaluate model
y_predict = model.predict(X_test)

# check results
print(classification_report(y_test, y_predict))
```

**Figura:** Título en la parte superior izquierda en azul: «Guardar el Modelo Usando Pickle», con la palabra «Pickle» subrayada en naranja. Párrafo explicativo sobre pickle y unpickling. Bloque superior: guardado del modelo con `pickle.dump` en modo `'wb'`. Bloque inferior: carga del modelo con `pickle.load` en modo `'rb'`, evaluación con `model.predict(X_test)` e impresión de `classification_report(y_test, y_predict)`.

(slides 50, 51)

### Ventajas y desventajas del Pickle en Python

Ventajas del Pickle en Python:

- **Módulo Estándar:** Fácil de usar para guardar/restaurar modelos de ML.
- **Versatilidad:** Maneja la mayoría de objetos de Python, incluidos personalizados.
- **Eficiencia:** Rápido para modelos pequeños.
- **Restauración Completa:** Devuelve modelos a su estado original.

**Figura:** Título en azul claro: «Ventajas del Pickle en Python:». Cuatro viñetas con términos clave en negrita seguidos de descripción: Módulo Estándar, Versatilidad, Eficiencia y Restauración Completa.

Ventajas del Pickle en Python:

- **Módulo Estándar:** Fácil de usar para guardar/restaurar modelos de ML.
- **Versatilidad:** Maneja la mayoría de objetos de Python, incluidos personalizados.
- **Eficiencia:** Rápido para modelos pequeños.
- **Restauración Completa:** Devuelve modelos a su estado original.

Desventajas del Pickle en Python:

- **Seguridad:** Riesgo al deserializar datos no confiables.
- **Compatibilidad:** Limitaciones entre versiones de Python y SO.
- **Tamaño de Archivo:** Grandes modelos resultan en archivos enormes.
- **Seguimiento:** Dificulta rastrear cambios en modelos actualizados frecuentemente.

**Figura:** Dos secciones de texto. Sección superior con título en azul claro «Ventajas del Pickle en Python:» y cuatro viñetas (Módulo Estándar, Versatilidad, Eficiencia, Restauración Completa). Sección inferior con título en azul claro «Desventajas del Pickle en Python:» y cuatro viñetas (Seguridad, Compatibilidad, Tamaño de Archivo, Seguimiento).

(slides 52, 53)

### Guardar el Modelo Usando Joblib

Guardar el Modelo Usando Joblib

Joblib es una herramienta del ecosistema Scipy que facilita la canalización en Python, enfocándose en almacenamiento en caché, memorización y computación paralela. Está optimizado para arrays de NumPy, siendo ideal para modelos de ML con muchos parámetros.

```python
import joblib

# save model with joblib
filename = 'joblib_model.sav'
joblib.dump(model, filename)
```

"Para guardar el modelo, debes definir un nombre de archivo con extensión '.sav' o '.pkl' y llamar al método dump() de Joblib.

Similar a pickle, Joblib ofrece el método load() para cargar el modelo de ML guardado."

**Figura:** Título en la parte superior izquierda en azul: «Guardar el Modelo Usando Joblib», con la palabra «Joblib» subrayada en naranja. Párrafo explicativo sobre Joblib como herramienta del ecosistema Scipy optimizada para arrays de NumPy. Bloque de código central con fondo oscuro (líneas 1–5): importa `joblib`, define `filename = 'joblib_model.sav'` y guarda el modelo con `joblib.dump(model, filename)`. Texto inferior con instrucciones para guardar el modelo definiendo un nombre de archivo con extensión '.sav' o '.pkl' y llamando al método `dump()` de Joblib, y nota de que Joblib ofrece el método `load()` para cargar el modelo guardado.

Guardar el Modelo Usando Joblib

Similar a pickle, Joblib ofrece el método load() para cargar el modelo de ML guardado."

```python
import joblib

# save model with joblib
filename = 'joblib_model.sav'
joblib.dump(model, filename)
```

```python
# load model with joblib
loaded_model = joblib.load(filename)

# evaluate model
y_predict = model.predict(X_test)

# check results
print(classification_report(y_test, y_predict))
```

**Figura:** Título en la parte superior izquierda en azul: «Guardar el Modelo Usando Joblib», con la palabra «Joblib» subrayada en naranja. Bloque superior (líneas 1–5): guardado del modelo con `joblib.dump`. Bloque inferior (líneas 1–8): carga del modelo con `joblib.load(filename)` en `loaded_model`, evaluación con `model.predict(X_test)` e impresión de `classification_report(y_test, y_predict)`.

(slides 54, 55)

### Pros y contras de Joblib

Guardar el Modelo Usando Joblib

Pros :

- Rendimiento rápido, ideal para grandes requisitos de memoria.
- Serialización paralelizable para mejor rendimiento en multicore.
- Uso eficiente de memoria con formato mapeado en memoria.
- Características de seguridad robustas y lista blanca de funciones.

**Figura:** Título en azul: «Guardar el Modelo Usando Joblib», con «Joblib» subrayado en naranja. Sección «Pros :» con cuatro viñetas listando ventajas de Joblib: rendimiento rápido para grandes requisitos de memoria, serialización paralelizable para multicore, uso eficiente de memoria con formato mapeado en memoria, y características de seguridad robustas con lista blanca de funciones.

Guardar el Modelo Usando Joblib

Pros :

- Rendimiento rápido, ideal para grandes requisitos de memoria.
- Serialización paralelizable para mejor rendimiento en multicore.
- Uso eficiente de memoria con formato mapeado en memoria.
- Características de seguridad robustas y lista blanca de funciones.

Contras :

- Optimizado principalmente para matrices numpy (puede fallar con otro tipo de objetos).
- Menos flexibilidad en comparación con Pickle.
- Menos conocido; puede ser difícil encontrar documentación.

**Figura:** Título en azul: «Guardar el Modelo Usando Joblib», con «Joblib» subrayado en naranja. Sección «Pros :» con cuatro viñetas de ventajas. Sección «Contras :» con tres viñetas de desventajas: optimizado principalmente para matrices numpy (puede fallar con otro tipo de objetos), menos flexibilidad en comparación con Pickle, y menos conocido con documentación difícil de encontrar.

(slides 56, 57)

### Guardar el Modelo Manualmente Json

Guardar el Modelo Manualmente            Json

Cuando deseas tener control total sobre el procedimiento de guardar y restaurar tu modelo de ML. A diferencia de los otros dos métodos, este no guarda directamente el modelo de ML en un archivo; en su lugar, necesitas definir explícitamente los diferentes parámetros de tu modelo para guardarlos.

```python
import json

# create json save function
def save_json(model, filepath, X_train, y_train):
    saved_model = {}
    saved_model["algorithm"] = model.get_params()['algorithm']
    saved_model["max_iter"] = model.get_params()['leaf_size']
    saved_model["solver"] = model.get_params()['metric']
    saved_model["metric_params"] = model.get_params()['metric_params']
    saved_model["n_jobs"] = model.get_params()['n_jobs']
    saved_model["n_neighbors"] = model.get_params()['n_neighbors']
    saved_model["p"] = model.get_params()['p']
    saved_model["weights"] = model.get_params()['weights']
    saved_model["X_train"] = X_train.tolist() if X_train is not None else "None"
    saved_model["y_train"] = y_train.tolist() if y_train is not None else "None"

    json_txt = json.dumps(saved_model, indent=4)
    with open(filepath, "w") as file:
        file.write(json_txt)

# save the iris-classification model in a json file
file_path = 'json_model.json'
save_json(model, file_path, X_train, y_train)
```

**Figura:** Título en la parte superior izquierda: «Guardar el Modelo Manualmente» en azul, seguido de «Json» en naranja y subrayado. Párrafo explicativo indicando que este método no guarda directamente el modelo de ML en un archivo, sino que requiere definir explícitamente los parámetros del modelo. Bloque de código con fondo oscuro que define la función `save_json(model, filepath, X_train, y_train)` la cual extrae parámetros del modelo mediante `model.get_params()` (mapeando `leaf_size` a `"max_iter"` y `metric` a `"solver"`), convierte `X_train` y `y_train` a listas con `.tolist()`, serializa con `json.dumps(saved_model, indent=4)` y escribe al archivo. Al final, define `file_path = 'json_model.json'` y llama `save_json(model, file_path, X_train, y_train)`.

Guardar el Modelo Manualmente            Json

Para leer este archivo JSON, solo necesitas abrirlo y acceder a los parámetros de la siguiente manera:

```python
# create json load function
def load_json(filepath):
    with open(filepath, "r") as file:
        saved_model = json.load(file)

    return saved_model

# load model configurations
saved_model = load_json('json_model.json')
saved_model
```

Desafortunadamente solo guarda un archivo (retrain)

**Figura:** Título: «Guardar el Modelo Manualmente» en azul, seguido de «Json» en naranja y subrayado. Texto instructivo: «Para leer este archivo JSON, solo necesitas abrirlo y acceder a los parámetros de la siguiente manera:». Bloque de código con fondo oscuro (líneas 1–10) que define `load_json(filepath)` usando `json.load(file)` y carga las configuraciones con `saved_model = load_json('json_model.json')`. A la derecha del bloque de código, captura de pantalla del objeto `saved_model` cargado, mostrando un diccionario con las claves y valores: `'algorithm': ['auto']`, `'max_iter': [30]`, `'solver': ['minkowski']`, `'metric_params': [None]`, `'n_jobs': [None]`, `'n_neighbors': [5]`, `'p': [2]`, `'weights': ['uniform']`, y `'X_train'` con listas anidadas de valores float (por ejemplo `[[-0.2951554541985178, -1.7452457384767541, 0.22911404969983298, 0.2301821098754603], ...]`). Texto en la parte inferior: «Desafortunadamente solo guarda un archivo (retrain)».

Guardar el Modelo Manualmente            Json

Pros:

- **Interoperabilidad:** Ideal para intercambiar modelos entre diferentes sistemas.
- **Legibilidad:** Formato basado en texto, adecuado para inspección humana.
- **Ligereza:** Menores tamaños de archivo que Pickle o Joblib; ideal para transferencias web.
- **Seguridad:** Minimiza amenazas al no ejecutar código durante deserialización.

Contras:

- **Compatibilidad:** Limitado a ciertos tipos de datos; no siempre apto para modelos avanzados.
- **Velocidad:** Serialización/deserialización puede ser más lenta en modelos grandes.
- **Flexibilidad:** Menor adaptabilidad en el proceso de serialización.
- **Precisión:** Formato con pérdida; no conserva toda la información del modelo original.

**Figura:** Título: «Guardar el Modelo Manualmente» en azul, seguido de «Json» en naranja y subrayado. Sección «Pros:» en azul con cuatro viñetas (Interoperabilidad, Legibilidad, Ligereza, Seguridad). Sección «Contras:» en azul con cuatro viñetas (Compatibilidad, Velocidad, Flexibilidad, Precisión).

(slides 58, 59, 60)

### Guardar el Modelo Usando Tensorflow

Guardar el Modelo Usando Tensorflow

```python
# import tensorflow dependencies
from tensorflow.keras.models import Sequential, model_from_json
from tensorflow.keras.layers import Dense

# define model architecture
model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X_train, y_train, epochs=150, batch_size=10, verbose=0)

# save model and its architecture
model.save('model.h5')
```

**Figura:** Título en la parte superior izquierda en azul: «Guardar el Modelo Usando Tensorflow», con la palabra «Tensorflow» subrayada en naranja. En el centro, bloque de código con fondo oscuro y resaltado de sintaxis, numerado de la línea 1 a la 18, que importa dependencias de TensorFlow/Keras (`Sequential`, `model_from_json`, `Dense`), define la arquitectura del modelo secuencial con tres capas `Dense` (12 neuronas con `input_dim=4` y activación `'relu'`, 8 neuronas con activación `'relu'`, 1 neurona con activación `'sigmoid'`), compila con `loss='categorical_crossentropy'`, `optimizer='adam'` y `metrics=['accuracy']`, entrena con `model.fit(X_train, y_train, epochs=150, batch_size=10, verbose=0)` y guarda el modelo con `model.save('model.h5')`.

Guardar el Modelo Usando Tensorflow

```python
# import tensorflow dependencies
from tensorflow.keras.models import Sequential, model_from_json
from tensorflow.keras.layers import Dense

# define model architecture
model = Sequential()
model.add(Dense(12, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X_train, y_train, epochs=150, batch_size=10, verbose=0)

# save model and its architecture
model.save('model.h5')
```

Model: "sequential_6"

| Layer (type) | Output Shape | Param # |
|---|---|---|
| dense_18 (Dense) | (None, 12) | 60 |
| dense_19 (Dense) | (None, 8) | 104 |
| dense_20 (Dense) | (None, 1) | 9 |

Total params: 173

Trainable params: 173

Non-trainable params: 0

```python
from tensorflow.keras.models import load_model

model = load_model('model.h5')
model.summary()
```

**Figura:** Título en la parte superior izquierda en azul: «Guardar el Modelo Usando Tensorflow», con la palabra «Tensorflow» subrayada en naranja. En la parte superior izquierda, bloque de código con fondo oscuro (líneas 1–18) idéntico al de la slide anterior: definición, compilación, entrenamiento y guardado del modelo con `model.save('model.h5')`. En la parte superior derecha, tabla de resumen del modelo etiquetada `Model: "sequential_6"` con columnas «Layer (type)», «Output Shape» y «Param #», mostrando tres capas `dense_18`, `dense_19` y `dense_20` con formas de salida `(None, 12)`, `(None, 8)` y `(None, 1)` y 60, 104 y 9 parámetros respectivamente; totales: 173 parámetros totales, 173 entrenables y 0 no entrenables. En la parte inferior, bloque de código más grande con fondo oscuro que importa `load_model` desde `tensorflow.keras.models`, carga el modelo con `model = load_model('model.h5')` y verifica la arquitectura con `model.summary()`.

(slides 61, 62)

### Ventajas y desventajas de Tensorflow

Ventajas

- Simplicidad: Uso directo de save() y load_model().
- Completitud: Arquitectura, optimizador y pesos en un solo archivo.
- Flexibilidad: Soporta HDF5, SavedModel (.pb) y TensorFlow Lite (.tflite).

Desventajas

- Tamaño: Archivos pueden ser grandes con muchas capas/parámetros.
- Compatibilidad: Posibles problemas entre diferentes versiones de Keras/TensorFlow.
- Limitaciones: Restricciones a características de Keras para almacenar modelos.

**Figura:** Sección «Ventajas» con tres viñetas: Simplicidad (uso directo de `save()` y `load_model()`), Completitud (arquitectura, optimizador y pesos en un solo archivo) y Flexibilidad (soporta HDF5, SavedModel `.pb` y TensorFlow Lite `.tflite`). Sección «Desventajas» con tres viñetas: Tamaño (archivos grandes con muchas capas/parámetros), Compatibilidad (posibles problemas entre versiones de Keras/TensorFlow) y Limitaciones (restricciones a características de Keras para almacenar modelos).

(slides 63)

**Figura:** Slide de transición con banner institucional de UTEC. marcos circundantes con escaleras, muros y pilares de concreto en luz cálida natural; en un muro del marco superior derecho se lee parcialmente el texto «CATRÓNIC» (parte de «MECATRÓNICA»). Sin contenido textual adicional de la lección.

## Contrafactuales

### Definición y propiedades

Contrafactuales

Let us consider a learning model $f(\theta, x)$:

- $f()$ — is the decision function.
- $\theta$ — is the parameters vector, previously adjusted
- $x$ — is the instance.

A counterfactual consists of a synthetic sample $x' = x + a$ based on the action $a$ that achieves the outcome $y'$ thus $f(\theta, x') = y'$ or $f(\theta, x') \geq y'$.

Important property: reduce the cost function $c(\cdot)$ of changing the instance. Then, $\min c(x, x')$.

https://github.com/interpretml/DiCE

**Figura:** Título en la parte superior izquierda en azul: «Contrafactuales». Texto en inglés con definiciones matemáticas del modelo de aprendizaje $f(\theta, x)$ y de contrafactuales como muestra sintética $x' = x + a$. En la parte inferior derecha, dos gráficos lado a lado. Gráfico izquierdo (espacio de características): ejes $x_1$ (horizontal) y $x_2$ (vertical); punto de instancia original etiquetado $x$; cinco vectores de acción $a$ que parten de $x$ hacia puntos sintéticos etiquetados $x + a^1$, $x + a^2$, $x + a^3$, $x + a^4$ y $x + a^5$; región sombreada en azul que representa el resultado deseado donde $r(a) \geq \tau$; área blanca donde $r(a) < \tau$; frontera de decisión curva separando ambas regiones. Gráfico derecho (espacio de costo): ejes $c_1(a)$ (horizontal) y $c_2(a)$ (vertical); puntos etiquetados $c(a^1)$, $c(a^2)$, $c(a^3)$, $c(a^4)$ y $c(a^5)$ que mapean las acciones del primer gráfico al espacio de costo-beneficio; región sombreada en azul indicando el conjunto de acciones con costo aceptable. En la parte inferior, URL de referencia: `https://github.com/interpretml/DiCE`.

(slides 65)

## Glosario

- **Latencia:** Tiempo de respuesta entre la acción del usuario y la respuesta del servidor a esta acción. Latencia de todo el proceso, empezando el envío de los datos al servidor, calcular la respuesta (inferencia) usando un modelo y enviar la respuesta.
- **Pickling:** Proceso de convertir una jerarquía de objetos de Python en un flujo de bytes.
- **Unpickling:** Proceso de convertir un flujo de bytes (de un archivo binario u otro objeto que parezca estar hecho de bytes) de nuevo a una jerarquía de objetos.
- **$f(\theta, x)$:** Función de decisión del modelo de aprendizaje, donde $\theta$ es el vector de parámetros previamente ajustados y $x$ es la instancia.
- **Rendimiento:** Número de respuestas satisfactorias por unidad de tiempo (1 segundo).
- **Contrafactual:** Consiste en una muestra sintética $x' = x + a$ basada en la acción $a$ que logra el resultado $y'$, de modo que $f(\theta, x') = y'$ o $f(\theta, x') \geq y'$. Propiedad importante: reducir la función de costo $c(\cdot)$ de cambiar la instancia; entonces, $\min c(x, x')$.
