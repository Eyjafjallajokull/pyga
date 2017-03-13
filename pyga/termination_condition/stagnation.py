from time import time

from .termination_condition import TerminationCondition


class Stagnation(TerminationCondition):
    def __init__(self, max_fitness_age, use_average=False):
        self.use_average = use_average
        self.max_fitness_age = max_fitness_age
        self.best_fitness = None
        self.best_fitness_age = None

    def should_terminate(self, population):
        current_best_fitness = population.get_best().fitness
        if self.best_fitness is None or self.best_fitness != current_best_fitness:
            self.best_fitness = current_best_fitness
            self.best_fitness_age = 1
        else:
            self.best_fitness_age += 1
        return self.max_fitness_age <= self.best_fitness_age

