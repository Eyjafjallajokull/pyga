from ..exception import ValidationException
from .crossover import CrossoverOperator


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

    def validate_parents(self, parent1, parent2):
        """
        Validate parents before mating.

        :param parent1: Candidate
        :param parent2: Candidate
        :raises ValidationException:
        """
        if len(parent1.data) != len(parent2.data):
            raise ValidationException('candidate data has different lengths')
