---
curso: BIGDATA
titulo: 15 - Semana 13/Sem13_Privacidad de Datos
slides: 27
fuente: 15 - Semana 13/Sem13_Privacidad de Datos.pdf
---

Privacidad y
Seguridad de los
Datos
Mg. Aldo Lezama Benavides


Semana 13
        Objetivo de la sesión

1. Comprender los principios fundamentales de la seguridad y privacidad
   de datos, reconociendo la importancia de proteger la información
   personal frente a riesgos de exposición, mal uso o reidentificación.
2. Analizar las principales técnicas de anonimización —como supresión,
   enmascaramiento, generación de datos sintéticos, generalización y k-
   anonimato— y su aplicación práctica para equilibrar privacidad y utilidad
   analítica.
3. Aplicar conceptos y herramientas en Python que permitan transformar
   datasets sensibles en versiones seguras mediante métodos de
   anonimización reproducibles y auditables.
        Contenido de la sesión

 01.              02.            03.

Conceptos       Técnicas de    Modelos de
 Básicos       Anonomización   Privacidad
01.   Conceptos Básicos
                                       Introducción


• La protección de datos personales es uno de los pilares más
  importantes en la era digital. Las organizaciones manejan
  información sensible de millones de personas y, por tanto,
  tienen la responsabilidad ética y legal de garantizar su
  privacidad.
• Exploraremos técnicas de anonimización de datos: como la
  supresión, el enmascaramiento, la generación de datos
  sintéticos, la generalización, el k-anonimato y la privacidad
  diferencial.
                ¿Por qué importa la privacidad de datos?


• El escándalo de Facebook y Cambridge Analytica en 2018
  evidenció cómo el mal uso de datos personales puede tener
  un impacto masivo. La información de más de 87 millones de
  usuarios fue recolectada sin consentimiento y empleada para
  manipular el comportamiento electoral. Este caso marcó un
  antes y un después en la percepción pública sobre la
  privacidad, impulsando nuevas regulaciones y políticas de
  protección de datos.
• La lección es clara: los datos son poder, y su mal uso puede
  socavar la confianza, la democracia y la reputación de las
  empresas. Cuidar la privacidad es, por tanto, una cuestión
  ética, legal y estratégica.
                      ¿Qué entendemos por privacidad?


La privacidad no consiste simplemente en ocultar información,
sino en controlar su flujo. Según la definición académica, es “la
capacidad de asegurar que la información fluya de acuerdo
con normas sociales y legales aceptadas”.
Esto implica decidir quién puede acceder, cuándo, y para qué
fines. La privacidad es contextual: lo que consideramos privado
depende del entorno, la cultura y la finalidad del uso de los
datos.
En la era digital, el desafío radica en mantener este control
cuando los datos son replicados, analizados o compartidos por
sistemas automatizados.
                         Tipos de Información Personal


La Identificación de Información Personal (PII) se refiere a
cualquier dato que pueda identificar directa o indirectamente a
una persona. Existen dos tipos:
• PII   sensible:   incluye   nombre   completo,    número    de
  documento, datos financieros o médicos. Su exposición
  puede causar daño, discriminación o fraude.
• PII no sensible: datos como género, ocupación o código
  postal. Aunque no identifican por sí solos, pueden combinarse
  con otros y revelar identidades.
Por ejemplo, si sabemos que alguien tiene 37 años, vive en un
distrito específico y trabaja en una empresa concreta, es posible
identificarlo sin necesidad de su nombre
              Regulaciones de privacidad: el caso del GDPR
El Reglamento General de Protección de Datos (GDPR) de la Unión
Europea marcó un hito mundial en la protección de la información
personal. Su propósito es garantizar que los datos sean tratados con
respeto a los derechos de las personas. Sus principios fundamentales son:
1. Licitud, lealtad y transparencia: los datos solo deben recolectarse con
   un propósito legítimo.
2. Limitación de propósito: no se pueden usar para fines distintos a los
   declarados.
3. Minimización de datos: recolectar solo lo estrictamente necesario.
4. Exactitud y actualización.
5. Limitación del almacenamiento: eliminar datos cuando ya no son útiles.
El GDPR ha servido como modelo para leyes en América Latina,
incluyendo la Ley de Protección de Datos Personales (Ley N° 29733) en
Perú.
02.   Técnicas Básicas de
      Anonimización
                           Técnicas: Supresión de Datos

La supresión consiste en eliminar total o parcialmente los datos que pueden poner en riesgo la privacidad.
Existen dos tipos principales:
• Supresión de atributos (Attribute Suppression): elimina columnas completas, como nombres o identificadores.
• Supresión de registros (Record Suppression): elimina filas que contienen valores sensibles o atípicos.
                  Técnicas: Enmascaramiento de datos


El enmascaramiento reemplaza los valores reales
por símbolos o patrones, preservando el formato del
dato. Por ejemplo, podemos transformar números de
tarjetas o correos electrónicos sin alterar     su
estructura.
Esto mantiene la integridad del conjunto de datos
para pruebas o entrenamiento de modelos, evitando
exponer información sensible. El enmascaramiento
es ampliamente usado en bancos, hospitales y
compañías de software.
                    Técnicas: Enmascaramiento parcial


En algunos casos, es útil conservar parte de la información visible. Por ejemplo, mostrar solo las primeras letras del
correo o los últimos dígitos de un número:




Así se logra un equilibrio entre anonimización y comprensión visual del dato.
                 Técnicas: Generación de datos sintéticos


La   librería   Faker   de   Python   permite   generar
información ficticia pero verosímil. Podemos crear
nombres, direcciones, correos y números de tarjetas:


