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

# Creating base class 
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
class Doctor(Person):
    def __init__(self,name,age,gender,specialization,consultation_fee):
        Person.__init__(self,name,age,gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee
class Patient(Person):
    def __init__(self,name,age,gender,disease,room_number):
        Person.__init__(self,name,age,gender)
        self.disease=disease
        self.room_number=room_number
class Surgeon(Doctor):
    def __init__(self,name,age,gender,specialization,consultation_fee,surgery_type):
        Doctor.__init__(self,name,age,gender,specialization , consultation_fee)
        self.surgery_type=surgery_type
    def perform_surgery(self):
        print("Surgery performed")

surgeon01=Surgeon("Aakash",21,"Male","anaesthesiologist",5000,"Invasive")
surgeon01.perform_surgery()
print(f"{surgeon01.name}| is a{surgeon01.specialization} who does {surgeon01.surgery_type} surgery")
