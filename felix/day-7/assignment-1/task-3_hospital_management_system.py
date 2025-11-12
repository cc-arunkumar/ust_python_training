# Task 3 — Hospital Management System
# Domain: Healthcare IT
# Business Requirement:
# UST Healthcare division needs a mini module to handle hospital roles.
# 1. Every Person has:
# name , age , gender
# 2. Doctor and Patient both inherit from Person, but have different fields:
# Doctor → specialization , consultation_fee
# Patient → disease , room_number
# 3. The hospital wants to extend Doctor to include Surgeon (with surgery_type and 
# perform_surgery() ).


# Creating Person class
class Person:
    def __init__(self,name,age,gender):
        self.name= name
        self.age = age
        self.gender = gender
       
# Doctor extends Person 
class Doctor(Person):
    def __init__(self, name, age, gender,specialization,consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee
       
# Patient extends Person 
class Patient(Person):
    def __init__(self, name, age, gender,disease,room_number):
        Person.__init__(self,name, age, gender)
        self.disease = disease
        self.room_number = room_number
        
# Surgeon extends Doctor
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgery_type):
        Doctor.__init__(self,name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type
        self.name = name
        self.specialization = specialization
    def perform_surgery(self):
        print(f"Name: {self.name}")
        print(f"Surgery type: {self.surgery_type}")
        print(f"Specialization: {self.specialization}")
        
        
# Creating objects for all classes
person = Person("Arun",25,"Male")
doctor = Doctor("Arun",25,"Male","ENT",500)
patient = Patient("Arun",25,"Male","Feaver",114)
surgeon  = Surgeon("Felix",23,"Male","ENT",500,"Eye")
surgeon.perform_surgery()

# output

# Name: Felix
# Surgery type: Eye
# Specialization: ENT