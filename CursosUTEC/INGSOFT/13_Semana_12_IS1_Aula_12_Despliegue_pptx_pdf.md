---
curso: INGSOFT
titulo: 13 - Semana 12/IS1 - Aula 12 - Despliegue__pptx
slides: 25
fuente: 13 - Semana 12/IS1 - Aula 12 - Despliegue__pptx.pdf
---

## Slide 1

Portada. Título: **Ingeniería de Software**. Subtítulo: *Profesor Christian Paz*. Imagen decorativa (silueta humana/robot en túnel tecnológico azul). Chrome UTEC / TransformaTec / "Reinventa el mundo".

## Slide 2

Título: **Desarrollo de Software**.

Diagrama horizontal de las 6 etapas del ciclo de desarrollo de software, conectadas por una línea de tiempo con íconos circulares (diana, lupa, cohete, calendario, cohete, cadena/eslabón). Cada etapa es una tarjeta con encabezado azul y descripción. La etapa **Despliegue** está resaltada en amarillo (es el foco del capítulo).

| Etapa | Descripción |
|-------|-------------|
| Análisis | ¿Qué debe hacer el software? |
| Diseño | ¿Cómo se hará el software? |
| Implementación | Hacer el Software. |
| Pruebas | ¿El software hace lo que se supone que debe hacer? |
| **Despliegue** (resaltado) | Entregar, poner en marcha. |
| Mantenimiento | El software funciona, pero le falta esto, o está lento, o necesita mejorar esto. |

## Slide 3

Divisor de sección. Número **1.** grande + ícono de portapapeles. Título: **Despliegue de Software**. Imagen decorativa (mano robótica tocando un globo terráqueo digital).

## Slide 4

Título: **Despliegue de Software (Deployment)**.

- El despliegue de software consiste en la transición de todas las estructuras de código fuente (código, scripts) hacia software en ejecución.
- Esta actividad inicia desde la etapa de Diseño especialmente referido a la arquitectura.
- Puede realizarse de forma manual hasta totalmente automatizada.
- Las actividades de despliegue usualmente son efectuadas por alguien con perfil de "DevOps".

## Slide 5

Título: **Diseño** (contexto de despliegue).

Diagrama de convergencia: tres cajas de entrada apuntan con flechas azules a una caja destino **Despliegue** (a la derecha). Cada flecha lleva una etiqueta con el artefacto que aporta esa etapa al despliegue:

- **Diseño** → "Diagramas de Arquitectura"
- **Desarrollo** → "Código, Scripts de BD, Configuración"
- **Pruebas** → "Casos de Prueba automatizados y manuales"

Es decir, el Despliegue toma insumos de Diseño (arquitectura), Desarrollo (código/scripts/config) y Pruebas (casos de prueba).

## Slide 6

Título: **Despliegue de Software**.

A la izquierda, **diagrama de arquitectura de referencia** (se repite en varias slides) de una app tipo catálogo de películas. Componentes y conexiones:
- **Frontend** (Vue) servido tras **NGINX**, conectado a **API Gateway** vía REST API y WebSocket; también usa **SOCKET.IO**.
- **API Gateway** (columna amarilla) implementado con **Express**; se comunica con **Movie service** (Node.js) vía RPC.
- **Movie service** (Node.js) usa **MySQL** y consume APIs externas **OMDb API** y **TMDb API** vía REST API.
- **Notification service** (Node.js) conectado a **SMTP service**.
- Todo dentro de un **AMQP Broker** implementado con **RabbitMQ**; contenerizado con **docker**.

A la derecha, texto **Con base en el modelo de arquitectura:**
- Definir la **infraestructura** que soportará la arquitectura.
- Considerar ambientes de desarrollo, pruebas y producción.
- Necesidades de red (permisos, firewall).
- Creación de scripts de despliegue.

## Slide 7

Título: **Despliegue de Software**. Mismo diagrama de arquitectura de la slide 6 (Frontend/NGINX/Vue, API Gateway/Express, Movie service/MySQL/OMDb/TMDb, Notification service/SMTP, RabbitMQ, docker).

A la derecha, texto **Con base en el modelo de arquitectura:**
- Inicialización de datos.
- Scripts de inicialización de datos.
- Configuración inicial del sistema.
- Cuál es el procedimiento de despliegue cada nueva versión.
- Validación del despliegue.

