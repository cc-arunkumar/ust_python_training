"""
print complete details for a Surgeon (name, specialization, surgery_type, etc.)
"""

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
# Inheriting From the Person Class
class Doctor(Person):
    def __init__(self, name, age, gender,specialization , consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization =specialization
        self.consultation_fee=consultation_fee
    
    def doctor_details(self):
        print(f"Doctor name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Specialization: {self.specialization}")
        print(f"Fee: {self.consultation_fee}")

# Inheriting From the Person Class
class Patient(Person):
    def __init__(self, name, age, gender,disease,room_number):
        Person.__init__(self,name, age, gender)
        self.disease=disease
        self.room_number=room_number

    def patient_details(self):
        print(f"PAient Name :{self.name}")
        print(f"Age :{self.age}")
        print(f"Gender :{self.gender}")
        print(f"Disease :{self.disease}")
        print(f"Room Number :{self.room_number}")

# Inheriting From the Doctor Class
class Surgeon(Doctor):
    def __init__(self, name, age, specialization, surgery_type):
        Person.__init__(self, name, age,gender="" )
        self.surgery_type=surgery_type
        self.specialization=specialization

    def perform_surgery(self):
        print(f"{self.surgery_type} id Performed by Dr.{self.name} ({self.age})Specialized in {self.specialization}")


print("---Doctor Details---")
# Doctor name, age, gender,disease,room_number
d1=Doctor("Arun",45,"Male","MBBS",1000)
d1.doctor_details()


print("---Patient Details---")
# PAtient details
p1=Patient("Madhan",24,"Male","Fever",18)
p1.patient_details()


print("---Surgeon Details---")
#Surgeon Details
s1=Surgeon("Aved",22,"Cardiologist","Heart Operation")
s1.perform_surgery()

"""
SAMPLE OUTPUT

---Doctor Details---
Doctor name: Arun
Age: 45
Specialization: MBBS
Fee: 1000
---Patient Details---
PAient Name :Madhan
Age :24
Gender :Male
Disease :Fever
Room Number :18
---Surgeon Details---
Heart Operation id Performed by Dr.Aved (22)Specialized in Cardiologist

"""