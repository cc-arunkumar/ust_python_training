#Task 2 — Autonomous Vehicle System
#creating vehicle class
class Vehicle:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
    
    #function to print info
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model} Year: {self.year}")

#creating Eclectric Vehicle class  
class ElectricVehicle(Vehicle):
    def __init__(self, name, model, year,battery_capacity,charge_status):
        Vehicle.__init__(self,name, model, year)
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status

    def charge_battery(self):
        print(f"Battery status is: {self.charge_status}")

#creating autonomous vehicle class
class AutonomousVehicle(Vehicle):
    def __init__(self,name, model, year,ai_version):
        Vehicle.__init__(self,name, model, year)
        self.ai_version =ai_version
        
    def run_autopilot(self):
        print(f"Autopilot is working and version is:{self.ai_version}")

#creating smart EV class
class SmartEV(ElectricVehicle,AutonomousVehicle):
    def __init__(self, name, model, year, battery_capacity, charge_status,ai_version):
        ElectricVehicle.__init__(self,name, model, year, battery_capacity, charge_status)
        AutonomousVehicle.__init__(self,name, model, year,ai_version)

#object creation and accessing methods
v1 = ElectricVehicle("Tata","Nexon EV",2025,"3Kwh",70)
v1.show_info()
v1.charge_battery()
print("=========================================")

v2 = AutonomousVehicle("Mercedes","S-Class",2024,2.5)
v2.show_info()
v2.run_autopilot()
print("=========================================")

v3 = SmartEV("Tesla","Model S",2023,"5Kwh",90,3.0)
v3.show_info()
v3.charge_battery()
v3.run_autopilot()
print("========================================")

#Sample Output
# Name: Tata
# Model: Nexon EV Year: 2025
# Battery status is: 70
# =========================================
# Name: Mercedes
# Model: S-Class Year: 2024
# Autopilot is working and version is:2.5
# =========================================
# Name: Tesla
# Model: Model S Year: 2023
# Battery status is: 90
# Autopilot is working and version is:3.0
# ========================================