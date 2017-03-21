import sys
import os
import logging

sys.path.append(os.environ["PWD"])
from pyga import *

population_size = 10
elite_count = 2
crossover_points = 2
crossover_mutate_probability = 0.2
max_weight = 15
city_names = ['a', 'b', 'c', 'd']
distances = [
    #  a    b    c    d
    [  0, 130, 180, 300], # a
    [130,   0, 320, 350], # b
    [180, 320,   0, 360], # c
    [300, 350, 360,   0]  # d
]


class SalesmanFitnessEvaluator(FitnessEvaluator):
    def __init__(self, distances):
        super().__init__()
        self.distances = distances

    def get_fitness(self, candidate, population):
        total_distance = 0
        cities_order = candidate.data
        for i, city in enumerate(cities_order):
            next_city = cities_order[i+1] if i+1 < len(cities_order) else cities_order[0]
            total_distance += self.distances[city][next_city]
        return Fitness(-total_distance, is_natural=False)


def print_results(result):
    print('Visit cities in this order:')
    cities_order = result.data
    for i, city in enumerate(cities_order):
        next_city = cities_order[i + 1] if i + 1 < len(cities_order) else cities_order[0]
        print('- ', city_names[city], distances[city][next_city])
    print('Total distance: ', abs(result.fitness))


logging.basicConfig(level=logging.DEBUG)
random = Random()
probability = Probability(crossover_mutate_probability, random)
candidate_factory = ListFactory(random, len(distances)-1)
crossover = ListOrderCrossover(probability, random)
mutation = ListOrderMutation(probability, random, 2)
operator = PipelineOperator()
operator.append_operator(crossover)
operator.append_operator(mutation)
fitness_evaluator = SalesmanFitnessEvaluator(distances)
selection_strategy = RouletteWheelSelection(random)
termination_condition = Stagnation(100)

engine = GenerationalEvolutionEngine()
engine.create(candidate_factory, operator, fitness_evaluator, selection_strategy)
population = engine.evolve(population_size, elite_count, termination_condition)

print_results(population.get_best())
