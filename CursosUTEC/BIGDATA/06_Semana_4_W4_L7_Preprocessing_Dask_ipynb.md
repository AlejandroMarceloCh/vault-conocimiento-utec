---
curso: BIGDATA
titulo: 06 - Semana 4/W4 L7 Preprocessing_Dask
slides: 0
fuente: 06 - Semana 4/W4 L7 Preprocessing_Dask.ipynb
---

<div class="cell markdown" id="C1SAjPX5-rc4">

# Preprocesamiento con **Dask**

</div>

<div class="cell markdown" id="IQR-KBAQ-faZ">

Curso: Big Data - UTEC

Docente: Aldo Lezama Benavides

</div>

<div class="cell markdown" id="zKqPE7hi4VWa">

#### Instalación

</div>

<div class="cell code" id="RVahfnz64uCq">

``` python
# !pip install dask-ml
```

</div>

<div class="cell code" id="bhyvdnVg40Dj">

``` python
import pandas as pd
import dask.dataframe as dd
```

</div>

<div class="cell code" id="4EWHtxDF46Tf">

``` python
# Crear un DataFrame de ejemplo
pdf = pd.DataFrame({
    'edad': [25, 45, 35, 50, 23, 40],
    'ingresos': [50000, 80000, 60000, 120000, 45000, 70000],
    'genero': ['M', 'F', 'F', 'M', 'F', 'M'],
    'ciudad': ['A', 'B', 'A', 'C', 'B', 'A']
})
```

</div>

<div class="cell code" id="2WjSCn3Y46Wx">

``` python
# Convertir a Dask DataFrame
ddf = dd.from_pandas(pdf, npartitions=2)
```

</div>

<div class="cell code" id="VQErbqzB46Zn">

``` python
# Mostrar el DataFrame original
print("DataFrame original:")
print(ddf.compute())
```

</div>

<div class="cell code" id="rpwZ67En5ikL">

``` python
ddf_num = ddf[['edad', 'ingresos']]
print(ddf_num.compute())
```

</div>

<div class="cell code" id="33Llayuc7x8_">

``` python
ddf_cat = cat.fit_transform(ddf[['genero', 'ciudad']])
print(ddf_cat.compute())
```

</div>

<div class="cell markdown" id="BK_vwF9h5i9U">

## StandardScaler

Escala los datos para que tengan media 0 y desviación estándar 1.

</div>

<div class="cell code" id="HFH5HPlB5WBg">

``` python
from dask_ml.preprocessing import StandardScaler
```

</div>

<div class="cell code" id="yzzdlm7C5Lu6">

``` python
scaler_std = StandardScaler()
ddf_std = scaler_std.fit_transform(ddf_num)
print("StandardScaler:")
print(ddf_std.compute())
```

</div>

<div class="cell markdown" id="6QhlXz315p6S">

## MinMaxScaler

Escala los datos para que estén en un rango específico, por defecto entre 0 y 1.

</div>

<div class="cell code" id="0PBXF4t_6qOw">

``` python
from dask_ml.preprocessing import MinMaxScaler
```

</div>

<div class="cell code" id="a3XAbkk85L1g">

``` python
scaler_mm = MinMaxScaler()
ddf_mm = scaler_mm.fit_transform(ddf_num)
print("MinMaxScaler:")
print(ddf_mm.compute())
```

</div>

<div class="cell markdown" id="KtiKBn9u9hTU">

## QuantileTransformer

Transforma las columnas para seguir una distribución normal o uniforme.

</div>

<div class="cell code" id="aSRSvi7b5L7R">

``` python
from dask_ml.preprocessing import QuantileTransformer
```

</div>

<div class="cell code" id="r2F3HXGk46cI">

``` python
qt = QuantileTransformer(output_distribution='normal')
ddf_qt = qt.fit_transform(ddf_num)
print("QuantileTransformer (normal):")
print(ddf_qt.compute())
```

</div>

<div class="cell markdown" id="yfO4Dowf8Dwi">

## Categorizer

Convierte columnas de tipo objeto en categorías (tipo 'category').

</div>

<div class="cell code" id="yReS0UXE7bCH">

``` python
from dask_ml.preprocessing import Categorizer
```

</div>

<div class="cell code" id="RaRuiuV77bFH">

``` python
cat = Categorizer()
print("Categorizer:")
print(ddf_cat.compute())
```

</div>

<div class="cell markdown" id="CxxUCtr28GCo">

## DummyEncoder

Aplica one-hot encoding a columnas categóricas.

</div>

<div class="cell code" id="8fGOQPLC7bNh">

``` python
from dask_ml.preprocessing import DummyEncoder
```

</div>

<div class="cell code" id="DnfEfTnj7bQP">

``` python
encoder = DummyEncoder()
ddf_dummy = encoder.fit_transform(ddf_cat)
print("DummyEncoder:")
print(ddf_dummy.compute())
```

</div>

<div class="cell markdown" id="F_rmrSMm8icd">

## LabelEncoder

Convierte etiquetas (una sola columna) en números enteros.

</div>

<div class="cell code" id="BsdqGKz48QyF">

``` python
from dask_ml.preprocessing import LabelEncoder
```

</div>

<div class="cell code" id="IUXTslNO7bTH">

``` python
le = LabelEncoder()
ddf_genero_enc = le.fit_transform(ddf['genero'])
print("LabelEncoder:")
print(ddf_genero_enc.compute())
```

</div>

<div class="cell markdown" id="SWeNiPZG8ucp">

## OrdinalEncoder

Convierte varias columnas categóricas en enteros según orden.

</div>

<div class="cell code" id="EXnwgGqa8nvp">

``` python
from dask_ml.preprocessing import OrdinalEncoder
```

</div>

<div class="cell code" id="5kZYtSMU8mUt">

``` python
oe = OrdinalEncoder()
ddf_ordinal = oe.fit_transform(ddf_cat)
print("OrdinalEncoder:")
print(ddf_ordinal.compute())
```

</div>
