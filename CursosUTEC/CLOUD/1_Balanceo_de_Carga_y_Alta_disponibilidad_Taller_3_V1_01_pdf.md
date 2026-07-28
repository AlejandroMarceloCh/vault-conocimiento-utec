---
curso: CLOUD
titulo: 1. Balanceo de Carga y Alta disponibilidad - Taller 3 - V1.01
slides: 23
fuente: 1. Balanceo de Carga y Alta disponibilidad - Taller 3 - V1.01.pdf
---

## Slide 1

Portada del taller (decorativa: logo UTEC en esquina superior derecha).

- **CS2032 - Cloud Computing (Ciclo 2024-1)**
- **Balanceo de Carga y Alta disponibilidad**
- Semana 7 - Taller 3: Balanceador de Carga
- Elaborado por: Geraldo Colchado

## Slide 2

Slide de contenido (tabla de índice) con barra lateral naranja "Contenido — Balanceador de Carga" y lista numerada de 7 puntos. Ítem 1 "Objetivo del taller 3" resaltado en negrita/subrayado (indica sección actual):

1. **Objetivo del taller 3**
2. Ejercicio 1: Crear contenedor de MongoDB en MV Bases de datos
3. Ejercicio 2: Crear contenedor de api-fruits con acceso a MongoDB en MV Desarrollo
4. Ejercicio 3: Desplegar contenedor api-fruits en 2 MV de producción
5. Ejercicio 4: Configurar y probar Balanceador de Carga
6. Ejercicio 5: Diagrama de Arquitectura de Solución
7. Cierre

## Slide 3

Título: "Objetivo del taller 3: Balanceador de Carga"

- Probar Balanceo de Carga y Alta disponibilidad con Api REST con acceso a base de datos MongoDB (NoSQL)

## Slide 4

Slide de contenido (mismo índice de 7 puntos que slide 2), ahora resaltado el ítem 2 "Ejercicio 1: Crear contenedor de MongoDB en MV Bases de datos" (sección actual).

## Slide 5

Título: "Ejercicio 1: Crear contenedor de MongoDB en MV Bases de datos"

- Paso 1: Ingrese a la máquina virtual "MV Bases de datos" por ssh a la IP Elástica
- Paso 2: Ejecute el contenedor de MongoDB:
```
$ docker run -d --rm --name mongo_c -p 27017:27017 -v mongo_data:/data/db mongo:latest
```
- Paso 3: Dado que el MongoDB se está ejecutando sin usuario y password (no tiene seguridad), sólo debe ser accedido por máquinas virtuales de la misma red local y no de internet, por lo que en el grupo de seguridad de la máquina virtual "MV Bases de datos" abra el puerto 27017 tanto para el mismo grupo de seguridad como para el grupo de seguridad de MV Desarrollo y MV Pruebas y para el grupo de seguridad de producción "GS-Prod".

**Captura de pantalla** (consola AWS, panel "Reglas de entrada (1/10)" de un Security Group) reproducida como tabla:

| Tipo | Protocolo | Intervalo de puertos | Origen |
|---|---|---|---|
| TCP personalizado | TCP | 8003 | 0.0.0.0/0 |
| TCP personalizado | TCP | 27017 | sg-0964e9fec1a1dbe9b / launch-wizard-... |
| TCP personalizado | TCP | 27017 | sg-009e76586e8ba8584 / GS-Prod |
| TCP personalizado | TCP | 8080 | 0.0.0.0/0 |

(Resaltado en amarillo: el título "Reglas de entrada", las dos filas del puerto 27017 y el texto "GS-Prod" y "launch-wizard-...", ilustrando las reglas que hay que agregar).

## Slide 6

Título: "Ejercicio 1: Crear contenedor de MongoDB en MV Bases de datos" (continuación)

Columna izquierda (pasos) y columna derecha (comandos de consola Mongo, en azul):

- Paso 4: Conectarse al linux del contenedor
```
$ docker exec -it mongo_c bash
```
- Paso 5: Conectarse al MongoDB
```
# mongosh
```
- Paso 6: Crear base de datos "food", colección "fruits", consultar datos y salir

Comandos mongosh (columna derecha):
```
use food

db.createCollection("fruits")

db.fruits.insertMany([ {name: "apple", origin: "usa", price: 5},
{name: "orange", origin: "italy", price: 3}, {name: "mango",
origin: "malaysia", price: 3} ])

db.fruits.find().pretty()

exit
exit
```

