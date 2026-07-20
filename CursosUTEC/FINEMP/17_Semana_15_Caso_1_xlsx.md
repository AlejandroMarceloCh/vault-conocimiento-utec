---
curso: FINEMP
titulo: 17 - Semana 15/Caso 1
slides: 0
fuente: 17 - Semana 15/Caso 1.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 17 - Semana 15/Caso 1.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Caso 1.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Caso 3
Filas: 757 · Columnas: 21
Columnas y tipos: Precios de los activos (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Rendimiento de los activos (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (float64), Estructura de Inversión (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (object), Unnamed: 15 (float64), Portafolio (object), Unnamed: 17 (object), Unnamed: 18 (object), Unnamed: 19 (object), Unnamed: 20 (object)

Muestra (primeras 40 de 757 filas, formato CSV):
Precios de los activos,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Rendimiento de los activos,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Estructura de Inversión,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Portafolio,Unnamed: 17,Unnamed: 18,Unnamed: 19,Unnamed: 20
Fecha,Netflix,Meta,Unilever,Exxon,R1,R2,R3,R4,,W1,W2,W3,W4,Suma,,RE(P),,,,
02.08.2021,515.150024,351.228271,51.350082,51.161499,,,,,,,,,,0,,Var(P),,,,
03.08.2021,510.820007,350.519684,51.852196,51.712383,,,,,,,,,,,,RI(P),,,,
04.08.2021,517.349976,358.18399,51.45768,50.503983,,,,,,,,,,,,Sharpe(P),,,,
05.08.2021,524.890015,362.225647,51.740807,50.823849,,,,,,Matriz de Varianzas y Covarianzas Poblacional,,,,,,,,,,
06.08.2021,520.549988,362.764557,51.369938,51.410278,,,,,,,,,,,,Rendimiento esperado y riesgo individual,,,,
09.08.2021,519.969971,360.868408,51.795074,50.823849,,,,,,,,,,,,,Netflix,Meta,Unilever,Exxon
10.08.2021,515.840027,360.389435,51.641304,51.694607,,,,,,,,,,,,RE ,,,,
11.08.2021,512.400024,359.221802,51.867443,51.845657,,,,,,,,,,,,RI,,,,
12.08.2021,510.720001,361.906311,51.587032,51.728405,,,,,,,,,,,,,,,,
13.08.2021,515.919983,362.435211,52.256401,51.20525,,,,,,,,,,,,Indicadores de rendimiento / riesgo,,,,
16.08.2021,517.919983,365.808289,51.740807,50.456615,,,,,,,,,,,,,Netflix,Meta,Unilever,Exxon
17.08.2021,518.909973,357.714935,51.650341,50.113865,,,,,,Factor de Corrección:,,,,,,Sharpe,,,,
18.08.2021,521.869995,354.721069,50.935745,49.058556,,,,,,,,,,,,Rf,,,,
19.08.2021,543.710022,354.391754,50.6101,47.561272,,,,,,,,,,,,,,,,
20.08.2021,546.880005,358.633026,50.990017,47.570297,,,,,,Matriz de Varianzas y Covarianzas Muestral,,,,,,,,,,
23.08.2021,553.330017,362.604889,50.999065,49.52758,,,,,,,Netflix,Meta,Unilever,Exxon,,,,,,
24.08.2021,553.409973,364.760468,50.601063,49.933472,,,,,,Netflix,,,,,,,,,,
25.08.2021,547.580017,367.634552,50.266369,50.023674,,,,,,Meta,,,,,,,,,,
26.08.2021,550.119995,363.632751,50.420147,49.347195,,,,,,Unilever,,,,,,,,,,
27.08.2021,558.919983,371.865845,50.212093,50.303291,,,,,,Exxon,,,,,,,,,,
30.08.2021,566.179993,379.879364,50.474422,49.753071,,,,,,,,,,,,,,,,
31.08.2021,569.190002,378.60199,50.365879,49.175808,,,,,,,,,,,,,,,,
01.09.2021,582.070007,381.26651,50.67342,48.499329,,,,,,,,,,,,,,,,
02.09.2021,588.549988,374.510406,49.624138,49.68092,,,,,,,,,,,,,,,,
03.09.2021,590.530029,375.488403,49.886459,49.491497,,,,,,,,,,,,,,,,
07.09.2021,606.710022,381.396271,49.786961,49.202866,,,,,,,,,,,,,,,,
08.09.2021,606.049988,376.795715,50.130688,48.751881,,,,,,,,,,,,,,,,
09.09.2021,597.539978,377.224823,49.615089,48.78796,,,,,,,,,,,,,,,,
10.09.2021,598.719971,377.913422,49.506546,48.688747,,,,,,,,,,,,,,,,
13.09.2021,589.289978,375.737915,49.949772,49.94249,,,,,,,,,,,,,,,,
14.09.2021,577.76001,375.757843,50.085461,49.229927,,,,,,,,,,,,,,,,
15.09.2021,582.869995,373.153229,49.714588,50.889561,,,,,,,,,,,,,,,,
16.09.2021,586.5,372.294952,49.334679,50.348381,,,,,,,,,,,,,,,,
17.09.2021,589.349976,363.972046,48.800995,49.753071,,,,,,,,,,,,,,,,
20.09.2021,575.429993,354.970551,49.054256,48.427166,,,,,,,,,,,,,,,,
21.09.2021,573.140015,356.746948,49.271362,48.382072,,,,,,,,,,,,,,,,
22.09.2021,590.650024,342.506165,49.388954,49.798176,,,,,,,,,,,,,,,,
23.09.2021,593.26001,345.250549,49.624138,51.484875,,,,,,,,,,,,,,,,
24.09.2021,592.390015,352.236176,49.361813,51.944881,,,,,,,,,,,,,,,,

Resumen numérico:
       Unnamed: 9  Unnamed: 15
count         0.0          0.0
mean          NaN          NaN
std           NaN          NaN
min           NaN          NaN
25%           NaN          NaN
50%           NaN          NaN
75%           NaN          NaN
max           NaN          NaN
