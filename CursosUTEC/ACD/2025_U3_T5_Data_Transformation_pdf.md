---
curso: ACD
titulo: [2025] U3_T5 Data Transformation
slides: 9
fuente: [2025] U3_T5 Data Transformation.pdf
---

## Slide 1

Portada.

# Data Transformation
**DS3021 Análisis Computacional de Datos**
Mg. José Espinoza Melgarejo

Fondo decorativo (túnel tecnológico azul con silueta).

## Slide 2

**Objetivo de sesión**

> Comprender conceptos y aplicar técnicas de Transformación de Datos de manera computacional como parte del preprocesamiento de datos.

Título rotado 90° en el margen izquierdo ("Objetivo de **sesión**"); foto decorativa de dos personas trabajando con teñido azul.

## Slide 3

Separador de sección.

**1. Data Transformation — Fundamentos**

Icono de portapapeles; imagen decorativa de mano robótica sobre globo de datos.

## Slide 4

**Data Transformation**

**Data Transformation** normalmente es **el último paso** de preprocesamiento de datos que se aplica.

Es posible que sea necesario transformar el conjunto de datos por los siguientes motivos:
- Que el dataset esté listo para un análisis prescrito
- Una transformación específica puede ayudar a que una determinada herramienta de análisis funcione mejor,
- Simplemente sin una transformación de datos correcta, los resultados de nuestro análisis pueden ser engañosos.

Banda superior decorativa con foto de equipo y línea degradada negro→celeste.

## Slide 5

**Razones para hacer Data Transformation**

Tres bloques rectangulares apilados verticalmente (etiqueta a la izquierda, texto explicativo a la derecha), diferenciados por color: celeste sólido, blanco con borde celeste y negro sólido.

| Razón | Descripción |
|---|---|
| **Necesidad** (bloque celeste) | El método analítico con el que trabajaremos no puede trabajar con el estado actual de los datos. |
| **Corrección** (bloque blanco, borde celeste) | Sin la transformación de datos adecuada, el análisis resultante será engañoso y erróneo. |
| **Efectividad** (bloque negro) | Si los datos pasan por algunos cambios prescritos, el análisis será más efectivo. |

## Slide 6

Separador de sección.

**2. Data Transformation — Métodos**

Mismo layout e imagen decorativa que la slide 3.

## Slide 7

**Métodos de Data Transformation**

Diagrama cíclico entre dos entidades:

- Izquierda: icono de teclado numérico ("123") etiquetado **Datos Numéricos**.
- Derecha: icono de marcadores numerados 1, 2, 3 etiquetado **Datos Categóricos**.

Flechas:
- Flecha recta celeste horizontal, de Numéricos → Categóricos, rotulada **Discretización**.
- Flecha curva superior, de Categóricos → Numéricos, rotulada **Ranking Transformation**.
- Flecha curva inferior, de Categóricos → Numéricos, rotulada **Codificación Binaria**.

Nota al pie junto a la flecha inferior: *\* Si es de tipo nominal es la única opción*.

## Slide 8

**Atributo Ordinal** (rótulo arriba a la izquierda)

Cuatro tablas en fila que muestran la misma columna original transformada de tres maneras distintas; tres flechas curvas en la base van desde la tabla original hacia cada resultado.

Tabla original — `Education level`:

| Education level |
|---|
| High School |
| Bachelor |
| High School |
| Masters |
| Doctorate |
| Bachelor |
| Masters |
| High School |
| High School |
| Bachelor |

Resultado 1 — **Binary Coding** (flecha celeste corta), one-hot de 4 columnas:

| High School | Bachelor | Masters | Doctorate |
|---|---|---|---|
| 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |

Resultado 2 — **Ranking Transformation** (flecha celeste media), `Education Rank`:

| Education Rank |
|---|
| 1 |
| 2 |
| 1 |
| 3 |
| 4 |
| 2 |
| 3 |
| 1 |
| 1 |
| 2 |

Resultado 3 — **Attribute Construction** (flecha gris larga, la que llega más lejos), `Education Years`:

| Education Years |
|---|
| 12 |
| 16 |
| 12 |
| 18 |
| 21 |
| 16 |
| 18 |
| 12 |
| 12 |
| 16 |

Mapeo implícito: High School=rank 1=12 años, Bachelor=2=16, Masters=3=18, Doctorate=4=21.

## Slide 9

Slide de cierre / separador.

**U3_L7 Data Transformation**

Foto decorativa de dos personas en laboratorio con teñido azul.
