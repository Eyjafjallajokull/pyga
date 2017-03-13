from pyga.factory import CandidateFactory
from pyga.candidate import Candidate


class BitStringFactory(CandidateFactory):
    def __init__(self, random, size):
        super().__init__(random)
        self.size = size

    def create_candidate(self):
        candidate = Candidate()
        candidate.data = ''.join([str(round(self.random.float())) for _ in range(self.size)])
        return candidate
