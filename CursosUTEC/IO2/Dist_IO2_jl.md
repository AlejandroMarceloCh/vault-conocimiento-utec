---
curso: IO2
titulo: Dist_IO2
slides: 0
fuente: Dist_IO2.jl
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: Dist_IO2.jl. -->

<!-- INTERPRETAR: código fuente (Dist_IO2.jl). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

```jl
### A Pluto.jl notebook ###
# v0.17.2

using Markdown
using InteractiveUtils

# This Pluto notebook uses @bind for interactivity. When running this notebook outside of Pluto, the following 'mock version' of @bind gives bound variables a default value (instead of an error).
macro bind(def, element)
    quote
        local iv = try Base.loaded_modules[Base.PkgId(Base.UUID("6e696c72-6542-2067-7265-42206c756150"), "AbstractPlutoDingetjes")].Bonds.initial_value catch; b -> missing; end
        local el = $(esc(element))
        global $(esc(def)) = Core.applicable(Base.get, el) ? Base.get(el) : iv(el)
        el
    end
end

# ╔═╡ 8b95a76c-8648-4295-9f2a-e9ce7e30f4e1
using PlutoUI, Plots, Distributions, DataFrames, StatsPlots

# ╔═╡ 3ade6cff-a9ac-4e1b-8c2b-9468a7476424
md"# Notebook Interactivo de Modelos discretos y continuos univariados"

# ╔═╡ 11d405ba-3f72-4155-930c-2720449d1f71
md"""

## Set up

En este notebook exploraremos distribuciones, podrás explorar entre la **teoría,  casos de aplicación y ejercicios**.  Para hacerlo más interesante, descubrirás que esta diseñado para ser **interactivo** y lo más intuitivo posible. Disfrútalo ✨

Por Alexia Berenice Torres Calderon para el Departemento de Ingeniería Industrial UTEC

Para poder utilizarlo:

1. Descarga e instala la última versión estable de Julia correspondiente a tu sistema operativo en el siguiente [enlace](https://julialang.org/downloads/#current_stable_release).

2. Abre la aplicación la aplicación de Julia y añade Pluto:

```julia
julia> ]
(@v1.x) pkg> add Pluto
```

3. Abre Pluto

```julia
julia> import Pluto
julia> Pluto.run() 
```


Y listo! Abrirá una pestaña en tu navegador predeterminado (`http://localhost:1234`).


"""

# ╔═╡ fb931c1d-3de4-489c-96d7-a69bb14fd1b2
PlutoUI.TableOfContents()

# ╔═╡ d0ae819a-d96a-4715-86f0-e6e480d0714b
begin
	function plot_cumulative!(ps, δ=1; label="")
	    
	    cumulative = cumsum(ps)
		
	
	    ys = [0; reduce(vcat, [ [cumulative[n], cumulative[n]] for n in 1:length(ps) ])]
	  
	    pop!(ys)
	    pushfirst!(ys,0)
		push!(ys,1)
	
	    xs = [-1; reduce(vcat, [ [n*δ, n*δ] for n in 0:length(ps)-1])];
		push!(xs,length(ps))
	
	    plot!(xs, ys, label=label, color=:black)
	
	    scatter!([n*δ for n in 0:length(ps)-1], cumulative, label="")
	end
	
	function TeoricBarplot( distribution, xmin, n_x_values, ylim=1;auto=false, geo=0)
		
		xvalues=[i for i in xmin:(xmin+n_x_values-1)]
		probs=[pdf(distribution, i) for i in xmin-geo:(xmin+n_x_values-1)-geo]
		
		if auto ==true 
		plot((xvalues, probs),seriestype =:bar, leg=false, 
	        ylabel="Probabilidad", xlabel="Valores de v.a X", xticks=xvalues, alpha = 0.5)
		
		else 
			plot((xvalues, probs),seriestype =:bar, leg=false, 
	        ylabel="Probabilidad", xlabel="Valores de v.a X", xticks=xvalues, ylims=(0,ylim+0.1), alpha = 0.5)
		end
		
	end
	
	RandomBinomial(p,N)=sum([rand()<p for i in 1:N]);
	

function plot_cumulative2!(ps, δ=1; label="")
	    
	    cumulative = cumsum(ps)

    ys = [0; reduce(vcat, [ [cumulative[n], cumulative[n]] for n in 1:length(ps) ])]

    pop!(ys)
    pushfirst!(ys, 0)

    xs = [0; reduce(vcat, [ [n*δ, n*δ] for n in 1:length(ps)])];

    plot!(xs, ys, label=label)
    scatter!([n*δ for n in 1:length(ps)], cumulative, label="")
	end
	
		function counts(data)
    d=Dict{Int64,Int64}()
    for i in data
        if haskey(d,i)
            d[i]+=1
            else 
            d[i]=1
        end
    end
    ks=collect(keys(d))
    vs=collect(values(d))
    p=sortperm(ks)
    
return ks[p],vs[p]
end
	
	function Canvas_Ber(lims,  N::Int64=0)
	    max=lims[end]
	    number_bins=length(lims)
	    data=[]
	    
	    p = plot(xlim=(0,max),ylim=(0,1), w=3, labels=false, ticks=false, showaxis=false, title= "Espacio muestral", xlabel="Negativo a COVID                 |                 Positivo a COVID");
		
	    
		vspan!(p,[lims[1],lims[2]], alpha = 0.2, labels = false);
		vspan!(p,[lims[2],lims[3]], alpha = 0.2, labels = false);
	    
	    return p
	end
	
	function ComparissonPlot(data, distribution; geo=0)
	
	Teorico=plot(minimum(data)-geo:1:maximum(data), x-> pdf(distribution,x), seriestype=:bar, leg=false)
	Empirico= plot(counts(data), seriestype=:bar, leg=false)
	plot(Teorico, Empirico,layout=2, title=["Teórico" "Empírico"])
	
end
	
end;


# ╔═╡ aacc06b4-1afb-4e83-8392-45b2e24eb51a
md"# _Distribuciones Discretas_"

# ╔═╡ efd9c782-f1af-4b37-823f-e1a8e606f434
md" 

## Distribución Bernoulli 

### Caso Introductorio

Entenderemos la distribución Bernoulli con un expermiento. En sala de recuperación de pacientes COVID de un hospital, se toman pruebas diarias a los pacientes para evaluar si aún presentan el virus o pueden ser dados de alta. Nosotros queremos simular el escenario de un día de un paciente. ¿Cómo hacemos esto? Consideraremos que existe una probabilidad de recuperación constante en el tiempo y le daremos un valor. Puedes usar el slider para cambiar este valor: " 

# ╔═╡ 91357e08-3a1c-41b3-9c03-1d839c3222ec

	@bind Prob Slider(0:0.05:1, default=0.25, show_value=true)

# ╔═╡ 05342071-26c0-40c4-8c7f-ff074595c6d7
md" Ya tenemos la probabilidad de recuperación, ahora simulemos la toma de la prueba. A continuacion se muestra la funcion que hará esto."

# ╔═╡ 39f0ce2f-650a-43f5-9129-0e1f4d70c215
function Prueba_Covid(p) #p es la probabilidad de recuperación
	
	prueba=rand()
	
	if prueba < p
		return "Negativo" , prueba
	else return "Positivo", prueba
	end
end

# ╔═╡ ae42451e-8ba3-47c2-8dfc-6c82cc0f7f7b
md" Presiona el boton para llamar a la función"

# ╔═╡ 450c7626-fb30-4b15-8bab-ed326698d958
@bind resultado Button("Toma la prueba COVID")

# ╔═╡ 1309cdd1-8346-4645-9156-58923aa8afed
begin
	Prueba=Prueba_Covid(Prob)
	begin resultado
		cuadro=1
		if Prueba[1]=="Positivo"
		Markdown.parse("`Resultado:  "*Prueba[1]*" a COVID-19 | El paciente no se recuperó`")
		else 
			Markdown.parse("`Resultado:  "*Prueba[1]*" a COVID-19  | El paciente se recuperó`")
		end
	end
end

# ╔═╡ 6ac7b024-ec4a-41c2-bb9b-8b3fe8c40021
md" Visualiza el espacio muestral al cambiar el valor de la probabilidad de recuperación y la aleatoriedad del experimento. "

# ╔═╡ 1cc0d686-cf69-443b-94e7-1c311b7c02ab
begin
	
	if cuadro==1
	Canvas_Ber([0,Prob,1])
	scatter!([Prueba[2]], rand(1), ms=7, labels=false, color="black", legend=false)
	end
end

# ╔═╡ bbe31497-8b9c-4d6e-87b5-d0adf2bc8f5a
md"
###### Este es un experimento Bernoulli. ¡Es así de simple! 
Tenemos solo dos posibles resultados: un éxito y un fracaso.
La probabilidad con la que trabajamos es la de obtener éxito.
En nuestro ejemplo, la probabilidad que consideramos fue la de recuperarse y salir negativo a COVID, entonces, el **éxito fue asignado a este valor**. Definamos el experimento:

Experimento = Tomar la prueba COVID

Espacio muestral = [Positivo, Negativo]

Probabilidad de exito (Haberse Recuperado) = $Prob

Variable aleatoria = Estado del paciente segun la prueba realizada

Imagen de la variable aleatoria = [Sé recuperó, No se recuperó]"

# ╔═╡ 2580129c-f92b-4ec3-a415-6d685f97111f
md"
---
### Más casos

###### Lanzamiento de una moneda
Tirar una moneda es probablemente el ejemplo de un experiemento Bernoulli más usado. Esta vez la probabilidad de exito es 0.5.

En este caso, asignaremos el éxito como obtener una cara."


# ╔═╡ 3e1b4956-7986-4835-bd11-4985ced5ab6a
@bind Moneda Button("Tira la moneda")

# ╔═╡ 3a9666e9-b549-4038-887a-4142b24af61e

begin Moneda
	rand() < 0.5 ? Resource("https://imgur.com/oiBrxLj.jpg", :width=>100) : 							Resource("https://imgur.com/lsIfpdt.jpg", :width=>100)
end


# ╔═╡ 2573ea72-8716-4575-90db-e533a59bde14
md""" 
Experimento = Lanzar la moneda

Espacio muestral = [Cara, Sello]

Probabilidad de exito (Cara) = 0.5

Variable aleatoria = Resultado del lanzamiento

