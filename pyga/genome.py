import uuid


class Genome:
    def __init__(self):
        self.data = {}
        self.fitness = None
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return self.id

