---
curso: METNUM
titulo: 13 - Semana 12/Sem12_Laboratorio de EDO problema de valores iniciales
slides: 23
fuente: 13 - Semana 12/Sem12_Laboratorio de EDO problema de valores iniciales.pdf
---

Métodos
Numéricos
Lab. EDO - PVI
S12
Hermes Yesser Pantoja Carhuavilca
(hpantoja@utec.edu.pe)
Jimmy Mendoza Montalvo
(jmendoza@utec.edu.pe)
Rósulo Pérez Cupe
(rperezc@utec.edu.pe)
Julio Cesar Barraza Bernaola
(jbarraza@utec.edu.pe)
Marco Antonio Cuyubamba Espinoza
(mcuyubamba@utec.edu.pe)


                                    Profesores: Utec-Ciencias
                                                      Índice
                                            1 Ecuaciones       Diferen-
                                                 ciales Ordinarias de
                                                 Primer Orden




Universidad de Ingeniería y Tecnología   Métodos Numéricos          June 1, 2026   1 / 22
        Objetivos
            Implementar en MATLAB los métodos de Euler, Heun y RK4 para resolver
            problemas de valor inicial y analizar el efecto del tamaño de paso en la solución
            numérica.




Universidad de Ingeniería y Tecnología          Métodos Numéricos                June 1, 2026   2 / 22
    ECUACIONES


1   DIFERENCIALES

    ORDINARIAS
    DE PRIMER ORDEN
Solución exacta de EDOs con MATLAB
  Conceptos clave
        syms y(t): Declara y como función simbólica de t
        diff(y,t): Representa la derivada dy
                                          dt
        dsolve: Resuelve exactamente la EDO

 Sintaxis completa


   1   syms y(t)                         % 1. Declarar variables
   2   ode = diff(y,t) == f(t,y);        % 2. Definir la ecuacion
   3   cond = y(t0) == y0;               % 3. Condicion inicial (opcional)
   4   sol = dsolve(ode, cond)           % 4. Resolver




Universidad de Ingeniería y Tecnología      Métodos Numéricos         June 1, 2026   4 / 22
Consideraciones importantes
 Notas esenciales
        Requisito indispensable:
        Debes tener instalado el Symbolic Math Toolbox
        Limitación fundamental:
        Solo funciona para EDOs con solución analítica
        Buena práctica:
        Usar nombres descriptivos para las variables
          ode (ecuación), cond (condición), sol (solución)

  ¿Y si no cumple estos requisitos?
 Considera usar métodos numéricos como ode45 para aproximar soluciones cuando:
        No existe solución simbólica.
        Requieres resultados numéricos concretos.

Universidad de Ingeniería y Tecnología              Métodos Numéricos            June 1, 2026   5 / 22
Solución y Evaluación con matlabFunction
  Problema de ejemplo
 Resolver:
                          dy
                              = y cos(t) + t,      y (0) = 2
                           dt
 Evaluar en t = π/4 y graficar en t ∈ [0, 5].

 Implementación en MATLAB (Parte simbólica)


   1   syms y(t)
   2   ode = diff(y,t) == y*cos(t) + t;     % Define EDO
   3   cond = y(0) == 2;                    % Condicion inicial
   4   sol = dsolve(ode, cond);             % Solucion simbolica



Universidad de Ingeniería y Tecnología   Métodos Numéricos         June 1, 2026   6 / 22
Solución y Evaluación con matlabFunction
 Implementación en MATLAB (Evaluación y gráfica)


   1   syms y(t)
   2   ode = diff(y,t) == -2*y + exp(-t);
   3   cond = y(0) == 1;
   4   sol = dsolve(ode, cond);            % Solucion simbolica
   5   f = matlabFunction(sol);            % Funcion numerica
   6   y_eval = f(0.5);                    % Evaluar en t = 0.5
   7   t = linspace(0, 2, 100);
   8   plot(t, f(t), 'LineWidth', 2);
   9   xlabel('t'); ylabel('y(t)');
 10    title('Solucion de dy/dt = -2y + e^{-t}');
 11    grid on;




Universidad de Ingeniería y Tecnología   Métodos Numéricos        June 1, 2026   7 / 22
Ecuaciones Diferenciales Ordinarias
Método de Euler
                                          xi+1 = xi + h · f (ti , xi )



Método de Runge Kutta de orden 2 (Heun)
                                                
                                       1     1
                       xi+1 = xi + h     k1 + k2
                                       2     2

donde:
                                         k1 = f (ti , xi )
                                         k2 = f (ti + h, xi + k1 · h)

Universidad de Ingeniería y Tecnología                  Métodos Numéricos   June 1, 2026   8 / 22
Continuación...
Método de Runge Kutta de orden 4
                                                       h
                                         xi+1 = xi +     (k1 + 2k2 + 2k3 + k4 )
                                                       6

donde
                                             k1 = f (ti , xi )
                                                                      
                                                               h     h
                                             k2 = f ti + , xi + k1 ·
                                                               2     2
                                                                      
                                                               h     h
                                             k3 = f ti + , xi + k2 ·
                                                               2     2

                                             k4 = f (ti + h, xi + k3 · h)

