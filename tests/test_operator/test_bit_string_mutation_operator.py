from unittest import TestCase
from unittest.mock import MagicMock

from pyga.common import Probability, Random
from pyga.candidate import Candidate
from pyga.operator.bit_string_mutation import BitStringMutationOperator
from pyga.population import Population


class BitStringMutationOperatorTestCase(TestCase):
    def test_apply_one(self):
        inputs, outputs = ('0110', '1010')
        candidate = Candidate()
        candidate.data = inputs
        population = Population()
        population.append(candidate)
        probability = Probability(1)
        random = Random()
        random.float = MagicMock(side_effect=[0.6, 0.1, 0.9, 0.4])
        crossover_operator = BitStringMutationOperator(probability, random)
        result = crossover_operator.apply(population)
        self.assertEqual(len(result), len(population))
        self.assertEqual(result[0].data, outputs)

    def test_apply_zero(self):
        inputs, outputs = ('aaaa', 'aaaa')
        candidate = Candidate()
        candidate.data = inputs
        population = Population()
        population.append(candidate)
        probability = Probability(0)
        random = Random()
        crossover_operator = BitStringMutationOperator(probability, random)
        result = crossover_operator.apply(population)
        self.assertEqual(len(result), len(population))
        self.assertEqual(result[0].data, outputs)
