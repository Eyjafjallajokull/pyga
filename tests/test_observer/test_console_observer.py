from unittest import TestCase

from pyga import Event, ConsoleObserver, Population, Candidate, Fitness


class ConsoleObserverTestCase(TestCase):
    def test_trigger(self):
        candidate = Candidate()
        candidate.fitness = Fitness(1)
        population = Population([candidate])
        observer = ConsoleObserver()
        observer.trigger(Event(Event.INITIALIZE, {'population': population}))
        observer.trigger(Event(Event.EVALUATED_POPULATION, {'generation': 1, 'population': population}))
        observer.trigger(Event(Event.TERMINATE, {'generation': 1, 'population': population}))
