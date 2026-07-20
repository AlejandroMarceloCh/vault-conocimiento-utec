---
curso: BIGDATA
titulo: 12 - Semana 10/Actividad 10.1 PyMongo Básico
slides: 0
fuente: 12 - Semana 10/Actividad 10.1 PyMongo Básico.ipynb
---

<div id="69f2df6b-569e-4226-9beb-6ac697fd2bf9" class="cell markdown">

## **PyMongo: Manejo Básico**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div id="29b4e670-a07a-4f98-b5ab-1d46a4e3de88" class="cell markdown">

### 1. Instalación

</div>

<div id="2aba65c2-fece-4370-b03d-d52a9b001d4d" class="cell code">

``` python
#pip install pymongo
```

</div>

<div id="d11ffd1f-7012-4762-ab68-df32a4087701" class="cell code">

``` python
#Verificar versión
import pymongo
print(pymongo.__version__)
```

</div>

<div id="33deae91-4b14-48e0-9e0f-0dd92245e9ec" class="cell markdown">

### 2. Conexión a MongoDB

</div>

<div id="5fae3dce-15f1-4434-bd18-1cbe6e65b789" class="cell markdown">

MongoDB Local

</div>

<div id="048ecf68-3bcc-479c-8146-f6775f64d0cf" class="cell code">

``` python
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
```

</div>

<div id="50ce53d4-0115-48cb-b4ec-904e9ea72639" class="cell markdown">

### 3. Seleccionar Base de Datos

</div>

<div id="183f4748-44a7-45f1-ae82-feba36498eb8" class="cell markdown">

MongoDB crea la base automáticamente si no existe

</div>

<div id="014d3d22-6ace-47ce-8873-acade5697ed6" class="cell code">

``` python
db = client["banco"]
```

</div>

<div id="7738f091-acdd-45fb-9d62-b4afcce08d67" class="cell code">

``` python
clientes = db["clientes"]
```

</div>

<div id="af3ac6ba-40b9-43c8-92fe-66c021fcaf0c" class="cell markdown">

### 4. Seleccionar Colección

</div>

<div id="fcda5ecf-ba11-44d2-9f35-0fa0dd0bf296" class="cell markdown">

Equivale a una tabla SQL.

</div>

<div id="e92e5a8f-41b5-4973-b975-392e46e9b78b" class="cell code">

``` python
clientes = db["clientes"]
```

</div>

<div id="f9443651-dc2b-458b-b3cf-4eff29eae651" class="cell markdown">

### 5. Insertar Documentos

</div>

<div id="5eae52a6-84bc-48e8-bb00-4e3e4a11b772" class="cell markdown">

Insertar un documento

</div>

<div id="4673b6ee-50cf-429c-9f32-ad78e7683083" class="cell code">

``` python
cliente = {
    "nombre": "Juan",
    "edad": 35,
    "ingreso": 4500
}

resultado = clientes.insert_one(cliente)

print("ID insertado:", resultado.inserted_id)

doc = clientes.find_one({"_id": resultado.inserted_id})

print(doc)
```

</div>

<div id="53ac0f4b-ac33-46f3-93db-8af1a1f8ddf6" class="cell markdown">

Insertar varios documentos

</div>

<div id="a8ec789f-49e8-4730-b0ee-9a71d2cfede7" class="cell code">

``` python
lista_clientes = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Pedro", "edad": 42},
    {"nombre": "Luis", "edad": 30}
]

resultado = clientes.insert_many(lista_clientes)

print("IDs insertados:", resultado.inserted_ids)

# Recuperar los documentos insertados
for _id in resultado.inserted_ids:
    doc = clientes.find_one({"_id": _id})
    print(doc)
```

</div>

<div id="f34e2a14-efd9-4dc9-984b-983a4db1505b" class="cell markdown">

### 6. Consultas Básicas

</div>

<div id="e340bf48-662c-4b1e-89b3-5541cbd09a62" class="cell markdown">

Obtener todos los documentos

</div>

<div id="06bf1645-5a37-4ba6-a3cb-f52b325af85a" class="cell code">

``` python
for doc in clientes.find():
    print(doc)
```

</div>

<div id="96ef3db2-7be2-4ef8-b56e-7f22a52d26c6" class="cell markdown">

Obtener uno

</div>

<div id="7047d11c-e01e-4930-92bc-938322427130" class="cell code">

``` python
cliente = clientes.find_one()
print(cliente)
```

</div>

<div id="78633d4c-7e6f-47da-9ceb-115cb64e807c" class="cell markdown">

Filtrar

</div>

<div id="06d33c7a-f217-4c88-a7e1-587b70c0aef8" class="cell code">

``` python
filtrar = clientes.find({"edad":30})

for doc in filtrar:
    print(doc)
```

</div>

