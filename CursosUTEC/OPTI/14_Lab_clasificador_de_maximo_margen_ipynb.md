---
curso: OPTI
titulo: 14_Lab_clasificador_de_maximo_margen
slides: 0
fuente: 14_Lab_clasificador_de_maximo_margen.ipynb
---

<div class="cell markdown" id="nkFg9ZmXN6qq">

# <center> Clasificador de Máximo Margen </center>

En esta actividad implementaremos un clasificador de máximo margen basandonos en la libreria cvxopt. Compararemos nuestros resultados con los obtenidos con el paquete sklearn.

</div>

<div class="cell code" id="xfpBLkSvzteS">

``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cvxopt import matrix, solvers
```

</div>

<div class="cell markdown" id="ntk4ZGbKOJ-O">

Utilizaremos la data del archivo maximo_margen.csv de

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="iCU0ZjZEa86F" outputId="b8918f48-4158-4af2-fbf8-86efe4ee6538">

``` python
!gdown 1PvK1ttdFLMLX9GsmC5jzODA9EnfesEve
```

<div class="output stream stdout">

    Downloading...
    From: https://drive.google.com/uc?id=1PvK1ttdFLMLX9GsmC5jzODA9EnfesEve
    To: /content/maximo_margen.csv
    
  0% 0.00/479 [00:00<?, ?B/s]
100% 479/479 [00:00<00:00, 1.94MB/s]

</div>

</div>

<div class="cell code" id="ZygfglGR3zYh">

``` python
data=pd.read_csv("maximo_margen.csv")
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:363}" id="XT3jyDHK32Ll" outputId="fa6d6b16-db00-4cd8-fc49-5dbba7a6e859">

``` python
data
```

<div class="output execute_result" execution_count="4">

``` json
{"summary":"{\n  \"name\": \"data\",\n  \"rows\": 10,\n  \"fields\": [\n    {\n      \"column\": \"x1\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.0756014305024861,\n        \"min\": -1.958825903018174,\n        \"max\": 1.6722622801083833,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          0.2384615448988786,\n          -0.0969538930356705,\n          1.6722622801083833\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"x2\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0.9905708425693125,\n        \"min\": -1.200353263654871,\n        \"max\": 1.9224536522326088,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          -0.174330928679177,\n          1.9224536522326088,\n          0.5947679680697149\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"y\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": -1,\n        \"max\": 1,\n        \"num_unique_values\": 2,\n        \"samples\": [\n          1,\n          -1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"color\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"red\",\n          \"blue\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"data"}
```

</div>

</div>

<div class="cell code" id="HYxPmNRTvH-G">

