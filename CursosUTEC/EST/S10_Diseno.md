---
curso: EST
titulo: S10- Diseño
slides: 23
fuente: S10- Diseño.pdf
---

# S10- Diseño

## Índice

Capítulo de Estadística y Probabilidades 2. Contenido transcrito de las diapositivas (fórmulas en LaTeX, figuras descritas).

# S10 — Diseño de Experimentos

## Slide 1 — Portada

**DISEÑO DE EXPERIMENTOS**

S10

Estadística y probabilidades II | UTEC

---

## Slide 2 — Definición de Experimento

Denominamos experimento, a una prueba o serie de pruebas para observar algún fenómeno, en las cuales se inducen cambios deliberados en las variables de entrada (factores controlables, susceptibles a manipulación o no controlables) de un proceso o sistema, de manera que sea posible observar e identificar las causas de los cambios en la variable de salida (variable respuesta, variable dependiente no manipulable).

---

## Slide 3 — Diseño Estadístico de Experimentos

El diseño estadístico de experimentos es esencialmente el plan para poner a funcionar el experimento, especificando el arreglo de las unidades experimentales en el tiempo y/o espacio, y el patrón de observaciones que va a reportar información. Por lo tanto, el diseño es una secuencia compleja de etapas proyectadas para garantizar que los datos sean obtenidos de tal manera que permitan un análisis objetivo, soportado en inferencias válidas respecto al planteamiento del problema, el cual debe ser lo más preciso posible y además viable económicamente.

Un buen diseño experimental es aquel que proporciona la información requerida con el mínimo esfuerzo experimental.

---

## Slide 4 — Conceptos Fundamentales I: Factor

**Factor:** Es una variable independiente o variable de entrada que puede afectar los resultados del experimento. Los factores se pueden clasificar en controlables y no controlables. El interés principal del experimentador es evaluar el efecto de estos factores.

---

## Slide 5 — Conceptos Fundamentales II: Tratamiento y Unidad Experimental

**Tratamiento:** Un tratamiento corresponde a los niveles de un factor o a una combinación de los niveles de dos o más factores en estudio y cuyo efecto se mide y compara con los de otros tratamientos.

**Unidad experimental:** Es la unidad a la cual se le aplica un tratamiento y en la cual se mide el efecto de un tratamiento.

---

## Slide 6 — Conceptos Fundamentales III: Variable Respuesta y Error

**Variable respuesta:** Es la variable en la cual se evaluarán los efectos de los tratamientos.

**Error experimental:** Es la variabilidad existente entre los resultados de unidades experimentales tratadas en forma similar. Cualquier factor no controlable contribuye al error experimental. El error experimental proviene de dos fuentes principales: variabilidad inherente al material experimental y variabilidad resultante de cualquier falta de uniformidad en la realización física del experimento.

---

## Slide 7 — Ejemplo 1: Efectividad de Antibióticos

Un experimento en el que se examina la efectividad de varios antibióticos en animales de laboratorio.

| Concepto | Valor |
|----------|-------|
| Variable de entrada | dosis (cantidad de antibiótico) |
| Factor | Antibióticos |
| Tratamientos | distintos tipos de antibióticos |
| Variable de salida | efectividad (midiendo el tiempo de recuperación) |
| Unidad experimental | animalitos |

---

## Slide 8 — Ejemplo 2: Métodos de Enseñanza

Se plantea un experimento con la finalidad de comparar tres métodos de enseñanza. Cada uno se aplica en un salón con 30 estudiantes.

| Concepto | Valor |
|----------|-------|
| Variable de entrada | Tiempo de aplicación de la metodología |
| Factor | Métodos de enseñanza |
| Tratamientos | cada tipo de enseñanza |
| Variable de salida | notas al finalizar la aplicación de metodologías |
| Unidad experimental | los 90 estudiantes |

---

## Slide 9 — Ejemplo Práctico: Comparación de Metodologías de Enseñanza

Supongamos que se desea determinar que metodología de enseñanza genera mejores resultados en los alumnos:

1) ABP → T1
2) Aprendizaje cooperativo → T2
3) Aula invertida → T3

