import random
from typing import List

from custom_types import Aliment, WeeklyPlanning


def mutate_aliment(planning: WeeklyPlanning, possible_aliments: List[Aliment]):
    lunch = random.choice(random.choice(planning))
    try:
        random_index = random.randrange(0, len(lunch))
    except ValueError:
        pass
    else:
        aliment = random.choice(possible_aliments)
        lunch[random_index] = aliment


def remove_aliment(planning: WeeklyPlanning, _: List[Aliment]):
    lunch: list = random.choice(random.choice(planning))
    try:
        random_index = random.randrange(0, len(lunch))
    except ValueError:
        pass
    else:
        del lunch[random_index]


def add_aliment(planning: WeeklyPlanning, possible_aliments: List[Aliment]):
    lunch: list = random.choice(random.choice(planning))
    lunch.append(random.choice(possible_aliments))


mutators = [mutate_aliment, remove_aliment, add_aliment]
