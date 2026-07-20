---
curso: OPTI
titulo: 07_Lab_regresión_lineal
slides: 0
fuente: 07_Lab_regresión_lineal.ipynb
---

<div class="cell code" id="Fpvk8U2cdsWm">

``` python
import numpy as np
import matplotlib.pyplot as plt
```

</div>

<div class="cell code" id="XvPgBCIIdrRQ">

``` python
def gradiente_descendiente(f, gradiente, alpha, x0, epsilon, max_iteraciones):
  iteraciones = 0

  tol=epsilon+1

  valores = [] # Lista para almacenar los valores de f

  while tol > epsilon:

    if iteraciones == max_iteraciones:
      print("El algoritmo no convergió en ", max_iteraciones, " iteraciones")
      break

    valores.append(f(x0))

    x1 = x0-alpha*gradiente(x0)

    tol = np.linalg.norm(x1-x0)

    x0=x1

    iteraciones += 1
  return x0, valores, iteraciones
```

</div>

<div class="cell code" id="G0YTUpP_ePou">

``` python
def residuos(punto):
  b0=punto[0]
  b1=punto[1]
  b2=punto[2]
  r1=6-(b0+3*b1+b2)
  r2=-4-(b0-b1+5*b2)
  r3=7-(b0+4*b1)
  return np.array([r1,r2,r3])
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="0TBmDPpLe5QV" outputId="fe3c0bb3-aee6-4865-dcc4-dcd74b7af6a1">

``` python
residuos([1, 1, 1])
```

<div class="output execute_result" execution_count="25">

    array([ 1, -9,  2])

</div>

</div>

<div class="cell code" id="3xu56qf2dsaG">

``` python
def R(punto):
  return 1/3*np.sum(residuos(punto)**2)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="JOHc7cOSey3T" outputId="6544cd0d-b8da-4525-8eb7-95e542b3a8ff">

``` python
R([1, 1, 1])
```

<div class="output execute_result" execution_count="27">

    np.float64(28.666666666666664)

</div>

</div>

<div class="cell code" id="hllV3-mve_gN">

``` python
def grad_R(punto):
  r=residuos(punto)
  R_b0=-2/3*np.sum(r)
  R_b1=-2/3*np.dot(r, np.array([3, -1, 4]))
  R_b2=-2/3*np.dot(r, np.array([1, 5, 0]))
  return np.array([R_b0, R_b1, R_b2])
```

</div>

<div class="cell code" id="oqxaP-TEgCM5">

``` python
alpha=0.01
x0=np.array([0, 0, 0])
epsilon=10**-6
max_iteraciones=1000
x0, valores, iteraciones=gradiente_descendiente(R, grad_R, alpha, x0, epsilon, max_iteraciones)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="B2DkqMThgTpy" outputId="de0ad1aa-24ad-4fa5-e2a1-8ba96b83523f">

``` python
x0
```

<div class="output execute_result" execution_count="30">

    array([ 0.33333232,  1.80951971, -0.47619044])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:432}" id="10nyPSm8gW4P" outputId="95339d70-510b-45b4-ef20-400d663f5e22">

``` python
plt.plot(valores, color='red')
plt.show()
```

<div class="output display_data">

![](605bfb085dd9d60fa9cb8f0293b90d32902f6492.png)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="qTklIQJXjnlm" outputId="9e66af4b-378d-4ebb-ed15-e905d069d31f">

``` python
valores[-1]
```

<div class="output execute_result" execution_count="32">

    np.float64(0.2857142859591495)

</div>

</div>

<div class="cell markdown" id="eKBCxHpkM-Qt">

# Regresión lineal

Realizaremos una regresion lineal utilizando la data del arhivo [auto-mpg.data](https://drive.google.com/file/d/1yC8tha9HyjDOomGw2QRwR_pPby4eF5eI/view?usp=sharing)

</div>

<div class="cell code" id="FizlAWqy7vu1">

``` python
import pandas as pd
import numpy as np
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="Rnd1OE88M98a" outputId="696582f2-cdd8-4785-f148-2b4cc4546194">

