---
curso: BIGDATA
titulo: 06 - Semana 4/Practica de Laboratorio
slides: 0
fuente: 06 - Semana 4/Practica de Laboratorio.ipynb
---

<div id="c3e2dd21-510e-4c48-8c0c-104f9fdca599" class="cell markdown">

# PRÁCTICA DE LABORATORIO – ANÁLISIS DE DATOS CON DASK

## Objetivo

Aplicar técnicas de procesamiento y análisis de datos utilizando Dask sobre un dataset de canciones de Spotify.

</div>

<div id="7910c07a-fb79-479a-917c-1e7edda935ff" class="cell markdown">

## Descripción del Dataset

El dataset contiene información de canciones de Spotify, incluyendo características musicales, popularidad y metadatos.

### Variables principales:

- **id**: Identificador único de la canción\
- **name**: Nombre de la canción\
- **artists**: Artista(s) de la canción\
- **popularity**: Nivel de popularidad (0 a 100)\
- **duration_ms**: Duración en milisegundos\
- **danceability**: Qué tan bailable es la canción\
- **tempo**: Velocidad de la canción (BPM)\
- **acousticness**: Probabilidad de que sea acústica\
- **release_date**: Fecha de lanzamiento

------------------------------------------------------------------------

</div>

<div id="ad1ab617-ad37-4674-8dbc-c30bf7e8283a" class="cell markdown">

## Parte 1: Preparación del entorno

1.  ¿Cómo se instala Dask con soporte completo para trabajar con archivos parquet?

------------------------------------------------------------------------

## Parte 2: Análisis exploratorio

1.  ¿Cuáles son las 10 canciones más populares del dataset?

2.  ¿Cuántas canciones tiene el artista Bad Bunny?

3.  ¿Cuántas canciones tienen una popularidad entre 50 y 60?

4.  ¿Cuántas canciones pertenecen a los artistas Adele o Drake?

5.  ¿Cuántas canciones tienen un nivel de acousticness mayor a 50?

------------------------------------------------------------------------

## Parte 3: Transformación de datos

1.  Cree nuevas columnas que representen el año y el mes de lanzamiento de cada canción.

2.  ¿Cuál es la duración promedio de las canciones en el dataset?

3.  ¿Cuál es la duración promedio (en minutos) de las canciones de Fonseca?

------------------------------------------------------------------------

## Parte 4: Calidad de datos

1.  ¿Existen registros duplicados en el dataset? ¿Cuántos?

2.  ¿Cuántos valores nulos existen por columna?

------------------------------------------------------------------------

## Parte 5: Estadística descriptiva

1.  Calcule la desviación estándar de las variables:

- popularity\
- tempo\
- danceability

------------------------------------------------------------------------

## Parte 6: Análisis y agrupaciones

1.  Realice agrupaciones relevantes sobre el dataset (por ejemplo, por artista o por año) y describa los resultados.

------------------------------------------------------------------------

## Parte 7: Filtros avanzados

1.  Filtre las canciones con una duración mayor a 5,000,000 milisegundos.\
    ¿Qué puede concluir?

------------------------------------------------------------------------

## Parte 8: Relaciones entre variables

1.  Calcule la matriz de correlación entre:

- popularity\
- danceability\
- tempo\
- acousticness

¿Qué relaciones encuentra?

------------------------------------------------------------------------

## Parte 9: Análisis por artista

1.  Filtre las canciones de los artistas Bad Bunny y/o J Balvin.\
    Compare sus características principales.

------------------------------------------------------------------------

## Entrega

- El trabajo debe ser entregado en un **Jupyter Notebook (.ipynb)**\
- El notebook debe estar **correctamente ejecutado (celdas con output visible)**\
- Incluir comentarios y conclusiones donde corresponda

------------------------------------------------------------------------

</div>

<div id="71ee29ed-c5e7-4a80-a2b5-a65786a67cdb" class="cell code">

``` python
```

</div>
