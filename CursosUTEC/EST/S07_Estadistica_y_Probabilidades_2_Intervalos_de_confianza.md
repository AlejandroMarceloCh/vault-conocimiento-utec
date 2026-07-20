---
curso: EST
titulo: S07- Estadística y Probabilidades  2_Intervalos de confianza
slides: 23
fuente: S07- Estadística y Probabilidades  2_Intervalos de confianza.pdf
---

# S07- Estadística y Probabilidades  2_Intervalos de confianza

## Índice

Capítulo de Estadística y Probabilidades 2. Contenido transcrito de las diapositivas (fórmulas en LaTeX, figuras descritas).

# S07: Estadística y Probabilidades 2 — Intervalos de confianza

## Slide 1 — Portada: Unidad 5 - Estimación puntual y por intervalos

**Estadística y probabilidades II**

**Unidad 5:**
**Estimación puntual y por intervalos**

S06, S07

UTEC — Universidad de Ingeniería y Tecnología

**Figura:** Portada con fondo gris, logo UTEC en esquina inferior izquierda, imagen de edificio de concreto moderno en ángulo a la derecha, decoración azul cian en esquina superior derecha.

---

## Slide 2 — Estimadores puntuales

**Estimadores puntuales**

Sabemos que los parámetros son valores específicos que resumen la información de una población.

En cambio los estimadores puntuales son expresiones que permiten resumir la información de una muestra, pero que tienen como objetivo aproximarse a algún parámetro.

**Ejemplo:**

- $\mu$ es un parámetro que representa a la media poblacional.
- $\bar{x}$ es un estimador puntual que representa a la media muestral.
- $\bar{x}$ es un estimador de $\mu$.

- $\pi$ es la proporción poblacional.
- $p$ es un estimador puntual que representa a la proporción muestral.
- $p$ es un estimador de $\pi$.

- $\sigma$ es la desviación poblacional.
- $s$ es un estimador puntual que representa a la desviación muestral.
- $s$ es un estimador de $\sigma$.

---

## Slide 3 — Parámetros y Estimadores

**Parámetros y Estimadores**

**PRINCIPALES PARAMETROS Y SUS ESTIMADORES:**

| PARÁMETROS | ESTIMADORES PUNTUALES |
|---|---|
| $\mu$ → media poblacional | $\bar{x}$ → media muestral | $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$ |
| $\sigma^2$ → varianza poblacional | $s^2$ → varianza muestral | $s^2 = \frac{\sum_{i=1}^{n} x_i^2 - n\bar{x}^2}{n-1}$ |
| $\sigma$ → desviación poblacional | $s$ → desviación muestral | $s = \sqrt{s^2}$ |
| $\pi$ → proporción poblacional | $p$ → proporción muestral | $p = \frac{x}{n} = \frac{\text{# de éxitos en la muestra}}{\text{Tamaño de muestra}}$ |

Tamaño de población: $N$
Tamaño de muestra: $n$

---

## Slide 4 — Intervalos de confianza de la media (Caso 1: σ conocida)

**Intervalos de confianza de la media**

El objetivo es hallar un intervalo que contenga al parámetro $\mu$, pero con un nivel de confianza dado por una probabilidad $\gamma$, de que ello ocurra.

Se obtiene aquí dos casos:

**CASO 1: Si se conoce $\sigma$** entonces el intervalo de confianza para $\mu$, usa una distribución normal

$$IC: \bar{X} - Z_{1-\frac{\alpha}{2}} \cdot \frac{\sigma}{\sqrt{n}} < \mu < \bar{X} + Z_{1-\frac{\alpha}{2}} \cdot \frac{\sigma}{\sqrt{n}}$$

Aquí:
- $\bar{X}$ es la media muestral.
- $n$ es tamaño de muestra.
- $\sigma$ es la desviación de población.
- $\alpha + \gamma = 1$ , siendo $\alpha$ el nivel de significación y $\gamma$ el nivel de confianza.
- $Z_{1-\frac{\alpha}{2}} = z_o$ tal que: $P(Z \leq z_o) = 1 - \frac{\alpha}{2}$

**Figura:** Distribución normal estándar con área central sombreada en azul, etiquetada "% Nivel de confianza". Colas señaladas como $\frac{\alpha}{2}$ a izquierda y derecha, con valores $-z_{\alpha/2}$ y $z_{\alpha/2}$ en eje x.

---

## Slide 5 — Intervalos de confianza de la media (Caso 2: σ desconocida)

**Intervalos de confianza de la media**

**CASO 2: Si no se conoce $\sigma$, pero en cambio se conoce $s$ la desviación de la muestra,** entonces el intervalo de confianza para $\mu$, usa una distribución t - student

$$IC: \bar{X} - t_{1-\frac{\alpha}{2}} \cdot \frac{s}{\sqrt{n}} < \mu < \bar{X} + t_{1-\frac{\alpha}{2}} \cdot \frac{s}{\sqrt{n}}$$

Aquí:
- $\bar{X}$ es la media muestral.
- $n$ es tamaño de muestra.
- $S$ es la desviación de población.
- $\alpha + \gamma = 1$ , siendo $\alpha$ el nivel de significación y $\gamma$ el nivel de confianza.
- $t_{1-\frac{\alpha}{2}} = t_o$ tal que: $P(T(n-1) \leq t_o) = 1 - \frac{\alpha}{2}$

---

## Slide 6 — Error muestral máximo y tamaño de muestra

**Error muestral máximo y tamaño de muestra**

El error muestral verdadero es $E = \bar{x} - \mu$

De los intervalos se deduce que:

**1)** $E = |\bar{x} - \mu| < Z_{1-\frac{\alpha}{2}} \cdot \frac{\sigma}{\sqrt{n}}$ → $E_{max} = Z_{1-\frac{\alpha}{2}} \cdot \frac{\sigma}{\sqrt{n}}$ cuando se conoce $\sigma$ 

$$n = \left(\frac{Z_{1-\frac{\alpha}{2}}}{E_{max}}\right)^2 \cdot \sigma^2$$

**2)** $E = |\bar{x} - \mu| < t_{1-\frac{\alpha}{2}} \cdot \frac{s}{\sqrt{n}}$ → $E_{max} = t_{1-\frac{\alpha}{2}} \cdot \frac{s}{\sqrt{n}}$ cuando no se conoce $\sigma$

