# searching an element in a stack

# Define a Stack class
class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.stack = []

    def size(self):
        # Return the number of elements in the stack
        return len(self.stack)

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def push(self, item):
        # Add an item to the top of the stack
        self.stack.append(item)

    def peek(self):
        # Return the top element without removing it
        if not self.is_empty():
            return self.stack[-1]  # Last element is the top of the stack
        else:
            return "Stack is empty"

    def pop(self):
        # Remove and return the top element of the stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    
    def search(self, item):
        # Search for an item in the stack
        if item in self.stack:
            return "Found"
        else:
            return "Not Found"


# Create a Stack object
stack = Stack()

# Initially, stack is empty
print("Size:", stack.size())             # Output: 0
print("Is Stack Empty:", stack.is_empty()) # Output: True

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

print("After adding element:", stack.stack)  # Output: [10, 20, 30]

# Pop → removes the top element (30)
print("Removed element:", stack.pop())       # Output: 30

# Search for an element that exists
print("Seaching the element:", stack.search(20))  # Output: Found

# Search for an element that does not exist
print("Seaching the element:", stack.search(40))  # Output: Not Found


# #output
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/stack_search_element.py
# Size: 0
# Is Stack Empty: True
# After adding element: [10, 20, 30]
# Removed element: 30
# Seaching the element: Found
# Seaching the element: Not Found
# PS C:\Users\303379\day4_training> 