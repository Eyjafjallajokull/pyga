from .roulette_wheel import RouletteWheelSelection


class RankSelection(RouletteWheelSelection):
    def select(self, population, selection_size):
        self._is_natural = population[0].fitness.is_natural
        self._fitness_sum = None

        max_ = max(self.get_segments(population))
        pointers = [self.random.float() * max_ for _ in range(selection_size)]
        selected = self.roulette(population, pointers)
        return selected

    def get_segments(self, population):
        segments = [1]
        for i in range(1, len(population)):
            segments.append(segments[i - 1] + i)
        return segments
