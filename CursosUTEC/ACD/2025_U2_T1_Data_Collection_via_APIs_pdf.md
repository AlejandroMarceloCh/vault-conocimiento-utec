---
curso: ACD
titulo: [2025] U2_T1 Data Collection via APIs
slides: 9
fuente: [2025] U2_T1 Data Collection via APIs.pdf
---

Data Collection
   vía APIs
DS3021 Análisis Computacional de Datos




                                  Mg. José Espinoza Melgarejo
Objetivo de sesión
                     Aplicar      diferentes   herramientas
                     computacionales para la recolección de
                     datos a través de APIs.
¿Cómo recolectamos los datos?
            Métodos                   Esfuerzo


            Descargar                   Baja



API (Application Program Interface)    Media



              Scrape                    Alto
1.
     Data Collection
     via APIs
                                         API
                          Application Programming Interface



Una API actúa como una capa de comunicación (una interfaz)
que permite que diferentes sistemas se comuniquen entre sí sin
tener que entender exactamente lo que hacen los demás.
  A web API


Una API web es un servicio disponible en la web que
proporciona acceso a recursos como datos sin procesar,
información filtrada y contenido integrado y dinámico,
normalmente en un formato intercambiable y listo para
usar, como JSON, CSV o XML.
                    Recolectar datos vía APIs




Sin Autenticación                           Con Autenticación
                                                            ●    1xx: Brinda información
●    Endpoint: URL de los            Web Server             ●    2xx: Exitoso
    datos.
                                                            ●    3xx: Proporcionar
●    Método (GET, PUT, POST o
                                                                información sobre
    DELETE).
                                                                redireccionamientos
●    Headers, proporcionan
                                                            ●    4xx: Error del lado del
    información como claves
                                                                cliente (nuestro error)
    de autenticación.
                                                            ●    5xx: Error del lado del
●    Data/body: GET no tiene
                                                                servidor
    esta sección
                                 Page              Page
                                Request           Content
                                      Beneficios de web APIs
                                                   Integración
                                                   Las API devuelven datos en un
                                                   formato estándar, como JSON, que
                                                   se pueden guardar y procesar.




                                                                        Automatización
                                                                        Ejecutar API y recopilar resultados es
Multiplataforma
                                                                        parte de la automatización, ya que
Cada API requiere una URL con
                                                                        las    API      contienen       código
argumentos       compatibles      o
                                                                        preconfigurado, como llamadas a
necesarios que deben ejecutarse o
                                                                        sus procesos o procedimientos
cargarse en el navegador web. Las
                                                                        internos, y dependencias necesarias,
dependencias de la máquina, el
                                                                        que          funcionan           como
sistema operativo y el navegador
                                                                        automatización.
web no son factores a considerar.



               Tiempo                                                          Seguridad
               Las API son fáciles de procesar,                                El procesamiento de API mediante
               llamar y cargar en el navegador.                                una suscripción y claves de API se
               Estas actividades toman menos                                   considera seguro. Sin embargo esta
               tiempo en comparación con las                                   seguridad se puede eludir con
               configuraciones     de máquinas                                 encabezados y servidores proxy
               completas o virtuales.                                          HTTP.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
