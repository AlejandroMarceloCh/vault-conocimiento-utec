---
curso: OPTI
titulo: 11_Lab_minimos_cuadrados
slides: 0
fuente: 11_Lab_minimos_cuadrados.ipynb
---

<div class="cell markdown" id="1SDlcP4peY86">

# Aplicación a mínimos cuadrados no lineales

Descarguemos el archivo minimos_cuadrados.csv

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="grJYn812UoWk" outputId="165542b1-8019-40d3-9fd6-21ea3fa49a92">

``` python
!gdown 1qqiRr7w-Wz-3LTcTY1GbbZYjz_8ycaOH
```

<div class="output stream stdout">

    Downloading...
    From: https://drive.google.com/uc?id=1qqiRr7w-Wz-3LTcTY1GbbZYjz_8ycaOH
    To: /content/minimos_cuadrados.csv
    
  0% 0.00/725 [00:00<?, ?B/s]
100% 725/725 [00:00<00:00, 2.28MB/s]

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:356}" id="cHUn0GspeY86" outputId="9b98463f-e00d-41bf-f259-9f7510a265d8">

``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("minimos_cuadrados.csv")

plt.scatter(data.x, data.y)
```

<div class="output error" ename="FileNotFoundError" evalue="[Errno 2] No such file or directory: 'minimos_cuadrados.csv'">

    ---------------------------------------------------------------------------
    FileNotFoundError                         Traceback (most recent call last)
    <ipython-input-4-db060dc96017> in <cell line: 0>()
          3 import matplotlib.pyplot as plt
          4 
    ----> 5 data=pd.read_csv("minimos_cuadrados.csv")
          6 
          7 plt.scatter(data.x, data.y)

    /usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py in read_csv(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)
       1024     kwds.update(kwds_defaults)
       1025 
    -> 1026     return _read(filepath_or_buffer, kwds)
       1027 
       1028 

    /usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py in _read(filepath_or_buffer, kwds)
        618 
        619     # Create the parser.
    --> 620     parser = TextFileReader(filepath_or_buffer, **kwds)
        621 
        622     if chunksize or iterator:

    /usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py in __init__(self, f, engine, **kwds)
       1618 
       1619         self.handles: IOHandles | None = None
    -> 1620         self._engine = self._make_engine(f, self.engine)
       1621 
       1622     def close(self) -> None:

    /usr/local/lib/python3.11/dist-packages/pandas/io/parsers/readers.py in _make_engine(self, f, engine)
       1878                 if "b" not in mode:
       1879                     mode += "b"
    -> 1880             self.handles = get_handle(
       1881                 f,
       1882                 mode,

    /usr/local/lib/python3.11/dist-packages/pandas/io/common.py in get_handle(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)
        871         if ioargs.encoding and "b" not in ioargs.mode:
        872             # Encoding
    --> 873             handle = open(
        874                 handle,
        875                 ioargs.mode,

    FileNotFoundError: [Errno 2] No such file or directory: 'minimos_cuadrados.csv'

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:206}" id="nsyYrlhvTG1j" outputId="72c5647b-2349-4510-f058-330ca541c07e">

``` python
data.head()
```

<div class="output execute_result" execution_count="20">

``` json
{"summary":"{\n  \"name\": \"data\",\n  \"rows\": 20,\n  \"fields\": [\n    {\n      \"column\": \"x\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2.9576560408895363,\n        \"min\": 0.301361330784857,\n        \"max\": 9.44970469223335,\n        \"num_unique_values\": 20,\n        \"samples\": [\n          4.3140128813684,\n          2.60232345899567,\n          1.74768718192354\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"y\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1.473619189842487,\n        \"min\": -2.00192944365582,\n        \"max\": 2.11733900310244,\n        \"num_unique_values\": 20,\n        \"samples\": [\n          -1.81343596714406,\n          0.773556531046186,\n          1.38038375820884\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe","variable_name":"data"}
```

</div>

</div>

<div class="cell markdown" id="exL_LH6SeY87">

Buscaremos encontrar la "mejor" función
``` math
y=A sen(\omega x+\phi),
```
es decir, los parámetros $`A, \omega`$ y $`\phi`$ que minimizan el error cuadrático. Para ello utilizaremos el Método de Gauss-Newton.

</div>

<div class="cell code" id="AST8yRcAZLjZ">

``` python
def predichos(parametros):
  A=parametros[0]
  omega=parametros[1]
  phi=parametros[2]
  predichos=A*np.sin(omega*np.array(data["x"])+phi)
  return predichos
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="9IXhNrl0ZkJ6" outputId="7455e46d-7bfd-454a-9534-c143a85ba73e">

``` python
A=1
omega=0.5
phi=1
parametros=[A, omega, phi]
predichos(parametros)
```

