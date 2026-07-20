---
curso: CONTAGER
titulo: S6 Calculo de utilidades
slides: 0
fuente: S6 Calculo de utilidades.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: S6 Calculo de utilidades.xlsx. -->

<!-- INTERPRETAR: datos tabulares de S6 Calculo de utilidades.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Teoria
Filas: 9 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (float64), Unnamed: 2 (float64), Unnamed: 3 (object)

Muestra (primeras 9 de 9 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,,,
,,,"La participación en las utilidades depende de la actividad que realice el empleador, como se muestra a continuación:"
,,,·Empresas Pesqueras 10%
,,,·Empresas de Telecomunicaciones 10%
,,,·Empresas Industriales 10%
,,,·Empresas Mineras 8%
,,,·Empresas de Comercio al por mayor y al por menor y Restaurantes 8%
,,,·Empresas que realizan otras actividades 5%
,,,·Empresas agrarias 5%*

Resumen numérico:
       Unnamed: 0  Unnamed: 1  Unnamed: 2
count         0.0         0.0         0.0
mean          NaN         NaN         NaN
std           NaN         NaN         NaN
min           NaN         NaN         NaN
25%           NaN         NaN         NaN
50%           NaN         NaN         NaN
75%           NaN         NaN         NaN
max           NaN         NaN         NaN

## Hoja: Caso 1
Filas: 30 · Columnas: 9
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (float64), Unnamed: 7 (float64), Unnamed: 8 (float64)

Muestra (primeras 30 de 30 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8
,,,,,,,,
,,LIQUIDACION DE DISTRIBUCION DE UTILIDADES  - EJERCICIO 2020,,,,,,
,,OMEGA S.A. RUC. 20101210201,,Empresa pertenece al sector pesquero,,,,
,,(D.L. N° 892 D.S. N° 009-98-TR),,,Ver % que le corresponde a este sector ,,,
,,Correspondiente al ejercicio 2020,,,economico,,,
,,,,,,,,
,CALCULO DEL MONTO DE LA PARTICIPACION EN LAS UTILIDADES,,,,,,,
,1.- UTILIDAD POR DISTRIBUIR,,,,,,,
,§Renta Anual de la empresa antes del impuesto:,78554780,"Resultado antes de participaciones e impuestos, dato del Estado de Resultados",,,,,
,§Porcentaje a distribuir:,0.1,,,,,,
,§Monto distribuir:,7855478,(multiplico el resultado antes de partici e impuestos x 10%),,,,,
,2.- CALCULO DE LA PARTICIPACION ,,,,,,,
,      2.1.-Según los días laborados,,Dato que lo da RRHH,,,,,
,        Numero de días laborados durante el ejercicio 2020 por todos los trabajadores,,,,,,,12.24052293692346
,        de la empresa con derecho a percibir utilidades:,320880,diastrabajados por todo el personal durante el año 2020,,,,,
,§Factor días laborados(50% monto a distribuir/total días laborados):                     ,12.24052293692346,,,,,,
,§Numero de días laborados durante el ejercicio 2020 por el trabajador:,32,Pepito Perez trabajador en planilla laboro durante el periodo 2020 32 dias,,,,,391.6967339815507
,Participación del trabajador según los días trabajados:,391.6967339815507,,,,,,
,       2.2.- Según las Remuneraciones percibidas ,,,Dato ,,,,
,§Remuneración computable total pagada durante el ejercicio 2020 a todos los ,,Dato que lo da RRHH,,,,,
,        trabajadores de la empresa:,45856523.8,,,,,,
,§Factor remuneración(50% monto a distribuir/total remuneración:,0.08565278556941118,,,,,,
,§Remuneración computable percibida durante el ejercicio 2020 por el trabajador.,4230.3,Salario mensual de Pepito Perez,,,,,
,        Participación del trabajador según las remuneraciones percibidas:,362.3369787942801,( 4230.30*0.0856527),,,,,
,3.- CALCULO DE LA PARTICIPACION,,,,,,,
,§Retención Judicial:,300,Suponga que hay una retencion judicial pendiente por descontarle a Pepito Perez,,,,,
,§Impuesto a la Renta de 5ta Categoría ,100,Suponga que hay un descuento de impuesto de 5ta categoria pendiente por descontarle,,,,,
,, ,,,,,,
,§NETO A PAGAR AL TRABAJADOR,354.03371277583085,"Neto a pagar a Pepito Perez, transferencia bancaria o cheque.",,,,,
,,,por el periodo 2020,,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 6  Unnamed: 7  Unnamed: 8
count         0.0         0.0         0.0    2.000000
mean          NaN         NaN         NaN  201.968628
std           NaN         NaN         NaN  268.316060
min           NaN         NaN         NaN   12.240523
25%           NaN         NaN         NaN  107.104576
50%           NaN         NaN         NaN  201.968628
75%           NaN         NaN         NaN  296.832681
max           NaN         NaN         NaN  391.696734

## Hoja: Caso 2
Filas: 31 · Columnas: 6
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (float64), Unnamed: 5 (object)

Muestra (primeras 31 de 31 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
,,CASO PRACTICO DE UTILIDADES,,,
,,LIQUIDACION DE DISTRIBUCION DE UTILIDADES  - EJERCICIO 2020,,,
,,HIRAOKA S.A. RUC.  ,,,El sector economico de Hiraoka es comercial
,,(D.L. N° 892 D.S. N° 009-98-TR),,,"Dato se toma de la tabla de ""teoria"""
,,,,,
,,,,,
,CALCULO DEL MONTO DE LA PARTICIPACION EN LAS UTILIDADES,,,,
,1.- UTILIDAD POR DISTRIBUIR,,,,
,§Renta Anual de la empresa antes del impuesto:,3000000,"Resultado antes de participaciones e impuestos, dato del Estado de Resultados",,
,§Porcentaje a distribuir:,0.08,,,
,§Monto distribuir:,240000,,,
,2.- CALCULO DE LA PARTICIPACION ,,,,
,      2.1.-Según los días laborados,,Dato que lo da RRHH,,
,        Numero de días laborados durante el ejercicio 2020 por todos los trabajadores,,,,
,        de la empresa con derecho a percibir utilidades:,10800,,,
,§Factor días laborados(50% monto a distribuir/total días laborados):                     ,11.11111111111111,,,
,§Numero de días laborados durante el ejercicio 2020 por el trabajador:,100,Dias trabajados de la Srta Evelyn Poblete durante el año 2020.,,
,Participación del trabajador según los días trabajados:,1111.111111111111,,,
,       2.2.- Según las Remuneraciones percibidas ,,,,
,§Remuneración computable total pagada durante el ejercicio 2020 a todos los ,,,,
,        trabajadores de la empresa:,960000,Dato que lo tiene el Area de RRHH,,
,§Factor remuneración(50% monto a distribuir/total remuneración:,0.125,,,
,§Remuneración computable percibida durante el ejercicio 2020 por el trabajador.,3000,S/3000 es la remuneracion mensual de la trabajadora Evelyn Poblete,,
,        Participación del trabajador según las remuneraciones percibidas:,375,,,
,,,,,
,3.- CALCULO DE LA PARTICIPACION,,,,
,§Retención Judicial:,0,,,
,§Impuesto a la Renta de 5ta Categoría ,0,,,
, , ,,,
,§NETO A PAGAR,1486.111111111111,Lo que se paga al trabajador por sus utilidades del año 2020,,
,"Fecha, 12 de abril 2021. ",,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 4
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN

## Hoja: Caso 3
Filas: 31 · Columnas: 6
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (float64), Unnamed: 5 (object)

Muestra (primeras 31 de 31 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
,,CASO PRACTICO DE UTILIDADES,,,
,,LIQUIDACION DE DISTRIBUCION DE UTILIDADES  - EJERCICIO 2020,,,
,,CLARO S.A. RUC.  ,,,Sector telecomunicaciones
,,(D.L. N° 892 D.S. N° 009-98-TR),,,
,,Correspondiente al ejercicio 2020,,,
,,,,,
,CALCULO DEL MONTO DE LA PARTICIPACION EN LAS UTILIDADES,,,,
,1.- UTILIDAD POR DISTRIBUIR,,,,
,§Renta Anual de la empresa antes del impuesto:,12000000,,,
,§Porcentaje a distribuir:,0.1,,,
,§Monto distribuir:,1200000,,,
,2.- CALCULO DE LA PARTICIPACION ,,,,
,      2.1.-Según los días laborados,,,,
,        Numero de días laborados durante el ejercicio 2020 por todos los trabajadores,,,,
,        de la empresa con derecho a percibir utilidades:,310000,,,
,§Factor días laborados(50% monto a distribuir/total días laborados):                     ,1.935483870967742,,,
,§Numero de días laborados durante el ejercicio 2020 por el trabajador:,260,dias que trabajo Carlita Rivera  en el año 2020,,
,Participación del trabajador según los días trabajados:,503.2258064516129,,,
,       2.2.- Según las Remuneraciones percibidas ,,,,
,§Remuneración computable total pagada durante el ejercicio 2020 a todos los ,,,,
,        trabajadores de la empresa:,2000000,,,
,§Factor remuneración(50% monto a distribuir/total remuneración:,0.3,,,
,§Remuneración computable percibida durante el ejercicio 2020 por el trabajador.,10000,,,
,        Participación del trabajador según las remuneraciones percibidas:,3000,,,
,3.- CALCULO DE LA PARTICIPACION,,,,
,§Retención Judicial:,S/.                   0.00,En este caso no hay descuentos ni retenciones de ley,,
,§Impuesto a la Renta de 5ta Categoría ,S/.                   0.00,a la trabajadora Carlita Rivera,,
,  , ,,,
,§NETO A PAGAR,3503.2258064516127,Lo que se le paga a Carlita Rivera por sus utilidades ,,
,"Fecha, 12 de abril 2021. ",,que le corresponden por el periodo 2020,,
,,,Recuerde que se le paga por transferencia o por cheque.,,

Resumen numérico:
       Unnamed: 0  Unnamed: 4
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN

## Hoja: Alumnos
Filas: 10 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object)

Muestra (primeras 10 de 10 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,Empresa Haylux S.A.C perteneciente al sector pesca,,
, Renta Anual de la empresa antes del impuesto:(Dato que se obtiene del Estado de Resultados), S/.68 550 700 ,SOLES
, Numero de días laborados durante el ejercicio 2020 por todos los trabajadores,,
, de la empresa con derecho a percibir utilidades:,285000,DIAS
,"Maria Jose Sifuentes Diaz trabajo durante el periodo 2020, 45 dias",,
,  Remuneración computable total pagada durante el ejercicio 2020 a todos los ,,
,  trabajadores de la empresa:,S/. 35 850  500 ,SOLES
, Remuneración computable percibida durante el ejercicio 2020 por el trabajadora Maria Jose Sifuentes Diaz,3800,SOLES
, Retención Judicial pendiente de descontarle,150,SOLES
, Impuesto a la Renta de 5ta Categoría pendiente de descontarle,80,SOLES

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

## Hoja: Plantilla
Filas: 29 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object)

Muestra (primeras 29 de 29 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,,CASO PRACTICO DE UTILIDADES,
,,LIQUIDACION DE DISTRIBUCION DE UTILIDADES  - EJERCICIO 2021,
,,EMPRESA:,
,,(D.L. N° 892 D.S. N° 009-98-TR),
,,,
,CALCULO DEL MONTO DE LA PARTICIPACION EN LAS UTILIDADES,,
,1.- UTILIDAD POR DISTRIBUIR,,
,§Renta Anual de la empresa antes del impuesto:,,
,§Porcentaje a distribuir:,,
,§Monto distribuir:,,
,2.- CALCULO DE LA PARTICIPACION ,,
,      2.1.-Según los días laborados,,
,        Numero de días laborados durante el ejercicio 2020 por todos los trabajadores,,
,        de la empresa con derecho a percibir utilidades:,,
,§Factor días laborados(50% monto a distribuir/total días laborados):                     ,,
,§Numero de días laborados durante el ejercicio 2020 por el trabajador:,,
,Participación del trabajador según los días trabajados:,,
,       2.2.- Según las Remuneraciones percibidas ,,
,§Remuneración computable total pagada durante el ejercicio 2020 a todos los ,,
,        trabajadores de la empresa:,,
,§Factor remuneración(50% monto a distribuir/total remuneración:,,
,§Remuneración computable percibida durante el ejercicio 2020 por el trabajador.,,
,        Participación del trabajador según las remuneraciones percibidas:,,
,3.- CALCULO DE LA PARTICIPACION,,
,§Retención Judicial:,,
,§Impuesto a la Renta de 5ta Categoría ,,
,  , ,
,§NETO A PAGAR,,Neto a pagar a la trabajadora Maria Jose Sifuentes
,"Fecha, 12 de abril 2021. ",,

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

## Hoja: Hoja1
Filas: 29 · Columnas: 3
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object)

Muestra (primeras 29 de 29 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2
,,CASO PRACTICO DE UTILIDADES
,,LIQUIDACION DE DISTRIBUCION DE UTILIDADES  - EJERCICIO 2021
,,EMPRESA:
,,(D.L. N° 892 D.S. N° 009-98-TR)
,,
,CALCULO DEL MONTO DE LA PARTICIPACION EN LAS UTILIDADES,
,1.- UTILIDAD POR DISTRIBUIR,
,§Renta Anual de la empresa antes del impuesto:,
,§Porcentaje a distribuir:,
,§Monto distribuir:,
,2.- CALCULO DE LA PARTICIPACION ,
,      2.1.-Según los días laborados,
,        Numero de días laborados durante el ejercicio 2021 por todos los trabajadores,
,        de la empresa con derecho a percibir utilidades:,
,§Factor días laborados,
,§Numero de días laborados durante el ejercicio 2021 por el trabajador:,
,Participación del trabajador según los días trabajados:,
,       2.2.- Según las Remuneraciones percibidas ,
,§Remuneración computable total pagada durante el ejercicio 2021 a todos los ,
,        trabajadores de la empresa:,
,§Factor remuneración,
,§Remuneración computable percibida durante el ejercicio 2021 por el trabajador.,
,        Participación del trabajador según las remuneraciones percibidas:,
,3.- CALCULO DE LA PARTICIPACION,
,§Retención Judicial:,
,§Impuesto a la Renta de 5ta Categoría ,
,  , 
,§NETO A PAGAR,
,"Fecha, 12 de abril 2021. ",

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

## Hoja: Hoja2
Filas: 10 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (float64), Unnamed: 2 (object), Unnamed: 3 (object)

Muestra (primeras 10 de 10 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,,Empresa Hiraoka S.A.C perteneciente al sector comercial.,Tasa 8%
,,Renta Anual de la empresa antes del impuesto:, S/.98 550 000 
,, Numero de días laborados durante el ejercicio 2021 por todos los trabajadores,
,, de la empresa con derecho a percibir utilidades:,295000
,,"El trabajador laboro durante el periodo 2020, 45 dias",
,,Remuneración computable total pagada durante el ejercicio 2021 a todos los ,
,,  trabajadores de la empresa:,S/. 45 810  600 
,,Remuneración computable percibida durante el ejercicio 2021 por el trabajador,4000
,,No tiene ninguna Retención Judicial  pendiente de descontarle,
,,Impuesto a la Renta de 5ta Categoría pendiente de descontarle,120

Resumen numérico:
       Unnamed: 0  Unnamed: 1
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN
