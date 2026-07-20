---
curso: INGSOFT
titulo: 14 - Semana 13/IS1 - Aula 15 - Mantenimiento de Software__pptx
slides: 29
fuente: 14 - Semana 13/IS1 - Aula 15 - Mantenimiento de Software__pptx.pdf
---

Ingeniería de Software

       Profesor Christian Paz
                                               Desarrollo de Software




    Análisis                     Diseño              Implementación            Pruebas                 Despliegue             Mantenimiento


Qué debe    hacer   el   Cómo      se   hará   el   Hacer el Software.   El software hace lo que   Entregar,   poner   en   El software funciona, pero
software?                software?                                       se supone que debe        marcha.                  le falta esto, o está lento,
                                                                         hacer?                                             o necesita mejorar esto.
Requerimiento




      Casos de Uso                            Casos de Prueba

                                 Reproducción de error.
                                 Corrección de error,            Aceptación     Software
                  Arquitectura
                                 Refactorización.                             Desplegado v0


                                                 Código Fuente
                                                 Configuración
      Diagramas de Clases
     Diagramas de Secuencia
Gestión de la Configuración



Los sistemas de software siempre cambian durante su desarrollo y uso.
 -   Se descubren bugs y deben corregirse.
 -   Requerimientos del sistema cambian.
 -   Se debe actualizar el software relacionado (bibliotecas, servicios, etc).
 -   Cambios impulsados por el mercado (legislación, económicos, oportunidades).
Gestión de la Configuración


Políticas, Procesos, Herramientas para administrar los cambios en los sistemas de
software.

                                                            Software
          Código Fuente v0
                                                          Desplegado v0
          Configuración v0
Gestión de la Configuración



Políticas, Procesos, Herramientas para administrar los cambios en los sistemas de
software.

                                                            Software
          Código Fuente v0
                                                          Desplegado v0


                                   Change Request
      Gestión de la Configuración




       Políticas, Procesos, Herramientas para administrar los cambios en los sistemas de
       software.

                 Código Fuente v0                                  Software
                   Branch: main                                  Desplegado v0

Nueva versión
                                          Change Request
 de librería

                     Cambios
                    Branch: dev
         Gestión de la Configuración




                             Código Fuente v0                                 Software
                               Branch: main                                 Desplegado v0

Nueva versión de librería.
    Commit: 5f4b3s                                         Change Request
                                                           Commit: 3d1a21


                                Cambios
                               Branch: dev
 Nueva pantalla.                                Merge to main
 Commit: 6c12c1                              Commit: 5f4b3s, 3d1a21

                             Código Fuente v1                                 Software
                               Branch: main                                 Desplegado v1
Gestión de la Configuración - Actividades




Administración del cambio.
Gestión de versiones.
Construcción del sistema.
Gestión de entregas.
Administración del cambio


● Descripción del cambio o prioridad.
● Impacto de NO realizar el cambio.
● Beneficios de realizar el cambio.
● Número de usuarios afectados por el cambio.
● Costos asociados al cambio.
● Cómo encaja en el ciclo de release del producto.
Administración del cambio - Ejemplo


El sistema sólo soporta usuarios con DNI, se requiere soportar documento de
extranjero.
Administración del cambio - Ejemplo


El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.
Prioridad: Media. <<<<- La define el Usuario / Product Owner
Administración del cambio - Ejemplo



  El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.
  Prioridad: Media.
  Impacto de NO realizar el cambio: Clientes potenciales perdidos hasta el momento: 100.
Administración del cambio - Ejemplo


El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.
Prioridad: Media.
Impacto de NO realizar el cambio: Clientes potenciales perdidos hasta el momento: 100.
Beneficios de realizar el cambio: Nuevos clientes pueden ser atendidos. <<<<--- clientes
extranjeros podrán comprar en la tienda online.
Administración del cambio - Ejemplo


El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.
Prioridad: Media.
Impacto de NO realizar el cambio: Clientes potenciales perdidos hasta el momento: 100.
Beneficios de realizar el cambio: Nuevos clientes pueden ser atendidos.
Número de usuarios afectados por el cambio: Todos. <<<<---- Usuarios con DNI verán un
nuevo campo en la interfaz.
Administración del cambio - Ejemplo


El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.
Prioridad: Media.
Impacto de NO realizar el cambio: Clientes potenciales perdidos hasta el momento: 100.
Beneficios de realizar el cambio: Nuevos clientes pueden ser atendidos.
Número de usuarios afectados por el cambio: Todos.
Costos asociados al cambio: 20 horas de desarrollo, 10 horas de prueba.
<<<<---- Jefe de Proyecto y el equipo deben realizar una estimación del esfuerzo y costos
asociados.
Administración del cambio - Ejemplo


El sistema sólo soporta usuarios con DNI, se requiere soportar documento de extranjero.

Prioridad: Media.

Impacto de NO realizar el cambio: Clientes potenciales perdidos hasta el momento: 100.

