from unittest import TestCase
from unittest.mock import MagicMock

from pyga import BitStringMutation
from pyga import Candidate
from pyga import Population
from pyga import Probability
from pyga import Random


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
        mutation_operator = BitStringMutation(probability, random)
        result = mutation_operator.apply(population)
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
        mutation_operator = BitStringMutation(probability, random)
        result = mutation_operator.apply(population)
        self.assertEqual(len(result), len(population))
        self.assertEqual(result[0].data, outputs)
