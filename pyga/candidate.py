import uuid


class Candidate:
    """
    Represents single candidate for problem resolution.

    Properties:
        fitness: Fitness

        data: candidate representation of resolution

    """
    def __init__(self):
        self.data = {}
        self.fitness = None
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return self.id