<div class="output execute_result" execution_count="21">

    array([-0.01541318,  0.9809444 , -0.54934845, -0.52977305, -0.12309674,
           -0.30741609, -0.72040643,  0.17324158,  0.91890925,  0.95651218,
            0.46951596, -0.72517517, -0.99474205,  0.00881372,  0.41890306,
            0.95443153, -0.72570322,  0.74493068, -0.91015535,  0.91304177])

</div>

</div>

<div class="cell code" id="UrwjGBjtZCWc">

``` python
def residuos(parametros):
  r=np.array(data["y"])-predichos(parametros)
  return r
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="_4s_LDx3Z8Hq" outputId="2310a335-a12d-45e6-c034-88e3db2eb5a2">

``` python
r=residuos(parametros)
r.T
```

<div class="output execute_result" execution_count="7">

    array([-1.79802279,  1.13639461,  1.28285876,  1.42943857, -1.85516062,
           -1.69451335,  2.4301324 , -1.51897761,  0.55362392,  0.61219694,
           -1.42557421,  2.30124108,  2.86146609, -1.80574342, -1.2834856 ,
            0.42595223,  0.04856201,  0.02862585,  1.36221848,  0.43907895])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="inkPIn0KaEbw" outputId="02d899af-5e02-4afd-e95e-3e109eed04cc">

``` python
np.mean(r**2)
```

<div class="output execute_result" execution_count="8">

    np.float64(2.303873243966809)

</div>

</div>

<div class="cell code" id="YVQPtUxbXu-w">

``` python
def gradiente(parametros):
  A=parametros[0]
  omega=parametros[1]
  phi=parametros[2]
  n=len(data)
  r=residuos(parametros)
  parcial_r_A=-np.sin(omega*np.array(data["x"])+phi)
  parcial_r_omega=-A*np.cos(omega*np.array(data["x"])+phi)*np.array(data["x"])
  parcial_r_phi=-A*np.cos(omega*np.array(data["x"])+phi)
  componente_1=2/n*np.dot(r, parcial_r_A)
  componente_2=2/n*np.dot(r, parcial_r_omega)
  componente_3=2/n*np.dot(r, parcial_r_phi)
  return np.array([componente_1, componente_2, componente_3])
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="u_KXQ9E7bK8j" outputId="b15d1d48-ccfc-4df0-b038-f8fa26ba1e97">

``` python
gradiente(parametros)
```

<div class="output execute_result" execution_count="10">

    array([ 0.66742384, -9.39955613, -1.59989904])

</div>

</div>

<div class="cell markdown" id="HQdLila9ehAq">

## Con gradiente descendiente

</div>

<div class="cell code" id="i3RTsYC4ei2a">

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

    x0 = x0-alpha*gradiente(x0)

    tol = np.linalg.norm(alpha*gradiente(x0))

    iteraciones += 1
  return x0, valores, iteraciones
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="6dzs-MrGekrC" outputId="d24c03d4-6752-4689-d0bd-afb56610a41e">

``` python
x0=np.random.rand(3)
x0
```

<div class="output execute_result" execution_count="35">

    array([0.40394216, 0.75010222, 0.86772364])

</div>

</div>

<div class="cell code" id="gJF3_OoCe5iC">

``` python
def f(parametros):
  r=residuos(parametros)
  return np.mean(r**2)
```

</div>

<div class="cell code" id="C5iGTftqe4X5">

``` python
alpha=0.01
epsilon=10**-6
max_iteraciones=10**4
parametros, valores, iteraciones=gradiente_descendiente(f, gradiente, alpha, x0, epsilon, max_iteraciones)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="XLACh0uKgWfC" outputId="dafde2b0-c8bc-4fde-eb11-02b628f9cd1d">

``` python
parametros
```

<div class="output execute_result" execution_count="38">

    array([1.97741175, 0.89990969, 0.51938004])

</div>

</div>

<div class="cell code" id="9Ncd68yr8YNQ">

``` python
def fit(x, parametros):
  A=parametros[0]
  omega=parametros[1]
  phi=parametros[2]
  return A*np.sin(omega*x+phi)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:447}" id="p4vleTii8YQF" outputId="eb9ee7f2-9f92-409a-957b-ce3acc8ec8b5">

``` python
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.001)
y = np.array([fit(t, parametros) for t in x])

plt.scatter(data.x, data.y)
plt.plot(x, y)
```

<div class="output execute_result" execution_count="40">

    [<matplotlib.lines.Line2D at 0x78808be1bdd0>]

</div>

<div class="output display_data">

![](7ad1de5bcbf98bbc8e24a9a47e0ce9fdcb9806f4.png)

</div>

</div>

