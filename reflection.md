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
One tradeoff the scheduler makes it that it sorts generate_plan by priority, then packs greedily, even if it is not the most optimal for completing tasks effeciently.
- Why is that tradeoff reasonable for this scenario?
This is reasonable because high priority tasks should be completed first, even if multiple tasks could be packed at the same time.


---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used it to brainstorm, debug, and refactor. It helped make algorithmic and stylistic changes more effeciently.
- What kinds of prompts or questions were most helpful?
Longer prompts that made multiple changes at once were helpful because they eliminated the need for multiple short prompts which would probably take more time.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
The AI suggested some changes to the scheduler which didn't change much of the actual use of the function. 
- How did you evaluate or verify what the AI suggested?
I judged what the function currently did and what would've changed with the new suggestion that the AI thought of. The only main difference was really just a change in how the code looked, which had no difference if the function of the method didn't change. 

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested the sorting algorithms for tasks and task completion issues.
- Why were these tests important?
These tests were important because they handled edge cases and made sure that the pawpal program logic was working smoothly.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am pretty confident that the scheduler works correctly. 
- What edge cases would you test next if you had more time?
Maybe more specific edge cases like having multiple pets with same name, more deep scheduling conflicts, etc.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am satisfied with the UML diagram and the relationships created between. I am also satisfied with the logic behind scheduler app because I think it captures the major components of what is necessary for a good scheduler.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would probably make the app more intricate by adding more features like, edit task, remove task, etc. I'd also like to make the UI better and more user friendly.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
There are a lot more edge cases and design issues that you need to consider that I originally had thought. Planning and documenting the progress is very important for future changes.
