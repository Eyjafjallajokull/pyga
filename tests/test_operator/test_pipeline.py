from unittest import TestCase
from unittest.mock import MagicMock

from pyga import Candidate
from pyga import Operator
from pyga import PipelineOperator
from pyga import Population
from pyga import ValidationException


class SampleOperator(Operator):
    def apply(self, selected_candidates):
        return selected_candidates


class PipelineOperatorTestCase(TestCase):
    def test_apply_empty(self):
        candidate = Candidate()
        population = Population()
        population.append(candidate)
        population.shuffle = MagicMock()
        sample_operator = SampleOperator()
        pipeline_operator = PipelineOperator()
        pipeline_operator.append_operator(sample_operator)
        result = pipeline_operator.apply(population)
        self.assertEqual(len(result), len(population))

    def test_validate(self):
        with self.assertRaises(ValidationException):
            pipeline_operator = PipelineOperator()
            pipeline_operator.append_operator(None)

