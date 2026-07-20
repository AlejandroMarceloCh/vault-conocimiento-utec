---
curso: COSTOS
titulo: S5 CVU (solucionario)
slides: 0
fuente: S5 CVU (solucionario).xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: S5 CVU (solucionario).xlsx. -->

<!-- INTERPRETAR: datos tabulares de S5 CVU (solucionario).xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: PREG-1
Filas: 130 · Columnas: 12
Columnas y tipos: PUNTO DE EQUILIBRIO (object), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (float64)

Muestra (primeras 40 de 130 filas, formato CSV):
PUNTO DE EQUILIBRIO,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11
,,,,,,,,,,,
"Una fábrica de parquet compra la madera en aserraderos de la zona. Tiene una demanda prácticamente ilimitada pero ciertas limitaciones en la provisión de la materia prima, debido a que los aserraderos proveedores se encuentran dispersos, a distintas distancias de la fábrica, lo que ocasiona diferentes costos en concepto de fletes.",,,,,,,,,,,
Los aserraderos cercanos pueden proveer hasta,,,,,,,20000,pies cuadrados (p2.),,,
Aserraderos más alejados pueden proveer otros ,,,,,,,30000,p2,,,
"Los más distantes, tienen una capacidad de provisión de hasta otros ",,,,,,,,,30000,p2,
El costo del flete de los aserraderos cercanos es de,,,,,,,,0.05,por p2.,,
Traer la madera desde los de distancia intermedia cuesta,,,,,,,,0.85,por p2.,,
El costo del flete de los aserraderos más alejados es de ,,,,,,,,1.5,por p2.,,
El costo de un p2 puesto en origen es      $,,,,,,0.2,,,,,
Otros costos variables alcanzan a ,,,,,0.04,por p2.,,,,,
El precio de venta de un p2 es de ,,,,,2,,,,,,
Los costos fijos mensuales suman ,,,,,53000,,,,,,
,,,,,,,,,,,
Calcular el punto de equilibrio .,,,,,,,,,,,
,,,,,,,,,,,
SOLUCION,,,,,,,,,,,
,,,,,,,,,,,
Se trata de un caso de contribuciones marginales decrecientes por tramos sucesivos.,,,,,,,,,,,
Primer paso: Calcular las contribuciones marginales unitarias para cada tramo.,,,,,,,,,,,
,,,,,,,,,,,
,Tramos,,desde,,hasta,pv,cv,cm,,,
,1,,,,20000,2,0.29000000000000004,1.71,,,
,2,,+ de,20000,50000,2,1.09,0.9099999999999999,,,
,3,,+ de,50000,80000,2,1.74,0.26,,,
,,,,,,,,,,,
,,Costo fijo,,,53000,,,,,,
,,,,,,,,,,,
Q1 =,,53000,,=,30994.152046783627,INEXISTENTE (Fuera del tramo),,,,,
,,1.71,,,,,,,,,
,,,,,,,,,,,
Resultado máximo en Tramo 1,,,,,,,,,,,
20000,x,1.71,,-,53000,=,-18800,,,,
,,,,,,,,,,,
Cont. Marg. máxima del tramo 1,,,,,20000,x,1.71,=,34200,,
,,,,,,,,,,,
Punto de equilibriio del tramo 2,,,,,,,,,,,
Q2 =,,53000,,-,34200,+,20000,=,40659.34065934066,tramo  viable,
,,0.9099999999999999,,,,,,,,,
,,,,,,,,,,,
El punto de equilibrio válido se encuentra en el tramo 2.,,,,,,,,,,,

Resumen numérico:
       Unnamed: 11
count          1.0
mean        8500.0
std            NaN
min         8500.0
25%         8500.0
50%         8500.0
75%         8500.0
max         8500.0

## Hoja: PREG 2
Filas: 17 · Columnas: 3
Columnas y tipos: precio (object), 25000 (float64), Unnamed: 2 (float64)

