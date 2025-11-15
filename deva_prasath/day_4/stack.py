# Class representing a simple Stack
class stack:
    def __init__(self):
        self.a = []  # Initialize the stack as an empty list

    # Method to return the size of the stack
    def size(self):
        return len(self.a)
    
    # Method to check if the stack is empty
    def is_empty(self):
        if len(self.a) == 0:
            return True
        else:
            return False
        
    # Method to push an item onto the stack
    def push(self, item):
        self.a.append(item)

    # Method to get the top item of the stack without removing it
    def peek(self):
        if not self.is_empty():
            return self.a[-1]  # Return the last item (top of the stack)
        else:
            return "Stack is empty"
        
    # Method to pop an item from the stack (remove the top item)
    def pop(self):
        if not self.is_empty():
            self.a.remove(self.a[-1])  # Remove the top item (last item)

    # Method to search for an element in the stack
    def search(self, ele):
        if not self.is_empty():
            for i in self.a:
                if i == ele:
                    return i  # Return the element if found
                else:
                    return "Not present"  # Return "Not present" for other elements

# Create a stack object
obj = stack()

# Test the stack functionality
print("Is stack empty:", obj.is_empty())
print("Length of the stack:", obj.size())
obj.push(10)
print("Adding element:", obj.peek())
print("Length of the stack:", obj.size())
obj.push(20)
print("Adding element:", obj.peek())
print("Length of the stack:", obj.size())
obj.push(30)
print("Adding element:", obj.peek())
print("Length of the stack:", obj.size())
print("Removing element:", obj.peek())
popped = obj.pop()  # Pop the top element from the stack
print("Length of the stack:", obj.size())
print("Is stack empty:", obj.is_empty())
print("Is 30 present:", obj.search(30))  # Check if 30 is present in the stack

#Sample output
# Is stack empty: True
# Length of the stack: 0
# Adding element: 10
# Length of the stack: 1
# Adding element: 20
# Length of the stack: 2
# Adding element: 30
# Length of the stack: 3
# Removing element: 30
# Length of the stack: 2
# Is stack empty: False
# Is 20 present: Not present