``` python
!gdown 1W5rCn6i2jmarrnBfVb4KOTX5fWyohfpK
```

<div class="output stream stdout">

    Downloading...
    From: https://drive.google.com/uc?id=1W5rCn6i2jmarrnBfVb4KOTX5fWyohfpK
    To: /content/auto-mpg.data
    
  0% 0.00/30.3k [00:00<?, ?B/s]
100% 30.3k/30.3k [00:00<00:00, 58.3MB/s]

</div>

</div>

<div class="cell code" id="8LIQikJgIIxl">

``` python
column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight',
                'Acceleration', 'Model Year', 'Origin']

data = pd.read_csv("auto-mpg.data", names=column_names,
                   comment='\t', sep=" ", skipinitialspace=True)

data=data[data.Horsepower!="?"]

```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="xJS4btmkZQhh" outputId="737bb1a7-721c-49db-9911-9d4c7d1ab8f2">

``` python
data["Horsepower"]=pd.to_numeric(data["Horsepower"])
data.info()
```

<div class="output stream stdout">

    <class 'pandas.core.frame.DataFrame'>
    Index: 392 entries, 0 to 397
    Data columns (total 8 columns):
     #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
     0   MPG           392 non-null    float64
     1   Cylinders     392 non-null    int64  
     2   Displacement  392 non-null    float64
     3   Horsepower    392 non-null    float64
     4   Weight        392 non-null    float64
     5   Acceleration  392 non-null    float64
     6   Model Year    392 non-null    int64  
     7   Origin        392 non-null    int64  
    dtypes: float64(5), int64(3)
    memory usage: 27.6 KB

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" id="-6RojoxMRDQ2" outputId="de510dcd-1d8d-4ab9-b554-d767c43a7a40">

``` python
data.head()
```

<div class="output execute_result" execution_count="37">

``` json
{"summary":"{\n  \"name\": \"data\",\n  \"rows\": 392,\n  \"fields\": [\n    {\n      \"column\": \"MPG\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 7.805007486571799,\n        \"min\": 9.0,\n        \"max\": 46.6,\n        \"num_unique_values\": 127,\n        \"samples\": [\n          17.5,\n          35.1,\n          28.8\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Cylinders\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 3,\n        \"max\": 8,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          4,\n          5,\n          6\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Displacement\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 104.64400390890465,\n        \"min\": 68.0,\n        \"max\": 455.0,\n        \"num_unique_values\": 81,\n        \"samples\": [\n          116.0,\n          307.0,\n          360.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Horsepower\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 38.49115993282855,\n        \"min\": 46.0,\n        \"max\": 230.0,\n        \"num_unique_values\": 93,\n        \"samples\": [\n          92.0,\n          100.0,\n          52.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Weight\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 849.4025600429494,\n        \"min\": 1613.0,\n        \"max\": 5140.0,\n        \"num_unique_values\": 346,\n        \"samples\": [\n          2472.0,\n          3221.0,\n          2700.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Acceleration\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2.7588641191880816,\n        \"min\": 8.0,\n        \"max\": 24.8,\n        \"num_unique_values\": 95,\n        \"samples\": [\n          14.7,\n          18.0,\n          14.3\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Model Year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3,\n        \"min\": 70,\n        \"max\": 82,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          81,\n          79,\n          70\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Origin\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 1,\n        \"max\": 3,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          1,\n          3,\n          2\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"data"}
```

</div>

</div>

<div class="cell code" id="Odwql38TJg4N">

``` python
nrow=data.shape[0]
ncol=data.shape[1]
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="WXnsHr6lR9QA" outputId="0c1732e6-0332-4af9-f81e-49789ad85535">

``` python
data.shape
```

<div class="output execute_result" execution_count="39">

    (392, 8)

</div>

</div>

<div class="cell markdown" id="m-XyL3I6O4_F">

### Variable a predecir

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:458}" id="8Q-YL7gVAyOM" outputId="5ba6b6ae-50a1-48c9-b421-8c410989db35">

``` python
y=data["MPG"]
y
```

<div class="output execute_result" execution_count="40">

    0      18.0
    1      15.0
    2      18.0
    3      16.0
    4      17.0
           ... 
    393    27.0
    394    44.0
    395    32.0
    396    28.0
    397    31.0
    Name: MPG, Length: 392, dtype: float64

</div>

</div>

<div class="cell markdown" id="JI-RywLMO8Fv">

### Variables predictivas

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" id="fSbMEBCWUopD" outputId="f4c49a1e-7aa7-4cf8-e722-da5bd13b1a1e">

``` python
X_modelo=data[['Cylinders','Displacement','Horsepower','Weight',
                'Acceleration', 'Model Year', 'Origin']]
