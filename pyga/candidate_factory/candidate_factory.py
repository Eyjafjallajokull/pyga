from ..population import Population


class CandidateFactory:
    """
    Creates new populations of candidates.

    :param random: Random number generator
    """
    def __init__(self, random):
        self.random = random

    def create_candidate(self):
        """
        Create single candidate instance.

        :return: Candidate
        """
        raise NotImplementedError()

    def create_population(self, size):
        """
        Create population of new candidates.

        :param size: int
        :return: Population
        """
        population = Population()
        for i in range(size):
            population.append(self.create_candidate())
        return population
