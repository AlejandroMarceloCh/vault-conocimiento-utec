---
curso: EST
titulo: S05- Estadística y Probabilidades 2 _ Distribuciones muestrales
slides: 27
fuente: S05- Estadística y Probabilidades 2 _ Distribuciones muestrales.pdf
---

# S05- Estadística y Probabilidades 2 _ Distribuciones muestrales

## Índice

Capítulo de Estadística y Probabilidades 2. Contenido transcrito de las diapositivas (fórmulas en LaTeX, figuras descritas).

# S05 — Distribuciones muestrales

## Slide 1 — Portada

**Tema:** Distribuciones muestrales

**Curso:** Estadística y probabilidades II

**Código:** S05

**Institución:** UTEC (Universidad de Ingeniería y Tecnología)

**Figura:** Portada con título en rojo sobre fondo azul, logo de UTEC en esquina inferior izquierda, imagen arquitectónica de fondo (edificio moderno de concreto gris).

---

## Slide 2 — Distribuciones muestrales (Concepto introductorio)

**Título:** Distribuciones muestrales

Cuando se trata de sacar una muestra de tamaño $n$, de una población de tamaño $N$, se tendrá varias posibilidades para elegir a los elementos muestreados, obteniéndose así muestras del mismo tamaño $n$, pero con elementos que pueden diferir, aunque sea en alguno de ellos.

Visto así, si tratamos de calcular, por ejemplo, la media de la muestra se va a tener que esta media tendrá valores distintos, comportándose entonces como una nueva variable que será aleatoria porque las muestras también son aleatorias.

Esto implica que se puede obtener probabilidades para la media de la muestra. A este conjunto de probabilidades, de todas las posibles muestras, se le conoce como distribución muestral para la media.

**En esta unidad veremos:**
- Distribución muestral de la media muestral
- Distribución muestral de la varianza muestral
- Distribución muestral de la proporción muestral
- Distribución muestral para la diferencia de medias muestrales
- Distribución muestral para la razón de varianzas muestrales
- Distribución muestral para la diferencia de proporciones

---

## Slide 3 — Parámetros y Estimadores

**Parámetros y Estimadores**

El objetivo fundamental en Estadística Inferencial es **inferir parámetros** (valores poblacionales) a partir de **estimadores** (muestrales).

**Parámetros:**
Valores de resumen de una población. Generalmente se obtiene a partir de un censo.

**Estimadores:**
Valores de resumen de una muestra. Generalmente se obtienen mediante una encuesta.

El principal papel de los estimadores es obtener valores que se aproximen a sus respectivos parámetros. Esta aproximación será buena siempre y cuando la muestra esté bien seleccionada que cumpla con la representatividad y la aleatoriedad.

En general siempre se va a generar un error de estimación:

$$\text{Error de estimación} = \text{Estimador} - \text{Parámetro}$$

---

## Slide 4 — Principales parámetros y sus estimadores

**PRINCIPALES PARAMETROS Y SUS ESTIMADORES:**

| PARÁMETROS | ESTIMADORES PUNTUALES |
|---|---|
| $\mu$ — media poblacional | $\bar{x}$ — media muestral | $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$ |
| $\sigma^2$ — varianza poblacional | $s^2$ — varianza muestral | $s^2 = \frac{\sum_{i=1}^{n} x_i^2 - n\bar{x}^2}{n-1}$ |
| $\sigma$ — desviación poblacional | $s$ — desviación muestral | $s = \sqrt{s^2}$ |
| $\pi$ — proporción poblacional | $p$ — proporción muestral | $p = \frac{x}{n} = \frac{\text{# de éxitos en la muestra}}{\text{Tamaño de muestra}}$ |

**Tamaño de población:** $N$

**Tamaño de muestra:** $n$

---

## Slide 5 — Ejemplo: Empresa con 3 trabajadores

**Ejemplo:**

En una empresa hay 3 trabajadores cuyos salarios son: 1800, 2000, 2400.
Se seleccionará 2 trabajadores con reposición y se calcula su promedio muestral.

**1) Calcular $\mu$:**

$$\mu = \frac{1800 + 2000 + 2400}{3} = 2066.67 \text{ (promedio verdadero de la población)}$$

**2) ¿Cuántas muestras de tamaño 2, con reposición se puede obtener?**

