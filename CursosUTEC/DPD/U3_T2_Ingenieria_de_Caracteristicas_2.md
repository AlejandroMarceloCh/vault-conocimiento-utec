---
curso: DPD
titulo: U3_T2_Ingeniería de Características_2.pptx
slides: 63
fuente: U3_T2_Ingeniería de Características_2.pptx.pdf
---

# U3_T2_Ingeniería de Características_2.pptx

## Índice

| Sección | Subtemas |
|---|---|
| Objetivo de la Sesión | Objetivo |
| Ingeniería de Características | Feature Engineering (Facebook, 2014) |
| Desbalance de clases (imbalance) | Distribución balanceada vs. desbalanceada; Casos de uso; Causas; Cómo lidiar; Selección de métricas; Resampling; Tomek Links; SMOTE; Métodos a nivel de algoritmos; Cost-sensitive learning; Class-balance loss; Focal loss |
| Aumento de datos (data augmentation) | Introducción; Objetivos; Tipos; Label-preserving (CV y NLP); Perturbación (CV y NLP); Datos sintéticos NLP; GAN; Taxonomía |
| Características aprendidas vs. características generadas | Feature engineering y deep learning; Engineered features (text); Learned features (text); Spam classification; Importancia en producción |
| Análisis exploratorio de datos con Python | Cookbook; Digital Data; Data; Common Techniques; Common Libraries; Data Preparation; POS; Stemming y Lemmatization; N-grams; Word Clouds; Sentiments; Topic Modeling |
| Selección de Características | Recurso invaluable; Eficacia crítica; Crecimiento exponencial |
| Referencias y recursos | Blooket; Books; Reading List |

DS-3022 INGENIERÍA DE CARACTERISTICAS - 2

**Figura:** Centro izquierdo: texto principal «DS-3022» en negro grande, debajo «INGENIERÍA DE CARACTERISTICAS - 2» con una línea horizontal azul claro debajo. Esquina inferior izquierda: robot caricaturesco con cabeza transparente mostrando cerebro y circuitos, saludando, con el texto estilizado azul «DS3022» debajo. una foto muestra el texto «UTEC Universidad de Ingeniería y Tecnología» grabado en un muro de concreto.

DS-3022
INGENIERÍA DE
CARACTERISTICAS - 2

(slides 1)

**Figura:** Centro: encabezado «Índice» y lista numerada de tres temas. algunos segmentos fotográficos están teñidos de azul y otros conservan el tono gris del concreto. En una sección inferior aparece un letrero con icono «i+» y el texto «LA NUEVA INGENIERÍA».

(slides 3)

**Figura:** Esquina inferior izquierda: gráfico decorativo de líneas horizontales discontinuas en amarillo y azul claro con pequeños iconos cuadrados y en forma de «T». Centro: lista numerada de tres temas en texto negro.

(slides 6)

## Objetivo de la Sesión

Objetivo de la Sesión

Objetivo de la Sesión

Proporcionar      una        comprensión   de   la
importancia de la ingeniería de características en
el proceso de modelado de datos y repasar
técnicas prácticas para crear y seleccionar
características efectivas.

**Figura:** una foto muestra un letrero con icono «i» y el texto «LA NUEVA INGENIERÍA»; un segmento fotográfico tiene filtro de color verde.

(slides 2)

## Ingeniería de Características

Ingeniería de Características

**Figura:** Centro izquierdo: número grande negro «1.» con línea horizontal gruesa negra debajo, seguido del título «Ingeniería de Características» en azul claro cursiva. una sección geométrica tiene superposición cian/azul.

Feature Engineering

Feature Engineering
2014

**Figura:** Captura de la primera página del artículo académico «Practical Lessons from Predicting Clicks on Ads at Facebook» (2014). Encabezado azul grande en la parte superior: «Feature Engineering». El documento está en formato académico de dos columnas. Título del artículo: «Practical Lessons from Predicting Clicks on Ads at Facebook». Autores: Xinran He, Junfeng Pan, Ou Jin, Tianbing Xu, Bo Liu, Tao Xu, Yanxin Shi, Antoine Atallah, Ralf Herbrich, Stuart Bowers, and Joaquin Quiñonero Candela. Afiliación: Facebook, 1601 Willow Road, Menlo Park, CA, United States. Emails de contacto: {panjunfeng, oujin, joaquinq, sbowers}@fb.com. El abstract menciona la predicción de clics en anuncios (Click-Through Rate o CTR) como tarea crítica de machine learning para sistemas de publicidad en línea; Facebook con más de 750 millones de usuarios activos diarios y más de 1 millón de anunciantes activos. El modelo propuesto combina árboles de decisión con regresión logística, superando el uso individual de cada método en más de 3%. Se referencia trabajo de Varian y Edelman (2007) sobre modelos de subasta bid and pay-per-click de Google, Yahoo! y Microsoft.

https://scontent.flim38-1.fna.fbcdn.net/v/t39.8562-6/240842589_204052295113548_74168590424110542_n.pdf?_nc_cat=109&ccb=1-7&_nc_sid=e280be&_nc_ohc=0omvdGnM_iQAb4kf1U3&_nc_ht=scontent.fli
m38-1.fna&oh=00_AfCmOW-Y5owoWTqIwqDVtPYQcCi_jNxUiK79ulE1RWsXJQ&oe=66220C0A

(slides 4–5)

## Desbalance de clases (imbalance)

### Distribución de datos balanceada vs. desbalanceada

Desbalance de clases (Class imbalance)

**Figura:** Centro izquierdo: número grande negro «2.» con línea horizontal gruesa negra debajo, seguido del título «Desbalance de clases (Class imbalance)» en azul brillante. un segmento fotográfico tiene superposición azul brillante que coincide con el color del título.

Distribución de datos balanceada vs. desbalanceada

**Figura:** Dos gráficos de barras lado a lado.

Gráfico izquierdo — título: «ML works well when the data distribution is like this:». Eje Y: «Number of examples», escala de 0 a 1,000. Eje X: cinco categorías «Cat», «Dog», «Chair», «Bike», «Person». Cada categoría tiene una barra azul claro de exactamente 1,000 ejemplos, representando un dataset perfectamente balanceado.

Gráfico derecho — título: «Not so well when it is like this:». Eje Y: «Number of examples», escala de 0 a 12,500. Eje X: cinco categorías médicas «Effusion», «Atelectasis», «Mass», «Consolidation», «Hernia». Distribución fuertemente desbalanceada (long-tail): Effusion ~11,500 ejemplos, Atelectasis ~10,000, Mass ~5,000, Consolidation ~4,000, Hernia apenas visible sobre la línea cero. Borde inferior: líneas discontinuas decorativas en azul claro y naranja.

(slides 7–8)

### Detección de fraude y casos de uso

Detección de fraude