X_modelo.head()
```

<div class="output execute_result" execution_count="41">

``` json
{"summary":"{\n  \"name\": \"X_modelo\",\n  \"rows\": 392,\n  \"fields\": [\n    {\n      \"column\": \"Cylinders\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 3,\n        \"max\": 8,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          4,\n          5,\n          6\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Displacement\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 104.64400390890465,\n        \"min\": 68.0,\n        \"max\": 455.0,\n        \"num_unique_values\": 81,\n        \"samples\": [\n          116.0,\n          307.0,\n          360.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Horsepower\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 38.49115993282855,\n        \"min\": 46.0,\n        \"max\": 230.0,\n        \"num_unique_values\": 93,\n        \"samples\": [\n          92.0,\n          100.0,\n          52.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Weight\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 849.4025600429494,\n        \"min\": 1613.0,\n        \"max\": 5140.0,\n        \"num_unique_values\": 346,\n        \"samples\": [\n          2472.0,\n          3221.0,\n          2700.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Acceleration\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2.7588641191880816,\n        \"min\": 8.0,\n        \"max\": 24.8,\n        \"num_unique_values\": 95,\n        \"samples\": [\n          14.7,\n          18.0,\n          14.3\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Model Year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3,\n        \"min\": 70,\n        \"max\": 82,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          81,\n          79,\n          70\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Origin\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 1,\n        \"max\": 3,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          1,\n          3,\n          2\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"X_modelo"}
```

</div>

</div>

<div class="cell markdown" id="Twjf3SBcVG4N">

Sklearn para regresión lineal

</div>

<div class="cell code" id="e-1Q-XsEQG5c">

``` python
from sklearn.linear_model import LinearRegression

mod=LinearRegression().fit(X_modelo, y)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="9OqRfgGnQG5d" outputId="f4a27c65-45b6-4f52-8dbd-4162e45ff8f3">

``` python
mod.coef_
```

<div class="output execute_result" execution_count="43">

    array([-0.49337632,  0.01989564, -0.01695114, -0.00647404,  0.08057584,
            0.75077268,  1.4261405 ])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="6ZLB0fTGVtNK" outputId="874a2207-efdc-4625-84ee-b2609720fdc5">

``` python
mod.intercept_
```

<div class="output execute_result" execution_count="44">

    np.float64(-17.218434622017536)

</div>

</div>

<div class="cell markdown" id="Dji4tVS_Vbl0">

Valores predichos

</div>

<div class="cell code" id="EgeN9YYtQG5d">

``` python
y_pred=mod.predict(X_modelo)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="v_puMt04rlxZ" outputId="9cd7f28d-7b34-44b7-b859-99d32f5e89bc">

``` python
import matplotlib.pyplot as plt
plt.scatter(y, y_pred)
plt.show()
```

<div class="output display_data">

![](c50301941f2b82faf981f3d3b11a9a8c5adc2aaf.png)

</div>

</div>

<div class="cell markdown" id="SLA21-wQV3Ga">

$`r^2`$

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="-u1eYtfTQG5d" outputId="e03130ee-dcc0-429d-eea9-0fc4279c3f9e">

``` python
from sklearn import metrics
metrics.r2_score(y, y_pred)
```

<div class="output execute_result" execution_count="47">

    0.8214780764810599

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="YCTjnWYJ5_G2" outputId="ada9b4c0-9f8a-484b-bca9-2130946d4efe">

``` python
(1/nrow*np.linalg.norm(y-y_pred)**2)**0.5
```

<div class="output execute_result" execution_count="48">

    np.float64(3.2935514183022025)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="dbFY0_27yuVz" outputId="ec7f50d7-2aee-4c20-92b2-1a195eb3c2f9">

``` python
metrics.root_mean_squared_error(y, y_pred)
```

<div class="output execute_result" execution_count="49">

    3.2935514183022025

</div>

</div>

<div class="cell markdown" id="CyS0-Okpal2W">

## **Ejercicio 1:**

Inicializamos $`\beta`$ al azar

a\) Halla los valores predichos considerando a $`\beta`$ como los coeficientes de la regresión.

b\) Halla el valor de la función objetivo $`\dfrac{1}{n}||y-X\beta||^2`$ (MSE) para dichos valores de $`\beta`$

</div>

<div class="cell code" id="REzTNzvifTWc">

``` python
from scipy.stats import uniform
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="FmAggTqufX7-" outputId="05fffce4-7561-4aea-d0ad-0cf1f34c6af0">

``` python
beta_inicial=uniform.rvs(size=8)
beta_inicial
```

<div class="output execute_result" execution_count="51">

    array([0.12189364, 0.89655211, 0.51742807, 0.10866584, 0.86552207,
           0.02686254, 0.39575632, 0.08185651])

</div>

</div>

<div class="cell markdown" id="tpXg29EykhQg">

a\)

