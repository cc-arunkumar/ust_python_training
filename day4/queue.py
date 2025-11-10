#queue

class Queue:
    def __init__(self):
        self.queue = []
   
    def enqueue(self, element):
        self.queue.append(element)
 
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
 
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
 
    def isEmpty(self):
        return len(self.queue) == 0
 
    def size(self):
        return len(self.queue)
 
    def search(self, element):
        for i in range(len(self.queue)):
            if self.queue[i] == element:
                return f"Element '{element}' found at position {i}"  # 0-based index
        return f"Element '{element}' not found in the queue"


# Example usage
myQueue = Queue()

myQueue.enqueue('varsha')
myQueue.enqueue('yashu')
myQueue.enqueue('vinutha')

print("queue:", myQueue.queue)
print("peek:", myQueue.peek())
print("dequeue:", myQueue.dequeue())
print("queue after dequeue:", myQueue.queue)
print("isempty:", myQueue.isEmpty())
print("size:", myQueue.size())


element_to_search = "yashu"   
print(myQueue.search(element_to_search))

#output
# queue: ['varsha', 'yashu', 'vinutha']
# peek: varsha
# dequeue: varsha
# queue after dequeue: ['yashu', 'vinutha']
# isempty: False
# size: 2
# Element 'yashu' found at position 0