## Modelos probabilísticos de Señales y Sistemas - IE0405
### Tarea 3
### Alan Umaña Castillo
### B77773

#### Inciso a):

&nbsp;&nbsp;&nbsp;&nbsp; Inicialmente, mediante **Pandas** se lee el archivo *xy.csv* y se crea un DataFrame con el nombre de *data*. Posteriormente, mediante la función *.sum* de **Pandas** se realiza la suma de cada *X* para todo *Y*, y de cada *Y* para todo *X*, esto con el fin de obtener las funciones de densidad marginales a partir de los datos suministrados. Finalmente, se guardan estos valores en arrays de *NumPy* llamados *xmarginal* y *ymarginal* respectivamente. 

&nbsp;&nbsp;&nbsp;&nbsp; Estos arrays son graficados en forma de histograma para determinar la forma de la función de distribución que modela los datos. De dichos histogramas, se observa que ambas distribuciones son similares a la distribución Gaussiana o normal.

&nbsp;&nbsp;&nbsp;&nbsp; Una vez hecho esto, se define una función llamada *gaussian*, la cual recibe un dominio *x*, la media y la desviación estándar de un conjunto de datos, y devuelve el valor de probabilidad de acuerdo a lo recibido en el argumento de la función. Ahora, mediante los arrays *xmarginal* y *ymarginal*, y la función anteriormente definida, se utiliza el método *optimize.curve_fit*, para obtener los parámetros de la función marginal (![formula](https://render.githubusercontent.com/render/math?math=\mu_x,\sigma_x,\mu_y,\sigma_y)) de cada variable aleatoria en el intervalo en el que se dan los datos. Este proceso arroja los siguiente resultados:

![formula](https://render.githubusercontent.com/render/math?math=\mu_x=9.904843809352778)

![formula](https://render.githubusercontent.com/render/math?math=\sigma_x=3.2994428756632264)

![formula](https://render.githubusercontent.com/render/math?math=\mu_y=15.07946090037476)

![formula](https://render.githubusercontent.com/render/math?math=\sigma_y=6.026937757836623)

#### Inciso b):

&nbsp;&nbsp;&nbsp;&nbsp; Para la función de desidad conjunta, ya que se asume independencia entre X y Y, se tendría que:

![formula](https://render.githubusercontent.com/render/math?math=f_{X,Y}(x,y)=f_{X}(x)f_{Y}(y))

&nbsp;&nbsp;&nbsp;&nbsp; Dado que se tienen funciones de densidad de probabilidad normales tanto para X como para Y:

![formula](https://render.githubusercontent.com/render/math?math=f_{X,Y}(x,y)=\frac{1}{\sqrt{2\pi}\sigma_x}e^{-\frac{(x-\mu_x)^2}{2\sigma_x^2}}\cdot\frac{1}{\sqrt{2\pi}\sigma_y}e^{-\frac{(y-\mu_y)^2}{2\sigma_y^2}})

&nbsp;&nbsp;&nbsp;&nbsp; Simplificando:

![formula](https://render.githubusercontent.com/render/math?math=f_{X,Y}(x,y)=\frac{1}{2\pi\sigma_x\sigma_y}e^{-\frac{(x-\mu_x)^2}{2\sigma_x^2}-\frac{(y-\mu_y)^2}{2\sigma_y^2}})

#### Inciso c):

&nbsp;&nbsp;&nbsp;&nbsp; Para calcular la correlación, se definió una función llamada *correlacion*, la cual recibe un dominio *x*, un ámbito *y*, dos medias ![formula](https://render.githubusercontent.com/render/math?math=\mu_x,\mu_y), y dos desviaciones estándar ![formula](https://render.githubusercontent.com/render/math?math=\sigma_x,\sigma_y). Esta función se encarga de calcular la integral

![formula](https://render.githubusercontent.com/render/math?math=R_{XY}=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\frac{xy}{2\pi\sigma_x\sigma_y}e^{-\frac{(x-\mu_x)^2}{2\sigma_x^2}-\frac{(y-\mu_y)^2}{2\sigma_y^2}}dydx)

mediante dos ciclos anidados.

&nbsp;&nbsp;&nbsp;&nbsp; Para un dominio de 0 a 1000, un ámbito de 0 a 1000, y los valores de ![formula](https://render.githubusercontent.com/render/math?math=\mu_x,\sigma_x,\mu_y) y ![formula](https://render.githubusercontent.com/render/math?math=\sigma_y) obtenidos en el inciso a), se obtiene que:


![formula](https://render.githubusercontent.com/render/math?math=R_{XY}=149.19466184953106)

&nbsp;&nbsp;&nbsp;&nbsp; Ahora, analizando la ecuación planteada para el cálculo de la correlación se tendria que:

![formula](https://render.githubusercontent.com/render/math?math=R_{XY}=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\frac{xy}{\sqrt{2\pi}^2\sigma_x\sigma_y}e^{-\frac{(x-\mu_x)^2}{2\sigma_x^2}-\frac{(y-\mu_y)^2}{2\sigma_y^2}}dydx)





