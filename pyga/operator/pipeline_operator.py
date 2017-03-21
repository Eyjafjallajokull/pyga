from ..exception import ValidationException
from .operator import Operator


class PipelineOperator(Operator):
    def __init__(self):
        super().__init__()
        self.operators = []

    def append_operator(self, operator):
        if not isinstance(operator, Operator):
            raise ValidationException('Operator must be type of Operator.')
        self.operators.append(operator)

    def apply(self, selected_candidates):
        for operator in self.operators:
            selected_candidates = operator.apply(selected_candidates)
        return selected_candidates