A las personas les interesan más los
eventos inusuales/potencialmente
catastróﬁcos.

- Detección de fraude
- Detección de Spam
- Detección de enfermedades
- Predicción de abandono (Churn)
- Filtrado de Cvs
  - Ejemplo. 2% de los cvs pasan por ﬁltrado
- Detección de objetos

Imagen de PyImageSearch

La mayoría de las cajas delimitadoras
no contienen ningún objeto

**Figura:** Texto en rosa en la parte superior: «A las personas les interesan más los eventos inusuales/potencialmente catastróﬁcos.» Lado izquierdo: lista con viñetas de casos de uso (fraude, spam, enfermedades, churn, filtrado de CVs con sub-punto del 2%, detección de objetos). Lado derecho: fotografía de un perro blanco y marrón corriendo en césped con un frisbee amarillo en la boca, cubierta por decenas de rectángulos delimitadores (bounding boxes) de colores superpuestos que representan regiones candidatas de detección de objetos. Crédito: «Imagen de PyImageSearch». Texto inferior centrado: «La mayoría de las cajas delimitadoras no contienen ningún objeto». Borde inferior: líneas discontinuas decorativas en azul claro y amarillo.

(slides 9)

### Causas del desbalance de clases

Causas Desbalance de clases

Causas Desbalance de clases

- Sesgos de muestreo
  - Áreas geográﬁcas limitadas
  - Sesgos de selección
- Específico de Dominio
  - Costoso, lento o inviable recolectar datos de ciertas classes
- Errores de etiquetado

**Figura:** Borde inferior: líneas geométricas abstractas discontinuas en amarillo y azul claro.

(slides 10)

### Cómo lidiar con el desbalance de clases

Cómo lidiar con el Desbalance de clases

Cómo lidiar con el Desbalance de clases

1. Selecionar las métricas correctas (Choose the right metrics)
2. Métodos a nivel de datos
3. Métodos a nivel de Algoritmos

(slides 11)

### 1. Selección de las métricas correctas

1. Selección de las métricas correctas

1. Selección de las métricas correctas

Qué Modelo seleccionarían?

Modelo A vs. Model B confusion matrices

| Model A | Actual CANCER | Actual NORMAL |
|---|---|---|
| Predicted CANCER | 10 | 10 |
| Predicted NORMAL | 90 | 890 |

| Model B | Actual CANCER | Actual NORMAL |
|---|---|---|
| Predicted CANCER | 90 | 90 |
| Predicted NORMAL | 10 | 810 |

**Figura:** Título «1. Selección de las métricas correctas». Pregunta en rosa arriba de las matrices: «Qué Modelo seleccionarían?». Dos matrices de confusión lado a lado comparando Modelo A y Modelo B para clasificación binaria (CANCER vs. NORMAL). Modelo A: TP=10, FP=10, FN=90, TN=890. Modelo B: TP=90, FP=90, FN=10, TN=810. Borde inferior: líneas decorativas en azul, amarillo y verde azulado.

(slides 12)

### Selección de métricas: comparación de modelos

1. Selección de las métricas correctas

El Modelo B tiene más chance de
decirte que tienes Cancer.

1. Selección de las métricas correctas

Modelo A vs. Model B confusion matrices

| Model A | Actual CANCER | Actual NORMAL |
|---|---|---|
| Predicted CANCER | 10 | 10 |
| Predicted NORMAL | 90 | 890 |

| Model B | Actual CANCER | Actual NORMAL |
|---|---|---|
| Predicted CANCER | 90 | 90 |
| Predicted NORMAL | 10 | 810 |

Ambos tiene la misma acuracia: 90%

**Figura:** Mismas dos matrices de confusión de la slide anterior. Anotación en rosa arriba a la derecha: «El Modelo B tiene más chance de decirte que tienes Cancer.» Anotación en rosa abajo al centro: «Ambos tiene la misma acuracia: 90%». Borde inferior izquierdo: líneas geométricas punteadas en amarillo y cian.

(slides 13)

### Métricas simétricas vs. métricas asimétricas

Métricas simétricas vs. métricas asimétricas

Métricas simétricas vs. métricas
asimétricas

| Symmetric metrics | Asymmetric metrics |
|---|---|
| Treat all classes the same | Measures a model's performance w.r.t to a class |
| Accuracy | F1, recall, precision, ROC |

$$\text{Accuracy} = \frac{(TP + TN)}{(TP + FP + TN + FN)}$$

$$F_1\text{-score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2TP}{2TP + FP + FN}$$

- TP: True positives
- TN: True negatives
- FP: False positives
- FN: False negatives

**Figura:** Tabla comparativa de dos columnas (métricas simétricas vs. asimétricas) con fórmulas de Accuracy y F1-score debajo, y definiciones de TP, TN, FP, FN con viñetas. Borde inferior: patrón de líneas discontinuas y punteadas en azul y amarillo.

(slides 14)

### Class imbalance: métricas asimétricas

Class imbalance: métricas asimétricas

Class imbalance: métricas asimétricas

- El rendimiento de tu modelo con respecto a una clase

| | CANCER (1) | NORMAL (0) | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|---|---|
| Model A | 10/100 | 890/900 | 0.9 | 0.5 | 0.1 | 0.17 |
| Model B | 90/100 | 810/900 | 0.9 | 0.5 | 0.9 | 0.64 |

⚠ El puntaje F1 para
CÁNCER como 1 es diferente
del puntaje F1 para NORMAL
como 1⚠

**Figura:** Tabla comparativa de Model A y Model B con columnas CANCER (1), NORMAL (0), Accuracy, Precision, Recall y F1. Ambos modelos tienen Accuracy 0.9 y Precision 0.5, pero Model A tiene Recall 0.1 y F1 0.17 mientras Model B tiene Recall 0.9 y F1 0.64. Advertencia en rojo debajo de la tabla con iconos de advertencia. Borde inferior: líneas discontinuas decorativas en azul claro y amarillo.

(slides 15)

### 2. Método a nivel de datos: Resampling

2. Método a nivel de datos: Resampling

2. Método a nivel de datos: Resampling

| Undersampling | Oversampling |
|---|---|
| Eliminar muestras de la clase mayoritaria | añadir más ejemplos a la clase minoritaria |

**Figura:** Dos diagramas lado a lado.

Undersampling (izquierda): texto «Eliminar muestras de la clase mayoritaria». Diagrama de barras «Original dataset» con barra naranja corta (clase minoritaria) y barra azul muy alta compuesta de múltiples segmentos apilados (clase mayoritaria). Flecha desde la barra azul alta hacia una barra azul significativamente más corta etiquetada «Samples of majority class». Estado final: barra naranja original junto a la barra azul acortada, logrando proporción más balanceada.

