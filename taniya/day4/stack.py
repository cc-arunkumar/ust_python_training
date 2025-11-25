# Stack implementation using a Python list
class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.stack = []
        
    def size(self):
        # Print the current size of the stack
        length = len(self.stack)
        print("Length of stack is:", length)
        
    def is_empty(self):
        # Check if the stack is empty
        empty = len(self.stack) == 0
        print("Stack is empty:", empty)
        return empty   # return value added for peek/pop usage
        
    def push(self, item):
        # Add item to the top of the stack
        self.stack.append(item)
        print("Item pushed in stack", item)
        s1.size()   # show size after push
        
    def peek(self):
        # Show the top item without removing it
        if not self.is_empty():
            print("Top item:", self.stack[-1])
        else:
            print("Stack is empty")
            
    def pop(self):
        # Remove and return the top item
        if not self.is_empty():
            remove = self.stack.pop()
            print("Item removed", remove)
        else:
            print("Stack is empty") 
        
# ------------------ Testing the Stack ------------------
s1 = Stack()
s1.size()        # Initially empty
s1.is_empty()    # Check empty status
s1.push(10)      # Push 10
s1.push(20)      # Push 20
s1.push(30)      # Push 30
s1.pop()         # Remove top (30)
s1.size()        # Size after pop
s1.peek()        # Show top item
s1.pop()         # Remove top (20)
s1.size()        # Size after pop
s1.is_empty()    # Check empty status