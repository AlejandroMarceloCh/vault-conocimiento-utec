---
curso: EST
titulo: S09_Estadística y probabilidades 2-No paramétricas
slides: 31
fuente: S09_Estadística y probabilidades 2-No paramétricas.pdf
---

# S09_Estadística y probabilidades 2-No paramétricas

## Índice

Pruebas no paramétricas (signos, rachas, chi-cuadrado de independencia y bondad de ajuste).

# Pruebas No Paramétricas — S09

## Slide 1 — Portada

**Pruebas no paramétricas**

S09

Estadística y probabilidades II — UTEC

---

## Slide 2 — Introducción a métodos paramétricos

En los temas anteriores, las pruebas de hipótesis que se estudiaron se basan en la suposición de que las muestras aleatorias se seleccionan de poblaciones normales.

Cuando las muestras son grandes, se ha visto que la media muestral, a pesar de no venir de una población normal, se le puede aproximar como una variable con distribución normal, esto debido al teorema del límite central.

A estas pruebas se les conoce como **métodos paramétricos**.

En esta unidad se va a estudiar procedimientos de prueba alternativos, llamadas **pruebas no paramétricas** que a menudo no requieren del conocimiento de la distribución de origen de los datos.

Los procedimientos no paramétricos o de **distribución libre** se usan con mayor frecuencia por los analistas de datos. Existen muchas aplicaciones en la ciencia y la ingeniería donde los datos se reportan no como valores continuos sino más bien en una escala ordinal tal que es bastante natural asignar rangos a los datos.

---

## Slide 3 — Prueba de signos — Introducción

La **prueba de signos** realiza una prueba de hipótesis sobre la **mediana** de una variable con distribución continua.

Esta prueba es el **equivalente no paramétrico** a la prueba de hipótesis referente al valor de la media poblacional.

Recordemos que la **mediana** de una distribución es un valor de la variable aleatoria $X$ tal que la probabilidad de que un valor observado de $X$ sea menor o igual, o mayor o igual, que la mediana es $0.5$.

Para poder realizar la prueba de signos se va a seguir el método de la prueba de hipótesis.

---

## Slide 4 — Prueba de signos — Procedimiento (Pasos 1-4)

**Paso 1: Hipótesis**

$$H_o: Me = Me_o$$
$$H_a: Me \neq Me_o \quad \text{(o } < \text{ o } > \text{)}$$

donde $\alpha$ es el nivel de significación.

**Paso 2: Estadístico de prueba**

En la tabla de datos de la muestra, colocar $(+)$ cuando el dato excede a $Me_o$ y colocar $(-)$ si los datos son menores que $Me_o$.

Si algún dato coincide con $Me_o$, se irá reduciendo el valor de $n$. Al final se obtiene un $n$ actualizado: $n_o$ $\quad$ $(n_o \leq n)$

**Paso 3: Calcular $R^+$ y $R^-$**

Calcular el valor de $R^+$ que representa la cantidad de positivos obtenidos. $R^-$ será cantidad de negativos.

---

## Slide 5 — Prueba de signos — Distribución binomial

En la prueba de signos se considera siempre una **distribución binomial** en el cual la probabilidad de éxito es igual al $0.5$

**Paso 4: Estadístico reducido**

$$R' = \text{menor valor entre } R^+ \text{ y } R^-$$

**Paso 5: Decisión**

Rechazar $H_o$ si $P\text{valor} < \alpha$

---

## Slide 6 — Ejemplo 1 — Prueba de signos (Baterías)

Debido al uso frecuente de la laptop, la empresa **SOLUCIONES TECNOLÓGICAS** recibe muchos pedidos de baterías, los cuales los trae de Estados Unidos y los precios son muy variados.

La empresa sospecha que el precio mediano que el cliente debe pagar es **S/ 2000**.

Use **5% de significación** y compruebe si es cierto o no lo que sospechan.

---

## Slide 7 — Ejemplo 2 — Prueba de signos (Notas de estudiantes)

Se presentan las notas del último examen parcial del curso de Estadística General de una muestra de 10 estudiantes que fueron elegidos al azar.

Se afirma que la **mediana poblacional de las notas es mayor a 13**.

Probar si dicha afirmación es cierta al nivel de significación del **5%**.

| Alumno | Nota |
|--------|------|
| 1      | 9    |
| 2      | 12   |
| 3      | 8    |
| 4      | 8    |
| 5      | 15   |
| 6      | 11   |
| 7      | 8    |
| 8      | 11   |
| 9      | 13   |
| 10     | 15   |

