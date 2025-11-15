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
# 3. The hospital wants to extend Doctor to include Surgeon (with surgery_type and perform_surgery() ).
# Task: Design this in such a way that code duplication is minimized and every
# class inherits logically.

#main Code
# 1. Every Person has:
# Enterprise Tech Systems – Inheritance Design Challenge 2
# name , age , gender

# Base class Person
class Person:
    def __init__(self, name, age, gender):
        # Initialize common attributes for all persons
        self.name = name
        self.age = age
        self.gender = gender

    def person_info(self):
        # Display basic person information
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


# Doctor class inherits from Person
class Doctor(Person):
    def __init__(self, name, age, gender, specialization, consultation_fee):
        # Call Person constructor to initialize common attributes
        Person.__init__(self, name, age, gender)
        # Add doctor-specific attributes
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def doctor_info(self):
        # Display doctor-specific information
        print(f"Specialization: {self.specialization}, Consultation Fee: ₹{self.consultation_fee}")


# Surgeon class inherits from Doctor
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        # Call Doctor constructor to initialize doctor attributes
        Doctor.__init__(self, name, age, gender, specialization, consultation_fee)
        # Add surgeon-specific attribute
        self.surgery_type = surgery_type

    def perform_surgery(self):
        # Simulate performing a surgery
        print(f"{self.name} is performing a {self.surgery_type} surgery.")

    def show_surgeon_details(self):
        # Display all details: person info, doctor info, and surgeon info
        self.person_info()      # From Person class
        self.doctor_info()      # From Doctor class
        print(f"Surgery Type: {self.surgery_type}")  # Surgeon-specific


# Sample input and function calls
surgeon = Surgeon("Dr. Mahitha", 40, "female", "Cardiology", 2500, "Bypass")

# Show complete details of the surgeon
surgeon.show_surgeon_details()

# Simulate performing a surgery
surgeon.perform_surgery()


# sample output
# Name: Dr. Mahitha, Age: 40, Gender: female
# Specialization: Cardiology, Consultation Fee: ₹2500
# Surgery Type: Bypass
# Dr. Mahitha is performing a Bypass surgery.  