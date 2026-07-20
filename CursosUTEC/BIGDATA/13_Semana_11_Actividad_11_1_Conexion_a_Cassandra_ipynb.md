---
curso: BIGDATA
titulo: 13 - Semana 11/Actividad 11.1 Conexión_a_Cassandra
slides: 0
fuente: 13 - Semana 11/Actividad 11.1 Conexión_a_Cassandra.ipynb
---

<div id="KILlZGwcXH7M" class="cell markdown" id="KILlZGwcXH7M">

## **Python con Cassandra**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div id="6cf5f465-65ab-4689-82a2-09ba7b1c0698" class="cell code" id="6cf5f465-65ab-4689-82a2-09ba7b1c0698">

``` python
from cassandra.cluster import Cluster

cluster = Cluster(['host.docker.internal'], port=9042)
session = cluster.connect()
print("Conectado correctamente a Cassandra")

rows = session.execute("SELECT release_version FROM system.local")
for row in rows:
    print("Versión Cassandra:", row.release_version)
```

</div>

<div id="8417be24-e424-4917-bb4e-bd09cdc7bc0c" class="cell code" id="8417be24-e424-4917-bb4e-bd09cdc7bc0c">

``` python
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS universidad
    WITH REPLICATION = {
        'class': 'SimpleStrategy',
        'replication_factor': 1
    }
""")
print("Keyspace 'universidad' creado o ya existente")

# Seleccionar el keyspace
session.set_keyspace('universidad')
```

</div>

<div id="59fc1758-77da-46a7-87ca-7bd959515fb5" class="cell code" id="59fc1758-77da-46a7-87ca-7bd959515fb5">

``` python
# Tabla de estudiantes
session.execute("""
    CREATE TABLE IF NOT EXISTS estudiante (
        id INT PRIMARY KEY,
        nombre TEXT,
        carrera TEXT,
        edad INT,
        ciudad TEXT
    )
""")
print("Tabla 'estudiante' creada")
```

</div>

<div id="c2034cb5-2151-4110-befc-402ab6383339" class="cell code" id="c2034cb5-2151-4110-befc-402ab6383339">

``` python
# =============================================
# Insertar algunos datos
# =============================================

session.execute("""
    INSERT INTO estudiante (id, nombre, carrera, edad, ciudad)
    VALUES (1, 'Aldo Lezama', 'Ingeniería Industrial', 28, 'Lima')
""")

session.execute("""
    INSERT INTO curso (codigo, nombre, creditos)
    VALUES ('BD101', 'Base de Datos', 3)
""")

session.execute("""
    INSERT INTO matricula (id_estudiante, codigo_curso, semestre, nota)
    VALUES (1, 'BD101', '2025-1', 17.5)
""")

print("Registros insertados correctamente")
```

</div>

<div id="7e9a277b-e07c-4019-83cf-1a220c68c5e4" class="cell code" id="7e9a277b-e07c-4019-83cf-1a220c68c5e4">

``` python
# =============================================
# Consultar datos
# =============================================
rows = session.execute("SELECT * FROM estudiante")
print("\n Estudiantes registrados:")
for row in rows:
    print(row)

rows = session.execute("SELECT * FROM curso")
print("\n Cursos registrados:")
for row in rows:
    print(row)

rows = session.execute("SELECT * FROM matricula")
print("\n Matrículas registradas:")
for row in rows:
    print(row)
```

</div>

<div id="d556f1dd-1d63-423d-bb00-f12706edb86f" class="cell code" id="d556f1dd-1d63-423d-bb00-f12706edb86f">

``` python
# =============================================
# Cerrar conexión
# =============================================
cluster.shutdown()
```

</div>
