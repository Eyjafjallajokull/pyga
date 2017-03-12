from .termination_condition import TerminationCondition


class TargetGeneration(TerminationCondition):
    def __init__(self, target_generation, engine):
        self.target_generation = target_generation
        self.engine = engine

    def should_terminate(self, population):
        return self.engine.generation >= self.target_generation
