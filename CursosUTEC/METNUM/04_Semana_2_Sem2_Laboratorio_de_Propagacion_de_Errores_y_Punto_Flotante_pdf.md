---
curso: METNUM
titulo: 04 - Semana 2/Sem2_Laboratorio de Propagación de Errores y Punto Flotante
slides: 26
fuente: 04 - Semana 2/Sem2_Laboratorio de Propagación de Errores y Punto Flotante.pdf
---

Métodos Numéricos
Lab. Propagación de
errores y punto flotante
S2
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
                                                       Índice
                                             1 Propagación de Errores
                                             2 Punto Flotante




Universidad de Ingeniería y Tecnología   Métodos Numéricos       March 23, 2026   1 / 25
        Objetivos
    Al finalizar esta sesión, el estudiante será capaz de:
            Analizar la propagación de errores numéricos en procesos iterativos mediante
            experimentación en MATLAB.
            Representar números reales en formato IEEE 754 (precisión simple y doble)
            para interpretar su efecto en los cálculos numéricos.




Universidad de Ingeniería y Tecnología       Métodos Numéricos             March 23, 2026   2 / 25
1   PROPAGACIÓN
    DE ERRORES
Propagación de errores: Resistencias

  Ejemplo                                       Modelos Matemáticos
 Dadas dos resistencias:                       Conexión en Serie:
        R1 = 20 ± 4 Ω
                                                             Req = R1 + R2
        R2 = 300 ± 2 Ω
 Determine el valor de la resistencia
                                               Conexión en Paralelo:
 equivalente y sus errores absolutos
 cuando se conectan en serie y en par-                                R1 R2
                                                             Req =
 alelo.                                                              R1 + R2




Universidad de Ingeniería y Tecnología   Métodos Numéricos                March 23, 2026   4 / 25
Solución en MATLAB (Cálculo Simbólico)
 1   clear all; syms R1 R2;
 2   er1 = 4; er2 = 2;
 3
 4   % --- Analisis en Serie ---
 5   f1 = R1 + R2;
 6   df1_R1 = diff(f1, R1);
 7   df1_R2 = diff(f1, R2);
 8   erf_serie = double(abs(df1_R1)*er1 + abs(df1_R2)*er2)
 9
10   % --- Analisis en Paralelo ---
11   f2 = R1*R2 / (R1 + R2);
12   df2_R1 = diff(f2, R1);
13   df2_R2 = diff(f2, R2);
14   erf2 = simplifyFraction(abs(df2_R1)*er1 + abs(df2_R2)*er2);
15   erf2_paralelo = double(subs(erf2, {R1, R2}, {20, 300}))



Universidad de Ingeniería y Tecnología   Métodos Numéricos    March 23, 2026   5 / 25
Implementación: Función de Error Total
 1   function [dy, y] = totalErrorFunction(f, x, dx)
 2   % Calcula la propagacion de errores mediante la serie de Taylor de ...
         1er orden
 3   % EJEMPLOS:
 4   % >> % Funcion real de una variable
 5   % >> x=2; dx=0.4; f=@(x) exp(x); [dy, y]= totalErrorFunction(f,x,dx)
 6   % >> % Funcion real de varias variables
 7   % >> x=[20,300]; dx=[4,2]; f=@(x) x(1)*x(2) / (x(1)+x(2));
 8   % >> [dy, y]= totalErrorFunction(f,x,dx)




Universidad de Ingeniería y Tecnología   Métodos Numéricos    March 23, 2026   6 / 25
Continuación...

 1           x = x(:); dx = dx(:);       % Estandarizando como vectores columna
 2           N = length(x); syms t [N 1]
 3           df_dt = jacobian(f(t), t); % Calculo del Jacobiano (Derivadas ...
                 parciales)
 4
 5           y = f(x);                  % Evaluar la funcion en el valor ...
                 nominal
 6           df_dx = double( subs(df_dt, t, x) ); % Evaluar derivadas en el ...
                 punto
 7
 8           dy = abs(df_dx) * dx;       % Calculo final de propagacion de ...
                 error absoluto
 9   end




