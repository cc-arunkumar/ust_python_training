#stack Implementation

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

stack = Stack()
print("Size:",stack.size())
print("Is Stack Empty:", stack.is_empty())
stack.push(10)
stack.push(20)
stack.push(30)
print("After adding element:", stack.stack)
print("Removed element:", stack.pop())
stack.push(40)
print("After adding element:", stack.stack)
print("Removed element:", stack.pop())


# sample output
# Size: 0
# Is Stack Empty: True
# After adding element: [10, 20, 30]
# Removed element: 30
# After adding element: [10, 20, 40]
# Removed element: 40
    

