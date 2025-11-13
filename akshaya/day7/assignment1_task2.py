# Task 2 — Autonomous Vehicle System
# Every Vehicle must have:
# make , model , year
# Method: show_info()
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show_info(self):
        print(f"Make: {self.make} | Model: {self.model} | Year: {self.year}")
        
#  Every ElectricVehicle should have:
# battery_capacity , charge_status
# Method: charge_battery()


class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status):
        Vehicle.__init__(self, make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status

    def charge_battery(self):
        print(f"Charging {self.make} {self.model} battery... Current charge: {self.charge_status}%")

# Every AutonomousVehicle should have:
# ai_version , run_autopilot()
class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year, ai_version):
        Vehicle.__init__(self, make, model, year)
        self.ai_version = ai_version

    def run_autopilot(self):
        print(f"Autopilot is running with AI Version: {self.ai_version}.")


class SmartEV(ElectricVehicle, AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        ElectricVehicle.__init__(self, make, model, year, battery_capacity, charge_status)
        AutonomousVehicle.__init__(self, make, model, year, ai_version)

    def show_info(self):
        print(f"Make: {self.make} | Model: {self.model} | Year: {self.year}")
        print(f"Battery Capacity: {self.battery_capacity} kWh | Current Charge Status: {self.charge_status}%")
        print(f"AI Version: {self.ai_version}")



vehicle1 = Vehicle("Toyota", "Corolla", 2021)
vehicle1.show_info()
print("------------------")

ev1 = ElectricVehicle("Tesla", "Model 3", 2023, 75, 80)
ev1.show_info()
ev1.charge_battery()
print("------------------")

av1 = AutonomousVehicle("Waymo", "Chrysler Pacifica", 2023, "v1.2.3")
av1.show_info()
av1.run_autopilot()
print("------------------")

smart_ev1 = SmartEV("Tesla", "Model S", 2023, 100, 60, "v2.0")
smart_ev1.show_info()
smart_ev1.charge_battery()
smart_ev1.run_autopilot()
print("------------------")

# sample output
# Make: Toyota | Model: Corolla | Year: 2021
# ------------------
# Make: Tesla | Model: Model 3 | Year: 2023
# Charging Tesla Model 3 battery... Current charge: 80%
# ------------------
# Make: Waymo | Model: Chrysler Pacifica | Year: 2023
# Autopilot is running with AI Version: v1.2.3.
# ------------------
# Make: Tesla | Model: Model S | Year: 2023
# Battery Capacity: 100 kWh | Current Charge Status: 60%
# AI Version: v2.0
# Charging Tesla Model S battery... Current charge: 60%
# Autopilot is running with AI Version: v2.0.
# ------------------
