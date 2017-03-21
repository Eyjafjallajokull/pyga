from .mutation import Mutation


class StringMutation(Mutation):
    def __init__(self, probability, random, alphabet):
        super().__init__()
        self.alphabet = alphabet
        self.probability = probability
        self.random = random

    def mutate(self, string):
        mutated = list(string)
        for i in range(len(mutated)):
            if self.probability.get_boolean():
                mutated[i] = self.random.choice(self.alphabet)
        return ''.join(mutated)
