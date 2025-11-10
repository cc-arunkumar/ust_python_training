class Stack:
    def __init__(self):
        self.stack=[]

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack)==0
    
    def push(self,value):
        self.stack.append(value)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def search(self,value):
        if not self.is_empty():
            for i in range(len(self.stack)):
                if self.stack[i]==value:
                    print(f"Value found at:{i}")


daily_task=Stack()

print(f"Is stack empty:{daily_task.is_empty()}")
print(f"Size of the stack:{daily_task.size()}")
daily_task.push(10)
print(f"Adding element:10")
daily_task.push(20)
print(f"Adding element:20")
daily_task.push(30)
print(f"Adding element:30")
print(daily_task.stack)
print(daily_task.size())
print(f"Removing element:{daily_task.pop()}")
print(daily_task.stack)
print(daily_task.is_empty())
daily_task.search(20)


# EXPECTED OUTPUT:
# Is stack empty:True
# Size of the stack:0
# Adding element:10
# Adding element:20
# Adding element:30
# [10, 20, 30]
# 3
# Removing element:30
# [10, 20]
# False
# Value found at:1