</div>

<div class="cell code" id="XVa_h0P2kiVB">

``` python
y_pred=beta_inicial[0]+np.matmul(X_modelo, np.transpose(beta_inicial[1:8]))
```

</div>

<div class="cell markdown" id="vTARrZdAlR6o">

b\)

</div>

<div class="cell code" id="-RO7h107lTB3">

``` python
residuos=y.to_numpy()-y_pred.to_numpy()
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="2V9r772wlVgu" outputId="facf7847-456d-4002-d66b-001df6aa7d7a">

``` python
(1/nrow)*np.linalg.norm(residuos)**2
```

<div class="output execute_result" execution_count="54">

    np.float64(7930585.8443555)

</div>

</div>

<div class="cell markdown" id="ZItFMSPIdXM1">

## **Ejercicio 2:**

El gradiente de la función objetivo es
``` math
-\dfrac{2}{n}X^t(y-X\beta)
```
Halla el vector gradiente para los valores de $`\beta`$ del ejercicio anterior.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="j1HQQ1pYmlva" outputId="63a1639f-e4fb-46ba-f98f-44c7c7780336">

``` python
grad_0=(-2/nrow)*np.sum(residuos)
grad_0
```

<div class="output execute_result" execution_count="55">

    np.float64(5402.618201386634)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:303}" id="U3irSAgMomP6" outputId="95644d0c-e5d0-4745-9e85-9d8806c1c750">

``` python
grad_1_p=(-2/nrow)*np.matmul(np.transpose(X_modelo), residuos)
grad_1_p
```

<div class="output execute_result" execution_count="56">

    Cylinders       3.201922e+04
    Displacement    1.207094e+06
    Horsepower      6.177767e+05
    Weight          1.743667e+07
    Acceleration    8.207972e+04
    Model Year      4.086325e+05
    Origin          7.761823e+03
    dtype: float64

</div>

</div>

<div class="cell markdown" id="nZrTNf1g_71U">

# Estandarización

</div>

<div class="cell code" id="P_DlvDc2_9Eq">

``` python
from sklearn.preprocessing import StandardScaler

scaler_X=StandardScaler()

X_stand=scaler_X.fit_transform(X_modelo)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:423}" id="bAiNQdoE2Bnh" outputId="cee5e5c5-b17e-4178-b15d-fd0d4dd97071">

``` python
pd.DataFrame(X_stand)
```

<div class="output execute_result" execution_count="58">

