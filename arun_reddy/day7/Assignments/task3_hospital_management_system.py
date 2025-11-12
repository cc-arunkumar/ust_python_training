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


class Person:
    def __init__(self,name , age , gender):
        self.name=name
        self.age=age
        self.gender=gender

# Doctor extends Person
class Doctor(Person):
    def __init__(self, name, age, gender,specialization,consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee
    # Surgeon extends Doctor
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgery_type):
        Doctor.__init__(self,name, age, gender, specialization, consultation_fee)
        self.name=name
        self.surgery_type=surgery_type
        self.specialization=specialization
    def perform_surgery(self):
        print(f"{self.name} having surgey {self.surgery_type}")
        print(f"Name :{self.name}")
        print(f"Specialization:{self.specialization}")
        print(f"Surgery type:{self.surgery_type}")
    # Patient extends Person
class Patient(Person):
    def __init__(self, name, age, gender,disease , room_number):
        Person.__init__(self,name, age, gender)
        self.disease=disease
        self.room_number=room_number


# �� print complete details for a Surgeon (name, specialization, surgery_type,
# etc.)
srgery=Surgeon("Arun",65,"Male","ENT",900,"apendix")
srgery.perform_surgery()

# sample execution 
# Arun having surgey apendix
# Name :Arun
# Specialization:ENT
# Surgery type:apendix