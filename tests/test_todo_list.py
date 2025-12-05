from lib.todo_list import *
import pytest

"""
Creating an instance of the class
Creates an empty dictionary
"""
def test_creating_instance_of_class_creates_empty_dict():
    mitch = Create_To_Do()
    actual = mitch.all_tasks
    expected = {}
    assert actual == expected

"""
Adding a task using add_task and using show_tasks
Returns a list of tasks
"""
def test_adding_two_tasks_and_showing_returns_tasks():
    mitch = Create_To_Do()
    mitch.add_task("Walk the dog")
    mitch.add_task("Wash the dishes")
    actual = mitch.show_tasks()
    expected = ["Walk the dog", "Wash the dishes"]
    assert actual == expected

"""
Marking a task as completed and using show_tasks
Returns a list of tasks excluding any marked as completed
"""
def test_completed_tasks_not_showing_in_show_tasks():
    mitch = Create_To_Do()
    mitch.add_task("Walk the dog")
    mitch.add_task("Wash the dishes")
    mitch.complete_task("Walk the dog")
    actual = mitch.show_tasks()
    expected = ["Wash the dishes"]
    assert actual == expected

def test_adding_completed_task_updates_task_to_not_started():
    mitch = Create_To_Do()
    mitch.add_task("Walk the dog")
    mitch.add_task("Wash the dishes")
    mitch.add_task("Vacuum the floor")
    mitch.complete_task("Walk the dog")
    mitch.complete_task("Vacuum the floor")
    mitch.add_task("Walk the dog")
    actual = mitch.show_tasks()
    expected = ["Walk the dog", "Wash the dishes"]
    assert actual == expected

"""
Calling show_tasks when empty
Returns an empty list
"""
def test_calling_empty_show_tasks_returns_empty_list():
    mitch = Create_To_Do()
    actual = mitch.show_tasks()
    expected = []
    assert actual == expected

"""
Completing a task that hasn't been added
Adds it to the list and prints a message to the user
"""
def test_completing_task_not_in_list_adds_completed_task_prints_msg(capsys):
    mitch = Create_To_Do()
    mitch.complete_task("Vacuum the floor")
    actual = capsys.readouterr()
    expected = "Vacuum the floor was not an existing task. It has been added as a completed task\n"
    assert actual.out == expected
    actual_two = mitch.show_tasks()
    expected_two = []
    assert actual_two == expected_two