Universidad de Ingeniería y Tecnología    Métodos Numéricos        March 23, 2026   7 / 25
Ejercicio: Potencia de un Circuito
Un circuito eléctrico incluye una fuente de
voltaje vs , una resistencia interna rs , y una
carga RL . La potencia disipada es:

                                     vs2 RL
                        P=
                                (RL + rs )2

Datos medidos:
       RL = 10 ± 0.01 Ω
       vs = 12V ± 1%
       rs ∈ [2.48, 2.51] Ω                                   Retos
                                                             1. Estime la potencia nominal P
                                                             (Watts).
                                                             2. Determine el error absoluto de P.
                                                             3. Halle el intervalo de confianza de P.
Universidad de Ingeniería y Tecnología        Métodos Numéricos                    March 23, 2026   8 / 25
Ejercicio: Cinemática (EL1 2024-1)
Un vehículo parte del reposo (MRUV).
Recorre una distancia x = 900 ± 18 m en un
tiempo t = 30 ± ∆t s. La aceleración se
calcula como:
                        2x
                  a= 2
                        t
Dato Clave: El error en la distancia (∆x = 18
m) contribuye exactamente al 75% del error
total de la aceleración.




Universidad de Ingeniería y Tecnología   Métodos Numéricos   March 23, 2026   9 / 25
Ejercicio: Cinemática (EL1 2024-1) - Continuación
  Desarrollo Computacional
 Implemente un script para hallar las siguientes variables:
   a) ace: Valor nominal de la aceleración.
   b) a_partial_x: Derivada parcial de la aceleración respecto a x, evaluada en
      x = 900 y t = 30.
   c) err_a: Error absoluto total de la aceleración.
   d) err_t: Incertidumbre original del tiempo (∆t).

Sugerencia: Utilice la fórmula general de propagación de errores y plantee una
ecuación para despejar ∆t.



Universidad de Ingeniería y Tecnología   Métodos Numéricos       March 23, 2026   10 / 25
2   PUNTO
    FLOTANTE
Comandos de Conversión de Bases en MATLAB
Conversiones Directas                         Bases Arbitrarias

 1   % Decimal a Binario                       1   % Decimal a Base 4
 2   dec2bin(168)                              2   dec2base(732, 4)
 3                                             3
 4   % Binario a Decimal                       4   % Base 6 a Decimal
 5   bin2dec('101101')                         5   base2dec('1452332', 6)
 6                                             6
 7   % Decimal a Hexadecimal                   7   % Base 3 a Base 5 (Anidado)
 8   dec2hex(543)                              8   dec2base(base2dec('122110', ...
 9                                                     3), 5)
10   % Hexadecimal a Decimal
11   hex2dec('1FA')




Universidad de Ingeniería y Tecnología   Métodos Numéricos              March 23, 2026   12 / 25
Conversión de Binarios Fraccionarios a Decimal
Caso 1: Solo Fracción (0.1010012 )            Caso 2: Mixto (1110.1012 )

 1   format long                               1   format long
 2   b = '101001';                             2   entera = '1110';
 3   % Multiplicar por 2^(-n) ...              3   fracc = '101';
         desplaza el punto                     4
 4   N = bin2dec(b) * 2^(-length(b))           5   dec_entera = bin2dec(entera);
                                               6   dec_fracc = bin2dec(fracc) * ...
                                                       2^(-length(fracc));
                                               7   N = dec_entera + dec_fracc




