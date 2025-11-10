class Queue:
    
    def __init__(self):
        self.queue=[]
    
    def is_empty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    
    def enqueue(self,item):
        self.queue.append(item)
        
    def peek(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            print("Queue is empty")
    
    def dequeue(self,item):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
    
    def search(self, item):
        if not self.is_empty():
            if item in self.queue:
                return True
            else:
                return False
        else:
            print("queue is empty")
            return False
            
        
    