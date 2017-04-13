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

## Project status: preparing first release

PyGa is a flexible, object-oriented framework for developing genetic algorithms in Python.

## Features

* Pluggable architecture -- source code is decoupled into many independent classes which can be used to build custom solutions.
* Batteries included -- most common selection strategies and evolutionary operators are already implemented.

## Installation

Until first release, package will not be published to pip repository.
Currently the only way to obtain code is to do `git clone` or download zip.

## Getting Started

Note: You should be familiar with how genetic algorithms work and what are basic components of the process.

```
engine = GenerationalEvolutionEngine()
engine.create(candidate_factory, operator, fitness_evaluator, selection_strategy)
population = engine.evolve(population_size, elite_count, termination_condition)

print(population.get_best())
```

## Examples

Some basic examples are available to give You an idea how PyGA works.

Evolve population of random strings to match "Hello World":

```console
python examples/match_string.py
DEBUG:root:generation = 0; best candidate: ooW e WdWod; fitness: 3
DEBUG:root:initialized population
DEBUG:root:generation = 1; best candidate: ooldd WdWod; fitness: 4
// snip
DEBUG:root:generation = 65; best candidate: Hello World; fitness: 11
DEBUG:root:finished processing
28056635-7393-43d9-8e3e-a2ebf6dc02bf
```

## Documentation

## Tests

The source code is very well covered by tests. To run all checks, run:

```console
make test
```

To execute tests and generate code coverage report, run:

```console
make coverage
```

## Credits

- [Watchmaker](https://github.com/dwdyer/watchmaker) for inspiration