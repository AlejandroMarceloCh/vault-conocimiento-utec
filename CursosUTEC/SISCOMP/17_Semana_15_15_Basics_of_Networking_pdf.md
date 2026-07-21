---
curso: SISCOMP
titulo: 17 - Semana 15/15. Basics of Networking
slides: 26
fuente: 17 - Semana 15/15. Basics of Networking.pdf
---

## Slide 1

Portada (decorativa). Título del curso: **COMPUTING SYSTEMS**. Subtítulo: "Basics of Networking". Professor: Luz A. Adanaqué. Fondo azul de túnel tecnológico con silueta de un robot humanoide.

## Slide 2

Slide de dos bloques sobre foto (científica en laboratorio con tubos de ensayo, tinte azul; decorativa).

- **Motivation**: Basis of networking
- **Goals**: Understand client-server architecture.

## Slide 3

**Summary** (agenda). Foto de mujer con visor VR y globo terráqueo de datos al fondo (decorativa). Lista numerada con íconos:

1. Introduction
2. Background
3. Client Server Architecture

## Slide 4

Portada de sección (decorativa: mano robótica señalando un globo de datos).

**1. Client-Server Architecture**

## Slide 5

Título: **Most network applications are based on the client-server model:**

- A ***server*** process and one or more ***client*** processes
- Server manages some ***resource***
- Server provides ***service*** by manipulating resource for clients
- Server activated by request from client (vending machine analogy)

**Diagrama (flujo de request/response):**
- Elipse verde "Client process" a la izquierda; elipse verde "Server process" al centro; cilindro naranja "Resource" a la derecha.
- Flecha superior de Client → Server rotulada "1. Client sends request".
- Flecha inferior de Server → Client rotulada "3. Server sends response".
- Flecha bidireccional entre Server process y Resource rotulada "2. Server handles request".
- Bajo el Client: "4. Client handles response".

Secuencia de pasos: (1) Client sends request → (2) Server handles request (manipulando el Resource) → (3) Server sends response → (4) Client handles response.

## Slide 6

Título lateral: **Hardware Organization**

**Diagrama de organización de hardware de una computadora (buses):**
- Recuadro "CPU chip" que contiene: "register file" (pila de registros) conectado por flechas gruesas bidireccionales con "ALU", y ambos conectados hacia abajo a "MI" (Memory Interface).
- "MI" se conecta por el **system bus** a "I/O bridge".
- "I/O bridge" se conecta por el **memory bus** a "main memory".
- "I/O bridge" baja (flecha gruesa) hacia el **I/O bus** (barra horizontal grande).
- Colgando del I/O bus: "USB controller" (→ mouse, keyboard), "graphics adapter" (→ monitor), "disk controller" (→ cilindro "disk"), y "network adapter" (resaltado en rosa, → "network" recuadro rosa).
- A la derecha del I/O bus se marcan los "Expansion slots" (dos ranuras); el network adapter está enchufado a un expansion slot.

Idea clave: el adaptador de red (network adapter) es otro dispositivo de I/O más, conectado al I/O bus vía expansion slot.

## Slide 7

Portada de sección (decorativa: mano robótica y globo de datos).

**2. Computer Networks**

## Slide 8

- A ***network*** is a hierarchical system of boxes and wires organized by geographical proximity
  - **SAN** (System Area Network) spans cluster or machine room
    - Switched Ethernet, Quadrics QSW, …
  - **LAN** (Local Area Network) spans a building or campus
    - Ethernet is most prominent example
  - **WAN** (Wide Area Network) spans country or world
    - Typically high-speed point-to-point phone lines
- An ***internetwork (internet)*** is an interconnected set of networks
  - The Global IP Internet (**uppercase** "I") is the most famous example of an internet (**lowercase** "i")
- Let us see how an internet is built from the ground up

## Slide 9

Portada de sección (decorativa: mano robótica y globo de datos).

**3. Ethernet Segment**

## Slide 10

Título: **Ethernet Segment: Lowest Level**

**Diagrama:** Tres recuadros "host" en la fila superior. Cada uno se conecta por una línea (twisted pair) a un recuadro central redondeado amarillo "hub". Los enlaces izquierdo y derecho están rotulados "100 Mb/s". Los puntos donde los cables entran al hub son los **port** (una flecha roja apunta a uno de ellos con la etiqueta "port").

- Ethernet segment consists of a collection of ***hosts*** connected by wires (twisted pairs) to a ***hub***
- Spans room or floor in a building

## Slide 11

Título lateral: **Next Level: Bridged Ethernet Segment**

**Diagrama (topología con bridges):**
- Arriba a la izquierda: hosts A, host, host B conectados a un "hub".
- Ese hub se conecta a un "bridge" **X** por enlace de **100 Mb/s**.
- El bridge X se conecta por **100 Mb/s** a otro "hub" (arriba a la derecha) que tiene 2 hosts.
- Abajo a la izquierda: un "hub" con 2 hosts, conectado por **100 Mb/s** a un "bridge" **Y**.
- El bridge Y se conecta por **100 Mb/s** a otro "hub" (abajo a la derecha) con 3 hosts (uno rotulado C).
- Los dos bridges X e Y están unidos verticalmente por un enlace de **1 Gb/s** (línea gruesa).

