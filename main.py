from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Alex", 30, "nonbinary")

biscuit = Pet("Biscuit", "Dog", "Golden", hunger=5)
biscuit.add_task(Task("Morning walk", 30, "high", start_time="09:00"))
biscuit.add_task(Task("Feeding", 10, "high", start_time="11:30"))

luna = Pet("Luna", "Cat", "Black", hunger=3)
luna.add_task(Task("Litter box cleaning", 15, "medium", start_time="07:00"))
luna.add_task(Task("Evening walk", 20, "medium", start_time="09:00"))  # conflicts with Biscuit's morning walk

owner.add_pet(biscuit)
owner.add_pet(luna)

scheduler = Scheduler(time_available=120)
plan = scheduler.generate_plan(owner)

plan = scheduler.filter_tasks()

print("Today's Schedule")
for pet, task in plan:
    print(f"{task.start_time} — {task.name} ({task.duration} min) [priority: {task.priority}] — {pet.get_name()}")

conflicts = scheduler.detect_conflicts()
if conflicts:
    print("\nScheduling Warnings")
    for warning in conflicts:
        print(f"⚠️  {warning}")
