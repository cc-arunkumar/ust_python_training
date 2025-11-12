"""
Task: The company wants to create a class SmartEV — a self-driving electric vehicle.
"""

class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def show_info(self):
        print(f"Maker :{self.make}")
        print(f"Model :{self.model}")
        print(f"Year :{self.year}")
#Inheritance from Vehicles
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year,battery_capacity,charge_status):
        Vehicle.__init__(self,make, model, year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status

    def charge_battery(self):
        print(f"Battery Capacity :{self.battery_capacity}")
        print(f"Charging Status :{self.charge_status}")
# Inheritance from Vehicle
class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year,ai_verison):
        Vehicle.__init__(self,make, model, year)
        self.ai_version=ai_verison
    
    def run_autopilot(self):
        print(f"{self.make} car version {self.ai_version} runs in Autopilot mode")


# Inheriting from ElectricVehicle and AutonomousVehicle
class SmartEV(ElectricVehicle,AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status,ai_version):
        ElectricVehicle.__init__(self, make, model, year,battery_capacity,charge_status)
        AutonomousVehicle.__init__(self,make, model, year,ai_version)

    def smart_ev_details(self):
        print(f"Smart EV Maker :{self.make}")
        print(f"Model :{self.model}")
        print(f"Year :{self.year}")
        print(f"Battery Capacity :{self.battery_capacity}")
        print(f"CHarging Status :{self.charge_status}")
        print(f"AI verison :{self.ai_version}")


# EV
print("---Electric Vehicles---")
ev1=ElectricVehicle("Tata","Gen 7",2025,"100000Mah","Charging")
ev1.charge_battery()

# Autonomous
print("---Autonomous Vehicles---")
a1=AutonomousVehicle("Toyota","Auto",2025,4.0)
a1.run_autopilot()

#SMart EV  make, model, year, battery_capacity, charge_status,ai_versio
print("---Smart EV---")
sev1=SmartEV("Tesla","Auto EV",2026,"50000mah","completed",6.3)
sev1.smart_ev_details()


"""
SAMPLE OUTPUT

---Electric Vehicles---
Battery Capacity :100000Mah
Charging Status :Charging
---Autonomous Vehicles---
Toyota car version 4.0 runs in Autopilot mode
---Smart EV---
Smart EV Maker :Tesla
Model :Auto EV
Year :2026
Battery Capacity :50000mah
CHarging Status :completed
AI verison :6.3

"""