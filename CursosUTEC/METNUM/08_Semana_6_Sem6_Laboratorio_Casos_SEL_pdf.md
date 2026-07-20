---
curso: METNUM
titulo: 08 - Semana 6/Sem6_Laboratorio Casos SEL
slides: 33
fuente: 08 - Semana 6/Sem6_Laboratorio Casos SEL.pdf
---

Métodos Numéricos
Lab. Valores Propios
S6
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
                                         1 Valores propios y aplica-
                                            ciones




Universidad de Ingeniería y Tecnología    Métodos Numéricos            1 / 32
        Objetivos
            Implementar rutinas en MATLAB para resolver ecuaciones y sistemas no
            lineales incorporando criterios de parada y generación automática de reportes
            de convergencia.




Universidad de Ingeniería y Tecnología            Métodos Numéricos                         2 / 32
    VALORES

1   PROPIOS Y
    APLICACIONES
Valores propios
Recordar, si A ∈ Rn×n decimos que λ es un valor propio, si existe v ̸= 0 de modo
que:

                                         Av = λv

Para encontrar los valores propios de una matriz (estos pueden ser reales o
complejos) se sigue:
   1   Formar el polinomio característico asociado a la matriz A, de la siguiente
       manera:
                                    p(λ) = det(A − λI),
       donde I es la identidad de orden n.
   2   Las raíces de p(λ) nos da los valores propios de la matriz A.
   3   Al resolver Av = λv , obteníamos los vectores propios asociados a λ.

Universidad de Ingeniería y Tecnología         Métodos Numéricos                    4 / 32
Ejemplo
Usando MATLAB, encontrar los valores propios de la siguiente matriz:
                                               
                                 4/5 −3/5 0
                           A = 3/5 4/5 0
                                  1      2    2

Con el comando eig(A) MATLAB nos devuelve los valores y vectores propios:

 1   format short
 2   A = [4/5 -3/5 0; 3/5 4/5 0; 1 2 2];
 3   [V,D] = eig(A)




Universidad de Ingeniería y Tecnología     Métodos Numéricos                5 / 32
...Continuación
Ejecutando el código en MatLab obtenemos:




Universidad de Ingeniería y Tecnología   Métodos Numéricos   6 / 32
Localización de Valores y Vectores propios
  Teorema (Gershgorin)
 Cada valor propio λ ∈ C de la matriz real An×n satisface alguna de las desigual-
 dades:                            X
                      |λ − Aii | ≤   Aij , i ∈ {1, 2, . . . , n}
                                         j̸=i

Por ejemplo, para n = 3:
                        
          a11 a12 a13                           D1 = {z ∈ C : |z − a11 | ≤ |a12 | + |a13 |}
     A = a21 a22 a23                          D2 = {z ∈ C : |z − a22 | ≤ |a21 | + |a23 |}
          a31 a32 a33                           D3 = {z ∈ C : |z − a33 | ≤ |a31 | + |a32 |}

Luego, si λ es un valor propio de A entonces λ ∈ Di para algún i = 1, 2, 3.


Universidad de Ingeniería y Tecnología                 Métodos Numéricos                      7 / 32
Código MATLAB

 1   function []=gershgorin(A)
 2       [m,n]=size(A);
 3       figure(1); clf;
 4       for j=1:n
 5           %(h;k) centro de la circunferencia
 6           h=A(j,j); k=0;
 7           r=sum(abs(A(j,:)))-abs(A(j,j));
 8           theta=[0:0.01:2*pi];
 9           xx=r*cos(theta)+h;
10           yy=r*sin(theta)+k;
11           figure(1);
12           plot(xx,yy,'LineWidth',2); hold on;
13       end
14       set(gca,'FontSize',14, 'FontName', 'Courier')
15       grid on
16   end

Universidad de Ingeniería y Tecnología   Métodos Numéricos   8 / 32
Usando MATLAB
  Ejemplo (1)
 Localizar los valores propios de la matriz:
                                             
                                       −4 0 1
                                 A =  1 0 1
                                        1 1 5

 Explique los resultados obtenidos con MATLAB.


 1   A = [-4 0 1; 1 0 1; 1 1 5];
 2   gershgorin(A)




Universidad de Ingeniería y Tecnología   Métodos Numéricos   9 / 32
Usando MATLAB
       2

       1

       0

     -1

     -2
       -6                -4              -2   0        2              4   6   8

Comente sobre la ubicación de los valores propios. Luego confirme usando la
función eig de MATLAB.



Universidad de Ingeniería y Tecnología            Métodos Numéricos           10 / 32
Usando MATLAB
  Ejemplo (2)
 Localizar los valores propios de la matriz:
                                             
                                       −3 1 1
                                 A =  1 0 1
                                        1 1 5

 Explique los resultados obtenidos con MATLAB.


 1   A = [-3 1 1; 1 0 1; 1 1 5];
 2   gershgorin(A)




Universidad de Ingeniería y Tecnología   Métodos Numéricos   11 / 32
Usando MATLAB
         2

         1

         0

       -1

       -2
         -6                -4            -2   0       2               4   6   8

