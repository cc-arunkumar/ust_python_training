#stacks

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack) == 0
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self,item):
        self.stack.append(item)
        print("Adding element=",item)

    def peek(self):
        if not self.is_empty():
           return self.stack[-1]
        else:
            print("stack is empty")
    def pop(self):
        if not self.is_empty():
            popped_item = self.stack.pop()
            return popped_item
        else:
            print("Stack is empty")
        

 
s = Stack()

print("length of stack",s.size())
print("is stack is empty",s.is_empty())
s.push(25)
s.push(30)
print("stack is",s.peek())
print("pop the element",s.pop())
# sample output
# length of stack True
# is stack is empty True
# Adding element= 25
# Adding element= 30
# stack is 30
# pop the element 30