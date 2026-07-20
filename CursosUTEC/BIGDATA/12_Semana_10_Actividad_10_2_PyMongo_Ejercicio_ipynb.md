---
curso: BIGDATA
titulo: 12 - Semana 10/Actividad 10.2 PyMongo Ejercicio
slides: 0
fuente: 12 - Semana 10/Actividad 10.2 PyMongo Ejercicio.ipynb
---

<div id="4bb3ded4-f21e-4948-9ba6-67c133ff82af" class="cell markdown">

## **PyMongo desde cero: conexión, consultas y operadores lógicos**

- Curso: Big Data
- Docente: Aldo Lezama Benavides

</div>

<div id="a45e279d-6db9-4367-b389-8d918187d90d" class="cell markdown">

### Conexión y uso de librería pymongo

</div>

<div id="0e172aff-4915-4379-8ed1-5213b4f5a799" class="cell code">

``` python
pip install pymongo
```

</div>

<div id="2ea58ef8-b4f2-4ddc-ab7b-93a4c928eeaa" class="cell code">

``` python
from pymongo import MongoClient
```

</div>

<div id="1f2da046-5ac6-40ac-b1ae-7d57840618c6" class="cell code">

``` python
client = MongoClient(host='localhost',port=27017)
```

</div>

<div id="007b509e-0f15-4fad-911d-cf88c8e433fa" class="cell code">

``` python
db = client['demo']
```

</div>

<div id="ec78e688-5129-43a6-848d-f0527d13cb89" class="cell code">

``` python
clientes = db ['clientes']
productos = db ['productos']
ventas = db ['ventas']
```

</div>

<div id="8954568a-6461-4f52-9936-b3d10f8d6d4b" class="cell markdown">

### Consulta de todos los registros

</div>

<div id="c11d1648-6a0a-400b-afd0-277dac8e9f01" class="cell code">

``` python
for document in clientes.find():
    print(document)
```

</div>

<div id="2196aa58-de61-4374-897e-c428a02d867d" class="cell markdown">

### Insertar Registros

</div>

<div id="816d3d50-398b-4ff3-8905-a7b50a97f143" class="cell code">

``` python
registro = { "nombre": "Tania", "edad": 36, "ciudad": "Chiclayo", "ingresos": 7500 }
clientes.insert_one(registro)
```

</div>

<div id="0530cae2-7c51-407e-9626-0da704f7e781" class="cell code">

``` python
clientes.insert_many([
    { "nombre": "Zuleika", "edad": 35, "ciudad": "Chiclayo", "ingresos": 8000 },
    { "nombre": "Irma", "edad": 27, "ciudad": "Huancavelica", "ingresos": 7000 }
])
```

</div>

<div id="0d5f39e4-7ed8-47cd-9981-f3404496a56d" class="cell markdown">

### Filtros

</div>

<div id="ce72a82e-cb25-4056-9436-987863b9d80b" class="cell code">

``` python
for doc in clientes.find({"ciudad": "Chiclayo"}):
    print(doc)
```

</div>

<div id="b90435d4-9abd-41b8-865f-a7e3ce152517" class="cell markdown">

### Selección de Campos

</div>

<div id="563a26c2-1da1-494b-9850-47b7343d266d" class="cell code">

``` python
for doc in clientes.find({}, {"_id": 0, "nombre": 1, "ciudad": 1}):
    print(doc)
```

</div>

<div id="7fbd9997-4b57-4e08-ba23-fc8d36ecd1c9" class="cell markdown">

### Conteo de Número de Registros

</div>

<div id="09b5e090-ea1d-49f5-8d22-80ce0b6c7e07" class="cell code">

``` python
print(ventas.count_documents({}))
```

</div>

<div id="12df2988-3df3-442b-a933-486efca63242" class="cell markdown">

### Ordenamiento

</div>

<div id="fe4a986d-cff8-4ae1-872a-a452c51ce718" class="cell code">

``` python
for doc in productos.find().sort("precio", -1):  # 1 = ascendente ; -1 = descendente
    print(doc)
```

</div>

<div id="b1be84d4-88f5-4d1f-81f7-bc8a14790bb7" class="cell code">

``` python
for doc in productos.find().sort("precio", 1):  # 1 = ascendente ; -1 = descendente
    print(doc)
```

</div>

<div id="9973d31f-dba9-4571-88c3-bebe1cbc44d1" class="cell markdown">

### Operadores de Comparación

</div>

<div id="3893c65d-7e4d-4f81-a34f-3a6407e1c18b" class="cell markdown">

------------------------------------------------------------------------

