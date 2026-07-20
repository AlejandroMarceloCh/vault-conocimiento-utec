---
curso: CLOUD
titulo: 1. Fund. Comp. Nube - Taller 1 - V1.01
slides: 25
fuente: 1. Fund. Comp. Nube - Taller 1 - V1.01.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Fundamentos de Computación en la Nube
Semana 1 - Taller 1: Introducción a Linux

                       ELABORADO POR: GERALDO COLCHADO
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Ejercicio 1: Instalar cliente SSH
Contenido                4. Ejercicio 2: Ingresar y salir de Linux
Fundamentos de
Computación en la Nube
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Compilar y ejecutar en C++
                         7. Ejercicio 5: Ejecutar en Python3
                         8. Ejercicio 6: Ejecutar en node.js
                         9. Cierre
Objetivo del taller 1:
Introducción a Linux

• Aprender a ingresar y salir de máquina virtual Linux en la nube
  con usuario y password

• Aprender comandos básicos de Linux

• Aprender a ejecutar programas en lenguajes de programación en
  Linux
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Ejercicio 1: Instalar cliente SSH
Contenido                4. Ejercicio 2: Ingresar y salir de Linux
Fundamentos de
Computación en la Nube
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Compilar y ejecutar en C++
                         7. Ejercicio 5: Ejecutar en Python3
                         8. Ejercicio 6: Ejecutar en node.js
                         9. Cierre
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
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Ejercicio 1: Instalar cliente SSH
Contenido                4. Ejercicio 2: Ingresar y salir de Linux
Fundamentos de
Computación en la Nube
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Compilar y ejecutar en C++
                         7. Ejercicio 5: Ejecutar en Python3
                         8. Ejercicio 6: Ejecutar en node.js
                         9. Cierre
Ejercicio 1:
Instalar cliente SSH

                             • Instale la extensión “Secure Shell” en Google Chrome (Menú
                               “Más herramientas” / “Extensiones” / “Abrir Chrome Web
                               Store”, luego buscar “Secure Shell”)




Cliente SSH (Secure Shell)
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Ejercicio 1: Instalar cliente SSH
Contenido                4. Ejercicio 2: Ingresar y salir de Linux
Fundamentos de
Computación en la Nube
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Compilar y ejecutar en C++
                         7. Ejercicio 5: Ejecutar en Python3
                         8. Ejercicio 6: Ejecutar en node.js
                         9. Cierre
Ejercicio 2:
Ingresar a Linux - Alternativa 1
                                   • Dirección IP: 146.190.169.149
                                   • Usuario: utec
                                   • Password: utec
Ejercicio 2:
Ingresar a Linux - Alternativa 2
ssh utec@146.190.169.149
Ejercicio 2:
Salir de Linux

                 • Salir de Linux:

                    $ exit
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Ejercicio 1: Instalar cliente SSH
Contenido                4. Ejercicio 2: Ingresar y salir de Linux
Fundamentos de
Computación en la Nube
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Compilar y ejecutar en C++
                         7. Ejercicio 5: Ejecutar en Python3
                         8. Ejercicio 6: Ejecutar en node.js
                         9. Cierre
                                                               Ejercicio 3 - Comandos básicos en Linux
                                                               •     Listar archivos
Ejercicio 3:                                                   •
                                                               •
                                                                     Crear directorio y acceder
                                                                     Crear archivo de texto con

Comandos básicos en Linux                                            pendientes



       Cada alumno cree un directorio dentro de su sección con la
       primera letra de su nombre y luego el apellido. Ejemplo: gcolchado
                                                                          Ejercicio 3 - Comandos básicos en Linux
                                                                          •     Listar archivos
        Ejercicio 3:                                                      •
                                                                          •
                                                                                Crear directorio y acceder
                                                                                Crear archivo de texto con

        Comandos básicos en Linux (1 de 3)                                      pendientes



Comando Funcionalidad                                       Ejemplo
ls         list: Lista el contenido del directorio (-a      ls -la
           muestra los archivos ocultos)
man        manual: Muestra la ayuda de un comando           man ls
pwd        print working directory: Imprime el directorio   pwd
           actual
mkdir      make directory: Crea un directorio               mkdir lab5
cd         change directory: Cambia al directorio indicado cd lab5
           (Directorio anterior se representa como ..)     cd ..
