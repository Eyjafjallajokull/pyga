from unittest import TestCase
from unittest.mock import MagicMock

from pyga.candidate import Candidate
from pyga.population import Population


class PopulationTestCase(TestCase):
    def test_sort_by_fitness(self):
        candidate1 = Candidate()
        candidate1.fitness = 1
        candidate2 = Candidate()
        candidate2.fitness = 2
        population = Population()
        population.append(candidate1)
        population.append(candidate2)
        population.sort_by_fitness()
        self.assertEqual(population[0], candidate1)
        population.sort_by_fitness(is_natural=False)
        self.assertEqual(population[0], candidate2)

    def test_get_best(self):
        population = Population()
        result = population.get_best()
        self.assertEqual(result, None)

        candidate1 = Candidate()
        candidate1.fitness = 1
        candidate2 = Candidate()
        candidate2.fitness = 2
        population.append(candidate1)
        population.append(candidate2)
        result = population.get_best()
        self.assertEqual(result, candidate2)
        result = population.get_best(is_natural=False)
        self.assertEqual(result, candidate1)

