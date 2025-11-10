class Queue:
    def __init__(self):
        self.queue = []
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
        
    def push(self,val):
        self.queue.append(val)
        print(f"number pushed is {val}")
    
    def peek(self):
        if not self.isEmpty():
            # return self.queue[0]
            print(f"peek element is {self.queue[0]}")
        else:
            print("queue is empty")
    
    def pop(self):
        print(f"deleted element is {self.queue[0]}")
        del self.queue[0]
    
    def printtheFunction(self):
        val = self.size()
        for i in range(val):
            print(self.queue[i])
    

    def find_element(self, val):
        if not self.isEmpty():
            for i in range(self.size()):
                if self.queue[i] == val:
                    print("Element found at index", i)
                    return i
            print("Element not found")
            return -1
        else:
            print("Queue is empty")
            return -1

            
         
    
        
newQueue = Queue()
newQueue.push(20)
newQueue.push(30)
newQueue.push(40)
newQueue.push(50)
newQueue.push(60)
newQueue.push(70)
newQueue.size()
newQueue.pop()
newQueue.peek()
newQueue.printtheFunction()
# print(newQueue)'
print(newQueue.find_element(50))