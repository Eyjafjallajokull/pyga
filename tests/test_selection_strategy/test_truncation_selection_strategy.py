from unittest import TestCase

from pyga.exception import ValidationException
from pyga.genome import Genome
from pyga.population import Population
from pyga.selection_strategy import *


class RankSelectionStrategyTestCase(TestCase):
    def setUp(self):
        self.obj = TruncationSelectionStrategy()

    def create_genome(self, fitness=None):
        genome = Genome()
        genome.fitness = fitness
        return genome

    def test_select_result_type(self):
        population = Population()
        population.append(self.create_genome(fitness=1))
        results = self.obj.select(population, True, 1)
        self.assertIsInstance(results, Population)

    def test_select_result_size(self):
        population = Population()
        population.append(self.create_genome(fitness=1))
        population.append(self.create_genome(fitness=2))
        population.append(self.create_genome(fitness=3))
        population.append(self.create_genome(fitness=4))
        for selection_size in range(len(population)):
            results = self.obj.select(population, True, selection_size+1)
            self.assertEqual(selection_size+1, len(results))

    def test_select_proper_items(self):
        population = Population()
        population.append(self.create_genome(fitness=1))
        population.append(self.create_genome(fitness=2))
        population.append(self.create_genome(fitness=3))
        population.append(self.create_genome(fitness=4))
        selection_size = 1
        results = self.obj.select(population, True, selection_size)
        self.assertEqual(results[0].fitness, 4)

    def test_select_proper_items_natural_false(self):
        population = Population()
        population.append(self.create_genome(fitness=4))
        population.append(self.create_genome(fitness=3))
        population.append(self.create_genome(fitness=2))
        population.append(self.create_genome(fitness=1))
        selection_size = 1
        results = self.obj.select(population, False, selection_size)
        self.assertEqual(results[0].fitness, 1)

    def test_validation_selection_size(self):
        with self.assertRaises(ValidationException):
            self.obj.select(Population(), True, 0)

    def test_validation_population_size(self):
        with self.assertRaises(ValidationException):
            self.obj.select(Population(), True, 5)