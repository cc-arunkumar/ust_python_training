# push()
# pop()
# peek()
# is_empty()
# size()


class Stack:
    def __init__(self):
        self.stack = [10,20,30]

    def is_empty(self):
        return len(self.stack) == 0 

    def size(self):
        return len(self.stack)   
    
    def push(self, item):
        self.stack.append(item)
        print("Pushing item:",item,"->Pushed Successfully")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    

    def search(self, item):
        if not self.is_empty() and item in self.stack:
            l = len(self.stack) - self.stack[::-1].index(item)
            print(f"Item {item} found at position {l} from bottom")
        else:
            print(f"Item {item} not found")



daily_task = Stack()

print("Is stack empty?",daily_task.is_empty())  
print("Size of stack:",daily_task.size())      

daily_task.push(10)


print("Top element:",daily_task.peek())  
daily_task.push(20)    
print("Size of the stack:",daily_task.size())
     
print("Top Element:",daily_task.peek()) 
print("Removing element:",daily_task.pop())       
print("Size of the stack:",daily_task.size()) 
daily_task.push(30)
print("Size of the stack:",daily_task.size())
     
print("Top Element:",daily_task.peek()) 
print("Removing element:",daily_task.pop())       
print("Size of the stack:",daily_task.size()) 

daily_task.search(20)

# ------------------------------------------------------------------

# Sample Output

# Is stack empty? False
# Size of stack: 3
# Pushing item: 10 ->Pushed Successfully
# Top element: 10
# Pushing item: 20 ->Pushed Successfully
# Size of the stack: 5
# Top Element: 20
# Removing element: 20
# Size of the stack: 4
# Pushing item: 30 ->Pushed Successfully
# Size of the stack: 5
# Top Element: 30
# Removing element: 30
# Size of the stack: 4
# Item 20 found at position 2 from bottom

    
