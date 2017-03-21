from unittest import TestCase

from pyga import TerminationCondition


class TerminationConditionTestCase(TestCase):
    def test_init(self):
        TerminationCondition()
