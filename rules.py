from collections import Counter

from custom_types import WeeklyPlanning


def egg_with_pasta(planning: WeeklyPlanning) -> int:
    score = 0
    for daily_planning in planning:
        for lunch in daily_planning:
            aliments_names = {aliment["name"] for aliment in lunch}
            if {"egg", "pasta"}.issubset(aliments_names):
                score += 1
    return score


def proteins_by_day(planning: WeeklyPlanning) -> float:
    proteins = 0
    for daily_planning in planning:
        for lunch in daily_planning:
            for aliment in lunch:
                proteins += aliment.get("proteins", 0)
    return 5 / (1 + abs(112 - proteins))


def energy_by_day(planning: WeeklyPlanning) -> float:
    energy = 0
    for daily_planning in planning:
        for lunch in daily_planning:
            for aliment in lunch:
                energy += aliment.get("energy", 0)
    return 5 / (1 + abs(869 - energy))


def proteins_after_workout(planning: WeeklyPlanning) -> int:
    score = 0
    for daily_planning in planning[::2]:
        if max(daily_planning, key=lambda p: sum(a["proteins"] for a in p)) is daily_planning[-1]:
            score += 1
    return score


def no_empty_lunch(planning: WeeklyPlanning) -> int:
    return int(bool(planning))


def enough_vegetables(planning: WeeklyPlanning) -> float:
    vegetable_mass = 0
    for daily_planning in planning:
        for lunch in daily_planning:
            for aliment in lunch:
                if "vegetable" in aliment.get("tags", []):
                    vegetable_mass += aliment.get("mass", 0)
    return vegetable_mass / 40


def not_too_much_aliments(planning: WeeklyPlanning) -> int:
    score = 0
    for daily_planning in planning:
        for lunch in daily_planning:
            if len(lunch) <= 5:
                score += 1
    return score


def not_too_much_repetition(planning: WeeklyPlanning) -> int:
    score = 10
    for daily_planning in planning:
        for lunch in daily_planning:
            counter = {}
            for aliment in lunch:
                if aliment["name"] not in counter:
                    counter[aliment["name"]] = 0
                counter[aliment["name"]] += 1
                if counter[aliment["name"]] > 2:
                    score -= 1
    return max(score, 0)


def all_egg(planning):
    score = 0
    for daily_planning in planning:
        for lunch in daily_planning:
            for aliment in lunch:
                if aliment["name"] == "egg":
                    score += 1
    return score


rules = [
    # egg_with_pasta,
    proteins_by_day,
    energy_by_day,
    proteins_after_workout,
    no_empty_lunch,
    enough_vegetables,
    no_empty_lunch,
    not_too_much_repetition,
    all_egg,
]