Beneficios de realizar el cambio: Nuevos clientes pueden ser atendidos.

Número de usuarios afectados por el cambio: 100.

Costos asociados al cambio: 20 horas de desarrollo, 10 horas de prueba.

5 horas para actualizar la BD (preparar scripts de creación, de actualización, etc)

5 horas para los cambios en los servicios (backend : X archivos)

10 horas para los cambios de UI (7 pantallas)

Cómo encaja en el ciclo de release del producto: Se podría entregar junto con la versión 2 del sistema.
Gestión de versiones


Consiste en tener seguimiento de las versiones de cada elemento que
construye el software (archivos de código fuente, documentos, archivos de
configuración, etc).
Garantizar que los cambios hechos por un desarollador no interfieran con
los de otros.
Gestión de versiones
Gestión de versiones


Repositorio: Conjunto de archivos organizados en carpetas.
Commit (changelist): Conjunto de cambios en diferentes archivos.
Branch: Todo repositorio tiene un branch principal (main, master)
Un branch es una copia de otro branch en un determinado punto de tiempo sobre el cual
se realizan commits sin afectar el branch original.

Gestión de versiones


Merge: Consiste en aplicar los cambios de un branch a otro branch.
Conflicto: Los cambios de un branch no pueden ser aplicados directamente porque el
branch receptor tiene cambios en la misma "línea" que los cambios requieren ser
aplicados.
Gestión de versiones


Conflicto oculto:
Main: Función getUsuario(dni)
Branch1: Edit: Función getUsuario(tipoDoc, numDoc)
Branch2: + Función getCarrito(dni) {
getUsuario(dni)
}
Branch1 ->> Main (OK)
Branch2 ->> Main (OK no conflicts)
Error de compilación.
Construcción del Sistema


A partir del código fuente (puede ser uno o varios repositorios), generar el software ejecutable.
ALTER TABLE MODIFY COLUMN DNI VARCHAR(9);
ALTER TABLE ADD COLUMN TipoDpcumento INT; // 0: DNI, 1: Carnet de Extranjeria
ALTER TABLE DROP PRIMARY KEY;
UPDATE SET TIPODOCUMENTO=0;
ALTER TABLE CREATE PRIMARY KEY;




           Construcción del Sistema
                                                                DNI (9) [PK]    Nombre       TelContacto   Password         TipoDocumento

                                                                45610987        Juan Silva   956789000     sdffsfsdfsdfsf   0

                                                                009878673       XXXX         7777777       dfsfsffssf       1




             •     Ejecutar validaciones de código fuente (SonarCube?).
             •     Compilar Bibliotecas y Dependencias.
             •     Compilar el Software y generar ejecutables.
             •     Leer archivos de configuración del ambiente apropiado (URLs, Credenciales de
                   BD).
             •     Ejecutar scripts de BD asociados a los cambios.
Construcción del Sistema



- Ejecutar pasos de validación automática:
   - Unit Tests.
   - Functional Tests.
- Desplegar en un ambiente intermedio.
- Ejecutar nuevas validaciones: Nightwatch Tests.
- Desplegar en el ambiente compartido.
Gestión de entregas (release)


Control de qué cambios (funcionales o no funcionales) fueron entregados / desplegados en cada versión y en
qué fecha.

Posibilidad de hacer rollback (volver a la versión anterior) caso el despliegue de la nueva versión introduce un
problema inesperado.
Caso de estudio
 El Software utiliza un Sistema de envío de SMS con un modelo de subscripción
 mensual.


 Se requiere utilizar una nueva API, que utiliza un protocolo POST, en la URL:

 https://mynewsms.com.pe/rest/envia-sms

 Con un formato json específico.



 ●   Descripción del cambio o prioridad: Alta.
 ●   Impacto de NO realizar el cambio: Se seguiría pagando un
     precio alto.
 ●   Beneficios de realizar el cambio: Se reduce el costo de
                                                                                 Sistema Actual: S/. 1000 Mensual (Maximo de
     operación del sistema.
                                                                                 100 x dia)
 ●   Número de usuarios afectados por el cambio: 3500 usuarios
                                                                                 Dia normal: 50 msg, 150 msg (50 x 0.5 = S/.
     x mes.                                                                      25)
 ●   Costos asociados al cambio: Nuevo proveedor:                                Extra: S/. 0.50
 ●   - Proveer documentación de su servicio (Autenticación).                     Mensualmente: 1200 soles.
 ●   - Velocidad 5ms, 5s: Nuevo: 10ms, 10s.
 ●   - Endpoint de Prueba.
                                                                                 Sistema Nuevo:
 ●   Cómo encaja en el ciclo de release del producto:
                                                                                 S/ 0.1 x msg
                                                                                 3500 -> 350 soles.
                    SMS Service

                                                           Feature Flags
                                                     Config.NuevoSMS = 100%




               If Config.NuevoSMS ==
                          true




          No
                                       Yes




Antigua

                                             Nueva
GRACIAS
CHRISTIAN PAZ TRILLO

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
