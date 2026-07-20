---
curso: FUNDOPS
titulo: 7 - Casos - Solución de 6 casos
slides: 0
fuente: 7 - Casos - Solución de 6 casos.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 7 - Casos - Solución de 6 casos.xlsx. -->

<!-- INTERPRETAR: datos tabulares de 7 - Casos - Solución de 6 casos.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Caso 1 - Data
Filas: 15 · Columnas: 5
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (object)

Muestra (primeras 15 de 15 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,Mesa de Ayuda,,,
,,,,
,a =,2.0,minutos/correo,
,σa =,3.0,minutos,
,m =,3.0,empleados,
,p =,4.0,minutos,
,σp =,2.0,minutos,
,,,,
,Utilización =,,,
,CVa =,,,
,CVp =,,,
,Tq =,,,Rpta. a
,,,,
,R = λ =,,,
,Iq =,,,Rpta. b

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0     5.00000
mean          NaN     2.80000
std           NaN     0.83666
min           NaN     2.00000
25%           NaN     2.00000
50%           NaN     3.00000
75%           NaN     3.00000
max           NaN     4.00000

## Hoja: Caso 1 - Solución
Filas: 17 · Columnas: 5
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (object)

Muestra (primeras 17 de 17 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,Mesa de Ayuda,,,
,,,,
,a =,2.0,minutos/correo,
,σa =,2.0,minutos,
,m =,3.0,empleados,
,p =,4.0,minutos,
,σp =,2.0,minutos,
,,,,
,Utilización =,0.6666666666666666,,
,CVa =,1.0,,
,CVp =,0.5,,
,Tq =,1.1911596519797847,minutos,Rpta. a
,,,,
,R = λ =,0.5,correos/minuto,
,Iq =,0.5955798259898923,correos,0.5955798259898923
,Ip =,2.0,correos,
,I =,2.5955798259898923,correos,Rpta. b

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0   13.000000
mean          NaN    1.696076
std           NaN    1.082370
min           NaN    0.500000
25%           NaN    0.666667
50%           NaN    2.000000
75%           NaN    2.000000
max           NaN    4.000000

## Hoja: Caso 2 - Data
Filas: 20 · Columnas: 5
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (object)

Muestra (primeras 20 de 20 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,Bufete de Abogados,,,
,,,,
,R = λ =,10.0,correos/hora,
,a =,,minutos/correo,
,CVa =,1.0,,
,m =,1.0,abogado,
,p =,5.0,minutos,
,σp =,4.0,minutos,
,CVp =,,,
,Utilización =,,,
,Tq =,,minutos,
,T =,,minutos,Rpta. a
,1 día =,10.0,horas,
,# Correos =,,correos,Rpta. b
,Tiempo en Casos =,,horas,Rpta. c
,,,,
,σp =,0.5,minutos,
,CVp =,,,
,Tq =,,minutos,
,T =,,minutos,Rpta. e

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0    7.000000
mean          NaN    4.500000
std           NaN    4.112988
min           NaN    0.500000
25%           NaN    1.000000
50%           NaN    4.000000
75%           NaN    7.500000
max           NaN   10.000000

## Hoja: Caso 2 - Solución
Filas: 24 · Columnas: 5
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (object)

Muestra (primeras 24 de 24 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,Bufete de Abogados,,,
,HORARIO: 8:00 -18:00 horas,,,
,R = λ =,10.0,correos/hora,
,a =,6.0,minutos/correo,
,CVa =,1.0,,
,m =,1.0,abogado,
,p =,5.0,minutos/correo,
,σp =,4.0,minutos,
,CVp =,0.8,,
,Utilización =,0.8333333333333334,,0.8333333333333334
,Tq =,20.500000000000007,minutos,20.500000000000007
,T =,25.500000000000007,minutos,Rpta. a
,1 día =,10.0,horas,
,# Correos =,100.0,correos,Rpta. b
,Tiempo en Casos =,1.6666666666666663,horas,Rpta. c
,,,,
,σp =,0.5,minutos,
,Utilización =,0.8333333333333334,,0.8333333333333334
,Tiempo en Casos =,1.6666666666666663,horas,Rpta. d
,La cantidad de tiempo que un abogado dedica a los grandes acuerdos es la misma.,,,
,CVp =,0.1,,
,Tq =,12.625000000000004,minutos,12.625000000000004
,T =,17.625000000000004,minutos,Rpta. e
,El tiempo que un cliente tiene que esperar disminuye.,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0   19.000000
mean          NaN   11.560526
std           NaN   22.715763
min           NaN    0.100000
25%           NaN    0.916667
50%           NaN    4.000000
75%           NaN   11.312500
max           NaN  100.000000

## Hoja: Caso 3 - Data
Filas: 23 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object)

Muestra (primeras 23 de 23 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,Alquiler de Automóviles,,
,,,
,m =,50.0,SUVs
,a =,2.4,horas
,R = λ =,,
,σa =,2.4,horas
,p =,3.0,días
,σp =,1.0,día
,,,
,Utilización =,,
,Nro. SUVs Estacionadas =,,SUVs
,,,
,R =,12.0,solicitudes/día
,a =,2.0,horas
,p =,4.0,días
,,,
,Utilización =,,
,Nro. SUVs Estacionadas =,,SUVs
,,,
,Monto Inicial por Alquiler =,80.0,US$/solicitud
,Ingreso Inicial =,,US$/día
,Monto Final por Alquiler =,55.0,US$/solicitud
,Ingreso Inicial =,,US$/día

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0   10.000000
mean          NaN   21.180000
std           NaN   29.106311
min           NaN    1.000000
25%           NaN    2.400000
50%           NaN    3.500000
75%           NaN   40.500000
max           NaN   80.000000

## Hoja: Caso 3 - Solución
Filas: 37 · Columnas: 5
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (object)

Muestra (primeras 37 de 37 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,Alquiler de Automóviles,,,
,,,,
,m =,50.0,SUVs,
,a =,2.4,horas/solicitud,
,R = λ =,10.0,solicitudes/día,
,σa =,2.4,horas,
,CVa =,1.0,,
,p =,3.0,días,
,σp =,1.0,día,
,CVp =,0.3333333333333333,,
,,,,
,%Utilización =,0.6,,30
,Nro. SUVs Estacionadas =,20.0,SUVs,Answer a
,,,,
,R = λ =,12.0,solicitudes/día,
,a =,2.0,horas,
,p =,4.0,días,
,,,,
,Utilización =,0.96,48,
,Nro. SUVs Estacionadas =,2.0000000000000018,SUVs,
,,,,
,Monto Inicial por Alquiler =,80.0,US$/día,
,Ingreso Inicial =,2400.0,US$/día,
,Monto Final por Alquiler =,55.0,US$/día,
,Ingreso Final =,2640.0,US$/día,
,La reducción de precio hace que el ingreso diario aumente.,,,Answer b
,,,,
,Tq =,1.149390103237377,minutos,Answer c
,,,,
,p =,4.0,días,
,σp =,0.0,días,
,CVp =,0.0,,
,a =,3.0,horas,
,σa =,3.0,horas,
,CVa =,1.0,,
,Utilización =,0.64,,
,Tq =,2.757107494486108,minutos,Answer d

Resumen numérico:
       Unnamed: 0   Unnamed: 2
count         0.0    28.000000
mean          NaN   189.365708
std           NaN   659.354309
min           NaN     0.000000
25%           NaN     1.000000
50%           NaN     2.578554
75%           NaN    10.500000
max           NaN  2640.000000

## Hoja: Caso 4 - Data
Filas: 20 · Columnas: 5
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (object)

Muestra (primeras 20 de 20 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,Tomás Juárez,,,
,,,,
,a =,3.0,minutos/llamada,
,σa =,3.0,minutos,
,CVa =,,,
,R =,,llamadas/minuto,
,p =,2.0,minutos,
,σp =,1.0,minuto,
,CVp =,,,
,Costo de Línea =,5.0,US$/hora,
,Tiempo =,8.0,horas,
,Tiempo =,480.0,minutos,
,Lectura =,1.0,página/minuto,
,Utilización =,,,
,Tiempo de Procesamiento =,,minutos,
,Tiempo para Lectura =,,minutos,
,Nro. de Páginas =,,páginas,Rpta. a)
,Tq =,,minutos,Rpta. b)
,Costo x Llamada =,,US$/llamada,
,Costo de Llamadas x Día =,,US$,

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0    8.000000
mean          NaN   62.875000
std           NaN  168.559813
min           NaN    1.000000
25%           NaN    1.750000
50%           NaN    3.000000
75%           NaN    5.750000
max           NaN  480.000000

## Hoja: Caso 4 - Solución
Filas: 22 · Columnas: 6
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object)

Muestra (primeras 22 de 22 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
,Tomás Juárez,,,,
,,,,,
,a =,3.0,minutos/llamada,,
,σa =,3.0,minutos,,
,CVa =,1.0,,,
,R =,0.3333333333333333,llamadas/minuto,,
,p =,2.0,minutos,,
,σp =,1.0,minuto,,
,CVp =,0.5,,,
,Costo de Línea =,5.0,US$/hora,para Tq y p,
,Tiempo =,8.0,horas,,
,Tiempo =,480.0,minutos,,
,Lectura =,1.0,página/minuto,,
,Utilización =,0.6666666666666666,,,
,Tiempo de Procesamiento =,320.0,minutos,,
,Tiempo para Lectura =,160.0,minutos,,
,Nro. de Páginas =,160.0,páginas,Rpta. a),
,Tq =,2.4999999999999996,minutos,Rpta. b),
,T =,4.5,minutos,,
,Costo x Llamada =,0.375,US$/llamada,,
,Nro. De Llamadas =,160.0,llamadas/día,,
,Costo de Llamadas x Día =,60.0,US$/día,60,Rpta. c)

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0   20.000000
mean          NaN   68.643750
std           NaN  129.594947
min           NaN    0.333333
25%           NaN    1.000000
50%           NaN    3.000000
75%           NaN   85.000000
max           NaN  480.000000

## Hoja: Caso 5 - Data
Filas: 41 · Columnas: 11
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (float64), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object)

