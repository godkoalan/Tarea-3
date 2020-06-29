import math
import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits import mplot3d
import pandas as pd
import numpy as np
from scipy import optimize
from pylab import meshgrid

datos=pd.read_csv('xy.csv', delimiter=',')
data=pd.DataFrame(datos)

xdata=[]
ydata=[]
prob=[]
with open("xyp.csv") as datos:
    readdatos = csv.reader(datos, delimiter=',')
    for row in readdatos:
        xdata.append(row[0])
        ydata.append(row[1])
        prob.append(row[2])
        
xdata=np.array([float(i) for i in xdata[1:]])
ydata=np.array([float(i) for i in ydata[1:]])
prob=np.array([float(i) for i in prob[1:]])

################################# INCISO A) ###################################

x=data.sum(1)
xmarg=x.values
xmarg = [(float(i)) for i in xmarg]
xmarginal = np.array(xmarg)
xdom=np.arange(len(xmarginal))
xdom=[(i+5) for i in xdom]
xdom=np.array(xdom)

y=data.sum(0)
ymarg=y.values
ymarg = [float(i) for i in ymarg[1:]]
ymarginal = np.array(ymarg)
ydom=np.arange(len(ymarginal))
ydom=[(i+5) for i in ydom]
ydom=np.array(ydom)

plt.bar(xdom, xmarginal, align='center', alpha=0.5, facecolor='cyan', edgecolor='black')
plt.title('Datos marginales de X')
plt.xlabel('X')
plt.ylabel('Densidad de X')
plt.grid(True)
plt.show()

plt.bar(ydom, ymarginal, align='center', alpha=0.5, facecolor='cyan', edgecolor='black')
plt.title('Datos marginales de Y')
plt.xlabel('Y')
plt.ylabel('Densidad de Y')
plt.grid(True)
plt.show()


def gaussian(x, mu, sigma):
    return (1/(np.sqrt(2*math.pi*sigma**2)))*np.exp((-(x-mu)**2/(2*sigma**2)))

parametrosx, covx = optimize.curve_fit(gaussian, xdom, xmarginal)
parametrosy, covy = optimize.curve_fit(gaussian, ydom, ymarginal)

mux=parametrosx[0]
sigmax=parametrosx[1]

muy=parametrosy[0]
sigmay=parametrosy[1]

print("La media de la función de densidad marginal de X es: ", mux)
print("La desviación estándar de la función de densidad de X es: ", sigmax)

print("La media de la función de densidad marginal de Y es: ", muy)
print("La desviación estándar de la función de densidad de Y es: ", sigmay)

###############################################################################

################################# INCISO B) ###################################

# Hecha en GitHub.

###############################################################################

############################## INCISO C) ######################################

xdomi=np.linspace(0,1000,1000)
ydomi=np.linspace(0,1000,1000)
def correlacion(x, y, mu1, sigma1, mu2, sigma2):
    correlacion=0
    for i in x:
        for j in y:
            corre=j*i*((1/(np.sqrt(2*math.pi*sigma2**2)))*np.exp((-(j-mu2)**2/(2*sigma2**2)))*(1/(np.sqrt(2*math.pi*sigma1**2)))*np.exp((-(i-mu1)**2/(2*sigma1**2))))
            correlacion=corre+correlacion
    return correlacion

correlacion=correlacion(xdomi, ydomi, mux, sigmax, muy, sigmay)
print("La correlación de las dos variables aleatorias es: ", correlacion)
covarianza=correlacion-(mux*muy)
print('La covarianza de las variables aleatorias es: ', covarianza)
coefcor=covarianza/(sigmax*sigmay)
print('El coeficiente de correlación de las variables aleatorias es: ', coefcor)


################################### INCISO D) #################################

def gaussmulti(x, y, mu1, sigma1, mu2, sigma2):
    return (1/(np.sqrt(2*math.pi*sigmax**2)))*np.exp((-(x-mux)**2/(2*sigmax**2))) * (1/(np.sqrt(2*math.pi*sigmay**2)))*np.exp((-(y-muy)**2/(2*sigmay**2)))

plt.plot(xdom, gaussian(xdom, mux, sigmax), 'c--', linewidth=2, alpha=0.6)
leyenda=mpatches.Patch(color='cyan', label='Curva de ajuste')
plt.legend(handles=[leyenda])
plt.title('Función de densidad marginal de X')
plt.xlabel('x')
plt.ylabel('fx(x)')
plt.grid(True)
plt.show()

plt.plot(ydom, gaussian(ydom, muy, sigmay), 'c--', linewidth=2, alpha=0.6)
leyenda=mpatches.Patch(color='cyan', label='Curva de ajuste')
plt.legend(handles=[leyenda])
plt.title('Función de densidad marginal de Y')
plt.xlabel('y')
plt.ylabel('fy(y)')
plt.grid(True)
plt.show()

dominio=np.linspace(5,15,100)
ambito=np.linspace(5,25,200)
X, Y = meshgrid(dominio, ambito)
Z = gaussmulti(X, Y, mux, sigmax, muy, sigmay)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='cool',linewidth=0, antialiased=False)
plt.title('Función de densidad conjunta')
plt.xlabel('X')
plt.ylabel('Y')
plt.zlabel('Densidad de datos')
plt.grid(True)
plt.show()
