from .termination_condition import TerminationCondition


class Stagnation(TerminationCondition):
    """
    Implements TerminationCondition to terminate evolution when there is no increase of best fitness value.

    :param max_fitness_age: int number of generations after which to terminate
    :param use_average: bool when False - measuring best fitness, when False - measuring average population fitness
    """
    def __init__(self, max_fitness_age, use_average=False):
        self.use_average = use_average
        self.max_fitness_age = max_fitness_age
        self.best_fitness = None
        self.best_fitness_age = None

    def should_terminate(self, population):
        """
        Executed by EvolutionEngine to determine when to end process. Returns True if evolution process should be
        terminated.

        Returns True when populations best fitness did't change for subsequent max_fitness_age generations.

        Note: this method has internal counter of generations, each function call increases counter by one.

        :param population: Population
        :return: boolean
        """
        current_best_fitness = population.get_best().fitness
        if self.best_fitness is None or self.best_fitness != current_best_fitness:
            self.best_fitness = current_best_fitness
            self.best_fitness_age = 1
        else:
            self.best_fitness_age += 1
        return self.max_fitness_age <= self.best_fitness_age