Muestra (primeras 40 de 41 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10
,Atlantic Video,,,,,,,,,
,,,,,,,,,,
,R =,30.0,clientes/hora,,,,,,,
,a =,,minutos,,,,,,,
,σa =,2.0,minutos,,,,,,,
,Cva =,,,,,,,,,
,p =,1.7,minutos,,,,,,,
,σp =,3.0,minutos,,,,,,,
,m =,1.0,empleado,,,,,,,
,CVp =,,,,,,,,,
,Utilización =,,,,,,,,,
,,,,,,,,,,
,Tq =,,minutos,,,,,,,
,,,,,,,,,,
,Tiempo Total =,8.0,horas,,,,,,,
,Tiempo de Clasificación =,1.5,minutos/video,,,,,,,
,Tiempo Ocupado =,,minutos,,,,,,,
,Tiempo para Clasificar =,,minutos,,,,,,,
,# Videos Clasificados =,,videos,,,,,,,
,,,,,,,,,,
,Iq =,,clientes,,,,,,,
,Ip =,,clientes,,,,,,,
,I =,,clientes,,,,,,,
,,,,,,,,,,
,% Clientes que no alquilan =,0.1,,,,,,,,
,R' =,,clientes/hora,,,,,,,
,a' =,,minutos,,,,,,,
,Utilización' =,,,,,,,,,
,Tq' =,,minutos,,,,,,,
,,,,,,,,,,
,,,,,m,% Utilización (u = p/am),Tq (minutos),Costo de Empleados por Cliente,Costo de Espera por Cliente,Costo Total por Cliente
,Costo de Espera =,0.75,US$/minuto,,1,,,,,
,Costo de Empleado =,10.0,US$/horaxempleado,,2,,,,,
,,,,,3,,,,,
,,,,,4,,,,,
,,,,,5,,,,,
,,,,,6,,,,,
,,,,,7,,,,,
,,,,,8,,,,,
,,,,,9,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 2  Unnamed: 4
count         0.0   10.000000         0.0
mean          NaN    5.805000         NaN
std           NaN    9.108801         NaN
min           NaN    0.100000         NaN
25%           NaN    1.125000         NaN
50%           NaN    1.850000         NaN
75%           NaN    6.750000         NaN
max           NaN   30.000000         NaN

## Hoja: Caso 5 - Solución
Filas: 41 · Columnas: 11
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object)

