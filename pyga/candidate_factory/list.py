from ..exception import ValidationException
from .candidate_factory import CandidateFactory
from ..candidate import Candidate


class ListFactory(CandidateFactory):
    """
    Generates candidates with data represented by integer list.

    :param random: Random number generator
    :param max_value: int maximum value, inclusive
    :param min_value: int minimum value, inclusive
    :param size: int length of list to generate
    :param is_unique: bool defines if list items should be unique
    """
    def __init__(self, random, max_value, min_value=0, size=None, is_unique=True):
        super().__init__(random)
        self.max_value = max_value
        self.min_value = min_value
        self.size = size
        self.is_unique = is_unique
        if self.size is None:
            self.size = max_value - min_value + 1
        if self.is_unique and self.max_value - self.min_value + 1 < self.size:
            raise ValidationException('ListFactory range is too low to generate enough values')

    def create_candidate(self):
        """
        Creates Candidate instance and randomly generates its data.

        :return: Candidate
        """
        candidate = Candidate()
        if self.is_unique:
            candidate.data = self.random.sample(range(self.min_value, self.max_value+1), self.size)
        else:
            candidate.data = [self.random.int(self.min_value, self.max_value+1) for _ in range(self.size)]
        return candidate
