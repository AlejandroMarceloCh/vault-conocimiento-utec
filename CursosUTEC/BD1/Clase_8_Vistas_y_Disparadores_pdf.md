---
curso: BD1
titulo: Clase 8 Vistas y Disparadores
slides: 54
fuente: Clase 8 Vistas y Disparadores.pdf
---

## Slide 1
Portada decorativa (logo UTEC, imagen de mujer con visor VR, fondo azul con globo terráqueo digital, logo "TRANSFORMATEC"). Texto: "CLASE 8: VISTAS Y DISPARADORES (SQL)", "CS2041- Base de Datos I", "Ciclo 2024-1". Correos de los profesores: Teófilo Chambilla - tchambilla@utec.edu.pe, Brenner Ojeda - bojeda@utec.edu.pe.

## Slide 2
Slide "Índice" con lista de temas del curso: Introducción, Vistas, Vistas Actualizable, Vistas Materializadas, Disparadores. Imagen decorativa de mano robótica tocando un holograma de mapa mundial (lado derecho).

## Slide 3
Slide de contexto del curso "CS2041 Base de Datos I - Ciclo 2024-1". Diagrama de línea de tiempo/roadmap del curso con barras de progreso horizontales bajo cada tema: Introducción, Modelo Relacional, Álgebra Relacional & Cálculo Relacional, Entidad-Relación, SQL (con subtexto "Actualización, Restricciones"), y resaltado en azul "SQL -Vistas y Disparadores" (tema de hoy, marcado con un icono de mascota ninja apuntando), luego Formas Normales (aún sin cubrir, barras en gris claro), con una bandera de meta al final. Las barras azules indican los temas ya cubiertos; las claras, pendientes.

## Slide 4
Título "¿Acaso hemos visto todo de SQL?". Captura de un GIF/imagen oscura de la Tierra vista desde el espacio con texto superpuesto "Lo que hemos visto de SQL" apuntando a una porción pequeña iluminada del planeta (analogía visual: lo visto de SQL es solo una fracción pequeña del total). Respuesta al pie: "(no)".

## Slide 5
Título "Lo que exploraremos hoy día". Misma imagen de la Tierra oscura con "Lo que hemos visto de SQL" señalando la porción pequeña iluminada. Al pie: "(vistas y disparadores)" — indicando que estos son parte de lo que falta por ver.

## Slide 6
Título "Motivación: Metacritic". Captura de pantalla del sitio web Metacritic (sección Music), mostrando el menú (Movies, Games, TV, Music, Features), submenú (New Releases, Coming Soon, High Scores, Browse A-Z, Publications, People), y un bloque "New Album Releases" con 3 álbumes destacados (Leonard Cohen 92, Lady Gaga 68, NxWorries 81, cada uno con conteo de críticas) y una lista lateral "More recent releases" con 6 álbumes y sus puntajes.

## Slide 7
Título "Motivación: Metacritic". Dos capturas de pantalla superpuestas de Metacritic: a la izquierda semi-transparente la vista anterior de "New Album Releases"; a la derecha la página de detalle del álbum "You Want It Darker" de Leonard Cohen, mostrando pestañas (Summary, Critic Reviews, User Reviews, Details & Credits), el Metascore 92 ("Universal acclaim", basado en 19 críticas), distribución de puntaje (Positive 19, Mixed 0, Negative 0), botón "Buy On amazon.com", y reseñas individuales de críticos (The Observer 100, The Guardian 100) con fecha y texto de reseña.

## Slide 8
Título "Metacritic: Evaluaciones de música". Muestra el esquema relacional con datos de ejemplo:

**Artista**
| nombre | país | retirado |
|---|---|---|
| Leonard Cohen | Canadá | false |
| Lady Gaga | EE.UU. | false |
| David Bowie | G.B. | true |
| Justin Bieber | Canadá | false |
| ... | ... | ... |

**Álbum**
| nombre | artista | año |
|---|---|---|
| Old Ideas | Leonard Cohen | 2012 |
| Dear Heather | Leonard Cohen | 2004 |
| You Want It Darker | Leonard Cohen | 2016 |
| Popular Problems | Leonard Cohen | 2014 |
| ARTPOP | Lady Gaga | 2013 |
| ... | ... | ... |

