---
curso: INGSOFT
titulo: 09 - Semana 7/IS1 - Aula 7 - Del diseño al desarrollo__pptx
slides: 8
fuente: 09 - Semana 7/IS1 - Aula 7 - Del diseño al desarrollo__pptx.pdf
---

## Slide 1

Portada (decorativa: fondo de túnel tecnológico azul con silueta de robot humanoide).

**Ingeniería de Software**

Profesor Christian Paz

## Slide 2

Título: **Desarrollo de Software**

Diagrama de línea de tiempo horizontal con 6 fases, cada una representada por un ícono circular azul conectado por una línea amarilla con puntos, y debajo una tarjeta con etiqueta y descripción:

| Fase (ícono) | Descripción |
|---|---|
| **Análisis** (diana/blanco) | ¿Qué debe hacer el software? |
| **Diseño** (lupa) | ¿Cómo se hará el software? |
| **Implementación** (cohete) | Hacer el Software. |
| **Pruebas** (calendario con checks) | El software hace lo que se supone que debe hacer? |
| **Despliegue** (cohete despegando) | Entregar, poner en marcha. |
| **Mantenimiento** (eslabones de cadena) | El software funciona, pero le falta esto, o está lento, o necesita mejorar esto. |

## Slide 3

Portada de sección (decorativa: imagen de mano robótica tocando un globo terráqueo digital).

**1. Del Diseño al Desarrollo**

(Ícono de portapapeles/checklist junto al título.)

## Slide 4

Título: **Salida del Diseño**

- **Diseño de Arquitectura:**
  - Componentes del Software y como se comunican.
  - Tecnologías a utilizar.
- **Diseño Estructural**
  - Qué entidades y atributos vamos a manipular.
- **Diseño de Interacción**
  - Cómo se van a ejecutar los principales procesos.

## Slide 5

Título: **Ejemplo: Venta de Entradas de Cine**

- Salida del Análisis: Requerimientos y Casos de Uso
- Restricción: Local único y sin confitería

Enlace: https://drive.google.com/file/d/1jY_S1PHpMIQBTENt9hcYRdkVaKHjWHOs/view?usp=sharing

## Slide 6

Título: **Actividad EC2: Diseño Detallado y de APIs**

Basado en su app de conversión de monedas, realizar un diseño detallado:

- Revisar los requerimientos y casos de uso.
- Revisar la arquitectura propuesta.
- Modelar las entidades a utilizar.
- Listar las APIs que serán expuestas por cada microservicio.

## Slide 7

Título: **Cómo comenzar a programar?**

Texto (parcialmente cubierto por el diagrama):

- Para cada componente (frontend o backend), crear los repositorios de software asociados.
- Crear los puntos de interacción (APIs) entre los componentes identificando sus entradas/salidas.
- Crear las entidades que nos permitirán la conexión entre los componentes.

Ejemplo de API:

```
API: GET /listing/{id_local}/movies?dia=2024-09-30
[
  { "name": "Transformers uno", "room": "Sala 1", "horaInicio": "19:00" }
]
```

**Diagrama de arquitectura** (recuadro a la derecha, estilo microservicios para el ejemplo del cine):

- Columna izquierda **Clients**: caja con Mobile App, Website, Mobile Web.
- Los clientes conectan (flecha bidireccional) con **Load Balancer**.
- Load Balancer conecta con **API Gateway Service**.
- El API Gateway distribuye hacia el bloque **Application APIs**, una pila vertical de cajas: Listing API, Cinema SeatLayout API, Seat Selection API, Payment API, Communication API.
- Las Application APIs conectan a la derecha con:
  - **Cinema Micro service** (cilindro/óvalo morado apilado, arriba).
  - **Cache** (cilindro amarillo, medio).
  - **RDBMS** (cilindro rojo/rosa, abajo).
- **RDBMS** conecta (flecha bidireccional) con **Backoffice Management System** (caja gris inferior derecha).

## Slide 8

Cierre (decorativa: fondo de dos personas con bata de laboratorio y lentes de seguridad).

**GRACIAS**

CHRISTIAN PAZ TRILLO
