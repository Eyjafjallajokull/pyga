from unittest import TestCase
from unittest.mock import MagicMock

from pyga import Candidate
from pyga import ListOrderCrossover
from pyga import Probability
from pyga import Random
from pyga import ValidationException


class ListCrossoverOperatorTestCase(TestCase):
    def test_apply(self):
        candidate1 = Candidate()
        candidate1.data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        candidate2 = Candidate()
        candidate2.data = [9, 3, 7, 8, 2, 6, 5, 1, 4]
        random = Random()
        random.int = MagicMock(side_effect=[3, 7])
        crossover_operator = ListOrderCrossover(Probability(1), random)
        result = crossover_operator.mate(candidate1, candidate2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].data, [1, 7, 3, 8, 2, 6, 5, 4, 9])
        self.assertEqual(result[1].data, [9, 3, 2, 4, 5, 6, 7, 1, 8])

    def test_validate(self):
        crossover_operator = ListOrderCrossover(Probability(1), Random())
        candidate1 = Candidate()
        candidate1.data = [1, 2, 3, 4]
        candidate2 = Candidate()
        candidate2.data = [5, 6, 7, 8]
        crossover_operator.validate_parents(candidate1, candidate2)

        candidate2.data = [1, 2, 3, 4, 5]
        with self.assertRaises(ValidationException):
            crossover_operator.validate_parents(candidate1, candidate2)