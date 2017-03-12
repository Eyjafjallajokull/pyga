from unittest import TestCase

from pyga import TimeLimit, Population
from time import sleep


class TimeLimitTestCase(TestCase):
    def test_should_terminate(self):
        population = Population()
        target_generation = TimeLimit(0.2)
        self.assertEqual(target_generation.should_terminate(population), False)
        sleep(0.4)
        self.assertEqual(target_generation.should_terminate(population), True)
