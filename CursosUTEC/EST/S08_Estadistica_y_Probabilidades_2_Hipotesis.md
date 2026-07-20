---
curso: EST
titulo: S08- Estadística y Probabilidades 2-Hipótesis
slides: 43
fuente: S08- Estadística y Probabilidades 2-Hipótesis.pdf
---

# S08- Estadística y Probabilidades 2-Hipótesis

## Índice

Capítulo de Estadística y Probabilidades 2. Contenido transcrito de las diapositivas (fórmulas en LaTeX, figuras descritas).

# S08 — Prueba de Hipótesis

## Slide 1 — Portada

**Título:** Estadística y probabilidades II

**Tema:** Prueba de hipótesis

**Código:** S08

**Institución:** UTEC (Universidad de Ingeniería y Tecnología)

**Equipo:** Equipo de ciencias

## Slide 2 — Repasando I.C.

Se ha obtenido un intervalo de confianza para el salario promedio de trabajadores de una empresa con 90% de confianza, hallándose: $< S/ 2024, S/ 2824 >$.

Si se conoce que la desviación de los salarios en la empresa es de $S/ 972.65$ y que el entrevistador recibió un pago de $S/ 540$, además por cada encuestado se ha generado un gasto de $S/ 6.00$, ¿cuál fue el gasto total de la encuesta?

## Slide 3 — Repasando I.C.

Con 90% de confianza se ha obtenido el intervalo de confianza para la proporción de vehículos que acuden a cumplir con la revisión técnica de su vehículo, pero que no lo pasan por tenerlo en malas condiciones: $<0.1342, 0.2658>$.

¿Cuál sería el intervalo de confianza si el nivel de confianza sube a 95?

¿De cuántos vehículos está conformada la muestra?

## Slide 4 — Hipótesis Estadística

**Una hipótesis estadística,** es una proposición que se plantea, referido a un parámetro de la población.

Dicha proposición es inicialmente una sospecha de lo que ocurre en la población.

Generalmente las hipótesis en su forma simple denominada hipótesis, son referidas a:

- $✓$ La media ($\mu$)
- $✓$ La varianza ($\sigma^2$)
- $✓$ La proporción ($\pi$)

**Para verificar o refutar las hipótesis** se debe tener evidencias, que se han obtenido desde una muestra. Evidentemente la muestra, para ser una buena evidencia, debe estar bien seleccionada y ser representativa de la población.

## Slide 5 — Hipótesis Nula y Alterna

Para realizar una prueba de hipótesis estadística, se debe plantear dos proposiciones que sean opuestas.

Para efectos de comprender en forma simple el planteamiento de las hipótesis, se establece:

- **$H_o$: Es la hipótesis nula** → aquí solo puede colocarse $\geq, \leq$ o $=$
- **$H_a$: Hipótesis alterna** → aquí solo se coloca $<, >, \neq$

Al finalizar el procedimiento de prueba de hipótesis se llegará a una decisión. Aquí se podrá deducir solo una de las siguientes situaciones:

- **Se rechaza $H_o$ (acepté $H_a$)**

O

- **No se rechaza $H_o$ (acepté $H_o$)**

## Slide 6 — Ejemplos

**Ejemplo 1:** Una empresa de servicios hidráulicos está considerando presentar un nuevo plan de servicio para piezas hidráulicas. El plan será presentado si se prefiere por más del 60% de los clientes:

$$H_0: \pi \leq 60\%$$
$$H_a: \pi > 60\% \text{ (lo que el investigador espera)}$$

**Ejemplo 2:** Para el curso de estadística 1 se piensa que la nota promedio en el examen final, no pasará de 15.

$$H_0: \mu \leq 15$$
$$H_a: \mu > 15$$

## Slide 7 — Tipos de Errores al Tomar Decisiones

**Figura:** Matriz de decisión con cuatro cuadrantes mostrando:

| Decisión | $H_o$ es Verdadera | $H_o$ es Falsa |
|----------|-------------------|----------------|
| **Rechazo $H_o$** | Error Tipo I: $\alpha = P(\text{Rech } H_o \mid H_o \text{ es V})$ | No es Error: Rechazo correcto |
| **No Rechazo $H_o$** | No es error: Decisión correcta | Error Tipo II: $\beta = P(\text{No rech } H_o \mid H_o \text{ es F})$ |

**Potencia** = $1 - \beta$

## Slide 8 — Prueba de Hipótesis de una Media

### Paso 1: Plantear las hipótesis

Se tiene 3 posibilidades:

| Caso Bilateral | Caso Unilateral Izq | Caso Unilateral Der |
|---|---|---|
| $H_0: \mu = \mu_0$ | $H_0: \mu \geq \mu_0$ | $H_0: \mu \leq \mu_0$ |
| $H_a: \mu \neq \mu_0$ | $H_a: \mu < \mu_0$ | $H_a: \mu > \mu_0$ |

### Paso 2: Fijar el nivel de significancia ($\alpha$)

Puede ser: 0.01, 0.05, 0.10, etc.

### Paso 3: Estadístico de prueba