Se pueden obtener $3^2 = 9$ muestras.

**3) Formar todas las posibles muestras y halle el promedio para cada caso:**

| Muestras con reposición | Promedio muestral: $\bar{X}$ |
|---|---|
| 1800, 1800 | 1800 |
| 1800, 2000 | 1900 |
| 1800, 2400 | 2100 |
| 2000, 1800 | 1900 |
| 2000, 2000 | 2000 |
| 2000, 2400 | 2200 |
| 2400, 1800 | 2100 |
| 2400, 2000 | 2200 |
| 2400, 2400 | 2400 |

**4) Formar la tabla de probabilidades del promedio muestral:**

| $\bar{X}$ | 1800 | 1900 | 2000 | 2100 | 2200 | 2400 |
|---|---|---|---|---|---|---|
| $P(\bar{X})$ | $1/9$ | $2/9$ | $1/9$ | $2/9$ | $2/9$ | $1/9$ |

$$E(\bar{X}) = 1800 \cdot \frac{1}{9} + 1900 \cdot \frac{2}{9} + 2000 \cdot \frac{1}{9} + 2100 \cdot \frac{2}{9} + 2200 \cdot \frac{2}{9} + 2400 \cdot \frac{1}{9}$$

$$E(\bar{X}) = 2066.67$$

---

## Slide 6 — Distribución de la media muestral: Expectativa y varianza

**Distribución de la media muestral:**

Si se toma todas las muestras posibles de tamaño $n$, se obtendría distintos valores de $\bar{x}$, y de ahí se calcula su valor esperado, obteniéndose que será igual a la media poblacional.

$$E(\bar{x}) = \mu$$

Donde:
- $\bar{x}$ ⟹ media muestral (valor aproximado)
- $\mu$ ⟹ media poblacional (valor verdadero)

Su varianza tiene dos posibilidades, que depende del tamaño de la población.

**Si la población es finita:**
$$V(\bar{x}) = \frac{\sigma^2}{n} \cdot \frac{N-n}{N-1} \Rightarrow \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} \cdot \sqrt{\frac{N-n}{N-1}}$$

**(Esto no lo evaluamos)**

**Si la población es infinita o la muestra es menos del 5% de la población:**
$$V(\bar{x}) = \frac{\sigma^2}{n} \Rightarrow \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$

Donde:
- $\sigma^2$ — varianza poblacional (verdadero)
- $s^2$ — varianza muestral (aproximado)
- $V(\bar{X})$ — varianza de la media muestral

---

## Slide 7 — LA MEDIA MUESTRAL

**LA MEDIA MUESTRAL:**

$$\bar{x} = \frac{\sum x_i}{n} \text{ → tamaño de muestra}$$

**Media de la media muestral:**
$$\mu_{\bar{x}} = \mu \text{ → media poblacional}$$

**Desviación de la media muestral:**
$$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} \text{ → desviación de población}$$

**Además se denomina:** Error estándar de la media muestral

---

## Slide 8 — Distribución de la media muestral: Tres casos principales

**Distribución de la media muestral:**

$$\bar{x} = \frac{\sum x_i}{n}$$

**CASO 1:** Si la población es normal y se conoce $\sigma$, entonces $\bar{x}$ tiene distribución normal con media $\mu$ y desviación $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$

$$\bar{x} \sim N\left(\mu, \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}\right)$$

(donde tamaño de muestra es $n$)

**La normal estandarizada:**
$$Z = \frac{\bar{x} - \mu}{\sigma_{\bar{x}}}$$

Aquí $\bar{x}$ se ha estandarizado y cuando se use la normal $Z$, se debe colocar en R, media $=0$ y desviación $=1$.

