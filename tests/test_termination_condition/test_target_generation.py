from unittest import TestCase

from pyga import TargetGeneration, EvolutionEngine
from pyga.population import Population


class TargetGenerationTestCase(TestCase):
    def test_should_terminate(self):
        population = Population()
        engine = EvolutionEngine()
        engine.generation = 99
        target_generation = TargetGeneration(100, engine)
        self.assertEqual(target_generation.should_terminate(population), False)
        engine.generation = 100
        self.assertEqual(target_generation.should_terminate(population), True)
        engine.generation = 101
        self.assertEqual(target_generation.should_terminate(population), True)