Universidad de Ingeniería y Tecnología   Métodos Numéricos            March 23, 2026   13 / 25
Representación IEEE 754 en MATLAB

 Precisión Simple (32 bits)                     Precisión Doble (64 bits)
 Representar 625:                              Representar 625:

   1   % Opcion 1: Usando sprintf                1   % Opcion 1: Usando sprintf
   2   N1 = sprintf('%tu', 625);                 2   N1 = sprintf('%bu', 625);
   3   N2 = str2double(N1);                      3   N2 = str2double(N1);
   4   N = dec2bin(N2, 32);                      4   N = dec2bin(N2, 64);
   5                                             5
   6   % Opcion 2: Usando typecast               6   % Opcion 2: Usando typecast
   7   N0 = single(625);                         7   N0 = double(625);
   8   N = typecast(N0, 'uint32');               8   N = typecast(N0, 'uint64');
   9   b = dec2bin(N, 32);                       9   b = dec2bin(N, 64);




Universidad de Ingeniería y Tecnología   Métodos Numéricos            March 23, 2026   14 / 25
Ejemplo: De IEEE 754 (32 bits) a Decimal
Problema: Identifique el valor decimal de 1 01111100 11000000000000000000000

 Script de Extracción

   1   b = '10111110011000000000000000000000';
   2   s = b(1);          % Bit de signo
   3   e = b(2:9);        % Exponente interno
   4   m = b(10:32);      % Mantisa fraccionaria
   5
   6   dec_s = bin2dec(s);
   7   dec_e = bin2dec(e);
   8   dec_m = bin2dec(m) * 2^(-length(m));
   9
 10    bias = 2^(length(e)-1) - 1;
 11    x = (-1)^dec_s * 2^(dec_e - bias) * (1 + dec_m)



Universidad de Ingeniería y Tecnología   Métodos Numéricos   March 23, 2026   15 / 25
Aritmética de Punto Flotante y Asociatividad
En la máquina, cada operación básica implica un redondeo implícito (fl):

       a ⊕ b = fl(fl(a) + fl(b))                   a ⊗ b = fl(fl(a) × fl(b))
       a ⊖ b = fl(fl(a) − fl(b))                   a ⊘ b = fl(fl(a)/fl(b))

  Ejemplo
Evalúe la suma 0.99 + 0.0044 + 0.0042 redondeando a tres cifras significativas.
¿Importa el orden en que se suman?

 Conclusión Aritmética
 En sistemas de punto flotante de precisión finita, la suma no es estrictamente
 asociativa. El orden de las operaciones puede alterar el resultado final por la
 acumulación de errores de truncamiento/redondeo.


Universidad de Ingeniería y Tecnología   Métodos Numéricos               March 23, 2026   16 / 25
Simulación de Hardware: Función redond.m
  Imitando la memoria finita

   1   function y = redond(x, n)
   2   % Devuelve x redondeado a 'n' cifras significativas.
   3       if x == 0
   4            y = 0;
   5       else
   6            s = sign(x);
   7            expo = ceil(log(abs(x))/log(10));
   8            mant = exp(log(abs(x)) - expo*log(10));
   9
 10                  nm = round(mant * 10^n) / (10^n); % Recorte
 11                  y = s * nm * 10^expo;             % Reconstruccion
 12           end
 13    end



Universidad de Ingeniería y Tecnología      Métodos Numéricos        March 23, 2026   17 / 25
Operaciones Aritméticas Simuladas
 1   function y=suma(a,b,n)
 2       y=redond(redond(a,n)+redond(b,n),n);
 3   end
 4
 5   function y=resta(a,b,n)
 6       y=redond(redond(a,n)-redond(b,n),n);
 7   end
 8
 9   function y=prod(a,b,n)
