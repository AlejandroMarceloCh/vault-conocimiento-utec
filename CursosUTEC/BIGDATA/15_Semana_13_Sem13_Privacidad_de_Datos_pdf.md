---
curso: BIGDATA
titulo: 15 - Semana 13/Sem13_Privacidad de Datos
slides: 27
fuente: 15 - Semana 13/Sem13_Privacidad de Datos.pdf
---

## Slide 1

Portada (decorativa: fondo cian con foto del edificio UTEC).

**Privacidad y Seguridad de los Datos**
Mg. Aldo Lezama Benavides
Semana 13

## Slide 2

**Objetivo de la sesión**

Lista numerada dentro de un marco de corchetes blancos:

1. **Comprender** los principios fundamentales de la seguridad y privacidad de datos, reconociendo la importancia de proteger la información personal frente a riesgos de exposición, mal uso o reidentificación.
2. **Analizar** las principales técnicas de anonimización —como supresión, enmascaramiento, generación de datos sintéticos, generalización y k-anonimato— y su aplicación práctica para equilibrar privacidad y utilidad analítica.
3. **Aplicar** conceptos y herramientas en Python que permitan transformar datasets sensibles en versiones seguras mediante métodos de anonimización reproducibles y auditables.

## Slide 3

**Contenido de la sesión**

Tres columnas, cada una encerrada en corchetes blancos, numeradas arriba:

| 01. | 02. | 03. |
|---|---|---|
| Conceptos Básicos | Técnicas de Anonomización | Modelos de Privacidad |

## Slide 4

Separador de sección: número grande **01.** entre corchetes, ícono de portapapeles con checklist, y el título **Conceptos Básicos**.

## Slide 5

**Introducción**

- La protección de datos personales es uno de los pilares más importantes en la era digital. Las organizaciones manejan información sensible de millones de personas y, por tanto, tienen la responsabilidad ética y legal de garantizar su privacidad.
- Exploraremos técnicas de anonimización de datos: como la supresión, el enmascaramiento, la generación de datos sintéticos, la generalización, el k-anonimato y la privacidad diferencial.

**Visual (derecha):** foto stock de un hombre tocando una pantalla holográfica translúcida con el texto "PERSONAL DATA PROTECTION" sobre una red de nodos; alrededor, íconos de candados hexagonales y fondo de dígitos binarios.

## Slide 6

**¿Por qué importa la privacidad de datos?**

- El escándalo de Facebook y Cambridge Analytica en 2018 evidenció cómo el mal uso de datos personales puede tener un impacto masivo. La información de más de 87 millones de usuarios fue recolectada sin consentimiento y empleada para manipular el comportamiento electoral. Este caso marcó un antes y un después en la percepción pública sobre la privacidad, impulsando nuevas regulaciones y políticas de protección de datos.
- La lección es clara: los datos son poder, y su mal uso puede socavar la confianza, la democracia y la reputación de las empresas. Cuidar la privacidad es, por tanto, una cuestión ética, legal y estratégica.

**Visual (derecha):** fotografía de una laptop con el logo de Facebook en pantalla, frente a un cartel corporativo metálico que dice "Cambridge Analytica" / "…tion Limited" y "STRATEG…".

## Slide 7

**¿Qué entendemos por privacidad?**

La privacidad no consiste simplemente en ocultar información, sino en controlar su flujo. Según la definición académica, es "**la capacidad de asegurar que la información fluya de acuerdo con normas sociales y legales aceptadas**".

Esto implica decidir quién puede acceder, cuándo, y para qué fines. La privacidad es contextual: lo que consideramos privado depende del entorno, la cultura y la finalidad del uso de los datos.

En la era digital, el desafío radica en mantener este control cuando los datos son replicados, analizados o compartidos por sistemas automatizados.

**Visual (derecha):** imagen de un mapamundi digital punteado en azul con líneas de red y nodos brillantes; al centro un ícono de candado con check y el texto "DATA PRIVACY".

## Slide 8

**Tipos de Información Personal**

La Identificación de Información Personal (PII) se refiere a cualquier dato que pueda identificar directa o indirectamente a una persona. Existen dos tipos:

- **PII sensible**: incluye nombre completo, número de documento, datos financieros o médicos. Su exposición puede causar daño, discriminación o fraude.
- **PII no sensible**: datos como género, ocupación o código postal. Aunque no identifican por sí solos, pueden combinarse con otros y revelar identidades.