Idea: los bridges interconectan múltiples segmentos Ethernet (hubs), usando enlaces más rápidos (1 Gb/s) en el backbone.

## Slide 12

Título: **LANs: Conceptual View**

**Diagrama:**
- Tres grupos de "host … host" conectados cada uno a una barra (bus de LAN): LAN 1 (abajo izquierda), un LAN central arriba, y LAN 2 (abajo derecha).
- LAN 1 conecta a un "router", este por **WAN** a otro "router", este por **WAN** a un tercer "router" que conecta a LAN 2. Los routers están en rosa; los enlaces WAN son líneas gruesas.
- Nota a la derecha (cursiva): "LAN 1 and LAN 2 might be completely different, totally incompatible (e.g., Ethernet, Fibre Channel, 802.11*, T1-links, DSL, …)".
- Abajo a la derecha: nube/esquema de "Ad hoc interconnection of networks" — varios routers y hosts conectados con líneas rojas onduladas irregulares dentro de óvalos grises solapados (topología arbitraria).

Texto:
- **Ad hoc interconnection of networks**
  - No particular topology
  - Vastly different router & link capacities

## Slide 13

Portada de sección (decorativa: mano robótica y globo de datos).

**4. Internet Protocol**

## Slide 14

Título: **Internet Protocol**

**How is it possible to send bits across incompatible LANs and WANs?**

**Solution: *protocol* software running on each host and router**
- Protocol is a set of rules that governs how hosts and routers should cooperate when they transfer data from network to network.
- Smooths out the differences between the different networks

## Slide 15

Título: **What does the protocol do?**

**Provides a *naming scheme***
- An internet protocol defines a uniform format for ***host addresses***
- Each host (and router) is assigned at least one of these internet addresses that uniquely identifies it

**Provides a *delivery mechanism***
- An internet protocol defines a standard transfer unit (***packet***)
- Packet consists of ***header*** and ***payload***
  - Header: contains info such as packet size, source and destination addresses
  - Payload: contains data bits sent from source host

## Slide 16

Título lateral: **Transferring Data**

**Diagrama detallado del recorrido de un dato de Host A (LAN1) a Host B (LAN2) a través de un Router:**

Lado izquierdo (LAN1, Host A "client"):
- (1) `data` — datos crudos que salen del cliente.
- Pasan por "protocol software" y se encapsulan: (2) trama con `data | PH | FH1`. Se marca "internet packet" (data + PH) y "LAN1 frame" (todo: data + PH + FH1).
- Bajan al "LAN1 adapter": (3) `data | PH | FH1` viaja por LAN1.

Centro (**Router**, recuadro rosa con "LAN1 adapter" y "LAN2 adapter" y "protocol software"):
- (4) trama entrante por LAN1: `data | PH | FH1`.
- El router quita FH1, procesa el internet packet y re-encapsula para LAN2.
- (5) trama saliente por LAN2: `data | PH | FH2` (nuevo frame header FH2, con "LAN2 frame" marcado).

Lado derecho (LAN2, Host B "server"):
- (6) `data | PH | FH2` llega al "LAN2 adapter".
- Sube a "protocol software", que desencapsula: (7) `data | PH | FH2`.
- (8) `data` — datos crudos entregados al server.

Leyenda:
- **PH: Internet packet header**
- **FH: LAN frame header**

Idea clave: la carga (data + PH, el internet packet) se conserva punta a punta; solo cambia el frame header (FH1 → FH2) al cruzar de LAN1 a LAN2 en el router.

## Slide 17

Portada de sección (decorativa: mano robótica y globo de datos).

**5. Internet Application**

## Slide 18

Título: **Internet Application**

**Diagrama de pila (stack) en cliente y servidor sobre la Global IP Internet:**

Columna izquierda "Internet client host" (de arriba abajo):
- "Client" (amarillo) — *User code*
- ↑↓ **Sockets interface (system calls)** (línea separadora)
- "TCP/IP" (verde) — *Kernel code*
- ↑↓ **Hardware interface (interrupts)** (línea separadora)
- "Network adapter" (verde) — *Hardware and firmware*

Columna derecha "Internet server host" (misma pila): "Server" (amarillo) / "TCP/IP" (verde) / "Network adapter" (verde), con flechas bidireccionales entre capas.

Abajo, barra rosa que une ambos adaptadores de red: **Global IP Internet**.

Idea: la interfaz de sockets separa el user code del kernel (TCP/IP); la interfaz de hardware separa el kernel del adaptador de red.

## Slide 19

Título: **A Programmer's view**

1. Hosts are mapped to a set of 32-bit ***IP addresses***
   - 128.2.203.179
2. The set of IP addresses is mapped to a set of identifiers called Internet ***domain names***
   - 128.2.203.179 is mapped to www.cs.cmu.edu
