from unittest import TestCase

from pyga.genome import Genome
from pyga.population import Population
from pyga.termination_condition import TargetFitness


class TargetFitnessTestCase(TestCase):
    def test_create_population(self):
        genome = Genome()
        genome.fitness = 50
        population = Population()
        population.append(genome)
        target_fitness_natural = TargetFitness(100, True)
        target_fitness_not_natural = TargetFitness(100, False)
        self.assertEqual(target_fitness_natural.should_terminate(population), False)
        self.assertEqual(target_fitness_not_natural.should_terminate(population), True)
        genome.fitness = 150
        self.assertEqual(target_fitness_natural.should_terminate(population), True)
        self.assertEqual(target_fitness_not_natural.should_terminate(population), False)
