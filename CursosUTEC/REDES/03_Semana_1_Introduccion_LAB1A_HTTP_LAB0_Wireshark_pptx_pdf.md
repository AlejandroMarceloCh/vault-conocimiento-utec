---
curso: REDES
titulo: 03 - Semana 1 _ Introducción + LAB1A_HTTP/LAB0_Wireshark.pptx
slides: 17
fuente: 03 - Semana 1 _ Introducción + LAB1A_HTTP/LAB0_Wireshark.pptx.pdf
---

## Slide 1

**Portada (decorativa).** Título grande **Wireshark** en azul, subtítulo "Computer **Networks**". A la derecha, foto de arquitectura brutalista de concreto (edificio geométrico contra cielo, estética). Metadatos del curso al pie izquierdo:

- CS4054 - 2026-2
- PROF.: garias@utec.edu.pe
- SRC: KUROSE – COMPUTER NETWORKS BOOK / PETERSON AND DAVIE – COMPUTER NETWORKS BOOK

## Slide 2

**Executive Summary**

- **Motivation:** Computer network abstraction allows to have a large implementation such as the Internet.
- **Problem:** We need to observe the details in data transmission over the network. *(resaltado en azul)*
- **Overview:** *(resaltado en rojo)*
  - Introduce a sniffer tool: Wireshark.
  - Analyze the behavior of web browsing.
  - Evaluate the packet contents under the HTTP protocol.
- **Conclusion:** We can begin with network experimentation and packet analysis. *(resaltado en verde)*

Slide de solo texto; el color codifica la estructura problema/solución/conclusión.

## Slide 3

**Outline** (índice del capítulo). Cinco barras horizontales apiladas; la primera, **Introduction**, resaltada en azul (sección activa); el resto en gris:

1. **Introduction** ← activa
2. Installation
3. Getting started
4. Test
5. Conclusions

## Slide 4

**Our course**

Texto: **A common Mistake:** The usual "Networks course": Primarily for learning network design, configuration, and troubleshooting of Cisco devices.

**Visual (lo que faltaba):** dos capturas/diagramas de **Cisco Packet Tracer** que ilustran el enfoque que este curso NO seguirá:

- **Izquierda:** captura de pantalla de la interfaz de Cisco Packet Tracer (barra de menús File/Edit/Options/View/Tools/Extensions, pestañas "Logical | Physical", barra de tiempo "Time: 01:21:42"). En el lienzo, una topología jerárquica: router 2911 "R1" conectado a un Cloud-PT "INTERNET" (enlace rojo), dos switches de distribución 3650-24PS (DS-1, DS-2), tres switches de acceso 2960-24TT (AS-1, AS-2, AS-3) con cableado cruzado, y al fondo PC-PT (PC0), Printer-PT (Printer0), Server-PT (Server0). Barra de herramientas de dibujo/cables abajo (etiqueta "Fiber").
- **Derecha:** diagrama de topología limpio tipo árbol. Un **Router0 (2911)** en la cima; debajo, tres switches **2960-24TT** (Switch0, Switch1, Switch2). Switch0 → PC1, PC2; Switch1 → PC3, PC4; Switch2 → PC5, PC6. Todos los PC son iconos PC-PT. Marcadores verdes triangulares (enlaces activos) sobre cada conexión. Rótulo "Cisco Packet Tracer".

## Slide 5

**Our course**

Texto: Capture, inspect, and analyze real network traffic to understand network protocols (e.g., TCP, UDP, ICMP, HTTP, DNS) at a deep level, troubleshooting network issues, and monitoring security threats.

**Visual (lo que faltaba):** dos figuras que contrastan teoría vs. práctica real.

- **Izquierda — infografía "7 Layers of the OSI Model" (fuente: BMC).** Ícono de laptop con barra de búsqueda `https://` arriba. Pila de 7 capas de color, cada una con nombre + rol + ejemplos:
  - 7. Application — End User layer — HTTP, FTP, IRC, SSH, DNS
  - 6. Presentation — Syntax layer — SSL, SSH, IMAP, FTP, MPEG, JPEG
  - 5. Session — Synch & send to port — API's, Sockets, WinSock
  - 4. Transport — End-to-end connections — TCP, UDP
  - 3. Network — Packets — IP, ICMP, IPSec, IGMP
  - 2. Data Link — Frames — Ethernet, PPP, Switch, Bridge
  - 1. Physical — Physical structure — Coax, Fiber, Wireless, Hubs, Repeaters
