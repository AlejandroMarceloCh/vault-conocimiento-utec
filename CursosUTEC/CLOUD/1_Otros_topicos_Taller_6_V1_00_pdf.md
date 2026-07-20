---
curso: CLOUD
titulo: 1. Otros tópicos - Taller 6 - V1.00
slides: 18
fuente: 1. Otros tópicos - Taller 6 - V1.00.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Otros tópicos
Semana 15 - Taller 6: Web Scraping en framework
serverless

                         ELABORADO POR: GERALDO COLCHADO
                              Con apoyo de Asistente de Cátedra y Laboratorio:
                              • Rubén Aaron Coorahua (ruben.coorahua@utec.edu.pe)
                            1. Objetivo del taller 6
                            2. Concepto: Web Scraping
                            3. Ejercicio 1: Web Scraping de Web Bomberos
Contenido                   4. Ejercicio 2: Propuesto
Web Scraping en framework   5. Ejercicio 3: Propuesto
serverless
                            6. Cierre
Web Scraping
Objetivo del Taller 6
• Comprender qué es Web Scraping
• Realizar Web Scraping en la Web de Bomberos
                            1. Objetivo del taller 6
                            2. Concepto: Web Scraping
                            3. Ejercicio 1: Web Scraping de Web Bomberos
Contenido                   4. Ejercicio 2: Propuesto
Web Scraping en framework   5. Ejercicio 3: Propuesto
serverless
                            6. Cierre
            Concepto
            Web Scraping

     “Extraer Legalmente el Contenido de
     la Web”

     “El web scraping se refiere al proceso
     de extracción de contenidos y datos de
     sitios web mediante software”




Fuente: https://kinsta.com/es/base-de-conocimiento/que-es-web-scraping/
            Concepto
            Web Scraping




                                  Ejemplos de tipos de datos que puedes scrapear de la web

Fuente: https://kinsta.com/es/base-de-conocimiento/que-es-web-scraping/
                            1. Objetivo del taller 6
                            2. Concepto: Web Scraping
                            3. Ejercicio 1: Web Scraping de Web Bomberos
Contenido                   4. Ejercicio 2: Propuesto
Web Scraping en framework   5. Ejercicio 3: Propuesto
serverless
                            6. Cierre
    Web Scraping
    Ejercicio 1: Web Scraping de Web Bomberos
•    Paso 1: Cree un repositorio en github con nombre api-web-scraping y suba los
     archivos indicados por el docente previa actualización de org y role en serverless.yml

•    Paso 2: Ingrese a “MV para serverless”

•    Paso 3: Actualice el archivo credentials en /home/ubuntu/.aws

•    Paso 4: Ingrese al directorio /home/ubuntu/lambdas/ y descargue el repositorio de
     github con git clone.
    Web Scraping
    Ejercicio 1: Web Scraping de Web Bomberos
•    Paso 5: Instale el pip3

     sudo apt install python3-pip

•    Paso 6: Instale las librerías no
     estándar de python3 en el mismo
     directorio y verifique:

     pip3 install -r requirements.txt -t .
    Web Scraping
    Ejercicio 1: Web Scraping de Web Bomberos
•    Paso 7: Despliegue el api y verifique

     serverless deploy
         Web Scraping
         Ejercicio 1: Web Scraping de Web Bomberos
•    Paso 8: Verifique que se haya grabado correctamente en dynamoDB la información de la web




https://sgonorte.bomberosperu.gob.pe/24horas/?criterio=/       Tabla en DynamoDB
                            1. Objetivo del taller 6
                            2. Concepto: Web Scraping
                            3. Ejercicio 1: Web Scraping de Web Bomberos
Contenido                   4. Ejercicio 2: Propuesto
Web Scraping en framework   5. Ejercicio 3: Propuesto
serverless
                            6. Cierre
          Web Scraping
          Ejercicio 2: Propuesto
Corregir la correspondencia columna vs contenido en tabla DynamoDB. Analice y modifique el lambda
scrap_table.py.




 https://sgonorte.bomberosperu.gob.pe/24horas/?criterio=/      Tabla en DynamoDB
                            1. Objetivo del taller 6
                            2. Concepto: Web Scraping
                            3. Ejercicio 1: Web Scraping de Web Bomberos
Contenido                   4. Ejercicio 2: Propuesto
Web Scraping en framework   5. Ejercicio 3: Propuesto
serverless
                            6. Cierre
       Web Scraping
       Ejercicio 3: Propuesto
Para todos los registros que en la columna “Tipo” contenga la palabra “INCENDIO” se debe notificar
a un tema SNS y al correo que esté suscrito. Modifique el lambda scrap_table.py.
                            1. Objetivo del taller 6
                            2. Concepto: Web Scraping
                            3. Ejercicio 1: Web Scraping de Web Bomberos
Contenido                   4. Ejercicio 2: Propuesto
Web Scraping en framework   5. Ejercicio 3: Propuesto
serverless
                            6. Cierre
Cierre:
Web Scraping - Qué aprendimos?
• Qué es Web Scraping
• Web Scraping en la Web de Bomberos
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
