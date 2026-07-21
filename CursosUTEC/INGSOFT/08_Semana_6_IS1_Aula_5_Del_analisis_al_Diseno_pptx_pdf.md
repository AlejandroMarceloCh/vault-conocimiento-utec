---
curso: INGSOFT
titulo: 08 - Semana 6/IS1 - Aula 5 - Del analisis al Diseño__pptx
slides: 20
fuente: 08 - Semana 6/IS1 - Aula 5 - Del analisis al Diseño__pptx.pdf
---

## Slide 1

Portada. Título grande "Ingeniería de Software" y subtítulo "Profesor Christian Paz". Fondo decorativo azul de un túnel tecnológico con figura humanoide/robot caminando. Logo UTEC y lema "Reinventa el mundo", marca TransformaTec (chrome decorativo).

## Slide 2

Slide de Agenda. Foto decorativa de dos personas frente a una computadora (tono azul). Contenido:

**Agenda**
- Diseño de Software
- Diseño de Arquitectura
- Diseño Detallado
- Caso de Estudio

## Slide 3

**Desarrollo de Software**

Diagrama de línea de tiempo horizontal con 6 fases conectadas por una línea con nodos amarillos. Cada fase tiene un ícono circular azul arriba y una tarjeta debajo con título y descripción:

| Fase | Ícono | Descripción |
|------|-------|-------------|
| Análisis | diana/blanco | ¿Qué debe hacer el software? |
| Diseño | lupa | ¿Cómo se hará el software? |
| Implementación | cohete | Hacer el Software. |
| Pruebas | calendario con checks | El software hace lo que se supone que debe hacer? |
| Despliegue | cohete despegando | Entregar, poner en marcha. |
| Mantenimiento | eslabones de cadena | El software funciona, pero le falta esto, o está lento, o necesita mejorar esto. |

## Slide 4

Slide divisoria de sección. Número grande "1." con ícono de portapapeles/checklist y título:

**1. Diseño de Software**

Imagen decorativa a la derecha (mano robótica tocando un globo terráqueo digital azul).

## Slide 5

**Diseño**

Objetivo:

- ¿Cómo vamos a hacer el software?
- ¿Qué información va a manejar el software y cómo se va a almacenar/transmitir?
- ¿En qué lenguaje? ¿En qué plataformas?
- ¿Cómo va a funcionar el software? ¿Cómo el usuario va a interactuar con él?
- ¿Cómo el equipo se va a organizar para desarrollar el software?
- ¿Cómo el software va a interactuar con otros softwares?

(Banner superior decorativo con foto de equipo trabajando.)

## Slide 6

**Diseño — Partes:**

- Diseño de Arquitectura.
- Diseño detallado.

Diagrama visual (derecha) que ilustra la relación entre tres conjuntos, con óvalos que agrupan nodos:
- Óvalo **Requirements** (izquierda) contiene R1, R2, R3.
- Óvalo **Architecture** (arriba derecha) contiene 3 nodos conectados en forma de grafo pequeño. Una flecha gruesa morada apunta desde Requirements hacia Architecture.
- Óvalo **Detailed design** (abajo derecha) contiene M1, M2, M3.
- Flechas moradas mapean requerimientos a módulos de diseño detallado: R1 → M2, R2 → M1, R3 → M3 (los requerimientos se cruzan y mapean a los módulos de implementación).
- Líneas azules conectan el óvalo Architecture con el óvalo Detailed design (relación de refinamiento).

## Slide 7

Slide divisoria de sección. Número grande "2." con ícono de portapapeles y título:

**2. Diseño de Arquitectura**

Imagen decorativa a la derecha (mano robótica/globo digital azul).

## Slide 8

**Diseño de Arquitectura**

- Representación visual de la estructura y organización de un sistema o aplicación de software.
- Muestra cómo los diferentes componentes de un sistema interactúan entre sí y cómo se distribuyen en el entorno de ejecución.
- Facilita la comunicación entre los diferentes participantes del proceso de desarrollo.

