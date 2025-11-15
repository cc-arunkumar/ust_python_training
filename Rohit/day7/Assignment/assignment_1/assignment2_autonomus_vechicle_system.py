# Task 2 — Autonomous Vehicle System
# Domain: Automotive / AI
# Business Requirement:
# UST Mobility is building an AI vehicle platform.


class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year 
    
    def show_info(self):
        print(self.make, " ", self.model, " ", self.year)
        

class Electric_vehichle (Vehicle):
    def __init__(self,make,model,year,battery_capacity,charge_status):
        Vehicle.__init__(self,make,model ,year)
        self.battery_capacity=battery_capacity
        self.charge_status = charge_status
        
    def charge_battery(self):
        print("Yes")
    
class AutonomousVehicle(Electric_vehichle):
    def __init__(self, make, model, year,battery_capacity,charge_status,ai_version):
        Electric_vehichle.__init__(self,make, model, year,battery_capacity,charge_status) 
        self.ai_version = ai_version
    
    def runPilot(self):
        if self.ai_version.lower()=="yes":
            print("yes")
        else:
            print("NOt i autopilot mode")

class SmartEV(AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        AutonomousVehicle.__init__(self,make, model, year, battery_capacity, charge_status, ai_version)
    
    # def show_value(self):
    #     print(self.make, " ", )

     
    
vechicle = SmartEV("SUV","Seltos","2025","good","fine","Yes")

vechicle.runPilot()

vechicle.show_info()   
vechicle.charge_battery() 


# ===========sample output===============
# yes
# SUV   Seltos   2025
# Yes