$$n = \left(\frac{Z_{1-\frac{\alpha}{2}}}{E_{max}}\right)^2 \cdot S^2$$

**NOTA:** cuando la muestra supera a 30, se puede usar siempre la Normal.

---

## Slide 7 — Ejemplo 1: Focos

**Ejemplo 1**

Un fabricante produce focos que tienen un promedio de vida de distribución normal y una **desviación estándar de 40 horas**. Si una muestra de 30 focos tiene una vida promedio de 780 horas.

a) Encuentre el intervalo de confianza del 95% para la media de la población de todos los focos que produce la empresa.

b) ¿Cuál es el error máximo que se está cometiendo al usar un intervalo de confianza del 95%?

$$IC: \bar{X} - Z_{1-\frac{\alpha}{2}} \cdot \frac{\sigma}{\sqrt{n}} < \mu < \bar{X} + Z_{1-\frac{\alpha}{2}} \cdot \frac{\sigma}{\sqrt{n}}$$

**Figura:** Imagen de bombilla incandescente azulada en esquina superior derecha.

---

## Slide 8 — Ejemplo 2: Baterías

**Ejemplo 2**

Una compañía utiliza baterías en sus juegos electrónicos que según ellos duran un promedio de 30 horas, para confirmar esto se prueba 16 baterías siendo la media muestral de 27.5 horas y su desviación estándar $S=5$ horas.

Encuentre un intervalo de confianza del 95% para la media. Suponga que la distribución de las duración de las baterías es aproximadamente normal.

$$IC: \bar{X} - t_{1-\frac{\alpha}{2}} \cdot \frac{s}{\sqrt{n}} < \mu < \bar{X} + t_{1-\frac{\alpha}{2}} \cdot \frac{s}{\sqrt{n}}$$

**Figura:** Tres baterías stylizadas con indicadores de carga (una amarilla/naranja, dos verdes y rojas).

---

## Slide 9 — Ejemplo 3: Salarios

**Ejemplo 3**

El salario de los trabajadores en una empresa, se distribuye como Normal y de información anterior se conoce que su varianza es $57600$ $soles^2$.

Se desea realizar una encuesta a los trabajadores para obtener mayor información sobre sus salarios, con un 95% de confianza. ¿De qué tamaño debe ser la muestra para cometer un error máximo de 50 soles?

¿y para tener un error máximo de 10 soles, que tamaño de muestra debe usarse?

**Figura:** Fotografía de grupo de personas en reunión de oficina, sentados alrededor de una mesa de trabajo.

---

## Slide 10 — Intervalos de confianza de una proporción

**Intervalos de confianza de una proporción**

El objetivo es hallar un intervalo que contenga al parámetro $\pi$, pero con un nivel de confianza dado por una probabilidad $\gamma$, de que ello ocurra.

$$p - Z_{1-\frac{\alpha}{2}} \cdot \sqrt{\frac{p(1-p)}{n}} < \pi < p + Z_{1-\frac{\alpha}{2}} \cdot \sqrt{\frac{p(1-p)}{n}}$$

Aquí:
- $p$ es la proporción muestral.
- $n$ es tamaño de muestra.
- $\alpha + \gamma = 1$ , siendo $\alpha$ el nivel de significación y $\gamma$ el nivel de confianza.
- $Z_{1-\frac{\alpha}{2}} = z_o$ tal que: $P(Z \leq z_o) = 1 - \frac{\alpha}{2}$

