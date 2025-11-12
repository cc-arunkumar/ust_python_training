#Task 3 : Hospital Management System 

#Code 
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
#Making child class
class Doctor(Person):
    def __init__(self, name, age, gender,specialization,consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee
            
class Patient(Person):
    def __init__(self, name, age, gender,disease,room_number):
        Person.__init__(self,name, age, gender)
        self.disease=disease
        self.room_number=room_number

class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgery_type):
        Doctor.__init__(self,name, age, gender, specialization, consultation_fee)
        self.surgery_type=surgery_type
    def perform_surgery(self):
        print(f"Name of the Surgeon : {self.name}")
        print(f"Specialization : {self.specialization}")
        print(f"{self.surgery_type} was performed by the surgeon ")
        print(f"Consultation fees is : {self.consultation_fee}")

sur1=Surgeon("Monalisa",25,"female","Heart-Specialist",500, "Heart-surgery")
sur1.perform_surgery()

#output
# Name of the Surgeon : Monalisa
# Specialization : Heart-Specialist
# Heart-surgery was performed by the surgeon 
# Consultation fees is : 500

        