Los datos sintéticos son muy valiosos en etapas de
desarrollo, simulaciones o pruebas donde se necesita
un dataset realista sin exponer personas reales.
                        Técnicas: Generalización de datos


La generalización reemplaza valores específicos por categorías
más amplias.
Por ejemplo:
• Edad: 34 → (30–40)
• Ocupación: “Bailarín” → “Artista”
Este método reduce el riesgo de reidentificación manteniendo la
utilidad para análisis estadístico.
                                Privacidad vs. Utilidad


Toda técnica de anonimización implica una pérdida de
información.
El reto consiste en encontrar un punto de equilibrio: proteger la
identidad sin sacrificar la capacidad analítica. Un dataset
completamente anónimo puede ser inútil; uno demasiado
detallado puede ser peligroso. La clave está en la minimización
proporcional: solo anonimizar lo necesario para cumplir el
objetivo
03.   Modelos de Privacidad
                                          Introducción


• Cuando se trata de anonimización de datos, una de las técnicas más utilizadas es K-Anonymity. Este enfoque
  garantiza que las identidades de las personas no puedan determinarse fácilmente a partir de los datos
  publicados, protegiendo así su privacidad. K-Anonimato es un concepto poderoso que ha ganado mucha
  atención en los últimos años debido a las crecientes preocupaciones sobre las violaciones de datos y el acceso
  no autorizado a información personal.
                           Definición del K-Anonimato


• K-Anonimato se refiere a una propiedad que garantiza la privacidad de las personas en un conjunto de
  datos. Garantiza que cualquier información divulgada no pueda vincularse a un individuo específico con un
  alto grado de confianza. En otras palabras, cuando los datos son K-Anonimizados, se vuelven
  indistinguibles de al menos K-1 otros individuos en el conjunto de datos. Esto hace que sea increíblemente
  difícil para un atacante identificar la información confidencial de una persona específica a partir de los datos
  anonimizados.
                      Requisitos para lograr el anonimato K
Para lograr K-Anonimato, se deben cumplir ciertos requisitos:


a) Generalización: la generalización implica reemplazar valores específicos en el conjunto de datos con valores más
   generales o menos precisos. Por ejemplo, en lugar de almacenar la edad exacta de un individuo, se puede
   generalizar en rangos de edad como 20-30, 30-40, etc. Este proceso ayuda a proteger las identidades de las
   personas al dificultar la vinculación de registros específicos con ellas.
b) Supresión: la supresión implica eliminar u omitir ciertos atributos del conjunto de datos por completo. Esto
   garantiza que no se divulgue información confidencial, como números de seguro social o direcciones. Sin
   embargo, suprimir demasiados atributos podría provocar una pérdida de utilidad de los datos, haciéndolos menos
   útiles para el análisis.
c) Perturbación: la perturbación implica agregar ruido o valores aleatorios al conjunto de datos. Al introducir ligeras
   modificaciones en los datos, resulta más difícil identificar individuos específicos. Sin embargo, es crucial lograr el
   equilibrio adecuado entre privacidad y precisión de los datos, ya que una perturbación excesiva puede hacer que
   los datos sean inútiles para el análisis.

Ejemplo
                           Limitaciones del anonimato K

Aunque efectivo, el k-anonimato tiene limitaciones.


No protege contra ataques de homogeneidad (cuando todos los miembros de un grupo tienen el mismo valor
sensible) ni de background knowledge (cuando un atacante posee información externa).


Por ello, se complementa con modelos más sofisticados como l-diversity y t-closeness.
                                       Privacidad diferencial

La privacidad diferencial (DP) es un enfoque
matemático que introduce ruido aleatorio en los
resultados, de modo que la inclusión o
exclusión    de      un    individuo   no    afecte
significativamente el resultado global.
Así se garantiza que ninguna persona pueda
ser   identificada    ni    siquiera    de   forma
probabilística.
                                       Privacidad diferencial



La privacidad diferencial es un conjunto de
sistemas y prácticas que ayudan a mantener la
seguridad   y   la   privacidad   de    los   datos
personales. En las soluciones de aprendizaje
automático, la privacidad diferencial puede ser
un requisito para el cumplimiento normativo.
                       Métricas de privacidad diferencial

La privacidad diferencial busca proteger contra la posibilidad de que un usuario genere un número indefinido de
informes que, eventualmente, revelen datos confidenciales. Un valor denominado épsilon mide el nivel de ruido (o
privacidad) de un informe. Épsilon tiene una relación inversa con el ruido o la privacidad: cuanto menor sea el valor de
épsilon, más ruido (y privacidad) tendrán los datos.


Los valores de épsilon son no negativos. Los valores inferiores a 1 proporcionan negación plausible completa.
Cualquier valor superior a 1 implica un mayor riesgo de exposición de los datos reales. Al implementar soluciones de
aprendizaje automático con privacidad diferencial, se recomienda utilizar datos con valores de épsilon entre 0 y 1.


Otro valor directamente correlacionado con épsilon es delta . Delta mide la probabilidad de que un informe no sea
completamente privado. Cuanto mayor sea delta, mayor será épsilon. Debido a esta correlación, épsilon se utiliza con
mayor frecuencia.
                      Conclusiones
      La privacidad de datos es un componente esencial de la confianza digital, y debe
01.   abordarse desde una perspectiva ética, legal y técnica en toda organización que
      gestione información personal.


      Las técnicas de anonimización permiten proteger la identidad sin perder valor
02.   analítico, siempre que se logre un balance adecuado entre precisión y
      confidencialidad.


      Modelos como el k-anonimato y la privacidad diferencial ofrecen marcos
03.   cuantitativos para garantizar que los datos publicados o analizados no puedan
      vincularse a individuos específicos, fortaleciendo la seguridad informacional.

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
