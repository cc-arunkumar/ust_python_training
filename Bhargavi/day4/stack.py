# Stack Operations using a class

# This program implements a Stack data structure using a Python class.
# It provides basic stack operations such as push (add element), pop (remove top element), peek (view top element), size, is_empty, display, and search.
# The stack follows the LIFO (Last-In-First-Out) principle, meaning the last element pushed is the first one removed.

class Stack:
    def __init__(self):
        self.stack = []   # initialize an empty list to represent the stack

    def size(self):
        return len(self.stack)   # return number of elements in the stack

    def is_empty(self):
        return len(self.stack) == 0   # check if stack is empty
    
    def push(self, item):
        self.stack.append(item)   # add item to the top of the stack

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]   # return top element without removing
        else:
            print("stack is empty")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()   # remove and return top element
        else:
            print("stack is empty")

    def display(self):
        print(self.stack)   # print the entire stack

    def search(self, item):
        if not self.is_empty():
            # check if item exists in stack
            return item in self.stack
        else: 
            print("Stack is empty")
            return False


# Testing the Stack
s = Stack()

print("Is_empty?", s.is_empty())   # check if stack is empty

# Push elements into the stack
s.push(10)
s.push(11)
s.push(100)
s.push(200)

# Pop removes the last pushed element (200)
print("Removed element from the stack:", s.pop())

# Peek shows the current top element (100)
print("Last element in the stack:", s.peek())

# Size shows number of elements left
print("The size of stack:", s.size())

# Display the stack contents
print("The stack is:")
s.display()

# Search for an element in the stack
print("The element is searched:", s.search(10))

# Expected Output:
# Is_empty? True
# Removed element from the stack: 200
# Last element in the stack: 100
# The size of stack: 3
# The stack is:
# [10, 11, 100]
# The element is searched: True
