from unittest import TestCase
from unittest.mock import MagicMock, call

from pyga import Candidate
from pyga import Crossover
from pyga import Population
from pyga import Probability
from pyga import Random


class CrossoverOperatorTestCase(TestCase):
    def test_apply_even(self):
        self._test_apply(4)

    def test_apply_odd(self):
        self._test_apply(5)

    def _test_apply(self, population_size):
        candidates = [Candidate() for _ in range(population_size)]
        for i in range(population_size):
            candidates[i].fitness = i
        population = Population()
        population.shuffle = MagicMock()
        population.append_list(candidates)
        random = Random()
        random.shuffle = MagicMock(side_effect=lambda x: x)
        crossover_operator = Crossover(Probability(1), random)
        crossover_operator.mate = MagicMock(return_value=(True, True))
        result = crossover_operator.apply(population)

        self.assertEqual(crossover_operator.mate.call_count, int(population_size / 2))
        self.assertEqual(crossover_operator.mate.call_args_list,
                         [call(candidates[i], candidates[i+1]) for i in range(0, population_size-1, 2)])
        self.assertEqual(len(result), population_size)

    def test_apply_zero_probability(self):
        population_size = 4
        candidates = [Candidate() for _ in range(population_size)]
        for i in range(population_size):
            candidates[i].fitness = i
        population = Population()
        population.shuffle = MagicMock()
        population.append_list(candidates)
        crossover_operator = Crossover(Probability(0), Random())
        crossover_operator.mate = MagicMock(return_value=(True, True))
        result = crossover_operator.apply(population)
        self.assertEqual(len(result), population_size)
