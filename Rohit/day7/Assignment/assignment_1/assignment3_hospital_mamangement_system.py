#Task 3 Hospital Management System
#Create parent class Person
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
#Create child class Doctor
class Doctor(Person):
    def __init__(self, name, age, gender,specialization,consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee
#Create Child class Patient
class Patient(Person):
    def __init__(self, name, age, gender,disease,room_number):
        Person.__init__(name, age, gender)
        self.disease=disease
        self.room_number=room_number
        
#Create child class Surgeon derive from Doctor class
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgery_type):
        Doctor.__init__(self,name, age, gender, specialization, consultation_fee)
        self.surgery_type=surgery_type
    def perform_surgery(self,status):
        if(status=="Yes"):
            print("Availability: ",status)
        else:
            print("No Surgeon Available")
    def details(self):
        print("Surgeon name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)
        print("Specialization: ",self.specialization)
        print("Consultation Fee: ",self.consultation_fee)
        print("Surgery type: ",self.surgery_type)
surgeon=Surgeon("Raj",45,"Male","Cancer",320000,"Heart")
surgeon.perform_surgery("Yes")
surgeon.details()

#====================Sample output=================
# Availability:  Yes
# Surgeon name:  Raj
# Age:  45
# Gender:  Male
# Specialization:  Cancer
# Consultation Fee:  320000
# Surgery type:  Heart