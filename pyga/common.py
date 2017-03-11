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


class Event:
    EVALUATED_POPULATION = 1
    TERMINATE = 2

    def __init__(self, event_type, data):
        self.type = event_type
        self.data = data