Muestra (primeras 40 de 41 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10
,Atlantic Video,,,,,,,,,
,m=1,,,,,,,,,
,R =,30.0,clientes/hora,,,,,,,
,a =,2.0,minutos/cliente,,,,,,,
,σa =,2.0,minutos/cliente,,,,,,,
,Cva =,1.0,,,,,,,,
,p =,1.7,minutos/cliente,,,,,,,
,σp =,3.0,minutos/cliente,,,,,,,
,m =,1.0,empleado,,,,,,,
,CVp =,1.7647058823529411,,,,,,,,
,Utilización =,0.85,,0.85,,,,,,
,,,,,,,,,,
,Tq =,19.81666666666666,minutos,Answer a,,,,,,
,,,,,,,,,,
,Tiempo Total =,8.0,horas,,,,,,,
,Tiempo de Clasificación =,1.5,minutos/video,,,,,,,
,Tiempo Ocupado =,408.0,minutos,,,,,,,
,Tiempo para Clasificar =,72.0,minutos,,,,,,,
,# Videos Clasificados =,48.0,videos,Answer b,,,1.7,,,
,,,,,,,5.666666666666666,,,
,Iq =,9.90833333333333,clientes,,,,2.057093425605536,,,
,Ip =,0.85,clientes,u,,,19.816666666666663,,,
,I =,10.75833333333333,clientes,Answer c,,,,,,
,,,,,,,,,,
,% Clientes que no alquilan =,0.1,,,,,,,,
,R' =,27.0,clientes/hora,,,,,,,
,a' =,2.2222222222222223,minutos,,,,,,,
,Utilización' =,0.7649999999999999,,0.7649999999999999,,,,,,
,Tq' =,11.384042553191481,minutos,considerar que el CVp sigue igual,,,,cost empleado * m / flujo,,$/hrxemp * emplea /cliente/hora
,,,,,,,,,,
,,,,,m,% Utilización (u = p/am),Tq (minutos),Costo de Empleados por Cliente,Costo de Espera por Cliente,Costo Total por Cliente
,Costo de Espera =,0.75,US$/minuto,,1,0.85,19.81666666666666,0.3333333333333333,14.862499999999994,15.195833333333328
,Costo de Empleado =,10.0,US$/horaxempleado,,2,0.425,0.8797487592982575,0.6666666666666666,0.6598115694736931,1.3264782361403598
,,,,,3,0.2833333333333333,0.1621177930761624,1,0.1215883448071218,1.1215883448071218
,,,,,4,0.2125,0.03899021538744555,1.3333333333333333,0.029242661540584164,1.3625759948739173
,,,,,5,0.16999999999999998,0.010700468308518582,1.6666666666666667,0.008025351231388936,1.6746920178980558
,,,,,6,0.14166666666666666,0.003198618621129555,2,0.0023989639658471666,2.002398963965847
,,,,,7,0.12142857142857143,0.00101810009718173,2.3333333333333335,0.0007635750728862975,2.3340969084062198
,,,,,8,0.10625,0.0003405112748212082,2.6666666666666665,0.00025538345611590614,2.6669220501227824
,,,,,9,0.09444444444444444,0.00011863655205224077,3,8.897741403918058e-05,3.0000889774140393

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0   25.000000
mean          NaN   26.974772
std           NaN   81.221162
min           NaN    0.100000
25%           NaN    1.000000
50%           NaN    2.222222
75%           NaN   11.384043
max           NaN  408.000000

## Hoja: Caso 6 - Data
Filas: 29 · Columnas: 5
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (object)

Muestra (primeras 29 de 29 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
,RentAPhone - Alquiler de Celulares,,,
,,,,
,m =,80.0,,
,R =,25.0,clientes/día,
,a =,,horas/cliente,
,CVa =,1.0,,
,p =,72.0,horas,
,σp =,100.0,horas,
,CVp =,,,
,Costo de Tarjetas =,1.0,$/horaxcliente en cola,
,% Utilización =,,,
,# Promedio de Celulares en Tienda =,,celulares,Rpta. a)
,Tq =,,horas,Rpta. b)
,Iq =,,clientes,
,Gasto en Tarjetas =,,$/mes,Rpta. c)
,,,,
,Costo de un Celular =,1000.0,$/unidad,
,Cantidad de Celulares a Comprar =,1.0,celular,
,m =,,celulares,
,% Utilización =,,,
,Tq =,,horas,
,Iq =,,clientes,
,Gasto en Tarjetas =,,$/mes,Rpta. d)
,Ahorro Mensual =,,US$/mes,
,σp =,0.0,horas,
,CVp =,0.0,,
,R =,20.0,clientes/día,
,% Utilización =,,,
,Tq =,,horas,Rpta. e)

