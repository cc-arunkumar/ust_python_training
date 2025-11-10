# Task: Stack Implementation using Class
# Scenario:
# Implement a Stack with push, pop, peek, size, is_empty, and search functionalities.

class Stack:
    def __init__(self):
        self.items = []  # Initialize an empty stack

    def size(self):
        return len(self.items)  # Return stack size

    def is_empty(self):
        return len(self.items) == 0  # Check if stack is empty

    def push(self, item):
        self.items.append(item)  # Push element onto the stack

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Return top element
        else:
            return None  # If stack is empty

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return top element
        else:
            print("Cannot pop from an empty stack")

    def search(self, item):
        if item in self.items:
            return "found"
        else:
            return "Not found"


# Example Usage
stack = Stack()
print("Size:", stack.size())
print("Is stack empty:", stack.is_empty())

stack.push(10)
stack.push(20)
stack.push(30)

stack.pop()

print("Peek element:", stack.peek())
print("Search 20:", stack.search(20))
print("Search 40:", stack.search(40))


# Sample Output:
# Size: 0
# Is stack empty: True
# Peek element: 20
# Search 20: found
# Search 40: Not found
