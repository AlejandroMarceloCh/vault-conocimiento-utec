---
curso: OPTI
titulo: 12_Lab_Soluciones_básicas_factibles
slides: 0
fuente: 12_Lab_Soluciones_básicas_factibles.ipynb
---

<div class="cell markdown" id="Nyd0145htCtQ">

# <center> Soluciones factibles</center>

</div>

<div class="cell markdown" id="vvgLfBUetSQg">

Las soluciones factibles de un problema de programación lineal son los puntos que cumplen todas las restricciones. Dado un problema \begin{eqnarray*} min & \quad & -2x_1-2x_2 \\ sa & & x_1+2x_2 \leq 3\\ & & 7x_1+4x_2 \leq 10 \\ & & x_1, x_2\geq 0. \end{eqnarray*}

Que transformado a su forma estándar es \begin{eqnarray*} min & \quad & -2x_1-2x_2 \\ sa & & x_1+2x_2+x_3 = 3\\ & & 7x_1+4x_2 +x_4 = 10 \\ & & x_1, x_2, x_3, x_4\geq 0. \end{eqnarray*} Las soluciones factibles corresponden a aquellas soluciones del sistema de ecuaciones que tienen todas las entradas mayores o iguales a $`0`$.

En este caso, la **matriz aumentada** del sistema es

``` math
\begin{bmatrix} 1 & 2 & 1 & 0 & 3 \\ 7 & 4 & 0 & 1 & 10\end{bmatrix}
```

</div>

<div class="cell markdown" id="D_g3eD4hG3Nl">

## **Ejercicio 1:**

a\) Halla 3 ejemplos de soluciones factibles del problema (no necesariamente básicas).

b\) ¿Existen infinitas soluciones factibles?

</div>

<div class="cell markdown" id="EM4B5FpvnitG">

# <center> Base ordenada </center>

Cada columna de la matriz de coeficientes $`A`$ corresponde a una variable del problema. Estas columnas son vectores de tamaño $`m`$ y una base del espacio de columnas es un conjunto de $`m`$ columnas linealmente independientes.

Por ejemplo, en el caso anterior, donde la matriz de coeficientes es

``` math
\begin{bmatrix} 1 & 2 & 1 & 0  \\ 7 & 4 & 0 & 1 \end{bmatrix}
```

la tercera y cuarta columna determinan una base. Esta base se puede representar por un vector de tamaño 2 que indique las columnas de la base. Considerando los índices de python, en este caso el vector que corresponde a la base es

``` math
(2, 3).
```

Hay un orden natural donde el primer índice corresponde a la columna que tiene el pivote en la primera fila; y el segundo, al de la segunda.

# Soluciones básicas

La solución básica correspondiente a una base de las columnas se obtien de la siguiente manera: igualamos a $`0`$ a las variables que no correspondan a la base y hallamos la solución del sistema.

Por ejemplo, la solución básica correspondiente a las columnas $`3`$ y $`4`$ se obtiene de la matriz aumentada

``` math
\begin{bmatrix} 1 & 2 & 1 & 0 & 3 \\ 7 & 4 & 0 & 1 & 10\end{bmatrix}
```

y es $`(0, 0, 3, 10)`$.

# Soluciones básicas factibles

Si todas las componentes de la solución básica son mayores o iguales a $`0`$, entonces decimos que es una **solución básica factible**.

</div>

<div class="cell markdown" id="Ueo7GdFuO-2i">

## **Ejercicio 2**:

¿Cuántas posibles bases (ordenadas) de columnas de la siguiente matriz existen?

``` math
\begin{bmatrix} 1 & 2 & 1 & 0  \\ 7 & 4 & 0 & 1 \end{bmatrix}
```

</div>

<div class="cell markdown" id="CpCd3s_1Jq52">

# <center> Solución básica factible inicial </center>

Si nos aseguramos de que $`m`$ últimas columnas de la matriz $`A`$ formen a la matriz identidad, entonces hay una manera sencilla de elegir una solución básica factible. Asumamos por el momento que este es el caso.

</div>

<div class="cell code" id="I4ag0JBohR0M">

``` python
import numpy as np
A=np.matrix([[1, 2, 1, 0], [7, 4, 0, 1]])
matriz_aumentada=np.matrix([[1, 2, 1, 0, 3], [7, 4, 0, 1,10]])
```

</div>

<div class="cell markdown" id="ey74upLZhk3D">

Guardamos los índices de las columnas correspondientes a la base en un arreglo

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="DyKtvarqnpLj" outputId="8b1c354c-39ef-4b99-d2cc-1c656699644d">

``` python
m=A.shape[0]
n=A.shape[1]
base=list(range(n-m, n)) # m últimas columnas
A[:, base]
```

<div class="output execute_result" execution_count="3">

    matrix([[1, 0],
            [0, 1]])

</div>

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="IUxvf5_GhdtC" outputId="b94dd8dc-b9f3-4af0-cfa1-d10dbe619d8d">

``` python
base
```

<div class="output execute_result" execution_count="4">

    [2, 3]

</div>

</div>

<div class="cell markdown" id="6TXp2dRMoqSH">

