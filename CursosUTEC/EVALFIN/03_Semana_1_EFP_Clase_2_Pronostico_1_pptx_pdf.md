---
curso: EVALFIN
titulo: 03 - Semana 1/EFP - Clase 2 - Pronóstico-1__pptx
slides: 36
fuente: 03 - Semana 1/EFP - Clase 2 - Pronóstico-1__pptx.pdf
---

## Slide 1

Portada del capítulo. Título "Métodos de Pronóstico de la Demanda", subtítulo "Evaluación Financiera de Proyectos - Semana 2". Imagen de fondo decorativa (túnel futurista azul con silueta humana/robótica) - decorativa.

## Slide 2

"Objetivo(s) de la sesión". Texto: Aplicar técnicas de pronóstico cuantitativo (medias móviles y regresión lineal), a partir del estudio de mercado, para estimar la demanda y proyectar los ingresos futuros en la evaluación de proyectos. Imagen decorativa (dos personas revisando documentos) - decorativa.

## Slide 3

"Contenido" - lista numerada de la sesión:
1. Estudio de mercado.
2. Pronóstico de la demanda.
3. Método de medias móviles (promedio móvil).
4. Regresión lineal.
5. Casos de aplicación.

Imagen decorativa (persona con visor VR) - decorativa.

## Slide 4

Slide separador de sección. "1. Estudio de mercado" con ícono de portapapeles. Imagen decorativa (mano robótica sobre globo digital) - decorativa.

## Slide 5

"Estudio de mercado". Definición: Análisis sistemático de las condiciones del mercado para un bien o servicio. Objetivo: Entender la demanda, la competencia y las preferencias del consumidor. Importancia: Base para la toma de decisiones en marketing, producción y estrategia comercial.

Imagen: ilustración de tres pares de zapatillas con carteles de "Precio S/.50", "Precio S/.100", "Precio S/.20" y manos sosteniendo billetes correspondientes (50, 50, 100, 20, 20), representando diferencias de precio/percepción del consumidor.

## Slide 6

"Análisis de la demanda de un bien o servicio". Definición de Demanda: Cantidad de un bien o servicio que los consumidores están dispuestos a comprar a un precio determinado.

Diagrama de 3 columnas conectadas por flechas (flujo secuencial):
| Factores que influyen | Métodos para estimar | Proyección de la demanda |
|---|---|---|
| Precio del producto. | Encuestas y entrevistas. | Uso de modelos estadísticos (regresión, series de tiempo). |
| Ingresos de los consumidores. | Análisis de datos históricos. | Consideración de tendencias y estacionalidad. |
| Gustos y preferencias. | Estudios de mercado secundarios (informes, estadísticas). | |
| Precios de bienes sustitutos o complementarios. | | |

## Slide 7

"Precios y volúmenes de demanda proyectados". Diagrama de 3 columnas (tarjetas de color):
- **Determinación de precios**: Basado en costos (margen sobre costos de producción). Basado en la competencia (análisis de precios de la competencia). Basado en el valor percibido (disposición a pagar del consumidor).
- **Supuestos de precios**: Ejemplo: Precio = Costo de producción + Margen de beneficio. Consideración de descuentos y promociones.
- **Proyección de volúmenes de demanda**: Escenarios: optimista, pesimista y realista. Uso de elasticidad-precio de la demanda.

## Slide 8

Slide separador de sección. "2. Pronóstico de la demanda" con ícono de portapapeles. Imagen decorativa (mano robótica sobre globo digital) - decorativa.

## Slide 9

"Pronóstico de la demanda". Definición: Proceso de estimar la cantidad de un bien o servicio que los consumidores comprarán en un período futuro. Objetivo: Apoyar la planificación de producción, inventarios, marketing y finanzas. Importancia: Reduce la incertidumbre en la toma de decisiones.

Imagen decorativa (ilustración de persona junto a globo terráqueo con gráfico de barras ascendente y monedas) - decorativa.

## Slide 10

"Pronóstico de la demanda" - diagrama de árbol/taxonomía de métodos de pronóstico:

```
Métodos
├── Cualitativos
│   ├── Encuestas y entrevistas
│   ├── Juicio de expertos
│   ├── Análisis de fuerza de ventas
│   └── Estudios de mercado
└── Cuantitativos
    ├── Series de tiempo
    │   ├── (1) Promedio móvil   [resaltado en rojo/círculo]
    │   ├── Suavización exponencial
    │   └── Descomposición de series
    ├── Métodos causales
    │   ├── (2) Regresión lineal   [resaltado en rojo/círculo]
    │   └── Modelos econométricos
    ├── Simulación (Monte Carlo)
    └── IA (Machine Learning)
```
Los ítems "(1) Promedio móvil" y "(2) Regresión lineal" están destacados con un óvalo rojo, indicando que son los dos métodos que se desarrollarán en el capítulo.

## Slide 11

Slide separador de sección. "3. Método de medias móviles (promedio móvil)" con ícono de portapapeles. Imagen decorativa (mano robótica sobre globo digital) - decorativa.

## Slide 12

"Método de medias móviles (promedio móvil)". Definición: Técnica de pronóstico que estima valores futuros utilizando el promedio de un número definido de periodos históricos. Sirve para: Pronosticar datos de corto plazo. Reducir la variabilidad aleatoria de la serie (eliminar "ruido"). Identificar tendencias de corto plazo.

Imagen: gráfico de velas de precios financieros (tipo trading) con una línea de media móvil roja superpuesta, marcadores triangulares rojos (venta) en picos y triángulos verdes (compra) en zonas de recuperación de tendencia, y un recuadro amarillo resaltando una zona de la serie donde el precio cruza la media móvil.

## Slide 13

"Método de medias móviles (promedio móvil)" - fórmula y pasos.

Fórmula (LaTeX):
$$PM_t = \frac{D_{t-1} + D_{t-2} + \dots + D_{t-n}}{n}$$

Donde: PM_t = pronóstico para el período "t". D_{t-1}, D_{t-2}... = Demandas reales de períodos anteriores. n = número de periodos incluidos en el promedio.

Pasos (columna derecha):
- **Definir el período n**: Determinar el número de periodos históricos que se utilizarán para el cálculo del promedio.
- **Calcular el promedio móvil**: Obtener el promedio de los últimos n valores observados de la serie.
- **Estimar el valor futuro**: Utilizar el promedio calculado como pronóstico para el siguiente periodo.
- **Actualizar el cálculo**: Para cada nuevo pronóstico, eliminar el dato más antiguo e incorporar el más reciente.

## Slide 14

"Ejemplo" — caso de universidad peruana, ventas 2017-2025, estimar 2026 con N=2.

Texto: En una universidad peruana se han recopilado datos de ventas de 2017 a 2025 y se desea estimar las ventas de 2026. 1° se decide cuantos números se van a promediar, en este caso decidimos N=2.

Gráfico de líneas "Ventas reales y estimadas por medias móviles": eje Y de 0 a 1,000,000, eje X años 2017-2026. Dos series: "Vtas reales" (línea gris, sube de ~524k en 2017 a un pico de ~936k en 2022, baja a ~792k en 2023, sube a ~916k en 2025) y "Vtas estimadas (MM)" (línea azul, comienza en 2019 desde ~551k y converge cerca de la línea real hacia 2025-2026, terminando en ~909k).

Tabla:
| Año | (1) Ventas reales | (2) Valor estimado = Promedio de 2 anteriores (N=2) | Error = Valor absoluto de (1)–(2) |
|---|---|---|---|
| 2017 | 524,248 | | |
| 2018 | 577,995 | | |
| 2019 | 618,391 | Media móvil = 551,121.5 (524,248+577,995)/2 | 618,391-551,121.5 = 67,269.5 |
| 2020 | 648,950 | Media móvil = 598,193 (577,995+618,391)/2 | 648,950-598,193 = 50,757 |
| 2021 | 870,772 | 633,670.5 | 237,102 |
| 2022 | 936,594 | 759,861 | 176,733 |
| 2023 | 792,747 | 903,683 | 110,936 |
| 2024 | 902,211 | 864,671 | 37,541 |
| 2025 | 916,889 | 847,479 | 69,410 |
| 2026 | | 909,550 | |

