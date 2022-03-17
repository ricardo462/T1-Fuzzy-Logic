import numpy as np
import matplotlib.pyplot as plt
"""
def ng(z1 = -1.0, o1 = -1.0, o2 = -0.7, z2 = -0.5):
    pass


class TrapezoidalFuzzySet:
    def __init__(self, z1, o1, o2, z2) -> None:
        self.z1 = z1
        self.o1 = o1
        self.o2 = o2
        self.z2 = z2

    def evaluate():
        pass
"""
order = {0:0.0, 1:1.0, 2:1.0, 3:0.0}
def pertenencia(value: float, fuzzy_set:list) -> float :
    lenght = len(fuzzy_set)
    for i in range(lenght - 1):
        value_set = fuzzy_set[i]
        if value == value_set:
            return order[i]
        
        next_value_set = fuzzy_set[i+1]
        if value_set < value and value < next_value_set:
            m = (order[i+1] - order[i]) / (next_value_set - value_set)
            return m * (value - value_set) + order[i]
    if value == next_value_set:
        return order[i+1]
"""            
def d_a(fuzzy_set_1:list , fuzzy_set_2:list) -> list:
    result = []
    for i in range(len(fuzzy_set_1)):
        element_1, element_2 = fuzzy_set_1[i], fuzzy_set_2[i]
        element = element_1 if element_1 <= element_2 else element_2
        result.append(element)
    return result
"""
def d_a(fuzzy_set_1:list , fuzzy_set_2:list) -> list:
    result = []
    for i in range(2):
        element_1, element_2 = fuzzy_set_1[i], fuzzy_set_2[i]
        element = element_1 if element_1 <= element_2 else element_2
        result.append(element)

    for i in range(2,4):
        element_1, element_2 = fuzzy_set_1[i], fuzzy_set_2[i]
        element = element_1 if element_1 > element_2 else element_2
        result.append(element)
    return result


ce = [-0.2, 0, 0, 0.2]
pp = [0.0, 0.2, 0.5, 0.7]
y = [0, 1.0, 1.0, 0]

r = d_a(ce, pp)
plt.figure(figsize = (10, 5))
plt.plot(r, y, label='pg')
plt.legend()
plt.title('Funciones de pertenencia difusos')
plt.ylabel('Grado de pertenencia')
plt.grid()

plt.show()