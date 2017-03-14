from .termination_condition import TerminationCondition


class Multicondition(TerminationCondition):
    """
    Can be used to create advanced termination strategies. You can attach any number of TerminationConditions. For example::

        mc = Multicondition(logic=Multicondition.LOGIC_OR)
        mc.add(TimeLimit(30))
        mc.add(TargetFitness(100))
        mc.should_terminate(population) # will return True when 30s pass or best candidate fitness is 100

    """
    LOGIC_AND = 1
    LOGIC_OR = 2

    def __init__(self, logic=LOGIC_AND):
        """
        :param logic: LOGIC_OR or LOGIC_AND
        """
        self.subconditions = []
        self.logic = logic

    def add(self, subcondition):
        """
        Add TerminationCondition instance to the pool.

        :param subcondition: TerminationCondition
        """
        if not isinstance(subcondition, TerminationCondition):
            raise TypeError('subcondition must be of type TerminationCondition')
        self.subconditions.append(subcondition)

    def should_terminate(self, population):
        """
        Executed by EvolutionEngine to determine when to end process. Returns True if evolution process should be
        terminated.

        When logic is LOGIC_AND -- Returns True when all sub-conditions are True
        When logic is LOGIC_OR -- Returns True when any sub-conditions is True

        :param population: Population
        :return: boolean
        """
        for subcondition in self.subconditions:
            subcondition_result = subcondition.should_terminate(population)
            if self.logic == self.LOGIC_AND:
                if not subcondition_result:
                    return False
            elif self.logic == self.LOGIC_OR:
                if subcondition_result:
                    return True

        if self.logic == self.LOGIC_AND:
            return True
        elif self.logic == self.LOGIC_OR:
            return False
