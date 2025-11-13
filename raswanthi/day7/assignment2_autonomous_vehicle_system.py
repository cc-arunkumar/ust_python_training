#Assignment 2 : Autonomous Vehicle System using Inheritance
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model 
        self.year=year
        
    def show_info(self):
        print(f"Manufacturer:{self.make} | Model:{self.model} | YEar:{self.year}")

#class ElectricVehicle inheriting behaviors from Vehicle
class ElectricVehicle(Vehicle):
    def __init__(self,make,model,year,battery_capacity,charge_status):
        Vehicle.__init__(self,make,model,year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status
        
    def charge_battery(self):
        if self.charge_status<100:
            print(f"Charging..{self.charge_status}%")
        elif self.charge_status==100:
            print(f"Battery is full")
            
#class AutonomousVehicle inheriting behaviors from ElectricVehicle
class AutonomousVehicle(ElectricVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version, run_autopilot):
        ElectricVehicle.__init__(self,make, model, year, battery_capacity, charge_status)
        self.ai_version = ai_version
        self.run_autopilot = run_autopilot

#class SmartEv inheriting properties from AutonomousVehicle     
class SmartEV(AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version, run_autopilot):
        AutonomousVehicle.__init__(make, model, year, battery_capacity, charge_status, ai_version, run_autopilot)
         


v1=Vehicle("Toyoto","Model 3","2024")
v2=Vehicle("Honda","Civic","2021")
v1.show_info()
v2.show_info()
print("------------------------------")

ev1 = ElectricVehicle("Tata", "Nexon EV", "2023", 30, 85)
ev2 = ElectricVehicle("Nissan", "Leaf", "2022", 45, 100)
ev1.charge_battery()
ev2.charge_battery()
print("-------------------------------")

'''output:
Manufacturer:Toyoto | Model:Model 3 | YEar:2024
Manufacturer:Honda | Model:Civic | YEar:2021
------------------------------
Charging..85%
Battery is full
-------------------------------
'''




        
        