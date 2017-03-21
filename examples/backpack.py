import sys
import os
import logging

sys.path.append(os.environ["PWD"])
from pyga import *

population_size = 10
elite_count = 2
crossover_points = 2
crossover_probability = 0.2
mutate_probability = 0.5
max_weight = 15
items = [
    # name, survival score, weight
    ['knife', 10, 1],
    ['beans', 30, 5],
    ['potatoes', 15, 10],
    ['unions', 2, 1],
    ['sleeping bag', 30, 7],
    ['rope', 10, 5],
    ['compass', 30, 1],
    ['matches', 20, 1],
    ['axe', 10, 1],
    ['comb', 0, 2],
    ['sunglasses', 0, 1]
]


class BackpackFitnessEvaluator(FitnessEvaluator):
    def __init__(self, items, max_weight):
        super().__init__()
        self.items = items
        self.max_weight = max_weight

    def get_fitness(self, candidate, population):
        survival_score_sum = 0
        weight_sum = 0
        for i, use in enumerate(candidate.data):
            if int(use) == 1:
                survival_score_sum += self.items[i][1]
                weight_sum += self.items[i][2]
        if weight_sum < self.max_weight:
            fitness = survival_score_sum
        else:
            fitness = 0
        return Fitness(fitness)


def print_results(result):
    print('Items to pack:')
    weight = 0
    for i, use in enumerate(list(result.data)):
        if int(use) == 1:
            print('- ', items[i][0])
            weight += items[i][2]
    print('Survival score: ', result.fitness)
    print('Backpack weight: ', weight)


logging.basicConfig(level=logging.DEBUG)
random = Random()
crossover_probability = Probability(crossover_probability, random)
mutate_probability = Probability(mutate_probability, random)
candidate_factory = BitStringFactory(random, len(items))
crossover = StringCrossover(crossover_probability, random, crossover_points)
mutation = BitStringMutation(mutate_probability, random)
operator = PipelineOperator()
operator.append_operator(crossover)
operator.append_operator(mutation)
fitness_evaluator = BackpackFitnessEvaluator(items, max_weight)
selection_strategy = RouletteWheelSelection(random)
termination_condition = Stagnation(100)

engine = GenerationalEvolutionEngine()
engine.create(candidate_factory, operator, fitness_evaluator, selection_strategy)
population = engine.evolve(population_size, elite_count, termination_condition)

print_results(population.get_best())
