# Task 3 — Hospital Management System

# Domain: Healthcare IT

# Business Requirement:
# UST Healthcare division needs a mini module to handle hospital roles.
    # 1. Every Person has:
    # Enterprise Tech Systems – Inheritance Design Challenge 2
    # name , age , gender
    # 2. Doctor and Patient both inherit from Person, but have different fields:
    # Doctor → specialization , consultation_fee
    # Patient → disease , room_number
    # 3. The hospital wants to extend Doctor to include Surgeon (with surgery_type and 
    # perform_surgery() ).

class Person:
    def __init__(self,name,age,gender):
        self.name = name 
        self.age = age 
        self.gender = gender
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender: {self.gender}")
        

class Doctor(Person):
    def __init__(self,name,age,gender, specialization , consultation_fee):
        Person.__init__(self,name,age,gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee

class Patient(Person):
    def __init__(self,name,age,gender,disease ,room_number):
        Person.__init__(self,name,age,gender)
        self.disease = disease
        self.room_number = room_number
        
class Surgeon(Doctor):
    def __init__(self,name,age,gender, specialization , consultation_fee,surgery_type):
        Doctor.__init__(self,name,age,gender, specialization , consultation_fee)
        self.surgery = surgery_type
    
    def perform_surgery(self):
        print("Performing Surgery...")


surgeon1 = Surgeon('Dr.Bob Johnson', 45, 'Male','Cardiologist', 2000, 'Heart Bypass')
surgeon1.perform_surgery()
surgeon1.display()
print("Specialization:",surgeon1.specialization)
print("Surgery Type:",surgeon1.surgery)
print("Consultation Fee: ",surgeon1.consultation_fee)
        

#Sample Output 
# Performing Surgery...
# Name: Dr.Bob Johnson
# Age : 45
# Gender: Male
# Specialization: Cardiologist
# Surgery Type: Heart Bypass
# Consultation Fee:  2000