---

## Slide 8 — Prueba de rachas — Introducción y definiciones

$$H_o: \text{La muestra sí es aleatoria}$$
$$H_a: \text{La muestra no es aleatoria}$$

donde $\alpha$ es el nivel de significación.

**Definiciones:**

- $n_1$: cantidad de $+$ (positivos)
- $n_2$: cantidad de $-$ (negativos)
- $R$: número de rachas (grupos de elementos consecutivos con igual signo)

**Procedimiento:**

Si es que se tiene datos numéricos se calcula la **mediana**. Se **elimina** los datos que coinciden con la mediana. Y cada dato que queda: si excede a la mediana se pone $(+)$. Si es menor que la mediana se pone $(-)$.

---

## Slide 9 — Prueba de rachas — Tabla para muestras pequeñas

Cuando la muestra es **menor o igual a 20**: Buscar en la tabla siguiente los valores $R_{min}$ y $R_{max}$ usando $n_1$ y $n_2$.

$$\text{Si } R \in [R_{min}; R_{max}] \Rightarrow \text{No se rechaza } H_o$$

| $n_1 / n_2$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|-------------|---|---|---|---|---|---|---|---|---|----|
| R mínimo    | - | - | - | - | - | - | - | - | - | -  |
| R máximo    | - | - | - | - | - | - | - | - | - | -  |

**Nota:** La tabla completa de valores $R_{min}$ y $R_{max}$ se encuentra en las referencias estadísticas correspondientes.

---

## Slide 10 — Prueba de rachas — Procedimiento para muestras grandes

$$H_o: \text{La muestra es aleatoria}$$
$$H_a: \text{La muestra no es aleatoria}$$

donde $\alpha$ es el nivel de significación.

**Procedimiento para $n > 20$:**

- Determine la **mediana** del conjunto de datos. (usar: `summary` o `median`)
- **Elimine** los datos que coinciden con la mediana.
- Coloque **positivo** $(+)$ si la observación es mayor a la mediana y **negativos** $(-)$ si el valor es menor a la mediana.
  - $n_1$: número de $+$
  - $n_2$: número de $-$
- **Calcular $R$**: el número de rachas
- **Haga los siguientes cálculos:**

$$\mu_R = \frac{2n_1 n_2}{n_1 + n_2} + 1$$

$$\sigma_R = \sqrt{\frac{2n_1 n_2 (2n_1 n_2 - n_1 - n_2)}{(n_1 + n_2)^2 (n_1 + n_2 - 1)}}$$

$$Z_o = \frac{R - \mu_R}{\sigma_R}$$

Y hacer una **prueba bilateral** (doble cola)

---

## Slide 11 — Ejemplo rachas — Examen de inglés

De una sección de inglés se acaba de tomar su examen final. A solicitud del director, se ha seleccionado un grupo de alumnos de los 50 que rindieron el final.

**¿Será este conjunto una muestra aleatoria de las notas? Use 95%**

$$H_o: \text{La muestra es aleatoria}$$
$$H_a: \text{La muestra no es aleatoria}$$

**Solución:**

- $n_1 = 6$ (+)
- $n_2 = 6$ (-)
- $R = 7$

Estamos con una **muestra pequeña**: $n = 13 < 20$

Usar tabla:
- $R_{min} = 3$
- $R_{max} = 11$

Como $R = 7$ está en $[3; 11]$ $\Rightarrow$ **No rechazo $H_o$**:

Con 5% de significación **no hay evidencias** de que la muestra no sea aleatoria, es decir **se puede aceptar como aleatoria**.

---

## Slide 12 — Ejemplo rachas — Edades de estudiantes (Con R Studio)

Para realizar un proyecto del curso de Estadística 2, un grupo de alumnos presenta una lista de datos que representan a sus edades. El profesor sospecha que las edades presentadas no corresponden a una muestra aleatoria. Por ello decide realizar una **prueba de rachas**, con **5% de significación**.

**¿A qué conclusión se llegará?**

Datos: 15, 22, 18, 21, 20, 18, 17, 19, 21, 22, 18, 22, 18, 17, 16, 15, 14, 16, 18, 20, 15, 20, 18, 15, 16

$$H_o: \text{La muestra es aleatoria}$$
$$H_a: \text{La muestra no es aleatoria}$$

