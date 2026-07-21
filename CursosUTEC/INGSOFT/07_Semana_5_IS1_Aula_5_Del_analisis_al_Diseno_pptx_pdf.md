---
curso: INGSOFT
titulo: 07 - Semana 5/IS1 - Aula 5 - Del analisis al Diseño__pptx
slides: 20
fuente: 07 - Semana 5/IS1 - Aula 5 - Del analisis al Diseño__pptx.pdf
---

## Slide 1

Portada. Título grande centrado: **Ingeniería de Software**. Subtítulo: *Profesor Christian Paz*. Fondo decorativo (silueta caminando en un túnel de datos azul). Chrome UTEC / "Reinventa el mundo" / TransformaTec: decorativo.

## Slide 2

**Agenda** (título vertical a la izquierda). Lista de temas del capítulo:

- Diseño de Software
- Diseño de Arquitectura
- Diseño Detallado
- Caso de Estudio

Foto de dos personas trabajando frente a una pantalla: decorativa.

## Slide 3

**Desarrollo de Software** — Diagrama de pipeline horizontal de 6 fases, cada una con un ícono (círculo azul) conectado por una línea con nodos amarillos. Debajo de cada ícono, una tarjeta con el nombre de la fase y su pregunta/descripción:

| Fase | Ícono | Descripción |
|------|-------|-------------|
| Análisis | diana/objetivo | ¿Qué debe hacer el software? |
| Diseño | lupa | ¿Cómo se hará el software? |
| Implementación | cohete | Hacer el Software. |
| Pruebas | calendario con checks | ¿El software hace lo que se supone que debe hacer? |
| Despliegue | cohete despegando | Entregar, poner en marcha. |
| Mantenimiento | eslabón/cadena | El software funciona, pero le falta esto, o está lento, o necesita mejorar esto. |

Las fases fluyen en orden: Análisis → Diseño → Implementación → Pruebas → Despliegue → Mantenimiento.

## Slide 4

Slide separadora de sección. Número grande **1.** con ícono de portapapeles, y título **Diseño de Software**. Franja lateral derecha con imagen decorativa (mano robótica tocando un globo de datos).

## Slide 5

**Diseño**

Objetivo:

- ¿Cómo vamos a hacer el software?
- ¿Qué información va a manejar el software y cómo se va a almacenar/transmitir?
- ¿En qué lenguaje? ¿En qué plataformas?
- ¿Cómo va a funcionar el software? ¿Cómo el usuario va a interactuar con él?
- ¿Cómo el equipo se va a organizar para desarrollar el software?
- ¿Cómo el software va a interactuar con otros softwares?

## Slide 6

**Partes:**

- Diseño de Arquitectura.
- Diseño detallado.

A la derecha, un diagrama conceptual que muestra el mapeo entre tres niveles (tres óvalos morados):

- **Requirements** (óvalo izquierdo): contiene los requisitos R1, R2, R3.
- **Architecture** (óvalo superior derecho): contiene un pequeño grafo de nodos conectados (componentes).
- **Detailed design** (óvalo inferior derecho): contiene los módulos M1, M2, M3.

Una flecha gruesa va de Requirements → Architecture. Líneas azules conectan Architecture con el Detailed design (descomposición). Flechas moradas cruzadas mapean requisitos a módulos: R1 → M1, R2 → M2, R3 → M3 (trazabilidad de requisitos a diseño detallado).

## Slide 7

Slide separadora de sección. Número grande **2.** con ícono de portapapeles, y título **Diseño de Arquitectura**. Imagen lateral decorativa (mano robótica y globo de datos).

## Slide 8

**Diseño de Arquitectura**

- Representación visual de la estructura y organización de un sistema o aplicación de software.
- Muestra cómo los diferentes componentes de un sistema interactúan entre sí y cómo se distribuyen en el entorno de ejecución.
- Facilita la comunicación entre los diferentes participantes del proceso de desarrollo.

## Slide 9

**Diseño de Arquitectura**

Texto a la izquierda:
- Ejemplo: Arquitectura de Sistema de Ventas de Entrada de Cine.
- Objetivo: Ver los clientes disponibles. Que APIs van a ofrecerse. Mecanismos de almacenamiento: Cache y RDBMS.

Diagrama de arquitectura (vista de componentes/APIs). Flujo de izquierda a derecha:

