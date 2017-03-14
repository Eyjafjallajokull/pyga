class FitnessEvaluator:
    """
    Abstract class for fitness calculators.
    """
    def __init__(self):
        self.is_natural = True

    def get_fitness(self, candidate, population):
        """
        Calculate fitness value for given candidate. Inheriting classes should return Fitness instance with specified
        value.

        If particular case requires reversed fitness values - the lower the better. Then all values should be negative
        and property ``is_natural`` in Fitness instance should be set to False.

        :param candidate: Candidate
        :param population: Population
        :return: Fitness
        """
        raise NotImplementedError()
