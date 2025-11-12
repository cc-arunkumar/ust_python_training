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

# Task: Design this in such a way that code duplication is minimized and every
# class inherits logically. print complete details for a Surgeon (name, specialization, surgery_type,
# etc.)
# Task 4 — E-Commerce Platform (Inventory System)

# Base class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

# Doctor class
class Doctor(Person):
    def __init__(self, name, age, gender, specialization, consultation_fee):
        Person.__init__(self, name, age, gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def doctor_info(self):
        self.show_info()
        print(f"Specialization: {self.specialization}, Consultation Fee: ₹{self.consultation_fee}")

# Patient class
class Patient(Person):
    def __init__(self, name, age, gender, disease, room_number):
        Person.__init__(self, name, age, gender)
        self.disease = disease
        self.room_number = room_number

    def patient_info(self):
        self.show_info()
        print(f"Disease: {self.disease}, Room Number: {self.room_number}")

# Surgeon class
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        Doctor.__init__(self, name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type

    def perform_surgery(self):
        print(f"{self.name} is performing a {self.surgery_type} surgery.")

    def surgeon_info(self):
        self.doctor_info()
        print(f"Surgery Type: {self.surgery_type}")

# Create a Surgeon object
s = Surgeon("Dr.Bhargavi", 100, "Female", "Cardiology", 1500, "stimulating")

# Print complete details
print("Surgeon Details:")
s.surgeon_info()
s.perform_surgery()




#output
