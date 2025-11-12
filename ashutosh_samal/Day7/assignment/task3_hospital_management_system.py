#Task 3 — Hospital Management System

#creating person class
class Person:
    def __init__(self,name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender

#creating doctor class    
class Doctor(Person):
    def __init__(self, name, age, gender,specialization , consultation_fee):
        super().__init__(name, age, gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee

#creating surgeon class
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee,surgery_type):
        super().__init__(name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type
    
    #function to print surgeon details
    def perform_surgery(self):
        print(f"Surgeon Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Specialization: {self.specialization}")
        print(f"Consultation Fees: {self.consultation_fee}")
        print(f"Surgery Type: {self.surgery_type}")

#creating patient class
class Patient(Person):
    def __init__(self, name, age, gender,disease , room_number):
        super().__init__(name, age, gender)
        self.disease = disease
        self.room_number =room_number
    
    #function to print patient details
    def patient_info(self):
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Disease: {self.disease}")
        print(f"Room Number: {self.room_number}")

patient1 = Patient("Amit",35,"Male","Heart Failure",301)
patient1.patient_info()
print("===============================")

surgeon1 = Surgeon("Deva",30,"male","Cardiology",1000,"Cardiac Surgeon")
surgeon1.perform_surgery()
print("================================")

#Sample Execution
# Patient Name: Amit
# Age: 35
# Gender: Male
# Disease: Heart Failure
# Room Number: 301
# ===============================
# Surgeon Name: Deva
# Age: 30
# Gender: male
# Specialization: Cardiology     
# Consultation Fees: 1000
# Surgery Type: Cardiac Surgeon
# ================================