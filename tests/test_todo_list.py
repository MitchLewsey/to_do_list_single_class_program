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




