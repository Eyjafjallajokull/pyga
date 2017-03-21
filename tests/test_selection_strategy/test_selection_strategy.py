from unittest import TestCase

from pyga import Population
from pyga import SelectionStrategy
from pyga import ValidationException


class SelectionStrategyTestCase(TestCase):
    def setUp(self):
        self.obj = SelectionStrategy()

    def test_validation_selection_size(self):
        with self.assertRaises(ValidationException):
            self.obj.validate(Population(), 0)

    def test_validation_population_size(self):
        with self.assertRaises(ValidationException):
            self.obj.validate(Population(), 5)