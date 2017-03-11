from unittest import TestCase

from pyga import Event, ConsoleObserver, Population, Genome


class ConsoleObserverTestCase(TestCase):
    def test_trigger(self):
        genome = Genome()
        genome.fitness = 1
        population = Population([genome])
        observer = ConsoleObserver()
        observer.trigger(Event(Event.INITIALIZE, {'population': population}))
        observer.trigger(Event(Event.EVALUATED_POPULATION, {'generation': 1, 'population': population}))
        observer.trigger(Event(Event.TERMINATE, {'generation': 1, 'population': population}))
