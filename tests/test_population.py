from unittest import TestCase

from pyga import Fitness
from pyga.candidate import Candidate
from pyga.population import Population


class PopulationTestCase(TestCase):
    def test_sort_by_fitness_empty(self):
        population = Population()
        population.sort_by_fitness()

    def test_sort_by_fitness_natural(self):
        candidate1 = Candidate()
        candidate1.fitness = Fitness(1)
        candidate2 = Candidate()
        candidate2.fitness = Fitness(2)
        population = Population([candidate2, candidate1])
        population.sort_by_fitness()
        self.assertEqual(population[0], candidate1)
        self.assertEqual(population[1], candidate2)

    def test_sort_by_fitness_not_natural(self):
        candidate1 = Candidate()
        candidate1.fitness = Fitness(-1, is_natural=False)
        candidate2 = Candidate()
        candidate2.fitness = Fitness(-2, is_natural=False)
        population = Population([candidate2, candidate1])
        population.sort_by_fitness()
        self.assertEqual(population[0], candidate1)
        self.assertEqual(population[1], candidate2)

    def test_get_best_empty(self):
        population = Population()
        result = population.get_best()
        self.assertEqual(result, None)

    def test_get_best_natural(self):
        candidate1 = Candidate()
        candidate1.fitness = Fitness(1)
        candidate2 = Candidate()
        candidate2.fitness = Fitness(2)
        result = Population([candidate1, candidate2]).get_best()
        self.assertEqual(result, candidate2)
        result = Population([candidate2, candidate1]).get_best()
        self.assertEqual(result, candidate2)

    def test_get_best_not_natural(self):
        candidate1 = Candidate()
        candidate1.fitness = Fitness(-1, is_natural=False)
        candidate2 = Candidate()
        candidate2.fitness = Fitness(-2, is_natural=False)
        result = Population([candidate1, candidate2]).get_best()
        self.assertEqual(result, candidate2)
        result = Population([candidate2, candidate1]).get_best()
        self.assertEqual(result, candidate2)

    def test_add(self):
        self.assertIsInstance(Population()+Population(), Population)
