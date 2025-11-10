# queue

class Queue:
    def __init__(self):
        self.queue = []
        
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return False if self.queue else True
    
    def peek(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            print("queue is empty")
    
    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("queue is empty")
    
    def push(self,item):
        print("Adding Element: ",item)
        self.queue.append(item)
        
p = Queue()
p.push(1)
p.push(2)
p.push(3)
p.push(4)
print(f"Size of queue: {p.size()}")
print(f"Is queue empty: {p.is_empty()}")
print(f"poped: {p.pop()}")
print(f"Element at the top: {p.peek()}")


# output

# Adding Element:  1
# Adding Element:  2
# Adding Element:  3
# Adding Element:  4
# Size of queue: 4
# Is queue empty: False
# poped: 1
# Element at the top: 4