from .roulette_wheel import RouletteWheelSelectionStrategy


class StochasticUniversalSamplingSelectionStrategy(RouletteWheelSelectionStrategy):
    '''
    Stochastic universal sampling
    https://en.wikipedia.org/wiki/Stochastic_universal_sampling
    '''
    def __init__(self, random):
        super().__init__(random)

    def select(self, population, selection_size):
        self._is_natural = population[0].fitness.is_natural

        distance = self.get_fitness_sum(population) / selection_size
        start = self.random.float() * distance
        pointers = [start + i * distance for i in range(selection_size)]
        return self.roulette(population, pointers)
