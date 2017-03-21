from unittest import TestCase

from pyga import EvolutionEngine
from pyga import Population
from pyga import TargetGeneration


class TargetGenerationTestCase(TestCase):
    def test_should_terminate(self):
        population = Population()
        engine = EvolutionEngine()
        engine.generation = 99
        termination_condition = TargetGeneration(100, engine)
        self.assertEqual(termination_condition.should_terminate(population), False)
        engine.generation = 100
        self.assertEqual(termination_condition.should_terminate(population), True)
        engine.generation = 101
        self.assertEqual(termination_condition.should_terminate(population), True)
