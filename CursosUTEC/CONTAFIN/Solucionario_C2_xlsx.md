---
curso: CONTAFIN
titulo: Solucionario C2
slides: 0
fuente: Solucionario C2.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Solucionario C2.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Solucionario C2.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Caso 1
Filas: 16 · Columnas: 17
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (float64), Unnamed: 14 (object), Unnamed: 15 (object), Unnamed: 16 (object)

Muestra (primeras 16 de 16 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16
,EMPRESA,TIENDA TAMBO SAC,,,,,,,,,,,,,,
,PRODUCTO,yogurt Gloria 250 mililitros sabor fresa.,,,,,,MÉTODO PEPS,,,,,,Unidades,V.V.U,Valor total de venta
,Fecha,DETALLE,ENTRADA,,,SALIDA,,,SALDO,,,,,100,3,300
,,,UNID,C/U,TOTAL S/.,UNID,C/U,COSTO TOTAL S/.,UNID,C/U,COSTO TOTAL S/.,LOTE,,50,3,150
,2022-10-01 00:00:00,Stock inicial,,,,,,,100,1.80,180.00,1,,80,3,240
,2022-10-02 00:00:00,Compra,200,2.00,400.00,,,,200,2.00,400.00,2,,Venta bruta,,690
,2022-10-03 00:00:00,Venta,,,,100,1.80,180.00,0,1.80,0.00,1,,-5,3,-15
,2022-10-03 00:00:00,Venta,,,,50,2.00,100.00,150,2.00,300.00,2,,Venta Neta,,675
,2022-10-20 00:00:00,Compra,180,1.95,351.00,,,,180,1.95,351.00,3,,Costo de venta,,430
,2022-10-22 00:00:00,Dev. A provee,-10,1.95,-19.50,,,,170,1.95,331.50,3,,Resultado Bruto,,245
,2022-10-25 00:00:00,Venta,,,,80,2.00,160.00,70,2.00,140.00,2,,,,
,2022-10-30 00:00:00,Dev. De cliente,,,,-5,2.00,-10.00,75,2.00,150.00,2,,La empresa obtuvo una ganancia de S/245 soles,,
,2022-10-31 00:00:00,Compra,300,2.00,600.00,,,,300,2.00,600.00,4,,por la venta de 225 unidades de yogurt Gloria,,
,,,670,,1331.5,225,,430.00,75,2.00,150.00,2,,,,
,,,,,,,,,170,1.95,331.50,3,,,,
,,,,,,COSTO DE VENTAS,,,300,2.00,600.00,4,,,,

Resumen numérico:
       Unnamed: 0  Unnamed: 13
count         0.0          0.0
mean          NaN          NaN
std           NaN          NaN
min           NaN          NaN
25%           NaN          NaN
50%           NaN          NaN
75%           NaN          NaN
max           NaN          NaN

## Hoja: Caso 2
Filas: 46 · Columnas: 3
Columnas y tipos: ESTADO DE FLUJO DE EFECTIVO (object), Unnamed: 1 (float64), Unnamed: 2 (object)

Muestra (primeras 40 de 46 filas, formato CSV):
ESTADO DE FLUJO DE EFECTIVO,Unnamed: 1,Unnamed: 2
POR EL AÑO 2021,,
EMPRESA COOL BOX,,
,,
ACTIVIDADES DE OPERACIÓN,,
FUENTES : ENTRADAS,,
COBRO A CLIENTES,60000.0,
COBRO DE FACTURAS A CLIENTES,25000.0,
,85000.0,
USOS:SALIDAS,,
PAGO DE RECIBO (SEDAPAL),600.0,
PAGO DE IMPUESTOS,14800.0,
PAGO DE SALARIOS,46000.0,
COMPRA AL CONTADO DE MERCADERIAS,37000.0,
,98400.0,
,,
Aumento (Disminución) del Efectivo y Equivalente de Efectivo Provenientes de Actividades de Operación,-13400.0,DEFICIT
,,
ACTIVIDADES DE INVERSION,,
FUENTE: ENTRADAS,,
"COBRO POR LA VENTA DE PROPIEDA,PLANTA Y EQUIPO",11000.0,
COBRO CUOTA POR UN PRESTAMO A CLIENTE,5000.0,
COBRO POR VENTA DE VITRINA,1500.0,
VENTA DE ACCIONES,48000.0,
,65500.0,
USO: SALIDAS,,
COMPRA AL CONTADO DE COMPUTADORAS LENOVO,20000.0,
PRESTAMO A CLIENTE,12000.0,
,32000.0,
,,
Aumento (Disminución) del Efectivo y Equivalente de Efectivo Provenientes de Actividades de inversion,33500.0,SUPERAVIT
,,
ACTIVIDADES DE FINANCIAMIENTO,,
FUENTES: ENTRADAS,,
DINERO RECIBIDO DEL BANCO BCP,80000.0,
EMISION DE ACCIONES,45000.0,
,125000.0,
USOS: SALIDAS,,
PAGO DE DIVIDENDOS A LOS SOCIOS,31000.0,
,31000.0,
,,

Resumen numérico:
          Unnamed: 1
count      27.000000
mean    46374.074074
std     40184.914818
min    -13400.000000
25%     16400.000000
50%     33500.000000
75%     72750.000000
max    132100.000000

## Hoja: Caso 3
Filas: 27 · Columnas: 17
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object), Unnamed: 13 (object), Unnamed: 14 (object), Unnamed: 15 (object), Unnamed: 16 (object)

