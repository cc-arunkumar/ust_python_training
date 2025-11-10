class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item}")

    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            return removed
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0


    def search(self, item):
        if item in self.queue:
            index = self.queue.index(item)
            print("Element Found")
            return index
        else:
            print("Element not found")
            return -1

queue = Queue()
print("Is queue empty?", queue.is_empty())

queue.enqueue(10)
queue.enqueue(20)
queue.search(30)
queue.search(10)
print(queue.is_empty())
print(queue.peek())
queue.dequeue()

