# Librerias Necesarios para Graficar
import math 
import numpy as np
from matplotlib import pyplot as plt 

# Data del Grafico
x = np.array(range(500))*0.1
y = np.zeros(len(x))

for i in range(len(x)):
    y[i] = math.sin(x[i])


# Creamos el grafico
plt.plot(x,y)
plt.show()
