from unittest import TestCase
from unittest.mock import MagicMock

from pyga import Random, Fitness
from pyga.exception import ValidationException
from pyga.candidate import Candidate
from pyga.population import Population
from pyga.selection_strategy import *


class StochasticUniversalSamplingSelectionStrategyTestCase(TestCase):
    def setUp(self):
        self.random = Random()
        self.obj = StochasticUniversalSamplingSelectionStrategy(self.random)

    def create_candidate(self, fitness=None, is_natural=True):
        candidate = Candidate()
        candidate.fitness = Fitness(fitness, is_natural=is_natural)
        return candidate

    def test_select_result_type(self):
        population = Population()
        population.append(self.create_candidate(fitness=1))
        results = self.obj.select(population, 1)
        self.assertIsInstance(results, Population)

    def test_select_result_size(self):
        population = Population()
        population.append(self.create_candidate(fitness=1))
        population.append(self.create_candidate(fitness=2))
        population.append(self.create_candidate(fitness=3))
        population.append(self.create_candidate(fitness=4))
        for selection_size in range(len(population)):
            results = self.obj.select(population, selection_size+1)
            self.assertEqual(selection_size+1, len(results))

    def test_select_proper_items(self):
        population = Population()
        population.append(self.create_candidate(fitness=1))
        population.append(self.create_candidate(fitness=2))
        population.append(self.create_candidate(fitness=3))
        population.append(self.create_candidate(fitness=4))
        selection_size = 3
        self.random.float = MagicMock(return_value=0.99)
        results = self.obj.select(population, selection_size)
        self.assertEqual(results[0].fitness, 3)
        self.assertEqual(results[1].fitness, 4)
        self.assertEqual(results[2].fitness, 4)

    def test_select_proper_items_natural_false(self):
        population = Population()
        population.append(self.create_candidate(fitness=-4, is_natural=False))
        population.append(self.create_candidate(fitness=-3, is_natural=False))
        population.append(self.create_candidate(fitness=-2, is_natural=False))
        population.append(self.create_candidate(fitness=-1, is_natural=False))
        selection_size = 3
        self.random.float = MagicMock(return_value=0.99)
        results = self.obj.select(population, selection_size)
        self.assertEqual(results[0].fitness, -4)
        self.assertEqual(results[1].fitness, -3)
        self.assertEqual(results[2].fitness, -1)

    def test_validation_selection_size(self):
        with self.assertRaises(ValidationException):
            self.obj.select(Population(), 0)

    def test_validation_population_size(self):
        with self.assertRaises(ValidationException):
            self.obj.select(Population(), 5)