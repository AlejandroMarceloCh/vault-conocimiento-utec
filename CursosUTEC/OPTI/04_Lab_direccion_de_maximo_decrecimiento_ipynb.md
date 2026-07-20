---
curso: OPTI
titulo: 04_Lab_dirección_de_máximo_decrecimiento
slides: 0
fuente: 04_Lab_dirección_de_máximo_decrecimiento.ipynb
---

<div class="cell markdown" id="l95mHb-GkX0c">

# Dirección de máximo decrecimiento

Considera la función

``` math
f(x, y)=10y^4+(1-x)^2.
```

</div>

<div class="cell markdown" id="o12ZpjTnkoFo">

## **Ejercicio 1:**

a\) Implementa la función $`f`$ y su gradiente.

b\) Halla la dirección de decrecimiento máximo en el punto $`(3, 0.5)`$.

</div>

<div class="cell code" id="qZ-0DpWRQj0J">

``` python
import numpy as np
```

</div>

<div class="cell code" id="nhl7Ot3pQL2A">

``` python
def f(x):
  return 10*x[1]**4+(1-x[0])**2

def grad_f(x):
  return np.array([-2*(1-x[0]), 40*x[1]**3])
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="2Tn4tKRgQius" outputId="d31e3366-fde7-4392-e99a-615a1ea8b09b">

``` python
-grad_f([3, 0.5])
```

<div class="output execute_result" execution_count="5">

    array([-4., -5.])

</div>

</div>

<div class="cell markdown" id="AuJBFwSoclMH">

## **Ejercicio 2:**

Si $`v`$ es la dirección de máximo decrecimiento, defina la función
``` math
g(\alpha)=f((3, 0.5)+\alpha v)
```
y grafíquela para $`\alpha>0`$. ¿En qué valor de $`\alpha`$ alcanza su mínimo?

</div>

<div class="cell code" id="jQHdWdBCIxYx">

``` python
def g(alpha):
  return f([3, 0.5]-alpha*grad_f([3, 0.5]))
```

</div>

<div class="cell code" id="209ocO5uQ6ml">

``` python
from scipy.optimize import minimize_scalar
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="A6adzB1lQ-9L" outputId="3e985c3b-8560-41a1-be1b-98d580543450">

``` python
minimize_scalar(g).x
```

<div class="output execute_result" execution_count="10">

    np.float64(0.1746750912822985)

</div>

</div>
