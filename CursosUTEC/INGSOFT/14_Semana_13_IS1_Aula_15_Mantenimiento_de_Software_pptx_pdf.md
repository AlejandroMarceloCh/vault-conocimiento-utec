---
curso: INGSOFT
titulo: 14 - Semana 13/IS1 - Aula 15 - Mantenimiento de Software__pptx
slides: 29
fuente: 14 - Semana 13/IS1 - Aula 15 - Mantenimiento de Software__pptx.pdf
---

## Slide 1

Portada decorativa (fondo azul de túnel tecnológico con silueta humano/robot).

Título: **Ingeniería de Software**
Subtítulo: Profesor Christian Paz

## Slide 2

Título: **Desarrollo de Software**

Diagrama de línea de tiempo horizontal con 6 fases, cada una con un ícono circular azul conectado por una línea con nodos amarillos. Debajo, tarjetas con el nombre de la fase (botón azul) y una descripción. La última tarjeta ("Mantenimiento") está resaltada en amarillo brillante — es el tema de la clase.

| Fase | Ícono | Descripción |
|------|-------|-------------|
| Análisis | diana/blanco | ¿Qué debe hacer el software? |
| Diseño | lupa | ¿Cómo se hará el software? |
| Implementación | cohete | Hacer el Software. |
| Pruebas | calendario con checks | ¿El software hace lo que se supone que debe hacer? |
| Despliegue | cohete despegando | Entregar, poner en marcha. |
| **Mantenimiento** (resaltado) | eslabón/cadena | El software funciona, pero le falta esto, o está lento, o necesita mejorar esto. |

## Slide 3

Diagrama de flujo (sin título) que muestra cómo se relacionan los artefactos del desarrollo. Cajas azules conectadas por flechas naranjas (dependencia/derivación) y amarillas (relación bidireccional / aceptación):

- **Requerimiento** →(naranja) **Casos de Uso**
- **Casos de Uso** ↔(flecha amarilla bidireccional) **Casos de Prueba**
- **Casos de Uso** →(naranja) **Arquitectura**
- **Casos de Uso** →(naranja) **Diagramas de Clases / Diagramas de Secuencia**
- **Arquitectura** →(naranja) **Código Fuente / Configuración**
- **Diagramas de Clases / Diagramas de Secuencia** →(naranja) **Código Fuente / Configuración**
- **Casos de Prueba** ↕(flecha naranja bidireccional vertical) **Código Fuente / Configuración**, con la etiqueta al costado: "Reproducción de error. Corrección de error, Refactorización."
- **Casos de Prueba** →(amarilla, etiqueta "Aceptación") **Software Desplegado v0** (caja de borde blanco/sin relleno).

Idea: el flujo de mantenimiento (reproducción/corrección de error, refactorización) ocurre en el lazo entre Casos de Prueba y Código Fuente.

## Slide 4

Título: **Gestión de la Configuración**

Texto:
Los sistemas de software siempre cambian durante su desarrollo y uso.
- Se descubren bugs y deben corregirse.
- Requerimientos del sistema cambian.
- Se debe actualizar el software relacionado (bibliotecas, servicios, etc).
- Cambios impulsados por el mercado (legislación, económicos, oportunidades).

## Slide 5

Título: **Gestión de la Configuración**

Texto: Políticas, Procesos, Herramientas para administrar los cambios en los sistemas de software.

Diagrama simple: caja **Código Fuente v0 / Configuración v0** ↔ (doble flecha azul) caja **Software Desplegado v0**. Representa el estado inicial: el código v0 se corresponde con el despliegue v0.

## Slide 6

Título: **Gestión de la Configuración** (misma frase de políticas/procesos/herramientas)

Igual que la slide 5 pero se agrega el origen de un cambio: caja rosada **Change Request** conectada por una línea a un ícono de un grupo de tres personas (usuarios/stakeholders). El Change Request nace de los usuarios.

## Slide 7

Título: **Gestión de la Configuración**

