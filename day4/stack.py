

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "stack is not empty"




    
daily_tasks=Stack()
print(daily_tasks.size())
print("is stack empty:",daily_tasks.is_empty())
daily_tasks.push("task1. logging")
daily_tasks.push("task2. coding")
daily_tasks.push("task3. learning")
print("adding elements in stack:",daily_tasks.size())

print("Popping the last element:", daily_tasks.pop())
print("Size after popping:", daily_tasks.size())
print("peek of the stack:",daily_tasks.peek())
daily_tasks.push("task. working")
print("size after pushing:",daily_tasks.size())



# output
# 0
# is stack empty: True
# adding elements in stack: 3
# Popping the last element: task3. learning
# Size after popping: 2
# peek of the stack: task2. coding
# size after pushing: 3




