from copy import deepcopy

from pyga.exception import ValidationException
from .selection_strategy import SelectionStrategy
from ..population import Population


class TruncationSelectionStrategy(SelectionStrategy):
    def __init__(self):
        super().__init__()

    def select(self, population, selection_size):
        if selection_size < 1:
            raise ValidationException('selection_size must not be lower then 1')
        if len(population) < selection_size:
            raise ValidationException('selection_size is greater then Population size')

        return Population([deepcopy(population[-i-1]) for i in range(selection_size)])
