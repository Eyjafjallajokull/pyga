from unittest import TestCase
from unittest.mock import MagicMock

from pyga.common import Random
from pyga.evolution_engine import EvolutionEngine
from pyga.factory import CandidateFactory
from pyga.fitness_evaluator import FitnessEvaluator
from pyga.genome import Genome
from pyga.operator import EvolutionaryOperator
from pyga.population import Population
from pyga.selection_strategy import SelectionStrategy
from pyga.termination_condition.termination_condition import TerminationCondition


class EvolutionEngineTestCase(TestCase):
    def setUp(self):
        random = Random()
        factory = CandidateFactory(random)
        factory.create_candidate = MagicMock(side_effect=lambda: Genome())
        operator = EvolutionaryOperator()
        fitness_evaluator = FitnessEvaluator()
        fitness_evaluator.get_fitness = MagicMock(return_value=5)
        selection_strategy = SelectionStrategy()
        self.engine = EvolutionEngine()
        self.engine.create(factory, operator, fitness_evaluator, selection_strategy)

    def create_population(self, size):
        population = Population()
        for _ in range(size):
            population.append(Genome())
        return population

    def test_create_invalid(self):
        self.engine = EvolutionEngine()
        with self.assertRaises(TypeError) as cm:
            self.engine.create(None, None, None, None)
        self.assertIn('CandidateFactory', str(cm.exception))

        random = Random()
        factory = CandidateFactory(random)
        with self.assertRaises(TypeError) as cm:
            self.engine.create(factory, None, None, None)
        self.assertIn('EvolutionaryOperator', str(cm.exception))

        operator = EvolutionaryOperator()
        with self.assertRaises(TypeError) as cm:
            self.engine.create(factory, operator, None, None)
        self.assertIn('FitnessEvaluator', str(cm.exception))

        fitness_evaluator = FitnessEvaluator()
        with self.assertRaises(TypeError) as cm:
            self.engine.create(factory, operator, fitness_evaluator, None)
        self.assertIn('SelectionStrategy', str(cm.exception))

    def test_evaluate_population(self):
        population = self.create_population(1)
        self.assertEqual(population[0].fitness, None)
        self.engine.evaluate_population(population)
        self.assertEqual(population[0].fitness, 5)

    def test_evolve_first(self):
        termination_condition = TerminationCondition()
        termination_condition.should_terminate = MagicMock(side_effect=[True])
        population_size = 100
        population = self.engine.evolve(population_size, 5, termination_condition)
        self.assertEqual(len(population), population_size)
        self.assertEqual(self.engine.generation, 0)

    def test_evolve_one(self):
        termination_condition = TerminationCondition()
        termination_condition.should_terminate = MagicMock(side_effect=[False, True])
        population_size = 100
        self.engine.next_evolution_step = MagicMock(side_effect=lambda x, _: x)
        population = self.engine.evolve(population_size, 5, termination_condition)
        self.assertEqual(len(population), population_size)
        self.assertEqual(self.engine.generation, 1)
