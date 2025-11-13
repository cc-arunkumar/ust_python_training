
class MO:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=10
    def add(self,a,b=0):
        print("2 vals")

    def add(self,a,b,c=0):
        print("3 vals")
        
l1=MO()
l1.add(10,20)
l1.add(20,20,39)