**Caso 1: Varianza poblacional conocida**

$$Z_o = \frac{\bar{x} - \mu_o}{\frac{\sigma}{\sqrt{n}}}$$

**Caso 2: Varianza poblacional desconocida, pero varianza muestral conocida**

$$T_o = \frac{\bar{x} - \mu_o}{\frac{s}{\sqrt{n}}}$$

## Slide 9 — Prueba de una Media (Región de Rechazo y Decisión)

### Paso 4: Región de Rechazo de $H_o$

**Figura:** Tres gráficos de distribución normal mostrando regiones de rechazo:

1. **Caso bilateral ($H_a: \neq$):** Dos colas con área $\alpha/2$ cada una; región de no rechazo en el centro con área $1-\alpha$
2. **Caso unilateral derecho ($H_a: >$):** Una cola derecha con área $\alpha$; región de no rechazo en el centro-izquierda con área $1-\alpha$
3. **Caso unilateral izquierdo ($H_a: <$):** Una cola izquierda con área $\alpha$; región de no rechazo en el centro-derecha con área $1-\alpha$

### Paso 5: Valor crítico

Borde de la región de rechazo de $H_o$. Depende del caso del paso 3.

**Para caso 1:** $Z_{\alpha/2}$ y $Z_{1-\alpha/2}$ o $Z_{1-\alpha}$ o $Z_{\alpha}$

**Para caso 2:** $T_{\alpha/2}$ y $T_{1-\alpha/2}$ o $T_{1-\alpha}$ o $T_{\alpha}$

### Paso 6: Decisión e interpretación

- Si el estadístico de prueba $\in$ región sombreada → **Rechazo $H_o$**
- Si el estadístico de prueba $\notin$ región sombreada → **No rechazo $H_o$**

## Slide 10 — Ejemplo 1

Una máquina está calibrada para embolsar azúcar a un peso promedio de 1000 g. Para determinar si se debe calibrar la máquina, se toma una muestra aleatoria de 64 bolsas y encuentra un promedio de 997 g. Si suponemos que el peso se distribuye normalmente con una desviación estándar de 20 g, ¿puede afirmarse que se está estafando al público consumidor de azúcar? Use 5% de significancia.

## Slide 11 — Ejemplo 2

Una máquina está calibrada para embolsar azúcar a un peso promedio de 1000 g. Para determinar si se debe calibrar la máquina, se toma una muestra aleatoria de 64 bolsas y encuentra un promedio de 997 g. Si suponemos que el peso se distribuye normalmente con una desviación estándar de 20 g, ¿puede afirmarse que la máquina necesita ser calibrada? Use 5% de significancia.

**Figura:** Distribución normal con valor crítico, mostrando regiones $RH_0$ en ambas colas ($\alpha/2$) y región de no rechazo $NRH_0$ en el centro ($1-\alpha$).

## Slide 12 — Ejemplo 3

Considerando el data frame `asistscinNA` de la base de datos `asistentestaller.csv`, como una muestra de todos los que asistieron al taller, en diversas fechas realizadas y con 10% de significación, ¿puede afirmarse que la edad promedio de las mujeres que asistieron al taller es superior a 18.5 años?

**Figura:** Distribución normal con región de no rechazo $NRH_0$ (área $1-\alpha$) y región de rechazo $RH_0$ (área $\alpha$ en la cola derecha), etiquetado con $H_a: >$.

## Slide 13 — Ejemplo 3 (Solución en R)

El mismo problema pero ahora con `t.test`:

```r
{r}
t.test(muestra2$Edad, alternative = "greater", mu= 18.5, conf.level = 0.90)
```

**Output:**

```
One Sample t-test

data: muestra2$Edad
t = 2.949, df = 49, p-value = 0.002438
alternative hypothesis: true mean is greater than 18.5
90 percent confidence interval:
 18.86926     Inf
sample estimates:
mean of x
    19.16
```

**Interpretación:**

*Cuando $p$-valor $< \alpha$ ⟹ siempre se rechaza $H_o$*

Aquí $p$-valor=0.002438 < $\alpha$= 0.10 ⟹ rechazo $H_o$

⟹ Hay evidencias de que la edad promedio de mujeres es mayor que 18.5 años

## Slide 14 — Prueba de Hipótesis con T para Medias con R

Para realizar este tipo de prueba se puede usar la función `t.test` que tiene la siguiente estructura:

```r
t.test(x, y = NULL,
       alternative = c("two.sided", "less", "greater"),
       mu = 0, paired = FALSE, var.equal = FALSE,
       conf.level = 0.95, ...)
```

Los argumentos a definir dentro de `t.test` para hacer la prueba son:

- **`x`:** vector numérico con los datos.
- **`alternative`:** tipo de hipótesis alterna. Los valores disponibles son `"two.sided"` cuando la hipótesis alterna es $\neq$, `"less"` para el caso $<$ y `"greater"` para $>$.
- **`mu`:** valor de referencia de la prueba.
- **`conf.level`:** nivel de confianza para reportar el intervalo de confianza asociado (opcional).

