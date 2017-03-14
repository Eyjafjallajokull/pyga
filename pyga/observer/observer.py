class Observer:
    """
    Abstract class for implementation of observers used to monitor EvolutionEngine process.
    """
    def trigger(self, event):
        """
        This function is trigger by EvolutionEngine when particular event occurs.

        :param event: Event
        """
        raise NotImplementedError()
