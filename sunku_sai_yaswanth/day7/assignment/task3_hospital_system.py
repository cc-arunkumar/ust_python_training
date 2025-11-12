# Task 3 — Hospital Management System
# Domain: Healthcare IT
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
# �� print complete details for a Surgeon (name, specialization, surgery_type,
# etc.)

class Person:
    def __init__(self,name , age , gender):
        self.name=name
        self.age=age
        self.gender=gender
class Doctor(Person):
    def __init__(self, name, age, gender ,specialization , consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee
class  Patient(Person):
    def __init__(self, name, age, gender,disease , room_number):
        Person.__init__(self,name, age, gender)
        self.disease=disease
        self.room_number=room_number
class  Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgary_type):
        Doctor.__init__(self,name, age, gender, specialization, consultation_fee)
        self.surgary_type=surgary_type

    def perform_surgery(self):
        print(f"surgen_name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender: {self.gender}")
        print(f"specialization: {self.specialization}")
        print(f"consultation fee: {self.consultation_fee}")
        print(f"surgary_type: {self.surgary_type}")

surgen=Surgeon("nani",29,'M',"ear problem",3000,"ear")
surgen.perform_surgery()

# output    #   
# surgen_name: nani
# age: 29
# gender: M
# specialization: ear problem
# consultation fee: 3000
# surgary_type: ear