from unittest import TestCase

from pyga import Candidate
from pyga import Fitness
from pyga import Population
from pyga import Stagnation


class StagnationTestCase(TestCase):
    def test_should_terminate(self):
        candidate = Candidate()
        candidate.fitness = Fitness(1)
        population = Population()
        population.append(candidate)
        termination_condition = Stagnation(3)
        self.assertEqual(termination_condition.should_terminate(population), False)
        self.assertEqual(termination_condition.should_terminate(population), False)
        self.assertEqual(termination_condition.should_terminate(population), True)
        candidate.fitness = Fitness(2)
        self.assertEqual(termination_condition.should_terminate(population), False)
        self.assertEqual(termination_condition.should_terminate(population), False)
        self.assertEqual(termination_condition.should_terminate(population), True)