La solución básica factible inicial se obtendría colocando ceros en las columnas que no corresponden a la base y colocando los valores de $`b`$ en la posición correcta.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="SmDpdcj5onOZ" outputId="684286e7-fa51-4146-f8b0-db0a94964721">

``` python
x=np.repeat(0., n) # inicializamos en ceros
for i in range(m):
  x[base[i]]=matriz_aumentada[i, n]
x
```

<div class="output execute_result" execution_count="7">

    array([ 0.,  0.,  3., 10.])

</div>

</div>

<div class="cell markdown" id="Kisu3D15fXls">

## **Ejercicio 3:**

Escribe las matrices $`A`$, $`b`$ y $`c`$ correspondientes al siguiente problema de programación lineal luego de convertirlo a su forma estándar.

\begin{eqnarray*} max & \quad & x_1+2x_2-x_3 \\ sa & & 0.1x_1-0.3x_2+0.1x_3 \leq 1\\ & & 1.8x_1 -3x_2 \leq 10 \\ & & x_1, x_2, x_3 \geq 0. \end{eqnarray*}

¿Qué columnas conforman la base inicial y cuál es la solución básica factible inicial?

</div>

<div class="cell markdown" id="kDTe8J2AHI49">

# <center> Cambio de la base </center>

Es posible reemplazar una columna de una base por otra. Para poder encontrar la nueva solución básica debemos pivotear la matriz.

</div>

<div class="cell markdown" id="1XBNh1uzgoRP">

## **Ejercicio 4:**

Dada la matriz aumentada

``` math
\begin{bmatrix} 0 & 2 & 1 & 0 & 2 & 3 \\ 1 & 1 & 0 & 0 & 2 & 8 \\ 0 & 0 & 0 & 1 & 2 & 9  \end{bmatrix}
```

y vector $`c=(-1, -4, 0, 0, 0)`$.

a\) Halla las columnas que pertenecen a la base actual y la solución básica factible.

b\) Indique la nueva solución básica si quitamos a la primera columna de la base (según el orden de la base) y agregamos a la quinta columna (índice 4).

</div>

<div class="cell code" id="v8ZLXM2h_Fsq">

``` python
```

</div>

<div class="cell markdown" id="3E3QQY0HdFbN">

# scipy.optimize.linprog

Ejemplo: \begin{eqnarray*} max & \quad & x_1+2x_2-x_3 \\ sa & & 0.1x_1-0.3x_2+0.1x_3 \leq 1\\ & & 1.8x_1 -3x_2 \leq 10 \\ & & x_1, x_2, x_3 \geq 0. \end{eqnarray*}

</div>

<div class="cell code" id="It10fAJMdIJn">

``` python
from scipy.optimize import linprog
import numpy as np
```

</div>

<div class="cell code" id="CEsFy0VEdMTf">

``` python
A=np.matrix([[0.1, -0.3, 0.1, 1, 0], [1.8, -3, 0, 0, 1]])
b=np.array([1, 10])
c=np.array([-1, -2, 1, 0, 0])
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="G4Au1HPndEnX" outputId="e29b8253-44ee-4b5d-a7c9-7a0c2e1d831e">

``` python
linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method="simplex")
```

<div class="output stream stderr">

    /tmp/ipython-input-1124007642.py:1: DeprecationWarning: `method='simplex'` is deprecated and will be removed in SciPy 1.11.0. Please use one of the HiGHS solvers (e.g. `method='highs'`) in new code.
      linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method="simplex")

</div>

<div class="output execute_result" execution_count="16">

     message: Optimization failed. The problem appears to be unbounded.
     success: False
      status: 3
         fun: -5.555555555555555
           x: [ 5.556e+00  0.000e+00  0.000e+00  4.444e-01  0.000e+00]
         nit: 2

</div>

</div>

<div class="cell markdown" id="PNHNo1Ddd-Gl">

Ejemplo:

\begin{eqnarray*} min & \quad & -2x_1-2x_2 \\ sa & & x_1+2x_2+x_3 = 3\\ & & 7x_1+4x_2 +x_4 = 10 \\ & & x_1, x_2, x_3, x_4\geq 0. \end{eqnarray*}

</div>

<div class="cell code" id="zeVitXxKdvF3">

``` python
A=np.matrix([[1, 2, 1, 0], [7, 4, 0, 1]])
b=np.array([3, 10])
c=np.array([-2, -2, 0, 0])
```

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="f9d9oBJNeIca" outputId="43c08dd7-f671-4eca-bd6a-f335ef08790d">

``` python
linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method="simplex")
```

<div class="output stream stderr">

    /tmp/ipython-input-1124007642.py:1: DeprecationWarning: `method='simplex'` is deprecated and will be removed in SciPy 1.11.0. Please use one of the HiGHS solvers (e.g. `method='highs'`) in new code.
      linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method="simplex")

</div>

<div class="output execute_result" execution_count="19">

     message: Optimization terminated successfully.
     success: True
      status: 0
         fun: -3.8
           x: [ 8.000e-01  1.100e+00  0.000e+00  0.000e+00]
         nit: 2

</div>

</div>
