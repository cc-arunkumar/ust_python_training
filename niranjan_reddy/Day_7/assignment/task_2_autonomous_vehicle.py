# Task 2 — Autonomous Vehicle System
# Domain: Automotive / AI
# Business Requirement:
# UST Mobility is building an AI vehicle platform.


# 1. Every Vehicle must have:
# make , model , year
# Method: show_info()
# Create Vehicle class


class Vehicle:
    def __init__(self,make , model , year):
        self.make=make
        self.model=model
        self.year=year

    def show_info(self):
        print(f"Vehicle Company: {self.make}")
        print(f"Vehicle Model: {self.model}")
        print(f"Vehicle manufacture year: {self.year}")

# 2. Every ElectricVehicle should have:
# battery_capacity , charge_status
# Method: charge_battery()

class ElectricVehicle(Vehicle):
    def __init__(self,make , model , year,battery_capacity , charge_status):
        Vehicle.__init__(self,make , model , year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status

    def charge_battery(self):
        print("--------------------------")
        print(f"Vehicle Company: {self.make}")
        print(f"Vehicle Model: {self.model}")
        print(f"Vehicle manufacture year: {self.year}")
        print(f"Vehicle battery capacity:{self.battery_capacity}")
        print(f"Vehicle charging status: {self.charge_status}")



# 3. Every AutonomousVehicle should have:
# ai_version , run_autopilot()

class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year,ai_version):
        Vehicle.__init__(self,make, model, year)
        self.ai_version=ai_version

    def run_autopilot(self):
        print("--------------------------")
        print("AutonomousVehicle if running")

# 4. The company wants to create a class SmartEV — a self-driving electric vehicle.

class SmartEV(ElectricVehicle,AutonomousVehicle):
    def __init__(self, make, model, year, ai_version,battery_capacity , charge_status):
        ElectricVehicle.__init__(self, make, model, year,battery_capacity , charge_status)
        AutonomousVehicle.__init__(self,make, model, year, ai_version)



vehicle1=Vehicle("Tata","Nexon",2011)
vehicle2=ElectricVehicle("Mahindra","BE6",2023,"150EV",80)
vehicle3=AutonomousVehicle("Tesla","Model Y",2021,2.1)
vehicle4=SmartEV("Tata","Curv.ev",2021,2.2,"200EV",90)

vehicle1.show_info()
vehicle2.charge_battery()
vehicle3.run_autopilot()
vehicle4.charge_battery()

# Sample Output
# Vehicle Company: Tata
# Vehicle Model: Nexon
# Vehicle manufacture year: 2011
# --------------------------
# Vehicle Company: Mahindra
# Vehicle Model: BE6
# Vehicle manufacture year: 2023
# Vehicle battery capacity:150EV
# Vehicle charging status: 80
# --------------------------
# AutonomousVehicle if running
# --------------------------
# Vehicle Company: Tata
# Vehicle Model: Curv.ev
# Vehicle manufacture year: 2021
# Vehicle battery capacity:200EV
# Vehicle charging status: 90

