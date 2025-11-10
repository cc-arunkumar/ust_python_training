class Queue:
    def __init__(self):
        self.queue=[]
        
    def size(self):
        return len(self.queue)  #length of queue
    
    def is_empty(self):
        return len(self.queue)==0    #check if queue is empty
    
    def push(self,item):
        self.queue.append(item)      #add to queue
        print("Adding Element: ",item)
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]        #find first element
        else:
            print("queue is empty")
    
    def pop(self):
        if not self.is_empty():
            self.queue.remove(self.queue[0])    #remove first element
        else:
            print("queue is empty")
    
    def element_search(self,elem):
        if not self.is_empty():
            for i in self.queue:
                if i == elem:
                    return True
        else:
            print("Queue is empty")
    
obj = Queue()

print("Is the queue empty: ",obj.is_empty())
print("Length of queue: ",obj.size())
obj.push(10)
print("Length of queue: ",obj.size())
obj.push(20)
print("Length of queue: ",obj.size())
obj.push(30)
obj.push(40)
obj.push(50)
print("Length of queue: ",obj.size())
print("Removing element: ",obj.peek())
obj.pop()
print("Length of queue: ",obj.size())
print("Is the queue empty: ",obj.is_empty())
print("Item search: ",obj.element_search(50))


#Sample Execution
# Is the queue empty:  True
# Length of queue:  0
# Adding Element:  10
# Length of queue:  1
# Adding Element:  20
# Length of queue:  2
# Adding Element:  30
# Adding Element:  40
# Adding Element:  50
# Length of queue:  5
# Removing element:  10
# Length of queue:  4
# Is the queue empty:  False
# Item search:  True
