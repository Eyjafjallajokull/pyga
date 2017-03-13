from .evolutionary_operator import EvolutionaryOperator


class StringMutationOperator(EvolutionaryOperator):
    def __init__(self, alphabet, probability, random):
        super().__init__()
        self.alphabet = alphabet
        self.probability = probability
        self.random = random

    def apply(self, selected_candidates):
        for candidate in selected_candidates:
            candidate.data = self.mutate(candidate.data)
        return selected_candidates

    def mutate(self, string):
        mutated = list(string)
        for i in range(len(mutated)):
            if self.probability.get_boolean():
                mutated[i] = self.random.choice(self.alphabet)
        return ''.join(mutated)
