class Stack:
    def __init__(self):
        self.stack=[]
        
    def size(self):
        return len(self.stack)  #length of stack
    
    def is_empty(self):
        return len(self.stack)==0    #check if stack is empty
    
    def push(self,item):
        self.stack.append(item)      #add to stack
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]        #find last element
        else:
            print("Stack is empty")
    
    def pop(self):
        if not self.is_empty():
            self.stack.remove(self.stack[-1])    #remove last element
        else:
            print("Stack is empty")
    
    def element_search(self,elem):
        if not self.is_empty():
            for i in self.stack:
                if i == elem:
                    return True
        else:
            print("Stack is empty")
            
obj =Stack()

print("Is the stack empty: ",obj.is_empty())
print("Length of Stack: ",obj.size())
obj.push(10)
print("Adding element: ",obj.peek())
print("Length of Stack: ",obj.size())
obj.push(20)
print("Adding element: ",obj.peek())
print("Length of Stack: ",obj.size())
obj.push(30)
print("Adding element: ",obj.peek())
print("Length of Stack: ",obj.size())
print("Removing element: ",obj.peek())
obj.pop()
print("Length of Stack: ",obj.size())
print("Is the stack empty: ",obj.is_empty())
print("Item search (20): ",obj.element_search(20))


#Sample Output
# Is the stack empty:  True
# Length of Stack:  0
# Adding element:  10
# Length of Stack:  1
# Adding element:  20
# Length of Stack:  2
# Adding element:  30
# Length of Stack:  3
# Removing element:  30
# Length of Stack:  2
# Is the stack empty:  False
# Item search (20):  True
