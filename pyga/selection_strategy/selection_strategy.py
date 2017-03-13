from ..exception import ValidationException


class SelectionStrategy:
    def __init__(self):
        pass

    def select(self, population, selection_size):
        raise NotImplementedError()

    def validate(self, population, selection_size):
        if selection_size < 1:
            raise ValidationException('selection_size must not be lower then 1')
        if len(population) < selection_size:
            raise ValidationException('selection_size is greater then Population size')