from unittest import TestCase
from unittest.mock import MagicMock

from pyga import Candidate
from pyga import Population
from pyga import CallbackFitnessEvaluator


class CallbackFitnessEvaluatorTestCase(TestCase):
    def test_get_fitness(self):
        candidate = Candidate()
        population = Population()
        population.append(candidate)
        callback = MagicMock(return_value=2)
        fitness_evaluator = CallbackFitnessEvaluator(callback)
        result = fitness_evaluator.get_fitness(candidate, population)
        self.assertEqual(callback.call_count, 1)
        self.assertEqual(result, 2)