pico       Abre archivo en editor de texto pico. Si el      pico holamundo.cpp
           archivo no existe lo crea.
                                                                          Ejercicio 3 - Comandos básicos en Linux
                                                                          •     Listar archivos
        Ejercicio 3:                                                      •
                                                                          •
                                                                                Crear directorio y acceder
                                                                                Crear archivo de texto con

        Comandos básicos en Linux (2 de 3)                                      pendientes



Comando Funcionalidad                                       Ejemplo
cp         copy: Copia un archivo de un directorio a otro   cp holamundo.cpp /home/ubuntu/lab5

mv         move: Renombra un archivo                        mv holamundo.cpp hola.cpp

cat        Muestra en pantalla el contenido de un archivo cat hola.cpp
           de texto
rm         remove: Borra un archivo                         rm hola.cpp

clear      Limpia la pantalla de la terminal                clear
                                                                           Ejercicio 3 - Comandos básicos en Linux
                                                                           •     Listar archivos
       Ejercicio 3:                                                        •
                                                                           •
                                                                                 Crear directorio y acceder
                                                                                 Crear archivo de texto con

       Comandos básicos en Linux (3 de 3)                                        pendientes



Comando Funcionalidad                                        Ejemplo
exit       Sale de la sesión de usuario de la terminal de    exit
           comandos
sudo       Ejecutar un comando en modo superusuario          sudo [reemplazar_comando]

shutdown   Reinicia (-r) o apaga (-h) el sistema operativo   sudo shutdown -r now
           Linux                                             sudo shutdown -h now
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Ejercicio 1: Instalar cliente SSH
Contenido                4. Ejercicio 2: Ingresar y salir de Linux
Fundamentos de
Computación en la Nube
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Compilar y ejecutar en C++
                         7. Ejercicio 5: Ejecutar en Python3
                         8. Ejercicio 6: Ejecutar en node.js
                         9. Cierre
Ejercicio 4:
Compilar y ejecutar en C++

• Cree un programa holamundo.cpp con pico:     • Compile el programa:

#include <iostream>                               $ g++ -o hola.exe holamundo.cpp
using namespace std;

int main()
                                               • Ejecute el programa:
{
     cout << "Hola mundo desde C++" << endl;
                                                  $ ./hola.exe
     return 0;
                                                  Hola mundo
}
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Ejercicio 1: Instalar cliente SSH
Contenido                4. Ejercicio 2: Ingresar y salir de Linux
Fundamentos de
Computación en la Nube
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Compilar y ejecutar en C++
                         7. Ejercicio 5: Ejecutar en Python3
                         8. Ejercicio 6: Ejecutar en node.js
                         9. Cierre
Ejercicio 5:
Ejecutar en Python3

• Cree un programa holamundo.py con pico:   • Ejecute el programa:

print("Hola Mundo desde python");              $ python3 holamundo.py
                                               Hola mundo

                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Ejercicio 1: Instalar cliente SSH
Contenido                4. Ejercicio 2: Ingresar y salir de Linux
Fundamentos de
Computación en la Nube
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Compilar y ejecutar en C++
                         7. Ejercicio 5: Ejecutar en Python3
                         8. Ejercicio 6: Ejecutar en node.js
                         9. Cierre
Ejercicio 6:
Ejecutar en node.js

• Cree un programa holamundo.js con pico:   • Ejecute el programa:

console.log("Hola Mundo desde node.js")        $ node holamundo.js
                                               Hola mundo
                         1. Objetivo del taller 1
                         2. Máquina virtual Linux en nube
                         3. Ejercicio 1: Instalar cliente SSH
Contenido                4. Ejercicio 2: Ingresar y salir de Linux
Fundamentos de
Computación en la Nube
                         5. Ejercicio 3: Comandos básicos
                         6. Ejercicio 4: Compilar y ejecutar en C++
                         7. Ejercicio 5: Ejecutar en Python3
                         8. Ejercicio 6: Ejecutar en node.js
                         9. Cierre
Cierre:
Introducción a Linux - Qué aprendimos?

• Aprender a ingresar y salir de máquina virtual Linux en la nube
  con usuario y password

• Aprender comandos básicos de Linux

• Aprender a ejecutar programas en lenguajes de programación en
  Linux
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
