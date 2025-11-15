class Stack:
    #constructor
    def __init__(self):
        self.stack=[]
        
    #method to get size of stack
    def size(self):
        print("length of stack: ", len(self.stack))
    
    #method to check if stack is empty
    def is_empty(self):
        return len(self.stack)==0
    
    #method to add item to stack
    def push(self,item):
        self.stack.append(item)
        print ("Adding item:",item)
        s1.size()
    
    #method to remove item from stack
    def pop(self):
        if not self.is_empty():
            remove=self.stack.pop()
            print("Removing element:",remove)
            s1.size()
        else:
            print("isempty")
            
    #method to view top item of stack
    def peek(self):
        if not self.is_empty():
            print(self.stack[-1])
        else:
            print("stack empty") 
    
    #method to search item in stack
    def search(self,item):
        if not self.is_empty():
            if item in self.stack:
                print( item ,"found in stack")
            else:
                print(item," not found in stack")
        else:
            print("stack is empty")
         
    #method to traverse the stack   
    def traverse(self):
        for items in reversed(self.stack):
            print(items)

        

s1=Stack()
print("Is stack empty?:",s1.is_empty())
s1.size()
s1.push(10)
s1.push(20)
s1.push(30)
s1.traverse()
s1.search(20)
s1.pop()
s1.pop()
print("Is stack empty?:",s1.is_empty())

# Is stack empty?: True
# length of stack:  0
# Adding item: 10
# length of stack:  1
# Adding item: 20
# length of stack:  2
# Adding item: 30
# length of stack:  3
# 20 found in stack
# Removing element: 30
# length of stack:  2
# Removing element: 20
# length of stack:  1
# Is stack empty?: False