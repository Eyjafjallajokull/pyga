from pyga.population import Population


class CandidateFactory:
    def __init__(self, random):
        self.random = random

    def create_candidate(self):
        raise NotImplementedError()

    def create_population(self, size):
        population = Population()
        for i in range(size):
            population.append(self.create_candidate())
        return population