**CASO 2:** Si la población no es normal, pero el tamaño de muestra es más de 30, entonces puede considerarse que $\bar{x}$ tiene distribución normal con media $\mu$ y desviación $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$ (sigma debe ser conocido)

$$\bar{x} \sim N\left(\mu; \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}\right)$$

**Teorema del límite central**

**CASO 3:** Si la población es normal, pero no se conoce $\sigma$ y el tamaño de muestra es pequeño (no pasa de 30), entonces puede considerarse que $\bar{x}$ tiene distribución $t - \text{student}$.

Así:
$$T_{(n-1)} = \frac{\bar{x} - \mu}{\frac{s}{\sqrt{n}}}$$

**$t - \text{student}$ con $n - 1$ grados de libertad.**

**$S$ — desviación muestral**

---

## Slide 9 — Ejemplo 1: Resistencia de láminas de metal

**Ejemplo 1**

El valor nominal de la resistencia de una lámina de cierto metal es de 8500 psi. Por estudios pasados se conoce que la desviación estándar de esta resistencia es 1950 psi. Si se toma una muestra de 100 láminas. ¿Cuál es la probabilidad de que la resistencia media de esa muestra:

a) ¿Esté entre 8200 y 8700 psi?
b) ¿Cuál es el valor máximo de la media muestral para tener una probabilidad de ocurrencia de 16%?

**Parámetros del problema:**
- $\mu = 8500$
- $\sigma = 1950$
- $n = 100 > 30$
- $\bar{x} \sim N(8500, 195)$ (donde $\sigma_{\bar{x}} = \frac{1950}{\sqrt{100}} = 195$)
- $\bar{x} \sim N(8500, 195)$

**Solución (con anotaciones manuscritas):**

a) $P(8200 < \bar{x} < 8700) = P(\bar{x} < 8700) - P(\bar{x} < 8200) = 0.8475 - 0.619 = 0.2285$

b) $P(\bar{x} \leq M) = 0.16$

**Código R (mostrado en la slide):**
```r
> pnorm(8700, 8500, 195)
[1] 0.8474696

> pnorm(8200, 8500, 195)
[1] 0.061679

> qnorm(0.16, 8500, 195)
[1] 8306.081
```

---

## Slide 10 — Ejemplo 2: Máquina que produce piezas

**Ejemplo 2**

Una máquina produce piezas con un tamaño que se ajusta a una distribución normal cuyo valor medio es de 14 cm.

1) ¿Cuál es la probabilidad de que la media de una muestra de tamaño 20 sea menor que 14,58 cm? sabiendo que la varianza muestral ha sido de 9 cm².

2) ¿Cuál es la probabilidad de que la media muestral difiera del promedio verdadero en a lo más 0,20 cm?

**Fórmula aplicable:**
$$T_{(n-1)} = \frac{\bar{x} - \mu}{\frac{s}{\sqrt{n}}}$$

**Código R (mostrado en la slide):**
```r
> pt(0.8646, 19)
[1] 0.8009784
```

---

## Slide 11 — Ejemplo 3: Bolsas de azúcar

**Ejemplo 3**

El contenido real de las bolsas de azúcar de 1 kg es una variable uniforme en [0.9; 1.1] kg.

1) Calcule el coeficiente de variación de los pesos reales de azúcar en bolsas de 1 kg.

2) Para hacer una inspección, se selecciona 100 bolsas de 1kg
   - 2.1) ¿Cuál es la probabilidad de que el peso promedio de estas bolsas exceda a 1,05 kg?
   - 2.2) ¿Cuál es la probabilidad de que el total de azúcar seleccionada no exceda a 96 kg?

3) ¿cuántas bolsas de azúcar de 1 kg se debe seleccionar para la inspección y así tener un peso promedio muestral mínimo de 1,01 kg en un 10% de las bolsas seleccionadas?

---

## Slide 12 — Distribución de la varianza muestral y proporción muestral

**Distribución de la varianza muestral**