Resumen numérico:
       Unnamed: 0   Unnamed: 2
count         0.0    11.000000
mean          NaN   118.181818
std           NaN   294.783927
min           NaN     0.000000
25%           NaN     1.000000
50%           NaN    20.000000
75%           NaN    76.000000
max           NaN  1000.000000

## Hoja: Caso 6 - Solución
Filas: 31 · Columnas: 6
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object)

Muestra (primeras 31 de 31 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
,RentAPhone - Alquiler de Celulares,,,,
,,,,,
,m =,80.0,,,
,R =,25.0,clientes/día,,
,a =,0.96,horas/cliente,,
,CVa =,1.0,,,
,p =,72.0,horas,,
,σp =,100.0,horas,,
,CVp =,1.3888888888888888,,,
,Costo de Tarjetas =,1.0,$/horaxcliente en cola,,
,% Utilización =,0.9375,,0.9375,
,# Promedio de Celulares en Tienda =,5.0,celulares,Rpta. a),1-u%
,Tq =,9.893159542153679,horas,Rpta. b),
,Iq =,10.30537452307675,clientes,,
,Gasto en Tarjetas =,7419.86965661526,$/mes,Rpta. c),
,,,,,
,Costo de un Celular =,1000.0,$/unidad,,
,Cantidad de Celulares a Comprar =,1.0,celular,,
,m =,81.0,celulares,,
,% Utilización =,0.925925925925926,,,
,Tq =,7.083751055524684,horas,,
,Iq =,7.378907349504879,clientes,,
,Gasto en Tarjetas =,5312.813291643513,$/mes,Rpta. d),
,Ahorro Mensual =,2107.056364971747,US$/mes,,
,σp =,0.0,horas,,
,CVp =,0.0,,,
,R =,20.0,clientes/día,,
,a =,1.2000000000000002,horas/cliente,,
,% Utilización =,0.7499999999999999,,,
,Tq =,0.06165960520843012,horas,Rpta. e),
,Tq =,3.699576312505807,minutos,Rpta. e),

Resumen numérico:
       Unnamed: 0   Unnamed: 2
count         0.0    28.000000
mean          NaN   581.083002
std           NaN  1713.727317
min           NaN     0.000000
25%           NaN     0.990000
50%           NaN     6.041876
75%           NaN    74.000000
max           NaN  7419.869657
