from pyga.factory import CandidateFactory
from pyga.candidate import Candidate


class StringFactory(CandidateFactory):
    def __init__(self, random, alphabet, size):
        super().__init__(random)
        if isinstance(alphabet, str):
            alphabet = list(alphabet)
        self.alphabet = alphabet
        self.size = size

    def create_candidate(self):
        candidate = Candidate()
        candidate.data = ''.join([self.random.choice(self.alphabet) for _ in range(self.size)])
        return candidate