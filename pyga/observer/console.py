import logging
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
            best = event.data['population'].get_best()
            generation = event.data['generation']
            logging.debug('generation = %d; best candidate: %s; fitness: %d' % (generation, str(best.data), best.fitness))
        elif event.type == Event.TERMINATE:
            logging.debug('finished processing')
