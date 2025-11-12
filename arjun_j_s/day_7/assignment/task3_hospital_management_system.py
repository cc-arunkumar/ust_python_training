#Task 3 — Hospital Management System
# Business Requirement:
# UST Healthcare division needs a mini module to handle hospital roles.
# 1. Every Person has:
# name , age , gender
# 2. Doctor and Patient both inherit from Person, but have different fields:
# Doctor → specialization , consultation_fee
# Patient → disease , room_number
# 3. The hospital wants to extend Doctor to include Surgeon (with surgery_type and 
# perform_surgery() ).
# Task: Design this in such a way that code duplication is minimized and every
# class inherits logically.
# print complete details for a Surgeon (name, specialization, surgery_type,etc.)

#Main class
class Person:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")

#Sub-class
class Doctor(Person):

    def __init__(self, name, age, gender,specialization , consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def show_doctor(self):
        self.show_info()
        print(f"Specialization : {self.specialization}")
        print(f"Consultation Fee : {self.consultation_fee}")

#Sub-class
class Patient(Person):

    def __init__(self, name, age, gender, disease, room_no):
        Person.__init__(self,name, age, gender)
        self.disease = disease
        self.room_no = room_no

    def show_doctor(self):
        self.show_info()
        print(f"Disease : {self.disease}")
        print(f"Room No : {self.room_no}")

#Sub-class
class Surgeon(Doctor):

    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        super().__init__(name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type

    def perform_surgery(self):
        self.show_doctor()
        print(f"Surgery Type : {self.surgery_type}")

#Creating the object    
surgeon = Surgeon("Arjun",23,"Male","Ortho",1000,"Severe")
surgeon.perform_surgery()

#Output
# Name : Arjun
# Age : 23
# Gender : Male
# Specialization : Ortho       
# Consultation Fee : 1000      
# Surgery Type : Severe  