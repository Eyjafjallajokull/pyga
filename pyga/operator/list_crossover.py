from pyga.operator.crossover import CrossoverOperator


class ListCrossoverOperator(CrossoverOperator):
    def __init__(self, crossover_points, probability, random):
        super().__init__(crossover_points, probability, random)

    def mate(self, parent1, parent2):
        list1, list2 = self.mate_lists(parent1.data, parent2.data)
        parent1.data = list1
        parent2.data = list2
        return parent1, parent2

    def mate_lists(self, list1, list2):
        indexes = [self.random.int(0, len(list1)-1) for _ in range(self.crossover_points)]
        indexes.sort()
        for i in range(len(indexes)):
            for j in range(indexes[i], len(list1)):
                tmp = list1[j]
                list1[j] = list2[j]
                list2[j] = tmp
        return list1, list2
