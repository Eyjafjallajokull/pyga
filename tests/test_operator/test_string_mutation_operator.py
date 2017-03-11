from unittest import TestCase
from unittest.mock import MagicMock, call

from pyga.common import Probability, Random
from pyga.genome import Genome
from pyga.operator.crossover_operator import CrossoverOperator
from pyga.operator.string_crossover_operator import StringCrossoverOperator
from pyga.operator.string_mutation_operator import StringMutationOperator
from pyga.population import Population


class StringMutationOperatorTestCase(TestCase):
    def test_apply_one(self):
        alphabet = 'abcd'
        inputs, outputs = ('aaaa', 'abcd')
        genome = Genome()
        genome.data = inputs
        population = Population()
        population.append(genome)
        probability = Probability(1)
        random = Random()
        random.choice = MagicMock(side_effect=['a', 'b', 'c', 'd'])
        crossover_operator = StringMutationOperator(alphabet, probability, random)
        result = crossover_operator.apply(population)
        self.assertEqual(len(result), len(population))
        self.assertEqual(result[0].data, outputs)

    def test_apply_zero(self):
        alphabet = 'abcd'
        inputs, outputs = ('aaaa', 'aaaa')
        genome = Genome()
        genome.data = inputs
        population = Population()
        population.append(genome)
        probability = Probability(0)
        random = Random()
        crossover_operator = StringMutationOperator(alphabet, probability, random)
        result = crossover_operator.apply(population)
        self.assertEqual(len(result), len(population))
        self.assertEqual(result[0].data, outputs)
