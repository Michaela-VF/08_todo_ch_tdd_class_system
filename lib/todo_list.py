# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._todos = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self._todos.append(todo)
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos 
        # that are not complete
        return [i for i in self._todos if not i.complete]
        #return self._todos #just to make the test pass!

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos 
        # that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


'''
todo_list = TodoList()
print(todo_list.add("1. Make the bed!"))'''