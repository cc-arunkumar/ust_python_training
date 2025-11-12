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


# 1. Every Person has:
# Enterprise Tech Systems – Inheritance Design Challenge 2 
# name , age , gender
class Person:
    def __init__(self,name , age , gender):
        self.name=name
        self.age=age
        self.gender=gender
    


# 2. Doctor and Patient both inherit from Person, but have different fields:
# Doctor → specialization , consultation_fee

class Doctor(Person):
    def __init__(self, name, age, gender,specialization , consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee

# Patient → disease , room_number
class Patient(Person):
    def __init__(self, name, age, gender,disease , room_number):
        Person.__init__(self,name, age, gender)
        self.disease=disease 
        self.room_number=room_number

# 3. The hospital wants to extend Doctor to include Surgeon (with surgery_type and perform_surgery() ).
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgery_type):
        Doctor.__init__(self,name, age, gender, specialization, consultation_fee)
        self.surgery_type=surgery_type
    
    def perform_surgery(self):
        print(f"Surgeon name: {self.name}")
        print(f"Surgeon age:{self.age}")
        print(f"Surgeon gender:{self.gender}")
        print(f"Surgeon Specialization: {self.specialization}")
        print(f"Surgery type:{self.surgery_type}")
        print(f"Cunsultation fee:{self.consultation_fee}")


doctor1=Surgeon("SRK",23,"M","ENT",150,"Eye sight")

doctor1.perform_surgery()


# Sample output

# Surgeon name: SRK
# Surgeon age:23
# Surgeon gender:M
# Surgeon Specialization: ENT
# Surgery type:Eye sight
# Cunsultation fee:150