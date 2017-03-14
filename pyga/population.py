class Population(list):
    """
    Represents collection of candidates in specific state. This class inherits from list type, so it is possible to
    access members using ``population[12]`` or slice it with ``population[-5:]``.
    """

    def __add__(self, other):
        self.append_list(other)
        return self

    def append_list(self, candidate_list):
        """
        Append list of candidates to current population.

        :param candidate_list: list of Candidate objects
        """
        for candidate in candidate_list:
            self.append(candidate)

    def sort_by_fitness(self):
        """
        Sort candidates in order from worst fitness to the best. Doesn't matter if fitness is natural or not.
        """
        if not len(self):
            return
        is_natural = self[0].fitness.is_natural
        self.sort(key=lambda x: x.fitness, reverse=not is_natural)

    def get_best(self):
        """
        Returns candidate with the best fitness.

        :return: Candidate
        """
        if not len(self):
            return None
        best = self[0]
        is_natural = self[0].fitness.is_natural
        for candidate in self:
            if (is_natural and candidate.fitness > best.fitness) or \
                    (not is_natural and candidate.fitness < best.fitness):
                best = candidate
        return best