**Evaluación**
| álbum | artista | fuente | eval |
|---|---|---|---|
| Popular Problems | Leonard Cohen | The Guardian | 80 |
| Popular Problems | Leonard Cohen | The Observer | 80 |
| Popular Problems | Leonard Cohen | Uncut | 90 |
| You Want It Darker | Leonard Cohen | The Observer | 100 |
| You Want It Darker | Leonard Cohen | Uncut | 90 |
| You Want It Darker | Leonard Cohen | Rolling Stone | 80 |
| You Want It Darker | Leonard Cohen | The Guardian | 100 |
| Dear Heather | Leonard Cohen | The Guardian | 60 |
| Dear Heather | Leonard Cohen | Uncut | 100 |
| Dear Heather | Leonard Cohen | Rolling Stone | 70 |
| Old Ideas | Leonard Cohen | Rolling Stone | 90 |
| Old Ideas | Leonard Cohen | Uncut | 80 |
| ARTPOP | Lady Gaga | Rolling Stone | 60 |
| ... | ... | ... | ... |

## Slide 9
Título "Agregación de evaluaciones". Mismas tres tablas (Artista, Álbum, Evaluación) que en el slide anterior. Debajo: captura de la tarjeta de Metacritic del álbum "You Want It Darker" de Leonard Cohen con puntaje 92 (basado en 19 críticas), junto a la consulta SQL:
```sql
SELECT FLOOR(AVG(eval)) AS pm
FROM Evaluación
WHERE álbum='You Want It Darker'
  AND artista='Leonard Cohen'
```
Resultado mostrado en tabla resaltada en celeste: `pm = 92`. Al pie, pregunta destacada en recuadro punteado: "¿Pero si quisiéramos hacer este tipo de consulta con mucha frecuencia? …"

## Slide 10
Título "Agregación de evaluaciones". Mismas tablas base, pero ahora la tabla **Álbum** tiene una columna adicional `pm` (calculada/simulada) con valores: Old Ideas=85, Dear Heather=74, You Want It Darker=92, Popular Problems=86, ARTPOP=61 (resaltada con recuadro punteado naranja indicando que sería una columna "hardcodeada" o materializada directamente en la tabla). Consulta:
```sql
SELECT pm
FROM Álbum
WHERE nombre='You Want It Darker'
  AND artista='Leonard Cohen'
```
Resultado: `pm=92`. Al pie: "¿Algún problema aquí? …" (la idea: guardar `pm` como columna física en Álbum requeriría actualizarla manualmente cada vez que cambien las evaluaciones).

## Slide 11
Título "Agregación de evaluaciones *dinámicas*". Se agrega una fila nueva a Evaluación en verde (You Want It Darker, Leonard Cohen, Mojo, 100 — una nueva fuente de evaluación), mostrando que la columna `pm` de la tabla Álbum (marcada con recuadro rojo, aún en 92) queda desactualizada/obsoleta tras el insert, porque es un valor estático que no se recalculó. Mismo query y resultado (`pm=92`, marcado en rojo indicando que está "congelado"/obsoleto).

## Slide 12
Slide separador de sección: "VISTAS", con subtítulo "Capítulo 3.6 | Ramakrishnan / Gehrke". Ilustración decorativa de mascota ninja sentada en un sillón sosteniendo un lápiz brillante (mascota recurrente del curso, decorativa).

## Slide 13
Título "Vistas: tablas virtuales". Imagen/GIF decorativo en fondo negro: una persona moviendo objetos de una mesa (cámara, cubo Rubik, taza roja, marco con foto de gato, libreta) — metáfora visual de "manipular algo tangible" pero relacionado a que las vistas son "virtuales" (no objetos físicos reales). Marca de agua "youtube.com/brusspup".

## Slide 14
Título "Vista: una tabla virtual". Muestra las tablas base Artista, Álbum, Evaluación (igual que antes). Código SQL:
```sql
CREATE VIEW ÁlbumEval AS
  SELECT álbum, artista,
    FLOOR(AVG(eval)) AS pm,
    COUNT(eval) AS num
  FROM Evaluación
  GROUP BY álbum, artista
```
Resultado (tabla ÁlbumEval, resaltada en amarillo), la vista virtual creada:
| álbum | artista | pm | num |
|---|---|---|---|
| Old Ideas | Leonard Cohen | 85 | 2 |
| Dear Heather | Leonard Cohen | 76 | 3 |
| You Want It Darker | Leonard Cohen | 94 | 5 |
| Popular Problems | Leonard Cohen | 83 | 3 |
| ARTPOP | Lady Gaga | 64 | 3 |