Se enriquece el diagrama con el flujo de branches:
- **Código Fuente v0 / Branch: main** ↔ **Software Desplegado v0**
- Caja rosada **Change Request** ← ligada al grupo de personas (a la derecha).
- Caja rosada **Nueva versión de librería** (izquierda) → (flecha azul) caja **Cambios / Branch: dev**.
- La caja **Change Request** también → (flecha azul) hacia **Cambios / Branch: dev**.

Idea: tanto el change request de usuarios como la actualización de librería se trabajan en el branch dev.

## Slide 8

Título: **Gestión de la Configuración**

Diagrama completo del ciclo de versión con commits:
- **Código Fuente v0 / Branch: main** ↔ **Software Desplegado v0** (arriba).
- Grupo de personas a la derecha ligado a **Change Request / Commit: 3d1a21** (caja rosada) → flecha naranja hacia **Cambios / Branch: dev**.
- **Nueva versión de librería. / Commit: 5f4b3s** (caja rosada, izquierda) → flecha naranja hacia **Cambios / Branch: dev**.
- **Nueva pantalla. / Commit: 6c12c1** (caja verde, abajo-izquierda) → flecha verde hacia **Cambios / Branch: dev**.
- Desde **Cambios / Branch: dev** → flecha naranja hacia abajo, con etiqueta rosada **Merge to main / Commit: 5f4b3s, 3d1a21** → **Código Fuente v1 / Branch: main**.
- **Código Fuente v1 / Branch: main** ↔ **Software Desplegado v1** (abajo).

Idea: se acumulan varios commits en dev y se hace merge a main, produciendo la v1 desplegada.

## Slide 9

Título: **Gestión de la Configuración - Actividades**

Lista (solo texto):
- Administración del cambio.
- Gestión de versiones.
- Construcción del sistema.
- Gestión de entregas.

## Slide 10

Título: **Administración del cambio**

Viñetas (los criterios para evaluar un change request):
- Descripción del cambio o prioridad.
- Impacto de NO realizar el cambio.
- Beneficios de realizar el cambio.
- Número de usuarios afectados por el cambio.
- Costos asociados al cambio.
- Cómo encaja en el ciclo de release del producto.

## Slide 11

Título: **Administración del cambio - Ejemplo**

Solo texto:
El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.

## Slide 12

Título: **Administración del cambio - Ejemplo** (acumulativo)

El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.
Prioridad: Media. <<<<- La define el Usuario / Product Owner

## Slide 13

Título: **Administración del cambio - Ejemplo** (acumulativo)

- El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.
- Prioridad: Media.
- Impacto de NO realizar el cambio: Clientes potenciales perdidos hasta el momento: 100.

## Slide 14

Título: **Administración del cambio - Ejemplo** (acumulativo)

- El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.
- Prioridad: Media.
- Impacto de NO realizar el cambio: Clientes potenciales perdidos hasta el momento: 100.
- Beneficios de realizar el cambio: Nuevos clientes pueden ser atendidos. <<<<--- clientes extranjeros podrán comprar en la tienda online.

## Slide 15

Título: **Administración del cambio - Ejemplo** (acumulativo)

- El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.
- Prioridad: Media.
- Impacto de NO realizar el cambio: Clientes potenciales perdidos hasta el momento: 100.
- Beneficios de realizar el cambio: Nuevos clientes pueden ser atendidos.
- Número de usuarios afectados por el cambio: Todos. <<<<---- Usuarios con DNI verán un nuevo campo en la interfaz.

## Slide 16

Título: **Administración del cambio - Ejemplo** (acumulativo)

- El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.
- Prioridad: Media.
- Impacto de NO realizar el cambio: Clientes potenciales perdidos hasta el momento: 100.
- Beneficios de realizar el cambio: Nuevos clientes pueden ser atendidos.
- Número de usuarios afectados por el cambio: Todos.
- Costos asociados al cambio: 20 horas de desarrollo, 10 horas de prueba. <<<<---- Jefe de Proyecto y el equipo deben realizar una estimación del esfuerzo y costos asociados.

## Slide 17

Título: **Administración del cambio - Ejemplo** (acumulativo, con desglose de costos)

