# Task 2 — Autonomous Vehicle System
# Domain: Automotive / AI
# Demonstrates hybrid inheritance where SmartEV inherits from ElectricVehicle and AutonomousVehicle.

# Base class for general vehicles
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Display basic vehicle information
    def show_info(self):
        print(f"Vehicle Make: {self.make}")
        print(f"Vehicle Model: {self.model}")
        print(f"Vehicle Year: {self.year}")


# Derived class for electric vehicles
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status):
        Vehicle.__init__(self, make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_status = charge_status

    # Simulate charging battery
    def charge_battery(self):
        print(f"\nCharging {self.make} {self.model}...")
        self.charge_status = "Fully Charged"
        print(f"Battery Capacity: {self.battery_capacity} kWh")
        print(f"Charge Status: {self.charge_status}")


# Derived class for autonomous vehicles
class AutonomousVehicle(Vehicle):
    def __init__(self, make, model, year, ai_version):
        Vehicle.__init__(self, make, model, year)
        self.ai_version = ai_version

    # Simulate autopilot operation
    def run_autopilot(self):
        print(f"\n{self.make} {self.model} is now driving autonomously using AI version {self.ai_version}")
        print("Autopilot engaged. Monitoring surroundings.")


# Multiple inheritance class combining both electric and autonomous features
class SmartEV(ElectricVehicle, AutonomousVehicle):
    def __init__(self, make, model, year, battery_capacity, charge_status, ai_version):
        ElectricVehicle.__init__(self, make, model, year, battery_capacity, charge_status)
        AutonomousVehicle.__init__(self, make, model, year, ai_version)

    # Display full SmartEV details
    def show_info(self):
        print("\n--- SmartEV Information ---")
        Vehicle.show_info(self)
        print(f"Battery Capacity: {self.battery_capacity} kWh")
        print(f"Charge Status: {self.charge_status}")
        print(f"AI Version: {self.ai_version}")

    # Activate smart autonomous mode
    def start_smart_mode(self):
        print(f"\nActivating Smart Mode for {self.make} {self.model}...")
        self.run_autopilot()
        print("SmartEV is in full autonomous electric mode")


# Object creation and demonstration
if __name__ == "__main__":
    # Create vehicle objects
    vehicle1 = Vehicle("Toyota", "Corolla", 2020)
    ev1 = ElectricVehicle("Tesla", "Model 3", 2023, 75, "80% Charged")
    av1 = AutonomousVehicle("BMW", "i7", 2024, "AI v5.2")
    smart_ev1 = SmartEV("Tesla", "Model X", 2025, 100, "90% Charged", "AI v6.1")

    # Display and test each vehicle type
    print("\n--- Vehicle ---")
    vehicle1.show_info()

    print("\n--- Electric Vehicle ---")
    ev1.show_info()
    ev1.charge_battery()

    print("\n--- Autonomous Vehicle ---")
    av1.show_info()
    av1.run_autopilot()

    print("\n--- SmartEV ---")
    smart_ev1.show_info()
    smart_ev1.start_smart_mode()


# Sample Output:
# --- Vehicle ---
# Vehicle Make: Toyota
# Vehicle Model: Corolla
# Vehicle Year: 2020

# --- Electric Vehicle ---
# Vehicle Make: Tesla
# Vehicle Model: Model 3
# Vehicle Year: 2023

# Charging Tesla Model 3...
# Battery Capacity: 75 kWh
# Charge Status: Fully Charged

# --- Autonomous Vehicle ---
# Vehicle Make: BMW
# Vehicle Model: i7
# Vehicle Year: 2024

# BMW i7 is now driving autonomously using AI version AI v5.2
# Autopilot engaged. Monitoring surroundings.

# --- SmartEV ---
# --- SmartEV Information ---
# Vehicle Make: Tesla
# Vehicle Model: Model X
# Vehicle Year: 2025
# Battery Capacity: 100 kWh
# Charge Status: 90% Charged
# AI Version: AI v6.1

# Activating Smart Mode for Tesla Model X...
# Tesla Model X is now driving autonomously using AI version AI v6.1
# Autopilot engaged. Monitoring surroundings.
# SmartEV is in full autonomous electric mode
