class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def push(self, element):
        self.queue.append(element)
    
    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")

q = Queue()

if q.is_empty():
    print("The Queue is empty")

print("Adding element 10")
q.push(10)
print("The length of the queue is", q.size())

print("Adding element 20")
q.push(20)
print("The length of the queue:", q.size())

print("Front element is:", q.peek())

print("Popping element:", q.pop())
print("Queue size after pop:", q.size())
