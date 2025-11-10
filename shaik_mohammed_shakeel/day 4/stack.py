#Stack

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self,item):
        self.stack.append(item)
        print(item,"Pushed Item Successfully")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is Empty")
    
    def search(self,item):
        if not self.is_empty() and item in self.stack:
            l=len(self.stack) - self.stack[::-1].index(item)
            print(f"Item{item} found at pos{l} from bottom")
        else:
            print(f"{item} not found")


s = Stack()
print("Is Stack Empty:",s.is_empty())
print("The size of Stack:",s.size())
s.push(10)
print("Adding Element:",s.peek())
print("The Length os Stack:",s.size())
s.push(20)
print("Adding Element:",s.peek())
print("The Length os Stack:",s.size())
s.push(30)
print("Adding Element:",s.peek())
print("The Length os Stack:",s.size())
print("Removing Element:",s.pop())
print("The Length os Stack:",s.size())
print("Is Stack Empty:",s.is_empty())
s.search(20)
s.push(10)
s.push(20)
print(s.pop())  
print(s.peek())
print(s.size())
print(s.is_empty())

#Sample Output
# Is Stack Empty: True
# The size of Stack: 0
# 10 Pushed Item Successfully
# Adding Element: 10
# The Length os Stack: 1
# 20 Pushed Item Successfully
# Adding Element: 20
# The Length os Stack: 2
# 30 Pushed Item Successfully
# Adding Element: 30
# The Length os Stack: 3
# Removing Element: 30
# The Length os Stack: 2
# Is Stack Empty: False
# Item20 found at pos2 from bottom
# 10 Pushed Item Successfully
# 20 Pushed Item Successfully
# 20
# 10
# 3
# False





