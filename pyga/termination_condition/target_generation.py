from .termination_condition import TerminationCondition


class TargetGeneration(TerminationCondition):
    def __init__(self, target_generation, engine):
        self.target_generation = target_generation
        self.engine = engine

    def should_terminate(self, population):
        """
        Executed by EvolutionEngine to determine when to end process. Returns True if evolution process should be
        terminated.

        Return True when generation reaches target_generation.

        :param population: Population
        :return: boolean
        """
        return self.engine.generation >= self.target_generation
