from .termination_condition import TerminationCondition


class TargetFitness(TerminationCondition):
    def __init__(self, target_fitness):
        self.target_fitness = target_fitness

    def should_terminate(self, population):
        """
        Executed by EvolutionEngine to determine when to end process. Returns True if evolution process should be
        terminated.

        Return True when populations best candidate has fitness equal to target_fitness.

        :param population: Population
        :return: boolean
        """
        best_fitness = population.get_best().fitness
        if best_fitness.is_natural:
            return best_fitness >= self.target_fitness
        else:
            return best_fitness <= self.target_fitness
