# Define a Stack class
class Stack:
    def __init__(self):
        # Initialize an empty list to hold stack elements
        self.stack = []

    # Return the number of elements in the stack
    def size(self):
        return len(self.stack)
    
    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Push an element onto the stack (top of stack)
    def push(self, element):
        self.stack.append(element)
    
    # Return the top element without removing it
    def peak(self):  # Note: the correct spelling is usually "peek"
        if not self.is_empty():
            return self.stack[-1]  # Last element is the top of stack
        else:
            print("Stack is empty")
    
    # Remove and return the top element
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
    
    # Search for an element in the stack
    def search(self, element):
        if self.is_empty():
            return "Stack is empty"
        # Corrected logic: your previous loop returned after the first iteration
        for i in self.stack:
            if i == element:
                return "Yes"
        return "No"


# Create a stack object
s = Stack()

# Check if stack is empty
if s.is_empty():
    print("The Stack is empty")

# Push elements
print("Adding element 10")
s.push(10)
print("The length of the stack is", s.size())

print("Adding element 20")
s.push(20)
print("The length of the stack:", s.size())

# Peek at the top element
print("Top element is:", s.peak())

# Pop the last element
print("Popping the last element:", s.pop())
print("Stack size after pop:", s.size())

# Search for an element
print("Is element 10 in stack?", s.search(10))


"""
SAMPLE OUTPUT

The Stack is empty
Adding element 10
The length of the stack is 1
Adding element 20
The length of the stack: 2
Top element is: 20
Popping the last element: 20
Stack size after pop: 1
Is element 10 in stack? Yes
"""