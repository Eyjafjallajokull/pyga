from unittest import TestCase

from pyga import Candidate
from pyga import Fitness
from pyga import Population
from pyga import StringFitnessEvaluator


class StringFitnessEvaluatorTestCase(TestCase):
    def _test_get_fitness(self, target, inputs, score):
        candidate = Candidate()
        candidate.data = inputs
        population = Population()
        population.append(candidate)
        fitness_evaluator = StringFitnessEvaluator(target)
        result = fitness_evaluator.get_fitness(candidate, population)
        self.assertIsInstance(result, Fitness)
        self.assertEqual(result, score)

    def test_get_fitness(self):
        self._test_get_fitness('abcdef', 'xxxxxx', 0)
        self._test_get_fitness('abcdef', 'abcxxx', 3)
        self._test_get_fitness('abcdef', 'abcdef', 6)
