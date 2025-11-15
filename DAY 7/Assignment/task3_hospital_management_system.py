"""
print complete details for a Surgeon (name, specialization, surgery_type, etc.)
"""

# Base class representing a general person
class Person:
    def __init__(self, name, age, gender):
        self.name = name      # Person's name
        self.age = age        # Person's age
        self.gender = gender  # Person's gender


# Doctor class inherits from Person
# Adds specialization and consultation fee
class Doctor(Person):
    def __init__(self, name, age, gender, specialization, consultation_fee):
        Person.__init__(self, name, age, gender)  # Initialize Person attributes
        self.specialization = specialization     # Doctor's specialization
        self.consultation_fee = consultation_fee # Consultation fee of the doctor
    
    # Display doctor details
    def doctor_details(self):
        print(f"Doctor Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Specialization: {self.specialization}")
        print(f"Fee: {self.consultation_fee}")


# Patient class inherits from Person
# Adds disease and room number attributes
class Patient(Person):
    def __init__(self, name, age, gender, disease, room_number):
        Person.__init__(self, name, age, gender)  # Initialize Person attributes
        self.disease = disease                     # Patient's disease
        self.room_number = room_number             # Assigned room number
    
    # Display patient details
    def patient_details(self):
        print(f"Patient Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Disease: {self.disease}")
        print(f"Room Number: {self.room_number}")


# Surgeon class inherits from Doctor
# Adds surgery-specific attributes and behavior
class Surgeon(Doctor):
    def __init__(self, name, age, specialization, surgery_type):
        Person.__init__(self, name, age, gender="") # Surgeon is also a person
        self.specialization = specialization        # Surgeon specialization
        self.surgery_type = surgery_type            # Type of surgery performed
    
    # Method to perform surgery
    def perform_surgery(self):
        print(f"{self.surgery_type} is performed by Dr.{self.name} ({self.age}) specialized in {self.specialization}")


# Example usage

print("---Doctor Details---")
d1 = Doctor("Arun", 45, "Male", "MBBS", 1000)
d1.doctor_details()  # Display doctor info


print("---Patient Details---")
p1 = Patient("Madhan", 24, "Male", "Fever", 18)
p1.patient_details()  # Display patient info


print("---Surgeon Details---")
s1 = Surgeon("Aved", 22, "Cardiologist", "Heart Operation")
s1.perform_surgery()  # Display surgeon info

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