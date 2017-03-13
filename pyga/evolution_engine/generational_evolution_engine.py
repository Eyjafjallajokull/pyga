from pyga.population import Population
from .evolution_engine import EvolutionEngine


class GenerationalEvolutionEngine(EvolutionEngine):
    def next_evolution_step(self, population, elite_count):
        if len(population) < elite_count:
            raise RuntimeError('population size is lower then elite_count')
        elite_population = Population(population[-elite_count:])
        self.selection_strategy.validate(population, len(population)-elite_count)
        next_population = self.selection_strategy.select(population,
                                                         len(population)-elite_count)
        self.evolutionary_operator.apply(next_population)
        return Population(next_population + elite_population)
