---
curso: BIGDATA
titulo: 03 - Semana 1/Semana 1 Laboratorio Caso Uber
slides: 5
fuente: 03 - Semana 1/Semana 1 Laboratorio Caso Uber.pdf
---

## Slide 1

Portada. Fondo cian con patrón hexagonal, logo UTEC (decorativo), lema "Reinventa el mundo" (decorativo) y foto del edificio UTEC (decorativa).

**CASO: UBER — ARQUITECTURA**

Mg. Aldo Lezama Benavides
Semana 1

## Slide 2

Título: **Caso: "Pricing dinámico en Uber"**

Texto (columna izquierda):

Uber nace como una solución para conectar pasajeros con conductores de forma eficiente. Con el crecimiento de la demanda, la empresa enfrentó un problema clave:

En horas pico (lluvia, conciertos, tráfico), la demanda superaba ampliamente la oferta de conductores. Esto generaba:

- Tiempos de espera largos
- Cancelaciones
- Mala experiencia de usuario

Para resolverlo, Uber implementa pricing dinámico (surge pricing), que ajusta precios en tiempo real para:

- Incentivar más conductores
- Regular la demanda
- Maximizar eficiencia del sistema

**Visual (derecha):** foto de una mano al volante de un auto (tablero Volkswagen visible) sosteniendo con la otra mano un smartphone con la app Uber abierta (logo "Uber" en pantalla). Ilustra el rol del conductor/usuario de la plataforma.

## Slide 3

Título: **Caso: "Pricing dinámico en Uber"**

Slide de tres columnas que contrasta los tres actores del sistema. Cada columna tiene una imagen arriba y bullets abajo.

**Columna 1 — Conductores** (ilustración de un conductor con gorra de taxi junto a un auto amarillo):
- Buscan maximizar ingresos
- Deciden cuándo conectarse

**Columna 2 — Pasajeros** (ilustración de un grupo de personas esperando en una parada bajo un cartel "TAXI", una levanta la mano, otra mira el celular, con maletas):
- Buscan rapidez y precio razonable
- Sensibles a precios altos

**Columna 3 — Plataforma Uber** (captura de la app Uber en un smartphone: cabecera "Uber", tarjetas "Pide un viaje" y "Pide comida", sección "Viajar de nuevo" con destinos guardados "Casa – Calle de Arturo Soria, 45" y "Trabajo – Paseo de la Castellana, 36"):
- Balancea oferta y demanda
- Optimiza experiencia + revenue

## Slide 4

Título: **Actividad**

Subtítulo: Traducir un problema de negocio en arquitectura Big Data.

Tres tarjetas de color (post-it) en fila:

**1. Entendimiento del negocio** (tarjeta azul):
- ¿Cuál es el principal problema en horas pico?
- ¿Por qué no basta con más conductores?
- ¿Qué pasa si no hay pricing dinámico?
- ¿Quiénes se ven afectados?

**2. Identificación de datos** (tarjeta naranja):
- ¿Qué datos genera un viaje?
- ¿Datos para entender demanda?
- ¿Datos de oferta?
- ¿Variables externas?
- ¿Otros datos?

**3. Tipos de datos** (tarjeta amarilla):
- Streaming
- Estructurados
- No Estructurados

## Slide 5

Título: **Caso: "Pricing dinámico en Uber"**

Continuación de la actividad, dos tarjetas de color en fila:

**4. Identificación de las Vs de Big Data** (tarjeta gris):
- Volumen
- Velocidad
- Variedad
- Veracidad
- Valor

**5. Arquitectura Big Data** (tarjeta celeste):
- Fuentes
- Ingestión
- Almacenamiento
- Procesamiento
- Consulta
- Visualización
