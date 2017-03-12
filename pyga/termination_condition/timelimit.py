from time import time

from .termination_condition import TerminationCondition


class TimeLimit(TerminationCondition):
    def __init__(self, seconds):
        self.seconds = seconds
        self._start_time = None

    def should_terminate(self, population):
        if not self._start_time:
            self._start_time = time()
        return self._start_time + self.seconds < time()