3. A process on one Internet host can communicate with a process on another Internet host over a ***connection***

## Slide 20

Título: **IP Addresses**

**32-bit IP addresses are stored in an *IP address struct***
- IP addresses are always stored in memory in ***network byte order*** (big-endian byte order)
- True in general for any integer transferred in a packet header from one machine to another.
  - E.g., the port number used to identify an Internet connection.

**Bloque de código (recuadro amarillo):**
```c
/* Internet address structure */
struct in_addr {
    uint32_t  s_addr; /* network byte order (big-endian) */
};
```

## Slide 21

Título: **Dotted Decimal Notation**

- By convention, each byte in a 32-bit IP address is represented by its decimal value and separated by a period
  - IP address: `0x8002C2F2` = `128.2.194.242`
    - (Se muestra el mapeo byte a byte con colores: 0x80→128, 02→2, C2→194, F2→242)
- Use `getaddrinfo` and `getnameinfo` functions (described later) to convert between IP addresses and dotted decimal format.

## Slide 22

Título lateral: **Internet Domain Names**

**Árbol jerárquico de nombres de dominio (de raíz a hojas):**
- Raíz: *unnamed root*
- First-level domain names: `.net`, `.edu`, `.gov`, `.com`
- Second-level domain names: bajo `.edu` → `mit`, `cmu`, `berkeley`; bajo `.com` → `amazon`
- Third-level domain names: bajo `cmu` → `cs`, `ece`; bajo `amazon` → `www` (176.32.98.166)
- Cuarto nivel: bajo `cs` → `ics`, `pdl`
- Hojas con IP: bajo `ics` → `whaleshark` (128.2.210.175); bajo `pdl` → `www` (128.2.131.66)

El nombre completo se lee de hoja a raíz (p. ej. www.pdl.cs.cmu.edu → 128.2.131.66).

## Slide 23

Título lateral: **Internet Domain System**

- The Internet maintains a mapping between IP addresses and domain names in a huge worldwide distributed database called ***DNS***
- Conceptually, programmers can view the DNS database as a collection of millions of ***host entries***.
  - Each host entry defines the mapping between a set of domain names and IP addresses.
  - In a mathematical sense, a host entry is an equivalence class of domain names and IP addresses.

## Slide 24

Título: **Anatomy of a Connection**

**Diagrama:** dos cajas con elipses verdes — "Client" (izquierda) y "Server (port 80)" (derecha) — unidas por una línea bidireccional (la conexión).

- Sobre el cliente: *Client socket address* `128.2.194.242:51213` (IP del host + puerto efímero).
- Sobre el servidor: *Server socket address* `208.216.181.15:80` (IP + puerto 80).
- Etiqueta central: **Connection socket pair** `(128.2.194.242:51213, 208.216.181.15:80)`.
- Bajo el cliente: Client host address `128.2.194.242`.
- Bajo el servidor: Server host address `208.216.181.15`.

Idea: una conexión queda identificada de forma única por el par de sockets (IP:puerto cliente, IP:puerto servidor).

## Slide 25

Título lateral: **Anatomy of a Connection**

**Diagrama (dos escenarios de request al mismo host de servidor `128.2.194.242`):**

Escenario superior:
- "Client host" (caja con elipse "Client") envía **Service request for 128.2.194.242:80 (i.e., the Web server)**.
- Llega al "Server host 128.2.194.242": el "Kernel" (elipse rosa) enruta la petición hacia "Web server (port 80)" (hay también un "Echo server (port 7)" sin usar).

Escenario inferior:
- El mismo Client envía **Service request for 128.2.194.242:7 (i.e., the echo server)**.
- El Kernel enruta hacia "Echo server (port 7)" (el "Web server (port 80)" queda sin usar).

Idea: el número de puerto en la petición determina a qué servicio del host destino el kernel entrega la conexión.

## Slide 26

Título lateral: **IP Address Structure**

- IP (V4) Address space divided into classes:

**Tabla/diagrama de clases (bits 0…31, con bits líderes y campos Net ID / Host ID):**

| Clase | Bits líderes | Estructura |
|-------|-------------|------------|
| Class A | `0` | Net ID (bits 1–7) + Host ID (bits 8–31) |
| Class B | `10` | Net ID (bits 2–15) + Host ID (bits 16–31) |
| Class C | `110` | Net ID (bits 3–23) + Host ID (bits 24–31) |
| Class D | `1110` | Multicast address |
| Class E | `1111` | Reserved for experiments |

(En el gráfico los campos Net ID están en amarillo y Host ID en rosa; las divisiones de bytes se marcan en las posiciones 0,1,2,3 … 8 … 16 … 24 … 31.)

- Network ID Written in form w.x.y.z/n
  - n = number of bits in host address
  - E.g., CMU written as 128.2.0.0/16
    - Class B address
- Unrouted (private) IP addresses:
  - 10.0.0.0/8    172.16.0.0/12    192.168.0.0/16
