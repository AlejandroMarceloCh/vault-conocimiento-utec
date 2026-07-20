---
curso: POWERBI
titulo: 13 - Semana 11/Dataset - DAX
slides: 0
fuente: 13 - Semana 11/Dataset - DAX.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 13 - Semana 11/Dataset - DAX.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Dataset - DAX.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Ventas
Filas: 11 · Columnas: 6
Columnas y tipos: nroVenta (int64), Fecha (datetime64[ns]), IdProducto (object), Unidades (int64), Precio (int64), Costo (int64)

Muestra (primeras 11 de 11 filas, formato CSV):
nroVenta,Fecha,IdProducto,Unidades,Precio,Costo
100,2025-10-10,P001,2,30,15
100,2025-10-10,P003,1,20,14
101,2025-10-10,P003,2,20,13
101,2025-10-10,P004,1,30,15
101,2025-10-10,P001,1,30,16
102,2025-10-11,P003,3,20,16
103,2025-10-11,P004,3,30,22
103,2025-10-11,P002,1,10,6
104,2025-10-12,P001,2,30,22
105,2025-10-12,P004,2,30,21
105,2025-10-12,P002,3,10,5

Resumen numérico:
         nroVenta   Unidades     Precio      Costo
count   11.000000  11.000000  11.000000  11.000000
mean   102.272727   1.909091  23.636364  15.000000
std      1.848833   0.831209   8.090398   5.674504
min    100.000000   1.000000  10.000000   5.000000
25%    101.000000   1.000000  20.000000  13.500000
50%    102.000000   2.000000  30.000000  15.000000
75%    103.500000   2.500000  30.000000  18.500000
max    105.000000   3.000000  30.000000  22.000000

## Hoja: Productos
Filas: 5 · Columnas: 4
Columnas y tipos: IdProducto (object), Nombre (object), Categoria (object), Activo (bool)

Muestra (primeras 5 de 5 filas, formato CSV):
IdProducto,Nombre,Categoria,Activo
P001,Arroz,Abarrotes,True
P002,Azucar,Abarrotes,True
P003,Vino,Bebidas,False
P004,Agua,Bebidas,True
P005,Fideos,Abarrotes,False