Por ejemplo, si sabemos que alguien tiene 37 años, vive en un distrito específico y trabaja en una empresa concreta, es posible identificarlo sin necesidad de su nombre.

**Visual (derecha):** infografía azul de Investopedia. Ilustración de una cabeza de perfil (mitad silueta, mitad rostro difuso) rodeada de tarjetas, documentos y un teléfono con firma. Texto: "Personally Identifiable Information (PII)", transcripción fonética `[ˈpərs-nə-lē ī-,den-tə-ˈfī-ə-bəl ,in-fər-ˈmā-shən]`, y la definición "Information that, when used alone or with other relevant data, can identify an individual."

## Slide 9

**Regulaciones de privacidad: el caso del GDPR**

El Reglamento General de Protección de Datos (GDPR) de la Unión Europea marcó un hito mundial en la protección de la información personal. Su propósito es garantizar que los datos sean tratados con respeto a los derechos de las personas. Sus principios fundamentales son:

1. Licitud, lealtad y transparencia: los datos solo deben recolectarse con un propósito legítimo.
2. Limitación de propósito: no se pueden usar para fines distintos a los declarados.
3. Minimización de datos: recolectar solo lo estrictamente necesario.
4. Exactitud y actualización.
5. Limitación del almacenamiento: eliminar datos cuando ya no son útiles.

El GDPR ha servido como modelo para leyes en América Latina, incluyendo la Ley de Protección de Datos Personales (Ley N° 29733) en Perú.

**Visual (derecha):** infografía sobre fondo azul marino con el título "GDPR" en blanco al centro. Cinco líneas punteadas salen del título hacia cinco íconos amarillos alineados abajo, cada uno con su etiqueta:
- persona con candado → "Data Protection Officer (DPO)"
- documento con check → "Compliance"
- reloj despertador con "GDPR" en la esfera → "25 May 2018"
- candado con una X → "Data Breaches"
- llave → "Personal Data"

## Slide 10

Separador de sección: **02.** entre corchetes, ícono de portapapeles, título **Técnicas Básicas de Anonimización**.

## Slide 11

**Técnicas: Supresión de Datos**

La supresión consiste en eliminar total o parcialmente los datos que pueden poner en riesgo la privacidad. Existen dos tipos principales:

- Supresión de atributos (Attribute Suppression): elimina columnas completas, como nombres o identificadores.
- Supresión de registros (Record Suppression): elimina filas que contienen valores sensibles o atípicos.

**Visual:** dos capturas de celdas de notebook (tema oscuro) lado a lado.

Izquierda — código y salida del dataset original:

```python
import pandas as pd

data = {
    'name': ['Ana Torres', 'Luis Pérez', 'María López',
             'Carlos Díaz', 'Lucía Rojas'],
    'age': [34, 45, 29, 52, 38],
    'salary': [52000, 63000, 48000, 80000, 59000],
    'performance': [88, 92, 75, 80, 90]
}

df = pd.DataFrame(data)
print("Dataset original:")
df
```

Salida `Dataset original:`

| | name | age | salary | performance |
|---|---|---|---|---|
| 0 | Ana Torres | 34 | 52000 | 88 |
| 1 | Luis Pérez | 45 | 63000 | 92 |
| 2 | María López | 29 | 48000 | 75 |
| 3 | Carlos Díaz | 52 | 80000 | 80 |
| 4 | Lucía Rojas | 38 | 59000 | 90 |

Derecha — supresión de atributo:

```python
# === Attribute suppression ===
# Eliminamos la columna 'name' por contener PII
# (información identificable)
df_suppressed = df.drop('name', axis='columns')

print("Dataset tras SUPRESIÓN DE ATRIBUTO:")
df_suppressed
```

Salida `Dataset tras SUPRESIÓN DE ATRIBUTO:`

| | age | salary | performance |
|---|---|---|---|
| 0 | 34 | 52000 | 88 |
| 1 | 45 | 63000 | 92 |
| 2 | 29 | 48000 | 75 |
| 3 | 52 | 80000 | 80 |
| 4 | 38 | 59000 | 90 |

## Slide 12

**Técnicas: Enmascaramiento de datos**

El enmascaramiento reemplaza los valores reales por símbolos o patrones, preservando el formato del dato. Por ejemplo, podemos transformar números de tarjetas o correos electrónicos sin alterar su estructura.

