from ..common import Fitness
from .fitness_evaluator import FitnessEvaluator


class StringFitnessEvaluator(FitnessEvaluator):
    def __init__(self, target_string):
        super().__init__()
        self.target_string = target_string

    def get_fitness(self, candidate, population):
        matches = 0
        candidate_string = candidate.data
        for i in range(len(candidate_string)):
            if candidate_string[i] == self.target_string[i]:
                matches += 1
        return Fitness(matches)
