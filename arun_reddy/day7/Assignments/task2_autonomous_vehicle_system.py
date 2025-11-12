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
# ⚙️ Task: Reuse as much code as possible by designing the inheritance chain
# properly.
# Think about the correct inheritance structure to achieve this


class Vehicle:
    def __init__(self,make , model , year):
        self.make=make
        self.model=model
        self.year=year
    def show_info(self):
        print("Info of teh Vehicle:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year,battery_capacity ,charge_status):
        Vehicle.__init__(self,make, model, year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status
    def charge_battery(self):
        print(f"battery capacity:{self.battery_capacity}")
        print(f"charging status:{self.charge_status}")


class AutonomousVehicle(ElectricVehicle):
    def __init__(self, make, model, year,battery_capacity , charge_status,ai_version):
        ElectricVehicle.__init__(self,make, model, year,battery_capacity,charge_status)
        self.ai_version=ai_version
        self.model=model
    def run_autopilot(self):
        print(f" {self.model} ia an {self.ai_version} vehicle")


class SmartEV(AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        AutonomousVehicle.__init__(self,make, model, year, battery_capacity, charge_status, ai_version)



smrtev=SmartEV("Honda","5000X",1987,"50000mAh","full","auto-pilot")
smrtev.charge_battery()
smrtev.run_autopilot()
smrtev.show_info()
        

# sample execution 
# battery capacity:50000mAh
# charging status:full
#  5000X ia an auto-pilot vehicle
# Info of teh Vehicle:
# Make: Honda
# Model: 5000X
# Year: 1987
        
    
        
        