class Population(list):
    def __add__(self, other):
        self.append_list(other)
        return self

    def append_list(self, candidate_list):
        for candidate in candidate_list:
            self.append(candidate)

    def sort_by_fitness(self):
        if not len(self):
            return
        is_natural = self[0].fitness.is_natural
        self.sort(key=lambda x: x.fitness, reverse=not is_natural)

    def get_best(self):
        if not len(self):
            return None
        best = self[0]
        is_natural = self[0].fitness.is_natural
        for candidate in self:
            if (is_natural and candidate.fitness > best.fitness) or \
                    (not is_natural and candidate.fitness < best.fitness):
                best = candidate
        return best
