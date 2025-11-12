# Task: 
# The company wants to create a class SmartEV — a self-driving electric vehicle.

# Base class
class Person:
    def __init__(self, name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender
    def get_details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")

# Subclass 1 — Doctor
class Doctor(Person):
    def __init__(self, name, age, gender, specialization,consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def get_doctor_details(self):
        print(f"name: {self.name}")
        print(f"specialization: {self.specialization}")
        print(f"Fees is : {self.consultation_fee}")

# Subclass 2 — Patient
class Patient(Person):
    def __init__(self, name, age, gender, disease, room_number):
        Person.__init__(self,name, age, gender)
        self.disease = disease
        self.room_number = room_number

    def get_patient_details(self):
        print(f"Name:{self.name}")
        print(f"Disease is :{self.disease}")
        print(f"Room number is:{self.room_number}")

# Surgeon class
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        Doctor.__init__(self,name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type
    def perform_surgery(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")
        print(f"specialized in: {self.specialization}")
        print(f"consultation fee is: {self.consultation_fee}")
        print(f"surgery type is: {self.surgery_type}")

#Testing
sur = Surgeon("Madhan", 22, "male", "MBBS", "₹600", "Cardio")
print("-----Surgeon Details-----")
sur.perform_surgery()

# sample output:

# -----Surgeon Details-----
# name: Madhan
# age: 22
# gender: male
# specialized in: MBBS
# consultation fee is: ₹600
# surgery type is: Cardio

