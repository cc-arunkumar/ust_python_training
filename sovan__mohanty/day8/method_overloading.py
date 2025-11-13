#Method Overloading 
class M_O:
    def add(self,a=0,b=0):
        print(f"Fisrt method: {a+b}")
    def add(self,a=0,b=0,c=0):
        print(f"Second method: {a+b+c}")
mo1=M_O()
mo1.add(10,20)
mo1.add(10,20,30)

#Sample Execution
# Second method: 30
# Second method: 60
