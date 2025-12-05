# To Do Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class create_to_do():

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Create all_tasks: dict
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self to_do_list
        pass # No code here yet

    def complete_task(self, task):
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Raise an exception if no task is set    
        pass # No code here yet

    def show_tasks(self):
        # Returns:
        #   A list of the tasks that are not completed
        # Side-effects:
        #   None
        pass # No code here yet



```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Creating an instance of the class
Creates an empty dictionary
"""
mitch = Create_To_Do
mitch.all_tasks() => {}

"""
Adding a task using add_task and using show_tasks
Returns a list of tasks
"""
mitch = Create_To_Do
mitch.add_task("Walk the dog")
mitch.add_task("Wash the dishes")
mitch.show_task() => ["Walk the dog", "Wash the dishes"]

"""
Marking a task as completed and using show_tasks
Returns a list of tasks excluding any marked as completed
"""
mitch = Create_To_Do
mitch.add_task("Walk the dog")
mitch.add_task("Wash the dishes")
mitch.complete_tasks("Walk the dog")
mitch.show_task() => ["Wash the dishes"]

"""
Adding a task that is already added and completed, updates the task to be "Not started" again.
"""
mitch = Create_To_Do
mitch.add_task("Walk the dog")
mitch.add_task("Wash the dishes")
mitch.complete_tasks("Walk the dog")
mitch.add_task("Walk the dog")
mitch.show_task() => ["Walk the dog", "Wash the dishes"]

"""
Calling show_tasks when empty
Returns an empty list
"""
mitch = Create_To_Do
mitch.show_tasks() => []

"""
Completing a task that hasn't been added
Adds it to the list and prints a message to the user
"""
mitch = Create_To_Do
mitch.complete_tasks("Walk the dog") => "Walk the dog was not an existing task. It has been added as a completed task"
mitch.show_tasks() => []


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
