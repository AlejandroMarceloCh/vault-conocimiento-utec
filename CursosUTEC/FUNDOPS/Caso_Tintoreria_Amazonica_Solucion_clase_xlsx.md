---
curso: FUNDOPS
titulo: Caso Tintorería Amazónica- Solución_clase
slides: 0
fuente: Caso Tintorería Amazónica- Solución_clase.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Caso Tintorería Amazónica- Solución_clase.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Caso Tintorería Amazónica- Solución_clase.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Data
Filas: 30 · Columnas: 7
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object)

Muestra (primeras 30 de 30 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
,,Tamaño de Planta,,,,
,Parámetros,Pequeña,Mediana,Grande,,
,Tasa de Producción en horario normal (kg/hora),60,80,90,,
,Tasa de Producción en horas extra (kg/hora),50,60,65,,
,Número de Operarios,7,8,8,,
,Consumo de kg material / kg producto,0.8,0.78,0.77,,
,Consumo de L agua / kg producto,7.5,5.5,4.8,,
,Capacidad de almacenaje,10000,15000,20000,,
,Consumo kW,80,110,140,,
,Costo fijo ($),150000,250000,350000,,
,Inversión ($),800000,1200000,1500000,,
,,,,,,
,,,,,,
,Costo de M.O. por Hora Normal ($/horaxoperario),40,,,,
,Porcentaje Adicional Horas Extras (%),0.6,,,Número de Horas por Día (horas/día),Costo por Hora (US$/hora)
,Nro. Días x Semana (días/semana),5,,Horas Mínimas,5,40
,Nro. Semanas x Año (semanas/año),52,,Horas Normales,8,40
,Nro. de Días x Año (días/año),260,,Horas Extras,2,64
,Costo de Electricidad (US$/kWh),0.15,,,,
,Costo de Agua (US$/l),0.03,,,,
,Costo de Almacenaje (US$/kg),3,,,,
,Costo de Almacenaje Adicional (US$/kg),6,,,,
,Factor de Almacenaje (%),0.15,,,,
,Costo de Materiales (US$/kg),2.93,,,,
,Precio (US$/kg),14,,,,
,Demanda Anual (kg/año),80000,,,,
,Precio de Venta (US$/kg),14,,,,
,Tasa de Descuento Anual (%),0.09,,,,
,Horizonte de Evaluación Financiera (años),5,,,,
,Tasa de Descuento Mensual (%),0.007207323316136716,,,,

Resumen numérico:
       Unnamed: 0
count         0.0
mean          NaN
std           NaN
min           NaN
25%           NaN
50%           NaN
75%           NaN
max           NaN

## Hoja: Solución
Filas: 155 · Columnas: 9
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (float64), Unnamed: 7 (object), Unnamed: 8 (float64)

Muestra (primeras 40 de 155 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8
,Tintorería Amazónica,,,Leyenda,,,,
,,,,,,,,
,Costo de M.O. por Hora Normal ($/horaxoperario),40,,Títulos,,,,
,Porcentaje Adicional Horas Extras (%),0.6,,Datos,,,,
,Nro. Días x Semana (días/semana),5,,Cálculos,,,,
,Nro. Semanas x Año (semanas/año),52,,Respuestas,,,,
,Nro. de Días x Año (días/año),260,,,,,,
,Costo de Electricidad (US$/kWh),0.15,,,,,,
,Costo de Agua (US$/l),0.03,,,,,,
,Costo de Almacenaje (US$/kg),3,,,,,,
,Costo de Almacenaje Adicional (US$/kg),6,,,,,,
,Factor de Almacenaje (%),0.15,,,,,,
,Costo de Materiales (US$/kg),2.93,,,,,,
,Precio (US$/kg),14,,,,,,
,Demanda Anual (kg/año),80000,,,,,,
,Precio de Venta (US$/kg),14,,,,,,
,Tasa de Descuento Anual (%),0.09,,,,,,
,Horizonte de Evaluación Financiera (años),5,,,,,,
,Tasa de Descuento Mensual (%),0.007207323316136716,,,,,,
,,,,,,,,
,,Número de Horas por Día (horas/día),Costo por Hora (US$/hora),,,,,
,Horas Mínimas,5,40,,,,,
,Horas Normales,8,40,,,,,
,Horas Extras,2,64,,,,,
,,,,,,,,
,Parámetros en Función al Tamaño de Planta,,,,,,,
,,,,,,,,
,,Tamaño de Planta,,,,,,
,Parámetros,Pequeña,Mediana,Grande,,,,
,Tasa de Producción en horario normal (kg/hora),60,80,90,,,,
,Tasa de Producción en horas extra (kg/hora),50,60,65,,,,
,Número de Operarios,7,8,8,,,,
,Consumo de kg material / kg producto,0.8,0.78,0.77,,,,
,Consumo de L agua / kg producto,7.5,5.5,4.8,,,,
,Capacidad de almacenaje,10000,15000,20000,,,,
,Consumo kW,80,110,140,,,,
,Costo fijo ($),150000,250000,350000,,,,
,Inversión ($),800000,1200000,1500000,,,,
,Capacidad de Producción Mínima (kg/año),78000,104000,117000,1 - Capacidad de Planta,,,
,Capacidad de Producción Normal (kg/año),124800,166400,187200,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 6  Unnamed: 8
count         0.0         0.0    2.000000
mean          NaN         NaN    6.003604
std           NaN         NaN    8.480185
min           NaN         NaN    0.007207
25%           NaN         NaN    3.005405
50%           NaN         NaN    6.003604
75%           NaN         NaN    9.001802
max           NaN         NaN   12.000000