Para medir el aprendizaje, como ya es conocido, se tomarán evaluaciones similares y se cuantifica el nivel de aprendizaje mediante las notas numéricas.

Sean $\mu_1, \mu_2, \mu_3, \ldots \mu_i$ las notas promedios de los estudiantes, con cada uno de los métodos.

---

## Slide 10 — Hipótesis en ANOVA

El objetivo inicial es comparar estas notas promedios. Por ello primero se debe plantear las hipótesis siguientes:

$$H_0: \mu_1 = \mu_2 = \mu_3$$

$$H_a: \text{algún } \mu_i \text{ es distinto de los otros}$$

Una forma de probar lo anterior sería realizar las pruebas de hipótesis por pares. Supongamos que usamos $\alpha = 5\%$

Pero aquí el nivel de confianza será menor que el que uno se plantea.

---

## Slide 11 — Notación en Diseño de Experimentos

| Notación | Definición |
|----------|-----------|
| $y_{ij}$ | dato j-ésimo del Tratamiento i |
| $y_i$ | suma de los datos del Tratamiento i |
| $\bar{y}_i$ | media estimada del Tratamiento i |
| $y$ | suma total de todos los datos originales |
| $\bar{y}$ | media total estimada |
| $k$ | cantidad de tratamientos |
| $N$ | cantidad total de datos |
| $\hat{\tau}_i$ | efecto estimado del tratamiento i: $\hat{\tau}_i = \bar{y}_i - \bar{y}$ |

---

## Slide 12 — Estructura de Datos en Diseño de Experimentos

| Tratamientos | T1 | T2 | $\cdots$ | T$k$ |
|---|---|---|---|---|
| | $y_{11}$ | $y_{21}$ | $\cdots$ | $y_{k1}$ |
| | $y_{12}$ | $y_{22}$ | $\cdots$ | $y_{k2}$ |
| | $\vdots$ | $\vdots$ | | $\vdots$ |
| | $y_{1n_1}$ | $y_{2n_2}$ | $\cdots$ | $y_{kn_k}$ |
| Totales | $y_1$ | $y_2$ | $\cdots$ | $y_k$ |

---

## Slide 13 — Datos del Ejemplo: Métodos de Aprendizaje

**FACTOR: MÉTODOS DE APRENDIZAJE**

Se va a comparar la efectividad de tres métodos de aprendizaje:

1) T1: ABP
2) T2: Aprendizaje cooperativo
3) T3: Aula invertida

Para medir el aprendizaje, como ya es conocido, se tomaron evaluaciones similares a 4 alumnos de cada tipo de aprendizaje y se cuantifica el nivel de aprendizaje mediante las notas.

| T1 | T2 | T3 |
|----|----|----|
| 15 | 17 | 15 |
| 12 | 18 | 8  |
| 18 | 17 | 16 |
| 15 | 12 | 17 |

$y_1$ | $y_2$ | $y_3$ |

---

## Slide 14 — Análisis de Variaciones

El objetivo inicial es comparar estas notas promedias. Por ello primero se debe plantear las hipótesis siguientes:

$$H_0: \mu_1 = \mu_2 = \mu_3$$

$$H_a: \text{algún } \mu_i \text{ es distinto de los otros}$$

Una forma de probar lo anterior sería realizar las pruebas de hipótesis por pares. Supongamos que usamos $\alpha = 5\%$.

Para hacer esta prueba, se debe analizar las variaciones que se presentan en los datos.

**Decisiones:**
- Si al hacer la prueba de hipótesis se obtiene que se debe aceptar $H_0$ → FIN: todas las medias son iguales.
- Si al haber la prueba, se obtienen que $H_a$ es verdadero → Se debe determinar cuál de los promedios es el diferente.

---

## Slide 15 — Descomposición de la Suma de Cuadrados Total (parte 1)

$$\text{SCT} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y})^2 \quad \text{(Suma de cuadrados total)}$$

Desarrollamos algebraicamente:

$$\text{SCT} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i + \bar{y}_i - \bar{y})^2$$

