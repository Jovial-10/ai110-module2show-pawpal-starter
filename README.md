# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Output from running `python main.py`:

```
Today's Schedule
08:00 — Morning walk (30 min) [priority: high] — Biscuit
08:30 — Feeding (10 min) [priority: high] — Biscuit
09:00 — Litter box cleaning (15 min) [priority: medium] — Luna
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```
====================================================================== test session starts ======================================================================
platform darwin -- Python 3.13.5, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/jovialrana/Documents/CodePath/ai110-module2show-pawpal-starter
plugins: anyio-4.14.1
collected 10 items                                                                                                                                              

tests/test_pawpal.py ..........                                                                                                                           [100%]

====================================================================== 10 passed in 0.02s =======================================================================

My tests cover scheduling conflicts, errors with marking completing tasks, and issues with adding tasks

Confidence Level: 4

## ✨ Features

### Priority-First Planning
`Scheduler.generate_plan(owner)` collects every pending (incomplete) task across all of an owner's pets, sorts them by priority (`high` → `medium` → `low`), and greedily packs them into the available time. If a higher-priority task doesn't fit, it's skipped rather than stopping the loop, so a smaller, lower-priority task later in line still gets a chance to fill the remaining time.

### Sorting by Time
`Scheduler.sort_by_time()` reorders the generated plan chronologically by each task's `start_time` (zero-padded `"HH:MM"` strings, compared lexicographically). Tasks with no `start_time` are pushed to the end instead of breaking the sort.

### Conflict Warnings
`Scheduler.detect_conflicts()` scans the current plan for tasks scheduled at the exact same `start_time` — regardless of which pet they belong to — and returns a list of human-readable warning strings instead of raising an error. It only catches exact time collisions, not partial overlaps between tasks with different durations.

### Filtering
`Scheduler.filter_tasks(completed=None, pet_name=None)` returns a filtered view of the plan by completion status and/or pet name, without mutating the underlying plan. Either filter can be omitted; combining both applies an AND.

### Daily/Weekly Recurrence
`Task.mark_complete()` marks a task completed and, if its `frequency` is `"daily"` or `"weekly"`, returns a new `Task` due one day or one week after its original `due_date` (or today, if unset). `Scheduler.complete_task(pet, task)` wraps this and automatically appends the new occurrence to the pet's task list, so recurring tasks regenerate themselves without manual re-entry.

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts the current plan chronologically by each task's `start_time` (`"HH:MM"` string comparison). Tasks with no `start_time` are pushed to the end. |
| Filtering | `Scheduler.filter_tasks(completed=None, pet_name=None)` | Returns plan entries filtered by completion status and/or pet name. Either argument can be omitted to skip that filter; combining both is an AND. |
| Conflict handling | `Scheduler.detect_conflicts()` | Groups the current plan by exact `start_time` and returns a warning message for every pair of tasks (same or different pets) scheduled at the same time, instead of raising an error. Note: it only catches exact time matches, not partial overlaps between tasks with different durations. |
| Recurring tasks | `Task.mark_complete()`, `Scheduler.complete_task()` | Marking a `"daily"` or `"weekly"` task complete returns a new `Task` due `today + timedelta(days=1)` or `+timedelta(days=7)`. `Scheduler.complete_task()` appends that new occurrence to the pet's task list automatically. |

## 📸 Demo Walkthrough

### Main UI features
- Enter owner and pet basic info (owner name, pet name, species).
- Add tasks with a title, duration (minutes), and priority (`low`/`medium`/`high`).
- View the pet's current task list in a table.
- Generate today's schedule from the scheduler, sorted chronologically by start time.
- See a confirmation message summarizing how many tasks were scheduled and how much time was used.
- See a warning for any tasks scheduled at the same time as another task.

### Example workflow
1. Enter an owner name (e.g., "Jordan") and add a pet (e.g., "Mochi", species "dog").
2. Add a task using the "Add task" form — e.g., "Morning walk", 20 minutes, high priority. Repeat for as many tasks as needed.
3. Review the "Current tasks" table to confirm everything was added correctly.
4. Click "Generate schedule." The scheduler pulls every pending task for the pet, sorts by priority, and greedily packs as many as fit into the available time (120 minutes by default).
5. View "Today's Schedule" as a table sorted by start time, along with a success message and any conflict warnings.

### Key Scheduler behaviors shown
- **Priority-first packing**: high-priority tasks are considered before medium/low, but a lower-priority task can still fill leftover time a higher-priority task couldn't fit into.
- **Chronological sorting**: the displayed schedule is ordered by `start_time` via `sort_by_time()`, not by priority or insertion order.
- **Conflict detection**: if two tasks share the same `start_time`, `detect_conflicts()` surfaces a warning instead of silently double-booking.

### Sample CLI output
Output from running `python main.py`:

```
Today's Schedule
09:00 — Morning walk (30 min) [priority: high] — Biscuit
11:30 — Feeding (10 min) [priority: high] — Biscuit
07:00 — Litter box cleaning (15 min) [priority: medium] — Luna
09:00 — Evening walk (20 min) [priority: medium] — Luna

Scheduling Warnings
⚠️  Conflict at 09:00: 'Evening walk' (Luna) clashes with 'Morning walk' (Biscuit)
```

Note: `main.py` calls `generate_plan()` and `filter_tasks()` but not `sort_by_time()`, so this output is in priority-packing order rather than chronological order — the Streamlit UI (`app.py`) calls `sort_by_time()` before displaying the plan, so its table is time-sorted.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
