from copy import deepcopy

from pyga.exception import ValidationException
from .selection_strategy import SelectionStrategy
from ..population import Population


class RouletteWheelSelectionStrategy(SelectionStrategy):
    def __init__(self, random):
        super().__init__()
        self.random = random
        self._is_natural = None

    def select(self, population, is_natural, selection_size):
        if selection_size < 1:
            raise ValidationException('selection_size must not be lower then 1')
        if len(population) < selection_size:
            raise ValidationException('selection_size is greater then Population size')
        self._is_natural = is_natural

        fitness_sum = 0
        for candidate in population:
            fitness_sum += self.get_normal_fitness(candidate)

        probabilities = [self.get_normal_fitness(population[0]) / fitness_sum]
        for i in range(1, len(population)):
            probabilities.append(probabilities[i-1] + self.get_normal_fitness(population[i]) / fitness_sum)

        selected = Population()
        for _ in range(selection_size):
            rand = self.random.float()
            for i in range(len(probabilities)):
                if rand < probabilities[i]:
                    selected.append(deepcopy(population[i]))
                    break
        return selected

    def get_normal_fitness(self, candidate):
        if self._is_natural:
            return candidate.fitness
        else:
            return -candidate.fitness
