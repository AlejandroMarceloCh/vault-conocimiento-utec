---
curso: IO2
titulo: SISTEMASEDO
slides: 0
fuente: SISTEMASEDO.Rmd
---

<!-- INTERPRETAR-POR-COMPOSER: este capítulo es PLACEHOLDER. Reescribí el cuerpo
     (qué es, qué enseña, para qué sirve en un proyecto real) en 150-250 palabras
     y dejá el bloque de código/data/tabla AL FINAL (trazabilidad). Fuente: SISTEMASEDO.Rmd. -->

<!-- INTERPRETAR: material de formato .rmd (SISTEMASEDO.Rmd). El capítulo debe ser una interpretación
     (qué es, qué contiene, qué enseña, para qué sirve en el curso), no el volcado. -->

---
title: "R Notebook"
output: html_notebook
---

```{r}

library(deSolve)

my_ode = function(t,state,parms){ 

  
  with(as.list(state,parms),{

#------------------------------------- 
   #Escribir las ecuaciones a continuación: (Los estados iniciales deberán ingresarse en el orden de las ecuaciones)
    
    dx = x-2*y
    dy = 2*x+y
    

    list(c(dx,dy))  #Escribir el retorno de las ecuaciones respetando el orden en el que se ingresaron arriba
    
#-------------------------------------
  })
}

resp <- function(DF,c,t){
  return(DF[which(DF[,1]==t) , c])
}

```


```{r}

init = c(x=1,y=0) #Ingresar los estados iniciales en el orden de las ecuaciones

out = ode(y=init,times=seq(0,100,0.01),func=my_ode) #Pueden cambiar los valores que se mostrarán del tiempo: seq(1er valor de t, último valor de t, aumento)   El aumento significa en cuanto irá avanzando el t, por ejemplo si ponen el valor de 0.1 tendrán 1.1 -> 1.2 -> 1.3, mientras que si el avance es 0.01 tendrán 1.01->1.02->1.03.

plot(out,type="l") 

```



```{r}

#resp(no tocar, variable, tiempo)
resp(out,"y",5)  

```
