---
curso: FINEMP
titulo: 13 - Semana 11/FE Semana 11 - Tasas de interés 2__pptx
slides: 24
fuente: 13 - Semana 11/FE Semana 11 - Tasas de interés 2__pptx.pdf
---

Valor del dinero en el tiempo – Parte 2
        Finanzas Empresariales - Semana 11
                           • Dominar la conversión entre tasas
                             nominales y efectivas, incluyendo el




Objetivo(s) de la sesión
                             cálculo de tasas equivalentes para
                             diferentes períodos de capitalización,
                             aplicable a productos financieros y
                             decisiones de inversión.

                           • Analizar el impacto financiero de la
                             tasa moratoria, comprendiendo su
                             cálculo y aplicación en casos de mora,
                             así como su efecto en deudas y
                             obligaciones incumplidas.




                                                                      2
Contenido
1. Tasa de interés efectiva.

2. Tasa de interés moratoria.

3. Casos de aplicación.




                                3
1.
     Tasa de interés efectiva




                                4
    Tasa de interés efectiva anual ( i )

•                               Se suele expresar en términos anual recibiendo
                                el nombre de Tasa Efectiva Anual o TEA.


                                La tasa de interés efectiva se emplea en:
                                • Préstamos concedidos por los bancos a
                                  empresas.
                                • Compras de bienes de consumo a plazos.
                                • Créditos hipotecarios.
                                • Créditos vehiculares.
                                • Préstamos de consumo.




                                                                                 5
                Tasas de interés nominal ( r ) y Tasa de interés efectiva ( i )

El Banco CIMA ofrece una tasa de 10% nominal anual con capitalización semestral ¿Cuál es la tasa
efectiva anual correspondiente?
   r            = 10%                                           i   = (1+ r/m)m - 1
   m            = 2 (dos capitalizaciones al año)               i   = (1+ 5%)2 - 1
   im           = r/m                                           i   = 10.25%
   im           = 10%/2
   isemestral   = 5%
                         10% nominal                                10.25% efectivo


                0                1                2         0             1           2

                    5% nominal       5% nominal


                0                1                2

                                                                                                   6
             Tasas de interés nominal ( r ) y TEA ( i )


 Tasa                    Unidad de     Período de Tasa Efectiva del período
        Capitalización                                                               Tasa Efectiva Anual (TEA)
Nominal                capitalización capitalización      de capitalización
  24%      Mensual          1        12 / 1 = 12       24% / 12 = 2%            ( 1 + 24% / 12 ) 12 - 1 = 26.82%

  24%     Bimestral         2         12 / 2 = 6        24% / 6 = 4%              ( 1 + 24% / 6 ) 6 - 1 = 26.53%

  24%     Trimestral        3         12 / 3 = 4        24% / 4 = 6%              ( 1 + 24% / 4 ) 4 - 1 = 26.25%

  24%     Semestral         6         12 / 6 = 2       24% / 2 = 12%              ( 1 + 24% / 2 ) 2 - 1 = 25.44%

  24%       Diario          1       365 / 1 = 365    24% / 365 = 0.07%        ( 1 + 24% / 365 ) 365 - 1 = 27.11%

  24%      Semanal          7        365 / 7 = 52     24% / 52 = 0.46%          ( 1 + 24% / 52 ) 52 - 1 = 27.05%


                                                                                                                   7
            Funciones en Microsoft Excel

Convertir tasa de interés efectiva en tasa de interés nominal
=TASA.NOMINAL(tasa_efect, núm_per_año)



Convertir tasa de interés nominal en tasa de interés efectiva
=INT.EFECTIVO(tasa_nominal, núm_per_año)



              Para tener en cuenta durante el curso:
              • Si trabajan con Excel online NUNCA utilicen la función DIVIDIR ya que no es
                reconocida por las versiones de Excel de escritorio.
              • Pueden reemplazar esta función por una fórmula que contenga el operador “/”.


                                                                                               8
                 Funciones en Microsoft Excel

 Tasa                                                  Tasa de interés efectiva a             Tasa de interés nominal a
                Tasa Efectiva Anual (TEA)
Nominal                                                 Tasa de interés nominal                Tasa de interés efectiva

 24%       ( 1 + 24% / 12 ) 12 - 1 = 26.82% =TASA.NOMINAL (26.82% ; 12) = 24%       =INT.EFECTIVO (24% ; 12) = 26.82%

 24%         ( 1 + 24% / 6 ) 6 - 1 = 26.53% =TASA.NOMINAL (26.53% ; 6) = 24%        =INT.EFECTIVO (24% ; 6) = 26.53%

 24%         ( 1 + 24% / 4 ) 4 - 1 = 26.25% =TASA.NOMINAL (26.25% ; 4) = 24%        =INT.EFECTIVO (24% ; 4) = 26.25%

 24%         ( 1 + 24% / 2 ) 2 - 1 = 25.44% =TASA.NOMINAL (25.44% ; 2) = 24%        =INT.EFECTIVO (24% ; 2) = 25.44%

 24%      ( 1 + 24% / 365 ) 365 - 1 = 27.11% =TASA.NOMINAL (27.11% ; 365) = 24%     =INT.EFECTIVO (24% ; 365) = 27.11%

 24%       ( 1 + 24% / 52 ) 52 - 1 = 27.05% =TASA.NOMINAL (27.05% ; 52) = 24%       =INT.EFECTIVO (24% ; 52) = 27.05%


                                                                                                                   9
            Conversión entre tasas efectivas

