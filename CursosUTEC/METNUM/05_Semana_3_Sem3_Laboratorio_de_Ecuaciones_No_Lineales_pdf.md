---
curso: METNUM
titulo: 05 - Semana 3/Sem3_Laboratorio de Ecuaciones No Lineales
slides: 27
fuente: 05 - Semana 3/Sem3_Laboratorio de Ecuaciones No Lineales.pdf
---

Métodos Numéricos
Lab. Ecuaciones no lineales
S3
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
                                            1 Métodos Cerrados
                                            2 Métodos Abiertos




Universidad de Ingeniería y Tecnología   Métodos Numéricos       April 9, 2026   1 / 26
        Objetivos
            Implementar rutinas en MATLAB para resolver ecuaciones y sistemas no
            lineales incorporando criterios de parada y generación automática de reportes
            de convergencia.




Universidad de Ingeniería y Tecnología         Métodos Numéricos              April 9, 2026   2 / 26
1   MÉTODOS
    CERRADOS
Introducción
Determine la solución de la ecuación xe−x = 0.2.
 1   f = @(x)(x.*exp(-x)-0.2)
 2   fplot(f,[0 8]); grid on;
 3   yline(0);
 4   fzero(f,0.7)
 5   fzero(f,2.8)


                              0.2

                              0.1

                                0

                             -0.1

                             -0.2
                                    0    2      4                6   8


Universidad de Ingeniería y Tecnología       Métodos Numéricos           April 9, 2026   4 / 26
Localización de raíces
Localizar gráficamente las raíces de f (x) = −x 2 + 2x + ex

 1   xx = [-4:0.01:4];
 2   f1 = @(x) x.^2-2.*x;
 3   yy1 = f1(xx);
 4   f2 = @(x) exp(x);
 5   yy2 = f2(xx);
 6   plot(xx,yy1,'r',xx,yy2,'b')
 7   grid on




Universidad de Ingeniería y Tecnología   Métodos Numéricos    April 9, 2026   5 / 26
Teorema de Bolzano
 Teorema
 Si f es continua en [a; b], f (a) × f (b) < 0 entonces existe al menos una raíz x ⋆ en
 el intervalo [a; b] tal que f (x ⋆ ) = 0.

Si f (a) × f (b) = 0, la raíz se encuentra en uno de los extremos del intervalo [a; b].
Ejemplo: Localizar las raíces de f (x) = −x 2 + 2x + ex

 1   f = @(x)(-x^2+2*x+exp(x));
 2   a = -1;
 3   b = 0;
 4   if f(a)*f(b) < 0
 5        fprintf('Existe al menos una raiz')
 6   else
 7        fprintf('No se puede afirmar que existe una raiz')
 8   end

Universidad de Ingeniería y Tecnología    Métodos Numéricos              April 9, 2026   6 / 26
Método de la Bisección
 1   function [x , iter ] = biseccion (f , a , b , tol )
 2       if f ( a ) * f ( b ) > 0
 3            error ( ' La funcion debe tener signos opuestos en a y b ') ;
 4       end
 5       iter = 0;
 6       while ( b - a ) / 2 > tol
 7            c = ( a + b ) / 2;
 8            if f ( c ) == 0
 9                    break ;
10            end
11            if f ( a ) * f ( c ) < 0
12                    b = c;
13            else
14                    a = c;
15            end
16            iter = iter + 1;
17       end
18       x = ( a + b ) / 2;
19   end

Universidad de Ingeniería y Tecnología    Métodos Numéricos              April 9, 2026   7 / 26
Método de la Bisección (Tabla)
 1   function z = biseccion2(f,a,b,Maxiter)
 2       % Version con tabla de salida
 3       disp('iter      a         b                  c      f(c)');
 4       for k = 1:Maxiter
 5           c = (a + b)/2;
 6           z(k,:) = [k, a, b, c, f(c)];
 7           if f(c) == 0
 8               break;
 9           end
10           if f(a)*f(c) < 0
11                b = c;
12           else
13                a = c;
14           end
15       end
16   end



Universidad de Ingeniería y Tecnología   Métodos Numéricos             April 9, 2026   8 / 26
Ejemplo 1
  Ejemplo
 Aproximar la solución de la ecuación no lineal ex−1 − cos π4 x = 0 utilizando el
                                                               

 método de la bisección. Realice 6 iteraciones.


 1   f = @(x) exp(x-1) - cos(pi/4*x);
 2   a = 0;
 3   b = 1;
 4   Maxiter = 6;
 5   z = biseccion2(f,a,b,Maxiter)




Universidad de Ingeniería y Tecnología   Métodos Numéricos          April 9, 2026   9 / 26
Ejercicio 1
  Ejercicio
 Aproximar la solución de la ecuación no lineal −x 2 + 2x + ex = 0 utilizando el
 método de la bisección con una tolerancia 1e-3 e indique el número de iteraciones
 necesarias para alcanzar dicha tolerancia.




Universidad de Ingeniería y Tecnología   Métodos Numéricos          April 9, 2026   10 / 26
Ejercicio 2 - EL1 2024 - 2
Se tiene la función:
                                                       2      cos(x)
                                         f (x) = e1+3x−x +           − sin(2x)
                                                                x
