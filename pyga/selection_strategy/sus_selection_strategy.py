from ..exception import ValidationException
from .roulette_wheel_selection_strategy import RouletteWheelSelectionStrategy


class StochasticUniversalSamplingSelectionStrategy(RouletteWheelSelectionStrategy):
    '''
    Stochastic universal sampling
    https://en.wikipedia.org/wiki/Stochastic_universal_sampling
    '''
    def __init__(self, random):
        super().__init__(random)

    def select(self, population, is_natural, selection_size):
        if selection_size < 1:
            raise ValidationException('selection_size must not be lower then 1')
        if len(population) < selection_size:
            raise ValidationException('selection_size is greater then Population size')
        self._is_natural = is_natural

        distance = self.get_fitness_sum(population) / selection_size
        start = self.random.float() * distance
        pointers = [start + i * distance for i in range(selection_size)]
        return self.rns(population, pointers)
