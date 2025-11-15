# adding Variable to object
# Define Car class
class Car:
    def __init__(self, engine, fuel_injector):
        # Initialize basic attributes of the car
        self.engine = engine
        self.fuel_injector = fuel_injector

    def accessories(self, ac, music, perfume):
        # Add comfort accessories to the car
        self.ac = ac
        self.music = music
        self.perfume = perfume

    def accessories1(self, air_bags, abs, fog_lights):
        # Add safety accessories to the car
        self.air_bags = air_bags
        self.abs = abs
        self.fog_lights = fog_lights


# Create Car object c1 with engine and fuel injector
c1 = Car("Tata", "UST")
# Add comfort accessories
c1.accessories("Ac", "Playlist", "Rose")
print("Car 1:")
# Print all attributes of c1 as a dictionary
print(c1.__dict__)

# Create Car object c2
c2 = Car("BMW", "Ferrori")
# Add comfort accessories
c2.accessories("6", "Yes", "Yes")
print("Car 2:")
# Print all attributes of c2
print(c2.__dict__)

# Create Car object c3
c3 = Car("swift", "Honda")
# Add comfort accessories
c3.accessories("Ac", "melody", "Lavendor")
# Add safety accessories
c3.accessories1("6", "Yes", "Yes")
print("Car 3:")
# Print all attributes of c3
print(c3.__dict__)

#output

# Car 1:
# {'engine': 'Tata', 'fuel_injector': 'UST', 'ac': 'Ac', 'music': 'Playlist', 'perfume': 'Rose'}
# Car 2:
# {'engine': 'BMW', 'fuel_injector': 'Ferrori', 'ac': '6', 'music': 'Yes', 'perfume': 'Yes'}    
# Car 3:
# {'engine': 'swift', 'fuel_injector': 'Honda', 'ac': 'Ac', 'music': 'melody', 'perfume': 'Lavendor', 'air_bags': 
# '6', 'abs': 'Yes', 'fog_lights': 'Yes'}