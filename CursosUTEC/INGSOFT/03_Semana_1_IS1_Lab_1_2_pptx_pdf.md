---
curso: INGSOFT
titulo: 03 - Semana 1/IS1 - Lab 1-2__pptx
slides: 5
fuente: 03 - Semana 1/IS1 - Lab 1-2__pptx.pdf
---

## Slide 1

Portada. Título grande "Ingeniería de Software", subtítulo "Laboratorio". Fondo decorativo (túnel tecnológico azul con silueta de figura caminando). Logo UTEC, "Reinventa el mundo" y "TransformaTec" son chrome decorativo.

## Slide 2

**Laboratorio de Software**

Objetivos del laboratorio (hands-on):

- Hands-on: hoy y mañana
- Levantar Zulip en local y correr en localhost:9991
- Realizar un cambio en algún mensaje de localización en español y visualizarlo.
- https://zulip.readthedocs.io/en/latest/contributing/contributing.html

(Solo texto en viñetas; el banner superior con figuras es decorativo.)

## Slide 3

**Diagrama de arquitectura de Zulip** (captura del diagrama oficial de architecture-overview). Muestra el flujo de una petición desde el cliente hasta la base de datos, con los componentes agrupados en cajas punteadas.

Componentes y flujo (de arriba hacia abajo):

- **Client** (caja naranja): Web app / Desktop (Electron/Qt) / iOS (React native) / Android.
- El Client se comunica con el backend vía **HTTPS requests** (flecha punteada bidireccional).
- Todo está encerrado en un contorno punteado rojo etiquetado **"Zulip"**.
- **NGINX** (caja verde): recibe las HTTPS requests. Sirve los assets estáticos: `/static/*` → "Static asset server" (flecha entrante). Actúa como **Reverse proxy** hacia el backend.
- Grupo **Backend** (contorno punteado verde):
  - **django** — "Application server". NGINX enruta hacia django con la etiqueta **"All other routes"**.
  - **Tornado** — "Realtime push server". NGINX enruta los **"Events"** hacia Tornado. django se conecta a Tornado (flecha django → Tornado).
- Grupo **Database** (contorno punteado azul):
  - **PostgreSQL** (círculo azul) — "Persistent data storage".
  - django ↔ PostgreSQL mediante **DB queries** (flecha bidireccional etiquetada "DB queries").

Esquema del flujo:

```
Client (Web/Desktop/iOS/Android)
   │  HTTPS requests
   ▼
NGINX  ◄── /static/*  (Static asset server)
   │  Reverse proxy
   ├── All other routes ──► django (Application server) ◄── DB queries ──► PostgreSQL (Persistent data storage)
   │                             │
   └── Events ──────────────► Tornado (Realtime push server)  ◄── django
```

## Slide 4

**Laboratorio de Software** — Enlaces de referencia.

- **Installation Guide:** https://zulip.readthedocs.io/en/latest/development/setup-recommended.html
- **Arquitectura:** https://zulip.readthedocs.io/en/latest/overview/architecture-overview.html
- **Entender la estructura de directorios:** https://zulip.readthedocs.io/en/latest/overview/directory-structure.html

(Solo texto/enlaces.)

## Slide 5

Slide de cierre. Texto grande "GRACIAS", subtítulo con el nombre del profesor "CHRISTIAN PAZ TRILLO". Fondo decorativo (foto de laboratorio con estudiantes). Chrome decorativo.