""" 

# ╔═╡ 5cf627ef-0c52-4e11-862a-de04f233f6be
md" 
---
### Exploremos la teoría del Modelo "

# ╔═╡ 141f72b9-c606-4871-b374-db1076b520f6
md"###### La variable aleatoria X ~ _Bernoulli(p)_, se distribuye Bernoulli parámetro p


Donde p= probabilidad de éxito"

# ╔═╡ 289d89e7-3b25-4f9d-b86f-156db859801c
md"Entonces, el modelo Bernoulli describe un experimento que tiene **sólo dos resultados posibles**. Uno que llamaremos **éxito** y el otro, **fracaso**. El modelo Bernoulli utiliza el parámetro **_p_**, que representa la **probabilidad de éxito**."

# ╔═╡ 502d45d4-ec81-4b3f-8e4b-ce708843af4d
md" ##### Exploremos su función de probabilidad de masa:

$$\begin{align*}

f(x)=P(X = x) = \begin{cases} p & \text{de tomar el valor } 1\\
1-p & \text{de tomar el valor } 0\end{cases}\\
\end{align*}$$"

# ╔═╡ 32a96882-eec2-4da6-b765-591fb72e7d33
md"  💡**Nota:** Decir que tomará valor `1` **si es un éxito** o `0` **si obtenemos un fracaso**, nos ayuda a generalizar el resultado. Por ejemplo, en el caso de lanzar la moneda, ya que defininimos el éxito como obtener cara, este valor sería representado por **1** y sello estaría representado por **0**."

# ╔═╡ 8549a117-88a6-4e38-a99d-5bb6d66647a6
md"Puedes mover el slider de la probabilidad para explorar la función de probabilidad de masa en su forma gráfica:"

# ╔═╡ 086b52fb-24e8-4e5a-9a00-3d568cea960f
md"Probabilidad de éxito (p): $(@bind P Slider(0:0.1:1; default=0.5, show_value=true))"

# ╔═╡ 5843e3ad-d3b4-4ee1-aa96-dc2f6734d57c
TeoricBarplot(Bernoulli(P),0,2)

# ╔═╡ 37302c26-5411-4e62-9c14-b3536628d6f8
md" ##### Exploremos su función de distribución acumulativa: "

# ╔═╡ eb08ffb6-faf4-44cf-a03a-f698c314df0c
md"
$$\begin{align*}
&F(x) = P(X \leq x)= \begin{cases} 0 & 
\text{si } x<0\\ 1-p & \text{si } 0\leq x < 1\\ 1 & \text{si } x \geq 1 
\end{cases}\\
\end{align*}$$"

# ╔═╡ 0193bc92-9fdd-49ff-b63c-71230af0f036
md"Puedes mover el slider de la probabilidad para ver la funcion de distribución de probabilidad en su forma gráfica:"

# ╔═╡ b34bef02-5d88-4648-b3fa-3e06fb06f434
@bind P1 Slider(0:0.1:1; default=0.5, show_value=true)

# ╔═╡ 788be74d-10e4-49ff-b6c4-0de59d38a7cc
begin
	 	
		TeoricBarplot(Bernoulli(P1),0,2)
		plot_cumulative!([1-P1, P1],label="")
	
end

# ╔═╡ 01512d62-9e0a-4332-9376-80faca75cc3e
md"
---
### Resumen Teórico"

# ╔═╡ a06b18f7-002d-4fa7-85f1-3800aab7dc9d
md"

$$\begin{align*}
&X = \begin{cases} 1 & \text{con probabilidad  } p\\
0 & \text{con probabilidad  } 1-p\end{cases}\\
&F(x) = \begin{cases} 0 & 
\text{si } x<0\\ 1-p & \text{si } 0\leq x < 1\\ 1 & \text{si } x \geq 1 
\end{cases}\\
&E(X)=0(1-p) + 1 (p)=p\\
&Var(X)=p(1-p)
\end{align*}$$
"

# ╔═╡ dbc6dee1-b373-419a-bfb0-60a7b95447e3
md" 
---

## Distribución Binomial

### Caso Introductorio

Entenderemos la distribución Binomial con un caso en el mismo hospital. Para el hospital es informacion valiosísima saber las probabilidades de cuantos de sus pacientes podrán ser dados de alta en un día. Para eso, debemos simular la recuperación diaria de todos sus pacientes. Ellos albergan a 100 pacientes COVID en sus instalaciones. ¿Cómo hacemos esto? Para empezar, **defininamos algunos parámetros:**"

# ╔═╡ 0fba673c-614c-4948-9889-140f4eebfbf3
md"- Número de pruebas diarias:"

# ╔═╡ 5aa0b173-f415-4157-a17b-dcf7cb07b79b

	@bind bin_pruebas NumberField(0:200, default=100)


# ╔═╡ 04f47231-7396-4c72-ac20-4fa02212c383
md" - Probabilidad de que una persona se recupere y salga negativo:"

# ╔═╡ 30f405b7-fc11-4857-b144-ee88e0b0717c
	@bind bin_prob Slider(0:0.05:1, default=0.25, show_value=true)

# ╔═╡ ef8e069f-c3de-4643-aa33-4c3fb594ccdb
md" 
💡 Recuerda que el notebook es interactivo y puedes cambiar los valores para hacer más pruebas"

# ╔═╡ 2cf03f51-d574-4efe-9546-32907e66852a
md"Podemos considerar la toma de la prueba entre personas como eventos independientes. Esto significa que estamos considerando que el progreso de un paciente no afecta en otros.

Entonces utilizaremos la función que creamos en el experimento bernoulli que simula la recuperación de un paciente en un día y la repetiremos el numero de pacientes que se encuentran en el hospital:
"

# ╔═╡ 6ce28ce9-26f1-479a-b093-1e8a61ca16f5
function Toma_de_Pruebas_Diaria(n,p)
	
	# n representa el numero de pruebas a realizar
	#p representa la probabilidad de que una de esas pruebas salga positivo
	
	registro_pacientes=[Prueba_Covid(p)[1] for i in 1:n]
	
	return registro_pacientes
end

# ╔═╡ f3e6a555-3d38-4325-afbf-5ff8dc0e3c52
md"Presiona el botón para simular las pruebas"

# ╔═╡ 6ee9a581-0b61-4f87-8d48-6769dc0d25b1
@bind bin_dia Button("Simula un día de pruebas")

# ╔═╡ e724289a-bbc2-4752-9904-d69845457540
begin bin_dia
	
	bin_registro=DataFrame(Pacientes=["Paciente"*string(i) for i in 1:bin_pruebas], Resultado=Toma_de_Pruebas_Diaria(bin_pruebas,bin_prob))
    bin_registro
end

# ╔═╡ 63b6571d-4021-438a-8cfe-bf4a3944e8cb
begin
	result_bin_dia=sum(bin_registro[!,2].=="Negativo")
	Markdown.parse("`Total de Negativos en un día:  "*string(result_bin_dia)*" | Pacientes Recuperados`")

end

# ╔═╡ a794d0e0-5598-446a-b37f-4bbced8c0254
md" En este día el número de pacientes recuperados es $result_bin_dia. Vuelve a presionar el botón para apreciar la aletoriedad del expermiento. Tambien, puedes jugar con el valor de la probabilidad y el número de pacientes.

###### Este es un experimento Binomial. ¡Es así de simple! 
Se repite **_n_** veces de manera independiente un **experimento Bernoulli** parámetro **_p_**, y se **reporta el número de éxitos** obtenidos. Ahora, definamos el experimento:

Experimento = Tomar $bin_pruebas pruebas COVID

Espacio muestral = [:Todas las combinaciones posibles]

Variable aleatoria = $X$ : Número de negativos de un total de $bin_pruebas pruebas tomadas en un dia

$ X ~ Bin( $bin_pruebas, $bin_prob) $

"

# ╔═╡ 0de8e1b6-8eac-4a5a-83b4-3313916e34e7
md"
###### Ahora repitamos el experimento muchas veces para observar su aleatoriedad y compararlo con la teoría de la distribución Binomial:

- Ingresa el número de repeticiones que deseas observar:"

# ╔═╡ 188171e4-f6e3-4847-83ff-d85cb1677562
@bind bin_rep  NumberField(0:200, default=100)

# ╔═╡ cbb87f4d-573e-4ea0-8182-4a69d3401eab
md"💡 Recomendación: Prueba repitiendolo 10 veces, aumenta a 100, a 1000, a 10000 y así para que observes lo que ocurre."

# ╔═╡ 0449916f-0d03-42c5-8f6d-61bb15064305
begin 
	data=[RandomBinomial(bin_prob, bin_rep) for i in 1:bin_rep];
	ComparissonPlot(data, Binomial(bin_rep, bin_prob))
end

# ╔═╡ 116140ef-907c-4b59-9238-93d9674f1233
md" Como podemos ver, mientras más veces repetimos el experimento, hay mayor parecido en las graficas. Exploremos la teoría detras de esto para entender un poco mejor. "

# ╔═╡ d09a3d1e-9e20-4197-ad4b-cdd63fae6772
md"
---
### Exploremos la teoría
"


# ╔═╡ b00c3786-23a6-468a-b960-8e560e38695e
md"###### La variable aleatoria X ~ _Binomial (p,N)_, se distribuye Bernoulli parámetro p, N

Donde:

**_p_** = probabilidad de éxito del experimento Bernoulli 

**_N_** = número de repeticiones

**_X_** cuenta la cantidad de éxitos de un total de **_N_** experimentos Bernoulli parámetro **_p_**
"


# ╔═╡ ba22e820-9c8c-485c-8205-9c2e64108842
md"
###### Función de probabilidad de masa:
$$\begin{align*}
& P(X=k)=\binom{n}{k}p^{k}(1-p)^{n-k}\\ 
&k=0,1,2,\ldots , n\\
\end{align*}$$"

# ╔═╡ 778f2336-fea5-41bf-ae80-e0fca9a84678
md" Mueve los slider y observa que cambios ocurren al alterar cada parámetro"

# ╔═╡ 3c4a347d-b8a5-4b83-a48e-460e8ddcac76
@bind bin_slidern1 Slider(0:20; default=10, show_value=true)

# ╔═╡ 81ce007c-359e-407b-8f93-82428048c974
@bind bin_sliderp1 Slider(0:0.1:1; default=0.5, show_value=true)

# ╔═╡ 51f0acab-0cf4-431d-a756-85f47a95a46b

TeoricBarplot(Binomial(bin_slidern1,bin_sliderp1),1,10)


# ╔═╡ 62fa4585-9438-49cb-843d-5242d62f0271
md" ##### Exploremos su función de distribución acumulativa: "

# ╔═╡ f4389c9a-6173-4678-8dbe-f8f132de23fe
md"""
$$\begin{align*}

