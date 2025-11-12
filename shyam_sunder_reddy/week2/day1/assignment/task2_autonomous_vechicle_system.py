# Task 2 — Autonomous Vehicle System
# Domain: Automotive / AI
# Business Requirement:
# UST Mobility is building an AI vehicle platform.
# 1. Every Vehicle must have:
# make , model , year
# Method: show_info()

class Vechile:
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
    
    #showing the information of vehicle
    def show_info(self):
        print("Name: ",self.name)
        print("Model: ",self.model)
        print("Year: ",self.year)

# 2. Every ElectricVehicle should have:
# battery_capacity , charge_status
# Method: charge_battery()
class ElectricVehicle(Vechile):
    def __init__(self,name,model,year,battery_capacity,charge_status):
        super().__init__(name,model,year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status
    
    #charge the vehicle
    def charge_battery(self):
        self.charge_status="Charging"


# 3. Every AutonomousVehicle should have:
# ai_version , run_autopilot()
class AutonomousVechicle(ElectricVehicle):
    def __init__(self,name,model,year,battery_capacity,charge_status,ai_version):
        super().__init__(name,model,year,battery_capacity,charge_status)
        self.ai_version=ai_version
    
    def run_autopilot(self):
        print("running Auto Pilot")
# 4. The company wants to create a class SmartEV — a self-driving electric
# vehicle.
class SmartEV(AutonomousVechicle):
    def __init__(self,name,model,year,battery_capacity,charge_status,ai_version):
        super().__init__(name,model,year,battery_capacity,charge_status,ai_version)
    

vec1=Vechile("maruti","f85",2000)
vec1.show_info()
print("-------------------------")

vec2=ElectricVehicle("Mahindra","be6",2020,5000,"idle")
vec2.show_info()
vec2.charge_battery()
print("-------------------------")

vec3=AutonomousVechicle("Tesla","Y",2022,9000,"charging",1.3)
vec3.show_info()
vec3.charge_battery()
vec3.run_autopilot()
print("-------------------------")

vec3=SmartEV("Tesla","x",2022,9000,"charging",1.3)
vec3.show_info()
vec3.charge_battery()
vec3.run_autopilot()
print("-------------------------")


# Sample output
# Name:  maruti
# Model:  f85
# Year:  2000
# -------------------------
# Name:  Mahindra
# Model:  be6
# Year:  2020
# -------------------------
# Name:  Tesla
# Model:  Y
# Year:  2022
# running Auto Pilot
# -------------------------
# Name:  Tesla
# Model:  x
# Year:  2022
# running Auto Pilot
# -------------------------