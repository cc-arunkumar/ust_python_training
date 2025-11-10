# stack

class Stack:
    def __init__(self):
        self.stack = []
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        # print("Is stack empty: ",end="")
        return False if self.stack else True
    
    def peek(self):
        if not self.is_empty():
            # print("Element at the top: ",end="")
            return self.stack[-1]
        else:
            print("Stack is empty")
    
    def pop(self):
        if not self.is_empty():
            # print("Element poped: ",end="")
            return self.stack.pop()
        else:
            print("Stack is empty")
    
    def push(self,item):
        print("Adding Element: ",item)
        self.stack.append(item)
        
    def search(self,item):
        if not self.is_empty():
            if item in self.stack:
                print(f"{item} is present in stack")
            else:
                print(f"{item} is not in stack")
    
p = Stack()
p.push(1)
p.push(2)
p.push(3)
p.push(4)
print(f"Size of stack: {p.size()}")
print(f"Is stack empty: {p.is_empty()}")
print(f"poped: {p.pop()}")
print(f"Element at the top: {p.peek()}")
p.search(2)
p.search(4)

# output

# Adding Element:  1   
# Adding Element:  2   
# Adding Element:  3   
# Adding Element:  4   
# Size of stack: 4     
# Is stack empty: False
# poped: 4
# Element at the top: 3
# 2 is present in stack
# 4 is not in stack