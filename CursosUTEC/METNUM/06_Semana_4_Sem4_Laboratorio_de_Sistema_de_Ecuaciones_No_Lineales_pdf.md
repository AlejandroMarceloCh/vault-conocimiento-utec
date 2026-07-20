---
curso: METNUM
titulo: 06 - Semana 4/Sem4_Laboratorio de Sistema de Ecuaciones No Lineales
slides: 18
fuente: 06 - Semana 4/Sem4_Laboratorio de Sistema de Ecuaciones No Lineales.pdf
---

Métodos Numéricos
Lab. S.E No Lineales
S04
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
                                             1 Método de Newton
                                             2 Método del Punto Fijo




Universidad de Ingeniería y Tecnología   Métodos Numéricos         April 15, 2026   1 / 17
        Objetivos
            Implementar rutinas en MATLAB para resolver ecuaciones y sistemas no
            lineales incorporando criterios de parada y generación automática de reportes
            de convergencia.




Universidad de Ingeniería y Tecnología        Métodos Numéricos              April 15, 2026   2 / 17
1   MÉTODO DE
    NEWTON
Introducción
Dado el sistema de ecuaciones no lineales:
                              
                                 f (x, y ) = 0
                                g(x, y ) = 0

El método de Newton consiste en realizar las siguientes iteraciones:

                        x(k +1) = x(k ) − J −1 (x(k ) )F(x(k ) )       k = 0; 1; 2; 3; · · ·

siendo necesario conocer el punto inicial o punto semilla x(0) , en notación matricial
tenemos:
                                                     f (x (k ) , y (k ) )
                (k +1)   (k )                                        
                  x            x           −1 (k )
                           =          − J (x )
                  y (k +1)     y (k )                g(x (k ) , y (k ) )
Siendo J la matriz Jacobiana del sistema.

Universidad de Ingeniería y Tecnología                 Métodos Numéricos                       April 15, 2026   4 / 17
El Jacobiano en MatLab
Matlab nos proporciona el comando jacobian para definir el jacobiano de funciones
vectoriales. Por ejemplo, para la función vectorial:

                            f (x, y ) = 2x − y − e−x = 0
                       

                          g(x, y ) = −x + 2y − e−y = 0

Usamos el siguiente script para este propósito:

 1   syms x y
 2   F = @(x,y) [2*x-y-exp(-x) ; -x+2*y-exp(-y)]
 3   dF = jacobian(F(x,y),[x,y])
 4   dFfun = matlabFunction(dF) % Revisar orden de argumentos de dFfun
 5   dFfun_eval = dFfun(3,4)

dFfun_eval proporciona la matriz Jacobiana evaluada en el punto (3, 4).


Universidad de Ingeniería y Tecnología   Métodos Numéricos         April 15, 2026   5 / 17
Ejemplo 1
  Ejercicio
 Resolver numéricamente (mediante el método de Newton) el siguiente sistema de
 ecuaciones no lineales:
                           f (x, y ) = 2x − y − e−x = 0
                      

                         g(x, y ) = −x + 2y − e−y = 0

                                         x (0)
                                                    
                                                   0.5
 Tomando como punto inicial x(0) =              =        , considere como criterio
                                         y (0)      1
 de terminación que el error relativo sea menor que una tolerancia prefijada Tol =
 1e − 3.




