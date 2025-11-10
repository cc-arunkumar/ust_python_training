#queue
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, element):
        self.queue.append(element)
        print(f"Adding element: {element}")
        print(f"Length of queue = {self.size()}")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty, cannot dequeue.")
        else:
            removed = self.queue.pop(0)
            print(f"Removed element: {removed}")
            print(f"Current queue size = {self.size()}")

    def search(self, element):
        if element in self.queue:
            position = self.queue.index(element) + 1
            print(f"Element {element} found in queue at position {position} from front.")
        else:
            print(f"Element {element} not found in queue.")

q = Queue()

q.enqueue(5)
q.enqueue(15)
q.enqueue(25)

q.search(15)
q.search(100)

# sample output
# Adding element: 5
# Length of queue = 1
# Adding element: 15
# Length of queue = 2
# Adding element: 25
# Length of queue = 3
# Element 15 found in queue at position 2 from front.
# Element 100 not found in queue.
