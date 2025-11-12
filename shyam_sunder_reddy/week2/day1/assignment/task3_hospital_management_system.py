# Task 3 — Hospital Management System
# Domain: Healthcare IT
# Business Requirement:
# UST Healthcare division needs a mini module to handle hospital roles.
# 1. Every Person has:
# Enterprise Tech Systems – Inheritance Design Challenge 2
# name , age , gender
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    
    def show_info(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)

# 2. Doctor and Patient both inherit from Person, but have different fields:
# Doctor → specialization , consultation_fee
class Doctor(Person):
    def __init__(self,name,age,gender,specialization,consultation_fee):
        super().__init__(name,age,gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee
   
# Patient → disease , room_number
class Patient(Person):
    def __init__(self,name,age,gender,disease,room_number):
        super().__init__(name,age,gender)
        self.disease=disease
        self.room_number=room_number

# 3. The hospital wants to extend Doctor to include Surgeon (with surgery_type and 
# perform_surgery() ).
class Surgon(Doctor):
    def __init__(self,name,age,gender,specialization,consultation_fee,surgery_type):
        super().__init__(name,age,gender,specialization,consultation_fee)
        self.surgery_type=surgery_type
    
    def perform_surgery(self):
        print("Specialization: ",self.specialization,"| Sugery Type",self.surgery_type)
        print("Performin surgery")

per1=Person("shyam",21,"Male")
per1.show_info()
print("-----------------------")

per2=Doctor("Ram",22,"Male","Heart",5000)
per2.show_info()
print("-----------------------")

per3=Patient("Anjan",34,"Female","Rabise",704)
per3.show_info()
print("-----------------------")

per4=Surgon("Mahes",70,"Male","Brain",90000,"Hemogloben")
per4.show_info()
per4.perform_surgery()
print("-----------------------")

#Sample Output
# Name:  shyam
# Age:  21
# Gender:  Male
# -----------------------
# Name:  Ram
# Age:  22
# Gender:  Male
# -----------------------
# Name:  Anjan
# Age:  34
# Gender:  Female
# -----------------------
# Name:  Mahes
# Age:  70
# Gender:  Male
#Gender:  Male
# Specialization:  Brain | Sugery Type Hemogloben
# Performin surgery
# -----------------------
