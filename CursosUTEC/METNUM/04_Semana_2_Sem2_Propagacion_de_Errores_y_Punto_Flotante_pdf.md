---
curso: METNUM
titulo: 04 - Semana 2/Sem2_Propagación de Errores y Punto Flotante
slides: 28
fuente: 04 - Semana 2/Sem2_Propagación de Errores y Punto Flotante.pdf
---

Métodos Numéricos
Propagación de Errores y
Punto Flotante - S2
Hermes Yesser Pantoja Carhuavilca
(hpantoja@utec.edu.pe)
Jimmy Mendoza Montalvo
(jmendozam@utec.edu.pe)
Rósulo Pérez Cupe
(rperezc@utec.edu.pe)
Julio Cesar Barraza Bernaola
(jbarraza@utec.edu.pe)
Marco Antonio Cuyubamba Espinoza
(mcuyubamba@utec.edu.pe)
Ronaldo Walter Laureano Huayanay
(rlaureano@utec.edu.pe)


                                    Profesores: Utec-Ciencias
        Objetivos
    Al finalizar esta sesión, el estudiante será capaz de:
            Explicar cómo se propagan los errores numéricos en procesos iterativos.
            Representar números reales en formato IEEE 754 en precisión simple y doble.




Universidad de Ingeniería y Tecnología            Métodos Numéricos                   1 / 27
                                                 Índice
                                         1 Propagación de Errores
                                         2 Representación    IEEE
                                           754




Universidad de Ingeniería y Tecnología   Métodos Numéricos          2 / 27
1   PROPAGACIÓN DE
    ERRORES
Propagación de errores
  El Problema de la Incertidumbre Acumulada
 En ingeniería, muchas veces calculamos resultados a partir de mediciones que
 ya contienen error. A medida que realizamos cálculos sucesivos, estos errores se
 acumulan, afectando el resultado final.

                                 Medición 1   entrada con error

                                  x1 ± δx1
                                                                  Proceso de Cálculo


                                 Medición 2
                                                                    Cálculo / Función                                  Resultado


                 Error Inicial
                                  x2 ± δx2




                                                                                                    Error Propagado
                                                                    y = f (x1 , x2 , . . . , xn )                        y ± δy

                                     ..
                                      .
                                                                                                                      Incertidumbre
                                                                                                                      Acumulada δy
                                 Medición N
                                  xn ± δxn


Universidad de Ingeniería y Tecnología                                              Métodos Numéricos                                 4 / 27
Operaciones Básicas
Sumas y Diferencias
Sean dos magnitudes medidas: x = x̃ ± ξx e y = ỹ ± ξy . Para la función q = x ± y ,
¿cuál es el error absoluto ξq ?

 Propiedad Aditiva del Error Absoluto
 El error absoluto de la suma o diferencia de dos o más magnitudes es, en el peor
 de los casos, aproximadamente igual a la suma de los errores absolutos de
 dichas magnitudes:
                             q = x ± y ⇒ ξq ≈ ξx + ξy




Universidad de Ingeniería y Tecnología      Métodos Numéricos                   5 / 27
Ejemplo 1: Corte de Tuberías Industriales
                                                 Situación: Tubería matriz de Ltotal . Se corta una
                                                 pieza de Lcorte . Estimar la longitud restante (Lrest ) y
                                Corte            su error.

                                                      Ltotal = 150.0 ± 0.5 cm
                                                      Lcorte = 112.0 ± 0.2 cm
             Ltotal = 150.0 ± 0.5 cm
                                                 Solución: La longitud restante es una diferencia:
                                         Lrest   Lrest = Ltotal − Lcorte . Por propiedad aditiva de
                                          ?
                                                 errores: ξrest ≈ ξtotal + ξcorte .
        Lcorte = 112.0 ± 0.2 cm                  Evaluando los valores:
                                                      Lrest = 150.0 − 112.0 = 38.0 cm
                                                      ξrest ≈ 0.5 + 0.2 = 0.7 cm
                                                        Lrest = 38.0 ± 0.7 cm

