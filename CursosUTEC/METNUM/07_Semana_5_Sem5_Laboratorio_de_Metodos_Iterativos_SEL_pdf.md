---
curso: METNUM
titulo: 07 - Semana 5/Sem5_Laboratorio de Metodos Iterativos SEL
slides: 29
fuente: 07 - Semana 5/Sem5_Laboratorio de Metodos Iterativos SEL.pdf
---

Métodos Numéricos
Lab. Métodos Iterativos - SEL
S5
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
                                             1 Método de Jacobi
                                             2 Método de Gauss-Seidel
                                             3 Convergencia




Universidad de Ingeniería y Tecnología   Métodos Numéricos        April 20, 2026   1 / 28
        Objetivos
            Implementar en MATLAB métodos iterativos (Jacobi y Gauss-Seidel) para
            resolver sistemas lineales, incorporando control de tolerancia.




Universidad de Ingeniería y Tecnología      Métodos Numéricos             April 20, 2026   2 / 28
Métodos Iterativos
Dado el sistema de ecuaciones lineales Ax = b → x (k +1) = Tx (k ) + c, dado x (0)
inicial, donde:
T : Matriz de iteración.
c: vector
       columna. 
        a11 a12 a13
A = a21 a22 a23  → A = D − L − U, donde:
        a31 a32 a33
                                                                                 
           a11 0  0                            0    0   0                 0 −a12 −a13
      D =  0 a22 0  ,                  L = −a21  0   0 ,         U = 0  0   −a23 
            0  0 a33                          −a31 −a32 0                 0  0    0




Universidad de Ingeniería y Tecnología           Métodos Numéricos             April 20, 2026   3 / 28
Ejemplo 1

  Ejemplo
                            
                       5 3 1
 Dada la matriz A = 3 6 2
                       4 3 8
 Halle la matriz D, L y U


 1   A = [5 3 1; 3 6 2; 4 3 8];
 2   D = diag(diag(A))
 3   L = -tril(A,-1)
 4   U = -triu(A,1)
 5   D - L - U % Obtenemos la matriz A



Universidad de Ingeniería y Tecnología   Métodos Numéricos   April 20, 2026   4 / 28
1   MÉTODO DE
    JACOBI
Método de Jacobi
Dado el sistema lineal Ax = b, podemos reescribirlo como:

                                         Ax = b → (D − L − U)x = b
                                            Dx = (L + U)x + b
                                              x = D−1 (L + U)x + D−1 b

Ecuación de recurrencia:

                                             x (k +1) = Tj x (k ) + cj


