from .termination_condition import TerminationCondition


class TargetFitness(TerminationCondition):
    def __init__(self, target_fitness):
        self.target_fitness = target_fitness

    def should_terminate(self, population):
        best_fitness = population.get_best().fitness
        if best_fitness.is_natural:
            return best_fitness >= self.target_fitness
        else:
            return best_fitness <= self.target_fitness
