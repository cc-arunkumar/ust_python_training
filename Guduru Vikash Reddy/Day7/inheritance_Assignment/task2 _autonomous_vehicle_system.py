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
# ⚙️ Task: Reuse as much code as possible by designing the inheritance chain
# properly.
# Think about the correct inheritance structure to achieve this.
# Step 1: Define a base class for all vehicles
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def show_info(self):
        print(f"make:",self.make)
        print(f"model:",self.model)
        print(f"year:",self.year)

# Step 2: Create a subclass for electric vehicles with battery-specific attributes
class ElectricVehicle(Vehicle):
    def __init__(self,make,model,year,battery_capacity,charge_status):
        Vehicle.__init__(self,make,model,year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status
    def  charge_battery(self):
        print(f"Battery capacity:",self.battery_capacity,"\ncharge status:",self.charge_status)

# Step 3: Create a subclass for autonomous vehicles with AI-specific attributes
class  AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year,ai_version):
        Vehicle.__init__(self, make, model, year)
        self.ai_version=ai_version
    def run_autopilot(self):
        print(f"ai version is running:",self.ai_version)

# Step 4: Combine electric and autonomous features into a SmartEv class using multiple inheritance
class SmartEv(ElectricVehicle,AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status,ai_version):
        ElectricVehicle.__init__(self,make,model,year,battery_capacity,charge_status)
        AutonomousVehicle.__init__(self,make,model,year,ai_version)

# Step 5: Instantiate a regular vehicle and display its info
vehicle=Vehicle("toyota","fortuner",2025)
vehicle.show_info()

# Step 6: Instantiate an electric vehicle and show battery status
vehicle1=ElectricVehicle("swift","maruti",2024,"2000mah","3hours")
vehicle1.charge_battery()

# Step 7: Instantiate an autonomous vehicle and run autopilot
vehicle2=AutonomousVehicle("Bmw","topend",2024,9)
vehicle2.run_autopilot()
# sample output
# make: toyota
# model: fortuner
# year: 2025
# Battery capacity: 2000mah
# charge status: 3hours
# ai version is running: 9
        
        
