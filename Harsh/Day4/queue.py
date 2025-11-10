class Queue:
    def __init__(self):
        self.queue=[]
        
    def size(self):
        print("length of queue: ", len(self.queue))
        
    def is_empty(self):
        return len(self.queue)==0
    
    def push(self,item):
        self.queue.append(item)
        print ("Adding item:",item)
        q1.size()
    
    def pop(self):
        if not self.is_empty():
            remove=self.queue.pop(0)
            print("Removing element:",remove)
            q1.size()
        else:
            print("isempty")
            
    def peek(self):
        if not self.is_empty():
            print(self.queue[0])
        else:
            print("queue empty") 
            
    def search(self,item):
        if not self.is_empty():
            if item in self.queue:
                print( item ,"found in queue")
            else:
                print(item, " not found in queue")
        else:
            print("queue is empty")
        
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
