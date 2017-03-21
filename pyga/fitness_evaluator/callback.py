from .fitness_evaluator import FitnessEvaluator


class CallbackFitnessEvaluator(FitnessEvaluator):
    """
    Implementation of FitnessEvaluator to calculate fitness using delegate function.

    :param callback: function which will be called to calculate fitness, it should return Fitness object
    """
    def __init__(self, callback):
        super().__init__()
        self.callback = callback

    def get_fitness(self, candidate, population):
        """
        Execute callback function to get fitness value for given candidate.

        :param candidate: Candidate
        :param population: Population
        :return: Fitness (value is int from 0 to length of target_string)
        """
        return self.callback(candidate, population)
