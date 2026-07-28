---
curso: CLOUD
titulo: 1. Balanceo de Carga y Alta disponibilidad - Taller 2 - V1.10
slides: 24
fuente: 1. Balanceo de Carga y Alta disponibilidad - Taller 2 - V1.10.pdf
---

## Slide 1

Portada del curso (decorativa: logo UTEC en esquina superior derecha).

- **CS2032 - Cloud Computing (Ciclo 2024-1)**
- **Balanceo de Carga y Alta disponibilidad**
- Semana 6 - Taller 2: Balanceador de Carga
- Elaborado por: Geraldo Colchado

## Slide 2

Slide de contenido/agenda (barra lateral naranja "Contenido / Balanceador de Carga"). Lista numerada de temas del taller:

1. Objetivo del taller 2 (resaltado en negrita/subrayado como sección activa)
2. Ejercicio 1: Crear imagen de api-employees con acceso a BD MySQL en MV desarrollo
3. Ejercicio 2: Desplegar contenedor api-employees en 2 MV de producción
4. Ejercicio 3: Configurar y probar Balanceador de Carga
5. Ejercicio 4: Diagrama de Arquitectura de Solución
6. Cierre

## Slide 3

Título: "Objetivo del taller 2: Balanceador de Carga"

- Probar Balanceo de Carga y Alta disponibilidad con Api REST con acceso a base de datos MySQL

## Slide 4

Slide de contenido/agenda (misma lista que Slide 2), con el ítem 2 "Ejercicio 1: Crear imagen de api-employees con acceso a BD MySQL en MV desarrollo" resaltado en negrita/subrayado como sección activa.

## Slide 5

Título: "Ejercicio 1: Crear imagen de api-employees con acceso a BD MySQL en MV desarrollo"

- Paso 1: En MV "MV desarrollo" cree el directorio /home/ubuntu/api-employees y copie por sftp o WinSCP o git clone los archivos indicados por el profesor.
- Paso 2: Analice el Dockerfile y main.py
- Paso 3: Cree la imagen

```
$ docker build -t api-employees .
```

Pie de página (barra naranja): Referencia del api-employees: https://techwasti.com/fastapi-mysql-simple-rest-api-example

## Slide 6

Título: "Ejercicio 1: Crear imagen de api-employees con acceso a BD MySQL en MV desarrollo"

- Paso 4: Suba la imagen a https://hub.docker.com. Ingrese a https://hub.docker.com con su usuario. Cree un repositorio público con el nombre api-employees.

```
$ docker login -u gcolchado                          (Reemplace amarillo)
$ docker tag api-employees gcolchado/api-employees    (Reemplace amarillo)
$ docker push gcolchado/api-employees                 (Reemplace amarillo)
$ docker logout
```

Nota visual: en la slide, "gcolchado" aparece resaltado en amarillo en cada línea de comando, indicando que el alumno debe reemplazarlo por su propio usuario de Docker Hub.

## Slide 7

Título: "Ejercicio 1: Crear imagen de api-employees con acceso a BD MySQL en MV desarrollo"

- **Paso 5: Cree la BD y Tabla en MySQL**
- Ingrese por ssh a la MV "MV Bases de Datos" y ejecute los 2 contenedores:

```
$ docker run -d --rm --name mysql_c -e MYSQL_ROOT_PASSWORD=utec -p 8005:3306 -v mysql_data:/var/lib/mysql mysql:8.0
$ docker run -d --rm --name adminer_c -p 8080:8080 adminer
```

- Ingrese a adminer y ejecute el script de base de datos entregado por el profesor:

```sql
DROP DATABASE IF EXISTS bd_api_employees;
CREATE DATABASE bd_api_employees CHARSET utf8mb4;
USE bd_api_employees;

CREATE TABLE employees (
   id INT(11) NOT NULL AUTO_INCREMENT,
   name VARCHAR(100) NOT NULL,
   age INT(11) NOT NULL,
   PRIMARY KEY (id)
);

INSERT INTO employees(name, age) VALUES('Jake', 21);
INSERT INTO employees(name, age) VALUES('Mathew', 24);
INSERT INTO employees(name, age) VALUES('Bob', 35);
commit;
```

