from unittest import TestCase
from unittest.mock import MagicMock

from pyga import Candidate
from pyga import Fitness
from pyga import Population
from pyga import Random
from pyga import RouletteWheelSelection


class RouletteWheelSelectionStrategyTestCase(TestCase):
    def setUp(self):
        self.random = Random()
        self.obj = RouletteWheelSelection(self.random)

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
        for candidate in results:
            self.assertEqual(candidate.fitness, 4)

    def test_select_proper_items_natural_false(self):
        population = Population()
        population.append(self.create_candidate(fitness=-4, is_natural=False))
        population.append(self.create_candidate(fitness=-3, is_natural=False))
        population.append(self.create_candidate(fitness=-2, is_natural=False))
        population.append(self.create_candidate(fitness=-1, is_natural=False))
        selection_size = 3
        self.random.float = MagicMock(return_value=0.99)
        results = self.obj.select(population, selection_size)
        for candidate in results:
            self.assertEqual(candidate.fitness, -1)

    def test_select_fitness_zero(self):
        population = Population()
        population.append(self.create_candidate(fitness=0))
        population.append(self.create_candidate(fitness=0))
        population.append(self.create_candidate(fitness=0))
        population.append(self.create_candidate(fitness=0))
        results = self.obj.select(population, 4)
        self.assertEqual(len(results), 4)