Universidad de Ingeniería y Tecnología                      Métodos Numéricos     June 1, 2026   9 / 22
Ejemplo
Dado el siguiente Problema de Valor Inicial (PVI):
                       dx
                           = 2x + et ; t ∈ [0; 1]; x(0) = 1
                       dt
Aproximar x(0.2) y el error, utilizando el método de Euler. Considere h = 0.1.

 1   f = @(t, y) 2*y + exp(t);
 2   h = 0.1; t = 0:h:0.2;
 3   y = zeros(size(t)); y(1) = 1;
 4
 5   % Metodo de Euler
 6   for i = 1:length(t)-1
 7       y(i+1) = y(i) + h * f(t(i), y(i));
 8   end
 9
10   % Solucion exacta
11   y_exact = @(t) -exp(t) + 2*exp(2*t);
12 fprintf('Aproximacion (Euler): y(0.2) = %.4f\n', y(end));
13 fprintf('Valor
Universidad                      exacto: y(0.2) = %.4f\n',
            de Ingeniería y Tecnología                         y_exact(0.2));
                                                  Métodos Numéricos           June 1, 2026   10 / 22
Continuación...
     Aproximar x(0.2) y el error, utilizando el método de Runge Kutta de orden 2.
     Considere h = 0.1.

      1    f = @(t, y) 2*y + exp(t); % EDO
      2    h = 0.1; t = 0:h:0.2; y = 1; % Condiciones iniciales
      3
      4    % Metodo RK2 (Heun)
      5    for i = 1:length(t)-1
      6        k1 = f(t(i), y(i));
      7        k2 = f(t(i) + h, y(i) + h*k1);
      8        y(i+1) = y(i) + h/2 * (k1 + k2);
      9    end
      10
      11   % Solucion exacta y error
      12   y_exact = -exp(0.2) + 2*exp(0.4);
      13   error = abs(y_exact - y(end));
      14
        15 % Resultados (Reemplazado el simbolo problematico aprox)