## Slide 8

Slide de contenido/agenda (misma lista), con el ítem 3 "Ejercicio 2: Desplegar contenedor api-employees en 2 MV de producción" resaltado en negrita/subrayado como sección activa.

## Slide 9

Título: "Ejercicio 2: Desplegar contenedor api-employees en 2 MV de producción"

- Paso 1: Ingrese por ssh y ejecute el contenedor en las 2 MV de producción

```
$ docker run -d --rm --name api-employees_c -p 8000:8000 gcolchado/api-employees
```

## Slide 10

Slide de contenido/agenda (misma lista), con el ítem 4 "Ejercicio 3: Configurar y probar Balanceador de Carga" resaltado en negrita/subrayado como sección activa.

## Slide 11

Título: "Ejercicio 3: Configurar y probar Balanceador de Carga"

- Paso 1: En grupo de seguridad "GS-Prod", que usan las 2 MV de producción, abra puerto 8000
- Paso 2: Crear un Target Group con las 2 MV de producción para el puerto 8000

Captura de pantalla (consola AWS, formulario de creación de Target Group):
- Campo "Target group name": `TG-Prod-8000` (resaltado en amarillo)
- Campo "Protocol": `HTTP` (resaltado en amarillo) — "Port": `8000` (resaltado en amarillo)
- Nota debajo del nombre: "A maximum of 32 alphanumeric characters includi[ng...]" (texto cortado en la imagen)

## Slide 12

Título: "Ejercicio 3: Configurar y probar Balanceador de Carga"

- Paso 3: Agregue un agente de escucha en el Balanceador de Carga

Captura de pantalla (consola AWS en español, formulario "lb-prod | Agregar agente de escucha"):
- Texto: "Los agentes de escucha pertenecientes a balanceadores de carga de aplicac[ión]... escucha debe incluir una acción predeterminada para garantizar que se enru[te el]... direccionamiento adicionales que necesite. Más información" (texto cortado a la derecha en la captura)
- Sección "Protocolo - Puerto": `HTTP` : `8000` (ambos resaltados en amarillo)
- Sección "Acciones predeterminadas": "1. Reenviar a..." con ícono de papelera
  - "Grupo de destino: peso (0-999)": `TG-Prod-8000` (resaltado en amarillo), peso `1`, con ícono X para eliminar
  - "Distribución del tráfico: 100%"

## Slide 13

Título: "Ejercicio 3: Configurar y probar Balanceador de Carga"

- Paso 4: Consulte la documentación del api

Captura de pantalla (navegador mostrando Swagger UI de FastAPI):
- Barra de dirección: `lb-prod-1845552211.us-east-1.elb.amazonaws.com:8000/docs` (con ":8000/docs" resaltado en amarillo), indicador "No es seguro"
- Título de la página: "FastAPI 0.1.0 OAS 3.1", enlace `/openapi.json`
- Sección "default" con lista de endpoints (tabla de rutas):

| Método | Ruta | Descripción |
|---|---|---|
| GET | /employees | Get Employees |
| POST | /employees | Add Employee |
| GET | /employees/{id} | Get Employee |
| PUT | /employees/{id} | Update Employee |
| DELETE | /employees/{id} | Delete Employee |

(cada fila con badge de color: GET=azul, POST=verde, PUT=naranja, DELETE=rojo, todos con flecha desplegable a la derecha)

## Slide 14

Título: "Ejercicio 3: Configurar y probar Balanceador de Carga"

- Paso 5: Pruebe en postman el api-employees con el enlace del balanceador

Slide es de transición/instrucción, sin captura adicional (el texto del paso es el único contenido visible).

## Slide 15

Título: "Ejercicio 3: Configurar y probar Balanceador de Carga"

Dos capturas de pantalla de Postman lado a lado, probando el endpoint GET a través del balanceador:

**Izquierda — "Consultar empleados" (GET /employees):**
- URL: `http://lb-prod-1845552211.us-east-1.elb.amazonaws.com:8000/employees` (":8000/employees" resaltado en amarillo)
- Respuesta 200 OK, JSON:
```json
{
    "employees": [
        [1, "Juan Pérez", 30],
        [2, "Mathew", 24],
        [3, "Bob", 35]
    ]
}
```