## Slide 15
Título "Vista: facilitan consultas más simples". Mismas tablas base + la vista ÁlbumEval ya creada. Consulta simplificada usando la vista:
```sql
SELECT pm
FROM ÁlbumEval
WHERE álbum='You Want It Darker'
  AND artista='Leonard Cohen'
```
Resultado: `pm=94`. Demuestra que consultar sobre la vista es mucho más simple que repetir el GROUP BY cada vez.

## Slide 16
Título "¿Cómo funcionan las vistas?" — diagrama tipo "notas manuscritas" (formas de nube/burbuja de colores) explicando el proceso en 3 pasos numerados en la esquina: (0) Crear la vista — con el `CREATE VIEW ÁlbumEval AS SELECT...` (burbuja naranja); (1) Extender la consulta de conformidad con la vista — sustituir `FROM ÁlbumEval` por la subconsulta completa (burbuja roja/rosa) mostrando `SELECT pm FROM ÁlbumEval WHERE...`; (2) Ejecutar la consulta extendida sobre las tablas bases — la consulta final anidada con subquery `(SELECT álbum, artista, FLOOR(AVG(eval)) AS pm, COUNT(eval) AS num FROM Evaluación GROUP BY álbum, artista) ÁlbumEval` (burbuja azul), dando resultado `pm=94`. Flechas conectan las burbujas mostrando el flujo: se crea la vista → se extiende la consulta que la referencia → se ejecuta sobre tablas base.

## Slide 17
Título "¿Cómo funcionan las vistas?" (continuación, versión más limpia sin las burbujas manuscritas). Recuadro amarillo destacado con explicación: "Con la vista, guardamos una sub-consulta frecuente para reutilizarla en varias consultas. (No estamos guardando/materializando los datos de la tabla virtual. ¡Así no hay problema con actualizaciones en los datos subyacentes!)". Debajo, la consulta extendida con subquery resaltada con recuadro punteado naranja indicando la porción que corresponde a la definición de la vista, y a la derecha el `CREATE VIEW` original y la consulta simple sobre la vista.

## Slide 18
Título "Eliminar una vista". Tablas base + vista ÁlbumEval (amarilla) como contexto. Código:
```sql
DROP VIEW ÁlbumEval
```

## Slide 19
Misma slide "Eliminar una vista" pero con una imagen superpuesta de una escena de la película Terminator (Arnold Schwarzenegger, rostro dañado/metálico) ocupando el centro — imagen decorativa/humorística (meme) sin relación directa al contenido técnico, ilustrando "eliminar/destruir" de forma humorística. El fondo se oscurece.

## Slide 20
Slide de transición: "VISTAS ACTUALIZABLES" (texto gris, fondo blanco, sin más contenido — separador de subsección).

## Slide 21
Título "¿Actualizar una vista?". Tablas base + vista ÁlbumEval (amarilla) sin cambios. Código:
```sql
INSERT INTO ÁlbumEval
VALUES ('Purpose','Justin Bieber',63,4)
```
Al pie, pregunta en recuadro punteado: "¿Qué pasa aquí entonces? …"

## Slide 22
Título "¿Actualizar una vista? ¡Hay ambigüedad!" (en rojo). Mismo INSERT del slide anterior. Recuadro amarillo: "La idea es actualizar las tablas bases mediante la vista (no la vista misma)." Recuadro gris: "¿Entonces, cuál sería el resultado de esta inserción sobre las tablas bases? …" Recuadro rojo con borde punteado: "¡No basta la información para actualizar las tablas bases!" (pm y num son valores agregados, no hay forma de "desagregarlos" en filas concretas de Evaluación).

## Slide 23
Título "Vistas de solo lectura". Mismo INSERT. Recuadro amarillo destacado: "Cuando la vista permite ambigüedad, la vista es solo lectura: no se puede actualizar."

