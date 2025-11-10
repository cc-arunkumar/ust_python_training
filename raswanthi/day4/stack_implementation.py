class Stack:
    def __init__(self):
        self.stack = []

    def push(self, stack):
        self.stack.append(stack)
        print(f"Added {stack}")

    def pop(self):
        if not self.is_empty():
            removed = self.stack.pop()
            print(f"Removed {removed}")
            return removed
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
    def search(self, item):
        if item in self.stack:
            index = self.stack.index(item)
            print("Element Found")
            return index
        else:
            print("Element not found")
            return -1

    
stack=Stack()
print("Is stack empty?", stack.is_empty())

stack.push(10)
stack.push(20)
stack.search(30)
stack.search(10)
print("Size of stack:", stack.size())
print("Is stack empty?", stack.is_empty())

