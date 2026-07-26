---
curso: ACD
titulo: [2025] U3_T4 Data Integration
slides: 10
fuente: [2025] U3_T4 Data Integration.pdf
---

## Slide 1

Portada.

**Data Integration**
*DS3021 Análisis Computacional de Datos*

Fondo decorativo (túnel tecnológico azul con silueta de persona).

## Slide 2

**Objetivo de sesión**

> Comprender conceptos y aplicar técnicas de Integración de Datos de manera computacional como parte del preprocesamiento de datos.

Foto decorativa (dos personas trabajando, teñida de azul) en la columna izquierda. El título "Objetivo de **sesión**" está rotado 90° en vertical al margen izquierdo.

## Slide 3

Slide divisoria de sección.

**1. Data Integration — Fundamentos**

Ícono de portapapeles junto al título; imagen decorativa de mano robótica tocando un globo terráqueo digital.

## Slide 4

**Data Integration**

- La integración de datos implica **combinar datos que residen en diferentes fuentes** y proporcionar a los usuarios una **vista unificada** de ellos.
- Hay muchos desafíos que deben superarse antes de que la integración sea posible.

**Visual — diagrama "Ejemplo de Data Integration"** (lado derecho): una tabla destino en la parte superior con encabezados `Column 1`, `Column 2`, `.`, `.`, `.`, `Column m` y filas `Row 1`, `Row 2`, `.`, `.`, `.`, `Row n`, con celdas rellenas con "xxx". Debajo, cuatro íconos de base de datos (cilindros apilados) de colores distintos — granate, negro, morado oscuro y verde — cada uno con una flecha que apunta hacia arriba a la tabla unificada (la granate y la verde en diagonal, las del centro verticales). Es decir: 4 fuentes heterogéneas → 1 tabla única.

Reproducción de la tabla del diagrama:

| | Column 1 | Column 2 | . | . | . | Column m |
|---|---|---|---|---|---|---|
| Row 1 | xxx | xxx | . | . | . | xxx |
| Row 2 | xxx | xxx | . | . | . | xxx |
| . | . | . | . | . | . | . |
| . | . | . | . | . | . | . |
| . | . | . | . | . | . | . |
| Row n | xxx | xxx | . | . | . | xxx |

## Slide 5

**Data Integration — Ejemplo**

Imagine que a una empresa le gustaría analizar su efectividad en la forma en que hace publicidad. Para **el análisis** la empresa necesita generar dos columnas de datos:
- las ventas totales por cliente y
- la cantidad total de gastos de publicidad por cliente.

**Visual — esquema de unión de dos fuentes:** a la izquierda, un cilindro de base de datos naranja rotulado "Database de Marketing" acompañado de un ícono de "ficha de persona/registro de cliente"; al centro un signo **+** grande; a la derecha, otro ícono de ficha de persona y un cilindro de base de datos celeste rotulado "Database de Ventas". Bajo el signo `+` hay una llave/corchete horizontal celeste que agrupa ambos lados y apunta a un ícono de listado/tabla resultante (barras negras apiladas) — el dataset integrado.

## Slide 6

**Data Integration — Direcciones**

**① (círculo azul con "1")** La primera es **agregando atributos**; podríamos querer complementar un conjunto de datos con más atributos descriptivos. En esta dirección, tenemos todos los datos que necesitamos, pero otras fuentes podrían enriquecer nuestro conjunto de datos.

**② (círculo rojo relleno con "2")** La segunda **es agregando objetos de datos (filas)**; es posible que tengamos múltiples fuentes de datos con distintos objetos de datos, e integrarlos conducirá a una población con más objetos de datos que representan la población que queremos analizar.

Visual: solo los dos numeradores circulares (uno de contorno azul, otro rojo sólido) a la izquierda de cada párrafo. Sin diagramas adicionales.

## Slide 7

Slide divisoria de sección.

**2. Data Integration — Desafíos**

Mismo layout que la slide 3 (ícono de portapapeles + imagen decorativa de mano robótica y globo digital).

## Slide 8

**Desafíos** *Data Integration*

**Visual — diagrama de 6 ítems en dos columnas.** Cada ítem es un círculo azul degradado con el número, conectado por un pequeño conector con punto amarillo a una caja rectangular gris de bordes redondeados con el texto.

Columna izquierda:
1. Identificación de Entidades
2. Recopilación de Datos sin sentido
3. Formato de Índice no Coincidente

Columna derecha:
4. Desajuste de Agregación
5. Objetos de datos (filas) Duplicados
6. Redundancia de Datos

## Slide 9

Slide de cierre / separador.

**U3_L6 Data Integration**

Foto decorativa de fondo (dos personas con lentes de seguridad y bata en un laboratorio, teñida de azul).

## Slide 10

Slide sin título propio: la ocupa por completo una **tabla grande** (tapa incluso el logo UTEC) que compara 5 situaciones al integrar dos DataFrames de canciones, `songIntegrate_df` y `songAttribute_df`. Columnas: **Situations | Description | Example**. En la columna Example, para cada situación se muestran dos mini-tablas: la de `songIntegrate_df` con columnas `Artists | Name` y la de `songAttribute_df` con columnas `Artist | Name`. Los nombres de variables y el código aparecen resaltados en verde lima.

| Situation | Description | Example — `songIntegrate_df` (Artists, Name) | Example — `songAttribute_df` (Artist, Name) |
|---|---|---|---|
| Situation 1 | - Songs with only one artist<br>- Songs with unique song names | 16 · Taylor Swift · You Need To Calm Down | 154047 · Taylor Swift · You Need To Calm Down |
| Situation 2 | - Songs with only one artist<br>- Songs with non-unique song names<br>**To see the difference between situations 1 and 2, run and compare the following code:**<br>`songAttribute_df.query("Name == 'Sucker'")`<br>`songAttribute_df.query("Name == 'You Need To Calm Down'")` | 9 · Jonas Brothers · Sucker | 21644 · New Found Glory · Sucker<br>154557 · Jonas Brothers · Sucker |
| Situation 3 | - Songs with more than one artist<br>- Both artists are recognized in both sources but in different ways | 6 · Ed Sheeran, Justin Bieber · I Don't Care | 154921 · Ed Sheeran · I Don't Care (with Justin Bieber) |
| Situation 4 | Songs with more than one artist but only `songAttribute_df` recognizes the second artist | 12 · Chris Brown · No Guidance | 154214 · Chris Brown · No Guidance (feat. Drake) |
| Situation 5 | Songs with more than one artist but only `songIntegrate_df` recognizes the second artist | 137 · DJ Sammy, Yanou · Heaven | 22487 · DJ Sammy · Heaven |

Código citado en Situation 2:

```python
songAttribute_df.query("Name == 'Sucker'")
songAttribute_df.query("Name == 'You Need To Calm Down'")
```
