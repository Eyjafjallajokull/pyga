from pyga.operator.mutation import Mutation


class ListOrderMutation(Mutation):
    """
    Mutate order on candidate which has data of list type.

    :param mutations: int
    :param probability: Probability
    :param random: Random
    """
    def __init__(self, probability, random, mutations):
        super().__init__()
        self.mutations = mutations
        self.probability = probability
        self.random = random

    def mutate(self, subject):
        """
        Perform order mutation on list.

        :param subject: list
        :return: list
        """
        for _ in range(self.mutations):
            a, b = sorted([self.random.int(0, len(subject) - 1),
                           self.random.int(0, len(subject) - 1)])
            tmp = subject[a]
            subject[a] = subject[b]
            subject[b] = tmp
        return subject
