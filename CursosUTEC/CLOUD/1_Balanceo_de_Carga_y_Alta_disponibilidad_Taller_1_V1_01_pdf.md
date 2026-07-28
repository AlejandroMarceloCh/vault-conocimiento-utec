---
curso: CLOUD
titulo: 1. Balanceo de Carga y Alta disponibilidad - Taller 1 - V1.01
slides: 21
fuente: 1. Balanceo de Carga y Alta disponibilidad - Taller 1 - V1.01.pdf
---

## Slide 1

Portada del curso. Texto: "CS2032 - Cloud Computing (Ciclo 2024-1) / Balanceo de Carga y Alta disponibilidad" con subtítulo "Semana 6 - Taller 1: Balanceador de Carga". Autor: "Elaborado por: Geraldo Colchado". Logo UTEC en esquina superior derecha (decorativo). Franja naranja decorativa en el pie.

## Slide 2

Slide de "Contenido" (agenda), con barra lateral naranja con el título "Contenido / Balanceador de Carga". Lista numerada de 7 puntos (ítem 1 "Objetivo del taller 1" en negrita/subrayado, indicando que es el punto activo):
1. Objetivo del taller 1
2. Ejercicio 1: Crear 2 MV para producción
3. Ejercicio 2: Crear Balanceador de Carga
4. Ejercicio 3: Probar Balanceo de Carga y Alta disponibilidad
5. Ejercicio 4: Desplegar contenedor de página web en 2 MV de producción en puerto 8080
6. Ejercicio 5: Diagrama de Arquitectura de Solución
7. Cierre

## Slide 3

Título: "Objetivo del taller 1: Balanceador de Carga". Contenido de texto (un solo bullet):
- Probar Balanceo de Carga y Alta disponibilidad

No hay elementos visuales adicionales.

## Slide 4

Slide de "Contenido" (agenda) repetida, mismo listado de 7 puntos que la Slide 2, ahora con el ítem 2 "Ejercicio 1: Crear 2 MV para producción" resaltado en negrita/subrayado como punto activo.

## Slide 5

Título: "Ejercicio 1: Crear 2 MV para producción". Instrucciones paso a paso (texto con partes resaltadas en azul y amarillo indicando valores clave a completar):
- Paso 1: Cree una máquina virtual con la AMI pública más reciente de Origen = amazon/Cloud9Ubuntu y nómbrela como "MV Prod 1" y cree un grupo de seguridad nuevo "GS-Prod" y abra puertos 22 y 80 (botón Editar).
- Paso 2: Cree una máquina virtual con la AMI pública más reciente de Origen = amazon/Cloud9Ubuntu y nómbrela como "MV Prod 2" y asigne grupo de seguridad existente "GS-Prod" y que esté en una **Zona de Disponibilidad diferente a la anterior MV (Elegir Subred)** — este último fragmento resaltado en amarillo como dato crítico.

## Slide 6

Slide de "Contenido" (agenda) repetida, mismo listado de 7 puntos, ahora con el ítem 3 "Ejercicio 2: Crear Balanceador de Carga" resaltado en negrita/subrayado como punto activo.

## Slide 7

Título: "Ejercicio 2: Crear Balanceador de Carga".
- Paso 1: Crear un Target Group con las 2 máquinas virtuales o instancias para el puerto 80.

Captura de pantalla de la consola de AWS mostrando el menú lateral "Equilibrio de carga" con las opciones "Balanceadores de carga" y "Grupos de destino" (con etiqueta "New" y un check ✓ en rojo señalando esta última). A la derecha, formulario de creación de Target Group con los campos:

| Campo | Valor |
|---|---|
| Target group name | TG-Prod-80 (resaltado en amarillo) |
| Protocol | HTTP (resaltado en amarillo) |
| Port | 80 (resaltado en amarillo) |

- Paso 2: Crear balanceador de carga (texto, sin captura en esta slide).

## Slide 8

Título: "Ejercicio 2: Crear Balanceador de Carga" (continuación, sin bullets de texto adicionales, solo capturas).

Captura izquierda: panel "Application Load Balancer" con diagrama esquemático que muestra un usuario (icono de laptop) conectándose mediante líneas punteadas a un bloque "ALB" que se ramifica en dos cajas "HTTP" y "HTTPS" (HTTPS resaltado en naranja), y desde ahí flechas hacia 3 íconos circulares representando destinos: Lambda (ícono λ), contenedores (ícono hexagonal) e instancias/EC2 (ícono de chip). Debajo, texto descriptivo: "Choose an Application Load Balancer when you need a flexible feature set for your applications with HTTP and HTTPS traffic. Operating at the request level, Application Load Balancers provide advanced routing and visibility features targeted at application architectures, including microservices and containers." Botón "Create" con check ✓ en rojo.

Captura derecha: formulario "Basic configuration" de creación del Load Balancer:
- Load balancer name: **lb-prod** (resaltado en amarillo)
- Security groups: lista con "default" (sg-073c8ac561aaa5255) y **GS-Prod** (sg-0915a314910929f9b, resaltado en amarillo), ambos en VPC vpc-0a3529c5417b25da4.

## Slide 9

Título: "Ejercicio 2: Crear Balanceador de Carga" (continuación). Sin bullets de texto, solo una captura de pantalla:

Panel de configuración de "Listener HTTP:80" (resaltado en amarillo):
- Protocol: HTTP, Port: 80 (rango permitido 1-65535)
- Default action: **Forward to** → **TG-Prod-80** (HTTP) — Target type: Instance, IPv4 (ambos "Forward to" y "TG-Prod-80" resaltados en amarillo)

