from random import random, randint, choice, sample, shuffle

from pyga.exception import ValidationException


class Random:
    @staticmethod
    def float():
        return random()

    @staticmethod
    def int(a, b):
        return randint(a, b)

    @staticmethod
    def boolean():
        return Random.float() > 0.5

    @staticmethod
    def choice(seq):
        return choice(seq)

    @staticmethod
    def sample(seq, number):
        return sample(seq, number)

    @staticmethod
    def shuffle(seq):
        shuffle(seq)


class Probability:
    def __init__(self, value, random_generator=Random):
        if value > 1:
            raise ValidationException('Probability value must be between 0, 1')
        self.value = value
        self.random = random_generator

    def get_boolean(self):
        return self.random.float() < self.value


class Fitness:
    def __init__(self, value, is_natural=True):
        self.value = value
        self.is_natural = is_natural

    def __repr__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __bool__(self):
        return self.value is not None

    def __add__(self, other):
        return self.value + float(other)

    def __sub__(self, other):
        return self.value - float(other)

    def __mul__(self, other):
        return self.value * float(other)

    def __lt__(self, other):
        return self.value < float(other)

    def __le__(self, other):
        return self.value <= float(other)

    def __eq__(self, other):
        return self.value == float(other)

    def __ne__(self, other):
        return self.value != float(other)

    def __ge__(self, other):
        return self.value >= float(other)

    def __gt__(self, other):
        return self.value > float(other)

    def __abs__(self):
        return abs(self.value)

class Event:
    EVALUATED_POPULATION = 1
    TERMINATE = 2
    INITIALIZE = 3

    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data