Muestra (primeras 27 de 27 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12,Unnamed: 13,Unnamed: 14,Unnamed: 15,Unnamed: 16
,TEMA: ESTADO DE CAMBIOS EN EL PATRIMONIO NETO,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,
,ALICORP S.A.C,Aportes de socios,LAS pueden/ comercializar,Mas aportes,Por una revaluacion de activos fijos,10% DE LA UTILIDAD POR LEY,,Ganancia o perdida de periodos anteriores,Ganancia o perdida por variacion del tipo de cambio,,,,,,,
,,,,,,,Facultativas,,,,,,,,,
,,,,,,,Estatutuarias,,,,Dato correcto.,,,,,
,PERIODO 2021,,,,,,,,,,,,,,,
, ,CAPITAL,ACCIONES DE INVERSION,CAPITAL ADICIONAL,RESULTADOS NO REALIZADOS,RESERVA LEGAL,OTRAS RESERVAS,RESULTADOS ACUMULADOS,DIFERENCIAS DE CONVERSION,TOTAL PATRIMONIO NETO,,,,,,
,,,,,,,,,,,,,,,,
,Saldos al 31.12.2020(Saldo inicial),1000000,,90000,,18000,5000,3200000,,4313000,S.I al 01.01.2020,,,,,
1.0,Distribucion de utilidades,,,,,,,-150000,,-150000,,,Comentario:,,,
2.0,Capitalizacion de utilidades no distribuidas ,30000,,,,,,-30000,,0,,,El patrimonio de Alicorp S.A.C aumento en 2170000 ,,,
3.0,Excedente de revaluacion(maquina),,,,20000,,,,,20000,,,y uno de los principales motivos de esto fue la utilidad ,,,
4.0,Utilidad obtenida en el ejercicio 2021,,,,,,,2000000,,2000000,,,obtenida en el ejercicio que es de 2000000.,,,
5.0,Detraer reserva legal del ejercicio 2021,,,,,188000,,-188000,,0,,,,,,
6.0,Otras reservas(reserva estatutuaria 1%),,,,,,20000,-20000,,0,,,,,,
7.0,Capital adicional de socios(reg.publicos),90000,,-90000,,,,,,0,,,,,,
8.0,Capital adicional de socios(no reg.publicos),,,300000,,,,,,300000,,,,,,
,Saldos de cuentas patrimoniales al 31.12.2021,1120000,0,300000,20000,206000,25000,4812000,0,6483000,S.F al 31.12.2020,,,,,
,,,,,,,,,,,,,,,,
,,,,,,,Result.acumul,5020000, ,,,,,,,
,,,,,,,reserva legal,502000,Ley de sociedades,,,,,,,
,,,,,,Verificar:,tope maximo 20% capital,206000,,,, , , , , 
,,,,,,,,,,,, , , , , 
,,,, ,,,Lo maximo para no llegar al tope ,188000,,,, , , , , 
,,,,,,,,,,,,,,,,
,,,,,,Observar que la reserva legal acumulada,,,,,,,,,,
,,,,,,"no puede exceder el limite de ley, ojo.",,,,,,,,,,

Resumen numérico:
       Unnamed: 0
count     8.00000
mean      4.50000
std       2.44949
min       1.00000
25%       2.75000
50%       4.50000
75%       6.25000
max       8.00000