Error medio = 107,107 (promedio de los errores).

## Slide 15

"Ejercicio 3.1" — enunciado: empresa peruana con ventas anuales (miles de soles) 2016-2025; estimar 2026 con medias móviles N=4. Graficar ventas y estimaciones. Calcular error promedio.

Tabla de datos:
| Año | Ventas (S/. 000) |
|---|---|
| 2016 | 550,000 |
| 2017 | 590,000 |
| 2018 | 620,000 |
| 2019 | 640,000 |
| 2020 | 660,000 |
| 2021 | 690,000 |
| 2022 | 720,000 |
| 2023 | 710,000 |
| 2024 | 750,000 |
| 2025 | 780,000 |
| 2026 | (por calcular) |

## Slide 16

"Ejercicio 3.1 - Solución". Gráfico de líneas "Ventas reales y estimadas por medias móviles" (0 a 1,000,000, años 2016-2026): "Vtas reales" (gris, tendencia ascendente de 550k a 780k) y "Vtas estimadas (MM)" (azul, comienza en 2020, ligeramente por debajo de la real, converge cerca del final ~740k en 2026).

Tabla:
| Año | Ventas (S/. 000) | Media móvil | Error |
|---|---|---|---|
| 2016 | 550,000 | | |
| 2017 | 590,000 | | |
| 2018 | 620,000 | | |
| 2019 | 640,000 | | |
| 2020 | 660,000 | 600,000 | 60,000 |
| 2021 | 690,000 | 627,500 | 62,500 |
| 2022 | 720,000 | 652,500 | 67,500 |
| 2023 | 710,000 | 677,500 | 32,500 |
| 2024 | 750,000 | 695,000 | 55,000 |
| 2025 | 780,000 | 717,500 | 62,500 |
| 2026 | | 740,000 | |

Error promedio 56,667.

## Slide 17

"Ejercicio 3.2" — enunciado: empresa con ventas anuales (miles de soles) 2014-2025; estimar 2026 con medias móviles N=3 y N=5, comparar cuál es más confiable. Graficar ventas y estimaciones.

Tabla de datos:
| Año | Ventas (S/. 000) |
|---|---|
| 2014 | 450,000 |
| 2015 | 470,000 |
| 2016 | 500,000 |
| 2017 | 530,000 |
| 2018 | 560,000 |
| 2019 | 600,000 |
| 2020 | 650,000 |
| 2021 | 700,000 |
| 2022 | 750,000 |
| 2023 | 800,000 |
| 2024 | 850,000 |
| 2025 | 900,000 |
| 2026 | (por calcular) |

## Slide 18

"Ejercicio 3.2 - Solución". Gráfico de líneas "Ventas reales y estimadas por medias móviles" (2014-2026): tres series "Ventas" (negro, la más alta), "Media móvil N=3" (azul, intermedia) y "Media móvil N=5" (gris, la más baja), todas con tendencia ascendente paralela.

Tabla:
| Año | Ventas (S/. 000) | Media móvil N=3 | Media móvil N=5 | Error N=3 | Error N=5 |
|---|---|---|---|---|---|
| 2014 | 450,000 | | | | |
| 2015 | 470,000 | | | | |
| 2016 | 500,000 | | | | |
| 2017 | 530,000 | 473,333 | | 56,667 | |
| 2018 | 560,000 | 500,000 | | 60,000 | |
| 2019 | 600,000 | 530,000 | 502,000 | 70,000 | 98,000 |
| 2020 | 650,000 | 563,333 | 532,000 | 86,667 | 118,000 |
| 2021 | 700,000 | 603,333 | 568,000 | 96,667 | 132,000 |
| 2022 | 750,000 | 650,000 | 608,000 | 100,000 | 142,000 |
| 2023 | 800,000 | 700,000 | 652,000 | 100,000 | 148,000 |
| 2024 | 850,000 | 750,000 | 700,000 | 100,000 | 150,000 |
| 2025 | 900,000 | 800,000 | 750,000 | 100,000 | 150,000 |
| 2026 | | 850,000 | 800,000 | | |

