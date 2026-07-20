---
curso: OPTI
titulo: 01_Lab_método_de_bisección
slides: 0
fuente: 01_Lab_método_de_bisección.ipynb
---

<div class="cell markdown" id="ZeYW5rW6-eYI">

# <center> El método de bisección </center>

### Gráfica de funciones

</div>

<div class="cell code" id="eUwbMktI-WJ5">

``` python
import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x**2

x = np.arange(-1, 1, 0.01)    # arreglo de posibles valores de x
y=np.array([f(t) for t in x])  # arreglo de las imagenes del arreglo anterior
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:430}" id="oCsbcoIK_A02" outputId="bf4129c9-1229-40f8-cc58-fe39437fd127">

``` python
plt.plot(x, y)
plt.show()
```

<div class="output display_data">

![](c2f1ce86ce37f533f715efe07a397ff4240025eb.png)

</div>

</div>

<div class="cell markdown" id="J7I70WGaAcz3">

### Funciones unimodales

**Ejercicio 1:** Implementa las siguientes funciones.

a\) $`f(x)=x^4-3x^2+2x+1`$

b\) $`g(x)=(x+1)^3+2`$

c\) $`h(x)=e^{2x}+x^4`$

Basandote en la gráfica de tales funciones. ¿Cuáles de ellas son unimodales?

</div>

<div class="cell markdown" id="NeUzCCEdAw-b">

**Ejercicio 2:** Dada la función

$`f(x)=x^4-3x^2+2x+1`$

Utiliza el Método de Bisección para encontrar

a\) Los puntos donde la función alcanza sus mímimos locales con una precisión de $`10^{-5}`$.

b\) El punto donde la función alcanza su máximo local con una precisión de $`10^{-5}`$.

c\) Los valores de los mínimos locales de la función y del máximo local de la función.

</div>

<div class="cell code" id="OG2_Gt3034YM">

``` python
def f_prima(x):
  return 4*x**3-6*x+2
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="heeFIes736Nz" outputId="0d6c7b7d-289a-4bb1-b5db-5a1fe6521a4c">

``` python
a=-2
b=-1

while abs(b-a)/2>10**(-5):
  x=(a+b)/2
  if f_prima(x)>0:
    b=x
  else:
    a=x

print(x)
```

<div class="output stream stdout">

    -1.3660125732421875

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="hDM4Q9Kr9vC0" outputId="69eb8392-0553-4cd9-abcd-3ba837ea0f2f">

``` python
a=-1
b=1

while abs(b-a)/2>10**(-5):
  x=(a+b)/2
  if -f_prima(x)>0:
    b=x
  else:
    a=x

print(x)
```

<div class="output stream stdout">

    0.3660125732421875

</div>

</div>

<div class="cell markdown" id="aqvDquNNSBxj">

**Ejercicio 3:**

a\) Implementa el método de bisección en una función. Que reciba como inputs:

- La derivada de la función objetivo
- Los límites del intervalo donde encontraremos el mínimo
- La precisión y que de como output al mínimo de la función en dicho intervalo.

b\) Utilizando la función de a), halla el mínimo de $`h(x)=e^{2x}+x^4`$ con una precisión de $`10^{-5}`$.

</div>

<div class="cell code" id="Dp0IGpruHU17">

``` python
def biseccion(f_prima, a, b, epsilon):
  tol=epsilon+1
  while tol>epsilon:
    x=(a+b)/2
    if f_prima(x)>0:
      b=x
    else:
      a=x
    tol=b-a
  return x
```

</div>

<div class="cell code" id="Jpp-TLrnIceJ">

``` python
def f_prima(x):
  return 2*np.exp(2*x)+4*x**3
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="98fmMpI1Ihg1" outputId="b2821ea4-6d03-40e2-b42e-18e242c1639b">

``` python
biseccion(f_prima, -2, 2, 10**-5)
```

<div class="output execute_result" execution_count="10">

    -0.5500411987304688

</div>

</div>
