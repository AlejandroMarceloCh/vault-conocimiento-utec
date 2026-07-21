---
curso: INGSOFT
titulo: 08 - Semana 6/IS1 - Aula 6 - Algunos elementos de Diseño__pptx
slides: 20
fuente: 08 - Semana 6/IS1 - Aula 6 - Algunos elementos de Diseño__pptx.pdf
---

## Slide 1

Portada. Título: **Ingeniería de Software**. Subtítulo: *Profesor Christian Paz*. Fondo decorativo (túnel tecnológico azul con figura caminando), logos UTEC / TransformaTec y lema "Reinventa el mundo".

## Slide 2

Título lateral vertical: **Agenda**.

Contenido (lista):
- Arquitectura Monolítica
- Arquitectura en Capas (Layers)
- Microservicios
- Arquitectura Orientada a Eventos
- Casos de Estudio

Bibliografía:
https://learning.oreilly.com/library/view/software-architecture-patterns/9781098134280/

(Imagen de dos personas trabajando frente a pantalla, decorativa.)

## Slide 3

Slide separador de sección. Número grande **1.** e ícono de checklist. Título: **Arquitectura Monolítica**. (Imagen de mano robótica tocando globo digital, decorativa.)

## Slide 4

Título: **Arquitectura Monolítica**

Texto:
- Un único elemento de distribución contiene toda la funcionalidad del software.
- Ej: Sistema Operativo.
- Juego que funciona localmente sin conexión a internet.
- Aplicación que se instala y ejecuta localmente.

**Visual (diagrama de componentes plug-in):** Un rectángulo central azul claro etiquetado **"Core system"**. A su izquierda y derecha, seis cajas rojas etiquetadas **"Plug-in component"** (tres a cada lado), cada una conectada al Core system por una gruesa línea roja. Representa el patrón monolítico basado en microkernel/plug-ins: un núcleo con componentes conectados directamente.

## Slide 5

**Visual (diagrama monolito de 2 niveles):** A la izquierda, una caja 3D azul con etiqueta superior **"User interface"** y debajo una cuadrícula de 6 botones/casillas (representando la UI y sus módulos). Una flecha naranja apunta hacia abajo desde esa caja a un cilindro azul de base de datos etiquetado **"Database"**. Muestra que UI y datos viven en un solo elemento desplegable.

Texto (derecha):

Ventajas:
- Eficiencia al usar el hardware.
- Baja necesidad de conectividad.
- Simplicidad de estructura de código

Desventajas
- Sin modularidad en tiempo de ejecución.
- Single Point of Failure.
- Dificultad de despliegue (actualizaciones).

## Slide 6

Slide separador de sección. Número grande **2.** e ícono de checklist. Título: **Arquitectura en Capas**. (Imagen de mano robótica, decorativa.)

## Slide 7

Título: **Arquitectura Cliente Servidor**

**Visual (diagrama cliente-servidor):** A la izquierda, tres íconos de clientes (una laptop, un smartphone y un desktop/monitor+torre) agrupados bajo la etiqueta **"Clients"**. Los tres se conectan con líneas a una nube central etiquetada **"Internet"**. Desde la nube sale una línea hacia la derecha a un ícono de servidor (torre gris) etiquetado **"Server"**. Ilustra clientes que acceden vía internet a un servidor central.

## Slide 8

Título: **Arquitectura de varias capas**

**Visual (diagrama de capas apiladas):** Cuatro bandas horizontales color crema, apiladas de arriba a abajo:
1. **Presentation layer** — con 3 cajas azules "Component".
2. **Business layer** — con 3 cajas azules "Component".
3. **Persistence layer** — con 3 cajas azules "Component".
4. **Database layer** — con 4 cilindros azules de base de datos.

Cada capa contiene sus propios componentes; la de datos contiene bases de datos.

Texto (derecha):
- Cada capa tiene una responsabilidad específica.
- La comunicación se hace a a través de red o no.
- Los elementos que transitan entre las capas deben ser lo más simple posible (POJO: Plain Old Java Objects).

## Slide 9

Texto (izquierda):

Ventajas:
- Facilidad de dividir el trabajo por especialidad (front, back, database).
- Manejo de código simple.
- Simplicidad de despiegue.

Desventajas
- Escalabilidad horizontal limitada.
- Funcionalidad está dividida en varias capas (agregar un campo en BD requiere campos en todas las capas).

**Visual (diagrama de flujo entre capas):** Las mismas cuatro capas crema apiladas (Presentation / Business / Persistence / Database layer), pero ahora con cajas nombradas y flechas que muestran el flujo de una petición:
- Presentation layer: cajas **"Customer screen"** y **"Customer delegate"**.
- Business layer: caja **"Customer object"**.
- Persistence layer: cajas **"Customer DAO"** y **"Order DAO"**.
- Database layer: cilindro **"Database"**.

Flechas negras punteadas bajan (request) desde Customer screen → delegate → Customer object → DAOs → Database, y flechas rojas punteadas suben de regreso (response). Ilustra cómo una operación atraviesa todas las capas de ida y vuelta.

## Slide 10

Slide separador de sección. Número grande **3.** e ícono de checklist. Título: **Microservicios**. (Imagen de mano robótica, decorativa.)

## Slide 11

Título: **Microservicios**

Texto (izquierda):
- Cada servicio se encarga de una funcionalidad específica y es responsable por el manejo de los datos asociados.
- API Gateway esconde la estructura interna de los microservicios a los clientes.
- Cada servicio puede escalar de forma diferente.
- Cada servicio es reutilizable.