Universidad de Ingeniería y Tecnología       Métodos Numéricos      April 15, 2026   6 / 17
Método de Newton para 2 Variables

 1   function z = newton2v(F,x0,Tol)
 2       syms x y
 3       dF = jacobian(F(x,y),[x,y]);
 4       dF_fun = matlabFunction(dF);
 5       dr = 1;
 6       i = 0;
 7       z = [i x0' dr];
 8       while dr > Tol
 9           x1 = x0 - inv(dF_fun(x0(1),x0(2)))*F(x0(1),x0(2));
10           dr = norm(x1 - x0,'inf')/norm(x1,'inf');
11           x0 = x1;
12           i = i + 1;
13           z = [z; i x1' dr];
14       end
15   end



Universidad de Ingeniería y Tecnología   Métodos Numéricos        April 15, 2026   7 / 17
Método de Newton Vectorizado

 1   function z = newtonVec(F,x0,Maxiter)
 2       n = length(x0);
 3       syms x [n 1]
 4       J_sym = jacobian(F(x),x);
 5       J = matlabFunction(J_sym, 'Vars',{x});
 6       error = NaN;
 7       z = [0 x0' error];
 8       for i = 1:Maxiter
 9           x1 = x0 - inv(J(x0))*F(x0);
10           error = norm(x1 - x0,'inf')/norm(x1,'inf');
11           x0 = x1;
12           z = [z; i x1' error];
13       end
14   end




Universidad de Ingeniería y Tecnología   Métodos Numéricos   April 15, 2026   8 / 17
Ejercicio 1
Adapte el script proporcionado para obtener la solución numérica del siguiente
sistema de ecuaciones:

                                   f (x, y , z) = 3x − cos(yz) − 12 = 0
            
            
                g(x, y , z) = x 2 − 81(y + 0.1)2 + sin(z) + 1.06 = 0
                                h(x, y , z) = e−xy + 20z + 10π3−3 = 0
            


                                       x (0)
                                                    
                                                  0.1
Tomando como punto inicial x(0) =  y (0)  =  0.1 , considere como criterio
                                       z (0)     −0.1
de terminación que el error relativo sea menor que una tolerancia prefijada
Tol = 1e − 4.




Universidad de Ingeniería y Tecnología       Métodos Numéricos     April 15, 2026   9 / 17
2   MÉTODO DEL
    PUNTO FIJO
Método del Punto Fijo
Si a partir del sistema de ecuaciones no lineales:
                                 
                                    f (x, y ) = 0
                                   g(x, y ) = 0

Podemos identificar dos funciones u : R2 → R y v : R2 → R tales que:
                               
                                  x = u(x, y )
                                  y = v (x, y )

Entonces cualquier punto fijo (si existe) p = (x ∗ , y ∗ ) de la función G(x, y ) = (u, v )
satisface trivialmente f (p) = 0 y g(p) = 0.
Conclusión: Cualquier punto fijo p de G es también raíz del sistema de
ecuaciones no lineales original.


Universidad de Ingeniería y Tecnología      Métodos Numéricos              April 15, 2026   11 / 17
Método del Punto Fijo

 1   function z = pfijos(G,x0,Tol)
 2       dr = 1;
 3       i = 0;
 4       z = [i x0' dr];
 5       while dr > Tol
 6           x1 = G(x0);
 7           dr = norm(x1-x0,'inf')/norm(x1,'inf');
 8           x0 = x1;
 9           i = i + 1;
10           z = [z; i x1' dr];
11       end
12   end




Universidad de Ingeniería y Tecnología   Métodos Numéricos   April 15, 2026   12 / 17
Ejemplo 2
  Ejercicio
 Resolver numéricamente (mediante el método del punto fijo) el siguiente sistema
 de ecuaciones no lineales:
                            f (x, y ) = 2x − y − e−x = 0
                      

                         g(x, y ) = −x + 2y − e−y = 0

                                         x (0)
                                                    
                                                   0.5
 Tomando como punto inicial x(0) =              =        , considere como criterio
                                         y (0)      1
 de terminación que el error relativo sea menor que una tolerancia prefijada Tol =
 1e − 3.




Universidad de Ingeniería y Tecnología       Métodos Numéricos      April 15, 2026   13 / 17
Ejercicio 2
Luego de establecer la regla de correspondencia de una función g adecuada
(aquella que garantice convergencia), adapte el script proporcionado para obtener
la solución numérica del siguiente sistema de ecuaciones:

                                  f (x, y , z) = 3x − cos(yz) − 12 = 0
             
             
               g(x, y , z) = x 2 − 81(y + 0.1)2 + sin(z) + 1.06 = 0
                               h(x, y , z) = e−xy + 20z + 10π3−3 = 0
             


                                       x (0)
                                                    
                                                  0.1
Tomando como punto inicial x(0) =  y (0)  =  0.1 , considere como criterio
                                       z (0)     −0.1
de terminación que el error relativo sea menor que una tolerancia prefijada
Tol = 1e − 4.



Universidad de Ingeniería y Tecnología       Métodos Numéricos    April 15, 2026   14 / 17
Ejercicio 3
Examen EL1 - 2022-2
Determine las coordenadas de uno de los dos puntos donde se cruzan las
circunferencias (x − 2)2 + y 2 = 4 y x 2 + (y − 3)2 = 4. Una estimación de las
ubicaciones de los puntos a partir de un boceto gráfico nos dice que hay una raíz
cerca al punto (2, 2), que será utilizado como punto semilla. Primero escriba el
sistema de ecuaciones no lineales en la forma
                                           
                                         x     0
                                      F     =
                                         y     0
luego use el método de Newton para calcular las coordenadas de la raíz
considerando una tolerancia de 0.00001.
Luego efectúe lo siguiente:
  1 Asigne en la variable n la cantidad de iteraciones que realiza el algoritmo.
  2 Asigne en la variable w (como vector columna) la solución aproximada
    calculada en la última iteración del algoritmo.
  3 Asigne en la variable Fw el valor absoluto de F (w), interprete el resultado.
Universidad de Ingeniería y Tecnología   Métodos Numéricos          April 15, 2026   15 / 17
Conclusiones
       El método de Newton es una técnica eficiente para encontrar raíces de
       sistemas no lineales, aunque requiere un buen punto inicial y el cálculo de la
       matriz Jacobiana en cada iteración.
       El método del punto fijo proporciona una alternativa al método de Newton, pero
       su convergencia depende de la elección adecuada de la función de iteración y
       de la proximidad a la solución.
       El análisis de convergencia y error es fundamental en los métodos numéricos
       para garantizar soluciones precisas y eficientes, permitiendo evaluar la
       viabilidad de cada método en distintos contextos.




Universidad de Ingeniería y Tecnología    Métodos Numéricos            April 15, 2026   16 / 17
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