<div id="055a4a63-a530-4e66-98d4-419af14f69bd" class="cell markdown">

Convertir a lista

</div>

<div id="3c79589c-cf6e-44dc-beb4-aeb77e7425fc" class="cell code">

``` python
resultado = list(clientes.find({"edad":30}))

print(resultado)
```

</div>

<div id="b46d3016-7c01-42c6-81f8-9a6b45297d5d" class="cell markdown">

#### 7. Operadores de Comparación

</div>

<div id="65d4aad2-8564-4d2b-8c7d-1df2bc92b100" class="cell markdown">

Mayor que

</div>

<div id="a65fcfe8-d009-4c1b-a46a-c9b0843c2060" class="cell code">

``` python
filter1 = clientes.find({"edad":{"$gt":30}})

for doc in filter1:
    print(doc)
```

</div>

<div id="6315868d-2b19-4acd-acd3-48e6fdd24ed3" class="cell markdown">

Menor que

</div>

<div id="da6d6126-e4d8-4533-834d-414767d5394b" class="cell code">

``` python
filter2 = clientes.find({"edad":{"$lt":30}})

for doc in filter2:
    print(doc)
```

</div>

<div id="e380402e-f696-4a3c-ae5b-b14d87a4fa37" class="cell markdown">

Mayor o igual

</div>

<div id="42e9772f-1a56-4174-bd7a-8a7565fb8504" class="cell code">

``` python
filter3 = clientes.find({"edad":{"$gte":30}})

for doc in filter3:
    print(doc)
```

</div>

<div id="54a942f3-d99b-4eac-997c-f8bc2aa9b6c3" class="cell markdown">

Entre dos valores

</div>

<div id="2a0528bf-61cf-41e6-bba5-1f4afd4ab8f4" class="cell code">

``` python
filter4 = clientes.find({"edad":{"$gte":25,"$lte":40}})
for doc in filter4:
    print(doc)
```

</div>

<div id="ebdf33a0-bdd0-4794-987f-7af312941ec8" class="cell markdown">

### 8. Operadores Lógicos

</div>

<div id="bfd54bce-f96d-445b-81dd-eb2bc9937c01" class="cell markdown">

AND

</div>

<div id="5cc7caf5-bd73-4fa4-858f-44fc36fc0e77" class="cell code">

``` python
oplog1 = clientes.find({  "$and":[{"edad":{"$gt":25}},{"ingreso":{"$gt":3000}}] })
for doc in oplog1:
    print(doc)
```

</div>

<div id="3ea4601b-8bb2-4925-a7f7-74e679046282" class="cell markdown">

OR

</div>

<div id="e2f6171a-414f-4c5b-bf20-434e7528ef19" class="cell code">

``` python
oplog2 = clientes.find({"$or":[{"edad":25},{"edad":30}]})
for doc in oplog2:
    print(doc)
```

</div>

<div id="db8631b7-6cb3-4d9a-9833-aea200d3014e" class="cell markdown">

NOT

</div>

<div id="6607d9c3-b81a-47b1-932f-29d984bb67f9" class="cell code">

``` python
oplog3 = clientes.find({"edad":{"$not":{"$gt":40}}})
for doc in oplog3:
    print(doc)
```

</div>

<div id="6303f1c3-7cfb-466d-bc66-dadbec16877d" class="cell markdown">

### 9. Proyección (SELECT columnas)

</div>

<div id="a61c567c-8c32-4c5c-a9f1-a9ee9ebc932e" class="cell markdown">

Mostrar solo ciertos campos

</div>

<div id="1874d7fe-743d-4978-8edb-165834b91719" class="cell code">

``` python
selec1 = clientes.find({},{"_id":0,"nombre":1,"edad":1})

for doc in selec1:
    print(doc)
```

</div>

<div id="fd234ac2-9072-4c80-bbf7-0031082e2232" class="cell markdown">

### 10. Ordenamiento

</div>

<div id="c32ee5a5-80de-414a-8f29-db5c2d4ca3ef" class="cell code">

``` python
ord1 = clientes.find().sort("edad",1)

for doc in ord1:
    print(doc)
```

</div>

<div id="1a614915-5181-4614-abd6-647ff3ef6f68" class="cell code">

``` python
ord2 = clientes.find().sort("edad",-1)
for doc in ord2:
    print(doc)
```

</div>

<div id="3b050b9b-d25d-4828-924a-994af38b9175" class="cell markdown">

### 11. Limitar Registros

</div>

<div id="d12e05f0-3827-4c7b-85dc-176737405d4b" class="cell code">

``` python
lim1 = clientes.find().limit(2)
for doc in lim1:
    print(doc)
```

</div>

<div id="6acb365b-17ca-4e60-ae2b-da4f3f4ef1c3" class="cell markdown">

### 12. Saltar Registros

