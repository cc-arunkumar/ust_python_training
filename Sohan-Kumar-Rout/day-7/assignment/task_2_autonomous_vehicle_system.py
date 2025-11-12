#Task 2: Autonomous Vehicle System

#Code 
class Vehicle:
    def __init__(self,name ,model,year):
        self.name=name
        self.model=model
        self.year=year
        
    def show_info(self):
        print(f"Name of vehicle : {self.name}")
        print(f"Model of Vehicle : {self.model}")
        print(f"Year of Manufacture : {self.year}")
    #Running run_autopilot method
    def run_autopilot(self):
        print(f"AI-Version : {self.ai_version}")
        
        
#Child class of vehicle
class ElectricVehicle(Vehicle):
    def __init__(self, name, model, year,battery_capacity,charge_status,ai_version):
        Vehicle.__init__(self,name, model, year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status
        self.ai_version=ai_version
        
    def charge_battery(self):
        print(f"Battery capacity of the Vehicle is : {self.battery_capacity}")
        print(f"Charge status of the vehicle is : {self.charge_status}")

#Inheriting child class 
class AutonomousVehicle(ElectricVehicle):
    def __init__(self, name, model, year,ai_version,battery_capacity,charge_status,):
        ElectricVehicle.__init__(self,name, model, year,battery_capacity,charge_status,ai_version)
        self.ai_version=ai_version
    def run_autopilot(self):
        print(f"AI-Version : {self.ai_version}")

class SmartEV(AutonomousVehicle):
    def __init__(self, name , model, year, battery_capacity, charge_status,ai_version):
        AutonomousVehicle.__init__(self, name, model, year,ai_version,battery_capacity,charge_status)
        
vec1=ElectricVehicle("Honda Amaze","CS1", 2003-1-11,"30000mh","34%","Mannual")
vec1.show_info()
vec1.charge_battery()
vec1.run_autopilot()
vec2 = SmartEV("BMW","M8", 1999-8-20,"80000mh","84%","auto-pilot")
vec2.show_info()
vec2.charge_battery()
vec2.run_autopilot()

#Output
# Name of vehicle : Honda Amaze
# Model of Vehicle : CS1
# Year of Manufacture : 1991
# Battery capacity of the Vehicle is : 30000mh
# Charge status of the vehicle is : 34%
# AI-Version : Mannual
# Name of vehicle : BMW
# Model of Vehicle : M8
# Year of Manufacture : 1971
# Battery capacity of the Vehicle is : 80000mh
# Charge status of the vehicle is : 84%
# AI-Version : auto-pilot

        
        