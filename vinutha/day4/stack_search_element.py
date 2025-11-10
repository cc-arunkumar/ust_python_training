# searching an element in a stack

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
    
    def search(self, item):
        if item in self.stack:
            return "Found"
        else:
            return "Not Found"


stack = Stack()
print("Size:",stack.size())
print("Is Stack Empty:", stack.is_empty())
stack.push(10)
stack.push(20)
stack.push(30)
print("After adding element:", stack.stack)
print("Removed element:", stack.pop())
print("Seaching the element:",stack.search(20))
print("Seaching the element:",stack.search(40))

# #output
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/stack_search_element.py
# Size: 0
# Is Stack Empty: True
# After adding element: [10, 20, 30]
# Removed element: 30
# Seaching the element: Found
# Seaching the element: Not Found
# PS C:\Users\303379\day4_training> 