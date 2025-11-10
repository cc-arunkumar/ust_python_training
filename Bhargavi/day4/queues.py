# Queue Operations
class Queue:
    def __init__(self):
        self.queue = []
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self , item):
        self.queue.append(item)

    def dequeue(self,item):
        if not self.is_empty():
           return self.queue.pop(0)
        else:
            print("Queue is empty")

    def peek(self , iteam):
        if not self.is_empty():
            return self.queue.peek[0]
        else:
            print("Queue is empty")

    def display(self):
       print (self.queue)

    def search(self , item):
        if not self.is_empty():
            for x in self.queue:
                if x == item:
                    return True 
                else:
                    return False
q = Queue()

q.enqueue(123)
q.enqueue(345)
q.enqueue(6)
q.enqueue(7)

print("The size of element" ,q.size())
print("Is the queue is empty :" ,q.is_empty())
print("The serached element is :", q.search(34))

print("The queue is :")
q.display()

# The size of element 4
# Is the queue is empty : False
# The serached element is : False
# The queue is :
# [123, 345, 6, 7]

        
