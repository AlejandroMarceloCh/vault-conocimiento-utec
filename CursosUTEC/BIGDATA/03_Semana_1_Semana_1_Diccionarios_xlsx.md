---
curso: BIGDATA
titulo: 03 - Semana 1/Semana 1 -Diccionarios
slides: 0
fuente: 03 - Semana 1/Semana 1 -Diccionarios.xlsx
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: 03 - Semana 1/Semana 1 -Diccionarios.xlsx. -->

<!-- INTERPRETAR: datos tabulares de Semana 1 -Diccionarios.xlsx. El capítulo debe ser una
     interpretación (qué contiene, estructura, qué enseña/para qué sirve), no el volcado. -->

## Hoja: Diccionario Revisiones Amazon
Filas: 10 · Columnas: 2
Columnas y tipos: Campo (object), Descripción (object)

Muestra (primeras 10 de 10 filas, formato CSV):
Campo,Descripción
overall,rating
verified,compra verificada
reviewTime,Fecha de la revisión
reviewerID,ID usuario
asin,producto
style,un diccionario de los metadatos del producto
reviewerName,Nombre del Usuario
reviewText,texto de la reseña
summary,resumen de la revisión
unixReviewTime,Fecha de la revisión formato unix

## Hoja: Diccionario Yellow Taxi
Filas: 20 · Columnas: 2
Columnas y tipos: Campo (object), Descripción (object)

Muestra (primeras 20 de 20 filas, formato CSV):
Campo,Descripción
VendorID,"Código que indica el proveedor del sistema TPEP que generó el registro (1=CMT, 2=Curb, 6=Myle, 7=Helix)."
tpep_pickup_datetime,Fecha y hora en que se inició el viaje (cuando se activó el taxímetro).
tpep_dropoff_datetime,Fecha y hora en que finalizó el viaje (cuando se desactivó el taxímetro).
passenger_count,Número de pasajeros en el vehículo.
trip_distance,Distancia recorrida del viaje en millas según el taxímetro.
RatecodeID,"Código de tarifa aplicada al final del viaje (1=Estándar, 2=JFK, 3=Newark, 4=Nassau/Westchester, 5=Tarifa negociada, 6=Viaje grupal, 99=Desconocido)."
store_and_fwd_flag,"Indica si el registro fue almacenado temporalmente antes de enviarse (Y=Sí, N=No)."
PULocationID,Zona TLC donde se inició el viaje.
DOLocationID,Zona TLC donde terminó el viaje.
payment_type,"Método de pago del pasajero (0=Flex Fare, 1=Tarjeta, 2=Efectivo, 3=Sin cargo, 4=Disputa, 5=Desconocido, 6=Viaje anulado)."
fare_amount,Tarifa base calculada por tiempo y distancia.
extra,Cargos adicionales y recargos misceláneos.
mta_tax,Impuesto MTA aplicado automáticamente según la tarifa.
tip_amount,Propina (solo registrada automáticamente para pagos con tarjeta).
tolls_amount,Total de peajes pagados durante el viaje.
improvement_surcharge,Recargo por mejora aplicado desde 2015.
total_amount,Monto total cobrado al pasajero (no incluye propinas en efectivo).
congestion_surcharge,Recargo por congestión del estado de Nueva York.
airport_fee,Tarifa adicional por recogidas en aeropuertos (JFK o LaGuardia).
cbd_congestion_fee,Cargo por zona de congestión (vigente desde 2025).
