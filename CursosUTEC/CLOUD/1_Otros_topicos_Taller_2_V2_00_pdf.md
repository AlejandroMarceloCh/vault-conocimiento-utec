---
curso: CLOUD
titulo: 1. Otros tópicos - Taller 2 - V2.00
slides: 27
fuente: 1. Otros tópicos - Taller 2 - V2.00.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Otros tópicos
Semana 13 - Taller 2: Enfoque aplicaciones serverless

                       ELABORADO POR: GERALDO COLCHADO
                       1. Objetivo del taller 2
                       2. Ejercicio 1: Framework serverless para lambdas
                       3. Ejercicio 2: Automatizar despliegue API REST
Contenido              4. Ejercicio 3: AWS CLI
Enfoque aplicaciones   5. Ejercicio 4: Ejercicio propuesto 1
serverless
                       6. Ejercicio 5: Ejercicio propuesto 2
                       7. Cierre
Enfoque aplicaciones serverless
Objetivo del Taller 2
• Aprender a utilizar el framework serverless para lambdas
• Aprender lo básico de AWS CLI
                       1. Objetivo del taller 2
                       2. Ejercicio 1: Framework serverless para lambdas
                       3. Ejercicio 2: Automatizar despliegue API REST
Contenido              4. Ejercicio 3: AWS CLI
Enfoque aplicaciones   5. Ejercicio 4: Ejercicio propuesto 1
serverless
                       6. Ejercicio 5: Ejercicio propuesto 2
                       7. Cierre
          Enfoque aplicaciones serverless
          Ejercicio 1: Framework serverless




Fuente: https://www.serverless.com/
Enfoque aplicaciones serverless
Ejercicio 1: Framework serverless
Paso 1: Crear una nueva máquina virtual
           Enfoque aplicaciones serverless
           Ejercicio 1: Framework serverless
Paso 2: Ingrese a la “MV para serverless” e instale node.js v20 y AWS CLI v2

ssh -i ./.ssh/labsuser.pem ubuntu@reemplazar_IP

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
source ~/.bashrc
nvm install 20
node -v
npm -v

sudo apt install unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
          Enfoque aplicaciones serverless
          Ejercicio 1: Framework serverless
          Paso 3: Instale serverless:

          npm install -g serverless




Fuente: https://www.serverless.com/
Enfoque aplicaciones serverless
Ejercicio 1: Framework serverless
Paso 4: Configure las credenciales de acceso a AWS

Crear el directorio /home/ubuntu/.aws

Crear el archivo credentials dentro del directorio anterior con el contenido indicado por el
docente. Nota: Estas credenciales sólo son válidas durante el Lab de AWS Academy (4 horas)
       Enfoque aplicaciones serverless
       Ejercicio 1: Framework serverless
Paso 5: Cree un usuario en https://www.serverless.com/ con su correo de @utec y un nombre de Organization
                       1. Objetivo del taller 2
                       2. Ejercicio 1: Framework serverless para lambdas
                       3. Ejercicio 2: Automatizar despliegue API REST
Contenido              4. Ejercicio 3: AWS CLI
Enfoque aplicaciones   5. Ejercicio 4: Ejercicio propuesto 1
serverless
                       6. Ejercicio 5: Ejercicio propuesto 2
                       7. Cierre
          Enfoque aplicaciones serverless
          Ejercicio 2: Automatizar despliegue API REST
Paso 1: Crear un directorio lambdas y luego “api-alumnos”
/home/ubuntu/lambdas/api-alumnos

Paso 2: Copiar los archivos indicados por el docente



Paso 3: Modificar el org y role en serverless.yml




Fuente: https://www.serverless.com/
           Enfoque aplicaciones serverless
           Ejercicio 2: Automatizar despliegue API REST
Paso 4: Login a serverless

serverless login




Paso 5: Desplegar el lambda y api Gateway

serverless deploy




Fuente: https://www.serverless.com/
          Enfoque aplicaciones serverless
          Ejercicio 2: Automatizar despliegue API REST
          Paso 6: Probar en postman




