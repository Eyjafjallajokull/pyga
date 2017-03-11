from ..common import Event
from ..observer import Observer
from ..factory import CandidateFactory
from ..fitness_evaluator import FitnessEvaluator
from ..operator import EvolutionaryOperator
from ..selection_strategy import SelectionStrategy


class EvolutionEngine:
    def __init__(self):
        self.observers = []
        self.candidate_factory = None
        self.evolutionary_operator = None
        self.fitness_evaluator = None
        self.selection_strategy = None
        self.generation = 0

    def create(self, candidate_factory, evolutionary_operator, fitness_evaluator, selection_strategy):
        if not isinstance(candidate_factory, CandidateFactory):
            raise TypeError('candidate_factory must be type of CandidateFactory.')
        self.candidate_factory = candidate_factory

        if not isinstance(evolutionary_operator, EvolutionaryOperator):
            raise TypeError('evolutionary_operator must be type of EvolutionaryOperator.')
        self.evolutionary_operator = evolutionary_operator

        if not isinstance(fitness_evaluator, FitnessEvaluator):
            raise TypeError('fitness_evaluator must be type of FitnessEvaluator.')
        self.fitness_evaluator = fitness_evaluator

        if not isinstance(selection_strategy, SelectionStrategy):
            raise TypeError('selection_strategy must be type of SelectionStrategy.')
        self.selection_strategy = selection_strategy

    def evolve(self, population_size, elite_count, termination_condition):
        self.generation = 0
        population = self.candidate_factory.create_population(population_size)
        self.evaluate_population(population)
        self.trigger_event(Event.INITIALIZE, {'population': population, 'generation': self.generation})
        should_terminate = termination_condition.should_terminate(population)
        while not should_terminate:
            self.generation += 1
            population = self.next_evolution_step(population, elite_count)
            self.evaluate_population(population)
            should_terminate = termination_condition.should_terminate(population)
        self.trigger_event(Event.TERMINATE, {'population': population, 'generation': self.generation})
        return population

    def evaluate_population(self, population):
        for candidate in population:
            candidate.fitness = self.fitness_evaluator.get_fitness(candidate, population)
        population.sort_by_fitness(is_natural=self.fitness_evaluator.is_natural)
        self.trigger_event(Event.EVALUATED_POPULATION, {'population': population, 'generation': self.generation})

    def next_evolution_step(self, population, elite_count):
        raise NotImplementedError()

    def add_observer(self, observer):
        if not isinstance(observer, Observer):
            raise TypeError('observer must be type of Observer')
        self.observers.append(observer)

    def trigger_event(self, event_type, event_data):
        event = Event(event_type, event_data)
        for observer in self.observers:
            observer.trigger(event)
