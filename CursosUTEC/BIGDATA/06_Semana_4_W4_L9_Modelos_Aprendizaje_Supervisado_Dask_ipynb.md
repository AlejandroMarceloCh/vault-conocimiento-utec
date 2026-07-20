---
curso: BIGDATA
titulo: 06 - Semana 4/W4 L9 Modelos_Aprendizaje_Supervisado_Dask
slides: 0
fuente: 06 - Semana 4/W4 L9 Modelos_Aprendizaje_Supervisado_Dask.ipynb
---

<div class="cell markdown" id="I5ZUSFpTHjxD">

# Modelos de Aprendizaje Supervisado en **Dask**

</div>

<div class="cell markdown" id="saqZepBrHm3m">

Curso: Big Data - UTEC

Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="38cASPf0HfXn">

``` python
# !pip install dask-ml
```

</div>

<div class="cell code" id="zsZnxqAhKK5s">

``` python
import dask.array as da
```

</div>

<div class="cell markdown" id="DydJI80U10GX">

## LogisticRegression

</div>

<div class="cell code" id="4tcQwy9xIATJ">

``` python
from dask_ml.linear_model import LogisticRegression
from dask_ml.datasets import make_classification
from dask_ml.metrics import accuracy_score
```

</div>

<div class="cell code" id="RYVLUlfzIAWr">

``` python
# Crear datos sintéticos (dask.array)
X, y = make_classification(n_samples=10000, n_features=10, chunks=1000, random_state=123)
```

</div>

<div class="cell code" id="iQw4okH8IdSQ">

``` python
X.compute()
```

</div>

<div class="cell code" id="qALVS-slIflX">

``` python
y.compute()
```

</div>

<div class="cell code" id="_zS2ocalIAZl">

``` python
# Crear y entrenar modelo
model = LogisticRegression()
model.fit(X, y)
```

</div>

<div class="cell code" id="RIh4hc96IAcp">

``` python
# Predicción
y_pred = model.predict(X).astype("int")
```

</div>

<div class="cell code" id="fu8nCXwfIAff">

``` python
# Ver resultados
print(y_pred.compute()[:10])
```

</div>

<div class="cell code" id="Wc27fMiULC83">

``` python
# Métricas
acc = accuracy_score(y, y_pred)

print("Logistic Regression:")
print("Accuracy:", acc)
```

</div>

<div class="cell markdown" id="-ACjKXE0KB7w">

## LinearRegression

</div>

<div class="cell code" id="ljc-aWQ_JqLm">

``` python
from dask_ml.linear_model import LinearRegression
from dask_ml.metrics import mean_squared_error, r2_score
```

</div>

<div class="cell code" id="LxiC-hQ4IAlQ">

``` python
# Crear datos sintéticos
X = da.random.random((10000, 3), chunks=1000)
coef = da.array([1.5, -2.0, 0.5])
y = X @ coef + 1.0 + da.random.normal(0, 0.1, size=10000, chunks=1000)
```

</div>

<div class="cell code" id="xv_BjMwPIAoR">

``` python
# Entrenar modelo
lr = LinearRegression()
lr.fit(X, y)
```

</div>

<div class="cell code" id="gkxBj5USJtt4">

``` python
# Ver coeficientes
print("Coeficientes:", lr.coef_)
print("Intercepto:", lr.intercept_)
```

</div>

<div class="cell code" id="KNvcU8XBIAqb">

``` python
# Predicciones
y_pred = lr.predict(X)
```

</div>

<div class="cell code" id="UKDPemp0MBqi">

``` python
y.compute()
```

</div>

<div class="cell code" id="T_iTC4xEL9qQ">

``` python
y_pred.compute()
```

</div>

<div class="cell code" id="8eoDyebgLgX-">

``` python
# Métricas
mse = mean_squared_error(y, y_pred)

print("Linear Regression:")
print("MSE:", mse)
```

</div>