Universidad de Ingeniería y Tecnología                      Métodos Numéricos                          6 / 27
Ejercicio: masa total del líquido en dos matraces
                                                   En un experimento se traslada líquido entre dos matraces y se desea
                                                   hallar la masa total del líquido y estimar su error.
                                                   Se conocen:

                                                              M1 = masa del matraz 1 + contenido = 540 ± 10 g,
                  M1                          M2              m1 = masa del matraz 1 vacío = 72 ± 1 g,

                                                              M2 = masa del matraz 2 + contenido = 940 ± 20 g,
          m1                             m2
                                                              m2 = masa del matraz 2 vacío = 97 ± 1 g.

                                                   Se pide:
           L1                            L2
                                                        Halle la masa total de líquido.
                                                        Estime el error absoluto correspondiente.


                                                    Respuesta:
                                                                             Ltotal = 1311 ± 32 g




Universidad de Ingeniería y Tecnología                               Métodos Numéricos                            7 / 27
Propagación en Funciones de 1 Variable
Sea q = f (x) con medida x̃ y error ∆x̃.
Serie de Taylor (1er orden):

           f (x) ≈ f (x̃) + f ′ (x̃)(x − x̃)
                                                          f (x)
Despreciando términos de orden
superior, el error absoluto estimado es:         f (x)
                                                                                           ≈ ∆f
              ∆f (x̃) ≈ |f ′ (x̃)||x − x̃|                f (x̃)
                                                                                  ∆x
 Fórmula de Propagación
                 ∆f (x̃) ≈ |f ′ (x̃)| ∆x̃
                                                                             x̃        x
El error se amplifica según la pendiente de la                                    x
función.

Universidad de Ingeniería y Tecnología                   Métodos Numéricos                        8 / 27
Ejemplo 2: Estimación de Energía Cinética
  Ejemplo
 Se ha medido la velocidad de un dron de 2 kg resultando en v = 15.0 ± 0.4
 m/s. Considerando la masa como un valor exacto, estime el valor de la Energía
 Cinética (Ek = 12 mv 2 ) y su error propagado.

Solución:
    Valor base: Evaluamos Ek (v ) = 21 (2)v 2 = v 2 ⇒ Ek (15.0) = 225 J.
    Derivada: dE
               dv = 2v .
                 k

    Propagación: Aplicamos la fórmula de primer orden:
                                   dEk
                     ∆Ek ≈                    · ∆v = |2(15.0)| · (0.4) = 30 · 0.4 = 12 J
                                   dv v =15.0
Este error de 12 Joules también se puede expresar como error relativo (er ) y relativo
porcentual (ep ):
                           ∆Ek     12
                     er =      =      ≈ 0.0533 ⇒ ep = 5.33%
                            Ek    225
Universidad de Ingeniería y Tecnología                   Métodos Numéricos                 9 / 27
Ejercicio: propagación de error en una función
Se tiene una aproximación x̃ = 2.5 con un error absoluto ∆x̃ = 0.01.
Considere la función:
                                                   f (x) = x 3 .
Se pide:
       Estimar el error en f (x) utilizando aproximación diferencial.
       Expresar el resultado como f (x̃) ± ∆f .
       Determinar el intervalo donde se encuentra el valor verdadero.


  Respuesta:
                                    ∆f ≈ 0.1875,   f (2.5) = 15.625 ± 0.1875
                                         ⇒   f (2.5) ∈ [15.4375, 15.8125]


Universidad de Ingeniería y Tecnología                      Métodos Numéricos   10 / 27
Propagación en Funciones Multivariables
El enfoque anterior se generaliza usando derivadas parciales para funciones
q = f (x1 , x2 , . . . , xn ).