| **Operador** | **Significado** | **Ejemplo** | **Descripción** |
|----|----|----|----|
| `$eq` | Igual a (=) | `{"edad": {"$eq": 30}}` | Busca documentos donde `edad` sea igual a 30 |
| `$ne` | No igual a (≠) | `{"ciudad": {"$ne": "Lima"}}` | Excluye los documentos con `ciudad = Lima` |
| `$gt` | Mayor que (\>) | `{"ingresos": {"$gt": 5000}}` | Busca ingresos mayores a 5000 |
| `$gte` | Mayor o igual (≥) | `{"edad": {"$gte": 40}}` | Busca edad mayor o igual a 40 |
| `$lt` | Menor que (\<) | `{"edad": {"$lt": 30}}` | Busca edad menor que 30 |
| `$lte` | Menor o igual (≤) | `{"edad": {"$lte": 25}}` | Busca edad menor o igual a 25 |
| `$in` | Está dentro de una lista | `{"ciudad": {"$in": ["Lima", "Arequipa"]}}` | Coincide si `ciudad` está en la lista |
| `$nin` | No está dentro de una lista | `{"ciudad": {"$nin": ["Lima", "Cusco"]}}` | Excluye esas ciudades |

------------------------------------------------------------------------

</div>

<div id="ba0170ce-8215-44bb-a3e6-d3a9a6394138" class="cell code">

``` python
for doc in clientes.find({"ingresos": {"$gt": 5000}}):
    print(doc)
```

</div>

<div id="fd1f1404-29ee-4c85-8258-d3d03304ee80" class="cell code">

``` python
for doc in clientes.find({"ingresos": {"$lte": 8000}}):
    print(doc)
```

</div>

<div id="e3ddb705-6946-4aa4-96a2-77ef416eb88e" class="cell markdown">

### Operadores Lógicos

</div>

<div id="ab5e7825-4772-455f-9737-ff13d4ea1737" class="cell markdown">

------------------------------------------------------------------------

| **Operador** | **Ejemplo** | **Descripción** |
|----|----|----|
| `$and` | `{"$and": [{"edad": {"$gt": 30}}, {"ciudad": "Lima"}]}` | Cumple ambas condiciones |
| `$or` | `{"$or": [{"edad": {"$lt": 25}}, {"ingresos": {"$gt": 7000}}]}` | Cumple al menos una condición |
| `$not` | `{"edad": {"$not": {"$gte": 30}}}` | Niega una condición |
| `$nor` | `{"$nor": [{"ciudad": "Lima"}, {"ciudad": "Cusco"}]}` | No cumple ninguna de las condiciones |

------------------------------------------------------------------------

</div>

<div id="41dfc66a-4fa2-4848-9416-73a74ae2088e" class="cell code">

``` python
for document in productos.find():
    print(document)
```

</div>

<div id="fa231e4e-f6a2-414d-976a-649c32befe9e" class="cell code">

``` python
consulta = {
    "$and": [
        {"categoria": "Tecnología"},
        {"precio": {"$gt": 1000}}
    ]
}

for doc in productos.find(consulta, {"_id": 0, "producto": 1, "categoria": 1, "precio": 1, "stock": 1}):
    print(doc)
```

</div>

<div id="d77252bd-8b12-4e89-bfcc-f85f0fcc57aa" class="cell code">

``` python
consulta = {
    "$or": [
        {"categoria": "Tecnología"},
        {"stock": {"$gt": 10}}
    ]
}

for doc in productos.find(consulta, {"_id": 0, "producto": 1, "categoria": 1, "precio": 1, "stock": 1}):
    print(doc)
```

</div>

<div id="16b1815d-4347-4762-af51-4a52135a9271" class="cell markdown">

### Eliminación

</div>

<div id="e15fe24d-e47f-4810-9541-1642e468af60" class="cell code">

``` python
for document in clientes.find():
    print(document)
```

</div>

<div id="cc18f578-1681-4768-95aa-f12722770f5e" class="cell code">

``` python
clientes.delete_one({"nombre": "Tania"})
```

</div>

<div id="07fe681e-6c9c-4d3b-a324-4fef56d77802" class="cell code">

``` python
for document in clientes.find():
    print(document)
```

</div>

<div id="2dda999b-8c01-4d76-a7ee-07039e6973fb" class="cell markdown">

### Cerrar Conexión

</div>

<div id="032fa37e-ab9b-4973-a10f-96f04a7a1f05" class="cell code">

``` python
client.close()
```

</div>

<div id="70582490-c5d3-479b-a429-cbea2700650a" class="cell code">

``` python
```

</div>
