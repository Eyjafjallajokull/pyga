import logging

import numpy

from ..common import Event
from .observer import Observer


class ConsoleObserver(Observer):
    """
    Basic EvolutionEngine observer which uses logging module to print debug information.
    """
    def trigger(self, event):
        """
        Print debug information.

        :param event: Event
        """
        if event.type == Event.INITIALIZE:
            logging.debug('initialized population')
        elif event.type == Event.EVALUATED_POPULATION:
            population = event.data['population']
            best = population.get_best()
            generation = event.data['generation']
            std = float(numpy.std([float(c.fitness) for c in population]))
            logging.debug('generation = %d; fitness: %.2f; std: %.2f; best candidate: %s' %
                          (generation, best.fitness, std, str(best.data)))
        elif event.type == Event.TERMINATE:
            logging.debug('finished processing')
