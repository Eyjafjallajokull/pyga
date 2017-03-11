from unittest import TestCase
from unittest.mock import MagicMock

from pyga.common import Random
from pyga.factory.string_factory import StringFactory
from pyga.fitness_evaluator import StringFitnessEvaluator
from pyga.genome import Genome
from pyga.population import Population


class StringFitnessEvaluatorTestCase(TestCase):
    def _test_get_fitness(self, target, inputs, score):
        genome = Genome()
        genome.data = inputs
        population = Population()
        population.append(genome)
        fitness_evaluator = StringFitnessEvaluator(target)
        result = fitness_evaluator.get_fitness(genome, population)
        self.assertEqual(result, score)

    def test_get_fitness(self):
        self._test_get_fitness('abcdef', 'xxxxxx', 0)
        self._test_get_fitness('abcdef', 'abcxxx', 3)
        self._test_get_fitness('abcdef', 'abcdef', 6)