Oversampling (derecha): texto «añadir más ejemplos a la clase minoritaria». Diagrama de barras «Original dataset» con barra azul alta (mayoritaria) y barra naranja corta (minoritaria). Flecha desde la barra naranja corta hacia una barra naranja alta compuesta de segmentos apilados etiquetada «Copies of the minority class». Estado final: barra azul original junto a la barra naranja aumentada.

Inferior izquierda: URL de referencia.

https://www.kaggle.com/raaa/resampling-strategies-for-imbalanced-datasets#t1

(slides 16)

### Resampling: riesgos

2. Método a nivel de datos: Resampling

2. Método a nivel de datos: Resampling

| Undersampling | Oversampling |
|---|---|
| Eliminar muestras de la clase mayoritaria | añadir más ejemplos a la clase minoritaria |
| Puede causar pérdida de información | Puede causar overﬁtting |

**Figura:** Mismos dos diagramas de barras de la slide anterior (undersampling con reducción de barra azul mayoritaria; oversampling con aumento de barra naranja minoritaria mediante copias). Adicionalmente, debajo de cada técnica aparece texto en rojo: undersampling — «Puede causar pérdida de información»; oversampling — «Puede causar overfitting». Inferior izquierda: URL de referencia.

https://www.kaggle.com/raaa/resampling-strategies-for-imbalanced-datasets#t1

(slides 17)

### Undersampling: Tomek Links

Undersampling: Tomek Links

Undersampling: Tomek Links

- Encontrar pares de muestras cercanas de clases opuestas.
- Eliminar la muestra de la clase mayoritaria en cada par.
  - Ventajas: Hace el límite de decisión más claro.
  - Desventajas: Hace el modelo menos robusto.

**Figura:** Secuencia de tres scatter plots mostrando el proceso de Tomek Links. Plot izquierdo (estado inicial): distribución de círculos azules (clase mayoritaria) y cuadrados naranjas (clase minoritaria) con solapamiento a lo largo del límite de decisión. Plot central (identificación): pares de un círculo azul y un cuadrado naranja que son vecinos más cercanos entre clases opuestas están resaltados con óvalos verdes, etiquetados «Tomek links». Plot derecho (resultado): los círculos azules que formaban parte de los Tomek links identificados han sido eliminados, dejando un espacio más limpio entre las dos clases y un límite de decisión más claro. Crédito: «Image from https://www.kaggle.com/raaa/resampling-strategies-for-imbalanced-datasets». Borde inferior: líneas tipo circuito en azul y naranja.

(slides 18)

### Oversampling: SMOTE

Oversampling: SMOTE

Oversampling: SMOTE

- Sintetizar muestras de la clase minoritaria como combinaciones convexas
    (aproximadamente lineales) de puntos existentes y sus vecinos más cercanos de la
    misma clase.

**Figura:** Diagrama explicativo de SMOTE. Plot izquierdo: scatter plot 2D con clase mayoritaria representada por muchas marcas «x» y clase minoritaria por pocas marcas «o». Región rectangular con borde discontinuo resalta un cluster de puntos minoritarios («o»). Vista ampliada a la derecha: los puntos minoritarios existentes («o») están conectados por líneas punteadas entre vecinos más cercanos de la misma clase; a lo largo de esas líneas se colocan nuevos círculos etiquetados «Synthetic instances» (instancias sintéticas). Algunas marcas «X» grandes de la clase mayoritaria aparecen en el fondo de la vista ampliada. Crédito: «Image from Analytics Vidhya». Número de slide «19».

(slides 19)

### SMOTE y Tomek Links: limitación dimensional

Oversampling: SMOTE

¡Tanto SMOTE como los Tomek Links solo
funcionan con datos de baja dimensión!

Oversampling: SMOTE

- Sintetizar muestras de la clase minoritaria como combinaciones convexas
    (aproximadamente lineales) de puntos existentes y sus vecinos más cercanos de la
    misma clase.

**Figura:** Mismo diagrama de SMOTE de la slide anterior: scatter plot 2D con clase mayoritaria («x») y minoritaria («o»), región ampliada con líneas punteadas entre vecinos minoritarios y nuevos puntos sintéticos («Synthetic instances») interpolados a lo largo de los segmentos. Adicionalmente, texto en rosa en la parte superior: «¡Tanto SMOTE como los Tomek Links solo funcionan con datos de baja dimensión!». Crédito: «Image from Analytics Vidhya». Número de slide «20».

(slides 20)

### 3. Métodos a nivel de algoritmos

L(X; θ) = ∑_x L(x; θ)

$$L(X; \theta) = \sum_{x} L(x; \theta)$$

**Figura:** Borde inferior: gráfico decorativo de líneas horizontales discontinuas en amarillo y azul claro con pequeños iconos cuadrados y en forma de «T». Centro de la slide: fórmula matemática en tipografía negra.

3. Métodos a nivel de algoritmos

3. Métodos a nivel de algoritmos

- Cost-sensitive learning
- Class-balanced loss
- Focal loss

**Figura:** Centro-izquierda: encabezado «3. Métodos a nivel de algoritmos» en azul claro, seguido de tres viñetas en texto negro.

(slides 21–22)

### Cost-sensitive learning

Cost-sensitive learning

Cost-sensitive learning

- $C_{ij}$: El costo si la clase $i$ es classiﬁcado como clase $j$

| | Actual NEGATIVE | Actual POSITIVE |
|---|---|---|
| Predicted NEGATIVE | $C(0, 0) = C_{00}$ | $C(1, 0) = C_{10}$ |
| Predicted POSITIVE | $C(0, 1) = C_{01}$ | $C(1, 1) = C_{11}$ |

- La pérdida causada por la instancia $x$ de la clase $i$ se convertirá en el promedio ponderado de todas las posibles clasiﬁcaciones de la instancia $x$.

$$L(x; \theta) = \sum_{j} C_{ij} P(j \mid x; \theta)$$

**Figura:** Título «Cost-sensitive learning» en negrita negra en la parte superior izquierda. Primera viñeta con $C_{ij}$ donde las letras $i$ y $j$ aparecen resaltadas en verde. Tabla de costos $2 \times 2$ con encabezados de columnas «Actual NEGATIVE» y «Actual POSITIVE», y encabezados de filas «Predicted NEGATIVE» y «Predicted POSITIVE», con celdas $C(0,0)=C_{00}$, $C(1,0)=C_{10}$, $C(0,1)=C_{01}$, $C(1,1)=C_{11}$. Segunda viñeta con las letras $x$ e $i$ resaltadas en verde. Fórmula centrada debajo.

(slides 23)

### Class-balance loss

Class-balance loss

Class-balance loss

- Dar más peso a las clases raras

Non-weighted loss

$$L(X; \theta) = \sum_{i} L(x_i; \theta)$$

Weighted loss

