---
curso: EST
titulo: Regresión
slides: 706
fuente: Regresión.qmd
---

# Regresión

## Índice

Material Quarto/R del curso (código + prosa). Ingesta directa sin transcripción (ya es markdown).

## Quarto

Quarto enables you to weave together content and executable code into a finished document. To learn more about Quarto see <https://quarto.org>.

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

```{r}
library(readr)
library(plyr)
library(dplyr)
library(tidyr)
library(tidyverse)
library(ggplot2)
```

# *REGRESIÓN LINEAL*

Objetivo: Relacionar variables independientes (Xi) con una variable dependiente (Y)

Ejemplo:

-   Cantidad de horas en el Gym : X1

-   Nota en el examen final : Y

-   Horas de estudio : X2

-   Horas que paso chateando en WhatsApp: X3

    Al final se va a obtener que Y está relacionada por una ecuación de la forma siguiente:

    $$
    Y=\beta_{0}+\beta_{1}*X1+\beta_{2}*X2+\beta_{3}*X3
    $$

Aquí se tiene que la variable Y depende de 3 variables Xi ==\> el modelo se llamara *Regresión múltiple.*

*Regresión simple :* Y depende de una sola X.

Se llama Lineal, porque las ecuaciones que se van a obtener solo contienen exponentes 1.

**Modelos:**

Regresión simple:

$$
Y=\beta_{o}+\beta_{1}.X1
$$

Regresión múltiple:

$$
Y=\beta_{o}+\beta_{1}.X1+\beta_{2}.X2+...+\beta_{k}.Xk
$$

-   Los betas con sub indice mayor o igual que 1, se llaman *coeficientes de regresión.*

-   Beta con sub indice CERO, se llama termino independiente o término constante.

Ejemplo teórico: "Rústica S.A." es una empresa dedicada a la remodelación de casonas históricas. Ellos saben que lo van a cobrar (Y) depende de la *nómina local de la casona* (valor tasado de la casona)

```{r}
#datos:
x1<- c(3,4,6,4,2,5)  # Nómina local de la casona que está en reparación.Unidades de cien mil dólares
y1<- c(6,8,9,5,4.5,9.5) # Valor que cobra la empresa que hace la reparación de casonas.Unidades de cien mil soles.
```

Graficando un "diagrama de dispersión"

```{r}
pairs(x1~y1)
```

-   En el eje Y, debe ir la variable dependiente.
-   En el eje X, debe ir la variable independiente.

La gráfica adecuada sería la que está abajo a la izquierda.

Se observa que hay una tendencia creciente ( a medida que X aumenta, entonces Y tambien aumenta)

También se puede obtener la gráfica así:

```{r}
plot(x1,y1) # aquí primero se coloca X, luego se coloca Y. la que se coloca primero irá en eje X, la otra va al eje Y.
```

**Covarianza:** Indica una medida de la tendencia lineal entre las variables . Mientras mas pequeño sea este valor, significará que hay poca relacional lineal. Mientras mas alto sea este valor la relación lineal es mas fuerte.

**Si es (+)** la linealidad es de izquierda a derecha: creciente (subida).

**Si es (-)** la linealidad es de izquierda a derecha: decreciente (bajada).

**Si es CERO** ==\> no hay relación lineal.

```{r}
cov(x1,y1)
```

$$
-\infty<Cov(X,Y)<\infty
$$

Como la covarianza es +2.5 (positivo) significa que hay una **tendencia creciente** de izquierda a derecha. *Pero no se sabe si esta relación es buena o mala.*

En general:

Si la covarianza es (+) entonces hay una relación creciente ( "a medida que X aumenta, entonces Y aumenta").

Si la covarianza es (-) entonces hay una relación decreciente ("a medida que X aumenta entonces Y disminuye").

Mas exactitud es con el ***coeficiente de correlación.***

**Correlación (r) para una regresión simple:**

$$
cor=r=\frac{Cov(X,Y)}{S(X)*S(Y)}
$$

```{r}
r<-cor(x1,y1)
r
```

-   En general se cumple: $-1\le r \le 1$

-   si \|r\|\>0.75 ==\> la relación lineal es buena.

-   si \|r\|\<0.75 ==\> la relación lineal es mala.

-   si r=0 ==\> No hay relación lineal

-   mientras mas cerca este de cero, la relación será mala.

*Interpretación:* Como r= 0.83333 \> 0.75 entonces la relación lineal es buena y es directa (creciente) (a medida que x crece, entonces y también crece) lo cual tiene sentido, pues si mas cuesta la casona, entonces la empresa cobrar mas.

