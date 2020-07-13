from typing import List, Dict, Union, Tuple, Callable

Aliment = Dict[str, Union[str, int, float]]
DailyPlanning = Tuple[List[Aliment], List[Aliment], List[Aliment], List[Aliment], List[Aliment]]
WeeklyPlanning = Tuple[DailyPlanning, DailyPlanning, DailyPlanning, DailyPlanning, DailyPlanning, DailyPlanning]
Rule = Callable[[WeeklyPlanning], Union[int, float]]
Mutator = Callable[[WeeklyPlanning, List[Aliment]], None]