## Slide 24
Título "Vistas actualizables". Se introduce un nuevo ejemplo: vista **EvaluaciónGuardian**, definida como filtro simple (sin agregación) sobre Evaluación:
```sql
CREATE VIEW EvaluaciónGuardian AS
  SELECT * FROM Evaluación
  WHERE fuente='The Guardian'
```
Tabla resultante (amarilla):
| álbum | artista | fuente | eval |
|---|---|---|---|
| Popular Problems | Leonard Cohen | The Guardian | 80 |
| You Want It Darker | Leonard Cohen | The Guardian | 100 |
| Dear Heather | Leonard Cohen | The Guardian | 60 |
| ... | ... | ... | ... |

## Slide 25
Continuación "Vistas actualizables". Se ejecuta:
```sql
INSERT INTO EvaluaciónGuardian VALUES
  ('Purpose','Justin Bieber','The Guardian',60)
```
Esta vez SÍ funciona: se agrega una nueva fila (en verde) tanto a la tabla base **Evaluación** ("Purpose", "Justin Bieber", "The Guardian", 60) como a la vista **EvaluaciónGuardian**, porque no hay ambigüedad (es una simple selección/filtro de columnas y filas, no una agregación).

## Slide 26
Título "Actualizando una vista". Texto explicativo (bullets):
- "Es difícil caracterizar precisamente las vistas actualizables, (incluyendo en la teoría de bases de datos) pero una vista es 'solo lectura' cuando involucra, por ejemplo:" — "Agregación (conteo, suma, etc)" (en azul) y "Proyección que elimine una columna que no permita nulos" (en azul).
- "A menudo, los motores no implementan vistas actualizables sobre varias tablas" (con "varias tablas" en rojo).
Recuadro amarillo al pie: "Pero por supuesto, no hay problema actualizar las tablas bases directamente (si uno tiene acceso) … La vista se actualizará automáticamente".

## Slide 27
Título "Vistas: ¡No son tablas físicas!". Mismo GIF decorativo de la persona moviendo objetos de la mesa (cámara, cubo Rubik, marco con gato) visto en el slide 13 — reutilizado como metáfora recurrente, marcado "decorativa".

## Slide 28
Título "¿Para qué sirven las vistas entonces?". Dos bullets principales:
- "Abreviatura/abstracción" (naranja) — "Reducir la complejidad de consultas, evitando repeticiones de patrones comunes"
- "Seguridad" (azul) — "Se puede dar acceso a una vista (un subconjunto de los datos) y no a todos los datos"
Al pie, pregunta/respuesta en recuadros: "¿Cuáles son los costos de mantener una vista?" → "¡Casi nada con respecto a la gestión de los datos! Pero …"

## Slide 29
Título "El costo de consulta". Comparación lado a lado de dos consultas SQL equivalentes:

Izquierda ("La consulta directa"):
```sql
SELECT FLOOR(AVG(eval)) AS pm
FROM Evaluación
WHERE álbum='You Want It Darker'
  AND artista='Leonard Cohen'
```

Derecha ("La consulta extendida con la vista"):
```sql
SELECT pm
FROM
  ( SELECT álbum, artista,
    FLOOR(AVG(eval)) AS pm,
      COUNT(eval) AS num
    FROM Evaluación
    GROUP BY álbum,artista ) ÁlbumEval
WHERE álbum='You Want It Darker'
  AND artista='Leonard Cohen'
```
Texto: "Son equivalentes pero la consulta extendida es mucho más difícil de optimizar". Pregunta al pie: "¿Y si el rendimiento de las consultas importa?"

## Slide 30
Slide separador: "VISTAS MATERIALIZADAS", con la misma mascota ninja decorativa sentada en el sillón sosteniendo el lápiz brillante.

## Slide 31
Título "Vista materializada: guardar tablas virtuales". Tablas base sin cambios. Código:
```sql
CREATE MATERIALIZED VIEW ÁlbumEval AS
  SELECT álbum, artista,
    FLOOR(AVG(eval)) AS pm,
    COUNT(eval) AS num
  FROM Evaluación
  GROUP BY álbum, artista
```
Resultado idéntico al de la vista normal (tabla ÁlbumEval con pm/num), pero ahora los datos SÍ se guardan físicamente (materializan).

