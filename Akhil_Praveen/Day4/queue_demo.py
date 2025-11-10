class Queue:
    def __init__(self):
        self.queue=[]
        
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return True if len(self.queue)==0 else False
    
    def push(self,value):
        print("Adding element: ",value)
        self.queue.append(value)
        print("Length of queue: ",daily_task.size())
        
    def peek(self):
        if self.is_empty():
            print("queue is empty!")
        else:
            return self.queue[-1]
        
    def pop(self):
        if self.is_empty():
            print("queue is empty!")
        else :
            rem_val=self.queue.pop(0)
            print("Removing element: ",rem_val)
            print("Length of queue: ",daily_task.size())
            
    def display(self):
        if self.is_empty():
            print("queue is empty!")
        else:
            return self.queue
    
    def search(self,item):
        if not self.is_empty():
            for i in self.queue:
                if i==item:
                    return f"item {item} Found"
        return f"item {item} Not found"
        
daily_task=Queue()
print("Is queue empty: ",daily_task.is_empty())
daily_task.push(10)
daily_task.push(20)
daily_task.push(30)
daily_task.push(40)
daily_task.push(50)
print(daily_task.search(30))
print(daily_task.search(60))
print("Is queue empty: ",daily_task.is_empty())
print("Peek element: ",daily_task.peek())
print(daily_task.display())
daily_task.pop()
daily_task.pop()
daily_task.pop()
daily_task.pop()
daily_task.pop()
print("Is queue empty: ",daily_task.is_empty())


# Is queue empty:  True
# Adding element:  10
# Length of queue:  1
# Adding element:  20
# Length of queue:  2
# Adding element:  30
# Length of queue:  3
# Adding element:  40
# Length of queue:  4
# Adding element:  50
# Length of queue:  5
# Is queue empty:  False
# Peek element:  50
# [10, 20, 30, 40, 50]
# Removing element:  10
# Length of queue:  4
# Removing element:  20
# Length of queue:  3
# Removing element:  30
# Length of queue:  2
# Removing element:  40
# Length of queue:  1
# Removing element:  50
# Length of queue:  0
# Is queue empty:  True