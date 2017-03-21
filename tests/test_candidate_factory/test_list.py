from unittest import TestCase
from unittest.mock import MagicMock

from pyga import ListFactory, ValidationException, Random


class ListFactoryTestCase(TestCase):
    def test_create_population_unique(self):
        random = Random()
        random.sample = MagicMock(return_value=[0, 1, 2, 3])
        candidate_factory = ListFactory(random, 3)
        result = candidate_factory.create_candidate()
        self.assertEqual(result.data, [0, 1, 2, 3])

    def test_create_population_not_unique(self):
        random = Random()
        random.int = MagicMock(side_effect=[0, 1, 2, 1, 2, 0])
        candidate_factory = ListFactory(random, 3, size=6, is_unique=False)
        result = candidate_factory.create_candidate()
        self.assertEqual(result.data, [0, 1, 2, 1, 2, 0])

    def test_validation(self):
        ListFactory(Random(), 3, size=3, is_unique=True)

        with self.assertRaises(ValidationException):
            ListFactory(Random(), 2, size=4, is_unique=True)
        with self.assertRaises(ValidationException):
            ListFactory(Random(), 3, size=5, is_unique=True)

        ListFactory(Random(), 4, size=2)