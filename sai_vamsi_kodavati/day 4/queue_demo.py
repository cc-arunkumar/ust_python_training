class Queue:
    def __init__(self):
        self.queue = [10,20,30]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, item):
        self.queue.append(item)
        print("Enqueuing item:", item, "-> Enqueued Successfully")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"
    
    def search(self, item):
        if item in self.queue:
            pos = self.queue.index(item) + 1
            print(f"Item {item} found at position {pos} from front")
        else:
            print(f"Item {item} not found in queue")


daily_task = Queue()

print("Is queue empty?", daily_task.is_empty())
print("Size of queue:", daily_task.size())

daily_task.enqueue(10)
print("Front element:", daily_task.peek())

daily_task.enqueue(20)
print("Size of the queue:", daily_task.size())
print("Front element:", daily_task.peek())

print("Removing element:", daily_task.dequeue())
print("Size of the queue:", daily_task.size())

daily_task.enqueue(30)
print("Size of the queue:", daily_task.size())
print("Front element:", daily_task.peek())

print("Removing element:", daily_task.dequeue())
print("Size of the queue:", daily_task.size())

daily_task.search(20)

# ---------------------------------------------------------------------

# Sample Output

# Is queue empty? False
# Size of queue: 3
# Enqueuing item: 10 -> Enqueued Successfully
# Front element: 10
# Enqueuing item: 20 -> Enqueued Successfully
# Size of the queue: 5
# Front element: 10
# Removing element: 10
# Size of the queue: 4
# Enqueuing item: 30 -> Enqueued Successfully
# Size of the queue: 5
# Front element: 20
# Removing element: 20
# Size of the queue: 4
# Item 20 found at position 3 from front


