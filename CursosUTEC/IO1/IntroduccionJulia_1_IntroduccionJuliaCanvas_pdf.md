---
curso: IO1
titulo: IntroduccionJulia_1__IntroduccionJuliaCanvas
slides: 17
fuente: IntroduccionJulia_1__IntroduccionJuliaCanvas.pdf
---

                                   IntroduccionJuliaCanvas

                                             April 28, 2025


    1   Introducción al lenguaje Julia
    Fabien Cornillier
    Universidad de Ingeniería y Tecnología – UTEC, Barranco, Lima, Perú
    VISUALIZACION: Utilizar el zoom del navegador Web (Chrome, Safari, etc.) para visualizar
    la totalidad de los slides más cargados!
    Para escribir algo en Julia, podemos utilizar la función println()

[ ]: println("Hola todos!")

    Para obtener información sobre una función en Julia, podemos utilizar el punto de interrogación:

[ ]: ?floor

    Utilizar variables en Julia

[ ]: unaVariable = 110
     typeof(unaVariable)

[ ]: println("El cuadrado de unaVariable es $(unaVariable*unaVariable)")

    Existen diferentes tipos de variables: números enteros, reales, racionales, imaginarios, booleanos,
    cadenas de carácteres, etc.

[ ]: a = 110
     typeof(a)

[ ]: typeof(123.45)

