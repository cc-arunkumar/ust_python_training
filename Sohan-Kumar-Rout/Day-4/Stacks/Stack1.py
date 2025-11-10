#Task : Stack Operation such as push,pop,peek,isEmpty,


#Code
class Stack:
    def __init__(self):
        self.stack=[]
    def size(self):
        return (len(self.stack))
    
    def isEmpty(self):
        return (len(self.stack)==0)
    
    def push(self,item):
        self.stack.append(item)

    def peek(self):
        if not  self.isEmpty():
            return self.stack[-1]
        print("Not available")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        print("Not available")

    def search(self,elem):
        if not self.isEmpty():
            for ser in self.stack:
                if ser==elem:
                    print("Found")
                else:
                    print("Not present")
    
obj=Stack()
print("Is the Stack Empty : ",obj.isEmpty())
print("Size of Stack : ",obj.size())
obj.push(int(input("Adding Element : ")))
print("Length of stack : ",obj.size())
obj.push(int(input("Adding Element : ")))
print("Length of stack : ",obj.size())
print("Removing Element : ",obj.pop())
print("Length of stack : ",obj.size())
obj.search(int(input("search element : ")))
print("Is the stack Empty : ",obj.isEmpty())
print("Remove Element : ",obj.pop())
print("Is the stack Empty : ",obj.isEmpty())

#Output
# Is the Stack Empty :  True
# Size of Stack :  0
# Adding Element : 2
# Length of stack :  1
# Adding Element : 2
# Length of stack :  2
# Removing Element :  2
# Length of stack :  1
# search element : 2
# Found
# Is the stack Empty :  False
# Remove Element :  2
# Is the stack Empty :  True



