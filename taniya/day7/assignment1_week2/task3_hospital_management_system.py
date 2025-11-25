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


# Define a base class Person
class Person:
    # Constructor to initialize person attributes
    def __init__(self, name, age, gender):
        self.name = name      # Person's name
        self.age = age        # Person's age
        self.gender = gender  # Person's gender

    # Method to display person information
    def show_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


# Define Doctor class that inherits from Person
class Doctor(Person):
    # Constructor to initialize doctor attributes
    def __init__(self, name, age, gender, specialization, consultation_fee):
        # Call Person constructor
        Person.__init__(self, name, age, gender)
        self.specialization = specialization        # Doctor's specialization
        self.consultation_fee = consultation_fee    # Doctor's consultation fee

    # Method to display doctor information
    def show_doctor_info(self):
        # First show basic person info
        self.show_person_info()
        # Then show doctor-specific info
        print(f"Specialization: {self.specialization}, Consultation Fee: ₹{self.consultation_fee}")


# Define Patient class that inherits from Person
class Patient(Person):
    # Constructor to initialize patient attributes
    def __init__(self, name, age, gender, disease, room_number):
        # Call Person constructor
        Person.__init__(self, name, age, gender)
        self.disease = disease          # Patient's disease
        self.room_number = room_number  # Patient's room number

    # Method to display patient information
    def show_patient_info(self):
        # First show basic person info
        self.show_person_info()
        # Then show patient-specific info
        print(f"Disease: {self.disease}, Room Number: {self.room_number}")


# Define Surgeon class that inherits from Doctor
class Surgeon(Doctor):
    # Constructor to initialize surgeon attributes
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        # Call Doctor constructor
        Doctor.__init__(self, name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type   # Type of surgery performed

    # Method to perform surgery
    def perform_surgery(self):
        print(f"{self.name} is performing a {self.surgery_type} surgery.")

    # Method to display surgeon information
    def show_surgeon_info(self):
        # First show doctor info
        self.show_doctor_info()
        # Then show surgeon-specific info
        print(f"Surgery Type: {self.surgery_type}")


# -------------------------------
# Object Creation
# -------------------------------

# Create a Surgeon object with given attributes
surgeon = Surgeon(
    name="Dr. Sonia",
    age=40,
    gender="Female",
    specialization="Cardiothoracic Surgery",
    consultation_fee=1500,
    surgery_type="Open Heart"
)

# -------------------------------
# Method Calls
# -------------------------------

# Show surgeon information
surgeon.show_surgeon_info()

# Perform surgery
surgeon.perform_surgery()


# -------------------------------
# Expected Output
# -------------------------------
# Name: Dr. Sonia, Age: 40, Gender: Female
# Specialization: Cardiothoracic Surgery, Consultation Fee: ₹1500
# Surgery Type: Open Heart
# Dr. Sonia is performing a Open Heart surgery.