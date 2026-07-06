"""Logic layer for PawPal+: Owner, Pet, Task, and Scheduler classes."""

from dataclasses import dataclass, field
from typing import List, Optional, Tuple

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


@dataclass
class Task:
    name: str
    duration: int
    priority: str
    start_time: Optional[str] = None
    frequency: str = "daily"
    completed: bool = False

    def get_priority(self) -> str:
        """Return this task's priority level."""
        return self.priority

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    type: str
    color: str
    hunger: int = 0
    tasks: List[Task] = field(default_factory=list)

    def get_name(self) -> str:
        """Return this pet's name."""
        return self.name

    def add_food(self, amount: int) -> None:
        """Feed the pet, reducing its hunger (floored at 0)."""
        self.hunger = max(0, self.hunger - amount)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return this pet's list of tasks."""
        return self.tasks


class Owner:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.pets: List[Pet] = []
        self.preferences: List[str] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's list of pets."""
        self.pets.append(pet)

    def get_name(self) -> str:
        """Return this owner's name."""
        return self.name

    def get_pets(self) -> List[Pet]:
        """Return this owner's list of pets."""
        return self.pets

    def get_preferences(self) -> List[str]:
        """Return this owner's scheduling preferences."""
        return self.preferences

    def get_all_tasks(self) -> List[Tuple[Pet, Task]]:
        """Return every (pet, task) pair across all of this owner's pets."""
        return [(pet, task) for pet in self.pets for task in pet.get_tasks()]


class Scheduler:
    def __init__(self, time_available: int):
        self.time_available = time_available
        self.plan: List[Tuple[Pet, Task]] = []

    def generate_plan(self, owner: Owner) -> List[Tuple[Pet, Task]]:
        """Build a priority-sorted plan of tasks that fits within the available time."""
        pending = [pair for pair in owner.get_all_tasks() if not pair[1].completed]
        pending.sort(key=lambda pair: PRIORITY_ORDER.get(pair[1].priority.lower(), len(PRIORITY_ORDER)))

        self.plan = []
        remaining_time = self.time_available
        for pet, task in pending:
            if task.duration <= remaining_time:
                self.plan.append((pet, task))
                remaining_time -= task.duration

        return self.plan

    def get_plan(self) -> List[Tuple[Pet, Task]]:
        """Return the most recently generated plan."""
        return self.plan

    def sort_by_time(self) -> List[Tuple[Pet, Task]]:
        """Sort the current plan by each task's start_time ("HH:MM"); tasks with no start_time sort last."""
        self.plan.sort(key=lambda pair: pair[1].start_time or "99:99")
        return self.plan

    def filter_tasks(
        self, completed: Optional[bool] = None, pet_name: Optional[str] = None
    ) -> List[Tuple[Pet, Task]]:
        """Return plan entries filtered by completion status and/or pet name."""
        return [
            (pet, task)
            for pet, task in self.plan
            if (completed is None or task.completed == completed)
            and (pet_name is None or pet.name == pet_name)
        ]

    def schedule_task(self, pet: Pet, task: Task) -> None:
        """Manually append a (pet, task) pair to the current plan."""
        self.plan.append((pet, task))
