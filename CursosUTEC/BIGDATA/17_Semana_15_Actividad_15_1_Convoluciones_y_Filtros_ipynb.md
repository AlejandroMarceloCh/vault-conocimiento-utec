---
curso: BIGDATA
titulo: 17 - Semana 15/Actividad 15_1_Convoluciones y Filtros
slides: 0
fuente: 17 - Semana 15/Actividad 15_1_Convoluciones y Filtros.ipynb
---

<div class="cell markdown" id="C8rbJewE84dX">

# **Convoluciones y Filtros Clásicos en Imágenes**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div class="cell code" id="IP-WSy05fA1r">

``` python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.signal import convolve2d
from skimage import data, color
```

</div>

<div class="cell code" id="DJaVK6c-fOhR">

``` python
img = mpimg.imread("futbol.jpg")   # cambia el nombre del archivo
plt.imshow(img)
plt.show()
```

</div>

<div class="cell code" id="ZRcR45RdhOrX">

``` python
img_gray = color.rgb2gray(img)
plt.imshow(img_gray, cmap='gray')
plt.show()
```

</div>

<div class="cell code" id="D-gb5qL3fjXt">

``` python
img_gray.shape
```

</div>

<div class="cell code" id="Vhxznjzyfja2">

``` python
def apply_filter(image, kernel):
    return convolve2d(image, kernel, mode='same', boundary='symm')

def show_filter_result(image, filtered, title):
    plt.figure(figsize=(8,4))
    plt.subplot(1,2,1)
    plt.imshow(image, cmap='gray')
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.imshow(filtered, cmap='gray')
    plt.title(title)
    plt.axis("off")
    plt.show()
```

</div>

<div class="cell markdown" id="3t8_QLiB7p5U">

## **Edge Detection — Sobel**

------------------------------------------------------------------------

Resalta bordes detectando cambios fuertes en intensidad.

</div>

<div class="cell markdown" id="7GwJvmR078oZ">

**Kernel Sobel (vertical):**

</div>

<div class="cell code" id="NtXSuxGJfjdg">

``` python
sobel_vertical = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])
sobel_v = apply_filter(img_gray, sobel_vertical)
show_filter_result(img_gray, sobel_v, "Sobel Vertical (Edge Detection)")
```

</div>

<div class="cell markdown" id="Tm4pFlf072FH">

**Kernel Sobel (horizontal):**

</div>

<div class="cell code" id="JJPVx1i4fjge">

``` python
sobel_horizontal = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])
sobel_h = apply_filter(img_gray, sobel_horizontal)
show_filter_result(img_gray, sobel_h, "Sobel Horizontal (Edge Detection)")
```

</div>

<div class="cell markdown" id="KqbaNgv28FJ6">

## **Edge Detection — Prewitt**

------------------------------------------------------------------------

Versión simplificada de Sobel.

</div>

<div class="cell code" id="wnGBUXYffji4">

``` python
prewitt = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])
prewitt_img = apply_filter(img_gray, prewitt)
show_filter_result(img_gray, prewitt_img, "Prewitt (Edge Detection)")
```

</div>

<div class="cell markdown" id="xCPey9fn8RI2">

## **Blur (Desenfoque)**

------------------------------------------------------------------------

Suaviza la imagen promediando el vecindario.

</div>

<div class="cell code" id="G0e2bHAoills">

``` python
blur = (1/9) * np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])
blur_img = apply_filter(img_gray, blur)
show_filter_result(img_gray, blur_img, "Blur (Suavizado 3x3)")
```

</div>

<div class="cell markdown" id="txgrZITb8XIx">

## **Sharpen (Afilado)**

------------------------------------------------------------------------

Realza bordes y resalta detalles.

</div>

<div class="cell code" id="m6qgnKpOiloi">

``` python
sharpen = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])
sharp_img = apply_filter(img_gray, sharpen)
show_filter_result(img_gray, sharp_img, "Sharpen (Afilado)")
```

</div>

<div class="cell markdown" id="vX7bjXH58dAx">

## **Emboss (Relieve)**

------------------------------------------------------------------------

Produce un efecto 3D donde un lado se ilumina y otro se oscurece.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:251}" id="VIENJ9shilrH" outputId="14ab2d04-9435-448a-99af-3f7650b96fa3">

``` python
emboss = np.array([
    [-2, -1, 0],
    [-1,  1, 1],
    [ 0,  1, 2]
])
emboss_img = apply_filter(img_gray, emboss)
show_filter_result(img_gray, emboss_img, "Emboss (Relieve)")
```

</div>

<div class="cell markdown" id="gdzOQSzW8f7v">

## **Outline (Contorno)**

------------------------------------------------------------------------

Resalta contornos de manera agresiva.

</div>

<div class="cell code" colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:251}" id="4CPlf7m1izfE" outputId="33fdf58b-92a0-4362-ab69-9769020c8a3f">

``` python
outline = np.array([
    [ -1, -1, -1],
    [ -1,  8, -1],
    [ -1, -1, -1]
])
outline_img = apply_filter(img_gray, outline)
show_filter_result(img_gray, outline_img, "Outline (Contorno)")
```

</div>