Esto mantiene la integridad del conjunto de datos para pruebas o entrenamiento de modelos, evitando exponer información sensible. El enmascaramiento es ampliamente usado en bancos, hospitales y compañías de software.

**Visual (derecha):** captura de notebook oscuro con dos celdas y sus salidas.

```python
import pandas as pd

# Dataset con números de tarjeta y correo
df = pd.DataFrame({
    'name': ['Ana Torres', 'Luis Pérez', 'María López'],
    'card_number': ['4532312788901234', '5239874412567890', '4916123456789012'],
    'email': ['ana.torres@gmail.com', 'luis.perez@gmail.com', 'maria.lopez@gmail.com']
})

print("Dataset original:")
df
```

Salida `Dataset original:`

| | name | card_number | email |
|---|---|---|---|
| 0 | Ana Torres | 4532312788901234 | ana.torres@gmail.com |
| 1 | Luis Pérez | 5239874412567890 | luis.perez@gmail.com |
| 2 | María López | 4916123456789012 | maria.lopez@gmail.com |

```python
# === Enmascaramiento total del número de tarjeta ===
df['card_number'] = '**** **** **** ****'

print("Dataset con tarjetas enmascaradas:")
df
```

Salida `Dataset con tarjetas enmascaradas:`

| | name | card_number | email |
|---|---|---|---|
| 0 | Ana Torres | \*\*\*\* \*\*\*\* \*\*\*\* \*\*\*\* | ana.torres@gmail.com |
| 1 | Luis Pérez | \*\*\*\* \*\*\*\* \*\*\*\* \*\*\*\* | luis.perez@gmail.com |
| 2 | María López | \*\*\*\* \*\*\*\* \*\*\*\* \*\*\*\* | maria.lopez@gmail.com |

## Slide 13

**Técnicas: Enmascaramiento parcial**

En algunos casos, es útil conservar parte de la información visible. Por ejemplo, mostrar solo las primeras letras del correo o los últimos dígitos de un número:

**Visual:** dos capturas de notebook lado a lado.

Izquierda:

```python
import pandas as pd

df = pd.DataFrame({
    'email': ['ana.torres@gmail.com', 'luis.perez@gmail.com', 'maria.lopez@gmail.com'],
    'card_number': ['4532312788901234', '5239874412567890', '4916123456789012']
})

print("Dataset original:")
df
```

Salida `Dataset original:`

| | email | card_number |
|---|---|---|
| 0 | ana.torres@gmail.com | 4532312788901234 |
| 1 | luis.perez@gmail.com | 5239874412567890 |
| 2 | maria.lopez@gmail.com | 4916123456789012 |

Derecha:

```python
# === Enmascaramiento parcial de correo electrónico ===
# Muestra solo la primera letra antes del @
df['email_masked'] = df['email'].apply(lambda s: s[0] + '****' + s[s.find('@'):])

# === Enmascaramiento parcial de tarjeta ===
# Conserva los últimos 4 dígitos
df['card_masked'] = df['card_number'].apply(lambda s: '**** **** **** ' + s[-4:])

print("Dataset con enmascaramiento parcial:")
df[['email_masked', 'card_masked']]
```

Salida `Dataset con enmascaramiento parcial:`

| | email_masked | card_masked |
|---|---|---|
| 0 | a\*\*\*\*@gmail.com | \*\*\*\* \*\*\*\* \*\*\*\* 1234 |
| 1 | l\*\*\*\*@gmail.com | \*\*\*\* \*\*\*\* \*\*\*\* 7890 |
| 2 | m\*\*\*\*@gmail.com | \*\*\*\* \*\*\*\* \*\*\*\* 9012 |

Al pie: "Así se logra un equilibrio entre anonimización y comprensión visual del dato."

## Slide 14

**Técnicas: Generación de datos sintéticos**

La librería Faker de Python permite generar información ficticia pero verosímil. Podemos crear nombres, direcciones, correos y números de tarjetas:

Los datos sintéticos son muy valiosos en etapas de desarrollo, simulaciones o pruebas donde se necesita un dataset realista sin exponer personas reales.

**Visual (derecha):** captura de notebook oscuro.

```python
from faker import Faker
import pandas as pd

fake = Faker('es_ES')

# Generamos un dataset sintético de clientes
data_fake = {
    'nombre': [fake.name() for _ in range(5)],
    'correo': [fake.email() for _ in range(5)],
    'tarjeta': [fake.credit_card_number() for _ in range(5)],
    'ciudad': [fake.city() for _ in range(5)]
}

df_fake = pd.DataFrame(data_fake)
print("🖊 Dataset sintético generado con Faker:")
df_fake
```

