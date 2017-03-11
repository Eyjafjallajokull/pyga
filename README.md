```
    _______  __   __  _______  _______
   |       ||  | |  ||       ||   _   |
   |    _  ||  |_|  ||    ___||  |_|  |
   |   |_| ||       ||   | __ |       |   Python framework for applying
   |    ___||_     _||   ||  ||       |   Genetic Algorithms
   |   |      |   |  |   |_| ||   _   |
   |___|      |___|  |_______||__| |__|
```

[![Build Status](https://travis-ci.org/Eyjafjallajokull/pyga.svg?branch=master)](https://travis-ci.org/Eyjafjallajokull/pyga)
[![codecov](https://codecov.io/gh/Eyjafjallajokull/pyga/branch/master/graph/badge.svg)](https://codecov.io/gh/Eyjafjallajokull/pyga)

## Usage

```
engine = GenerationalEvolutionEngine()
engine.create(candidate_factory, operator, fitness_evaluator, selection_strategy)
population = engine.evolve(population_size, elite_count, termination_condition)

print(population.get_best())
```

## Examples

```console
python examples/match_string.py
```

## Tests

```console
make test
make coverage
```