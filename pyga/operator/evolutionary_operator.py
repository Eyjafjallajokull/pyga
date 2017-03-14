class EvolutionaryOperator:
    """
    Abstract class for all implementations of operators.
    """
    def apply(self, selected_candidates):
        """
        Perform mutation, crossover or any other operation on given candidates.

        Can return the same or new instance of population.

        :param selected_candidates: Population
        :return: Population
        """
        raise NotImplementedError()
