class FitnessEvaluator:
    def __init__(self):
        self.is_natural = True

    def get_fitness(self, candidate, population):
        raise NotImplementedError()
