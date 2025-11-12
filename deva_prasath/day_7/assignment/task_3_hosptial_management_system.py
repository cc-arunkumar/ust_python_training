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



# Person class to store general details of a person
class Person:
    def __init__(self, name, age, gender):
        self.name = name  # Person's name
        self.age = age    # Person's age
        self.gender = gender  # Person's gender
    
    def show(self):
        # Display person's details
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")

# Doctor class inherits from Person, adds doctor specific attributes
class Doctor(Person):
    def __init__(self, name, age, gender, specialisation, consultation_fee):
        Person.__init__(self, name, age, gender)  # Inherit from Person
        self.specialisation = specialisation  # Doctor's specialisation
        self.consultation_fee = consultation_fee  # Consultation fee
    
    def doc_show(self):
        # Display doctor's specialisation and consultation fee
        print(f"Speciality is {self.specialisation}")
        print(f"Consultation fee is {self.consultation_fee}")

# Patient class inherits from Person, adds patient specific attributes
class Patient(Person):
    def __init__(self, name, age, gender, disease, room_number):
        Person.__init__(self, name, age, gender)  # Inherit from Person
        self.disease = disease  # Patient's disease
        self.room_number = room_number  # Patient's room number
    
    def pat_show(self):
        # Display patient's disease and room number
        print(f"Disease is {self.disease}")
        print(f"Room number is {self.room_number}")

# Surgeon class inherits from Doctor, adds surgery related attributes
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialisation, consultation_fee, surgery_type):
        Doctor.__init__(self, name, age, gender, specialisation, consultation_fee)  # Inherit from Doctor
        self.surgery_type = surgery_type  # Type of surgery the surgeon performs
    
    def perform_surgery(self):
        # Display surgeon details and surgery type
        print(f"The surgeon name is {self.name}")
        print(f"The surgeon age is {self.age}")
        print(f"The surgeon gender is {self.gender}")
        print(f"The surgeon specialisation is {self.specialisation}")
        print(f"The surgeon consultation fee is {self.consultation_fee}")
        print(f"The surgery type is {self.surgery_type}")

# Object creation and method calls
d1 = Doctor("Varun", 35, "Male", "Dermatology", 1000)  # Create Doctor object
d1.show()  # Display Doctor details
d1.doc_show()  # Display Doctor speciality and consultation fee
print("-----------------------------------------")
p1 = Patient("Gokul", 30, "Male", "Cancer", 200)  # Create Patient object
p1.show()  # Display Patient details
p1.pat_show()  # Display Patient's disease and room number
print("-----------------------------------------")
s1 = Surgeon("Raj", 40, "Male", "Cardiology", 2000, "Open-heart-surgery")  # Create Surgeon object
s1.perform_surgery()  # Display Surgeon details and perform surgery



#Sample output
# The surgeon name is Raj
# Name:Varun
# Age:35
# Gender:Male
# Speciality is Dermatology
# Consultation fee is 1000
# -----------------------------------------
# Name:Gokul
# Age:30
# Gender:Male
# Disease is Cancer
# Room number is 200
# -----------------------------------------
# The surgeon name is Raj
# The surgeon age is 40
# The surgeon gender is Male
# The surgeon specialisation is Cardiology
# The surgeon consulation fee is 2000
# The surgery type is Open-heart-surgery


        