&F(x)\equiv P(X\leq x)=\sum_{k\leq x}\binom{n}{k}p^k(1-p)^{n-k}\\
&\forall x\in \mathbb{R}\\
\end{align*}$$"""


# ╔═╡ 90f96e72-8c73-4511-8354-c41ba2cf6953
begin
	pdf_bin= [pdf(Binomial(bin_slidern1, bin_sliderp1), i) for i in 1:bin_slidern1]
	plot_cumulative2!(pdf_bin, label="")
end

# ╔═╡ e7c54ff8-5fbb-49a5-84d6-1f426e472f1c
md"
---
### Resumen Teórico

$$\begin{align*}
& P(X=k)=\binom{n}{k}p^{k}(1-p)^{n-k}\\ 
&k=0,1,2,\ldots , n\\
&F(x)\equiv P(X\leq x)=\sum_{k\leq x}\binom{n}{k}p^k(1-p)^{n-k}\\
&\forall x\in \mathbb{R}\\
\end{align*}$$"

# ╔═╡ 07f5624f-260f-4738-8616-a4c6f74cf7c0
md" 
---

## Distribución Geométrica

### Caso Introductorio

Entenderemos la distribución Geométrica con un caso en el mismo hospital. Queremos saber probabilidades de cuantos días pasará un paciente de COVID en el hospital. Esta es información importante tanto para los pacientes como para el planeamiento de recursos del hospital. Entonces, ¿cómo podemos estudiar estas probabilidades? Simularemos esta situación. Recordemos que estamos considerando la probabilidad de recuperación diaria como constante en el tiempo. Definamos este parámetro:

"

# ╔═╡ c590ff79-7ae2-4b94-9981-52e94d56e8ff
	@bind geo_prob Slider(0:0.05:1, default=0.25, show_value=true)

# ╔═╡ 1468cf1d-9d4b-45fa-897a-bfeecd51772c
md" ¿Cómo podemos saber el tiempo que estará un paciente en el hospital, si contamos con la probabilidad diaria de que sea dado de alta y deje las intalaciones? 

Debemos contar la cantidad de días que se tome la prueba hasta que esta salga negativo y pueda ser dado de alta. Entonces, escribamos una función que nos permita hacer eso: "

# ╔═╡ 38f5ac07-f21d-4792-8966-1bc92b4d7ef0
function dias_Recuperacion(p)
    dias=0
    estado="Positivo"
    while estado=="Positivo"
        estado=Prueba_Covid(p)[1]
        dias+=1
    end
    return dias
end

# ╔═╡ 8496b0d6-12b9-4728-bc91-c5b8f56ea739
@bind geo_boton Button("Simula estadía de un paciente")

# ╔═╡ 453c9c94-c56c-4208-9171-e9244cc94295
begin geo_boton
	
	geo_dias= dias_Recuperacion(geo_prob)
	Markdown.parse("`Días hasta recuperación:  "*string(geo_dias)*"`")
	
end

# ╔═╡ 3f07ba26-441c-4c21-a139-3adf298d765b
md" Puedes presionar el botón varias veces para apreciar la aleatoriedad del experimento"

# ╔═╡ 145e4c65-9e3b-4c8b-9c40-f41892fc9d7c
md"
###### Ahora repitamos el experimento muchas veces para observar su aleatoriedad y compararlo con la teoría de la distribución Geometrica:
"

# ╔═╡ ee30e1f0-9f93-4af6-b51e-4df0de63afad
md"Ingresa el número de repeticiones que deseas observar: $(@bind geo_rep  NumberField(0:200, default=100))"

# ╔═╡ e7340cda-92b7-4496-a47b-a733cc2a59b9
md"💡 Recomendación: Prueba repitiendolo 10 veces, aumenta a 100, a 1000, a 10000 y así para que observes lo que ocurre."

# ╔═╡ bb984796-fb9f-4f93-81c8-629d1107c52e
begin
	data_geo=[dias_Recuperacion(geo_prob) for i in 1:geo_rep]
	ComparissonPlot(data_geo, Geometric(geo_prob), geo=1)
	
end

# ╔═╡ c009f68e-9d39-4d41-8f47-0620ddae717c
md" Como podemos ver, mientras más veces repetimos el experimento, hay mayor parecido en las gráficas. Exploremos la teoría detras de esto para entender un poco mejor."

# ╔═╡ 8048479d-5a08-401b-a1a0-b7c501b82927
#Markdown.parse("`Promedio días de recuperación:  "*string(mean(data_geo))*"`")

# ╔═╡ 514df2eb-a1f9-4665-927c-7d74aa2f1505
md"
---
### Exploremos la teoría
"


# ╔═╡ 603d216a-0ec9-4631-ad5a-0dc1221b4a0d
md"###### La variable aleatoria X ~ _Geométrica (p)_, se distribuye Geométrica parámetro **_p_**

Donde p = probabilidad de éxito del experimento Bernoulli 

**_X_** cuenta la cantidad de repeticiones que debo de hacer de un experimento Bernoulli parámetro **_p_** hasta obtener el primer éxito

p es constante en el tiempo!!!
"


# ╔═╡ d9ea4012-45ee-4baf-bf4f-a2b0ec71b69c
md"
###### Función de probabilidad de masa:
$$
\begin{align*}
&P(X=k)=(1-p)^{k-1}p\\
&k=1,2\ldots\\
\end{align*}$$"

# ╔═╡ 7c63a28c-9599-44eb-a144-45ec2eff4dfb
md"Mueve el slider para cambiar el valor de p"

# ╔═╡ f72fd27b-3f9a-4f3f-a412-71b37797d4dd
@bind geo_prob2 Slider(0:0.05:1, default=0.5, show_value=true)

# ╔═╡ 81ba5f86-6762-4b8f-ba64-a4779c7c65d1
TeoricBarplot(Geometric(geo_prob2),1,20, 0.35, auto=true, geo=1)

# ╔═╡ 23eead02-a4bd-43b3-9dfb-0f83a9acc3ef
md"
###### Función de distribuacion acumulada:
$$
\begin{align*}
&F(x)\equiv P(X\leq x)=\sum_{k\leq x}(1-p)^{k-1}p\\
&\forall x\in \mathbb{R}
\end{align*}$$"

# ╔═╡ 21a292db-3871-4133-8396-67e5ebc1c509
begin
	TeoricBarplot(Geometric(geo_prob2),1, 20,1, geo=1)
	pdf_geo= [pdf(Geometric(geo_prob2), i) for i in 0:20]
	plot_cumulative2!(pdf_geo, label="")
end

# ╔═╡ 0b4e7950-5e5b-4056-987e-c6d93546bd48
md"
---
### Resumen Teórico

$$
\begin{align*}
&P(X=k)=(1-p)^{k-1}p\\
&k=1,2\ldots\\
&F(x)\equiv P(X\leq x)=\sum_{k\leq x}(1-p)^{k-1}p\\
&\forall x\in \mathbb{R}\\
&E(X)=\sum_{k=1}^\infty 
kp(k)= \sum_{k=1}^\infty k(1-p)^{k-1}p=\frac{1}{p}\\
&Var(X)=\frac{1-p}{p^2}\\
\end{align*}$$"

# ╔═╡ e4399d37-e193-4d64-9280-6356cb84fb71
md"## Distribución Poisson

Caso Introductorio:

Entenderemos la distribución Poisson simulando las llegadas de Pacientes COVID al hospital. Entonces, diremos el número de llegadas en un día se distribuye Poisson parámetro λ, donde λ es el valor esperado de llegadas diarias.

"

# ╔═╡ 8fd03ee5-78d1-495b-ae4c-6d01235cb6a6
md"*λ = 10*"

# ╔═╡ 35319d90-67ca-48a3-b04d-db0d9853a59d
md"""
¿Cuantas días deseas simluar? = $(@bind n_poiss NumberField(0:200, default=1))
"""

# ╔═╡ d231762e-fb25-45f3-bb1c-6dc06392959c
@bind run_poiss Button("Simula llegadas")

# ╔═╡ f61f9db3-b6a5-4dbf-a195-3d9cb3cbf9b3
md"
---
### Exploremos la teoría
"

# ╔═╡ aa287c53-48ea-4bc6-98be-309b6e89785d
md"
###### La variable aleatoria X ~ _Poisson(λ)_, se distribuye Poisson parámetro **_λ_**

Donde λ = valor esperado de X

X cuenta en una unidad de tiempo cuantos eventos ocurren

**_X_** en el caso general, cuenta la cantidad de eventos en una unidad de tiempo


Diremos que un evento $S$ es un evento Poisson si ocurre en el tiempo obedeciendo a los siguientes principios:

1. **Independencia de incrementos de tiempo disjuntos.** Es decir, el número de veces que $S$ ocurre en un intervalo de tiempo es independiente del número de veces que ocurre en cualquier otro intervalo de tiempo disjunto a éste.

2. **Los eventos no ocurren en grupos.** Es decir, la probabilidad de que haya dos o más ocurrencias de eventos en un intervalo de tiempo muy pequeño es cero.

3. **La tasa de llegada es constante.** El número promedio de llegadas por unidad de tiempo es constante e igual a $\lambda$. No cambia en el tiempo."

# ╔═╡ 8903b303-2926-4064-9a58-d9d6329883fd

md"
###### Función de probabilidad de masa:
$P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!} 
\quad x=0,1,2\ldots$"



# ╔═╡ 44674e1a-e2ae-415a-802d-740751cd0949
md"Mueve el slider para cambiar el valor del parámetro"

# ╔═╡ ae6a2835-6b02-4e7f-986a-e5ccfc728f93
@bind poiss_lambda Slider(0:1:100, default=20, show_value=true)

# ╔═╡ 75dfb55f-9737-4286-b093-4992f87e346d
begin run_poiss
	[rand(Poisson(poiss_lambda)) for i in 1:n_poiss]
end

# ╔═╡ a5fff464-9b3e-4cdd-9cf9-332736269ff7
plot(Poisson(poiss_lambda), seriestype=:bar, legend=false)

# ╔═╡ 153ad89f-de01-4963-91cb-fe2c2b842eb9
md"
###### Función de distribución acumulada:
$F(x)=P(X\leq x)=\sum_{k=0}^{\left\lfloor
x\right\rfloor}\frac{e^{-\lambda}\lambda^k}{k!}$"

# ╔═╡ 9092b7a7-d5bd-45bc-99a1-19f545aacb1d
begin
	TeoricBarplot(Poisson(poiss_lambda),0 , 1.7*poiss_lambda , 0.9)
	pdf_poiss= [pdf(Poisson(poiss_lambda), i) for i in 0: 1.7*poiss_lambda]
	plot_cumulative2!(pdf_poiss, label="")
end

# ╔═╡ 7b4b1265-83af-42c6-86dc-70126460bfde
md"
---
### Resumen Teórico


$\text{f.p.m.} \quad P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!} 
\quad x=0,1,2\ldots$

$\text{f.d.a.} \quad F(x)=P(X\leq x)=\sum_{k=0}^{\left\lfloor
x\right\rfloor}\frac{e^{-\lambda}\lambda^k}{k!}$

$E(X)=\sum_{k=0}^\infty 
k\frac{e^{-\lambda}\lambda^k}{k!}=\sum_{k=1}^\infty 
k\frac{e^{-\lambda}\lambda^{k-1}\lambda}{(k-1)!}=\lambda 
e^{-\lambda}e^\lambda=\lambda$

$Var(X)=\lambda$
"

# ╔═╡ 9c00f83b-e97a-42ec-bc7f-5c95138d100f
md"""
# Distribuciones continuas
"""

# ╔═╡ a015fdca-02e6-44ab-912d-e3c1efec2eef
md"Introducción al tiempo continuo:"

# ╔═╡ 4c5b357e-d4c5-4f72-8b35-bbd1824da232
md"""
p = $(@bind p Slider(0.1:0.05:1, default=.2, show_value=true))
"""

# ╔═╡ 6c1c43e7-96d9-4c70-bc95-dfe683d4af7e
md"""
N = $(@bind N Slider(10:10:100, default=20, show_value=true))
"""

# ╔═╡ be5a0d38-f24b-40ac-92a0-faf9e608024e
md"""
δ = $(@bind δ Slider(0.1:0.05:1, default=1, show_value=true))
"""

# ╔═╡ 296f430f-7129-4d8f-84b2-6c398efb4ebe
begin
	continua_pdf(p, N) = [p * (1 - p)^(n-1) for n in 1:N]
	plot()
	plot_cumulative!(continua_pdf(p, N), 1, label="delta = 1")
	plot_cumulative!(continua_pdf(p, N), δ, label="delta = $(δ)")
end

# ╔═╡ 5e7de748-ad79-4aff-a1fb-040c8099d0b1
md"
###### Función de distribución acumulativa:
$$
F(x)\equiv P(X\leq x)=\int_{-\infty}^x f(t)dt \quad \forall x\in \mathbb{R}$$

Propiedades:

$$
\begin{align*}
& 0\leq F(x)\leq 1 \quad \forall x\in \mathbb{R}\\\\
& F(-\infty)\equiv \lim_{x\rightarrow -\infty}F(x)=0\\\\
& F(+\infty)\equiv \lim_{x\rightarrow \infty}F(x)=1\\\\
& F \text{ es una función  no decreciente}\\\\
& F \text{ es una función continua}
\end{align*}$$"

# ╔═╡ 4ccca494-91ef-4b11-831a-d4229e1eb5c5
md"###### Función de densidad

Dada una variable aleatioria continua $X$, su función de **densidad de probabilidad** permite calcular probabilidades asociadas a la variable aleatoria $X$ y además satisface las siguientes propiedades:

$$
\begin{align*}
&f(x) \geq 0\\\\
&\int_{-\infty}^{+\infty}f(x)dx=1\\\\
\end{align*}
$$


Algunas observaciones
$$
\begin{align*}
&P(X=a)=\int_a^af(x)dx=0\\
&\int_{a}^{b}f(x)dx=P(a\leq X\leq b)\\\\
\end{align*}$$"

# ╔═╡ f73f3507-03ac-4957-9cba-082b61d462ef
md"## Distribución uniforme"

# ╔═╡ 9b7feb58-6779-4137-aacd-200caec77965
md"💡: Simulemos una variable aleatoria continua, para entender estos conceptos. Lo haremos con la siguiente función:"

# ╔═╡ d8633435-5c37-4d78-89da-001efbfa6829
uniform(a, b) = a + rand() * (b - a);

# ╔═╡ ef25478e-e577-4e3c-8de8-df0f4de115e3
@bind datos_unif NumberField(0:200, default=100)

# ╔═╡ 1e6dff27-ccba-48c8-b015-411b334e63bb
md"Mínimo (a): $(@bind unif_min NumberField(0:200, default=0))"

# ╔═╡ 4c25ea05-a4b0-4cb3-98f0-b19ffb75f2a8
md"Máximo (b): $(@bind unif_max NumberField(0:200, default=1))"

# ╔═╡ 8fbc2beb-1655-4bd9-8003-ee4865f37e52
data_unif = [uniform(unif_min, unif_max) for i in 1:datos_unif]

# ╔═╡ 91e6d916-bf2e-4565-b408-b5669b30fe80
#P(X=15.568756) =0

#=
Casos Favorables/ Casos Totales


1/inf =0 
=#

# ╔═╡ 8c993fe9-2719-4825-adf7-fc07c43b349d
begin
	
	histogram(data_unif,nbins=20, legend=false)  # function in Plots.jl
	scatter!(data_unif, zero.(data_unif), ms=2, alpha=0.3)
end

# ╔═╡ c0c22c1f-7508-40bd-bda7-afaeda8d58b2
md"
---
### Exploremos la teoría

Parametros de la uniforme = a,b
"

# ╔═╡ 607711f0-d4bf-44ae-a7b9-06aadd057b63
md"""###### La variable aleatoria X ~ _Uniforme(a,b)_, se distribuye Uniforme parámetro **_a_**, **_b_**

Donde :

###### **_a_** = Mínimo del rango de valores de X
	 