$$L(X; \theta) = \sum_{i} W_{y_i} L(x_i; \theta)$$

$$W_c = \frac{N}{\text{number of samples of class C}}$$

```python
model.fit(features, labels, epochs=10, batch_size=32, class_weight={"fraud": 0.9, "normal": 0.1})
```

**Figura:** Título «Class-balance loss» en negrita negra. Viñeta «Dar más peso a las clases raras». Etiquetas «Non-weighted loss» y «Weighted loss» en tipografía rosa. Tres fórmulas matemáticas: pérdida no ponderada como suma sobre $i$ de $L(x_i; \theta)$; pérdida ponderada como suma sobre $i$ de $W_{y_i} L(x_i; \theta)$; y definición de peso $W_c = N / \text{number of samples of class C}$. Bloque de código Python en la parte inferior con `model.fit(...)` y `class_weight={"fraud": 0.9, "normal": 0.1}`.

(slides 24)

### Focal loss

Focal loss

Focal loss

- Dar más peso a las muestras difíciles:
    - Disminuir el peso de las muestras bien clasiﬁcadas

$$p_t = \begin{cases} p & \text{if } y = 1 \\ 1 - p & \text{otherwise} \end{cases}$$

$$CE(p_t) = -\log(p_t)$$

$$FL(p_t) = -(1 - p_t)^\gamma \log(p_t)$$

Focal Loss for Dense Object Detection (Lin et al., 2017)

**Figura:** Título «Focal loss» en negrita negra. Dos viñetas anidadas sobre dar más peso a muestras difíciles y disminuir el peso de muestras bien clasificadas. Tres fórmulas matemáticas: definición de $p_t$ como caso $p$ si $y=1$ y $1-p$ en otro caso; entropía cruzada $CE(p_t) = -\log(p_t)$; focal loss $FL(p_t) = -(1-p_t)^\gamma \log(p_t)$. Pie de página con enlace «Focal Loss for Dense Object Detection (Lin et al., 2017)».

(slides 25)

## Aumento de datos (data augmentation)

Aumento de datos (Data augmentation)

**Figura:** Centro izquierdo: número grande negro «3.» con línea horizontal gruesa negra debajo, seguido del título «Aumento de datos (Data augmentation)» en azul brillante. un segmento fotográfico tiene superposición azul brillante que coincide con el color del título. En una pared de concreto visible aparecen fragmentos de texto vertical como «INGE», «NIECI», «RABLE».

(slides 26)

### Introducción

Aumento de datos (Data augmentation)

Aumento de datos (Data augmentation)

"El aumento de datos es la nueva ingeniería de características."
- Josh Wills, prev Director of Data Engineering @ Slack

**Figura:** Título «Aumento de datos (Data augmentation)» en azul brillante y negrita en la parte superior izquierda. Cita central en color rosa/magenta: «"El aumento de datos es la nueva ingeniería de características."» con atribución debajo «- Josh Wills, prev Director of Data Engineering @ Slack» en el mismo color.

(slides 27)

### Data augmentation: objetivos

Data augmentation: objetivos

Data augmentation: objetivos

- Mejorar el rendimiento del modelo en general o en ciertas clases.
- Generalizar mejor.
- Fomentar ciertos comportamientos.

**Figura:** Título «Data augmentation: objetivos» en negrita negra. Tres viñetas en español.

(slides 28)

### Tipos de data augmentation

Data augmentation

Data augmentation

1. Transformación Simple label-preserving
2. Perturbación
3. Síntesis de datos

**Figura:** Título «Data augmentation» en negrita negra. Lista numerada de tres métodos de aumento de datos.

(slides 29)

### Label-preserving: Computer Vision

Label-preserving: Computer Vision

Label-preserving:
Computer Vision

Recorte aleatorio, volteo,
borrado, etc.

Imagen de An Eﬃcient Multi-Scale Focusing Attention Network for Person Re-Identiﬁcation (Huang et al., 2021)

**Figura:** Título «Label-preserving: Computer Vision» en negrita negra. Subtítulo «Recorte aleatorio, volteo, borrado, etc.» en español. Lado derecho: grilla de imágenes de re-identificación de personas con seis columnas etiquetadas «original», «random flip», «random crop», «random erase», «random patch» y «autoaug», y tres filas con tres personas distintas (camiseta roja con shorts, camiseta morada con pantalón negro, camiseta negra con pantalón oscuro). Cada columna muestra la transformación aplicada: «original» muestra las fotos fuente; «random flip» voltea horizontalmente; «random crop» recorta/zoom; «random erase» añade una banda vertical de color tapando parte de la persona; «random patch» inserta un parche rectangular gris o de otra región; «autoaug» aplica cambios automáticos de contraste/brillo/color. Pie de página con enlace «Imagen de An Eﬃcient Multi-Scale Focusing Attention Network for Person Re-Identiﬁcation (Huang et al., 2021)».

(slides 30)

### Label-preserving: NLP

Label-preserving: NLP

Label-preserving: NLP

| | |
|---|---|
| Original | I'm so happy to see you. |
| Generado | I'm so glad to see you. |
| | I'm so happy to see y'all. |
| | I'm very happy to see you. |