## Slide 10

Slide de "Contenido" (agenda) repetida, mismo listado de 7 puntos, ahora con el ítem 4 "Ejercicio 3: Probar Balanceo de Carga y Alta disponibilidad" resaltado en negrita/subrayado como punto activo.

## Slide 11

Título: "Ejercicio 3: Probar Balanceo de Carga y Alta disponibilidad".
- Paso 1: Editar la página de inicio de Apache en las 2 Máquinas Virtuales
- Paso 2: Probar con el enlace del balanceador de carga varias veces

Dos capturas de pantalla lado a lado de navegador web, ambas apuntando a la misma URL del balanceador de carga (resaltada en amarillo: `lb-prod-1751801894.us-east-1.elb.amazonaws.com`), mostrando la página por defecto "Apache2 Ubuntu Default Page":
- Captura izquierda: banda roja con texto "It works! (Ambiente producción 1)" — respuesta servida por la MV Prod 1.
- Captura derecha (con icono de Ubuntu visible, barra "No es seguro"): banda roja con texto "It works! (Ambiente producción 2)" — respuesta servida por la MV Prod 2.

Esto demuestra que el balanceador alterna las respuestas entre las dos instancias (round-robin), evidenciando el balanceo de carga funcionando. Ambas páginas incluyen el texto estándar de Apache indicando reemplazar el archivo en `/var/www/html/index.html`.

## Slide 12

Título: "Ejercicio 3: Probar Balanceo de Carga y Alta disponibilidad" (continuación). Lista de pasos para probar alta disponibilidad:
- Paso 3: Detener la instancia "MV Prod 1" y probar
- Paso 4: Detener la instancia "MV Prod 2" y probar
- Paso 5: Iniciar la instancia "MV Prod 1" y probar
- Paso 6: Iniciar la instancia "MV Prod 2" y probar

Sin imágenes, solo texto.

## Slide 13

Slide de "Contenido" (agenda) repetida, mismo listado de 7 puntos, ahora con el ítem 5 "Ejercicio 4: Desplegar contenedor de página web en 2 MV de producción en puerto 8080" resaltado en negrita/subrayado como punto activo.

## Slide 14

Título: "Ejercicio 4: Desplegar contenedor de página web en 2 MV de producción en puerto 8080".
- Paso 1: En grupo de seguridad "GS-Prod" abra puerto 8080
- Paso 2: Crear un Target Group con las 2 máquinas virtuales o instancias para el puerto 8080

Captura de pantalla del formulario de Target Group:

| Campo | Valor |
|---|---|
| Target group name | TG-Prod-8080 (resaltado en amarillo) |
| Protocol | HTTP (resaltado en amarillo) |
| Port | 8080 (resaltado en amarillo) |

## Slide 15

Título: "Ejercicio 4: Desplegar contenedor de página web en 2 MV de producción en puerto 8080" (continuación).
- Paso 3: Agregue un agente de escucha en el Balanceador de Carga

Captura de pantalla de la consola AWS (en español) "lb-prod | Agregar agente de escucha", con botón azul "Agregar agente de escucha" a la izquierda y formulario a la derecha:
- Protocolo - Puerto: HTTP : 8080 (ambos resaltados en amarillo)
- Acciones predeterminadas → "1. Reenviar a..." → Grupo de destino: peso (0-999) → **TG-Prod-8080** (resaltado en amarillo), peso 1, Distribución del tráfico 100%.

## Slide 16

Título: "Ejercicio 4: Desplegar contenedor de página web en 2 MV de producción en puerto 8080" (continuación).
- Paso 4: Despliegue contenedor de página web en 2 MV de producción en el puerto 8080 de una imagen pública que ya tenga en hub.docker.com:

```
$ docker run -d --rm --name websimple_c -p 8080:80 gcolchado/websimple
```

(el usuario `gcolchado` está resaltado en amarillo)

- Paso 5: Pruebe el balanceador de carga varias veces. Primero probarlo sin paso 4 en puerto 8080, luego desplegar en 1 MV el contenedor y probar y luego desplegar el contenedor en la otra MV y probar. (este último tramo de texto en color azul, indicando instrucción metodológica).

## Slide 17

Slide de "Contenido" (agenda) repetida, mismo listado de 7 puntos, ahora con el ítem 6 "Ejercicio 5: Diagrama de Arquitectura de Solución" resaltado en negrita/subrayado como punto activo.

## Slide 18

Título: "Ejercicio 5: Diagrama de Arquitectura de Solución".
- Paso 1: Elabore en draw.io el Diagrama de Arquitectura de Solución de la Aplicación Web balanceada en carga usando el puerto 8080. Publique su diagrama en el padlet. Este ejercicio es guiado.

Sin imágenes; slide de solo texto/instrucción.

## Slide 19

Slide de "Contenido" (agenda) repetida, mismo listado de 7 puntos, ahora con el ítem 7 "Cierre" resaltado en negrita/subrayado como punto activo.

## Slide 20

Título: "Cierre: Balanceador de Carga - Qué aprendimos?". Un solo bullet de texto:
- Balanceo de Carga y Alta disponibilidad

Sin imágenes adicionales.

## Slide 21

Slide final. Texto centrado "Gracias" y debajo "Elaborado por docente: Geraldo Colchado". Franja naranja decorativa en el pie. Slide decorativa de cierre, sin contenido técnico adicional.
