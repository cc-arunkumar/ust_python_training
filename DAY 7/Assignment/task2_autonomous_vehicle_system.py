"""
Task: The company wants to create a class SmartEV — a self-driving electric vehicle.
"""

# Base class representing a general vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make      # Manufacturer of the vehicle
        self.model = model    # Model name of the vehicle
        self.year = year      # Year of manufacture
    
    # Method to display vehicle basic information
    def show_info(self):
        print(f"Maker : {self.make}")
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")


# ElectricVehicle inherits from Vehicle
# Adds battery-related attributes
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status):
        Vehicle.__init__(self, make, model, year)  # Initialize Vehicle attributes
        self.battery_capacity = battery_capacity   # Capacity of the battery
        self.charge_status = charge_status         # Charging status of the vehicle
    
    # Method to show battery status
    def charge_battery(self):
        print(f"Battery Capacity : {self.battery_capacity}")
        print(f"Charging Status : {self.charge_status}")


# AutonomousVehicle inherits from Vehicle
# Adds AI-related functionality
class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year, ai_version):
        Vehicle.__init__(self, make, model, year)  # Initialize Vehicle attributes
        self.ai_version = ai_version               # AI software version
    
    # Method to enable autopilot functionality
    def run_autopilot(self):
        print(f"{self.make} car version {self.ai_version} runs in Autopilot mode")


# SmartEV inherits both ElectricVehicle and AutonomousVehicle
# Combines features of electric and autonomous vehicles
class SmartEV(ElectricVehicle, AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        # Initialize ElectricVehicle attributes
        ElectricVehicle.__init__(self, make, model, year, battery_capacity, charge_status)
        # Initialize AutonomousVehicle attributes
        AutonomousVehicle.__init__(self, make, model, year, ai_version)
    
    # Method to display all Smart EV details
    def smart_ev_details(self):
        print(f"Smart EV Maker : {self.make}")
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")
        print(f"Battery Capacity : {self.battery_capacity}")
        print(f"Charging Status : {self.charge_status}")
        print(f"AI Version : {self.ai_version}")


# Example usage

# Electric Vehicle example
print("---Electric Vehicles---")
ev1 = ElectricVehicle("Tata", "Gen 7", 2025, "100000Mah", "Charging")
ev1.charge_battery()  # Display battery info

# Autonomous Vehicle example
print("---Autonomous Vehicles---")
a1 = AutonomousVehicle("Toyota", "Auto", 2025, 4.0)
a1.run_autopilot()    # Display autopilot info

# Smart EV example
print("---Smart EV---")
sev1 = SmartEV("Tesla", "Auto EV", 2026, "50000mah", "completed", 6.3)
sev1.smart_ev_details()  # Display combined EV and autonomous info


"""
SAMPLE OUTPUT

---Electric Vehicles---
Battery Capacity :100000Mah
Charging Status :Charging
---Autonomous Vehicles---
Toyota car version 4.0 runs in Autopilot mode
---Smart EV---
Smart EV Maker :Tesla
Model :Auto EV
Year :2026
Battery Capacity :50000mah
CHarging Status :completed
AI verison :6.3

"""