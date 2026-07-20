---
curso: ACD
titulo: [2025-1] Proyecto Parte I - Adquisición de datos-3
slides: 3
fuente: [2025-1] Proyecto Parte I - Adquisición de datos-3.pdf
---

 DS3021 Análisis Computacional de Datos
 Semestre 2025-1



                               Proyecto Final
                   DS3021 Análisis Computacional de Datos

 Parte I: Adquisición de Datos

I.     Objetivo

       ● Aplicar técnicas de adquisición de datos para el proceso de análisis
         computacional de datos

 II.   Instrucciones

 Para este proyecto usaremos como fuente una página peruana y que tenga
 información relevante para llevar a cabo un proceso de web scraping. Puede tomar
 como referencia alguna de las mostradas abajo u otra y realice lo siguiente:
       i. Crear un script en Python para extraer datos de la página web seleccionada. El
          script debe:
              o Utilizar técnicas apropiadas de web scraping (BeautifulSoup, Scrapy,
                  Selenium o APIs)
              o Extraer al menos 6 atributos diferentes relevantes para análisis (debe
                  contener tanto atributos numéricos como categóricos)
              o Manejar adecuadamente paginación si es necesario
              o Incluir al menos 1000 registros en el dataset final
    ii. Exportar el dataset como archivo CSV con codificación UTF-8
   iii. Crear un diccionario de datos que incluya:
              o Nombre de cada variable/columna
              o Tipo de dato
              o Descripción breve del contenido
              o Ejemplo de valores


III.   Páginas sugeridas

 1.    Noticias y Medios de Comunicación

          Página                          URL               Posibles datos a extraer
                                                           Titulares, resúmenes,
        El Comercio             https://elcomercio.pe/
                                                           fechas, autores, secciones
                                                           Noticias por categoría,
        La República            https://larepublica.pe/
                                                           fecha, contenido
DS3021 Análisis Computacional de Datos
Semestre 2025-1

                                                         Últimas noticias, política,
        Perú21                   https://peru21.pe/
                                                         deportes
                                                         Noticias económicas y
        Gestión                  https://gestion.pe/
                                                         financieras
                                                         Investigaciones y
     Ojo Público              https://ojo-publico.com/
                                                         periodismo de datos


2. Portales de Empleo

        Página                           URL             Posibles datos a extraer
                                                        Cargo, empresa, salario,
    Bumeran Perú          https://www.bumeran.com.pe/
                                                        requisitos
                         https://www.computrabajo.com.p Descripción de empleos,
 Computrabajo Perú
                                           e/           ciudad, categoría
                                                        Puesto, empresa,
     Indeed Perú               https://pe.indeed.com/   ubicación, sueldo (si
                                                        aplica)

3. Comparación de Precios / Productos

       Página                            URL             Posibles datos a extraer
                                                         Precio, nombre del
   Falabella Perú          https://www.falabella.com.pe/
                                                         producto, categoría
                                                         Precios de alimentos y
      Plaza Vea           https://www.plazavea.com.pe/
                                                         otros productos
                                                         Tecnología,
      Linio Perú             https://www.linio.com.pe/   electrodomésticos,
                                                         categorías y precios
                                                         Publicaciones de
   Mercado Libre
                        https://www.mercadolibre.com.pe/ productos, precios,
       Perú
                                                         descripción


4. Clima y Transporte

        Página                           URL              Posibles datos a extraer
                                                         Temperaturas,
       Senamhi             https://www.senamhi.gob.pe/   precipitaciones,
                                                         pronóstico
                         https://www.metropolitano.com.p Horarios, estaciones,
 Metropolitano Lima
                                        e/               rutas
 ATU (Autoridad de                                       Líneas, paraderos,
                              https://www.atu.gob.pe/
 Transporte Urbano)                                      proyectos viales
 DS3021 Análisis Computacional de Datos
 Semestre 2025-1

 5. Datos Gubernamentales

        Página                            URL                 Posibles datos a extraer
   Superintendencia                                          Universidades,
     Nacional de             https://www.sunedu.gob.pe/      licenciamiento, datos de
  Educación (Sunedu)                                         programas
      Sistema de                                             Razón social, estado del
                                      https://e-
   Consulta de RUC                                           RUC, actividad
                              consultaruc.sunat.gob.pe/
       (SUNAT)                                               económica
       EsSalud             https://www.essalud.gob.pe/tran   Contratos, servicios
    Transparencia                    sparencia/              médicos, reportes

IV.   Consideraciones Importantes

      ●   Respetar robots.txt: Verifique las políticas del sitio antes de scraping
      ●   Ética y legalidad: No extraer información personal sensible
      ●   Rendimiento: Usar ‘time.sleep()’ entre requests para no saturar servidores
      ●   Headers: Utilizar User-Agent realista para evitar bloqueos
      ●   Manejo de errores: Implementar ‘try-except’ para conexiones fallidas
      ●   Almacenamiento: Guardar datos de forma incremental para evitar pérdidas

V.    Entregables y Deadlines

      ● Deadline: 8 de noviembre de 2025
      ● Entregables:
            ○ Dataset .csv
            ○ Script .ipynb (documentado)
            ○ Diccionario de datos .pdf
      ● El peso de esta primera parte de su proyecto es de 30% de la nota final de
        Proyecto P.
