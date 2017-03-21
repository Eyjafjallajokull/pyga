from unittest import TestCase
from unittest.mock import MagicMock

from pyga import Candidate
from pyga import ListOrderMutation
from pyga import Population
from pyga import Probability
from pyga import Random


class ListOrderMutationOperatorTestCase(TestCase):
    def test_apply(self):
        candidate = Candidate()
        candidate.data = [1, 2, 3, 4]
        population = Population([candidate])
        probability = Probability(1)
        random = Random()
        random.int = MagicMock(side_effect=[1, 3])
        crossover_operator = ListOrderMutation(probability, random, 1)
        result = crossover_operator.apply(population)
        self.assertEqual(len(result), len(population))
        self.assertEqual(result[0].data, [1, 4, 3, 2])