## Slide 8

Título: **Despliegue de Software**. Mismo diagrama de arquitectura de referencia.

A la derecha, texto **Con base en el modelo de arquitectura:**
- Cómo monitorear el funcionamiento del software.
- Cómo alertar sobre algún funcionamiento incorrecto del software.
- Cómo proceder a atender una alerta generada.

## Slide 9

Título: **Preparación**.

- Definir la Infraestructura que soportará la arquitectura propuesta:
  - Hardware o Virtualización (ambientes en nube).
  - Sistema Operativo.
- Ej:
- Frontend: VM en AWS.
- Movie Service: Lambda.
- MySQL: RDBMS gestionado por AWS.
- Api Gateway en AWS.

A la derecha, el mismo diagrama de arquitectura de referencia (versión reducida).

## Slide 10

Título: **Preparación**. (Variante del ejemplo anterior con infraestructura on-premise en vez de AWS.)

- Definir la Infraestructura que soportará la arquitectura propuesta:
  - Hardware o Virtualización (ambientes en nube).
  - Sistema Operativo.
- Ej:
- Frontend: Nginx instalado en IP 192.168.0.204.
- Movie Service: Dockerizado en k8s.
- MySQL: Servidor en IP 192.168.0.205 Puerto 1593.
- Api Gateway configurado en el mismo Nginx del frontend.

A la derecha, el mismo diagrama de arquitectura de referencia.

## Slide 11

Título: **Preparación**. (Dimensionamiento de ambientes.)

Columna izquierda:
- Ambientes:
  - Desarrollo.
  - Pruebas.
  - Producción
- Ej:
- Desarrollo: Servidor con 16G de RAM.
- Pruebas: 32GB de RAM.
- Producción: 64GB de RAM.

Columna derecha:
- Instalación de Software necesario.

## Slide 12

Título: **Preparación**. (Conectividad y seguridad.)

- Conectividad de Red y Seguridad.

Nginx tendrá salida a Internet y requerirá un SSL / HTTPS.

Debido a la conexión al API externa, Movie Service deberá tener salida a internet.

A la derecha, el mismo diagrama de arquitectura de referencia.

## Slide 13

Título: **Versionamiento de Software**.

Proceso de asignar identificadores únicos a diferentes versiones de un programa o aplicación para gestionar y rastrear sus cambios a lo largo del tiempo.

- **Identificar el estado del software**: Saber si es una versión inicial, una actualización menor o una importante.
- **Facilitar la colaboración**: Ayuda a los equipos a coordinar el trabajo en diferentes versiones.
- **Mantener la trazabilidad**: Permite saber qué funcionalidades o cambios están presentes en cada versión.
- **Mejorar la compatibilidad**: Garantiza que los usuarios o sistemas relacionados puedan adaptarse a nuevas versiones.

## Slide 14

Título: **Versionamiento de Software**.

Texto: Herramientas: Git (Github, GitLab, Azure Devops).

A la derecha, **diagrama de flujo de ramas Git (Git flow) con Pull Requests**, en dos filas:

- Fila superior: cilindro **Git — Shared Repo** → rama **feature** (Feature Branch) → **Pull Request** (ícono morado de upload) → rama **develop** (Develop Branch) → cilindro **Git — Shared Repo**.
- Fila inferior: cilindro **Git — Shared Repo** con ramas **hotfix** y **release** (Hotfix or Release Branch) → **Pull Request** → ramas **develop** y **master** (Develop or Master Branch) → cilindro **Git — Shared Repo**.

Ilustra cómo las ramas (feature/hotfix/release) se integran vía Pull Request hacia develop/master en el repo compartido.

## Slide 15

Título: **Integración Continua (CI)**.

Integrar con frecuencia los cambios de código de todos los desarrolladores en un repositorio central, seguido de la automatización de pruebas y compilaciones para garantizar que el nuevo código no cause problemas en el proyecto.

(En negrita) Detectar y solucionar errores rápidamente, mejorar la calidad del software y reducir el tiempo necesario para lanzar actualizaciones.

## Slide 16

Título: **Integración Continua (CI)**.

