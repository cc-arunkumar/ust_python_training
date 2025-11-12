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
# 1. Every Vehicle must have:
# make , model , year
# Method: show_info()
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
# 2. Every ElectricVehicle should have:
# battery_capacity , charge_status
# Method: charge_battery()
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status):
        Vehicle.__init__(self, make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status

    def charge_battery(self):
        if self.charge_status == 100:
            print("Battery fully charged.")
        else:
            print(f"Remaining battery: {self.charge_status}%")
            
# 3. Every AutonomousVehicle should have:
# ai_version , run_autopilot()
class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year, ai_version):
        Vehicle.__init__(self, make, model, year)
        self.ai_version = ai_version

    def run_autopilot(self):
        print(f"Running autopilot with AI version: {self.ai_version}")
# 4. The company wants to create a class SmartEV — a self-driving electric vehicle.
class SmartEv(ElectricVehicle, AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        ElectricVehicle.__init__(self, make, model, year, battery_capacity, charge_status)
        AutonomousVehicle.__init__(self, make, model, year, ai_version)

# Sample input
smart_car = SmartEv("UST Motors", "EagleX", 2024, 85, 60, "v3.2")
smart_car.show_info()
smart_car.charge_battery()
smart_car.run_autopilot()

#output:
# Make: UST Motors, Model: EagleX, Year: 2025
# Remaining battery: 60%
# Running autopilot with AI version: v3.2