## Slide 15 — t.test

1) Se puede hacer prueba de hipótesis para $\mu$, considerando que no se conoce $\sigma$.

```r
t.test (Variable, alternative = "...", conf.level = 0.95)
```

2) Se puede hacer prueba de hipótesis para la diferencia de dos medias $\mu_1 - \mu_2$.

```r
t.test(Variable 1, Variable 2, alternative= "...", paired = FALSE, var.equal = TRUE,
conf.level = 0.95)
```

- Si se coloca `var.equal=True` se está considerando que $\sigma^2_1 = \sigma^2_2$
- Si se coloca `var.equal= False` se está considerando que $\sigma^2_1 \neq \sigma^2_2$

Si se coloca `paired = TRUE`, se estará considerando tener datos pareados, es decir, se tendrá una muestra en dos situaciones: un **"ANTES"** y un **"DESPUÉS"**.

## Slide 16 — P-valor

Una manera más rápida de hacer una prueba de hipótesis es mediante el p-valor. Para el caso de 1 media:

**Si se conoce $\sigma$:**

- Cuando $H_a: <$ ⟹ $p_v = P(Z < Z_o)$ (Siendo $Z_o$ el estadístico de prueba)
- Cuando $H_a: >$ ⟹ $p_v = P(Z > Z_o)$
- Cuando $H_a: \neq$ ⟹ $p_v = 2P(Z > |Z_o|)$

**Análogamente si no se conoce $\sigma$** (usar T–student)

---

**En general, para toda prueba de hipótesis:**

$$\boxed{\text{Se rechazará } H_o \text{ si } p_v < \alpha}$$

---

**Ejemplo:**

| Dato | Valor |
|------|-------|
| $H_o$: $\mu = 1000$ | |
| $H_a$: $\mu \neq 1000$ | |
| $\sigma = 20$ | |
| $n = 64$ | |
| $\alpha = 0.05$ | |
| $\bar{x} = 997$ | |

Cálculo:

$$Z_o = \frac{997 - 1000}{20/8} = -1.2$$

