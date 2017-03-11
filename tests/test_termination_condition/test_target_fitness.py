from unittest import TestCase

from pyga.candidate import Candidate
from pyga.population import Population
from pyga.termination_condition import TargetFitness


class TargetFitnessTestCase(TestCase):
    def test_create_population(self):
        candidate = Candidate()
        candidate.fitness = 50
        population = Population()
        population.append(candidate)
        target_fitness_natural = TargetFitness(100, True)
        target_fitness_not_natural = TargetFitness(100, False)
        self.assertEqual(target_fitness_natural.should_terminate(population), False)
        self.assertEqual(target_fitness_not_natural.should_terminate(population), True)
        candidate.fitness = 150
        self.assertEqual(target_fitness_natural.should_terminate(population), True)
        self.assertEqual(target_fitness_not_natural.should_terminate(population), False)
