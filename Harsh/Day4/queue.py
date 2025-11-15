class Queue:
    #constructor
    def __init__(self):
        self.queue=[]
    
    #method to get size of queue
    def size(self):
        print("length of queue: ", len(self.queue))
        
    #method to check if queue is empty
    def is_empty(self):
        return len(self.queue)==0
    
    #method to add item to queue
    def push(self,item):
        self.queue.append(item)
        print ("Adding item:",item)
        q1.size()
    
    #method to remove item from queue
    def pop(self):
        if not self.is_empty():
            remove=self.queue.pop(0)
            print("Removing element:",remove)
            q1.size()
        else:
            print("isempty")
    
    #method to view front item of queue
    def peek(self):
        if not self.is_empty():
            print(self.queue[0])
        else:
            print("queue empty") 
    
    #method to search item in queue
    def search(self,item):
        if not self.is_empty():
            if item in self.queue:
                print( item ,"found in queue")
            else:
                print(item, " not found in queue")
        else:
            print("queue is empty")
    
    #method to traverse the queue
    def traverse(self):
        for items in self.queue:
            print(items)

q1=Queue()
print("Is queue empty?:",q1.is_empty())
q1.size()
q1.push(10)
q1.push(20)
q1.push(30)
q1.traverse()
q1.search(10)
q1.pop()
q1.pop()
q1.search(20)
print("Is queue empty?:",q1.is_empty())


# Is queue empty?: True
# length of queue:  0      
# Adding item: 10
# length of queue:  1      
# Adding item: 20
# length of queue:  2      
# Adding item: 30
# length of queue:  3      
# 10 found in queue        
# Removing element: 10     
# length of queue:  2      
# Removing element: 20     
# length of queue:  1      
# 20  not found in queue   
# Is queue empty?: False 
