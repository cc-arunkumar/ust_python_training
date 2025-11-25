# Define a Car class
class Car:
    # Constructor to initialize engine and fuel injector
    def __init__(self, engine, fuel_injector):
        self.engine = engine              # Car engine type
        self.fuel_injector = fuel_injector  # Car fuel injector brand

    # Method to add accessories set 1
    def accessories1(self, AC, music, perfume):
        self.AC = AC            # AC brand
        self.music = music      # Music system brand
        self.perfume = perfume  # Perfume brand

    # Method to add accessories set 2
    def accessories2(self, airbag, abs, fog, light):
        self.airbag = airbag    # Airbag type
        self.abs = abs          # ABS type
        self.fog = fog          # Fog light type
        self.light = light      # Headlight type


# Create first Car object with engine and fuel injector
c1 = Car("Tata", "UST")

# Print separator line
print("***********************************")

# Print dictionary representation of c1 (only engine and fuel_injector so far)
print(c1.__dict__)

# Create second Car object
c2 = Car("BMW", "XYZ")

# Add accessories1 to c2
c2.accessories1("Samsung", "Sony", "Wonders")

# Print separator line
print("***********************************")

# Print dictionary representation of c2 (engine, fuel_injector, AC, music, perfume)
print(c2.__dict__)

# Add accessories2 to c1
c1.accessories2("abc", "xyz", "xbc", "sd")

# Print separator line
print("***********************************")

# Print dictionary representation of c1 (engine, fuel_injector, airbag, abs, fog, light)
print(c1.__dict__)

# Add accessories1 and accessories2 again to c1 (overwriting previous values)
c1.accessories1("sams", "boat", "wg")
c1.accessories2("xvc", "df", "jksj", "hvel")

# Print separator line
print("***********************************")

# Print updated dictionary representation of c1 (all attributes updated)
print(c1.__dict__)


# -------------------------------
# Expected Output
# -------------------------------
# ***********************************
# {'engine': 'Tata', 'fuel_injector': 'UST'}
# ***********************************
# {'engine': 'BMW', 'fuel_injector': 'XYZ', 'AC': 'Samsung', 'music': 'Sony', 'perfume': 'Wonders'}
# ***********************************
# {'engine': 'Tata', 'fuel_injector': 'UST', 'airbag': 'abc', 'abs': 'xyz', 'fog': 'xbc', 'light': 'sd'}
# ***********************************
# {'engine': 'Tata', 'fuel_injector': 'UST', 'airbag': 'xvc', 'abs': 'df', 'fog': 'jksj', 'light': 'hvel', 'AC': 'sams', 'music': 'boat', 'perfume': 'wg'}