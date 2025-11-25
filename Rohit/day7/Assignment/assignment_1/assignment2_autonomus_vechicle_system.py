# Task 2 — Autonomous Vehicle System
# Domain: Automotive / AI
# Business Requirement:
# UST Mobility is building an AI vehicle platform.

# Base class representing a generic Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        # Initialize vehicle attributes: make, model, and year
        self.make = make
        self.model = model
        self.year = year 
    
    def show_info(self):
        # Print basic vehicle information
        print(self.make, " ", self.model, " ", self.year)
        

# Subclass representing Electric Vehicles (inherits from Vehicle)
class Electric_vehichle(Vehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status):
        # Call parent class (Vehicle) constructor to initialize common attributes
        Vehicle.__init__(self, make, model, year)
        # Initialize electric vehicle-specific attributes
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status
        
    def charge_battery(self):
        # Print confirmation that battery is charging
        print("Yes")
    

# Subclass representing Autonomous Vehicles (inherits from Electric_vehichle)
class AutonomousVehicle(Electric_vehichle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        # Call parent class (Electric_vehichle) constructor
        Electric_vehichle.__init__(self, make, model, year, battery_capacity, charge_status) 
        # Initialize autonomous vehicle-specific attribute
        self.ai_version = ai_version
    
    def runPilot(self):
        # Check if AI version is enabled for autopilot
        if self.ai_version.lower() == "yes":
            print("yes")
        else:
            print("NOt i autopilot mode")


# Subclass representing Smart Electric Vehicles (inherits from AutonomousVehicle)
class SmartEV(AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        # Call parent class (AutonomousVehicle) constructor
        AutonomousVehicle.__init__(self, make, model, year, battery_capacity, charge_status, ai_version)
    
    # Example of extending functionality (commented out)
    # def show_value(self):
    #     print(self.make, " ", )


# Create an instance of SmartEV with attributes
vechicle = SmartEV("SUV", "Seltos", "2025", "good", "fine", "Yes")

# Call method from AutonomousVehicle to check autopilot mode
vechicle.runPilot()

# Call method from Vehicle to show basic vehicle info
vechicle.show_info()   

# Call method from Electric_vehichle to simulate charging battery
vechicle.charge_battery() 


# ===========sample output===============
# yes
# SUV   Seltos   2025
# Yes
