from unittest import TestCase
from unittest.mock import MagicMock

from pyga import Candidate
from pyga import CandidateFactory
from pyga import Operator
from pyga import FitnessEvaluator
from pyga import GenerationalEvolutionEngine
from pyga import Population
from pyga import Random
from pyga import SelectionStrategy


class GenerationalEvolutionEngineTestCase(TestCase):
    def setUp(self):
        random = Random()
        factory = CandidateFactory(random)
        evolutionary_operator = Operator()
        evolutionary_operator.apply = MagicMock(side_effect=lambda p: p)
        fitness_evaluator = FitnessEvaluator()
        fitness_evaluator.get_fitness = MagicMock(return_value=5)
        selection_strategy = SelectionStrategy()
        selection_strategy.validate = MagicMock()
        selection_strategy.select = MagicMock(side_effect=lambda p, s: p[0:s])
        self.engine = GenerationalEvolutionEngine()
        self.engine.create(factory, evolutionary_operator, fitness_evaluator, selection_strategy)

    def test_next_evolution_step(self):
        population = Population()
        for i in range(5):
            population.append(Candidate())
        result = self.engine.next_evolution_step(population, 3)
        self.assertEqual(len(result), len(population))
        self.assertEqual(self.engine.selection_strategy.validate.call_count, 1)
        self.assertEqual(self.engine.selection_strategy.select.call_count, 1)
        self.assertEqual(self.engine.evolutionary_operator.apply.call_count, 1)

    def test_next_evolution_step_invalid(self):
        with self.assertRaises(RuntimeError):
            self.engine.next_evolution_step(Population(), 1)