``` python
X=np.matrix(data[["x1", "x2"]])
y=np.matrix(data[["y"]])
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="cy5Jy7RsvM6X" outputId="b11092d9-2217-46f5-cb25-dd3456d933b6">

``` python
X
```

<div class="output execute_result" execution_count="6">

    matrix([[-0.65076261, -1.20035326],
            [-0.09695389,  1.92245365],
            [-1.68086995, -0.07834043],
            [-0.36796486, -1.08722747],
            [-1.22895473, -0.60085082],
            [ 1.67226228,  0.59476797],
            [ 0.26863138, -0.74626433],
            [-1.9588259 ,  0.20587107],
            [ 0.23846154, -0.17433093],
            [ 0.20481741,  1.07818571]])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="jCZwf8CVvNmA" outputId="7785b2c9-08c3-4aaa-8156-a0ae6df886b5">

``` python
y
```

<div class="output execute_result" execution_count="7">

    matrix([[-1],
            [ 1],
            [-1],
            [-1],
            [-1],
            [ 1],
            [-1],
            [-1],
            [-1],
            [ 1]])

</div>

</div>

<div class="cell markdown" id="XcZOKwG7OXYO">

Graficamos la data con los colores rojo correspondiente a la clase $`y=1`$ y azul a $`y=-1`$.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="AtH5Z6NN33bF" outputId="14aaeb40-43cb-4785-deff-3b16b935d839">

``` python
plt.scatter(data.x1, data.x2, color=data.color)
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.show()
```

<div class="output display_data">

![](77805b079240bbcf49edc3f3b421e2e4d8d75ad1.png)

</div>

</div>

<div class="cell markdown" id="ZTSWS08CyG1s">

Problema original \begin{eqnarray*} min &\quad & \frac{1}{2}\|\|\beta\|\|^2 \\ sa & & y_i(b_0+x^t_i\beta)\geq 1 \quad i=1, \dots, m \\ \\ \end{eqnarray*}

donde $`m`$ es la cantidad de datos.

</div>

<div class="cell markdown" id="JzrRFyXpOf4C">

El problema dual es \begin{eqnarray*} max &\quad & \sum\_{i=1}^m \mu_i - \frac{1}{2}\sum\_{i, j=1}^m \mu_i\mu_jy_iy_jx^t_ix_j \\ sa & & \sum\_{i=1}^m y_i\mu_i=0 \\ & & \mu_i\geq 0, \quad i=1, \dots, m \end{eqnarray*}

</div>

<div class="cell markdown" id="xTL4DZ82Pkq1">

#### **Parte 1**

Escribe este problema en su forma estándar. Para ello debes convertir el problema en un problema de minimización y las inecuaciones deben ser de la forma $`\leq 0`$.

\begin{eqnarray*} min &\quad & -\sum\_{i=1}^m \mu_i + \frac{1}{2}\sum\_{i, j=1}^m \mu_i\mu_jy_iy_jx^t_ix_j \\ sa & & \sum\_{i=1}^m y_i\mu_i=0 \\ & & -\mu_i\leq 0, \quad i=1, \dots, m \end{eqnarray*}

</div>

<div class="cell markdown" id="aC6tOHrAPMHd">

#### **Parte 2**

Halla la matriz Hessiana de la función objetivo. Almacena esta matriz en una variable.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="-osfPbo2h8Eg" outputId="be9bd5af-93c0-406c-f0fb-e60efe43f16f">

``` python
np.matmul(X, np.transpose(X))
```

<div class="output execute_result" execution_count="9">

    matrix([[ 1.86433993, -2.24452955,  1.1878835 ,  1.54451481,  1.52099102,
             -1.80217743,  0.72096557,  1.02761264,  0.05407684, -1.42749124],
            [-2.24452955,  3.7052281 ,  0.01236104, -2.05446879, -1.0359559 ,
              0.98128151, -1.46070345,  0.58569339, -0.35826291,  2.0529042 ],
            [ 1.1878835 ,  0.01236104,  2.83146103,  0.70367495,  2.112784  ,
             -2.8574498 , -0.39307175,  3.27640358, -0.38716569, -0.42873697],
            [ 1.54451481, -2.05446879,  0.70367495,  1.31746171,  1.10547367,
             -1.26198183,  0.71251217,  0.49695042,  0.1017919 , -1.24759873],
            [ 1.52099102, -1.0359559 ,  2.112784  ,  1.10547367,  1.87135144,
             -2.41250146,  0.11825773,  2.28361056, -0.18831156, -0.89954009],
            [-1.80217743,  0.98128151, -2.8574498 , -1.26198183, -2.41250146,
              3.15021007,  0.00536801, -3.15322515,  0.29508379,  0.98377875],
            [ 0.72096557, -1.46070345, -0.39307175,  0.71251217,  0.11825773,
              0.00536801,  0.62907327, -0.67983635,  0.19415521, -0.74959115],
            [ 1.02761264,  0.58569339,  3.27640358,  0.49695042,  2.28361056,
             -3.15322515, -0.67983635,  3.87938182, -0.50299435, -0.1792344 ],
            [ 0.05407684, -0.35826291, -0.38716569,  0.1017919 , -0.18831156,
              0.29508379,  0.19415521, -0.50299435,  0.08725518, -0.13912004],
            [-1.42749124,  2.0529042 , -0.42873697, -1.24759873, -0.89954009,
              0.98377875, -0.74959115, -0.1792344 , -0.13912004,  1.20443459]])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="pDVLIGTbh--t" outputId="321f7734-4ce0-4190-99ec-e4f365add627">

``` python
np.matmul(y, np.transpose(y))
```

<div class="output execute_result" execution_count="10">

    matrix([[ 1, -1,  1,  1,  1, -1,  1,  1,  1, -1],
            [-1,  1, -1, -1, -1,  1, -1, -1, -1,  1],
            [ 1, -1,  1,  1,  1, -1,  1,  1,  1, -1],
            [ 1, -1,  1,  1,  1, -1,  1,  1,  1, -1],
            [ 1, -1,  1,  1,  1, -1,  1,  1,  1, -1],
            [-1,  1, -1, -1, -1,  1, -1, -1, -1,  1],
            [ 1, -1,  1,  1,  1, -1,  1,  1,  1, -1],
            [ 1, -1,  1,  1,  1, -1,  1,  1,  1, -1],
            [ 1, -1,  1,  1,  1, -1,  1,  1,  1, -1],
            [-1,  1, -1, -1, -1,  1, -1, -1, -1,  1]])

</div>

</div>

<div class="cell code" id="lnRwhKZyiBZU">

``` python
P=matrix(np.multiply(np.matmul(X, np.transpose(X)),np.matmul(y, np.transpose(y))))
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="Hx44HXevizDT" outputId="70f5d6b0-f9a5-4a71-86bc-b21f19f96e05">