- **Derecha — captura real de Wireshark** (archivo `odd-http.pcap`, tema oscuro, macOS). Barra de herramientas con íconos; barra de filtro "Apply a display filter … <⌘/>"; botones de coloreo "TCP", "Squirrels", "Not Squirrels". El panel de lista muestra ~10 paquetes TCP entre `200.121.1.131` y `172.16.0.122`, con columnas No./Time/Source/Destination/Protocol/TCP Seg Len/Length/Info; los Info incluyen `[ACK] Seq=1`, `[TCP ACKed unseen segment]`, `[TCP Spurious Retransmission]`, `[TCP Window Update]`, `[TCP Dup ACK]`. Panel de detalles desglosa Frame 1 (1454 bytes on wire), Ethernet II, Internet Protocol Version 4 (Src 200.121.1.131, Dst 172.16.0.122), Transmission Control Protocol (Source Port 10554, Destination Port 80, Seq 1, Ack 1, Len 1400, Stream index 0, "Conversation completeness: Incomplete (28)"). Panel inferior con volcado hexadecimal + ASCII. Pie: "Packets: 3083 · Displayed: 3083 (100.0%) · Profile: Default". Rótulo "Source: BMC".

## Slide 6

**What is wireshark used for?**

Wireshark is commonly used for:

- Network troubleshooting
- Security analysis
- Protocol development
- Educational purposes (learning how networks function)
- Packet-level network analysis

Slide de solo texto (lista de viñetas).

## Slide 7

**Wireshark**

Texto: Wireshark is a packet sniffer. Popular: ~1 million downloads monthly.

**Visual (lo que faltaba):** diagrama de arquitectura de un packet sniffer (fuente Kurose). Muestra dónde se ubica Wireshark respecto al SO:

- Ícono de computadora a la izquierda con flechas "to/from network".
- Recuadro grande sombreado = "packet sniffer". Dentro, en **user space**, un bloque **packet analyzer** conectado (flecha bidireccional) a un bloque **packet capture (pcap)** que está en el nivel de **operating system**.
- Al pcap llega una flecha rotulada "copy of all frames sent and received over interface (link)" desde la pila de red del kernel.
- Pila de red (derecha): **Application (e.g., Web browser)** en user space; debajo de la línea punteada "user space / operating system": **Transport (TCP/UDP)**, **Network (IP)**, **Link (Ethernet, 802.11)**, **Physical**, con flecha "to/from network".
- Anotaciones laterales: en verde "**User level:** from hello world to spotify and beyond" (arriba) y en rojo "**OS kernel:** linux, win, mac, etc." (abajo).
- Nota inferior: "On kernel, because: • Library functions associated to drivers. • Requires direct control on the link layer."

## Slide 8

**Wireshark**

Texto (repite): Wireshark is a packet sniffer. Popular: ~1 million downloads monthly.

**Visual (lo que faltaba):** infografía "**What is OSI Model?**" (fuente: ByteByteGo, banner negro). Ilustra la **encapsulación** de datos entre dos equipos:

- **Device A** (izquierda) → flecha → **Device B** (derecha), ambos iconos de monitor.
- A cada lado, la pila OSI numerada 7→1 con colores: 7 Application, 6 Presentation, 5 Session (verdes); 4 Transport (azul); 3 Network, 2 Data Link, 1 Physical (naranjas/amarillos).
- En el centro, secuencia descendente de "paquetes" que van ganando cabeceras (encapsulación): arriba un bloque solo con datos (verde+rosa), luego se le añade cabecera de transporte (azul), luego de red (naranja), luego de enlace (amarillo), hasta el nivel físico (bloque completo amarillo). Flecha verde hacia abajo en Device A (encapsula) y flecha verde hacia arriba en Device B (desencapsula). Rótulo "Source: ByteByteGo".

## Slide 9

**What is wireshark used for?**

Texto: **Example: NAT Protocol**

**Visual (lo que faltaba):** diagrama del funcionamiento de NAT (fuente: Xataka).

- Topología lineal: **Host** (`10.0.0.1`) — nube "Private Network" — **Router + NAT** (`150.150.0.1`) — nube "Internet" — **Server** (`200.100.10.1`).
- Debajo, cuatro cabeceras de paquete con campos Source IP / Destination IP mostrando cómo NAT reescribe direcciones:
  - **Lado privado, ida (arriba-izq):** Source IP `10.0.0.1` → Destination IP `200.100.10.1`.
  - **Lado público, ida (arriba-der):** Source IP `150.150.0.1` → Destination IP `200.100.10.1`. *(la IP origen cambió por NAT)*
  - **Lado privado, vuelta (abajo-izq):** Source IP `200.100.10.1` → Destination IP `10.0.0.1`.
  - **Lado público, vuelta (abajo-der):** Source IP `200.100.10.1` → Destination IP `150.150.0.1`.
