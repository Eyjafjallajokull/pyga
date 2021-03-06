from unittest import TestCase
from unittest.mock import MagicMock

from pyga import Candidate
from pyga import Probability
from pyga import Random
from pyga import StringCrossover
from pyga import ValidationException


class StringCrossoverOperatorTestCase(TestCase):
    def _test_apply(self, strings, random, points):
        candidate1 = Candidate()
        candidate1.data = strings[0][0]
        candidate2 = Candidate()
        candidate2.data = strings[0][1]
        crossover_points = points
        crossover_operator = StringCrossover(Probability(1), random, crossover_points)
        result = crossover_operator.mate(candidate1, candidate2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].data, strings[1][0])
        self.assertEqual(result[1].data, strings[1][1])

    def test_apply_single_point(self):
        random = Random()
        random.int = MagicMock(return_value=3)
        self._test_apply([['AAAAAA', 'BBBBBB'], ['AAABBB', 'BBBAAA']], random, 1)

    def test_apply_two_points(self):
        random = Random()
        random.int = MagicMock(side_effect=[2, 4])
        self._test_apply([['AAAAAA', 'BBBBBB'], ['AABBAA', 'BBAABB']], random, 2)

    def test_apply_four_points(self):
        random = Random()
        random.int = MagicMock(side_effect=[2, 4, 6, 8])
        self._test_apply([['AAAAAAAAAA', 'BBBBBBBBBB'], ['AABBAABBAA', 'BBAABBAABB']], random, 4)

    def test_validate(self):
        crossover_operator = StringCrossover(Probability(1), Random(), 1)
        candidate1 = Candidate()
        candidate1.data = 'AAAA'
        candidate2 = Candidate()
        candidate2.data = 'BBBB'
        crossover_operator.validate_parents(candidate1, candidate2)
        candidate2.data = 'BBBBB'
        with self.assertRaises(ValidationException):
            crossover_operator.validate_parents(candidate1, candidate2)
