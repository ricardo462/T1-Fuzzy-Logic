from typing_extensions import Self


class FuzzySet:
    def __init__(self, z_1, o_1, o_2, z_2) -> None:
        self.z_1 = z_1
        self.o_1 = o_1
        self.o_2 = o_2
        self.z_2 = z_2
        self.set = [z_1, o_1, o_2, z_2]

    def pertenencia(value):
        pass



class TrapeziodalFuzzySet(FuzzySet):
    def __init__(self, z_1, o_1, o_2, z_2) -> None:
        super().__init__(z_1, o_1, o_2, z_2)

    def pertenencia(self, value):
        order = {0:0.0, 1:1.0, 2:1.0, 3:0.0}
        lenght = len(len(self.set))
        for i in range(lenght - 1):
            value_set = self.set[i]
            if value == value_set:
                return order[i]
            
            next_value_set = self.set[i+1]
            if value_set < value and value < next_value_set:
                m = (order[i+1] - order[i]) / (next_value_set - value_set)
                return m * (value - value_set) + order[i]
        if value == next_value_set:
            return order[i+1]


class GammaFuzzySet(FuzzySet):
    def __init__(self, z_1, o_1, o_2, z_2) -> None:
        super().__init__(z_1, o_1, o_2, z_2)

    def pertenencia(value):
        return super().pertenencia()