Comente sobre la ubicación de los valores propios. Luego confirme usando la
función eig de MATLAB.



Universidad de Ingeniería y Tecnología            Métodos Numéricos               12 / 32
Usando MATLAB
  Ejemplo (3)
 Localizar los valores propios de la matriz:
                                                
                                   −3/4 1/16 1/8
                             T =  1/8 −1/4 1/8
                                   −1/4 1/4 1/3

 Explique los resultados obtenidos con MATLAB.


 1   T = [-3/4 1/16 1/8; 1/8 -1/4 1/8; -1/4 1/4 1/3];
 2   gershgorin(T)




Universidad de Ingeniería y Tecnología   Métodos Numéricos   13 / 32
Usando MATLAB
                            0.5




                               0




                           -0.5
                               -1        -0.5   0            0.5    1


Comente sobre la ubicación de los valores propios. Luego confirme usando la
función eig de MATLAB. En caso de que se trate de la matriz de iteraciones T,
¿podría concluir sobre la convergencia del método iterativo?


Universidad de Ingeniería y Tecnología          Métodos Numéricos          14 / 32
Aplicación: El Algoritmo "PageRank"
       Califica páginas indexadas de acuerdo a su “importancia” dentro de la red.
       Marca registrada de Google.
       Lleva su nombre debido a su inventor Larry Page.




Universidad de Ingeniería y Tecnología       Métodos Numéricos                  15 / 32
El Modelo "PageRank"
El universo de páginas de internet públicas es un gran grafo dirigido donde:
    Cada página web es un nodo.
    Hay una arista orientada entre páginas que citan a otras páginas.




Universidad de Ingeniería y Tecnología     Métodos Numéricos                   16 / 32
La importancia de una página web
Es alta si:
       La citan muchas páginas.
       La citan páginas “importantes”.




Universidad de Ingeniería y Tecnología   Métodos Numéricos   17 / 32
Ejemplo de 5 páginas de internet (Algoritmo de
PageRank)




Universidad de Ingeniería y Tecnología   Métodos Numéricos   18 / 32
Continuación...
aij = 1 si la página j tiene un link a la página i, y aij = 0 en otro caso
                                                        
                                        0 1 0 1 1
                                      0 0 1 1 1
                                                        
                                  A= 1 0 0 1 0
                                                         
                                      0 0 0 0 1
                                        0 0 1 0 0
Asociar la clasificación ri a la página i de tal manera que ri > rj indique que la
página está mejor clasificada que la página j.
Se requiere que:
                                               0 ≤ ri ≤ 1

y
                                         r1 + r2 + . . . + r5 = 1

Universidad de Ingeniería y Tecnología                  Métodos Numéricos            19 / 32

Continuación...
Definamos el vector de clasificación:
                                                   
                                                   r1
                                                  r2 
                                                   
                                                  r3 
                                               r =   
                                                  r4 
                                                   r5
Además, insistimos en que la clasificación ri de la página i debe ser proporcional a
la suma de las clasificaciones de las páginas que enlazan con la página i:
                                         r1 = α (r2 + r4 + r5 ) ,
donde α es una constante,
                                         r2 = α (r5 + r3 + r4 )
                                         r3 = α (r1 + r4 )
                                         r4 = α (r5 )
Universidad de Ingeniería y Tecnología   r = α (r ) Métodos Numéricos           20 / 32
Continuación...
Notación Matricial
                                                                                            
          r1 = α (r2 + r4 + r5 )                                        0      1   0   1   1 r1
          r2 = α (r5 + r3 + r4 )                                       0
                                                                              0   1   1     r2 
                                                                                           1  
          r3 = α (r1 + r4 )                        →              r = α
                                                                       1      0   0   1      r3 
                                                                                           0 
                                                                                                 
          r4 = α (r5 )                                                 0      0   0   0   1 r4 
          r5 = α (r3 )                                                  0      0   1   0   0 r5

Haciendo λ = α1 :

                                         r = αAr       →        Ar = λr

Así obtenemos un problema de valores y vectores propios.


Universidad de Ingeniería y Tecnología                     Métodos Numéricos                          21 / 32
Usando MatLab

 1   %Resolviendo problemas de valores y vectores propios
 2   %para el vector de clasificacion r
 3   clc
 4   A=[0 1 0 1 1;0 0 1 1 1 ; 1 0 0 1 0;0 0 0 0 1;0 0 1 0 0]
 5   [Q,D]=eig(A)
 6   %El primer valor es el unico real, ese es el que necesitamos
 7   evals=diag(D)
 8   vp1=evals(1)
 9   %Encontramos la constante de proporcionalidad alpha
10   alpha=1/vp1
11   %Encontramos el vector r como vector propio correspondiente al
12   %primer valor propio
13   r=Q(:,1)
14   %Normalizando el vector de clasificacion
15   r=r/sum(r)



