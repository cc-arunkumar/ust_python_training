# methodoverloading 
class Methodoverloading:
    def add(self,a,b=0):
        print("2 parameter")
        sum=a+b
        print(sum)
    def add(self,a,b,c=0):
        sum=a+b+c
        print("3 parameter")
        print(sum)
m1=Methodoverloading()
m1.add(10,20)
m1.add(10,20,30)


# #3 parameter
# 30
# 3 parameter
# 60