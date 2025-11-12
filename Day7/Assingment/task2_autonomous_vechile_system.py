# Task 2 — Autonomous Vehicle System
# Domain: Automotive / AI

# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Subclass 1 — ElectricVehicle
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status):
        Vehicle.__init__(self, make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status

    def charge_battery(self):
        print(f"{self.make} {self.model} battery capacity: {self.battery_capacity} Ah")
        print(f"charge status: {self.charge_status}")

# Subclass 2 — AutonomousVehicle
class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year, ai_version):
        Vehicle.__init__(self, make, model, year)
        self.ai_version = ai_version

    def run_autopilot(self):
        print(f"{self.make} {self.model} AI version: {self.ai_version}")


class SmartEV(AutonomousVehicle, ElectricVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        ElectricVehicle.__init__(self, make, model, year, battery_capacity, charge_status)
        AutonomousVehicle.__init__(self, make, model, year, ai_version)

    def show_smart_ev(self):
        self.show_info()
        self.charge_battery()
        self.run_autopilot()


# Testing
ev = SmartEV("Volkswagen", "Touran", 2003, 45, "Charging", 2)
ev.show_smart_ev()

# sample output:
# Make: Volkswagen
# Model: Touran
# Year: 2003
# Volkswagen Touran battery capacity: 45 Ah
# charge status: Charging
# Volkswagen Touran AI version: 2
