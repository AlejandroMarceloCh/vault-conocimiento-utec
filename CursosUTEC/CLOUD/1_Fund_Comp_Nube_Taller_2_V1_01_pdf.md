---
curso: CLOUD
titulo: 1. Fund. Comp. Nube - Taller 2 - V1.01
slides: 24
fuente: 1. Fund. Comp. Nube - Taller 2 - V1.01.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Fundamentos de Computación en la Nube
Semana 1 - Taller 2: Grupos, Usuarios y Permisos en Linux

                        ELABORADO POR: GERALDO COLCHADO
                         1. Objetivo del taller 2
                         2. Máquina virtual Linux en nube
                         3. Conceptos: Linux - Usuarios y Grupos
Contenido                4. Conceptos: Linux - Permisos sobre
Fundamentos de              archivos
Computación en la Nube
                         5. Conceptos: Linux - Cambiar permisos
                            sobre archivos
                         6. Conceptos: Linux - Espacio ocupado por
                            directorios y por sistema de archivos
                         7. Cierre
Objetivo del taller 2:
Grupos, Usuarios y Permisos en Linux

• Aprender a crear grupos y usuarios en Linux

• Entender los permisos de archivos en Linux

• Aprender a cambiar permisos de archivos en Linux
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Conceptos: Linux - Usuarios y Grupos
Contenido                4. Conceptos: Linux - Permisos sobre
Fundamentos de              archivos
Computación en la Nube
                         5. Conceptos: Linux - Cambiar permisos
                            sobre archivos
                         6. Conceptos: Linux - Espacio ocupado por
                            directorios y por sistema de archivos
                         7. Cierre
        Máquina Virtual Linux en nube:
        Proveedor Digital Ocean


Ubuntu Linux (1 CPU, 1 GB RAM, 25 GB SSD)
        IP pública: 146.190.169.149
                                              Internet
  Aplicaciones de Software:
  • Servidor Web (Ej.: Apache)
  • Servidor BD (Ej.: MySQL, PostgreSQL)
  • Servidor Shell Seguro (Ej: SSH)
  • Servidor Transferencia de Archivos SFTP
  • Compiladores: c, c++, python, node.js
  • Etc.
                                                         Cliente SSH (Secure Shell)
Ejercicio 2:
Ingresar a Linux
ssh utec@146.190.169.149
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Conceptos: Linux - Usuarios y Grupos
Contenido                4. Conceptos: Linux - Permisos sobre
Fundamentos de              archivos
Computación en la Nube
                         5. Conceptos: Linux - Cambiar permisos
                            sobre archivos
                         6. Conceptos: Linux - Espacio ocupado por
                            directorios y por sistema de archivos
                         7. Cierre
Conceptos:
Linux - Usuarios
                   Usuario: Entidad creada en Linux para otorgar permisos que
 Ubuntu Server
                     permitan al usuario realizar tareas específicas. Se crean
 22.04 x 64 bits   usuarios para personas que requieren acceso al computador,
                   también para servicios/aplicaciones que requieren acceso a
                      ciertos archivos y otros recursos del sistema operativo.
                     Creados en Instalación:           Creados por usuario root:
                          (UID < 1000)                      (UID >= 1000)
                     root: Para administración del            gcolchado
                     sistema operativo.                       jperez
 Multiusuario        otros usuarios del sistema.              acastillo

                                        $ cat /etc/passwd
Conceptos:
Linux - Usuarios y Grupos
                       $ cat /etc/passwd             $ cat /etc/group
 Ubuntu Server
 22.04 x 64 bits
                            1 Grupo                   0 .. N Grupos
                            primario                   adicionales




                                           Usuario
 Multiusuario
          Conceptos:
          Linux - Usuarios y Grupos. Cómo crear un usuario ?

           Ubuntu Server                 $ useradd -m jperez
           22.04 x 64 bits                                           Nombre de usuario
                                                               Crea su directorio home automáticamente
                                           Por defecto se crea un grupo con el mismo nombre de usuario y se le
                                           asigna como grupo primario

                                         $ passwd jperez
                                           Para crear un password o contraseña
                                                                               Login o $ su jperez y luego $ id
                                         $ userdel jperez
            Multiusuario                   Para eliminar el usuario