Universidad de Ingeniería y Tecnología   Métodos Numéricos            22 / 32
Aproximación de Valores y Vectores Propios
Método de la Potencia: Matlab



 1   function [z]=potencia(A,x0,Maxiter)
 2   z=[x0' 1];
 3   for k=1:Maxiter
 4       y1=A*x0;
 5       [maxi,pos]=max(abs(y1));
 6       u=y1(pos); % valor propio
 7       x1=y1/u; %vector propio normalizado
 8       z=[z;x1' u];
 9       x0=x1;
10   end




Universidad de Ingeniería y Tecnología   Métodos Numéricos   23 / 32
Ejemplo
Aproximar el valor propio dominante de la siguiente matriz.
                                              
                                       2 −12
                                 A=
                                       1 −5

Considere el vector inicial X (0) = [1; 1]




Universidad de Ingeniería y Tecnología       Métodos Numéricos   24 / 32
Método de descomposición QR
El método estima los valores propios de una matriz cuadrada An×n . En condiciones
adecuadas, este algoritmo produce una sucesión de matrices, todas similares o
semejantes a A (las matrices semejantes tienen los mismos valores propios).
La idea del método es la siguiente:
   1   Factorizar A = Q1 R1 usando la forma de Gram - Schmidt.
   2   Del paso anterior, los factores se intercambian para formar A1 = R1 Q1 , que se
       factoriza usando la forma de Gram - Schmidt como A1 = Q2 R2 .
   3   La siguiente iteración es formar A2 = R2 Q2 y factorizarla. Y así sucesivamente.
Observaciones:
       La sucesión A, A1 , A2 , . . . , An convergerá a una matriz triangular (o casi) que
       almacenará los valores propios.
       La cantidad de iteraciones debe ser alta para convergencia.


Universidad de Ingeniería y Tecnología           Métodos Numéricos                     25 / 32
Método QR de Gram - Schmidt (álgebra lineal)

 1   function [Q R] = gs_c(A)
 2       [m,n] = size(A);
 3       Q = zeros(m,n);
 4       R = zeros(n);
 5       for j = 1:n
 6           R(1:j-1,j) = Q(:,1:j-1)'*A(:,j);
 7           temp = A(:,j) - Q(:,1:j-1)*R(1:j-1,j);
 8           R(j,j) = norm(temp);
 9           Q(:,j) = temp/R(j,j);
10       end
11   end




Universidad de Ingeniería y Tecnología   Métodos Numéricos   26 / 32
Ejemplo 1:
Caso real: Encuentre
                     una aproximación a los valores propios de
      1 −1 4
A = 3 2 −1, de manera anticipada sabemos que los valores propios son
      2 1 −1
λ1 = 3; λ2 = −2; λ3 = 1.

 1   A = [1 -1 4; 3 2 -1; 2 1 -1]; % ingresamos A
 2   [V D] = eig(A) % calculamos los valores y vectores propios usando eig
 3   T = A;
 4   iter = 500; % efectuamos 500 iteraciones
 5   for i = 1:iter
 6       [Q1 R1] = gs_c(T); % la funcion gs_c factoriza QR usando G-S
 7       T = R1*Q1;
 8   end
 9   T


Universidad de Ingeniería y Tecnología   Métodos Numéricos              27 / 32
Resultado:
La matriz T es una matriz triangular (o casi) donde los valores propios se
almacenan en la diagonal:




Universidad de Ingeniería y Tecnología     Métodos Numéricos                 28 / 32
Ejemplo 2:
Caso complejo: Encuentre una aproximación a los valores propios de
                   
      4/5 −3/5 0
A = 3/5 4/5 0, de manera anticipada sabemos que los valores propios son
       1     2    2
λ1 = 2, λ2 = 5 , λ3 = 4−3i
            4+3i
                       5 .

 1   A = [4/5 -3/5 0; 3/5 4/5 0; 1 2 2]; % ingresamos A
 2   T = A;
 3   iter = 500; % efectuamos 500 iteraciones
 4   for i = 1:iter
 5       [Q1 R1] = gs_c(T); % la funcion gs_c factoriza QR usando G-S
 6       T = R1*Q1;
 7   end
 8   T % el elemento T(1,1) nos dara el valor real
 9   B = T(2:3,2:3) % el bloque nos dara los v.p restantes
10   v = eig(B)


Universidad de Ingeniería y Tecnología   Métodos Numéricos              29 / 32
Ejecución en Matlab




Universidad de Ingeniería y Tecnología   Métodos Numéricos   30 / 32
Conclusiones
       Los valores propios son fundamentales para resolver problemas reales, como
       el algoritmo PageRank, que clasifica nodos según su importancia relativa.
       El Teorema de Gershgorin localiza los valores propios dentro de discos
       definidos por los elementos diagonales y las sumas de los elementos no
       diagonales de la matriz.
       El método de la potencia encuentra el valor propio dominante, fundamental
       para la convergencia en métodos iterativos y análisis de estabilidad en
       sistemas dinámicos.




Universidad de Ingeniería y Tecnología      Métodos Numéricos                   31 / 32
Gracias

<!-- vision-pendiente: deck sin figuras (ensamblado texto-primero) -->
