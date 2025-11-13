class Stack:
    def __init__(self):
        self.stack=[]

    def size(self):
        return(len(self.stack))

    def isEmpty(self):
        return(len(self.stack)==0)

    def push(self,item):
        self.stack.append(item)

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is Empty")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is Empty")
    
    def search(self,element):
        cout=0
        if not self.isEmpty():
            for stack in self.stack:
                if(stack==element):
                    print("Element found in the Stack")
                    cout+=1
                    break
            if(cout==0):
                print("Element not found in the Stack")


obj=Stack()
print("Is Stack empty: ",obj.isEmpty())
print("Length of the stack: ",obj.size())
obj.push(int(input("Adding Element: ")))
print("Length of the stack: ",obj.size())
obj.push(int(input("Adding Element: ")))
print("Length of the stack: ",obj.size())
obj.push(int(input("Adding Element: ")))
print("Length of the stack: ",obj.size())
print("Removing Element: ",obj.pop())
print("Length of the stack: ",obj.size())
print("Is Stack empty: ",obj.isEmpty())
obj.search(int(input("Element to serach: ")))

    
    