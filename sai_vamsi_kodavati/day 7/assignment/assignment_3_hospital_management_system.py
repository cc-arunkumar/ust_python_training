# assignment_3_hospital_management_system

# Every Person has: name , age , gender
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

# 2.Doctor and Patient both inherit from Person, but have different fields:
# Doctor → specialization , consultation_fee
# Patient → disease , room_number


# Doctor class inherits from Person
class Doctor(Person):
    def __init__(self,name,age,gender,specialization,consultation_fee):
        Person.__init__(self,name,age,gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee

# Patient class inherits from Person
class Patient(Person):
    def __init__(self, name, age, gender,disease,room_number):
        Person.__init__(self,name, age, gender)
        self.disease = disease
        self.room_number = room_number

# 3.The hospital wants to extend Doctor to include Surgeon (with surgery_type and perform_surgery() ).

# Surgeon class inherits from Doctor
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgery_type):
        Doctor.__init__(self,name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type
        
    def perform_surgery(self):
        print(f"Name:{self.name}")
        print(f"age:{self.age}")
        print(f"gender:{self.gender}")
        print(f"Specialization:{self.specialization}")
        print(f"Consultation Fee:{self.consultation_fee}")
        print(f"Surgery_Type:{self.surgery_type}")


# Surgeon object
surgeon1 = Surgeon("Dr.Vijay", 40, "Male", "Neurosurgeon", 2500, "Brain Surgery")
surgeon1.perform_surgery()


# -------------------------------------------------------------------------------------------------

# Sample Output

# Name:Dr.Vijay
# age:40
# gender:Male
# Specialization:Neurosurgeon
# Consultation Fee:2500
# Surgery_Type:Brain Surgery
