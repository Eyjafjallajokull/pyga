from unittest import TestCase

from pyga import Candidate


class CandidateTestCase(TestCase):
    def test_init(self):
        candidate = Candidate()
        self.assertTrue(str(candidate))
