class Stack:
    def __init__(self):
        self.stack1 = []  

    def size(self):
        return len(self.stack1)

    def is_empty(self):
        return len(self.stack1) == 0
    
    def push(self, item):
        self.stack1.append(item)
    
    def pop1(self):
        if not self.is_empty():
            return self.stack1.pop()
        else:
            return "Stack is Empty!"
    
    def peek(self):
        if not self.is_empty():
            return self.stack1[-1]
        else:
            return "Stack is Empty"   



stack = Stack()
print("Is Stack Empty : ",stack.is_empty()) 
print("Length of Stack : ",stack.size())
print("Adding Element : 10")
stack.push(10)
print("Length of Stack : ",stack.size())
print("Adding Element : 30")
stack.push(30)
print("Length of Stack : ",stack.size())
print("Removing Element : 30")
print("Removed Element ", stack.pop1())
print("Length of Stack : ",stack.size())
print("Element On Top : ", stack.peek())
print("Is Stack Empty : ", stack.is_empty())
stack.pop1()
print("After Popping the final Element : ", stack.peek())


#sample output
# Is Stack Empty :  True
# Length of Stack :  0
# Adding Element : 10
# Length of Stack :  1
# Adding Element : 30
# Length of Stack :  2
# Removing Element : 30
# Removed Element  30
# Length of Stack :  1
# Element On Top :  10
# Is Stack Empty :  False
# After Popping the final Element :  Stack is Empty