``` json
{"summary":"{\n  \"name\": \"pd\",\n  \"rows\": 392,\n  \"fields\": [\n    {\n      \"column\": 0,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.0012779557930158,\n        \"min\": -1.4510037003144203,\n        \"max\": 1.483947024779763,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          -0.8640135552955837,\n          -0.277023410276747,\n          0.30996673474208963\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 1,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.0012779557930116,\n        \"min\": -1.2095632239069316,\n        \"max\": 2.4934159666563414,\n        \"num_unique_values\": 81,\n        \"samples\": [\n          -0.7502789832169132,\n          1.077289557862118,\n          1.5844159069573467\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 2,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.0012779557930127,\n        \"min\": -1.5209754434541274,\n        \"max\": 3.2654519904664348,\n        \"num_unique_values\": 93,\n        \"samples\": [\n          -0.3243685849739868,\n          -0.11626304436874499,\n          -1.364896288000196\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 3,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.0012779557930123,\n        \"min\": -1.6085753990039313,\n        \"max\": 2.549061410924434,\n        \"num_unique_values\": 346,\n        \"samples\": [\n          -0.5959839559280975,\n          0.2869391999086888,\n          -0.3272169605598902\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 4,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.0012779557930125,\n        \"min\": -2.736982934397379,\n        \"max\": 3.36026177596301,\n        \"num_unique_values\": 95,\n        \"samples\": [\n          -0.3053436749084146,\n          0.8923293931980906,\n          -0.4505161680122328\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 5,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.0012779557930123,\n        \"min\": -1.625315334018757,\n        \"max\": 1.636409636640043,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          1.3645992224184762,\n          0.8209783939753429,\n          -1.625315334018757\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": 6,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.0012779557930127,\n        \"min\": -0.7166410451853079,\n        \"max\": 1.769405766430982,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          -0.7166410451853079,\n          1.769405766430982,\n          0.526382360622837\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe"}
```

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="DrvTRvBCAS7Q" outputId="9468a367-0b49-4a9a-bd43-8aefa67533d1">

``` python
np.mean(X_stand[:,0])
```

<div class="output execute_result" execution_count="59">

    np.float64(-1.0875654118777043e-16)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="Kf8yYKJ_AeDg" outputId="1797ba33-cc89-4314-cfa0-d1ac03651eda">

``` python
np.std(X_stand[:,0])
```

<div class="output execute_result" execution_count="60">

    np.float64(1.0)

</div>

</div>

<div class="cell code" id="BFXAgR_rCgWr">

``` python
y=data[["MPG"]]
scaler_Y=StandardScaler()

y_stand=scaler_Y.fit_transform(y)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:423}" id="7LwIa1Xw2Ytf" outputId="e4c3ca78-d018-4861-8eb2-e04889a5402a">

``` python
pd.DataFrame(y_stand)
```

<div class="output execute_result" execution_count="62">

``` json
{"summary":"{\n  \"name\": \"pd\",\n  \"rows\": 392,\n  \"fields\": [\n    {\n      \"column\": 0,\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.0012779557930118,\n        \"min\": -1.85321790367213,\n        \"max\": 2.9703586531203157,\n        \"num_unique_values\": 127,\n        \"samples\": [\n          -0.7627817139717101,\n          1.4950626317609241,\n          0.6868569852770835\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe"}
```

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="uxHOdFwpC2yv" outputId="e808d495-95a2-4137-b2c4-493bb75f47da">

``` python
np.std(y_stand)
```

<div class="output execute_result" execution_count="63">

    np.float64(1.0)

</div>

</div>

<div class="cell code" id="35zodWUiDAMM">

``` python
beta=np.random.normal(loc=0, scale=1, size=7) # Esta lista no incluye al c0
```

</div>

<div class="cell code" id="UsxkyVdHDLDl">

``` python
y_hat=np.matmul(X_stand, np.transpose(beta))
```

</div>

<div class="cell code" id="nQGI7LQREKo5">

``` python
r=y_stand.flatten()-y_hat # usamos flatten para convertir ambos a arreglos unidimensionales
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="JS25IPibEXso" outputId="538fde52-4f6f-40cd-f092-43ad00de55c7">

``` python
R=(1/nrow)*np.linalg.norm(r)**2
R
```

<div class="output execute_result" execution_count="67">

    np.float64(10.568051861366573)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="WMePz15BEqlK" outputId="3feb0a63-b515-43ff-fd18-b5e9ddf3704c">

