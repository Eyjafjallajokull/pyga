from unittest import TestCase
from unittest.mock import MagicMock

from pyga.genome import Genome
from pyga.population import Population
from pyga.termination_condition import Multicondition
from pyga.termination_condition import TerminationCondition


class MulticonditionTestCase(TestCase):
    def test_logical_and(self):
        population = Population()
        population.append(Genome())

        tc1 = TerminationCondition()
        tc1.should_terminate = MagicMock(return_value=True)
        tc2 = TerminationCondition()
        tc2.should_terminate = MagicMock(return_value=False)
        multicondition = Multicondition(logic=Multicondition.LOGIC_AND)
        multicondition.add(tc1)
        multicondition.add(tc2)
        self.assertFalse(multicondition.should_terminate(population))

        tc2.should_terminate = MagicMock(return_value=True)
        self.assertTrue(multicondition.should_terminate(population))

    def test_logical_or(self):
        population = Population()
        population.append(Genome())

        tc1 = TerminationCondition()
        tc1.should_terminate = MagicMock(return_value=True)
        tc2 = TerminationCondition()
        tc2.should_terminate = MagicMock(return_value=False)
        multicondition = Multicondition(logic=Multicondition.LOGIC_OR)
        multicondition.add(tc1)
        multicondition.add(tc2)
        self.assertTrue(multicondition.should_terminate(population))

        tc1.should_terminate = MagicMock(return_value=False)
        self.assertFalse(multicondition.should_terminate(population))

