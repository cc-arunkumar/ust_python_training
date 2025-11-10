class Queue:
    def __init__(self):
        self.queue=[]
        
    def size(self):
        length = len(self.queue)
        print("Length of queue is:",length)
        
    def is_empty(self):
        empty = len(self.queue)==0
        print("Queue is empty:",empty)
        
    def push(self,item):
        self.queue.append(item)
        print ("Item pushed in Queue",item)
        s1.size()
        
    def peek(self):
        if not self.is_empty():
           print("top item:",self.queue[0])
        else:
            print("Queue is empty")
            
    def pop(self):
        if not self.is_empty():
            remove=self.queue.pop(0)
            print("item removed",remove)
        else:
            print("Queue is empty") 
        
    
s1 =Queue()
s1.size()
s1.is_empty()
s1.push(10)
s1.push(20)
s1.push(30)
s1.pop()
s1.size()
s1.peek()
s1.pop()
s1.size()
s1.is_empty()