**Derecha — "Consulta un empleado" (GET /employees/1):**
- URL: `http://lb-prod-1845552211.us-east-1.elb.amazonaws.com:8000/employees/1` (":8000/employees/1" resaltado en amarillo)
- Respuesta 200 OK, JSON:
```json
{
    "employee": [1, "Juan Pérez", 30]
}
```

## Slide 16

Título: "Ejercicio 3: Configurar y probar Balanceador de Carga"

Captura de pantalla de Postman — "Nuevo empleado" (POST /employees):
- URL: `http://lb-prod-1845552211.us-east-1.elb.amazonaws.com:8000/employees` (método POST y ":8000/employees" resaltados en amarillo)
- Body (raw, JSON):
```json
{
  "name": "Juan Pérez",
  "age": 25
}
```
- Respuesta 200 OK (582 ms), JSON:
```json
{
    "message": "Employee added successfully"
}
```

## Slide 17

Título: "Ejercicio 3: Configurar y probar Balanceador de Carga"

Captura de pantalla de Postman — "Modificar empleado" (PUT /employees/1):
- URL: `http://lb-prod-1845552211.us-east-1.elb.amazonaws.com:8000/employees/1` (método PUT y ":8000/employees/1" resaltados en amarillo)
- Body (raw, JSON):
```json
{
  "name": "Jorge Carrasco",
  "age": 19
}
```
- Respuesta 200 OK (363 ms), JSON:
```json
{
    "message": "Employee modified successfully"
}
```

## Slide 18

Sin título de sección visible (continuación de Ejercicio 3). Captura de pantalla de Postman — "Eliminar empleado" (DELETE /employees/15):
- URL: `http://lb-prod-1845552211.us-east-1.elb.amazonaws.com:8000/employees/15` (":8000/employees/15" resaltado en amarillo)
- Respuesta 200 OK (4.92 ms), JSON:
```json
{
    "message": "Employee deleted successfully"
}
```

## Slide 19

Título: "Ejercicio 3: Configurar y probar Balanceador de Carga"

- Paso 6: Detener la instancia "MV Prod 1" y probar
- Paso 7: Detener la instancia "MV Prod 2" y probar
- Paso 8: Iniciar la instancia "MV Prod 1", ejecutar el contenedor y probar

```
$ docker run -d --rm --name api-employees_c -p 8000:8000 gcolchado/api-employees
```

- Paso 9: Iniciar la instancia "MV Prod 2", ejecutar el contenedor y probar

```
$ docker run -d --rm --name api-employees_c -p 8000:8000 gcolchado/api-employees
```

(El propósito de estos pasos es demostrar la alta disponibilidad: apagar cada instancia detrás del balanceador y verificar que el servicio sigue disponible mientras al menos una MV esté activa.)

## Slide 20

Slide de contenido/agenda (misma lista), con el ítem 5 "Ejercicio 4: Diagrama de Arquitectura de Solución" resaltado en negrita/subrayado como sección activa.

## Slide 21

Título: "Ejercicio 4: Diagrama de Arquitectura de Solución"

- Paso 1: Elabore en draw.io el Diagrama de Arquitectura de Solución del Api REST con acceso a base de datos MySQL balanceada en carga usando el puerto 8000. Publique su diagrama en el padlet. Este ejercicio es guiado.

(No se incluye un diagrama de ejemplo en la slide; el ejercicio pide al alumno elaborarlo por su cuenta en draw.io.)

## Slide 22

Slide de contenido/agenda (misma lista), con el ítem 6 "Cierre" resaltado en negrita/subrayado como sección activa.

## Slide 23

Título: "Cierre: Balanceador de Carga - Qué aprendimos?"

- Balanceo de Carga y Alta disponibilidad con Api REST con acceso a base de datos MySQL

## Slide 24

Slide de cierre (decorativa, solo texto centrado):

- "Gracias"
- "Elaborado por docente: Geraldo Colchado"