###### **_b_**= Máximo del rango de valores de X
"""


# ╔═╡ 8e7dba6d-8f35-47d8-afda-2c36d1313a4a
md"
###### Función de densidad de probabilidad:
$$
\begin{align*}
f(x) &= \begin{cases}
\frac{1}{b - a} & \text{ si } a \leq x \leq b \\\\ 
              0 & \text{ fuera }\\\\
        \end{cases}
\end{align*}$$"

# ╔═╡ 93c6323a-7dac-4174-aea5-139cc38283f4
md"Mínimo (a): $(@bind a NumberField(0:200, default=0))"

# ╔═╡ 61a15261-b13f-46a5-9a01-3c18d0245e23
md"Máximo (b): $(@bind b NumberField(0:200, default=5))"

# ╔═╡ e9b56895-7ea0-4ac6-90df-4b77bfa30e02
begin
	plot(vcat([a-0.2,a],[ i+0.1 for i in a-0.1:0.1:b-0.1],[b,b+0.2]), vcat([0,0],[pdf(Uniform(a,b),i) for i in a:0.1:b],[0,0]), legend=false, ylims=(0,2), yticks= [1/b-a], linewidth=3)
end

# ╔═╡ 877346f2-d025-4330-adaa-7585af22a653
md"
###### Función de distribución acumulada:
$$
\begin{align*}
F(x) \equiv & P(X\leq x)= \int_{a}^{x}\frac{1}{b-a}dt\\\\
          = & \begin{cases}
                0 & \text{ si } x < a\\\\
                \frac{x-a}{b - a} & \text{ si } a \leq x \leq b\\\\
                1 & \text{ si } x > b
              \end{cases}
\end{align*}$$"

# ╔═╡ 18cfedaa-67af-4b96-8dd5-fe7173c47ffa
plot!([a,b],[0,1], linewidth=3)

# ╔═╡ bfb3dc19-2d4c-43f4-84f0-fdeffcf2fb61
md"
## Exponencial

Posibles aplicaciones del modelo exponencial:

1. La longitud de los intervalos de tiempo que transcurren entre dos sucesos consecutivos de la variable aleatoria discreta Poisson parámetro $\lambda$. Así como el parámetro de la Poisson representa el número de llegadas por unidad de tiempo, el parámetro de la exponencial tiene unidades del inverso del tiempo.

2. El tiempo transcurrido en un centro de llamadas hasta recibir la primera llamada del día.

3. El intervalo de tiempo entre terremotos de una determinada magnitud.

4. El tiempo de vida de un componente electrónico."

# ╔═╡ 50a8398c-792a-4d2b-9899-4dafaa188c24
md"
---
### Exploremos la teoría

###### La variable aleatoria X ~ _Exponencial(λ)_, se distribuye Exponencial parámetro **_λ_**


Donde :

###### **_λ_** = 1/E(x)

###### Función de densidad de probabilidad:
$$
\begin{align*}
f(x) =& \begin{cases}
\lambda e^{-\lambda x} & \text{ si } x\geq 0\\\\
0 \quad & \text{ si } x<0
\end{cases}
\end{align*}$$"

# ╔═╡ d237deda-a25d-45d3-817a-7019dd0dd15c
md"""
λ = $(@bind λ Slider(0:0.1:1, default=0.5, show_value=true))
"""

# ╔═╡ f48ab57e-5ca7-4be8-af30-a6626dd9ed40
begin
	plot()
	
	plot(Exponential(1/λ), linewidth=2,legend=false)
	
end

# ╔═╡ 7828063d-2948-4562-bf4a-78a47f763040
md"
###### Función de de distribución acumulada:
$$
\begin{align*}
F(x)\equiv& P(X\leq x)= \int_0^x\lambda e^{-\lambda t}dt\\\\
         =& \begin{cases}
1-e^{-\lambda x} &  \text{ si } x \geq 0\\\\
0 &  \text{ si } x < 0 \\\\
\end{cases}
\end{align*}$$"

# ╔═╡ e9939368-a08f-4994-a823-c1b6b72b9814
md"""
Evalúa la probabilidad de X ≤  $(@bind try_exp NumberField(0:200, default=1) )
"""

# ╔═╡ b6dd8143-2486-47b9-899d-710bf2180e2a
begin try_exp
	plot()
	plot(Exponential(1/λ), linewidth=2,legend=false)
	range = 0:0.1:try_exp;
	plot!(0:0.1:10/λ, x->cdf(Exponential(1/λ),x), legend=false, linewidth=2, color=:red)
	plot!(range, x->pdf(Exponential(1/λ),x), fill=true, alpha=0.4, legend=false)
end

# ╔═╡ e2362438-85c6-48ff-b842-9d1be1b38eaf
md"
---
### Resumen Teórico


$$
\begin{align*}

f(x) =& \begin{cases}
\lambda e^{-\lambda x} & \text{ si } x\geq 0\\\\
0 \quad & \text{ si } x<0
\end{cases}\\


F(x)\equiv& P(X\leq x)
         = \begin{cases}
1-e^{-\lambda x} &  \text{ si } x \geq 0\\\\
0 &  \text{ si } x < 0 \\\\
\end{cases}\\

E(X)=&\int_{0}^{\infty}x\lambda e^{-\lambda x}= \frac{1}{\lambda}\\\\
Var(X)\equiv & E(X^{2})-E^{2}(X)=\\\\
            =& \int_{0}^{\infty}x^{2}\lambda e^{-\lambda x}-\left(\int_{0}^{\infty}x\lambda e^{-\lambda x}\right)^{2}\\\\
            =&\frac{1}{\lambda^{2}}
\end{align*}$$"

# ╔═╡ 6fe18bac-716d-459c-a19a-c429fb96e199
md"## Distribucion normal"

# ╔═╡ d685f0c8-c242-40af-a0bd-be0f8154fb9b
md"##### Normal(μ =1, σ=0)  vs  Normal(μ, σ)

Normal estándar vs Normal con diferentes parámetros

###### La variable aleatoria X ~ _Normal(μ, σ)_, se distribuye Normal parámetro **_μ_**, **_σ_**


Donde :

###### **_μ_** = es la media de X 
###### **_σ_** = es la desviación de X "

# ╔═╡ bd25ad8a-5b8a-4a03-9305-94e87005b288
md""" μ = $(@bind μ Slider(0:1:50, default=0, show_value=true)) """

# ╔═╡ 1e8bb19b-cec6-4eb2-9f5f-2d47485c1e83
md""" σ = $(@bind σ1 Slider(1:1:50, default=1, show_value=true)) """

# ╔═╡ 22670544-e631-4ebb-8bdb-9c6bf28f9c33
begin
	plot()
	plot!(Normal(), fill=(0, .3, :blue), label = "media = 0 ; sd = 1")
	plot!(Normal(μ, σ1), fill=(0, .3, :green), label = "media = $(μ) ; sd = $(σ1)")
end

# ╔═╡ 09715306-246e-433f-9909-a9ee69b7d010

md"
---
### Exploremos la teoría
"

# ╔═╡ 6626a65f-59ca-40b1-9f8c-de50e490af9c
md"###### La variable aleatoria X ~ _Normal(μ, σ)_, se distribuye Normal parámetro **_μ_**, **_σ_**


Donde :

###### **_μ_** = es la media de X 
###### **_σ_** = es la desviación de X "

# ╔═╡ bcca6c59-34da-40e8-aa8b-12f4fe8514a2
md"


###### Función de densidad de probabilidad:
$$
f(x)=\frac{1}{\sqrt{2\pi} \sigma} e^{\frac{-(x-\mu)^2}{2\sigma^2}} \text{ para } -\infty < x < +\infty$$"

# ╔═╡ f77643c0-5d88-4c18-88e9-0b1a1878656a
md"""
μ = $(@bind mean_norm NumberField(0:200, default=0) )
"""

# ╔═╡ 6bb57b4f-88e6-4b9f-b233-a9ddf19486b1
md"""
σ = $(@bind mean_des NumberField(0:200, default=1) )
"""

# ╔═╡ c68d80bc-5fba-46b9-85e2-6711c21a2478
begin
	plot(Normal(mean_norm,mean_des), fill=(0, .5,:lightblue))	
	vline!([mean_norm], color=:red, linewidth= 3 )
	vline!([mean_norm+mean_des],color=:green, linewidth= 3 )
	vline!([mean_norm-mean_des],color=:green, linewidth= 3, legend=false )
end

# ╔═╡ 56ab33eb-b6a7-4471-b498-67dd7a8d8a6e
begin
	#=plot(Normal(mean_norm,mean_des), fill=(0, .5,:lightblue))	
	plot!(0:0.1:30, x-> cdf(Normal(mean_norm,mean_des),x), legend=false)=#
end

# ╔═╡ d19137e6-07cd-4149-bfd7-77fb3dbecdba
md"
---
### Resumen Teórico

$$
\begin{align*}
&f(x)=\frac{1}{\sqrt{2\pi} \sigma} e^{\frac{-(x-\mu)^2}{2\sigma^2}} \text{ para } -\infty < x < +\infty\\
&E(X)=\mu\\
&V(X)=\sigma^{2}
\end{align*}$$"


# ╔═╡ 4714c1b3-faf8-4ade-8a4b-2359bb0b2bb4
test_data = [rand(Normal(11,3)) for i in 1:1000]

# ╔═╡ 742f5961-f239-4f97-bf90-d792f551edcf
begin
	scatter(test_data, legend=false)
end

# ╔═╡ db0032c5-4c5c-430e-bf31-988f90adf32e
begin
	hline!([11], linewidth= 3)
	hline!([11-3], linewidth= 3, color=:purple)
	hline!([11+3], linewidth= 3, color=:purple)
end

# ╔═╡ 4c6855a3-d121-40e5-96a6-6b06335762d1
squared_difference = [(dato - mean(test_data))^2 for dato in test_data]

# ╔═╡ 24a69164-7dbc-4c82-87c9-451417290b5e
varianza = mean(squared_difference)

# ╔═╡ e0450f6b-537f-4236-879d-54a4cdf9deb7
md"---
### Comandos evaluar normal en R
```julia
dnorm(x, mean=0, sd=1) #Calcula P(X=x) para una normal estandar
pnorm(x, mean=0, sd=1) #Calcula P(X<=x) para una normal estandar
pnorm(x, mean=0, sd=1, lower.tail = FALSE) #Calcula P(X>=x) para una normal estandar
qnorm(0.95, mean=0, sd=1, lower.tail=TRUE) #Calcula X dado que le das una prob (p) de ser para una normal estandar
```"

# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
DataFrames = "a93c6f00-e57d-5684-b7b6-d8193f3e46c0"
Distributions = "31c24e10-a181-5473-b8eb-7969acd0382f"
Plots = "91a5bcdd-55d7-5caf-9e0b-520d859cae80"
PlutoUI = "7f904dfe-b85e-4ff6-b463-dae2292396a8"
StatsPlots = "f3b207a7-027a-5e70-b257-86293d7955fd"

[compat]
DataFrames = "~1.2.2"
Distributions = "~0.25.16"
Plots = "~1.21.3"
PlutoUI = "~0.7.9"
StatsPlots = "~0.14.27"
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

[[AbstractFFTs]]
deps = ["LinearAlgebra"]
git-tree-sha1 = "485ee0867925449198280d4af84bdb46a2a404d0"
uuid = "621f4979-c628-5d54-868e-fcf4e3e8185c"
version = "1.0.1"

[[Adapt]]
deps = ["LinearAlgebra"]
git-tree-sha1 = "84918055d15b3114ede17ac6a7182f68870c16f7"
uuid = "79e6a3ab-5dfb-504d-930d-738a2a938a0e"
version = "3.3.1"

[[ArgTools]]
uuid = "0dad84c5-d112-42e6-8d28-ef12dabb789f"

[[Arpack]]
deps = ["Arpack_jll", "Libdl", "LinearAlgebra"]
git-tree-sha1 = "2ff92b71ba1747c5fdd541f8fc87736d82f40ec9"
uuid = "7d9fca2a-8960-54d3-9f78-7d1dccf2cb97"
version = "0.4.0"

[[Arpack_jll]]
deps = ["Libdl", "OpenBLAS_jll", "Pkg"]
git-tree-sha1 = "e214a9b9bd1b4e1b4f15b22c0994862b66af7ff7"
uuid = "68821587-b530-5797-8361-c406ea357684"
version = "3.5.0+3"

[[Artifacts]]
uuid = "56f22d72-fd6d-98f1-02f0-08ddc0907c33"

[[AxisAlgorithms]]
deps = ["LinearAlgebra", "Random", "SparseArrays", "WoodburyMatrices"]
git-tree-sha1 = "a4d07a1c313392a77042855df46c5f534076fab9"
uuid = "13072b0f-2c55-5437-9ae7-d433b7a33950"
version = "1.0.0"

[[Base64]]
uuid = "2a0f44e3-6c83-55bd-87e4-b1978d98bd5f"

[[Bzip2_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "19a35467a82e236ff51bc17a3a44b69ef35185a2"
uuid = "6e34b625-4abd-537c-b88f-471c36dfa7a0"
version = "1.0.8+0"

[[Cairo_jll]]
deps = ["Artifacts", "Bzip2_jll", "Fontconfig_jll", "FreeType2_jll", "Glib_jll", "JLLWrappers", "LZO_jll", "Libdl", "Pixman_jll", "Pkg", "Xorg_libXext_jll", "Xorg_libXrender_jll", "Zlib_jll", "libpng_jll"]
git-tree-sha1 = "4b859a208b2397a7a623a03449e4636bdb17bcf2"
uuid = "83423d85-b0ee-5818-9007-b63ccbeb887a"
version = "1.16.1+1"

[[ChainRulesCore]]
deps = ["Compat", "LinearAlgebra", "SparseArrays"]
git-tree-sha1 = "30ee06de5ff870b45c78f529a6b093b3323256a3"
uuid = "d360d2e6-b24c-11e9-a2a3-2a2ae2dbcce4"
version = "1.3.1"

[[Clustering]]
deps = ["Distances", "LinearAlgebra", "NearestNeighbors", "Printf", "SparseArrays", "Statistics", "StatsBase"]
git-tree-sha1 = "75479b7df4167267d75294d14b58244695beb2ac"
uuid = "aaaa29a8-35af-508c-8bc3-b662a17a0fe5"
version = "0.14.2"

[[ColorSchemes]]
deps = ["ColorTypes", "Colors", "FixedPointNumbers", "Random"]
git-tree-sha1 = "9995eb3977fbf67b86d0a0a0508e83017ded03f2"
uuid = "35d6a980-a343-548e-a6ea-1d62b119f2f4"
version = "3.14.0"

[[ColorTypes]]
deps = ["FixedPointNumbers", "Random"]
git-tree-sha1 = "024fe24d83e4a5bf5fc80501a314ce0d1aa35597"
uuid = "3da002f7-5984-5a60-b8a6-cbb66c0b333f"
version = "0.11.0"

[[Colors]]
deps = ["ColorTypes", "FixedPointNumbers", "Reexport"]
git-tree-sha1 = "417b0ed7b8b838aa6ca0a87aadf1bb9eb111ce40"
uuid = "5ae59095-9a9b-59fe-a467-6f913c188581"
version = "0.12.8"

[[Compat]]
deps = ["Base64", "Dates", "DelimitedFiles", "Distributed", "InteractiveUtils", "LibGit2", "Libdl", "LinearAlgebra", "Markdown", "Mmap", "Pkg", "Printf", "REPL", "Random", "SHA", "Serialization", "SharedArrays", "Sockets", "SparseArrays", "Statistics", "Test", "UUIDs", "Unicode"]
git-tree-sha1 = "6071cb87be6a444ac75fdbf51b8e7273808ce62f"
uuid = "34da2185-b29b-5c13-b0c7-acf172513d20"
version = "3.35.0"

[[CompilerSupportLibraries_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "e66e0078-7015-5450-92f7-15fbd957f2ae"

[[Contour]]
deps = ["StaticArrays"]
git-tree-sha1 = "9f02045d934dc030edad45944ea80dbd1f0ebea7"
uuid = "d38c429a-6771-53c6-b99e-75d170b6e991"
version = "0.5.7"

[[Crayons]]
git-tree-sha1 = "3f71217b538d7aaee0b69ab47d9b7724ca8afa0d"
uuid = "a8cc5b0e-0ffa-5ad4-8c14-923d3ee1735f"
version = "4.0.4"

[[DataAPI]]
git-tree-sha1 = "bec2532f8adb82005476c141ec23e921fc20971b"
uuid = "9a962f9c-6df0-11e9-0e5d-c546b8b5ee8a"
version = "1.8.0"

[[DataFrames]]
deps = ["Compat", "DataAPI", "Future", "InvertedIndices", "IteratorInterfaceExtensions", "LinearAlgebra", "Markdown", "Missings", "PooledArrays", "PrettyTables", "Printf", "REPL", "Reexport", "SortingAlgorithms", "Statistics", "TableTraits", "Tables", "Unicode"]
git-tree-sha1 = "d785f42445b63fc86caa08bb9a9351008be9b765"
uuid = "a93c6f00-e57d-5684-b7b6-d8193f3e46c0"
version = "1.2.2"

[[DataStructures]]
deps = ["Compat", "InteractiveUtils", "OrderedCollections"]
git-tree-sha1 = "7d9d316f04214f7efdbb6398d545446e246eff02"
uuid = "864edb3b-99cc-5e75-8d2d-829cb0a9cfe8"
version = "0.18.10"

[[DataValueInterfaces]]
git-tree-sha1 = "bfc1187b79289637fa0ef6d4436ebdfe6905cbd6"
uuid = "e2d170a0-9d28-54be-80f0-106bbe20a464"
version = "1.0.0"

[[DataValues]]
deps = ["DataValueInterfaces", "Dates"]
git-tree-sha1 = "d88a19299eba280a6d062e135a43f00323ae70bf"
uuid = "e7dc6d0d-1eca-5fa6-8ad6-5aecde8b7ea5"
version = "0.4.13"

[[Dates]]
deps = ["Printf"]
uuid = "ade2ca70-3891-5945-98fb-dc099432e06a"

[[DelimitedFiles]]
deps = ["Mmap"]
uuid = "8bb1440f-4735-579b-a4ab-409b98df4dab"

[[Distances]]
deps = ["LinearAlgebra", "Statistics", "StatsAPI"]
git-tree-sha1 = "9f46deb4d4ee4494ffb5a40a27a2aced67bdd838"
uuid = "b4f34e82-e78d-54a5-968a-f98e89d6e8f7"
version = "0.10.4"

[[Distributed]]
deps = ["Random", "Serialization", "Sockets"]
uuid = "8ba89e20-285c-5b6f-9357-94700520ee1b"

[[Distributions]]
deps = ["ChainRulesCore", "FillArrays", "LinearAlgebra", "PDMats", "Printf", "QuadGK", "Random", "SparseArrays", "SpecialFunctions", "Statistics", "StatsBase", "StatsFuns"]
git-tree-sha1 = "f4efaa4b5157e0cdb8283ae0b5428bc9208436ed"
uuid = "31c24e10-a181-5473-b8eb-7969acd0382f"
version = "0.25.16"

[[DocStringExtensions]]
deps = ["LibGit2"]
git-tree-sha1 = "a32185f5428d3986f47c2ab78b1f216d5e6cc96f"
uuid = "ffbed154-4ef7-542d-bbb7-c09d3a79fcae"
version = "0.8.5"

[[Downloads]]
deps = ["ArgTools", "LibCURL", "NetworkOptions"]
uuid = "f43a241f-c20a-4ad4-852c-f6b1247861c6"

[[EarCut_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "3f3a2501fa7236e9b911e0f7a588c657e822bb6d"
uuid = "5ae413db-bbd1-5e63-b57d-d24a61df00f5"
version = "2.2.3+0"

[[Expat_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "b3bfd02e98aedfa5cf885665493c5598c350cd2f"
uuid = "2e619515-83b5-522b-bb60-26c02a35a201"
version = "2.2.10+0"

[[FFMPEG]]
deps = ["FFMPEG_jll"]
git-tree-sha1 = "b57e3acbe22f8484b4b5ff66a7499717fe1a9cc8"
uuid = "c87230d0-a227-11e9-1b43-d7ebe4e7570a"
version = "0.4.1"

[[FFMPEG_jll]]
deps = ["Artifacts", "Bzip2_jll", "FreeType2_jll", "FriBidi_jll", "JLLWrappers", "LAME_jll", "Libdl", "Ogg_jll", "OpenSSL_jll", "Opus_jll", "Pkg", "Zlib_jll", "libass_jll", "libfdk_aac_jll", "libvorbis_jll", "x264_jll", "x265_jll"]
git-tree-sha1 = "d8a578692e3077ac998b50c0217dfd67f21d1e5f"
uuid = "b22a6f82-2f65-5046-a5b2-351ab43fb4e5"
version = "4.4.0+0"

[[FFTW]]
deps = ["AbstractFFTs", "FFTW_jll", "LinearAlgebra", "MKL_jll", "Preferences", "Reexport"]
git-tree-sha1 = "d7ba5d3df9453b3516ebdd341db238e6e67b94ff"
uuid = "7a1cc6ca-52ef-59f5-83cd-3a7055c09341"
version = "1.4.4"

[[FFTW_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "3676abafff7e4ff07bbd2c42b3d8201f31653dcc"
uuid = "f5851436-0d7a-5f13-b9de-f02708fd171a"
version = "3.3.9+8"

[[FillArrays]]
deps = ["LinearAlgebra", "Random", "SparseArrays", "Statistics"]
git-tree-sha1 = "caf289224e622f518c9dbfe832cdafa17d7c80a6"
uuid = "1a297f60-69ca-5386-bcde-b61e274b549b"
version = "0.12.4"

[[FixedPointNumbers]]
deps = ["Statistics"]
git-tree-sha1 = "335bfdceacc84c5cdf16aadc768aa5ddfc5383cc"
uuid = "53c48c17-4a7d-5ca2-90c5-79b7896eea93"
version = "0.8.4"

[[Fontconfig_jll]]
deps = ["Artifacts", "Bzip2_jll", "Expat_jll", "FreeType2_jll", "JLLWrappers", "Libdl", "Libuuid_jll", "Pkg", "Zlib_jll"]
git-tree-sha1 = "21efd19106a55620a188615da6d3d06cd7f6ee03"
uuid = "a3f928ae-7b40-5064-980b-68af3947d34b"
version = "2.13.93+0"

[[Formatting]]
deps = ["Printf"]
git-tree-sha1 = "8339d61043228fdd3eb658d86c926cb282ae72a8"
uuid = "59287772-0a20-5a39-b81b-1366585eb4c0"
version = "0.4.2"

[[FreeType2_jll]]
deps = ["Artifacts", "Bzip2_jll", "JLLWrappers", "Libdl", "Pkg", "Zlib_jll"]
git-tree-sha1 = "87eb71354d8ec1a96d4a7636bd57a7347dde3ef9"
uuid = "d7e528f0-a631-5988-bf34-fe36492bcfd7"
version = "2.10.4+0"

[[FriBidi_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "aa31987c2ba8704e23c6c8ba8a4f769d5d7e4f91"
uuid = "559328eb-81f9-559d-9380-de523a88c83c"
version = "1.0.10+0"

[[Future]]
deps = ["Random"]
uuid = "9fa8497b-333b-5362-9e8d-4d0656e87820"

[[GLFW_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Libglvnd_jll", "Pkg", "Xorg_libXcursor_jll", "Xorg_libXi_jll", "Xorg_libXinerama_jll", "Xorg_libXrandr_jll"]
git-tree-sha1 = "0c603255764a1fa0b61752d2bec14cfbd18f7fe8"
uuid = "0656b61e-2033-5cc2-a64a-77c0f6c09b89"
version = "3.3.5+1"

[[GR]]
deps = ["Base64", "DelimitedFiles", "GR_jll", "HTTP", "JSON", "Libdl", "LinearAlgebra", "Pkg", "Printf", "Random", "Serialization", "Sockets", "Test", "UUIDs"]
git-tree-sha1 = "182da592436e287758ded5be6e32c406de3a2e47"
uuid = "28b8d3ca-fb5f-59d9-8090-bfdbd6d07a71"
version = "0.58.1"

[[GR_jll]]
deps = ["Artifacts", "Bzip2_jll", "Cairo_jll", "FFMPEG_jll", "Fontconfig_jll", "GLFW_jll", "JLLWrappers", "JpegTurbo_jll", "Libdl", "Libtiff_jll", "Pixman_jll", "Pkg", "Qt5Base_jll", "Zlib_jll", "libpng_jll"]
git-tree-sha1 = "ef49a187604f865f4708c90e3f431890724e9012"
uuid = "d2c73de3-f751-5644-a686-071e5b155ba9"
version = "0.59.0+0"

[[GeometryBasics]]
deps = ["EarCut_jll", "IterTools", "LinearAlgebra", "StaticArrays", "StructArrays", "Tables"]
git-tree-sha1 = "58bcdf5ebc057b085e58d95c138725628dd7453c"
uuid = "5c1252a2-5f33-56bf-86c9-59e7332b4326"
version = "0.4.1"

[[Gettext_jll]]
deps = ["Artifacts", "CompilerSupportLibraries_jll", "JLLWrappers", "Libdl", "Libiconv_jll", "Pkg", "XML2_jll"]
git-tree-sha1 = "9b02998aba7bf074d14de89f9d37ca24a1a0b046"
uuid = "78b55507-aeef-58d4-861c-77aaff3498b1"
version = "0.21.0+0"

[[Glib_jll]]
deps = ["Artifacts", "Gettext_jll", "JLLWrappers", "Libdl", "Libffi_jll", "Libiconv_jll", "Libmount_jll", "PCRE_jll", "Pkg", "Zlib_jll"]
git-tree-sha1 = "a32d672ac2c967f3deb8a81d828afc739c838a06"
uuid = "7746bdde-850d-59dc-9ae8-88ece973131d"
version = "2.68.3+2"

[[Graphite2_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "344bf40dcab1073aca04aa0df4fb092f920e4011"
uuid = "3b182d85-2403-5c21-9c21-1e1f0cc25472"
version = "1.3.14+0"

[[Grisu]]
git-tree-sha1 = "53bb909d1151e57e2484c3d1b53e19552b887fb2"
uuid = "42e2da0e-8278-4e71-bc24-59509adca0fe"
version = "1.0.2"

[[HTTP]]
deps = ["Base64", "Dates", "IniFile", "Logging", "MbedTLS", "NetworkOptions", "Sockets", "URIs"]
git-tree-sha1 = "60ed5f1643927479f845b0135bb369b031b541fa"
uuid = "cd3eb016-35fb-5094-929b-558a96fad6f3"
version = "0.9.14"

[[HarfBuzz_jll]]
deps = ["Artifacts", "Cairo_jll", "Fontconfig_jll", "FreeType2_jll", "Glib_jll", "Graphite2_jll", "JLLWrappers", "Libdl", "Libffi_jll", "Pkg"]
git-tree-sha1 = "129acf094d168394e80ee1dc4bc06ec835e510a3"
uuid = "2e76f6c2-a576-52d4-95c1-20adfe4de566"
version = "2.8.1+1"

[[IniFile]]
deps = ["Test"]
git-tree-sha1 = "098e4d2c533924c921f9f9847274f2ad89e018b8"
uuid = "83e8ac13-25f8-5344-8a64-a9f2b223428f"
version = "0.5.0"

[[IntelOpenMP_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "d979e54b71da82f3a65b62553da4fc3d18c9004c"
uuid = "1d5cc7b8-4909-519e-a0f8-d0f5ad9712d0"
version = "2018.0.3+2"

[[InteractiveUtils]]
deps = ["Markdown"]
uuid = "b77e0a4c-d291-57a0-90e8-8db25a27a240"

[[Interpolations]]
deps = ["AxisAlgorithms", "ChainRulesCore", "LinearAlgebra", "OffsetArrays", "Random", "Ratios", "Requires", "SharedArrays", "SparseArrays", "StaticArrays", "WoodburyMatrices"]
git-tree-sha1 = "61aa005707ea2cebf47c8d780da8dc9bc4e0c512"
uuid = "a98d9a8b-a2ab-59e6-89dd-64a1c18fca59"
version = "0.13.4"

[[InvertedIndices]]
git-tree-sha1 = "bee5f1ef5bf65df56bdd2e40447590b272a5471f"
uuid = "41ab1584-1d38-5bbf-9106-f11c6c58b48f"
version = "1.1.0"

[[IrrationalConstants]]
git-tree-sha1 = "f76424439413893a832026ca355fe273e93bce94"
uuid = "92d709cd-6900-40b7-9082-c6be49f344b6"
version = "0.1.0"

[[IterTools]]
git-tree-sha1 = "05110a2ab1fc5f932622ffea2a003221f4782c18"
uuid = "c8e1da08-722c-5040-9ed9-7db0dc04731e"
version = "1.3.0"

[[IteratorInterfaceExtensions]]
git-tree-sha1 = "a3f24677c21f5bbe9d2a714f95dcd58337fb2856"
uuid = "82899510-4779-5014-852e-03e436cf321d"
version = "1.0.0"

[[JLLWrappers]]
deps = ["Preferences"]
git-tree-sha1 = "642a199af8b68253517b80bd3bfd17eb4e84df6e"
uuid = "692b3bcd-3c85-4b1f-b108-f13ce0eb3210"
version = "1.3.0"

[[JSON]]
deps = ["Dates", "Mmap", "Parsers", "Unicode"]
git-tree-sha1 = "8076680b162ada2a031f707ac7b4953e30667a37"
uuid = "682c06a0-de6a-54ab-a142-c8b1cf79cde6"
version = "0.21.2"

[[JpegTurbo_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "d735490ac75c5cb9f1b00d8b5509c11984dc6943"
uuid = "aacddb02-875f-59d6-b918-886e6ef4fbf8"
version = "2.1.0+0"

[[KernelDensity]]
deps = ["Distributions", "DocStringExtensions", "FFTW", "Interpolations", "StatsBase"]
git-tree-sha1 = "591e8dc09ad18386189610acafb970032c519707"
uuid = "5ab0869b-81aa-558d-bb23-cbf5423bbe9b"
version = "0.6.3"

[[LAME_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "f6250b16881adf048549549fba48b1161acdac8c"
uuid = "c1c5ebd0-6772-5130-a774-d5fcae4a789d"
version = "3.100.1+0"

[[LERC_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "bf36f528eec6634efc60d7ec062008f171071434"
uuid = "88015f11-f218-50d7-93a8-a6af411a945d"
version = "3.0.0+1"

[[LZO_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "e5b909bcf985c5e2605737d2ce278ed791b89be6"
uuid = "dd4b983a-f0e5-5f8d-a1b7-129d4a5fb1ac"
version = "2.10.1+0"

[[LaTeXStrings]]
git-tree-sha1 = "c7f1c695e06c01b95a67f0cd1d34994f3e7db104"
uuid = "b964fa9f-0449-5b57-a5c2-d3ea65f4040f"
version = "1.2.1"

[[Latexify]]
deps = ["Formatting", "InteractiveUtils", "LaTeXStrings", "MacroTools", "Markdown", "Printf", "Requires"]
git-tree-sha1 = "a4b12a1bd2ebade87891ab7e36fdbce582301a92"
uuid = "23fbe1c1-3f47-55db-b15f-69d7ec21a316"
version = "0.15.6"

[[LazyArtifacts]]
deps = ["Artifacts", "Pkg"]
uuid = "4af54fe1-eca0-43a8-85a7-787d91b784e3"

[[LibCURL]]
deps = ["LibCURL_jll", "MozillaCACerts_jll"]
uuid = "b27032c2-a3e7-50c8-80cd-2d36dbcbfd21"

[[LibCURL_jll]]
deps = ["Artifacts", "LibSSH2_jll", "Libdl", "MbedTLS_jll", "Zlib_jll", "nghttp2_jll"]
uuid = "deac9b47-8bc7-5906-a0fe-35ac56dc84c0"

[[LibGit2]]
deps = ["Base64", "NetworkOptions", "Printf", "SHA"]
uuid = "76f85450-5226-5b5a-8eaa-529ad045b433"

[[LibSSH2_jll]]
deps = ["Artifacts", "Libdl", "MbedTLS_jll"]
uuid = "29816b5a-b9ab-546f-933c-edad1886dfa8"

[[Libdl]]
uuid = "8f399da3-3557-5675-b5ff-fb832c97cbdb"

[[Libffi_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "0b4a5d71f3e5200a7dff793393e09dfc2d874290"
uuid = "e9f186c6-92d2-5b65-8a66-fee21dc1b490"
version = "3.2.2+1"

[[Libgcrypt_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Libgpg_error_jll", "Pkg"]
git-tree-sha1 = "64613c82a59c120435c067c2b809fc61cf5166ae"
uuid = "d4300ac3-e22c-5743-9152-c294e39db1e4"
version = "1.8.7+0"

[[Libglvnd_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libX11_jll", "Xorg_libXext_jll"]
git-tree-sha1 = "7739f837d6447403596a75d19ed01fd08d6f56bf"
uuid = "7e76a0d4-f3c7-5321-8279-8d96eeed0f29"
version = "1.3.0+3"

[[Libgpg_error_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "c333716e46366857753e273ce6a69ee0945a6db9"
uuid = "7add5ba3-2f88-524e-9cd5-f83b8a55f7b8"
version = "1.42.0+0"

[[Libiconv_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "42b62845d70a619f063a7da093d995ec8e15e778"
uuid = "94ce4f54-9a6c-5748-9c1c-f9c7231a4531"
version = "1.16.1+1"

[[Libmount_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "9c30530bf0effd46e15e0fdcf2b8636e78cbbd73"
uuid = "4b2f31a3-9ecc-558c-b454-b3730dcb73e9"
version = "2.35.0+0"

[[Libtiff_jll]]
deps = ["Artifacts", "JLLWrappers", "JpegTurbo_jll", "LERC_jll", "Libdl", "Pkg", "Zlib_jll", "Zstd_jll"]
git-tree-sha1 = "c9551dd26e31ab17b86cbd00c2ede019c08758eb"
uuid = "89763e89-9b03-5906-acba-b20f662cd828"
version = "4.3.0+1"

[[Libuuid_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "7f3efec06033682db852f8b3bc3c1d2b0a0ab066"
uuid = "38a345b3-de98-5d2b-a5d3-14cd9215e700"
version = "2.36.0+0"

[[LinearAlgebra]]
deps = ["Libdl"]
uuid = "37e2e46d-f89d-539d-b4ee-838fcccc9c8e"

[[LogExpFunctions]]
deps = ["ChainRulesCore", "DocStringExtensions", "IrrationalConstants", "LinearAlgebra"]
git-tree-sha1 = "86197a8ecb06e222d66797b0c2d2f0cc7b69e42b"
uuid = "2ab3a3ac-af41-5b50-aa03-7779005ae688"
version = "0.3.2"

[[Logging]]
uuid = "56ddb016-857b-54e1-b83d-db4d58db5568"

[[MKL_jll]]
deps = ["Artifacts", "IntelOpenMP_jll", "JLLWrappers", "LazyArtifacts", "Libdl", "Pkg"]
git-tree-sha1 = "5455aef09b40e5020e1520f551fa3135040d4ed0"
uuid = "856f044c-d86e-5d09-b602-aeab76dc8ba7"
version = "2021.1.1+2"

[[MacroTools]]
deps = ["Markdown", "Random"]
git-tree-sha1 = "0fb723cd8c45858c22169b2e42269e53271a6df7"
uuid = "1914dd2f-81c6-5fcd-8719-6d5c9610ff09"
version = "0.5.7"

[[Markdown]]
deps = ["Base64"]
uuid = "d6f4376e-aef5-505a-96c1-9c027394607a"

[[MbedTLS]]
deps = ["Dates", "MbedTLS_jll", "Random", "Sockets"]
git-tree-sha1 = "1c38e51c3d08ef2278062ebceade0e46cefc96fe"
uuid = "739be429-bea8-5141-9913-cc70e7f3736d"
version = "1.0.3"

[[MbedTLS_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "c8ffd9c3-330d-5841-b78e-0817d7145fa1"

[[Measures]]
git-tree-sha1 = "e498ddeee6f9fdb4551ce855a46f54dbd900245f"
uuid = "442fdcdd-2543-5da2-b0f3-8c86c306513e"
version = "0.3.1"

[[Missings]]
deps = ["DataAPI"]
git-tree-sha1 = "2ca267b08821e86c5ef4376cffed98a46c2cb205"
uuid = "e1d29d7a-bbdc-5cf2-9ac0-f12de2c33e28"
version = "1.0.1"

[[Mmap]]
uuid = "a63ad114-7e13-5084-954f-fe012c677804"

[[MozillaCACerts_jll]]
uuid = "14a3606d-f60d-562e-9121-12d972cd8159"

[[MultivariateStats]]
deps = ["Arpack", "LinearAlgebra", "SparseArrays", "Statistics", "StatsBase"]
git-tree-sha1 = "8d958ff1854b166003238fe191ec34b9d592860a"
uuid = "6f286f6a-111f-5878-ab1e-185364afe411"
version = "0.8.0"

[[NaNMath]]
git-tree-sha1 = "bfe47e760d60b82b66b61d2d44128b62e3a369fb"
uuid = "77ba4419-2d1f-58cd-9bb1-8ffee604a2e3"
version = "0.3.5"

[[NearestNeighbors]]
deps = ["Distances", "StaticArrays"]
git-tree-sha1 = "16baacfdc8758bc374882566c9187e785e85c2f0"
uuid = "b8a86587-4115-5ab1-83bc-aa920d37bbce"
version = "0.4.9"

[[NetworkOptions]]
uuid = "ca575930-c2e3-43a9-ace4-1e988b2c1908"

[[Observables]]
git-tree-sha1 = "fe29afdef3d0c4a8286128d4e45cc50621b1e43d"
uuid = "510215fc-4207-5dde-b226-833fc4488ee2"
version = "0.4.0"

[[OffsetArrays]]
deps = ["Adapt"]
git-tree-sha1 = "c870a0d713b51e4b49be6432eff0e26a4325afee"
uuid = "6fe1bfb0-de20-5000-8ca7-80f57d26f881"
version = "1.10.6"

[[Ogg_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "887579a3eb005446d514ab7aeac5d1d027658b8f"
uuid = "e7412a2a-1a6e-54c0-be00-318e2571c051"
version = "1.3.5+1"

[[OpenBLAS_jll]]
deps = ["Artifacts", "CompilerSupportLibraries_jll", "Libdl"]
uuid = "4536629a-c528-5b80-bd46-f80d51c5b363"

[[OpenSSL_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "15003dcb7d8db3c6c857fda14891a539a8f2705a"
uuid = "458c3c95-2e84-50aa-8efc-19380b2a3a95"
version = "1.1.10+0"

[[OpenSpecFun_jll]]
deps = ["Artifacts", "CompilerSupportLibraries_jll", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "13652491f6856acfd2db29360e1bbcd4565d04f1"
uuid = "efe28fd5-8261-553b-a9e1-b2916fc3738e"
version = "0.5.5+0"

[[Opus_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "51a08fb14ec28da2ec7a927c4337e4332c2a4720"
uuid = "91d4177d-7536-5919-b921-800302f37372"
version = "1.3.2+0"

[[OrderedCollections]]
git-tree-sha1 = "85f8e6578bf1f9ee0d11e7bb1b1456435479d47c"
uuid = "bac558e1-5e72-5ebc-8fee-abe8a469f55d"
version = "1.4.1"

[[PCRE_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "b2a7af664e098055a7529ad1a900ded962bca488"
uuid = "2f80f16e-611a-54ab-bc61-aa92de5b98fc"
version = "8.44.0+0"

[[PDMats]]
deps = ["LinearAlgebra", "SparseArrays", "SuiteSparse"]
git-tree-sha1 = "4dd403333bcf0909341cfe57ec115152f937d7d8"
uuid = "90014a1f-27ba-587c-ab20-58faa44d9150"
version = "0.11.1"

[[Parsers]]
deps = ["Dates"]
git-tree-sha1 = "438d35d2d95ae2c5e8780b330592b6de8494e779"
uuid = "69de0a69-1ddd-5017-9359-2bf0b02dc9f0"
version = "2.0.3"

[[Pixman_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "b4f5d02549a10e20780a24fce72bea96b6329e29"
uuid = "30392449-352a-5448-841d-b1acce4e97dc"
version = "0.40.1+0"

[[Pkg]]
deps = ["Artifacts", "Dates", "Downloads", "LibGit2", "Libdl", "Logging", "Markdown", "Printf", "REPL", "Random", "SHA", "Serialization", "TOML", "Tar", "UUIDs", "p7zip_jll"]
uuid = "44cfe95a-1eb2-52ea-b672-e2afdf69b78f"

[[PlotThemes]]
deps = ["PlotUtils", "Requires", "Statistics"]
git-tree-sha1 = "a3a964ce9dc7898193536002a6dd892b1b5a6f1d"
uuid = "ccf2f8ad-2431-5c83-bf29-c5338b663b6a"
version = "2.0.1"

[[PlotUtils]]
deps = ["ColorSchemes", "Colors", "Dates", "Printf", "Random", "Reexport", "Statistics"]
git-tree-sha1 = "9ff1c70190c1c30aebca35dc489f7411b256cd23"
uuid = "995b91a9-d308-5afd-9ec6-746e21dbc043"
version = "1.0.13"

[[Plots]]
deps = ["Base64", "Contour", "Dates", "Downloads", "FFMPEG", "FixedPointNumbers", "GR", "GeometryBasics", "JSON", "Latexify", "LinearAlgebra", "Measures", "NaNMath", "PlotThemes", "PlotUtils", "Printf", "REPL", "Random", "RecipesBase", "RecipesPipeline", "Reexport", "Requires", "Scratch", "Showoff", "SparseArrays", "Statistics", "StatsBase", "UUIDs"]
git-tree-sha1 = "2dbafeadadcf7dadff20cd60046bba416b4912be"
uuid = "91a5bcdd-55d7-5caf-9e0b-520d859cae80"
version = "1.21.3"

[[PlutoUI]]
deps = ["Base64", "Dates", "InteractiveUtils", "JSON", "Logging", "Markdown", "Random", "Reexport", "Suppressor"]
git-tree-sha1 = "44e225d5837e2a2345e69a1d1e01ac2443ff9fcb"
uuid = "7f904dfe-b85e-4ff6-b463-dae2292396a8"
version = "0.7.9"

[[PooledArrays]]
deps = ["DataAPI", "Future"]
git-tree-sha1 = "a193d6ad9c45ada72c14b731a318bedd3c2f00cf"
uuid = "2dfb63ee-cc39-5dd5-95bd-886bf059d720"
version = "1.3.0"

[[Preferences]]
deps = ["TOML"]
git-tree-sha1 = "00cfd92944ca9c760982747e9a1d0d5d86ab1e5a"
uuid = "21216c6a-2e73-6563-6e65-726566657250"
version = "1.2.2"

[[PrettyTables]]
deps = ["Crayons", "Formatting", "Markdown", "Reexport", "Tables"]
git-tree-sha1 = "0d1245a357cc61c8cd61934c07447aa569ff22e6"
uuid = "08abe8d2-0d0c-5749-adfa-8a2ac140af0d"
version = "1.1.0"

[[Printf]]
deps = ["Unicode"]
uuid = "de0858da-6303-5e67-8744-51eddeeeb8d7"

[[Qt5Base_jll]]
deps = ["Artifacts", "CompilerSupportLibraries_jll", "Fontconfig_jll", "Glib_jll", "JLLWrappers", "Libdl", "Libglvnd_jll", "OpenSSL_jll", "Pkg", "Xorg_libXext_jll", "Xorg_libxcb_jll", "Xorg_xcb_util_image_jll", "Xorg_xcb_util_keysyms_jll", "Xorg_xcb_util_renderutil_jll", "Xorg_xcb_util_wm_jll", "Zlib_jll", "xkbcommon_jll"]
git-tree-sha1 = "ad368663a5e20dbb8d6dc2fddeefe4dae0781ae8"
uuid = "ea2cea3b-5b76-57ae-a6ef-0a8af62496e1"
version = "5.15.3+0"

[[QuadGK]]
deps = ["DataStructures", "LinearAlgebra"]
git-tree-sha1 = "12fbe86da16df6679be7521dfb39fbc861e1dc7b"
uuid = "1fd47b50-473d-5c70-9696-f719f8f3bcdc"
version = "2.4.1"

[[REPL]]
deps = ["InteractiveUtils", "Markdown", "Sockets", "Unicode"]
uuid = "3fa0cd96-eef1-5676-8a61-b3b8758bbffb"

[[Random]]
deps = ["Serialization"]
uuid = "9a3f8284-a2c9-5f02-9a11-845980a1fd5c"

[[Ratios]]
deps = ["Requires"]
git-tree-sha1 = "7dff99fbc740e2f8228c6878e2aad6d7c2678098"
uuid = "c84ed2f1-dad5-54f0-aa8e-dbefe2724439"
version = "0.4.1"

[[RecipesBase]]
git-tree-sha1 = "44a75aa7a527910ee3d1751d1f0e4148698add9e"
uuid = "3cdcf5f2-1ef4-517c-9805-6587b60abb01"
version = "1.1.2"

[[RecipesPipeline]]
deps = ["Dates", "NaNMath", "PlotUtils", "RecipesBase"]
git-tree-sha1 = "d4491becdc53580c6dadb0f6249f90caae888554"
uuid = "01d81517-befc-4cb6-b9ec-a95719d0359c"
version = "0.4.0"

[[Reexport]]
git-tree-sha1 = "45e428421666073eab6f2da5c9d310d99bb12f9b"
uuid = "189a3867-3050-52da-a836-e630ba90ab69"
version = "1.2.2"

[[Requires]]
deps = ["UUIDs"]
git-tree-sha1 = "4036a3bd08ac7e968e27c203d45f5fff15020621"
uuid = "ae029012-a4dd-5104-9daa-d747884805df"
version = "1.1.3"

[[Rmath]]
deps = ["Random", "Rmath_jll"]
git-tree-sha1 = "bf3188feca147ce108c76ad82c2792c57abe7b1f"
uuid = "79098fc4-a85e-5d69-aa6a-4863f24498fa"
version = "0.7.0"

[[Rmath_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "68db32dff12bb6127bac73c209881191bf0efbb7"
uuid = "f50d1b31-88e8-58de-be2c-1cc44531875f"
version = "0.3.0+0"

[[SHA]]
uuid = "ea8e919c-243c-51af-8825-aaa63cd721ce"

[[Scratch]]
deps = ["Dates"]
git-tree-sha1 = "0b4b7f1393cff97c33891da2a0bf69c6ed241fda"
uuid = "6c6a2e73-6563-6170-7368-637461726353"
version = "1.1.0"

[[SentinelArrays]]
deps = ["Dates", "Random"]
git-tree-sha1 = "54f37736d8934a12a200edea2f9206b03bdf3159"
uuid = "91c51154-3ec4-41a3-a24f-3f23e20d615c"
version = "1.3.7"

[[Serialization]]
uuid = "9e88b42a-f829-5b0c-bbe9-9e923198166b"

[[SharedArrays]]
deps = ["Distributed", "Mmap", "Random", "Serialization"]
uuid = "1a1011a3-84de-559e-8e89-a11a2f7dc383"

[[Showoff]]
deps = ["Dates", "Grisu"]
git-tree-sha1 = "91eddf657aca81df9ae6ceb20b959ae5653ad1de"
uuid = "992d4aef-0814-514b-bc4d-f2e9a6c4116f"
version = "1.0.3"

[[Sockets]]
uuid = "6462fe0b-24de-5631-8697-dd941f90decc"

[[SortingAlgorithms]]
deps = ["DataStructures"]
git-tree-sha1 = "b3363d7460f7d098ca0912c69b082f75625d7508"
uuid = "a2af1166-a08f-5f64-846c-94a0d3cef48c"
version = "1.0.1"

[[SparseArrays]]
deps = ["LinearAlgebra", "Random"]
uuid = "2f01184e-e22b-5df5-ae63-d93ebab69eaf"

[[SpecialFunctions]]
deps = ["ChainRulesCore", "LogExpFunctions", "OpenSpecFun_jll"]
git-tree-sha1 = "a322a9493e49c5f3a10b50df3aedaf1cdb3244b7"
uuid = "276daf66-3868-5448-9aa4-cd146d93841b"
version = "1.6.1"

[[StaticArrays]]
deps = ["LinearAlgebra", "Random", "Statistics"]
git-tree-sha1 = "3240808c6d463ac46f1c1cd7638375cd22abbccb"
uuid = "90137ffa-7385-5640-81b9-e52037218182"
version = "1.2.12"

[[Statistics]]
deps = ["LinearAlgebra", "SparseArrays"]
uuid = "10745b16-79ce-11e8-11f9-7d13ad32a3b2"

[[StatsAPI]]
git-tree-sha1 = "1958272568dc176a1d881acb797beb909c785510"
uuid = "82ae8749-77ed-4fe6-ae5f-f523153014b0"
version = "1.0.0"

[[StatsBase]]
deps = ["DataAPI", "DataStructures", "LinearAlgebra", "Missings", "Printf", "Random", "SortingAlgorithms", "SparseArrays", "Statistics", "StatsAPI"]
git-tree-sha1 = "8cbbc098554648c84f79a463c9ff0fd277144b6c"
uuid = "2913bbd2-ae8a-5f71-8c99-4fb6c76f3a91"
version = "0.33.10"

[[StatsFuns]]
deps = ["ChainRulesCore", "IrrationalConstants", "LogExpFunctions", "Reexport", "Rmath", "SpecialFunctions"]
git-tree-sha1 = "46d7ccc7104860c38b11966dd1f72ff042f382e4"
uuid = "4c63d2b9-4356-54db-8cca-17b64c39e42c"
version = "0.9.10"

[[StatsPlots]]
deps = ["Clustering", "DataStructures", "DataValues", "Distributions", "Interpolations", "KernelDensity", "LinearAlgebra", "MultivariateStats", "Observables", "Plots", "RecipesBase", "RecipesPipeline", "Reexport", "StatsBase", "TableOperations", "Tables", "Widgets"]
git-tree-sha1 = "233bc83194181b07b052b4ee24515564b893faf6"
uuid = "f3b207a7-027a-5e70-b257-86293d7955fd"
version = "0.14.27"

[[StructArrays]]
deps = ["Adapt", "DataAPI", "StaticArrays", "Tables"]
git-tree-sha1 = "1700b86ad59348c0f9f68ddc95117071f947072d"
uuid = "09ab397b-f2b6-538f-b94a-2f83cf4a842a"
version = "0.6.1"

[[SuiteSparse]]
deps = ["Libdl", "LinearAlgebra", "Serialization", "SparseArrays"]
uuid = "4607b0f0-06f3-5cda-b6b1-a6196a1729e9"

[[Suppressor]]
git-tree-sha1 = "a819d77f31f83e5792a76081eee1ea6342ab8787"
uuid = "fd094767-a336-5f1f-9728-57cf17d0bbfb"
version = "0.2.0"

[[TOML]]
deps = ["Dates"]
uuid = "fa267f1f-6049-4f14-aa54-33bafae1ed76"

[[TableOperations]]
deps = ["SentinelArrays", "Tables", "Test"]
git-tree-sha1 = "019acfd5a4a6c5f0f38de69f2ff7ed527f1881da"
uuid = "ab02a1b2-a7df-11e8-156e-fb1833f50b87"
version = "1.1.0"

[[TableTraits]]
deps = ["IteratorInterfaceExtensions"]
git-tree-sha1 = "c06b2f539df1c6efa794486abfb6ed2022561a39"
uuid = "3783bdb8-4a98-5b6b-af9a-565f29a5fe9c"
version = "1.0.1"

[[Tables]]
deps = ["DataAPI", "DataValueInterfaces", "IteratorInterfaceExtensions", "LinearAlgebra", "TableTraits", "Test"]
git-tree-sha1 = "368d04a820fe069f9080ff1b432147a6203c3c89"
uuid = "bd369af6-aec1-5ad0-b16a-f7cc5008161c"
version = "1.5.1"

[[Tar]]
deps = ["ArgTools", "SHA"]
uuid = "a4e569a6-e804-4fa4-b0f3-eef7a1d5b13e"

[[Test]]
deps = ["InteractiveUtils", "Logging", "Random", "Serialization"]
uuid = "8dfed614-e22c-5e08-85e1-65c5234f0b40"

[[URIs]]
git-tree-sha1 = "97bbe755a53fe859669cd907f2d96aee8d2c1355"
uuid = "5c2747f8-b7ea-4ff2-ba2e-563bfd36b1d4"
version = "1.3.0"

[[UUIDs]]
deps = ["Random", "SHA"]
uuid = "cf7118a7-6976-5b1a-9a39-7adc72f591a4"

[[Unicode]]
uuid = "4ec0a83e-493e-50e2-b9ac-8f72acf5a8f5"

[[Wayland_jll]]
deps = ["Artifacts", "Expat_jll", "JLLWrappers", "Libdl", "Libffi_jll", "Pkg", "XML2_jll"]
git-tree-sha1 = "3e61f0b86f90dacb0bc0e73a0c5a83f6a8636e23"
uuid = "a2964d1f-97da-50d4-b82a-358c7fce9d89"
version = "1.19.0+0"

[[Wayland_protocols_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Wayland_jll"]
git-tree-sha1 = "2839f1c1296940218e35df0bbb220f2a79686670"
uuid = "2381bf8a-dfd0-557d-9999-79630e7b1b91"
version = "1.18.0+4"

[[Widgets]]
deps = ["Colors", "Dates", "Observables", "OrderedCollections"]
git-tree-sha1 = "eae2fbbc34a79ffd57fb4c972b08ce50b8f6a00d"
uuid = "cc8bc4a8-27d6-5769-a93b-9d913e69aa62"
version = "0.6.3"

[[WoodburyMatrices]]
deps = ["LinearAlgebra", "SparseArrays"]
git-tree-sha1 = "59e2ad8fd1591ea019a5259bd012d7aee15f995c"
uuid = "efce3f68-66dc-5838-9240-27a6d6f5f9b6"
version = "0.5.3"

[[XML2_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Libiconv_jll", "Pkg", "Zlib_jll"]
git-tree-sha1 = "1acf5bdf07aa0907e0a37d3718bb88d4b687b74a"
uuid = "02c8fc9c-b97f-50b9-bbe4-9be30ff0a78a"
version = "2.9.12+0"

[[XSLT_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Libgcrypt_jll", "Libgpg_error_jll", "Libiconv_jll", "Pkg", "XML2_jll", "Zlib_jll"]
git-tree-sha1 = "91844873c4085240b95e795f692c4cec4d805f8a"
uuid = "aed1982a-8fda-507f-9586-7b0439959a61"
version = "1.1.34+0"

[[Xorg_libX11_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libxcb_jll", "Xorg_xtrans_jll"]
git-tree-sha1 = "5be649d550f3f4b95308bf0183b82e2582876527"
uuid = "4f6342f7-b3d2-589e-9d20-edeb45f2b2bc"
version = "1.6.9+4"

[[Xorg_libXau_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "4e490d5c960c314f33885790ed410ff3a94ce67e"
uuid = "0c0b7dd1-d40b-584c-a123-a41640f87eec"
version = "1.0.9+4"

[[Xorg_libXcursor_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libXfixes_jll", "Xorg_libXrender_jll"]
git-tree-sha1 = "12e0eb3bc634fa2080c1c37fccf56f7c22989afd"
uuid = "935fb764-8cf2-53bf-bb30-45bb1f8bf724"
version = "1.2.0+4"

[[Xorg_libXdmcp_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "4fe47bd2247248125c428978740e18a681372dd4"
uuid = "a3789734-cfe1-5b06-b2d0-1dd0d9d62d05"
version = "1.1.3+4"

[[Xorg_libXext_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libX11_jll"]
git-tree-sha1 = "b7c0aa8c376b31e4852b360222848637f481f8c3"
uuid = "1082639a-0dae-5f34-9b06-72781eeb8cb3"
version = "1.3.4+4"

[[Xorg_libXfixes_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libX11_jll"]
git-tree-sha1 = "0e0dc7431e7a0587559f9294aeec269471c991a4"
uuid = "d091e8ba-531a-589c-9de9-94069b037ed8"
version = "5.0.3+4"

[[Xorg_libXi_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libXext_jll", "Xorg_libXfixes_jll"]
git-tree-sha1 = "89b52bc2160aadc84d707093930ef0bffa641246"
uuid = "a51aa0fd-4e3c-5386-b890-e753decda492"
version = "1.7.10+4"

[[Xorg_libXinerama_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libXext_jll"]
git-tree-sha1 = "26be8b1c342929259317d8b9f7b53bf2bb73b123"
uuid = "d1454406-59df-5ea1-beac-c340f2130bc3"
version = "1.1.4+4"

[[Xorg_libXrandr_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libXext_jll", "Xorg_libXrender_jll"]
git-tree-sha1 = "34cea83cb726fb58f325887bf0612c6b3fb17631"
uuid = "ec84b674-ba8e-5d96-8ba1-2a689ba10484"
version = "1.5.2+4"

[[Xorg_libXrender_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libX11_jll"]
git-tree-sha1 = "19560f30fd49f4d4efbe7002a1037f8c43d43b96"
uuid = "ea2f1a96-1ddc-540d-b46f-429655e07cfa"
version = "0.9.10+4"

[[Xorg_libpthread_stubs_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "6783737e45d3c59a4a4c4091f5f88cdcf0908cbb"
uuid = "14d82f49-176c-5ed1-bb49-ad3f5cbd8c74"
version = "0.1.0+3"

[[Xorg_libxcb_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "XSLT_jll", "Xorg_libXau_jll", "Xorg_libXdmcp_jll", "Xorg_libpthread_stubs_jll"]
git-tree-sha1 = "daf17f441228e7a3833846cd048892861cff16d6"
uuid = "c7cfdc94-dc32-55de-ac96-5a1b8d977c5b"
version = "1.13.0+3"

[[Xorg_libxkbfile_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libX11_jll"]
git-tree-sha1 = "926af861744212db0eb001d9e40b5d16292080b2"
uuid = "cc61e674-0454-545c-8b26-ed2c68acab7a"
version = "1.1.0+4"

[[Xorg_xcb_util_image_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_xcb_util_jll"]
git-tree-sha1 = "0fab0a40349ba1cba2c1da699243396ff8e94b97"
uuid = "12413925-8142-5f55-bb0e-6d7ca50bb09b"
version = "0.4.0+1"

[[Xorg_xcb_util_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libxcb_jll"]
git-tree-sha1 = "e7fd7b2881fa2eaa72717420894d3938177862d1"
uuid = "2def613f-5ad1-5310-b15b-b15d46f528f5"
version = "0.4.0+1"

[[Xorg_xcb_util_keysyms_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_xcb_util_jll"]
git-tree-sha1 = "d1151e2c45a544f32441a567d1690e701ec89b00"
uuid = "975044d2-76e6-5fbe-bf08-97ce7c6574c7"
version = "0.4.0+1"

[[Xorg_xcb_util_renderutil_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_xcb_util_jll"]
git-tree-sha1 = "dfd7a8f38d4613b6a575253b3174dd991ca6183e"
uuid = "0d47668e-0667-5a69-a72c-f761630bfb7e"
version = "0.3.9+1"

[[Xorg_xcb_util_wm_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_xcb_util_jll"]
git-tree-sha1 = "e78d10aab01a4a154142c5006ed44fd9e8e31b67"
uuid = "c22f9ab0-d5fe-5066-847c-f4bb1cd4e361"
version = "0.4.1+1"

[[Xorg_xkbcomp_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_libxkbfile_jll"]
git-tree-sha1 = "4bcbf660f6c2e714f87e960a171b119d06ee163b"
uuid = "35661453-b289-5fab-8a00-3d9160c6a3a4"
version = "1.4.2+4"

[[Xorg_xkeyboard_config_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Xorg_xkbcomp_jll"]
git-tree-sha1 = "5c8424f8a67c3f2209646d4425f3d415fee5931d"
uuid = "33bec58e-1273-512f-9401-5d533626f822"
version = "2.27.0+4"

[[Xorg_xtrans_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "79c31e7844f6ecf779705fbc12146eb190b7d845"
uuid = "c5fb5394-a638-5e4d-96e5-b29de1b5cf10"
version = "1.4.0+3"

[[Zlib_jll]]
deps = ["Libdl"]
uuid = "83775a58-1f1d-513f-b197-d71354ab007a"

[[Zstd_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "cc4bf3fdde8b7e3e9fa0351bdeedba1cf3b7f6e6"
uuid = "3161d3a3-bdf6-5164-811a-617609db77b4"
version = "1.5.0+0"

[[libass_jll]]
deps = ["Artifacts", "Bzip2_jll", "FreeType2_jll", "FriBidi_jll", "HarfBuzz_jll", "JLLWrappers", "Libdl", "Pkg", "Zlib_jll"]
git-tree-sha1 = "5982a94fcba20f02f42ace44b9894ee2b140fe47"
uuid = "0ac62f75-1d6f-5e53-bd7c-93b484bb37c0"
version = "0.15.1+0"

[[libfdk_aac_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "daacc84a041563f965be61859a36e17c4e4fcd55"
uuid = "f638f0a6-7fb0-5443-88ba-1cc74229b280"
version = "2.0.2+0"

[[libpng_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Zlib_jll"]
git-tree-sha1 = "94d180a6d2b5e55e447e2d27a29ed04fe79eb30c"
uuid = "b53b4c65-9356-5827-b1ea-8c7a1a84506f"
version = "1.6.38+0"

[[libvorbis_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Ogg_jll", "Pkg"]
git-tree-sha1 = "b910cb81ef3fe6e78bf6acee440bda86fd6ae00c"
uuid = "f27f6e37-5d2b-51aa-960f-b287f2bc3b7a"
version = "1.3.7+1"

[[nghttp2_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "8e850ede-7688-5339-a07c-302acd2aaf8d"

[[p7zip_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "3f19e933-33d8-53b3-aaab-bd5110c3b7a0"

[[x264_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "4fea590b89e6ec504593146bf8b988b2c00922b2"
uuid = "1270edf5-f2f9-52d2-97e9-ab00b5d0237a"
version = "2021.5.5+0"

[[x265_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg"]
git-tree-sha1 = "ee567a171cce03570d77ad3a43e90218e38937a9"
uuid = "dfaa095f-4041-5dcd-9319-2fabd8486b76"
version = "3.5.0+0"

[[xkbcommon_jll]]
deps = ["Artifacts", "JLLWrappers", "Libdl", "Pkg", "Wayland_jll", "Wayland_protocols_jll", "Xorg_libxcb_jll", "Xorg_xkeyboard_config_jll"]
git-tree-sha1 = "ece2350174195bb31de1a63bea3a41ae1aa593b6"
uuid = "d8fb68d0-12a3-5cfd-a85a-d49703b185fd"
version = "0.9.1+5"
"""

