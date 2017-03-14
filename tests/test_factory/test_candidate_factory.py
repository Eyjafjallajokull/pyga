from unittest import TestCase
from unittest.mock import MagicMock

from pyga.common import Random
from pyga.candidate_factory.candidate_factory import CandidateFactory


class CandidateFactoryTestCase(TestCase):
    def test_create_population(self):
        random = Random()
        size = 4
        candidate_factory = CandidateFactory(random)
        candidate_factory.create_candidate = MagicMock()
        result = candidate_factory.create_population(size)
        self.assertEqual(candidate_factory.create_candidate.call_count, size)
        self.assertEqual(len(result), size)