**Cálculos:**

- $n_1 = 9$
- $n_2 = 10$
- $R = 9$

$$\mu_R = 10.43$$

$$\sigma_R = 1.206$$

$$Z_o = \frac{R - \mu_R}{\sigma_R} = \frac{9 - 10.43}{1.206} = -1.18$$

**Valores críticos:** $Z_{0.025} = -1.96$, $Z_{0.975} = 1.96$

Como $-1.18$ **no está en la zona de rechazo** $\Rightarrow$ **No se rechaza $H_o$**:

**Los datos son aleatorios.**

---

## Slide 13 — Ejemplo rachas — Juego LA TINKA

Para comprobar si el juego de **LA TINKA** es aleatorio, se ha seleccionado 10 bolillas:

$$12, 16, 15, 40, 26, 17, 22, 26, 12, 34$$

Usando **5% de significación**, determine si se trata de un juego correcto.

$$H_o: \text{La muestra es aleatoria}$$
$$H_a: \text{La muestra no es aleatoria}$$

---

## Slide 14 — Prueba Kolmogorov-Smirnov (KS) — Introducción

Esta prueba permite determinar si los datos de una muestra **corresponden o no a una distribución normal**, con una media y una desviación dadas.

**Las hipótesis serán:**

$$H_o: \text{Las observaciones } \mathbf{se \ ajustan \ a \ una \ normal}$$
$$H_a: \text{Las observaciones } \mathbf{no \ se \ ajustan \ a \ una \ normal}$$

**Procedimiento:**

Se sugiere formar una tabla con las siguientes columnas:

- $X$: contiene las **observaciones diferentes** ordenadas de menor a mayor
- $f_i$: contiene las **frecuencias** de las observaciones
- $F_i$: es la **frecuencia absoluta acumulada**
- $F_S(X)$: son las **frecuencias relativas acumuladas** $(H_i = F_i/n)$
- $z = \frac{X - \mu}{\sigma}$: para cada dato, es cada punto **estandarizado**
- $F_T(X) = P(Z \leq z)$
- $D_1 = |F_T(X) - F_S(X)|$ y $D_2 = |F_T(X) - F_S(X_{i-1})|$ son las **mayores diferencias** de sus respectivas columnas

---

## Slide 15 — Prueba KS — Estadístico de prueba y decisión

**El estadístico de prueba es:**

$$D = \max(D_1, D_2)$$

El cual debe compararse con:

$$D_\alpha \text{ (valor crítico de Kolmogorov-Smirnov)}$$

**Siendo:**

$$n: \text{número de filas de la tabla construida}$$

**DECISIÓN:** Si $D < D_\alpha$ $\Rightarrow$ **no se rechaza $H_o$**

---

## Slide 16 — Prueba KS — Valores críticos (aparición de fórmulas F)

- Si se desea: $P(F(m, n) \geq q)$
- Si se desea: $P(F(m, n) \leq k)$

---

## Slide 17 — Ejemplo KS — Notas de Programación

**Ejemplo 1**

Las 12 notas siguientes fueron enviadas al director de carrera, en un curso de Programación.

Con **5% de significación**, **¿se puede afirmar que provienen de una distribución normal?**

```r
nfinal <- c(13.38, 12.69, 13.66, 16.46, 15.14, 17.21, 14.15, 16.06, 14.52, 11.92, 12.13, 14.56)
```

---

## Slide 18 — Prueba χ² de independencia — Introducción

El objetivo aquí es determinar si dos **variables categóricas** mantienen alguna relación (dependientes) o no se relacionan (independientes).

$$H_o: \text{Las dos variables son independientes}$$
$$H_a: \text{Las dos variables son dependientes}$$

**Procedimiento:**

Formar una tabla entre las dos variables con $m$ filas y $n$ columnas:

- $O_{ij}$: frecuencias observadas
- $TF_i$: total de fila $i$
- $TC_j$: total de columna $j$

| Filas / Columnas | $C_1$ | $\ldots$ | $C_n$ | TOTAL |
|---|---|---|---|---|
| $F_1$ | $O_{11}$ | $\ldots$ | $O_{1n}$ | $TF_1$ |
| $F_2$ | $O_{21}$ | $\ldots$ | $O_{2n}$ | $TF_2$ |
| $\ldots$ | $\ldots$ | $\ldots$ | $\ldots$ | $\ldots$ |
| $F_m$ | $O_{m1}$ | $\ldots$ | $O_{mn}$ | $TF_m$ |
| TOTAL | $TC_1$ | $\ldots$ | $TC_n$ | $N$ |

