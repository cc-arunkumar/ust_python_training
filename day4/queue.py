class queue:
    def __init__(self):
        self.queue=[]
    
    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

        
    def search(self,item):
        if item in self.queue:
            index_item=self.queue.index(item)
            return (f"{item}{index_item}")
        else:
            return ("item is not found")
        

q = queue()
print("size of queue:",q.size())
q.enqueue("apple")
q.enqueue("banana")
q.enqueue("cherry")
print("queue after push:",q.size())
print("queue before search pop:", q.queue)

print(q.search("banana"))  
print("queue after search pop:", q.queue)
print("pop from queue:",q.dequeue())
print("size after pop:",q.size())



# /output
# size of queue: 0
# queue after push: 3
# queue before search pop: ['apple', 'banana', 'cherry']
# banana1
# queue after search pop: ['apple', 'banana', 'cherry']
# pop from queue: apple
# size after pop: 2





