from unittest import TestCase
from unittest.mock import MagicMock

from pyga import Random, StringFactory


class StringFactoryTestCase(TestCase):
    def test_create_population(self):
        random = Random()
        random.choice = MagicMock(side_effect=['a','a','c','d'])
        candidate_factory = StringFactory(random, 'abcd', 4)
        result = candidate_factory.create_candidate()
        self.assertEqual(result.data, 'aacd')
