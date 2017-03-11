import sys
import os
import logging

sys.path.append(os.environ["PWD"])
from pyga import *

subject_string = 'Hello World'
population_size = 10
elite_count = 2
crossover_points = 2
crossover_mutate_probability = 0.2

alphabet = ''.join(set(list(subject_string)))
logging.basicConfig(level=logging.DEBUG)
random = Random()
observer = ConsoleObserver()
probability = Probability(crossover_mutate_probability, random)
candidate_factory = StringFactory(random, alphabet, len(subject_string))
crossover = StringCrossoverOperator(crossover_points, probability, random)
mutation = StringMutationOperator(alphabet, probability, random)
operator = PipelineOperator()
operator.append_operator(crossover)
operator.append_operator(mutation)
fitness_evaluator = StringFitnessEvaluator(subject_string)
selection_strategy = RouletteWheelSelectionStrategy(random)
termination_condition = TargetFitness(len(subject_string), fitness_evaluator.is_natural)

engine = GenerationalEvolutionEngine()
engine.add_observer(observer)
engine.create(candidate_factory, operator, fitness_evaluator, selection_strategy)
population = engine.evolve(population_size, elite_count, termination_condition)

print(population.get_best())
