from unittest import TestCase
from unittest.mock import MagicMock

from pyga import Candidate
from pyga import CandidateFactory
from pyga import EvolutionEngine
from pyga import Operator
from pyga import FitnessEvaluator
from pyga import Observer, Event, Fitness
from pyga import Population
from pyga import Random
from pyga import SelectionStrategy
from pyga import TerminationCondition


class EvolutionEngineTestCase(TestCase):
    def setUp(self):
        random = Random()
        factory = CandidateFactory(random)
        factory.create_candidate = MagicMock(side_effect=lambda: Candidate())
        operator = Operator()
        fitness_evaluator = FitnessEvaluator()
        fitness_evaluator.get_fitness = MagicMock(side_effect=lambda c, p: Fitness(5))
        selection_strategy = SelectionStrategy()
        self.engine = EvolutionEngine()
        self.engine.create(factory, operator, fitness_evaluator, selection_strategy)

    def create_population(self, size):
        population = Population()
        for _ in range(size):
            population.append(Candidate())
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
        self.assertIn('Operator', str(cm.exception))

        operator = Operator()
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

    def test_add_observer(self):
        with self.assertRaises(TypeError) as cx:
            self.engine.add_observer(False)
        self.engine.add_observer(Observer())

    def test_trigger_event(self):
        observer = Observer()
        observer.trigger = MagicMock()
        self.engine.add_observer(observer)
        self.engine.trigger_event(Event.EVALUATED_POPULATION, {})
        self.assertEqual(observer.trigger.call_count, 1)