Salida `Dataset sintético generado con Faker:`

| | nombre | correo | tarjeta | ciudad |
|---|---|---|---|---|
| 0 | Débora Dueñas Romeu | zjuan@example.com | 30310947140445 | Navarra |
| 1 | René del Jover | silvestre44@example.net | 4684970353485 | Madrid |
| 2 | Jafet Edelmiro Poza Zorrilla | manunicolau@example.org | 30437019633179 | Melilla |
| 3 | Virginia Gomez Luna | gvazquez@example.com | 213174847674542 | Salamanca |
| 4 | Arturo de Garrido | lagusti@example.net | 3515971311098622 | Murcia |

## Slide 15

**Técnicas: Generalización de datos**

La generalización reemplaza valores específicos por categorías más amplias.
Por ejemplo:
- Edad: 34 → (30–40)
- Ocupación: "Bailarín" → "Artista"

Este método reduce el riesgo de reidentificación manteniendo la utilidad para análisis estadístico.

**Visual (derecha):** captura de notebook oscuro.

```python
import pandas as pd

# Dataset original
df = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'María', 'Carlos'],
    'edad': [23, 37, 52, 68],
    'ciudad': ['Lima', 'Cusco', 'Arequipa', 'Trujillo']
})

# Generalización de edad (en rangos)
df['edad_generalizada'] = pd.cut(df['edad'],
                                 bins=[0, 30, 50, 70],
                                 labels=['Joven', 'Adulto', 'Mayor'])

# Generalización de ciudad (en macrozonas)
zonas = {'Lima': 'Costa', 'Trujillo': 'Costa', 'Arequipa': 'Sierra',
         'Cusco': 'Sierra'}
df['zona'] = df['ciudad'].map(zonas)

# Eliminamos columnas originales
df = df.drop(columns=['edad', 'ciudad'])

df
```

Salida:

| | nombre | edad_generalizada | zona |
|---|---|---|---|
| 0 | Ana | Joven | Costa |
| 1 | Luis | Adulto | Sierra |
| 2 | María | Mayor | Sierra |
| 3 | Carlos | Mayor | Costa |

## Slide 16

**Privacidad vs. Utilidad**

Toda técnica de anonimización implica una pérdida de información.

El reto consiste en encontrar un punto de equilibrio: proteger la identidad sin sacrificar la capacidad analítica. Un dataset completamente anónimo puede ser inútil; uno demasiado detallado puede ser peligroso. La clave está en la minimización proporcional: solo anonimizar lo necesario para cumplir el objetivo.

**Visual (derecha):** ilustración sobre fondo amarillo de una balanza (tabla de madera sobre un pivote triangular) con un candado azul en un extremo y una moneda dorada con símbolo "$" en el otro — metáfora del trade-off privacidad vs. valor.

## Slide 17

Separador de sección: **03.** entre corchetes, ícono de portapapeles, título **Modelos de Privacidad**.

## Slide 18

**Introducción**

- Cuando se trata de anonimización de datos, una de las técnicas más utilizadas es K-Anonymity. Este enfoque garantiza que las identidades de las personas no puedan determinarse fácilmente a partir de los datos publicados, protegiendo así su privacidad. K-Anonimato es un concepto poderoso que ha ganado mucha atención en los últimos años debido a las crecientes preocupaciones sobre las violaciones de datos y el acceso no autorizado a información personal.

Slide solo de texto.

## Slide 19

**Definición del K-Anonimato**

- K-Anonimato se refiere a una propiedad que garantiza la privacidad de las personas en un conjunto de datos. Garantiza que cualquier información divulgada no pueda vincularse a un individuo específico con un alto grado de confianza. En otras palabras, cuando los datos son K-Anonimizados, se vuelven indistinguibles de al menos K-1 otros individuos en el conjunto de datos. Esto hace que sea increíblemente difícil para un atacante identificar la información confidencial de una persona específica a partir de los datos anonimizados.

Slide solo de texto.

## Slide 20

**Requisitos para lograr el anonimato K**

Para lograr K-Anonimato, se deben cumplir ciertos requisitos:

