class Queue:
    def __init__(self):
        self.queue=[]
    def is_size(self):
        return len(self.queue)
    def is_empty(self):
        return len(self.queue)==0
    def push(self,item):
        self.queue.append(item)
    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return "queue is empty"
    def display(self):
        for item in self.queue:
            print("The elemnet is :",item)
    
    def searchElement(self,item):
        if not self.is_empty():
            return item in self.queue
        return "queue is empty"


daily_tak2=Queue()
print("The size of the queue:",daily_tak2.is_size())
print("Is queue Empty :",daily_tak2.is_empty())
print("Adding an element 90")
daily_tak2.push(90)
print("Adding an element 78:")
daily_tak2.push(78)
print("Adding an element 67")
daily_tak2.push(67)
print(daily_tak2.pop())
print(daily_tak2.peek())
daily_tak2.display()
print("Search the element 78:",daily_tak2.searchElement(78))