Tj = D−1 (L + U): Matriz de Iteración de Jacobi.
cj = D−1 b: Vector columna del lado derecho.
Dado x (0) , la solución iterativa avanza aplicando la ecuación de recurrencia hasta
alcanzar la convergencia.
Universidad de Ingeniería y Tecnología                  Métodos Numéricos   April 20, 2026   6 / 28
Función Jacobi

 1   function [z] = jacobi(A,b,x0,Tol)
 2       D = diag(diag(A));
 3       L = -tril(A,-1);
 4       U = -triu(A,1);
 5       Tj = inv(D)*(L+U);
 6       cj = inv(D)*b;
 7       error = 1;
 8       z = [x0' error];
 9       while error > Tol
10           x1 = Tj*x0 + cj;
11           error = norm(x1-x0,inf)/norm(x1,inf);
12           z = [z; x1' error];
13           x0 = x1;
14       end
15   end



Universidad de Ingeniería y Tecnología   Métodos Numéricos   April 20, 2026   7 / 28
Ejemplo 2
El sistema lineal Ax = b dado por:

                                         10x1 − x2 + 2x3              =6
                                         −x1 + 11x2 − x3 + 3x4        = 25
                                         2x1 − x2 + 10x3 − x4         = −11
                                         3x2 − x3 + 8x4               = 15
                                              T
Tiene una solución única x ∗ = 1 2 −1 1 . Utilice el método iterativo de
                              

Jacobi para encontrar aproximaciones x (k ) a x ∗ , comenzando con
                  T
x (0) = 0 0 0 0 hasta que se cumpla:
       


                                           ||x (k +1) − x (k ) ||∞
                                                                   < 10−3
                                                ||x (k +1) ||∞



Universidad de Ingeniería y Tecnología                  Métodos Numéricos     April 20, 2026   8 / 28
Solución

 1   A = [10 -1 2 0; -1 11 -1 3; 2 -1 10 -1; 0 3 -1 8];
 2   b = [6; 25; -11; 15];
 3   Tol = 1e-3;
 4   x0 = [0; 0; 0; 0];
 5   z = jacobi(A,b,x0,Tol)




Universidad de Ingeniería y Tecnología   Métodos Numéricos   April 20, 2026   9 / 28
Ejercicio 1
Dado el sistema de ecuaciones:
                                         4x1 + 2x2 + x3  =9
                                         x1 + 5x2 + 3x3  = 14
                                         2x1 + 6x2 + 9x3 = 23

Aproximar la solución
                   utilizando
                              el método de Jacobi. Realice 10 iteraciones.
                   0.5
Considere x (0) =  1 .
                   0.5
Nota: Modifique la función jacobi.m para resolver el ejercicio.




Universidad de Ingeniería y Tecnología           Métodos Numéricos   April 20, 2026   10 / 28
2   MÉTODO DE
    GAUSS-SEIDEL
Método de Gauss Seidel
Dado el sistema lineal Ax = b, podemos reescribirlo como:
                                     Ax = b → (D − L − U)x = b
                                   (D − L)x = Ux + b
                                          x = (D − L)−1 Ux + (D − L)−1 b
Ecuación de recurrencia:

                                          x (k +1) = Tgs x (k ) + cgs

Tgs = (D − L)−1 U: Matriz de Iteración de Gauss-Seidel.
cgs = (D − L)−1 b: Vector columna del lado derecho.
Dado x (0) , la solución iterativa avanza aplicando la ecuación de recurrencia hasta
alcanzar la convergencia.
Universidad de Ingeniería y Tecnología                Métodos Numéricos    April 20, 2026   12 / 28
Función Gauss-Seidel

 1   function [z] = gausseidel(A,b,x0,Tol)
 2       D = diag(diag(A));
 3       L = -tril(A,-1);
 4       U = -triu(A,1);
 5       Tgs = inv(D-L)*U;
 6       cgs = inv(D-L)*b;
 7       error = 1;
 8       z = [x0' error];
 9       while error > Tol
10           x1 = Tgs*x0 + cgs;
11           error = norm(x1-x0,'inf')/norm(x1,'inf');
12           z = [z; x1' error];
13           x0 = x1;
14       end
15   end



Universidad de Ingeniería y Tecnología   Métodos Numéricos   April 20, 2026   13 / 28
Ejemplo 3
El sistema lineal Ax = b dado por:

                                         10x1 − x2 + 2x3              =6
                                         −x1 + 11x2 − x3 + 3x4        = 25
                                         2x1 − x2 + 10x3 − x4         = −11
                                         3x2 − x3 + 8x4               = 15
                                          T
Tiene una solución única x ∗ = 1 2 −1 1 . Utilice el método iterativo de
                              

Gauss-Seidel para encontrar aproximaciones x (k ) a x ∗ , comenzando con
                  T
x (0) = 0 0 0 0 hasta que sea cumpla:
       


                                           ||x (k +1) − x (k ) ||∞
                                                                   < 10−3
                                                ||x (k +1) ||∞



Universidad de Ingeniería y Tecnología                 Métodos Numéricos      April 20, 2026   14 / 28
Solución

 1   A = [10 -1 2 0; -1 11 -1 3; 2 -1 10 -1; 0 3 -1 8];
 2   b = [6; 25; -11; 15];
 3   Tol = 1e-3;
 4   x0 = [0; 0; 0; 0];
 5   z = gausseidel(A,b,x0,Tol)




Universidad de Ingeniería y Tecnología   Métodos Numéricos   April 20, 2026   15 / 28
Ejercicio 1
Dado el sistema de ecuaciones:
                                         4x1 + 2x2 + x3  =9
                                         x1 + 5x2 + 3x3  = 14
                                         2x1 + 6x2 + 9x3 = 23

Aproximar la solución
                   utilizando
                              el método de Gauss Seidel. Realice 10 iteraciones.
                   0.5
Considere x (0) =  1 .
                   0.5
Nota: Modifique la función gausseidel.m para resolver el ejercicio.




Universidad de Ingeniería y Tecnología           Métodos Numéricos   April 20, 2026   16 / 28
Ejercicio 2 (EL1 - 2024-2)
Considere el siguiente sistema de ecuaciones lineales en función del parámetro c:
                          
                          6x1 − 2x2 + cx3 = 4
                          
                            −3x1 + (2 + c)x2 + x3 = 5
                          
                            cx1 + 3x2 + 5x3 = 2
                          

El parámetro c varía en [−15, −3] con incrementos de 1. Realice lo siguiente:
  1 Determine el número de casos en el rango de c en los cuales el método de
    Gauss-Seidel converge. Almacene este valor en la variable numconverge.
  2 Aplique el método de Gauss-Seidel (solo en los casos en los que exista
                                                        T
    convergencia) con un vector semilla x (0) = 0 0 0 con una tolerancia de
                                               

    1e-5 y almacene las soluciones en una matriz xsol, donde las columnas
    representen las soluciones para cada valor de c.
  3 Determine la cantidad de iteraciones necesarias para alcanzar la convergencia
    usando el método de Gauss-Seidel en cada caso y almacene estos valores en
    un vector columna niterv.
Universidad de Ingeniería y Tecnología   Métodos Numéricos        April 20, 2026   17 / 28
    CONVERGENCIA

3
Convergencia
Definición: Diagonal estrictamente dominante
A es una matriz diagonal estrictamente dominante
                                               
                                    a11 a12 a13
                               A = a21 a22 a23 
                                    a31 a32 a33

si se cumple:

                                         |a11 | > |a12 | + |a13 |
                                         |a22 | > |a21 | + |a23 |
                                         |a33 | > |a31 | + |a32 |



Universidad de Ingeniería y Tecnología            Métodos Numéricos   April 20, 2026   19 / 28

Función Diagonal Estrictamente Dominante

 1   function op = diagdom(A)
 2       % op = 0: No es diagonal estrictamente dominante (D.E.D.)
 3       % op = 1: Es diagonal estrictamente dominante (D.E.D.)
 4       [m,n] = size(A);
 5       op = 1; % asumir que A es D.E.D., luego verificar:
 6       if m == n
 7           for k = 1:m
 8               if abs(A(k,k)) ≤ sum(abs(A(k,:))) - abs(A(k,k))
 9                   op = 0; % Si una fila no cumple, A no es D.E.D.
10                   break;
11               end
12           end
13       end
14   end




Universidad de Ingeniería y Tecnología   Métodos Numéricos    April 20, 2026   20 / 28
Ejemplo 4
  Ejemplo
                               
                       −8 1  6
 Dada la matriz A =  8 13   4 , determinar si la matriz A es diagonal
                        1 9 −10
 estrictamente dominante.

Solución:
| − 8| > |1| + |6|, cumple (8 > 7)
|13| > |8| + |4|, cumple (13 > 12)
| − 10| = |1| + |9|, No cumple (10 ≯ 10)
Por lo tanto no es diagonal estrictamente dominante.

 1   A = [-8 1 6; 8 13 4; 1 9 -10];
 2   op = diagdom(A)

Universidad de Ingeniería y Tecnología   Métodos Numéricos   April 20, 2026   21 / 28
Teoremas de Convergencia
  Teorema
 Si A es diagonal estrictamente dominante entonces el método de Jacobi y Gauss-
 Seidel son convergentes para cualquier x (0) inicial.

  Teorema
 El método de Jacobi es convergente si y solo si el radio espectral ρ(Tj ) < 1.
 El método de Gauss-Seidel es convergente si y solo si el radio espectral ρ(Tgs ) <
 1.
 Donde:
 ρ(T ) = max(abs(λi )): Radio espectral
 λi es valor propio de T , λi es raíz del polinomio característico: p(λ) = |T − λi I|


Universidad de Ingeniería y Tecnología   Métodos Numéricos            April 20, 2026   22 / 28
Continuación...
  Ejemplo
 Dado el sistema, verificar si el método de Jacobi y Gauss Seidel es convergente:

                                         4x1 + 2x2 + x3  =9
                                         x1 + 5x2 + 3x3  = 14
                                         2x1 + 6x2 + 9x3 = 23

Solución:

 1   A = [4 2 1; 1 5 3; 2 6 9];
 2   op = diagdom(A);
 3   if op == 1
 4        fprintf('El metodo de Jacobi Y Gauss Seidel son convergentes')
 5   else
 6        fprintf('No se puede afirmar nada solo con D.E.D, revisar ...
              radio espectral')
Universidad de Ingeniería y Tecnología           Métodos Numéricos   April 20, 2026   23 / 28
Continuación...
  Ejemplo
 Considere el sistema lineal Ax = b dado por:

                                         10x1 − x2     +2x3                = 6
                                         −x1 + 11x2     −x3 + 3x4 = 25
                                          2x1 − x2    +10x3 − x4 = −11
                                             3x2        −x3 + 8x4 = 15


    1   Calcular las matrices de iteración TJ (Jacobi) y TGS (Gauss-Seidel)
    2   Determinar los radios espectrales ρ(TJ ) y ρ(TGS )
    3   Verificar la convergencia de ambos métodos iterativos

Universidad de Ingeniería y Tecnología                 Métodos Numéricos         April 20, 2026   24 / 28
Solución

 1   A = [ 10 -1 2 0; -1 11 -1 3; 2 -1 10 -1; 0 3 -1 8];
 2   D = diag(diag(A));
 3   L = -tril(A,-1);
 4   U = -triu(A,1);
 5   Tj = inv(D)*(L+U);
 6   Tgs = inv(D-L)*U;
 7   rho_j = max(abs(eig(Tj)))
 8   rho_gs = max(abs(eig(Tgs)))




Universidad de Ingeniería y Tecnología   Métodos Numéricos   April 20, 2026   25 / 28
Actividad
Considere el sistema lineal Ax = b, donde:
                                          
                            1 p 0           1
                    A = 1 1 1 , b = 1 ,                  p, q ∈ R
                            0 q 1           1

   1   Halle las matrices de iteración de los métodos de Jacobi y Gauss-Seidel, en
       términos de p y q.
   2   Para qué valores de p y q el método iterativo de Jacobi presenta
       convergencia? (según el criterio del radio espectral).
   3   Para qué valores de p y q el método iterativo de Gauss-Seidel presenta
       convergencia? (según el criterio del radio espectral).
   4   ¿Existen valores de p y q para los cuales un método converge y el otro
       diverge?

Universidad de Ingeniería y Tecnología   Métodos Numéricos              April 20, 2026   26 / 28
Conclusiones
       La implementación de métodos iterativos requiere descomponer la matriz en
       componentes específicas (diagonal, triangular inferior y superior), asegurando
       flexibilidad para sistemas grandes y dispersos.
       La diagonal dominancia permite evaluar la matriz A para concluir si la
       convergencia podría ocurrir o no se puede afirmar nada, mientras que el radio
       espectral determina si el método converge o diverge.
       Los métodos iterativos tienen amplia aplicabilidad en ingeniería para resolver
       sistemas de ecuaciones lineales, como en análisis estructural, dinámica de
       fluidos y transferencia de calor.




Universidad de Ingeniería y Tecnología    Métodos Numéricos           April 20, 2026   27 / 28
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
