class Stack:
    def __init__(self):
        self.stack=[]
        
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return True if len(self.stack)==0 else False
    
    def push(self,value):
        print("Adding element: ",value)
        self.stack.append(value)
        print("Length of stack: ",daily_task.size())
        
    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            return self.stack[-1]
        
    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
        else :
            rem_val=self.stack.pop()
            print("Removing element: ",rem_val)
            print("Length of stack: ",daily_task.size())
            
    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            return self.stack
        
daily_task=Stack()
print("Is stack empty: ",daily_task.is_empty())
daily_task.push(10)
daily_task.push(20)
daily_task.push(30)
daily_task.push(40)
daily_task.push(50)
print("Is stack empty: ",daily_task.is_empty())
print("Peek element: ",daily_task.peek())
print(daily_task.display())
daily_task.pop()
daily_task.pop()
daily_task.pop()
daily_task.pop()
daily_task.pop()
print("Is stack empty: ",daily_task.is_empty())

# Is stack empty:  True
# Adding element:  10
# Length of stack:  1
# Adding element:  20
# Length of stack:  2
# Adding element:  30
# Length of stack:  3
# Adding element:  40
# Length of stack:  4
# Adding element:  50
# Length of stack:  5
# Is stack empty:  False
# Peek element:  50
# [10, 20, 30, 40, 50]
# Removing element:  50
# Length of stack:  4
# Removing element:  40
# Length of stack:  3
# Removing element:  30
# Length of stack:  2
# Removing element:  20
# Length of stack:  1
# Removing element:  10
# Length of stack:  0
# Is stack empty:  True