10       y=redond(redond(a,n)*redond(b,n),n);
11   end
12
13   function y=div(a,b,n)
14       y=redond(redond(a,n)/redond(b,n),n);
15   end
16
17   function y=raiz(a,n)
18          y=redond(sqrt(redond(a,n)),n);
Universidad
19 end de Ingeniería y Tecnología       Métodos Numéricos   March 23, 2026   18 / 25
Solución: Evaluación de Asociatividad
 1   % Usando las funciones de aritmetica simulada
 2   R1 = suma(suma(0.99, 0.0044, 3), 0.0042, 3)
 3   disp(R1)
 4
 5   R2 = suma(0.99, suma(0.0044, 0.0042, 3), 3)
 6   disp(R2)
 7
 8   % No se debe de hacer (simulacion incorrecta)
 9   S = redond(0.99 + 0.0044 + 0.0042, 3)
10   disp(S)


Análisis
Al ejecutar el código, los resultados de R1 y R2 serán distintos, corroborando empíricamente que la suma no es
asociativa debido a la precisión finita (n = 3).



Universidad de Ingeniería y Tecnología              Métodos Numéricos                    March 23, 2026   19 / 25

Ejemplo: Raíces de una Ecuación Cuadrática
  Ejemplo
 Calcule las raíces de la ecuación de segundo grado:

                                         0.2x 2 − 47.9x + 6 = 0

 realizando operaciones con cuatro cifras significativas.
 Nota: Utilice la siguiente función.


 1   function [x1, x2] = cuadratica(a, b, c, n)
 2       Delta = resta(prod(b,b,n), prod(4,prod(a,c,n),n), n);
 3       x1 = div(suma(-b, raiz(Delta,n), n), prod(2,a,n), n);
 4       x2 = div(resta(-b, raiz(Delta,n), n), prod(2,a,n), n);
 5   end



Universidad de Ingeniería y Tecnología           Métodos Numéricos   March 23, 2026   20 / 25
Solución y Consideraciones: Ecuación
Cuadrática
 1   a = input('Ingrese el coeficiente a: ');
 2   b = input('Ingrese el coeficiente b: ');
 3   c = input('Ingrese el coeficiente c: ');
 4
 5   [x1, x2] = cuadratica(a, b, c, 4)



Observación Importante
Observe que cuando las raíces son complejas, cuadratica() no trabaja de la manera esperada. Esto se debe
a que la función redond() programada anteriormente no está diseñada para manejar correctamente el redondeo
de números imaginarios.




Universidad de Ingeniería y Tecnología            Métodos Numéricos                   March 23, 2026   21 / 25
Límites de la Máquina en MATLAB
       Épsilon de la Máquina (eps): En IEEE 754 (doble precisión) es
       2−52 ≈ 2.22 × 10−16 . Es el límite de resolución entre 1.0 y el siguiente número
       representable. Almacena ≈ 16 dígitos decimales fiables.
       Límite Inferior (realmin): Devuelve el número de punto flotante normalizado
       positivo más pequeño. Equivale a 2−1022 . Valores menores caen en
       subnormales o "underflow".
       Límite Superior (realmax): Devuelve el número finito más grande
       representable. Equivale a (2 − 2−52 ) × 21023 . Valores mayores resultan en
       Infinito ("overflow").




Universidad de Ingeniería y Tecnología    Métodos Numéricos            March 23, 2026   22 / 25
Conclusiones
       El cálculo simbólico en MATLAB (funciones syms, jacobian, diff) facilita
       enormemente el desarrollo analítico para el cálculo de la propagación de
       errores multivariable.

       Se simuló matemáticamente el proceso de representación numérica,
       demostrando que en el computador la aritmética no obedece ciegamente los
       axiomas del álgebra real (p. ej., pérdida de asociatividad).




Universidad de Ingeniería y Tecnología   Métodos Numéricos          March 23, 2026   23 / 25
Bibliografía
      Steven C. Chapra y Raymond P. Canale.
      Métodos numéricos para ingenieros, 7a ed., McGraw-Hill, 2015.
      Richard L. Burden y J. Douglas Faires.
      Análisis numérico, 7a ed., Thompson, 2002.




Universidad de Ingeniería y Tecnología   Métodos Numéricos        March 23, 2026   24 / 25
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