**Figura:** Título «Label-preserving: NLP» en negrita negra. Tabla/ejemplo con etiquetas «Original» y «Generado» en la columna izquierda y oraciones en inglés en la columna derecha; en las oraciones generadas las palabras sustituidas o añadidas («glad», «y'all», «very») aparecen resaltadas en negrita.

(slides 31)

### Perturbación: las redes neuronales pueden ser sensibles al ruido

Perturbación: las redes neuronales pueden ser sensibles al ruido.

Perturbación: las redes neuronales
pueden ser sensibles al ruido.

- 67.97% Kaggle CIFAR-10 imágenes del
   test
- 16.04% ImageNet imágenes del test
 pueden ser mal clasiﬁcadas cambiando
 solo un píxel (Su et al., 2017).
 (Su et al., 2017)

| Modelo | Etiqueta correcta | Etiqueta predicha |
|---|---|---|
| AllConv | SHIP | CAR (99.7%) |
| AllConv | HORSE | DOG (70.7%) |
| AllConv | CAR | AIRPLANE (82.4%) |
| AllConv | DEER | AIRPLANE (49.8%) |
| AllConv | HORSE | DOG (88.0%) |
| NiN | HORSE | FROG (99.9%) |
| NiN | DOG | CAT (75.5%) |
| NiN | DEER | DOG (86.4%) |
| NiN | BIRD | FROG (88.8%) |
| NiN | SHIP | AIRPLANE (62.7%) |
| VGG | DEER | AIRPLANE (85.3%) |
| VGG | BIRD | FROG (86.5%) |
| VGG | CAT | BIRD (66.2%) |
| VGG | SHIP | AIRPLANE (88.2%) |
| VGG | CAT | DOG (78.2%) |

**Figura:** Título «Perturbación: las redes neuronales pueden ser sensibles al ruido.» en negrita negra. Viñetas con porcentajes 67.97% (CIFAR-10) y 16.04% (ImageNet) y texto sobre mal clasificación cambiando un solo píxel con cita (Su et al., 2017) repetida. Lado derecho: grilla $3 \times 5$ de imágenes CIFAR-10 de baja resolución organizadas en tres columnas por arquitectura de modelo («AllConv», «NiN», «VGG»); cada imagen muestra un punto blanco indicando el píxel modificado, con etiqueta correcta en negro mayúsculas arriba y etiqueta predicha errónea en azul negrita con porcentaje de confianza abajo (valores concretos en la tabla).

(slides 32)

### Perturbation: Computer Vision

Perturbation: Computer Vision

Perturbation:
Computer Vision

- Ruido aleatorio
- Estrategia de búsqueda
  - DeepFool
    (Moosavi-Dezfooli et al.,
    2016): encontrar la mínima
    inyección de ruido
    necesaria para causar una
    clasiﬁcación errónea con
    alta confianza.

**Figura:** Título «Perturbation: Computer Vision» en negrita negra. Viñetas «Ruido aleatorio» y «Estrategia de búsqueda» con sub-viñeta «DeepFool» (hipervínculo) y descripción de Moosavi-Dezfooli et al., 2016. Lado derecho: cinco imágenes ilustrando ataques adversarios. Arriba: foto de cabeza de ballena emergiendo del agua, etiquetada en magenta «Ballena». Fila central: a la izquierda la misma imagen de ballena casi idéntica al original, etiquetada «Tortuga con ruido DeepFool»; a la derecha visualización del ruido DeepFool como puntos multicolor dispersos sobre fondo negro. Fila inferior: a la izquierda la misma imagen de ballena, etiquetada «Tortuga con ruido fast gradient sign»; a la derecha visualización del ruido fast gradient sign como campo denso de estática multicolor.

(slides 33)

### Perturbation: NLP

Perturbation: NLP

Perturbation: NLP

- Random replacement
      - Ejemplo:
            BERT (10% * 15% = 1.5%)

- 80% of the time: Replace the word with the `[MASK]` token, e.g., `my dog is hairy` → `my dog is [MASK]`
- 10% of the time: Replace the word with a random word, e.g., `my dog is hairy` → `my dog is apple`
- 10% of the time: Keep the word unchanged, e.g., `my dog is hairy` → `my dog is hairy`. The purpose of this is to bias the representation towards the actual observed word.

BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (Devlin et al., 2018)

**Figura:** Título «Perturbation: NLP» en negrita negra. Columna izquierda: viñeta «Random replacement» con sub-viñeta «Ejemplo: BERT (10% * 15% = 1.5%)». Columna derecha: tres viñetas en inglés describiendo la estrategia de enmascaramiento de BERT (80% `[MASK]`, 10% palabra aleatoria, 10% sin cambio) con ejemplos `my dog is hairy` transformado a `my dog is [MASK]`, `my dog is apple`, o sin cambio. Pie de página con enlace «BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (Devlin et al., 2018)».

(slides 34)

### Datos sintéticos: NLP

Datos sintéticos: NLP

Datos sintéticos: NLP

- Template-based
    - Very common in conversational AI
- Language model-based

| | |
|---|---|
| Template | Find me a [CUISINE] restaurant within [NUMBER] miles of [LOCATION]. |
| Generated queries | ● Find me a Vietnamese restaurant within 2 miles of my ofﬁce. |
| | ● Find me a Thai restaurant within 5 miles of my home. |
| | ● Find me a Mexican restaurant within 3 miles of Google headquarters. |

**Figura:** Título «Datos sintéticos: NLP» en negrita negra. Dos viñetas «Template-based» (con sub-viñeta «Very common in conversational AI») y «Language model-based». Tabla con fila «Template» mostrando plantilla con placeholders [CUISINE], [NUMBER], [LOCATION]; fila «Generated queries» con tres consultas generadas donde Vietnamese/2/my office, Thai/5/my home, y Mexican/3/Google headquarters aparecen en negrita.

(slides 35)

### Data augmentation: GAN

Data augmentation: GAN

Data augmentation: GAN

Example: kidney segmentation with
data augmentation by CycleGAN

Data augmentation using generative adversarial networks (CycleGAN) to improve generalizability in CT segmentation tasks (Sandfort et al., 2019)

**Figura:** Título «Data augmentation: GAN» en negrita negra. Texto «Example: kidney segmentation with data augmentation by CycleGAN». Lado derecho: grilla $4 \times 4$ de imágenes de tomografía computarizada (CT) de riñones con cuatro filas numeradas 1–4 y cuatro columnas etiquetadas «CT» (corte CT en escala de grises), «Expert» (segmentación manual de riñones en rojo semitransparente), «Augmentation: CycleGAN» (imágenes sintéticas generadas por CycleGAN con máscara roja), y «Augmentation: Standard» (aumento estándar con máscara roja); flechas blancas en algunas filas señalan regiones de interés. Pie de página con enlace «Data augmentation using generative adversarial networks (CycleGAN) to improve generalizability in CT segmentation tasks (Sandfort et al., 2019)».

(slides 36)

### Taxonomía de image data augmentations

Fig. 2 A taxonomy of image data augmentations covered

Fig. 2 A taxonomy of image data augmentations covered; the colored lines in the figure depict which data augmentation method the corresponding meta-learning scheme uses, for example, meta-learning using Neural Style Transfer is covered in neural augmentation [36]

A survey on Image Data Augmentation for Deep Learning (Connor Shorten & Taghi M. Khoshgoftaar, 2019)

**Figura:** Diagrama de árbol (taxonomía) con nodo raíz «Image Data Augmentation» que se divide en dos ramas principales: «Basic Image Manipulations» (con sub-nodos Kernel Filters, Color Space Transformations, Geometric Transformations, Random Erasing, Mixing Images) y «Deep Learning Approaches» (con sub-nodos Adversarial Training, Neural Style Transfer, GAN Data Augmentation). Varios sub-nodos (Geometric Transformations en azul, Mixing Images en rojo, Neural Style Transfer en verde, entre otros) conectan mediante líneas de colores hacia el nodo central «Meta Learning», que a su vez se ramifica en Neural Augmentation (línea verde), AutoAugment (línea azul) y Smart Augmentation (línea roja). Leyenda de figura debajo. Khoshgoftaar, 2019)».

(slides 37)

## Características aprendidas vs. características generadas

Learned features vs. engineered features

**Figura:** Centro izquierdo: número grande negro «4.» con línea horizontal gruesa negra debajo, seguido del título «Learned features vs. engineered features» en azul brillante. un segmento fotográfico tiene superposición azul brillante que coincide con el color del título. En una pared de concreto visible aparecen fragmentos de texto vertical.

