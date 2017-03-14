from time import time

from .termination_condition import TerminationCondition


class TimeLimit(TerminationCondition):
    def __init__(self, seconds):
        self.seconds = seconds
        self._start_time = None

    def should_terminate(self, population):
        """
        Executed by EvolutionEngine to determine when to end process. Returns True if evolution process should be
        terminated.

        Returns True when specified number of seconds passed.

        Note: counter is started when this method is first called.

        :param population: Population
        :return: boolean
        """
        if not self._start_time:
            self._start_time = time()
        return self._start_time + self.seconds < time()
