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

# Base class representing a general person

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

# Subclass representing a Doctor, inherits from Person

class Doctor(Person):
    def __init__(self,name,age,gender,specialization,consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee


# Subclass representing a Patient, inherits from Person

class Patient(Person):
    def __init__(self, name, age, gender,disease,room_number):
        Person.__init__(self,name, age, gender)
        self.disease=disease
        self.room_number=room_number


# Subclass representing a Surgeon, inherits from Doctor

class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgery_type):
        Doctor.__init__(self,name, age, gender, specialization, consultation_fee)
        self.surgery_type=surgery_type

     # Method to print surgeon details and surgery type

    def perform_surgery(self):
        print(f"Surgeon Name: {self.name}")
        print(f"Surgeon Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Surgeon Specialization: {self.specialization}")
        print(f"Colsultation Price: {self.consultation_fee}")
        print(f"Surgery Type: {self.surgery_type}")

# Creating a Surgeon object
d1=Surgeon("Indu",20,"Female","MBBS",500,"cardiologist")

# Calling the method to show surgeon details
d1.perform_surgery()
print()

#Sample output
# Surgeon Age: 20
# Gender: Female
# Surgeon Specialization: MBBS
# Colsultation Price: 500
# Surgery Type: cardiologist
