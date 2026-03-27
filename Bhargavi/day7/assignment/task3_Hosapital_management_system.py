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

# Base class Person
class Person:
    def __init__(self, name, age, gender):
        # Common attributes for all persons
        self.name = name
        self.age = age
        self.gender = gender
    
    # Display basic person information
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


# Doctor class inherits from Person
class Doctor(Person):
    def __init__(self, name, age, gender, specialization, consultation_fee):
        # Initialize base class attributes
        Person.__init__(self, name, age, gender)
        # Doctor-specific attributes
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def doctor_info(self):
        # Display doctor details including specialization and fee
        self.show_info()
        print(f"Specialization: {self.specialization}, Consultation Fee: ₹{self.consultation_fee}")


# Patient class inherits from Person
class Patient(Person):
    def __init__(self, name, age, gender, disease, room_number):
        # Initialize base class attributes
        Person.__init__(self, name, age, gender)
        # Patient-specific attributes
        self.disease = disease
        self.room_number = room_number

    def patient_info(self):
        # Display patient details including disease and room number
        self.show_info()
        print(f"Disease: {self.disease}, Room Number: {self.room_number}")


# Surgeon class inherits from Doctor
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        Doctor.__init__(self, name, age, gender, specialization, consultation_fee)
        # Surgeon-specific attribute
        self.surgery_type = surgery_type
    
    #display surgeon type
    def perform_surgery(self):
        print(f"{self.name} is performing a {self.surgery_type} surgery.")
    
    # Display complete surgeon details including doctor info and surgery type
    def surgeon_info(self):
        self.doctor_info()
        print(f"Surgery Type: {self.surgery_type}")


# Create a Surgeon object
s = Surgeon("Dr.Bhargavi", 100, "Female", "Cardiology", 1500, "stimulating")

# Print complete details
print("Surgeon Details:")
s.surgeon_info()     
s.perform_surgery()  # Shows surgery action




#output
# Surgeon Details:
# Name: Dr.Bhargavi, Age: 100, Gender: Female
# Specialization: Cardiology, Consultation Fee: ₹1500
# Surgery Type: stimulating
# Dr.Bhargavi is performing a stimulating surgery.