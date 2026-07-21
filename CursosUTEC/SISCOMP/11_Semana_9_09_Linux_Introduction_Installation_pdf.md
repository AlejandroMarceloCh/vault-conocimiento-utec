---
curso: SISCOMP
titulo: 11 - Semana 9/09. Linux Introduction & Installation
slides: 18
fuente: 11 - Semana 9/09. Linux Introduction & Installation.pdf
---

## Slide 1

Portada (decorativa: fondo azul de túnel tecnológico con figura humanoide).

**COMPUTING SYSTEMS**
Linux Introduction & Installation
Professor: Luz Adanaque

## Slide 2

Slide de agenda con foto decorativa (científica de laboratorio a la izquierda).

**Motivation**
- To become familiar with the Linux environment as a foundation for system-level work.
- To understand why Linux is widely used in programming, servers, and embedded systems.

**Goals**
- Install and run Linux inside a virtual machine using QEMU.
- Practice essential shell commands.

## Slide 3

**Summary** (índice con foto decorativa de mujer con visor VR y globo terráqueo). Cada punto tiene un ícono a su izquierda:

1. From ISA to OS (ícono portapapeles/lista)
2. About Linux (ícono bombilla)
3. Installing Linux in a VM (ícono bombilla)
4. Basic shell commands (ícono utensilios/herramientas)

## Slide 4

Slide separador de sección (decorativa: mano robótica tocando globo digital).

**1. From ISA to OS**

## Slide 5

**Why Move Beyond the ISA?**

- The ISA defines how the **processor executes instructions**. **But running real programs requires more than instructions.**
- We need a system **that manages memory, files, and hardware** — that's the Operating System.

VISUAL — Diagrama de capas de abstracción (torre vertical, de arriba hacia abajo). Cada fila tiene un nombre de capa (izquierda), un ícono/símbolo (centro) y los elementos que maneja (derecha):

| Capa | Elementos (derecha) |
|------|---------------------|
| Application Software (con recuadro `>"hello world!"`) | programs |
| **Operating Systems** (fila resaltada en rosa; ícono de laptop) | device drivers, kernel |
| Architecture (ícono de registros/instrucciones) | instructions, registers |
| Micro-architecture (ícono de datapaths con flechas) | datapaths, controllers |
| Logic (ícono de sumador `+`) | adders, memories |
| Digital Circuits (ícono compuerta AND) | AND gates, NOT gates |
| Analog Circuits (ícono amplificador) | amplifiers, filters |
| Devices (ícono transistor) | transistors, diodes |
| Physics (ícono átomo) | electrons |

La capa del OS (device drivers + kernel) queda resaltada como el foco del tema.

## Slide 6

**ISA Limitations**

- Directly programming hardware is powerful **but complex**.
- Every task (I/O, storage, multitasking) must be **manually controlled**.
- **Hard to scale** beyond simple demos or embedded systems.
  - **Need abstraction layers for efficiency and safety.**

**That why, the OS abstracts the hardware!**

VISUAL — Diagrama "OS Abstraction layers and their Interfaces" (título al pie). Muestra bloques apilados con líneas horizontales de colores que marcan las interfaces entre capas:
- Bloques (de arriba a abajo): **Application programs** → **Libraries/utilities** → **Operating system** → **Execution hardware** → (base) **System interconnect (bus)** + **Memory translation** + **I/O devices and networking** + **Main memory**.
- Etiquetas de interfaces al margen izquierdo, cada una con su línea de color:
  - **API** (verde) — Application Programming Interface, entre Application programs y Libraries.
  - **ABI** (azul-verde) — Application Binary Interface.
  - **I** (azul) — Instruction interface (entre Libraries y OS).
  - **IS** (rojo) — Instruction Set (entre OS y hardware).
  - **A** (rojo) — línea que separa el software del Execution hardware.

## Slide 7

**The Operating System**

- **Definition**
  - **A program that controls** the **execution of application** programs.
  - An **interface** between **applications and hardware**.
- **With 3 important keys:**
  - **Convenience**: Simple to use, from the programmer's perspective.
  - **Efficiency**: Important metric related to the specific task.
  - **Ability to evolve**: Permits the effective development, testing, and introduction of new system functions without interfering with service.

VISUAL — El mismo diagrama de la slide 6 ("OS Abstraction layers and their Interfaces"): pila de bloques (Application programs / Libraries-utilities / Operating system / Execution hardware / System interconnect + Memory translation + I/O devices + Main memory) con las interfaces AP, ABI, I, IS, A marcadas al margen izquierdo.

## Slide 8

Slide separador de sección (decorativa: mano robótica y globo digital).

**2. About Linux**

## Slide 9

**What is Linux?**

- Linux is a free and open-source kernel based on **Unix**.
- Created by **Linus Torvalds** in 1991.
- Uses a **monolithic architecture** that manages hardware, memory, and **processes**.

**What is a kernel?**
- The kernel is the core part of an OS **between the hardware and user programs**, managing how applications use CPU, memory, storage, and devices.