$$\frac{(n-1) \cdot s^2}{\sigma^2} = \chi^2_{(n-1)}$$

Donde:
- $s^2$ — varianza muestral
- $\sigma^2$ — varianza poblacional

---

**Distribución de la proporción muestral**

$$p \sim N(\mu_p, \sigma_p)$$

Siendo:
$$\mu_p = \pi$$

$$\sigma_p = \sqrt{\frac{\pi(1-\pi)}{n}}$$

Donde:
- $\pi$ — proporción poblacional

---

## Slide 13 — Ejemplo 4: Notas de estadística

**Ejemplo 4**

En el curso de Estadística, se conoce de ciclos anteriores que las notas se distribuyen normalmente con media 13.5 y varianza 16. Para verificar como están en este ciclo, se seleccionan 25 notas

a) ¿cuál es la probabilidad de que la desviación muestral sea a lo más 4?
b) Calcule la varianza muestral máxima con probabilidad 0.80

**Código R (mostrado en la slide):**
```r
{r}
pchisq(24, 24)

[1] 0.5384027
```

---

## Slide 14 — Ejemplo 5: Alumnos aprobados

**Ejemplo 5**

De 120 alumnos se ha encontrado que 100 han aprobado el curso. Se seleccionará una muestra de tamaño 20 alumnos.

a) ¿Cuál es la probabilidad de que el porcentaje de aprobados en la muestra sea por lo menos del 75%?

b) Calcule la probabilidad de que, en los alumnos muestreados, se tenga a lo más 3 desaprobados.

---

## Slide 15 — Distribución de la diferencia de proporciones y razón de varianzas

**Distribución de la diferencia de proporciones muestrales**

Consideremos que se tiene dos muestras de tamaños $n_1$ y $n_2$, además se conocen las respectivas proporciones poblacionales $\pi_1$ y $\pi_2$.

$$p_1 - p_2 \sim N\left(\pi_1 - \pi_2, \sqrt{\frac{\pi_1(1-\pi_1)}{n_1} + \frac{\pi_2(1-\pi_2)}{n_2}}\right)$$

---

**Distribución de la razón de varianzas**

Consideremos que se tiene dos muestras de tamaños $n_1$ y $n_2$ que provienen de dos poblacionales normales $X_1$ y $X_2$ con varianzas poblacionales $\sigma_1^2$ y $\sigma_2^2$

$$\frac{s_1^2}{s_2^2} \cdot \frac{\sigma_2^2}{\sigma_1^2} \sim F_{(n_1-1, n_2-1)}$$

---

## Slide 16 — Ejemplo 6: Comparación de ventas Toyota vs Nissan

**Ejemplo 6**

Se desea comparar las ventas de autos en un mes, entre las marcas Toyota y Nissan. En el mes de Febrero, los de Toyota vendieron de sus 80 autos que disponían, la cantidad de 64 vehículos, mientras que en Nissan de los 90 que tenían disponible en dicho mes, se vendió 54.

¿cuál es la probabilidad de que, al tomar de sus respectivas bases de datos, muestras de 40 y 30 vehículos respectivamente, se obtenga que el porcentaje de autos que fueron vendidos de Toyota supere al de Nissan en al menos un 5%?

---

## Slide 17 — Ejemplo 7: Duraciones de focos

**Ejemplo 7**

En dos empresas A y B, que producen focos, las duraciones respectivas tienen desviaciones estándar de 40h y 50h. Se selecciona una muestra de 8 focos de A y 16 de B, ¿cuál es la probabilidad de que la varianza de la primera muestra supere a la varianza muestral de la segunda en un 20% de su valor, por lo menos? Considere que las distribuciones de las duraciones son normales.

---

## Slide 18 — Distribución de la diferencia de medias muestrales (Caso 1: Varianzas conocidas)

**Distribución de la diferencia de medias muestrales**

Se considera aquí dos muestras de tamaños $n_1$ y $n_2$.
Las variables poblacionales $X_1$ y $X_2$ respectivas, de ambas muestras se consideran como normales:

$$X_1 \sim N(\mu_1, \sigma_1)$$
$$X_2 \sim N(\mu_2, \sigma_2)$$

Según se conozca o no, las varianzas de la población, se obtendrá los casos:

**Caso 1: Si las varianzas de la población son conocidas.**

Aquí la distribución de la diferencia de medias muestrales $\bar{x}_1 - \bar{x}_2$ origina una distribución normal:

$$\bar{x}_1 - \bar{x}_2 \sim N\left(\mu_1 - \mu_2, \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}\right)$$

**Su forma estandarizada será:**

Si se conoce $\sigma_1$ y $\sigma_2$

$$\Rightarrow \frac{\bar{X}_1 - \bar{X}_2 - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} = z$$

---

## Slide 19 — Distribución de la diferencia de medias muestrales (Caso 2: Varianzas desconocidas e iguales)

**Distribución de la diferencia de medias muestrales**

Continuando con las dos muestras de tamaños $n_1$ y $n_2$.
Las variables poblacionales $X_1$ y $X_2$ respectivas, de ambas muestras se consideran como normales:

$$X_1 \sim N(\mu_1, \sigma_1)$$
$$X_2 \sim N(\mu_2, \sigma_2)$$

**Caso 2: Si las varianzas de la población son desconocidas pero iguales.**

Aquí la distribución de la diferencia de medias muestrales $\bar{x}_1 - \bar{x}_2$ origina una distribución $t - \text{student}$.

**Si no se conoce $\sigma_1$ y $\sigma_2$ pero se sabe que son iguales**

$$\frac{\bar{x}_1 - \bar{x}_2 - (\mu_1 - \mu_2)}{\sqrt{S_p^2 \left(\frac{1}{n_1} + \frac{1}{n_2}\right)}} = T_{(n_1 + n_2 - 2)}$$

**Siendo**

$$S_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}$$

---

## Slide 20 — Distribución de la diferencia de medias muestrales (Caso 2: Varianzas desconocidas y diferentes)

**Distribución de la diferencia de medias muestrales**

Continuando con las dos muestras de tamaños $n_1$ y $n_2$.
Las variables poblacionales $X_1$ y $X_2$ respectivas, de ambas muestras se consideran como normales:

$$X_1 \sim N(\mu_1, \sigma_1)$$
$$X_2 \sim N(\mu_2, \sigma_2)$$

**Caso 2: Si las varianzas de la población son desconocidas pero diferentes.**

Aquí la distribución de la diferencia de medias muestrales $\bar{x}_1 - \bar{x}_2$ origina también una distribución $t - \text{student}$.

**Si no se conoce $\sigma_1$ y $\sigma_2$ pero se sabe que son diferentes**

$$T(v) = \frac{\bar{X}_1 - \bar{X}_2 - (\mu_1 - \mu_2)}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

**Siendo**

$$v = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{\left(\frac{s_1^2}{n_1}\right)^2}{n_1-1} + \frac{\left(\frac{s_2^2}{n_2}\right)^2}{n_2-1}} = \text{grados de libertad}$$

---

# S05: Estadística y Probabilidades 2 — Distribuciones Muestrales (Slides 21–27)

## Slide 21 — Ejemplo 8: Comparación de salarios entre géneros

Se tiene la siguiente información de una determinada empresa:

- Salario medio de hombres = 3000 soles, $\sigma^2 = 40000$
- Salario medio de mujeres = 3200 soles, $\sigma^2 = 90000$

Si tomamos una muestra aleatoria de 36 hombres y 49 mujeres, ¿cuál es la probabilidad de que el salario medio de los hombres sea al menos 300 soles mayor al de las mujeres?

Considerar que los salarios se distribuyen normalmente.

---

## Slide 22 — Ejemplo 9: Investigación de calidad del aire