**Figura:** Distribución normal estándar con área central sombreada en azul, etiquetada "Probabilidad estar dentro del intervalo" y "% Nivel de confianza". Colas señaladas como $\frac{\alpha}{2}$.

---

## Slide 11 — Error muestral máximo y tamaño de muestra (Proporciones)

**Error muestral máximo y tamaño de muestra**

El error muestral verdadero es $E = \bar{x} - \mu$

De los intervalos se deduce que:

$$E = |p - \pi| < Z_{1-\frac{\alpha}{2}} \cdot \sqrt{\frac{p(1-p)}{n}}$$ → $$E_{max} = Z_{1-\frac{\alpha}{2}} \cdot \sqrt{\frac{p(1-p)}{n}}$$

$$n = \left(\frac{Z_{1-\frac{\alpha}{2}}}{E_{max}}\right)^2 \cdot p(1-p)$$

---

## Slide 12 — Intervalos de confianza de la diferencia de proporciones

**Intervalos de confianza de la diferencia de proporciones**

El objetivo es hallar un intervalo que contenga a la diferencia $\pi_1 - \pi_2$, pero con un nivel de confianza dado por una probabilidad $\gamma$, de que ello ocurra.

$$p_1 - p_2 - Z_{1-\frac{\alpha}{2}} \cdot \sqrt{\frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}} < \pi_1 - \pi_2 < p_1 - p_2 + Z_{1-\frac{\alpha}{2}} \cdot \sqrt{\frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}}$$

Aquí:
- $p1, p2$ son proporciones muestrales.
- $n1, n2$ son tamaño de muestra.
- $\alpha + \gamma = 1$ , siendo $\alpha$ el nivel de significación y $\gamma$ el nivel de confianza.
- $Z_{1-\frac{\alpha}{2}} = z_o$ tal que: $P(Z \leq z_o) = 1 - \frac{\alpha}{2}$

---

## Slide 13 — Nota: Interpretación de diferencia de proporciones

**Nota:**

Si el intervalo de confianza para la diferencia de proporciones es

$$A < \pi_1 - \pi_2 < B$$

Se obtendrá 3 casos:

- $(+) < \pi_1 - \pi_2 < (+)$ → $\pi_1 > \pi_2$

- $(-) < \pi_1 - \pi_2 < (-)$ → $\pi_1 < \pi_2$

- $(-) < \pi_1 - \pi_2 < (+)$ → $\pi_1 = \pi_2$

---

## Slide 14 — Ejemplo 4: Toyota Mitsui (una proporción)

**Ejemplo 4**

En Toyota Mitsui, se está revisando como están las ventas desde el 2020. Para ello se ha tomado una muestra de 80 registros de venta y se ha encontrado que de los vehículos Corolla se han vendido 32 unidades. Con 90% de confianza, obtenga un intervalo para el porcentaje de Corollas vendidos.

---

## Slide 15 — Ejemplo 5: Toyota Mitsui (dos proporciones)

**Ejemplo 5**

En Toyota Mitsui, se está revisando como están las ventas desde el 2020. Para ello se ha tomado una muestra de 80 registros de venta y se ha encontrado que de los vehículos Corolla se han vendido 32 unidades y 28 RAVs ¿Con 98% de confianza determine un intervalo para el porcentaje de Corollas que se vende en la empresa.

---

## Slide 16 — Intervalos de confianza de varianzas (Para 1 varianza)

**Intervalos de confianza de varianzas**

**PARA 1 VARIANZA**

$$\frac{(n-1)s^2}{\chi^2_{(1-\frac{\alpha}{2},n-1)}} < \sigma^2 < \frac{(n-1)s^2}{\chi^2_{(\frac{\alpha}{2},n-1)}}$$

Aquí:
- $s^2$ es la varianza muestral.
- $n$ es tamaño de muestra.
- $\alpha + \gamma = 1$ , siendo $\alpha$ el nivel de significación y $\gamma$ el nivel de confianza.
- $\chi^2_{(1-\frac{\alpha}{2},n-1)} = Xo$ tal que: $P(\chi^2_{(n-1)} \leq X_o) = 1 - \frac{\alpha}{2}$ usar `qchi(1 - $\frac{\alpha}{2}$, n-1)`
- $\chi^2_{(\frac{\alpha}{2},n-1)} = Yo$ tal que: $P(\chi^2_{(n-1)} \leq Y_o) = \frac{\alpha}{2}$ usar `qchi($\frac{\alpha}{2}$, n-1)`

---

## Slide 17 — Intervalos de confianza de varianzas (Para 2 varianzas)

**Intervalos de confianza de varianzas**

