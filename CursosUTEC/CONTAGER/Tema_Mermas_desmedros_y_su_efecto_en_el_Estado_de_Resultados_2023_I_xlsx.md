---
curso: CONTAGER
titulo: Tema Mermas desmedros y su efecto en el Estado de Resultados 2023-I
slides: 0
fuente: Tema Mermas desmedros y su efecto en el Estado de Resultados 2023-I.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Tema Mermas desmedros y su efecto en el Estado de Resultados 2023-I.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Tema Mermas desmedros y su efecto en el Estado de Resultados 2023-I.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: MERMAS Y DESMEDROS
Filas: 15 · Columnas: 13
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (float64), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (float64), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (float64), Unnamed: 8 (float64), Unnamed: 9 (float64), Unnamed: 10 (float64), Unnamed: 11 (object), Unnamed: 12 (object)

Muestra (primeras 15 de 15 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12
,,,,,,,,,,,INVENTARIOS (NIC 2),
,,,,,,,,,,,,
,,,,,,,,,,,MATERIA PRIMA,
,,,,,,,,,,,PRODUCTOS EN PROCESO,
,,,,,,,,,,,PRODUCTO TERMINADO,
,,,,,,,,,,,ENVASES Y EMBALAJES,
,,,,,,,,,,,MERCADERIAS,
,,,,,,,,,,,SUMINISTROS,
,,,,,,,,,,,,EERR
,,,,,,,,,,,COSTO,GASTO
,,,,,,,,,,,MERMA,MERMA
,,,,,,,,,,,NORMAL,ANORMAL
,,,,,,,,,,,,
,,,,,,,,,,,,DESMEDRO
,,,,,,,,,,,,ANORMAL

Resumen numérico:
       Unnamed: 0  Unnamed: 1  Unnamed: 2  Unnamed: 3  Unnamed: 4  Unnamed: 5  Unnamed: 6  Unnamed: 7  Unnamed: 8  Unnamed: 9  Unnamed: 10
count         0.0         0.0         0.0         0.0         0.0         0.0         0.0         0.0         0.0         0.0          0.0
mean          NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN
std           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN
min           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN
25%           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN
50%           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN
75%           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN
max           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN

## Hoja: Gastos
Filas: 13 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (float64), Unnamed: 3 (object)

Muestra (primeras 13 de 13 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,GASTOS DEDUCIBLES,,GASTOS QUE SUNAT SI PERMITE QUE LOS RESTES EN EL ESTADO DE RESULTADOS
,,,EJEMPLOS
,,,GASTOS DE PLANILLA DE TU PERSONAL CON CONTRATO
,,,"GASTOS DE AGUA,LUZ TELEFONIA PAGADOS CON MEDIOS DE PAGO"
,,,
,GASTOS NO DEDUCIBLES,,AQUELLOS GASTOS QUE EXDECEN LOS LIMITES PERMITIDOS POR
,,,LA ADMINISTRACION TRIBUTARIA
,,,GASTOS QUE SUNAT NO ACEPTA QUE LOS RESTES EN EL ESTADO DE RESULTADOS
,,,
,EJEMPLOS DE GASTOS NO DEDUCIBLES,,
,GASTOS POR COMPRAS SIN COMPROBANTES DE PAGO,,
,GASTOS POR COMPRAS CON COMPROBANTES CON ENMENDADURAS O TACHAS,,
,"GASTOS POR COMPRAS ECHAS EN EFECTIVO, ES DECIR SIN USAR MEDIOS DE PAGO.",,

Resumen numérico:
       Unnamed: 0  Unnamed: 2
count         0.0         0.0
mean          NaN         NaN
std           NaN         NaN
min           NaN         NaN
25%           NaN         NaN
50%           NaN         NaN
75%           NaN         NaN
max           NaN         NaN

## Hoja: APLICACION EERR
Filas: 27 · Columnas: 12
Columnas y tipos: Unnamed: 0 (object), Unnamed: 1 (float64), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (float64), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (float64), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object)

Muestra (primeras 27 de 27 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11
,,,ESTADO DE RESULTADOS,,,,,,,,
,,,SOLES,,,,,SE INCLUYE LA,,,
,,,EMPRESA ABC,,,,,MERMA NORMAL,,,
,,+,VENTAS,,500000,,,COMO PARTE DEL,,,
,,-,"DEV,DSCT,REBA,ANULAC",,0,,,COSTO DE VENTAS,,,
,,=,VENTA NETA,,500000,,,,,,
,,-,COSTO DE VENTAS,,3200,,,,,,
,,=,UTILIDAD BRUTA,,496800,,,,,,
GO: GA y GV,,-,GASTOS ADMINISTRATIVOS,,6000,MERMA ANORMAL,,CON INFORME TECNICO DE POR QUE SUCEDIÓ,,,
,,,,,8000,DESMEDRO DE LA HARINA,,SE DESTRUYE POR ORDEN DE SUNAT,,,
,,-,GASTOS DE VENTAS,,1000,,,,,,
,,+,OTROS INGRESOS,,0,,,,SUPONGA QUE SUNAT LE OBSERVA ESTOS GASTOS Y NO SON ACEPTADOS COMO GASTOS,,
,,=,RESULTADO OPERATIVO,,481800,,,,,,
,,-,GASTOS FINANCIEROS,,100,,,,,,
,,+,INGRESOS FINANCIEROS,,50,,,,IMPUESTO A LA RENTA 29.5%,,
,,=,RESULTADOS ANTES DE PARTICIPACIONES E  IMPUESTOS,,,,481750.0,,142116.25,CONTABLE,
,,,ADICIONES:,,,,,,,,
,,+,GASTO POR MERMA NO SUSTENTADOS ADECUADAMENTE,,,,6000.0,,,,
,,+,GASTO POR DESMEDRO NO SUSTENTADO ADECUADAMENTE,,,,8000.0,,IMPUESTO A LA RENTA 29.5%,,
,,,RESULTADO ANTES DE PARTICIPACIONES E IMPUESTOS AJUSTADO,,,,495750.0,,146246.25,SEGÚN SUNAT,
,,,,,(Según Sunat),,,,,,
,,,,,,,,,DIFERENCIA CONTABLE VERSUS TRIBUTARIA,,
,,,,,,,,,4130,,
,,,,,,,,,,,LA DIFERENCIA
,,,,,,,,,,,AFECTA AL FLUJO DE CAJA
,,,,,,,,,,,PROYECTADO Y
,,,,,,,,,,,TE ASIGNAN MULTA E INTERESES

Resumen numérico:
       Unnamed: 1  Unnamed: 4     Unnamed: 7
count         0.0         0.0       4.000000
mean          NaN         NaN  247875.000000
std           NaN         NaN  278198.407915
min           NaN         NaN    6000.000000
25%           NaN         NaN    7500.000000
50%           NaN         NaN  244875.000000
75%           NaN         NaN  485250.000000
max           NaN         NaN  495750.000000

## Hoja: ADICIONES
Filas: 20 · Columnas: 11
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (float64), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (float64), Unnamed: 10 (object)

Muestra (primeras 20 de 20 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10
,,,,,,,,,,
,EL GASTO ES NO DEDUCIBLE PARA LA DETERMINACION DE LA BASE PARA EL CALCULO DEL IMPUESTO A LA RENTA,,,,,,,,,
,CUANDO:,,PERIODO 2022,,,,S/.,,,
,NO ESTAN RELACIONADOS CON LA ACTIVIDAD DE LA EMPRESA,,UTILIDAD ANTES DE PARTICIPACIONES E IMPUESTOS,,,,200000,(CONTABLE),,
,LAS MULTAS IMPUESTAS,,IMPUESTO A LA RENTA,,,,59000,(CONTABLE),,
,GASTOS CON COMPROBANTES DE PAGO DE,,ADICIONES:,,,,,,,
,PROVEEDORES NO HABIDOS O CON ENMENDADURAS,+,GASTO POR VIAJE NO SUSTENTADO,,,,4000,,,
,O ERRORES DE EMISION,+,MULTA,,,,1000,,,
,GASTOS DE INDOLE PERSONAL,+,GASTO SIN COMPROBANTES DE PAGO,,,,3112,,,
,GASTOS POR DONACIONES SUPERIOR AL LIMITE PERMITIDO,+,GASTOS POR COMPROBANTES MAL EMITIDOS,,,,2500,,,
,(Tope maximo 1.5% de las ventas anuales),+,GASTOS DE MOVILIDAD Y ALIMENTACION QUE EXCEDEN EL LIMITE,,,,1000,,,
,GASTOS DE COBRANZA DUDOSA NO PERMITIDOS,+,GASTOS POR DONACIONES QUE EXCEDEN EL LIMITE PERMITIDO,,,,1800,,,DIFERENCIA:
,"(PARTES RELACIONADAS,CON GARANTIAS,PRORROGADOS)",+,GASTOS DE COBRANZA DUDOSA NO AUTORIZADOS,,,,1200,,,6965.539999999994
,MERMA ANORMAL SIN INFORME TECNICO,+,GASTO POR MERMA ANORMAL SIN INFORME TECNICO,,,,4000,,,EFECTO
,DESMEDRO SIN INFORME TECNICO DE QUE FUE DESTRUIDO,+,GASTO POR DESMEDRO SIN EVIDENCIA DE DESTRUCCION TOTAL,,,,5000,,,PAGO MAS
,GASTOS PAGADOS SIN HACER USO DE MEDIOS DE PAGO,,UTILIDAD TRIBUTARIA,,,,223612,,,IMPUESTOS
,GASTOS DE MOVILIDAD X DIA LIMITE MAXIMO 4% DE LA R.M.V,,IMPUESTO A LA RENTA,,,,65965.54,,,A SUNAT
,EXCESO DE REMUNERACIONES DEL DIRECTORIO,,,,,,,,,AFECTA
,"(UTILIDAD ANUAL + SUELDOS DE DIRECTORES) *6%, es el tope maximo.",,,,,,,,,EL FLUJO DE 
,LIMITE DE GASTOS RECREATIVOS PARA EL PERSONAL HASTA 40 U.I.T,,,,,,,,,CAJA

Resumen numérico:
       Unnamed: 0  Unnamed: 4  Unnamed: 5  Unnamed: 6  Unnamed: 9
count         0.0         0.0         0.0         0.0         0.0
mean          NaN         NaN         NaN         NaN         NaN
std           NaN         NaN         NaN         NaN         NaN
min           NaN         NaN         NaN         NaN         NaN
25%           NaN         NaN         NaN         NaN         NaN
50%           NaN         NaN         NaN         NaN         NaN
75%           NaN         NaN         NaN         NaN         NaN
max           NaN         NaN         NaN         NaN         NaN

## Hoja: CASO STUDENTS
Filas: 19 · Columnas: 13
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (float64), Unnamed: 4 (object), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (float64), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (float64), Unnamed: 11 (object), Unnamed: 12 (object)

Muestra (primeras 19 de 19 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12
,,,,,,,,,,,,
,EL GASTO ES NO DEDUCIBLE PARA LA DETERMINACION DE LA BASE PARA EL CALCULO DEL IMPUESTO A LA RENTA,,,,,,,,,,,
,CUANDO:,,,PERIODO 2021,,,,S/.,,,,
1.0,NO ESTAN RELACIONADOS CON LA ACTIVIDAD,S/.,,UTILIDAD ANTES DE PARTICIPACIONES E IMPUESTOS,,,,250000,(CONTABLE),,,
,ECONOMICA DE LA EMPRESA,10000,,IMPUESTO A LA RENTA 29.5%,,,,,(CONTABLE),,,
2.0,LAS MULTAS,16000,,ADICIONES:,,,,,,,,
3.0,DESMEDRO SIN INFORME TECNICO DE QUE FUE DESTRUIDO,5000,,,,,,,,,,
4.0,GASTOS CON COMPROBANTES DE PAGO DE,20000,,,,,,,,,,
,PROVEEDORES NO HABIDOS O CON ENMENDADURAS,,,,,,,,,,,
,O ERRORES DE EMISION,,,,,,,,,,,
5.0,GASTOS DE INDOLE PERSONAL,2800,,,,,,,,,,
6.0,GASTOS POR DONACIONES SUPERIOR AL LIMITE PERMITIDO,500,,,,,,,,,,Soles
7.0,GASTOS DE COBRANZA DUDOSA NO PERMITIDOS,2600,,,,,,,,,,
,"(PARTES RELACIONADAS,CON GARANTIAS,PRORROGADOS)",,,,,,,,,,EFECTO,
8.0,MERMA ANORMAL SIN INFORME TECNICO,7800,,,,,,,,,PAGO MAS,
9.0,COMPRAS HECHAS AL CONTADO(sin medios de pago),5000,,UTILIDAD TRIBUTARIA,,,,,,,IMPUESTOS,
,,,,IMPUESTO A LA RENTA 29.5%,,,,,,,A SUNAT,
,,,,,,,,,,,GOLPEA MI FLUJO DE CAJA PROYECTADO,
,,,,,,,,,,,MAS INTERESES Y MULTAS POR DECLARAR DATOS FALSOS,

Resumen numérico:
       Unnamed: 0  Unnamed: 3  Unnamed: 5  Unnamed: 6  Unnamed: 7  Unnamed: 10
count    9.000000         0.0         0.0         0.0         0.0          0.0
mean     5.000000         NaN         NaN         NaN         NaN          NaN
std      2.738613         NaN         NaN         NaN         NaN          NaN
min      1.000000         NaN         NaN         NaN         NaN          NaN
25%      3.000000         NaN         NaN         NaN         NaN          NaN
50%      5.000000         NaN         NaN         NaN         NaN          NaN
75%      7.000000         NaN         NaN         NaN         NaN          NaN
max      9.000000         NaN         NaN         NaN         NaN          NaN

## Hoja: Tips
Filas: 13 · Columnas: 14
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (float64), Unnamed: 2 (float64), Unnamed: 3 (float64), Unnamed: 4 (float64), Unnamed: 5 (float64), Unnamed: 6 (float64), Unnamed: 7 (float64), Unnamed: 8 (float64), Unnamed: 9 (float64), Unnamed: 10 (float64), Unnamed: 11 (object), Unnamed: 12 (float64), Unnamed: 13 (object)

Muestra (primeras 13 de 13 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13
,,,,,,,,,,,,,
,,,,,,,,,,,LEY DE BANCARIZACION,,
,,,,,,,,,,,$1000,,
,,,,,,,,,,,,,
,,,,,,,,,,,COMPRO EN WILSON AL CONTADO,,
,,,,,,,,,,,$1400,,
,,,,,,,,,,,,,
,,,,,,,,,,,,,
,,,,,,,,,,,EFECTOS:,,
,,,,,,,,,,,PAGARAS MAS IMPUESTO A LA RENTA,,
,,,,,,,,,,,ADICION,1400.0,$
,,,,,,,,,,,PERDIDA DEL CREDITO FISCAL,,
,,,,,,,,,,,DEL IGV COMPRAS,,

Resumen numérico:
       Unnamed: 0  Unnamed: 1  Unnamed: 2  Unnamed: 3  Unnamed: 4  Unnamed: 5  Unnamed: 6  Unnamed: 7  Unnamed: 8  Unnamed: 9  Unnamed: 10  Unnamed: 12
count         0.0         0.0         0.0         0.0         0.0         0.0         0.0         0.0         0.0         0.0          0.0          1.0
mean          NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN       1400.0
std           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN          NaN
min           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN       1400.0
25%           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN       1400.0
50%           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN       1400.0
75%           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN       1400.0
max           NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN         NaN          NaN       1400.0