En general r se interpreta así:

1\) si r=1 ==\> existe relación lineal directa (creciente) y perfecta.

2\) si r= -1 ==\> existe una relación lineal inversa (decreciente) y perfecta.

3\) si \|r\| \> 0.75 ==\> la relación lineal es buena ( y se puede hacer predicciones)

4\) si \|r\| \< 0.75 ==\> la relación lineal es mala (no sería confiable las predicciones que se hacen)

5\) si r=0 ==\> no hay una relación lineal. Podría haber otro tipo de relación: cuadrática, logaritmica, logística, exponencial, etc.

**AHORA HALLEMOS LA ECUACIÓN DE REGRESIÓN:**

1°) Transformamos los datos de los vectores, a un data frame

```{r}
datosreg<-data.frame("X1"=x1,"Y1"=y1)
datosreg
```

2°) Ahora hallamos el reporte de regresión, usando *lm* (linear models)

```{r}
resultados<- lm(datosreg$Y1 ~ datosreg$X1)   # primero debe ir Y1 y luego X1 
resultados
summary(resultados)
```

Obteniendo información del reporte anterior. $\beta_{0}=2$, $\beta_{1}=1.25$

ECUACIÓN DE REGRESIÓN.

$$
\hat{y}=2+1.25*x
$$

$$
x: \text{valor real de la variable X}.\\
y: \text{valor real de la variable y}. \\
\hat{y}: \text{valor estimado de Y, por la ecuación de regresión }.
$$

$\beta_{0}$ es la intersección de la recta con el eje Y.

$\beta_{1}$ es la pendiente de la recta:

De izquierda a derecha:

Si pendiente\>0 ==\> la recta sube.

Si pendiente\<0 ==\> la recta baja.

**NOTA:** signo de Covarianza = Signo de r = Signo de $\beta_{1}$

En general la ecuación será: $$\hat{Y}=\beta_0 + \beta_1*X$$

Reemplazando valores:\
La ecuación de regresión estimada será:

$$
\hat{Y}=2+1.25*X1
$$

**COEFICIENTE DE DETERMINACIÓN:**

Es un coeficiente que te indica *el grado de colinealidad* de los datos, con respecto a la recta de regresión:

$$
\text{Coeficiente de determinación}= R^2\text{%}= (r^2)\cdot 100\text{%}
$$

Su interpretación:

**"El** $r^2$ **% de las variaciones de Y son explicadas por las variaciones de X o del modelo de regresión."**

Para el ejemplo, sería:

```{r}
coef_det <-(r^2)*100
coef_det
```

```         
```

El 69.44% de las variaciones en el cobro de la empresa que remodela, son explicados por las variaciones en la nómina local.

o también:

El 69.44% de las variaciones en el costo de remodelación es explicado por el modelo de regresión.

**NOTA:** cuando el ***coeficiente de determinación*** pasa de 50% , la relación lineal es buena.

**NOTA:**

En regresión simple: $|r|=\sqrt{R^2}$

Puede salir r, *positivo o negativo.* Pero el signo correcto de r es el mismo signo de $\beta_{1}$

3°) Graficamos el diagrama de dispersión y la recta de regresión:

```{r}
plot(datosreg$X1,datosreg$Y1,xlab="X1",ylab="Y1")
abline(resultados)   
```

No creer que en la imagen anterior, la recta viene del origen de coordenadas.\
En realidad la recta pasa por el punto (0;2).,

Hallando los errores : $e_{i}= Y_{i} - \hat{Y}_{i}$

**Es decir:** Error = Valor real de Y - Valor estimado de Y.

```{r}
x1<- c(3,4,6,4,2,5)  # valores reales de X
"x1"
x1
y1<- c(6,8,9,5,4.5,9.5)    # valores reales de Y
"y1"
y1
ye<- 2+1.25*x1       # Y estimados ( lo que se calcula con la ecuación de recta de regresión)
"ye"
ye
ei<- y1-ye           # errores = Y real - Y estimado
"ei"
ei
```

**NOTA:**

La suma de los errores da CERO.

Un dato real es Yi (obtenido mediante encuesta o mediciones).

Un dato estimado es Ye (obtenido reemplazando X real en la ecuación de regresión: Ye=bo+ b1\*X)

==\> ERROR DE ESTIMACIÓN: ei= Yi - Ye

Los errores de estimación deben de cumplir 3 condiciones:

1\) Deben ser independientes.

2\) Deben tener distribución normal.

3\) Deben tener igual varianza.

# ANÁLISIS DE ERRORES.

1\) **Analizando la independencia de los residuos (errores )**

```{r}
# install.packages("lmtest")
```

luego:

```{r}
library(lmtest)
```

**Test de Durwin Watson para probar la independencia de los errores:**

Se va a probar:

*Ho: Los errores son independientes( no hay relación)*

*Ha: Los errores son dependientes (hay relación)*

```{r}
dwtest(resultados,alternative ="two.sided",iterations = 1000)
# resultados es lo que se obtuvo en un CHUNK de mas arriba, al usar lm.
# siempre se pondrá " two.sided".
```

Como el estadístico de prueba **DW=1.5455 está *entre 1.5 y 2.5*** se acepta Ho , es decir, los errores son independientes.

*En general siempre que DW esté entre 1.5 y 2.5 **se aceptará Ho.***

Tambien: *P-valor= 0.6733 \> alfa=0.05* ==\> **No rechazo Ho: son independientes.**

################################################################## 

2)  ***test de normalidad***

    Ho: los errores son normales **con media CERO**

    Ha: los errores no son normales con media cero.

```{r}
mean(ei)  # media de los errores
sd(ei)    # desviación de los errores
# los errores ya están calculados en un CHUNK de mas arriba.
```

test de Kolmogorov Smirnov

```{r}
ks.test(ei,mean(ei),sd(ei))
```

P-valor=1 \>alfa=0.05 ==\>\> No rechazo ho ==\>Acepto Ho ==\> "Los errores son normales con media CERO"

3)  **la homocedasticidad (varianzas iguales)**

*Prueba de Breusch--Pagan*: (*requiere library(lmtest)*) se va a probar:

*Ho: las varianzas de los errores es constante o son iguales (homocedasticidad)*

*Ha: las varianzas de los errores no es constante (heterocedasticidad)*

```{r}
bptest(lm(y1~x1))
```

como p valor es mayor que ALFA= 0.05 ==\> no rechazo Ho: Acepto Ho ==\> si hay homocedasticidad (las varianzas son iguales).

**Conclusión:** Al pasar las tres pruebas se está validando los cálculos anteriores:

Correlación, la ecuación de regresión, coeficiente de determinación ==\> todo ello está correcto.

Los errores a data frame

```{r}
estimaciones<-data.frame("X1"=x1,"Y1"=y1,"Y-estimado"=ye,"errores"=ei)
estimaciones
```

######################################################################################### 

**Ejemplo:**

Hacer todo un análisis de regresión para el *data frame **cars***

```{r}
cars
```

Cars contiene datos de velocidad de vehículos y la distancia de frenado

Notamos que la distancia depende de velocidades.\
consideramos que **x= velocidad** (variable independiente), **y=distancia** (variable dependiente) Su diagrama de dispersión:

```{r}
pairs(cars$dist~cars$speed, data=cars)
```

Tambien:

```{r}
plot(cars$speed, cars$dist)  # en PLOT primero se escribe X, luego va Y.
```

Covarianza:

```{r}
cov(cars$speed, cars$dist)
```

Como es positiva significa que habrá una relación lineal ascendente de izquierda a derecha. Relación directa.

Coeficiente de correlación:

```{r}
cor(cars$dist,cars$speed)
```

r=0.80689 es mayor que 0.75 ==\> la velocidad y la distancia del móvil se relacionan aceptablemente en forma directa ( a medida que uno crece, la otra variable también crece).

```{r}
modelo<-lm(cars$dist~cars$speed, data=cars)  # obligatorio aqui: primero Y, luego X
summary(modelo)
anova(modelo)
```

***Beta 0= bo= -17.5791***

***Beta 1= b1=3.9324***

**Interpretaciones:**

x= velocidad en *m/seg*

y= distancia en *m.*

**Beta 0:** **"Cuando X=0, se tendrá que Y= b0"** .Cuando la velocidad es CERO, la distancia de frenado es -17.5791. Es decir, cuando la velocidad es cero, la distancia es nula.

**Beta 1: " Por cada unidad de aumento en X1, la variable Y varía (aumenta o disminuye) en promedio en beta 1 unidades".**

Por cada 1metro/ seg que aumenta la velocidad, la distancia aumentará en promedio en 3.9324 metros.

