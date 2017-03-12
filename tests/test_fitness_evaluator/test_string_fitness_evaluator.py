from unittest import TestCase

from pyga.common import Fitness
from pyga.fitness_evaluator import StringFitnessEvaluator
from pyga.candidate import Candidate
from pyga.population import Population


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