## Slide 32
Título "Vista materializada: consultar directamente". Se consulta la vista materializada:
```sql
SELECT pm
FROM ÁlbumEval
WHERE álbum='You Want It Darker'
  AND artista='Leonard Cohen'
```
Resultado: `pm=92` — más rápido porque los datos ya están precalculados/almacenados, no requiere recalcular el agregado.

## Slide 33
Título "Vista materializada: actualización". Se inserta una nueva evaluación en verde (You Want It Darker, Leonard Cohen, Mojo, 100). El valor `pm=92` en la vista materializada queda marcado con recuadro rojo punteado, indicando que está desactualizado (no se refrescó automáticamente tras el insert).

## Slide 34
Continuación "Vista materializada: actualización". Se ejecuta:
```sql
REFRESH MATERIALIZED VIEW ÁlbumEval
```
Tras esto, la tabla ÁlbumEval se actualiza y el valor de `pm` para "You Want It Darker" pasa a 94 (en verde), reflejando la nueva evaluación agregada.

## Slide 35
Título "Materializar vistas vs. Crear tablas". Comparación lado a lado con ícono "VS" al centro:

Izquierda:
```sql
CREATE MATERIALIZED VIEW ÁlbumEval AS
  SELECT álbum, artista,
    FLOOR(AVG(eval)) AS pm,
      COUNT(eval) AS num
  FROM Evaluación
  GROUP BY álbum,artista
```

Derecha:
```sql
CREATE TABLE ÁlbumEval AS
  SELECT álbum, artista,
    FLOOR(AVG(eval)) AS pm,
      COUNT(eval) AS num
  FROM Evaluación
  GROUP BY álbum,artista
```

Pregunta/respuesta al pie: "¿Cuál es la diferencia más importante entre crear una tabla y crear una vista materializada?" → "En una vista materializada, se guarda la consulta para facilitar la actualización de la vista en una fase posterior" + `REFRESH MATERIALIZED VIEW ÁlbumEval`.

## Slide 36
Título "¿Se pueden cambiar vistas?". Código genérico `ALTER [MATERIALIZED] VIEW ...`. Captura de un bloque de sintaxis SQL (estilo consola/monoespaciado) mostrando las variantes de `ALTER VIEW`: `ALTER COLUMN ... SET DEFAULT expression`, `ALTER COLUMN ... DROP DEFAULT`, `OWNER TO {new_owner | CURRENT_USER | SESSION_USER}`, `RENAME TO new_name`, `SET SCHEMA new_schema`, `SET (view_option_name [=value] [,...])`, `RESET (view_option_name [,...])`. Al pie: "… es limitado."

## Slide 37
Slide tipo cartel de advertencia amarillo "WARNING" con ícono de triángulo de exclamación. Texto: "Vistas 'virtuales' son estándares" (negro) y "Vistas materializadas no son estándares" (en rojo), con subtexto "(pero hay soporte en Oracle y Postgres 13+)".

## Slide 38
Slide separador: "DISPARADORES (o GATILLOS/TRIGGERS)", subtítulo "Capítulo 3.6 | Ramakrishnan / Gehrke". Misma mascota ninja decorativa.

## Slide 39
Título "¿Actualizar una tabla automáticamente?". Tabla Evaluación (sin cambios visibles) y tabla ÁlbumEval (con pm/num) como contexto. Pregunta en recuadro punteado: "¿Cómo podríamos actualizar la tabla ÁlbumEval dada una inserción a Evaluación?"

## Slide 40
Título "Disparadores: Evento/Condición/Acción". Tablas de contexto (ÁlbumEval y Evaluación). Código SQL de un trigger:
```sql
CREATE TRIGGER SerAmigable
  AFTER UPDATE OF pm ON ÁlbumEval
  REFERENCING
    OLD ROW AS TuplaAntigua
    NEW ROW AS TuplaNueva
  FOR EACH ROW
    WHEN (TuplaAntigua.pm > TuplaNueva.pm)
    SET TuplaNueva.pm = TuplaAntigua.pm
```
Pregunta/respuesta: "¿Qué hace el disparador?" → "Si intentamos reducir el pm de un álbum, se restaurará el valor previo" y "¿Dónde están Evento/Condición/Acción?" (Evento=AFTER UPDATE OF pm, Condición=WHEN, Acción=SET).

