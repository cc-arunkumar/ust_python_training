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
# 4. The company wants to create a class SmartEV — a self-driving electricvehicle

# Parent class
class Vehicle():
    def __init__(self,make,model,year):
        self.make=make
        self.model = model
        self.year = year
    def show_info(self):
        print(f"Make of vehicle: {self.make}")
        print(f"Model of vehicle: {self.model}")
        print(f"Year of vehicle: {self.year}")
        
# Child class
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year,battery,charge_status):
        Vehicle.__init__(self,make, model, year)
        self.battery_capacity=battery
        self.charge_status=charge_status
    def charge_battery(self):
        self.show_info()
        print(f"Battery capacity is {self.battery_capacity}")
        print(f"Charge status is {self.charge_status}")
        
# Child class
class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year,ai_version):
        Vehicle.__init__(self,make, model, year)
        self.ai_version=ai_version
        
    def run_autopilot(self):
        self.show_info()
        print(f"Ai version: {self.ai_version}")

# child class by multiple inheritance
class SmartEv(ElectricVehicle,AutonomousVehicle):
    def __init__(self, make, model, year, battery, charge_status,ai_version):
        ElectricVehicle.__init__(self,make, model, year, battery, charge_status)
        AutonomousVehicle.__init__(self, make, model, year,ai_version)
        
    def show(self):
        self.show_info()
        print(f"Battery capacity is {self.battery_capacity}")
        print(f"Charge status is {self.charge_status}")
        print(f"Ai version: {self.ai_version}")
        
# Object creation and getting info
smart1 = SmartEv("Porshe","Taycan",2022,"100%","Full",3.17)
smart1.show()
        
        
        
# Output
# Make of vehicle: Porshe
# Model of vehicle: Taycan
# Year of vehicle: 2022
# Battery capacity is 100%
# Charge status is Full
# Ai version: 3.17