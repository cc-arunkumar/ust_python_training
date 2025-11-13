# hospital management system

# Requirement:
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
# class inherits logically.
# print complete details for a Surgeon (name, specialization, surgery_type, etc.)


# Base class for all people
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


# Shared medical attributes
class MedicalProfessional:
    def __init__(self, specialization, consultation_fee):
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def __str__(self):
        return f"\nSpecialization: {self.specialization}, Consultation Fee: {self.consultation_fee}"


# Doctor inherits from both Person and MedicalProfessional
class Doctor(Person, MedicalProfessional):
    def __init__(self, name, age, gender, specialization, consultation_fee):
        Person.__init__(self, name, age, gender)
        MedicalProfessional.__init__(self, specialization, consultation_fee)

    def __str__(self):
        return f"{Person.__str__(self)}, {MedicalProfessional.__str__(self)}"


# Patient inherits from Person
class Patient(Person):
    def __init__(self, name, age, gender, disease, room_number):
        super().__init__(name, age, gender)
        self.disease = disease
        self.room_number = room_number

    def __str__(self):
        return f"{super().__str__()}, Disease: {self.disease}, Room Number: {self.room_number}"


# Surgeon inherits from Doctor (which already inherits from Person and MedicalProfessional)
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        super().__init__(name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type

    def perform_surgery(self):
        return f"{self.name} is performing a {self.surgery_type} surgery."

    def __str__(self):
        return f"{super().__str__()}, Surgery Type: {self.surgery_type}"


# Create a Surgeon object
surgeon = Surgeon(name="Usha Rani", age=55, gender="Female", specialization="Orthopedics",
                  consultation_fee=600, surgery_type="Knee Replacement")

# Print complete details for a Surgeon
print(surgeon)

# Perform surgery
print(surgeon.perform_surgery())

#o/p:
# Name: Usha Rani, Age: 55, Gender: Female, Specialization: Orthopedics, Consultation Fee: 600, Surgery Type: Knee Replacement
# Usha Rani is performing a Knee Replacement surgery.