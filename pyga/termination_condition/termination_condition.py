class TerminationCondition:
    """
    Abstract class.
    """
    def should_terminate(self, population):
        """
        Executed by EvolutionEngine to determine when to end process. Returns True if evolution process should be
        terminated.

        :param population: Population
        :return: boolean
        """
        raise NotImplementedError()
