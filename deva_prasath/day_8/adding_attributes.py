# Define a Cars class
class Cars:
    # Constructor to initialize engine and fuel injector attributes
    def __init__(self, engine, fuel_injector):
        self.engine = engine
        self.fuel_injector = fuel_injector
    
    # Method to set accessories for the car
    def accessories(self, AC, Purifier, TPMS):
        self.AC = AC
        self.Purifier = Purifier
        self.TPMS = TPMS
    
    # Method to set important accessories for the car
    def imp_accessories(self, airbag, ADAS, foglight):
        self.airbag = airbag
        self.ADAS = ADAS
        self.foglight = foglight
    

# Create an instance of Cars for the first car
c1 = Cars("Nissan", "npme")
# Set accessories for this car
c1.accessories("Blue star", "Xioami", "4 tyre Nissan TPMS")
# Print the car's attributes
print(c1.__dict__)  # __dict__ shows all the instance attributes
print("----------------------------------------------------------------------")

# Create another instance of Cars for the second car
c2 = Cars("Volkswagen", "vpme")
# Set important accessories for this car
c2.imp_accessories("Level-5", "Level-2", "White Foglights")
# Print the car's attributes
print(c2.__dict__)
print("----------------------------------------------------------------------")

# Create another instance of Cars for the third car
c3 = Cars("Benz", "bpme")
# Print the car's attributes (only engine and fuel injector will be displayed as accessories are not set)
print(c3.__dict__)
