from unittest import TestCase
from unittest.mock import MagicMock

from pyga.common import Probability, Random
from pyga.candidate import Candidate
from pyga.operator.string_crossover import StringCrossoverOperator


class StringCrossoverOperatorTestCase(TestCase):
    def _test_apply(self, strings, random, points):
        candidate1 = Candidate()
        candidate1.data = strings[0][0]
        candidate2 = Candidate()
        candidate2.data = strings[0][1]
        crossover_points = points
        crossover_operator = StringCrossoverOperator(crossover_points, Probability(1), random)
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