a) **Generalización**: la generalización implica reemplazar valores específicos en el conjunto de datos con valores más generales o menos precisos. Por ejemplo, en lugar de almacenar la edad exacta de un individuo, se puede generalizar en rangos de edad como 20-30, 30-40, etc. Este proceso ayuda a proteger las identidades de las personas al dificultar la vinculación de registros específicos con ellas.

b) **Supresión**: la supresión implica eliminar u omitir ciertos atributos del conjunto de datos por completo. Esto garantiza que no se divulgue información confidencial, como números de seguro social o direcciones. Sin embargo, suprimir demasiados atributos podría provocar una pérdida de utilidad de los datos, haciéndolos menos útiles para el análisis.

c) **Perturbación**: la perturbación implica agregar ruido o valores aleatorios al conjunto de datos. Al introducir ligeras modificaciones en los datos, resulta más difícil identificar individuos específicos. Sin embargo, es crucial lograr el equilibrio adecuado entre privacidad y precisión de los datos, ya que una perturbación excesiva puede hacer que los datos sean inútiles para el análisis.

## Slide 21

**Ejemplo**

Slide con tres capturas de notebook en fila (izquierda → derecha) que muestran el pipeline completo de k-anonimato.

**Bloque 1 — dataset original:**

```python
import pandas as pd

# Dataset original
df = pd.DataFrame({
    'edad': [23, 24, 24, 35, 36, 37, 52, 52],
    'ciudad': ['Lima', 'Lima', 'Lima', 'Cusco', 'Cusco',
               'Cusco', 'Arequipa', 'Arequipa'],
    'diagnóstico': ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'B']
})

print("Dataset original:")
df
```

Salida `Dataset original:`

| | edad | ciudad | diagnóstico |
|---|---|---|---|
| 0 | 23 | Lima | A |
| 1 | 24 | Lima | B |
| 2 | 24 | Lima | A |
| 3 | 35 | Cusco | A |
| 4 | 36 | Cusco | B |
| 5 | 37 | Cusco | B |
| 6 | 52 | Arequipa | A |
| 7 | 52 | Arequipa | B |

**Bloque 2 — generalización y conteo de frecuencias:**

```python
# === Paso 1: Generalización de edad (en rangos de 10 años)
df['edad_grupo'] = pd.cut(df['edad'], bins=[20, 30, 40, 60],
                          labels=['20-29', '30-39', '40-59'])

# === Paso 2: Verificamos frecuencia de combinaciones
freq = df.groupby(['edad_grupo', 'ciudad'],
                  observed=True).size().reset_index(name='count')

print("Frecuencia por grupo (antes de asegurar K-anonimato):")
freq
```

Salida `Frecuencia por grupo (antes de asegurar K-anonimato):`

| | edad_grupo | ciudad | count |
|---|---|---|---|
| 0 | 20–29 | Lima | 3 |
| 1 | 30–39 | Cusco | 3 |
| 2 | 40–59 | Arequipa | 2 |

**Bloque 3 — filtrado a K=2:**

```python
# === Paso 3: Aseguramos K=2 (cada grupo debe tener al menos 2 registros)
k = 2
anon_groups = freq[freq['count'] >= k]
df_k_anon = df.merge(anon_groups[['edad_grupo', 'ciudad']],
                     on=['edad_grupo', 'ciudad'], how='inner')

print("Dataset que cumple K-Anonimato (K=2):")
df_k_anon[['edad_grupo', 'ciudad', 'diagnóstico']]
```

Salida `Dataset que cumple K-Anonimato (K=2):`

| | edad_grupo | ciudad | diagnóstico |
|---|---|---|---|
| 0 | 20–29 | Lima | A |
| 1 | 20–29 | Lima | B |
| 2 | 20–29 | Lima | A |
| 3 | 30–39 | Cusco | A |
| 4 | 30–39 | Cusco | B |
| 5 | 30–39 | Cusco | B |
| 6 | 40–59 | Arequipa | A |
| 7 | 40–59 | Arequipa | B |

## Slide 22

**Limitaciones del anonimato K**

Aunque efectivo, el k-anonimato tiene limitaciones.

No protege contra ataques de homogeneidad (cuando todos los miembros de un grupo tienen el mismo valor sensible) ni de background knowledge (cuando un atacante posee información externa).

Por ello, se complementa con modelos más sofisticados como l-diversity y t-closeness.

Slide solo de texto.

## Slide 23

**Privacidad diferencial**

