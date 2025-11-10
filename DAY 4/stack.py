class Stack:
    def __init__(self):
        self.stack=[]

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack)==0
    
    def push(self,element):
        self.stack.append(element)
    
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        else : print("Stack is empty")
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else : print("Stack is Empty")
    
    def search(self,element):
        if not self.is_empty():
            for i in self.stack:
                if i==element: return "Yes"
                else: return "No"
        else: return "Stack is Empty"


s=Stack()


if(s.is_empty()):
    print("The Stack is empty")

print("Adding element 10")
s.push(10)
# s.peak()
print("The length of the stack is",s.size())

print("Adding element 20")
s.push(20)
print("The length of the stack :",s.size())
s.peak()

print("Poping the last element :", s.pop())
# print(s)
# print(s.self.stack())

print("Element is there : ",s.search(10))