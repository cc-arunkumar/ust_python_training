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
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class Doctor(Person):
    def __init__(self, name, age, gender, specialization, consultation_fee):
        Person.__init__(self, name, age, gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def doctor_info(self):
        print(f"Specialization: {self.specialization}, Consultation Fee: ₹{self.consultation_fee}")

class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        Doctor.__init__(self, name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type

    def perform_surgery(self):
        print(f"{self.name} is performing a {self.surgery_type} surgery.")

    def show_surgeon_details(self):
        self.person_info()
        self.doctor_info()
        print(f"Surgery Type: {self.surgery_type}")

# Sample input and function calls
surgeon = Surgeon("Dr. Mahitha", 40, "female", "Cardiology", 2500, "Bypass")
surgeon.show_surgeon_details()
surgeon.perform_surgery()

# sample output
# Name: Dr. Mahitha, Age: 40, Gender: female
# Specialization: Cardiology, Consultation Fee: ₹2500
# Surgery Type: Bypass
# Dr. Mahitha is performing a Bypass surgery.  