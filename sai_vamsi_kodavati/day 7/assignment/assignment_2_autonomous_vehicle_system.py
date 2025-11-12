# assignment_2_Autonomous Vehicle System

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def show_info(self):
        print(f"Company:{self.make}")
        print(f"Model:{self.model}")
        print(f"Year:{self.year}")

class ElectricVehicle(Vehicle):
    def __init__(self,make,model,year,battery_capacity,charge_status):
        Vehicle.__init__(self,make,model,year)
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status

    
    def charge_battery(self):
        print(f"Charging Status:{self.charge_status}")

class AutonomousVehicle(Vehicle):
    def __init__(self,make,model,year,ai_version):
        Vehicle.__init__(self,make,model,year)
        self.ai_version = ai_version
        
    
    def run_autopilot(self):
        print(f"Auto Pilot running on AI Version:{self.ai_version}")

class SmartEV(ElectricVehicle,AutonomousVehicle):
    def __init__(self, make, model,year,battery_capacity,charge_status,ai_version):
        
        ElectricVehicle.__init__(self,make,model,year,battery_capacity,charge_status)
        AutonomousVehicle.__init__(self,make,model,year,ai_version)


vehicle1 = Vehicle("Hyundai","Creta",2025)
print("\n ----Vehicle----")
vehicle1.show_info()

vehicle2 = ElectricVehicle("BMW","X5",2023,100,"40% charged")
print("\n ----Electric Vehicle----")
vehicle2.show_info()
vehicle2.charge_battery()

vehicle3 = AutonomousVehicle("Tata","Nexon",2023,"v121.11")
print("\n ----Autonomous Vehicle----")
vehicle3.show_info()
vehicle3.run_autopilot()

car = SmartEV("Maruti","Baleno",2024,100,"60% charged","v121.10")

print("\n ---Smart EV's---")
car.show_info()
car.charge_battery()
car.run_autopilot()

# ---------------------------------------------------------------------------------------

# Sample Output

#  ----Vehicle----
# Company:Hyundai
# Model:Creta
# Year:2025

#  ----Electric Vehicle----
# Company:BMW
# Model:X5
# Year:2023
# Charging Status:40% charged

#  ----Autonomous Vehicle----
# Company:Tata
# Model:Nexon
# Year:2023
# Auto Pilot running on AI Version:v121.11

#  ---Smart EV's---
# Company:Maruti
# Model:Baleno
# Year:2024
# Charging Status:60% charged
# Auto Pilot running on AI Version:v121.10


