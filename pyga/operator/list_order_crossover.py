from .list_crossover import ListCrossover
from copy import copy


class ListOrderCrossover(ListCrossover):
    """
    Partially Mapped Cross-over (PMX) algorithm

    Designed for lists of unique items for which order is important.

    :param probability: Probability
    :param random: Random
    """
    def __init__(self, probability, random):
        super().__init__(probability, random, 2)

    def mate_lists(self, parent_list1, parent_list2):
        """
        Crossover two lists.

        :param parent_list1: list
        :param parent_list2: list
        :return: list, list
        """
        indexes = [self.random.int(0, len(parent_list1)-1) for _ in range(self.crossover_points)]
        indexes.sort()
        list1 = copy(parent_list1)
        list2 = copy(parent_list2)
        for j in range(indexes[0], indexes[1]):
            tmp = list1[j]
            list1[j] = list2[j]
            list2[j] = tmp
        list1 = self.legalize_offspring_list(list1, parent_list1, indexes)
        list2 = self.legalize_offspring_list(list2, parent_list2, indexes)
        return list1, list2

    def legalize_offspring_list(self, subject, other, segment):
        """
        After initial crossover, lists may not contain all items, and some
        will be repeated. This method fixes subject list.

        :param subject: list
        :param other: list
        :param segment: list
        :return: list
        """
        s0 = segment[0]
        s1 = segment[1]
        for n in range(s0, s1):
            if other[n] not in subject[s0:s1]:
                i = other[n]
                j = subject[n]
                index_of_j_in_other = other.index(j)
                if index_of_j_in_other < s0 or index_of_j_in_other >= s1:
                    subject[index_of_j_in_other] = i
                else:
                    k = subject[index_of_j_in_other]
                    index_of_k_in_other = other.index(k)
                    subject[index_of_k_in_other] = i
        return subject