## Slide 9

**Diseño de Arquitectura**

Texto izquierda:
- Ejemplo: Arquitectura de Sistema de Ventas de Entrada de Cine.
- Objetivo: Ver los clientes disponibles. Que APIs van a ofrecerse. Mecanismos de almacenamiento: Cache y RDBMS.

Diagrama de arquitectura de bloques (derecha):
- **Clients** (columna izquierda): Mobile App, Website, Mobile Web.
- Flecha bidireccional hacia **Load Balancer**.
- Load Balancer ↔ **API Gateway Service**.
- API Gateway ↔ bloque **Application APIs** que agrupa: Listing API, Cinema SeatLayout API, Seat Selection API, Payment API, Communication API.
- Application APIs conecta hacia la derecha con:
  - **Cinema Micro service** (óvalos morados apilados).
  - **Cache** (cilindro amarillo).
  - **RDBMS** (cilindro rojo).
- **RDBMS** ↔ **Backoffice Management System** (bloque abajo derecha).

## Slide 10

**Diseño de Arquitectura**

Texto izquierda:
- Ejemplo: Arquitectura de Sistema de Ventas de Entrada de Cine.
- Objetivo: Ver las plataformas (Nginx, MySQL, Docker). Ver los Lenguajes (Vue, NodeJS). Ver Protocolos (REST, WebSockets).

Diagrama tecnológico (derecha) con logos de tecnologías:
- **Frontend** dentro de contenedor **NGINX**, construido con **Vue** (logo V verde). Conecta con SOCKET.IO (ícono rayo) y con el API Gateway vía **REST API** y **WebSocket**.
- **API Gateway** = **Express** (bloque amarillo central).
- Recuadro punteado etiquetado **AMQP Broker** (con logo **RabbitMQ** al pie) contiene:
  - **Movie service** (NodeJS/JS) con base **MySQL**, conectado al API Gateway vía **RPC**. Consume APIs externas **OMDb API** y **TMDb API** vía **REST API**.
  - **Notification service** (NodeJS/JS) conectado a **SMTP service**.
- Todo el conjunto corre sobre **docker** (logo Docker al pie derecho).

## Slide 11

**Diseño de Arquitectura**

Texto izquierda:
- Ejemplo: Arquitectura de Sistema de Ventas de Entrada de Cine.
- Objetivo: Ver los elementos de información y la interacción entre ellos.

Diagrama de flujo de datos (DFD, derecha) con procesos (rectángulos redondeados), entidades externas (rectángulos) y almacenes de datos (rectángulos abiertos), y flechas etiquetadas con los datos:
- **Customer** (entidad) → `ticket requirements` → **Check bookings** (proceso).
- **Bookings** (almacén) → `available seats` → **Check bookings**.
- **Customers** (almacén) → `name, address, credit card` → **Make bookings** (proceso), con flecha de retorno hacia Customers.
- **Make bookings** → `customer ID, seat no, time, date` → **Bookings** (almacén).
- **Plays** (almacén) → `title, price, time` → **Print tickets** (proceso).
- **Bookings** → `seat no., time, date` → **Print tickets**.
- **Print tickets** → `ticket details` → **Customer** (entidad, derecha).
- Flecha de **Make bookings** hacia **Print tickets**.

## Slide 12

**C4**

- Modelo de arquitectura en niveles.
- Referencia: https://learning.oreilly.com/library/view/creating-software-with/9798888650219/f_0046.xhtml#c4-model.

Imagen (derecha): infografía "The C4 model for visualising software architecture — c4model.com". Muestra una cascada de 4 diagramas conectados por flechas "Zoom in" (verde, amarilla, roja), cada uno haciendo zoom en un elemento del anterior. Etiquetas en la parte inferior:
- **Level 1 — Context**
- **Level 2 — Containers**
- **Level 3 — Components**
- **Level 4 — Code**

## Slide 13

Slide divisoria de sección. Número grande "3." con ícono de portapapeles y título:

