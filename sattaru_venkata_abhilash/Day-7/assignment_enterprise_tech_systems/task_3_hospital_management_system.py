# Task 3 — Hospital Management System
# Domain: Healthcare IT

# Base class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Derived class - Doctor
class Doctor(Person):
    def __init__(self, name, age, gender, specialization, consultation_fee):
        Person.__init__(self, name, age, gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee

# Derived class - Patient
class Patient(Person):
    def __init__(self, name, age, gender, disease, room_number):
        Person.__init__(self, name, age, gender)
        self.disease = disease
        self.room_number = room_number

# Multilevel inheritance - Surgeon inherits from Doctor
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        Doctor.__init__(self, name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type

    def perform_surgery(self):
        print(f"Surgeon Name: {self.name}")
        print(f"Surgeon Age: {self.age}")
        print(f"Surgeon Gender: {self.gender}")
        print(f"Specialization: {self.specialization}")
        print(f"Surgery Type: {self.surgery_type}")
        print(f"Consultation Fee: ₹{self.consultation_fee}")
        print("-" * 40)

# Doctor objects
doctor1 = Doctor("Dr. Meera", 40, "F", "Cardiologist", 1500)
doctor2 = Doctor("Dr. Shakeel", 38, "M", "Dermatologist", 1200)

# Patient objects
patient1 = Patient("Abhi", 25, "M", "Heart Disease", 204)
patient2 = Patient("Vikas", 28, "M", "Skin Allergy", 105)
patient3 = Patient("Niranjan", 30, "M", "Fever", 307)

# Surgeon objects
surgeon1 = Surgeon("Dr. Sai", 45, "M", "Neurosurgeon", 2500, "Brain Tumor Removal")
surgeon2 = Surgeon("Dr. SRK", 42, "F", "ENT", 1500, "Eye Surgery")

# Display surgeon details
print("\n--- Surgeon Details ---")
surgeon1.perform_surgery()
surgeon2.perform_surgery()


# Sample Output:
# --- Surgeon Details ---
# Surgeon Name: Dr. Sai
# Surgeon Age: 45
# Surgeon Gender: M
# Specialization: Neurosurgeon
# Surgery Type: Brain Tumor Removal
# Consultation Fee: ₹2500
# ----------------------------------------
# Surgeon Name: Dr. SRK
# Surgeon Age: 42
# Surgeon Gender: F
# Specialization: ENT
# Surgery Type: Eye Surgery
# Consultation Fee: ₹1500
# ----------------------------------------
