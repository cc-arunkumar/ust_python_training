class Stack:
    def __init__(self):
        self.stack=[]

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack)==0 
    
    def push(self,item):
        self.stack.append(item)

    def push_multiple(self,items):
        for item in items:
            self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

daily_tasks=[1,2,3,4,5]
def stats(stk):
    # print("stack:",stk.stack)
    print("size of stack:",stk.size())
    print("If stack is_empty:",stk.is_empty())   

daily_tasks=Stack()
daily_tasks.push("Task 1")
daily_tasks.push("Task 2")
stats(daily_tasks)
daily_tasks.push_multiple(["Task 3","Task 4","Task 5"])
stats(daily_tasks)
print 
print("Popping tasks:",daily_tasks.pop())
stats(daily_tasks)
print("Popping tasks:",daily_tasks.pop())
stats(daily_tasks)

# size of stack: 2
# If stack is_empty: False
# size of stack: 5
# If stack is_empty: False
# Popping tasks: Task 5
# size of stack: 4
# If stack is_empty: False
# Popping tasks: Task 4
# size of stack: 3
# If stack is_empty: False