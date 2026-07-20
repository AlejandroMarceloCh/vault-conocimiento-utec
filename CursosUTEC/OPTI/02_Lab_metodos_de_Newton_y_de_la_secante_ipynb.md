---
curso: OPTI
titulo: 02_Lab_métodos_de_Newton_y_de_la_secante
slides: 0
fuente: 02_Lab_métodos_de_Newton_y_de_la_secante.ipynb
---

<div class="cell markdown" id="Fw6tA_-VR4uR">

# Método de Newton

## **Ejercicio 1:**

Considere la función
``` math
f(x)=e^{x^2}+(2x-1)^3.
```

a\) Implemente y grafique la función $`f`$.

b\) Implemente $`f'`$ y $`f''`$ en funciones de Python.

c\) Utilice el método de Newton para hallar el mínimo.

- Pruebe 3 valores diferentes valores para el punto inicial e indique si el algoritmo converge al valor que minimiza la función en cada caso.
- Considere como condición de parada 100 iteraciones.

d\) Implemente el algoritmo con condición de parada de modo que la precisión sea $`\epsilon=10^{-5}`$.

</div>

<div class="cell code" id="E5ok6iYmjleW">

``` python
from scipy.optimize import minimize_scalar
import numpy as np
```

</div>

<div class="cell code" id="zmIzzJyuk4Yr">

``` python
def f(x):
  return np.exp(x**2)+(2*x-1)**3
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="nTG3uZdrk_Vu" outputId="8b2c6e59-cc71-4bbb-9df8-0856bd2b7e03">

``` python
f(-2)
```

<div class="output execute_result" execution_count="10">

    np.float64(-70.40184996685576)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="0wBWoT2VlBsH" outputId="21a13578-0495-4720-e86e-24044e1a079a">

``` python
f(-1)
```

<div class="output execute_result" execution_count="11">

    np.float64(-24.281718171540955)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="qS5YDHqxlCp1" outputId="1d6e899d-b8f6-4709-b5a5-12c9585ed24e">

``` python
f(-2.01)
```

<div class="output execute_result" execution_count="13">

    np.float64(-69.67398227610927)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="grJN8j2VmplW" outputId="a912dfb1-140a-4dfd-a43c-8994212199a4">

``` python
minimize_scalar(f)
```

<div class="output execute_result" execution_count="14">

     message: 
              Optimization terminated successfully;
              The returned value satisfies the termination criteria
              (using xtol = 1.48e-08 )
     success: True
         fun: -73.63104446232228
           x: -1.895410353051928
         nit: 15
        nfev: 19

</div>

</div>

<div class="cell markdown" id="27HhjAgqSe59">

# Método de la secante

## **Ejercicio 2:**

Considere la función
``` math
f(x)=\dfrac{1}{2}x^2-\text{sen} x.
```

a\) Implemente y grafique la función $`f`$.

b\) Implemente el Método de la Secante en una función y utilicela para hallar el mínimo de la función con una precisión de $`\epsilon=10^{-5}`$.

</div>

<div class="cell code" id="jKFmpvZnnMtf">

``` python
import numpy as np
def f_prima(x):
  return x-np.cos(x)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="AIHK4B52mGBn" outputId="dff4a811-84d1-4df2-8c95-7e1df1a23b78">

``` python
x_anterior=20
x=10
tolerancia=10**-5
distancia=tolerancia+1
iter=0
while (distancia>tolerancia):
  x_nuevo=x-f_prima(x)/(f_prima(x)-f_prima(x_anterior))*(x-x_anterior)
  distancia=np.abs(x_nuevo-x)
  x_anterior=x
  x=x_nuevo
  iter+=1
print(x)
print(iter)
```

<div class="output stream stdout">

    0.7390851332098767
    8

</div>

</div>

<div class="cell markdown" id="QMqOTEAp8ddG">

# Bracketing

</div>

<div class="cell markdown" id="XNYjICZr8bw-">

## **Ejercicio 3:**

Halle el mínimo de la función
``` math
f(x)=2x-1+4(1024-x)^4.
```

</div>

<div class="cell code" id="mi-tV9woT38B">

``` python
import matplotlib.pyplot as plt
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:445}" id="XNXvmOkxTty3" outputId="7e220581-6e94-4e50-d50b-717f504bb130">

``` python
def f(x):
  return 2*x-1+4*(1024-x)**4

x = np.arange(-3, 200, 0.01)    # arreglo de posibles valores de x
y=np.array([f(t) for t in x])  #
plt.plot(x, y)
plt.show()
```

<div class="output display_data">

![](28c42fadc6da471441db7fd993d81909fdfa4112.png)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="eEa_aXt_T-mu" outputId="8ee4e2a5-689c-498d-ea2c-9eeed99fb396">

``` python
a=1
b=0
factor=2

s=1
if f(a)<f(b):
  temp=a
  a=b
  b=temp
c=b+s
while f(c)<f(b):
  a=b
  b=c
  s=factor*s
  c=b+s
print(a,c)
```

<div class="output stream stdout">

    512 2048

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:445}" id="9y2cB_t8UIZK" outputId="b3025d82-3c26-4efc-8714-9a6ca3be42b8">

``` python
x = np.arange(512, 2048, 0.01)    # arreglo de posibles valores de x
y=np.array([f(t) for t in x])  #
plt.plot(x, y)
plt.show()
```

<div class="output display_data">

![](d1dfa81f7d59c02a6497d3c72412f086d00ddc68.png)

</div>

</div>
