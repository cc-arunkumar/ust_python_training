# Task 2 — Autonomous Vehicle System
#  Domain: Automotive / AI
#  Business Requirement:
#  UST Mobility is building an AI vehicle platform.
#   Every Vehicle must have:
#  make , 
# model , 
# year
#  Method: 
# show_info()
#   Every ElectricVehicle should have:
#  battery_capacity , 
# charge_status
#  Method: 
# charge_battery()
#   Every AutonomousVehicle should have:
#  ai_version , 
# run_autopilot()
#   The company wants to create a class SmartEV — a self-driving electric 
# vehicle.

# Define a base Vehicle class
class Vehicle:
    # Constructor to initialize vehicle attributes
    def __init__(self, make, model, year):
        self.make = make          # Manufacturer name
        self.model = model        # Model name
        self.year = year          # Year of manufacture

    # Method to display vehicle information
    def show_info(self):
        print(f"made {self.make} model is {self.model} made in year {self.year}")


# Define ElectricVehicle class that inherits from Vehicle
class ElectricVehicle(Vehicle):
    # Constructor to initialize electric vehicle attributes
    def __init__(self, make, model, year, battery_capacity, charge_status):
        # Call Vehicle constructor
        Vehicle.__init__(self, make, model, year)
        self.battery_capacity = battery_capacity   # Battery capacity in kWh
        self.charge_status = charge_status         # Current charge percentage

    # Method to charge battery to 100%
    def charge_battery(self):
        self.charge_status = 100
        print(f"battery capacity is {self.battery_capacity} and the charge status is {self.charge_status}%")


# Define AutonomousVehicle class that inherits from ElectricVehicle
class AutonomousVehicle(ElectricVehicle):
    # Constructor to initialize autonomous vehicle attributes
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        # Call ElectricVehicle constructor
        ElectricVehicle.__init__(self, make, model, year, battery_capacity, charge_status)
        self.ai_version = ai_version   # AI version or autopilot capability

    # Method to run autopilot based on AI version
    def run_autopilot(self):
        if self.ai_version == 'yes':
            print("YES")               # Autopilot is available
        else:
            print("Not autopilot ")    # Autopilot not available


# Define SmartEV class that inherits from AutonomousVehicle and ElectricVehicle
class SmartEV(AutonomousVehicle, ElectricVehicle):
    # Constructor to initialize SmartEV attributes
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        # Call AutonomousVehicle constructor
        AutonomousVehicle.__init__(self, make, model, year, battery_capacity, charge_status, ai_version)


# -------------------------------
# Object Creation and Method Calls
# -------------------------------

# Create a SmartEV object with given attributes
smart_ev = SmartEV("UST Motors", "NeoDrive", 2025, 85, 60, "yes")

# Charge the battery to 100%
smart_ev.charge_battery()

# Show vehicle information
smart_ev.show_info()

# Run autopilot feature
smart_ev.run_autopilot()


# -------------------------------
# Expected Output
# -------------------------------
# battery capacity is 85 and the charge status is 100%
# made UST Motors model is NeoDrive made in year 2025
# YES