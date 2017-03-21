from unittest import TestCase
from unittest.mock import MagicMock

from pyga import BitStringFactory, Random


class BitStringFactoryTestCase(TestCase):
    def test_create_population(self):
        random = Random()
        random.float = MagicMock(side_effect=[0, 1, 1, 0])
        candidate_factory = BitStringFactory(random, 4)
        result = candidate_factory.create_candidate()
        self.assertEqual(result.data, '0110')
