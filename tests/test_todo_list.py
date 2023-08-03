from lib.todo_list import *

'''
Initially the todos list is empty.
'''

def test_initially_has_an_empty_list_of_todos():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

    