## Slide 41
Continuación "Disparadores: Evento/Condición/Acción". Se ejecuta:
```sql
UPDATE ÁlbumEval
SET pm = 50
WHERE álbum = 'ARTPOP'
  AND artista = 'Lady Gaga'
```
El valor `pm=64` de ARTPOP queda marcado con recuadro punteado amarillo, indicando que el trigger evita la reducción. Resultado: "No cambia." (el trigger restauró el valor original de 64 porque 50<64 activó la condición WHEN).

## Slide 42
Repetición del slide 39 (misma pregunta "¿Cómo podríamos actualizar la tabla ÁlbumEval dada una inserción a Evaluación?"), como transición hacia el siguiente ejemplo de trigger más completo (evento distinto: inserción en vez de update).

## Slide 43
Título "Disparadores: Evento/Condición/Acción". Código SQL completo de un trigger más elaborado (estilo PL/pgSQL con bloque BEGIN/END):
```sql
CREATE TRIGGER ActualizarPM
  AFTER INSERT OR UPDATE ON Evaluación
  REFERENCING NEW ROW AS TN
    FOR EACH ROW
      BEGIN
        IF EXISTS
          ( SELECT * FROM ÁlbumEval A
            WHERE A.álbum = TN.álbum
            AND A.artista = TN.artista )
        THEN
          UPDATE ÁlbumEval
            SET pm = P.pmn, num=P.numn
            FROM (
              SELECT AVG(E.eval) AS pmn,
                    COUNT(E.eval) AS numn
              FROM Evaluación E
              WHERE E.álbum = TN.álbum
                    AND E.artista = TN.artista
            ) P;
        ELSE
          INSERT INTO ÁlbumEval
              (álbum, artista, pm, num)
            SELECT E.álbum, E.artista,
                AVG(E.eval) AS pmn,
                COUNT(E.eval) AS numn
            FROM Evaluación E
            WHERE E.álbum = TN.álbum
                AND E.artista = TN.artista;
      END IF;
    END;
```
Recuadro amarillo: "Actualizaciones atrasadas" (AFTER, no BEFORE). Pregunta al pie: "¿Qué pasaría si tuviéramos BEFORE INSERT …?"

## Slide 44
Slide "WARNING" (cartel amarillo). Texto: "Disparadores son estándares" (negro) y "¡Pero su implementación en varios motores varía muchísimo!" (rojo), subtexto: "Por ejemplo, Postgres usa 'stored procedures' …".

## Slide 45
Título "Disparadores en Postgres". Muestra que en Postgres el trigger requiere separar la lógica en una función/stored procedure y luego el trigger la referencia:
```sql
CREATE FUNCTION updatePm() RETURNS TRIGGER AS $$
BEGIN
  IF EXISTS
    ( SELECT * FROM ÁlbumEval A
      WHERE A.álbum = NEW.álbum
      AND A.artista = NEW.artista )
  THEN  UPDATE ÁlbumEval
      SET pm = P.pmn, num=P.numn
      FROM (
        SELECT AVG(E.eval) AS pmn,
          COUNT(E.eval) AS numn
        FROM Evaluación E
        WHERE E.álbum = NEW.álbum
        AND E.artista = NEW.artista
      ) P;
  ELSE
    INSERT INTO ÁlbumEval
      (álbum, artista, pm, num)
      SELECT E.álbum, E.artista,
        AVG(E.eval) AS pmn,
        COUNT(E.eval) AS numn
      FROM Evaluación E
      WHERE E.álbum = NEW.álbum
        AND E.artista = NEW.artista;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```
Etiquetado "Stored Procedure" (recuadro celeste). Debajo, en recuadro morado etiquetado "Trigger":
```sql
CREATE TRIGGER ActualizarPM
AFTER INSERT OR UPDATE ON Evaluación
FOR EACH ROW EXECUTE PROCEDURE updatePm();
```

## Slide 46
Título "Disparadores + Vistas Mat. en Postgres". Tres bloques de código apilados: (naranja, "Vista Mat.") `CREATE MATERIALIZED VIEW ÁlbumEval AS SELECT álbum, artista, FLOOR(AVG(eval)) AS pm, COUNT(eval) AS num FROM Evaluación GROUP BY álbum, artista`; (celeste, "Stored Procedure") `CREATE FUNCTION updateVMPm() RETURNS TRIGGER AS $$ BEGIN REFRESH MATERIALIZED VIEW ÁlbumEval; RETURN NEW; END; $$ LANGUAGE plpgsql;`; (morado, "Trigger") `CREATE TRIGGER ActualizarVmPM AFTER INSERT OR UPDATE ON Evaluación FOR EACH ROW EXECUTE PROCEDURE updateVmPm();`. Muestra el enfoque alternativo: en vez de actualizar fila por fila, se refresca toda la vista materializada.