(slides 38)

### Feature engineering

Feature engineering

Feature engineering

¿promete el aprendizaje profundo no más ingeniería de características?

**Figura:** Título «Feature engineering» en negrita negra. Pregunta en gris «¿promete el aprendizaje profundo no más ingeniería de características?».

(slides 39)

### Feature engineering: deep learning en la industria

Feature engineering

Feature engineering

¿promete el aprendizaje profundo no más ingeniería de características?

- Estamos aún lejos de eso
- No todos los modelos de ML de la industria son Deep Learning

**Figura:** Título «Feature engineering» en negrita negra. Pregunta en gris «¿promete el aprendizaje profundo no más ingeniería de características?». Dos viñetas: «Estamos aún lejos de eso» y «No todos los modelos de ML de la industria son Deep Learning».

(slides 40)

### Engineered features: text

Engineered features: text

**Stopword removal**

I have a dog. He's sleeping.

**Lemmatization**

I have dog. He's sleeping.

**Contraction**

I have dog. He's sleep.

**Punctuation**

I have dog. He is sleep.

**Lowercase**

I have dog He is sleep

**N-gram**

i have dog he is sleep

| | col 1 | col 2 | col 3 | col 4 | ... |
|---|---|---|---|---|---|
| # samples (fila 1) | 0 | 3 | 0 | 0 | ... |
| # samples (fila 2) | 1 | 0 | 0 | 0 | ... |
| # samples (fila 3) | 0 | 0 | 1 | 0 | ... |
| # samples (fila 4) | ... | ... | ... | ... | ... |

# features

| I | you | have | dog | cat | he | she | is | they | sleep | I, have | have, dog | good, dog | ... |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Features | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | ... |

Classiﬁer (e.g. LogReg)

**Figura:** La slide presenta el título «Engineered features: text» en la parte superior izquierda, en tipografía grande, negrita y negra. En el centro-izquierda, una columna vertical de seis pasos de preprocesamiento de texto, cada uno con su etiqueta a la izquierda y el texto resultante a la derecha, con palabras o fragmentos resaltados en rosa que indican el cambio aplicado en cada paso: (1) «Stopword removal» transforma «I have **a** dog. He's sleeping.» en «I have dog. He's sleeping.»; (2) «Lemmatization» transforma «I have dog. He's sleep**ing**.» en «I have dog. He's sleep.»; (3) «Contraction» transforma «I have dog. **He's** sleep.» en «I have dog. He is sleep.»; (4) «Punctuation» transforma «I have dog. He is sleep**.**» en «I have dog He is sleep»; (5) «Lowercase» transforma «**I** have dog **H**e is sleep» en «i have dog he is sleep»; (6) «N-gram» muestra el mismo texto «i have dog he is sleep». En el centro-derecha, una matriz numérica etiquetada con «# samples» en el lado izquierdo (filas) y «# features» en la parte superior (columnas), con valores enteros visibles como 0, 3, 0, 0 en la primera fila, 1, 0, 0, 0 en la segunda, 0, 0, 1, 0 en la tercera, y puntos suspensivos en la cuarta fila. Una flecha grande de color rosa apunta desde la matriz hacia la derecha, hacia un recuadro redondeado con borde rosa que contiene el texto «Classiﬁer (e.g. LogReg)». En la parte inferior, una fila de encabezados de vocabulario (I, you, have, dog, cat, he, she, is, they, sleep, I, have, have, dog, good, dog, ...) con una fila «Features» debajo que muestra valores binarios 1 o 0 para cada token o bigrama. Número de slide «41» en la esquina inferior derecha.

(slides 41)

### Learned features: text

Learned features: text

one-hot encoding

| | col 1 | col 2 | col 3 | col 4 | ... |
|---|---|---|---|---|---|
| # samples (fila 1) | 0 | 0 | 0 | 0 | ... |
| # samples (fila 2) | 0 | 0 | 0 | 0 | ... |
| # samples (fila 3) | 0 | 0 | 1 | 0 | ... |
| # samples (fila 4) | ... | ... | ... | ... | ... |

Feature learner (e.g. embeddings)

Classiﬁer (e.g. softmax)

Text

I have a dog. He's sleeping.

| | I | you | have | dog | cat | he | she | is | they | sleep | mom | food | yes | ... |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| One-hot | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | ... |

**Figura:** La slide presenta el título «Learned features: text» en la parte superior izquierda, en tipografía grande, negrita y negra. En la parte superior central, una matriz dispersa de one-hot encoding etiquetada «one-hot encoding» arriba y «# samples» a la izquierda, con mayoría de ceros y unos pocos unos. Una flecha grande de color rosa apunta desde la matriz hacia la derecha, hacia un diagrama de red neuronal: una capa de entrada con cinco nodos verdes conectados densamente a una capa oculta de cinco nodos azules, etiquetada debajo como «Feature learner (e.g. embeddings)»; la capa azul se conecta a un único nodo de salida rojo con una flecha saliente, etiquetada debajo como «Classiﬁer (e.g. softmax)». En la parte inferior, el texto de ejemplo «I have a dog. He's sleeping.» seguido de una tabla one-hot que mapea el vocabulario: I=1, you=0, have=1, dog=1, cat=0, he=1, she=0, is=1, they=0, sleep=0, mom=0, food=0, yes=0, y puntos suspensivos para más columnas. Número de slide «42» en la esquina inferior derecha.

(slides 42)

### Feature engineering: spam classification

Feature engineering: spam classiﬁcation

Más características:

- Frecuencia de publicación, máximo de publicaciones por día
- Repetitividad de las publicaciones
- Detección de idioma, errores tipográﬁcos, puntuación anormal, proporción de mayúsculas/minúsculas
- IP, otros usuarios desde la misma IP
- Palabras NSFW, enlaces en la lista negra

**Figura:** La slide presenta el título «Feature engineering: spam classiﬁcation» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, el subtítulo «Más características:» seguido de una lista con cinco viñetas en español. Número de slide «43» en la esquina inferior derecha.

(slides 43)

### Feature engineering en producción

Feature engineering

- Para tareas complejas, ¡el número de características puede ascender hasta millones!
- Gran parte del trabajo de producción de ML implica idear nuevas características.
  - Los estafadores desarrollan nuevas técnicas muy rápidamente, por lo que es necesario idear nuevas características con la misma rapidez para contrarrestar.

A menudo se requiere conocimiento especializado en la materia.

**Figura:** La slide presenta el título «Feature engineering» en la parte superior izquierda, en tipografía grande, negrita y negra. El contenido consiste en dos bullets principales en español, el segundo con un sub-bullet indentado, y una frase de cierre al pie de la slide. Número de slide «44» en la esquina inferior derecha.

