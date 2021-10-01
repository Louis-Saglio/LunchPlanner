from random import choice
from SudokuSolver.genetic import Individual, Number


def generate_random_genome(size=100, bases="01"):
    return [choice(bases) for _ in range(size)]


class SimpleIndividual(Individual):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.genome = generate_random_genome()

    @property
    def floor(self):
        return -len(self.genome)

    @property
    def maxi(self):
        return len(self.genome) * 2

    def _rate(self) -> Number:
        return self.genome.count("1") - self.genome.count("0")

    def mutate(self):
        self

    def clone(self) -> "Individual":
        pass

    def mate(self, other: "Individual") -> "Individual":
        pass
