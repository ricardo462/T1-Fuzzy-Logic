from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
y = [0, 1.0, 1.0, 0]
ng = [-1.0, -1.0, -0.7, -0.5]
np_ = [-0.7, -0.5, -0.2, 0]
ce = [-0.2, 0, 0, 0.2]
pp = [0.0, 0.2, 0.5, 0.7]
pg = [0.5, 0.7, 1.0, 1.0]
# defining plot size
plt.figure(figsize = (10, 5))
 
# specifying plot coordinates
plt.plot(ng, y, label='ng')
plt.plot(np_, y, label='np')
plt.plot(ce, y, label='ce')
plt.plot(pp, y, label='pp')
plt.plot(pg, y, label='pg')
plt.legend()
plt.title('Funciones de pertenencia difusos')
plt.ylabel('Grado de pertenencia')
plt.grid()

plt.show()