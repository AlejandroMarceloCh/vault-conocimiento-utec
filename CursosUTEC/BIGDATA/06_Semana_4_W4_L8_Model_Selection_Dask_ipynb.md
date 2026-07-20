---
curso: BIGDATA
titulo: 06 - Semana 4/W4 L8 Model_Selection_Dask
slides: 0
fuente: 06 - Semana 4/W4 L8 Model_Selection_Dask.ipynb
---

<div class="cell markdown" id="gjRyTkgmEfXP">

# Selección de Modelo con **Dask**

</div>

<div class="cell markdown" id="Yur8bN5dEfdy">

Curso: Big Data - UTEC

Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="hbduQCVKATZR">

``` python
# pip install dask-ml
```

</div>

<div class="cell code" id="kaLLLcF4_jfy">

``` python
import dask.dataframe as dd
import pandas as pd
import numpy as np
```

</div>

<div class="cell code" id="6k1DOyea_wBt">

``` python
# Crear DataFrame de ejemplo
pdf = pd.DataFrame({
    'feature1': np.random.rand(100),
    'feature2': np.random.rand(100),
    'target': np.random.randint(0, 2, 100)
})
ddf = dd.from_pandas(pdf, npartitions=4)
```

</div>

<div class="cell code" id="tSDcSXbsA1ME">

``` python
# Separamos características y target
X = ddf[['feature1', 'feature2']]
y = ddf['target']

print("DataFrame original:")
print(ddf.head())
```

</div>

<div class="cell code" id="nw2rS_ONC7KX">

``` python
# Convertir Dask DataFrame a Dask Array
X_da = X.to_dask_array(lengths=True)
y_da = y.to_dask_array(lengths=True)
```

</div>

<div class="cell markdown" id="Z3GRd-vU_lcH">

## train_test_split

Divide un conjunto de datos en entrenamiento y prueba.

</div>

<div class="cell code" id="McdrjBGG_pVB">

``` python
from dask_ml.model_selection import train_test_split
```

</div>

<div class="cell code" id="OppPGX51_pYH">

``` python
X_train, X_test, y_train, y_test = train_test_split(X_da, y_da, test_size=0.2, random_state=123, shuffle=True)

print("train_test_split:")
print("X_train:")
print(X_train.compute())
print("X_test:")
print(X_test.compute())
```

</div>

<div class="cell markdown" id="Lv20JG1ZBFPa">

## KFold

Importa y crea validación cruzada en K pliegues, genera índices para train y test.

</div>

<div class="cell code" id="LFC43wfQ_pa9">

``` python
from dask_ml.model_selection import KFold

kf = KFold(n_splits=3, shuffle=True, random_state=123)

print("\nKFold splits:")
for fold, (train_index, test_index) in enumerate(kf.split(X_da)):
    print(f"Fold {fold + 1}:")
    print("Train indices:", train_index.compute()[:5])
    print("Test indices:", test_index.compute()[:5])
```

</div>

<div class="cell markdown" id="0XvLtc9sB7dk">

# GridSearchCV

Importa y realiza búsqueda exhaustiva de hiperparámetros con validación cruzada.

</div>

<div class="cell code" id="S4FvfCdPCDJK">

``` python
from dask_ml.model_selection import GridSearchCV
from dask_ml.linear_model import LogisticRegression
```

</div>

<div class="cell code" id="gLqw4ZgI_pd1">

``` python
model = LogisticRegression()

param_grid = {'C': [0.01, 0.1, 1.0, 10]}

grid_search = GridSearchCV(model, param_grid, cv=3)
grid_search.fit(X_da, y_da)

print("GridSearchCV:")
print("Mejores parámetros:", grid_search.best_params_)
print("Mejor score:", grid_search.best_score_)
```

</div>

<div class="cell markdown" id="AELfHTNaDTmU">

## RandomizedSearchCV

Importa y realiza búsqueda aleatoria de hiperparámetros con validación cruzada.

</div>

<div class="cell code" id="Rf4-aHy1_pgr">

``` python
from dask_ml.model_selection import RandomizedSearchCV
```

</div>

<div class="cell code" id="7JBpF6Jl_pjZ">

``` python
param_distributions = {'C': np.logspace(-2, 1, 20)}

random_search = RandomizedSearchCV(model, param_distributions, n_iter=5, cv=3, random_state=123)
random_search.fit(X_da, y_da)

print("RandomizedSearchCV:")
print("Mejores parámetros:", random_search.best_params_)
print("Mejor score:", random_search.best_score_)
```

</div>