- Flechas rojas punteadas rotuladas "**Changes according to NAT**" conectan los campos que se traducen. Flechas gris grandes indican el sentido del tráfico. Rótulo "Source: Xataka".

## Slide 10

**Outline.** Misma lista de 5 secciones; ahora la barra activa (azul) es **Installation**. Introduction en gris arriba, Getting started / Test / Conclusions en gris debajo.

## Slide 11

**Get Wireshark**

Texto:

```
http://www.wireshark.org/download.html
```

Available for: Windows, Mac, Linux

**Don't forget to restart your computer.** *(en rojo)*

Install in Ubuntu:

```bash
1. sudo apt install wireshark
2. Select YES (for root privileges on the pop up window) or (manually):
   sudo dpkg-reconfigure wireshark-common
   sudo usermod -aG wireshark <yourusername>
```

*(Nota: en la slide aparece "dpkq-reconfigure", errata por `dpkg-reconfigure`.)*

**Visual (lo que faltaba):** captura del navegador en `wireshark.org/download.html`. Banner azul "Join us June 14–19 in Richmond, Virginia for SharkFest'25 US…", logo WIRESHARK, texto "The current stable release of Wireshark is 4.4.5. It supersedes all previous releases." Lista desplegada **Stable Release: 4.4.5** con enlaces de descarga: Windows x64 Installer, Windows Arm64 Installer, Windows x64 PortableApps®, macOS Arm Disk Image, macOS Intel Disk Image, Source Code. Debajo "Old Stable Release: 4.2.11". Pop-up inferior "Big News: Introducing Stratoshark – 'Wireshark for the Cloud'!".

## Slide 12

**Outline.** Barra activa (azul) = **Getting started**. Introduction e Installation en gris arriba; Test y Conclusions en gris debajo.

## Slide 13

**First steps**

Pasos numerados (con globos azules ①②③ superpuestos sobre la captura para señalar cada punto):

1. **Execute Wireshark** *(verde)*
2. **Select a network interface:** *(morado)* — Ethernet (eth, en) o Wireless (w, en)
3. **Start capturing!** *(rojo)*

**Visual (lo que faltaba):** captura de la pantalla de bienvenida de Wireshark en macOS, título "The Wireshark Network Analyzer".

- **①** apunta a la barra de herramientas superior (íconos de captura: aleta azul = start, cuadro rojo = stop, engranaje = capture options, etc.) y a la barra de filtro "Apply a display filter … <⌘/>".
- **③** apunta al botón de iniciar captura (aleta azul).
- Panel "**Welcome to Wireshark**" → sección "**Capture**", campo "…using this filter: [Enter a capture filter …]", desplegable "All interfaces shown".
- **②** apunta a la **lista de interfaces**: **Wi-Fi: en0** (resaltada en azul, con sparkline de tráfico), awdl0, llw0, utun0, utun1, USB 10/100/1000 LAN: en5 (con sparkline), Loopback: lo0, Thunderbolt Bridge: bridge0, Thunderbolt 1: en1, Thunderbolt 2: en2, gif0, stf0, ap1, y capturas remotas: Cisco remote capture (ciscodump), Random packet generator (randpkt), SSH remote capture (sshdump), UDP Listener remote capture (udpdump).

## Slide 14

**Change interface**

Solo título; el contenido es la captura anotada.

**Visual (lo que faltaba):** captura del diálogo "**Wireshark · Capture Options**" (macOS, interfaz activa "Wi-Fi: en0"). Una **flecha azul** señala el ícono de **engranaje** (Capture Options) en la barra de herramientas.

- Pestañas: **Input** (activa) / Output / Options.
- Tabla de interfaces con columnas: **Interface | Traffic | Link-layer Header | Promisc | Snaplen (B) | Buffer (MB) | Mon**.
  - **Wi-Fi: en0** (fila seleccionada, azul) — Ethernet — Promisc ✓ — Snaplen default — Buffer 2. Subfila: "Addresses: fe80::1c3d:5df1:e3f4:5d16, 192.168.68.103".
  - awdl0 — Ethernet; llw0 — Ethernet; utun0 — BSD loopback; utun1 — BSD loopback; USB 10/100/1000 LAN: en5 — Ethernet; Loopback: lo0 — BSD loopback; Thunderbolt Bridge: bridge0 — Ethernet; Thunderbolt 1: en1 — Ethernet; Thunderbolt 2: en2 — Ethernet; gif0 — BSD loopback; stf0 — BSD loopback; ap1 — Ethernet. Todas con Promisc ✓, Snaplen default, Buffer 2.
