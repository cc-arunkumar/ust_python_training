# stack

class stack:
    def __init__(self):
        self.stack=[]
        
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack)==0
    
    def push(self, item):
        self.stack.append(item)
        print("Adding element=",item)
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            
            
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty, can't pop")
    
    
    def search(self, item):
        if not self.is_empty():
            if item in self.stack:
                return True
            else:
                return False
        else:
            print("stack is empty")
            return False
daily_task=stack()

print("Is stack empty= ",daily_task.is_empty())
print("Length of stack = ",daily_task.size())
daily_task.push(10)
print("Search an element 10 is there or not=",daily_task.search(10))
print("Length of stack = ",daily_task.size())
daily_task.push(20)
print("Length of stack = ",daily_task.size())
daily_task.push(30)
print("Length of stack = ",daily_task.size())
print("Removing the element=",daily_task.pop())
print("Length of stack = ",daily_task.size())
print("Removing the element=",daily_task.pop())
print("Length of stack = ",daily_task.size())
print("Removing the element=",daily_task.pop())
print("Length of stack = ",daily_task.size())
print("Searching for 200 : ",daily_task.search(200))

# Sample output

# Is stack empty=  True

# Length of stack =  0

# Adding element= 10  

# Search an element 10 is there or not= True

# Length of stack =  1

# Adding element= 20

# Length of stack =  2

# Adding element= 30

# Length of stack =  3

# Removing the element= 30

# Length of stack =  2

# Removing the element= 20

# Length of stack =  1

# Removing the element= 10

# Length of stack =  0

# stack is empty

# Searching for 200 :  False