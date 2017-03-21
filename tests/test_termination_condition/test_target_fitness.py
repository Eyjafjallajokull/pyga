from unittest import TestCase

from pyga import Candidate
from pyga import Fitness
from pyga import Population
from pyga import TargetFitness


class TargetFitnessTestCase(TestCase):
    def test_should_terminate(self):
        candidate = Candidate()
        candidate.fitness = Fitness(50)
        population = Population()
        population.append(candidate)
        termination_condition = TargetFitness(100)
        self.assertEqual(termination_condition.should_terminate(population), False)
        candidate.fitness = Fitness(150)
        self.assertEqual(termination_condition.should_terminate(population), True)

    def test_should_terminate_not_natural(self):
        candidate = Candidate()
        candidate.fitness = Fitness(-50, is_natural=False)
        population = Population()
        population.append(candidate)
        termination_condition = TargetFitness(-100)
        self.assertEqual(termination_condition.should_terminate(population), False)
        candidate.fitness = Fitness(-150, is_natural=False)
        self.assertEqual(termination_condition.should_terminate(population), True)
