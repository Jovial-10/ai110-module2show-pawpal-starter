from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Alex", 30, "nonbinary")

biscuit = Pet("Biscuit", "Dog", "Golden", hunger=5)
biscuit.add_task(Task("Morning walk", 30, "high", start_time="08:00"))
biscuit.add_task(Task("Feeding", 10, "high", start_time="08:30"))

luna = Pet("Luna", "Cat", "Black", hunger=3)
luna.add_task(Task("Litter box cleaning", 15, "medium", start_time="09:00"))

owner.add_pet(biscuit)
owner.add_pet(luna)

scheduler = Scheduler(time_available=120)
plan = scheduler.generate_plan(owner)

print("Today's Schedule")
for pet, task in plan:
    print(f"{task.start_time} — {task.name} ({task.duration} min) [priority: {task.priority}] — {pet.get_name()}")