Muestra (primeras 17 de 17 filas, formato CSV):
precio,25000,Unnamed: 2
costo variable auto,22000.0,
cvariable comisión,500.0,
,,22500.0
costos fijos,,
alquiler,50000.0,
servicios,60000.0,
publicidad,10000.0,
,,120000.0
,,
utilidad adicional,,55000.0
,,
a. ¿Cuantos automóviles debe vender EL FARO SAC para alcanzar el punto de equilibrio?,,
,48.0,
"b. ¿Cuántos automóviles debe vender para alcanzar la meta de utilidad de S/.55,000 ?",,
,70.0,
"c. ¿Cuantos automóviles debe vender EL FARO SAC para alcanzar el punto de equilibrio, si deciden eliminar personal de ventas por un costo de S/.20,000 y aumentar la comisión de S/.500 a S/.1,000? Es la mejor decisión como empresa?",,
,50.0,

Resumen numérico:
              25000     Unnamed: 2
count      8.000000       3.000000
mean   17833.500000   65833.333333
std    24319.274913   49644.570029
min       48.000000   22500.000000
25%       65.000000   38750.000000
50%     5250.000000   55000.000000
75%    29000.000000   87500.000000
max    60000.000000  120000.000000

## Hoja: PREG 3
Filas: 83 · Columnas: 13
Columnas y tipos: Unnamed: 0 (float64), pregunta 3 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (float64), Unnamed: 12 (object)

Muestra (primeras 40 de 83 filas, formato CSV):
Unnamed: 0,pregunta 3,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12
,,,,,,,,,,,,
,"Caramel S.A. es un distribuidor de golosinas y tiene la siguiente proyección para el año 2,011.",,,,,,,,,,,
,,,,,,,,,,,,
,Precio promedio de Venta,,,,4.3,por caja,,,,,,
,,Costos promedios variables,,,,Costos Fijos anuales,,,,,,
,Costo de golosinas,,,2.58,por caja,Venta,,155310,,,,
,Gasto de Ventas,,,0.129,por caja,Administrativos  ,,85524,,,,
,,,,,,,,,,,,
,,Volumen de Ventas esperadas: ,,,,185000,cajas,,,,,
,,Impuesto a la Renta,,,,0.3,,,,,,
,,,,,,,,,,,,
,Los fabricantes de golosinas han anunciado que incrementaran  sus precios en un,,,,,,,0.1,"por aumentos en los insumos, mano de obra y otros.",,,
,Caramel S.A. espera que los otros costos no varíen,,,,,,,,,,,
,a)     Determine el punto de equilibrio en unidades y soles ,,,,,,,,,,,
,b)    Si los fabricantes suben sus precios en ,,,,0.1,", Caramel S.A. cuanto deberá subir su precio para no variar su  Margen de Contribución",,,,,,
,c)     Si Caramel S.A. decide no aumentar su precio pese al aumento de los fabricantes.,,,,,,,,,,,
,    ¿Cuánto deberá aumentar sus ventas para lograr la misma utilidad neta que la proyectada.?,,,,,,,,,,,
,,,,,,,,,,,,
,SOLUCION,,,,,,,,,,,
,,,,,,,,,,,,
,,,,                 ESCENARIO I,,,                 ESCENARIO II,,,                 ESCENARIO III,,
,,,,,,,Incremento,,0.1,Incremento,,0.1
,,,,,,,Nuevo Precio de Venta,,4.558,Nueva unidades,,35806.45161290333
,ESTADO DE RESULTADOS,,,,,Costeo,,,Costeo,,,Costeo
,,,,,,Variable,,,Variable,,,Variable
,,,,,,S/.,,,S/.,,,S/.
,VENTAS,,,,,,,,,,,
,Precio de Venta,,,4.3,185000,795500,4.558,185000,843230,4.3,220806.45161290333,949467.7419354842
,TOTAL VENTAS,,,,,795500,,,843230,,,949467.7419354842
,COSTO VARIABLE PRODUCCION,,,,,,,,,,,
,MPD + MOD + CIF,,,2.58,185000,477300,2.8380000000000005,185000,525030.0000000001,2.8380000000000005,220806.45161290333,626648.7096774197
,Costo de Producción Variable,,,,,477300,,,525030.0000000001,,,626648.7096774197
,Gastos de Ventas (V),,,0.129,185000,23865,0.129,185000,23865,0.129,220806.45161290333,28484.03225806453
,MARGEN DE CONTRIBUCION,,,2.709,,294335,2.9670000000000005,,294334.9999999999,2.9670000000000005,,294334.99999999994
,MARGEN DE CONTRIBUCION %,,,,,0.37,,,0.3490566037735848,,,0.30999999999999983
,COSTOS Y GASTOS FIJOS,,,,,,,,,,,
,Costo de Producción,,,,,0,,,0,,,0
,Gastos de Administración,,,,,85524,,,85524,,,85524
,Gastos de Ventas,,,,,155310,,,155310,,,155310
,TOTAL COSTOS + GASTOS (F),,,,,240834,,,240834,,,240834

