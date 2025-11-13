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

class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def show_info(self):     
        print(f"made {self.make} model is {self.model} made in year {self.year}")
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year,battery_capacity,charge_status):
        Vehicle.__init__(self,make, model, year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status
    
    def charge_battery(self):
        self.charge_status=100
        print(f"battery capacity is {self.battery_capacity} and the charge status is {self.charge_status}%")

class AutonomousVehicle(ElectricVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status,ai_version):
        ElectricVehicle.__init__(self,make, model, year,battery_capacity,charge_status)
        self.ai_version=ai_version
    def run_autopilot(self):
        if self.ai_version=='yes':
            print("YES")
        else:
            print("Not autopilot ")
        
class SmartEV(AutonomousVehicle,ElectricVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        AutonomousVehicle.__init__(self,make, model, year, battery_capacity, charge_status, ai_version)
        
smart_ev = SmartEV("UST Motors", "NeoDrive", 2025, 85, 60, "yes")
smart_ev.charge_battery()
smart_ev.show_info()
smart_ev.run_autopilot()
        
# Output
# battery capacity is 85 and the charge status is 
# 100%
# made UST Motors model is NeoDrive made in year 2025
# YES