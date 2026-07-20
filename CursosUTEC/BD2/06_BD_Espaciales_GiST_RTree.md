---
curso: BD2
titulo: 06 BD Espaciales - GiST - RTree
slides: 67
fuente: 06 BD Espaciales - GiST - RTree.pdf
---

# 06 BD Espaciales - GiST - RTree

## Índice

- [Introducción](#introducción)
  - [Referencias](#referencias)
  - [Problema](#problema)
- [Conceptos](#conceptos)
  - [Datos Espaciales](#datos-espaciales)
  - [Datos Geoespaciales](#datos-geoespaciales)
  - [BD Espacial](#bd-espacial)
  - [GIS](#gis)
  - [Tipos de consulta espacial](#tipos-de-consulta-espacial)
  - [Distancias](#distancias)
- [Índices Espaciales GiST en PostgreSQL](#índices-espaciales-gist-en-postgresql)
  - [Índice espacial](#índice-espacial)
  - [GiST](#gist)
  - [Uso de GiST en PostgreSQL](#uso-de-gist-en-postgresql)
  - [PostGIS: Funciones de Análisis Espacial](#postgis-funciones-de-análisis-espacial)
  - [PostGIS: Creación y definición de geometrías](#postgis-creación-y-definición-de-geometrías)
  - [PostGIS: Medición y análisis](#postgis-medición-y-análisis)
  - [PostGIS: Relaciones espaciales](#postgis-relaciones-espaciales)
  - [Ejemplo: Creación de tabla e inserción de datos](#ejemplo-creación-de-tabla-e-inserción-de-datos)
  - [Ejemplo: Creación de índice](#ejemplo-creación-de-índice)
  - [Ejemplo: Consulta por rango (rectángulo geográfico)](#ejemplo-consulta-por-rango-rectángulo-geográfico)
  - [Ejemplo: Consulta por rango](#ejemplo-consulta-por-rango)
  - [Conclusiones](#conclusiones)
- [Índices Espaciales R-Tree](#índices-espaciales-r-tree)
  - [Introducción al R-Tree](#introducción-al-r-tree)
  - [Estructura del R-Tree](#estructura-del-r-tree)
  - [Construcción](#construcción)
  - [Búsqueda por Rango](#búsqueda-por-rango)
  - [Búsqueda KNN](#búsqueda-knn)
  - [MINDIST](#mindist)
  - [Inserción](#inserción)
  - [Ejercicio: Construcción con Split cuadrático](#ejercicio-construcción-con-split-cuadrático)
  - [Variantes de R-Tree](#variantes-de-r-tree)
- [Glosario](#glosario)

## Introducción

### Referencias

- Spatial SQL: A Practical Approach to Modern GIS Using SQL, Forrest et al.
- Spatial Databases With Application To Gis, Rigaux et al.

### Problema

Problema:
Dada una colección de
puntos geográficos, se
requiere consultar aquellos
puntos pertenecientes a una
región especifica.

**Figura:** A la derecha del texto, un mapa de Melbourne, Australia, con nombres de barrios visibles como Carlton, Fitzroy North y North Melbourne. El mapa está poblado con numerosos marcadores de ubicación (pins) de distintos colores: azul oscuro/negro, rojo y naranja, representando puntos geográficos en una base de datos. Un rectángulo rojo (bounding box) delimita un área específica alrededor de «University of Melbourne» y «Carlton», ilustrando una consulta espacial por rango: el objetivo es identificar los puntos (pins) que se encuentran dentro de ese rectángulo.

- Aplicación en servicios de movilidad
  - Empresas como Uber y Google Maps
    usan BD espaciales espaciales para:
    - Gestionar información
      georreferenciada (mapas y
      ubicación en tiempo real).
    - Identificar vehículos disponibles
      en las cercanías.
    - Calcular y proponer rutas más
      eficientes.
    - Implementar sistemas de
      geofencing para delimitar áreas
      de operación o restricción.

**Figura:** Dos imágenes a la izquierda del texto. **Imagen superior:** fragmento de mapa de una ciudad (Hayes Valley, San Francisco) con un círculo rojo dibujado sobre varias manzanas; dentro y alrededor del círculo aparecen varios iconos de autos azules y un pin de ubicación verde, ilustrando una búsqueda de proximidad o consulta de vehículos cercanos. **Imagen inferior:** ilustración de «Geofencing Marketing»; a la izquierda, una mano sostiene un smartphone que muestra la notificación «50% Off Coupon available today only! Nearby at Bone Clothes 454 22nd Ave.»; a la derecha, un mapa estilizado con un pin rojo y un área circular azul sombreada alrededor, representando un límite geográfico virtual (geofence) que activa la notificación al entrar el usuario.

- Ciudades Inteligentes, gestión de infraestructura, sensores IoT, y
  análisis de tráfico en tiempo real usando consultas espaciales
  eficientes.

Smart City Solutions - SuperMap

**Figura:** En el centro de la slide, captura de pantalla del «Kediri Geospatial Monitoring Dashboard» (viernes, 8 de octubre de 2021), en idioma indonesio. **Tarjetas de métricas superiores:** población (Femenino: 767, Masculino: 709, Total: 1.476); datos de criminalidad (7 acciones criminales reportadas vs. 5 casos resueltos). **Mapa central:** región de Kediri con numerosos pins naranjas superpuestos. **Gráficos estadísticos:** gráfico de barras de Educación con graduados por nivel (SD, SMP, SMA, PT) para 2019, 2020 y 2021; gráfico de barras horizontales de Crecimiento Empresarial por sectores (jasa, perdagangan, pertanian); gráfico de líneas inferior «Durasi Macet Tiap Hari (dalam Jam)» con duración de atascos en horas a lo largo de 20 días. **Datos ambientales y en vivo:** clima a 27°C con precipitación, humedad y viento; calidad del aire etiquetada «GOOD» con índice 40; ventana de cámara en vivo en la esquina inferior derecha mostrando una carretera de noche. Enlace inferior: «Smart City Solutions - SuperMap».

Gestión de cajas logísticas en 3D:
- Optimizar el uso del almacén, reduciendo huecos y maximizando capacidad.
- Evitar colisiones entre cajas y rutas de transporte.
- Localizar cajas cercanas a un punto de referencia, o todas las cajas en un área
  especifica.

**Figura:** Dos imágenes. **Izquierda:** fotografía realista de un almacén grande con techo alto, mostrando numerosas cajas de cartón de distintos tamaños apiladas en filas y montones sobre el piso de concreto. **Derecha:** visualización 3D generada por computadora de prismas rectangulares de colores (verde, azul, rojo, púrpura, etc.) empaquetados dentro de un sistema de coordenadas 3D con ejes etiquetados de 0 a 100; las cajas son semitransparentes y representan cómo se modelan computacionalmente los datos espaciales (bounding boxes) para resolver problemas de empaquetado y colisiones.

(slides 3–6)

## Conceptos

### Datos Espaciales

Datos Espaciales:
- Colección de datos que representan objetos con
  ubicación y forma en un espacio métrico (generalmente
  en 2D y 3D).
- Se diferencian de datos convencionales en que poseen
  geometría asociada: coordenadas, dimensiones,
  relaciones.
- Características fundamentales:
  - Posición: dónde está el objeto (coordenadas x, y, z)
  - Forma: cómo es su geometría (punto, línea,
    polígono)
  - Atributos: información descriptiva adicional
    (nombre, población, área)
  - Relaciones: cómo se relaciona con otros objetos
    (adyacencia, contención)

| Primitive | Feature | Representation |
| :--- | :--- | :--- |
| Points | Fotografía aérea satelital mostrando árboles o arbustos dispersos en un campo. | Recuadro blanco con varios puntos verdes pequeños dispersos. |
| Lines | Fotografía aérea satelital de un río serpenteante y carreteras circundantes. | Recuadro blanco con una línea azul ondulada continua. |
| Polygons | Fotografía aérea satelital mostrando un lago alargado. | Recuadro blanco con una forma irregular rellena en azul sólido que representa el área del lago. |

**Figura:** A la derecha del texto, tabla de tres columnas (Primitive, Feature, Representation) que ilustra cómo las características del mundo real se representan como primitivas geométricas: puntos (árboles dispersos → puntos verdes), líneas (río y carreteras → línea azul ondulada) y polígonos (lago → forma rellena azul).

Datos Espaciales:

Ejemplos:
Posiciones de robots en una fábrica,
Plano CAD de un hospital,
Modelo 3D de piezas mecánicas,
Modelo 3D de cajas en un almacén.

**Figura:** Dos imágenes ilustrativas. **Inferior izquierda:** imagen en escala de grises de componentes mecánicos renderizados en 3D (engranajes, tapas roscadas, conectores), representando el ejemplo de «Modelo 3D de piezas mecánicas». **Derecha:** plano arquitectónico CAD detallado de planta baja con líneas de cuadrícula, distribución de habitaciones y anotaciones técnicas; la leyenda inferior incluye textos como «UNIVERSIDAD DE GUAYAQUIL», «FACULTAD DE ARQUITECTURA Y DISEÑO» y «PLANTA BAJA»; una etiqueta azul en la esquina dice «A/3». Ilustra el ejemplo «Plano CAD de un hospital».

(slides 7–8)

### Datos Geoespaciales

Datos Geoespaciales:
- Subconjunto de los datos espaciales que
  están georreferenciados a la superficie
  terrestre. Usan sistemas de coordenadas
  geográficas (latitud/longitud) definidos en
  un elipsoide.
- Se puede manejar como geometry con SRID
  geográfico (4326) para consultas planas,
  o geography, que calcula distancias
  geodésicas sobre el elipsoide.

Ejemplo: Coordenadas con latitud y longitud.

| SRID | Sistema | Descripción |
| :--- | :--- | :--- |
| 4326 | WGS 84 | Latitud/longitud en grados. Ampliamente usado en GPS y en la web. |
| 3857 | Web Mercator | Proyección usada en Google Maps, OpenStreetMap. |
| 32718 | UTM zona 18S | Coordenadas en metros para el sur de Perú. |

**Figura:** A la derecha del texto, mapa mundial (interfaz Google Maps) con numerosos pins de colores (rojo, azul, naranja, púrpura) fuertemente agrupados en Norteamérica, Europa y partes de Asia y África, ilustrando datos georreferenciados globales. Debajo del mapa, tabla de tres SRID comunes.

(slide 9)

### BD Espacial

BD Espacial:
Es un sistema de gestión de bases de datos (SGBD)
que incorpora tipos de datos, funciones y
estructuras de indexación especializados para
almacenar, consultar y analizar información que
tiene una localización en el espacio.

Generalmente es una base de datos tradicional
(como PostgreSQL, Oracle o SQL Server) ampliada
para manejar geometrías (puntos, líneas, polígonos)
y operaciones espaciales como parte de su lenguaje
de consulta.

(slide 10)

### GIS

GIS (Geographic Information System):
- Es un ecosistema tecnológico que combina
  mapas y bases de datos para responder
  preguntas espaciales como "¿en dónde?",
  "¿qué tan lejos esta?", "¿qué hay en este
  lugar?".
- Para ello integra hardware, software, datos y
  procedimientos que permitan gestionar,
  modelar, analizar y visualizar información
  geoespacial.

Software GIS más comunes:
- QGIS (libre y de código abierto).
- ArcGIS (comercial).
- PostGIS (extensión espacial para PostgreSQL).

**Figura:** A la derecha, captura de pantalla de una interfaz de software GIS (probablemente ArcGIS Pro). **Área de mapa:** región costera de una ciudad con superposiciones de líneas de colores (rojo, verde, azul, rosa) representando rutas de tránsito o autobuses, y áreas sombreadas que representan densidad de población o zonas urbanas. **Panel izquierdo:** lista de capas titulada «Drawing Order» con capas como «Bus Routes», «Population» (gradiente de color de amarillo a rojo oscuro), «Urban Area» y «Topographic». Barra de herramientas superior estilo cinta con opciones de análisis, edición e imágenes.

(slide 11)

### Tipos de consulta espacial

#### Búsqueda por Intersección

Búsqueda por Intersección:
Encontrar los objetos $s \in S$ tales que su geometría intersecta con una geometría de
consulta $Q$:

$$R = \{ s \in S \mid s \cap Q \neq \emptyset \}$$

**Figura:** Diagrama comparando un estado INPUT con un estado OUTPUT, conectados por una flecha hacia la derecha. **Marco INPUT:** dentro de un borde rectangular, el conjunto $S$ consiste en dos cuadrados azul claro en la base con dos triángulos amarillos encima (uno erguido a la izquierda, otro invertido a la derecha). La consulta $Q$ es un círculo verde en la parte inferior que solapa la mitad inferior de los dos cuadrados azules. **Marco OUTPUT:** mismo borde rectangular; las formas de $S$ (cuadrados y triángulos) aparecen atenuadas en gris claro. El resultado $R$ se resalta: el semicírculo superior del círculo verde (la porción que intersectó con los dos cuadrados azules) aparece en verde sólido; la mitad inferior del círculo, que no intersecta con ninguna otra forma, está atenuada.

(slide 12)

#### Búsqueda por Rango

Búsqueda por Rango:
Retorna todos los objetos que se encuentran total o parcialmente dentro de una región
definida por Q (rectángulo, polígono, círculo).
Formalmente, dado un colección de objetos $S$ y una región de consulta $Q$, el resultado es:

$$R = \{ s \in S \mid s \subseteq Q \}$$

**Figura:** Dos mapas de ejemplo debajo del texto. **Mapa izquierdo (consulta rectangular):** mapa de un área urbana (Melbourne visible) con un rectángulo rojo dibujado sobre una porción específica; pins de colores (rojos y negros) dispersos por el mapa; los pins rojos están dentro del área rectangular de consulta y los negros fuera. **Mapa derecho (consulta circular):** mapa de un barrio (Hayes Valley, San Francisco, con «Painted Ladies» mencionado) con un círculo rojo definiendo la región de consulta; varios iconos azules y verdes (puntos de interés o vehículos), varios contenidos dentro del límite circular.

(slide 13)

#### Búsqueda de los k Vecinos Más Cercanos

Búsqueda de los k Vecinos Más Cercanos:
Para un punto de consulta $q$ y un conjunto $S$, el resultado es el subconjunto $R \subset S$ de
tamaño $k$ tal que:

$$\forall s \in R, \forall s' \in S \mid d(q, s) \leq d(q, s').$$

**Figura:** Mapa de una región costera (alrededor de Italia y Córcega) con puntos de interés, mayormente aeropuertos y ciudades. **Punto de consulta ($q$):** icono de un avión pequeño negro ubicado sobre el mar entre la península y una isla. **Conjunto de puntos ($S$):** puntos azules y estrellas rojas dispersos por el mapa. **Conjunto resultado ($R$):** cinco puntos específicos resaltados con estrellas rojas y conectados al icono del avión con líneas punteadas rojas, representando los $k$ vecinos más cercanos ($k=5$). **Ubicaciones marcadas como los 5 vecinos más cercanos (estrellas rojas):** Pisa / S. Giusto, Marina Di Campo, Grosseto Airport, Bastia-Poretta, Corte. **Otros puntos del conjunto $S$ más lejanos (puntos azules):** Sarzana / Luni, Massa Cinquale Airport, Lucca / Tassignano Airport, Firenze / Peretola, Ampugnano, Calvi - Sainte-Catherine, Ajaccio-Napoléon-Bonaparte, Propriano.

(slide 14)

### Distancias

Distancia Euclidiana:
Aplicable a geometrías planas. Dado los puntos $p =
(x_1, y_1)$, $q = (x_2, y_2)$, la Distancia Euclidiana se
calcula de la siguiente forma:

$$d_E(p, q) = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$

Distancia Geodésica:
Toma en cuenta la superficie curva de la Tierra.
Generalmente se aplica la fórmula de Haversine que
calcular la longitud del arco de gran círculo en un
elipsoide.

$$d_G = 2R \arcsin \left( \sqrt{\sin^2 \frac{\Delta \phi}{2} + \cos \phi_1 \cos \phi_2 \sin^2 \frac{\Delta \lambda}{2}} \right)$$

**Figura:** A la derecha del texto, mapa mundial centrado en el océano Pacífico que ilustra ambos conceptos. **Dos puntos:** un punto verde en Japón y un punto rojo en la costa oeste de Sudamérica (cerca de Perú). **Línea roja (recta):** conecta los dos puntos directamente a través del mapa, representando la distancia euclidiana medida en una proyección 2D plana. **Línea azul (curva):** arco curvo que se eleva a través del Pacífico norte, representando la distancia geodésica (trayectoria de gran círculo), la distancia real más corta siguiendo la curvatura de la Tierra.

(slide 15)

## Índices Espaciales GiST en PostgreSQL

### Índice espacial

- Un índice espacial es una estructura de datos que permite
  realizar consultas eficientes sobre datos espaciales (geográficos).
- Permite búsquedas como:
  - Puntos dentro de un área
  - Objetos que se intersectan
  - Encontrar los vecinos más cercanos.

**Figura:** Tres diagramas en la parte inferior izquierda y un diagrama R-Tree a la derecha. **Diagramas inferiores izquierdos (MBR):** tres marcos cuadrados que muestran el concepto de Minimum Bounding Rectangles (MBR); el primero muestra una estrella amarilla intersectada por tres líneas de colores (roja, azul, verde); el segundo y tercero muestran cómo estas formas irregulares (la estrella y las líneas) pueden encerrarse o representarse mediante rectángulos simples para simplificar los cálculos espaciales. **Visualización R-Tree (derecha):** **Plano espacial (arriba):** plano 2D con varios rectángulos pequeños etiquetados con letras minúsculas **d, e, f, g, h, i, j**, agrupados en tres cajas delimitadoras mayores etiquetadas con letras mayúsculas: **A (caja amarilla)** encierra **d, e** y **f**; **B (caja verde)** encierra **g** y **h**; **C (caja azul)** encierra **i** y **j**; las cajas de nivel superior se solapan parcialmente (A se solapa con B y C). **Estructura de árbol (abajo):** diagrama jerárquico; nodo raíz contiene entradas **A, B** y **C**; ramas descendientes: nodo **A** apunta a nodo hoja con **d, e, f**; nodo **B** apunta a nodo hoja con **g, h**; nodo **C** apunta a nodo hoja con **i, j**.

(slide 17)

### GiST

GiST (Generalized Search Tree) permite búsquedas por
rango, proximidad y otras operaciones complejas que
no son posibles con B-Tree.

Ideal para datos espaciales, búsquedas difusas y full-
text search.

Soporta estructuras como R-Tree, B-Tree, y más.

**Figura:** Tres cajas horizontales de color naranja claro, cada una con un icono y un punto descriptivo.

(slide 18)

### Uso de GiST en PostgreSQL

- Se usa R-Tree junto con PostGIS para trabajar con geometrías.
  - PostGIS extiende PostgreSQL con funciones espaciales.

- Instalación de PostGis en Docker

```bash
docker run --name postgis -p 5501:5432 -e
POSTGRES_PASSWORD=123456 -d postgis/postgis
```

- Instalación en Windows
  usando StackBuilder

https://postgis.net

**Figura:** capa media etiquetada «PostGIS»; capa inferior etiquetada «PostgreSQL». Debajo del diagrama, URL «https://postgis.net».

PostgreSQL: Documentation: GiST Index

(slide 19)

### PostGIS: Funciones de Análisis Espacial

| Categoría | Funciones |
| :--- | :--- |
| Constructoras | `ST_MakePoint`, `ST_MakeLine`, `ST_MakePolygon`, `ST_GeomFromText`, `ST_GeomFromGeoJSON` |
| Métricas | `ST_Area`, `ST_Length`, `ST_Perimeter`, `ST_Distance`, `ST_MaxDistance`, `ST_3DDistance` |
| Transformación | `ST_Transform`, `ST_Simplify`, `ST_Buffer`, `ST_Envelope`, `ST_ConvexHull`, `ST_Centroid` |
| Conjunto | `ST_Union`, `ST_Intersection`, `ST_Difference`, `ST_SymDifference` |
| Validación | `ST_IsValid`, `ST_IsValidReason`, `ST_MakeValid`, `ST_IsSimple`, `ST_IsEmpty` |

**Figura:** Tabla con dos columnas; la columna izquierda contiene el nombre de la categoría en recuadros azul oscuro con texto blanco (Constructoras, Métricas, Transformación, Conjunto, Validación); la columna derecha lista las funciones SQL correspondientes en recuadros azul claro con texto monoespaciado negro.

(slide 20)

### PostGIS: Creación y definición de geometrías

• `ST_MakePoint(x, y)`
   • Crea un punto a partir de coordenadas.

```sql
SELECT ST_MakePoint(-3.7038, 40.4168); -- Resultado: POINT(-3.7038 40.4168)
```

• `ST_SetSRID(geom, srid)`
   • Asigna el sistema de referencia espacial.

```sql
SELECT ST_SetSRID(ST_MakePoint(-3.7038, 40.4168), 4326);
```

• `ST_GeomFromText('WKT', srid)`
   • Crea geometrías a partir de una cadena en formato WKT (Well-Known Text).

```sql
SELECT ST_GeomFromText('POINT(-3.7038 40.4168)', 4326);
```

| Sistema | SRID | Descripción |
|---|---|---|
| WGS 84 | 4326 | Sistema más usado en GPS. Utiliza latitud y longitud. |
| NAD 83 | 4269 | Muy usado en Norteamérica. Similar a WGS 84 pero con ligeras diferencias. |
| ETRS 89 | 4258 | Sistema geodésico para Europa. |

**Figura:** El título «PostGis: Creación y definición de geometrías» aparece en la parte superior. Tres funciones PostGIS con viñetas y ejemplos SQL con resaltado de sintaxis (palabras clave en azul, valores numéricos en verde, cadenas en rojo). En la parte inferior, tabla de tres filas con sistemas de referencia espacial (WGS 84, NAD 83, ETRS 89) y sus SRIDs y descripciones.

(slide 21)

### PostGIS: Medición y análisis

• `ST_Distance(geom1, geom2)`
   • Calcula la distancia entre dos geometrías (en grados si están en 4326).

```sql
SELECT ST_Distance(
  ST_SetSRID(ST_MakePoint(-3.7038, 40.4168), 4326),
  ST_SetSRID(ST_MakePoint(-3.7039, 40.4170), 4326)
);
```

   • Si necesitas la distancia geodésica, puedes usar `geography` en vez de `geometry`:

```sql
SELECT ST_Distance(
  ST_SetSRID(ST_MakePoint(-3.7038, 40.4168), 4326)::geography,
  ST_SetSRID(ST_MakePoint(-3.7039, 40.4170), 4326)::geography
);
```

PosGis: ST_Distance

**Figura:** Slide con título «PostGis: Medición y análisis» en la parte superior. A la izquierda, ilustración comparativa sobre una superficie curva gris etiquetada «Cortical surface»: dos puntos conectados por una línea recta negra etiquetada «Euclidean distance» y por una línea púrpura que sigue la curvatura de la superficie etiquetada «Geodesic distance». A la derecha, el texto y los ejemplos SQL de `ST_Distance`. En la parte inferior, enlace «PosGis: ST_Distance».

• `ST_Area(geom)`
  • Devuelve el área de una región geométrica (en grados² o metros² según el tipo).

```sql
-- Área de un polígono (en grados)
SELECT ST_Area(ST_GeomFromText('POLYGON((0 0,0 1,1 1,1 0,0 0))', 4326));
```

```sql
-- Área en metros si se convierte a `geography`
SELECT ST_Area(ST_GeomFromText('POLYGON((0 0,0 1,1 1,1 0,0 0))', 4326)::geography);
```

**Figura:** El título «PostGis: Medición y análisis» aparece en la parte superior. Función `ST_Area(geom)` con descripción y dos bloques de código SQL (área en grados y área en metros con cast a `geography`). Comentarios en verde, palabras clave en azul.

(slides 22–23)

### PostGIS: Relaciones espaciales

• `ST_Within(geom1, geom2)`
  • ¿Está geom1 dentro de geom2?

```sql
SELECT ST_Within(
  ST_SetSRID(ST_MakePoint(1, 1), 4326),
  ST_GeomFromText('POLYGON((0 0,0 2,2 2,2 0,0 0))', 4326)
);
-- Resultado: true
```

• `ST_Contains(geom1, geom2)`
  • ¿geom1 contiene completamente a geom2?

```sql
SELECT ST_Contains(
  ST_GeomFromText('POLYGON((0 0,0 2,2 2,2 0,0 0))', 4326),
  ST_SetSRID(ST_MakePoint(1, 1), 4326)
);
-- Resultado: true
```

**Figura:** Slide con título «PostGis: Relaciones espaciales» en la parte superior. Dos funciones espaciales (`ST_Within` y `ST_Contains`) con descripciones en forma de pregunta y ejemplos SQL que verifican si un punto (1, 1) está dentro de un polígono cuadrado definido por (0,0) a (2,2), con resultado `true` en ambos casos.

• `ST_Intersects(geom1, geom2)`
  • ¿Las geometrías se cruzan o se tocan?

```sql
SELECT ST_Intersects(
  ST_GeomFromText('POLYGON((0 0, 0 3, 4 3, 4 0, 0 0))', 4326),
  ST_GeomFromText('POLYGON((2 1, 2 4, 6 4, 6 1, 2 1))', 4326)
);
-- Resultado: true
```

• `ST_Union(geom1, geom2)`
  • Une dos geometrías en una sola.

```sql
SELECT ST_Union(
  ST_GeomFromText('POLYGON((0 0,0 1,1 1,1 0,0 0))'),
  ST_GeomFromText('POLYGON((1 0,1 1,2 1,2 0,1 0))')
);
```

**Figura:** Slide con título «PostGis: Relaciones espaciales» en la parte superior. Dos funciones: `ST_Intersects` con ejemplo de dos polígonos que se solapan (resultado `true`) y `ST_Union` con ejemplo de dos cuadrados unitarios adyacentes.

(slides 24–25)

### Ejemplo: Creación de tabla e inserción de datos

```sql
-- Create the extension for PostGIS
CREATE EXTENSION postgis;

-- Create a table for restaurants with their names and locations
CREATE TABLE restaurantes (
  id SERIAL PRIMARY KEY,
  nombre TEXT,
  ubicacion GEOMETRY(Point, 4326)
);

-- Insert sample data into the restaurantes table
INSERT INTO restaurantes (nombre, ubicacion)
VALUES
('Restaurante El Marino', ST_SetSRID(ST_MakePoint(-3.7038, 40.4168), 4326)),
('La Parrilla', ST_SetSRID(ST_MakePoint(-3.7092, 40.4192), 4326)),
('Casa UTEC', ST_SetSRID(ST_MakePoint(-3.6934, 40.4115), 4326)),
('El Rincón Trujillano', ST_SetSRID(ST_MakePoint(-3.7001, 40.4160), 4326)),
('Sushi Bar', ST_SetSRID(ST_MakePoint(-3.6989, 40.4180), 4326));
```

**Figura:** Slide con título «Ejemplo: Creación de tabla e inserción de datos» en la parte superior. Bloque de código SQL con tres secciones: creación de la extensión PostGIS, definición de la tabla `restaurantes` con columna `ubicacion` de tipo `GEOMETRY(Point, 4326)`, e inserción de cinco restaurantes con coordenadas en Madrid. Resaltado de sintaxis: palabras clave en azul, nombres de tabla/columna en marrón, cadenas en rojo, comentarios en verde.

(slide 26)

### Ejemplo: Creación de índice

```sql
-- Create a GIST index on the location column for efficient spatial queries
CREATE INDEX idx_restaurantes_gist
ON restaurantes
USING GIST (ubicacion);
```

Esto permite acelerar los siguientes métodos de búsqueda:

• `ST_DWithin`
• `ST_Contains`
• `ST_Intersects`
• `&&` (intersección de bounding boxes)

```sql
-- Filtro basado en MBR: ultra-rápido
SELECT id FROM lugares
WHERE geom && ST_MakeEnvelope(
  -77.15, -12.15, -76.95, -11.95, 4326);

-- Primero usa && para filtrar,
-- luego comprueba la interseccion real
SELECT id FROM lugares
WHERE ST_Intersects(geom,
  ST_MakeEnvelope(-77.15, -12.15,
                  -76.95, -11.95, 4326));
```

**Figura:** Slide con título «Ejemplo: Creación de índice» en la parte superior. A la izquierda, código SQL para crear un índice GiST sobre la columna `ubicacion` de la tabla `restaurantes`, seguido de una lista de cuatro métodos de búsqueda que se aceleran. A la derecha, bloque de código con fondo oscuro que muestra dos consultas de ejemplo sobre la tabla `lugares`: una usando el operador `&&` con `ST_MakeEnvelope` (filtro MBR ultra-rápido) y otra usando `ST_Intersects` (primero filtra con `&&`, luego comprueba la intersección real).

(slide 27)

### Ejemplo: Consulta por rango (rectángulo geográfico)

```sql
-- Search for restaurants within a bounding box
SELECT nombre,
    ST_Y(ubicacion::geometry) as latitud,
    ST_X(ubicacion::geometry) as longitud
FROM restaurantes
WHERE ubicacion && ST_MakeEnvelope(
    -3.70, 40.41,   -- Esquina inferior izquierda
    -3.69, 40.42,   -- Esquina superior derecha
    4326
);
```

| nombre (text) | latitud (double precision) | longitud (double precision) |
|---|---|---|
| Casa UTEC | 40.4115 | -3.6934 |
| Sushi Bar | 40.418 | -3.6989 |

**Figura:** Slide con título «Ejemplo: Consulta por rango (rectángulo geográfico)» en la parte superior. Bloque de código SQL que busca restaurantes dentro de un bounding box definido con `ST_MakeEnvelope` (esquina inferior izquierda: -3.70, 40.41; esquina superior derecha: -3.69, 40.42; SRID 4326), extrayendo latitud con `ST_Y` y longitud con `ST_X`. Debajo, captura de pantalla de interfaz «Data Output» (tipo pgAdmin) con tabla de resultados de dos filas: «Casa UTEC» (latitud 40.4115, longitud -3.6934) y «Sushi Bar» (latitud 40.418, longitud -3.6989).

(slide 28)

### Ejemplo: Consulta por rango

```sql
-- Search for restaurants within 800 meters of a given point
WITH punto_referencia AS (
    SELECT ST_SetSRID(ST_MakePoint(-3.7038, 40.4123), 4326)::geography AS punto
)
SELECT nombre,
       ST_Distance(ubicacion::geography, punto) as distancia_metros
FROM restaurantes, punto_referencia
WHERE ST_DWithin(
    ubicacion::geography, punto, 800
)
ORDER BY distancia_metros;
```

| # | nombre (text) | distancia_metros (double precision) |
|---|---|---|
| 1 | Restaurante El Marino | 499.69174257 |
| 2 | El Rincón Trujillano | 517.13173189 |
| 3 | Sushi Bar | 757.34867531 |

**Figura:** Slide con título «Ejemplo: Consulta por rango» en la parte superior. Bloque de código SQL con CTE `punto_referencia` que define un punto de referencia (-3.7038, 40.4123) cast a `geography`, consulta con `ST_Distance` y filtro `ST_DWithin` de 800 metros, ordenado por distancia. Debajo, captura de pantalla de «Data Output» con tres resultados: Restaurante El Marino (499.69 m), El Rincón Trujillano (517.13 m) y Sushi Bar (757.35 m).

(slide 29)

### Conclusiones

• R-Tree es esencial para trabajar con datos espaciales
• La combinación de GiST + PostGIS convierte a PostgreSQL en una potente base de datos espacial, capaz de competir con soluciones comerciales como Oracle Spatial o ArcGIS Enterprise.
• Los índices espaciales basados en GiST ofrecen un rendimiento altamente eficiente para consultas como:
   • Intersección de geometrías.
   • Búsqueda de vecinos cercanos (KNN).
   • Contención o solapamiento de regiones.

**Figura:** Título «Conclusiones» en la parte superior. Tres viñetas principales con sub-viñetas en la tercera.

(slide 30)

## Índices Espaciales R-Tree

### Introducción al R-Tree

• El R-Tree es un índice espacial jerárquico que organiza objetos geométricos (puntos, líneas, polígonos) mediante rectángulos mínimos (MBR) para facilitar búsquedas espaciales eficientes.
    • Cada rectángulo representa un nodo o entrada en el árbol.
    • Los nodos internos agrupan elementos espacialmente cercanos para mejorar la eficiencia de búsqueda.

Es ampliamente utilizado en Sistemas de Información Geográfica (GIS), motores de bases de datos como PostgreSQL (con PostGIS), Oracle Spatial, etc.

A. Guttman. R-trees: A dynamic index structure for spatial searching. In Proc. ACM International Conference on Management of Data (SIGMOD'84), pages 47—57. ACM Press, 1984

**Figura:** Slide con título «Índice Espacial: R-Tree» en la parte superior. A la izquierda, dos diagramas ilustrando MBRs:
- **Diagrama izquierdo:** objetos espaciales irregulares (polígonos sombreados en gris) cada uno encerrado en un rectángulo azul (MBR individual); un rectángulo rojo más grande agrupa varios rectángulos azules.
- **Diagrama derecho (vista jerárquica):** un rectángulo rojo grande contiene varios rectángulos azules más pequeños; dentro de los rectángulos azules hay puntos negros representando datos puntuales.

A la derecha, caja verde con texto sobre uso en GIS y motores de bases de datos. En la parte inferior, cita bibliográfica de A. Guttman (SIGMOD'84).

(slide 33)

### Estructura del R-Tree

• Es un árbol balanceado similar a un B-Tree.
• Garantiza que puntos cercanos se almacenen en lo posible en la misma página de datos o subárbol.
• Regiones de páginas jerárquicamente organizadas siempre deben estar contenidas completamente en la región de su padre.
• Estructura dinámica: operaciones de inserción y borrado eficientes $O(\log n)$
• Permite buscar objetos espaciales en una área determinada.

**Figura:** Slide con título «Índice Espacial: R-Tree» en la parte superior izquierda y cinco viñetas de características del R-Tree. A la derecha, dos diagramas complementarios:

**Diagrama superior (representación espacial):** espacio 2D con rectángulos anidados representando MBRs.
- **Nivel raíz:** dos rectángulos discontinuos azules grandes etiquetados **R1** y **R2** cubren todo el espacio de datos.
- **Nivel intermedio:** dentro de R1, tres rectángulos discontinuos azules etiquetados **R3**, **R4** y **R5**; dentro de R2, dos etiquetados **R6** y **R7**.
- **Nivel hoja/datos:** dentro de los rectángulos intermedios, rectángulos sólidos rojos:
  - **R3** contiene R8, R9 y R10.
  - **R4** contiene R11 y R12.
  - **R5** contiene R13 y R14.
  - **R6** contiene R15 y R16.
  - **R7** contiene R17, R18 y R19.

**Diagrama inferior (jerarquía del árbol):**
- **Nodo raíz:** contiene entradas **R1** y **R2**.
- **Primer nivel (hijos de la raíz):**
  - Un nodo con punteros a **R3**, **R4** y **R5** (vinculado desde R1).
  - Un nodo con punteros a **R6** y **R7** (vinculado desde R2).
- **Nivel hoja:**
  - **R3** apunta a hojas **R8**, **R9**, **R10**.
  - **R4** apunta a hojas **R11**, **R12**.
  - **R5** apunta a hojas **R13**, **R14**.
  - **R6** apunta a hojas **R15**, **R16**.
  - **R7** apunta a hojas **R17**, **R18**, **R19**.

• Las hojas del R-tree poseen registros de la forma

$$(P, \text{identificador\_tupla})$$

o En donde, P es un punto n-dimensional

$$P=\{p_0, p_1, p_2, \ldots, p_n\}$$

• $n$: número de dimensiones
• Describe extensión del objeto a lo largo de la dimensión.

• Los nodos internos del R-tree contienen entradas de la forma

$$(R, \text{puntero\_hijo})$$

○ R cubre todos los rectángulos del nodo hijo, $R=\{L,U\}$

• Restricciones del nodo:
  ○ M: máximo número de entradas en un nodo
  ○ m: mínimo número de entradas en un nodo, generalmente $m = M/2$

**Figura:** Slide con título «Índice Espacial: R-Tree» en la parte superior. Texto con viñetas describiendo el formato de registros en nodos hoja $(P, \text{identificador\_tupla})$ con $P=\{p_0, p_1, p_2, \ldots, p_n\}$, formato de nodos internos $(R, \text{puntero\_hijo})$ con $R=\{L,U\}$, y restricciones del nodo (M máximo, m mínimo, generalmente $m = M/2$).

(slides 34–35)

### Construcción

Podemos visualizar las ubicaciones de interés simplemente como puntos en el espacio ...

**Figura:** Slide con título «R-Tree: construcción» en la parte superior izquierda. A la izquierda, sistema de coordenadas 2D con ejes X (horizontal) e Y (vertical), poblado con numerosos puntos negros pequeños (cuadrados) distribuidos en aproximadamente seis grupos o clusters: superior izquierdo, inferior izquierdo, centro superior, centro inferior, superior derecho e inferior derecho. A la derecha, texto «Podemos visualizar las ubicaciones de interés simplemente como puntos en el espacio ...».

(slide 36)

• Agrupamos los puntos en MBRs
• Cada MBR se puede representar con solo dos puntos $\{L, U\}$: la esquina inferior izquierda y la esquina superior derecha.
• Podemos agrupar recursivamente en MBRs más grandes.

MBR: Minimum Bounding Rectangle

**Figura:** Slide con título «R-Tree: construcción» en la parte superior izquierda. A la izquierda, plano cartesiano 2D con puntos negros agrupados en nueve rectángulos etiquetados en azul claro **R1** a **R9**:
- **R1, R2, R3:** tres rectángulos pequeños apilados verticalmente en el lado izquierdo.
- **R7, R8:** dos rectángulos en la parte inferior izquierda que se solapan parcialmente.
- **R5:** rectángulo alto y delgado en el centro.
- **R4:** rectángulo horizontal ancho en la parte superior derecha, solapándose parcialmente con la parte superior de R5.
- **R6:** rectángulo pequeño debajo de R4 y a la derecha de R5.
- **R9:** rectángulo pequeño en la esquina inferior derecha.

A la derecha, tres viñetas explicativas y la definición del acrónimo MBR.

(slide 37)

**Figura:** Slide con título «R-Tree: construcción» en la parte superior izquierda. La slide se divide en dos partes:

**Parte izquierda (representación espacial):** puntos negros organizados en una jerarquía de MBRs:
- **MBRs de nivel hoja (etiquetas azules R1–R9):** los rectángulos más pequeños que contienen directamente los puntos.
  - **R1, R2, R3:** en el área superior izquierda.
  - **R4, R5, R6:** en el área superior derecha (R4 y R5 se solapan parcialmente).
  - **R7, R8, R9:** a lo largo de la parte inferior (R7 y R8 se solapan parcialmente).
- **MBRs de nivel superior (etiquetas negras R10–R12, contorno naranja):**
  - **R10:** contiene R1, R2 y R3.
  - **R11:** contiene R4, R5 y R6.
  - **R12:** contiene R7, R8 y R9.

**Parte derecha (estructura de árbol):**
- **Nodo raíz:** contiene las entradas **R10**, **R11** y **R12**.
- **Nodos internos (nivel 1):**
  - Flecha desde **R10** apunta a un nodo con **R1**, **R2** y **R3**.
  - Flecha desde **R11** apunta a un nodo con **R4**, **R5** y **R6**.
  - Flecha desde **R12** apunta a un nodo con **R7**, **R8** y **R9**.
- **Nodos hoja:** nueve casillas cuadradas vacías en la parte inferior, cada una apuntada por una de las entradas R1 a R9, representando punteros a los objetos de datos espaciales (los puntos).

(slide 38)

En los nodos hoja tenemos la ubicación espacial de los datos y un puntero al registro físico.

**Figura:** Slide con título «R-Tree: construcción» en la parte superior izquierda. A la izquierda, el texto sobre nodos hoja. A la derecha, diagrama de árbol con tres niveles:

**Nivel raíz (R10):**
- Una caja en la parte superior etiquetada **R10** con coordenadas **{(1,0),(7,9)}**, representando el bounding box global.

**Nivel intermedio (R1, R2, R3):**
- Una caja horizontal larga conectada a R10 por una flecha, dividida en tres secciones:
  - **R1:** {(1,3),(5,4)}
  - **R2:** {(2,0),(7,9)}
  - **R3:** {(1,1),(7,8)}

**Nivel hoja (nodos de datos):**
- Tres cajas verticales conectadas a R1, R2 y R3 respectivamente, conteniendo puntos (coordenadas) y punteros a registros físicos (enteros):
  - **Bajo R1:** (3,4)→77, (1,3)→88, (2,3)→22, (5,4)→13
  - **Bajo R2:** (2,2)→47, (3,0)→86, (7,9)→52
  - **Bajo R3:** (5,1)→32, (1,4)→45, (5,6)→27, (7,8)→73

(slide 39)

### Búsqueda por Rango

**Figura:** Slide con título «R-Tree: Búsqueda por Rango» en la parte superior izquierda. La slide se divide en dos partes:

**Parte izquierda (representación espacial):** plano 2D con objetos rectangulares etiquetados **A**, **B**, **C**, **D**, **E**, **F**, **G**, **H** y **J**, y sus MBRs:
- **P5** (contorno azul): MBR grande a la izquierda que contiene los objetos A, B, C, D y E.
  - **P1** (contorno amarillo): contiene A, B y C.
  - **P2** (contorno amarillo): contiene B, D y E (P1 y P2 se solapan).
- **P6** (contorno azul): MBR grande a la derecha que contiene los objetos F, G, H y J.
  - **P3** (contorno amarillo): contiene F y G.
  - **P4** (contorno amarillo): contiene G, H y J.

**Consulta de búsqueda:** un pequeño rectángulo sombreado en rojo colocado sobre el objeto **G**, representando la ventana o rango de búsqueda.

**Parte derecha (estructura de árbol):**
- **Nodo raíz:** contiene dos entradas: **[P5 | P6]**.
  - Una **flecha roja** apunta a **P6**, indicando que el rango de búsqueda intersecta el MBR de P6.
  - Una **X roja** sobre la rama que lleva a **P5**, indicando que esa sub-rama se **poda** porque el rango no intersecta P5.
- **Nivel intermedio:**
  - Bajo P5 (podada): nodo **[P1 | P2]**.
  - Bajo P6 (recorrida): nodo **[P3 | P4]**.
- **Nodos hoja:**
  - Desde P1: **[A | B | C | ]**
  - Desde P2: **[D | E | | ]**
  - Desde P3: **[F | G | | ]** — la **G** aparece resaltada en rojo, indicando que es un resultado dentro del rango de búsqueda.
  - Desde P4: **[H | J | | ]**

(slide 40)

**Figura:** La slide se divide en dos partes: a la izquierda, una representación espacial en 2D; a la derecha, el árbol R-Tree correspondiente.

**Parte izquierda (espacial):** Diez objetos espaciales representados como rectángulos pequeños etiquetados **A** a **J**. Cuatro MBR de nivel hoja (cian), etiquetados **P1**, **P2**, **P3** y **P4**:
- **P1:** contiene los objetos **A**, **B** y **C**.
- **P2:** contiene los objetos **D** y **E** (con solapamiento parcial con B).
- **P3:** contiene los objetos **F** y **G**.
- **P4:** contiene los objetos **H** y **J** (con solapamiento parcial con G).

Dos MBR de nivel superior:
- **P5** (contorno amarillo): contiene **P1** y **P2**.
- **P6** (contorno cian): contiene **P3** y **P4**.

Una consulta **Q** se representa como un círculo translúcido rojo pequeño, ubicado en la esquina inferior derecha del área de P5, solapándose específicamente con el objeto **E** dentro del MBR de P2.

**Parte derecha (árbol):**
- **Nodo raíz:** contiene dos entradas: **P5** y **P6**.
  - Una **flecha naranja** apunta a **P5**, indicando que la búsqueda comienza por esa rama.
  - Una **X roja** sobre la línea que lleva a **P6**, indicando que esa rama se **poda** porque Q no intersecta el MBR de P6.
- **Nivel interno (bajo P5):** nodo con **P1** y **P2**.
  - **X roja** sobre la línea que lleva a **P1** (podada: Q no intersecta P1).
  - Se sigue la línea hacia **P2** (Q intersecta el MBR de P2).
- **Nodos hoja:**
  - **P1** → **A, B, C**
  - **P2** → **D, E** — la **E** aparece resaltada en rojo como resultado de la búsqueda (intersecta con el círculo de consulta Q).
  - **P3** → **F, G**
  - **P4** → **H, J**

(slide 41)

¿MBR intersects with Query Region?

$R=\{L, U\}$

**Figura:** Tres diagramas que ilustran distintas formas en que un círculo de consulta puede intersectar un MBR rectangular (contorno azul):
- **MBR:** definido por $R=\{L, U\}$, donde **$L$** (punto azul) marca la esquina inferior izquierda y **$U$** (punto naranja) marca la esquina superior derecha.
- **Región de consulta (círculo):** círculo rojo claro con centro **$Q$** y **radio** indicado por un segmento horizontal azul.
- **Diagrama izquierdo:** el círculo intersecta el **borde vertical izquierdo** del rectángulo; flecha verde de doble punta muestra la distancia mínima de $Q$ al borde.
- **Diagrama central:** el círculo intersecta el **borde horizontal inferior** del rectángulo; flecha verde muestra la distancia mínima de $Q$ a ese borde.
- **Diagrama derecho:** el círculo intersecta la **esquina inferior izquierda ($L$)** del rectángulo; flecha verde muestra la distancia mínima de $Q$ a la esquina $L$.

Condición de intersección (texto en verde en la parte inferior):

$$\text{MINDIST}(Q, \text{MBR}) \leq \text{radio}$$

(slide 42)

```text
function RangeSearch(node, queryRegion, resultList):
  if node is a leaf:
     for each entry in node:
       if entry is within queryRegion:
          add entry to resultList
  else:
     for each childNode in node:
       if childNode's MBR intersects queryRegion:
          RangeSearch(childNode, queryRegion, resultList)
```

Condición de filtro:
- `MINDIST(Q, MBR) <= r` (resaltado en amarillo — corresponde a la verificación de intersección del MBR del nodo hijo con la región de consulta)
- `ED(Q, P) <= r` (resaltado en cian — corresponde a la verificación de que una entrada/punto está dentro de la región de consulta)

**Figura:** A la derecha del pseudocódigo, dos diagramas:

**Diagrama de árbol (arriba):**
- **Raíz** en la parte superior.
- Dos nodos internos hijos: **$p_1$** y **$p_2$** (cajas azules).
- Bajo $p_1$: tres nodos hoja **$p_{11}$**, **$p_{12}$**, **$p_{13}$** (cajas rosadas).
- Bajo $p_2$: tres nodos hoja **$p_{21}$**, **$p_{22}$**, **$p_{23}$** (cajas rosadas).

**Diagrama espacial (abajo):**
- Caja exterior grande que representa todo el espacio.
- Rectángulos **azules** para los MBR de los nodos internos $p_1$ y $p_2$ (parcialmente solapados).
- Rectángulos **rosados** para los MBR de los nodos hoja: $p_{11}$, $p_{12}$, $p_{13}$ dentro del área de $p_1$ (inferior derecha); $p_{21}$, $p_{22}$, $p_{23}$ dentro del área de $p_2$ (superior izquierda).
- **Región de consulta:** círculo **amarillo** con punto central rojo etiquetado **$q$**.
  - El círculo $q$ intersecta los rectángulos azules de $p_1$ y $p_2$.
  - Intersecta específicamente los MBR hoja $p_{22}$ y $p_{11}$.
  - No intersecta $p_{21}$, $p_{23}$, $p_{13}$ ni $p_{12}$.

(slide 43)

### Búsqueda KNN

- Para aplicar la búsqueda de los K vecinos más cercanos (KNN) en un R-Tree, se utiliza una lógica similar a la búsqueda por rango, pero con un radio dinámico que se ajusta a medida que se encuentran vecinos más cercanos.
- El algoritmo explora los nodos ordenados por distancia mínima (MINDIST) y va actualizando el conjunto de los K vecinos más cercanos, reduciendo el radio de búsqueda para descartar ramas que no puedan contener mejores candidatos.

**Figura:** A la izquierda, un gráfico 2D con ejes X e Y titulado **2-NN** (búsqueda de los 2 vecinos más cercanos):
- **Punto de consulta $q$:** punto rojo etiquetado **$q(12,6)$** en la parte inferior central del gráfico.
- **Círculo de búsqueda:** círculo rojo centrado en $q$, representando el radio de búsqueda actual.
- Dos flechas rojas desde $q$ hacia los dos puntos más cercanos: **$p_5$** y **$p_9$** (candidatos 2-NN).
- El espacio se divide en MBR anidados etiquetados **N1** a **N7**:
  - **N7** (rectángulo grande a la izquierda) contiene:
    - **N4:** puntos $p_6$ y $p_1$.
    - **N6:** puntos $p_2$ y $p_5$ ($p_5$ es uno de los 2 vecinos más cercanos).
    - **N2:** punto $p_4$.
  - **N1** (rectángulo grande a la derecha) contiene:
    - **N3:** puntos $p_7$ y $p_8$.
    - **N5:** puntos $p_3$ y $p_9$ ($p_9$ es el otro vecino más cercano).
- $p_5$ queda a la izquierda y ligeramente debajo de $q$; $p_9$ a la derecha y ligeramente arriba de $q$.

(slide 44)

Búsqueda 1NN

**Figura:** La slide se divide en dos partes: representación espacial a la izquierda y jerarquía del R-Tree a la derecha.

**Parte izquierda (espacial):** Plano cartesiano 2D con puntos agrupados en MBR anidados.
- **Rectángulos de nivel superior (naranja):** **R10**, **R11** y **R12**.
  - **R10** (cuadrante superior izquierdo): contiene tres rectángulos azules **R1**, **R2** y **R3**, cada uno con un grupo de puntos negros (5 puntos cada uno).
  - **R11** (cuadrante superior derecho): contiene dos rectángulos azules **R4** y **R5** (6 y 7 puntos respectivamente). Un **punto rojo etiquetado «q»** se ubica dentro de los límites de R11 pero fuera de R4 y R5, cerca de **R5**.
  - **R12** (rectángulo ancho en la parte inferior): contiene tres rectángulos azules **R6**, **R7** y **R8** (entre 5 y 6 puntos cada uno).
- **Rectángulos de nivel hoja (azul):** **R1** a **R8**, que encierran directamente los puntos de datos (puntos negros).

**Parte derecha (árbol):**
- **Nodo raíz:** contiene las entradas **R10**, **R11** y **R12** (en naranja).
- **Nodos internos:**
  - Hijo de R10 → **R1, R2, R3** (en azul).
  - Hijo de R11 → **R4, R5** (en azul).
  - Hijo de R12 → **R6, R7, R8** (en azul).
- **Nodos hoja:** cajas vacías debajo de cada entrada R1–R8, representando los punteros a datos o clusters de puntos.

(slide 45)

Búsqueda 1NN

**Figura:** Misma estructura que la slide anterior, con el punto de consulta **q** en una posición diferente.

**Parte izquierda (espacial):**
- **Rectángulos de nivel superior (naranja):** **R10**, **R11** y **R12** (misma disposición).
- **Rectángulos de nivel hoja (azul):** **R1** a **R8** con sus respectivos grupos de puntos negros.
- El **punto rojo «q»** ahora se ubica entre R10 y R11, más cerca del borde derecho de **R10** y del borde izquierdo de **R11**, específicamente junto a **R2** (dentro del área de R10).

**Parte derecha (árbol):**
- **Nodo raíz:** **R10, R11, R12** (naranja).
- **Nodos internos:**
  - R10 → **R1, R2, R3** (azul).
  - R11 → **R4, R5** (azul).
  - R12 → **R6, R7, R8** (azul).
- **Nodos hoja:** cajas vacías bajo R1–R8.

(slide 46)

```text
function NearestNeighborSearch(node, queryPoint, bestEntry):
  if node is a leaf:
     for each entry in node:
       dist = Distance(queryPoint, entry.object)
       if dist < bestEntry.Dist:
          bestEntry.Dist = dist
          bestEntry.Object = entry
  else:
     # Ordenar hijos por distancia mínima entre su MBR y el punto de consulta
     sortedChildren = sort node.children by MinDist(queryPoint, child.MBR)

     for each childNode in sortedChildren:
       if MinDist(queryPoint, childNode.MBR) < bestEntry.Dist:
          NearestNeighborSearch(childNode, queryPoint, bestEntry)
```

Condición de filtro:
- `MINDIST(Q, MBR) <= bestEntry` (resaltado en amarillo — poda: solo se explora una rama si la distancia mínima a su MBR es menor que la mejor distancia encontrada)
- `ED(Q, P) <= bestEntry` (resaltado en cian — en nodos hoja, se actualiza el mejor candidato si se encuentra un objeto más cercano)

¿Cola de prioridad en lugar de aplicar sort?

**Figura:** Slide con el pseudocódigo en un recuadro gris. Las líneas de condición de filtro están resaltadas en amarillo y cian respectivamente. En la parte inferior derecha, la pregunta «¿Cola de prioridad en lugar de aplicar sort?».

(slide 47)

```text
function NearestNeighborSearch(node, queryPoint, bestEntry):
  if node is a leaf:
     for each entry in node:
       dist = Distance(queryPoint, entry.object)
       if dist < bestEntry.Dist:
          bestEntry.Dist = dist
          bestEntry.Object = entry
  else:
     # Ordenar hijos por distancia mínima entre su MBR y el punto de consulta
     sortedChildren = sort node.children by MinDist(queryPoint, child.MBR)

     for each childNode in sortedChildren:
       if MinDist(queryPoint, childNode.MBR) < bestEntry.Dist:
          NearestNeighborSearch(childNode, queryPoint, bestEntry)
```

¿Si usamos una cola de prioridad para evitar el sort?

**Figura:** Mismo pseudocódigo que la slide anterior. La línea `sortedChildren = sort node.children by MinDist(queryPoint, child.MBR)` está resaltada en naranja. En la parte inferior, la pregunta en texto naranja: «¿Si usamos una cola de prioridad para evitar el sort?».

(slide 48)

### MINDIST

La distancia entre un punto y el punto más cercano posible dentro de un MBR

Se calcula en base a la proyección de los puntos en cada eje

$Q = (x,y)$

$R = \{(L.x,L.y)(U.x,U.y)\}$

MINDIST(Q, R)

- **Punto de consulta Q:** cuadrado rosa etiquetado $Q = (x, y)$ en la zona superior izquierda del gráfico.
- **MBR R:** rectángulo azul que contiene varios puntos negros pequeños (datos).
  - Definido por $R = \{(L.x, L.y), (U.x, U.y)\}$.
  - **Punto rojo** en la esquina inferior izquierda: coordenadas $(L.x, L.y)$.
  - **Punto verde** en la esquina superior derecha: coordenadas $(U.x, U.y)$.
- **MINDIST(Q, R):** flecha naranja desde $Q$ hacia el borde más cercano del rectángulo $R$ (línea horizontal), representando la distancia mínima del punto al MBR.
- Líneas discontinuas azules proyectan $Q$ y las esquinas de $R$ sobre los ejes.

Caja amarilla clara a la izquierda con el texto descriptivo.

(slide 49)

La distancia entre un punto y el punto más cercano posible dentro de un MBR

Se calcula en base a la proyección de los puntos en cada eje

$Q = (x,y)$

$R = \{(L.x,L.y)(U.x,U.y)\}$

MINDIST(Q, R)

- $Q.x < L.x$: $L.x - Q.x$
- $Q.x > U.x$: $Q.x - U.x$
- Else: 0

**Figura:** Mismo diagrama que la slide anterior (punto $Q$ rosa, MBR $R$ azul con puntos internos, esquinas $L$ roja y $U$ verde, flecha naranja MINDIST(Q, R)). A la derecha del diagrama, las reglas de cálculo por proyección en el eje $x$:
- Si $Q.x < L.x$: distancia $= L.x - Q.x$
- Si $Q.x > U.x$: distancia $= Q.x - U.x$
- Else: 0

Caja amarilla clara a la izquierda con el texto descriptivo.

(slide 50)

$Q = (x,y)$

$R = \{(L.x,L.y)(U.x,U.y)\}$

$D$

$$MINDIST(Q, R) = \sqrt{\sum_{i=1}^{D} (q_i - r_i)^2}$$

$$r_i = l_i \text{ si } q_i < l_i$$
$$= u_i \text{ si } q_i > u_i$$
$$= q_i \text{ otro caso}$$

**Figura:** Diagrama cartesiano 2D con punto $Q = (x,y)$ (cuadrado rosa), MBR $R$ (rectángulo azul con puntos negros internos), esquina inferior izquierda $L$ (punto rojo) y esquina superior derecha $U$ (punto verde). Flecha naranja de doble punta conecta $Q$ con el borde vertical más cercano de $R$. A la derecha, la fórmula matemática de MINDIST en $D$ dimensiones con la definición piecewise de $r_i$.

(slide 51)

$$MINDIST(Q, R) = \sqrt{\sum_{i=1}^{D} (q_i - r_i)^2}$$

$$r_i = l_i \text{ si } q_i < l_i$$
$$= u_i \text{ si } q_i > u_i$$
$$= q_i \text{ otro caso}$$

$p_1(1,2)$

$p_2(12,13)$

$p_3(6,3)$

$(5,1)$ — $(9,7)$

MINDIST($p_1$, R) = ??
MINDIST($p_2$, R) = ??
MINDIST($p_3$, R) = ??

**Figura:** Dos diagramas lado a lado con el mismo rectángulo $R$ (contorno azul claro):
- Esquina inferior izquierda (punto rojo): $(5, 1)$.
- Esquina superior derecha (punto verde): $(9, 7)$.
- Rectángulo contiene varios puntos negros internos.

**Diagrama izquierdo:** tres puntos magenta:
- $p_1$ en $(1, 2)$ — a la izquierda del rectángulo.
- $p_2$ en $(12, 13)$ — arriba a la derecha del rectángulo.
- $p_3$ en $(6, 3)$ — dentro del rectángulo.

Debajo: MINDIST($p_1$, R) = ??, MINDIST($p_2$, R) = ??, MINDIST($p_3$, R) = ??

Fórmula MINDIST en la esquina superior derecha.

(slide 52)

$$MINDIST(Q, R) = \sqrt{\sum_{i=1}^{D} (q_i - r_i)^2}$$

$$r_i = l_i \text{ si } q_i < l_i$$
$$= u_i \text{ si } q_i > u_i$$
$$= q_i \text{ otro caso}$$

$(5,1)$ — $(9,7)$

MINDIST(point, R) = 4.0

MINDIST(point, R) = 6.7

MINDIST(point, R) = 0

**Figura:** Dos diagramas con el mismo rectángulo $R$ (esquinas $(5,1)$ y $(9,7)$):

**Diagrama izquierdo (puntos externos):**
- Punto en $(1, 2)$: MINDIST(point, R) = **4.0**
- Punto en $(12, 13)$: MINDIST(point, R) = **6.7**

**Diagrama derecho (punto interno):**
- Punto en $(6, 3)$ dentro del rectángulo: MINDIST(point, R) = **0**

Fórmula MINDIST en la esquina superior derecha.

(slide 53)

Calcule el MINDIST entre Q y el MBR formado por los puntos

$$MINDIST(Q, R) = \sqrt{\sum_{i=1}^{D} (q_i - r_i)^2}$$

$$r_i = l_i \text{ si } q_i < l_i$$
$$= u_i \text{ si } q_i > u_i$$
$$= q_i \text{ otro caso}$$

P1=
P2=
P3=
P4=
MBR=
Q=
MINDIST(Q, MBR)=

**Figura:** Gráfico 2D con eje X de 0 a 8 y eje Y de 0 a 10:
- **Punto Q (rojo):** aproximadamente en $(1.2, 2.1)$, etiquetado «Q».
- **Punto 1 (verde):** en $(3.5, 4)$.
- **Punto 2 (verde):** en $(6, 7)$.
- **Punto 3 (verde):** en $(7, 3)$.
- **Punto 4 (verde):** aproximadamente en $(4.75, 1)$.

A la derecha del gráfico, lista de variables en blanco para completar: P1=, P2=, P3=, P4=, MBR=, Q=, MINDIST(Q, MBR)=.

Fórmula MINDIST en la esquina superior derecha.

(slide 54)

Calcule el MINDIST entre Q y el MBR formado por los puntos

$$MINDIST(Q, R) = \sqrt{\sum_{i=1}^{D} (q_i - r_i)^2}$$

$$r_i = l_i \text{ si } q_i < l_i$$
$$= u_i \text{ si } q_i > u_i$$
$$= q_i \text{ otro caso}$$

P1=(3,4)
P2=(5,7)
P3=(6,3)
P4=(4,1)
MBR={(3,1), (6,7)}
Q=(1,2)

MINDIST(Q, MBR)
= $(1 - 3)^2 + (2 - 2)^2$
= $4 + 0$
= $\sqrt{4}$
= $2$

**Figura:** Mismo gráfico 2D que la slide anterior (eje X: 0–8, eje Y: 0–10) con:
- Punto Q (rojo) en aproximadamente $(1.2, 2)$.
- Puntos 1–4 (verdes) en las posiciones indicadas.
- Rectángulo amarillo (MBR) con esquinas en $(3,1)$ y $(6,7)$ según los datos de texto; flecha marrón horizontal desde Q hacia el borde del MBR en $y=2$.

A la derecha, los valores completados y el cálculo paso a paso.

(slide 55)

### Inserción

Insert X

**Figura:** La slide se divide en dos partes: representación espacial a la izquierda y árbol a la derecha.

**Parte izquierda (espacial):** Cuatro MBR delineados en cian, etiquetados **P1**, **P2**, **P3** y **P4**:
- **P1** (superior izquierda): contiene **A**, **B** y **C**.
- **P2** (inferior centro-izquierda): contiene **D**, **E** y el nuevo objeto **X** (rectángulo rojo sólido). P2 se solapa ligeramente con P1 en el área de B.
- **P3** (superior centro-derecha): contiene **F** y **G**.
- **P4** (derecha): contiene **H**, **I** y **J**.

El objeto **X** se muestra como un rectángulo rojo sólido, ubicado junto a D y E dentro del MBR de P2.

**Parte derecha (árbol — «Insert X»):**
- **Nodo raíz:** cuatro entradas: **P1, P2, P3, P4**.
- **Nodos hoja** (capacidad de 4 slots cada uno):
  - **P1** → **[A, B, C, _]**
  - **P2** → **[D, E, X, _]** — **X** resaltada en rojo como elemento recién insertado.
  - **P3** → **[F, G, _, _]**
  - **P4** → **[H, I, J, _]**

(slide 56)

Insert Y

**Figura:** La slide se divide en dos partes: representación espacial a la izquierda y árbol a la derecha.

**Parte izquierda (espacial):** Cuatro MBR delineados en cian, etiquetados **P1**, **P2**, **P3** y **P4**:
- **P1** (superior izquierda): contiene **A**, **B** y **C**.
- **P2** (inferior izquierda/centro): contiene **D** y **E**.
- **P3** (superior derecha): contiene **F** y **G**.
- **P4** (derecha): contiene **H**, **I** y **J**.

Un nuevo objeto **Y** se muestra como un pequeño rectángulo rojo sólido, ubicado cerca del límite entre P1 y P2, solapándose ligeramente con el borde inferior del MBR de P1 y el área superior izquierda del MBR de P2.

**Parte derecha (árbol — «Insert Y»):**
- **Nodo raíz:** **P1, P2, P3, P4**.
- **Nodos hoja** (4 slots cada uno):
  - **P1** → **[A, B, C, _]**
  - **P2** → **[D, E, _, _]**
  - **P3** → **[F, G, _, _]**
  - **P4** → **[H, I, J, _]**

Y aún no ha sido insertado en el árbol.

(slide 57)

Insert Y

**Figura:** La slide se divide en dos partes: representación espacial a la izquierda y árbol a la derecha.

**Parte izquierda (espacial):** Cuatro MBR delineados en cian, etiquetados **P1**, **P2**, **P3** y **P4**:
- **P1** (superior izquierda): contiene **A**, **B** y **C**.
- **P2** (inferior izquierda): contiene **D**, **E** y el nuevo objeto **Y** (rectángulo rojo sólido).
- **P3** (superior derecha): contiene **F** y **G**.
- **P4** (derecha): contiene **H**, **I** y **J**.

El objeto **Y** se ubica espacialmente dentro del MBR de P2.

**Parte derecha (árbol — «Insert Y»):**
- **Nodo raíz:** **P1, P2, P3, P4**.
- **Nodos hoja** (4 slots cada uno):
  - **P1** → **[A, B, C, _]**
  - **P2** → **[D, E, Y, _]** — **Y** resaltada en rojo, insertada en el nodo hoja de P2.
  - **P3** → **[F, G, _, _]**
  - **P4** → **[H, I, J, _]**

(slide 58)

Insert Y

**Figura:** La slide se divide en dos partes: representación espacial a la izquierda y árbol a la derecha.

**Parte izquierda (espacial):** Cuatro MBR delineados en cian, etiquetados **P1**, **P2**, **P3** y **P4**:
- **P1** (superior izquierda): contiene **A**, **B** y **C**.
- **P2** (inferior centro): contiene **D** y **E**.
- **P3** (superior derecha): contiene **F** y **G**.
- **P4** (derecha): contiene **H**, **I** y **J**.

El objeto **Y** (rectángulo rojo) se muestra fuera de los agrupamientos existentes, cerca de la esquina inferior izquierda de P1 y el lado izquierdo de P2. **Flechas de doble punta azules** desde Y hacia los límites de P1 y P2, indicando el proceso de comparación para decidir qué región requiere la menor expansión para incluir Y.

**Parte derecha (árbol — «Insert Y»):**
- **Nodo raíz:** **P1, P2, P3, P4**.
- **Nodos hoja** (4 slots cada uno):
  - **P1** → **[A, B, C, _]**
  - **P2** → **[D, E, _, _]**
  - **P3** → **[F, G, _, _]**
  - **P4** → **[H, I, J, _]**

Y aún no ha sido insertado; se evalúa entre P1 y P2.

(slide 59)

Insert Y

**Figura:** La slide se divide en dos partes: representación espacial a la izquierda y árbol a la derecha.

**Parte izquierda (espacial):** Cuatro regiones con MBR delineados en cian:
- **P1** (superior izquierda, contorno azul): contiene **A**, **B**, **C** y el nuevo objeto **Y** (rectángulo rojo sólido, ubicado dentro del área de P1).
- **P2** (inferior centro, contorno azul): contiene **D** y **E**.
- **P3** (superior derecha): contiene **F** y **G**.
- **P4** (inferior derecha, contorno azul): contiene **H**, **I** y **J**.

**Parte derecha (árbol — «Insert Y»):**
- **Nodo raíz:** **P1, P2, P3, P4**.
- **Nodos hoja** (4 slots cada uno):
  - **P1** → **[A, B, C, Y]** — **Y** resaltada en rojo, insertada en el nodo hoja de P1.
  - **P2** → **[D, E, _, _]**
  - **P3** → **[F, G, _, _]**
  - **P4** → **[H, I, J, _]**

(slide 60)

MINDIST(Y, P1) = MINDIST(Y, P2)

**Figura:** La slide se divide en dos partes: a la izquierda, una representación espacial en 2D; a la derecha, un diagrama de árbol titulado «Insert Y».

**Parte izquierda (espacial):** Cuatro MBR (Minimum Bounding Rectangles) delineados en cian, etiquetados **P1**, **P2**, **P3** y **P4**.
- **P1** (superior izquierda) contiene los objetos **A**, **B** y **C**.
- **P2** (inferior izquierda) contiene los objetos **D** y **E**.
- **P3** (superior derecha) contiene los objetos **F** y **G**.
- **P4** (inferior derecha) contiene los objetos **H**, **I** y **J**.

Un nuevo objeto **Y** se muestra como un pequeño rectángulo sólido en color rojo, ubicado fuera de los MBR existentes, en la zona inferior izquierda cerca de P2. Flechas de doble punta en color azul se extienden desde Y hacia los bordes de P1 y P2, indicando que la distancia mínima de Y a P1 es igual a la distancia mínima de Y a P2 (condición expresada en la parte superior: MINDIST(Y, P1) = MINDIST(Y, P2)).

**Parte derecha (árbol — «Insert Y»):**
- **Nodo raíz:** contiene cuatro entradas: **P1**, **P2**, **P3**, **P4**.
- **Nodos hoja** (cada uno con capacidad de 4 slots):
  - **P1** → **[A, B, C, _]**
  - **P2** → **[D, E, Y, _]** — la **Y** aparece en color rojo, indicando la inserción del nuevo objeto en la rama correspondiente a P2.
  - **P3** → **[F, G, _, _]**
  - **P4** → **[H, I, J, _]**

Los slots vacíos (_) indican capacidad máxima (fan-out) de 4 por nodo.

(slide 61)

**Figura:** La slide se divide en dos partes: a la izquierda, representación espacial en 2D; a la derecha, diagrama de árbol titulado «Insert Y».

**Parte izquierda (espacial):** Cuatro MBR delineados en cian, etiquetados **P1**, **P2**, **P3** y **P4**.
- **P1** (superior izquierda, contorno azul) contiene los objetos **A**, **B** y **C**.
- **P2** (inferior izquierda) es la región donde se coloca el nuevo objeto **Y**; contiene los objetos **D** y **E**. El MBR de P2 se ha expandido para acomodar Y.
- **P3** (superior derecha, contorno azul) contiene los objetos **F** y **G**.
- **P4** (inferior derecha, contorno azul) contiene los objetos **H**, **I** y **J**.

El objeto **Y** se muestra como un pequeño rectángulo sólido en color rojo, ubicado en el cuadrante inferior izquierdo junto a D y E. Bandas horizontales y verticales en color salmón se cruzan en el objeto Y, indicando la extensión espacial o la recalculación del MBR de la región P2 para acomodar la nueva entrada. Flechas de doble punta en color azul indican la distancia o expansión necesaria dentro del área P2 para incluir Y.

**Parte derecha (árbol — «Insert Y»):**
- **Nodo raíz:** contiene cuatro entradas: **P1**, **P2**, **P3**, **P4**.
- **Nodos hoja** (cada uno con 4 slots, capacidad máxima M = 4):
  - **P1** → **[A, B, C, _]**
  - **P2** → **[D, E, Y, _]** — la **Y** está resaltada en rojo como elemento recién insertado.
  - **P3** → **[F, G, _, _]**
  - **P4** → **[H, I, J, _]**

No se requiere split: cada nodo hoja tiene 4 slots y P2 solo tenía dos objetos (D y E) antes de la inserción, por lo que Y se agregó sin desbordar el nodo.

(slide 62)

- ¿Qué pasa cuando el nodo se llena?
  - Split cuadrático
  - Split lineal
  - Split optimizado

Mola, F., & Siciliano, R. (1997). A fast splitting procedure for classification trees. Statistics and Computing, 7(3), 209-216

- ¿Operación de eliminación?
  - Similar al B-Tree

**Figura:** El título «R-Tree: Inserción» aparece en la parte superior. Dos preguntas con viñetas: la primera sobre qué ocurre cuando el nodo se llena (tres sub-viñetas con tipos de split y referencia bibliográfica en cursiva debajo); la segunda sobre la operación de eliminación (sub-viñeta «Similar al B-Tree»). La palabra «eliminación» aparece en negrita.

(slide 63)

### Ejercicio: Construcción con Split cuadrático

Construya el RTree para los siguientes puntos:

**Split cuadrático:**

1. Crear dos nuevos nodos con los dos hijos mas separados entre si.
2. Agregar los demás hijos al nodo más cercano.

M=4      m=2

| Etiqueta | X | Y |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 11 |
| 3 | 6,5 | 9,5 |
| 4 | 1 | 9 |
| 5 | 1 | 13 |
| 6 | 2 | 9 |
| 7 | 8 | 1 |
| 8 | 4 | 8 |
| 9 | 2 | 4 |
| 10 | 4 | 10 |
| 11 | 6 | 3 |
| 12 | 6 | 1 |
| 13 | 2 | 2 |
| 14 | 7 | 5 |
| 15 | 7 | 2 |
| 16 | 2 | 13 |
| 16 | 4 | 9 |
| 17 | 0 | 5 |
| 18 | 1 | 5 |
| 19 | 1 | 11 |
| 20 | 5,2 | 9 |
| 21 | 7 | 12 |
| 22 | 8 | 3 |
| 23 | 7 | 11 |
| 24 | 7 | 15 |
| 25 | 3 | 15 |
| 26 | 4 | 2 |

**Figura:** Plano cartesiano con eje X de 0 a 9 y eje Y de 0 a 15. Veintisiete puntos verdes numerados distribuidos en la cuadrícula. Posiciones aproximadas según la cuadrícula:
- En y=15: punto **25** en x≈3, punto **24** en x≈7.
- En y=14: punto **16** en x≈4.
- En y=13: punto **5** en x≈1.
- En y=12: punto **21** en x≈7.
- En y=11: punto **2** en x≈2, punto **19** en x≈1.
- En y=10: punto **10** en x≈4, punto **23** en x≈7, punto **3** en x≈6,5 (entre líneas de cuadrícula).
- En y=9: punto **4** en x≈1, punto **6** en x≈2, punto **16** (segunda etiqueta) en x≈4, punto **20** en x≈5,2, punto **8** en x≈4.
- En y=5: punto **17** en x≈0, punto **18** en x≈1, punto **14** en x≈7.
- En y=4: punto **9** en x≈2.
- En y=3: punto **11** en x≈6, punto **13** en x≈2, punto **26** en x≈4, punto **15** en x≈7, punto **22** en x≈8.
- En y=2: punto **1** en x≈1, punto **12** en x≈6, punto **7** en x≈8.
- En y=1: (eje inferior).

A la derecha del gráfico, el algoritmo «Split cuadrático» con dos pasos numerados y los parámetros M=4, m=2.

(slide 64)

1. Crear dos nuevos nodos con los dos hijos mas separados entre si.
2. Agregar los demás hijos al nodo más cercano.

M=4      m=2

| Etiqueta | X | Y |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 11 |
| 3 | 7 | 10 |
| 4 | 1 | 9 |
| 5 | 1 | 13 |
| 6 | 2 | 9 |
| 7 | 9 | 1 |
| 8 | 4 | 8 |
| 9 | 2 | 4 |
| 10 | 4 | 10 |
| 11 | 7 | 3 |
| 12 | 7 | 1 |
| 13 | 2 | 2 |
| 14 | 8 | 5 |
| 15 | 8 | 2 |
| 16 | 2 | 13 |
| 16 | 4 | 9 |
| 17 | 0 | 5 |
| 18 | 1 | 5 |
| 19 | 1 | 11 |
| 20 | 6 | 9 |
| 21 | 8 | 12 |
| 22 | 9 | 3 |
| 23 | 8 | 11 |
| 24 | 8 | 15 |
| 25 | 4 | 15 |
| 26 | 4 | 2 |

**Figura:** Plano cartesiano con eje X de 0 a 9 y eje Y de 0 a 15. Veintisiete puntos verdes circulares numerados del 1 al 26 (la etiqueta «16» aparece dos veces: en (2, 13) y en (4, 9)). Distribución idéntica a la slide anterior, mostrando el estado inicial antes del split. En la parte superior izquierda, el título «Split:» con las dos reglas numeradas. Debajo del gráfico, los parámetros M=4 y m=2.

(slide 65)

1. Crear dos nuevos nodos con los dos hijos mas separados entre si.
2. Agregar los demás hijos al nodo más cercano.

M=4      m=2

**Figura — Cuadrícula espacial (parte inferior izquierda):** Plano cartesiano con eje X de 0 a 9 y eje Y de 0 a 15. Doce puntos verdes numerados con MBR (Minimum Bounding Rectangles) superpuestos:

**MBRs de nivel bajo (azul):**
- **R1:** rectángulo horizontal que contiene los puntos **4** y **6**.
- **R2:** rectángulo vertical que contiene los puntos **5** y **2**.
- **R3:** segmento horizontal que contiene los puntos **12** y **7**.
- **R4:** rectángulo horizontal que contiene los puntos **10** y **3**.
- **R5:** rectángulo vertical que contiene los puntos **1** y **9**.

**MBRs de nivel superior (rojo):**
- **R6:** engloba el área superior izquierda/central; contiene los MBRs R1, R2, R4 y el punto **8**.
- **R7:** engloba el área inferior; contiene los MBRs R3, R5 y el punto **11**.

**Figura — Diagrama de árbol (parte superior derecha):**
- **Nodo raíz:** contiene dos entradas **R6** y **R7**, con 4 slots totales (2 vacíos).
- **Nivel 1:**
  - Flecha desde **R6** hacia un nodo que contiene **R2**, **R1** y **R4** (1 slot vacío).
  - Flecha desde **R7** hacia un nodo que contiene **R3** y **R5** (2 slots vacíos).

Debajo de la cuadrícula: M=4 (máximo de entradas por nodo), m=2 (mínimo de entradas por nodo).

(slide 66)

### Variantes de R-Tree

- R+ Tree: No permite solapamiento entre MBR de nodos hermanos.

T. Sellis, N. Roussopoulos, and C. Faloutsos. The R+Tree: A dynamic index for multi-dimensional objects. In VLDB, 1987

- R* Tree: Mejora el rendimiento reinsertando elementos y reorganizando nodos para reducir solapamientos.

Beckmann, N.; Kriegel, H. P.; Schneider, R.; Seeger, B. (1990). "The R*-tree: an efficient and robust access method for points and rectangles". SIGMOD '90.

**Figura:** El título «Variantes de R-Tree» en la parte superior. Dos viñetas principales: R+ Tree con su descripción y referencia bibliográfica en cursiva; R* Tree con su descripción y referencia bibliográfica en cursiva. Todo el texto en negro.

(slide 67)

## Glosario

| Término | Definición |
| :--- | :--- |
| **Datos Espaciales** | Colección de datos que representan objetos con ubicación y forma en un espacio métrico (generalmente en 2D y 3D). Se diferencian de datos convencionales en que poseen geometría asociada: coordenadas, dimensiones, relaciones. |
| **Datos Geoespaciales** | Subconjunto de los datos espaciales que están georreferenciados a la superficie terrestre. Usan sistemas de coordenadas geográficas (latitud/longitud) definidos en un elipsoide. |
| **BD Espacial** | Sistema de gestión de bases de datos (SGBD) que incorpora tipos de datos, funciones y estructuras de indexación especializados para almacenar, consultar y analizar información que tiene una localización en el espacio. |
| **GIS** | Ecosistema tecnológico que combina mapas y bases de datos para responder preguntas espaciales como "¿en dónde?", "¿qué tan lejos esta?", "¿qué hay en este lugar?". |
| **SRID** | Sistema de referencia espacial. Identificador numérico que asigna el sistema de coordenadas a una geometría (por ejemplo, 4326 para WGS 84). |
| **geometry** | Tipo de dato PostGIS para geometrías planas; con SRID geográfico (4326) permite consultas planas. |
| **geography** | Tipo de dato PostGIS que calcula distancias geodésicas sobre el elipsoide. |
| **WKT** | Well-Known Text. Formato de cadena de texto para representar geometrías (por ejemplo, `POINT(-3.7038 40.4168)`). |
| **MBR** | Minimum Bounding Rectangle. Rectángulo mínimo que encierra un objeto geométrico; cada MBR se representa con dos puntos $\{L, U\}$: la esquina inferior izquierda y la esquina superior derecha. |
| **Índice espacial** | Estructura de datos que permite realizar consultas eficientes sobre datos espaciales (geográficos). |
| **GiST** | Generalized Search Tree. Permite búsquedas por rango, proximidad y otras operaciones complejas que no son posibles con B-Tree. Soporta estructuras como R-Tree, B-Tree, y más. |
| **PostGIS** | Extensión espacial para PostgreSQL que añade funciones espaciales y tipos de geometría. |
| **R-Tree** | Índice espacial jerárquico que organiza objetos geométricos (puntos, líneas, polígonos) mediante rectángulos mínimos (MBR) para facilitar búsquedas espaciales eficientes. Es un árbol balanceado similar a un B-Tree. |
| **MINDIST** | Distancia entre un punto y el punto más cercano posible dentro de un MBR. Se calcula en base a la proyección de los puntos en cada eje. |
| **Split cuadrático** | Procedimiento de división de nodos llenos en R-Tree: (1) crear dos nuevos nodos con los dos hijos más separados entre sí; (2) agregar los demás hijos al nodo más cercano. |
| **R+ Tree** | Variante de R-Tree que no permite solapamiento entre MBR de nodos hermanos. |
| **R* Tree** | Variante de R-Tree que mejora el rendimiento reinsertando elementos y reorganizando nodos para reducir solapamientos. |