Aproximación por Serie de Taylor de varias variables:

                                                 ∂f                            ∂f
               f (x1 , x2 ) ≈ f (x̃1 , x̃2 ) +                   (x1 − x̃1 ) +                 (x2 − x̃2 )
                                                 ∂x1 (x̃1 ,x̃2 )               ∂x2 (x̃1 ,x̃2 )

Para el caso del peor escenario (donde los errores no se cancelan entre sí),
tomamos los valores absolutos:

  Fórmula General de Propagación (Suma de Errores Máximos)

                                                    ∂f                     ∂f
                        ξq = ∆f (x̃1 , x̃2 ) ≈                      ∆x̃1 +                 ∆x̃2
                                                    ∂x1 (x̃1 ,x̃2 )        ∂x2 (x̃1 ,x̃2 )

Universidad de Ingeniería y Tecnología                           Métodos Numéricos                           11 / 27
Ejemplo 3: Volumen de un Tanque Cilíndrico
                                         Paso 1: Valor Nominal

                                              V = π(2.50)2 (5.00) ≈ 98.174 m3

  Ejemplo                                Paso 2: Derivadas Parciales

 Estime el volumen V = πr 2 h de         ∂V             ∂V
                                            = 2πrh ;        = πr 2
 un tanque industrial y su error         ∂r             ∂h
 absoluto dados:                 Paso 3: Propagación del Error
     Radio r = 2.50 ± 0.02
     r = 2.50 ± 0.8%             ∆V ≈ |2πrh| ∆r + πr 2 ∆h
        Altura h = 5.00 ± 0.05 m         ∆V ≈ |2π(2.50)(5.00)|(0.02) + |π(2.50)2 |(0.05)
                                         ∆V ≈ (78.54)(0.02) + (19.63)(0.05)
                                         ∆V ≈ 1.571 + 0.982 = 2.553 m3

Universidad de Ingeniería y Tecnología            Métodos Numéricos                 12 / 27
Ejercicio: propagación de error en la deflexión de
un mástil
La deflexión y de la punta de un mástil en un bote de vela está dada
por:
                                  FL4                                Se pide:
                              y=
                                  8EI
                                                                           Estimar ∆y .
donde:                                                                     Expresar y ± ∆y .
       F : carga lateral uniforme (N/m),                                  Hallar el intervalo.
       L: altura (m),
       E: módulo de elasticidad (N/m2 ),
                                                                     Solución:
       I: momento de inercia (m4 ).
                                                                                    ∆y ≈ 0.011482
Se tienen los siguientes datos:
                                                                                y ≈ 0.164025 ± 0.011482
                    F̃ = 750             ∆F̃ = 30
                                                                               y ∈ [0.152543, 0.175507] m
                    L̃ = 9               ∆L̃ = 0.03
                    Ẽ = 7.5 × 109       ∆Ẽ = 5 × 107
                    Ĩ = 0.0005          ∆Ĩ = 0.000005



Universidad de Ingeniería y Tecnología                     Métodos Numéricos                                13 / 27
Propagación del error en producto
Si tenemos dos magnitudes:
     x = x̃ ± ξx .
     y = ỹ ± ξy .
Sea q = xy , ¿podremos estimar ξq ?
Definimos la función q = g(x, y ) = xy y usando la serie de Taylor:
                                                         ∂g       ∂g
                                         ∆g(x̃, ỹ ) ≈      ∆x̃ +    ∆ỹ
                                                         ∂x       ∂y
Entonces ∂g      ∂g
         ∂x = y, ∂y = x de modo que

                                           ∆g(x̃, ỹ ) ≈ |ỹ | ∆x̃ + |x̃| ∆ỹ
El error relativo del producto es aproximadamente la suma de errores relativos:
                                              ∆g(x̃, ỹ )   ∆x̃    ∆ỹ
                                                          ≈      +
                                               |x̃ ỹ |     |x̃|   |ỹ |
Universidad de Ingeniería y Tecnología                         Métodos Numéricos   14 / 27
2   REPRESENTACIÓN
    IEEE 754
