from lib.todo import *

'''
If we give a complete task,
#mark_complete will return True.
'''

def test_returns_true_when_task_complete():
    todo = Todo("1. Make the bed!")
    assert todo.mark_complete() == True