**So, Linux is not the OS itself!**

VISUALES:
1. Diagrama de arquitectura del kernel de Linux (esquina superior derecha) — muestra el stack gráfico/OpenGL. De arriba a abajo y de izquierda a derecha:
   - **3D computer game** → **Geometry data / Texture data / Sound data** → **Game engine**.
   - Nota lateral: "OpenGL commands or shaders written in GLSL (vertex, tessellation control, tessellation evaluation, geometry, fragment and compute shaders)".
   - **Windowing library (SDL, GLFW, etc.)** → **Subroutines**; **GNU C Library** → **Subroutines**; a la derecha **Mesa 3D** y **DRM library → Subroutines**.
   - Flechas de "system calls" y "subroutine calls" bajan a la banda roja **System Call Interface (SCI)**.
   - Bloque **Linux kernel** (rojo): Process scheduler, Memory manager, Other Linux kernel subsystems, KMS, DRM.
   - Base **Hardware** (naranja/azul): CPU, System RAM, Devices, Screen, Display controller, Graphics RAM, GPU.
2. **Tux**, el pingüino mascota de Linux (etiqueta: "↑ Tux. The mascot of Linux").
3. Foto de **Linus Torvalds** (etiqueta: "← Linus Torvalds").

## Slide 10

**Linux Distros**

**There are a LOT of distros!!!**
**Distro popularity rankings**

VISUALES:
1. Captura de pantalla del sitio **DistroWatch.com** ("Put the fun back into computing. Use Linux, BSD."). Muestra la interfaz con barra de navegación (Noticias/Opiniones/Reseñas, Paquetes, Buscar/Enviar distribución, Tutoriales y aprendizaje, Recursos relacionados), una columna "Las más nuevas distribuciones" (AnduinOS 1.4.0, Talos 1.11.3, Mobian 13.0, Athena 25.11, HackerOS 3.3, Zorin 18, CentOS, FunOS 25.10, Peppermint, TUXEDO, Manjaro 25.0.10, Tails 7.1, Mint) y una noticia destacada "Distribution Release: Mobian 13.0" (fecha 2025-10-15).
2. Tabla lateral derecha **"Las más visitadas"** — ranking DistroWatch, Período: Last 6 months, columnas Puesto / Distribución / HPD (hits por día):

| Puesto | Distribución | HPD |
|--------|-------------|-----|
| 1 | CachyOS | 4168 |
| 2 | Mint | 2643 |
| 3 | MX Linux | 1781 |
| 4 | Debian | 1666 |
| 5 | EndeavourOS | 1378 |
| 6 | Pop!_OS | 1269 |
| 7 | Manjaro | 1097 |
| 8 | Ubuntu | 1076 |
| 9 | Fedora | 987 |
| 10 | AnduinOS | 931 |
| 11 | Zorin | 915 |
| 12 | openSUSE | 833 |
| 13 | Nobara | 697 |
| 14 | NixOS | 580 |
| 15 | Bluestar | 569 |
| 16 | elementary | 546 |
| 17 | KDE neon | 525 |
| 18 | BigLinux | 501 |
| 19 | TUXEDO | 471 |
| 20 | Garuda | 465 |
| 21 | antiX | 457 |
| 22 | AlmaLinux | 428 |
| 23 | Kali | 413 |
| 24 | Q4OS | 399 |
| 25 | SparkyLinux | 393 |
| 26 | FreeBSD | 377 |
| 27 | EasyOS | 350 |

3. Logos de tres distros populares en la parte inferior: **Ubuntu**, **Linux Mint**, **Debian** (espiral).

## Slide 11

**Linux Current Usage**

- Runs **everywhere**: from supercomputers to smartphones and IoT devices.
- Dominates servers: most web servers and cloud systems **run on Linux** (e.g. AWS, Google Cloud).
- **Android is based on the Linux kernel.**
- Used in **development**: preferred by programmers, DevOps, and cybersecurity professionals.

VISUALES:
1. Infografía de Intel **"LINUX BY THE NUMBERS"** (fondo azul) con estadísticas:
   - **99%+** of the top high performance computing systems run on Linux.
   - **80%** of the IoT market runs on Linux.
   - **90%** of the world's stock exchanges are powered by Linux.
   - **3,900+** Linux developers worldwide.
   - Bullet trains, nuclear subs & Roku streaming boxes all run on Linux.
   - **200+** Linux distributions are listed by Wikipedia.
   - Linux kernel has over **19 MILLION** lines of code.
   - Intel is the **#1** Linux kernel contributor.
2. Logos de proveedores cloud abajo: **Google Cloud**, **aws** (Amazon Web Services), **Azure** (A).

## Slide 12

Slide separador de sección (decorativa: mano robótica y globo digital).

**3. Installing Linux in a VM**

## Slide 13

**Requirements**

- **Operating System**: A Windows 10 or 11 machine (this guide assumes Windows).
- **Virtualization Support**: Enabled in BIOS/UEFI
  - Look for Intel VT-x or AMD-V options.
  - Check your computer manufacturer's manual if unsure.
