---
curso: REDES
titulo: 06 - Semana 4 _ LAB1B_DNS/LAB2_UDP/LAB2_UDP.pptx
slides: 9
fuente: 06 - Semana 4 _ LAB1B_DNS/LAB2_UDP/LAB2_UDP.pptx.pdf
---

## Slide 1

**UDP (User Datagram Protocol)**
Computer Networks

Portada del capítulo. A la derecha, foto a gran formato de una estructura brutalista de concreto (edificio de bloques de hormigón visto desde abajo contra el cielo), recortada con un corte diagonal y una franja celeste. Elemento puramente decorativo.

Fuentes citadas: Kurose – Computer Networks Book; Peterson and Davie – Computer Networks Book.

## Slide 2

**Transport Layer**

It acts as the liaison between the **Application layer** and the lower **network layers**.

Diagrama comparativo de tres pilas de capas, alineadas horizontalmente para mostrar la correspondencia entre modelos:

- **OSI Model** (7 capas, numeradas 1–7 de abajo hacia arriba):
  7 Application, 6 Presentation, 5 Session (las tres en verde) · 4 Transport (azul) · 3 Network, 2 Data Link, 1 Physical (en amarillo/naranja).
- **TCP/IP Model (RFC1122)** (4 capas): Application (agrupa OSI 5–7) · Transport · Network · Link (agrupa Data Link + Physical).
- **TCP/IP Model (Common)** (5 capas, numeradas 1–5): Application (5) · Transport (4) · Network (3) · Data Link (2) · Physical (1).

Líneas punteadas conectan horizontalmente las capas equivalentes entre los tres modelos (Transport↔Transport↔Transport, Network↔Network↔Network, etc.). La capa **Transport** (nivel 4) queda resaltada como el foco del tema.

Fuente: NetworkAcademy.io

## Slide 3

**Transport Layer**

There are two primary ways to move data across the network:
1. **TCP**: **Connection-oriented**. Focuses on **reliability**.
2. **UDP**: **Connectionless**. Focuses on **speed**.

Diagrama "TCP vs UDP Communication", dividido en dos mitades por una línea vertical:

- **Lado TCP**: laptop (Client) a la izquierda y un servidor (rack naranja) a la derecha. Intercambio del three-way handshake mostrado con flechas: `SYN` (cliente→servidor), `SYN-ACK` (servidor→cliente), `ACK` (cliente→servidor). Debajo, un esquema de **Unicast (One-to-One)**: un nodo origen (naranja) apunta con una sola flecha a un nodo destino, resto de nodos sin conexión.
- **Lado UDP**: laptop (Client) y servidor. El servidor manda flujo sin handshake: una flecha `Request` (servidor→cliente) y tres flechas `Response` sucesivas (cliente→servidor / flujo continuo), sin establecimiento previo. Debajo, dos esquemas: **Broadcast (One-to-All)** — un nodo origen naranja con flechas a todos los nodos — y **Multicast (One-to-Several)** — un nodo origen con flechas solo a un subconjunto de nodos.

Fuente: Cheap Ssl Security.

## Slide 4

**TCP vs UDP**

Reliability vs. Speed

Tabla comparativa (encabezado gris, tres columnas):

| Feature | TCP | UDP |
|---|---|---|
| Connection | Handshake required (3-way) | No handshake (Connectionless) |
| Delivery | Guaranteed & In-order | Best-effort (No guarantee) |
| Error Recovery | Retransmits lost packets | No retransmission |
| Overhead | Heavy header (20 bytes) | Lightweight header (8 bytes) |

## Slide 5

**TCP vs UDP**

Slide con una metáfora visual mediante dos fotografías, tituladas **TCP** y **UDP**:

- **TCP**: foto de una mujer bebiendo agua de una botella de forma controlada y ordenada (entrega confiable, sorbo a sorbo).
- **UDP**: foto de un hombre riendo mientras le echan/vierten agua a la cara desde una botella, chorro descontrolado y salpicando (envío rápido best-effort, sin control, "algo se pierde").

No hay texto adicional; la analogía visual ilustra fiabilidad ordenada (TCP) vs velocidad sin control (UDP).

## Slide 6

**UDP**

A simple, message-based protocol that sends data without establishing a formal connection.

1. **Stateless**: The sender doesn't track if the data was received.
2. **Low Latency**: Minimal delay because there is no "flow control" or "congestion control."
3. **Header Simplicity**: It only contains 4 fields:
   a. Source Port,
   b. Destination Port,
   c. Length, and
   d. Checksum.

Slide solo de texto (sin figuras).

## Slide 7

**UDP**

Diagrama del formato del encabezado UDP en estilo RFC (ASCII art), con la escala de bits en la parte superior (0–7, 8–15, 16–23, 24–31, es decir dos palabras de 16 bits por fila):

```
 0      7 8     15 16    23 24    31
+--------+--------+--------+--------+
|     Source      |   Destination   |
|      Port       |      Port       |
+--------+--------+--------+--------+
|                 |                 |
|     Length      |     Checksum    |
+--------+--------+--------+--------+
|
|          data octets ...
+---------------- ...
```

Título de la figura: **User Datagram Header Format**

Muestra el header de 8 bytes: primera palabra de 32 bits = Source Port (16 bits) + Destination Port (16 bits); segunda palabra = Length (16 bits) + Checksum (16 bits); luego siguen los data octets (payload).

## Slide 8

**UDP**

This protocol provides a procedure for application programs to send messages to other programs with a minimum of protocol mechanism. The protocol is transaction oriented, and delivery and duplicate protection are not guaranteed.

Diagrama de bloques del datagrama UDP (dos niveles):

- Nivel superior: un rectángulo dividido en dos celdas — **UDP Header** | **UDP Data** — rotulado arriba con la llave **"8 Bytes"** que abarca el UDP Header.
- Líneas diagonales expanden el UDP Header hacia el nivel inferior, una tabla 2×2 con los cuatro campos y su tamaño:
  - **Source port — 16 bits** | **Destination port — 16 bits**
  - **Length — 16 bits** | **Checksum — 16 bits**

Refuerza que el header UDP mide 8 bytes = 4 campos de 16 bits cada uno.

## Slide 9

**UDP**

*Use Cases*

- **Live Streaming:** Speed is more important than a perfectly reconstructed frame.
- **Online Gaming:** Reducing "lag" is the top priority.
- **VoIP (Voice over IP):** Minor packet loss is unnoticeable in human speech, but delays are frustrating.
- **DNS (Domain Name System):** Fast, short request/response cycles.

Slide solo de texto (sin figuras).