</div>

<div id="fa2283c0-9a1f-491e-a995-bc848dacdb6c" class="cell code">

``` python
sal1 = clientes.find().skip(2)
for doc in sal1:
    print(doc)
```

</div>

<div id="ac93a06a-7fbe-4778-b30f-7e5b339f5df1" class="cell markdown">

### 13. Actualizar Registros

</div>

<div id="f83b2039-3a0d-4537-a694-8c0cf5197c33" class="cell markdown">

update_one

</div>

<div id="723bb5fd-8bfb-41e3-974a-a68ae3626b78" class="cell code">

``` python
clientes.update_one({"nombre":"Juan"},{"$set":{"edad":36}})

for doc in clientes.find():
    print(doc)
```

</div>

<div id="55b44ecb-01f9-41b9-a58d-6c3610d8d3fc" class="cell markdown">

update_many

</div>

<div id="1ffe18d2-62bf-4e56-af15-cecbec120a02" class="cell code">

``` python
clientes.update_many({"edad":{"$lt":30}},{"$set":{"segmento":"Joven"}})

for doc in clientes.find():
    print(doc)
```

</div>

<div id="60009f94-8ed7-4af8-ab47-bbbecc5c1193" class="cell markdown">

Incrementar

</div>

<div id="3427bfcd-020a-4430-b1f3-b327988eafba" class="cell code">

``` python
clientes.update_one({"nombre":"Juan"},{"$inc":{"edad":1}})

for doc in clientes.find():
    print(doc)
```

</div>

<div id="e39b2314-c900-44cf-acfe-0959ff8dc057" class="cell markdown">

Agregar elemento a lista

</div>

<div id="b7b47040-f9fe-4cb4-b01c-fd6ce0157bd2" class="cell code">

``` python
clientes.update_one({"nombre":"Juan"},{"$push":{"productos":"Tarjeta"}})

for doc in clientes.find():
    print(doc)
```

</div>

<div id="d26e50dd-5d60-4b6d-83fc-b5f4503b9fbd" class="cell markdown">

### 14. Eliminar Registros

</div>

<div id="3812f2ea-4b03-49af-9cc3-077e2550a577" class="cell markdown">

Uno

</div>

<div id="8a1dda37-8b53-4fb6-a077-e58ad22ccc63" class="cell code">

``` python
clientes.delete_one({"nombre":"Juan"})

for doc in clientes.find():
    print(doc)
```

</div>

<div id="cae084ca-64fb-43b9-99c1-79df66f81322" class="cell markdown">

Varios

</div>

<div id="a8909276-b433-45de-a7ed-35f0b4c26dc3" class="cell code">

``` python
clientes.delete_many({"edad":{"$lt":29}})

for doc in clientes.find():
    print(doc)
```

</div>

<div id="a310a633-3492-4441-8447-68c6e5176740" class="cell markdown">

### 15. Contar Registros

</div>

<div id="5920e6b8-c387-4075-b4ef-eafcaf163476" class="cell code">

``` python
clientes.count_documents({"edad":{"$gt":30}})
```

</div>

<div id="e8324927-a48c-4ea7-9fa4-a4dd4f0635f1" class="cell markdown">

### 16. Búsquedas con Regex

</div>

<div id="0a27a778-2719-4e0c-9779-fccf4e815bbc" class="cell markdown">

Empieza con P

</div>

<div id="292e92c9-f64d-46c0-85a6-e8689358a833" class="cell code">

``` python
resultado = clientes.find({"nombre":{"$regex":"^P"}})

for doc in resultado:
    print(doc)
```

</div>

<div id="4770a1bb-3d7e-4e71-aaf8-1ee1f9633f82" class="cell markdown">

Contiene ui

</div>

<div id="fb3f3c06-63b4-429f-8f2e-ceeec31b603a" class="cell code">

``` python
resultado = clientes.find({"nombre":{"$regex":"ui"}})
for doc in resultado:
    print(doc)
```

</div>

<div id="9c689ef8-ca75-4bc9-94ec-b7795eae8010" class="cell markdown">

### 17. Trabajando con Fechas

</div>

<div id="7ba667a6-b7e2-422a-9228-260f6a19ade3" class="cell code">

``` python
from datetime import datetime

clientes.insert_one({"nombre":"Juan","fecha_registro":datetime.now()})

for doc in clientes.find():
    print(doc)
```

</div>

<div id="70b4686c-b55b-499f-b37e-b26c1a67dd62" class="cell markdown">

### 18. Consultar Fechas

</div>

<div id="4675981d-2bdd-4fae-be59-0d545475a05e" class="cell code">

``` python
from datetime import datetime

resultado = clientes.find({"fecha_registro": {"$gte": datetime(2026,1,1)}})

for doc in resultado:
    print(doc)
```

</div>