en el intervalo [−7, 7].
Realice lo siguiente:
   1   Determine el número de raíces reales y asigne el valor a la variable nvar.
   2   Localice el intervalo [a, b] de longitud 1, que contenga la menor raíz. Donde a y
       b son números enteros, almacene el resultado en el vector fila test, donde
       test = [a, b].
   3   Aproxime la menor raíz (en el intervalo dado inicialmente) utilizando el método
       de la bisección con una tolerancia tol = 1 × 10−5 y asigne el resultado a la
       variable yaprox. Considere como intervalo [a, b] para la ejecución del método
       lo localizado en el ítem anterior.

Universidad de Ingeniería y Tecnología                     Métodos Numéricos     April 9, 2026   11 / 26
2   MÉTODOS
    ABIERTOS
Método de Newton
Se desea resolver de forma aproximada:

                                                  f (x) = 0

Formula de recurrencia:

                                                                f (x (k ) )
                                         x (k +1) = x (k ) −               
                                                               f ′ x (k )

Dado un x (0) , para k = 0, 1, 2, . . .




Universidad de Ingeniería y Tecnología                Métodos Numéricos        April 9, 2026   13 / 26
Función Newton

 1   function z = newton(f,x0,Tol)
 2       syms x
 3       df = diff(f,x);
 4       df = matlabFunction(df);
 5       dr = 1;
 6       i = 0;
 7       z = [i x0 f(x0) df(x0) dr];
 8       while(dr > Tol)
 9           x1 = x0 - f(x0)/df(x0);
10           dr = abs(x1 - x0)/abs(x1);
11           x0 = x1;
12           i = i + 1;
13           z = [z; i x1 f(x1) df(x1) dr];
14       end
15   end



Universidad de Ingeniería y Tecnología   Métodos Numéricos   April 9, 2026   14 / 26
Ejemplo 1
  Ejemplo
 Usar el método de Newton para aproximar las raíces de f (x) = ex−1 − cos π4 x ,
                                                                              

 comenzando con x (0) = 0.01 con una tolerancia de 1e-2.


 1   f = @(x) exp(x-1) - cos(pi/4*x);
 2   x0 = 0.01;
 3   Tol = 1e-2;
 4   z = newton(f,x0,Tol)




Universidad de Ingeniería y Tecnología   Métodos Numéricos        April 9, 2026   15 / 26
Ejemplo 2
  Ejemplo
 Usar el método de Newton para aproximar las raíces de f (x) = x 3 − 2x + 2,
 comenzando con x (0) = 1 con una tolerancia de 1e-3. Analice el funcionamiento
 del código bajo esta situación.


 1   f = @(x) x^3-2*x+2;
 2   x0 = 1;
 3   Tol = 1e-3;
 4   z = newton(f,x0,Tol)




Universidad de Ingeniería y Tecnología   Métodos Numéricos        April 9, 2026   16 / 26
Ejercicio 3 - Examen EL1 2024 - 2
El rendimiento de un motor de combustión interna está influenciado por varios factores, incluyendo la temperatura
del motor, la presión interna y la velocidad de operación. La eficiencia térmica η(T ) de un motor puede ser
modelada por:
                                                                         c
                                           η(T ) = η0 − k (T − Topt )2 +
                                                                         T
donde:
       η0 = 0.35: eficiencia máxima del motor.
       k = 0.01: constante que describe la pérdida de eficiencia por desviación de Topt .
       Topt = 90◦ : temperatura óptima para máxima eficiencia.
       c = 300: constante relacionada con el calor generado en el motor.
Se busca calcular la temperatura T en °C a la cual η(T ) = 0.2 usando el método de Newton-Raphson:
   1 Defina una función f (T ) cuya raíz corresponda al problema, es decir, resuelva f (T ) = η(T ) − 0.2.
   2 Calcule T con tolerancia 1 × 10−5 usando Newton-Raphson, iniciando en T = 80◦ . Almacene el resultado
     en Taprox.
   3 Determine la cantidad de iteraciones necesarias para alcanzar la solución y almacénela en iterations.
Adicionalmente, almacene el valor de |f (85)| en la variable nvalue.



Universidad de Ingeniería y Tecnología                 Métodos Numéricos                       April 9, 2026   17 / 26
Método del Punto Fijo
Dada
                                                 f (x) = 0 → x = g(x)

Condiciones de convergencia
       |g ′ (x)| < 1        ∀x ∈ [a; b]
       g([a; b]) ⊂ [a; b]
Ecuación de recurrencia:
                                                           
                                         x (k +1) = g x (k ) ;   k = 0, 1, 2, . . .




Universidad de Ingeniería y Tecnología                     Métodos Numéricos          April 9, 2026   18 / 26
Función Punto Fijo

 1   function z = pfijo(g,x0,Tol)
 2       % Metodo del punto fijo: x_{k+1} = g(x_k)
 3       dr = 1;
 4       i = 0;
 5       z = [i x0 g(x0) dr];
 6       while(dr>Tol)
 7           x1 = g(x0);
 8           dr = abs(x1 - x0)/abs(x1);
 9           x0 = x1;
