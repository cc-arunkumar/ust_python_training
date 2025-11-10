#Queue

class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self,item):
        self.queue.append(item)
        print(item,"Pushed Successfully")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is Empty")

    def search(self,item):
        if not self.is_empty() and item in self.queue:
            position=self.queue.index(item)+1
            print(f"Item {item} found at {position} ")
        else:
            print("Item Not found")
    

s = Queue()
print("Is Queue Empty:",s.is_empty())
print("The size of Queue:",s.size())
s.enqueue(10)
print("Adding Element:",s.peek())
print("The Length os Queue:",s.size())
s.enqueue(20)
print("Adding Element:",s.peek())
print("The Length os Queue:",s.size())
s.enqueue(30)
print("Adding Element:",s.peek())
print("The Length os Queue:",s.size())
print("Removing Element:",s.pop())
print("The Length of Queue:",s.size())
print("Is Queu Empty:",s.is_empty())
print(s.search(30))
    
# sample output
# Is Queue Empty: True
# The size of Queue: 0
# 10 Pushed Successfully
# Adding Element: 10
# The Length os Queue: 1
# 20 Pushed Successfully
# Adding Element: 10
# The Length os Queue: 2
# 30 Pushed Successfully
# Adding Element: 10
# The Length os Queue: 3
# Removing Element: 10
# The Length of Queue: 2
# Is Queu Empty: False
# Item 30 found at 2
# Search the item position:  None
# PS C:\Users\303397\Desktop\Training> & C:/Users/303397/AppData/Local/Microsoft/WindowsApps/python3.12.exe "c:/Users/303397/Desktop/Training/DAY 4/queue.py"
# Is Queue Empty: True
# The size of Queue: 0
# 10 Pushed Successfully
# Adding Element: 10
# The Length os Queue: 1
# 20 Pushed Successfully
# Adding Element: 10
# The Length os Queue: 2
# 30 Pushed Successfully
# Adding Element: 10
# The Length os Queue: 3
# Removing Element: 10
# The Length of Queue: 2
# Is Queu Empty: False
# Item 30 found at 2