$$P\text{-valor} = 2P(Z > |-1.2|) = 2(pnorm(1.2, 0, 1, lower.tail = F) = 2(0.115) = 0.23$$

El valor 0.1150697 mostrado corresponde a $P(Z > 1.2)$.

## Slide 17 — Ejemplo 4

En estudios previos se ha determinado que el nivel de colesterol promedio de pacientes con problemas cardíacos es 220. Un cardiólogo piensa que en realidad el nivel es más alto y para probar su afirmación usa la muestra:

```
217  223  225  245  238  216  217  226  202  233
235  242  219  221  234  199  236  248  218  224
```

¿Habrá suficiente evidencia estadística para apoyar la afirmación del cardiólogo? Justificar su respuesta con un $\alpha = 0.05$.

**Código R:**

```r
{r}
datos <- c(217,235,223,242,225,219,245,221,238,234,216,199,217,236,226,248,202,218,233,224)
datos

{r}
t.test(datos,alternative = "greater",mu= 220, conf.level = 0.95)
```

**Output:**

```
One Sample t-test

data: datos
t = 2.015, df = 19, p-value = 0.02914
alternative hypothesis: true mean is greater than 220
95 percent confidence interval:
 220.8371     Inf
sample estimates:
mean of x
   225.9
```

## Slide 18 — Prueba de Hipótesis de una Proporción

### Paso 1: Plantear las hipótesis

Se tiene 3 posibilidades:

| Caso Bilateral | Caso Unilateral Izq | Caso Unilateral Der |
|---|---|---|
| $H_0: \pi = \pi_0$ | $H_0: \pi \geq \pi_0$ | $H_0: \pi \leq \pi_0$ |
| $H_a: \pi \neq \pi_0$ | $H_a: \pi < \pi_0$ | $H_a: \pi > \pi_0$ |

### Paso 2: Fijar el nivel de significancia ($\alpha$)

Puede ser: 0.01, 0.05, 0.10, etc.

### Paso 3: Estadístico de prueba

$$Z_o = \frac{p - \pi_o}{\sqrt{\frac{\pi_o(1 - \pi_o)}{n}}}$$

Donde:
- **$p$:** proporción muestral
- **$\pi_o$:** Proporción poblacional que se está probando en $H_o$

## Slide 19 — Prueba de una Proporción (Región de Rechazo y Decisión)

### Paso 4: Región de Rechazo de $H_o$

**Figura:** Tres gráficos de distribución normal mostrando regiones de rechazo:

1. **Caso bilateral ($H_a: \neq$):** Dos colas con área $\alpha/2$ cada una; región de no rechazo en el centro con área $1-\alpha$
2. **Caso unilateral derecho ($H_a: >$):** Una cola derecha con área $\alpha$; región de no rechazo en el centro-izquierda con área $1-\alpha$
3. **Caso unilateral izquierdo ($H_a: <$):** Una cola izquierda con área $\alpha$; región de no rechazo en el centro-derecha con área $1-\alpha$

### Paso 5: Valor crítico

Borde de la región de rechazo de $H_o$. Depende del caso del paso 3.

$$Z_{\alpha/2} \text{ y } Z_{1-\alpha/2} \text{ o } Z_{1-\alpha} \text{ o } Z_{\alpha}$$

### Paso 6: Decisión e interpretación

- Si el estadístico de prueba $\in$ región sombreada → **Rechazo $H_o$**
- Si el estadístico de prueba $\notin$ región sombreada → **No rechazo $H_o$**

## Slide 20 — Ejemplo 5

El administrador de un supermercado afirma que menos del 10% de los productos que ofrece su proveedor son defectuosos. Si la afirmación es correcta se procederá a mantener al proveedor, caso contrario cambiarán de proveedor. Para tomar una mejor decisión se selecciona una muestra de 180 productos de los cuales sólo 13 productos presentaron algún defecto. Usando un nivel de significancia del 5% ¿Qué decisión debe tomar el administrador?

**Estadístico de prueba:**

$$Z_o = \frac{p - \pi_o}{\sqrt{\frac{\pi_o(1 - \pi_o)}{n}}}$$

---

## Slide 21 — Ejemplo 6: Prueba de una proporción

En una empresa se ha estimado que el 25% de los trabajadores tienen su propia movilidad y ello implica que deben agrandar su playa de estacionamiento. ¿Es posible refutar esta estimación?, si un estudio realizado por la compañía de vigilancia y seguridad tomó muestra de 90 trabajadores y encontró que 32 de ellos tienen su vehículo. Utilice un nivel de significancia del 6%.

**Estadístico de prueba:**

$$Z_o = \frac{p - \pi_0}{\sqrt{\frac{\pi_0(1 - \pi_0)}{n}}}$$

---

## Slide 22 — Prueba de hipótesis de una varianza: Paso 1

**Paso 1: Plantear las hipótesis**

Se tiene 3 posibilidades:

| Hipótesis bilateral | Hipótesis unilateral izquierda | Hipótesis unilateral derecha |
|---|---|---|
| $H_0: \sigma^2 = \sigma^2_0$ | $H_0: \sigma^2 \geq \sigma^2_0$ | $H_0: \sigma^2 \leq \sigma^2_0$ |
| $H_a: \sigma^2 \neq \sigma^2_0$ | $H_a: \sigma^2 < \sigma^2_0$ | $H_a: \sigma^2 > \sigma^2_0$ |

**Paso 2: Fijar el nivel de significancia (α).** Puede ser: 0.01, 0.05, 0.10, etc.

**Paso 3: Estadístico de prueba:**

$$\chi^2_o = \frac{(n-1)S^2}{\sigma^2_o}$$

Con $n-1$ grados de libertad

---

## Slide 23 — Prueba de una varianza: Paso 4, 5, 6

**Paso 4: Región de Rechazo de Ho**

**Figura:** Se muestran tres distribuciones chi-cuadrado según el tipo de hipótesis:
- *Hipótesis bilateral* ($H_a: \neq$): dos colas sombreadas con zonas de rechazo en $\chi^2_{\alpha/2, n-1}$ (izquierda) y $\chi^2_{1-\alpha/2, n-1}$ (derecha), región no rechazo al centro.
- *Hipótesis unilateral derecha* ($H_a: >$): cola derecha sombreada en $\chi^2_{1-\alpha, n-1}$, región no rechazo a la izquierda.
- *Hipótesis unilateral izquierda* ($H_a: <$): cola izquierda sombreada en $\chi^2_{\alpha, n-1}$, región no rechazo a la derecha.

**Paso 5: Valor crítico:** borde de la región de rechazo de Ho. Depende del caso del paso 3.

$$\chi^2_{\alpha/2} \text{ y } \chi^2_{1-\alpha/2} \quad \text{o} \quad \chi^2_{1-\alpha} \quad \text{o} \quad \chi^2_{\alpha}$$

**Paso 6: Decisión e interpretación**

- Si el estadístico de prueba ∈ región sombreada → Rechazo Ho.
- Si el estadístico de prueba ∉ región sombreada → No rechazo Ho.

---

## Slide 24 — Ejemplo 7: Rodamientos esféricos

Los rodamientos esféricos que fabrica una máquina deben de tener un diámetro relativamente uniforme para ser aptos para su uso. El responsable de la máquina asegura que la desviación estándar máxima aceptable para estos rodamientos es de 0.025 centímetros y él sospecha que este requerimiento no se está cumpliendo. Para ello ha tomado una muestra de 50 rodamientos producidos por la máquina y obtenido una varianza muestral de 0.0272. ¿Son fundamentadas las sospechas del responsable? Use $\alpha = 0.05$.

---

## Slide 25 — Prueba de hipótesis para diferencia de medias: Muestras independientes

**PRUEBA DE HIPÓTESIS PARA LA DIFERENCIA DE MEDIAS CON MUESTRAS INDEPENDIENTES**

Se llama así, con muestras independientes, cuando cada una no están relacionadas y una no influye en la otra.

**Paso 1: Planteo de las hipótesis**

Se tiene 3 posibilidades:

| PH unilateral izquierda | PH unilateral derecha | PH bilateral |
|---|---|---|
| $H_0: \mu_1 - \mu_2 \geq k$ | $H_0: \mu_1 - \mu_2 \leq k$ | $H_0: \mu_1 - \mu_2 = k$ |
| $H_1: \mu_1 - \mu_2 < k$ | $H_1: \mu_1 - \mu_2 > k$ | $H_1: \mu_1 - \mu_2 \neq k$ |

**Paso 2: Fijar el nivel de significación**

Fijar $\alpha$ (DATO)

**CASO 1: SI LAS VARIANZAS SON HOMOGÉNEAS** $\sigma^2_1 = \sigma^2_2$

**Paso 3: Hallar el estadístico de prueba**

$$T_o = t_{cal} = \frac{\overline{x_1} - \overline{x_2} - k}{Sp\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$

Donde:

$$Sp^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1 + n_2 - 2}$$

$$g.l. = n_1 + n_2 - 2$$

**CASO 2: SI LAS VARIANZAS SON HETEROGÉNEAS** $\sigma^2_1 \neq \sigma^2_2$

**Paso 3: Hallar el estadístico de prueba**

$$T_o = t_{cal} = \frac{\overline{x_1} - \overline{x_2} - k}{\sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}}$$

