import sys
import os
import logging
from collections import defaultdict

sys.path.append(os.environ["PWD"])
from pyga import *

population_size = 100
elite_count = 5
crossover_points = 2
crossover_probability = 0.2
mutate_probability = 0.5
max_day_span = 2
max_hour_span = 8
teachers = [
    ['Anna'],
    ['Susan'],
    ['John'],
    ['Oliver'],
    ['Victoria']
]
courses = [
    # class name, teacher id
    ['Polish beginner', 1],
    ['Polish intermediate', 1],
    ['Italian beginner', 2],
    ['English beginner', 3],
    ['Spanish beginner', 0],
    ['Spanish intermediate', 0],
    ['German beginner', 3],
]
classes = [
    # course id, duration
    [0, 2],
    [0, 2],
    [1, 1],
    [1, 1],
    [1, 1],
    [2, 1],
    [3, 1],
    [4, 2],
    [5, 2],
]
classrooms = [
    ['west'],
    ['east']
]


class CustomData(list):
    VALID_FITNESS = 10000

    def init(self, random):
        for _ in range(len(classes)):
            self.append([
                random.int(0, max_day_span-1),
                random.int(0, max_hour_span-1),
                random.int(0, len(classrooms)-1)])
        return self

    def mutate(self, probability, random):
        for i in range(len(self)):
            if probability.get_boolean():
                self[i][0] = random.int(0, max_day_span-1)
            if probability.get_boolean():
                self[i][1] = random.int(0, max_hour_span-1)
            if probability.get_boolean():
                self[i][2] = random.int(0, len(classrooms)-1)

    def mate(self, probability, random, other):
        for i in range(len(self)):
            if probability.get_boolean():
                f = random.float()
                if f < 0.3:
                    tmp = self[i][0]
                    self[i][0] = other.data[i][0]
                    other.data[i][0] = tmp
                elif f < 0.6:
                    tmp = self[i][1]
                    self[i][1] = other.data[i][1]
                    other.data[i][1] = tmp
                else:
                    tmp = self[i][2]
                    self[i][2] = other.data[i][2]
                    other.data[i][2] = tmp

    @staticmethod
    def decode(data):
        results = []
        for i, class_data in enumerate(data):
            results.append({'class': i,
                            'course': classes[i][0],
                            'duration': classes[i][1],
                            'day': class_data[0],
                            'hour': class_data[1],
                            'classroom': class_data[2]})
        return results

    @staticmethod
    def get_fitness(candidate, population):
        data = CustomData.decode(candidate.data)
        data.sort(key=lambda x: x['day']*24 + x['hour'])
        fitness = float(CustomData.VALID_FITNESS)
        for ci, c in enumerate(data):
            if ci == len(data)-1:
                continue
            for d in data[ci+1:]:
                if CustomData.time_overlap(c, d):
                    # teacher overlaps
                    c_teacher = teachers[courses[c['course']][1]]
                    d_teacher = teachers[courses[d['course']][1]]
                    if c_teacher == d_teacher:
                        fitness -= 1

                    # classroom overlaps
                    if c['classroom'] == d['classroom']:
                        fitness -= 1

                if c['course'] == d['course'] and c['day'] == d['day']:
                    space = d['hour'] - c['hour']+c['duration']
                    if space > 1:
                        fitness += 0.01

        return Fitness(fitness)

    @staticmethod
    def time_overlap(c, d):
        return c['day'] == d['day'] and \
                                c['hour'] <= d['hour']+d['duration'] and d['hour'] <= c['hour']+c['duration']


class CustomDataCandidateFactory(CandidateFactory):
    def create_candidate(self):
        candidate = Candidate()
        candidate.data = CustomData().init(self.random)
        return candidate


class CustomDataMutation(Mutation):
    def __init__(self, probability, random):
        super().__init__()
        self.probability = probability
        self.random = random

    def mutate(self, data):
        data.mutate(self.probability, self.random)
        return data


class CustomDataCrossover(Crossover):
    def mate(self, parent1, parent2):
        parent1.data.mate(self.probability, self.random, parent2)
        return parent1, parent2


def print_results(result):
    data = CustomData.decode(result.data)
    if result.fitness != CustomData.VALID_FITNESS:
        print('Could not find valid class schedule, try to increase time span, or reduce number of classes')

    print('Chronological calendar:')
    data.sort(key=lambda x: x['day']*24 + x['hour'])
    for c in data:
        print(c['day'], c['hour'], '-', c['hour']+c['duration'], courses[c['course']][0], teachers[courses[c['course']][1]][0], classrooms[c['classroom']][0])
    print()

    print('Teacher calendars:')
    data_by_teachers = defaultdict(list)
    for c in data:
        data_by_teachers[courses[c['course']][1]].append(c)
    for teacher, teacher_classes in data_by_teachers.items():
        print(teachers[teacher][0])
        for c in teacher_classes:
            print(c['day'], c['hour'], '-', c['hour']+c['duration'], courses[c['course']][0], classrooms[c['classroom']][0])
    print()

    print('Classroom calendars:')
    data_by_classrooms = defaultdict(list)
    for c in data:
        data_by_classrooms[c['classroom']].append(c)
    for classroom, classroom_classes in data_by_classrooms.items():
        print(classrooms[classroom][0])
        for c in classroom_classes:
            print(c['day'], c['hour'], '-', c['hour'] + c['duration'], courses[c['course']][0], teachers[courses[c['course']][1]][0])
    print()

    print('Course calendars:')
    data_by_course = defaultdict(list)
    for c in data:
        data_by_course[c['course']].append(c)
    for course, course_classes in data_by_course.items():
        print(courses[course][0], teachers[courses[c['course']][1]][0])
        for c in course_classes:
            print(c['day'], c['hour'], '-', c['hour'] + c['duration'], classrooms[c['classroom']][0])

logging.basicConfig(level=logging.DEBUG)
random = Random()
crossover_probability = Probability(crossover_probability, random)
mutate_probability = Probability(mutate_probability, random)
candidate_factory = CustomDataCandidateFactory(random)
crossover = CustomDataCrossover(crossover_probability, random)
mutation = CustomDataMutation(mutate_probability, random)
operator = PipelineOperator()
operator.append_operator(crossover)
operator.append_operator(mutation)
fitness_evaluator = CallbackFitnessEvaluator(CustomData.get_fitness)
selection_strategy = RouletteWheelSelection(random)
termination_condition = Stagnation(500)

engine = GenerationalEvolutionEngine()
engine.add_observer(ConsoleObserver())
engine.create(candidate_factory, operator, fitness_evaluator, selection_strategy)
population = engine.evolve(population_size, elite_count, termination_condition)

print_results(population.get_best())
