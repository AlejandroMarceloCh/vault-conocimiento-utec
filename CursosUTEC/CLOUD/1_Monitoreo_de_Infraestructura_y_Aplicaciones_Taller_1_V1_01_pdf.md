---
curso: CLOUD
titulo: 1. Monitoreo de Infraestructura y Aplicaciones - Taller 1 - V1.01
slides: 24
fuente: 1. Monitoreo de Infraestructura y Aplicaciones - Taller 1 - V1.01.pdf
---

CS2032 - Cloud Computing (Ciclo 2024-1)
Monitoreo de Infraestructura y Aplicaciones
Semana 12 - Taller 1: CloudWatch

                      ELABORADO POR: GERALDO COLCHADO
             1. Objetivo del taller 1
             2. Ejercicio 1: Paneles automáticos
             3. Ejercicio 2: Monitorear página web (FrontEnd)
Contenido    4. Ejercicio 3: Monitorear sensor IoT (BackEnd)
CloudWatch   5. Cierre
CloudWatch
Objetivo del Taller 1
• Aprender a monitorear servicios serverless usando CloudWatch
• Aprender a monitorear una página web
• Aprender a monitorear la ejecución de un backend
             1. Objetivo del taller 1
             2. Ejercicio 1: Paneles automáticos
             3. Ejercicio 2: Monitorear página web (FrontEnd)
Contenido    4. Ejercicio 3: Monitorear sensor IoT (BackEnd)
CloudWatch   5. Cierre
CloudWatch
Ejercicio 1: Paneles automáticos
CloudWatch
Ejercicio 1: Paneles automáticos
CloudWatch
Ejercicio 1: Paneles automáticos
CloudWatch
Ejercicio 1: Paneles automáticos
             1. Objetivo del taller 1
             2. Ejercicio 1: Paneles automáticos
             3. Ejercicio 2: Monitorear página web (FrontEnd)
Contenido    4. Ejercicio 3: Monitorear sensor IoT (BackEnd)
CloudWatch   5. Cierre
        CloudWatch
        Ejercicio 2: Monitorear página web (FrontEnd)
Paso 1: Crear un bucket

Paso 2: Subir página web en
directorio raíz y hacer públicos los
archivos




Paso 3: Configurar “Alojamiento de
sitios web estáticos”.
       CloudWatch
       Ejercicio 2: Monitorear página web (FrontEnd)
Paso 4: Crear un tema SNS “TemaPagWebNoDisponible” y suscriba un correo electrónico válido

Paso 5: Crear un lambda “ValidarPagWeb” que acceda a la página web y si hay error publique en tema
“TemaPagWebNoDisponible” con el código fuente entregado por el docente

Paso 6: Crear una regla en CloudWatch “ValidadorPagWeb” para ejecutar el lambda cada 1 minuto
       CloudWatch
       Ejercicio 2: Monitorear página web (FrontEnd)
Paso 7: Valide en Cloud Watch los logs de ejecución del Lambda “ValidarPagWeb”

Paso 8: Modifique el url en el lambda “ValidarPagWeb” para forzar las excepciones y le llegue el correo de
error. Ejemplos:
http://gcolchado10.s3-website-us-east-1.amazonaws.com/hola.html           (No existe el archivo hola.html)
http://gcolchado10.s3-website-us-east-1.amazonaws.com-pepe                (No existe esta página)
http://gcolchado10.s3-website-us-east-1.amazonaws.com                     (OK)

Paso 9: Desactive la regla creada en EventBridge para que ya no valide
             1. Objetivo del taller 1
             2. Ejercicio 1: Paneles automáticos
             3. Ejercicio 2: Monitorear página web (FrontEnd)
Contenido    4. Ejercicio 3: Monitorear sensor IoT (BackEnd)
CloudWatch   5. Cierre
       CloudWatch
       Ejercicio 3: Monitorear sensor IoT (BackEnd)
Paso 1: Crear tema SNS “TemaSensorIoTAveriado” y suscribir un correo válido

Paso 2: Crear una alarma en CloudWatch
CloudWatch
Ejercicio 3: Monitorear sensor IoT (BackEnd)
CloudWatch
Ejercicio 3: Monitorear sensor IoT (BackEnd)
        CloudWatch
        Ejercicio 3: Monitorear sensor IoT (BackEnd)
Paso 3: Verificar que le llegue un correo notificando que no se están recibiendo lecturas del sensor IoT
       CloudWatch
       Ejercicio 3: Monitorear sensor IoT (BackEnd)
Paso 4: Verificar que la Alarma esté en estado “En modo alarma”
        CloudWatch
        Ejercicio 3: Monitorear sensor IoT (BackEnd)
Paso 5: Habilite la regla en EventBridge para que se generen lecturas del sensor cada 1 minuto. Déjelo en ejecución por
unos 6 minutos.
       CloudWatch
       Ejercicio 3: Monitorear sensor IoT (BackEnd)
Paso 6: Verificar que la Alarma esté en estado “CORRECTO”

        CloudWatch
        Ejercicio 3: Monitorear sensor IoT (BackEnd)
Paso 7: Deshabilite la regla y verifique en unos 10 a 15 minutos más aprox. que le llegue nuevamente el correo de alarma
de que no se están recibiendo lecturas del sensor IoT y que la Alarma esté en estado “En modo alarma”
             1. Objetivo del taller 1
             2. Ejercicio 1: Paneles automáticos
             3. Ejercicio 2: Monitorear página web (FrontEnd)
Contenido    4. Ejercicio 3: Monitorear sensor IoT (BackEnd)
CloudWatch   5. Cierre
Cierre:
CloudWatch - Qué aprendimos?
• Monitorear servicios serverless usando CloudWatch
• Monitorear una página web
• Monitorear la ejecución de un backend
              Gracias




Elaborado por docente: Geraldo Colchado

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