10           i = i + 1;
11           z = [z; i x1 g(x1) dr];
12       end
13   end




Universidad de Ingeniería y Tecnología   Métodos Numéricos   April 9, 2026   19 / 26

Ejemplo 1


  Ejemplo
 Usar el método del punto fijo para aproximar las raíces de f (x) = x 2 − 2x − 3,
 comenzando con x0 = 4, utilice 10 iteraciones. Analice previamente su conver-
 gencia.




Universidad de Ingeniería y Tecnología   Métodos Numéricos         April 9, 2026   20 / 26
 1   syms x
 2   g = ma tlabFu nction ( sqrt (2* x +3) ) ;
 3
 4   % CONDICION DE EXISTENCIA :
 5   xx = [0:0 .01 :4];
 6   yy = g ( xx ) ;
 7   plot ( xx , yy , 'r ' ,[0 4] ,[ g (0) g (4) ] , ' ob ') ; grid on ;
 8   % Se visualiza que g ([0;4]) in [0;4] ( cumple )
 9
10   % CONDICION DE CONTRACCION :
11   dg = diff ( g ( x ) ) ;
12   fudg = mat labFun ction ( dg ) ;
13   xx = [0:0 .01 :4];
14   yy1 = abs ( fudg ( xx ) ) ;
15   plot ( xx , yy1 , 'b ') ; grid on ;
16   % Se visualiza que |g '( x ) | <1 para x in [0;4] ( cumple )
17
18   % METODO DE PUNTO FIJO :
19   x0 = 4;
20   Maxiter = 10;
21   z = pfijo (g , x0 , Maxiter )

Universidad de Ingeniería y Tecnología               Métodos Numéricos     April 9, 2026   21 / 26
Ejercicio 4 - Examen EL1 - 2024 - 2
Considere la estimación de un parámetro α a partir de la distribución de eficiencia
de una antena parabólica, que tiene la función de eficiencia E(r ; α) como:

                                                          αre−ar
                                             E(r ; α) =
                                                          1 − e−α
donde α > 0 y r = 1, 2, 3, . . .. La eficiencia de la antena depende de las
características de construcción y se ajusta en base a mediciones discretas de la
señal. La ecuación de máxima verosimilitud para α, basada en una muestra
aleatoria R1 , R2 , . . . , Rn , se reduce a
                                           nα                             X
                                   R−            =0    donde       R=         Ri .
                                         1 − e−α




Universidad de Ingeniería y Tecnología                Métodos Numéricos              April 9, 2026   22 / 26
Continuación...
Para encontrar una solución a esta ecuación, podríamos reescribirla como:

                                                                           R
                                         α̂ = R̄(1 − e−α̂ ) donde R̄ =       .
                                                                           n
Por lo tanto, α se considera como la eficiencia promedio observada en las
mediciones. La identidad reformulada sugiere la iteración de punto fijo:
                         (
                           α(0) = R̄
                           α(k +1) = R̄ 1 − exp(−α(k ) )
                                                        


Los datos que vamos a emplear en el problema son una muestra de tal manera que
R̄ = 4.




Universidad de Ingeniería y Tecnología                 Métodos Numéricos         April 9, 2026   23 / 26
Continuación...
Se le pide efectuar lo siguiente:
   1 Defina la función del método del punto fijo g(α) donde g tiene la notación trabajada en clase y asigne el
     valor de g(1) a la variable numérica g1.
   2 Efectúe las iteraciones del método del punto fijo hasta alcanzar una tolerancia de 10−5 . Almacene la
     cantidad de iteraciones en la variable numérica niter_pf.
   3 Se sabe que el valor exacto de α̂ se puede calcular en MATLAB con el comando lambertw (consulte la
     documentación de MATLAB para ello) de la siguiente forma:

                                         αexacto = 4 + lambertw (−3/exp(4)) .

       Halle el error absoluto de la aproximación dada por el método del punto fijo y almacene el resultado en la
       variable numérica error_pf.
   4 Aplique el método de la bisección para resolver la ecuación R̄(1 − e−α̂ ) − α̂ = 0 en el intervalo [0, 4].
     Realice tantas iteraciones como las realizadas por el método del punto fijo. Almacene el error absoluto de la
     aproximación por el método de la bisección (ojo que ya conoce el valor exacto) en la variable numérica
     error_bi.




Universidad de Ingeniería y Tecnología                 Métodos Numéricos                      April 9, 2026   24 / 26
Conclusiones
       Los métodos cerrados como bisección garantizan convergencia, mientras que
       los abiertos como Newton son más rápidos pero dependen de una buena
       aproximación inicial.
       La precisión y eficiencia de un método depende a su vez de la función y la
       tolerancia elegida, afectando el número de iteraciones necesarias.
       Los métodos numéricos son herramientas esenciales para resolver ecuaciones
       no lineales en ingeniería y ciencias cuando no es posible encontrar soluciones
       analíticas exactas.




Universidad de Ingeniería y Tecnología    Métodos Numéricos            April 9, 2026   25 / 26
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
