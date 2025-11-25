#Creating a Vehicle class adding the attributes to it.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def show_info(self):
        print(f"Vehicle Make: {self.make}")
        print(f"Vehicle Model: {self.model}")
        print(f"Vehicle Year: {self.year}")

#Inheriting the class Vehicle to Electric_Vehicle
class Electric_Vehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity, charger_status):
        Vehicle.__init__(self, make, model, year)
        self.battery_capacity = battery_capacity
        self.charger_status = charger_status

    def show_battery_info(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh and Charger Status: {self.charger_status}")

#Inheriting Electric_Vehicle to AutonomusVehicle class.
class AutonomusVehicle(Electric_Vehicle):
    def __init__(self, make, model, year,battery_capacity, charger_status, ai_version):
        Electric_Vehicle.__init__(self, make, model, year, battery_capacity, charger_status)
        self.ai_version = ai_version

    def show_ai_version(self):
        print(f"The AI Version of the Vehicle is: {self.ai_version}")

    def run_autopilot(self):
        print("Autopilot is now engaged. The vehicle is driving itself.")

#Inheriting the final class SmartEV from AutonomusVehicle.
class  SmartEV(AutonomusVehicle):
    def __init__(self, make, model, year, battery_capacity, charger_status, ai_version):
        AutonomusVehicle.__init__(self, make, model, year, battery_capacity, charger_status, ai_version)
    
    def is_veicle_smart(self):
        print("This vehicle is a Smart Electric Vehicle with Autonomous capabilities.")

a1 = AutonomusVehicle('Tesla', 'Model X', '2022','3390', 'Fully-Charged','2.0')
a1.show_info()
a1.show_ai_version()
a1.run_autopilot()

print("------------------------------------------------------------------------")
s1 = SmartEV('Tesla', 'Model S', '2023', 100, 'Fully Charged', '5.0')
s1.show_info()
s1.is_veicle_smart()

print("------------------------------------------------------------------------")
e1 = Electric_Vehicle('Nissan', 'Leaf', '2023', 40, 'Charging')
e1.show_info()
e1.show_battery_info()



#Console Output:
# Vehicle Make: Tesla
# Vehicle Model: Model X
# Vehicle Year: 2022
# The AI Version of the Vehicle is: 2.0
# Autopilot is now engaged. The vehicle is driving itself.
# ------------------------------------------------------------------------
# Vehicle Make: Tesla
# Vehicle Model: Model S
# Vehicle Year: 2023
# This vehicle is a Smart Electric Vehicle with Autonomous capabilities.
# ------------------------------------------------------------------------
# Vehicle Make: Nissan
# Vehicle Model: Leaf
# Vehicle Year: 2023
# Battery Capacity: 40 kWh and Charger Status: Charging