- El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.
- Prioridad: Media.
- Impacto de NO realizar el cambio: Clientes potenciales perdidos hasta el momento: 100.
- Beneficios de realizar el cambio: Nuevos clientes pueden ser atendidos.
- Número de usuarios afectados por el cambio: 100.
- Costos asociados al cambio: 20 horas de desarrollo, 10 horas de prueba.
  - 5 horas para actualizar la BD (preparar scripts de creación, de actualización, etc)
  - 5 horas para los cambios en los servicios (backend: X archivos)
  - 10 horas para los cambios de UI (7 pantallas)
- Cómo encaja en el ciclo de release del producto: Se podría entregar junto con la versión 2 del sistema.

## Slide 18

Título: **Gestión de versiones**

Solo texto:
- Consiste en tener seguimiento de las versiones de cada elemento que construye el software (archivos de código fuente, documentos, archivos de configuración, etc).
- Garantizar que los cambios hechos por un desarrollador no interfieran con los de otros.

## Slide 19

Título: **Gestión de versiones**

Diagrama tipo grafo de commits de git (círculos conectados):
- Fila inferior en morado: **Main** (rama principal, varios commits en línea).
- Fila superior en verde: **Your work** — tres commits verdes que salen de main y vuelven a main (branch propio que se mergea).
- Abajo un commit azul: **Another person's work** — otra rama que también parte y regresa a main.

Idea visual: dos personas trabajan en branches paralelos derivados de main y luego integran.

## Slide 20

Título: **Gestión de versiones**

Texto (definiciones):
- Repositorio: Conjunto de archivos organizados en carpetas.
- Commit (changelist): Conjunto de cambios en diferentes archivos.
- Branch: Todo repositorio tiene un branch principal (main, master).
- Un branch es una copia de otro branch en un determinado punto de tiempo sobre el cual se realizan commits sin afectar el branch original.

Diagrama pequeño abajo: fila de 4 nodos verdes en línea (rama principal, flechas verdes) con un nodo morado arriba que sale de la línea y vuelve a ella (flechas moradas) — ilustra un branch que se ramifica y luego hace merge.

## Slide 21

Título: **Gestión de versiones**

Texto:
- Merge: Consiste en aplicar los cambios de un branch a otro branch.
- Conflicto: Los cambios de un branch no pueden ser aplicados directamente porque el branch receptor tiene cambios en la misma "línea" que los cambios requieren ser aplicados.

Ilustración: dos ramas con cajas amarillas de texto. Rama **main**: "HELLO, WORLD!" → "HELLO, DOG!". Rama **abid/main**: "HELLO, CAT!". Al intentar unirlas colisionan en una explosión (estrella naranja/roja) = conflicto de merge sobre la misma línea.

## Slide 22

Título: **Gestión de versiones**

Texto — ejemplo de **conflicto oculto** (semántico, no detectado por el sistema de versiones):

```
Conflicto oculto:
Main:    Función getUsuario(dni)
Branch1: Edit: Función getUsuario(tipoDoc, numDoc)
Branch2: + Función getCarrito(dni) {
             getUsuario(dni)
         }
Branch1 ->> Main (OK)
Branch2 ->> Main (OK no conflicts)
Error de compilación.
```

Idea: Branch1 cambia la firma de `getUsuario`, Branch2 agrega una llamada con la firma vieja; ambos mergean sin conflicto textual, pero el resultado no compila.

## Slide 23

Título: **Construcción del Sistema**

Texto: A partir del código fuente (puede ser uno o varios repositorios), generar el software ejecutable.

Diagrama de pipeline CI/CD dividido en 4 zonas numeradas, con flechas azules de flujo:
1. **Code Repository** — Developer hace "Commit", flecha "CODE" hacia el repo (íconos de Git/GitHub).
2. **Building Service** — flecha "BUILD" hacia servidor de build (ícono de Jenkins, el mayordomo).
3. **Deployment Service** — flechas "DEPLOY" y "READY"; flecha "STAGE" hacia **Target Cloud** (logos metacloud y AWS), etiqueta "CloudCenter / Cloud Agnostic". También flecha "INTEGRATE" hacia **Load-Balancer** (Avi Service Engine).
4. **Application Service** — flecha "TEST" hacia una caja **APP**, y flecha "CONSUME" hacia **Enduser**.

## Slide 24

Título: **Construcción del Sistema**

