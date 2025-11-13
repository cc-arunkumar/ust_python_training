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
# Creatting base class
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def show_info(self):
        print(f"Make:{self.make}|Model:{self.model}Year:{self.year}")

# Cerating 2 child classes ofVehicle
class ElectricVehicle(Vehicle):
    def __init__(self,make,model,year,battery_capacity,charge_status):
        Vehicle.__init__(self,make,model,year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status
        
    def charge_battery(self):
        print("Charging")

class AutonomousVehicle(Vehicle):
    def __init__(self,make,model,year,ai_version):
        Vehicle.__init__(self,make,model,year)
        self.ai_version=ai_version
    def run_autopilot(self):
        print("Autopilot initiated....")

# creating clas that inherits AutonomousVehicle and ElectricVehicle
class SmartEv(ElectricVehicle,AutonomousVehicle):
    def __init__(self,make,model,year,battery_capacity,charge_status,ai_version):
        ElectricVehicle.__init__(self,make,model,year,battery_capacity,charge_status)
        AutonomousVehicle.__init__(self,make,model,year,ai_version)


SmartEv01=SmartEv("Hyundai","i20",2010,"100kw","90%","ai12.10.1")
SmartEv01.charge_battery()
SmartEv01.run_autopilot()
    
# Charging
# Autopilot initiated....