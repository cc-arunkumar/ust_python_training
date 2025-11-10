# class queue:
#     def __init__(self):
#         self.a=[]

#     def size(self):
#         return len(self.a)
    
#     def is_empty(self):
#         if len(self.a)==0:
#             return True
#         else:
#             return False
        
#     def push(self,item):
#         self.a.append(item)

#     def peek(self):
#         if not self.is_empty():
#             return self.a[0]
#         else:
#             return "Queue is empty"
        
#     def pop(self):
#         if not self.is_empty():
#             self.a.remove(self.a[0])

#     def search(self,ele):
#         if not self.is_empty():
#             for i in self.a:
#                 if i==ele:
#                     return "Present"
                
#             return "Not present" 

# obj=queue()

# print("Is queue empty:",obj.is_empty())
# print("Length of the queue:",obj.size())
# obj.push(10)
# print("Adding element:",obj.peek())
# print("Length of the queue:",obj.size())
# obj.push(20)
# print("Adding element:",obj.peek())
# print("Length of the queue:",obj.size())
# obj.push(30)
# print("Adding element:",obj.peek())
# print("Length of the queue:",obj.size())
# print("Removing element:",obj.peek())
# popped=obj.pop()
# print("Length of the queue:",obj.size())
# print("Is queue empty:",obj.is_empty())

# print("Is 20 present:",obj.search(30))

class queue:
    def __init__(self):
        self.a = []

    def size(self):
        return len(self.a)
    
    def is_empty(self):
        return len(self.a) == 0
        
    def push(self, item):
        self.a.append(item)

    def peek(self):
        if not self.is_empty():
            return self.a[-1]
        return "Queue is empty"
        
    def pop(self):
        if not self.is_empty():
            return self.a.pop(0)
        return "Queue is empty"

    def search(self, ele):
        if not self.is_empty():
            for i in self.a:
                if i == ele:
                    return "Present"
            return "Not present"
        return "Queue is empty"
obj = queue()

print("Is queue empty:", obj.is_empty())
print("Length of the queue:", obj.size())
obj.push(10)
print("Adding element:", obj.peek())
print("Length of the queue:", obj.size())
obj.push(20)
print("Adding element:", obj.peek())
print("Length of the queue:", obj.size())
obj.push(30)
print("Adding element:", obj.peek())
print("Length of the queue:", obj.size())
print("Removing element:", obj.pop())
print("Length of the queue:", obj.size())
print("Is queue empty:", obj.is_empty())

print("Is 30 present:", obj.search(30))



# Sample output

# Is queue empty: True
# Length of the queue: 0
# Adding element: 10
# Length of the queue: 1
# Adding element: 20
# Length of the queue: 2
# Adding element: 30
# Length of the queue: 3
# Removing element: 10
# Length of the queue: 2
# Is queue empty: False
# Is 30 present: Present