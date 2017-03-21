from unittest import TestCase
from unittest.mock import MagicMock

from pyga import Candidate
from pyga import Population
from pyga import Probability
from pyga import Random
from pyga import StringMutation


class StringMutationOperatorTestCase(TestCase):
    def test_apply_one(self):
        alphabet = 'abcd'
        inputs, outputs = ('aaaa', 'abcd')
        candidate = Candidate()
        candidate.data = inputs
        population = Population()
        population.append(candidate)
        probability = Probability(1)
        random = Random()
        random.choice = MagicMock(side_effect=['a', 'b', 'c', 'd'])
        crossover_operator = StringMutation(probability, random, alphabet)
        result = crossover_operator.apply(population)
        self.assertEqual(len(result), len(population))
        self.assertEqual(result[0].data, outputs)

    def test_apply_zero(self):
        alphabet = 'abcd'
        inputs, outputs = ('aaaa', 'aaaa')
        candidate = Candidate()
        candidate.data = inputs
        population = Population()
        population.append(candidate)
        probability = Probability(0)
        random = Random()
        crossover_operator = StringMutation(probability, random, alphabet)
        result = crossover_operator.apply(population)
        self.assertEqual(len(result), len(population))
        self.assertEqual(result[0].data, outputs)