- Detección temprana de errores: Al probar cambios con frecuencia, los problemas se identifican rápidamente.
- Colaboración eficiente: Los desarrolladores trabajan en paralelo sin causar conflictos en el código.
- Mayor calidad del software: Se asegura que el código siempre esté en un estado funcional y probado.
- Menor riesgo en despliegues: Las actualizaciones pequeñas y frecuentes son más seguras que grandes cambios aplicados de una vez.

## Slide 17

Título: **Integración Continua (CI)**.

Herramientas
- Jenkins.
- Github actions.
- Ansible.

## Slide 18

Título: **Integración Continua**.

**Diagrama de flujo de un pipeline de CI**:
- Tres **Developer** (cada uno con laptop) hacen **"Commit changes"** (flechas amarillas) hacia el **Git Repository** (ícono de git en el centro).
- Entre el Git Repository y el **CI Server** (cilindro) hay una relación **Poll** (el CI Server sondea el repo).
- El CI Server ejecuta el **Build script** (ícono de documento a la derecha), cuyas tareas son:
  - Run static code analysis
  - Deployment to Integration sandbox
  - Run all tests
- El CI Server **genera** ("Generate") un **Feedback Mechanism** (caja superior), que retorna información al Developer (flecha punteada de vuelta hacia el desarrollador).

## Slide 19

Título: **Despliegue continuo (CD)**.

Consiste en automatizar todo el proceso de implementación de nuevas versiones del software en un entorno de producción, asegurando que los cambios que han pasado las pruebas automatizadas se desplieguen directamente a los usuarios finales.

Garantizar que los cambios en el código, como nuevas funcionalidades, correcciones de errores o mejoras, lleguen rápidamente a producción de manera confiable y sin intervención manual.

## Slide 20

Título: **Despliegue continuo (CD)**.

Herramientas
- Jenkins.
- Github actions.
- Ansible.

## Slide 21

Título: **CD**.

**Diagrama de arquitectura de un pipeline CD con Jenkins y Docker Registry**:
- Fuentes de código (izquierda), cada una con su tecnología:
  - **Bitbucket (Cloud)** — frontend Node Js
  - **Gitlab (Cloud)** — database Postgresql
  - **GitHub** — backend Java Micronaut
- Las tres fuentes apuntan al **jenkins-build-server.net** (container docker-machine, ícono Jenkins+Docker).
- Jenkins hace **push** hacia el **docker server icr-docker-00.registry.com** (registry Docker), con operaciones **docker push / docker pull**.
- Jenkins hace **deploy** hacia el **docker-machine-client** (ícono Docker abajo al centro), que sirve al **navegador web** y al **terminal Soporte**.
- El docker-machine-client hace **docker pull (cache) — Descarga desde la caché** desde el **docker server icr-mirror-00.registry.com** (registry espejo/mirror).
- El mirror **se almacena en caché** desde el **Docker Hub** (ícono negro, derecha).
- La **1ra vez descarga desde internet** ("docker pull — 1ra vez descarga desde internet") va desde el docker-machine-client hacia Docker Hub.

Esquema: registro local + mirror con caché para evitar descargar imágenes de Docker Hub cada vez.

## Slide 22

Título: **Implementación**.

- Configuración del Sistema:
  - URLs.
  - Cadenas de Conexión a BD.
  - Usuarios / Passwords / Certificados de las APIs.
  - Inicialización de BD.

## Slide 23

Título: **Implementación**.

Texto (izquierda):
- API Key OMDb: Desarrollo y Producción.
- Cadena de Conexión BD.
- Ruta de Conexión del frontend al API Gateway.

A la derecha, el mismo diagrama de arquitectura de referencia (Frontend/NGINX/Vue, Express/API Gateway, Movie service/MySQL/OMDb/TMDb, Notification service/SMTP, RabbitMQ, docker), mostrando dónde aplican esos parámetros de configuración.

## Slide 24

Título: **Validación**.

- Pruebas Unitarias / Integración ejecutadas antes de despliegue.
- Una vez que se realice el despliegue en cualquier ambiente:
  - Validar que la versión desplegada funcione.

## Slide 25

Cierre. Título grande: **GRACIAS**. Subtítulo: *CHRISTIAN PAZ TRILLO*. Imagen decorativa (personas en laboratorio con gafas de seguridad). Chrome UTEC / TransformaTec.