Texto: Comparamos los errores promedio de ambos N desde 2019, año desde el cual disponemos de los errores para ambos. Error promedio N=3: 93,333 (marcado como "Mejor" con flecha azul). Error promedio N=5: 134,000.

## Slide 19

Slide separador de sección. "4. Regresión lineal" con ícono de portapapeles. Imagen decorativa (mano robótica sobre globo digital) - decorativa.

## Slide 20

"Regresión lineal". Definición: Técnicas estadísticas utilizadas para estimar valores futuros estableciendo una relación lineal entre una variable dependiente y una o más variables independientes a partir de datos históricos. Sirve para: Pronosticar datos de corto y mediano plazo. Identificar tendencias en los datos. Analizar la relación entre variables relevantes.

Aplicaciones (columna derecha):
- **Economía y Finanzas**: para prever el comportamiento de variables económicas, como la inflación o el crecimiento del PIB, en función de factores como la tasa de interés o la inversión.
- **Marketing**: para determinar cómo los cambios en el precio de un producto afectan las ventas.
- **Ingeniería**: para analizar la relación entre la temperatura y la resistencia de materiales.
- **Medicina**: para entender la relación entre dosis de un medicamento y su efectividad o efectos secundarios.

## Slide 21

"Pasos del proceso de regresión lineal" — diagrama de flujo de 5 pasos (flechas tipo chevron secuenciales):
1. **Definir las variables**: Identificar la variable independiente (X) y la variable dependiente (Y) que se desea estimar.
2. **Recopilar y organizar los datos**: Utilizar datos históricos consistentes y relevantes para el análisis.
3. **Estimar la ecuación de regresión**: Calcular la recta que mejor ajusta los datos, generalmente mediante el método de mínimos cuadrados.
4. **Evaluar el ajuste del modelo**: Analizar indicadores como el coeficiente de determinación y el coeficiente de correlación.
5. **Realizar la proyección**: Utilizar la ecuación estimada para predecir valores futuros de la variable dependiente.

## Slide 22

"Regresión lineal simple". Ecuación (LaTeX):
$$Y = a + bX$$

Donde: Y = variable dependiente (se intenta predecir). X = variable independiente (se utiliza para hacer la predicción). a = intersección con el eje Y cuando X es cero (intercepto o constante), en color azul. b = pendiente o inclinación de la recta (indica el cambio en Y por cada unidad de cambio en X), en color naranja/dorado.

Imagen: diagrama clásico de dispersión con recta de regresión ajustada; puntos negros representan "Valor observado / Dato (y)" con líneas verticales que muestran la distancia (residuo) hasta la "Recta de regresión estimada"; ejes rotulados "y" (vertical) y "x" (horizontal).

## Slide 23

Slide de material complementario: gráfico "Gráfico de Ventas en miles" con puntos de dispersión (años 2017-2023, valores ~685 a ~821) y línea de tendencia roja ajustada. Ecuación mostrada en el gráfico: y = 22.964x - 45646, R² = 0.9439. Texto superpuesto en verde grande: "Regresión Lineal Simple en Excel". Enlace debajo del gráfico: https://www.youtube.com/watch?v=VE19S9iWuWk (hasta el minuto 3:12) — referencia a video tutorial de cómo hacer regresión lineal en Excel.

## Slide 24

"Ejercicio 4.1" — enunciado: se cuenta con información de ventas anuales; estimar ventas para 2026 con regresión lineal.

Tabla de datos:
| Año | Ventas en miles |
|---|---|
| 2019 | 685 |
| 2020 | 698 |
| 2021 | 710 |
| 2022 | 735 |
| 2023 | 745 |
| 2024 | 798 |
| 2025 | 821 |
| 2026 | (por calcular) |

## Slide 25

"Ejercicio 4.1 - Solución". Gráfico de dispersión "Gráfico de Ventas en miles" con puntos rojos (años 2019-2025) y línea de tendencia azul ajustada, ecuación en el gráfico: f(x) = 22.9642857142857x − 45692.0714285714, R² = 0.943913007744009.

