---
curso: OPTI
titulo: 11_Lab_Regresion_logistica_con_Newton
slides: 0
fuente: 11_Lab_Regresion_logistica_con_Newton.ipynb
---

<div class="cell markdown" id="zNMuI-VrVGRY">

# Regresión logística

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:237}" id="zH3Kr8xQ3zAO" outputId="56ac6060-9f1d-4d74-824e-27082a819d20">

``` python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.special import expit

data=pd.DataFrame({"x1":[1, 0, 2, -1, 1.5, -2], "x2":[1, 0, 2, -0.5, 1.5, -0.5], "y":[1, 0, 1, 0,0, 1]})

data
```

<div class="output execute_result" execution_count="5">

``` json
{"summary":"{\n  \"name\": \"data\",\n  \"rows\": 6,\n  \"fields\": [\n    {\n      \"column\": \"x1\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.541103500742244,\n        \"min\": -2.0,\n        \"max\": 2.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          1.0,\n          0.0,\n          -2.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"x2\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.0684880283216405,\n        \"min\": -0.5,\n        \"max\": 2.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          0.0,\n          1.5,\n          2.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"y\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"data"}
```

</div>

</div>

<div class="cell code" id="kgj49ZCUW48U">

``` python
data["color"]="blue"
data.loc[data.y==0, "color"]="red"
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="UH1dHafys_hO" outputId="b6128e0a-b6f0-45d4-fd0a-0cb718644e8f">

``` python
plt.scatter(data.x1, data.x2, color=data.color)
plt.show()
```

<div class="output display_data">

![](4782e6ced1e7689f14a11dc2164848660315ac05.png)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:237}" id="A_49MO7cbHyg" outputId="29cc5291-3fa5-4dc0-c45c-6a03f4204710">

``` python
X_data=data[["x1", "x2"]]
X_data
```

<div class="output execute_result" execution_count="8">

``` json
{"summary":"{\n  \"name\": \"X_data\",\n  \"rows\": 6,\n  \"fields\": [\n    {\n      \"column\": \"x1\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.541103500742244,\n        \"min\": -2.0,\n        \"max\": 2.0,\n        \"num_unique_values\": 6,\n        \"samples\": [\n          1.0,\n          0.0,\n          -2.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"x2\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.0684880283216405,\n        \"min\": -0.5,\n        \"max\": 2.0,\n        \"num_unique_values\": 5,\n        \"samples\": [\n          0.0,\n          1.5,\n          2.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"X_data"}
```

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:237}" id="vBdpzVYBUD3f" outputId="e299f2cb-ad27-4501-9cf9-582005fd06e2">

``` python
data[["y"]]
```

<div class="output execute_result" execution_count="9">

``` json
{"summary":"{\n  \"name\": \"data[[\\\"y\\\"]]\",\n  \"rows\": 6,\n  \"fields\": [\n    {\n      \"column\": \"y\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          0,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe"}
```

</div>

</div>

<div class="cell markdown" id="GYRXMtzxcjz7">

Definimos la función logística
``` math
\phi(x)=\dfrac{1}{1+e^{-x}}
```

</div>

<div class="cell code" id="OhFNS9EFcVmm">

``` python
def logistica(x):
  return 1/(1+np.exp(-x))
```

</div>

<div class="cell markdown" id="o1njxYwmcnFY">

Si fijamos un $`\beta=(b_0, b_1, b_2)`$ podemos calcular las probabilidades predichas

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="A6FzFSQSdHqN" outputId="f79f190b-30a5-4818-b81f-7a55f95b485b">

``` python
X=np.matrix(X_data)

B=pd.DataFrame(data={"constante":[1 for i in range(len(X))]})

X=np.concatenate([B, X], axis=1)

X
```

<div class="output execute_result" execution_count="11">

    matrix([[ 1. ,  1. ,  1. ],
            [ 1. ,  0. ,  0. ],
            [ 1. ,  2. ,  2. ],
            [ 1. , -1. , -0.5],
            [ 1. ,  1.5,  1.5],
            [ 1. , -2. , -0.5]])

</div>

</div>

<div class="cell markdown" id="CYFBh5V6dd0S">

Calculamos $`p=\phi(X\beta)`$, la matriz de probabilidades predichas

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="ux08ZNVxcvcF" outputId="9def587f-b8d2-4cff-fb46-4b79989f0dae">

``` python
beta=[1, 1, 1] # valores al azar (no entrenados)
beta=np.transpose(np.matrix(beta))
p=logistica(np.matmul(X, beta))
p
```

<div class="output execute_result" execution_count="12">

    matrix([[0.95257413],
            [0.73105858],
            [0.99330715],
            [0.37754067],
            [0.98201379],
            [0.18242552]])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="aFyG8TYfWCmc" outputId="be702651-91aa-40f9-e64c-66af94c71399">

``` python
y=data[["y"]]
y=np.matrix(y)
y
```

<div class="output execute_result" execution_count="13">

    matrix([[1],
            [0],
            [1],
            [0],
            [0],
            [1]])

</div>

</div>

<div class="cell markdown" id="sNUEnAyhe4NI">

Definimos la función log-likelihood (con signo negativo) $`-\ell`$ la cual será nuestra función objetivo

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="9nqHRzqFe4NQ" outputId="06ebd73b-bec4-4094-ca3e-1fa8bd6368aa">

``` python
def log_likelihood(X, y, beta):
  p=expit(np.matmul(X, beta))
  return -np.sum(np.multiply(y,np.log(p))+np.multiply((1-y), np.log(1-p)))

# La probamos
log_likelihood(X, y, beta)
```

<div class="output execute_result" execution_count="11">

    np.float64(7.562204577661753)

</div>

</div>

<div class="cell markdown" id="-90nVkc4JhKF">

Calculamos el gradiente
``` math
\nabla \ell = X^t(y-p)
```

</div>

<div class="cell code" id="-p0shE5rKEgJ">

``` python
gradiente=np.matmul(np.transpose(X), y-p)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="egl_PfmBKD77" outputId="0ca93930-71a1-4de4-9ac6-80a644eebdd9">

``` python
gradiente
```

<div class="output execute_result" execution_count="13">

    matrix([[-1.21891984],
            [-2.66981739],
            [-1.63222601]])

</div>

</div>

<div class="cell markdown" id="FdXYP2MYKFDS">

Calculamos el Hessiano
``` math
H\ell = -X^tWX
```
donde $`W`$ es una matriz diagonal
``` math
W=\begin{bmatrix} p_1(1-p_1) & 0 & 0 &  \dots & 0 \\ 0 & p_2(1-p_2) & 0 & \dots & 0 \\ \vdots &  & \ddots & \vdots \\ 0 & \dots & & p_n(1-p_n)\end{bmatrix}
```

</div>

<div class="cell code" id="v0w6iLhqgrk9">

``` python
W=np.diag(np.array(np.multiply(p, 1-p)).flatten())
hessiano=-np.matmul(np.matmul(np.transpose(X), W) , X)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="VCV_gax0g20n" outputId="fc6918e9-b851-42c2-e5ff-3e59643be66a">

``` python
hessiano
```

<div class="output execute_result" execution_count="15">

    matrix([[-0.65024952,  0.44832978,  0.10710825],
            [ 0.44832978, -0.9430995 , -0.37815828],
            [ 0.10710825, -0.37815828, -0.20754752]])

</div>

</div>

<div class="cell markdown" id="8nTu-Vl6K31F">

En cada paso, el vector $`\beta`$ cambia de acuerdo al método de Newton
``` math
\beta_{k+1}=\beta_k-(H\ell)^{-1}\nabla \ell
```
o
``` math
\beta_{k+1}=\beta_k-(H\ell+\mu I)^{-1}\nabla \ell
```

</div>

<div class="cell code" id="3P4RI1Z18Asd">

``` python
def Newton_logistica(X, y, beta, mu,  epsilon, max_iter):
  # Newton con la modificacion de Levenberg-Marquardt
  # No tiene tamaño de paso
  tol=epsilon+1

  iter=1

  valores=[]

  while tol>epsilon:
    p=expit(np.matmul(X, beta))

    W=np.diag(np.array(np.multiply(p, 1-p)).flatten())

    gradiente=-np.matmul(np.transpose(X), y-p)

    hessiano=np.matmul(np.matmul(np.transpose(X), W) , X)

    cambio=np.matmul(np.linalg.inv(hessiano+mu*np.eye(len(beta))), gradiente)

    beta=beta-cambio

    tol=np.linalg.norm(cambio)

    loglike=log_likelihood(X, y, beta)

    valores=np.concatenate((valores, loglike), axis=None)

    if (iter>=max_iter):
      print("El algoritmo no convergió en ", max_iter, "iteraciones")
      break

    iter+=1

  plt.plot(valores)
  return p,beta
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:586}" id="WdY7N9yu6pb5" outputId="ab640921-da8a-443c-b924-c1a0b9f90915">

