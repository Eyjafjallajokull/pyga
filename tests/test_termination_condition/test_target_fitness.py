from unittest import TestCase

from pyga import Fitness
from pyga.candidate import Candidate
from pyga.population import Population
from pyga.termination_condition import TargetFitness


class TargetFitnessTestCase(TestCase):
    def test_should_terminate(self):
        candidate = Candidate()
        candidate.fitness = Fitness(50)
        population = Population()
        population.append(candidate)
        target_fitness = TargetFitness(100)
        self.assertEqual(target_fitness.should_terminate(population), False)
        candidate.fitness = Fitness(150)
        self.assertEqual(target_fitness.should_terminate(population), True)

    def test_should_terminate_not_natural(self):
        candidate = Candidate()
        candidate.fitness = Fitness(-50, is_natural=False)
        population = Population()
        population.append(candidate)
        target_fitness = TargetFitness(-100)
        self.assertEqual(target_fitness.should_terminate(population), False)
        candidate.fitness = Fitness(-150, is_natural=False)
        self.assertEqual(target_fitness.should_terminate(population), True)
