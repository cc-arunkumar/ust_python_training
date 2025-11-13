#Task 2 Autonomous Vehicle System

#Creating Vehicle class as Parent classs
class Vehicle:
    #value initialization
    def __init__(self,name,model,year):
        self.name=name
        self.model=model
        self.year=year
    #Creating  display function
    
    def  show_info(self):
        print(f"Make: {self.name}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        
#Creating  Electric Vehicle class 
class ElectricVehicle(Vehicle):
    def __init__(self,name,model,year,battery_capacity,charge_status):
        Vehicle. __init__(self,name,model,year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status
    def charge_battery(self):
        print(f"Battery capacity of the vehicle is: {self.battery_capacity} so charge status is {self.charge_status}")

#Creating  Autonomous Vehicle class
class AutonomousVehicle(Vehicle):
    def __init__(self,name,model,year,ai_version):
        Vehicle. __init__(self,name,model,year)
        self.ai_version=ai_version
    
    #Creating run autopilot function
    def run_autopilot(self):
        print("The autopilot is available: ")
#Creating class SmartEV class derived from ElectricVehicle and AutonomousVehicle class:
class SmartEV(ElectricVehicle,AutonomousVehicle):
    def __init__(self, name, model, year, battery_capacity, charge_status,ai_version):
        ElectricVehicle.__init__(self,name,model,year,battery_capacity,charge_status)
        AutonomousVehicle.__init__(self,name,model,year,ai_version)
#Object creation
name=input("Enter the vehicle name: ")
model=input("Eneter the model: ")
year=input("Enter the year: ")
bc=input("Enter the battery capacity: ")
cs=input("Enter the charge status: ")
aiv=input("Enter the ai_version: ")
v=Vehicle(name,model,year)
v.show_info()
ev=ElectricVehicle(name,model,year,bc,cs)
ev.charge_battery()
av=AutonomousVehicle(name,model,year,aiv)
av.run_autopilot()
sev=SmartEV(name,model,year,bc,cs,aiv)
sev.charge_battery()
print(sev.run_autopilot())

#Sample Execution
# Enter the vehicle name: Tata Harrier
# Eneter the model: SUV
# Enter the year: 2019
# Enter the battery capacity: 90KMPV
# Enter the charge status: Full
# Enter the ai_version: V2.0
# Make: Tata Harrier
# Model: SUV
# Year: 2019
# Battery capacity of the vehicle is: 90KMPV so charge status is Full
# The autopilot is available:
# Battery capacity of the vehicle is: 90KMPV so charge status is Full
# None




    
    
    
            
        
    