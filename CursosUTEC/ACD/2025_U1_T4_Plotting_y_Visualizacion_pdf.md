---
curso: ACD
titulo: [2025] U1_T4 Plotting y Visualización
slides: 9
fuente: [2025] U1_T4 Plotting y Visualización.pdf
---

Plotting y Visualización
 para Análisis de Datos
   DS3021 Análisis Computacional de Datos




                                     Mg. José Espinoza Melgarejo
Objetivo de sesión
                     Describir técnicas computacionales para
                     hacer plotting y visualizaciones en Python
                     con la finalidad de realizar análisis de
                     datos
Contenido

1.   Introducción



2.   Matplotlib



3.   Laboratorio
     Matplotlib
1.
     Introducción
                      Introducción


●   Realizar visualizaciones (a veces llamadas gráficos) es una de las tareas
    más importantes en el análisis de datos.
●   Puede ser parte del proceso exploratorio, por ejemplo, para ayudar a
    identificar valores atípicos o transformaciones de datos necesarias, o
    como una forma de generar ideas para modelos.
●   Para otros, crear una visualización interactiva para la web puede ser el
    objetivo final.
●   Python tiene muchas bibliotecas complementarias para realizar
    visualizaciones   estáticas   o   dinámicas,   pero   nos   centraremos
    principalmente en matplotlib y las bibliotecas que se basan en esta.
2.
 Matplotlib
                              Matplotlib

●   Matplotlib es un paquete de trazado de escritorio diseñado para crear
    diagramas y figuras adecuadas para su publicación.
●   El proyecto fue iniciado por John Hunter en 2002 para habilitar una
    interfaz de trazado similar a MATLAB en Python. Las comunidades
    matplotlib e IPython han colaborado para simplificar el trazado interactivo
    desde el shell de IPython.
●   Matplotlib admite varios backends GUI en todos los sistemas operativos y
    puede exportar visualizaciones a todos los formatos de gráficos
    rasterizados y vectoriales comunes (PDF, SVG, JPG, PNG, BMP, GIF, etc.).
●   Figure: es el objeto con el nivel más alto en la jerarquía.
    Corresponde a toda la representación gráfica y
    generalmente puede contener muchos Axes.

●   Axes(ejes): Se entiende por diagrama o gráfico. Cada
    objeto Axe pertenece a una sola Figura y se caracteriza
    por dos Axes. Otros objetos como el título, label x y label
    y.

●   Axis: Los objetos de eje que tienen en cuenta los valores
    numéricos que se representarán en los ejes definen los
    límites y administran los ticks (la marca en los ejes) y las
    etiquetas de tick (el texto de la etiqueta representado en
    cada tick).
3.
 Laboratorio
 Matplotlib

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