**PARA 2 VARIANZAS**

$$\frac{s^2_1}{s^2_2} \cdot F\left(\frac{\alpha}{2}, n_2 - 1, n_1 - 1\right) < \frac{\sigma^2_1}{\sigma^2_2} < \frac{s^2_1}{s^2_2} \cdot F\left(1 - \frac{\alpha}{2}, n_2 - 1, n_1 - 1\right)$$

Si el intervalo de confianza para la razón de 2 varianzas es $A < \frac{\sigma^2_1}{\sigma^2_2} < B$

- $(\# > 1) < \frac{\sigma^2_1}{\sigma^2_2} < (\# > 1)$ → $\sigma^2_1 > \sigma^2_2$

- $(\# < 1) < \frac{\sigma^2_1}{\sigma^2_2} < (\# < 1)$ → $\sigma^2_1 < \sigma^2_2$

- $(\# < 1) < \frac{\sigma^2_1}{\sigma^2_2} < (\# > 1)$ → $\sigma^2_1 = \sigma^2_2$

---

## Slide 18 — t.test (Introducción)

**t.test**

**En R-Studio:**

La función `t.test` se usa para calcular intervalos de confianza para la media y diferencia de medias, con muestras independientes y dependientes (o pareadas). La función y sus argumentos son los siguientes:

```r
t.test(x, y = NULL,
       alternative = c("two.sided", "less", "greater"),
       mu = 0, paired = FALSE, var.equal = FALSE,
       conf.level = 0.95, ...)
```

---

## Slide 19 — t.test (Casos de uso)

**t.test**

1) Se puede hallar el intervalo de confianza para $\mu$, considerando que no se conoce $\sigma$.

```r
t.test(Variable, conf.level = 0.95)
```

2) Se puede hallar el intervalo de confianza para la diferencia de dos medias $\mu_1 - \mu_2$.

```r
t.test(Variable 1, Variable 2, paired=FALSE, var.equal = TRUE, conf.level = 0.95)
```

- Si se coloca `var.equal=True` se está considerando que $\sigma^2_1 = \sigma^2_2$
- Si se coloca `var.equal=False` se está considerando que $\sigma^2_1 \neq \sigma^2_2$

Por el momento se debe considerar `paired=False`.

---

## Slide 20 — Ejemplo 6: Asistentestaller.csv

**Ejemplo 6**

Considere el data.frame "Asistentestaller.csv" dado en el Quiz 3.

Cargar dicha base de datos a R, con el nombre "asistaller".

Eliminar todos los NA del data.frame "asistaller". … use `drop_na(data)` y denominarlo "asistsinNA".

**Responder lo siguiente:**

1) Con 90% de confianza ¿se puede afirmar que las varianzas de las edades de hombres y mujeres que asistieron al taller son iguales?

2) Con 90% de confianza ¿se puede afirmar que la edad promedio de los hombres es mayor que la edad promedio de las mujeres que asistieron al taller?

3) Usando 90% de confianza ¿la proporción de mujeres que está en el tercer ciclo es la misma que la proporción de hombres que está en el tercer ciclo?

---

## Slide 21 — Solución: Comparación de varianzas

1) Con 90% de confianza ¿se puede afirmar que las varianzas de las edades de hombres y mujeres que asistieron al taller son iguales?

**Intervalo de confianza para el cociente de varianzas:**

$$\frac{s_1^2}{s_2^2} \cdot F\left(\frac{\alpha}{2}, n_2 - 1, n_1 - 1\right) < \frac{\sigma_1^2}{\sigma_2^2} < \frac{s_1^2}{s_2^2} \cdot F\left(1 - \frac{\alpha}{2}, n_2 - 1, n_1 - 1\right)$$

---

## Slide 22 — Solución: Comparación de medias

2) Con 90% de confianza ¿se puede afirmar que la edad promedio de los hombres es mayor que la edad promedio de las mujeres que asistieron al taller?

---

## Slide 23 — Solución: Comparación de proporciones

3) Usando 90% de confianza ¿la proporción de mujeres que está en el tercer ciclo es la misma que la proporción de hombres que está en el tercer ciclo?

**Código R:**

```r
problema 3:
table(asistCiclo, asistSexcor)
```

**Tabla de contingencia (ciclo vs. sexo):**

| Ciclo | F  | M  |
|-------|----|----|
| 2     | 5  | 8  |
| 3     | 11 | 32 |
| 4     | 2  | 15 |
| 5     | 4  | 9  |
| 6     | 4  | 6  |
| 7     | 0  | 3  |
| 8     | 0  | 1  |

**Cálculos de proporciones:**

```
# de mujeres: 26  ==> en ciclo3: 11 ==> p(F)=11/26=0.423
# de hombres: 74  ==> en ciclo3: 32 ==> p(M)=32/74=0.432
```