Universidad
        16 de Ingeniería y Tecnología(Heun): y(0.2) =
            fprintf('RK2                            Métodos Numéricos
                                                      %.6f\nError                 June 1, 2026 ...
                                                                      = %.6f\n', y(end),         11 / 22
Continuación...
     Aproximar x(0.2) y el error, utilizando el método de Runge Kutta de orden 4.
     Considere h = 0.1.

      1   f = @(t, y) 2*y + exp(t);   % Definicion de la EDO
      2   h = 0.1; t = 0:h:0.2; y = 1; % Condiciones iniciales
      3
      4   % Metodo RK4
      5   for i = 1:length(t)-1
      6       k1 = f(t(i), y(i));
      7       k2 = f(t(i) + h/2, y(i) + h/2*k1);
      8       k3 = f(t(i) + h/2, y(i) + h/2*k2);
      9       k4 = f(t(i) + h, y(i) + h*k3);
     10       y(i+1) = y(i) + h/6 * (k1 + 2*k2 + 2*k3 + k4);
     11   end
     12
     13     % Solucion exacta y error
     14     y_exact = -exp(0.2) + 2*exp(0.4);
        15 error = abs(y_exact - y(end));
Universidad
        16 de
            % Ingeniería y Tecnología(Reemplazado simbolo
                Resultados                          Métodos Numéricos
                                                             problematico)   June 1, 2026   12 / 22
Funciones en Matlab
Ejercicio 1
Implementar la función Euler, con la siguiente cabecera

 1   function [z]=euler(f,a,b,x0,h)

Ejercicio 2
Implementar la función Runge Kutta 2, con la siguiente cabecera

 1   function [z]=rk2(f,a,b,x0,h)

Ejercicio 3
Implementar la función Runge Kutta 4, con la siguiente cabecera

 1   function [z]=rk4(f,a,b,x0,h)

Universidad de Ingeniería y Tecnología   Métodos Numéricos        June 1, 2026   13 / 22
El comando ode45 de Matlab
El comando ode45 en MATLAB resuelve ecuaciones diferenciales de la forma:

                                         dy
                                            = f (t, y ),   y (t0 ) = y0
                                         dt
Sintaxis básica:

 1   [t, y] = ode45(f, [t0 tf], y0)

donde:
       f es la función derivada f(t, y), declarada como una función anónima @f.
       [t0 tf] define el intervalo de integración (tspan),
       y0 es la condición inicial.


Universidad de Ingeniería y Tecnología                Métodos Numéricos   June 1, 2026   14 / 22
¿Qué es y cómo funciona ode45?
El comando ode45 es una herramienta de MATLAB para resolver ecuaciones diferenciales numéricamente, como
las que modelan crecimiento poblacional, movimiento de objetos o circuitos eléctricos.

¿Cómo trabaja?
       Paso variable: Ajusta automáticamente "cuántos pasos da" para equilibrar precisión y velocidad.
       Error controlado: Intenta mantener los resultados dentro de una tolerancia aceptable.
       Solución suave: Funciona mejor cuando la solución no tiene cambios bruscos o repentinos.

¿Cuándo usarlo?
       En problemas típicos (ej.: modelos físicos sin fuerzas extremas, sistemas biológicos estables).
       Cuando no sabes qué método elegir: es la opción "por defecto" en MATLAB.
       Si la simulación tarda demasiado o falla, puede que necesites otro método (pero eso lo veremos después).


Salida: Dos vectores: t: tiempos donde se calculó la solución. y: valores de la solución en esos tiempos.




Universidad de Ingeniería y Tecnología                 Métodos Numéricos                       June 1, 2026   15 / 22
Ejemplo
Dado el siguiente Problema de Valor Inicial (PVI):

                                     dy
                                        = 2y + et ;   t ∈ [0; 1];     y (0) = 1
                                     dt
aproximar la solución.
Solución:

 1   f=@(x,y)(2*y+exp(x))
 2   [x,y]=ode45(f,[0 1],1)




Universidad de Ingeniería y Tecnología                Métodos Numéricos           June 1, 2026   16 / 22
Aplicación de Ecuaciones Diferenciales
Ordinarias de primer orden
Una varilla de acero se calienta hasta 800◦ C y luego se deja enfriar al medio
ambiente la cual se encuentra a 20◦ C, si se sabe que el modelo matemático
correspondiente es representado por la ley de enfriamiento de Newton, la cual es:

                                         dT
                                            = k (T − Ta )
                                         dt
donde Ta , es la temperatura ambiente en ◦ C y k es la constante de enfriamiento en
s−1 .




Universidad de Ingeniería y Tecnología         Métodos Numéricos    June 1, 2026   17 / 22
Continuación...
   1   Si después de 30 segundos la temperatura se reduce a 500◦ C, calcule k con 4
       decimales, resolviendo la EDO analíticamente.
   2   Usando el método de Runge Kutta de orden 2, estime la temperatura en el
       instante t = 4 segundos considerando un tamaño de paso de 2 segundos.
   3   Graficar la curva: T vs t en los primeros 5 minutos. Considere el comando
       ode45.




Universidad de Ingeniería y Tecnología   Métodos Numéricos           June 1, 2026   18 / 22
Ejercicio
En un circuito eléctrico, se dispone de un condensador con capacidad constante
C = 1.1 faradios y una resistencia R = 2.1 ohmios. Se le aplica un voltaje:

                                         E(t) = e−0.06πt sin(2t − π)

La ecuación que rige el comportamiento de un circuito sin inducción es:

                                                  dI   I   dE
                                              R      +   =
                                                  dt   C   dt
Supongamos que la intensidad en el instante inicial es I(0) = 1 amperio. Halle el
valor aproximado de la intensidad cada 0.2 segundos, durante los dos primeros
segundos, use el método de Runge - Kutta de orden 4.




Universidad de Ingeniería y Tecnología               Métodos Numéricos   June 1, 2026   19 / 22

Examen EL2 - 2025 - 0
Si se supone que el arrastre es proporcional al cuadrado de la velocidad, se puede modelar la velocidad de un
objeto que cae, como un paracaidista, por medio de la ecuación diferencial siguiente:

                                                dv     cd 2
                                                   =g−   v
                                                dt     m

Donde:

       v : velocidad (m/s)                                       cd : coeficiente de arrastre (0.225 kg/m)
       t: tiempo (s)                                             m: masa (90 kg)
       g: aceleración de la gravedad (9.81 m/s2 )

Si se asume que el cuerpo parte del reposo (v (0) = 0). Se necesita conocer la velocidad transcurridos 10
segundos, para ello:
      Utilice el método de Euler para resolver la EDO que modela la velocidad, con un tamaño de paso de tiempo:
      h = ∆t = 0.1. Almacene el resultado obtenido en la variable ValueEuler.
      Halle la velocidad exacta para 10 segundos, almacene el resultado en la variable ValueExacto.
      Utilice el método de Runge Kutta de orden 4 (RK4) para resolver la EDO que modela la velocidad con un
      tamaño de paso de tiempo, almacene el resultado en la variable ValueRK4.
      Calcule el error absoluto entre la solución numérica (utilizando el método de RK4) y la solución exacta en el
      punto de tiempo. Almacene el resultado en la variable ValueError.
Universidad de Ingeniería y Tecnología                 Métodos Numéricos                       June 1, 2026   20 / 22
Conclusiones
       Se analizaron métodos numéricos para resolver EDO de primer orden con PVI,
       incluyendo Euler, Runge-Kutta de orden 2 y 4, destacando su precisión y
       aplicabilidad.
       Se implementaron estos métodos en MATLAB, mostrando su uso mediante
       funciones personalizadas y el comando ode45 para resolver ecuaciones
       diferenciales.
       Se estudiaron aplicaciones prácticas, como el modelo de enfriamiento de
       Newton y circuitos eléctricos, resaltando la importancia de estos métodos en
       ingeniería.




Universidad de Ingeniería y Tecnología   Métodos Numéricos            June 1, 2026   21 / 22

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
