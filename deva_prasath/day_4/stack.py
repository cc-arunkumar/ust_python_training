class stack:
    def __init__(self):
        self.a=[]

    def size(self):
        return len(self.a)
    
    def is_empty(self):
        if len(self.a)==0:
            return True
        else:
            return False
        
    def push(self,item):
        self.a.append(item)

    def peek(self):
        if not self.is_empty():
            return self.a[-1]
        else:
            return "Stack is empty"
        
    def pop(self):
        if not self.is_empty():
            self.a.remove(self.a[-1])
    def search(self,ele):
        if not self.is_empty():
            for i in self.a:
                if i==ele:
                    return i
                else:
                    return "Not present" 


            
obj=stack()

print("Is stack empty:",obj.is_empty())
print("Length of the stack:",obj.size())
obj.push(10)
print("Adding element:",obj.peek())
print("Length of the stack:",obj.size())
obj.push(20)
print("Adding element:",obj.peek())
print("Length of the stack:",obj.size())
obj.push(30)
print("Adding element:",obj.peek())
print("Length of the stack:",obj.size())
print("Removing element:",obj.peek())
popped=obj.pop()
print("Length of the stack:",obj.size())
print("Is stack empty:",obj.is_empty())
print("Is 20 present:",obj.search(30))


#Sample output
# Is stack empty: True
# Length of the stack: 0
# Adding element: 10
# Length of the stack: 1
# Adding element: 20
# Length of the stack: 2
# Adding element: 30
# Length of the stack: 3
# Removing element: 30
# Length of the stack: 2
# Is stack empty: False
# Is 20 present: Not present