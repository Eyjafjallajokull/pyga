from pyga.common import Random


class Population(list):
    def shuffle(self):
        Random.shuffle(self)

    def append_list(self, genome_list):
        for genome in genome_list:
            self.append(genome)

    def sort_by_fitness(self, is_natural=True):
        self.sort(key=lambda x: x.fitness, reverse=not is_natural)

    def get_best(self, is_natural=True):
        best = self[0]
        for candidate in self:
            if (is_natural and candidate.fitness > best.fitness) or \
                    (not is_natural and candidate.fitness < best.fitness):
                best = candidate
        return best