Arriba, bloque de código SQL (scripts de migración de BD asociados al cambio de documento):
```sql
ALTER TABLE MODIFY COLUMN DNI VARCHAR(9);
ALTER TABLE ADD COLUMN TipoDpcumento INT; // 0: DNI, 1: Carnet de Extranjeria
ALTER TABLE DROP PRIMARY KEY;
UPDATE SET TIPODOCUMENTO=0;
ALTER TABLE CREATE PRIMARY KEY;
```

Tabla ejemplo del resultado en BD:

| DNI (9) [PK] | Nombre | TelContacto | Password | TipoDocumento |
|--------------|--------|-------------|----------|---------------|
| 45610987 | Juan Silva | 956789000 | sdffsfsdfsdfsf | 0 |
| 009878673 | XXXX | 7777777 | dfsfsffssf | 1 |

Viñetas (pasos del build):
- Ejecutar validaciones de código fuente (SonarCube?).
- Compilar Bibliotecas y Dependencias.
- Compilar el Software y generar ejecutables.
- Leer archivos de configuración del ambiente apropiado (URLs, Credenciales de BD).
- Ejecutar scripts de BD asociados a los cambios.

## Slide 25

Título: **Construcción del Sistema**

Texto (continuación de pasos):
- Ejecutar pasos de validación automática:
  - Unit Tests.
  - Functional Tests.
- Desplegar en un ambiente intermedio.
- Ejecutar nuevas validaciones: Nightwatch Tests.
- Desplegar en el ambiente compartido.

## Slide 26

Título: **Gestión de entregas (release)**

Solo texto:
- Control de qué cambios (funcionales o no funcionales) fueron entregados / desplegados en cada versión y en qué fecha.
- Posibilidad de hacer rollback (volver a la versión anterior) caso el despliegue de la nueva versión introduce un problema inesperado.

## Slide 27

Título: **Caso de estudio**

Texto (izquierda):
El Software utiliza un Sistema de envío de SMS con un modelo de subscripción mensual.
Se requiere utilizar una nueva API, que utiliza un protocolo POST, en la URL: https://mynewsms.com.pe/rest/envia-sms
Con un formato json específico.

Change request evaluado:
- Descripción del cambio o prioridad: Alta.
- Impacto de NO realizar el cambio: Se seguiría pagando un precio alto.
- Beneficios de realizar el cambio: Se reduce el costo de operación del sistema.
- Número de usuarios afectados por el cambio: 3500 usuarios x mes.
- Costos asociados al cambio: Nuevo proveedor:
  - Proveer documentación de su servicio (Autenticación).
  - Velocidad 5ms, 5s: Nuevo: 10ms, 10s.
  - Endpoint de Prueba.
- Cómo encaja en el ciclo de release del producto:

Diagrama (arriba derecha): caja **Registro de Usuarios** → (flecha) caja **Proveedor SMS**, con etiqueta del protocolo actual "Protocolo GET  https://mysms.com.pe/rest/sms?numTelefono=".

Cálculo de costos (abajo derecha):
- Sistema Actual: S/. 1000 Mensual (Máximo de 100 x día). Día normal: 50 msg, 150 msg (50 x 0.5 = S/. 25). Extra: S/. 0.50. Mensualmente: 1200 soles.
- Sistema Nuevo: S/ 0.1 x msg. 3500 -> 350 soles.

## Slide 28

Título: (sin título; diagrama de flujo)

Flujo de decisión con **Feature Flags** para migrar entre proveedores de SMS gradualmente:
- Caja **SMS Service** → (flecha) rombo de decisión **If Config.NuevoSMS == true**.
- Rama **No** (izquierda) → caja **Antigua** (proveedor viejo).
- Rama **Yes** (derecha) → caja **Nueva** (proveedor nuevo).
- Caja aparte arriba a la derecha: **Feature Flags / Config.NuevoSMS = 100%**.

Idea: la selección de proveedor se controla por un feature flag (aquí al 100% ya usa el nuevo), permitiendo rollout progresivo.

## Slide 29

Cierre decorativo (fondo azul con foto de laboratorio).

Texto: **GRACIAS** — Christian Paz Trillo