<div class="cell markdown" id="B6EPUEXokFpE">

## Gauss-Newton

</div>

<div class="cell code" id="XQzQejbmkSxj">

``` python
def Jacobiano(parametros):
  A=parametros[0]
  omega=parametros[1]
  phi=parametros[2]
  n=len(data)
  r=residuos(parametros)
  columna_1=-np.sin(omega*np.array(data["x"])+phi)
  columna_2=-A*np.cos(omega*np.array(data["x"])+phi)*np.array(data["x"])
  columna_3=-A*np.cos(omega*np.array(data["x"])+phi)
  J=np.matrix([columna_1, columna_2, columna_3])
  J=np.transpose(J)
  return J
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="BVWDE7j-ddN4" outputId="030fc3de-bdaf-4664-8704-cc1607ff07e8">

``` python
Jacobiano([1, 1, 1])
```

<div class="output execute_result" execution_count="45">

    matrix([[ 0.8244176 , -2.4416536 , -0.56598199],
            [-0.5719946 ,  1.25717337,  0.82025738],
            [ 0.82961851,  5.250096  ,  0.55833066],
            [ 0.85467615,  4.90592295,  0.51916151],
            [ 0.68396244, -3.30471656, -0.72951723],
            [ 0.36631638, -4.56697525, -0.93049036],
            [ 0.50796131,  7.71589158,  0.86137989],
            [ 0.97533643, -0.86853482, -0.22072349],
            [-0.18789661,  1.91779485,  0.98218881],
            [-0.99977539, -0.01164796, -0.02119348],
            [ 0.91843574,  1.30763661,  0.39557022],
            [ 0.49602522,  7.76596812,  0.86830811],
            [-0.71373469,  5.34414869,  0.70041616],
            [ 0.85086403, -2.24106409, -0.52538596],
            [ 0.95718579,  0.98962901,  0.28947428],
            [-0.38379771,  1.6138444 ,  0.92341719],
            [-0.58437684, -4.79366781, -0.81148241],
            [ 0.44460283,  2.33097352,  0.89572782],
            [-0.96008832, -1.83774998, -0.27969699],
            [-0.96392145, -0.08021843, -0.26618686]])

</div>

</div>

<div class="cell code" id="J2Sh6_C1k_HY">

``` python
def Gauss_Newton(parametros_iniciales, Jacobiano, residuos, epsilon, max_iter):
  parametros=parametros_iniciales
  tol=epsilon+1
  iter=1
  while tol>epsilon:
    J=Jacobiano(parametros)
    r=residuos(parametros)
    cambio=-(r@J)@np.linalg.inv(J.T@J)
    parametros=parametros+cambio.tolist()[0]
    tol=np.linalg.norm(cambio)
    if iter==max_iter:
      print("El método no convergió en ", max_iter, " iteraciones.")
  return parametros
```

</div>

<div class="cell code" id="KomPXhvjmHn7">

``` python
parametros_iniciales=np.random.rand(3)
epsilon=10**-6
max_iter=10**3
parametros=Gauss_Newton(parametros_iniciales, Jacobiano, residuos, epsilon, max_iter)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="mWlvDldvPB09" outputId="9985b7ba-a9af-476d-93ec-a6b103859985">

``` python
parametros
```

<div class="output execute_result" execution_count="73">

    array([1.97748801, 0.89992679, 0.51926841])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="u64_W-WZvj34" outputId="717a68bd-c131-47ff-e51a-b22c7d379d70">

``` python
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.001)
y = np.array([fit(t, parametros) for t in x])

plt.scatter(data.x, data.y)
plt.plot(x, y)
plt.show()
```

<div class="output display_data">

![](319323bd2ed1fb05c4911d65640bd5caec3ce3e8.png)

</div>

</div>

<div class="cell markdown" id="dzHXMaRZjeJg">

## **Ejercicio 1:**

Descarga el archivo data_exponencial.csv. Estimaremos los coeficientes de un modelo

``` math
y=f(x)=b_0e^{b_1 x}
```

a\) Carga la data y realiza un scatterplot de x e y.

b\) Implementa la función $`f`$ en python. Debe recibir como entrada a $`x`$ y a los parámetros.

c\) Implementa la función $`r`$ que recibe como input a los parámetros y da como output los residuos.

d\) Implementa la matriz Jacobiana de $`r`$ que recibe como input los parámetros y da como output la matriz Jacobiana.

e\) Implementa el algoritmo de Gauss-Newton con la modificación de Levenberg-Marquardt.

- Debe tener como inputs a la matriz Jacobiana, r, los parametros iniciales, mu, la tolerancia y la cantidad máxima de iteraciones.
- Debe tener como output a los parámetros entrenados y graficar un plot del valor de la función respecto del número de iteración.

