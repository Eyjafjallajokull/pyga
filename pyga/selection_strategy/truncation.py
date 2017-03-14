from copy import deepcopy

from .selection_strategy import SelectionStrategy
from ..population import Population


class TruncationSelectionStrategy(SelectionStrategy):
    """
    Implementation of truncation selection.
    """
    def select(self, population, selection_size):
        """
        Return only the best candidates.

        :param population: Population
        :param selection_size: int
        :return: Population
        """
        return Population([deepcopy(population[-i-1]) for i in range(selection_size)])
