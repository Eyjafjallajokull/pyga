from copy import deepcopy

from pyga.exception import ValidationException
from .selection_strategy import SelectionStrategy
from ..population import Population


class TruncationSelectionStrategy(SelectionStrategy):
    def __init__(self):
        super().__init__()

    def select(self, population, selection_size):
        return Population([deepcopy(population[-i-1]) for i in range(selection_size)])
