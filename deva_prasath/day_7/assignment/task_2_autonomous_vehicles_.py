# Task 2 — Autonomous Vehicle System
# Domain: Automotive / AI
# Business Requirement:
# UST Mobility is building an AI vehicle platform.


# 1. Every Vehicle must have:
# make , model , year
# Method: show_info()
# Create Vehicle class

# Vehicle class to store general vehicle details
class Vehicle:
    def __init__(self, name, model, year):
        self.name = name  # Vehicle name
        self.model = model  # Vehicle model
        self.year = year  # Vehicle manufacturing year
    
    def show_info(self):
        # Display vehicle information
        print(f"The Company make is {self.name}")
        print(f"The model is {self.model}")
        print(f"The Company make is {self.year}")

# ElectricVehicle class inherits from Vehicle, adds battery related attributes
class ElectricVehicle(Vehicle):
    def __init__(self, name, model, year, battery_capacity, charge_status):
        Vehicle.__init__(self, name, model, year)  # Inherit from Vehicle
        self.battery_capacity = battery_capacity  # Battery capacity
        self.charge_status = charge_status  # Battery charge status
    
    def charge_battery(self):
        # Display battery charge status
        print(f"Battery is up to date and the status is {self.charge_status}")

# AutonomousVehicle class inherits from Vehicle, adds AI related attributes
class AutonomousVehicle(Vehicle):
    def __init__(self, name, model, year, ai_version):
        Vehicle.__init__(self, name, model, year)  # Inherit from Vehicle
        self.ai_version = ai_version  # AI version
    
    def auto_pilot(self):
        # Display autopilot version
        print(f"Autopilot is working with version {self.ai_version}")
        
# SmartEV class inherits from both ElectricVehicle and AutonomousVehicle
class SmartEV(ElectricVehicle, AutonomousVehicle):
    def __init__(self, name, model, year, battery_capacity, charge_status, ai_version):
        ElectricVehicle.__init__(self, name, model, year, battery_capacity, charge_status)  # Initialize ElectricVehicle
        AutonomousVehicle.__init__(self, name, model, year, ai_version)  # Initialize AutonomousVehicle
    

# Object creation and method calls
v1 = ElectricVehicle("Tesla", "Y1-g", 2024, "2KW", 85)  # Create ElectricVehicle object
v1.show_info()  # Display ElectricVehicle info
v1.charge_battery()  # Display battery charge status
print("------------------------------")
v2 = AutonomousVehicle("BMW", "X8", 2025, '3.12.1')  # Create AutonomousVehicle object
v2.show_info()  # Display AutonomousVehicle info
v2.auto_pilot()  # Display autopilot version
print("------------------------------")
v3 = SmartEV("Benz", "Z-20", 2030, "10KW", 98, '9.1.0')  # Create SmartEV object
v3.show_info()  # Display SmartEV info






#Sample output
# The Company make is Tesla
# The model is Y1-g
# The Company make is 2024
# Battery is up to date and the status is 85
# ------------------------------
# The Company make is BMW
# The model is X8
# The Company make is 2025
# Autopilot is working with version 3.12.1
# ------------------------------
# The Company make is Benz
# The model is Z-20
# The Company make is 2030



        