[ ]: typeof(3//4 + 1//2)

[ ]: typeof("Hola mundo!")




                                                    1
    1.1     Estructuras de datos
    1.1.1    Tuplas

[ ]: a = (�, "Hola", 2.34, 10)

[ ]: typeof(�)

    Podemos acceder a un valor en particular de la tupla a:

[ ]: a = (�, "Hola", 2.34, 10)
     a[2]

    En Julia, el primer elemento de una estructura de datos como una tupla o un arreglo se encuentra
    con el índice 1 contrario a otros lenguajes como C o C++ que empiezan con el índice 0.

[ ]: a[1]

    Si intentamos modificar el valor de un elemento de una tupla, Julia genera un mensaje de error:

[ ]: a[2] = "Hello!"

    En Julia, una tupla es inmutable, significa que no podemos cambiar sus valores después de
    definirla.
    Podemos asociar un nombre (una etiqueta) a cada elemento de una tupla:

[ ]: unaPersona = (nombre = "José", telefono = "999877344")

    En este caso, para acceder a un elemento podemos utilizar su etiqueta:

[ ]: unaPersona[:nombre]

[ ]: unaPersona[:telefono]


    1.1.2    Arreglos

[ ]: unArreglo = [1,2,3]

[ ]: typeof(unArreglo)

    Es un arreglo de enteros.
    Podemos crear un arreglo con elementos de diferentes tipos:

[ ]: otroArreglo = [1, "Hola", �]

[ ]: typeof(otroArreglo)

    Creación de arreglo por comprehensión:

[ ]: c = [i^2 for i in 1:5]

    Creación de un rango numérico:

                                                   2
[ ]: rango1 = 10:20
     typeof(10:20)

[ ]: arreglo = collect(rango1)

    Utilizamos un rango para definir un arreglo:

[ ]: arreglo = collect(10:20)

[ ]: typeof(arreglo)

    Otro tipo de rango:

[ ]: arreglo = collect(100:-10:0)

[ ]: arreglo = collect(100:-10:0)

    Agregar un elemento al final de un arreglo:

[ ]: arreglo = [1,2,3]

[ ]: append!(arreglo, 3)

    El punto de exclamación en el nombre de la función push!() es una convención en Julia para
    señalar que la utilización de la función cambia el valor de un argumento. Aquí el argumento
    arreglo cambia.
    Podemos agregar un arreglo al final de otro arreglo:

[ ]: arreglo = [1, "Hello", 3]
     append!(arreglo, [5,"Hola",7])

    Restar el último elemento de un arreglo:

[ ]: arreglo = [2,5,8,6]
     ultimo_valor = pop!(arreglo)

[ ]: println("El valor del último elemento antes de restarlo fue $ultimo_valor.")
     println(arreglo)

    Podemos agregar un elemento al inicio de un arreglo:

[ ]: pushfirst!(arreglo, 0)

    o restar el primer elemento:

[ ]: primero = popfirst!(arreglo)

    Existen varias funciones muy útiles para arreglos. Por ejemplo, tenemos la función sum():

[ ]: sum([i^2 for i in 1:20])

    o length():


                                                    3
[ ]: length(arreglo)

       Ordenar un arreglo:

[ ]: arreglo = [4,7,5,9,1,3,8]

[ ]: ordencreciente(x,y) = (x < y)
     ordendecreciente(x,y) = (x > y)
     sort!(arreglo, lt=ordendecreciente)

[ ]:        arreglo = [(entero = 3, mensaje = "Hola"), (entero = 1, mensaje = "Todos"),␣
         ↪(entero = 2, mensaje = "UTEC")]

[ ]: sort!(arreglo, lt=(x,y)->(x[:entero]<y[:entero]))

       Arreglos de más de una dimensión:

[ ]: arreglo = [(i-j) for i in 1:10, j in 1:10]
     # typeof(arreglo)

       Acceder a un elemento del arreglo:

[ ]: arreglo[1:3,1:4]

       Acceder a todos los elementos de la tercera fila del arreglo:

[ ]: arreglo[3,:]

       Acceder a todos los elementos de la cuarta columna del arreglo:

[ ]: arreglo[:,4]

       Acceder a una parte del arreglo. Ejemplo: acceder a todos los elementos de las columnas 2 a 4.

[ ]: arreglo[:,2:4]

       Obtener el tamaño de un arreglo:

[ ]: (filas, columnas) = size(arreglo)
     println("Tiene $filas filas y $columnas columnas!")

       Crear un arreglo de ceros:

[ ]: vacio = zeros(10, 3)

       Crear un arreglo de unos:

[ ]: muchosunos = ones(10,3)

       Crear un arreglo llenado con cualquier cosa:

[ ]: cualquier = fill(nothing, (10, 3))



                                                         4
[ ]: cualquier2 = fill("Hola", (10, 3))


    1.1.3   Diccionarios
[ ]: function test()
         dico = Dict(i => i^2 for i in 1:10)
         return dico
     end

[ ]: dico = test()

    Contrario a una tupla, podemos cambiar el valor de un elemento de un diccionario:

[ ]: dico[4] = 8

[ ]: dico

    Podemos agregar una nueva entrada en el diccionario:

[ ]: dico["Gimena"]="987345765"

[ ]: dico

    Restar una entrada del diccionario:

[ ]: elemento = pop!(dico, "Maria")

[ ]: dico

[ ]: elemento

    Crear un diccionario vacío para llenarlo después:

[ ]: dico = Dict()

[ ]: dico["José"] = "123456789"

[ ]: dico


    1.1.4   Conjuntos

[ ]: A = [1,3,5,7, 7]
     B = [1,2,4,6,7]

[ ]: Set(A)

[ ]: union(A,B)

[ ]: intersect(A,B)



                                                    5
[ ]: setdiff(B,A)


    1.1.5   Estructuras
[ ]: struct Cliente
         id::Int64
         nombre::String
         edad::Int64
         cuenta::String
     end

[ ]: cliente1 = Cliente(1, "Maria", 28, "1234567890")

[ ]: cliente2 = Cliente(2, "José", 45, "09875")

[ ]: cliente3 = Cliente(3, "Richard", 24, "64334")

[ ]: clientes = [cliente1, cliente2, cliente3]

    Ordenar el arreglo de clientes en orden creciente de edad:

[ ]: sort!(clientes, lt = (x,y)->(x.edad < y.edad))

    Acceder a un campo de una estructura:

[ ]: cliente1.cuenta

    Modificar el número de cuenta del cliente 1:

[ ]: cliente1.cuenta = "987654321"

    No se puede!!! Una estructura es inmutable por defecto!

    1.1.6   Estructuras mutables
[ ]: mutable struct Vendedor
         id::Int64
         nombre::String
         edad::Int64
         tienda::String
     end

[ ]: vendedor1 = Vendedor(1, "José", 45, "Pan de la Chola")

    José decide finalmente trabajar en Napoléon Haute Pâtisserie:

[ ]: vendedor1.tienda = "Napoléon Haute Pâtisserie"

[ ]: vendedor1




                                                    6
    1.2     Estructuras de control
    1.2.1    if… elseif… else… end
[ ]: x = 5
     y = 10

     if x < y
         println("x es menor que y")
     elseif x > y
         println("x es mayor que y")
     else
         println("x es igual a y")
     end

    1.2.2    Expresiones lógicas
      • a == b (devolver true si a es igual a b)
      • a != b (true si a es distinto de b)
      • a < b (true si a es menor que b)
      • a > b (true si a es mayor que b)
      • a <= b (true si a es menor o igual que b)
      • a >= b (true si a es mayor o igual que b)
    Varias expresiones se pueden escribir de manera más simple:

                                operador    símbolo     secuencia teclado
                                     !=        �           \ne+ TAB
                                     <=        �           \le+ TAB
                                     >=        �           \ge+ TAB


    Operador “Y”: &&

[ ]: x = 5
     y = 10
     if (x < y) && (x % 5 == 0)
         println("Excelente!")
     else
         println("Bad!")
     end

    Operador “O”: ||

[ ]: x = 5
     y = 10
     if (x < y) || (x % 5 == 0)
         println("Excelente!")
     else
         println("Bad!")


                                                    7
     end

    Operador “not”: !

[ ]: x = 5
     y = 10
     if !((x < y) || (x % 5 == 0))
         println("Excelente!")
     else
         println("Bad!")
     end

    Se podría reescribir como:

[ ]: x = 5
     y = 10
     if (x � y) && (x % 5 � 0)
         println("Excelente!")
     else
         println("Bad!")
     end


    1.2.3   Averiguar si un elemento está en un conjunto (arreglo, tupla, diccionario, etc.)

[ ]: x = 6
     if x � [1,2,3,4,5]
         println("Super!")
     else
         println("Donde está?")
     end

[ ]: 6 in [1,2,3,4,5]

[ ]: 'A' � "Actualmente"

[ ]: 'A' in "UTEC"


    1.2.4   Averiguar si un conjunto está vacío

[ ]: a = []
     isempty(a)

[ ]: push!(a, "Hola")
     isempty(a)




                                                  8
    1.2.5   Bucle for
[ ]: for i � 1:3
         println("Turno $i")
     end


    1.2.6   Bucle doble
[ ]: for i in 1:3, j in 1:4
         println("Turno $i - Subturno $j")
     end


    1.2.7 for con break
[ ]: for i in 1:3, j in 1:4
         println("Turno $i - Subturno $j")
         if i + j == 6
             break
         end
     end


    1.2.8 for con continue
[ ]: for i in 1:3, j in 1:4
         if i + j == 4
             continue
         end
         println("Turno $i - Subturno $j - Suma:$(i + j)")
     end

    A veces necesitamos iterar sobre el contenido un arreglo con un bucle for utilizando el contador:

[ ]: a = ["Hola", "Cómo", "están?"]
     for palabra in a
         println(palabra)
     end
     enumerate(a)
     # for (k, v) in enumerate(a)
     #     println("Valor del elemento $k: $v")
     # end


    1.2.9   Bucle while
[ ]: valor = 1
     while valor < 100
         println("El valor es igual a $valor")
         valor += valor * 2
     end



                                                    9
    1.3   Operador ternario
[ ]: hora_despegue = 12.5
     hora_llegada_aeropuerto = 13
     if hora_llegada_aeropuerto < hora_despegue
         println("Bienvenida a bordo!")
     else
         println("Has perdido tu vuelo!")
     end
     # (condición ? si verdadero : si falso):
     resultado = (hora_llegada_aeropuerto < hora_despegue ? "Bienvenida a bordo!" :␣
      ↪"Has perdido tu vuelo!")

     println(resultado)


    1.4   Funciones
    Definimos una función cuadrado(x) que retorna el cuadrado de un número x:

[ ]: function cuadrado(x)
         resultado = x^2
         return resultado
     end

    Probamos con números:

[ ]: cuadrado(�) # real irracional

[ ]: cuadrado(10) # entero

[ ]: cuadrado(1im) # número imaginario

[ ]: cuadrado("Hola") # Cadena de carácteres!!!

    Explicación: Una manera de concatenar dos cadenas de carácteres es juntarlas con el operados
    de multiplicación *. Por ejemplo:

[ ]: "Hola " * "todos!"

    Así, cuadrado("Hola") es lo mismo que "Hola" * "Hola".
    Podriamos querer limitar la función cuadrado a cualquier tipo de número:

[ ]: function cuadrado(x::T) where T<:Number
         resultado = x^2
         return resultado
     end

[ ]: cuadrado(9)

[ ]: cuadrado(�)



                                                  10
    Una función puede retornar una tupla, o una tupla nombrada:

[ ]: function minimaxi(x::Vector{T}) where T<:Number
         min = minimum(x)
         max = maximum(x)
         return (valor_minimo = min, valor_maximo = max)
     end

[ ]: resultados = minimaxi([sin(x) for x in -1:0.1:1])

[ ]: resultados.valor_maximo

[ ]: mini, maxi = minimaxi([3,6,1,9,12,4,7])

[ ]: mini

[ ]: maxi

    Dos maneras distintas para definir una misma función:

[ ]: function cuadrado1(numero)
         return numero * numero
     end

[ ]: cuadrado1(3)

[ ]: cuadrado2(numero) = numero * numero

[ ]: cuadrado2(3)


    1.4.1   Función con argumentos con valores por defecto

[1]: function lanzar_dados(numero_dados, caras = 6)
         println("Con dado de $caras caras")
         return [rand(1:caras) for i in 1:numero_dados]
     end

    lanzar_dados (generic function with 2 methods)

[2]: lanzar_dados(3, 8)

    Con dado de 8 caras
    3-element Vector{Int64}:
     5
     7
     4

[3]: lanzar_dados(4)

    Con dado de 6 caras

                                                  11
     4-element Vector{Int64}:
      4
      4
      3
      3

     1.5   Broadcasting
     Podemos aplicar una función a cada elemento de una estructura, por ejemplo un arreglo o una
     tupla:

[4]: cuadrado(x) = x * x

     cuadrado (generic function with 1 method)

[5]: cuadrado.([1,2,3,4,5]) # con arreglo

     5-element Vector{Int64}:
       1
       4
       9
      16
      25

[6]: t = (1,2,3)
     j = cuadrado.(t) # con tupla
     println(t)
     println(j)

     (1, 2, 3)
     (1, 4, 9)
     Se puede también aplicar a los operadores binarios, por ejemplo +, -, *, etc.:

[12]: using LinearAlgebra
      [1,2,3] * [3,2,1]' # [1 x 2, 2 x 2, 3 x 1]

     3×3 Matrix{Int64}:
      3 2 1
      6 4 2
      9 6 3
     Nos damos cuenta que la multiplicación de dos vectores no está definida!
     Para multiplicar los elementos de dos vectores término a término:

[ ]: [1,2,3] .* [3,2,1]

     Podemos utilizar el paquete LinearAlgebra para multiplicar dos vectores:

[ ]: using LinearAlgebra
     a = [1,2,3]


                                                     12
      b = [3,2,1]
      c = a' * b # a' es la transpuesta de a

[ ]: d = a * b'


     1.6   Multiple dispatch
     Definimos una función producto(x,y), la podemos utilizar con cualquier números, enteros, reales,
     imaginarios, racionales, etc., también con cadenas de carácteres:

[13]: function producto(x,y)
          return x * y
      end

     producto (generic function with 1 method)

[14]: producto(10, 5)

     50

[15]: producto("Hola", "todos")

     "Holatodos"
     Sin embargo, esa función no se puede aplicar a vectores, pero podemos definir una función producto
     (con el mismo nombre) para vectores (o arreglos de números en general):

[16]: function producto(x::Array{T}, y::Array{T}) where T<:Number
          return x .* y
      end

     producto (generic function with 2 methods)

[17]: producto(2, 4) # las variables son números, se utiliza la primera versión de la␣
       ↪función producto



     8

[18]: producto([1,2,3,4], [4,3,2,1]) # las variables son arreglos, se utiliza la␣
       ↪segunda versión de la función producto



     4-element Vector{Int64}:
      4
      6
      6
      4

[ ]: # producto([1 2;3 4], [4 3;2 1])
     function producto(x,y)
         return x .* y
     end



                                                    13
      producto((1,2,3), (4,5,6))

     Así podemos utilizar el mismo nombre producto(x,y) para definir funciones distintas!
     Para saber cuales son las diferentes versiones de una función, podemos utilizar la función methods:

[20]: methods(producto)
      #methods(*)

     # 2 methods for generic function "producto" from Main:
      [1] producto(x::Array{T}, y::Array{T}) where T<:Number
          @ ~/Documents/GitHub/CursoInvestigacionOperaciones/TutorialJulia/
      ↪IntroduccionJuliaCanvas.ipynb:1

      [2] producto(x, y)
          @ ~/Documents/GitHub/CursoInvestigacionOperaciones/TutorialJulia/
      ↪IntroduccionJuliaCanvas.ipynb:1


     También podemos saber cual versión se utiliza en casos específicos con @which:

[21]: @which producto(�, 100)

     producto(x, y)
          @ Main ~/Documents/GitHub/CursoInvestigacionOperaciones/TutorialJulia/
      ↪IntroduccionJuliaCanvas.ipynb:1


[22]: @which producto("Hola", "UTEC")

     producto(x, y)
          @ Main ~/Documents/GitHub/CursoInvestigacionOperaciones/TutorialJulia/
      ↪IntroduccionJuliaCanvas.ipynb:1


[23]: @which producto([1,2,3,4], [4,3,2,1])

     producto(x::Array{T}, y::Array{T}) where T<:Number
          @ Main ~/Documents/GitHub/CursoInvestigacionOperaciones/TutorialJulia/
      ↪IntroduccionJuliaCanvas.ipynb:1


[24]: @which producto([1 2;3 4], [4 3;2 1])

     producto(x::Array{T}, y::Array{T}) where T<:Number
          @ Main ~/Documents/GitHub/CursoInvestigacionOperaciones/TutorialJulia/
      ↪IntroduccionJuliaCanvas.ipynb:1



     1.7   Funciones utiles: map, reduce, mapreduce, filter

     2 map
     La función map permite aplicar una función sobre cada elemento de una estructura:

 [ ]: map(x -> x * 2, [1,2,3,4,5])




                                                     14
     x -> x * 2 es una función anónima, está definida sin nombre solamente para ser utilizada en la
     función map.

     2.0.1 reduce
     Aplicamos un operador binario (entre dos variables) entre cada elemento de un “conjunto” de
     elementos. Por exemplo:

[28]: reduce(^, 3:-1:1)

     9
     es equivalente a 1 × 2 × 3 × ⋯ × 20, o también:

[ ]: factorial(20)


     2.0.2 mapreduce
     Podemos aplicar una función específica a cada elemento antes de aplicar un operador binario entre
     cada elemento:

[ ]: mapreduce(x -> x * 2, +, [1,2,3,4])

     sería equivalente a (1 × 2) + (2 × 2) + (3 × 2) + (4 × 2).

     2.0.3 filter
     Podemos filtrar elementos de un “conjunto”. Por ejemplo, filtrar todos los números enteros múltiples
     de 5 entre 1 y 20:

[29]: a = filter(x -> (x % 5 == 0), 1:20)
      println(a)

     [5, 10, 15, 20]
     Existe también una versión de esa función que modifica el arreglo (con el !):

[30]: b = collect(1:20)
      println("Antes: $b")
      filter!(x -> (x % 5 == 0), b)
      println("Después: $b")

     Antes: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
     Después: [5, 10, 15, 20]

     2.1   Duplicar arreglos
[31]: a = [1, 2, 3]
      b = a
      a .*= 10; # multiplicamos por 10 cada elemento del arreglo a
      #a = a .* 10



                                                       15
     3-element Vector{Int64}:
      10
      20
      30
     Chequeamos los valores del areglo b, y… tenemos un problema!

[32]: b

     3-element Vector{Int64}:
      10
      20
      30
     Si cambiamos los valores de a, cambiamos también los valores de b!
     Explicación: Podemos ver a y b como punteros (en el sentido de C o C++). Cuando hacemos b
     = a, hacemos que b apunte al arreglo a. En este caso, ambos a y b apuntan al mismo arreglo!
     Podemos evitar esa situación con la función copy():

[35]: a = [1, 2, 3]
      b = copy(a)
      a .*= 10;

[36]: b

     3-element Vector{Int64}:
      1
      2
      3
     Pero…

[37]: a = [1, 2, 3]
      b = [4, 5, 6]
      c = [7, 8, 9]
      arreglo1 = [a, b, c]
      arreglo2 = copy(arreglo1)
      a .*= 10;

[ ]: arreglo1

[ ]: arreglo2

     Tenemos otro problema! El primer elemento del arreglo2 también está multiplicado por 10…
     Podemos evitar esa nueva situación con la función deepcopy():

[ ]: a = [1, 2, 3]
     b = [4, 5, 6]
     c = [7, 8, 9]



                                                   16
     arreglo1 = [a, b, c]
     arreglo2 = deepcopy(arreglo1)
     a .*= 10;

[ ]: arreglo1

[ ]: arreglo2

    Explicación: La función deepcopy() hace una copia “profunda”, es decir que duplica cada el-
    emento, que sea una variable simple, un arreglo, una tupla o un diccionario, y eso de manera
    recursiva. Al contrario, la función copy() sólo hace una copia de los elementos simples, pero sólo
    copia el puntero que apunta a una estructura compleja de datos (arreglo, tupla, diccionario, etc.),
    no copia el objeto apuntado.


    3    ¿Donde encontrar más información?
        • Documentación oficial de Julia: https://docs.julialang.org/en/v1
        • Una excelente introducción a Julia (más o menos 1 hora): https://juliaacademy.com/p/intro-
          to-julia
        • Otra buena introducción de 2022 (3 horas): https://youtu.be/uiQpwMQZBTA
        • Otros tutoriales interesantes: https://juliaacademy.com/
        • Practicar Julia con ejercicio y mentoring gratis (excelente!): https://exercism.org/tracks/julia
        • Manual oficial: https://docs.julialang.org/en/v1/manual/getting-started/
        • Cuando tenemos una pregunta de programación, casi siempre otros programadores han tenido
          la misma pregunta antes. Un excelente sitio para encontrar las respuestas a las preguntas
          más comunes es stackoverflow: https://stackoverflow.com/questions/tagged/julia




                                                      17