$$v = \frac{\left(\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}\right)^2}{\frac{(S_1^2/n_1)^2}{n_1-1} + \frac{(S_2^2/n_2)^2}{n_2-1}} = g.l.$$

---

## Slide 26 — Prueba de comparación de 2 medias: Paso 4, 5, 6

**CASO 1: SI LAS VARIANZAS SON HOMOGÉNEAS**

**Paso 4: Determinar los valores críticos**

**Figura:** Tres distribuciones t con $n_1 + n_2 - 2$ grados de libertad:
- *Unilateral izquierda*: región sombreada izquierda en $t_{\alpha, n_1+n_2-2}$
- *Unilateral derecha*: región sombreada derecha en $t_{1-\alpha, n_1+n_2-2}$
- *Bilateral*: dos colas sombreadas en $t_{\alpha/2, n_1+n_2-2}$ y $t_{1-\alpha/2, n_1+n_2-2}$

**CASO 2: SI LAS VARIANZAS SON HETEROGÉNEAS**

**Paso 4: Determinar los valores críticos**

**Figura:** Tres distribuciones t con $v$ grados de libertad:
- *Unilateral izquierda*: región sombreada izquierda
- *Unilateral derecha*: región sombreada derecha
- *Bilateral*: dos colas sombreadas (nota: se usa "RNR" para región no rechazo, "RR" para región rechazo)

**Paso 5: Decisión**

Decisión: Se rechaza Ho o No se rechaza Ho

**Paso 6: Conclusión**

Conclusión: Mencionar el nivel de significación y concluir con H1.

---

## Slide 27 — Prueba de hipótesis de comparación de 2 varianzas

**PRUEBA DE HIPÓTESIS DE COMPARACIÓN DE 2 VARIANZAS**

**Paso 1: Plantear las hipótesis**

Se tiene 3 posibilidades

| | | |
|---|---|---|
| $H_0: \sigma^2_1 = \sigma^2_2$ | $H_0: \sigma^2_1 \geq \sigma^2_2$ | $H_0: \sigma^2_1 \leq \sigma^2_2$ |
| $H_a: \sigma^2_1 \neq \sigma^2_2$ | $H_a: \sigma^2_1 < \sigma^2_2$ | $H_a: \sigma^2_1 > \sigma^2_2$ |

**Paso 2: Fijar el nivel de significancia (α).** Puede ser: 0.01, 0.05, 0.10, etc.

**Paso 3: Estadístico de prueba:**

$$F_o = \frac{S^2_1}{S^2_2}$$

$$F(n_1 - 1; n_2 - 1)$$

---

## Slide 28 — Prueba de comparación de 2 medias: Paso 4, 5, 6

**Paso 4: Región de Rechazo de Ho**

**Figura:** Se muestran tres distribuciones F con diferentes grados de libertad según el tipo de hipótesis:
- *Hipótesis bilateral* ($H_a: \neq$): dos colas sombreadas con zonas de rechazo en $F(\alpha/2, n_1-1, n_2-1)$ (izquierda) y $F(1-\alpha/2, n_1-1, n_2-1)$ (derecha).
- *Hipótesis unilateral derecha* ($H_a: >$): cola derecha sombreada en $F(1-\alpha, n_1-1, n_2-1)$.
- *Hipótesis unilateral izquierda* ($H_a: <$): cola izquierda sombreada en $F(\alpha, n_1-1, n_2-1)$.

**Paso 5: Valor crítico:** borde de la región de rechazo de Ho. Depende del caso del paso 3.

$$F_{\alpha/2} \text{ y } F_{1-\alpha/2} \quad \text{o} \quad F_{1-\alpha} \quad \text{o} \quad F_{\alpha}$$