``` python
P
```

<div class="output execute_result" execution_count="12">

    <10x10 matrix, tc='d'>

</div>

</div>

<div class="cell markdown" id="4O3R9nuWQIxM">

#### **Parte 3**

Revisa la documentación de solvers.qp y explora los inputs que necesita la función para conseguir hallar los valores de $`\mu_i`$.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:186}" id="CAUOQVucU7XL" outputId="a09e72b9-1720-4add-8cf2-b966a080e4d6">

``` python
solvers.qp
```

<div class="output execute_result" execution_count="13">

    <function cvxopt.coneprog.qp(P, q, G=None, h=None, A=None, b=None, solver=None, kktsolver=None, initvals=None, **kwargs)>

</div>

</div>

<div class="cell markdown" id="OMeURMNkQ2eU">

#### **Parte 4**

Halla los inputs que necesita la función solvers.qp. Nota que las matrices deben ser objetos *matrix* (de cvxopt) y sus entradas deben ser números reales (no enteros).

</div>

<div class="cell code" id="l-ch3VTGiGEu">

``` python
q=matrix(np.repeat(-1.0, 10))
G=matrix(-np.eye(10))
h=matrix(np.transpose(np.repeat(0., 10)))
A=matrix(np.transpose(y), tc="d")
b=matrix([[0.]])
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="H5lBK9bOst0y" outputId="2e77392a-ed37-4830-c568-3430124eadbe">

``` python
h
```

<div class="output execute_result" execution_count="15">

    <10x1 matrix, tc='d'>

</div>

</div>

<div class="cell markdown" id="uVj8rIL9RMLG">

#### **Parte 5**

Utiliza la función solvers.qp para hallar los $`\mu_i`$. Reconoce cuáles de ellos son distintos de $`0`$. Estos valores son importantes pues corresponden a los vectores de soporte del hiperplano.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="9tdoIWRuQELw" outputId="f5e6da28-ef76-4705-bc3a-db1722886632">

``` python
sol=solvers.qp(P=P, q=q, G=G, h=h, A=A, b=b)
```

<div class="output stream stdout">

         pcost       dcost       gap    pres   dres
     0: -1.3475e+00 -3.0543e+00  2e+01  4e+00  2e+00
     1: -1.4414e+00 -2.3660e+00  2e+00  3e-01  1e-01
     2: -1.3589e+00 -1.5123e+00  2e-01  5e-16  6e-16
     3: -1.4338e+00 -1.4399e+00  6e-03  3e-16  5e-16
     4: -1.4385e+00 -1.4386e+00  6e-05  2e-16  4e-16
     5: -1.4386e+00 -1.4386e+00  6e-07  2e-16  2e-16
    Optimal solution found.

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="Qb14HJUrFVDW" outputId="36899d1e-9127-49e3-99af-e08c4c6f7c2c">

``` python
sol
```

<div class="output execute_result" execution_count="17">

    {'x': <10x1 matrix, tc='d'>,
     'y': <1x1 matrix, tc='d'>,
     's': <10x1 matrix, tc='d'>,
     'z': <10x1 matrix, tc='d'>,
     'status': 'optimal',
     'gap': 6.100045218566044e-07,
     'relative gap': 4.240385127226085e-07,
     'primal objective': -1.4385592429800085,
     'dual objective': -1.4385598529845303,
     'primal infeasibility': 2.288783403339746e-16,
     'dual infeasibility': 2.330932792347465e-16,
     'primal slack': 9.48637933373363e-09,
     'dual slack': 1.6814745599344546e-08,
     'iterations': 5}

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="ge6UKxMVzjPO" outputId="a8112ab0-d896-4ffe-c867-8013f26404fc">

``` python
u=np.transpose(sol["x"])
u=u.flatten()
u
```

<div class="output execute_result" execution_count="18">

    array([3.52405076e-08, 4.04467526e-08, 9.23346864e-08, 1.10051332e-08,
           3.27947548e-08, 3.94645492e-01, 9.48637933e-09, 3.58990507e-07,
           1.43855901e+00, 1.04391402e+00])

</div>

</div>

<div class="cell markdown" id="so7lCOTRUFdR">

#### **Parte 6**

Halla los valores de los coeficientes $`\beta=(b_1, \dots, b_n)`$ usando la relación

``` math
\beta=\sum_{i=1}^m \mu_iy_ix_i
```

donde $`x_i`$ es el vector correspondiente a la fila $`i`$ en nuestra data.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="o7BMehCViR-P" outputId="3f615805-cfd4-42d6-a507-445caf549ba5">

``` python
beta=np.matmul(np.multiply(u, np.transpose(y)), X)
print(beta)
b1=beta[0, 0]
b2=beta[0, 1]
print(b1, b2)
```

<div class="output stream stdout">

    [[0.53072245 1.61104109]]
    0.5307224534150436 1.6110410868162792

</div>

</div>

<div class="cell markdown" id="jCJAHgFaVYoW">

#### **Parte 7**

Halla el valor de $`b_0`$ utilizando una entrada que corresponda a un vector de soporte. Los vectores de soporte son tales que $`\mu_i\neq 0`$. En este caso se cumple la igualdad
``` math
y_i(b_0+x^t_i\beta)=1.
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="Jp4tauD8WD6t" outputId="ccbbe3b6-f994-4245-ed12-4eb2372fbfe9">