---

## Slide 19 — Prueba χ² — Frecuencias esperadas y estadístico

Se calcula las **frecuencias esperadas**:

$$E_{ij} = \frac{TF_i \cdot TC_j}{N}$$

| Filas / Columnas | $C_1$ | $\ldots$ | $C_n$ | TOTAL |
|---|---|---|---|---|
| $F_1$ | $O_{11} (E_{11})$ | $\ldots$ | $O_{1n} (E_{1n})$ | $TF_1$ |
| $F_2$ | $O_{21} (E_{21})$ | $\ldots$ | $O_{2n} (E_{2n})$ | $TF_2$ |
| $\ldots$ | $\ldots$ | $\ldots$ | $\ldots$ | $\ldots$ |
| $F_m$ | $O_{m1} (E_{m1})$ | $\ldots$ | $O_{mn} (E_{mn})$ | $TF_m$ |
| TOTAL | $TC_1$ | $\ldots$ | $TC_n$ | $N$ |

**Estadístico de prueba:**

$$\chi_o^2 = \sum_i \sum_j \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

**Región de rechazo de $H_o$:** es una gráfica de CHI cuadrado de cola derecha. Su valor crítico es:

$$\chi^2_{(1-\alpha; (m-1)(n-1))}$$

---

## Slide 20 — Prueba χ² de bondad de ajuste — Introducción

El objetivo es determinar si una muestra sigue o no una determinada **distribución de probabilidades**:

$$H_o: \text{La muestra sí sigue la distribución}$$
$$H_a: \text{La muestra no sigue la distribución}$$

**Procedimiento:**

Se construye una tabla con:

| $X_i$ | $O_i$ | $P_i$ | $E_i$ | CHI |
|---|---|---|---|---|
| $x_1$ | $O_1$ | $P_1$ | $E_1$ | $C_1$ |
| $:$ | $:$ | $:$ | $:$ | $:$ |
| $x_k$ | $O_k$ | $P_k$ | $E_k$ | $C_k$ |
| | $N$ | $1$ | $N$ | $\chi_o^2$ |

**Observaciones:**

- La **probabilidad $P_i$** se calcula asumiendo que $H_o$ es verdad.
- **Grados de libertad:** $g.l. = \text{número de filas} - \text{número de parámetros desconocidos} - 1$

En general:

$$g.l. = \text{(filas)} - \text{(parámetros desconocidos)} - 1$$

---

# S09 — Pruebas no paramétricas (Slides 21-31)

## Slide 21 — Ejemplo 1: Prueba de Kolmogorov-Smirnov para Normalidad

**Contexto:**

Las 12 notas siguientes fueron enviadas al director de carrera, en un curso de Programación. Con 5% de significación ¿Se puede afirmar que provienen de una distribución normal?

**Código R:**

```r
nfinal <- c(13.38, 12.69, 13.66, 16.46, 15.14, 17.21, 14.15, 16.06, 14.52, 11.92, 12.13, 14.56)
```

**Prueba de ks.test (Kolmogorov-Smirnov):**

```r
ks.test(nfinal, pnorm, mean(nfinal), sd(nfinal))
```

**Output:**

```
Exact one-sample Kolmogorov-Smirnov test

data: nfinal
D = 0.11087, p-value = 0.9946
alternative hypothesis: two-sided
```

**Conclusión:** p-valor = 0.9946 > α = 0.05 ⟹ No rechazamos $H_0$. Los datos sí provienen de una distribución normal.

---

## Slide 22 — Prueba de Independencia: Introducción

**Objetivo:**

Determinar si dos variables categóricas mantienen alguna relación (dependientes) o no se relacionan (independientes).

**Hipótesis:**

- $H_0$: las dos variables son independientes
- $H_a$: las dos variables son dependientes

**Construcción de la tabla de contingencia:**

Formar una tabla entre las dos variables con m filas y n columnas:

- $O_{ij}$ → frecuencias observadas
- $TF_i$ → total de fila i
- $TC_j$ → total de columna j

**Tabla general:**

| | Columnas | | | TOTAL |
|---|---|---|---|---|
| | | C1 | ... | Cn | |
| **Filas** | F1 | O11 | | O1n | TF1 |
| | F2 | O21 | | O2n | TF2 |
| | Fm | Om1 | | Omn | TFm |
| **TOTAL** | | TC1 | ... | Tn | N |

