---
curso: FINEMP
titulo: 16 - Semana 14/Caso 1_TESLA
slides: 0
fuente: 16 - Semana 14/Caso 1_TESLA.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 16 - Semana 14/Caso 1_TESLA.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Caso 1_TESLA.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Paramétrico
Filas: 252 · Columnas: 9
Columnas y tipos: Precios del activo (object), Unnamed: 1 (object), Rendimientos (object), Unnamed: 3 (float64), Rendimiento Promedio y Riesgo (object), Unnamed: 5 (object), Unnamed: 6 (float64), Unnamed: 7 (float64), VaR Paramétrico (object)

Muestra (primeras 40 de 252 filas, formato CSV):
Precios del activo,Unnamed: 1,Rendimientos,Unnamed: 3,Rendimiento Promedio y Riesgo,Unnamed: 5,Unnamed: 6,Unnamed: 7,VaR Paramétrico
Periodo,Cotización,%,,,TESLA,,,Nivel de confianza
2022-11-29 00:00:00,180.830002,,,RE ,,,,Nivel de significancia
2022-11-30 00:00:00,194.699997,,,RI,,,,z
2022-12-01 00:00:00,194.699997,,,,,,,Volatilidad
2022-12-02 00:00:00,194.860001,,,,,,,Monto
2022-12-05 00:00:00,182.449997,,,,,,,t
2022-12-06 00:00:00,179.820007,,,,,,,
2022-12-07 00:00:00,174.039993,,,,,,,VaR (%)
2022-12-08 00:00:00,173.440002,,,,,,,VaR (UM)
2022-12-09 00:00:00,179.050003,,,,,,,
2022-12-12 00:00:00,167.820007,,,,,,,
2022-12-13 00:00:00,160.949997,,,,,,,
2022-12-14 00:00:00,156.800003,,,,,,,
2022-12-15 00:00:00,157.669998,,,,,,,
2022-12-16 00:00:00,150.229996,,,,,,,
2022-12-19 00:00:00,149.869995,,,,,,,
2022-12-20 00:00:00,137.800003,,,,,,,
2022-12-21 00:00:00,137.570007,,,,,,,
2022-12-22 00:00:00,125.349998,,,,,,,
2022-12-23 00:00:00,123.150002,,,,,,,
2022-12-27 00:00:00,109.099998,,,,,,,
2022-12-28 00:00:00,112.709999,,,,,,,
2022-12-29 00:00:00,121.82,,,,,,,
2022-12-30 00:00:00,123.18,,,,,,,
2023-01-03 00:00:00,108.099998,,,,,,,
2023-01-04 00:00:00,113.639999,,,,,,,
2023-01-05 00:00:00,110.339996,,,,,,,
2023-01-06 00:00:00,113.059998,,,,,,,
2023-01-09 00:00:00,119.769997,,,,,,,
2023-01-10 00:00:00,118.849998,,,,,,,
2023-01-11 00:00:00,123.220001,,,,,,,
2023-01-12 00:00:00,123.559998,,,,,,,
2023-01-13 00:00:00,122.400002,,,,,,,
2023-01-17 00:00:00,131.490005,,,,,,,
2023-01-18 00:00:00,128.779999,,,,,,,
2023-01-19 00:00:00,127.169998,,,,,,,
2023-01-20 00:00:00,133.419998,,,,,,,
2023-01-23 00:00:00,143.75,,,,,,,
2023-01-24 00:00:00,143.889999,,,,,,,
2023-01-25 00:00:00,144.429993,,,,,,,

Resumen numérico:
       Unnamed: 3  Unnamed: 6  Unnamed: 7
count         0.0         0.0         0.0
mean          NaN         NaN         NaN
std           NaN         NaN         NaN
min           NaN         NaN         NaN
25%           NaN         NaN         NaN
50%           NaN         NaN         NaN
75%           NaN         NaN         NaN
max           NaN         NaN         NaN

## Hoja: Simulación Histórica
Filas: 252 · Columnas: 8
Columnas y tipos: Precios del activo (object), Unnamed: 1 (object), Crecimientos (object), Unnamed: 3 (float64), Escenarios del precio del activo (object), Escenario Rentabilidades (float64), Unnamed: 6 (float64), VaR Simulación Histórica (object)

Muestra (primeras 40 de 252 filas, formato CSV):
Precios del activo,Unnamed: 1,Crecimientos,Unnamed: 3,Escenarios del precio del activo,Escenario Rentabilidades,Unnamed: 6,VaR Simulación Histórica
Periodo,Cotización,%,,TESLA,,,Nivel de confianza
2022-11-29 00:00:00,180.830002,,,,,,Nivel de significancia
2022-11-30 00:00:00,194.699997,,,,,,z
2022-12-01 00:00:00,194.699997,,,,,,Volatilidad
2022-12-02 00:00:00,194.860001,,,,,,Monto
2022-12-05 00:00:00,182.449997,,,,,,t
2022-12-06 00:00:00,179.820007,,,,,,
2022-12-07 00:00:00,174.039993,,,,,,VaR (%)
2022-12-08 00:00:00,173.440002,,,,,,VaR (UM)
2022-12-09 00:00:00,179.050003,,,,,,
2022-12-12 00:00:00,167.820007,,,,,,
2022-12-13 00:00:00,160.949997,,,,,,
2022-12-14 00:00:00,156.800003,,,,,,
2022-12-15 00:00:00,157.669998,,,,,,
2022-12-16 00:00:00,150.229996,,,,,,
2022-12-19 00:00:00,149.869995,,,,,,
2022-12-20 00:00:00,137.800003,,,,,,
2022-12-21 00:00:00,137.570007,,,,,,
2022-12-22 00:00:00,125.349998,,,,,,
2022-12-23 00:00:00,123.150002,,,,,,
2022-12-27 00:00:00,109.099998,,,,,,
2022-12-28 00:00:00,112.709999,,,,,,
2022-12-29 00:00:00,121.82,,,,,,
2022-12-30 00:00:00,123.18,,,,,,
2023-01-03 00:00:00,108.099998,,,,,,
2023-01-04 00:00:00,113.639999,,,,,,
2023-01-05 00:00:00,110.339996,,,,,,
2023-01-06 00:00:00,113.059998,,,,,,
2023-01-09 00:00:00,119.769997,,,,,,
2023-01-10 00:00:00,118.849998,,,,,,
2023-01-11 00:00:00,123.220001,,,,,,
2023-01-12 00:00:00,123.559998,,,,,,
2023-01-13 00:00:00,122.400002,,,,,,
2023-01-17 00:00:00,131.490005,,,,,,
2023-01-18 00:00:00,128.779999,,,,,,
2023-01-19 00:00:00,127.169998,,,,,,
2023-01-20 00:00:00,133.419998,,,,,,
2023-01-23 00:00:00,143.75,,,,,,
2023-01-24 00:00:00,143.889999,,,,,,
2023-01-25 00:00:00,144.429993,,,,,,

