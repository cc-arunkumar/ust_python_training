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
# 4. The company wants to create a class SmartEV — a self-driving electric vehicle.
# Task: Reuse as much code as possible by designing the inheritance chain
# properly.
# Think about the correct inheritance structure to achieve this.

# main Code:

# 1. Base Vehicle class
# Every Vehicle must have: make, model, year
# Method: show_info() to display vehicle details
class Vehicle:
    def __init__(self, make, model, year):
        # Initialize common vehicle attributes
        self.make = make
        self.model = model
        self.year = year

    def show_info(self):
        # Display vehicle information
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


# 2. ElectricVehicle class (inherits from Vehicle)
# Every ElectricVehicle should have: battery_capacity, charge_status
# Method: charge_battery() to show battery status
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status):
        # Call Vehicle constructor to initialize common attributes
        Vehicle.__init__(self, make, model, year)
        # Initialize electric vehicle-specific attributes
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status

    def charge_battery(self):
        # Check battery status
        if self.charge_status == 100:
            print("Battery fully charged.")
        else:
            print(f"Remaining battery: {self.charge_status}%")


# 3. AutonomousVehicle class (inherits from Vehicle)
# Every AutonomousVehicle should have: ai_version
# Method: run_autopilot() to simulate autopilot functionality
class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year, ai_version):
        # Call Vehicle constructor to initialize common attributes
        Vehicle.__init__(self, make, model, year)
        # Initialize autonomous vehicle-specific attributes
        self.ai_version = ai_version

    def run_autopilot(self):
        # Display autopilot running info
        print(f"Running autopilot with AI version: {self.ai_version}")


# 4. SmartEv class (inherits from both ElectricVehicle and AutonomousVehicle)
# Represents a self-driving electric vehicle (combination of both features)
class SmartEv(ElectricVehicle, AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        # Initialize ElectricVehicle part
        ElectricVehicle.__init__(self, make, model, year, battery_capacity, charge_status)
        # Initialize AutonomousVehicle part
        AutonomousVehicle.__init__(self, make, model, year, ai_version)


# Sample usage
smart_car = SmartEv("UST Motors", "EagleX", 2024, 85, 60, "v3.2")

# Call methods from different parent classes
smart_car.show_info()        # From Vehicle class
smart_car.charge_battery()   # From ElectricVehicle class
smart_car.run_autopilot()    # From AutonomousVehicle class

#output:
# Make: UST Motors, Model: EagleX, Year: 2025
# Remaining battery: 60%
# Running autopilot with AI version: v3.2