---

## Slide 23 — Prueba de Independencia: Fórmulas y Estadístico

**Cálculo de frecuencias esperadas:**

$$E_{ij} = \frac{TF_i \times TC_j}{N}$$

Ejemplo: $E_{23} = \frac{TF_2 \times TC_3}{N}$

**Tabla con frecuencias observadas y esperadas:**

| | Columnas | | | TOTAL |
|---|---|---|---|---|
| | | C1 | ... | Cn | |
| **Filas** | F1 | O11 (E11) | | O1n (E1n) | TF1 |
| | F2 | O21 (E21) | | O2n (E2n) | TF2 |
| | Fm | Om1 (Em1) | | Omn (Emn) | TFm |
| **TOTAL** | | TC1 | ... | TCn | N |

**Estadístico de prueba:**

$$\chi^2_o = \sum_i \sum_j \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

**Región de rechazo de $H_0$:**

Es una gráfica de chi-cuadrado de cola derecha. Su valor crítico es:

$$\chi^2_{(1-\alpha; (m-1) \times (n-1))}$$

**Grados de libertad:** $(m-1) \times (n-1)$

---

## Slide 24 — Ejemplo 1 (full R): Independencia de Destino y Servicio

**Problema:**

Utilizando la base de datos del parcial "DatosBuses.csv" y con 5% de significación, compruebe si las variables Destino y Servicio son o no independientes.

**Hipótesis:**

- $H_0$: Destino y Servicio son independientes (no hay relación)
- $H_a$: Destino y Servicio son dependientes (sí hay relación)

**Lectura de datos:**

```r
DB <- read.csv("DatosBuses.csv")
DB
```

**Construcción de tabla de contingencia:**

```r
tab <- table(DB$Destino, DB$Servicio)
tab
```

**Tabla obtenida:**

| Destino | Crucero | Suite | Crucero Tour | Perú | Imperial | Tour Perú |
|---|---|---|---|---|---|---|
| Centro | 11 | 8 | 15 | 14 |
| Norte | 14.045 | 18.285 | 20.67 |
| Oriente | 21.730 | 28.290 | 31.98 |
| Sur | 15.370 | 26.010 | 22.62 |

**Aquí se tiene:** m = 4 filas y n = 3 columnas

**Obtención de valores esperados:**

```r
chisq.test(tab)$expected  # Ver valores esperados en la tabla cruzada
```

**Output — Valores esperados:**

```
Warning: Chi-squared approximation may be incorrect

                    Crucero Suite Crucero Tour Perú Imperial Tour Perú
Centro              14.045        18.285       20.67
Norte               14.045        18.285       20.67
Oriente             21.730        28.290       31.98
Sur                 15.370        20.010       22.62
```

**Obtención del estadístico de prueba:**

```r
chisq.test(tab)  # estadístico y p-valor
```

**Output:**

```
Pearson's Chi-squared test

data: tab
X-squared = 6.1176, df = 6, p-value = 0.4101
```

**Conclusión:** p-valor = 0.4101 > α = 0.05 ⟹ No rechazamos $H_0$. Las variables Destino y Servicio son independientes.

---

## Slide 25 — Ejemplo (Sin R)

Determine con 10% de significación si el Sexo de los estudiantes influye en la nota final del curso. Use la información siguiente:

| Notas | Sexo H | Sexo M | TOTAL |
|-------|--------|--------|-------|
| [11;14] | 30 (26) | 20 (22) | TF1: 50 |
| [15;18] | 80 (72.8) | 60 (67.2) | TF2: 140 |
| [19;20] | 20 (31.2) | 40 (28.8) | TF3: 60 |
| **TOTAL** | TC1 = 130 | TC2 = 120 | N = 250 |

$H_0$: Sexo y Nota son Indep. · $H_a$: Sexo y Nota son depend. · $\alpha = 0.10$

$$E_{ij} = \frac{TF_i \times TC_j}{N}, \quad E_{11} = \frac{50 \times 130}{250} = 26, \quad E_{12} = \frac{50 \times 120}{250} = 24$$