- **Disk Space**: At least 20 GB of free storage for the virtual machine.
- **Memory**: Minimum 4 GB RAM (8 GB recommended).

VISUALES:
1. Logo grande de **QEMU** (pájaro naranja/negro con texto "QEMU"). Texto: "We will be using **QEMU** as our hypervisor."
2. Banner promocional de QEMU ("A generic and open source machine emulator and virtualizer") con tres capturas de pantalla que ilustran sus modos: **Full-system emulation** (run operating systems for any machine, on any supported architecture), **User-mode emulation** (run programs for another Linux/BSD target, on any supported architecture), **Virtualization** (run KVM and Xen virtual machines with near native performance).

## Slide 14

**QEMU INSTALLATION & ISO PREPARATION**

- **Download QEMU from** https://qemu.weilnetz.de/w64/ (Search for the "QEMU installer" under the base directory.)
- Run the installation wizard and make sure to enable the "Add QEMU to System PATH" option.
- Open a terminal window, and check the qemu installed version, using the following command:

```
qemu-system-x86_64 --version
```

- **After this, download the Ubuntu distro .iso from** https://ubuntu.com/download/desktop

VISUAL — Captura del listado de directorio **"QEMU Binaries for Windows (64 bit)"** de qemu.weilnetz.de/w64/. Tabla con columnas Name / Last modified / Size / Description:

| Name | Last modified | Size | Description |
|------|---------------|------|-------------|
| Parent Directory | - | - | |
| 2011/ … 2025/ (carpetas por año) | varias fechas | - | experimental QEMU for Windows |
| old/ | 2023-06-02 21:50 | - | |
| qemu-w64-setup-20250819.exe | 2025-08-19 22:27 | 172M | QEMU Installer for Windows (64 bit) |
| qemu-w64-setup-20250819.sha512 | 2025-08-19 22:28 | 158 | SHA-512 for installer |
| qemu-w64-setup-20250826.exe | 2025-08-26 21:48 | 172M | QEMU Installer for Windows (64 bit) |
| qemu-w64-setup-20250826.sha512 | 2025-08-26 21:48 | 158 | SHA-512 for installer |

Pie: "https://qemu.weilnetz.de/w64/ directory."

## Slide 15

**QEMU INSTALLATION & ISO PREPARATION**

- Create a virtual QEMU DISK at your preferred local pwd.
  - Run the command qemu-img create wizard and make sure to enable the "Add QEMU to System PATH" option.

```
cd C:\qemu
qemu-img create -f qcow2 ubuntu_disk.qcow2 20G
```

- With the Ubuntu .iso and QEMU disk created, use the following to start the vm:

```
qemu-system-x86_64 -m 4096 -cdrom ubuntu.iso -boot d -hda ubuntu_disk.qcow2
```

Explicación de los flags (en el diagrama):
- `-m 4096`: assigns 4 GB of RAM.
- `-cdrom ubuntu.iso`: specifies the installer.
- `-boot d`: boots from the CD.
- `-hda ubuntu_disk.qcow2`: the destination disk for the installation.

Nota al pie (en rojo): "If the commands fails, make sure the qemu installation directory is added to the user PATH."

## Slide 16

Slide separador de sección (decorativa: mano robótica y globo digital).

**4. Basic shell commands**

## Slide 17

**Basic Shell commands**

After the initial Ubuntu setup, open a terminal using: **CTRL + ALT + T**

1. **ls** – Lists files and directories in the current folder.
2. **pwd** – Prints the current working directory (shows where you are).
3. **cd** – Changes the current directory.
4. **cp** – Copies files or directories.
5. **mv** – Moves or renames files and directories.
6. **rm** – Removes (deletes) files or directories.
7. **source** – Runs a script in the current shell environment.
8. **export** – Sets environment variables.
9. **exit** – Closes the current terminal session.

**Try this commands!**

VISUAL — Flecha grande apuntando a una captura del **terminal por defecto de Ubuntu** (ventana con marco naranja, barra de título "mark@linux-desktop: ~", menú File/Edit/View/Search/Terminal/Help, prompt verde `mark@linux-desktop:~$` sobre fondo púrpura oscuro). Etiqueta: "Ubuntu default terminal."

## Slide 18

**Reference Books**

- Patterson, D. A., & Hennessy, J. L. (2020). *Computer Organization and Design RISC-V Edition: The Hardware Software Interface.* Morgan Kaufmann.
- "The elements of computing systems: building a modern computer from first principles" Nisan, N., & Schocken, S. (2021). MIT press.
- Silberschatz, A., Gagne, G., & Galvin, P. B. (2015). *Operating system concepts* (9th edition, international student version). John Wiley & Sons Inc.
- "Digital Design and Computer Architecture, RISC-V Edition". Morgan Kaufmann. Harris, S., & Harris, D. (2021).

(Foto decorativa: profesor escribiendo en pizarra frente a alumnos.)
