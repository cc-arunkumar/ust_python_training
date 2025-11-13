# Task 3 — Hospital Management System
#  Domain: Healthcare IT
#  Business Requirement:
#  UST Healthcare division needs a mini module to handle hospital roles.
#  Every Person has:
# name , 
# age , 
# gender
#  
#   Doctor and Patient both inherit from Person, but have different fields:
#  Doctor → 
# specialization , 
# consultation_fee
#  Patient → 
# disease , 
# room_number
#  The hospital wants to extend Doctor to include Surgeon (with surgery_type and perform_surgery() )


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


class Doctor(Person):
    def __init__(self, name, age, gender, specialization, consultation_fee):
        Person.__init__(self, name, age, gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def show_doctor_info(self):
        self.show_person_info()
        print(f"Specialization: {self.specialization}, Consultation Fee: ₹{self.consultation_fee}")


class Patient(Person):
    def __init__(self, name, age, gender, disease, room_number):
        Person.__init__(self, name, age, gender)
        self.disease = disease
        self.room_number = room_number

    def show_patient_info(self):
        self.show_person_info()
        print(f"Disease: {self.disease}, Room Number: {self.room_number}")


class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        Doctor.__init__(self, name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type

    def perform_surgery(self):
        print(f"{self.name} is performing a {self.surgery_type} surgery.")

    def show_surgeon_info(self):
        self.show_doctor_info()
        print(f"Surgery Type: {self.surgery_type}")
        

surgeon = Surgeon(
    name="Dr. Sonia",
    age=40,
    gender="Female",
    specialization="Cardiothoracic Surgery",
    consultation_fee=1500,
    surgery_type="Open Heart"
)


surgeon.show_surgeon_info()
surgeon.perform_surgery()

# Output
# Name: Dr. Sonia, Age: 40, Gender: Female
# Specialization: Cardiothoracic Surgery, Consultation Fee: ₹1500
# Surgery Type: Open Heart
# Dr. Sonia is performing a Open Heart surgery.