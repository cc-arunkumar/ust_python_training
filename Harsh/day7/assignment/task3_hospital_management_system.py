class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
        
class Doctor(Person):
    def __init__(self, name, age, gender,specialization,consultation_fee):
        Person.__init__(self,name, age, gender)
        self.specialization=specialization
        self.consultation_fee=consultation_fee
        
    def display(self):
        super().display()
        print(f"Specialization:{self.specialization}, Consultation_fee:{self.consultation_fee}")
        
class Patient(Person):
    def __init__(self, name, age, gender,disease,room_number):
        Person.__init__(self,name, age, gender)
        self.room_number=room_number
        self.disease=disease
    
    def display(self):
        super().display()
        print(f"Disease: {self.disease}, Room Number: {self.room_number}")
        
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        Doctor.__init__(self,name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type

    def perform_surgery(self):
        print(f"Performing {self.surgery_type} surgery.")

    def display(self):
        super().display()
        print( f"Surgery Type: {self.surgery_type}")
        
s1=Surgeon("Dr. Jaiswal",30,"Male","Cardiology",10000,"HeartBypass")
s2 = Surgeon("Dr. Sharma", 50, "Female", "Neurology", 7000, "Brain Tumor Removal")
s3 = Surgeon("Dr. Khan", 38, "Male", "Orthopedics", 4500, "Knee Replacement")
print("------------------------------------------")
s1.display()
s1.perform_surgery()
print("------------------------------------------")
s2.display()
s2.perform_surgery()
print("------------------------------------------")
s3.display()
s3.perform_surgery()
print("------------------------------------------")
    
# ------------------------------------------
# Name: Dr. Jaiswal, Age: 30, Gender: Male
# Specialization:Cardiology, Consultation_fee:10000
# Surgery Type: HeartBypass
# Performing HeartBypass surgery.
# ------------------------------------------
# Name: Dr. Sharma, Age: 50, Gender: Female
# Specialization:Neurology, Consultation_fee:7000
# Surgery Type: Brain Tumor Removal
# Performing Brain Tumor Removal surgery.
# ------------------------------------------
# Name: Dr. Khan, Age: 38, Gender: Male
# Specialization:Orthopedics, Consultation_fee:4500
# Surgery Type: Knee Replacement
# Performing Knee Replacement surgery.
# ------------------------------------------