``` python
np.set_printoptions(precision=4)
print(u)
```

<div class="output stream stdout">

    [3.5241e-08 4.0447e-08 9.2335e-08 1.1005e-08 3.2795e-08 3.9465e-01
     9.4864e-09 3.5899e-07 1.4386e+00 1.0439e+00]

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="UqrQ2w6ujpHo" outputId="9c813621-d092-4c89-ef09-0b4c9292b0fd">

``` python
u[8]
```

<div class="output execute_result" execution_count="21">

    np.float64(1.438559008130301)

</div>

</div>

<div class="cell markdown" id="gcl0YGk9j53q">

$`b_0=\frac{1}{y_i}-x^t_i\beta`$

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="yEMfyi_jjwxg" outputId="5777b1f2-4b87-417e-f5c3-903f6fefa70f">

``` python
y[9, 0] # y_9
```

<div class="output execute_result" execution_count="22">

    np.int64(1)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="cuJGnjUTkI2W" outputId="0ae615c3-7cf0-4ee1-a533-506951309fbd">

``` python
b0=1/y[9, 0]-(X[9, 0]*b1+X[9, 1]*b2)
b0
```

<div class="output execute_result" execution_count="23">

    np.float64(-0.8457026705802144)

</div>

</div>

<div class="cell markdown" id="eYoNu2b3WEzn">

#### **Parte 8**

Grafica el hiperplano hallado con la data.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="84Zn0b1Y1bjh" outputId="a8a020db-d36c-4e5c-f1e6-50f39100dbfe">

``` python
plt.scatter(data.x1, data.x2, c=data["color"])
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
b=-b0/b2
m=-b1/b2
x=np.arange(-2,2,0.01)
plt.plot(x, b+m*x)
#plt.savefig('imagen1.png', dpi=300)

plt.scatter(data.x1[[5, 8, 9]], data.x2[[5, 8, 9]], c="black")
plt.show()
```

<div class="output display_data">

![](383b0af6b6576357e6e41ec4421937f83f525bf5.png)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="Cta5bspM2B41" outputId="75010a2b-9a9f-4293-eaa0-c14fbf73b876">

``` python
M=1/np.linalg.norm(beta)
M
```

<div class="output execute_result" execution_count="25">

    np.float64(0.5895505300943907)

</div>

</div>

<div class="cell markdown" id="C_UYyKruWMLg">

#### **Parte 9**

Utilizamos el paquete sklearn para hallar el hiperplano.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:135}" id="uxB882O9AuXr" outputId="529ffc78-abf9-4f8d-a2b5-0a8090e98ea2">

``` python
from sklearn import svm
clf = svm.SVC(C=10000, kernel="linear") # Imponemos un valor de C muy alto para que corresponda al clasificador de máximo margen

X=np.array(data[["x1", "x2"]])
y=np.array(data[["y"]])

clf.fit(X, y) # Entrenamos el modelo que queda almacenado en clf
```

<div class="output stream stderr">

    /usr/local/lib/python3.11/dist-packages/sklearn/utils/validation.py:1408: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().
      y = column_or_1d(y, warn=True)

</div>

<div class="output execute_result" execution_count="26">

    SVC(C=10000, kernel='linear')

</div>

</div>

<div class="cell markdown" id="5_ke1SOMWc4a">

#### **Parte 10**

Obten los coeficientes del modelo entrenado. Investiga los atributos del objeto clf.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="ATblGeF5LtNU" outputId="35beb0a8-c14d-41a9-d144-bf2f60c10e69">

``` python
clf.coef_
```

<div class="output execute_result" execution_count="27">

    array([[0.53032422, 1.61103029]])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="S9MQKbedLvlS" outputId="80dce699-1f0b-459e-e748-f61fba89ee3f">

``` python
clf.intercept_
```

<div class="output execute_result" execution_count="28">

    array([-0.8454165])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="n2IWabrwkWKz" outputId="5f12fa18-3f35-4513-8886-a5d956b6b4c0">

``` python
clf.support_
```

<div class="output execute_result" execution_count="29">

    array([8, 5, 9], dtype=int32)

</div>

</div>