**Visual (diagrama de microservicios):** Arriba a la derecha, un ícono de laptop con "http://www" (el cliente). Una flecha naranja baja a una barra 3D ancha etiquetada **"API gateway"**. Desde el API gateway salen tres flechas naranjas hacia abajo, cada una a una caja 3D **"Service"**. Cada Service tiene su propia flecha naranja hacia abajo a un cilindro **"Database"** independiente (tres bases de datos separadas, una por servicio). Muestra el aislamiento de datos por servicio detrás del gateway.

## Slide 12

Título: **Microservicios**

Texto de rutas (arriba, mapeo URL pública → dirección interna):
- https://miservidor.com.pe/account/crearcuenta → http://192.168.1.12/crearcuenta
- https://miservidor.com.pe/inventory/registrar → http://192.168.1.13/registrar
- https://miservidor.com.pe/shipping/entregar

**Visual (diagrama de microservicios estilo AWS):** A la izquierda dos clientes: un círculo con ícono de móvil (**"Mobile app"**) y un círculo con ícono de monitor (**"Browser"**). El Mobile app conecta vía una caja **"REST API"** a un círculo azul central **"API GATEWAY"**. El Browser conecta vía una caja **"Web"** a un hexágono **"Storefront WebApp"**. Desde el API Gateway y el Storefront WebApp salen líneas cruzadas hacia tres hexágonos de servicio (cada uno precedido por una etiqueta **"REST API"**):
- **Account Service** → cilindro **"Account DB"**
- **Inventory Service** → cilindro **"Inventory DB"**
- **Shipping Service** → cilindro **"Shipping DB"**

Cada servicio tiene su propia base de datos. Una línea vertical a la derecha delimita el conjunto de servicios/DBs.

Texto (derecha):
- Son componentes de software independientes.
- Despliegue independiente.
- Comunicación estándar HTTP.
- Independencia de datos.
- Escalabilidad.

Notas de código/estructura (abajo derecha):
```
Common
- Entidades (POJO)
- Helpers

Account Service
- Import Common
```

## Slide 13

Texto:

Ventajas:
- Independencia de cada funcionalidad.
- Agilidad para los cambios.
- Alta tolerancia a fallas y facilidad de escalamiento horizontal y vertical.

Desventajas
- Cuando existen muchas interacciones entre los microservicios (orquestación) puede resultar complejo y costoso.
- Cuando los datos están muy interconectados.
- Consideraciones para latencia, seguridad y replicación de datos.

(Solo texto sobre banner decorativo superior.)

## Slide 14

Slide separador de sección. Número grande **4.** e ícono de checklist. Título: **Arquitectura Orientada a Eventos**. (Imagen de mano robótica, decorativa.)

## Slide 15

Título: **Arquitectura Orientada a Eventos**

Texto (izquierda):
- En algunas situaciones, los procesos de software pueden ser considerados como eventos.
- Ej: Creación de Cuenta de Alumno.
  - Creación de Cuenta Google.
  - Creación de Cuenta Canvas.
  - Creación en el Sistema Financiero.
  - Notificación Usuario está listo para uso.

**Visual (diagrama orientado a eventos):** Flujo con cajas y canales:
- Caja verde **"Initiating event"** → (flecha punteada) canal **"Event channel"** (cilindro azul con flecha) → caja 3D **"Event processor"** (arriba derecha).
- Ese Event processor baja (flecha) a una caja naranja **"Processing event"**.
- La caja naranja envía (flecha punteada) a otro **"Event channel"** central.
- Ese canal distribuye (flechas punteadas) hacia dos cajas 3D **"Event processor"** (a la izquierda, apiladas).

Ilustra el patrón mediador/broker: un evento inicial fluye por canales a procesadores que generan nuevos eventos procesados, propagados a otros procesadores de forma asíncrona.

## Slide 16

Texto:

Ventajas:
- Alta tolerancia a fallas.
- Manejo asíncrono de operaciones pesadas o lentas.

Desventajas
- Si los clientes requieren una respuesta inmediata.
- Complejidad en el manejo de errores.

- peru.gob.pe/miscertificados
- -> insertar en una cola mi dni, correo al cual me reporten.

(Solo texto sobre banner decorativo superior.)

## Slide 17

Slide separador de sección. Número grande **5.** e ícono de checklist. Título: **Casos de Estudio**. (Imagen de mano robótica, decorativa.)

## Slide 18

Título: **Caso de Estudio**

Texto:
- Sistema de venta de entradas masivo (Concierto) [Demanda por compra > Posibilidad de Atención].
- Sistema de control de ingreso de ese evento asumiendo que el local de ingreso es remoto y tiene mala conectividad a internet.
- https://excalidraw.com/#json=tLIFaYHjyPSWmPYBJ8Upo,bS6WL-bN37ZGYog_jYr-Jg

(Solo texto sobre banner decorativo superior.)

## Slide 19

Título: **Caso de Estudio**

Texto:
- Venta de entradas en eventos masivos (Ej: Concierto con alta demanda).

(Solo texto sobre banner decorativo superior.)

## Slide 20

Slide de cierre. Título grande: **GRACIAS**. Subtítulo: *CHRISTIAN PAZ TRILLO*. (Fondo decorativo de laboratorio con dos personas, logos UTEC/TransformaTec, lema "Reinventa el mundo".)
