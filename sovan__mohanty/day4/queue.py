#Task Queue

class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return (len(self.queue) == 0)

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
             return "Queue is empty"

    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return "Queue is empty"
    def search(self,element):
        cout=0
        if not self.isEmpty():
            for queue in self.queue:
                if(queue==element):
                    print("Element found")
                    cout+=1
                    break
            if(cout==0):
                print("Element not found")
obj=Queue()
print("Is queue empty: ",obj.isEmpty())
print("Length of the queue: ",obj.size())
obj.push(int(input("Adding Element: ")))
print("Length of the queue: ",obj.size())
obj.push(int(input("Adding Element: ")))
print("Length of the queue: ",obj.size())
obj.push(int(input("Adding Element: ")))
print("Length of the queue: ",obj.size())
print("Removing Element: ",obj.pop())
print("Length of the queue: ",obj.size())
print("Is queue empty: ",obj.isEmpty())
obj.search(int(input("Element to serach: ")))

#Sample Execution
# Is queue empty:  True
# Length of the queue:  0
# Adding Element: 3
# Length of the queue:  1
# Adding Element: 45
# Length of the queue:  2
# Adding Element: 44
# Length of the queue:  3
# Removing Element:  3
# Length of the queue:  2
# Is queue empty:  False
# Element to serach: 45
# Element found