(slides 44)

## Análisis exploratorio de datos con Python

### Exploratory Data Analysis with Python Cookbook

Exploratory Data Analysis with Python Cookbook

**Exploratory Data Analysis with Python Cookbook**

Over 50 recipes to analyze, visualize, and extract insights from structured and unstructured data

Ayodele Oluleye

1ST EDITION

**Figura:** La slide muestra la portada del libro «Exploratory Data Analysis with Python Cookbook» centrada en la diapositiva. La portada tiene un marco negro con el logo de Packt (`<packt>`) en la esquina superior derecha del marco. La mitad superior de la portada presenta una imagen abstracta dorada en espiral que se asemeja a una turbina mecánica o un vórtice con luz emanando del centro. La mitad inferior tiene fondo gris oscuro/negro. En la parte superior del área de título, una etiqueta naranja dice «1ST EDITION». El título principal «Exploratory Data Analysis with Python Cookbook» aparece en letras blancas grandes. Debajo, el subtítulo «Over 50 recipes to analyze, visualize, and extract insights from structured and unstructured data» en texto blanco más pequeño. El nombre del autor «Ayodele Oluleye» aparece en la parte inferior del marco. El fondo de la slide es blanco.

(slides 45)

### Digital Data

Digital Data

- Emails
- Social Media Posts
- Text Messages

**Figura:** La slide presenta el título «Digital Data» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, una lista con tres viñetas: «Emails», «Social Media Posts» y «Text Messages».

(slides 46)

### Data

Data

- Unstructured Data
  - Raw text data

**Figura:** La slide presenta el título «Data» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, una lista con un bullet principal «Unstructured Data» y un sub-bullet con círculo vacío indentado «Raw text data».

(slides 47)

### Common Techniques (Prepare and Analyze)

Common Techniques (Prepare and Analyze)

- Data Preparation
- Removing Stop Words
- Analyzing part of speech (POS)
- Normalization ( stemming and lemmatization)
- Analysis Ngrams
- Creating Word clouds
- Checking term frequency
- Checking Sentiments

**Figura:** La slide presenta el título «Common Techniques (Prepare and Analyze)» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, una lista con ocho viñetas enumerando técnicas de preparación y análisis de texto.

(slides 48)

### Common Libraries

Common Libraries

