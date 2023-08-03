from lib.todo_list import *
from lib.todo import *

''''
Given I add 2 todo tasks,
I can see them added into the incomplete todo list
'''

def test_adds_multiple_instances_and_lists_them():
    todo_list = TodoList()
    task_1 = Todo("1. Make the bed!")
    task_2 = Todo("2. Feed the birds!")
    todo_list.add(task_1)
    todo_list.add(task_2)
    assert todo_list.incomplete() == [task_1, task_2]

''''
Given I add 2 todo tasks,
and call #mark_complete 
I can see them added into the incomplete todo list
'''