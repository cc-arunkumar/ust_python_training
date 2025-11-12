# Task 2 — Autonomous Vehicle System
# Domain: Automotive / AI
# Business Requirement:
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
# Think about the correct inheritance structure to achieve this.

class vehical:
    def __init__(self,make , model , year):
        self.make=make
        self.model=model
        self.year=year
    def show_info(self):
        print(f"vehical making: {self.make}, model: {self.model}, year: {self.year}")
        print("***************************************")

class ElectricVehicle(vehical):
    def __init__(self, make, model, year,battery_capacity , change_status):
        vehical.__init__(self,make, model, year)
        self.battery_capacity=battery_capacity
        self.change_status=change_status
    def change_batary(self):
        print(f"battery capacity: {self.battery_capacity}, charge status {self.change_status}")
        print("*************************************")

class  AutonomousVehicle(vehical):
    def __init__(self, make, model, year,ai_version):
        vehical.__init__(self,make, model, year)
        self.ai_version=ai_version
    def  run_autopilot(self):
        print(f"vehical is running auto piolet : {self.ai_version}")
        print("*************************************")
class SmartEv(ElectricVehicle,AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, change_status,ai_version):
        ElectricVehicle.__init__(self,make, model, year, battery_capacity, change_status)
        AutonomousVehicle.__init__(self,make,model,year,ai_version)
    def get_details(self):
        print(f"vechical making: {self.make}")
        print(f"vechical model: {self.model}")
        print(f"vehical year: {self.year}")
        print(f"vehical battery_capacity: {self.battery_capacity}")
        print(f"vechical change_ststus: {self.change_status}")
        print(f"vechical version:{self.ai_version}")

vehical1=vehical('honda','UST',2025)
vehical2=ElectricVehicle("EY","nexon",2017,1500,"processing")
vehical3=AutonomousVehicle("BMW","newty",2025,"new_lanched")
vehical4=SmartEv("TATA","max",2014,20000,"finished","new")

vehical1.show_info()
vehical2.change_batary()
vehical3.run_autopilot()
vehical4.get_details()

# output
# vehical making: honda, model: UST, year: 2025
# ***************************************
# battery capacity: 1500, charge status processing
# *************************************
# vehical is running auto piolet : new_lanched
# *************************************
# vechical making: TATA
# vechical model: max
# vehical year: 2014
# vehical battery_capacity: 20000
# vechical change_ststus: finished
# vechical version:new
    



        