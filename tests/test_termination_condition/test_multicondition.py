from unittest import TestCase
from unittest.mock import MagicMock

from pyga.candidate import Candidate
from pyga.population import Population
from pyga.termination_condition import Multicondition
from pyga.termination_condition import TerminationCondition


class MulticonditionTestCase(TestCase):
    def test_add(self):
        with self.assertRaises(TypeError):
            Multicondition().add(None)

    def test_logical_and(self):
        population = Population()
        population.append(Candidate())

        tc1 = TerminationCondition()
        tc1.should_terminate = MagicMock(return_value=True)
        tc2 = TerminationCondition()
        tc2.should_terminate = MagicMock(return_value=False)
        termination_condition = Multicondition(logic=Multicondition.LOGIC_AND)
        termination_condition.add(tc1)
        termination_condition.add(tc2)
        self.assertFalse(termination_condition.should_terminate(population))

        tc2.should_terminate = MagicMock(return_value=True)
        self.assertTrue(termination_condition.should_terminate(population))

    def test_logical_or(self):
        population = Population()
        population.append(Candidate())

        tc1 = TerminationCondition()
        tc1.should_terminate = MagicMock(return_value=True)
        tc2 = TerminationCondition()
        tc2.should_terminate = MagicMock(return_value=False)
        termination_condition = Multicondition(logic=Multicondition.LOGIC_OR)
        termination_condition.add(tc1)
        termination_condition.add(tc2)
        self.assertTrue(termination_condition.should_terminate(population))

        tc1.should_terminate = MagicMock(return_value=False)
        self.assertFalse(termination_condition.should_terminate(population))

