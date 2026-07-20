---
curso: CLOUD
titulo: 1. Virtualización con Máq. Vir. - Taller 2 - V1.01
slides: 22
fuente: 1. Virtualización con Máq. Vir. - Taller 2 - V1.01.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Virtualización con máquinas virtuales
Semana 2 - Taller 2: Máquina Virtual en AWS (EC2)

                      ELABORADO POR: GERALDO COLCHADO
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Página Web estática simple
                         3. Ejercicio 2: Página Web estática plantilla
Contenido                4. Ejercicio 3: Api REST python
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 4: Api REST node.js
                         6. Ejercicio 5: Apagar máquina virtual
                         7. Cierre
Objetivo del taller 2:
Máquina Virtual en AWS (EC2)
•   Publicar una Página Web estática simple
•   Publicar una Página Web estática plantilla
•   Ejecutar un Api REST python
•   Apagar máquina virtual
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Página Web estática simple
                         3. Ejercicio 2: Página Web estática plantilla
Contenido                4. Ejercicio 3: Api REST python
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 4: Api REST node.js
                         6. Ejercicio 5: Apagar máquina virtual
                         7. Cierre
Ejercicio 1:
Página web estática simple
•   Paso 1: Ingresar desde navegador a dirección-IP
•   Paso 2: Ingresar a la máquina virtual a este directorio:
    /var/www/html/
•   Paso 3: Crear el directorio /var/www/html/utec y dar permisos
    de escritura para usuario ubuntu:
    $ sudo mkdir utec
    $ sudo chmod 777 utec
•   Paso 4: Copiar la página web estática simple con sftp o WinSCP
•   Paso 5: Probar en el navegador dirección-IP/utec/curso.html
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Página Web estática simple
                         3. Ejercicio 2: Página Web estática plantilla
Contenido                4. Ejercicio 3: Api REST python
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 4: Api REST node.js
                         6. Ejercicio 5: Apagar máquina virtual
                         7. Cierre
Ejercicio 2:
Página web estática plantilla
•   Paso 1: Crear el directorio /var/www/html/salient y dar permisos
    de escritura para usuario ubuntu:
    $ sudo mkdir salient
    $ sudo chmod 777 salient
•   Paso 2: Copiar la página web estática plantilla con sftp o WinSCP
•   Paso 3: Probar en el navegador dirección-IP/salient
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Página Web estática simple
                         3. Ejercicio 2: Página Web estática plantilla
Contenido                4. Ejercicio 3: Api REST python
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 4: Api REST node.js
                         6. Ejercicio 5: Apagar máquina virtual
                         7. Cierre
           Ejercicio 3:
           Api REST python                            API REST con Python, Flask y SQLite3

          •     Paso 1: Crear directorio /home/ubuntu/python3/api-students
          •     Paso 2: Copiar por sftp o WinSCP o github los programas:
                app.py       (Aplicación python con flask)
                db.py        (Script crear base de datos sqlite)
          •     Paso 3: Instalar flask en máquina virtual:
                $ pip3 install flask
          •     Paso 4: Crear la base de datos sqlite
                $ python3 db.py


Referencia: https://codesnnippets.com/creating-rest-api-with-python-and-flask-web-development-with-python-and-flask-part-6/
           Ejercicio 3:
           Api REST python                            API REST con Python, Flask y SQLite3

          •     Paso 5: Abrir puerto 8000 en reglas de entrada de grupo de
                seguridad de máquina virtual
          •     Paso 6: Ejecutar api:
                $ python3 app.py
          •     Probar el api con https://www.postman.com/




Referencia: https://codesnnippets.com/creating-rest-api-with-python-and-flask-web-development-with-python-and-flask-part-6/
           Ejercicio 3:
           Api REST python                            API REST con Python, Flask y SQLite3

 Nuevo
 estudiante




Referencia: https://codesnnippets.com/creating-rest-api-with-python-and-flask-web-development-with-python-and-flask-part-6/
           Ejercicio 3:
           Api REST python                            API REST con Python, Flask y SQLite3

  Leer
  estudiantes




Referencia: https://codesnnippets.com/creating-rest-api-with-python-and-flask-web-development-with-python-and-flask-part-6/
           Ejercicio 3:
           Api REST python                            API REST con Python, Flask y SQLite3
Leer un
estudiante




Referencia: https://codesnnippets.com/creating-rest-api-with-python-and-flask-web-development-with-python-and-flask-part-6/
           Ejercicio 3:
           Api REST python                            API REST con Python, Flask y SQLite3
Modificar un
estudiante




Referencia: https://codesnnippets.com/creating-rest-api-with-python-and-flask-web-development-with-python-and-flask-part-6/
           Ejercicio 3:
           Api REST python                            API REST con Python, Flask y SQLite3

Eliminar un
estudiante




Referencia: https://codesnnippets.com/creating-rest-api-with-python-and-flask-web-development-with-python-and-flask-part-6/
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Página Web estática simple
                         3. Ejercicio 2: Página Web estática plantilla
Contenido                4. Ejercicio 3: Api REST python
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 4: Api REST node.js
                         6. Ejercicio 5: Apagar máquina virtual
                         7. Cierre
Ejercicio 4:
Api REST node.js            API REST con node.js y SQLite3

•   Busque en internet un ejemplo de Api REST con node y SQLite3 e
    implemente el api en su máquina virtual
•   Abra el puerto que necesite en su máquina virtual
•   Cree su base de datos sqlite
•   Ejecute su api
•   Pruebe el api con https://www.postman.com/
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Página Web estática simple
                         3. Ejercicio 2: Página Web estática plantilla
Contenido                4. Ejercicio 3: Api REST python
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 4: Api REST node.js
                         6. Ejercicio 5: Apagar máquina virtual
                         7. Cierre
Ejercicio 5:
Apagar máquina virtual
•   Alternativa 1: Ejecute el comando
    $ sudo shutdown -h now

•   Alternativa 2: “Detener instancia” desde la consola de AWS




Nota: La máquina virtual sólo se puede iniciar desde la consola de AWS con la opción “Iniciar
instancia”
                         1. Objetivo del taller 2
                         2. Ejercicio 1: Página Web estática simple
                         3. Ejercicio 2: Página Web estática plantilla
Contenido                4. Ejercicio 3: Api REST python
Máquina Virtual en AWS
(EC2)
                         5. Ejercicio 4: Api REST node.js
                         6. Ejercicio 5: Apagar máquina virtual
                         7. Cierre

Cierre:
Máquina Virtual en AWS (EC2) - Qué aprendimos?
•   Publicar una Página Web estática simple
•   Publicar una Página Web estática plantilla
•   Ejecutar un Api REST python
•   Apagar máquina virtual
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