Se realizará una investigación sobre la calidad del aire en Av. Abancay y Wilson. Un indicador de la calidad es el número de partículas en suspensión por $m^3$ de aire, que se asume siguen distribuciones Normales independientes de media 62.037 unidades en Av. Abancay y 61.022 unidades en Av. Wilson.

En la primera Avenida se realizan 12 mediciones, obteniéndose una varianza de 8.44 y en la segunda 15 mediciones, con una varianza de 9.44. 

Calcule la probabilidad de que la media muestral de Av. Abancay sea como mínimo tres unidades mayores a la media muestral de Av. Wilson. 

Considere además que, dado la cercanía de los lugares de estudio, se asume que las varianzas son iguales.

---

## Slide 23 — Ejemplo 10: Comparación de métodos de estudio

Un equipo de docentes está investigando si existen o no diferencias entre dos métodos de estudio cuyo objetivo es reducir la ansiedad generada en la temporada de exámenes. Para lo cual se seleccionan dos muestras de tamaño 10 cada una, a las que se les aplicó el método X e Y respectivamente. 

Obteniéndose que las varianzas muestrales son de 3.7 y 4.2 puntos respectivamente. 

Suponiendo que las puntuaciones de ansiedad de ambas poblaciones siguen distribuciones muestrales con medias poblacionales de 90 y 87.3 puntos respectivamente y que las varianzas poblacionales son diferentes debido a que los métodos usan procedimientos totalmente distintos. 

Hallar la probabilidad de que las medias muestrales con ambos métodos se diferencien en a lo más 6 unidades.

---

## Slide 24 — PROYECTO P1: Parte 1 — "CONSIDERANDO LA BASE DE DATOS COMO UNA POBLACIÓN"

Dado que la base contiene una gran cantidad de datos entonces se puede asumir que es una población, por lo tanto, cualquier cálculo produce alguno de los siguientes, a partir de una columna numérica:

- **Media poblacional:** $\mu$
- **Desviación poblacional:** $\sigma$
- **Varianza poblacional:** $\sigma^2$
- **Proporción poblacional:** $\pi$ (para columna cualitativa)

El alumno deberá crear **3 CASOS** (problemas de: una media $\bar{X}$, una proporción, una varianza $s^2$, etc)

Cada caso es como un problema donde se pide calcular alguna probabilidad.

Cada grupo calculará el tamaño de muestra que usará, según lo visto en clase y con ello hace los cálculos.

---

## Slide 25 — [Divisor — Estadística y probabilidades]

**Figura:** Recuadro gris vacío con marco azul superior, usado como transición visual en el material del curso.

---

## Slide 26 — [Divisor — Estadística y probabilidades]

**Figura:** Recuadro gris vacío con marco azul superior, usado como transición visual en el material del curso.

---

## Slide 27 — Algo de R: Generación de muestras y cálculo de medias

Supongamos que un curso de Estadística tiene 5 alumnos cuyas notas son:

$$\text{Notas} = \{15, 12, 17, 12, 16\}$$

### 1) Seleccionemos todas las muestras de tamaño 2

- **Sacar una sola muestra con r:**
$$\text{sample}(\text{base}, \text{tamaño muestral}, F \text{ (sin remplazo)})$$

- **Sacar todas las muestras sin reposición:**
$$\text{Combn}(\text{base}, \text{tamaño})$$

- **Sacar todas las muestras con reposición de tamaño 3 (como ejemplo)**
$$\text{expand.grid}(\text{base}, \text{base}, \text{base})$$

### 2) Convertir la matriz de muestras a un data frame simple

$$\text{nombre del tibble} \gets \text{as\_tibble}(\text{matriz})$$

- Si se desea previamente trasponer a una matriz, basta con usar la función
$$t(\text{matriz})$$

### 3) Para hallar las medias muestrales por columnas, del tibble

```r
vectorsalida[[i]] <- estadístico(tibble[[i]])
# 3. cuerpo for (i in seq_along(tibble)) {
# 2. secuencia vectorsalida <- vector("double", ncol(tibble))
# 1. output
```
