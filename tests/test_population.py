from unittest import TestCase
from unittest.mock import MagicMock

from pyga.genome import Genome
from pyga.population import Population


class PopulationTestCase(TestCase):
    def test_sort_by_fitness(self):
        genome1 = Genome()
        genome1.fitness = 1
        genome2 = Genome()
        genome2.fitness = 2
        population = Population()
        population.append(genome1)
        population.append(genome2)
        population.sort_by_fitness()
        self.assertEqual(population[0], genome1)
        population.sort_by_fitness(is_natural=False)
        self.assertEqual(population[0], genome2)

    def test_get_best(self):
        population = Population()
        result = population.get_best()
        self.assertEqual(result, None)

        genome1 = Genome()
        genome1.fitness = 1
        genome2 = Genome()
        genome2.fitness = 2
        population.append(genome1)
        population.append(genome2)
        result = population.get_best()
        self.assertEqual(result, genome2)
        result = population.get_best(is_natural=False)
        self.assertEqual(result, genome1)