Tabla:
| Año | Ventas en miles |
|---|---|
| 2019 | 685 |
| 2020 | 698 |
| 2021 | 710 |
| 2022 | 735 |
| 2023 | 745 |
| 2024 | 798 |
| 2025 | 821 |
| 2026 | **833** (resaltado en amarillo) |

## Slide 26

"Ejercicio 4.2" — enunciado: empresa desea entender cómo el gasto en publicidad afecta las ventas mensuales; datos de últimos 6 meses.

Tabla:
| Gasto en Publicidad (miles USD) | Ventas (miles unidades) |
|---|---|
| 2 | 30 |
| 4 | 40 |
| 6 | 50 |
| 8 | 65 |
| 10 | 80 |
| 12 | 95 |

Se pide: 1. Diagrama de dispersión. 2. Ecuación de la recta de ajuste. 3. Coeficiente de determinación. 4. Coeficiente de correlación. 5. Calcule las ventas para un gasto de publicidad de 15 mil dólares.

## Slide 27

"Ejercicio 4.2 - Solución". Gráfico de dispersión "Ventas (en miles de unidades)" con puntos rojos y línea de tendencia azul; ecuación en gráfico: f(x) = 6.57142857142857x + 14, R² = 0.991100702576112.

Respuestas: 1. Diagrama de dispersión (mostrado). 2. Ecuación de la recta de ajuste: Y = 14 + 6.57X. 3. Coeficiente de determinación: 99.11%. 4. Coeficiente de correlación: 99.55% (relación directa). 5. Calcule las ventas para un gasto de publicidad de 15 mil dólares: 112.55.

## Slide 28

"Ejercicio 4.3" — enunciado: tienda de electrónica analiza cómo el precio afecta la demanda; datos de últimos 5 meses.

Tabla:
| Precio del producto (USD) | Demanda (unidades) |
|---|---|
| 100 | 250 |
| 150 | 200 |
| 200 | 150 |
| 250 | 120 |
| 300 | 100 |

Se pide: 1. Diagrama de dispersión. 2. Ecuación de la recta de ajuste. 3. Coeficiente de determinación. 4. Coeficiente de correlación. 5. Calcule la demanda si la tienda decide fijar el precio en 180 dólares.

## Slide 29

"Ejercicio 4.3 - Solución". Gráfico de dispersión "Curva de Demanda" con puntos rojos y línea de tendencia azul descendente; ecuación en gráfico: f(x) = −0.76x + 316, R² = 0.967828418230563.

Respuestas: 1. Diagrama de dispersión (mostrado). 2. Ecuación de la recta de ajuste: Y = 316 - 0.76X. 3. Coeficiente de determinación: 96.78%. 4. Coeficiente de correlación: -98.38% (relación inversa). 5. Calcule la demanda si el precio es 180 dólares: 179.2.

## Slide 30

Slide separador de sección. "5. Casos de aplicación" con ícono de portapapeles. Imagen decorativa (mano robótica sobre globo digital) - decorativa.

## Slide 31

"Ejercicio 5.1" — enunciado: empresa ABC S.A. con ventas anuales (miles de soles) 2018-2025; estimar ventas para 2026-2032 (7 años) con medias móviles N=4. Graficar ventas y estimaciones.

Tabla de datos:
| Año | Ventas (S/. 000) |
|---|---|
| 2018 | 550,000 |
| 2019 | 570,000 |
| 2020 | 590,000 |
| 2021 | 610,000 |
| 2022 | 630,000 |
| 2023 | 650,000 |
| 2024 | 670,000 |
| 2025 | 690,000 |
| 2026-2032 | (por calcular) |

## Slide 32

"Ejercicio 5.1 - Solución". Gráfico de líneas "Ventas reales y estimadas por medias móviles" (2018-2032): "Ventas" (gris, ascendente hasta 2025 luego se detiene) y "Media móvil" (azul, sigue de cerca y se estabiliza/aplana en el rango proyectado 2026-2032, alrededor de 660k-670k).

