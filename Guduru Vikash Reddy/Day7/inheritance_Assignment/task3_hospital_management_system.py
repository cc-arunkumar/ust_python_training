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
# ⚙️ Task: Design this in such a way that code duplication is minimized and every
# class inherits logically.
# �� print complete details for a Surgeon (name, specialization, surgery_type,
# etc.)

# Step 1: Define a base class for all persons with common attributes
class Persons:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

# Step 2: Create a Doctor class inheriting from Persons and add medical specialization
class Doctor(Persons):
    def __init__(self, name, age, gender,specialization,consultation_fee):
        Persons.__init__(self,name,age,gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee

# Step 3: Create a Patient class inheriting from Persons and add illness and room info
class Patient(Persons):
    def  __init__(self, name, age, gender,disease,room_number):
        Persons.__init__(self,name,age,gender)
        self.disease=disease
        self.room_number=room_number

# Step 4: Create a Surgeon class inheriting from Doctor and add surgery capability
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgery):
        Doctor.__init__(self,name, age, gender,specialization,consultation_fee)
        self.surgery=surgery
    def perform_surgery(self):
        print(f"Name:",self.name)
        print(f"Age:",self.age)
        print(f"Gender:",self.gender)
        print(f"Specialization:",self.specialization)
        print(f"consultation fee:",self.consultation_fee)
        print(f"performing surgery:",self.surgery)

# Step 5: Instantiate a Surgeon and perform surgery
person=Surgeon("Mohammad",22,"male","plastic",500,"plastic surgery")

person.perform_surgery()

# sample output
# Name: Mohammad
# Age: 22
# Gender: male
# Specialization: plastic
# consultation fee: 500
# performing surgery: plastic surgery
        
        
        