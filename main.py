import json
import random
from typing import List, Iterable, Collection

from custom_types import Aliment, WeeklyPlanning, Rule, Mutator
from mutators import mutators
from rules import rules


def build_lunch_planning(aliments: List[Aliment]) -> WeeklyPlanning:
    # Type checker cannot figure out the return type of random.choices
    # noinspection PyTypeChecker
    return [[random.choices(aliments, k=1) for _ in range(4)] for _ in range(6)]


def print_random_planning():
    with open("aliments.json") as file:
        print(json.dumps(build_lunch_planning(json.load(file)), indent=2))


def compute_planning_fitness(planning: WeeklyPlanning, rules: Iterable[Rule]) -> int:
    return sum(rule(planning) for rule in rules)


def mutate_planning(planning: WeeklyPlanning, possible_aliments: List[Aliment], mutators: Collection[Mutator]):
    mutator: Mutator = random.choices(mutators, weights=[0.7, 0.16, 0.14], k=1)[0]
    mutator(planning, possible_aliments)


def main(
    population_size: int,
    aliments_db_path: str,
    rules: Iterable[Rule],
    generation_number: int,
    mutators: Collection[Mutator],
):
    with open(aliments_db_path) as file:
        aliments: List[Aliment] = json.load(file)

    population = [build_lunch_planning(aliments) for _ in range(population_size)]

    for gen_index in range(generation_number):
        for planning in population:
            if random.random() > 0.01:
                mutate_planning(planning, aliments, mutators)

        scores = [compute_planning_fitness(planning, rules) ** 10 for planning in population]
        population = random.choices(population, scores, k=population_size)

        with open(f"out/{gen_index}.json", "w") as file:
            file.write(
                json.dumps(
                    [
                        [[[k["name"] for k in j] for j in n] for n in i]
                        for i in sorted(population[:10], key=lambda p: compute_planning_fitness(p, rules))
                    ],
                    indent=2,
                )
            )


if __name__ == "__main__":
    main(population_size=100, aliments_db_path="aliments.json", rules=rules, generation_number=200, mutators=mutators)
