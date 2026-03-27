#method Overridiing
# This program demonstrates method overriding, where child classes redefine a parent class method to provide specialized behavior.
# The output changes depending on the object type, showing polymorphism in action.

#Base class
class Employeee:
    def get_details(self):
        print("I am very good in the work ")
        
# Child class Bhargavi inherits from Employeee     
class Bhargavi(Employeee):#inheritance
    def get_details(self): #method overridding
        print("I am ust worker")
        
# Child class Veena inherits from Employeee
class Veena(Employeee):
    def get_details(self): # Overriding the base class method with specific behavior
        print("I am manger of the project")
      

# Creating objects  
e1 = Employeee()
e2 = Bhargavi()
e3 = Veena()


# Calling get_details() on different objects
e2.get_details()
e1.get_details()
e3.get_details()

#output
# I am ust worker
# I am very good in the work 
# I am manger of the project 