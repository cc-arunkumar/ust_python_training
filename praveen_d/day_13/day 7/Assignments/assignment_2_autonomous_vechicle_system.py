# Task 2 — Autonomous Vehicle System
# Domain: Automotive / AI
# Business Requirement:
# UST Mobility is building an AI vehicle platform.


# 1. Every Vehicle must have:
# make , model , year
# Method: show_info()
class Vechical:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def show_info(self):
        print(f"The Make of the vechical:{self.make}")
        print(f"The Model of the vechical:{self.model}")
        print(f"The Year made:{self.year}")

# 2. Every ElectricVehicle should have:
# battery_capacity , charge_status
# Method: charge_battery()
class E_V(Vechical):
    def __init__(self,make,model,year,battery_capacity,charge_status):
        Vechical.__init__(self,make,model,year)
        self.battery_capacity=battery_capacity
        self.charge_status=charge_status

    def charge_battery(self):
        print(f"Current charge:{self.charge_status}")
        if self.charge_status>80:
            print("Battery condition is good")
        elif self.charge_status>49:
            print("Try to charge soon")
        else:
            print("Charging required")

# 3. Every AutonomousVehicle should have:
# ai_version , run_autopilot()
class Auto_Vechical(Vechical):
    def __init__(self,make,model,year,ai_version):
        Vechical.__init__(self,make,model,year)
        self.ai_version=ai_version

    def run_autopilot(self):
        if self.ai_version=="Enabled":
            print(f"{self.make} {self.model} featers the auto pilot mode")
        else:
            print("There is no auto-pilot for this model")

# 4. The company wants to create a class SmartEV — a self-driving electric
# vehicle.

class Smart_Ev(E_V,Auto_Vechical):
    def __init__(self, make, model, year, battery_capacity, charge_status,ai_version):
        E_V.__init__(self,make,model,year,battery_capacity,charge_status)
        Auto_Vechical.__init__(self,make,model,year,ai_version)

    def check_car(self):
        if self.ai_version=="Enabled" and self.battery_capacity==True:
            print("The brand new EV_Autopilot car has been built")
        else:
            print("The car should have some required featers")

    def show_all_info(self):
        self.show_info()
        self.charge_battery()
        self.run_autopilot()




vechiel=Vechical("BMW","B710",2025)
vechiel.show_info()
print("------------------------------------------------------")
ev_vechile=E_V("Mercedes","9G7",2020,True,30)
ev_vechile.charge_battery()
print("------------------------------------------------------")
auto_vechical= Auto_Vechical("Rollsroys","ZR12",2019,"Enabled")
auto_vechical.run_autopilot()
print("------------------------------------------------------")
smart_ev= Smart_Ev("Volksvagen","YDW72",2025,True,90,"Enabled")
smart_ev.check_car()
smart_ev.show_all_info()


# Sample output:
# The Make of the vechical:BMW
# The Model of the vechical:B710
# The Year made:2025
# ------------------------------------------------------
# Current charge:30
# Charging required
# ------------------------------------------------------
# Rollsroys ZR12 featers the auto pilot mode
# ------------------------------------------------------
# The brand new EV_Autopilot car has been built
# The Make of the vechical:Volksvagen
# The Model of the vechical:YDW72
# The Year made:2025
# Current charge:90
# Battery condition is good
# Volksvagen YDW72 featers the auto pilot mode
# PS C:\UST python> 