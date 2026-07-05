# PawPal+ Project Reflection

## 1. System Design

- 3 core actions a user should be able to perform using this app. 
1. Add and customize user and pet info
2. Generate a unique daily schedule based on constraints/priorities
3. Display the plan in a simple and understandable way

# Brainstorming - Objects/attributes for the class: Pet (color, type, hunger, name), 
# Owner (name, age, gender), Schedule (task, business), etc
# Methods for those classes: getName, addFood, addTask, getPlan, etc

**a. Initial design**

- Briefly describe your initial UML design.
It includes all 4 main classes with attributes and methods that will be useful for the app.
- What classes did you include, and what responsibilities did you assign to each?
Owner, Pet, Task, Scheduler. Owner will have methods to add Pets and getter methods for Owner like name. Pet will have attributes to make it unique and methods like addFood or addTask. Task will have have attributes like duration and priority and methods like markComplete to assist with the Scheduler class. Scheduler will allow users to generate schedules according to what Tasks they have and their other constraints such as time.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
Yes, I made a few small changes after reviewing my first skeleton. I added a preferences attribute to Owner since the README said the scheduler should consider owner preferences, but I hadn't included that anywhere yet. I also added a start_time attribute to Task so I can later check if tasks overlap, since duration alone wasn't enough to detect scheduling conflicts. I made generate_plan in Scheduler actually set self.plan instead of just returning a list, so get_plan won't return old or empty data after a new plan is made. Lastly, I renamed Scheduler's add_task method to schedule_task, since Pet already had its own add_task method and having two methods with the same name but different purposes was confusing.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
