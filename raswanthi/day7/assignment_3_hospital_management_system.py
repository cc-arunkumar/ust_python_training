#Assignment 3: Hospital Management System using Inheritance

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print(f"Name: {self.name} | Age: {self.age} | Gender: {self.gender}")


class Doctor(Person):
    def __init__(self, name, age, gender, specialization, consultation_fee):
        super().__init__(name, age, gender)
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def show_doctor_info(self):
        self.show_info()
        print(f"Specialization: {self.specialization} | Consultation Fee: ₹{self.consultation_fee}")


class Patient(Person):
    def __init__(self, name, age, gender, disease, room_number):
        super().__init__(name, age, gender)
        self.disease = disease
        self.room_number = room_number

    def show_patient_info(self):
        self.show_info()
        print(f"Disease: {self.disease} | Room Number: {self.room_number}")


class Surgeon(Doctor):
    def __init__(self, name, age, gender, specialization, consultation_fee, surgery_type):
        super().__init__(name, age, gender, specialization, consultation_fee)
        self.surgery_type = surgery_type

    def perform_surgery(self):
        print(f"{self.name} is performing a {self.surgery_type} surgery.")

    def show_surgeon_info(self):
        self.show_doctor_info()
        print(f"Surgery Type=> {self.surgery_type}")

doc1 = Doctor("Dr. Ravi",45, "Male", "Orthopedics", 1200)
doc1.show_doctor_info()
print("---------------------------------------")

pat1 = Patient("Kumar", 60, "Male", "Diabetes", "Room 101")
pat2=Patient("Meera",35,"Female","Diabetes","Room 102")
pat1.show_patient_info()
pat2.show_patient_info()
print("---------------------------------------")

surgeon1 = Surgeon("Dr. Tara", 45, "Female", "Cardiology", 1500, "Bypass")
surgeon1.show_surgeon_info()
surgeon1.perform_surgery()
print("---------------------------------------")

'''output:
Name: Dr. Ravi | Age: 45 | Gender: Male
Specialization: Orthopedics | Consultation Fee: ₹1200
---------------------------------------
Name: Kumar | Age: 60 | Gender: Male
Disease: Diabetes | Room Number: Room 101
Name: Meera | Age: 35 | Gender: Female
Disease: Diabetes | Room Number: Room 102
---------------------------------------
Name: Dr. Tara | Age: 45 | Gender: Female
Specialization: Cardiology | Consultation Fee: ₹1500
Surgery Type=> Bypass
Dr. Tara is performing a Bypass surgery.
'''