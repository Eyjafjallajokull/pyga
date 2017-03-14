from copy import deepcopy

from .selection_strategy import SelectionStrategy
from ..population import Population


class RouletteWheelSelectionStrategy(SelectionStrategy):
    """
    Implementation of fitness proportionate selection

    https://en.wikipedia.org/wiki/Fitness_proportionate_selection
    :param random: Random
    """
    def __init__(self, random):
        super().__init__()
        self.random = random
        self._is_natural = None
        self._fitness_sum = None

    def select(self, population, selection_size):
        """
        Select candidates using roulette selection.

        :param population: Population
        :param selection_size: int
        :return: Population
        """
        self._is_natural = population[0].fitness.is_natural
        self._fitness_sum = None

        pointers = [self.random.float() * self.get_fitness_sum(population) for _ in range(selection_size)]
        selected = self.roulette(population, pointers)
        return selected

    def roulette(self, population, points):
        """
        Perform roulette selection.

        :param population: Population
        :param points: list
        :return: Population
        """
        selected = Population()
        segments = self.get_segments(population)
        for rand in points:
            for i in range(len(segments)):
                if rand < segments[i]:
                    selected.append(deepcopy(population[i]))
                    break
        return selected

    def get_segments(self, population):
        segments = [self.get_normal_fitness(population[0])]
        for i in range(1, len(population)):
            segments.append(segments[i - 1] + float(self.get_normal_fitness(population[i])))
        return segments

    def get_normal_fitness(self, candidate):
        """
        Return normalized fitness

        :param candidate: Candidate
        :return: float or int
        """
        if self._is_natural:
            return candidate.fitness
        else:
            return abs(candidate.fitness)

    def get_fitness_sum(self, population):
        if not self._fitness_sum:
            self._fitness_sum = 0
            for candidate in population:
                self._fitness_sum += float(self.get_normal_fitness(candidate))
        return self._fitness_sum
