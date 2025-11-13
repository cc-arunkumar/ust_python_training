#Creating a class Person with the required attributes.
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

#Creating a class Doctor and Inheriting the properties of class Person in it.
class Doctor(Person):
    def __init__(self, name, age, gender, specialization, consultationfee):
        self.specialization = specialization
        self.consultationfee = consultationfee
        super().__init__(name, age, gender)
    
    def display_info(self):
        super().display_info()
        print(f"Specialization: {self.specialization}")
        print(f"Consultation Fee: {self.consultationfee}")


#Creating a class Patient and Inheriting the properties of Person in it.
class Patient(Person):
    def __init__(self, name, age, gender, disease, room_no):
        self.disease = disease
        self.room_no = room_no
        super().__init__(name, age, gender)
    
    def display_info(self):
        super().display_info()
        print(f"Disease: {self.disease}")
        print(f"Room Number: {self.room_number}")

#Creating a class Surgeon and Inheriting the properties of Doctor in it.
class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultationfee, surgery_type):
        self.surgery_type = surgery_type
        super().__init__(name, age, gender, specialization, consultationfee)

    def perform_surgery(self):
            print(f"Performing {self.surgery_type} surgery.")
        
    def display_info(self):
            super().display_info()
            print(f"Surgery Type: {self.surgery_type}")

#Example Values:
surgeon = Surgeon("Dr. Meera Iyer", 45, "Female", "Orthopadic", 15000, "Knee Replacement")
surgeon.display_info()
surgeon.perform_surgery()

print("------------------------------------------------------------------------")

surgeon = Surgeon("Dr. Ranjit Dash", 55, "Male", "Cardiac", 125000, "Heart Bypass")
surgeon.display_info()
surgeon.perform_surgery()

print("---------------------------------------------------------------------------")


#Console Output:
# Name: Dr. Meera Iyer
# Age: 45
# Gender: Female
# Specialization: Orthopadic
# Consultation Fee: 15000
# Surgery Type: Knee Replacement
# Performing Knee Replacement surgery.
# ------------------------------------------------------------------------
# Name: Dr. Ranjit Dash
# Age: 55
# Gender: Male
# Specialization: Cardiac
# Consultation Fee: 125000
# Surgery Type: Heart Bypass
# Performing Heart Bypass surgery.
# ---------------------------------------------------------------------------