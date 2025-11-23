# Task 3 — Hospital Management System
# Domain: Healthcare IT
# Business Requirement:
# UST Healthcare division needs a mini module to handle hospital roles.
# Task: Design this in such a way that code duplication is minimized and every
# class inherits logically.
# print complete details for a Surgeon (name, specialization, surgery_type,
# etc.)

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
    def __init__(self, name, age, gender,specialization,consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee

# Patient → disease , room_number
class Patient(Person):
    def __init__(self, name, age, gender,disease,room_number):
        Patient.__init__(self,name, age, gender)
        self.disease=disease
        self.room_number=room_number

# 3. The hospital wants to extend Doctor to include Surgeon (with surgery_type and 
# perform_surgery() ).
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgery_type):
        Doctor.__init__(self,name, age, gender, specialization, consultation_fee)
        self.surgery_type=surgery_type

    def perform_surgery(self):
        if self.surgery_type==self.specialization:
            print(f"Doctor Name:{self.name}")
            print(f"Doctor Age:{self.age}")
            print(f"Doctor Gender:{self.gender}")
            print(f"Doctor Specialization:{self.specialization}")
            print(f"Doctor {self.name} will perfome the {self.surgery_type} surgery")
        else:
            print("looking for the best surgen")

dr_surgen=Surgeon("David Livingstone",28,"Male","Heart",800,"Heart")
dr_surgen.perform_surgery()

# sample output:
# Doctor Name:David Livingstone
# Doctor Age:28
# Doctor Gender:Male
# Doctor Specialization:Heart
# Doctor David Livingstone will perfome the Heart surgery
    