- Pandas (manipulación de datos)
- Matplotlib (visualización de datos)
- Seaborn (visualización de datos)
- NLTK (Procesamiento de Texto)
- Scikit-learn (ML (incluye procesamiento de texto)
- Gensim (ML- Representación vectorial de texto)
- PyLDAvis (Topic Modeling)

**Figura:** La slide presenta el título «Common Libraries» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, una lista con siete viñetas que nombran bibliotecas de Python con su función entre paréntesis en español.

(slides 49)

### 1. Data Preparation

1. Data Preparation

- Expanding Contractions (don't --> do not)
- Removing Punctuations ( , . - ; )
- Converting to Lowercase (Textual Data -> textual data)
- Performing Tokenization (split text into tokens)
- Removing Stopwords ( remove irrelevant tokens)

**Figura:** La slide presenta el título «1. Data Preparation» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, una lista con cinco viñetas que describen pasos de preparación de datos textuales, cada uno con un ejemplo o descripción entre paréntesis.

(slides 50)

### Analyzing Part of Speech

Analyzing Part of Speech

- Nouns
- Verbs
- Adjectives
- Adverbs

https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

https://universaldependencies.org/u/pos/

**Figura:** La slide presenta el título «Analyzing Part of Speech» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, una lista con cuatro viñetas: «Nouns», «Verbs», «Adjectives» y «Adverbs». En la parte inferior aparecen dos URLs en líneas separadas.

(slides 51)

### Stemming and Lemmatization

Stemming and Lemmatization

- Original Text:
  - "Los estudiantes están estudiando para los exámenes ﬁnales."
- Stemmed Text:
  - "Los estudiant están estudi para los exam ﬁnal."
- Lemmatized Text:
  - "El estudiante está estudiar para el examen ﬁnal."

**Figura:** La slide presenta el título «Stemming and Lemmatization» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, tres bullets que comparan el procesamiento de una oración en español: texto original, texto con stemming (palabras truncadas como «estudiant», «estudi», «exam») y texto con lematización (formas de diccionario como «estudiante», «estudiar», «examen»).

(slides 52)

### Analyzing n-grams

Analyzing n-grams

- Sequence of n tokens
  - 1-gram - unigram
  - 2-gram - bigram
  - 3-gram - trigram

**Figura:** La slide presenta el título «Analyzing n-grams» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, un bullet principal «Sequence of n tokens» con tres sub-bullets indentados que definen unigram, bigram y trigram.

(slides 53)

### N-grams

N-grams

- Sentence: "La casa está en la colina"
  - 1-grams -> ["La", "casa", "está", "en", "la", "colina"]
  - 2-grams -> ["La casa", "casa está", "está en", "en la", "la colina"]
  - 3-grams -> ["La casa está", "casa está en", "está en la", "en la colina"]

**Figura:** La slide presenta el título «N-grams» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, un bullet con la oración de ejemplo «La casa está en la colina» y tres sub-bullets que muestran las listas de unigrams, bigrams y trigrams resultantes.

(slides 54)

### Creating Word Clouds

Creating Word Clouds

- Visual representation
- Most common words

**Figura:** La slide presenta el título «Creating Word Clouds» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, dos viñetas: «Visual representation» y «Most common words».

(slides 55)

### Checking Sentiments: categorías

Checking Sentiments

Categorias

- La película fue increible (positivo)
- La película fue ok (neutro)
- La película fue desastrosa (negativo)

**Figura:** La slide presenta el título «Checking Sentiments» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, el subtítulo «Categorias» en gris, seguido de tres viñetas con ejemplos de oraciones en español y su categoría de sentimiento entre paréntesis: positivo, neutro y negativo.

(slides 56)

### Checking Sentiments: intensidades

Checking Sentiments

Intensidades por Categoria

- La pelicula fue increible (positivo: 0.9, neutro: 0.1, negativo:0.0)
- La pelicula fue ok (positivo: 0.2, neutro:0.6, negativo:0.2)
- La pelicula fue horrible (positivo:0.0, neutro: 0.0, negativo:1.0)

**Figura:** La slide presenta el título «Checking Sentiments» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, el subtítulo «Intensidades por Categoria» en gris, seguido de tres viñetas con ejemplos de oraciones en español y sus puntuaciones de intensidad para las categorías positivo, neutro y negativo (valores que suman 1.0 en cada caso). En la esquina inferior derecha hay un icono de tres formas hexagonales azules y blancas.

(slides 57)

### Topic Modeling

Topic Modeling

- Un documento se basa en:
  - Tópicos (temas) -- palabras más importantes
  - Vocabulario -- palabras complementarias
- Un documento es una distribución probabilística de tópicos y palabras complementarias
- Si tengo tópicos y sus distribuciones puedo construir documentos

**Figura:** La slide presenta el título «Topic Modeling» en la parte superior izquierda, en tipografía grande, negrita y negra. Debajo del título, tres bullets en español: el primero con dos sub-bullets sobre tópicos y vocabulario, el segundo sobre distribución probabilística, y el tercero sobre construcción de documentos a partir de tópicos y distribuciones.

(slides 58)

## Selección de Características

Selección de Características

**Recurso Invaluable**

La selección de características es un recurso invaluable para los científicos de datos.

**Eficacia Crítica**

Seleccionar características importantes es crucial para la eficacia del algoritmo.

Datos irrelevantes, redundantes o ruidosos afectan la precisión y el costo computacional.

**Crecimiento Exponencial**

Es cada vez más importante debido al crecimiento en tamaño y complejidad de los datos promedio.

**Figura:** La slide presenta el título «Selección de Características» en la parte superior izquierda, en tipografía grande, negrita y negra. El fondo es blanco. Tres tarjetas rectangulares de color azul claro están dispuestas horizontalmente en el centro de la slide. Tarjeta izquierda: subtítulo «Recurso Invaluable» en azul negrita, seguido del texto «La selección de características es un recurso invaluable para los científicos de datos.» Tarjeta central: subtítulo «Eficacia Crítica» en azul negrita, seguido del texto «Seleccionar características importantes es crucial para la eficacia del algoritmo.» y, en texto más pequeño y gris, «Datos irrelevantes, redundantes o ruidosos afectan la precisión y el costo computacional.» Tarjeta derecha: subtítulo «Crecimiento Exponencial» en azul negrita, seguido del texto «Es cada vez más importante debido al crecimiento en tamaño y complejidad de los datos promedio.» En la esquina inferior derecha hay un icono estilizado azul y blanco con formas hexagonales y de flecha.

(slides 62)

## Referencias y recursos

### Blooket — Ing caracteristicas

Ing caracteristicas

**Figura:** La slide muestra una captura de pantalla de la interfaz de Blooket para crear o editar un set de preguntas. El fondo general es gris claro con un patrón de hexágonos grandes entrelazados. En el centro, una tarjeta blanca rectangular con sombra contiene: en la parte superior, un rectángulo teal sólido con la palabra «Blooket» en tipografía blanca redondeada; debajo, el título del set «Ing caracteristicas» en gris oscuro; un icono de candado gris con la etiqueta «Private»; un botón grande teal «Save Set» con icono de disquete; y dos botones grises más pequeños: «Edit Info» (con icono de lápiz) a la izquierda y «Time Limit» (con icono de reloj) a la derecha.

(slides 59)

### Books

Books

- Book1 .- Python Data Analytics (2015)
- Book 2 .- Data Analytics A Practical Guide To Data Analytics For -- James Fahl – 2017
- Book3 .- DATA ANALYTICS_ Simple and Effective Tips and Tricks to -- Smith, Benjamin – 2020
- Book4.- Data Analytics -- Nair;Sajeev - New Delhi – 2020

**Figura:** La slide presenta el título «Books» en la parte superior izquierda, en tipografía sans-serif negra. Debajo del título, una lista con cuatro viñetas que enumeran libros con formatos de citación heterogéneos (variaciones en espaciado, guiones, dobles guiones, guiones en y ubicación).

(slides 60)

### Reading List: Data Analytics

Reading List: Data Analytics

**Python Data Analytics**
(2015)

**A Practical Guide To Data Analytics**
James Fahl (2017)

**Simple and Effective Tips and Tricks**
Smith, Benjamin (2020)

**Data Analytics**
Nair; Sajeev - New Delhi (2020)

**Figura:** La slide presenta el título «Reading List: Data Analytics» en la parte superior izquierda, en tipografía grande, negrita y negra. El contenido central consiste en cuatro tarjetas rectangulares de color azul claro dispuestas en una cuadrícula de 2×2. Cada tarjeta muestra el título del libro en azul medio y los datos bibliográficos en gris más pequeño. Tarjeta superior izquierda: «Python Data Analytics» y «(2015)», sin autor indicado. Tarjeta superior derecha: «A Practical Guide To Data Analytics» y «James Fahl (2017)». Tarjeta inferior izquierda: «Simple and Effective Tips and Tricks» y «Smith, Benjamin (2020)». Tarjeta inferior derecha: «Data Analytics» y «Nair; Sajeev - New Delhi (2020)».

(slides 61)

## Glosario

- **TP (True positives):** Casos positivos correctamente clasificados como positivos.
- **TN (True negatives):** Casos negativos correctamente clasificados como negativos.
- **FP (False positives):** Casos negativos incorrectamente clasificados como negativos.
- **FN (False negatives):** Casos positivos incorrectamente clasificados como negativos.
- **Métricas simétricas:** Tratan todas las clases por igual (ej. Accuracy).
- **Métricas asimétricas:** Miden el rendimiento del modelo con respecto a una clase (ej. F1, recall, precision, ROC).
- **Undersampling:** Eliminar muestras de la clase mayoritaria. Puede causar pérdida de información.
- **Oversampling:** Añadir más ejemplos a la clase minoritaria. Puede causar overfitting.
- **Tomek Links:** Pares de muestras cercanas de clases opuestas; se elimina la muestra de la clase mayoritaria en cada par. Ventaja: hace el límite de decisión más claro. Desventaja: hace el modelo menos robusto.
- **SMOTE:** Sintetiza muestras de la clase minoritaria como combinaciones convexas (aproximadamente lineales) de puntos existentes y sus vecinos más cercanos de la misma clase.
- **$C_{ij}$:** El costo si la clase $i$ es clasificado como clase $j$.
- **Class-balance loss:** Dar más peso a las clases raras mediante $W_c = \frac{N}{\text{number of samples of class C}}$.
- **Focal loss:** Dar más peso a las muestras difíciles; disminuir el peso de las muestras bien clasificadas. $FL(p_t) = -(1 - p_t)^\gamma \log(p_t)$.
- **Unigram (1-gram):** Secuencia de un token.
- **Bigram (2-gram):** Secuencia de dos tokens consecutivos.
- **Trigram (3-gram):** Secuencia de tres tokens consecutivos.
- **Stemming:** Reducción de palabras a su raíz truncando sufijos (ej. «estudiantes» → «estudiant»).
- **Lematización:** Reducción de palabras a su forma de diccionario (ej. «estudiantes» → «estudiante»).
- **Topic Modeling:** Un documento se basa en tópicos (palabras más importantes) y vocabulario (palabras complementarias); es una distribución probabilística de tópicos y palabras complementarias.