- Checkbox "☑ Enable promiscuous mode on all interfaces".
- Campo "Capture filter for selected interfaces: [Enter a capture filter …]", botones "Manage Interfaces…", "Compile BPFs".
- Botones inferiores: Help, Close, **Start** (azul).

## Slide 15

**Expected output**

Texto:

- **Packet:** unit in network layer *(rojo)*
- **Frame:** unit in data link layer. *(verde)*

**Visual (lo que faltaba):** captura completa de Wireshark (archivo `intro-wireshark-trace.pcap`) con **rótulos que identifican cada zona de la interfaz** (flechas hacia cada panel):

- **command menus** → barra de menús (Wireshark / File / Edit / View / Go / Capture / Analyze / Statistics / Telephony / Wireless / Tools / Help) + barra de herramientas.
- **display filter specification** → barra "Apply a display filter … <⌘/>".
- **listing of captured packets** → tabla de paquetes (No./Time/Source/Destination/Protocol/Length/Info). Se ven paquetes 280–291 entre `10.0.0.44` y `128.119.245.12`: varios TCP con `[SYN]`, `[SYN, ACK]`, `[ACK]`; el paquete **286** es **HTTP** `GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1` (904 bytes); el **288** es HTTP `HTTP/1.1 200 OK (text/html)`; el **290** HTTP `GET /favicon.ico HTTP/1.1`.
- **Details of selected packet** → árbol del Frame 286: "Frame 286: 904 bytes on wire (7232 bits)…", "Ethernet II, Src: Apple_98:d9:27 (78:4f:43:98:d9:27), Dst: Intel_80:00:00 (00:50:f1:80:00:00)", "Internet Protocol Version 4, Src: 10.0.0.44, Dst: 128.119.245.12" (expandido: Version 4, Header Length 20 bytes, Total Length 890, Identification 0x0000, Flags 0x4000 Don't fragment, TTL 64, Protocol TCP (6), Header checksum 0xb7ce, Source 10.0.0.44, Destination 128.119.245.12), "Transmission Control Protocol, Src Port: 53962, Dst Port: 80, Seq: 1, Ack: 1, Len: 838", "Hypertext Transfer Protocol".
- **packet content (in hexadecimal and ASCII)** → panel inferior con volcado hex + columna ASCII (se lee "$·GET /w ireshark -labs/IN TRO-wire shark-fi le1.html HTTP/1. 1··Host: gaia.cs .umass.e").
- Pie: "Packets: 651 · Displayed: 651 (100.0%) · Dropped: 0 (0.0%) · Profile: Default".

## Slide 16

**Outline.** Barra activa (azul) = **Test**. Introduction / Installation / Getting started en gris arriba; Conclusions en gris debajo.

## Slide 17

**Test**

Instrucciones del laboratorio:

- **Start** the capture.
- **Open** a browser and access: `https://www.cisco.com/`
- **Stop** the capture.
- **Filter** http messages.

**Visual (lo que faltaba):** captura de Wireshark (interfaz "USB 10/100/1000 LAN: en5") mostrando el resultado del filtro. Una **flecha azul** apunta desde el texto de instrucciones hacia la barra de filtro.

- Barra de filtro con `http` escrito (fondo verde = filtro válido).
- Lista muestra solo 2 paquetes HTTP tras filtrar:
  - **346** 43.977951 — Src `192.168.68.102` → Dst `128.119.245.12` — HTTP — 466 — `GET /wireshark-labs/INTRO-wireshark-file1…`
  - **348** 44.094851 — Src `128.119.245.12` → Dst `192.168.68.102` — HTTP — 504 — `HTTP/1.1 200 OK (text/html)`
- Panel de detalles del Frame 346 (466 bytes on wire): Ethernet II (Src RealtekS_68:09:34 00:e0:4c:68:09:34, Dst Tp-LinkT_95:b6:cc 3c:84:6a:95:b6:cc), IPv4 (Src 192.168.68.102, Dst 128.119.245.12), TCP (Src Port 51706, Dst Port 80, Seq 1, Ack 1, Len 400), Hypertext Transfer Protocol (resaltado).
- Panel hex/ASCII abajo (se lee "···GET /w ireshark -labs/IN TRO-wire shark-fi le1.html HTTP/1. 1··Host: gaia.cs .umass.e du··Upgr ade-Inse cure-Req uests: 1 ··Accept : text/h tml,appl ication/ xhtml+xm l,applic").
- Pie: "Hypertext Transfer Protocol: Protocol … Packets: 891 · Displayed: 2 (0.2%) · Profile: Default".