## Slide 7

Slide de contenido (mismo índice de 7 puntos), ahora resaltado el ítem 3 "Ejercicio 2: Crear contenedor de api-fruits con acceso a MongoDB en MV Desarrollo".

## Slide 8

Título: "Ejercicio 2: Crear contenedor de api-fruits con acceso a MongoDB en MV Desarrollo"

- Paso 1: En MV "MV Desarrollo" cree el directorio /home/ubuntu/api-fruits y copie por sftp o WinSCP los archivos indicados por el profesor.
- Paso 2: Analice el Dockerfile y app.py. En app.py reemplace por IP privada de su MV "MV Bases de datos" (resaltado en amarillo: "IP privada").

**Captura de código** (fragmento de app.py, fondo oscuro tipo editor, con una flecha roja manuscrita señalando la IP):
```python
class MongoAPI:
    def __init__(self, data):
        log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
        self.client = MongoClient("mongodb://172.31.92.214:27017") # IP privada de MV Base de Datos
        database = data['database']
        collection = data['collection']
```

- Paso 3: Cree la imagen
```
$ docker build -t api-fruits .
```

Pie de página: "Referencia del api-fruits: https://ishmeet1995.medium.com/how-to-create-restful-crud-api-with-python-flask-mongodb-and-docker-8f6ccb73c5bc"

## Slide 9

Título: "Ejercicio 2: Crear contenedor de api-fruits con acceso a MongoDB en MV Desarrollo" (continuación)

- Paso 4: Suba la imagen a https://hub.docker.com
  - Ingrese a https://hub.docker.com con su usuario
  - Cree un repositorio público con el nombre api-fruits
```
$ docker login -u gcolchado          (Reemplace amarillo)
$ docker tag api-fruits gcolchado/api-fruits   (Reemplace amarillo)
$ docker push gcolchado/api-fruits             (Reemplace amarillo)
$ docker logout
```
(el usuario "gcolchado" está resaltado en amarillo en cada línea, indicando que debe reemplazarse por el usuario propio de Docker Hub).

## Slide 10

Título: "Ejercicio 2: Crear contenedor de api-fruits con acceso a MongoDB en MV Desarrollo" (continuación)

- Paso 5: Ejecute el contenedor:
```
$ docker run -d --rm --name api-fruits_c -p 8001:8001 api-fruits
```
- Paso 6: Abra el puerto 8001 en el grupo de seguridad de MV "MV Desarrollo"
- Paso 7: Pruebe en postman o testfully el api-fruits con la IP de la MV "MV Desarrollo"

## Slide 11

Título: "Ejercicio 2: Crear contenedor de api-fruits con acceso a MongoDB en MV Desarrollo" (continuación)

**Dos capturas de pantalla de Postman lado a lado:**

Izquierda — "Consultar frutas": request `GET http://50.19.130.135:8001/mongodb` (URL resaltada amarillo), tab Body/raw/JSON con:
```json
{
  "database": "food",
  "collection": "fruits"
}
```
Respuesta (pretty JSON) devuelve el arreglo de frutas:
```json
[
  {"name": "apple", "origin": "usa", "price": 5},
  {"name": "orange", "origin": "italy", "price": 3},
  {"name": "mango", "origin": "malaysia", "price": 3}
]
```

Derecha — "Crear fruta": request `POST http://50.19.130.135:8001/mongodb` (método y URL resaltados amarillo), Body/raw/JSON:
```json
{
  "database": "food",
  "collection": "fruits",
  "Document": {"name": "pear", "origin": "usa", "price": 10}
}
```
Respuesta:
```json
{
  "Document_ID": "63323ea48059a314f0c91ec8",
  "Status": "Successfully Inserted"
}
```

## Slide 12

Título: "Ejercicio 2: Crear contenedor de api-fruits con acceso a MongoDB en MV Desarrollo" (continuación)

**Dos capturas de pantalla de Postman lado a lado:**

Izquierda — "Modificar fruta": request `PUT http://50.19.130.135:8001/mongodb`, Body/raw/JSON:
```json
{
  "database": "food",
  "collection": "fruits",
  "Filter": {"name": "pear"},
  "DataToBeUpdated": {"origin": "peru", "price": 11.5}
}
```
Respuesta: `{"Status": "Successfully Updated"}`

