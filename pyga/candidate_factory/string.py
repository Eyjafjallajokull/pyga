from .candidate_factory import CandidateFactory
from ..candidate import Candidate


class StringFactory(CandidateFactory):
    """
    Generates candidates with data represented by fixed-length strings, using specified alphabet.

    :param random: Random number generator
    :param alphabet: string or list should contain unique characters
    :param size: int length of strings to generate
    """
    def __init__(self, random, alphabet, size):
        super().__init__(random)
        if isinstance(alphabet, str):
            alphabet = list(alphabet)
        self.alphabet = alphabet
        self.size = size

    def create_candidate(self):
        """
        Creates Candidate instance and randomly generates its data. Each character is randomly choosen from alphabet.

        :return: Candidate
        """
        candidate = Candidate()
        candidate.data = ''.join([self.random.choice(self.alphabet) for _ in range(self.size)])
        return candidate
