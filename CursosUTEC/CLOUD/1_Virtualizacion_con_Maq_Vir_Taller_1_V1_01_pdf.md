---
curso: CLOUD
titulo: 1. Virtualización con Máq. Vir. - Taller 1 - V1.01
slides: 26
fuente: 1. Virtualización con Máq. Vir. - Taller 1 - V1.01.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Virtualización con máquinas virtuales
Semana 2 - Taller 1: Máquina Virtual en AWS (EC2)

                      ELABORADO POR: GERALDO COLCHADO
                         1. Objetivo del taller 1
                         2. AWS Academy
                         3. Ejercicio 1: Crear máquina virtual
Contenido                4. Ejercicio 2: Acceder a máquina virtual
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Ejecutar programas
                         7. Ejercicio 5: Transferencia de archivos
                         8. Cierre
Objetivo del taller 1:
Máquina Virtual en AWS (EC2)
•   Entender qué es AWS Academy
•   Creación de Máquina Virtual en EC2
•   Acceder a Máquina Virtual y practicar comandos básicos
•   Ejecutar programas
•   Transferencia de archivos
                         1. Objetivo del taller 1
                         2. AWS Academy
                         3. Ejercicio 1: Crear máquina virtual
Contenido                4. Ejercicio 2: Acceder a máquina virtual
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Ejecutar programas
                         7. Ejercicio 5: Transferencia de archivos
                         8. Cierre
AWS Academy:
Beneficios
           AWS Academy
           Cómo ingresar?
https://awsacademy.instructure.com/
                         1. Objetivo del taller 1
                         2. AWS Academy
                         3. Ejercicio 1: Crear máquina virtual
Contenido                4. Ejercicio 2: Acceder a máquina virtual
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Ejecutar programas
                         7. Ejercicio 5: Transferencia de archivos
                         8. Cierre
                                                     Esta AMI ya tiene instalado g++,
                                                     python3, node y Apache Web Server
Ejercicio 1:
Crear máquina virtual “MV Desarrollo”
•   Paso 1: Ingresar al servicio EC2
•   Paso 2: Ingresar al menú “Imágenes” / “AMI”
•   Paso 3: Buscar “Imágenes públicas” y “Origen = amazon/Cloud9ubuntu”
•   Paso 4: Ordenar por columna “Nombre de AMI” descendente
•   Paso 5: Seleccionar primer registro (Check) y botón “Lanzar instancia a partir
    de una AMI”
•   Paso 6: Elija “Par de claves” = “vockey”
•   Paso 7: En “Configuraciones de Red” marcar:
    • “Permitir el tráfico de SSH desde” “Cualquier lugar”
    • “Permitir el tráfico de HTTP desde Internet” “Cualquier lugar”
•   Paso 8: Botón “Lanzar instancia”
                         1. Objetivo del taller 1
                         2. AWS Academy
                         3. Ejercicio 1: Crear máquina virtual
Contenido                4. Ejercicio 2: Acceder a máquina virtual
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Ejecutar programas
                         7. Ejercicio 5: Transferencia de archivos
                         8. Cierre
Ejercicio 2:
Acceder a máquina virtual
•   Alternativa 1: Desde consola de AWS Academy ejecutar:
    $ ssh -i ./.ssh/labsuser.pem ubuntu@reemplazarIP

•   Alternativa 2: Desde Símbolo del sistema de Windows 10 ejecutar:
    $ ssh -i labsuser.pem ubuntu@reemplazarIP

    Nota: Previamente descargar el archivo ”labsuser.pem” desde ”Download PEM” en ”AWS
    Details” de ”AWS Academy”. El archivo ”labsuser.pem” debe estar en el mismo directorio
    donde se ejecuta el comando ssh.
                         1. Objetivo del taller 1
                         2. AWS Academy
                         3. Ejercicio 1: Crear máquina virtual
Contenido                4. Ejercicio 2: Acceder a máquina virtual
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Ejecutar programas
                         7. Ejercicio 5: Transferencia de archivos
                         8. Cierre
Ejercicio 3:
Comandos básicos
•   Crear la siguiente estructura de directorios:
                         1. Objetivo del taller 1
                         2. AWS Academy
                         3. Ejercicio 1: Crear máquina virtual
Contenido                4. Ejercicio 2: Acceder a máquina virtual
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Ejecutar programas
                         7. Ejercicio 5: Transferencia de archivos
                         8. Cierre
    Ejercicio 4:
    Ejecutar programas
•   Crear un programa hola
    mundo en estos 3 lenguajes
    de programación y
    ejecutarlos en:
                         1. Objetivo del taller 1
                         2. AWS Academy
                         3. Ejercicio 1: Crear máquina virtual
Contenido                4. Ejercicio 2: Acceder a máquina virtual
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Ejecutar programas
                         7. Ejercicio 5: Transferencia de archivos
                         8. Cierre
