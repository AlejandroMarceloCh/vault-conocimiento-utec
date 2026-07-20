---
curso: ACD
titulo: [2025] U1_T3 Pandas para Ciencia de Datos
slides: 11
fuente: [2025] U1_T3 Pandas para Ciencia de Datos.pdf
---

       Pandas
para Ciencia de Datos
  DS3021 Análisis Computacional de Datos




                                    Mg. José Espinoza Melgarejo
Objetivo de sesión
                     Describir técnicas para cargar, almacenar
                     y manipular de manera efectiva en
                     memoria grandes conjuntos de datos
                     utilizando Python a través de Pandas.
Contenido

1.   Introducción



2.
     Estructuras de
     Pandas



3.   Laboratorio
     Pandas Data Structures
1.
     Introducción
                     Previamente


●   Revisamos la librería NumPy
●   Recordemos que el         objeto ndarray    proporciona características
    esenciales para el tipo de datos limpios y bien organizados que
    normalmente se ven en las tareas de computación numérica.
●   Sin embargo NumPy cuenta con algunas limitaciones cuando
    necesitamos más flexibilidad (adjuntar etiquetas a los datos, trabajar con
    datos faltantes, etc.) y agrupaciones.
●   Cada una de estas tareas es una pieza importante para analizar los
    datos menos estructurados disponibles en muchas formas en el mundo
    que nos rodea.
                                         Pandas

Para realizar análisis de datos, primero los datos deben estar
estructurados de una manera que podamos manipular y realizar
operaciones, una forma común en Python en la que esto se hace
es a través del módulo Pandas.

Pandas es una biblioteca de código abierto que proporciona
estructuras de datos y herramientas de análisis de datos fáciles de
usar y de alto rendimiento para el lenguaje de programación
Python.
  ● Pandas ha sido construido en base a NumPy.
2.
 Estructuras de
 Pandas
    Estructuras de Datos
         en Pandas


Pandas cuenta con tres estructuras de datos fundamentales:
 ● Series (1D)
 ● DataFrame (2D)
 ● Index
                                            Serie

                                                                       index
●   Una    serie     es  un    array    etiquetado
    unidimensional capaz de contener cualquier
                                                                               0           20
    tipo de datos (enteros, cadenas, float, objetos
    de Python, etc).                                                           1           25            Datos
                                                                                                       (valores)
                                                                               2           78
●   Una serie consta de dos elementos (arrays):                                3           10
     ○ Datos unidimensionales (valores)
     ○ Indexs (índices)

                Es similar a una lista o array, pero la diferencia clave radica en su capacidad para
                    mantener un índice, lo que proporciona una búsqueda rápida y capacidad
                                             potente de alinear los datos.
                                  DataFrame                                       Nombre de
                                                                                  columnas
●   Un DataFrame es una estructura de datos                               Edad   Puntaje
                                                              index
    bidimensional compuesta de filas y columnas,
    exactamente como una hoja de cálculo simple o una
                                                                      0   20       10
    tabla SQL.
●   Cada columna de un DataFrame es una Serie. Estas                  1   25       15
    columnas deben tener la misma longitud, pero pueden               2   78       18
    tener diferentes tipos de datos: float, int, bool, etc.           3    10      10
●   Un dataframe consta de tres elementos:
      ○ Datos bidimensionales (valores)
                                                                                           Valores de
      ○ Indexs Columnas                                                                    columnas
      ○ Indexs Filas
3.
 Laboratorio
 Pandas Data
 Structures

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
