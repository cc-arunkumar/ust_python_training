#Task : Queue Operations such as push,pop,peek,search,traverse,is_Empty

#Code
class Queue:
    def __init__(self):
        self.queue=[]
    def is_Empty(self):
        return len(self.queue)==0
    def push(self,item):
        self.queue.append(item)

    def pop(self):
        if not self.is_Empty():
            remove=self.queue.pop(0)
            print("Removing element : ",remove)
            return remove
        else:
            print("The queue is empty ")
            return None
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "queue is empty"
    def size(self):
        return len(self.queue)
    
    def search(self,elem):
        if not self.is_Empty():
                if elem in self.queue:
                    print("Found")
                else:
                    print("Not Present")
    def traverse(self):
        return self.queue
obj=Queue()
print("Is Queue empty? : ",obj.is_Empty())
print("Size of the queue : ",obj.size())
obj.push(int(input("Enter the number to Enque : ")))
obj.push(int(input("Enter the number to Enque : ")))
obj.push(int(input("Enter the number to Enque : ")))
obj.push(int(input("Enter the number to Enque : ")))
obj.push(int(input("Enter the number to Enque : ")))
print("Traversing each Element in queue : ",obj.traverse())
obj.search(32)
print("Pop the element : ",obj.pop())
print("Size after pop : ",obj.size())

#Output
# Is Queue empty? :  True
# Size of the queue :  0
# Enter the number to Enque : 2
# Enter the number to Enque : 3
# Enter the number to Enque : 4
# Enter the number to Enque : 32
# Enter the number to Enque : 5
# Traversing each Element in queue :  [2, 3, 4, 32, 5]
# Found
# Removing element :  2
# Pop the element :  2
# Size after pop :  4





