class Stack:
    def __init__(self):
        self.stack=[]
        
    def size(self):
        length = len(self.stack)
        print("Length of stack is:",length)
        
    def is_empty(self):
        empty = len(self.stack)==0
        print("Stack is empty:",empty)
        
    def push(self,item):
        self.stack.append(item)
        print ("Item pushed in stack",item)
        s1.size()
        
    def peek(self):
        if not self.is_empty():
           print("top item:",self.stack[-1])
        else:
            print("stack is empty")
            
    def pop(self):
        if not self.is_empty():
            remove=self.stack.pop()
            print("item removed",remove)
        else:
            print("stack is empty") 
        
    
s1 =Stack()
s1.size()
s1.is_empty()
s1.push(10)
s1.push(20)
s1.push(30)
s1.pop()
s1.size()
s1.peek()
s1.pop()
s1.size()
s1.is_empty()