**3. Diseño Detallado**

Imagen decorativa a la derecha (mano robótica/globo digital azul).

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

Slide con un **diagrama de clases UML** (derecha) y texto descriptivo (izquierda, parcialmente tapado por el diagrama).

Texto izquierda:
- Un Cliente tiene 0 a n cuentas.
- Un Cliente usa tarjeta.
- Una Cuenta tiene Operaciones.
- Una Operación es realizada en un Cajero Automático.
- Un Cajero Automático tiene un Dispensador.
- La Tarjeta tiene una operación de validación de clave.
- La Cuenta tiene operación de verificación de saldo y una de retiro.

Diagrama de clases UML con las siguientes clases (atributos / métodos) y relaciones:

- **Cliente**: nombres, apellidos, fecha nacimiento.
- **Cuenta**: numero de cuenta, tipo de cuenta, moneda, saldo // existeSaldo(monto), retiro(monto).
- **Tarjeta**: Numero // validaClave().
- **Operacion**: fecha, monto, moneda.
- **Cajero Automatico**: Direccion // Dispensar(monto).
- **Dispensador**: Tipo de Billete, Número de Billetes.

Relaciones:
- Cliente `1` — `0..n` Cuenta (agregación, etiqueta "Relation").
- Cliente → Tarjeta (asociación "Usa").
- Cuenta ◇— Operacion (agregación: la cuenta tiene operaciones).
- Cajero Automatico ◆— (composición) con Operacion.
- Cajero Automatico `1` → `1` Dispensador (el cajero tiene un dispensador).

## Slide 17

**Modelos de Interacción**

- Muestran la interacción entre los actores y los componentes.
- Muestran la interacción entre los objetos del diagrama de clases.
- Muestran el "tiempo de ejecución de una aplicación".
- Son importantes para entender procesos complejos, que constan de varios pasos.

## Slide 18

Slide con un **diagrama de secuencia UML** (derecha) y texto descriptivo (izquierda).

Texto izquierda:
- Un Cliente inserta la tarjeta en un Cajero y se le solicita un PIN.
- El Usuario digita el PIN y se valida si es correcto o no.
- El usuario ingresa un monto para el retiro y se le presenta una lista de cuentas disponibles.
- El usuario selecciona una cuenta y realiza el retiro.
- Se crea la operación y se actualiza el saldo en la cuenta.

Diagrama de secuencia con líneas de vida: **Cliente** (actor), **Cajero**, **Tarjeta**, **Cuenta**, **Operación**. Mensajes en orden:
1. Cliente → Cajero: `Inserta tarjeta`
2. Cajero → Cliente: `Solicita PIN`
3. Cliente → Tarjeta: `Digita PIN`
4. Tarjeta ⇢ Cliente: `PIN OK` (retorno punteado)
5. Cliente → Tarjeta: `Ingresa Monto para retiro`
6. Tarjeta ⇢ Cliente: `Lista de Cuentas` (retorno punteado)
7. Cliente → Cuenta: `Retiro (monto)`
8. Cuenta → Operación: `CreaOperacion(fecha, monto)`
9. Cuenta → Cuenta: `Actualiza saldo` (auto-mensaje)
10. Cuenta ⇢ Tarjeta/Cajero: `AutorizaRetiro` (retorno punteado)

## Slide 19

**Diseño Detallado**

- En el Desarrollo Moderno de Software, no resulta necesario hacer un diseño muy detallado antes de comenzar a programar.
- Se sugiere tener un modelo estructural muy general que contemple la interacción de las entidades más importantes.
- Talvez algunos diagramas de interacción para los flujos más relevantes.
- El resto del diseño detallado se va a modificar tanto durante el desarrollo que es más eficiente hacerlo a la par con el desarrollo.

## Slide 20

Slide de cierre. Texto grande "GRACIAS" y "CHRISTIAN PAZ TRILLO". Fondo decorativo (foto de laboratorio con dos personas trabajando, tono azul). Chrome UTEC/TransformaTec.
