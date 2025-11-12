#Task 2 — Autonomous Vehicle System
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
# Task: Reuse as much code as possible by designing the inheritance chain
# properly.
# Think about the correct inheritance structure to achieve this

#Main class
class Vehicle:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def show_info(self):
        print(f"Make : {self.make}")
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")

#Sub-class
class ElectricVehicle(Vehicle):

    def __init__(self, make, model, year, battery_cap, charge_status):
        Vehicle.__init__(self,make, model, year)
        self.battery_cap = battery_cap
        self.charge_status = charge_status
    
    def charge_battery(self):
        self.show_info()
        print(f"Battery Capacity : {self.battery_cap}")
        print(f"Charge Status : {self.charge_status}")

#Sub-class
class AutonomousVehicle(Vehicle):

    def __init__(self, make, model, year, ai_version):
        Vehicle.__init__(self,make, model, year)
        self.ai_version = ai_version
    
    def run_autopiolt(self):
        self.show_info()
        print(f"AI Version : {self.ai_version}")

#Sub-class
class SmartEV(ElectricVehicle,AutonomousVehicle):

    def __init__(self, make, model, year, battery_cap, charge_status, ai_version):
        ElectricVehicle.__init__(self,make, model, year, battery_cap, charge_status)
        AutonomousVehicle.__init__(self,make, model, year, ai_version)

    def show(self):
        self.show_info()
        print(f"Battery Capacity : {self.battery_cap}")
        print(f"Charge Status : {self.charge_status}")
        print(f"AI Version : {self.ai_version}")

#Creating the object
smart_ev = SmartEV("BMW","i3",2018,"100%","Full",2.10)
smart_ev.show()

#Output
# Make : BMW
# Model : M4
# Year : 2018
# Battery Capacity : 100%
# Charge Status : Full   
# AI Version : 2.1