Sistemas de Punto Flotante
Un sistema de punto flotante se define formalmente mediante cuatro parámetros o
elementos F (β, p, L, U):
       β: Base del sistema (ej. 2 para binario, 10 para decimal).
       p: Precisión (número de dígitos de la parte fraccionaria de la mantisa).
       L: Límite inferior del exponente.
       U: Límite superior del exponente.




Universidad de Ingeniería y Tecnología        Métodos Numéricos                   16 / 27
Aritmética de Punto Flotante y el Estándar
IEEE-754
  El Límite del Hardware
 Trabajamos con memoria finita. La notación de punto flotante reconoce este límite,
 ofreciendo un rango amplio sin requerir precisión infinita.

Todo número real x ̸= 0 en binario normalizado se escribe:

                                         x = ± (1.d1 d2 . . . dp )2 × 2E

El Caso Ariane 5 (1996)
Un error de conversión de punto flotante de
64-bits a entero de 16-bits provocó un                     Normativa IEEE 754
desbordamiento. El cohete se desintegró 40s                Define cómo los procesadores modernos alma-
después del despegue.                                      cenan números para estandarizar la precisión
                                                           y prevenir anomalías matemáticas.

Universidad de Ingeniería y Tecnología                     Métodos Numéricos                       17 / 27
Estructura IEEE-754 (Visualización en Bits)
Precisión Simple (Float - 32 bits)

             S Exponente (8 bits)               Mantisa Fraccionaria (23 bits)

                       Bits 23 al 30                     Bits 0 al 22 (23 bits)
           Bit 31         (8 bits)



Precisión Doble (Double - 64 bits)

             S Exp (11 bits)                Mantisa Fraccionaria (52 bits)

                 Bits 52 al 62                       Bits 0 al 51 (52 bits)
           Bit 63 (11 bits)


S = Bit de Signo (0 = Positivo, 1 = Negativo). El "1." previo a la mantisa es implícito.


Universidad de Ingeniería y Tecnología                  Métodos Numéricos                  18 / 27
IEEE-754
La representación de punto flotante de Precisión Simple




Universidad de Ingeniería y Tecnología    Métodos Numéricos   19 / 27

Formato IEEE 754 en Precisión Simple (32 bits)
       Cálculo del Sesgo (Bias):
       Para evitar almacenar signos en el exponente, se suma un sesgo.

                             bias = 2k −1 − 1        ⇒     Para 8 bits: 28−1 − 1 = 127

       Relación de Exponentes:

                                                    Eext = Eint − 127

       Donde:
       Eext : Exponente externo (el valor real matemático).
       Eint : Exponente interno (almacenado en la cadena de bits según IEEE 754).
       Fórmula General (Números Normalizados):

                                         x = (−1)bs × 2(Eint −127) × (1.Mantisa)2

Universidad de Ingeniería y Tecnología                       Métodos Numéricos           20 / 27
Excepciones de la Normativa IEEE 754
No todos los arreglos de bits siguen la fórmula normalizada. Existen
configuraciones reservadas para casos matemáticos especiales:


 Casos Especiales
        Cero Exacto: Eint = 0, Mantisa = 0. (Puede ser +0 o −0).
        Números Subnormales: Eint = 0, Mantisa ̸= 0. Se usan para representar
        números extremadamente cercanos a cero (No asumen el 1 implícito).
        Infinito (±∞): Eint = 255, Mantisa = 0. Resultan de divisiones entre cero,
        por ejemplo.
        NaN (Not a Number): Eint =√255, Mantisa ̸= 0. Resultan de operaciones
        indeterminadas como 0/0 o −1.


Universidad de Ingeniería y Tecnología       Métodos Numéricos                  21 / 27
Ejemplo 2
 Ejemplo
 Representa −3.75 en representación de precisión simple.

