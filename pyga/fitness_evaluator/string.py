from ..common import Fitness
from .fitness_evaluator import FitnessEvaluator


class StringFitnessEvaluator(FitnessEvaluator):
    """
    Implementation of FitnessEvaluator to calculate fitness for Candidate objects with string data.

    :param target_string: string to which candidate data will be compared to
    """
    def __init__(self, target_string):
        super().__init__()
        self.target_string = target_string

    def get_fitness(self, candidate, population):
        """
        Score how good candidate matches target_string. Fitness value is equal to the number of characters that match
        target_string.

        :param candidate: Candidate
        :param population: Population
        :return: Fitness (value is int from 0 to length of target_string)
        """
        matches = 0
        candidate_string = candidate.data
        for i in range(len(candidate_string)):
            if candidate_string[i] == self.target_string[i]:
                matches += 1
        return Fitness(matches)
