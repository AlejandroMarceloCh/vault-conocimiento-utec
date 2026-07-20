---
curso: METNUM
titulo: 14 - Semana 13/Sem13_Laboratorio de Sistema EDO
slides: 30
fuente: 14 - Semana 13/Sem13_Laboratorio de Sistema EDO.pdf
---

Métodos
Numéricos
Lab. Sistemas EDO
S13
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
                                            1 Sistemas de Ecuaciones
                                              Diferenciales Ordinarias
                                              de Primer Orden
                                            2 Ecuaciones         Difer-
                                              enciales    de    Orden
                                              Superior




Universidad de Ingeniería y Tecnología   Métodos Numéricos          June 1, 2026   1 / 29
        Objetivos
            Implementar métodos numéricos de un paso en MATLAB para resolver
            ecuaciones diferenciales de orden superior y sistemas de ecuaciones
            diferenciales ordinarias.
            Implementar el método de disparo en MATLAB para resolver problemas de
            valor de frontera.
            Implementar diferencias finitas en MATLAB para resolver problemas de valor de
            frontera




Universidad de Ingeniería y Tecnología        Métodos Numéricos               June 1, 2026   2 / 29
    SISTEMAS DE

1   ECUACIONES
    DIFERENCIALES
    ORDINARIAS DE
    PRIMER ORDEN
