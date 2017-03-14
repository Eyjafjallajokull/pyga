from ..exception import ValidationException


class SelectionStrategy:
    """
    Abstract class for different implementations of candidate selection algorithms.
    """
    def __init__(self):
        pass

    def select(self, population, selection_size):
        """
        This method is used to by EvolutionEngine to select candidates for next population.

        Important: during selection candidates should be copied using deepcopy function.

        :param population: Population
        :param selection_size: int
        :return: Population
        """
        raise NotImplementedError()

    def validate(self, population, selection_size):
        """
        Method used to validate state of population, before actually performing selection

        :param population: Population
        :param selection_size: int
        :raises ValidationException:
        """
        if selection_size < 1:
            raise ValidationException('selection_size must not be lower then 1')
        if len(population) < selection_size:
            raise ValidationException('selection_size is greater then Population size')