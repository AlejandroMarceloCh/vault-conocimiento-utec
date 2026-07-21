---
curso: INGSOFT
titulo: 04 - Semana 2/IS1 - Lab 2-1__pptx
slides: 7
fuente: 04 - Semana 2/IS1 - Lab 2-1__pptx.pdf
---

## Slide 1

Portada. Título **"Ingeniería de Software"**, subtítulo *"Laboratorio"*. Chrome decorativo (logo UTEC, "Reinventa el mundo", TransformaTec, imagen de fondo de un robot/humanoide en túnel tecnológico).

## Slide 2

Diagrama de arquitectura de **Zulip** (no aparece en el texto plano — es todo visual). Muestra el flujo de una petición desde el cliente hasta la base de datos, con tres agrupaciones punteadas: contorno rojo exterior **"Zulip"**, contorno azul **"Database"** y contorno verde **"Backend"**.

Componentes y conexiones:

- **Client** (caja naranja): etiquetado a la derecha como Web app, Desktop (Electron/Qt), iOS (React native), Android.
- Client ⇅ **NGINX** mediante flecha punteada bidireccional etiquetada **"HTTPS requests"**.
- **NGINX** (caja verde): recibe también `/static/*` desde un **"Static asset server"** (flecha entrante desde la derecha).
- NGINX ⇅ Backend mediante **"Reverse proxy"** (flechas bidireccionales hacia abajo).
- Dentro de **Backend** (recuadro verde punteado):
  - **django** (caja verde/teal) — "Application server". Recibe desde NGINX **"All other routes"**.
  - **Tornado** (caja azul) — "Realtime push server". Recibe/envía **"Events"** hacia NGINX.
  - django → Tornado (flecha).
- Dentro de **Database** (recuadro azul punteado): **PostgreSQL** (círculo azul) — "Persistent data storage".
- **PostgreSQL** ⇄ **django** mediante flecha bidireccional etiquetada **"DB queries"**.

Flujo resumido: Client → (HTTPS) → NGINX → (reverse proxy) → django (rutas generales) / Tornado (eventos en tiempo real); django consulta PostgreSQL.

## Slide 3

Título "Laboratorio de Software".

Texto: **Requerimiento 1**: Adicionar el número de usuarios suscritos a un canal en el menú del lado izquierdo.

Captura de pantalla de la UI de Zulip (parte derecha de la slide). Muestra la barra lateral izquierda de Zulip con:
- Sección superior: Combined feed, Mentions, Reactions, Starred messages, Drafts.
- **DIRECT MESSAGES**: "Iago, Zoe", "Prospero from The Tempest".
- **MY CHANNELS**: lista de canales con hashtag — announce (seleccionado), design, devel, errors, social, support, test, Verona, 조리법 😎, ビデオゲーム.
- Sobre el canal `announce` está abierto un menú contextual (popover) encabezado por **# announce**, cuya primera línea resaltada es **"12 subscribed users"**. Una flecha roja apunta desde el texto del requerimiento hacia esa línea "12 subscribed users".
- El resto del menú contextual: Mark all messages as read, Go to channel feed, Copy link to channel, Channel settings, Pin channel to top, Mute channel, Unsubscribe, Change color.
- Al fondo se ve una lista de compra (milk, eggs, bread, fruit) en el feed.

## Slide 4

Título "Laboratorio de Software".

Texto: **Requerimiento 2**: Adicionar el número de tópicos de un canal en el menú del lado izquierdo, indicando cuántos de ellos son "followed".

Captura de pantalla de la UI de Zulip. Barra lateral con DIRECT MESSAGES (Iago, Zoe; Prospero from The Tempest) y MY CHANNELS (announce, design, devel, errors, **social** expandido, support). Bajo `social` se ven sus tópicos: "my topic" (con icono de seguido ·))), "owned keurig is slowly", "OLD printer skipping erratically", "PLOTS".

Menú contextual (popover) abierto sobre el canal **# social** con las líneas:
- **12 subscribed users**
- **4 topics (1 followed)** ← una flecha roja apunta desde el texto del requerimiento hacia esta línea, resaltando el número de tópicos y cuántos son followed.
- Mark all messages as read, Go to channel feed, Copy link to channel, Channel settings, Pin channel to top, Mute channel, Unsubscribe, Change color.

## Slide 5

Título "Laboratorio de Software". Slide de solo texto (sin figuras nuevas).

- **Requerimiento no funcional**: Implementar nuevas APIs Backend para el requerimiento 2.
- Realizar los cambios solicitados y documentar en un diagrama de flujo qué elementos de software fueron modificados (archivos de UI, archivos de backend).
- Adjuntar captura de pantalla de los elementos añadidos (si posible, video).
- Casos de Prueba: Adicionar suscriptor, adicionar tópico, seguir un nuevo tópico.
- Adjuntar el Git Diff con los archivos modificados.

## Slide 6

Título "Laboratorio de Software". Slide de solo texto (enlaces de referencia).

- **Installation Guide**: https://zulip.readthedocs.io/en/latest/development/setup-recommended.html
- **Arquitectura**: https://zulip.readthedocs.io/en/latest/overview/architecture-overview.html
- **Entender la estructura de directorios**: https://zulip.readthedocs.io/en/latest/overview/directory-structure.html

## Slide 7

Cierre. **"GRACIAS"**, autor *CHRISTIAN PAZ TRILLO*. Chrome decorativo (fondo de laboratorio, logo UTEC, TransformaTec).
