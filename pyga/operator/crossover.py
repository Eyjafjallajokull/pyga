from ..population import Population
from .operator import Operator


class Crossover(Operator):
    """
    Abstract class for crossover operators. Uses probability to choose witch candidates will be used as parents to
    create new offspring.

    :param probability: of crossover occurring for given two selected candidates
    :type probability: Probability
    :param random:
    :type random: Random
    """
    def __init__(self, probability, random):
        super().__init__()
        self.probability = probability
        self.random = random

    def apply(self, selected_candidates):
        """
        Perform crossover on given candidates.

        :param selected_candidates: Population
        :return: Population
        """
        self.random.shuffle(selected_candidates)
        result = Population()
        candidates_count = len(selected_candidates)
        for i in range(0, candidates_count-1, 2):
            if self.probability.get_boolean():
                parent1, parent2 = selected_candidates[i], selected_candidates[i+1]
                self.validate_parents(parent1, parent2)
                crossover = self.mate(parent1, parent2)
                result.append_list(crossover)
            else:
                result.append(selected_candidates[i])
                result.append(selected_candidates[i+1])
        if candidates_count % 2 == 1:
            result.append(selected_candidates[-1])
        return result

    def mate(self, parent1, parent2):
        """
        Perform crossover on two parents. Should always produce and return two offspring candidates.

        :param parent1: Candidate
        :param parent2: Candidate
        :return: Candidate, Candidate
        """
        raise NotImplementedError()

    def validate_parents(self, parent1, parent2):
        """
        Validate parents before mating.

        :param parent1: Candidate
        :param parent2: Candidate
        :raises ValidationException:
        """
        pass
