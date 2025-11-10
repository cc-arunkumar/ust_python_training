class Stack: 
    def __init__(self):
        self.stack=[]
        
    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self,val):
        self.stack.append(val)
        print(f"adding element {val}")
        
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            
    def pop(self):
        if not self.isEmpty():
            # val = self.stack[:-1]
            # return self.stack.remove(val)
            return self.stack.pop()
        else:
            print("Stack is empty")
        
        
my_stack = Stack()
print("stack is empty",my_stack.isEmpty())
my_stack.push(10)
my_stack.push(30)
my_stack.push(40)
my_stack.push(50)
my_stack.push(60)

print("size ",my_stack.size())
print("peek element is ",my_stack.peek())
print("pop element is ",my_stack.pop())

list = [1,2,3,4,5,6,7]
del list[0]
print(list)


# ==============sample output=================
# stack is empty True
# adding element 10
# adding element 30
# adding element 40
# adding element 50
# adding element 60
# size  5
# peek element is  60
# pop element is  60

