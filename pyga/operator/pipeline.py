from pyga.exception import ValidationException
from .evolutionary_operator import EvolutionaryOperator


class PipelineOperator(EvolutionaryOperator):
    def __init__(self):
        super().__init__()
        self.operators = []

    def append_operator(self, operator):
        if not isinstance(operator, EvolutionaryOperator):
            raise ValidationException('Operator must be type of EvolutionaryOperator.')
        self.operators.append(operator)

    def apply(self, selected_candidates):
        for operator in self.operators:
            selected_candidates = operator.apply(selected_candidates)
        return selected_candidates
