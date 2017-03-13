from unittest import TestCase

from pyga import TimeLimit, Population
from time import sleep


class TimeLimitTestCase(TestCase):
    def test_should_terminate(self):
        population = Population()
        termination_condition = TimeLimit(0.2)
        self.assertEqual(termination_condition.should_terminate(population), False)
        sleep(0.4)
        self.assertEqual(termination_condition.should_terminate(population), True)
