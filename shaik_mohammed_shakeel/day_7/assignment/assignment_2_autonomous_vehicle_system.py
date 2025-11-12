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

# Base class representing a general vehicle
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    # Method to display basic vehicle details
    def show_info(self):
        print(f"Vehicle Company: {self.make}")
        print(f"Vehicle Model: {self.model}")
        print(f"Vehicle Year: {self.year}")

# Subclass for Electric Vehicles, inherits from Vehicle

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year,battery_capacity,charge_status):
        Vehicle.__init__(self,make, model, year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status

    def charge_battery(self):
        print(f"Battery Capacity is {self.battery_capacity} and status is {self.charge_status}")


# Subclass for Autonomous Vehicles, inherits from Vehicle

class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year,ai_version):
        Vehicle.__init__(self,make, model, year)
        self.ai_version=ai_version
    def run_autopilot(self):
        print(f"Autopilot version {self.ai_version} is running:")

# Multiple inheritance: SmartEV inherits from both ElectricVehicle and AutonomousVehicle

class SmartEV(ElectricVehicle, AutonomousVehicle):
    def __init__(self,make, model, year,battery_capacity,charge_status,ai_version):
        ElectricVehicle.__init__(self, make, model, year,battery_capacity,charge_status)
        AutonomousVehicle.__init__(self, make, model, year,ai_version)

#Creating Object

vehicle1=Vehicle("Toyota","Fortuner",2022)
vehicle2=ElectricVehicle("Ford","Endevour",2021,70,"Plugged")
Vehicle3=AutonomousVehicle("Hyundai","creta",2023,101.00)
vehicle4=SmartEV("Tata","Nexon",2025,100,"Charging",101.77)

# Displaying information and calling class-specific methods

vehicle1.show_info()
vehicle2.charge_battery()
Vehicle3.run_autopilot()
vehicle4.run_autopilot()
print()


#sample output
# Vehicle Company: Toyota
# Vehicle Model: Fortuner
# Vehicle Year: 2022
# Battery Capacity is 70 and status is Plugged
# Autopilot version 101.0 is running:
# Autopilot version 101.77 is running:
    
