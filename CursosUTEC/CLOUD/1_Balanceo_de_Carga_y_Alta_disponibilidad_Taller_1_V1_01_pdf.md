---
curso: CLOUD
titulo: 1. Balanceo de Carga y Alta disponibilidad - Taller 1 - V1.01
slides: 21
fuente: 1. Balanceo de Carga y Alta disponibilidad - Taller 1 - V1.01.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Balanceo de Carga y Alta disponibilidad
Semana 6 - Taller 1: Balanceador de Carga

                       ELABORADO POR: GERALDO COLCHADO
                       1. Objetivo del taller 1
                       2. Ejercicio 1: Crear 2 MV para producción
                       3. Ejercicio 2: Crear Balanceador de Carga
Contenido              4. Ejercicio 3: Probar Balanceo de Carga y Alta
                          disponibilidad
Balanceador de Carga
                       5. Ejercicio 4: Desplegar contenedor de página
                          web en 2 MV de producción en puerto 8080
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
Objetivo del taller 1:
Balanceador de Carga
• Probar Balanceo de Carga y Alta disponibilidad
                       1. Objetivo del taller 1
                       2. Ejercicio 1: Crear 2 MV para producción
                       3. Ejercicio 2: Crear Balanceador de Carga
Contenido              4. Ejercicio 3: Probar Balanceo de Carga y Alta
                          disponibilidad
Balanceador de Carga
                       5. Ejercicio 4: Desplegar contenedor de página
                          web en 2 MV de producción en puerto 8080
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
    Ejercicio 1:
    Crear 2 MV para producción
•   Paso 1: Cree una máquina virtual con la AMI pública más reciente de Origen
    = amazon/Cloud9Ubuntu y nómbrela como “MV Prod 1” y cree un grupo de
    seguridad nuevo “GS-Prod” y abra puertos 22 y 80 (botón Editar).

•   Paso 2: Cree una máquina virtual con la AMI pública más reciente de Origen
    = amazon/Cloud9Ubuntu y nómbrela como “MV Prod 2” y asigne grupo de
    seguridad existente “GS-Prod” y que esté en una Zona de Disponibilidad
    diferente a la anterior MV (Elegir Subred)
                       1. Objetivo del taller 1
                       2. Ejercicio 1: Crear 2 MV para producción
                       3. Ejercicio 2: Crear Balanceador de Carga
Contenido              4. Ejercicio 3: Probar Balanceo de Carga y Alta
                          disponibilidad
Balanceador de Carga
                       5. Ejercicio 4: Desplegar contenedor de página
                          web en 2 MV de producción en puerto 8080
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
    Ejercicio 2:
    Crear Balanceador de Carga
•   Paso 1: Crear un Target Group con las 2 máquinas virtuales o instancias para
    el puerto 80




•   Paso 2: Crear balanceador de carga
Ejercicio 2:
Crear Balanceador de Carga
Ejercicio 2:
Crear Balanceador de Carga
                       1. Objetivo del taller 1
                       2. Ejercicio 1: Crear 2 MV para producción
                       3. Ejercicio 2: Crear Balanceador de Carga
Contenido              4. Ejercicio 3: Probar Balanceo de Carga y Alta
                          disponibilidad
Balanceador de Carga
                       5. Ejercicio 4: Desplegar contenedor de página
                          web en 2 MV de producción en puerto 8080
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
    Ejercicio 3:
    Probar Balanceo de Carga y Alta disponibilidad
•   Paso 1: Editar la página de inicio de Apache en las 2 Máquinas Virtuales
•   Paso 2: Probar con el enlace del balanceador de carga varias veces
    Ejercicio 3:
    Probar Balanceo de Carga y Alta disponibilidad
•   Paso 3: Detener la instancia “MV Prod 1” y probar

•   Paso 4: Detener la instancia “MV Prod 2” y probar

•   Paso 5: Iniciar la instancia “MV Prod 1” y probar

•   Paso 6: Iniciar la instancia “MV Prod 2” y probar
                       1. Objetivo del taller 1
                       2. Ejercicio 1: Crear 2 MV para producción
                       3. Ejercicio 2: Crear Balanceador de Carga
Contenido              4. Ejercicio 3: Probar Balanceo de Carga y Alta
                          disponibilidad
Balanceador de Carga
                       5. Ejercicio 4: Desplegar contenedor de
                          página web en 2 MV de producción en
                          puerto 8080
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
    Ejercicio 4:
    Desplegar contenedor de página web en 2 MV de
    producción en puerto 8080
•   Paso 1: En grupo de seguridad “GS-Prod” abra puerto 8080
•   Paso 2: Crear un Target Group con las 2 máquinas virtuales o instancias para
    el puerto 8080
    Ejercicio 4:
    Desplegar contenedor de página web en 2 MV de
    producción en puerto 8080
•   Paso 3: Agregue un agente de escucha en el Balanceador de Carga
    Ejercicio 4:
    Desplegar contenedor de página web en 2 MV de
    producción en puerto 8080
•   Paso 4: Despliegue contenedor de página web en 2 MV de producción en el
    puerto 8080 de una imagen pública que ya tenga en hub.docker.com:

    $ docker run -d --rm --name websimple_c -p 8080:80 gcolchado/websimple

•   Paso 5: Pruebe el balanceador de carga varias veces. Primero probarlo sin
    paso 4 en puerto 8080, luego desplegar en 1 MV el contenedor y probar y
    luego desplegar el contenedor en la otra MV y probar.
                       1. Objetivo del taller 1
                       2. Ejercicio 1: Crear 2 MV para producción
                       3. Ejercicio 2: Crear Balanceador de Carga
Contenido              4. Ejercicio 3: Probar Balanceo de Carga y Alta
                          disponibilidad
Balanceador de Carga
                       5. Ejercicio 4: Desplegar contenedor de página
                          web en 2 MV de producción en puerto 8080
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
    Ejercicio 5:
    Diagrama de Arquitectura de Solución
•   Paso 1: Elabore en draw.io el Diagrama de Arquitectura de Solución de la
    Aplicación Web balanceada en carga usando el puerto 8080. Publique su
    diagrama en el padlet. Este ejercicio es guiado.
                       1. Objetivo del taller 1
                       2. Ejercicio 1: Crear 2 MV para producción
                       3. Ejercicio 2: Crear Balanceador de Carga
Contenido              4. Ejercicio 3: Probar Balanceo de Carga y Alta
                          disponibilidad
Balanceador de Carga
                       5. Ejercicio 4: Desplegar contenedor de página
                          web en 2 MV de producción en puerto 8080
                       6. Ejercicio 5: Diagrama de Arquitectura de
                          Solución
                       7. Cierre
Cierre:
Balanceador de Carga - Qué aprendimos?
• Balanceo de Carga y Alta disponibilidad

              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
