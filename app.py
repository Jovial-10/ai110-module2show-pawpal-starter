import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

if "owner" not in st.session_state:
    st.session_state.owner = Owner(owner_name, age=0, gender="unspecified")

if "pet" not in st.session_state:
    pet = Pet(pet_name, species, color="unknown")
    st.session_state.owner.add_pet(pet)
    st.session_state.pet = pet

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(time_available=120)

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.pet.add_task(Task(task_title, int(duration), priority))

pet_tasks = st.session_state.pet.get_tasks()
if pet_tasks:
    st.write("Current tasks:")
    st.table(
        [{"title": t.name, "duration_minutes": t.duration, "priority": t.priority} for t in pet_tasks]
    )
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("Generates today's plan from the scheduler and the pet's tasks.")

if st.button("Generate schedule"):
    plan = st.session_state.scheduler.generate_plan(st.session_state.owner)
    if plan:
        st.write("Today's Schedule:")
        for pet, task in plan:
            st.write(
                f"{task.start_time or '—'} — {task.name} ({task.duration} min) "
                f"[priority: {task.priority}] — {pet.get_name()}"
            )
    else:
        st.info("No tasks fit in the available time. Add tasks above and try again.")