**Paso 6: Decisión e interpretación**

- Si el estadístico de prueba ∈ región sombreada → Rechazo Ho.
- Si el estadístico de prueba ∉ región sombreada → No rechazo Ho.

Con R−studio usar: `Var.test →`

```r
var.test(I1, I2, null.value=1, alternative="two.sided", conf.level=0.95)
```

---

## Slide 29 — Ejemplo 8: Resistencia de discos

Una característica importante de cierto producto es su durabilidad; es decir, su capacidad de resistir el desgaste. Un ingeniero de discos selecciono dos muestras de diferentes marcas que su empresa usa, los cuales dieron los siguientes resultados de la resistencia.

| Marca A [1] | $n_1 = 6$ | 4131 | 3665 | 3849 | 3876 | 3791 | 3843 |
|---|---|---|---|---|---|---|---|
| Marca B [2] | $n_2 = 7$ | 2997 | 2632 | 2957 | 2714 | 2788 | 3046 | 3231 |

El ingeniero propone a la gerencia que, **si encuentra diferencia en la resistencia promedio en ambas marcas**, entonces realizará **cambios en su toma de decisión**. Utilizando un nivel de significación del 8%.

**Código R:**

```r
var.test(marca1, marca2, null.value=1, alternative="two.sided", conf.level=0.92)
```

**Output de R:**

```
F test to compare two variances

data: marca1 and marca2
F = 0.53558, num df = 5, denom df = 6, p-value = 0.51
alternative hypothesis: true ratio of variances is not equal to 1
92 percent confidence interval:
0.11013 2.96006
sample estimates:
ratio of variances
0.5335823
```

---

## Slide 30 — Continuación Ejemplo 8

| Marca A [1] | 4131 | 3665 | 3849 | 3876 | 3791 | 3843 |
|---|---|---|---|---|---|---|
| Marca B [2] | 2997 | 2632 | 2957 | 2714 | 2788 | 3046 | 3231 |

El ingeniero propone a la gerencia que, **si encuentra diferencia en la resistencia promedio en ambas marcas**, entonces realizará **cambios en su toma de decisión**. Utilizando un nivel de significación del 8%.

**Código R:**

```r
t.test(marca1, marca2, NULL=0, alternative = "two.sided", conf.level = 0.92)
```

**Output de R:**

```
Welch Two Sample t-test

data: marca1 and marca2
t = 9.4368, df = 10.787, p-value = 1.527e-06
alternative hypothesis: true difference in means is not equal to 0
92 percent confidence interval:
755.3824 1144.3795
sample estimates:
mean of x  mean of y
3859.167  2909.286
```

---

## Slide 31 — Ejemplo 9: Placas de Ate vs Lurín

Por los resultados de los últimos meses, el ingeniero de producción considera que las placas producidas en la **planta de Ate tienen un índice promedio de rigidez axial mayor** que las producidas en la **planta Lurín**. Si esta consideración es cierta, realizará las **acciones correctivas en ambas plantas**. Para tal fin, se ha obtenido la siguiente información:

| Planta | Número de placas | Índice promedio (libras/pulg²) | Desviación estándar (libras/pulg²) |
|---|---|---|---|
| Ate (1) | 16 | 455 | 15 |
| Lurín (2) | 21 | 420 | 58 |

Con un nivel de significación de 5% y asuma que el índice de rigidez axial tiene distribución normal

**Código R:**

```r
Fizq <- qf(alfa/2, n1-1,n2-1)
Fder <- qf(1-alfa/2,n1-1,n2-1)
Fizq
```

**Output:**

```
[1] 0.3628576
[1] 2.373096
```

---

## Slide 32 — Continuación Ejemplo 9

| Planta | Número de placas | Índice promedio (libras/pulg²) | Desviación estándar (libras/pulg²) |
|---|---|---|---|
| Ate (1) | 16 | 455 | 15 |
| Lurín (2) | 21 | 420 | 58 |

**Código R con varianzas homogéneas o iguales:**

```{r}
#como alternativa es MAYOR
To <- qt(1 alfa, n1+n2 -2)
To

# Estadístico de prueba
#varianza ponderada
S2p <- ((n1-1)*(S1^2)+(n2-1)*(S2^2))/(n1+n2-2)
S2p
# Estadístico de prueba
To= ((x1-x2)-(k))/sqrt(S2p*(1/n1 + 1/n2))
To

[1] 1.689572
[1] 2018.714
[1] 2.347466
```

---

## Slide 33 — Prueba de hipótesis para diferencia de medias con muestras relacionadas o pareadas

**PRUEBA DE HIPÓTESIS PARA LA DIFERENCIA DE MEDIAS CON MUESTRAS RELACIONADAS O PAREADAS**

Se llama así, cuando se trata de los mismos elementos seleccionados, pero en dos instantes: un Antes y un Después.

**Paso 1: Planteo de las hipótesis**

Se tiene 3 posibilidades:

| PH unilateral izquierda | PH unilateral derecha | PH bilateral |
|---|---|---|
| $H_0: \mu_1 - \mu_2 \geq k$ | $H_0: \mu_1 - \mu_2 \leq k$ | $H_0: \mu_1 - \mu_2 = k$ |
| $H_1: \mu_1 - \mu_2 < k$ | $H_1: \mu_1 - \mu_2 > k$ | $H_1: \mu_1 - \mu_2 \neq k$ |

**Paso 2: Fijar el nivel de significación**

Fijar $\alpha$

**Paso 3: Hallar el estadístico de prueba**

$$T_o = t_{cal} = \frac{\bar{d} - k}{S_d / \sqrt{n}}$$

Donde:

- $\bar{d}$: promedio de las diferencias de los datos 1 − (2)
- $S_d$: desviación de las diferencias 1 − (2)

Con R−studio usar: `t.test`

---

## Slide 34 — Muestras pareadas: Paso 4, 5, 6

**Paso 4: Hallar las regiones críticas**

**Figura:** Tres distribuciones t con $n-1$ grados de libertad según el tipo de hipótesis:
- *Unilateral izquierda*: región sombreada izquierda (RR) separada por $T(\alpha; n-1)$, región no rechazo (RNR) a la derecha.
- *Unilateral derecha*: región no rechazo (RNR) a la izquierda, región sombreada derecha (RR) separada por $T(1-\alpha; n-1)$.
- *Bilateral*: dos colas sombreadas (RR), región no rechazo (RNR) al centro, separadas por $T(\alpha/2; n-1)$ y $T(1-\alpha/2; n-1)$.

**Paso 5: Decisión**

Decisión: Se rechaza Ho o No se rechaza Ho

**Paso 6: Conclusión**

Conclusión: Mencionar el nivel de significación y concluir con H1.

Con R−studio usar: `t.test`

```r
t.test(x, y, ..., NULL=0, paired=FALSE, var.equal = FALSE, conf.level = 0.95, ...)
```

---

## Slide 35 — Ejemplo 10: Utilidades de empresas informáticas

Un Agente de la Bolsa de valores presenta las utilidades por acción, hasta fincs de julio del 2022, en una muestra aleatoria elegida entre las empresas informáticas de Lima. Los datos correspondientes (en dólares) se muestran a continuación:

| Empresa | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Utilidad Pronosticadas [1] | 7.3 | 26.6 | 37.8 | 21.3 | 25.3 | 25.4 | 20.6 | 25.3 | 19.0 | 20.9 |
| Utilidad Reales [2] | 12.9 | 20.1 | 25.9 | 16.0 | 18.4 | 27.2 | 15.1 | 22.8 | 7.7 | 18.1 |

El agente considera que el promedio de las utilidades pronosticadas será superior al promedio de las utilidades reales. Asumiendo normalidad en las utilidades, ¿el agente de bolsa tiene la razón? Utilice un nivel de significación del 3%.

**Código R:**

```r
t.test(muestra1, muestra2, NULL=0, alternative = "greater", paired = TRUE, conf.level = 0.97)
```

**Output de R:**

```
Paired t-test

data: muestra1 and muestra2
t = 2.6602, df = 9, p-value = 0.0130
alternative hypothesis: true difference in means is greater than 0
97 percent confidence interval:
0.6681761   Inf
sample estimates:
mean difference
4.53
```

---

## Slide 36 — Prueba de hipótesis de 2 proporciones

**PRUEBA DE HIPÓTESIS DE 2 PROPORCIONES**

**Paso 1: Plantear las hipótesis**

Se tiene 3 posibilidades

| | | |
|---|---|---|
| $H_0: \pi_1 - \pi_2 = \pi_0$ | $H_0: \pi_1 - \pi_2 \geq \pi_0$ | $H_0: \pi_1 - \pi_2 \leq \pi_0$ |
| $H_a: \pi_1 - \pi_2 \neq \pi_0$ | $H_a: \pi_1 - \pi_2 < \pi_0$ | $H_a: \pi_1 - \pi_2 > \pi_0$ |

**Paso 2: Fijar el nivel de significancia (α).** Puede ser: 0.01, 0.05, 0.10, etc.

**Paso 3: Estadístico de prueba:**

