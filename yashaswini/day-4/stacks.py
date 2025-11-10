class Stack:
    def __init__(self):
        self.items = []
 
    def size(self):
        return len(self.items)
 
    def is_empty(self):
        return len(self.items) == 0
 
    def push(self, item):
        self.items.append(item)
 
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  
 
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Cannot pop from an empty stack")
 
    def search(self, item):
        if item in self.items:
            return "found"
        else:
            return "Not found"
 
stack = Stack()
print("Size:", stack.size())
print("Is stack empty:", stack.is_empty())
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
print("Peek element:", stack.peek())
print("Search 30", stack.search(20))
print("Search 90:", stack.search(40))


#o/p:
# Size: 0
# Is stack empty: True
# Peek element: 20
# Search 30 found
# Search 90: Not found