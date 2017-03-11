from .termination_condition import TerminationCondition


class Multicondition(TerminationCondition):
    LOGIC_AND = 1
    LOGIC_OR = 2

    def __init__(self, logic=LOGIC_AND):
        self.subconditions = []
        self.logic = logic

    def add(self, subcondition):
        self.subconditions.append(subcondition)

    def should_terminate(self, population):
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
