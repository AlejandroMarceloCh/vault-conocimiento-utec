---
curso: FUNDOPS
titulo: Casos de Balance de Línea - Solución (clase)
slides: 0
fuente: Casos de Balance de Línea - Solución (clase).xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Casos de Balance de Línea - Solución (clase).xlsx. -->

<!-- INTERPRETAR: datos tabulares de Casos de Balance de Línea - Solución (clase).xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Case 1 - Data
Filas: 7 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object)

Muestra (primeras 7 de 7 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,,,
,Recurso,Tiempo de Procesamiento (minutos),Número de Operarios
,1,10,2
,2,6,1
,3,16,3
,,,
,Salario =,10,$/hora

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

## Hoja: Case 1 - Solution
Filas: 24 · Columnas: 6
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Capacidad = 1/T. procesamiento (object)

Muestra (primeras 24 de 24 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Capacidad = 1/T. procesamiento
,,,,,
,Recurso,Tiempo de Procesamiento por Operario (minutos),Número de Operarios,Tiempo Promedio de Procesamiento (minutos/unidad) ,Capacidad (unidades/hora)
,1,10,2,5,12
,2,6,1,6,10
,3,16,3,5.333333333333333,11.25
,,,,,
,Salario =,10,$/hora,,
,# Unidades =,100,unidades,,
,Cadencia del sistema =,6,minutos/unidad,el proceso mas lento = Tiempo de ciclo,
,Capacidad del sistema =,10,unidades/hora,el proceso con menor capacidad,
,Tiempo 1a unidad =,32,minutos,,
,Tiempo 100 unid. =,626,minutos,Answer a,
,Tiempo Efectivo de M.O. =,32,minutos/unidad,Answer b,tiempo efectivo de mano de obra por cada unidad producida
,Tiempo ocioso1 =,2,minutos/unidad,,
,Tiempo ocioso2 =,0,minutos/unidad,,
,Tiempo ocioso3 =,2.000000000000001,minutos/unidad,,
,Tiempo ocioso total =,4.000000000000001,minutos/unidad,,
,Tiempo Total =,36,minutos/unidad,,
,%Utilización =,0.8888888888888888,,Answer c,
,Costo M.O. =,6,$/unidad,Answer d,
,,,,,
,,,,,
,,,,,
,,,,tiempo eefectivo es el tiempo que el operario esta trabajando por unidad,

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

## Hoja: Case 2 - Data
Filas: 8 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object)

Muestra (primeras 8 de 8 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,,,
,Tarea,Tiempo (segundos),Operario
,1,30,1
,2,25,2
,3,35,3
,4,40,
,5,15,4
,6,30,

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

## Hoja: Case 2 - Solution
Filas: 16 · Columnas: 7
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object), Unnamed: 6 (object)

Muestra (primeras 16 de 16 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
,,,,,,
,Tarea,Tiempo (segundos),Operario,Tiempo de Procesamiento (segundos),Tiempo de Procesamiento Óptimo (segundos),Operario
,1,30,1,30,55,1
,2,25,2,25,,
,3,35,3,75,35,2
,4,40,,,40,3
,5,15,4,45,45,4
,6,30,,,,
,Total =,175,,,,
,,,,,,
,Tiempo de Ciclo =,75,segundos,Answer a,,
,Capacidad =,48,unidades/hora,Answer b,,
,Tiempo de Ciclo Óptimo =,55,segundos,,,
,Capacidad Óptima =,65.45454545454545,unidades/hora,"Answer c, d",,
,,,,,,
,"con ritmo de cinta transpotadora, la velocidad es constante , no hay cola, antes de cualquier proceso, ya que todos trabajan a la misma velocidad",,,,,

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

## Hoja: Case 3 - Data
Filas: 14 · Columnas: 4
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object)

Muestra (primeras 14 de 14 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3
,Power Toys Inc.,,
,,,
,Estación,Tarea,Tiempo de Procesamiento (segundos)
,1,Acoplar batería,75
,2,Insertar receptor de control remoto,85
,3,Insertar chip,90
,4,Ensamblar eje delantero,65
,5,Ensamblar eje posterior,70
,6,Instalar motor eléctrico,55
,7,Conectar motor a batería,80
,8,Conectar el motor al eje trasero,65
,9,Montar cuerpo de plástico,80
,,,
,Salario =,15,$/hora

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

## Hoja: Case 3 - Solution
Filas: 33 · Columnas: 6
Columnas y tipos: Unnamed: 0 (float64), Unnamed: 1 (object), Unnamed: 2 (object), Unnamed: 3 (object), Unnamed: 4 (object), Unnamed: 5 (object)

Muestra (primeras 33 de 33 filas, formato CSV):
Unnamed: 0,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
,Power Toys Inc.,,,,
,,,,,
,Estación,Tarea,Tiempo de Procesamiento (segundos),Con Recorte de Personal,
,1,Acoplar batería,75,75,Answer g
,2,Insertar receptor de control remoto,85,85,
,3,Insertar chip,90,90,
,4,Ensamblar eje delantero,65,135,
,5,Ensamblar eje posterior,70,,
,6,Instalar motor eléctrico,55,135,
,7,Conectar motor a batería,80,,
,8,Conectar el motor al eje trasero,65,145,
,9,Montar cuerpo de plástico,80,,
,,Total =,665,,
,,,,,
,Salario =,15,$/hora,,
,Cuello de Botella =,Estación 3,,,
,Tiempo de Ciclo =,90,segundos/unidad,Answer a,
,Capacidad =,40,unidades/hora,Answer b,
,M.O. =,810,segundos/unidad,,
,Costo M.O. =,3.375,$/unidad,Answer c,
,Tiempo Celda =,665,segundos/unidad,,
,Tiempo Ocioso 2 =,5,segundos,,
,%Utilización 2 =,0.9444444444444444,,Answer d,(85/90)
,Costo M.O. Celda =,2.7708333333333335,$/unidad,Answer e,1 trabajador realiza todas las tareas / no hay tiempo ocioso
,%Utilización 2 =,0.5862068965517241,,Answer f,con la nueva distribución de tareas
,# Operarios =,6,operarios,T.ocioso =145-85,60
,Tiempo Promedio =,110.83333333333333,segundos,%Ut. = 85/(85+60),0.5862068965517241
,TCiclo Recorte =,145,segundos,,
,Capacidad con Recorte =,24.82758620689655,unidades/hora,Answer h,
,,,,,
,,,,,
,,$15-----1 hora (3600 seg),X= (15 * 665)/3600,,
,,X------665 seg,2.7708333333333335,,

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
