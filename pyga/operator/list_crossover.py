from ..exception import ValidationException
from .crossover import Crossover


class ListCrossover(Crossover):
    """
    Crossover for candidates which data is represented by lists.
    List items are not evaluated in any way, so it can any type of data.

    :param probability: Probability of crossover occurring for given 2 selected candidates
    :param random: Random
    :param crossover_points: int number of cut points
    """
    def __init__(self, probability, random, crossover_points):
        super().__init__(probability, random)
        self.crossover_points = crossover_points

    def mate(self, parent1, parent2):
        """
        Perform list crossover on two parents.

        :param parent1: Candidate
        :param parent2: Candidate
        :return: Candidate, Candidate
        """
        parent1.data, parent2.data = self.mate_lists(parent1.data, parent2.data)
        return parent1, parent2

    def mate_lists(self, list1, list2):
        """
        Crossover two lists, of any type of data.

        :param list1: list
        :param list2: list
        :return: list, list
        """
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