Tabla:
| Año | Ventas (S/. 000) | Media móvil N=4 | Error |
|---|---|---|---|
| 2018 | 550,000 | | |
| 2019 | 570,000 | | |
| 2020 | 590,000 | | |
| 2021 | 610,000 | | |
| 2022 | 630,000 | 580,000 | 50,000 |
| 2023 | 650,000 | 600,000 | 50,000 |
| 2024 | 670,000 | 620,000 | 50,000 |
| 2025 | 690,000 | 640,000 | 50,000 |
| 2026 | 660,000 | 660,000 | NA |
| 2027 | 667,500 | 667,500 | NA |
| 2028 | 671,875 | 671,875 | 0A |
| 2029 | 672,344 | 672,344 | NA |
| 2030 | 667,930 | 667,930 | NA |
| 2031 | 669,912 | 669,912 | NA |
| 2032 | 670,515 | 670,515 | NA |

Nota: para 2026 en adelante, "Ventas" y "Media móvil" coinciden porque son valores proyectados (se usa el propio pronóstico como dato). Error promedio N=4: 50,000.

## Slide 33

"Ejercicio 5.2" — enunciado: empresa Green Garden SAC evalúa expandir su área de cultivo de paltas; pronosticar el crecimiento del consumo per cápita en EEUU para la temporada 2026, usando un reporte del USDA ERS sobre Suministro y Utilización de Vegetales Frescos.

Tabla (datos en millones de libras, salvo columnas de consumo):
| Año | Producción | Importaciones | Total (Suministro) | Exportaciones | Consumo Doméstico | Consumo de paltas (libras) | Consumo de paltas (kg) |
|---|---|---|---|---|---|---|---|
| 2018 | 527.6 | 1.9 | 529.5 | 50.7 | 478.8 | 2.08 | 0.94 |
| 2019 | 383.4 | 1.5 | 384.9 | 24.9 | 360 | 1.55 | 0.70 |
| 2020 | 458.0 | 3.4 | 461.4 | 28.9 | 432.5 | 1.85 | 0.84 |
| 2021 | 553.0 | 7.3 | 560.3 | 41.9 | 518.4 | 2.19 | 0.99 |
| 2022 | 457.0 | 3.7 | 460.7 | 24.1 | 436.6 | 1.83 | 0.83 |
| 2023 | 369.4 | 15.8 | 385.2 | 22.6 | 362.6 | 1.51 | 0.68 |
| 2024 | 614.0 | 4.0 | 618.0 | 47.2 | 570.8 | 2.35 | 1.07 |
| 2025 | 414.0 | 12.5 | 426.5 | 38.8 | 387.7 | 1.58 | 0.72 |

Nota al margen: "Los datos están en millones de libras. 1 Kg = 0.453592 libras."

## Slide 34

"Ejercicio 5.2" (continuación) — solo texto, se pide: 1. Ecuación de la recta de ajuste. 2. Coeficiente de determinación. 3. Coeficiente de correlación. 4. Consumo per cápita de paltas (en Kg) en EEUU para la temporada 2026.

## Slide 35

"Ejercicio 5.2 - Solución". Gráfico de dispersión "Consumo de paltas (kg)" (eje Y 0.00-1.20, eje X años 2017-2026) con puntos rojos (valores oscilando entre ~0.68 y ~1.07) y línea de tendencia azul casi plana/ligeramente descendente; ecuación en gráfico: f(x) = −0.0047519161904762x + 10.4530816390476, R² = 0.00663288554503749.

Respuestas: 1. Ecuación de la recta de ajuste: Y = 10.453 - 0.0048X. 2. Coeficiente de determinación: 0.66%. 3. Coeficiente de correlación: -8.12% (relación inversa). 4. Consumo per cápita de paltas (kg) en EEUU para 2026: 0.73 kg. Nota implícita: el R² extremadamente bajo (0.66%) indica que el modelo lineal prácticamente no explica la variabilidad del consumo — el pronóstico es poco confiable pese al cálculo.

## Slide 36

Slide de cierre, idéntica a la portada (slide 1): "Métodos de Pronóstico de la Demanda" / "Evaluación Financiera de Proyectos - Semana 2". Imagen de fondo decorativa (túnel futurista azul con silueta humana/robótica) - decorativa.