• Proceso de transformar una tasa de interés efectiva en otra tasa equivalente, pero en un período
  de tiempo diferente.

• Permite estandarizar las tasas de interés a un mismo periodo de tiempo para facilitar la
  comparación entre diferentes ofertas financieras o para realizar cálculos financieros más
  precisos.

Fórmula



Donde:
n1 número de días del período de la Tasa Efectiva 1 (lo que quiero calcular).
n2 número de días del período de la Tasa Efectiva 2 (dato ya dado).



                                                                                                     10
           Ejercicio 1.1

Convertir las siguientes tasas efectivas:
1. 12% efectiva anual a efectiva trimestral.      2.87 %
2. 2% efectiva bimestral a efectiva anual.         12.62
                                                       %
3. 0.1% efectiva diaria a efectiva mensual.
                                                  3.04 %
4. 15% efectiva mensual a efectiva diaria.
                                                  0.47 %
5. 0.8% efectiva quincenal a efectiva
   semestral.                                      10.03
                                                       %
6. 6% efectiva trimestral a efectiva quincenal.
                                                  0.98 %
7. 0.85% efectiva semanal a efectiva
   bimestral.                                     7.52 %
8. 24% efectiva semestral a efectiva semanal.     0.84 %


                                                           11
           Ejercicio 1.2

1. Convierta la Tasa Efectiva Anual (TEA) de 50% a una Tasa Efectiva Mensual (TEM).       3.44%



2. Convierta la Tasa Efectiva Bimestral (TEB) de 7.9% a una Tasa Efectiva Trimestral (TET). 12.08%



3. ¿Cuál es la tasa efectiva semestral (TES) para un depósito de ahorro que gana una tasa nominal
   anual 24% capitalizable mensualmente?                                                   12.62%




                                                                                                     12
2.
     Tasa de interés moratoria




                                 13
           Interés moratorio

• Es un recargo que se aplica cuando el deudor    Fórmula
  incumple con el plazo de pago.

• Representa una penalidad por la demora, no
  una rentabilidad pactada.

• Protege al acreedor frente al incumplimiento    Donde:
  del contrato.
                                                  • Im      Interés moratorio.
• Su tasa suele ser mayor que la compensatoria,   • Mv      Monto vencido.
  y puede estar regulada por ley o contrato.      • rm      Tasa de interés moratoria.
                                                  • n       Días de mora.




                                                                                         14
            Interés moratorio

¿Para qué sirve?                                Características

• Incentivar el pago puntual.                   • Se aplica solo después de la fecha de
                                                  vencimiento.
• Resarcir al acreedor por el incumplimiento.
                                                • Es adicional al interés compensatorio.
• Cubrir posibles costos financieros por el
  retraso.                                      • La tasa puede ser fija o acordada por contrato.

                                                • Puede estar regulada por ley o normativas
                                                  sectoriales (como en bancos).




                                                                                               15
              Ejercicio 2.1

El Sr. Ramírez debía pagar una cuota de S/ 9,000    •
el 15 de abril, pero recién pagó 10 días después.
El contrato indica una tasa moratoria anual del
15%.
¿Cuánto debe pagar de interés moratorio por el
retraso?
Datos
• Im     Interés moratorio
• Mv     9,000
• rm     15%
• n      10




                                                        16
             Ejercicio 2.2

Carla debía pagar S/ 10,000 en 60 días con una     •
tasa compensatoria del 12% anual. Sin embargo,
por un contratiempo, se retrasó 20 días. La tasa
moratoria pactada era del 24% anual.
¿Cuánto tuvo que pagar por interés
compensatorio, interés moratorio y en total?


Datos
• Im    Interés moratorio
• Mv    10,000
• rm    24%
• n     20



                                                       17
3.
     Casos de aplicación




                           18
            Caso 1

Su empresa debe pagar impuestos por un total       Solución:
de 3 millones de pesos dentro de 270 días. Un      n = 270 días = 9 meses
banco de confianza le ofrece una tasa de interés
                                                   Tasa de i 12% anual, capitaliza cada 30 días =
del 12% anual, con capitalización cada 30 días.
                                                   Tasa Efectiva Mensual 1%
¿Cuánto dinero debe depositar hoy para
garantizar el pago de los impuestos en el plazo
establecido?                                       F = A * (1 + i) n
                                                   3,000,000 = A * (1 + 1% ) 9
Datos:                                             A = 3,000,000 / (1 + 1% ) 9
• F          3,000,000                             A = 2,743,019.47
• n          270 días
• Tasa de i 12% anual, capitaliza cada 30 días     Depositando hoy 2,743,019.47 se podrá retirar,
                                                   dentro de 9 meses (270 días), los 3,000,000 que
