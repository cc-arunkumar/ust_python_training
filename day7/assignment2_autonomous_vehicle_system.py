#Autonomous Vehicle System

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


# Base class: Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Intermediate class: ElectricAndAutonomousVehicle
class ElectricAndAutonomousVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status
        self.ai_version = ai_version

    def charge_battery(self):
        print(f"Charging battery to {self.battery_capacity} kWh. Current charge: {self.charge_status}%")

    def run_autopilot(self):
        print(f"Running autopilot with AI version {self.ai_version}.")

# Final subclass: SmartEV (Electric & Autonomous)
class SmartEV(ElectricAndAutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        super().__init__(make, model, year, battery_capacity, charge_status, ai_version)

    def show_info(self):
        super().show_info()  # Calling the method from the base class
        print(f"Battery Capacity: {self.battery_capacity} kWh, Charge Status: {self.charge_status}%")
        print(f"AI Version: {self.ai_version}")

# Example usage
smart_ev = SmartEV("Tesla", "Model X", 2025, 100, 85, "v2.5")
smart_ev.show_info()
smart_ev.charge_battery()
smart_ev.run_autopilot()


#o/p:
# Make: Tesla, Model: Model X, Year: 2025
# Battery Capacity: 100 kWh, Charge Status: 85%
# AI Version: v2.5
# Charging battery to 100 kWh. Current charge: 85%
# Running autopilot with AI version v2.5.