from ..population import Population
from .evolutionary_operator import EvolutionaryOperator


class CrossoverOperator(EvolutionaryOperator):
    def __init__(self, crossover_points, probability, random):
        super().__init__()
        self.crossover_points = crossover_points
        self.probability = probability
        self.random = random

    def apply(self, selected_candidates):
        self.random.shuffle(selected_candidates)
        result = Population()
        candidates_count = len(selected_candidates)
        for i in range(0, candidates_count-1, 2):
            if self.probability.get_boolean():
                crossover = self.mate(selected_candidates[i], selected_candidates[i+1])
                result.append_list(crossover)
            else:
                result.append(selected_candidates[i])
                result.append(selected_candidates[i+1])
        if candidates_count % 2 == 1:
            result.append(selected_candidates[-1])
        return result

    def mate(self, parent1, parent2):
        raise NotImplementedError()
