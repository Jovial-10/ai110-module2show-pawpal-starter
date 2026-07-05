"""Logic layer for PawPal+: Owner, Pet, Task, and Scheduler classes."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    name: str
    duration: int
    priority: str
    completed: bool = False

    def get_priority(self) -> str:
        pass

    def mark_complete(self) -> None:
        pass


@dataclass
class Pet:
    name: str
    type: str
    color: str
    hunger: int = 0
    tasks: List[Task] = field(default_factory=list)

    def get_name(self) -> str:
        pass

    def add_food(self, amount: int) -> None:
        pass

    def add_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass


class Owner:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_name(self) -> str:
        pass

    def get_pets(self) -> List[Pet]:
        pass


class Scheduler:
    def __init__(self, time_available: int):
        self.time_available = time_available
        self.plan: List[Task] = []

    def generate_plan(self, pet: Pet) -> List[Task]:
        pass

    def get_plan(self) -> List[Task]:
        pass

    def add_task(self, task: Task) -> None:
        pass