Resumen numérico:
       Unnamed: 0   Unnamed: 11
count         0.0  3.000000e+00
mean          NaN  2.208065e+05
std           NaN  3.564477e-11
min           NaN  2.208065e+05
25%           NaN  2.208065e+05
50%           NaN  2.208065e+05
75%           NaN  2.208065e+05
max           NaN  2.208065e+05

## Hoja: PREG 4
Filas: 53 · Columnas: 13
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object), Unnamed: 7 (object), Unnamed: 8 (object), Unnamed: 9 (object), Unnamed: 10 (object), Unnamed: 11 (object), Unnamed: 12 (object)

Muestra (primeras 40 de 53 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6,Unnamed: 7,Unnamed: 8,Unnamed: 9,Unnamed: 10,Unnamed: 11,Unnamed: 12
,,"Una empresa de servicios turísticos EL CAMPO SAC para el mes de Mayo 2011, genera un promedio de S/.",,,,,,,,,4000,
,por persona con su paquete turístico de siete días a la ciudad de Cuzco.,,,,,,,,,,,
,Los costos variables por personas fueron:,,,,,,,,,,,
,,Tarifa aérea,,,,S/.,800,,,,,
,,Hospedajes en hoteles,,,,,1400,,,,,
,,Alimentos,,,,,600,,,,,
,,Transporte terrestre,,,,,300,,,,,
,,Boletos para entrada a Machu Pichu,,,,,500,,,,,
,,TOTAL,,,,,3600,,,,,
,El costo fijo mensual fueron S/.,,,48000,,,,,,,,
,CALCULE,,,,,,,,,,,
,1,El numero de paquetes turísticos que deben venderse para alcanzar el punto de equilibrio.,,,,,,,,,,
,2,Calcule el ingreso necesario para obtener una utilidad operativa de S/.,,,,,,100000,después ,,,
,,de impuesto a la renta (Tasa de ,,,0.3,),,,,,,
,3,Si los costos fijos aumentan en S/. ,,,24000,¿Cuál es la disminución que debe alcanzarse en el ,,,,,,
,,Costo Variable por persona para mantener el punto de equilibrio que se calculo en la pregunta 1.,,,,,,,,,,
,,,,,,,,,,,,
,SOLUCION,,,,,,,,,,,
,,,,,,,,,,,,
,1,Calculo del numero de paquetes turísticos,,,,,,,,,,
,,Datos,,,,,,,,,,
,,Pvu =,4000,,Cvu =,3600,,CF =,48000,,,
,,,,,,,,,,,,
,,Pe =,CF,=,,48000,,=,120,paquetes turísticos,,
,,,Pv - Cv,,4000,-,3600,,,,,
,,,,,,,,,,,,
,2,Determinación del ingreso,,,,,,,,,,
,,1ro. Determinación de paquetes a vender para obtener la Utilidad Operativa,,,,,,,,,,
,,UAI =,Ventas - CF - Cvariable,,,,,,,,,
,,142857.14285714287,=,4000,x,Z,-,48000,-,3600,x,Z
,,142857.14285714287,+,48000,=,400,Z,,,,,
,,400,Z,=,190857.14285714287,,,,,,,
,,,Z,=,477.14285714285717,paquetes,,,,,,
,,,,,,,,,,,,
,,2do. Determinamos el ingreso para obtener UO de S/.,,,,,100000,,,,,
,,Ingreso necesario es =,,4000,x,477.14285714285717,=,1908571.4285714286,,,,
,,EGP,,,,,,,,,,
,,Ventas,,1908571.4285714286,,,,,,,,
,,Cvariable,,-1717714.285714286,,,,,,,,
,,MC,,190857.14285714272,,,,,,,,

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
