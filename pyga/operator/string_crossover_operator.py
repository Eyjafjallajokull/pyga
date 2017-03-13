from .list_crossover_operator import ListCrossoverOperator


class StringCrossoverOperator(ListCrossoverOperator):
    def __init__(self, crossover_points, probability, random):
        super().__init__(crossover_points, probability, random)

    def mate(self, parent1, parent2):
        list1, list2 = self.mate_lists(list(parent1.data), list(parent2.data))
        parent1.data = "".join(list1)
        parent2.data = "".join(list2)
        return parent1, parent2
