import matplotlib.pyplot as plt
from utils import d_a, plot_rule, max

y = [0, 1.0, 1.0, 0]
ng = [-1.0, -1.0, -0.7, -0.5]
np = [-0.7, -0.5, -0.2, 0]
ce = [-0.2, 0, 0, 0.2]
pp = [0.0, 0.2, 0.5, 0.7]
pg = [0.5, 0.7, 1.0, 1.0]
"""
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
"""
"""
plot_rule(d_a(ng, np), d_a(ng, np), 1)
plot_rule(d_a(np, pg), ng, 2)
plot_rule(d_a(pp, pg), np, 3)
plot_rule(ce, np, 4)
plot_rule(ce, pp, 5)
plot_rule(d_a(ng, np), pp, 6)
plot_rule(d_a(ng, pp), ng, 7)
plot_rule(d_a(pp, pg), d_a(pp, pg), 8)
"""

a = [0.1,0.2,0.3,0.4]
b = [0.1,0.2,0.4,0.5]
print(max(a,b))
plt.figure()
plt.plot(a,y)
plt.plot(b,y)
#plt.plot(max(a,b), y)
plt.grid()
plt.show()





