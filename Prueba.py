# Librerias Necesarios para Graficar
import math 
import numpy as np
import sympy as sy
from matplotlib import pyplot as plt 

sy.init_printing(use_unicode = False, wrap_line = False)

# Data del Grafico
#x = np.array(range(500))*0.1
#y = np.zeros(len(x))
#
#for i in range(len(x)):
#    y[i] = math.sin(x[i])
#

# Creamos el grafico
#plt.plot(x,y)
#plt.show()

x = sy.Symbol('x')

integral = sy.integrate((x**2 + x + 1), x)
print(sy.integrate((x**2 + x + 1), x))
print(sy.sinc(0))

sy.pprint(integral)