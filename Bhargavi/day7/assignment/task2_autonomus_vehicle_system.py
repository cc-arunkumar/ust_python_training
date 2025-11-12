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
# 4. The company wants to create a class SmartEV — a self-driving electric
# vehicle.

#Base class
class Vehicle:
    def __init__(self, made, model, year):
        self.made = made
        self.model = model
        self.year = year
        
    def show_info(self):
        print(f"{self.year} {self.made} {self.model}")
        
        
#ElectricalVehicle
class ElectricalVehicle(Vehicle):
    def __init__(self, made, model, year, battery_capacity, charge_status):
        Vehicle.__init__(self, made, model, year)
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status
        
    def charge_battery(self):
        print(f"Charging... Battery at {self.charge_status}% of {self.battery_capacity} kWh")

#AutonomusVehicle     
class AutonomusVehicle(Vehicle):
    def __init__(self,made ,model,year,ai_version ):
         Vehicle.__init__(self, made, model, year)
         self.ai_version = ai_version    
         
    def run_autopilot(self):
        print(f"autopilot running using AI version : {self.ai_version}")
        
        
#multiple inheritance      
class SmartEV(ElectricalVehicle , AutonomusVehicle):
    def __init__(self,made,model, year,battery_capacity,charge_status,ai_version):
        ElectricalVehicle.__init__(self, made, model, year,battery_capacity,charge_status)
        AutonomusVehicle.__init__(self, made, model, year,ai_version)
        
v1 = Vehicle("china" , "Tar", 2003)   
v1.show_info()
print("/n************")

e1 = ElectricalVehicle("India" , "tata", 2005,89,67)   
e1.show_info()
e1.charge_battery()
print("/n************")

a1 =AutonomusVehicle("paksithan", "van",2008,1)   
a1.show_info()
a1.run_autopilot()
print("/n************")

s1 = SmartEV("paksithan" , "van", 2008,56,78, 1)   
s1.show_info()
s1.run_autopilot()
e1.charge_battery()
print("/n************")

#ouput
# 2003 china Tar
# /n************
# 2005 India tata
# Charging... Battery at 67% of 89 kWh
# /n************
# 2008 paksithan van
# autopilot running using AI version : 1
# /n************
# 2008 paksithan van
# autopilot running using AI version : 1
# Charging... Battery at 67% of 89 kWh
# /n************