Nota: Ejecutar comandos con usuario root o con usuario que tenga permisos de root (pertenezca al grupo sudo)
$ sudo -i    (Me convierte en root), de lo contrario:
$ sudo useradd -m jperez
Conceptos:
Linux - Usuarios y Grupos. Cómo crear un usuario ?

 Ubuntu Server
 22.04 x 64 bits           1 Grupo              0 .. N Grupos
                          primario:             adicionales:
                         estudiantes                tesistas




                                       jperez
 Multiusuario
          Conceptos:
          Linux - Usuarios y Grupos. Cómo crear un grupo ?

           Ubuntu Server                 $ groupadd estudiantes
           22.04 x 64 bits                                          Nombre de grupo


                                         $ groupadd tesistas




            Multiusuario

Nota: Ejecutar comandos con usuario root o con usuario que tenga permisos de root (pertenezca al grupo sudo)
          Conceptos:
          Linux - Usuarios y Grupos. Cómo crear un usuario ?

           Ubuntu Server                 $ useradd -m jperez -g estudiantes -G tesistas
           22.04 x 64 bits                                                                  Grupo adicional
                                                                          Grupo primario

                                         $ passwd jperez
                                           Para crear un password o contraseña
                                                                             Login o $ su jperez y luego $ id


            Multiusuario

Nota: Ejecutar comandos con usuario root o con usuario que tenga permisos de root (pertenezca al grupo sudo)
Conceptos:
Linux - Usuarios y Grupos. Cómo crear un usuario ?

 Ubuntu Server
 22.04 x 64 bits           1 Grupo                  0 .. N Grupos
                          primario:             adicionales: tesistas,
                         estudiantes               investigadores




                                       jperez
 Multiusuario
          Conceptos:
          Linux - Usuarios y Grupos. Cómo crear un usuario ?

           Ubuntu Server                 $ groupadd investigadores
           22.04 x 64 bits

                                         $ usermod jperez -a -G investigadores
                                                                       Adiciona el Grupo adicional indicado

                                                                          $ usermod jperez -a -G sudo
                                                                             Login o $ su jperez y luego $ id

            Multiusuario                 $ userdel jperez

Nota: Ejecutar comandos con usuario root o con usuario que tenga permisos de root (pertenezca al grupo sudo)
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Conceptos: Linux - Usuarios y Grupos
Contenido                4. Conceptos: Linux - Permisos sobre
Fundamentos de              archivos
Computación en la Nube
                         5. Conceptos: Linux - Cambiar permisos
                            sobre archivos
                         6. Conceptos: Linux - Espacio ocupado por
                            directorios y por sistema de archivos
                         7. Cierre
                                  Ejercicio: Probar el acceso a los
Conceptos:                        archivos con otros usuarios

Linux - Permisos sobre archivos
                                             4
                                             2
                                             1
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Conceptos: Linux - Usuarios y Grupos
Contenido                4. Conceptos: Linux - Permisos sobre
Fundamentos de              archivos
Computación en la Nube
                         5. Conceptos: Linux - Cambiar permisos
                            sobre archivos
                         6. Conceptos: Linux - Espacio ocupado por
                            directorios y por sistema de archivos
                         7. Cierre
Conceptos:
Linux - Cambiar permisos sobre archivos

Ejemplo:                            Suma   4   2   1

$ chmod 664 archivo

$ chmod 660 archivo



Ejercicio: Probar el acceso a los
archivos con otros usuarios
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Conceptos: Linux - Usuarios y Grupos
Contenido                4. Conceptos: Linux - Permisos sobre
Fundamentos de              archivos
Computación en la Nube
                         5. Conceptos: Linux - Cambiar permisos
                            sobre archivos
                         6. Conceptos: Linux - Espacio ocupado por
                            directorios y por sistema de archivos
                         7. Cierre

Conceptos:
Linux - Espacio ocupado por directorios y sistema de archivos


                             Espacio ocupado por
                             directorios




                                            Espacio ocupado
                                            por sistema de
                                            archivos
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Conceptos: Linux - Usuarios y Grupos
Contenido                4. Conceptos: Linux - Permisos sobre
Fundamentos de              archivos
Computación en la Nube
                         5. Conceptos: Linux - Cambiar permisos
                            sobre archivos
                         6. Conceptos: Linux - Espacio ocupado por
                            directorios y por sistema de archivos
                         7. Cierre
Cierre:
Grupos, Usuarios y Permisos en Linux

Qué aprendimos?

• Aprender a crear grupos y usuarios en Linux

• Entender los permisos de archivos en Linux

• Aprender a cambiar permisos de archivos en Linux
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