Solución:
Normalizamos de acuerdo a las normas de la IEEE 754.
    −3.75 = −11.112 = −1.111 × 21
    Bias = 127, por lo que 127 + 1 = 128 (es el exponente actual).
    El primer 1 en la mantisa es implícito, por lo que tenemos:
     1 10000000 11100000000000000000000
    Desde que tenemos implícito 1 en el significando, esto es igual a :
    −1.1112 × 2(128−127) = −1.1112 × 21 = −11.112 = −3.75




Universidad de Ingeniería y Tecnología     Métodos Numéricos              22 / 27
Ejemplo IEEE: De Decimal a Binario
 Ejercicio Práctico
 Representa −13.4 en representación IEEE 754 de precisión simple.
 (Ejemplo de conversión con parte fraccionaria periódica mixta)

1. Binario: 13 = 11012 . Para la parte fraccionaria 0.4, multiplicamos por 2
iterativamente y obtenemos el periodo 0110.
⇒ −13.410 = −1101.011001100110 . . .2
2. Normalización Científica: −1.10101100110011001100110 . . .2 × 23
3. Componentes:
     Signo: Negativo → bs = 1
     Exponente: Eint = 3 + 127 = 13010 = 100000102
     Mantisa (23 bits): f = 10101100110011001100110
                                  1      10000010   10101100110011001100110

Universidad de Ingeniería y Tecnología                    Métodos Numéricos    23 / 27
Ejemplo IEEE: De Binario a Decimal
Ejercicio: Identifique el valor base 10 de la siguiente cadena de 32 bits:

                                  0      10000100   01100000000000000000000

1. Componentes: Signo positivo (bs = 0), Exponente interno 100001002 = 13210 ,
Mantisa fraccionaria f = 0112 .
2. Aplicar la fórmula IEEE 754:

                                      Valor = (−1)0 × (1.011)2 × 2(132−127)
                                             = (+1) × (1.375)10 × 25
                                             = 1.375 × 32 = 44.010

Comprobación directa: 1.0112 × 25 = 1011002 = 32 + 8 + 4 = 4410 .



Universidad de Ingeniería y Tecnología                     Métodos Numéricos   24 / 27
El Épsilon de Máquina (ϵ)
  Resolución del Sistema Computacional
 El Épsilon de máquina (ϵ) se define como el número positivo más pequeño
 representable tal que:

                               1+ϵ >1    (en la aritmética del computador)


Representa la distancia entre el número 1.0 y el siguiente número de punto flotante
que la máquina puede distinguir.
       Para Precisión Simple (23 bits de mantisa): ϵ = 2−23 ≈ 1.19 × 10−7
       Para Precisión Doble (52 bits de mantisa): ϵ = 2−52 ≈ 2.22 × 10−16
Importancia Industrial: Define el límite absoluto del error de redondeo relativo. Si
la tolerancia requerida por un algoritmo iterativo es menor al épsilon, este entrará
en un bucle infinito.
Universidad de Ingeniería y Tecnología                Métodos Numéricos         25 / 27
Conclusiones
       La serie de Taylor (primer orden) es la herramienta fundamental analítica para
       predecir cómo se propaga la incertidumbre de una medición física hacia el
       diseño final.
       La memoria de la computadora es finita. El estándar IEEE 754 sacrifica
       precisión absoluta en los últimos decimales a favor de un rango dinámico
       extremo (10−38 a 1038 en precisión simple).
       Entender el Épsilon de Máquina previene errores críticos en métodos
       numéricos que requieren validaciones de tolerancia.




Universidad de Ingeniería y Tecnología        Métodos Numéricos                   26 / 27
Bibliografía
      Steven C. Chapra y Raymond P. Canale.
      Métodos numéricos para ingenieros, 7a ed. McGraw-Hill, 2015.
      Richard L. Burden y J. Douglas Faires.
      Análisis numérico, 7a ed. Thompson, 2002.




Universidad de Ingeniería y Tecnología     Métodos Numéricos         27 / 27

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
