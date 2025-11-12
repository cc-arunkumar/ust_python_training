# UST Healthcare division needs a mini module to handle hospital roles.
# 1. Every Person has:
# Enterprise Tech Systems – Inheritance Design Challenge 2
# name , age , gender
# 2. Doctor and Patient both inherit from Person, but have different fields:
# Doctor → specialization , consultation_fee
# Patient → disease , room_number
# 3. The hospital wants to extend Doctor to include Surgeon (with surgery_type and perform_surgery() ).

# Parent class
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        
# child class
class Doctor(Person):
    def __init__(self, name, age, gender,specialization,consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee
    def show_doc(self):
        self.show_info()
        print(f"Specialization: {self.specialization}")
        print(f"Consultation fee: {self.consultation_fee}")

# child class
class Patient(Person):
    def __init__(self, name, age, gender,disease,room_number):
        Person.__init__(self,name, age, gender)
        self.disease=disease
        self.room_number=room_number
    def show_patient(self):
        self.show_info()
        print(f"disease: {self.disease}")
        print(f"Consultation fee: {self.room_number}")
        
# child class of doctor by multi-level inheritance
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgery_type):
        super().__init__(name, age, gender, specialization, consultation_fee)
        self.surgery_type=surgery_type
        
    def perform_surgery(self):
        self.show_doc()
        print(f"Surgery type: {self.surgery_type}")
        
# Object creation and getting info
surg1 = Surgeon("Akhil",22,"Male","ENT","100000","Minor")
surg1.perform_surgery()

# Output
# Name: Akhil
# Age: 22
# Gender: Male
# Specialization: ENT
# Consultation fee: 100000
# Surgery type: Minor