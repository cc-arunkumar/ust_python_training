class Queue:
    def __init__(self):
        self.queue1 = []  

    def size(self):
        return len(self.queue1)

    def is_empty(self):
        return len(self.queue1) == 0
    
    def enqueue(self, item):
        self.queue1.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue1.pop(0)
        else:
            return "Queue is Empty!"
    
    def top(self):
        if not self.is_empty():
            return self.queue1[0]
        else:
            return "Queue is Empty"   
    def search(self, element):
        if not self.is_empty():
            for i in range(len(self.queue1)):  
                if self.queue1[i] == element:   
                    return "It Contains The Element"
            return "Element Not Present"       
        else:
            return "Queue is empty"

queue = Queue()
print("Is Queue Empty : ",queue.is_empty()) 
print("Length of Queue : ",queue.size())
print("Adding Element : 10")
queue.enqueue(10)
print("Length of Queue : ",queue.size())
print("Adding Element : 30")
queue.enqueue(30)
print("Length of Queue : ",queue.size())
print("Removing Element : 30")
print("Adding Element : 20")
queue.enqueue(20)
print("Adding Element : 40")
queue.enqueue(40)
print("IS 40 Present : ", queue.search(40))
print("Removed Element ", queue.dequeue())
print("Length of Queue : ",queue.size())
print("Element On Top : ", queue.top())
print("Is Queue Empty : ", queue.is_empty())
queue.dequeue()
print("After Popping the final Element : ", queue.top())


#Sample Output:
# Is Queue Empty :  True
# Length of Queue :  0
# Adding Element : 10
# Length of Queue :  1
# Adding Element : 30
# Length of Queue :  2
# Removing Element : 30
# Adding Element : 20
# Adding Element : 40
# IS 40 Present :  It Contains The Element
# Removed Element  10
# Length of Queue :  3
# Element On Top :  30
# Is Queue Empty :  False
# After Popping the final Element :  20
