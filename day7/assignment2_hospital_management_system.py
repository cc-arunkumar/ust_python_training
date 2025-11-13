# Task 3 — Hospital Management System 
# UST Healthcare division needs a mini module to handle hospital roles.
# 1. Every Person has:
# name , age , gender

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
# 2. Doctor and Patient both inherit from Person, but have different fields:
# Doctor → specialization , consultation_fee


class Doctor(Person):
    def __init__(self,name,age,gender,consultation_fee,specialization):
        Person.__init__(self,name,age,gender)
        self.consultation_fee=consultation_fee
        self.specialization=specialization
    def get_details(self):
        print(f"Doctor: {self.name}, Age: {self.age}, Gender: {self.gender}, "
              f"Fee: {self.consultation_fee}, Specialization: {self.specialization}")
        
# Patient → disease , room_number

class Patient(Person):
    def __init__(self,name,age,gender,disease,room_number):
        Person.__init__(self,name,age,gender)
        self.disease=disease
        self.room_number=room_number
    def get_details(self):
        print(f"Patient: {self.name}, Age: {self.age}, Gender: {self.gender}, "
              f"Disease: {self.disease}, Room number: {self.room_number}")
        
# The hospital wants to extend Doctor to include Surgeon (with surgery_type and perform_surgery() ).

class Surgeon(Doctor):
    def __init__(self,name,age,gender,consultation_fee,specialization,surgery_type):
        Doctor.__init__(self,name,age,gender,consultation_fee,specialization)
        self.surgery_type=surgery_type
    def perform_surgery(self, patient_name):
        print(f"Dr. {self.name} is performing a {self.surgery_type} surgery on patient {patient_name}.")
        
# Sample data
# Doctor
doc = Doctor("Meera", 45, "Female", 500, "Cardiology")
doc.get_details()

# Patient
pat = Patient("Rahul", 30, "Male", "Appendicitis", 101)
pat.get_details()

# Surgeon
surgeon = Surgeon("Arjun", 50, "Male", 1000, "Orthopedics", "Knee Replacement")
surgeon.get_details()
surgeon.perform_surgery("Rahul")

# Output
# Doctor: Meera, Age: 45, Gender: Female, Fee: 500, Specialization: Cardiology
# Patient: Rahul, Age: 30, Gender: Male, Disease: Appendicitis, Room number: 101
# Doctor: Arjun, Age: 50, Gender: Male, Fee: 1000, Specialization: Orthopedics
# Dr. Arjun is performing a Knee Replacement surgery on patient Rahul.
        
        
    
        