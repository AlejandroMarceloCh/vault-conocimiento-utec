---
curso: OPTI
titulo: 10_Lab_método_de_Newton
slides: 0
fuente: 10_Lab_método_de_Newton.ipynb
---

<div class="cell markdown" id="hSEebkzgsQzv">

# El método de Newton

Implementaremos el Método de Newton para minimizar la función

``` math
f(x, y)=100(y-x^2)^2+(1-x)^2
```

</div>

<div class="cell markdown" id="e9ldSv70srL6">

En primer lugar implementamos la función, su gradiente y su Hessiano

</div>

<div class="cell code" id="FizlAWqy7vu1">

``` python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return 100*(x[1]-x[0]**2)**2+(1-x[0])**2

def gradiente(x):
  fx=-400*(x[1]-x[0]**2)*x[0]+2*x[0]-2
  fy=200*(x[1]-x[0]**2)
  return np.array([fx, fy])

def hessiano(x):
  fxx=-400*(x[1]-x[0]**2)+800*x[0]**2+2
  fxy=-400*x[0]
  fyy=200
  return np.matrix([[fxx, fxy], [fxy, fyy]])
```

</div>

<div class="cell markdown" id="FmrgSykjs6ig">

Luego implementamos el método:

``` math
\mathbf{x}_{k+1}=\mathbf{x}_k-Hf(\mathbf{x}_k)^{-1}\nabla f(\mathbf{x}_k)
```

Añadimos un parámetro que nos indique si queremos obtener la gráfica

</div>

<div class="cell code" id="DCILdexftAlw">

``` python

def Newton(x0, gradiente, hessiano, epsilon, max_iter, grafica=True):
  tol=epsilon+1

  iter=0

  valores=[]

  while(tol>epsilon):
    valores=np.concatenate((valores, f(x0)), axis=None)

    p=np.matmul(gradiente(x0), np.linalg.inv(hessiano(x0))) # paso

    x0=x0-np.array(p).flatten()

    tol=np.linalg.norm(p)

    iter+=1

    if (iter>=max_iter):
      print("El algoritmo no convergión en ", iter, "iteraciones")
      break

  if (grafica==True):
      plt.plot(valores)
      plt.show()

  return x0, iter


```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:447}" id="wF34Nl9CWfcI" outputId="ae2b7f82-d876-4a36-c3e7-931b18635d19">

``` python
x0=np.array([2,10])
solucion=Newton(x0, gradiente, hessiano, epsilon=10**-8, max_iter=10**3, grafica=True)
print(solucion)
```

<div class="output display_data">

![](0488aa14e5a58b2b76851e7dafee0e231fd29e6f.png)

</div>

<div class="output stream stdout">

    (array([1., 1.]), 6)

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="ul8kEhPEvdeA" outputId="66673d0b-2cab-48e8-bc98-82a886c33dac">

``` python
x0=np.array([2, 2])
p=np.matmul(gradiente(x0), np.linalg.inv(hessiano(x0)))
np.linalg.norm(p)
```

<div class="output execute_result" execution_count="5">

    1.9900265001650128

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="wLWFhdgEvwLP" outputId="b104a57c-c377-4af3-bf07-bc371808d209">

``` python
3*np.eye(2)
```

<div class="output execute_result" execution_count="6">

    array([[3., 0.],
           [0., 3.]])

</div>

</div>

<div class="cell markdown" id="z1go25ZmNG5g">

# Inclusión de un tamaño de paso

``` math
\mathbf{x}_{k+1}=\mathbf{x}_k-\alpha Hf(\mathbf{x}_k)^{-1}\nabla f(\mathbf{x}_k),
```

donde $`\alpha`$ es el tamaño de paso.

</div>

<div class="cell markdown" id="kRWcPeVFNeXr">

# Modificación de Levenberg-Marquardt

``` math
\mathbf{x}_{k+1}=\mathbf{x}_k-\alpha [Hf(\mathbf{x}_k)+\mu I]^{-1}\nabla f(\mathbf{x}_k),
```
donde $`\alpha`$ y $`\mu`$ son constantes.

</div>

<div class="cell markdown" id="QQFX7MAHeY84">

**Ejercicio 1:**

Trabaja en grupos

1.  Implementa el algoritmo del Método de Newton con tamaño de paso constante.
2.  Implementa la modificación de Levenberg-Marquardt con un valor de $`\mu`$ constante.
3.  Utiliza los algoritmos para encontrar el mínimo de la función $`f`$ definida arriba. Indica el número de pasos que se necesitaron y realiza plots de los valores de la función con respecto al número de iteraciones.

</div>