# ╔═╡ Cell order:
# ╟─3ade6cff-a9ac-4e1b-8c2b-9468a7476424
# ╟─11d405ba-3f72-4155-930c-2720449d1f71
# ╠═8b95a76c-8648-4295-9f2a-e9ce7e30f4e1
# ╟─fb931c1d-3de4-489c-96d7-a69bb14fd1b2
# ╟─d0ae819a-d96a-4715-86f0-e6e480d0714b
# ╟─aacc06b4-1afb-4e83-8392-45b2e24eb51a
# ╟─efd9c782-f1af-4b37-823f-e1a8e606f434
# ╟─91357e08-3a1c-41b3-9c03-1d839c3222ec
# ╟─05342071-26c0-40c4-8c7f-ff074595c6d7
# ╠═39f0ce2f-650a-43f5-9129-0e1f4d70c215
# ╟─ae42451e-8ba3-47c2-8dfc-6c82cc0f7f7b
# ╟─450c7626-fb30-4b15-8bab-ed326698d958
# ╟─1309cdd1-8346-4645-9156-58923aa8afed
# ╟─6ac7b024-ec4a-41c2-bb9b-8b3fe8c40021
# ╟─1cc0d686-cf69-443b-94e7-1c311b7c02ab
# ╟─bbe31497-8b9c-4d6e-87b5-d0adf2bc8f5a
# ╟─2580129c-f92b-4ec3-a415-6d685f97111f
# ╟─3a9666e9-b549-4038-887a-4142b24af61e
# ╟─3e1b4956-7986-4835-bd11-4985ced5ab6a
# ╟─2573ea72-8716-4575-90db-e533a59bde14
# ╟─5cf627ef-0c52-4e11-862a-de04f233f6be
# ╟─141f72b9-c606-4871-b374-db1076b520f6
# ╟─289d89e7-3b25-4f9d-b86f-156db859801c
# ╟─502d45d4-ec81-4b3f-8e4b-ce708843af4d
# ╟─32a96882-eec2-4da6-b765-591fb72e7d33
# ╟─8549a117-88a6-4e38-a99d-5bb6d66647a6
# ╟─086b52fb-24e8-4e5a-9a00-3d568cea960f
# ╟─5843e3ad-d3b4-4ee1-aa96-dc2f6734d57c
# ╟─37302c26-5411-4e62-9c14-b3536628d6f8
# ╟─eb08ffb6-faf4-44cf-a03a-f698c314df0c
# ╟─0193bc92-9fdd-49ff-b63c-71230af0f036
# ╟─b34bef02-5d88-4648-b3fa-3e06fb06f434
# ╟─788be74d-10e4-49ff-b6c4-0de59d38a7cc
# ╟─01512d62-9e0a-4332-9376-80faca75cc3e
# ╟─a06b18f7-002d-4fa7-85f1-3800aab7dc9d
# ╟─dbc6dee1-b373-419a-bfb0-60a7b95447e3
# ╟─0fba673c-614c-4948-9889-140f4eebfbf3
# ╟─5aa0b173-f415-4157-a17b-dcf7cb07b79b
# ╟─04f47231-7396-4c72-ac20-4fa02212c383
# ╟─30f405b7-fc11-4857-b144-ee88e0b0717c
# ╟─ef8e069f-c3de-4643-aa33-4c3fb594ccdb
# ╟─2cf03f51-d574-4efe-9546-32907e66852a
# ╠═6ce28ce9-26f1-479a-b093-1e8a61ca16f5
# ╟─f3e6a555-3d38-4325-afbf-5ff8dc0e3c52
# ╟─6ee9a581-0b61-4f87-8d48-6769dc0d25b1
# ╟─63b6571d-4021-438a-8cfe-bf4a3944e8cb
# ╟─e724289a-bbc2-4752-9904-d69845457540
# ╟─a794d0e0-5598-446a-b37f-4bbced8c0254
# ╟─0de8e1b6-8eac-4a5a-83b4-3313916e34e7
# ╟─188171e4-f6e3-4847-83ff-d85cb1677562
# ╟─cbb87f4d-573e-4ea0-8182-4a69d3401eab
# ╟─0449916f-0d03-42c5-8f6d-61bb15064305
# ╟─116140ef-907c-4b59-9238-93d9674f1233
# ╟─d09a3d1e-9e20-4197-ad4b-cdd63fae6772
# ╟─b00c3786-23a6-468a-b960-8e560e38695e
# ╟─ba22e820-9c8c-485c-8205-9c2e64108842
# ╟─778f2336-fea5-41bf-ae80-e0fca9a84678
# ╟─3c4a347d-b8a5-4b83-a48e-460e8ddcac76
# ╟─81ce007c-359e-407b-8f93-82428048c974
# ╟─51f0acab-0cf4-431d-a756-85f47a95a46b
# ╟─62fa4585-9438-49cb-843d-5242d62f0271
# ╟─f4389c9a-6173-4678-8dbe-f8f132de23fe
# ╟─90f96e72-8c73-4511-8354-c41ba2cf6953
# ╟─e7c54ff8-5fbb-49a5-84d6-1f426e472f1c
# ╟─07f5624f-260f-4738-8616-a4c6f74cf7c0
# ╟─c590ff79-7ae2-4b94-9981-52e94d56e8ff
# ╟─1468cf1d-9d4b-45fa-897a-bfeecd51772c
# ╠═38f5ac07-f21d-4792-8966-1bc92b4d7ef0
# ╟─8496b0d6-12b9-4728-bc91-c5b8f56ea739
# ╟─453c9c94-c56c-4208-9171-e9244cc94295
# ╟─3f07ba26-441c-4c21-a139-3adf298d765b
# ╟─145e4c65-9e3b-4c8b-9c40-f41892fc9d7c
# ╟─ee30e1f0-9f93-4af6-b51e-4df0de63afad
# ╟─e7340cda-92b7-4496-a47b-a733cc2a59b9
# ╟─bb984796-fb9f-4f93-81c8-629d1107c52e
# ╟─c009f68e-9d39-4d41-8f47-0620ddae717c
# ╟─8048479d-5a08-401b-a1a0-b7c501b82927
# ╟─514df2eb-a1f9-4665-927c-7d74aa2f1505
# ╟─603d216a-0ec9-4631-ad5a-0dc1221b4a0d
# ╟─d9ea4012-45ee-4baf-bf4f-a2b0ec71b69c
# ╟─7c63a28c-9599-44eb-a144-45ec2eff4dfb
# ╟─f72fd27b-3f9a-4f3f-a412-71b37797d4dd
# ╟─81ba5f86-6762-4b8f-ba64-a4779c7c65d1
# ╟─23eead02-a4bd-43b3-9dfb-0f83a9acc3ef
# ╟─21a292db-3871-4133-8396-67e5ebc1c509
# ╟─0b4e7950-5e5b-4056-987e-c6d93546bd48
# ╟─e4399d37-e193-4d64-9280-6356cb84fb71
# ╟─8fd03ee5-78d1-495b-ae4c-6d01235cb6a6
# ╟─35319d90-67ca-48a3-b04d-db0d9853a59d
# ╟─d231762e-fb25-45f3-bb1c-6dc06392959c
# ╟─75dfb55f-9737-4286-b093-4992f87e346d
# ╟─f61f9db3-b6a5-4dbf-a195-3d9cb3cbf9b3
# ╟─aa287c53-48ea-4bc6-98be-309b6e89785d
# ╟─8903b303-2926-4064-9a58-d9d6329883fd
# ╟─44674e1a-e2ae-415a-802d-740751cd0949
# ╟─ae6a2835-6b02-4e7f-986a-e5ccfc728f93
# ╟─a5fff464-9b3e-4cdd-9cf9-332736269ff7
# ╟─153ad89f-de01-4963-91cb-fe2c2b842eb9
# ╟─9092b7a7-d5bd-45bc-99a1-19f545aacb1d
# ╟─7b4b1265-83af-42c6-86dc-70126460bfde
# ╟─9c00f83b-e97a-42ec-bc7f-5c95138d100f
# ╟─a015fdca-02e6-44ab-912d-e3c1efec2eef
# ╟─4c5b357e-d4c5-4f72-8b35-bbd1824da232
# ╟─6c1c43e7-96d9-4c70-bc95-dfe683d4af7e
# ╟─be5a0d38-f24b-40ac-92a0-faf9e608024e
# ╟─296f430f-7129-4d8f-84b2-6c398efb4ebe
# ╟─5e7de748-ad79-4aff-a1fb-040c8099d0b1
# ╟─4ccca494-91ef-4b11-831a-d4229e1eb5c5
# ╟─f73f3507-03ac-4957-9cba-082b61d462ef
# ╟─9b7feb58-6779-4137-aacd-200caec77965
# ╠═d8633435-5c37-4d78-89da-001efbfa6829
# ╟─ef25478e-e577-4e3c-8de8-df0f4de115e3
# ╟─1e6dff27-ccba-48c8-b015-411b334e63bb
# ╟─4c25ea05-a4b0-4cb3-98f0-b19ffb75f2a8
# ╠═8fbc2beb-1655-4bd9-8003-ee4865f37e52
# ╠═91e6d916-bf2e-4565-b408-b5669b30fe80
# ╟─8c993fe9-2719-4825-adf7-fc07c43b349d
# ╟─c0c22c1f-7508-40bd-bda7-afaeda8d58b2
# ╟─607711f0-d4bf-44ae-a7b9-06aadd057b63
# ╟─8e7dba6d-8f35-47d8-afda-2c36d1313a4a
# ╟─93c6323a-7dac-4174-aea5-139cc38283f4
# ╟─61a15261-b13f-46a5-9a01-3c18d0245e23
# ╠═e9b56895-7ea0-4ac6-90df-4b77bfa30e02
# ╟─877346f2-d025-4330-adaa-7585af22a653
# ╟─18cfedaa-67af-4b96-8dd5-fe7173c47ffa
# ╟─bfb3dc19-2d4c-43f4-84f0-fdeffcf2fb61
# ╟─50a8398c-792a-4d2b-9899-4dafaa188c24
# ╟─d237deda-a25d-45d3-817a-7019dd0dd15c
# ╟─f48ab57e-5ca7-4be8-af30-a6626dd9ed40
# ╟─7828063d-2948-4562-bf4a-78a47f763040
# ╟─e9939368-a08f-4994-a823-c1b6b72b9814
# ╟─b6dd8143-2486-47b9-899d-710bf2180e2a
# ╟─e2362438-85c6-48ff-b842-9d1be1b38eaf
# ╟─6fe18bac-716d-459c-a19a-c429fb96e199
# ╟─d685f0c8-c242-40af-a0bd-be0f8154fb9b
# ╟─bd25ad8a-5b8a-4a03-9305-94e87005b288
# ╟─1e8bb19b-cec6-4eb2-9f5f-2d47485c1e83
# ╟─22670544-e631-4ebb-8bdb-9c6bf28f9c33
# ╟─09715306-246e-433f-9909-a9ee69b7d010
# ╟─6626a65f-59ca-40b1-9f8c-de50e490af9c
# ╟─bcca6c59-34da-40e8-aa8b-12f4fe8514a2
# ╟─f77643c0-5d88-4c18-88e9-0b1a1878656a
# ╟─6bb57b4f-88e6-4b9f-b233-a9ddf19486b1
# ╟─c68d80bc-5fba-46b9-85e2-6711c21a2478
# ╟─56ab33eb-b6a7-4471-b498-67dd7a8d8a6e
# ╟─d19137e6-07cd-4149-bfd7-77fb3dbecdba
# ╠═4714c1b3-faf8-4ade-8a4b-2359bb0b2bb4
# ╠═742f5961-f239-4f97-bf90-d792f551edcf
# ╠═db0032c5-4c5c-430e-bf31-988f90adf32e
# ╠═4c6855a3-d121-40e5-96a6-6b06335762d1
# ╠═24a69164-7dbc-4c82-87c9-451417290b5e
# ╟─e0450f6b-537f-4236-879d-54a4cdf9deb7
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002

```
