from datetime import date, timedelta

from pawpal_system import Pet, Scheduler, Task


def test_mark_complete_changes_status():
    task = Task("Feeding", 10, "high")
    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet("Biscuit", "Dog", "Golden")
    assert len(pet.get_tasks()) == 0

    pet.add_task(Task("Morning walk", 30, "high"))

    assert len(pet.get_tasks()) == 1


def test_sort_by_time_returns_chronological_order():
    pet = Pet("Biscuit", "Dog", "Golden")
    scheduler = Scheduler(time_available=120)
    scheduler.schedule_task(pet, Task("Evening walk", 30, "high", start_time="18:00"))
    scheduler.schedule_task(pet, Task("Morning walk", 30, "high", start_time="08:00"))
    scheduler.schedule_task(pet, Task("Midday feeding", 10, "high", start_time="12:00"))

    sorted_plan = scheduler.sort_by_time()

    assert [task.start_time for _, task in sorted_plan] == ["08:00", "12:00", "18:00"]


def test_sort_by_time_pushes_missing_start_time_to_end():
    pet = Pet("Biscuit", "Dog", "Golden")
    scheduler = Scheduler(time_available=120)
    scheduler.schedule_task(pet, Task("Unscheduled play", 15, "low"))
    scheduler.schedule_task(pet, Task("Morning walk", 30, "high", start_time="08:00"))

    sorted_plan = scheduler.sort_by_time()

    assert [task.start_time for _, task in sorted_plan] == ["08:00", None]


def test_mark_complete_daily_task_rolls_forward_one_day():
    today = date(2026, 7, 7)
    task = Task("Feeding", 10, "high", frequency="daily", due_date=today)

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is not None
    assert next_task.completed is False
    assert next_task.due_date == today + timedelta(days=1)
    assert next_task.name == task.name


def test_mark_complete_non_recurring_task_does_not_roll_forward():
    task = Task("Vet visit", 60, "high", frequency="once")

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is None


def test_complete_task_appends_next_occurrence_to_pet():
    pet = Pet("Biscuit", "Dog", "Golden")
    task = Task("Feeding", 10, "high", frequency="daily")
    pet.add_task(task)
    scheduler = Scheduler(time_available=120)
    scheduler.schedule_task(pet, task)

    scheduler.complete_task(pet, task)

    assert len(pet.get_tasks()) == 2
    assert pet.get_tasks()[1].completed is False
    assert pet.get_tasks()[1].due_date == date.today() + timedelta(days=1)


def test_detect_conflicts_flags_same_start_time_across_pets():
    biscuit = Pet("Biscuit", "Dog", "Golden")
    luna = Pet("Luna", "Cat", "Black")
    scheduler = Scheduler(time_available=120)
    scheduler.schedule_task(biscuit, Task("Morning walk", 30, "high", start_time="08:00"))
    scheduler.schedule_task(luna, Task("Litter box cleaning", 15, "medium", start_time="08:00"))

    warnings = scheduler.detect_conflicts()

    assert len(warnings) == 1
    assert "08:00" in warnings[0]


def test_detect_conflicts_ignores_tasks_without_start_time():
    pet = Pet("Biscuit", "Dog", "Golden")
    scheduler = Scheduler(time_available=120)
    scheduler.schedule_task(pet, Task("Unscheduled play", 15, "low"))
    scheduler.schedule_task(pet, Task("Another unscheduled task", 10, "low"))

    warnings = scheduler.detect_conflicts()

    assert warnings == []


def test_detect_conflicts_no_warnings_for_distinct_times():
    pet = Pet("Biscuit", "Dog", "Golden")
    scheduler = Scheduler(time_available=120)
    scheduler.schedule_task(pet, Task("Morning walk", 30, "high", start_time="08:00"))
    scheduler.schedule_task(pet, Task("Feeding", 10, "high", start_time="08:30"))

    warnings = scheduler.detect_conflicts()

    assert warnings == []