- **Clients** (caja gris): Mobile App, Website, Mobile Web.
- Flecha bidireccional → **Load Balancer** (caja azul).
- Load Balancer ↔ **API Gateway Service** (caja azul).
- API Gateway ↔ bloque **Application APIs** (caja azul que contiene): Listing API, Cinema SeatLayout API, Seat Selection API, Payment API, Communication API.
- Application APIs conecta hacia:
  - **Cinema Micro service** (óvalo morado, apilado indicando varias instancias).
  - **Cache** (cilindro amarillo).
  - **RDBMS** (cilindro rojo).
- **RDBMS** ↔ **Backoffice Management System** (caja gris inferior).

Enfatiza los clientes, las APIs ofrecidas y los mecanismos de almacenamiento (Cache y RDBMS).

## Slide 10

**Diseño de Arquitectura**

Texto a la izquierda:
- Ejemplo: Arquitectura de Sistema de Ventas de Entrada de Cine.
- Objetivo: Ver las plataformas (Nginx, MySQL, Docker). Ver los Lenguajes (Vue, NodeJS). Ver Protocolos (REST, WebSockets).

Diagrama de arquitectura tecnológico (mismo sistema, vista de tecnologías/protocolos):

- **Frontend** (con logos NGINX y Vue) — se comunica con el **API Gateway** vía REST API y WebSocket (SOCKET.IO).
- **API Gateway** (columna central, con logo Express).
- API Gateway ↔ **Movie service** (NodeJS/JS + base MySQL) vía RPC.
- Movie service consume **OMDb API** y **TMDb API** externas vía REST API.
- API Gateway → **Notification service** (NodeJS/JS) que conecta con **SMTP service**.
- Todo el bloque de servicios está dentro de un contorno punteado etiquetado **AMQP Broker** con logo **RabbitMQ** (mensajería asíncrona).
- Logo **docker** abajo a la derecha (contenedores).

Muestra plataformas (Nginx, MySQL, Docker), lenguajes (Vue, NodeJS) y protocolos (REST, WebSockets, RPC, AMQP).

## Slide 11

**Diseño de Arquitectura**

Texto a la izquierda:
- Ejemplo: Arquitectura de Sistema de Ventas de Entrada de Cine.
- Objetivo: Ver los elementos de información y la interacción entre ellos.

Diagrama de flujo de datos (DFD) del sistema de reservas de cine. Procesos (cajas redondeadas), entidades externas (cajas) y almacenes de datos (cajas abiertas), con flujos etiquetados:

- **Customer** (entidad) → `ticket requirements` → **Check bookings** (proceso).
- **Check bookings** ← `available seats` ← **Bookings** (almacén de datos).
- **Customers** (almacén) → `name, address, credit card` → **Make bookings** (proceso); **Make bookings** también escribe de vuelta a **Customers**.
- **Make bookings** → `customer ID, seat no, time, date` → **Bookings** (almacén).
- **Plays** (almacén) → `title, price, time` → **Print tickets** (proceso).
- **Bookings** → `seat no., time, date` → **Print tickets**.
- **Print tickets** → `ticket details` → **Customer** (entidad de salida).

Muestra los elementos de información (Customers, Bookings, Plays) y cómo se mueven entre procesos.

## Slide 12

**C4**

- Modelo de arquitectura en niveles.
- Referencia: https://learning.oreilly.com/library/view/creating-software-with/9798888650219/f_0046.xhtml#c4-model.

A la derecha, imagen del **C4 model for visualising software architecture** (c4model.com). Muestra 4 diagramas encadenados con flechas "Zoom in" de mayor a menor nivel de abstracción:

- **Level 1 – Context** (recuadro verde): diagrama de contexto del sistema con actor y sistemas externos.
- **Level 2 – Containers** (recuadro verde/amarillo): contenedores (Web App, Single Page App, Mobile App, Database, API Application, etc.).
- **Level 3 – Components** (recuadro amarillo/rojo): componentes internos de un contenedor (controladores, servicios).
- **Level 4 – Code** (recuadro rojo): diagrama de clases del código.

Cada nivel hace zoom-in del anterior (Context → Containers → Components → Code).

## Slide 13

Slide separadora de sección. Número grande **3.** con ícono de portapapeles, y título **Diseño Detallado**. Imagen lateral decorativa (mano robótica).

## Slide 14

**Diseño Detallado**