Ejemplo 1
Considere el sistema EDO de primer orden
                   (
                     x1′ = x1 + 5x2 + sen t,             x1 (0) = −1
                     x2′ = 5x1 − 3x2 + 2 cos t,          x2 (0) = 1


   1   Hallar la solución exacta en Matlab utilizando el comando dsolve.
   2   Graficar la solución.




Universidad de Ingeniería y Tecnología    Métodos Numéricos            June 1, 2026   4 / 29
Ejemplo 1 - Solución

 1   syms x1(t) x2(t)
 2   Dx1 = diff(x1,t); Dx2 = diff(x2,t);
 3   sol = dsolve(Dx1 == x1 + 5*x2 + sin(t), Dx2 == 5*x1 - 3*x2 + ...
         2*cos(t), x1(0)==-1, x2(0)==1);
 4   sol_x1 = matlabFunction(sol.x1);
 5   sol_x2 = matlabFunction(sol.x2);
 6   tt = t0:0.05:tf;
 7   x1_sol = sol_x1(tt); x2_sol = sol_x2(tt);
 8   figure(1);
 9   subplot(2,1,1);
10   plot(tt,x1_sol,'-k','LineWidth',1.5); grid on; hold on;
11   xlabel('Tiempo'); ylabel('x1');
12   title('Solucion Exacta del Sistema EDO de Primer Orden')
13   subplot(2,1,2);
14   plot(tt,x2_sol,'-k','LineWidth',1.5); grid on; hold on;
15   xlabel('Tiempo'); ylabel('x2');

Universidad de Ingeniería y Tecnología   Métodos Numéricos     June 1, 2026   5 / 29
Ejemplo 1
                      1
                                                      x 1 (exacta)
               x1     0


                     -1
                          0              0.2   0.4              0.6      0.8        1
                                                     Tiempo
                      1
                                                      x 2 (exacta)
            x2     0.5


                      0
                          0              0.2   0.4              0.6      0.8        1
                                                     Tiempo
Universidad de Ingeniería y Tecnología               Métodos Numéricos         June 1, 2026   6 / 29
Sistemas EDO de Primer Orden
MÉTODO DE EULER PARA SISTEMAS EDO (FORMA VECTORIAL)

                                            yi+1 = yi + hF(ti , yi )


MÉTODO DE RK2 (HEUN) PARA SISTEMAS EDO (FORMA VECTORIAL)
                                                                           
                                                              1     1
                                         yi+1 = yi + h          k1 + k2
                                                              2     2
donde:
                                           k1 = F(ti , yi )
                                           k2 = F(ti + h, yi + hk1 )



Universidad de Ingeniería y Tecnología                  Métodos Numéricos       June 1, 2026   7 / 29
Sistema de EDO de Primer Orden
MÉTODO DE RK4 PARA SISTEMAS EDO (FORMA VECTORIAL)

                                                       h
                                         yi+1 = yi +     (k1 + 2k2 + 2k3 + k4 )
                                                       6
donde:
                                             k1 = F(ti , yi )
                                                                  
                                                              h h
                                             k2 = F ti + , yi + k1
                                                              2 2
                                                                  
                                                              h h
                                             k3 = F ti + , yi + k2
                                                              2 2

                                             k4 = F(ti + h, yi + hk3 )


Universidad de Ingeniería y Tecnología                     Métodos Numéricos      June 1, 2026   8 / 29
Ejemplo de Sistema de EDO (Continuación)
Considere el sistema EDO de primer orden
                   (
                     x1′ = x1 + 5x2 + sen t,              x1 (0) = −1
                     x2′ = 5x1 − 3x2 + 2 cos t,           x2 (0) = 1


       Aproximar x1 (t) y x2 (t) utilizando el método de Euler. Considere h = 0.1.

         1   F = @(t,y) [ 1*y(1) + 5*y(2) + 1*sin(t)
         2                5*y(1) - 3*y(2) + 2*cos(t) ];
         3   t0 = 0; tf = 1;
         4   y0 = [-1 1]';
         5   h = 0.1;




Universidad de Ingeniería y Tecnología     Métodos Numéricos             June 1, 2026   9 / 29
Ejemplo de Sistema de EDO (Continuación)
       Luego aplicamos el método de Euler:

         1   t_euler = t0:h:tf; t_euler = t_euler';
         2   iter = 0:length(t_euler)-1; iter = iter';
         3   m = length(t_euler);
         4   n = length(y0);
         5   y_euler = zeros(m,n);
         6   K1 = zeros(m,n);
         7   y_euler(1,:) = y0;
         8   for i = 1:length(t_euler)-1
         9       K1(i,:) = F(t_euler(i,1),y_euler(i,:));
       10        y_euler(i+1,:) = y_euler(i,:) + h*K1(i,:);
       11    end




Universidad de Ingeniería y Tecnología   Métodos Numéricos    June 1, 2026   10 / 29
 x2_euler = y_euler(:,2);
 T = table(iter,t_euler, x1_euler, x2_euler, k1, 'VariableNames
 Ejemplo de Sistema
 {'i','t_euler',          de 'x2_euler',
                 'x1_euler', EDO (Continuación)
                                         'K1'});
 disp(T);
        Tabla de resultados
        i          t_euler                x1_euler    x2_euler                     K1
        __         _______                _________   ________            ____________________

         0               0                       -1          1                  4           -6
         1             0.1                     -0.6        0.4             1.4998        -2.21
         2             0.2                 -0.45002      0.179            0.64366     -0.82695
         3             0.3                 -0.38565   0.096306             0.3914      -0.3065
         4             0.4                 -0.34651   0.065656            0.37119    -0.087401
         5             0.5                 -0.30939   0.056916            0.45461     0.037455
         6             0.6                 -0.26393   0.060661            0.60402      0.14903
         7             0.7                 -0.20353   0.075564            0.81851      0.28534
         8             0.8                 -0.12168     0.1041             1.1162      0.47272
         9             0.9                -0.010062    0.15137             1.5301       0.7388
        10               1                  0.14295    0.22525                  0            0

Método de Runge-Kutta de 2do Orden:
 Universidad de Ingeniería y Tecnología               Métodos Numéricos               June 1, 2026   11 / 29
Ejemplo de Sistema de EDO (Continuación)
                       1
                                                     x 1 (exacta)
                                                     x 1 (euler)
                x1     0


                      -1
                           0             0.2   0.4            0.6    0.8       1
                                                 Tiempo
                       1
                                                     x 2 (exacta)
                                                     x 2 (euler)
              x2    0.5


                       0
                           0             0.2   0.4            0.6    0.8       1
                                                 Tiempo
Universidad de Ingeniería y Tecnología           Métodos Numéricos         June 1, 2026   12 / 29
Funciones en Matlab
Ejercicio 1: Implementar la función Euler, con la siguiente cabecera:
 1   function [iter,t_euler,y_euler,K1]=eulerV(F,t0,tf,y0,h)


Ejercicio 2: Implementar la función Runge Kutta 2, con la siguiente cabecera:
 1   function [iter,t_RK2,y_RK2,K1,K2] = RK2V(F,t0,tf,y0,h)


Ejercicio 3: Implementar la función Runge Kutta 4, con la siguiente cabecera:
 1   function [iter,t_RK4,y_RK4,K1,K2,K3,K4] = RK4V(F,t0,tf,y0,h)

Compare sus resultados con la gráfica siguiente:


Universidad de Ingeniería y Tecnología   Métodos Numéricos          June 1, 2026   13 / 29
Ejemplo de Sistema de EDO (Continuación)
                        1           x 1 (exacta)
                                    x 1 (euler)
                                    x 1 (RK2)
                 x1     0           x 1 (RK4)




                       -1
                            0                   0.2   0.4                   0.6   0.8       1
                                                            Tiempo
                        1
                                                              x 2 (exacta)
                                                              x 2 (euler)
                                                              x 2 (RK2)
               x2    0.5                                      x 2 (RK4)




                        0
                            0                   0.2   0.4                   0.6   0.8       1
                                                            Tiempo
Universidad de Ingeniería y Tecnología                  Métodos Numéricos               June 1, 2026   14 / 29
El comando ode45 de Matlab
El comando ode45 en MATLAB también resuelve sistemas de ecuaciones
diferenciales de la forma:
                           dy
                              = F(t, y) con y(t0 ) = y0
                           dt
Sintaxis básica:
 1   [t, y] = ode45(F, [t0 tf], y0)
 2   [t, y] = ode45(F, tspan, y0)

donde:
       F es la función que define el S.EDO F(t, y), la cual puede declararse como
       una función anónima (@F).
       [t0 tf] es el intervalo donde se resuelve el sistema.
       tspan es un vector de tiempos especificados por el usuario.
       y0 es el vector de condiciones iniciales del sistema.
Universidad de Ingeniería y Tecnología     Métodos Numéricos         June 1, 2026   15 / 29
Ejemplo
Considere el sistema EDO de primer orden
                   (
                     x1′ = x1 + 5x2 + sen t,                              x1 (0) = −1
                     x2′ = 5x1 − 3x2 + 2 cos t,                           x2 (0) = 1
                                                    T
aproximar la solución y =                    x1 x2        usando ode45.
       Solución:
         1   F = @(t,y) [ 1*y(1) + 5*y(2) + 1*sin(t)
         2                5*y(1) - 3*y(2) + 2*cos(t) ];
         3   t0 = 0; tf = 1; tspan = t0:h:tf;
         4   y0 = [-1 1]';
         5   [t,y]=ode45(F,[t0 tf],y0)
         6   [t,y]=ode45(F,tspan,y0)



Universidad de Ingeniería y Tecnología                     Métodos Numéricos            June 1, 2026   16 / 29
Ejercicio
Resuelva el siguiente sistema de ecuaciones diferenciales utilizando los métodos
de Runge-Kutta de orden 2 y de orden 4. Obtenga la solución aproximada en x = 2
con un tamaño de paso igual a 0.5.

                          dy1
                        
                         dx = −0.5y1 ,                   y1 (0) = 4
                        
                        
                                                                       x ∈ [0, 2]
                         dy2 = 4 − 0.3y2 − 0.1y1 ,
                        
                                                          y2 (0) = 6
                        
                          dx




Universidad de Ingeniería y Tecnología           Métodos Numéricos                  June 1, 2026   17 / 29
2   EDO DE
    ORDEN SUPERIOR
Ejemplo 2
Dada la ecuación diferencial de segundo orden de valor inicial

                                        1
                           y ′′ + 5y ′ − y = − cos t;      y (0) = 1, y ′ (0) = 0
                                        5


   1   Hallar la solución exacta utilizando el comando dsolve de Matlab.
   2   Graficar la solución.




Universidad de Ingeniería y Tecnología            Métodos Numéricos                 June 1, 2026   19 / 29

Ejemplo 2 - Solución Exacta

 1   syms y(t)
 2   Dy = diff(y,1);
 3   D2y = diff(y,2);
 4   sol = dsolve(D2y == -5*Dy + 0.2*y - cos(t), y(0)==1, Dy(0)==0);
 5   sol = matlabFunction(sol);
 6   tt = 0:0.1:10;
 7   yexac = sol(tt);
 8   figure(1); clf;
 9   plot(tt,yexac,'-k','LineWidth',1.5); grid on;
10   title('Solucion de la EDO de Segundo Orden')
11   xlabel('Tiempo');
12   ylabel('y');




Universidad de Ingeniería y Tecnología   Métodos Numéricos     June 1, 2026   20 / 29
Ejemplo 2 - Solución Exacta
                                         Solución de la EDO de Segundo Orden
                   1.6

                   1.5

                   1.4

                   1.3

               y   1.2

                   1.1

                     1

                   0.9

                   0.8
                         0                2           4               6        8      10
                                                          Tiempo


Universidad de Ingeniería y Tecnología                    Métodos Numéricos        June 1, 2026   21 / 29
Ejemplo 2: EDO de 2◦ Orden a S.EDO de 1◦ Orden
Para reducirlo a un sistema de primer orden, definimos:

                                                      x1 = y ,      x2 = y ′ .

Derivando estas ecuaciones, obtenemos:
                                                                   1
                                         x1′ = x2 ,    x2′ = −5x2 + x1 − cos t.
                                                                   5
Así, el sistema equivalente de primer orden con condiciones iniciales es:
                     (
                       x1′ = x2 ,                  x1 (0) = 1
                         ′          1
                       x2 = −5x2 + 5 x1 − cos t,   x2 (0) = 0



Universidad de Ingeniería y Tecnología                           Métodos Numéricos   June 1, 2026   22 / 29
Ejemplo 2: EDO de 2◦Orden a S.EDO de 1◦Orden
Solución con Método de RK2 Vectorizado
Aplicamos el método de Runge-Kutta de segundo orden con h = 0.1 para el
sistema:           (
                     x1′ = x2 ,                x1 (0) = 1
                       ′         1
                     x2 = −5x2 + 5 x1 − cos t, x2 (0) = 0
Definimos el sistema en forma vectorial:
                                                             
                        x1                         x2
                   y=       , F(t, y) =
                        x2                 −5x2 + 15 x1 − cos t

Considerando:
                                         k1 = F(t0 , y0 )
                                         k2 = F(t0 + h, y0 + hk1 )

Universidad de Ingeniería y Tecnología               Métodos Numéricos   June 1, 2026   23 / 29
Ejemplo 2: EDO de 2◦Orden a S.EDO de 1◦Orden
 1   F = @(t,y) [ y(2) ; -5*y(2) + (1/5)*y(1) - cos(t) ];
 2   y0 = [1 0]';
 3   t0 = 0; tf = 10; h = 0.25;
 4   t_RK2 = t0:h:tf; t_RK2 = t_RK2';
 5   iter = 0:length(t_RK2)-1; iter = iter';
 6   m = length(t_RK2); n = length(y0);
 7   y_RK2 = zeros(m,n);
 8   K1 = zeros(m,n); K2 = zeros(m,n);
 9   y_RK2(1,:) = y0;
10   for i = 1:length(t_RK2)-1
11       K1(i,:) = F(t_RK2(i,1),y_RK2(i,:));
12       K2(i,:) = F(t_RK2(i,1)+h,y_RK2(i,:)+h*K1(i,:));
13       y_RK2(i+1,:) = y_RK2(i,:) + h*(0.5*K1(i,:)+0.5*K2(i,:));
14   end




Universidad de Ingeniería y Tecnología   Métodos Numéricos     June 1, 2026   24 / 29
Ejemplo 2 - Solución con RK2
                       1.5
                                         y(exacta)
                                         x 1 (RK2)
                 x1
                          1

                              0                 2    4               6       8   10
                                                         Tiempo

                       0.2               x 2 (RK2)


                x2     0.1
                          0
                      -0.1
                              0                 2    4               6       8   10
                                                         Tiempo


Universidad de Ingeniería y Tecnología                   Métodos Numéricos       June 1, 2026   25 / 29
th h = 0.5.    damping coefficient c takes on three values: 5 (underdamped), 40
               (critically damped), and 200 (overdamped). The spring constant
       Ejercicio
un (without    k = 20 N/m. The initial velocity is zero, and the initial displacement
       El movimiento de un sistema acoplado masa-resorte (véase la figura inferior) está
                 = la
       descritoxpor  1 m. Solve diferencial
                       ecuación this equation   using aque
                                             ordinaria   numerical
                                                           sigue: method over the
               time period 0 ≤ t ≤ 15 s.′′Plot the displacement versus time for each
                                     mx (t) + cx ′ (t) + kx = 0
               of the three values of the damping coefficient on the same curve.
       donde x = desplazamiento desde la posición de equilibrio(m), k = 20N/m, t =
 0 to 3:tiempo, m = 20 kg masa, y c = coeficiente de amortiguamiento (N.s/m). El
       coeficiente de amortiguamiento adopta tres valores: 5 (subamortiguado), 40
                FIGURE P25.16
       (amortiguamiento crítico), y 200 (sobreamortiguamiento). La velocidad inicial es de
       cero y el desplazamiento inicial es x = 1.
                                                                    x
od to solve                                                     k

                                                m               c



       Universidad de Ingeniería y Tecnología       Métodos Numéricos      June 1, 2026   26 / 29
Preguntas
   1   Resuelva la ecuación usando el método de Runge Kutta de orden 2 para
       ecuaciones diferenciales de grado 2 para h = 2.5; y 0 ≤ t ≤ 5 s.
   2   Realice el ejercicio anterior para cada uno de los tres valores del coeficiente de
       amortiguamiento.




Universidad de Ingeniería y Tecnología      Métodos Numéricos             June 1, 2026   27 / 29
Conclusiones
       Se estudiaron técnicas para transformar ecuaciones diferenciales de orden
       superior en sistemas de primer orden, permitiendo su solución numérica con
       métodos estándar.
       Se aplicaron métodos numéricos de un solo paso, como Euler y Runge-Kutta,
       para resolver sistemas de ecuaciones diferenciales, comparando precisión y
       estabilidad.
       Se implementaron estos métodos en MATLAB, demostrando su efectividad en
       la resolución de sistemas acoplados y ecuaciones de orden superior en
       aplicaciones de ingeniería.




Universidad de Ingeniería y Tecnología   Métodos Numéricos          June 1, 2026   28 / 29
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