Ejercicio 5:
Transferencia de archivos por SFTP

SFTP es el Protocolo de transferencia de archivos SSH o Protocolo de
transferencia segura de archivos

•   Desde Símbolo del sistema de Windows 10 ejecutar:
    $ sftp -i labsuser.pem ubuntu@reemplazarIP

    Nota: Previamente descargar el archivo ”labsuser.pem” desde ”Download PEM” en ”AWS
    Details” de ”AWS Academy”. El archivo ”labsuser.pem” debe estar en el mismo directorio
    donde se ejecuta el comando sftp.
                 Ejercicio 5:
                 Transferencia de archivos por SFTP
                •        Mostrar la ayuda:
                         sftp> help

                •        Comandos para el sistema remoto (Máquina Virtual en AWS):
                         sftp> pwd                   (Mostrar directorio actual)
                         sftp> ls -l                 (Listar archivos)
                         sftp> cd nombre_dir         (Cambiar de directorio)

                •        Comandos para el sistema local (Computadora Windows 10):
                         sftp> lpwd                   (Mostrar directorio actual)
                         sftp> lls                    (Listar archivos)
                         sftp> lcd nombre_dir         (Cambiar de directorio)


Tutoriales recomendados:
https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server-es
https://www.hostinger.es/tutoriales/como-usar-sftp
                 Ejercicio 5:
                 Transferencia de archivos por SFTP
                Ejercicio: Transfiera el programa holamundo.cpp del sistema remoto al local:

                •        Transferencia de archivo remoto al sistema local:
                         sftp> get archivoRemoto                 (Descargar archivo remoto a sistema local)




Tutoriales recomendados:
https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server-es
https://www.hostinger.es/tutoriales/como-usar-sftp
                 Ejercicio 5:
                 Transferencia de archivos por SFTP
                Ejercicio: Transfiera el directorio utec del sistema remoto al local:

                •        Transferencia de contenido de directorio remoto al sistema local:
                         sftp> get -r directorioRemoto           (Descarga contenido de directorio a sistema local)




Tutoriales recomendados:
https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server-es
https://www.hostinger.es/tutoriales/como-usar-sftp
                 Ejercicio 5:
                 Transferencia de archivos por SFTP
                Ejercicio: Transfiera un archivo de texto (Ej: pendientes.txt) del sistema local al remoto:

                •        Transferencia de archivo local al sistema remoto:
                         sftp> put archivoLocal                   (Subir archivo local a sistema remoto)




Tutoriales recomendados:
https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server-es
https://www.hostinger.es/tutoriales/como-usar-sftp

                 Ejercicio 5:
                 Transferencia de archivos por SFTP
                Ejercicio: Transfiera un directorio del sistema local al remoto:

                •        Transferencia de contenido de directorio local a sistema remoto:
                         sftp> put -r directorioLocal            (Subir contenido de directorio a sistema remoto)




                 Ejercicio: Salir del SFTP:

                         sftp> bye



Tutoriales recomendados:
https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server-es
https://www.hostinger.es/tutoriales/como-usar-sftp
                 Ejercicio 5:
                 Transferencia de archivos por WinSCP
                Ejercicio: Transfiera archivos por WinSCP desde Windows a Máquina Virtual en Linux según
                indicaciones del docente.




                Nota: Previamente descargar el archivo ”labsuser.ppk” desde ”Download PPK” en ”AWS
                Details” de ”AWS Academy”.
Tutoriales recomendados:
https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server-es
https://www.hostinger.es/tutoriales/como-usar-sftp
Ejercicio 5:
Transferencia de archivos por github
En caso se tengan bloqueos en la red de la universidad para utilizar SFTP y/o WinSCP puede
utilizar github para transferir su código fuente a la Máquina Virtual:

•   Cree una nueva cuenta en github (https://github.com/ ) o acceda a una que ya tenga.
•   Cree un nuevo repositorio en github que sea público.
•   Suba sus archivos de código fuente al nuevo repositorio.
•   Ingrese a su máquina virtual y ubíquese en el directorio donde va a descargar.
•   Ejecute el comando git para clonar su repositorio de github. Ejemplo:
     git clone https://github.com/gcolchado/app01.git
                         1. Objetivo del taller 1
                         2. AWS Academy
                         3. Ejercicio 1: Crear máquina virtual
Contenido                4. Ejercicio 2: Acceder a máquina virtual
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Ejecutar programas
                         7. Ejercicio 5: Transferencia de archivos
                         8. Cierre
Cierre:
Máquina Virtual en AWS (EC2) - Qué aprendimos?
•   Entender qué es AWS Academy
•   Creación de Máquina Virtual en EC2
•   Acceder a Máquina Virtual y practicar comandos básicos
•   Ejecutar programas
•   Transferencia de archivos
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