La privacidad diferencial (DP) es un enfoque matemático que introduce ruido aleatorio en los resultados, de modo que la inclusión o exclusión de un individuo no afecte significativamente el resultado global.

Así se garantiza que ninguna persona pueda ser identificada ni siquiera de forma probabilística.

**Visual (derecha):** infografía titulada "Privacidad Diferencial — ¿Adivina quién?". Muestra dos rejillas de avatares caricaturescos etiquetados con nombres (Alex, Alfred, Anita, Anne, Bernard, Bill, Charles, Claire, David, Eric, Frank, George, Herman, Joe, Maria, Max, Paul, Peter, Philip, Richard, Robert, Sam, Susan, Tom):
- Rejilla izquierda = conjunto **D** (completo).
- Rejilla derecha = conjunto **D′**, idéntico salvo que un avatar (Herman) fue reemplazado por un rectángulo azul sólido (individuo removido).

Desde cada rejilla sale una flecha curva hacia el centro: la roja rotulada $M(D)$ y la azul rotulada $M(D')$, convergiendo en un símbolo grande **≈**. Es decir, la salida del mecanismo es aproximadamente igual con o sin ese individuo:

$$M(D) \approx M(D')$$

## Slide 24

**Privacidad diferencial**

La privacidad diferencial es un conjunto de sistemas y prácticas que ayudan a mantener la seguridad y la privacidad de los datos personales. En las soluciones de aprendizaje automático, la privacidad diferencial puede ser un requisito para el cumplimiento normativo.

**Visual (derecha):** diagrama de arquitectura (estilo Microsoft) con 7 pasos numerados. Elementos: **User** (ícono de personas con lupa) a la izquierda, un **Privacy Module** (caja gris al centro), un **Budget Store** (caja con ábaco + documento "Budget") a la derecha, y un **Private Dataset** (cilindro de base de datos) al extremo derecho. Dos líneas punteadas naranjas marcan el borde de confianza.

Flujo:
1. El User "Submits a query" → entra al Privacy Module.
2. El módulo ("Dataset checks budget and access credentials") → "Checks budget and private compute" contra el Budget Store.
3. Budget Store → flecha hacia el Private Dataset.
4. "Credentials to access the data" → del Budget Store/módulo al Private Dataset.
5. "Private data" regresa al Privacy Module.
6. "Mechanism adds noise" (dentro del módulo) → genera el **Report**.
7. El User "Gets back a run that has a differentially private report".

## Slide 25

**Métricas de privacidad diferencial**

La privacidad diferencial busca proteger contra la posibilidad de que un usuario genere un número indefinido de informes que, eventualmente, revelen datos confidenciales. Un valor denominado épsilon ($\varepsilon$) mide el nivel de ruido (o privacidad) de un informe. Épsilon tiene una relación inversa con el ruido o la privacidad: cuanto menor sea el valor de épsilon, más ruido (y privacidad) tendrán los datos.

Los valores de épsilon son no negativos ($\varepsilon \ge 0$). Los valores inferiores a 1 proporcionan negación plausible completa. Cualquier valor superior a 1 implica un mayor riesgo de exposición de los datos reales. Al implementar soluciones de aprendizaje automático con privacidad diferencial, se recomienda utilizar datos con valores de épsilon entre 0 y 1 ($0 \le \varepsilon \le 1$).

Otro valor directamente correlacionado con épsilon es delta ($\delta$). Delta mide la probabilidad de que un informe no sea completamente privado. Cuanto mayor sea delta, mayor será épsilon. Debido a esta correlación, épsilon se utiliza con mayor frecuencia.

Slide solo de texto.

## Slide 26

**Conclusiones**

Tres bloques numerados en cian, cada texto dentro de corchetes:

**01.** La privacidad de datos es un componente esencial de la confianza digital, y debe abordarse desde una perspectiva ética, legal y técnica en toda organización que gestione información personal.

**02.** Las técnicas de anonimización permiten proteger la identidad sin perder valor analítico, siempre que se logre un balance adecuado entre precisión y confidencialidad.

**03.** Modelos como el k-anonimato y la privacidad diferencial ofrecen marcos cuantitativos para garantizar que los datos publicados o analizados no puedan vincularse a individuos específicos, fortaleciendo la seguridad informacional.

## Slide 27

Slide de cierre: solo el logo UTEC sobre fondo cian (decorativa). Sin contenido.
