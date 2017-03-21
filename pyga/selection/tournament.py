from copy import deepcopy

from .selection_strategy import SelectionStrategy
from ..population import Population


class TournamentSelection(SelectionStrategy):
    """
    Implementation of tournament selection

    :param tournament_size: int
    :param random: Random
    """
    def __init__(self, tournament_size, random):
        super().__init__()
        self.tournament_size = tournament_size
        self.random = random

    def select(self, population, selection_size):
        """
        :param population: Population
        :param selection_size: int
        :return: Population
        """
        selected = Population()
        for _ in range(selection_size):
            tournament_candidates = Population(self.random.sample(population, self.tournament_size))
            selected.append(deepcopy(tournament_candidates.get_best()))
        return selected
