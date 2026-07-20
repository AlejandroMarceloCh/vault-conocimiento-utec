---
curso: ACD
titulo: [2025] U1_T2 Numpy para Ciencia de Datos
slides: 19
fuente: [2025] U1_T2 Numpy para Ciencia de Datos.pdf
---

       Numpy
para Ciencia de Datos
  DS3021 Análisis Computacional de Datos




                                    Mg. José Espinoza Melgarejo
Objetivo de sesión aquí
                          Describir técnicas para cargar, almacenar y
                          manipular de manera efectiva en memoria
                          grandes conjuntos de datos utilizando Python
                          a través de librería Numpy.
Contenido

1.   Introducción



2.   Numpy




3.    Laboratorio
      Numpy Basics
1.
     Introducción
 Los datasets provienen de diferentes recursos y en distintos
formatos. Para manejar la heterogeneidad, podríamos pensar
               en los datasets como un array.
           “No importa cuáles sean los
Tiempo
            datos, el primer paso para
 Intensi
                 analizarlos será
   dad
             transformarlos en array
             (matrices) de números.”
  Por esta razón, el almacenamiento y la
manipulación eficientes de arrays numéricos
son fundamentales para el ciclo de vida de la
             Ciencia de Datos.
2.
 Numpy
                             Numpy
NumPy es la biblioteca fundamental del ecosistema Python Data Science para la
computación científica. Algunas de las características clave de NumPy incluyen:

  ●   Velocidad: las matrices NumPy son hasta 50 veces más rápidas que las
      listas estándar de Python
  ●   Rendimiento: NumPy combina la facilidad de uso de Python con la
      velocidad de C
  ●   Indexación y difusión: las funciones tan utilizadas en Pandas se heredan
      de NumPy.
  ●   Herramientas: NumPy tiene una amplia gama de funciones matemáticas y
      herramientas computacionales para prácticamente todas las necesidades.
      Puede realizar operaciones como ajuste de curvas, optimización, álgebra
      lineal, transformaciones, etc., con facilidad.

NumPy es la base sobre la que se construyen muchas otras bibliotecas
informáticas científicas. Algunas de las bibliotecas conocidas que utilizan NumPy
como son : SciPy, Statsmodels, Scikit-Learn, SpaCy, Matplotlib, Seaborn, etc.
                                        NumPy


●   NumPy (abreviatura de Numerical Python) es una de las principales librerías para usar en
    computación científica en Python.
●   Permite trabajar con arrays multidimensional de alto rendimiento y también proporciona
    herramientas para trabajar con estos arrays.
●   Los arrays pueden tener más de 3 dimensiones, pero en este curso solo trabajaremos con 2
    dimensiones.
●   Los arrays bidimensionales se pueden ver como matrices. Esta es una forma conveniente de
    almacenar y manipular datos multivariados con Python.
                         ¿Qué es un array?

Un array es una cuadrícula (grid) de datos numéricos del mismo tipo. Los arrays vienen en
diferentes rangos, formas y tamaños.


  Rango (ndim)    El número de dimensiones en un array

  Forma (shape)   El número de elementos en cada dimensión de un array. Es representado como
                  una tupla

  Tamaño (size)   El número total de elementos de un array
                       Ejemplos

A)    0        0   0   0   0   0   0   0



     Rango:
     Forma:
     Tamaño:
                             Ejemplos

A)     0      0       0      0   0   0   0   0



     Rango: 1
     Forma: (8,0)
     Tamaño: 8 (elementos)
                   Ejemplos

B)   0       0         0      0   0

     0       0         0      0   0

     0       0         0      0   0



         Rango:
         Forma:
         Tamaño:
                   Ejemplos

B)   0        0            0     0   0

     0        0            0     0   0

     0        0            0     0   0



         Rango: 2- dimensiones
         Forma: (3,5)
         Tamaño: 15 elementos
NumPy puede soportar todo tipo de calculaciones matemáticas y
estadísticas para una colección de números como: mean, median,
standard deviation (std) y variance (var).

Otra cosa relacionada a números que no estás seguro que Numpy lo
tiene, fácil Numpy sí lo tiene, googlealo.
¿Cómo llegamos del punto A al punto B?
¿Cómo llegamos del punto A al punto B?



                           Una lista de Python
                          diseñada para manejar todo
                          tipo de datos.




                             Un array NumPy
                          diseñada     para  datos
                          homogéneos y que implican
                          muchos cálculos.
3.
 Laboratorio
 Numpy Basics

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
