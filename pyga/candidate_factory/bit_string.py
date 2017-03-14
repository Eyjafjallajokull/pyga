from .candidate_factory import CandidateFactory
from ..candidate import Candidate


class BitStringFactory(CandidateFactory):
    """
    Generates candidates with data represented by fixed-length binary strings.

    :param random: Random number generator
    :param size: int length of strings to generate
    """
    def __init__(self, random, size):
        super().__init__(random)
        self.size = size

    def create_candidate(self):
        """
        Creates Candidate instance and randomly generates its bit string data.

        :return: Candidate
        """
        candidate = Candidate()
        candidate.data = ''.join([str(round(self.random.float())) for _ in range(self.size)])
        return candidate