- Dar mayor detalle a los componentes del Diseño de Arquitectura.
- Conseguir mapear el detalle de los requerimientos a objetos de implementación.
- UX: Interfaz de Usuario (Prototipos en la herramienta final).
- Modelos Estructurales: Datos.
- Modelos de Interacción: Procesos.

## Slide 15

**Modelos Estructurales**

- Diagramas de clases, donde inicialmente las clases representan objetos del mundo real.
- Al adicionar más detalles se crean clases para necesidades de implementación.
- Es importante modelar a alto nivel las estructuras de datos de la aplicación para entender como se comparten los datos y como serán almacenados.

## Slide 16

**Modelos** (diagrama de clases UML del sistema de cajero automático).

Texto explicativo a la izquierda:
- Un Cliente tiene 0 a n cuentas.
- Un Cliente usa tarjeta.
- Una Cuenta tiene Operaciones.
- Una Operación es realizada en un Cajero Automático.
- Un Cajero Automático tiene un Dispensador.
- La Tarjeta tiene una operación de validación de clave.
- La Cuenta tiene operación de verificación de saldo y una de retiro.

Diagrama de clases UML con las siguientes clases (nombre / atributos / métodos) y relaciones:

- **Cliente**: nombres, apellidos, fecha nacimiento.
- **Tarjeta**: Numero / validaClave().
- **Cuenta**: numero de cuenta, tipo de cuenta, moneda, saldo / existeSaldo(monto), retiro(monto).
- **Operacion**: fecha, monto, moneda.
- **Cajero Automatico**: Direccion / Dispensar(monto).
- **Dispensador**: Tipo de Billete, Número de Billetes.

Relaciones:
- Cliente **1 —— 0..n** Cuenta (asociación "Relation", un cliente tiene 0 a n cuentas).
- Cliente ——▷ Tarjeta (asociación "Usa").
- Cuenta ◇—— Operacion (agregación: una cuenta tiene operaciones).
- Operacion —— Cajero Automatico (una operación se realiza en un cajero).
- Cajero Automatico ◆—— Dispensador (composición 1: el cajero tiene un dispensador).

## Slide 17

**Modelos de Interacción**

- Muestran la interacción entre los actores y los componentes.
- Muestran la interacción entre los objetos del diagrama de clases.
- Muestran el "tiempo de ejecución de una aplicación".
- Son importantes para entender procesos complejos, que constan de varios pasos.

## Slide 18

**Modelos** (diagrama de secuencia UML del retiro en cajero).

Texto explicativo a la izquierda:
- Un Cliente inserta la tarjeta en un Cajero y se le solicita un PIN.
- El Usuario digita el PIN y se valida si es correcto o no.
- El usuario ingresa un monto para el retiro y se le presenta una lista de cuentas disponibles.
- El usuario selecciona una cuenta y realiza el retiro.
- Se crea la operación y se actualiza el saldo en la cuenta.

Diagrama de secuencia con líneas de vida: **Cliente** (actor), **Cajero**, **Tarjeta**, **Cuenta**, **Operación**. Secuencia de mensajes:

1. Cliente → Cajero: `Inserta tarjeta`
2. Cajero → Cliente: `Solicita PIN`
3. Cliente → Tarjeta: `Digita PIN`
4. Tarjeta ⇢ Cliente: `PIN OK` (respuesta punteada)
5. Cliente → Tarjeta: `Ingresa Monto para retiro`
6. Tarjeta ⇢ Cliente: `Lista de Cuentas` (respuesta punteada)
7. Cliente → Cuenta: `Retiro (monto)`
8. Cuenta → Operación: `CreaOperacion(fecha, monto)`
9. Cuenta → Cuenta: `Actualiza saldo` (auto-mensaje)
10. Cuenta ⇢ Cliente/Tarjeta: `AutorizaRetiro` (respuesta punteada)

## Slide 19

**Diseño Detallado**

- En el Desarrollo Moderno de Software, no resulta necesario hacer un diseño muy detallado antes de comenzar a programar.
- Se sugiere tener un modelo estructural muy general que contemple la interacción de las entidades más importantes.
- Talvez algunos diagramas de interacción para los flujos más relevantes.
- El resto del diseño detallado se va a modificar tanto durante el desarrollo que es más eficiente hacerlo a la par con el desarrollo.

## Slide 20

Slide de cierre. Título grande **GRACIAS**. Subtítulo: *CHRISTIAN PAZ TRILLO*. Fondo decorativo (laboratorio con dos personas). Chrome UTEC / TransformaTec: decorativo.