``` python
grad=(-2/nrow)*np.matmul(np.transpose(X_stand), r)
grad
```

<div class="output execute_result" execution_count="68">

    array([ 5.79026531,  6.03118942,  5.40312458,  6.15358377, -2.1713899 ,
           -3.00752708, -4.5619755 ])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="a564V0LRE6j0" outputId="c357171c-4dc8-47c7-a2bf-395692be9ec9">

``` python
alpha=0.01
beta=beta-alpha*grad
beta
```

<div class="output execute_result" execution_count="69">

    array([ 0.07754913,  0.84570597,  0.4801079 ,  0.70456165,  0.77761687,
           -0.17823297, -0.4680221 ])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="42JXAtvfFNy1" outputId="24bd23ea-888a-42bc-9c24-9346306bf437">

``` python
y_hat=np.matmul(X_stand, np.transpose(beta))
r=y_stand.flatten()-y_hat
R=(1/nrow)*np.linalg.norm(r)**2
R
```

<div class="output execute_result" execution_count="70">

    np.float64(8.930375565304944)

</div>

</div>

<div class="cell markdown" id="bzb2vsHmxQ9u">

Gradiente descendiente

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="67A5kdY-xQPp" outputId="3b93c1b3-0383-48ce-eb2a-2776a6ab10f9">

``` python
epsilon=10**-6
alpha=0.1
valores=[]
beta=np.random.normal(loc=0, scale=1, size=7)
tol=epsilon+1
while tol>epsilon:
  #gradiente
  y_hat=np.matmul(X_stand, np.transpose(beta))
  r=y_stand.flatten()-y_hat
  grad=(-2/nrow)*np.matmul(np.transpose(X_stand), r)

  #funcion objetivo
  R=(1/nrow)*np.linalg.norm(r)**2
  valores.append(R)

  #actualizacion
  beta=beta-alpha*grad
  tol=np.linalg.norm(alpha*grad)

beta
```

<div class="output execute_result" execution_count="72">

    array([-0.10776051,  0.26662185, -0.08357133, -0.70452817,  0.02847874,
            0.35434154,  0.14717496])

</div>

</div>

<div class="cell code" id="VEMO2LQ6yee0">

``` python
import matplotlib.pyplot as plt
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:447}" id="FviPviGUyEeD" outputId="f0f24be4-fc69-41a5-e809-eed553f88e42">

``` python
plt.plot(valores)
```

<div class="output execute_result" execution_count="73">

    [<matplotlib.lines.Line2D at 0x7afff4fc76b0>]

</div>

<div class="output display_data">

![](4713225e99719f699efa5620496e1844da18a6d7.png)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="UTesaCDw0TQl" outputId="fc4b0e15-4973-485d-87b8-94d26c933532">

``` python
scaler_X.scale_
```

<div class="output execute_result" execution_count="111">

    array([1.70360611e+00, 1.04510444e+02, 3.84420327e+01, 8.48318447e+02,
           2.75534291e+00, 3.67903490e+00, 8.04490081e-01])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="N0tlJ6ph0WWk" outputId="d550f6a7-6dc7-4608-d1c3-b693cafea144">

``` python
scaler_Y.scale_
```

<div class="output execute_result" execution_count="112">

    array([7.79504576])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="caplsciF0dRl" outputId="e36ac41a-8fad-4f69-96e1-b24a4e8ae155">

``` python
beta*(scaler_Y.scale_)/scaler_X.scale_
```

<div class="output execute_result" execution_count="113">

    array([-0.4933794 ,  0.01989574, -0.0169512 , -0.00647405,  0.08057589,
            0.7507727 ,  1.42614151])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="h6nDbREr0oAX" outputId="3c143f0a-a5f1-460c-da4c-7763c8c81c4f">

``` python
#sklearn
mod.coef_
```

<div class="output execute_result" execution_count="114">

    array([-0.49337632,  0.01989564, -0.01695114, -0.00647404,  0.08057584,
            0.75077268,  1.4261405 ])

</div>

</div>

<div class="cell code" id="pXIBTI2W0yk2">

``` python
```

</div>
