# Task 2 — Autonomous Vehicle System

# Domain: Automotive / AI

# Business Requirement:
# UST Mobility is building an AI vehicle platform.
    # 1. Every Vehicle must have:
    # name , model , year
    # Method: show_info()
    # 2. Every ElectricVehicle should have:
    # battery_capacity , charge_status
    # Method: charge_battery()
    # 3. Every AutonomousVehicle should have:
    # ai_version , run_autopilot()
    # 4. The company wants to create a class SmartEV — a self-driving electricvehicle.


class Vehicle:
    def __init__(self,name,model,year):
        self.name = name 
        self.model = model
        self.year =year 
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Model : {self.model}")
        print(f"Launched in: {self.year}")
    
class ElectricVehicle(Vehicle):
    def __init__(self,name,model,year,battery_capacity,charge_status):
        Vehicle.__init__(self,name,model,year)
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status
    
    def charge_battery():
        print("Charge the Battery!")
        
class AutonomousVehicle(Vehicle):
    def __init__(self,name,model,year,ai_version):
        Vehicle.__init__(self,name,model,year)
        self.ai_version = ai_version
        
    def run_autopilot(self):
        print("Running in Autopilot Mode....")

class SmartEV(ElectricVehicle,AutonomousVehicle):
    def __init__(self, name, model, year, battery_capacity, charge_status,ai_version):
        ElectricVehicle.__init__(self,name, model, year, battery_capacity, charge_status)
        AutonomousVehicle.__init__(self,name,model,year,ai_version)


ev_vehicle1 = ElectricVehicle('Maruthi','EV600',2025,65000,'Charging')
ev_vehicle1.show_info()

smartev_vehicle1 = SmartEV('MG','EV690',2025,80000,'Idle','2.0')
smartev_vehicle1.run_autopilot()
smartev_vehicle1.show_info()

#Sample Output
# Name: Maruthi
# Model : EV600
# Launched in: 2025

# Running in Autopilot Mode....
# Name: MG
# Model : EV690
# Launched in: 2025