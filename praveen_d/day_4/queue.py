class Queue:

    def __init__(self):
        self.queue=[]
    
    def is_empty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    
    def enqueue(self,value):
        self.queue.append(value)
        print(f"Appended {value} successfully !")

    def dequeue(self):
        if not self.is_empty():
            print(f"Removed {self.queue[0]} sucessfully")
            return self.queue.pop(0)



queue_tasks=Queue()

print(queue_tasks.is_empty())

queue_tasks.enqueue(10)
queue_tasks.enqueue(20)
queue_tasks.enqueue(30)
queue_tasks.dequeue()
print(queue_tasks.queue)

# EXPECTED OUTPUT:
# True
# Appended 10 successfully !
# Appended 20 successfully !
# Appended 30 successfully !
# Removed 10 sucessfully
# [20, 30]

