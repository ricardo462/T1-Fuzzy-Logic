import matplotlib.pyplot as plt
from utils import d_a, plot_rule, maquina_de_inferencia
import numpy # solo para manejo de arreglos

y = [0, 1.0, 1.0, 0]
ng = [-1.0, -1.0, -0.7, -0.5]
np = [-0.7, -0.5, -0.2, 0]
ce = [-0.2, 0, 0, 0.2]
pp = [0.0, 0.2, 0.5, 0.7]
pg = [0.5, 0.7, 1.0, 1.0]

# defining plot size
plt.figure(figsize = (10, 5))
 
# specifying plot coordinates
plt.plot(ng, y, label='ng')
plt.plot(np, y, label='np')
plt.plot(ce, y, label='ce')
plt.plot(pp, y, label='pp')
plt.plot(pg, y, label='pg')
plt.legend()
plt.title('Funciones de pertenencia difusos')
plt.ylabel('Grado de pertenencia')
plt.grid()

plt.show()

plot_rule(d_a(ng, np), d_a(ng, np), 1)
plot_rule(d_a(np, pg), ng, 2)
plot_rule(d_a(pp, pg), np, 3)
plot_rule(ce, np, 4)
plot_rule(ce, pp, 5)
plot_rule(d_a(ng, np), pp, 6)
plot_rule(d_a(ng, pp), ng, 7)
plot_rule(d_a(pp, pg), d_a(pp, pg), 8)



num_points = 200
E1 = -0.3
E2 = numpy.linspace(-1, 1, num_points)

respuesta = []
for e2 in E2:
    respuesta += [maquina_de_inferencia(E1, e2)]


plt.figure()
plt.plot(E2, respuesta)
plt.title('Respuesta del controlador cuando E1 = -0.3 y E2 varía')
plt.xlabel('E2')
plt.ylabel('Salida')
plt.grid()
plt.show()


E1 = numpy.linspace(-1, 1, num_points)
E2 = 0.6 

respuesta = []
for e1 in E1:
    respuesta += [maquina_de_inferencia(e1, E2)]


plt.figure()
plt.plot(E1, respuesta)
plt.title('Respuesta del controlador cuando E2 = 0.6 y E1 varía')
plt.xlabel('E1')
plt.ylabel('Salida')
plt.grid()
plt.show()


