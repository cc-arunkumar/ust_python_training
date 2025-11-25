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
#Creating a class Person with the required attributes.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

#Creating a class Doctor and Inheriting the properties of class Person in it.
class Doctor(Person):
    def __init__(self, name, age, gender, specialization, consultationfee):
        self.specialization = specialization
        self.consultationfee = consultationfee
        Person.__init__(self, name, age, gender)
    
    def display_info(self):
        Person.display_info(self)
        print(f"Specialization: {self.specialization}")
        print(f"Consultation Fee: {self.consultationfee}")


#Creating a class Patient and Inheriting the properties of Person in it.
class Patient(Person):
    def __init__(self, name, age, gender, disease, room_no):
        self.disease = disease
        self.room_no = room_no
        Person.__init__(self, name, age, gender)
    
    def display_info(self):
        super().display_info()
        print(f"Disease: {self.disease}")
        print(f"Room Number: {self.room_number}")

#Creating a class Surgeon and Inheriting the properties of Doctor in it.
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultationfee, surgery_type):
        self.surgery_type = surgery_type
        Doctor.__init__(self, name, age, gender, specialization, consultationfee)

    def perform_surgery(self):
            print(f"Performing {self.surgery_type} surgery.")
        
    def display_info(self):
            super().display_info()
            print(f"Surgery Type: {self.surgery_type}")

#Example Values:
surgeon = Surgeon("Dr. Meera Iyer", 45, "Female", "Orthopadic", 15000, "Knee Replacement")
surgeon.display_info()
surgeon.perform_surgery()

print("------------------------------------------------------------------------")

surgeon = Surgeon("Dr. Ranjit Dash", 55, "Male", "Cardiac", 125000, "Heart Bypass")
surgeon.display_info()
surgeon.perform_surgery()

print("---------------------------------------------------------------------------")


#Console Output:
# Name: Dr. Meera Iyer
# Age: 45
# Gender: Female
# Specialization: Orthopadic
# Consultation Fee: 15000
# Surgery Type: Knee Replacement
# Performing Knee Replacement surgery.
# ------------------------------------------------------------------------
# Name: Dr. Ranjit Dash
# Age: 55
# Gender: Male
# Specialization: Cardiac
# Consultation Fee: 125000
# Surgery Type: Heart Bypass
# Performing Heart Bypass surgery.
# ---------------------------------------------------------------------------