$$\chi^2_0 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}} = 32.475 \quad ; \quad g.l. = (\#f-1)(\#c-1) = 2 \times 2 = 4 \quad ; \quad \chi^2_{(1-\alpha,4)} = 7.77$$

Como $\chi^2_0 \in$ región de rechazo $\Rightarrow$ se rechaza $H_0$: Sexo y Notas sí dependientes.

**Figura:** Curva chi-cuadrado sesgada a la derecha con la región de rechazo sombreada en la cola derecha ($\alpha=0.10$) y el valor crítico $\chi^2_{(1-\alpha,4)}=7.77$ en el eje.

## Slide 26 — Ejemplo (Sin R)

**Título:** Ejemplo (Sin R)

Determine con 10% de significación si el Sexo de los estudiantes influye en la nota final del curso. Use la información siguiente:

α = 0.10

$$H_0: \text{Sexo y Nota son independientes (no influye)}$$
$$H_a: \text{Sexo y Nota son dependientes (si influye)}$$

| | **Sexo** | | TOTAL |
|---|---|---|---|
| | H | M | |
| **Notas** [11;14] | 30 (26) | 20 (22) | TF=50 |
| [15;18] | 80 (72.8) | 60 (67.2) | TF=140 |
| [19;20] | 20 (31.2) | 40 (28.8) | TF=60 |
| **TOTAL** | TC₁= 130 | TC₂= 120 | N=250 |

**Cálculo de frecuencias esperadas:**

$$E_{ij} = \frac{TF_i \times TC_j}{N}$$

$$E_{11} = \frac{TF_1 \times TC_1}{N} = \frac{50 \times 130}{250} = 26$$

$$E_{12} = \frac{TF_1 \times TC_2}{N} = \frac{50 \times 120}{250} = 24$$

**Estadístico de prueba:**

$$\chi^2_o = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}} = \frac{(30-26)^2}{26} + \frac{(20-22)^2}{22} + \frac{(80-72.8)^2}{72.8} + \frac{(60-67.2)^2}{67.2} + \frac{(20-31.2)^2}{31.2} + \frac{(40-28.8)^2}{28.8}$$

$$\chi^2_o = 22.495 \text{ (Estadística de prueba)}$$

**Grados de libertad:**

$$\text{g.l.} = (m-1) \times (n-1) = 2 \times 2 = 4$$

**Valor crítico:**

$$\chi^2_{(0.90, 4)} = 7.77$$

**Gráfica:** Distribución chi-cuadrado con cola derecha α = 0.10, región de rechazo sombreada.

**Conclusión:** Como χ² ∈ Región Sombreada ⇒ Rechazo H₀ ⇒ luego Sexo y Nota son dependientes.

---

## Slide 27 — PRUEBA DE BONDAD DE AJUSTE

**Objetivo:** Determinar si una muestra sigue o no una determinada distribución de probabilidades.

$$H_o: \text{la muestra sí sigue la distribución}$$
$$H_a: \text{la muestra no sigue la distribución}$$

**Estructura de la tabla:**

| Xi | Oi | Pi | Ei | CHI |
|---|---|---|---|---|
| x1 | O1 | P1 | E1 | C1 |
| : | : | : | : | : |
| xk | Ok | Pk | Ek | Ck |
| | N | 1 | N | χ²o |

**Notas:**
- Crear una tabla: variable, valores observados (frecuencias), P(Xi), esperados ➔ Ei = N*Pi
- La probabilidad Pi se calcula asumiendo que Ho es verdad.

**Fórmula del estadístico:**

$$\chi^2_o = \sum_i \frac{(O_i - E_i)^2}{E_i}$$

**Grados de libertad:**

$$\text{g.l.} = \# \text{filas} - \# \text{parámetros desconocidos} - 1$$

---

## Slide 28 — Ejemplo (Prueba del dado)

**Título:** Ejemplo

Se desea determinar si un dado esta o no correcto. Para ello se prueba lanzando 60 veces el dado y se anota los números obtenidos. Use 10% de significación y los datos siguientes:

**Hipótesis:**

$$H_o: \text{El dado es correcto} \left(P = \frac{1}{6}\right)$$
$$H_a: \text{El dado no es correcto}$$

**Tabla de datos:**

| Xi | Oi | Pi | Ei = N*Pi | CHI = (O-E)²/E |
|---|---|---|---|---|
| 1 | 6 | 1/6 | 10 | 1.6 |
| 2 | 10 | 1/6 | 10 | 0 |
| 3 | 12 | 1/6 | 10 | 0.4 |
| 4 | 13 | 1/6 | 10 | 0.9 |
| 5 | 11 | 1/6 | 10 | 0.1 |
| 6 | 8 | 1/6 | 10 | 0.4 |
| | N=60 | 1 | 60 | χ²o = 3.4 |

