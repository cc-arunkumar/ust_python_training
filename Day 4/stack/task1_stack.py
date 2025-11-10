

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack)==0
    
    def push(self,items):
        return self.stack.append(items)
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def search(self,items):
        if not self.is_empty():
            for i in self.stack:
                if i==items:
                    return "yes"
                else:
                    return "No"
       


    
s = Stack()
print("Size of the Stack:",s.size())
print("Is stack empty?",s.is_empty())
s.push(10)
s.push(20)
s.push(30)
print("Top item in Stack:",s.peek())
print("removing last element:",s.pop())
print("element found:",s.search(30))

# sample output:
# Size of the Stack: 0
# Is stack empty? True
# Top item in Stack: 30
# removing last element: 30
# element found: No






   


