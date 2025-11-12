# Task 2 — Autonomous Vehicle System
# Domain: Automotive / AI
# Business Requirement:
# UST Mobility is building an AI vehicle platform.
# 1. Every Vehicle must have:
# make , model , year
# Method: show_info()
# 2. Every ElectricVehicle should have:
# battery_capacity , charge_status
# Method: charge_battery()
# 3. Every AutonomousVehicle should have:
# ai_version , run_autopilot()
# 4. The company wants to create a class SmartEV — a self-driving electric
# vehicle.

# Creating Parent Class Vehicle:

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        
    def show_info(self):
        print(f"Manufacture: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year of Manufacturing: {self.year}")
        
# ElectricVehicle extends Vehicle
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status):
        Vehicle.__init__(self,make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status
    
    def charge_battery(self):
        print(f"Charge Capacity: {self.battery_capacity}")
        print(f"Charging Status: {self.charge_status}")
       
# AutonomousVehicle extends ElectricVehicle 
class AutonomousVehicle(ElectricVehicle):
    def __init__(self, make, model, year, battery_capacity,charge_status,ai_version):
        ElectricVehicle.__init__(self,make,model,year,battery_capacity,charge_status)
        self.ai_version = ai_version
        self.model = model
        
    def run_autopilot(self):
        print(f"{self.model} has {self.ai_version}")
      
# SmartEv extends AutonomousVehicle  
class SmartEv(AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        AutonomousVehicle.__init__(self,make, model, year, battery_capacity, charge_status, ai_version)
        
        
# Creating objects for all classes
vehicle = Vehicle("BMW","I4","2023")
ev = ElectricVehicle("BMW","I4","2023","83%",100)
av = AutonomousVehicle("BMW","I4","2023","Charging","Co pilot")
smartev = SmartEv("BMW","I4","2023","85%",100,"Co pilot")
smartev.show_info()
smartev.charge_battery()
smartev.run_autopilot()

# output

# Manufacture: BMW
# Model: I4
# Year of Manufacturing: 2023
# Charge Capacity: 85%
# Charging Status: 100
# I4 has Co pilot