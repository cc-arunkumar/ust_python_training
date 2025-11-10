#Queues
class Queue:
    def __init__(self):
        self.Queue=[]   
    def size(self):
        return len(self.Queue) 
    def is_empty(self):
        return  len(self.Queue)==0  
    def enqueue(self,item):   
        self.Queue.append(item)
        print("Adding element:",item)
    def peek(self):
        if not self.is_empty():
            return self.Queue,[-1]
        else:
            print("Queue is empty") 
    def dequeue(self):
        if not self.is_empty():
            return self.Queue.pop(0)
        else:
          print("Queue ia empty")
q=Queue()
print("stack size is ",q.size())
print("is stack is empty",q.is_empty())
q.enqueue(30)
q.enqueue("maga")
print("Queue is",q.peek())
print("Dequeue the element",q.dequeue())
print("Queue after dequeue:",q.Queue)
# sample output
# stack size is  0
# is stack is empty True
# Adding element: 30
# Adding element: maga
# Queue is ([30, 'maga'], [-1])
# Dequeue the element 30
# Queue after dequeue: ['maga']