#method Overridiing

class Employeee:
    def get_details(self):
        print("I am very good in the work ")
        
class Bhargavi(Employeee):#inheritance
    def get_details(self): #method overridding
        print("I am ust worker")
        
class Veena(Employeee):
    def get_details(self):
        print("I am manger of the project")
        
e1 = Employeee()
e2 = Bhargavi()
e3 = Veena()

e2.get_details()
e1.get_details()
e3.get_details()

#output
# I am ust worker
# I am very good in the work 
# I am manger of the project 