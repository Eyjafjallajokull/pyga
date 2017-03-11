from ..common import Event
from .observer import Observer
import logging


class ConsoleObserver(Observer):
    def trigger(self, event):
        if event.type == Event.EVALUATED_POPULATION:
            best = event.data['population'].get_best()
            generation = event.data['generation']
            logging.debug('generation = %d; best candidate: %s; fitness: %d' % (generation, str(best.data), best.fitness))
