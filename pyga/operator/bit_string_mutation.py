from .evolutionary_operator import EvolutionaryOperator


class BitStringMutationOperator(EvolutionaryOperator):
    def __init__(self, probability, random):
        super().__init__()
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
                mutated[i] = str(round(self.random.float()))
        return ''.join(mutated)
