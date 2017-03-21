from .mutation import Mutation


class BitStringMutation(Mutation):
    def __init__(self, probability, random):
        super().__init__()
        self.probability = probability
        self.random = random

    def mutate(self, string):
        mutated = list(string)
        for i in range(len(mutated)):
            if self.probability.get_boolean():
                mutated[i] = str(round(self.random.float()))
        return ''.join(mutated)
