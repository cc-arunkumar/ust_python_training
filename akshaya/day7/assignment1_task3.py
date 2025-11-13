# Task 3 — Hospital Management System

# # 1. Every Person has
# name , age , gender
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        print(f"Name: {self.name} | Age: {self.age} | Gender: {self.gender}")

# Doctor and Patient both inherit from Person, but have different fields:
# Doctor → specialization , consultation_fee
# Patient → disease , room_number
class Doctor(Person):
    def __init__(self, name, age, gender, specialization, consultation_fee):
        Person.__init__(self, name, age, gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def get_details(self):
        super().get_details()  
        print(f"Specialization: {self.specialization} | Consultation Fee: ₹{self.consultation_fee}")


class Patient(Person):
    def __init__(self, name, age, gender, disease, room_number):
        Person.__init__(self, name, age, gender)
        self.disease = disease
        self.room_number = room_number

    def get_details(self):
        super().get_details() 
        print(f"Disease: {self.disease} | Room Number: {self.room_number}")

# The hospital wants to extend Doctor to include Surgeon (with surgery_type and 
# perform_surgery() ).
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        Doctor.__init__(self, name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type

    def get_details(self):
        super().get_details() 
        print(f"Surgery Type: {self.surgery_type}")

    def perform_surgery(self):
        print(f"Surgeon {self.name} is performing a {self.surgery_type} surgery.")


person1 = Person("Amit", 30, "Male")
person1.get_details()
print("------------------")

doctor1 = Doctor("Dr. Ramesh", 45, "Male", "Cardiologist", 1500)
doctor1.get_details()
print("------------------")

patient1 = Patient("Neha", 60, "Female", "Pneumonia", "102")
patient1.get_details()
print("------------------")

surgeon1 = Surgeon("Dr. Gupta", 50, "Male", "Orthopedics", 2000, "Knee Replacement")
surgeon1.get_details()
surgeon1.perform_surgery()
print("------------------")

# sample output

# Name: Amit | Age: 30 | Gender: Male
# ------------------
# Name: Dr. Ramesh | Age: 45 | Gender: Male
# Specialization: Cardiologist | Consultation Fee: ₹1500
# ------------------
# Name: Neha | Age: 60 | Gender: Female
# Disease: Pneumonia | Room Number: 102
# ------------------
# Name: Dr. Gupta | Age: 50 | Gender: Male
# Specialization: Orthopedics | Consultation Fee: ₹2000
# Surgery Type: Knee Replacement
# Surgeon Dr. Gupta is performing a Knee Replacement surgery.
# ------------------