$$\text{SCT} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} [(y_{ij} - \bar{y}_i)^2 + (\bar{y}_i - \bar{y})^2 + 2(y_{ij} - \bar{y}_i)(\bar{y}_i - \bar{y})]$$

---

## Slide 16 — Descomposición de la Suma de Cuadrados Total (parte 2)

Separando los tres términos:

$$\text{SCT} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2 + \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\bar{y}_i - \bar{y})^2 + 2\sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)(\bar{y}_i - \bar{y})$$

En el tercer término:

$$2\sum_{i=1}^{k} (\bar{y}_i - \bar{y}) \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i) = 2\sum_{i=1}^{k} (\bar{y}_i - \bar{y})(0) = 0$$

Porque $\sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i) = 0$ para cada $i$.

---

## Slide 17 — Descomposición Final: Identidad de ANOVA

$$\text{SCT} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (y_{ij} - \bar{y}_i)^2 + \sum_{i=1}^{k} \sum_{j=1}^{n_i} (\bar{y}_i - \bar{y})^2$$

$$\boxed{\text{SCT} = \text{SCE} + \text{SCTr}}$$

Donde:
- **SCT**: suma de cuadrados total
- **SCE**: suma de cuadrados del error
- **SCTr**: Suma de cuadrados de tratamientos

---

## Slide 18 — Tabla de ANOVA

| Fuente | Grados de Libertad | Suma de Cuadrados | Cuadrado Medio | Estadístico de Prueba | P-valor |
|--------|-------------------|-------------------|----------------|----------------------|---------|
| Tratamientos | $k-1$ | SCTr | CMTr | $F_0$ | P valor |
| Error | $N-k$ | SCE | CME | | |
| TOTAL | $N-1$ | SCT | | | |

Donde:
- $k$ = # de tratamientos
- $n_i$ = # de datos en cada tratamiento i
- $N$ = # total de datos → $N = n \cdot k$ (cuando todos tienen igual n)

---

## Slide 19 — Fórmulas de Suma de Cuadrados

$$\text{SCTr} = \sum_{i=1}^{k} \sum_{j=1}^{n} (\bar{y}_i - \bar{y})^2$$

$$\text{SCE} = \sum_{i=1}^{k} \sum_{j=1}^{n} (y_{ij} - \bar{y}_i)^2$$

$$\text{SCT} = \sum_{i=1}^{k} \sum_{j=1}^{n} (y_{ij} - \bar{y})^2$$

**Cuadrados Medios:**

- $\text{CMTr} = \frac{\text{SCTr}}{k-1}$
- $\text{CME} = \frac{\text{SCE}}{N-k}$
- Estadístico de prueba: $F_0 = \frac{\text{CMTr}}{\text{CME}}$ (distribuye como $F_{k-1, N-k}$)

---

## Slide 20 — Intervalos de Confianza en ANOVA

**Para una sola media (media de un tratamiento):**

$$\mu_i \in \left\langle \bar{y}_i \pm t_{(1-\alpha/2, N-K)} \cdot \sqrt{\frac{\text{CME}}{n_i}} \right\rangle$$

**Para 2 medias (para comparar 2 medias):**

Si todos los tratamientos tienen igual cantidad de datos:
$$\mu_i - \mu_j \in \left\langle \bar{y}_i - \bar{y}_j \pm t_{(1-\alpha/2, N-K)} \cdot \sqrt{2 \cdot \frac{\text{CME}}{n}} \right\rangle$$

Si no todos los tratamientos tienen igual cantidad de datos:
$$\mu_i - \mu_j \in \left\langle \bar{y}_i - \bar{y}_j \pm t_{(1-\alpha/2, N-K)} \cdot \sqrt{\text{CME} \left(\frac{1}{n_i} + \frac{1}{n_j}\right)} \right\rangle$$

---

# S10 — Diseño de Experimentos (Slides 21-23)

## Slide 21

[Página en blanco]

---

## Slide 22

[Página en blanco]

---

## Slide 23 — Niveles de Complejidad Analítica

### Texto introductorio

La complejidad analítica presenta una relación directa entre valor y la dificultad de los procesos de análisis.

---

