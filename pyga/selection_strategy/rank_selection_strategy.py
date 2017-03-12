from pyga.exception import ValidationException
from .roulette_wheel_selection_strategy import RouletteWheelSelectionStrategy


class RankSelectionStrategy(RouletteWheelSelectionStrategy):
    def select(self, population, is_natural, selection_size):
        if selection_size < 1:
            raise ValidationException('selection_size must not be lower then 1')
        if len(population) < selection_size:
            raise ValidationException('selection_size is greater then Population size')
        self._is_natural = is_natural
        self._fitness_sum = None

        max_ = max(self.get_segments(population))
        pointers = [self.random.float() * max_ for _ in range(selection_size)]
        selected = self.roulette(population, pointers)
        return selected

    def get_segments(self, population):
        segments = [1]
        for i in range(1, len(population)):
            segments.append(segments[i - 1] + i)
        return segments