## Slide 47
Título "Disparadores en Postgres". Comparación lado a lado ("VS" al centro) de los dos enfoques completos: izquierda = Vista Materializada + Stored Procedure con `REFRESH MATERIALIZED VIEW` + Trigger `ActualizarVmPM` (del slide 46); derecha = Stored Procedure `updatePm()` con lógica condicional IF EXISTS/UPDATE/INSERT + Trigger `ActualizarPM` (del slide 45).

## Slide 48
Repetición del slide 47 (mismo contenido) con recuadro añadido: pregunta "¿Cuál es la diferencia entre ambos?" → respuesta en amarillo: "La opción izquierda actualizará la vista entera cada vez." y "La opción derecha actualizará solo el álbum que cambió."

## Slide 49
Imagen decorativa (foto real, no diagrama técnico): un camión de la empresa "Shaffer Trucking" atascado bajo un puente bajo, con el eslogan pintado en el remolque "ON THE ROAD TO SUCCESS, THERE ARE NO SHORTCUTS." y "OUR MOST VALUABLE RESOURCE SITS 63 FEET AHEAD." — imagen humorística/meme de transición, sin relación técnica directa (marcada "decorativa").

## Slide 50
Slide separador: "RESUMEN" (texto azul, fondo blanco, sin más contenido).

## Slide 51
Título ausente (continuación de Resumen). Comparación de 4 sintaxis SQL lado a lado con "VS" al centro: arriba-izquierda `CREATE VIEW ÁlbumEval AS ...`; arriba-derecha `CREATE TABLE ÁlbumEval AS ...`; abajo-izquierda `CREATE MATERIALIZED VIEW ÁlbumEval AS ...`; abajo-derecha `CREATE TRIGGER ActualizarPM AFTER INSERT, UPDATE ON Evaluación REFERENCING NEW ROW AS TN FOR EACH ROW ...` — resumen visual de las 4 alternativas cubiertas en la clase.

## Slide 52
Tabla comparativa de resumen del curso, organizada en 4 cuadrantes con "VS" al centro:

| | Vistas | Tablas físicas (sin disparadores) |
|---|---|---|
| | No hay datos físicos | Hay que actualizarlas a mano |
| | • Más caro ejecutar consultas (rojo) | • Más barato ejecutar consultas (verde) |
| | • Los resultados no pueden ser obsoletos (verde) | • Los resultados pueden ser obsoletos (rojo) |
| | • Más barato actualizar tablas (verde) | |

| | Vistas materializadas | Tablas físicas (con disparadores) |
|---|---|---|
| | Las actualizaciones ejecutan a veces | Las actualizaciones ejecutan automáticamente |
| | • Más barato ejecutar consultas (verde) | • Más barato ejecutar consultas (verde) |
| | • Los resultados pueden ser obsoletos (rojo) | • Los resultados deberían ser actualizados (rojo) |
| | – (pero se puede usar un disparador con costo de actualización) | • Más caro actualizar tablas (rojo) |
| | • Poco portable (rojo) | • Agregan mucha complejidad (rojo) |
| | | • Poco portable (rojo) |

## Slide 53
Slide de cierre "Preguntas?" sobre fondo teal/verde azulado. Imagen decorativa de un bote a la deriva en un mar tormentoso texturizado con dígitos binarios (0 y 1), con un ícono de base de datos (cilindros dorados apilados) dentro del bote — metáfora de "navegar" el mar de datos.

## Slide 54
No presente / duplicado: el material fuente contiene 53 slides de imagen distintas correspondientes a las 54 numeradas del PDF (la slide 53 "Preguntas?" es la última imagen disponible, page-054.png). Se transcribió la totalidad de las 54 páginas de imagen provistas (page-001 a page-054); el contenido de cierre del capítulo es el slide "Preguntas?" descrito arriba.
