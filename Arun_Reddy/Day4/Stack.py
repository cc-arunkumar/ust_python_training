class Stack:
    def __init__(self):
        self.stack=[]
        
    def sizes(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self,item):
        self.stack.append(item)
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is Empty"
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def display(self):
        for item in self.stack:
            print("The element is",item)


daily_task = Stack()
print("Size = ", daily_task.sizes())
print("Is Stack is Empty:",daily_task.is_empty())
print("Adding an element 90")
daily_task.push(90)
print("Adding an element 80")
daily_task.push(80)
print("Adding an element 45")
daily_task.push(45)
print("Adding an element 50")
daily_task.push(50)
print("stacks top element :",daily_task.peek())
print("Removing the top element:")
print(daily_task.pop())
print("Displaying the elements:")
daily_task.display()