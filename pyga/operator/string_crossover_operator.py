from pyga.operator.crossover_operator import CrossoverOperator


class StringCrossoverOperator(CrossoverOperator):
    def __init__(self, crossover_points, probability, random):
        super().__init__(crossover_points, probability, random)

    def mate(self, parent1, parent2):
        indexes = [self.random.int(0, len(parent1.data)-1) for _ in range(self.crossover_points)]
        indexes.sort()
        string1 = list(parent1.data)
        string2 = list(parent2.data)
        for i in range(len(indexes)):
            for j in range(indexes[i], len(parent1.data)):
                tmp = string1[j]
                string1[j] = string2[j]
                string2[j] = tmp
        parent1.data = "".join(string1)
        parent2.data = "".join(string2)
        return parent1, parent2