• A         ?
                                                   necesita la empresa para pagar sus impuestos.

                                                                                                    19
            Caso 2

Estoy evaluando dos alternativas de                 Solución:
financiamiento a 6 meses de S/. 20,000 para         Banco A tasa 6% anual capitaliza cada 15 días.
capital de trabajo.
                                                    • TEQ = 6% / 24 = 0.25%
El Banco A me ofrece una tasa del 6% anual
                                                    • TES = (1 + TEQ) ^ (180/15) =3.041596%
capitalizable cada 15 días y el banco B me ofrece
la misma tasa pero con capitalización diaria.       Banco B tasa 6% anual capitaliza diario.
¿Qué alternativa elije y cual es el interés         • TED = 6% / 360 = 0.0167%
resultante ganado por el banco?                     • TES = (1 + TED) ^ (180/1) =3.045196%
Datos:                                              Elijo al Banco A ya que su TES es menor.
• n = 6 meses                                       A más capitalizaciones, mayor tasa y viceversa.
• A = 20,000
• Banco A tasa 6% anual capitaliza cada 15 días.    • Interés = F – A = 20,000*(1+3.041596%) - 20,000
• Banco B tasa 6% anual capitaliza diario.          • Interés = 608.32
                                                    El banco A estará ganando 608.32 en intereses.

                                                                                                     20

            Caso 3

Un alumno necesita acumular $5,000 dentro de                Actualmente, dispone de $1,000, los cuales
dos años para financiar un viaje.                           destinará parcialmente a un fondo de inversión
Para lograrlo, planea realizar dos aportes:                 con una tasa del 0.75% mensual, utilizando el
$2,000 dentro de 6 meses en una cuenta con                  resto para comprar vestuario.
rendimiento del 1% mensual, y otros $2,000 en               ¿Cuánto puede gastar hoy en ropa sin
el mes 15 en una segunda cuenta que paga                    comprometer su meta de ahorro?
1.25% mensual.

  X ( 1 + 0.75% ) 24 = 1.1964135 X                                     1.1964135 X + 2,392.29 + 2,236.58 = 5,000
                                                                                                      X = 371.13
                   2,000 ( 1 + 1% ) 18 = 2,392.29                                        1,000 – 371.13 = 628.87
                                         2,000 ( 1 + 1.25% ) 9 = 2,236.58
                                                                                 Puede disponer de 628.87 para
                                                                                gastar en ropa sin comprometer
Mes             Mes                   Mes                       Mes                            su meta de 5,000
 0               6                    15                         24
X=?            2,000                                           5,000
                                                                                                             21
                                     2,000
            Caso 4

Un CEO desea renovar uno de los equipos más        1. ¿El saldo de la Cuenta A al final de los 3 años
costosos de su empresa dentro de 3 años y             será suficiente para cubrir el enganche?
necesita acumular $50,000 para el financiar la               No es suficiente, solo alcanza a 19,024
inversión. Para lograrlo, evalúa las siguientes
opciones de ahorro:                                2. Asumiendo que mantiene la misma tasa y
                                                      frecuencia de capitalización ¿cuánto debería
• Cuenta A: Depositar $15,000 hoy en una              ser el valor de cada aporte en la Cuenta B
  cuenta que paga una tasa del 8% anual               para alcanzar exactamente los $50,000?.
  capitalizable trimestralmente.                                                   Cuotas de 15.518

• Cuenta B: Realizar 3 aportes iguales de $5,000   3. Si el CEO combinara ambas estrategias
  al final de cada año en una cuenta con interés      (Cuenta A + Cuenta B), ¿cuál sería el monto
  del 7% anual capitalizable mensualmente.            total acumulado?
                                                                      Con A y B se llega a 35,134.11



                                                                                                    22
            Caso 5

Una persona desea crear un fondo educativo          Opción 3
para su hijo, quien comenzará la universidad en     • Inversión inicial: $20,000 hoy.
5 años. Para cubrir los gastos, necesita acumular
                                                    • Tasa de interés: 5.8% anual, con capitalización
$30,000 y está evaluando tres opciones de
                                                      quincenal.
inversión:
Opción 1
• Inversión inicial: $18,000 hoy.                   1. ¿Cuál de las 3 opciones le permitirá alcanzar
                                                       (o superar) los $30,000 en 5 años?
• Tasa de interés: 6% anual, capitalizable
  semestralmente.                                      Opción 2 con 30,696
Opción 2                                            2. Si elige la Opción 2, ¿cuál debería ser el
                                                       monto de cada aporte anual para llegar
• Aportes: 5 depósitos iguales al final de cada
                                                       exactamente a $30,000?
  año, comenzando dentro de un año.
• Tasa de interés: 5.5% anual, capitalizable           5,375
  anualmente.                                       3. Si combina la Opción 1 y Opción 3, ¿cuánto
                                                       dinero tendrá al final del período?
                                                       50,909.70
                                                                                                    23
Valor del dinero en el tiempo – Parte 2
        Finanzas Empresariales - Semana 11

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