Ecuación de regresión: ***y= -17.5791+3.9324(x) + ei***, Y estimado: **Ye= -17.5791+3.9324(x)**

&&&&&&&&&&&&&&&&&&&&&&&&

Ustedes deben probar los tres supuestos para los errores.

&&&&&&&&&&&&&&&&&&&&&&&

**PRUEBAS DE HIPÓTESIS.**

Del reporte anterior:

**1) Prueba de significancia de coeficientes:**

***Prueba de BETA 0:***

**Ho:** $\beta_o$ *= 0* ( no significativo o no apropiado)

**Ha:** $\beta_o \ne 0$ *0* ( significativo o apropiado)

*P valor de Beta 0 = 0.0123* \< alfa= 0.05 ==\> **Rechazo Ho:** Beta 0 es diferente de cero ==\> es significativo.

***Prueba de BETA 1:***

**Ho:** Beta 1= 0 ( no significativo)

**Ha:** Beta 1 diferente de 0 (significativo)

P valor aprox de Beta 1= 0 \< alfa=0.05 ==\> **rechazo Ho** ==\> Beta1 es diferente de cero ==\> es significativo.

**NOTA:** El p valor mas pequeño de los coeficientes significativos, indica al *coeficiente mas significativo.*

En el ejemplo de CARS, el mas significativo es $\beta_{1}.$

**2) Prueba de significancia de todo el modelo:**

**Ho:** modelo no significativo ( no apropiado)\
**Ha:** modelo significativo ( apropiado o adecuado)

En el ejemplo de CARS, se ha obtenido al final del reporte de *lm*:

```         
F-statistic: 89.57 on 1 and 48 DF,  p-value: 1.49e-12
```

P valor aprox es 0 \< alfa ==\> modelo significativo ==\> es un modelo apropiado.

## 

**3) Prueba general de coeficientes:** *Continuando de CARS.*\
a) *¿Se puede afirmar que por cada 1 metro / seg, que se aumenta a la velocidad del móvil, la distancia se incrementará en promedio **en 4 metros**? ==\> ¿Beta 1 =4?*

*b) ¿Se puede afirmar que por cada 1 metro / seg, que se aumenta a la velocidad del móvil, la distancia se incrementará en promedio **en menos de 4 metros**? ==\> ¿Beta 1 \< 4?*

*c) ¿Se puede afirmar que por cada 1 metro / seg, que se aumenta a la velocidad del móvil, la distancia se incrementará en promedio **en mas de 4 metros**? ==\> ¿Beta 1 \> 4?*

**SOLUCIÓN (C)**

*Prueba general:*\
**Ho:** Beta 1 \< = 4\
**Ha:** Beta 1 \> 4 (esto es lo que se está preguntando)

Del Word:\
Se rechazará Ho si:

$$
T_{\beta1}>t(1-\alpha, n-k-1)
$$\
siendo: $$T(\beta_1)=\frac{\beta_1 - b}{SE(\beta_1)}$$

En el problema, el estadístico de prueba es:\
$$T(\beta_1)=\frac{3.9324  - 4}{0.4155}=-0.1626$$

Valor crítico: n=50, k=1, alfa=0.05\
$$t(1-\alpha, n-k-1)=t(0.95, 48)$$

```{r}
qt(0.95,48)
```

Como se está probando en Ha: \> entonces la región crítica está sombreada por el lado derecho, a partir del valor crítico: 1.677224

Como el Estadístico de prueba es (-) , no está a la derecha del valor crítico y por ello, No rechazo Ho ==\>Acepto Ho: Es decir, *Beta1 no puede ser mayor de 4.*

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Gráfico de la regresión de CARS:

```{r}
plot(cars$speed,cars$dist, xlab="X",ylab="Y")
abline(modelo)
# modelo, es el reporte obtenido con lm
```

**Del reporte de regresion tomamos este fragmento:**

```         
Residual standard error: 15.38 on 48 degrees of freedom
Multiple R-squared:  0.6511,    Adjusted R-squared:  0.6438 
F-statistic: 89.57 on 1 and 48 DF,  p-value: 1.49e-12
```

**COEFICIENTE DE DETERMINACIÓN:** En un modelo de regresión simple (una sola X) $$R^2 \text{%}=(\text{coeficiente de correlación})^2*\text{100%}$$

Este coeficiente indica que porcentaje de las variaciones de Y, son explicadas por las variaciones del modelo o por las variaciones de las X.

En el ejemplo de CARS:

*Multiple R-squared: 0.6511*\
R\^2= 0.6511 equivale a 65.11% ==\> *"el 65.11% de las variaciones de las Distancias recorridas (Y) son explicadas por el modelo de regresión"*\

Coeficiente de correlación: $r=+ - \sqrt{R^2}$ ...en regresión simple (una sola X)

R\^2 sin porcentaje.

==\> $r=+- \sqrt{0.6511}=+-0.807$

Propiedad:

$$
\text{signo de r = signo de  } \beta_{1}
$$

Luego: $r= +0.807 > 0.75$ El modelo es bueno.

data frame

```{r}
datoscars<- data.frame("X"=cars$speed, "Y"=cars$dist,"Y-est"=-17.5791+3.9324*cars$speed, "e"=cars$dist-(-17.5791+3.9324*cars$speed))
datoscars
```

################################################################################################## 

comprobando los supuestos:

1\) Independencia de los errores:

*Ho: Los errores son independientes*

*Ha: los errores son dependientes*

```{r}
dwtest(modelo,alternative ="two.sided",iterations = 1000)
```

como el estadístico DW está *entre 1.5 y 2.5* entonces los residuos son independientes.

o tambien con Pvalor =0.1904 \> alfa=0.05 ==\> No rechazas Ho: Son independientes.

2)  test de normalidad:

```{r}
mean(datoscars$e)
sd(datoscars$e)
```

test de Kolmogorov-Smirnov

*Ho: Los errores son normales con media cero*

*Ha: los errores no son normales con media cero*

```{r}
ks.test(datoscars$e,mean(datoscars$e),sd(datoscars$e))
```

Como p-valor =0.9412 \> Alfa=0.05 ==\> Acepto Ho: Con 5% de significación puede afirmarse que los errores son normales con media cero.

3)  la homocedasticidad:

*Ho: los errores tienen una varianza constante*

*Ha: los errores no tienen varianza constante.*

Prueba de Breusch--Pagan: (requiere library(lmtest))

```{r}
bptest(lm(cars$dist~cars$speed))
```

Como *p-valor = 0.07297 \> alfa= 0.05* ==\> acepto Ho: los errores tienen una varianza constante.

hasta aqui el quiz 5.

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

Regresión múltiple:

```{r}
library(readr)
library(plyr)
library(dplyr)
library(tidyr)
library(tidyverse)
library(ggplot2)

```

descargamos un data.frame de R:

```{r}
trees  # árboles
```

datos de árboles:

Girth ==\> circunferencia del tronco del arbol (X1)

Height ==\> altura del tronco (X2)

Volume ==\> volumen del tronco (Y)

k=2 (dos variables X)

n=31 observaciones

```{r}
anovamult<-lm(trees$Volume~trees$Girth+trees$Height, data=trees)
anovamult
summary(anovamult)
anova(anovamult)
```

El modelo obtenido es:

```         
Coefficients: 
(Intercept)   trees$Girth  trees$Height  
-57.9877        4.7082        0.3393  
```

$$
\beta_{0}=-57.9877\\
\beta_{1}=4.7082 \\
\beta_{2}=0.3393
$$

$$
y=-57.9877+4.7082*X1+0.3393*X2
$$

-   ¿El modelo es adecuado?

    Ho: Modelo no adecuado (no significativo)

    Ha: Modelo adecuado (significativo)

    Del reporte:

    ```         
    F-statistic (Fo): 255 on 2 and 28 DF,  p-value: < 2.2e-16
    ```

Como Pvalor es aproximado a cero \< alfa = 0.05 ==\> Rechazo Ho: Modelo adecuado.

Pero:

-   ¿Todos los coeficientes son adecuados?

```         
              Estimate  Std. Error  t value  Pr(>|t|)    
(Intercept)  -57.9877     8.6382     -6.713   2.75e-07 ***
trees$Girth    4.7082     0.2643     17.816    < 2e-16 *** 
trees$Height   0.3393     0.1302     2.607     0.0145 * 
```

Para Bo: Pvalor= (\*\*\*) aproximado a cero \<alfa ==\> rechazo Ho: Si es significativo.

Para B1: Pvalor= (\*\*\*) aproximado a cero \<alfa ==\> rechazo Ho: Si es significativo.

Para B2: Pvalor= 0.0145 \<alfa = 0.05 ==\> rechazo Ho: Si es significativo.

Todos los coeficientes son significativos es decir son apropiados con alfa = 5%.

CORRELACION:

```{r}
cor(trees)
```
