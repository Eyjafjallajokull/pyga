from ..common import Event
from ..observer import Observer
from ..candidate_factory import CandidateFactory
from ..fitness_evaluator import FitnessEvaluator
from ..operator import EvolutionaryOperator
from ..selection_strategy import SelectionStrategy


class EvolutionEngine:
    """
    Abstract class for main controller of evolution process.
    """
    def __init__(self):
        self.observers = []
        self.candidate_factory = None
        self.evolutionary_operator = None
        self.fitness_evaluator = None
        self.selection_strategy = None
        self.generation = 0

    def create(self, candidate_factory, evolutionary_operator, fitness_evaluator, selection_strategy):
        """
        Initialize all components of an engine.

        :param candidate_factory: CandidateFactory
        :param evolutionary_operator: EvolutionaryOperator
        :param fitness_evaluator: FitnessEvaluator
        :param selection_strategy: SelectionStrategy
        :raises TypeError: When any of parameters is of invalid type.
        """
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
        """
        Heart of PyGA. Initializes population of candidates using CandidateFactory and processes it using
        FitnessEvaluator and EvolutionaryOperator. Function continues until TerminationCondition returns True.

        :param population_size: int
        :param elite_count: int Number of candidates to be preserved without applying evolutionary operator.
        :param termination_condition: TerminationCondition
        :return: Population
        """
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
        """
        Calculate fitness using FitnessEvaluator for all candidates in population.

        :param population: Population
        :return: Population
        """
        for candidate in population:
            candidate.fitness = self.fitness_evaluator.get_fitness(candidate, population)
        population.sort_by_fitness()
        self.trigger_event(Event.EVALUATED_POPULATION, {'population': population, 'generation': self.generation})

    def next_evolution_step(self, population, elite_count):
        """
        Abstract method, here all operations of selection, mutation, and crossover should be performed.

        :param population: Population
        :param elite_count: int Number of candidates to be preserved without applying evolutionary operator.
        :return: Population
        """
        raise NotImplementedError()

    def add_observer(self, observer):
        """
        Add observer for custom reporting of evolution progress.

        :param observer: Observer
        """
        if not isinstance(observer, Observer):
            raise TypeError('observer must be type of Observer')
        self.observers.append(observer)

    def trigger_event(self, event_type, event_data):
        """
        Trigger event on observer objects.

        :param event_type: See constants in Event class.
        :param event_data: dict
        """
        event = Event(event_type, event_data)
        for observer in self.observers:
            observer.trigger(event)
