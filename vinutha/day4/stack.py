#stack Implementation

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
            return self.stack[-1]  # Last element is the top
        else:
            return "Stack is empty"

    def pop(self):
        # Remove and return the top element of the stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"


# Create a Stack object
stack = Stack()

# Initially, stack is empty
print("Size:", stack.size())              # Output: 0
print("Is Stack Empty:", stack.is_empty()) # Output: True

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
print("After adding element:", stack.stack)  # Output: [10, 20, 30]

# Pop → removes the top element (30)
print("Removed element:", stack.pop())       # Output: 30

# Push another element (40)
stack.push(40)
print("After adding element:", stack.stack)  # Output: [10, 20, 40]

# Pop again → removes the top element (40)
print("Removed element:", stack.pop())       # Output: 40



# sample output
# Size: 0
# Is Stack Empty: True
# After adding element: [10, 20, 30]
# Removed element: 30
# After adding element: [10, 20, 40]
# Removed element: 40
    