Fuente: https://www.serverless.com/
           Enfoque aplicaciones serverless
           Ejercicio 2: Automatizar despliegue API REST
Paso 7: Analice el serverless.yml y los
nombres de lambda y api gateway




Fuente: https://www.serverless.com/
                       1. Objetivo del taller 2
                       2. Ejercicio 1: Framework serverless para lambdas
                       3. Ejercicio 2: Automatizar despliegue API REST
Contenido              4. Ejercicio 3: AWS CLI
Enfoque aplicaciones   5. Ejercicio 4: Ejercicio propuesto 1
serverless
                       6. Ejercicio 5: Ejercicio propuesto 2
                       7. Cierre
          Enfoque aplicaciones serverless
          Ejercicio 3: AWS CLI




Fuente: https://aws.amazon.com/es/cli/
          Enfoque aplicaciones serverless
          Ejercicio 3: AWS CLI
          Pre - requisito: Validar que haya configurado las credenciales de acceso a AWS. Nota: Estas
          credenciales sólo son válidas durante el Lab de AWS Academy (4 horas)




          Paso 1: Validar que esté instalado el AWS CLI



Fuente: https://aws.amazon.com/es/cli/
          Enfoque aplicaciones serverless
          Ejercicio 3: AWS CLI
          Ejemplo 1: Listar todos los buckets

          $ aws s3 ls




Fuente: https://aws.amazon.com/es/cli/
          Enfoque aplicaciones serverless
          Ejercicio 3: AWS CLI
          Ejemplo 2: Listar todos los temas de SNS

          $ aws sns list-topics --region us-east-1




Fuente: https://aws.amazon.com/es/cli/

                       1. Objetivo del taller 2
                       2. Ejercicio 1: Framework serverless para lambdas
                       3. Ejercicio 2: Automatizar despliegue API REST
Contenido              4. Ejercicio 3: AWS CLI
Enfoque aplicaciones   5. Ejercicio 4: Ejercicio propuesto 1
serverless
                       6. Ejercicio 5: Ejercicio propuesto 2
                       7. Cierre
Enfoque aplicaciones serverless
Ejercicio 4: Ejercicio propuesto 1
• Automatice el despliegue del lambda “CrearAlumno” usando el archivo entregado por el
  docente “CrearAlumno.py” y modificando el serverless.yml manteniendo el mismo api
  Gateway

• Publique la foto de ejecución en postman de su api rest
                       1. Objetivo del taller 2
                       2. Ejercicio 1: Framework serverless para lambdas
                       3. Ejercicio 2: Automatizar despliegue API REST
Contenido              4. Ejercicio 3: AWS CLI
Enfoque aplicaciones   5. Ejercicio 4: Ejercicio propuesto 1
serverless
                       6. Ejercicio 5: Ejercicio propuesto 2
                       7. Cierre
          Enfoque aplicaciones serverless
          Ejercicio 5: Ejercicio propuesto 2
• Revise este enlace: https://docs.aws.amazon.com/es_es/cli/latest/userguide/cli-services-s3-commands.html

• Elabore un comando que permita copiar todos los archivos de un directorio de un bucket a otro bucket S3

• Suba en el padlet una captura de pantalla de la ejecución del comando y la evidencia de los archivos
  copiados.




Fuente: https://aws.amazon.com/es/cli/
                       1. Objetivo del taller 2
                       2. Ejercicio 1: Framework serverless para lambdas
                       3. Ejercicio 2: Automatizar despliegue API REST
Contenido              4. Ejercicio 3: AWS CLI
Enfoque aplicaciones   5. Ejercicio 4: Ejercicio propuesto 1
serverless
                       6. Ejercicio 5: Ejercicio propuesto 2
                       7. Cierre
Cierre:
Enfoque aplicaciones serverless - Qué aprendimos?
• Utilizar el framework serverless para lambdas
• Lo básico de AWS CLI
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
