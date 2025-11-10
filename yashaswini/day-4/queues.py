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
        return f"Element '{element}' found at position {i}"
    return f"Element '{element}' not found in the queue"

myQueue = Queue()

myQueue.enqueue('virat')
myQueue.enqueue('messi')
myQueue.enqueue('arjun')

print("Queue:", myQueue.queue)
print("Peek:", myQueue.peek())
print("Dequeue:", myQueue.dequeue())
print("Queue after Dequeue:", myQueue.queue)
print("isEmpty:", myQueue.isEmpty())
print("Size:", myQueue.size())
element_to_search = input("Enter an element to search in the queue: ")
print(myQueue.search(element_to_search))


#o/p:
# Queue: ['virat', 'messi', 'arjun']
# Peek: virat
# Dequeue: virat
# Queue after Dequeue: ['messi', 'arjun']
# isEmpty: False
# Size: 2
# Enter an element to search in the queue: arjun
# Element 'arjun' found at position 1