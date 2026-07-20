---
curso: OPTI
titulo: 05_Lab_método_del_descenso_máximo
slides: 0
fuente: 05_Lab_método_del_descenso_máximo.ipynb
---

<div class="cell markdown" id="-azAdOFS5FtB">

# Método del descenso máximo

Implementaremos este método para encontrar el mínimo de la función

``` math
f(x, y)=10y^4+(1-x)^2.
```

</div>

<div class="cell markdown" id="Sj-Ub5ZF5Q9D">

En el laboratorio anterior definimos la función y su gradiente

</div>

<div class="cell markdown" id="7vfn5sqq76Sq">

Programaremos una función que implemente el método de descenso máximo. Debe recibir como input:

- La función a optimizar (de modo que su input sea un array o lista)
- El gradiente de la función (de modo que su input sea un array o lista)
- La tolerancia
- Un número máximo de iteraciones pasado el cual el algoritmo se detiene.
- Punto inicial $`x_0`$.

Debe tener como output:

- El punto donde se encuentra el mínimo
- El valor mínimo de la función.
- Los valores de la función en los puntos intermedios

</div>

<div class="cell code" id="Q6Zad_zyV-lT">

``` python
import numpy as np
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt
```

</div>

<div class="cell code" id="7DMjukjVOPWW">

``` python
def f(x):
    return 10*(x[1]**4)+(1-x[0])**2

def gradiente_f(x):  #input lista x=[a, b]
  fx=-2*(1-x[0])
  fy=40*(x[1]**3)
  return np.array([fx, fy])
```

</div>

<div class="cell code" id="DiMV4LZs67z0">

``` python
def descenso_maximo(f, gradiente, x0, epsilon, max_iter):

  tol=epsilon+1 # Para entrar en el loop

  iter=0

  lista_valores=[f(x0)]

  while (tol>epsilon) and (iter<max_iter):
    iter+=1

    # calculo del alpha correcto
    def g(alpha):
      punto=x0-alpha*gradiente(x0)
      return f(punto)
    alpha=minimize_scalar(g).x

    #actualizacion
    x1=x0-alpha*gradiente(x0)   # Actualizamos el punto
    tol=np.linalg.norm(x1-x0) # Calculamos la norma de la diferencia entre y un punto y el anterior.
    x0=x1

    #almacenamos el valor de la funcion
    lista_valores.append(f(x0))

  if (iter==max_iter):
    print("El método no convergió")
  xmin=x0
  return [xmin, f(xmin), lista_valores]
```

</div>

<div class="cell code" id="6QTVdz6MbVF9">

``` python
x0=[3, 0.5]
epsilon=10**-5
max_iter=1000
min, valor_min, lista=descenso_maximo(f, gradiente_f, x0, epsilon, max_iter)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:445}" id="rcq9SI2dWuHd" outputId="31c6e380-38d7-4c9f-917b-80498be3f85b">

``` python
plt.plot(lista[10:])
plt.show()
```

<div class="output display_data">

![](f00e57fe55fc11632e5c4af410c9bfd36529f4a3.png)

</div>

</div>

<div class="cell code" id="v6hc9Y1hlocB">

``` python
def f(x):
    return 10000*x[0]**2+x[1]**2

def gradiente_f(x):  #input lista x=[a, b]
  fx=20000*x[0]
  fy=2*x[1]
  return np.array([fx, fy])
```

</div>

<div class="cell code" id="Rte0Jhmmly4w">

``` python
x0=[10,2]
epsilon=10**-5
max_iter=100
min, valor_min, lista=descenso_maximo(f, gradiente_f, x0, epsilon, max_iter)
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="0xoDah0xmbzm" outputId="ae24ceb1-f076-43e2-ef97-53b144d10985">

``` python
min
```

<div class="output execute_result" execution_count="21">

    array([1.59130913e-10, 3.17665616e-11])

</div>

</div>

<div class="cell markdown" id="Fprm6nSvc3ZG">

## **Ejercicio 1:**

Encuentre el mínimo de la función

``` math
f(x, y)=10(y-x^2)^2+(1-x)^2
```

utilizando el método de descenso máximo probando diferentes puntos iniciales.

</div>
