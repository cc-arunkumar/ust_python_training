#Stack Basics
li=[1,2,3,4,5,6]

class Stack:
    def __init__(self):
        self.stack=[]
        
    def isempty(self):
        return len(self.stack)==0
    
    def size(self):
        return f"Length of the Stack: {len(self.stack)}"
    
    def push(self,element):
        self.stack.append(element)
        return f"Adding Element: {element}"
        
    def peek(self):
        if not self.isempty():
            return f"Top of the Stack: {self.stack[-1]}"
        else:
            return "No Elements in Stack to Peek"
    
    def pop(self):
        if not self.isempty():
            pop_ele = self.stack[-1]
            self.stack.remove(self.stack[-1])
            return f"Removing Element: {pop_ele}"
        else:
            return "No Elements in stack to Pop"
        
    def search(self,element):
        if not self.isempty():
            if element in self.stack:
                return f"{element} found in Stack" 
            return f"{element} Not Found in Stack"
        return "stack is empty"
    
st = Stack()
print("Is Stack Empty: ",st.isempty())
print(st.size())
print(st.push(10))
print(st.size())
print(st.push(20))
print(st.size())
print(st.push(30))
print(st.size())
print(st.pop())
print(st.size())
print("Is Stack Empty:",st.isempty())
print(st.search(20))


#Sample Output
# Is Stack Empty:  True
# Length of the Stack: 0
# Adding Element: 10
# Length of the Stack: 1
# Adding Element: 20
# Length of the Stack: 2
# Adding Element: 30
# Length of the Stack: 3
# Removing Element: 30
# Length of the Stack: 2
# Is Stack Empty: False
# 20 found in Stack