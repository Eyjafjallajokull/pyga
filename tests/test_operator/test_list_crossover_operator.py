from unittest import TestCase
from unittest.mock import MagicMock, call

from pyga import ValidationException
from pyga.common import Probability, Random
from pyga.candidate import Candidate
from pyga.operator.list_crossover import ListCrossoverOperator


class ListCrossoverOperatorTestCase(TestCase):
    def _test_apply(self, strings, random, points):
        candidate1 = Candidate()
        candidate1.data = strings[0][0]
        candidate2 = Candidate()
        candidate2.data = strings[0][1]
        crossover_points = points
        crossover_operator = ListCrossoverOperator(crossover_points, Probability(1), random)
        result = crossover_operator.mate(candidate1, candidate2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].data, strings[1][0])
        self.assertEqual(result[1].data, strings[1][1])

    def test_apply_single_point(self):
        random = Random()
        random.int = MagicMock(return_value=2)
        self._test_apply([[[1, 2, 3, 4], [5, 6, 7, 8]],
                          [[1, 2, 7, 8], [5, 6, 3, 4]]], random, 1)

    def test_apply_two_points(self):
        random = Random()
        random.int = MagicMock(side_effect=[1, 3])
        self._test_apply([[[1, 2, 3, 4], [5, 6, 7, 8]],
                          [[1, 6, 7, 4], [5, 2, 3, 8]]], random, 2)

    def test_validate(self):
        crossover_operator = ListCrossoverOperator(1, Probability(1), Random())
        candidate1 = Candidate()
        candidate1.data = [1, 2, 3, 4]
        candidate2 = Candidate()
        candidate2.data = [5, 6, 7, 8]
        crossover_operator.validate_parents(candidate1, candidate2)

        candidate2.data = [1, 2, 3, 4, 5]
        with self.assertRaises(ValidationException):
            crossover_operator.validate_parents(candidate1, candidate2)