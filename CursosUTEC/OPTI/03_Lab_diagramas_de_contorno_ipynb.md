---
curso: OPTI
titulo: 03_Lab_diagramas_de_contorno
slides: 0
fuente: 03_Lab_diagramas_de_contorno.ipynb
---

<div class="cell markdown" id="ffwwhvwuDP1b">

# Diagrama de contorno de una función de 2 variables

</div>

<div class="cell code" id="VnUcfjkUCfS8">

``` python
import numpy as np
import matplotlib.pyplot as plt
```

</div>

<div class="cell markdown" id="4NgrhsRYNFYT">

Implementamos la función
``` math
f(x, y)=x^2+y^2
```

</div>

<div class="cell code" id="iH6vDyonNE4z">

``` python
def f(x, y):
    return x**2+y**2
```

</div>

<div class="cell markdown" id="Cl87kdK8O9DU">

Creamos un arreglo de valores en el plano cartesiano

</div>

<div class="cell code" id="jBEW2bkOPCqa">

``` python
x = np.arange(-10,10,0.02) # límites para x y el tamaño de paso
y = np.arange(-10,10,0.02) # límites para y y el tamaño de paso
X,Y= np.meshgrid(x,y)      # almacenamos los valores del grid.
```

</div>

<div class="cell markdown" id="i4xA7AYxPElC">

Evaluamos la función en todos esos valores

</div>

<div class="cell code" id="gRZq8Ol2PHUb">

``` python
Z = f(X,Y)
```

</div>

<div class="cell markdown" id="H3jLsfD0PJS7">

Creamos un objeto Axes llamado ax, aplicamos el método contour y luego agregamos las etiquetas. Estos 3 comandos deben estar en la misma celda.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="JsiiWvpADGes" outputId="543e1446-fca9-4d5f-e3da-b4b6e2c15afe">

``` python
fig, ax = plt.subplots(1, 1)
CS=ax.contour(X,Y,Z, levels=[1,  10, 30,  100],  linewidths=1) # Especificamos los niveles a dibujar.
ax.clabel(CS, inline=True, fontsize=8)
plt.show()
```

<div class="output display_data">

![](7e5ad30070c6128a6b340bbe2d36c34725042103.png)

</div>

</div>

<div class="cell markdown" id="VKNpnyggSBBH">

Implementemos una función que reciba como input

- La función a graficar
- Los límites para x
- Los límites para y
- Los niveles a graficar

y que de como output

- El diagrama de contorno de la función

</div>

<div class="cell code" id="AVnLvF8SSQ-B">

``` python
def diagrama_contorno(f, xmin, xmax, ymin, ymax, niveles):
  x = np.arange(xmin,xmax,0.02) # límites para x y el tamaño de paso
  y = np.arange(ymin,ymax,0.02) # límites para y y el tamaño de paso
  X,Y= np.meshgrid(x,y)      # almacenamos los valores del grid.
  Z = f(X,Y)
  fig, ax = plt.subplots(1, 1)
  CS=ax.contour(X,Y,Z, levels=niveles,  linewidths=1) # Especificamos los niveles a dibujar.
  ax.clabel(CS, inline=True, fontsize=8)
  plt.close(fig)
  return fig
```

</div>

<div class="cell markdown" id="uVSsSGeUdvkD">

Probamos nuestra función con
``` math
f(x, y)=x^2+y^2
```

</div>

<div class="cell code" id="PqemFc9zTEQK">

``` python
def f(x, y):
    return x**2+y**2
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="Ip-4B4Q8Sqkh" outputId="697e70d8-3b96-4e72-a6f1-fb74c251a825">

``` python
xmin=-2
xmax=2
ymin=-2
ymax=2
niveles=[0.5, 1, 2]
diagrama_contorno(f, xmin, xmax, ymin, ymax, niveles)
```

<div class="output execute_result" execution_count="8">

![](82756d96261bc65fb3c09d01d3cc03cb5add00cf.png)

</div>

</div>

<div class="cell markdown" id="8keLJmoed2x8">

Utilizamos nuestra función para obtener el diagrama de contorno de
``` math
g(x, y)=x^2-y^2
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="fc9G-feoFQ0f" outputId="b64b6f4a-d16c-46ce-efac-62f1186ed2cd">

``` python
def g(x, y):
    return x**2-y**2

xmin=-2
xmax=2
ymin=-2
ymax=2
niveles=[-2, -1, 0, 1, 2]
diagrama_contorno(g, xmin, xmax, ymin, ymax, niveles)
```

<div class="output execute_result" execution_count="9">

![](bcc16a96419347d8b727849864360d7d082c881d.png)

</div>

</div>

<div class="cell markdown" id="KQJGpFX_Z3TA">

Utilizamos nuestra función para obtener el diagrama de contorno de
``` math
h(x, y)=\dfrac{x-y}{x^2+y^2}
```

</div>

<div class="cell code" id="6Ol-WK4DFBXq">

``` python
def h(x, y):
    return (x-y)/(x**2+y**2)

xmin=-2
xmax=2
ymin=-2
ymax=2
niveles=[-10, -6, -1, 0, 1,  6, 10]
fig=diagrama_contorno(h, xmin, xmax, ymin, ymax, niveles)
```

</div>

<div class="cell markdown" id="3LuscRg5eEB7">

Hemos guardado la figura en fig

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="SpzqexX6bWT2" outputId="845c3262-0a0d-4560-fbdb-d01a5386d1ce">

``` python
fig
```

<div class="output execute_result" execution_count="14">

![](07ce9f0801217877864d5a8aa660d11e941076f3.png)

</div>

</div>

<div class="cell markdown" id="2SaYiwRqeINb">

Podemos graficar puntos en el Axes (ver <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html>)

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="r2WB1NHab6Yg" outputId="a4c72b4b-5e5d-4476-dce2-ba5c78e5638f">

``` python
fig=diagrama_contorno(h, xmin, xmax, ymin, ymax, niveles)
ax=fig.get_axes()[0]
ax.plot(1, 1, "ro", ms=5) # Coordenadas del punto y propiedades graficas
fig
```

<div class="output execute_result" execution_count="15">

![](1bc24bcc5e1009bc8be009b6efb9f6b2f6f25454.png)

</div>

</div>

<div class="cell markdown" id="6Tr-bDIcft3W">

# **Ejercicio:**

Grafica el diagrama de contorno de la función

``` math
f(x, y)=10(y-x^2)^2+(1-x)^2
```

y grafica un punto azul cerca de donde se encuentra el mínimo.

**Sugerencia:** Elige los niveles adecuadamente de modo que puedas observar aproximadamente dónde se encuentra el mínimo.

</div>