### Gráfico: Relación Complejidad vs Valor

**Figura:** Gráfico de barras 3D con eje X "Complejidad" y eje Y "Valor para la organización". Cuatro categorías de altura creciente:
- Analítica descriptiva (teal, más baja)
- Analítica diagnóstica (amarillo)
- Analítica prescriptiva (rosa/magenta)
- Analítica predictiva (naranja, más alta)

Línea diagonal ascendente etiquetada "Optimización" que atraviesa las barras, indicando crecimiento en complejidad.

---

## Analítica Descriptiva

### Pregunta central
¿Qué ha pasado?

### Definición y alcance

¿Qué pasó? El primer nivel de complejidad permite responder a la pregunta sobre lo que ha ocurrido en determinado fenómeno bajo análisis. Las técnicas de estadística descriptiva nos permiten analizar una gran variedad de datos históricos (estructurados y no estructurados) y con diferentes métodos estadísticos podemos organizar estos datos y obtener información sobre lo que sucede.

### Figura asociada

Gráfico de distribuciones de probabilidad con múltiples curvas suavizadas en colores (azul, rojo/rosa, verde) solapadas, mostrando diferentes distribuciones sobre un eje de datos.

---

## Analítica de Diagnóstico

### Pregunta central
¿Por qué ha pasado?

### Definición y alcance

¿Por qué sucedió? El segundo nivel de complejidad analítica nos permite responder a la pregunta ¿por qué sucedió un determinado fenómeno. En este nivel de complejidad encontramos las técnicas de inferencia estadística, que mediante la construcción de modelos nos permite estudiar la relación y comparación de variables para obtener conclusiones útiles.

### Figura asociada

Gráfico circular con etiquetas:
- Sección etiquetada con $px$ y $0$
- Sección etiquetada con $y = y0$ y $y0 = py$
- Sección con $0$
- Múltiples regiones en colores (azul, rojo, amarillo, verde) representando componentes multivariados

---

## Analítica Prescriptiva

### Pregunta central
¿Qué debo hacer para que ocurra?

### Definición y alcance

¿Qué hacer para que ocurra? El cuarto nivel de complejidad es la analítica prescriptiva, donde mediante diferentes técnicas estadísticas es posible "prescribir" el comportamiento futuro de determinadas variables, mediante la simulación de escenarios y estimación de probabilidades de ocurrencia, cuantificando así el efecto de las decisiones futuras. Estos métodos estadísticos, en combinación con la programación computacional, dan origen al machine learning, que mediante la iteración de estas operaciones logra ajustar los modelos para automatizar los procesos de toma de decisiones.

### Figura asociada

[No visible en esta presentación de la slide 23. Se menciona en el orden jerárquico como nivel 4]

---

## Analítica Predictiva

### Pregunta central
¿Qué va a pasar?

### Definición y alcance

¿Qué pasará? El tercer nivel de complejidad corresponde a la analítica predictiva, que mediante la aplicación de algoritmos matemáticos y estadísticos a datos históricos, nos permitirá identificar patrones, detectar tendencias y realizar pronósticos para orientar el comportamiento de fenómenos futuros. Dentro de estas técnicas encontramos los modelos de regresión, modelos lineales generalizados y series de tiempo.

### Figura asociada

Gráfico de serie temporal con línea en color teal/verde mostrando tendencia ascendente con volatilidad, representando pronósticos y proyecciones futuras. El eje horizontal representa tiempo y el vertical, valores de la variable de interés.

---

## Orden jerárquico de los niveles

Según el diagrama y el flujo presentado:

1. **Analítica Descriptiva** (nivel base) → Responde ¿Qué ha pasado?
2. **Analítica de Diagnóstico** (nivel 2) → Responde ¿Por qué ha pasado?
3. **Analítica Predictiva** (nivel 3) → Responde ¿Qué va a pasar?
4. **Analítica Prescriptiva** (nivel avanzado) → Responde ¿Qué debo hacer para que ocurra?

La progresión muestra aumento en:
- Complejidad computacional y analítica
- Valor generado para la organización
- Sofisticación de técnicas estadísticas y de machine learning aplicadas
