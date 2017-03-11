from random import Random
from unittest import TestCase
from unittest.mock import MagicMock, call

from pyga.common import Probability
from pyga.genome import Genome
from pyga.operator.crossover_operator import CrossoverOperator
from pyga.population import Population


class CrossoverOperatorTestCase(TestCase):
    def test_apply_even(self):
        self._test_apply(4)

    def test_apply_odd(self):
        self._test_apply(5)

    def _test_apply(self, population_size):
        genomes = [Genome() for _ in range(population_size)]
        for i in range(population_size):
            genomes[i].fitness = i
        population = Population()
        population.shuffle = MagicMock()
        population.append_list(genomes)
        crossover_points = 1
        crossover_operator = CrossoverOperator(crossover_points, Probability(1), Random())
        crossover_operator.mate = MagicMock(return_value=(True, True))
        result = crossover_operator.apply(population)

        self.assertEqual(crossover_operator.mate.call_count, int(population_size / 2))
        self.assertEqual(crossover_operator.mate.call_args_list,
                         [call(genomes[i], genomes[i+1]) for i in range(0, population_size-1, 2)])
        self.assertEqual(len(result), population_size)

    def test_apply_zero_probability(self):
        population_size = 4
        genomes = [Genome() for _ in range(population_size)]
        for i in range(population_size):
            genomes[i].fitness = i
        population = Population()
        population.shuffle = MagicMock()
        population.append_list(genomes)
        crossover_points = 1
        crossover_operator = CrossoverOperator(crossover_points, Probability(0), Random())
        crossover_operator.mate = MagicMock(return_value=(True, True))
        result = crossover_operator.apply(population)
        self.assertEqual(len(result), population_size)