f\) Grafica la función con los parámetros entrenados sobre el scatterplot.

g\) Utiliza scipy.optimize.curve_fit para obtener los parámetros y compáralos con tus resultados.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="UnEc48meVT-s" outputId="ace453cd-f55b-4b69-c7e1-d8341c61aa7d">

``` python
!gdown 1l22tLFImTtU9OAl1YFkmyEb720-iK9nT
```

<div class="output stream stdout">

    Downloading...
    From: https://drive.google.com/uc?id=1l22tLFImTtU9OAl1YFkmyEb720-iK9nT
    To: /content/data_exponencial.csv
    
  0% 0.00/2.10k [00:00<?, ?B/s]
100% 2.10k/2.10k [00:00<00:00, 6.51MB/s]

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="rLXFXzwxrfOz" outputId="2e3f4833-604a-4bf4-a140-bf46e09a975a">

``` python
data_exponencial=pd.read_csv("data_exponencial.csv")

plt.scatter(data_exponencial[0:10].x, data_exponencial[0:10].y)
plt.show()
```

<div class="output display_data">

![](8238835e5cea29bc4ca240d52c47e8c7d5e97bb0.png)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:363}" id="HLdfB-AjZRzS" outputId="4c4b307b-0a91-4a85-bdec-939ba1b63f4e">

``` python
data_exponencial[0:10]
```

<div class="output execute_result" execution_count="9">

``` json
{"summary":"{\n  \"name\": \"data_exponencial[0:10]\",\n  \"rows\": 10,\n  \"fields\": [\n    {\n      \"column\": \"x\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3.205286284110826,\n        \"min\": -3.4271251806058,\n        \"max\": 4.94722219416872,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          -3.4271251806058,\n          4.94722219416872,\n          3.27657676767558\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"y\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2.189762839303006,\n        \"min\": 0.368388351616117,\n        \"max\": 6.09799046830022,\n        \"num_unique_values\": 10,\n        \"samples\": [\n          0.661159684336922,\n          6.09799046830022,\n          3.93305054672055\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}","type":"dataframe"}
```

</div>

</div>

<div class="cell code" id="tUISuaoPpPfo">

``` python
def predichos(parametros):
  # parametros =[b0, b1]
  b0=parametros[0]
  b1=parametros[1]
  predichos=b0*np.exp(b1*np.array(data_exponencial["x"]))
  return predichos
```

</div>

<div class="cell code" id="AQs5nIB1o8CA">

``` python
def residuos(parametros):
  r=np.array(data_exponencial["y"])-predichos(parametros)
  return r
```

</div>

<div class="cell code" id="Z7mK2EgmonYR">

``` python
def Jacobiano(parametros):
  b0=parametros[0]
  b1=parametros[1]
  n=len(data_exponencial)
  columna_1=-np.exp(b1*np.array(data_exponencial["x"]))
  columna_2=-b0*np.exp(b1*np.array(data_exponencial["x"]))*np.array(data_exponencial["x"])
  J=np.matrix([columna_1, columna_2])
  J=np.transpose(J)
  return J
```

</div>

<div class="cell code" id="Y6Sbf-KJqGIK">

``` python
parametros_iniciales=np.random.rand(2)
epsilon=10**-6
max_iter=10**3
parametros=Gauss_Newton(parametros_iniciales, Jacobiano, residuos, epsilon, max_iter)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="sow58R2aqP-q" outputId="628a2f84-7d66-49dd-b687-c4ceca6222fa">

``` python
parametros
```

<div class="output execute_result" execution_count="101">

    array([1.3911336 , 0.30051746])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="OZiQ2hPVqXKE" outputId="079c8ba5-96c5-4e0c-ce77-4697836b4589">

``` python
import matplotlib.pyplot as plt

x = np.arange(-4, 5, 0.001)
y = np.array([parametros[0]*np.exp(parametros[1]*t) for t in x])

plt.scatter(data_exponencial.x, data_exponencial.y)
plt.plot(x, y)
plt.show()
```

<div class="output display_data">

![](1abeaf94510c453734b97747d84e21d45950df84.png)

</div>

</div>

<div class="cell markdown" id="atdw0OBRnadO">

# **Ejercicio 2:**

Descarga el archivo data_cubica.csv. Estima los coeficientes del modelo. Corrobora tu resultado con un plot de las variables y la función estimada.

``` math
y=b_0+b_1x+b_2x^2+b_3x^3
```

</div>

<div class="cell code" id="ygmSPwV2VckT">

``` python
!gdown 17pez27NXzv0Sr_toVSX_fFTj-S37msUp
```

</div>

<div class="cell code" id="p4QxEiiJVfb3">

``` python
```

</div>