$$Z_o = \frac{(p_1 - p_2) - \pi_o}{\sqrt{\bar{P}(1 - \bar{P})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}$$

Donde:

$$\bar{P} = \frac{n_1p_1 + n_2p_2}{n_1 + n_2} = \frac{x_1 + x_2}{n_1 + n_2}$$

---

## Slide 37 — Prueba de dos proporciones: Paso 4, 5, 6

**Paso 4: Región de Rechazo de Ho**

**Figura:** Se muestran tres distribuciones normal estándar según el tipo de hipótesis:
- *Hipótesis bilateral* ($H_a: \neq$): dos colas sombreadas en $Z_{\alpha/2}$ (izquierda) y $Z_{1-\alpha/2}$ (derecha).
- *Hipótesis unilateral derecha* ($H_a: >$): cola derecha sombreada en $Z_{1-\alpha}$.
- *Hipótesis unilateral izquierda* ($H_a: <$): cola izquierda sombreada en $Z_{\alpha}$.

**Paso 5: Valor crítico:** borde de la región de rechazo de Ho. Depende del caso del paso 3.

$$Z_{\alpha/2} \text{ y } Z_{1-\alpha/2} \quad \text{o} \quad Z_{1-\alpha} \quad \text{o} \quad Z_{\alpha}$$

**Paso 6: Decisión e interpretación**

- Si el estadístico de prueba ∈ región sombreada → Rechazo Ho.
- Si el estadístico de prueba ∉ región sombreada → No rechazo Ho.

---

## Slide 38 — Ejemplo 11: Medicinas para presión sanguínea

Considere el caso de una compañía que fabrica productos medicinales y que está probando dos nuevos compuestos destinados a reducir los niveles de presión sanguínea. Los compuestos se administran a dos conjuntos de animales de laboratorio.

En el grupo uno, 71 de 100 animales respondieron a la droga 1 con niveles menores de presión arterial.

En el grupo dos, 58 de 90 animales respondieron a la droga 2 con menores niveles de presión sanguínea.

La compañía desea probar a un nivel de significancia de 0.05 si existe una diferencia en la eficacia de las dos medicinas.

---

## Slide 39 — Ejemplo 12: COMPU S.A. (Comparación de proveedores)

La empresa COMPU S.A fabricante de microprocesadores compra los microcircuitos de sus productos a dos proveedores: una muestra de 200 microcircuitos del proveedor X contuvo 20 defectuosos, mientras que una muestra de 280 piezas del proveedor Y presentó 35 con fallas.

La empresa sospecha que el proveedor Y genera mas defectuosos que X y por ello piensan en dejar de solicitar sus productos. ¿Qué decisión tomar al 1% de significación?

---

## Slide 40 — Ejemplo 13: Golf (Marcas de cigarrillos)

La empresa Golf fabricante de cigarrillos distribuye dos marcas de cigarrillos. En una encuesta se encuentra que 144 de 200 fumadores no prefieren la marca A y que 121 de 150 fumadores encuestados no prefieren la marca B. ¿Se puede concluir al nivel de significación 0.025 que la marca A se vende más rápidamente que la marca B?

---

## Slide 41 — Ejemplo 14

Se desea determinar si el curso de Estadística 2 es más simple en la segunda mitad del curso, que en la primera mitad. Para ello se ha obtenido las notas de los alumnos, tanto en el parcial como en el final:

- Parcial: 12, 15, 17, 13, 10, 11, 13 → $n = 7$ (Antes)
- Final: 11, 17, 19, 13, 13, 12, 14 → $n = 7$ (Después)

**Al 95% ¿Qué se puede concluir?**

### Planteamiento de hipótesis

$$H_0: \mu_p \geq \mu_f$$

$$H_a: \mu_p < \mu_f \quad \text{(La 2ª parte es más simple)}$$

$$\alpha = 0.05$$

### Estadístico de prueba

$$T_0 = \frac{\bar{d}}{S_d / \sqrt{n}} = -2.2478$$

donde $d = \mu_p - \mu_f$

### Región de rechazo

**Figura:** Distribución t de Student con 6 grados de libertad. La región crítica (sombreada en la cola izquierda) comienza en $T_{\alpha, n-1} = T_{0.05, 6} = -1.94$. El estadístico observado $T_0 = -2.2478$ cae en la región de rechazo.

### Decisión

Como $T_0 = -2.2478 \in$ Región de rechazo (pues $-2.2478 < -1.94$), se **rechaza $H_0$**.

### Conclusión

Con 95% de significación hay evidencia de que el tramo final es más simple.

### Salida R

```r
data: parcial and final
t = -2.2478, df = 6, p-value = 0.03282
alternative hypothesis: true mean difference is less than 0
95 percent confidence interval:
-Inf -0.1548815
sample estimates:
mean difference
-1.142857
```

---

## Slide 42 — Ejemplo 15

Para transportar mercadería desde una sede M hasta una sede N en un camión, el conductor cree que con 10 galones llegará a su destino, ya que según registros anteriores de 36 veces que viajaron de M a N, en promedio se usa 9.6 galones de combustible. Considere que la desviación es de 1 galón. Use 5% de significación de ser necesario.

1) Interprete los errores tipo 1 y 2
2) ¿Indique cuál es el error más grave?
3) ¿Para qué valores del promedio muestral, si se podría considerar que llega a su destino?
4) Calcule el P-Valor

---

## Slide 43 — Ejemplo 15 (continuación)

Para transportar mercadería desde una sede M hasta una sede N en un camión, el conductor cree que con 10 galones llegará a su destino, ya que según registros anteriores de 36 veces que viajaron de M a N, en promedio se usa 9.6 galones de combustible. Considere que la desviación es de 1 galón. Use 5% de significación de ser necesario.

1) Interprete los errores tipo 1 y 2
2) Indique ¿cuál es el error más grave?
3) ¿Para qué valores del promedio muestral, si se podría considerar que llega a su destino?
4) Calcule el P-Valor