Derecha — "Eliminar fruta": request `DELETE http://50.19.130.135:8001/mongodb`, Body/raw/JSON:
```json
{
  "database": "food",
  "collection": "fruits",
  "Filter": {"name": "pear"}
}
```
Respuesta: `{"Status": "Successfully Deleted"}`

## Slide 13

Slide de contenido (mismo índice de 7 puntos), ahora resaltado el ítem 4 "Ejercicio 3: Desplegar contenedor api-fruits en 2 MV de producción".

## Slide 14

Título: "Ejercicio 3: Desplegar contenedor api-fruits en 2 MV de producción"

- Paso 1: Ingrese por ssh y ejecute el contenedor en las 2 MV de producción
```
$ docker run -d --rm --name api-fruits_c -p 8001:8001 gcolchado/api-fruits
```

## Slide 15

Slide de contenido (mismo índice de 7 puntos), ahora resaltado el ítem 5 "Ejercicio 4: Configurar y probar Balanceador de Carga".

## Slide 16

Título: "Ejercicio 4: Configurar y probar Balanceador de Carga"

- Paso 1: En grupo de seguridad "GS-Prod", que usan las 2 MV de producción, abra puerto 8001
- Paso 2: Crear un Target Group con las 2 MV de producción para el puerto 8001

**Captura de pantalla** (consola AWS, formulario de creación de Target Group), campos resaltados en amarillo:
- Target group name: `TG-Prod-8001`
- Protocol: `HTTP`  Port: `8001`

## Slide 17

Título: "Ejercicio 4: Configurar y probar Balanceador de Carga" (continuación)

- Paso 3: Agregue un agente de escucha en el Balanceador de Carga

**Captura de pantalla** (consola AWS, panel "lb-prod | Agregar agente de escucha"):
- Protocolo - Puerto: `HTTP` : `8001` (resaltado amarillo)
- Acciones predeterminadas → "1. Reenviar a..." → Grupo de destino: peso (0-999): `TG-Prod-8001` (resaltado amarillo), peso `1`, Distribución del tráfico `100%`

## Slide 18

Título: "Ejercicio 4: Configurar y probar Balanceador de Carga" (continuación)

- Paso 4: Pruebe en postman el balanceador de carga varias veces.
- Paso 5: Detener la instancia "MV Prod 1" y probar
- Paso 6: Detener la instancia "MV Prod 2" y probar
- Paso 7: Iniciar la instancia "MV Prod 1", ejecutar el contenedor y probar
```
$ docker run -d --rm --name api-fruits_c -p 8001:8001 gcolchado/api-fruits
```
- Paso 8: Iniciar la instancia "MV Prod 2", ejecutar el contenedor y probar
```
$ docker run -d --rm --name api-fruits_c -p 8001:8001 gcolchado/api-fruits
```

**Captura de pantalla de Postman** (derecha): request `GET http://lb-prod-1556863965.us-east-1.elb.amazonaws.com:8001/mongodb` (URL del balanceador de carga resaltada en amarillo), Body/raw/JSON:
```json
{
  "database": "food",
  "collection": "fruits"
}
```
Respuesta (pretty) con el arreglo de frutas (apple/orange/mango con origin y price), confirmando que el balanceador reenvía correctamente al backend con acceso a MongoDB.

## Slide 19

Slide de contenido (mismo índice de 7 puntos), ahora resaltado el ítem 6 "Ejercicio 5: Diagrama de Arquitectura de Solución".

## Slide 20

Título: "Ejercicio 5: Diagrama de Arquitectura de Solución"

- Paso 1: Elabore en draw.io el Diagrama de Arquitectura de Solución del Api REST con acceso a base de datos MongoDB balanceada en carga usando el puerto 8001. Publique su diagrama en el padlet.

Slide solo de texto/instrucción, sin diagrama incluido (el diagrama es tarea a elaborar por el alumno).

## Slide 21

Slide de contenido (mismo índice de 7 puntos), ahora resaltado el ítem 7 "Cierre".

## Slide 22

Título: "Cierre: Balanceador de Carga - Qué aprendimos?"

- Balanceo de Carga y Alta disponibilidad con Api REST con acceso a base de datos MongoDB (NoSQL)

## Slide 23

Slide final de agradecimiento (decorativa): "Gracias" — "Elaborado por docente: Geraldo Colchado".
