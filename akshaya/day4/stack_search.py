#stack
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def push(self, element):
        self.stack.append(element)
        print(f"Adding element: {element}")
        print(f"Length of stack = {self.size()}")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty, cannot pop.")
        else:
            removed = self.stack.pop()
            print(f"Removed element: {removed}")
            print(f"Current stack size = {self.size()}")

    def search(self, element):
        if element in self.stack:
            position = len(self.stack) - self.stack.index(element)
            print(f"Element {element} found in stack at position {position} from top.")
        else:
            print(f"Element {element} not found in stack.")

s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.search(20)
s.search(50)

# sample output
# Adding element: 10
# Length of stack = 1
# Adding element: 20
# Length of stack = 2
# Adding element: 30
# Length of stack = 3
# Element 20 found in stack at position 2 from top.
# Element 50 not found in stack.