Resumen numérico:
       Unnamed: 3  Escenario Rentabilidades  Unnamed: 6
count         0.0                       0.0         0.0
mean          NaN                       NaN         NaN
std           NaN                       NaN         NaN
min           NaN                       NaN         NaN
25%           NaN                       NaN         NaN
50%           NaN                       NaN         NaN
75%           NaN                       NaN         NaN
max           NaN                       NaN         NaN

## Hoja: Simulación de Montecarlo
Filas: 252 · Columnas: 9
Columnas y tipos: Precios del activo (object), Unnamed: 1 (object), Crecimientos (object), N (0,1) Independientes (object), Escenario del Precio del Activo (float64), Escenario Rentabilidades (float64), Unnamed: 6 (float64), Unnamed: 7 (float64), VaR Simulación de Montecarlo (object)

Muestra (primeras 40 de 252 filas, formato CSV):
Precios del activo,Unnamed: 1,Crecimientos,"N (0,1) Independientes",Escenario del Precio del Activo,Escenario Rentabilidades,Unnamed: 6,Unnamed: 7,VaR Simulación de Montecarlo
Periodo,Cotización,%,R1,,,,,Nivel de confianza
2022-11-29 00:00:00,180.830002,,,,,,,Nivel de significancia
2022-11-30 00:00:00,194.699997,,,,,,,z
2022-12-01 00:00:00,194.699997,,,,,,,Volatilidad
2022-12-02 00:00:00,194.860001,,,,,,,Inversión
2022-12-05 00:00:00,182.449997,,,,,,,t
2022-12-06 00:00:00,179.820007,,,,,,,Riesgo
2022-12-07 00:00:00,174.039993,,,,,,,VaR (%)
2022-12-08 00:00:00,173.440002,,,,,,,VaR (UM)
2022-12-09 00:00:00,179.050003,,,,,,,
2022-12-12 00:00:00,167.820007,,,,,,,
2022-12-13 00:00:00,160.949997,,,,,,,
2022-12-14 00:00:00,156.800003,,,,,,,
2022-12-15 00:00:00,157.669998,,,,,,,
2022-12-16 00:00:00,150.229996,,,,,,,
2022-12-19 00:00:00,149.869995,,,,,,,
2022-12-20 00:00:00,137.800003,,,,,,,
2022-12-21 00:00:00,137.570007,,,,,,,
2022-12-22 00:00:00,125.349998,,,,,,,
2022-12-23 00:00:00,123.150002,,,,,,,
2022-12-27 00:00:00,109.099998,,,,,,,
2022-12-28 00:00:00,112.709999,,,,,,,
2022-12-29 00:00:00,121.82,,,,,,,
2022-12-30 00:00:00,123.18,,,,,,,
2023-01-03 00:00:00,108.099998,,,,,,,
2023-01-04 00:00:00,113.639999,,,,,,,
2023-01-05 00:00:00,110.339996,,,,,,,
2023-01-06 00:00:00,113.059998,,,,,,,
2023-01-09 00:00:00,119.769997,,,,,,,
2023-01-10 00:00:00,118.849998,,,,,,,
2023-01-11 00:00:00,123.220001,,,,,,,
2023-01-12 00:00:00,123.559998,,,,,,,
2023-01-13 00:00:00,122.400002,,,,,,,
2023-01-17 00:00:00,131.490005,,,,,,,
2023-01-18 00:00:00,128.779999,,,,,,,
2023-01-19 00:00:00,127.169998,,,,,,,
2023-01-20 00:00:00,133.419998,,,,,,,
2023-01-23 00:00:00,143.75,,,,,,,
2023-01-24 00:00:00,143.889999,,,,,,,
2023-01-25 00:00:00,144.429993,,,,,,,

Resumen numérico:
       Escenario del Precio del Activo  Escenario Rentabilidades  Unnamed: 6  Unnamed: 7
count                              0.0                       0.0         0.0         0.0
mean                               NaN                       NaN         NaN         NaN
std                                NaN                       NaN         NaN         NaN
min                                NaN                       NaN         NaN         NaN
25%                                NaN                       NaN         NaN         NaN
50%                                NaN                       NaN         NaN         NaN
75%                                NaN                       NaN         NaN         NaN
max                                NaN                       NaN         NaN         NaN
