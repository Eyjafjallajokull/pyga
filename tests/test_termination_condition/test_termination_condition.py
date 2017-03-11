from unittest import TestCase
from unittest.mock import MagicMock

from pyga.common import Random
from pyga.termination_condition import TerminationCondition


class TerminationConditionTestCase(TestCase):
    def test_init(self):
        TerminationCondition()