**Grados de libertad:**

$$\text{g.l.} = \# \text{filas} - 1 = 5$$

**Valor crítico:**

$$\chi^2_{(0.9, 5)} = 9.23$$

**Gráfica:** Distribución chi-cuadrado con α = 0.10, región de rechazo sombreada a la derecha.

**Conclusión:** χ²o = 3.4 ∉ Región Sombreada ⇒ No Rechazo H₀ ⇒ el dado está correcto.

---

## Slide 29 — Ejemplo (Supermercado de peras)

**Título:** Ejemplo

Se realizó un estudio en un supermercado muy conocido que consistió en evaluar 600 bolsas de peras, cada una de las bolsas contiene 3 peras de las cuales algunas se encuentran en buen estado y otras en mal estado. Los resultados al evaluar 600 bolsas son los siguientes:

| Número de peras en mal estado por bolsa | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Frecuencia (Número de bolsas) | 300 | 150 | 100 | 50 |

Use nivel de significación del 5% y determine si el # de peras falladas es Binomial. Calcule su p-valor.

---

## Slide 30 — Ejemplo (Continuación - Cálculos con distribución Binomial)

**Tabla de datos:**

| Número de peras en mal estado por bolsa | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Frecuencia (Número de bolsas) | 300 | 150 | 100 | 50 |

**Hipótesis:**

$$H_o: \text{Los datos sí siguen una binomial}$$
$$H_a: \text{Los datos no siguen la binomial}$$

**Binomial requiere n y P:**

$$n = 3, \quad P = P(\text{malgrade}) = ?$$

**Cálculo de p:**

$$\text{Para Binomial: } E(X) = n \cdot p$$
$$n \cdot p = \frac{1}{N}\left(\sum x_i \cdot O_i\right)$$
$$n \cdot p = \frac{0 \times 300 + 1 \times 150 + 2 \times 100 + 3 \times 50}{600} = \frac{600}{600} = 1$$
$$p = \frac{1}{3} = 0.2977$$

**Cálculo de probabilidades con binomial:**

```r
P<- dbinom(0:3, 3, po)
P
sum(P)
```

**Resultado:**

```
[1] 0.37671468  0.43467078  0.16718107  0.02143347
[1] 1
```

**Tabla de cálculos:**

| Xi | Oi | Pi | Ei | CHI |
|---|---|---|---|---|
| 0 | 300 | 0.3967 | 226.020 | |
| 1 | 150 | 0.3967 | 260.807 | |
| 2 | 100 | 0.1672 | 100.308 | |
| 3 | 50 | 0.0214 | 12.861 | |
| | N=600 | 1 | 600 | |

**Cálculo de frecuencias esperadas:**

```r
E<- 600*P
E
sum(E)
```

**Resultado:**

```
[1] 226.02881  260.80247  100.30864  12.86008
[1] 600
```

**Contribución a chi:**

```r
Chi<- (0-E)*(0-E)/E
Chi
```

**Resultado:**

```
[1] 2.420814e+01  4.707466e+01  9.496676e-04  1.072601e+02
```

**Estadístico:**

```r
CHI0<- sum(Chi)
CHI0
```

**Resultado:**

```
[1] 178.5438
```

**Grados de libertad:**

$$\text{g.l.} = 4 - 1 - 1 = 2$$

**Conclusión:** 

$$H_o: \text{Los datos sí siguen una binomial}$$
$$H_a: \text{Los datos no siguen la binomial}$$

$$\alpha = 0.05$$

$$\chi^2_{(0.95, 2)} = 6$$

Como χ² ∉ Región Sombreada ⇒ Rechazo H₀ ⇒ No sigue una binomial

---

## Slide 31 — Ejemplo (Variables X y Y)

**Título:** Ejemplo

Una variable X toma 3 valores, mientras que la variable Y toma 2 valores. Se ha realizado el experimento de relacionar los valores de ambas variables, obteniéndose la siguiente tabla de frecuencias.
Use 5% y determine si las variables tienen alguna relación.
Halle su p-valor.

**Tabla de datos:**

| | Y1 | Y2 | |
|---|---|---|---|
| X1 | 120 | 80 | |
| X2 | 70 | 80 | |
| X3 | 130 | 120 | |
| | | | |
