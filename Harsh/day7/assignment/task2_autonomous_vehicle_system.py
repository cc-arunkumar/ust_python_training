class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def show_info(self):
        print(f"Company name:{self.make}, Model:{self.model}, Year:{self.year}")
        
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status):
        Vehicle.__init__(self,make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status
        
    def display(self):
        super().show_info()
        print(f"Battery capacity:{self.battery_capacity}kW,Charged status:{self.charge_status}")

    def charge_battery(self):
        if self.charge_status == 100:
            print( "Battery fully charged!")
        else:
            print(f"Battery is {self.charge_status}% charged")

class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year, ai_version):
        Vehicle.__init__(self,make, model, year)
        self.ai_version = ai_version

    def run_autopilot(self):
        print( f"Autopilot engaged with AI version {self.ai_version}")

class SmartEV(ElectricVehicle, AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, ai_version, charge_status):
        ElectricVehicle.__init__(self, make, model, year, battery_capacity, charge_status)
        AutonomousVehicle.__init__(self, make, model, year, ai_version)

print("------------------------------------------")   
v1=Vehicle("Honda","Civic",2000)
v1.show_info()
print("------------------------------------------")
e1=ElectricVehicle("Porsche","911 Gt",2024,85,90)
e1.display()
e1.charge_battery()
print("------------------------------------------")
a1=AutonomousVehicle("Tesla","tesla model y",2022,"v2.0",)
a1.show_info()
a1.run_autopilot()
print("------------------------------------------")
smart_ev3 = SmartEV("BMW", "M5", 2020,100,"v2.8",100)
smart_ev3.display()
smart_ev3.charge_battery()
smart_ev3.run_autopilot()
print("------------------------------------------")

# ------------------------------------------
# Company name:Honda, Model:Civic, Year:2000        
# ------------------------------------------        
# Company name:Porsche, Model:911 Gt, Year:2024     
# Battery capacity:85kW,Charged status:90
# Battery is 90% charged
# ------------------------------------------        
# Company name:Tesla, Model:tesla model y, Year:2022
# Autopilot engaged with AI version v2.0
# ------------------------------------------        
# Company name:BMW, Model:M5, Year:2020
# Battery capacity:100kW,Charged status:100
# Battery fully charged!
# Autopilot engaged with AI version v2.8
# ------------------------------------------