``` python
beta=np.random.uniform(0, 1, 3) #[-0.21, 0.45]
beta=np.matrix(beta)
beta=np.transpose(beta)
mu=0
Newton_logistica(X, y, beta, mu, 10**(-6),10**3)
```

<div class="output execute_result" execution_count="17">

    (matrix([[0.35298336],
             [0.04586811],
             [0.86094123],
             [0.13888258],
             [0.64761892],
             [0.95370577]]),
     matrix([[-3.03503191],
             [-4.84994063],
             [ 7.27902139]]))

</div>

<div class="output display_data">

![](5b8da50bd29ec14a050afcfbc87aba1011d0c740.png)

</div>

</div>

<div class="cell markdown" id="gIUhVieLOXx5">

Lo comparamos con los coeficientes obtenidos con la libreria sklearn

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="SjqF8hLV6Fur" outputId="cb125d3a-0c78-4913-d183-117e3073e0d9">

``` python
from sklearn.linear_model import LogisticRegression

modelo=LogisticRegression(verbose=True, penalty=None)
modelo.fit(data[["x1", "x2"]], data["y"])
print(modelo.intercept_, modelo.coef_)
```

<div class="output stream stdout">

    [-3.03585037] [[-4.85127292  7.28109419]]

</div>

<div class="output stream stderr">

    [Parallel(n_jobs=1)]: Done   1 out of   1 | elapsed:    0.0s finished

</div>

</div>
